"""Hand-drawn blackboard scene graph.

Times are seconds from the start of the narration. Drawing is a pure
function of time, so any frame can be rendered on its own.
"""

from __future__ import annotations

import math
import random
import re
from copy import deepcopy
from dataclasses import dataclass, field

import cairo

W, H = 1920, 1080
FPS = 30

# Thumbnail slot: 22% of width by 24% of height, top-right.
T_W = 0.22 * W
T_H = 0.24 * H
T_X = W - T_W - 16
T_Y = 14
T_RECT = (T_X, T_Y, T_W, T_H)


def _rgb(hex_color: str) -> tuple[float, float, float]:
    h = hex_color.lstrip("#")
    return tuple(int(h[i : i + 2], 16) / 255 for i in (0, 2, 4))


CHALK = _rgb("F2F2F2")
CORAL = _rgb("FF6B5B")
CYAN = _rgb("4FC3F7")
AMBER = _rgb("FFB74D")
GRAY = _rgb("8A9099")
BOARD = _rgb("111418")

ROW_RE = re.compile(
    r"^\|\s*(\d+\.\d+)\s*\|[^|]*\|\s*([0-9]+(?:\.[0-9]+)?)\s*\|"
)

ARROWS = {
    "→": "right",
    "←": "left",
    "↑": "up",
    "↓": "down",
    "⇔": "both",
}


def ease(p: float) -> float:
    p = 0.0 if p < 0 else 1.0 if p > 1 else p
    return p * p * (3 - 2 * p)


def seed_for(text: str) -> int:
    h = 2166136261
    for ch in text:
        h ^= ord(ch)
        h = (h * 16777619) & 0xFFFFFFFF
    return h


def load_storyboard_times(path: str) -> dict[str, float]:
    rows: dict[str, float] = {}
    with open(path, encoding="utf-8") as handle:
        for line in handle:
            match = ROW_RE.match(line)
            if match:
                rows[match.group(1)] = float(match.group(2))
    return rows


def _dist(a, b) -> float:
    return math.hypot(b[0] - a[0], b[1] - a[1])


def subpath(pts: list[tuple[float, float]], frac: float) -> list[tuple[float, float]]:
    if not pts:
        return []
    if frac >= 0.999 or len(pts) == 1:
        return list(pts)
    if frac <= 0:
        return [pts[0]]
    lengths = [_dist(pts[i], pts[i + 1]) for i in range(len(pts) - 1)]
    total = sum(lengths) or 1.0
    target = total * frac
    out = [pts[0]]
    acc = 0.0
    for i, length in enumerate(lengths):
        if acc + length >= target - 1e-6:
            u = 0.0 if length < 1e-6 else (target - acc) / length
            out.append(
                (
                    pts[i][0] + (pts[i + 1][0] - pts[i][0]) * u,
                    pts[i][1] + (pts[i + 1][1] - pts[i][1]) * u,
                )
            )
            return out
        acc += length
        out.append(pts[i + 1])
    return out


def wobble(pts: list[tuple[float, float]], seed: int, amp: float = 1.7) -> list[tuple[float, float]]:
    rng = random.Random(seed)
    if len(pts) < 3:
        return list(pts)
    out = []
    last = len(pts) - 1
    for i, (x, y) in enumerate(pts):
        if i == 0 or i == last:
            out.append((x, y))
        else:
            out.append((x + rng.uniform(-amp, amp), y + rng.uniform(-amp, amp)))
    return out


def subdivide(p0, p1, n: int) -> list[tuple[float, float]]:
    return [
        (p0[0] + (p1[0] - p0[0]) * i / n, p0[1] + (p1[1] - p0[1]) * i / n)
        for i in range(n)
    ]


def rect_points(x, y, w, h, n: int = 5) -> list[tuple[float, float]]:
    pts: list[tuple[float, float]] = []
    corners = [(x, y), (x + w, y), (x + w, y + h), (x, y + h), (x, y)]
    for a, b in zip(corners, corners[1:]):
        pts.extend(subdivide(a, b, n))
    pts.append((x, y))
    return pts


def line_points(x1, y1, x2, y2, n: int = 8) -> list[tuple[float, float]]:
    pts = subdivide((x1, y1), (x2, y2), n)
    pts.append((x2, y2))
    return pts


def brace_points(x, y1, y2, width: float = 16) -> list[tuple[float, float]]:
    if y2 < y1:
        y1, y2 = y2, y1
    mid = (y1 + y2) / 2
    return [
        (x + width, y1),
        (x + width * 0.45, y1 + min(18, (y2 - y1) * 0.08)),
        (x + 2, mid - min(22, (y2 - y1) * 0.12)),
        (x - width * 0.55, mid),
        (x + 2, mid + min(22, (y2 - y1) * 0.12)),
        (x + width * 0.45, y2 - min(18, (y2 - y1) * 0.08)),
        (x + width, y2),
    ]


@dataclass
class Elem:
    id: str
    row: str
    kind: str
    t0: float
    dur: float
    color: tuple[float, float, float]
    text: str = ""
    size: float = 28
    x: float = 0
    y: float = 0
    w: float = 0
    h: float = 0
    x2: float = 0
    y2: float = 0
    points: list | None = None
    zone: str = "main"
    group: str = "root"
    regroup: tuple | None = None
    lw: float = 3.2
    style: str = "solid"
    fill: bool = False
    grow: str = "perimeter"
    ax: str = "left"
    ay: str = "top"
    max_w: float = 520
    base_opacity: float = 1.0
    arrow: bool = False
    rotation: float = 0.0
    a0: float = 0.0
    a1: float = 0.0
    target: str | None = None
    phrase: str | None = None
    text_segs: list = field(default_factory=list)
    opacity_keys: list = field(default_factory=list)
    fill_keys: list = field(default_factory=list)
    ghost_keys: list = field(default_factory=list)
    ghost_color: tuple | None = None
    versions: list = field(default_factory=list)
    highlight_spans: list = field(default_factory=list)
    slide: tuple | None = None
    erase: tuple | None = None
    cache: dict = field(default_factory=dict)


@dataclass
class Xform:
    t: float
    dur: float
    bbox: tuple
    dest: tuple


class Board:
    def __init__(self, duration: float):
        self.duration = duration
        self.elems: list[Elem] = []
        self.by_id: dict[str, Elem] = {}
        self.rows: dict[str, float] = {}
        self.groups: dict[str, Xform] = {}
        self.cur_row = ""
        self.cur_t = 0.0
        self.fade: tuple[float, float] | None = None
        self.t_occupied: list[tuple[float, float]] = []
        self._bg: cairo.ImageSurface | None = None
        self._measure = cairo.Context(
            cairo.ImageSurface(cairo.FORMAT_ARGB32, 8, 8)
        )
        self._glyph_ok: dict[str, bool] = {}
        self.debug_boxes = False

    # --- authoring -----------------------------------------------------

    def at(self, row: str, t: float) -> "Board":
        if row in self.rows:
            raise ValueError(f"duplicate row {row}")
        self.rows[row] = t
        self.cur_row = row
        self.cur_t = t
        return self

    def _add(self, elem: Elem) -> Elem:
        if elem.id in self.by_id:
            raise ValueError(f"duplicate id {elem.id}")
        self.elems.append(elem)
        self.by_id[elem.id] = elem
        return elem

    def text(
        self,
        id,
        text,
        x,
        y,
        *,
        color=CHALK,
        size=28,
        max_w=640,
        zone="main",
        ax="left",
        ay="top",
        opacity=1.0,
        style="solid",
    ):
        dur = max(0.12, len(text) / 14.0)
        elem = Elem(
            id=id,
            row=self.cur_row,
            kind="text",
            t0=self.cur_t,
            dur=dur,
            color=color,
            text=text,
            size=size,
            x=x,
            y=y,
            zone=zone,
            ax=ax,
            ay=ay,
            max_w=max_w,
            base_opacity=opacity,
            style=style,
            text_segs=[(self.cur_t, text, dur)],
        )
        return self._add(elem)

    def rect(
        self,
        id,
        x,
        y,
        w,
        h,
        *,
        color=CHALK,
        lw=3.2,
        zone="main",
        style="solid",
        fill=False,
        grow="perimeter",
    ):
        return self._add(
            Elem(
                id=id,
                row=self.cur_row,
                kind="rect",
                t0=self.cur_t,
                dur=0.6,
                color=color,
                x=x,
                y=y,
                w=w,
                h=h,
                lw=lw,
                zone=zone,
                style=style,
                fill=fill,
                grow=grow,
            )
        )

    def box(
        self,
        id,
        x,
        y,
        w,
        h,
        text,
        *,
        color=CHALK,
        size=26,
        zone="main",
        style="solid",
        tcolor=None,
        ax="center",
        ay="middle",
    ):
        self.rect(id, x, y, w, h, color=color, zone=zone, style=style)
        self.text(
            id + ".t",
            text,
            x + w / 2 if ax == "center" else x + 14,
            y + h / 2 if ay == "middle" else y + 10,
            color=tcolor or color,
            size=size,
            max_w=w - 22,
            zone=zone,
            ax=ax,
            ay=ay,
        )
        return self.by_id[id]

    def bar(self, id, x, y, w, h, *, color=CORAL, zone="main", style="solid", lw=3.0):
        elem = self._add(
            Elem(
                id=id,
                row=self.cur_row,
                kind="bar",
                t0=self.cur_t,
                dur=0.6,
                color=color,
                x=x,
                y=y,
                w=w,
                h=h,
                lw=lw,
                zone=zone,
                style=style,
                fill=style == "solid",
                fill_keys=[(self.cur_t, 1.0, 0.6)],
            )
        )
        return elem

    def line(
        self,
        id,
        x1,
        y1,
        x2,
        y2,
        *,
        color=CHALK,
        lw=3.2,
        zone="main",
        style="solid",
        arrow=False,
        dur=None,
    ):
        kind_dur = 0.4 if dur is None and not arrow else (dur or 0.6)
        return self._add(
            Elem(
                id=id,
                row=self.cur_row,
                kind="line",
                t0=self.cur_t,
                dur=kind_dur,
                color=color,
                x=x1,
                y=y1,
                x2=x2,
                y2=y2,
                lw=lw,
                zone=zone,
                style=style,
                arrow=arrow,
            )
        )

    def arrow(self, id, x1, y1, x2, y2, text=None, *, color=CHALK, size=24, zone="main", style="solid", tdx=0, tdy=-8, max_w=280, lw=3.2):
        self.line(id, x1, y1, x2, y2, color=color, zone=zone, style=style, arrow=True, lw=lw)
        if text:
            mx = (x1 + x2) / 2 + tdx
            my = (y1 + y2) / 2 + tdy
            self.text(
                id + ".t",
                text,
                mx,
                my,
                color=color,
                size=size,
                max_w=max_w,
                zone=zone,
                ax="center",
                ay="middle",
            )
        return self.by_id[id]

    def poly(self, id, points, *, color=CHALK, lw=3.2, zone="main", style="solid", arrow=False):
        return self._add(
            Elem(
                id=id,
                row=self.cur_row,
                kind="poly",
                t0=self.cur_t,
                dur=0.6,
                color=color,
                points=[tuple(p) for p in points],
                lw=lw,
                zone=zone,
                style=style,
                arrow=arrow,
            )
        )

    def circle(self, id, x, y, r, *, color=CHALK, zone="main", style="solid", fill=False, lw=3.0):
        return self._add(
            Elem(
                id=id,
                row=self.cur_row,
                kind="circle",
                t0=self.cur_t,
                dur=0.45,
                color=color,
                x=x,
                y=y,
                w=r,
                lw=lw,
                zone=zone,
                style=style,
                fill=fill,
            )
        )

    def dot(self, id, x, y, *, color=CHALK, r=6.0, zone="main"):
        return self._add(
            Elem(
                id=id,
                row=self.cur_row,
                kind="dot",
                t0=self.cur_t,
                dur=0.18,
                color=color,
                x=x,
                y=y,
                w=r,
                zone=zone,
                fill=True,
            )
        )

    def brace(self, id, x, y1, y2, *, color=CHALK, zone="main", width=16):
        return self._add(
            Elem(
                id=id,
                row=self.cur_row,
                kind="poly",
                t0=self.cur_t,
                dur=0.4,
                color=color,
                points=brace_points(x, y1, y2, width),
                lw=3.0,
                zone=zone,
                x=x,
                y=min(y1, y2),
                w=width,
                h=abs(y2 - y1),
            )
        )

    def stamp(self, id, text, x, y, *, color=CHALK, size=26, zone="main", style="dashed", rot=-4.0, max_w=420):
        return self._add(
            Elem(
                id=id,
                row=self.cur_row,
                kind="stamp",
                t0=self.cur_t,
                dur=0.5,
                color=color,
                text=text,
                size=size,
                x=x,
                y=y,
                zone=zone,
                style=style,
                rotation=rot,
            max_w=max_w,
            ax="center",
            ay="middle",
            text_segs=[(self.cur_t, text, 0.5)],
        )
        )

    def arc(self, id, cx, cy, r, a0, a1, *, color=CHALK, zone="main", lw=3.2):
        return self._add(
            Elem(
                id=id,
                row=self.cur_row,
                kind="arc",
                t0=self.cur_t,
                dur=0.5,
                color=color,
                x=cx,
                y=cy,
                w=r,
                a0=a0,
                a1=a1,
                lw=lw,
                zone=zone,
            )
        )

    def link(self, id, x1, y1, target, *, color=CHALK, zone="main"):
        return self._add(
            Elem(
                id=id,
                row=self.cur_row,
                kind="link",
                t0=self.cur_t,
                dur=0.6,
                color=color,
                x=x1,
                y=y1,
                target=target,
                zone=zone,
                arrow=True,
            )
        )

    def append(self, id, extra):
        elem = self.by_id[id]
        prev = elem.text_segs[-1][1] if elem.text_segs else elem.text
        full = prev + extra
        dur = max(0.12, len(extra) / 14.0)
        elem.text_segs.append((self.cur_t, full, dur))
        elem.text = full

    def set_fill(self, id, frac, ghost=None, ghost_color=None):
        elem = self.by_id[id]
        elem.fill_keys.append((self.cur_t, frac, 0.35))
        if ghost is not None:
            elem.ghost_keys.append((self.cur_t, ghost, 0.35))
        if ghost_color is not None:
            elem.ghost_color = ghost_color

    def redraw_poly(self, id, points):
        elem = self.by_id[id]
        elem.versions.append((self.cur_t, [tuple(p) for p in points], 0.55))

    def slide(self, id, x, y, color=None):
        elem = self.by_id[id]
        elem.slide = (self.cur_t, x, y, 0.6, color)

    def dup(self, src, new_id, text=None):
        src_elem = self.by_id[src]
        elem = deepcopy(src_elem)
        elem.id = new_id
        elem.row = self.cur_row
        elem.t0 = self.cur_t
        elem.group = "root"
        elem.regroup = None
        elem.erase = None
        elem.slide = None
        elem.highlight_spans = []
        elem.opacity_keys = []
        elem.versions = []
        elem.cache = {}
        label = src_elem.text if text is None else text
        # A sliding copy is already written; it must not redraw.
        elem.text = label
        elem.text_segs = [(self.cur_t, label, 0.01)]
        elem.dur = 0.01
        elem.base_opacity = 1.0
        return self._add(elem)

    def _match(self, elem: Elem, t: float, zone=None, ids=None, group=None) -> bool:
        if elem.t0 > t + 1e-9:
            return False
        if zone is not None and elem.zone != zone:
            return False
        if ids is not None and elem.id not in ids:
            return False
        if group is not None and self.group_at(elem, t) != group:
            return False
        return True

    def erase(self, *, zone=None, ids=None, group=None):
        t = self.cur_t
        for elem in self.elems:
            if not self._match(elem, t, zone, ids, group):
                continue
            if self.group_at(elem, t) != "root" and group is None and zone is not None:
                # Thumbnail elements keep their original zone string but must
                # survive a later erase of that zone on the main board.
                if elem.regroup and elem.regroup[0] < t:
                    continue
            if elem.erase and elem.erase[0] <= t:
                continue
            elem.erase = (t, 0.3)

    def erase_all(self, thumbs: bool = True):
        t = self.cur_t
        for elem in self.elems:
            if elem.t0 > t:
                continue
            if elem.erase and elem.erase[0] <= t:
                continue
            if not thumbs and elem.regroup and elem.regroup[0] <= t:
                continue
            elem.erase = (t, 0.3)

    def dim(self, *, zone=None, ids=None, level=0.4):
        t = self.cur_t
        for elem in self.elems:
            if not self._match(elem, t, zone, ids, None):
                continue
            if elem.regroup and elem.regroup[0] <= t:
                continue
            if elem.erase and elem.erase[0] <= t:
                continue
            elem.opacity_keys.append((t, level, 0.25))

    def undim(self, id):
        self.by_id[id].opacity_keys.append((self.cur_t, 1.0, 0.25))

    def highlight(self, id, until=None):
        self.by_id[id].highlight_spans.append((self.cur_t, until))

    def shrink_to_t(self, group: str, keep_zones: set[str] | None = None, dest=None):
        t = self.cur_t
        kept: list[Elem] = []
        for elem in self.elems:
            if elem.t0 >= t - 1e-9:
                continue
            if elem.erase and elem.erase[0] <= t:
                continue
            if elem.regroup and elem.regroup[0] <= t:
                continue
            if keep_zones is not None and elem.zone not in keep_zones:
                continue
            elem.regroup = (t, group)
            kept.append(elem)
        if not kept:
            raise RuntimeError(f"shrink {group} kept nothing at {t}")
        bbox = self._union(self.local_rect(e, t) for e in kept)
        # Pad so a stroke on the bbox edge is inside the map.
        bbox = (bbox[0] - 8, bbox[1] - 8, bbox[2] + 16, bbox[3] + 16)
        self.groups[group] = Xform(t, 0.8, bbox, dest or T_RECT)
        for elem in self.elems:
            if elem in kept:
                continue
            if elem.t0 >= t:
                continue
            if elem.erase and elem.erase[0] <= t:
                continue
            if elem.regroup and elem.regroup[0] <= t:
                continue
            elem.erase = (t, 0.3)

    def restore(self, source_group: str, dest, new_group: str, emphasise=()):
        t = self.cur_t
        source = self.groups[source_group]
        clones = []
        for elem in list(self.elems):
            if self.group_at(elem, t) != source_group:
                continue
            if elem.erase and elem.erase[0] <= t:
                continue
            clone = deepcopy(elem)
            clone.id = f"{elem.id}@{new_group}"
            clone.row = self.cur_row
            clone.t0 = t
            clone.dur = 0.6
            clone.group = new_group
            clone.regroup = None
            clone.erase = None
            clone.slide = None
            clone.highlight_spans = []
            clone.opacity_keys = []
            clone.versions = []
            clone.cache = {}
            clone.zone = new_group
            final = elem.text_segs[-1][1] if elem.text_segs else elem.text
            clone.text = final
            clone.text_segs = [(t, final, 0.55)] if final else []
            if elem.kind == "bar":
                # Show the settled fill immediately as the copy is drawn.
                settled = self._keyed(elem.fill_keys, t, default=1.0)
                clone.fill_keys = [(t, settled, 0.45)]
                clone.ghost_keys = []
            clones.append(clone)
        if not clones:
            raise RuntimeError(f"restore found nothing in {source_group}")
        for clone in clones:
            self._add(clone)
        self.groups[new_group] = Xform(t, 0.0, source.bbox, dest)
        for eid in emphasise:
            target = f"{eid}@{new_group}"
            if target in self.by_id:
                self.by_id[target].highlight_spans.append((t, None))

    def fade_out(self, t0: float, t1: float):
        self.fade = (t0, t1)

    # --- time-varying state --------------------------------------------

    def group_at(self, elem: Elem, t: float) -> str:
        if elem.regroup and t >= elem.regroup[0] - 1e-9:
            return elem.regroup[1]
        return elem.group

    def anchor_pos(self, elem: Elem, t: float) -> tuple[float, float]:
        x, y = elem.x, elem.y
        if elem.slide and t >= elem.slide[0]:
            t0, x1, y1, dur, _color = elem.slide
            p = 1.0 if dur <= 0 else min(1.0, (t - t0) / dur)
            p = ease(p)
            x = elem.x + (x1 - elem.x) * p
            y = elem.y + (y1 - elem.y) * p
        return x, y

    def color_at(self, elem: Elem, t: float):
        if elem.slide and elem.slide[4] is not None and t >= elem.slide[0]:
            t0, _x, _y, dur, color = elem.slide
            if t >= t0 + dur * 0.82:
                return color
        return elem.color

    def opacity_at(self, elem: Elem, t: float) -> float:
        current = elem.base_opacity
        for t0, val, dur in elem.opacity_keys:
            if t < t0:
                break
            p = 1.0 if dur <= 0 else min(1.0, (t - t0) / dur)
            if p >= 1:
                current = val
            else:
                current = current + (val - current) * ease(p)
                break
        return current

    def erase_p(self, elem: Elem, t: float) -> float:
        if not elem.erase or t < elem.erase[0]:
            return 0.0
        return min(1.0, (t - elem.erase[0]) / elem.erase[1])

    def visible(self, elem: Elem, t: float) -> bool:
        if t < elem.t0 - 1e-6:
            return False
        if elem.erase and t >= elem.erase[0] + elem.erase[1] - 1e-6:
            return False
        return True

    def reveal(self, elem: Elem, t: float) -> float:
        if t <= elem.t0:
            return 0.0
        dur = elem.dur or 0.01
        return max(0.0, min(1.0, (t - elem.t0) / dur))

    def _keyed(self, keys, t, default=0.0) -> float:
        current = default
        for t0, val, dur in keys:
            if t < t0:
                break
            p = 1.0 if dur <= 0 else min(1.0, (t - t0) / dur)
            if p >= 1:
                current = val
            else:
                current = current + (val - current) * ease(p)
                break
        return current

    def text_shown(self, elem: Elem, t: float, full: bool = False) -> str:
        if not elem.text_segs:
            return ""
        shown = ""
        for t0, complete, dur in elem.text_segs:
            if t < t0:
                break
            if full or dur <= 0 or t >= t0 + dur:
                shown = complete
            else:
                prev = len(shown)
                extra = len(complete) - prev
                n = prev + max(1, int(math.ceil(extra * (t - t0) / dur)))
                return complete[: min(len(complete), n)]
        return shown

    def xform_params(self, group: str, t: float) -> tuple[float, float, float]:
        xf = self.groups.get(group)
        if xf is None or t < xf.t:
            return 1.0, 0.0, 0.0
        if xf.dur <= 0:
            p = 1.0
        else:
            p = ease(min(1.0, (t - xf.t) / xf.dur))
        bx, by, bw, bh = xf.bbox
        dx, dy, dw, dh = xf.dest
        bw = max(bw, 1.0)
        bh = max(bh, 1.0)
        s_final = min(dw / bw, dh / bh) * 0.92
        cx0 = bx + bw / 2
        cy0 = by + bh / 2
        cx1 = dx + dw / 2
        cy1 = dy + dh / 2
        s = 1 + (s_final - 1) * p
        cx = cx0 + (cx1 - cx0) * p
        cy = cy0 + (cy1 - cy0) * p
        return s, cx - cx0 * s, cy - cy0 * s

    # --- text measure --------------------------------------------------

    def _font(self, cr, size, fallback=False):
        cr.select_font_face(
            "DejaVu Sans" if fallback else "Patrick Hand",
            cairo.FONT_SLANT_NORMAL,
            cairo.FONT_WEIGHT_NORMAL,
        )
        cr.set_font_size(size)

    def _hand_ok(self, ch: str) -> bool:
        if ch in self._glyph_ok:
            return self._glyph_ok[ch]
        if ch in ARROWS or ch == "\n":
            ok = False
        else:
            self._font(self._measure, 80, False)
            ok = self._measure.text_extents(ch).width > 0.4 or ch == " "
        self._glyph_ok[ch] = ok
        return ok

    def _pieces(self, text: str) -> list[tuple[str, str]]:
        pieces: list[tuple[str, str]] = []
        buf = []
        mode = None

        def flush():
            nonlocal buf, mode
            if buf and mode:
                pieces.append((mode, "".join(buf)))
            buf = []

        for ch in text:
            if ch in ARROWS:
                flush()
                pieces.append(("arrow", ARROWS[ch]))
                mode = None
                continue
            want = "hand" if self._hand_ok(ch) else "fallback"
            if mode != want:
                flush()
                mode = want
            buf.append(ch)
        flush()
        return pieces

    def _piece_width(self, kind: str, data: str, size: float) -> float:
        if kind == "arrow":
            return size * 0.78
        self._font(self._measure, size, kind == "fallback")
        return self._measure.text_extents(data).x_advance

    def layout_text(self, text: str, size: float, max_w: float) -> list[list[tuple[str, str]]]:
        # Wrap on spaces, keeping arrows attached to the surrounding tokens.
        words = text.split(" ")
        lines: list[list[tuple[str, str]]] = []
        cur: list[tuple[str, str]] = []
        cur_w = 0.0
        space_w = self._piece_width("hand", " ", size)

        def width_of(pieces):
            return sum(self._piece_width(k, d, size) for k, d in pieces)

        for index, word in enumerate(words):
            parts = self._pieces(word)
            ww = width_of(parts)
            extra = (space_w if cur else 0.0) + ww
            if cur and cur_w + extra > max_w and word:
                lines.append(cur)
                cur = []
                cur_w = 0.0
                extra = ww
            if cur:
                cur.append(("hand", " "))
                cur_w += space_w
            cur.extend(parts)
            cur_w += ww
        if cur:
            lines.append(cur)
        return lines or [[]]

    def text_block_size(self, text: str, size: float, max_w: float) -> tuple[float, float, float]:
        self._font(self._measure, size, False)
        _ascent, _descent, height, _a, _b = self._measure.font_extents()
        line_h = height * 1.02
        lines = self.layout_text(text, size, max_w)
        widths = []
        for line in lines:
            widths.append(sum(self._piece_width(k, d, size) for k, d in line))
        return max(widths or [0]), line_h * max(1, len(lines)), line_h

    def local_rect(self, elem: Elem, t: float) -> tuple[float, float, float, float]:
        if elem.kind == "text":
            label = self.text_shown(elem, t, full=True) or elem.text
            tw, th, _lh = self.text_block_size(label, elem.size, elem.max_w)
            x, y = self.anchor_pos(elem, t)
            if elem.ax == "center":
                x -= tw / 2
            if elem.ay == "middle":
                y -= th / 2
            return (x, y, max(tw, 4), max(th, 4))
        if elem.kind == "stamp":
            tw, th, _lh = self.text_block_size(elem.text, elem.size, elem.max_w)
            pad = 14
            w, h = tw + pad * 2, th + pad * 2
            return (elem.x - w / 2, elem.y - h / 2, w, h)
        if elem.kind in ("rect", "bar"):
            return (elem.x, elem.y, elem.w, elem.h)
        if elem.kind == "line":
            x, y = self.anchor_pos(elem, t)
            dx, dy = x - elem.x, y - elem.y
            xs = [elem.x + dx, elem.x2 + dx]
            ys = [elem.y + dy, elem.y2 + dy]
            pad = 16
            return (min(xs) - pad, min(ys) - pad, abs(xs[1] - xs[0]) + pad * 2, abs(ys[1] - ys[0]) + pad * 2)
        if elem.kind == "poly":
            pts = elem.points or [(0, 0)]
            if elem.versions:
                for vt, new_pts, _dur in elem.versions:
                    if t >= vt:
                        pts = new_pts
            xs = [p[0] for p in pts]
            ys = [p[1] for p in pts]
            pad = 14
            return (min(xs) - pad, min(ys) - pad, max(xs) - min(xs) + pad * 2, max(ys) - min(ys) + pad * 2)
        if elem.kind == "circle":
            return (elem.x - elem.w, elem.y - elem.w, elem.w * 2, elem.w * 2)
        if elem.kind == "dot":
            return (elem.x - elem.w, elem.y - elem.w, elem.w * 2, elem.w * 2)
        if elem.kind == "arc":
            return (elem.x - elem.w, elem.y - elem.w, elem.w * 2, elem.w * 2)
        if elem.kind == "link":
            return (elem.x, elem.y, 8, 8)
        return (elem.x, elem.y, max(elem.w, 4), max(elem.h, 4))

    def screen_rect(self, elem: Elem, t: float) -> tuple[float, float, float, float]:
        if elem.kind == "link":
            rect = self.local_rect(elem, t)
            return rect
        x, y, w, h = self.local_rect(elem, t)
        # local_rect for text already includes slide via anchor_pos.
        # For rect/bar, slide is not used (they don't slide). For line, included.
        # Group transform is around original coordinates. Text local_rect is in
        # the same local space (slide already applied inside local_rect).
        s, ox, oy = self.xform_params(self.group_at(elem, t), t)
        if elem.kind == "text":
            # anchor_pos slide is in local_rect; do not slide twice.
            return (ox + x * s, oy + y * s, w * s, h * s)
        if elem.slide and elem.kind not in ("text",):
            ax, ay = self.anchor_pos(elem, t)
            # local_rect for line already applied slide. Others don't slide.
            pass
        return (ox + x * s, oy + y * s, w * s, h * s)

    def _union(self, rects) -> tuple[float, float, float, float]:
        rects = list(rects)
        x0 = min(r[0] for r in rects)
        y0 = min(r[1] for r in rects)
        x1 = max(r[0] + r[2] for r in rects)
        y1 = max(r[1] + r[3] for r in rects)
        return (x0, y0, x1 - x0, y1 - y0)

    # --- finalize / checks ---------------------------------------------

    def finalize(self, storyboard: dict[str, float]):
        missing = [row for row in storyboard if row not in self.rows]
        extra = [row for row in self.rows if row not in storyboard]
        mismatch = [
            (row, self.rows[row], storyboard[row])
            for row in storyboard
            if row in self.rows and abs(self.rows[row] - storyboard[row]) > 0.05
        ]
        if missing or extra or mismatch:
            raise SystemExit(
                f"storyboard rows missing={missing[:12]} extra={extra[:12]} mismatch={mismatch[:8]}"
            )
        times = sorted(set(storyboard.values()))

        def deadline(t: float) -> float:
            for rt in times:
                if rt > t + 0.03:
                    return rt - 0.02
            return t + 8

        for elem in self.elems:
            room = deadline(elem.t0) - elem.t0
            elem.dur = min(elem.dur, max(0.08, room))
            elem.text_segs = [
                (t0, full, min(dur, max(0.08, deadline(t0) - t0)))
                for t0, full, dur in elem.text_segs
            ]
            elem.versions = [
                (t0, pts, min(dur, max(0.08, deadline(t0) - t0)))
                for t0, pts, dur in elem.versions
            ]
            elem.fill_keys = [
                (t0, val, min(dur, max(0.08, deadline(t0) - t0)))
                for t0, val, dur in elem.fill_keys
            ]

    def overflow_report(self) -> list[str]:
        problems = []
        for elem in self.elems:
            if elem.kind == "link":
                continue
            samples = []
            end = elem.t0 + (elem.dur or 0.2) + 0.05
            if elem.erase:
                end = min(end, elem.erase[0] - 0.04)
            if end > elem.t0 + 0.02:
                samples.append(end)
            if elem.slide:
                samples.append(elem.slide[0] + elem.slide[3] + 0.05)
            if elem.regroup:
                samples.append(elem.regroup[0] + 0.9)
            for t in samples:
                if t < elem.t0 or t > self.duration:
                    continue
                if elem.erase and t >= elem.erase[0]:
                    continue
                x, y, w, h = self.screen_rect(elem, t)
                pad = 4
                if x < -pad or y < -pad or x + w > W + pad or y + h > H + pad:
                    problems.append(
                        f"{elem.id} row {elem.row} t={t:.1f} rect=({x:.0f},{y:.0f},{w:.0f},{h:.0f})"
                    )
                # Main-board ink should stay out of T while a thumbnail is showing,
                # except during the shrink animation itself.
                if elem.regroup and t < elem.regroup[0] + 0.8:
                    continue
                if self.group_at(elem, t) != "root":
                    continue
                for a, b in self.t_occupied:
                    if a <= t <= b and _overlap((x, y, w, h), T_RECT):
                        problems.append(
                            f"{elem.id} overlaps T at t={t:.1f} rect=({x:.0f},{y:.0f},{w:.0f},{h:.0f})"
                        )
                        break
        return problems

    # --- drawing -------------------------------------------------------

    def ensure_bg(self):
        if self._bg is not None:
            return
        surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, W, H)
        cr = cairo.Context(surface)
        cr.set_source_rgb(*BOARD)
        cr.paint()
        vignette = cairo.RadialGradient(W / 2, H / 2, H * 0.15, W / 2, H / 2, H * 0.78)
        vignette.add_color_stop_rgba(0, 0, 0, 0, 0)
        vignette.add_color_stop_rgba(1, 0, 0, 0, 0.38)
        cr.set_source(vignette)
        cr.paint()
        rng = random.Random(7)
        for _ in range(1800):
            x = rng.randrange(W)
            y = rng.randrange(H)
            cr.set_source_rgba(1, 1, 1, rng.uniform(0.012, 0.045))
            cr.rectangle(x, y, rng.choice((1, 1, 2)), rng.choice((1, 1, 2)))
            cr.fill()
        self._bg = surface

    def render(self, surface: cairo.ImageSurface, t: float):
        self.ensure_bg()
        cr = cairo.Context(surface)
        cr.set_operator(cairo.OPERATOR_SOURCE)
        cr.set_source_surface(self._bg, 0, 0)
        cr.paint()
        cr.set_operator(cairo.OPERATOR_OVER)
        alive = [e for e in self.elems if self.visible(e, t)]
        for elem in alive:
            if elem.kind != "link":
                self._draw_elem(cr, elem, t)
        for elem in alive:
            if elem.kind == "link":
                self._draw_link(cr, elem, t)
        if self.debug_boxes:
            self._draw_debug(cr, alive, t)
        if self.fade and t >= self.fade[0]:
            span = max(0.05, self.fade[1] - self.fade[0])
            p = min(1.0, (t - self.fade[0]) / span)
            cr.set_source_rgba(*BOARD, p)
            cr.paint()

    def _draw_debug(self, cr, alive, t):
        cr.save()
        cr.set_line_width(1)
        cr.set_source_rgba(1, 0.2, 0.2, 0.7)
        for elem in alive:
            if elem.kind == "link":
                continue
            x, y, w, h = self.screen_rect(elem, t)
            cr.rectangle(x, y, w, h)
            cr.stroke()
        cr.restore()

    def _stroke(self, cr, pts, color, alpha, lw, style, scale: float):
        if len(pts) < 2 or alpha <= 0.01:
            return
        cr.save()
        cr.set_source_rgba(color[0], color[1], color[2], alpha)
        cr.set_line_width(lw)
        cr.set_line_cap(cairo.LINE_CAP_ROUND)
        cr.set_line_join(cairo.LINE_JOIN_ROUND)
        if style == "dashed":
            cr.set_dash([16 / scale, 11 / scale])
        elif style == "dotted":
            cr.set_dash([0.8 / scale, 9 / scale])
        cr.move_to(*pts[0])
        for pt in pts[1:]:
            cr.line_to(*pt)
        cr.stroke()
        cr.restore()

    def _path(self, elem: Elem) -> list[tuple[float, float]]:
        key = "path"
        if elem.cache.get(key) is not None and not elem.versions:
            return elem.cache[key]
        if elem.kind == "rect":
            pts = wobble(rect_points(elem.x, elem.y, elem.w, elem.h), seed_for(elem.id), 1.5)
        elif elem.kind == "line":
            pts = wobble(
                line_points(elem.x, elem.y, elem.x2, elem.y2),
                seed_for(elem.id),
                1.35,
            )
        elif elem.kind == "poly":
            pts = wobble(list(elem.points or []), seed_for(elem.id), 1.15)
        else:
            pts = []
        if not elem.versions:
            elem.cache[key] = pts
        return pts

    def _poly_now(self, elem: Elem, t: float):
        pts = list(elem.points or [])
        reveal = self.reveal(elem, t)
        started = elem.t0
        for vt, new_pts, dur in elem.versions:
            if t < vt:
                break
            pts = new_pts
            started = vt
            reveal = 1.0 if dur <= 0 else min(1.0, (t - vt) / dur)
        if elem.kind == "poly" and elem.versions and t >= elem.versions[0][0]:
            pts = wobble(pts, seed_for(elem.id + "@" + str(int(started * 10))), 1.15)
        else:
            pts = self._path(elem) if elem.kind != "poly" or not elem.versions else pts
            if elem.kind == "poly" and not elem.versions:
                pts = self._path(elem)
        return pts, reveal

    def _draw_elem(self, cr, elem: Elem, t: float):
        alpha = self.opacity_at(elem, t)
        if alpha <= 0.02:
            return
        group = self.group_at(elem, t)
        s, ox, oy = self.xform_params(group, t)
        cr.save()
        cr.set_matrix(cairo.Matrix(s, 0, 0, s, ox, oy))
        ep = self.erase_p(elem, t)
        if ep > 0:
            x, y, w, h = self.local_rect(elem, t)
            cr.rectangle(x + w * ep - 8, y - 30, w * (1 - ep) + 80, h + 60)
            cr.clip()
        color = self.color_at(elem, t)
        if elem.kind == "text":
            self._draw_text(cr, elem, t, color, alpha)
        elif elem.kind == "rect":
            self._draw_rect(cr, elem, t, color, alpha, s)
        elif elem.kind == "bar":
            self._draw_bar(cr, elem, t, color, alpha, s)
        elif elem.kind == "line":
            self._draw_line(cr, elem, t, color, alpha, s)
        elif elem.kind == "poly":
            pts, reveal = self._poly_now(elem, t)
            shown = subpath(pts, reveal)
            self._stroke(cr, shown, color, alpha, elem.lw, elem.style, s)
            if elem.arrow and reveal > 0.92 and len(pts) >= 2:
                self._arrow_head(cr, pts[-2], pts[-1], color, alpha, elem.lw + 1)
        elif elem.kind == "circle":
            self._draw_circle(cr, elem, t, color, alpha, s)
        elif elem.kind == "dot":
            if self.reveal(elem, t) > 0.2:
                cr.set_source_rgba(*color, alpha)
                cr.arc(elem.x, elem.y, elem.w, 0, math.tau)
                cr.fill()
        elif elem.kind == "arc":
            reveal = self.reveal(elem, t)
            cr.set_source_rgba(*color, alpha)
            cr.set_line_width(elem.lw)
            cr.set_line_cap(cairo.LINE_CAP_ROUND)
            a1 = elem.a0 + (elem.a1 - elem.a0) * reveal
            cr.arc(elem.x, elem.y, elem.w, elem.a0, a1)
            cr.stroke()
        elif elem.kind == "stamp":
            self._draw_stamp(cr, elem, t, color, alpha, s)
        hi, pulse = self._highlight(elem, t)
        if hi:
            self._draw_hi(cr, elem, t, color, alpha, pulse, s)
        cr.restore()

    def _highlight(self, elem: Elem, t: float) -> tuple[bool, float]:
        pulse = 1.0
        active = False
        for t0, until in elem.highlight_spans:
            end = 1e9 if until is None else until
            if t0 <= t < end:
                active = True
                u = t - t0
                if u < 0.5:
                    pulse = 1.0 + 0.45 * math.sin(u / 0.5 * math.pi)
        return active, pulse

    def _draw_hi(self, cr, elem, t, color, alpha, pulse, scale):
        x, y, w, h = self.local_rect(elem, t)
        pad = 7
        cr.save()
        cr.set_source_rgba(color[0], color[1], color[2], min(1, alpha))
        cr.set_line_width((elem.lw * 2.1 * pulse))
        cr.set_line_cap(cairo.LINE_CAP_ROUND)
        if elem.style == "dashed":
            cr.set_dash([16 / scale, 11 / scale])
        elif elem.style == "dotted":
            cr.set_dash([0.8 / scale, 9 / scale])
        pts = wobble(
            rect_points(x - pad, y - pad, w + pad * 2, h + pad * 2, n=4),
            seed_for(elem.id + "#"),
            1.2,
        )
        cr.move_to(*pts[0])
        for pt in pts[1:]:
            cr.line_to(*pt)
        cr.close_path()
        cr.stroke()
        cr.restore()

    def _draw_text(self, cr, elem, t, color, alpha):
        shown = self.text_shown(elem, t, full=False)
        if not shown:
            return
        lines = self.layout_text(shown, elem.size, elem.max_w)
        _tw, th, line_h = self.text_block_size(shown, elem.size, elem.max_w)
        x, y = self.anchor_pos(elem, t)
        if elem.ax == "center":
            # Recompute width of shown lines for centering.
            pass
        top = y - th / 2 if elem.ay == "middle" else y
        self._font(cr, elem.size, False)
        ascent = cr.font_extents()[0]
        cr.save()
        if elem.rotation:
            cr.translate(x, y)
            cr.rotate(elem.rotation * math.pi / 180)
            cr.translate(-x, -y)
        for i, line in enumerate(lines):
            lw = sum(self._piece_width(k, d, elem.size) for k, d in line)
            lx = x - lw / 2 if elem.ax == "center" else x
            baseline = top + i * line_h + ascent
            self._draw_pieces(cr, line, lx, baseline, elem.size, color, alpha)
        cr.restore()

    def _draw_pieces(self, cr, pieces, x, baseline, size, color, alpha):
        cursor = x
        for kind, data in pieces:
            if kind == "arrow":
                self._inline_arrow(cr, data, cursor, baseline, size, color, alpha)
                cursor += size * 0.78
                continue
            self._font(cr, size, kind == "fallback")
            cr.set_source_rgba(color[0], color[1], color[2], alpha)
            cr.move_to(cursor, baseline)
            cr.show_text(data)
            cursor += cr.text_extents(data).x_advance

    def _inline_arrow(self, cr, kind, x, baseline, size, color, alpha):
        y = baseline - size * 0.32
        length = size * 0.62
        cr.save()
        cr.set_source_rgba(*color, alpha)
        cr.set_line_width(max(2.0, size * 0.07))
        cr.set_line_cap(cairo.LINE_CAP_ROUND)
        if kind == "right":
            cr.move_to(x, y)
            cr.line_to(x + length, y)
            cr.move_to(x + length - size * 0.16, y - size * 0.12)
            cr.line_to(x + length, y)
            cr.line_to(x + length - size * 0.16, y + size * 0.12)
        elif kind == "left":
            cr.move_to(x + length, y)
            cr.line_to(x, y)
            cr.move_to(x + size * 0.16, y - size * 0.12)
            cr.line_to(x, y)
            cr.line_to(x + size * 0.16, y + size * 0.12)
        elif kind == "up":
            cr.move_to(x + length / 2, y + size * 0.18)
            cr.line_to(x + length / 2, y - size * 0.22)
            cr.move_to(x + length / 2 - size * 0.12, y - size * 0.06)
            cr.line_to(x + length / 2, y - size * 0.22)
            cr.line_to(x + length / 2 + size * 0.12, y - size * 0.06)
        elif kind == "down":
            cr.move_to(x + length / 2, y - size * 0.22)
            cr.line_to(x + length / 2, y + size * 0.18)
            cr.move_to(x + length / 2 - size * 0.12, y + size * 0.02)
            cr.line_to(x + length / 2, y + size * 0.18)
            cr.line_to(x + length / 2 + size * 0.12, y + size * 0.02)
        elif kind == "both":
            cr.move_to(x, y)
            cr.line_to(x + length, y)
            cr.move_to(x + size * 0.14, y - size * 0.1)
            cr.line_to(x, y)
            cr.line_to(x + size * 0.14, y + size * 0.1)
            cr.move_to(x + length - size * 0.14, y - size * 0.1)
            cr.line_to(x + length, y)
            cr.line_to(x + length - size * 0.14, y + size * 0.1)
        cr.stroke()
        cr.restore()

    def _draw_rect(self, cr, elem, t, color, alpha, scale):
        reveal = self.reveal(elem, t)
        if elem.grow == "right":
            self._clip_frac(cr, elem, reveal, "right")
            self._fill_and_outline(cr, elem, color, alpha, scale, dashed=elem.style != "solid")
            return
        if elem.grow == "up":
            self._clip_frac(cr, elem, reveal, "up")
            self._fill_and_outline(cr, elem, color, alpha, scale, dashed=elem.style != "solid")
            return
        pts = subpath(self._path(elem), reveal)
        if elem.fill and reveal > 0.72:
            cr.save()
            cr.set_source_rgba(color[0], color[1], color[2], alpha * 0.9)
            cr.rectangle(elem.x, elem.y, elem.w, elem.h)
            cr.fill()
            cr.restore()
        style = elem.style if reveal > 0.98 or elem.style == "solid" else elem.style
        self._stroke(cr, pts, color, alpha, elem.lw, elem.style, scale)

    def _clip_frac(self, cr, elem, frac, how):
        if frac >= 0.999:
            return
        if how == "right":
            cr.rectangle(elem.x - 2, elem.y - 4, elem.w * frac + 2, elem.h + 8)
        else:
            shown = elem.h * frac
            cr.rectangle(elem.x - 4, elem.y + elem.h - shown, elem.w + 8, shown + 4)
        cr.clip()

    def _fill_and_outline(self, cr, elem, color, alpha, scale, dashed=False):
        if elem.fill and not dashed:
            cr.set_source_rgba(color[0], color[1], color[2], alpha * 0.92)
            cr.rectangle(elem.x, elem.y, elem.w, elem.h)
            cr.fill()
        self._stroke(cr, self._path(elem), color, alpha, elem.lw, elem.style, scale)

    def _draw_bar(self, cr, elem, t, color, alpha, scale):
        fill = self._keyed(elem.fill_keys, t, default=0.0)
        ghost = self._keyed(elem.ghost_keys, t, default=0.0)
        solid_h = max(0.0, elem.h * fill)
        if solid_h > 0.5 and elem.style == "solid":
            cr.set_source_rgba(color[0], color[1], color[2], alpha * 0.92)
            cr.rectangle(elem.x, elem.y + elem.h - solid_h, elem.w, solid_h)
            cr.fill()
        # Outline of the solid portion (or the whole dashed ghost bar).
        if elem.style != "solid":
            outline_h = elem.h * max(fill, 0.001)
            y = elem.y + elem.h - outline_h
            pts = wobble(rect_points(elem.x, y, elem.w, outline_h, n=4), seed_for(elem.id), 1.3)
            self._stroke(cr, subpath(pts, self.reveal(elem, t)), color, alpha, elem.lw, elem.style, scale)
        else:
            y = elem.y + elem.h - max(solid_h, 1)
            pts = wobble(
                rect_points(elem.x, y, elem.w, max(solid_h, 1), n=3),
                seed_for(elem.id),
                1.2,
            )
            self._stroke(cr, pts, color, alpha, elem.lw, "solid", scale)
        if ghost > fill + 0.02:
            gy = elem.y + elem.h - elem.h * ghost
            gh = elem.h * (ghost - fill)
            pts = wobble(rect_points(elem.x, gy, elem.w, gh, n=3), seed_for(elem.id + "g"), 1.1)
            gcolor = elem.ghost_color or color
            self._stroke(cr, pts, gcolor, alpha * 0.4, elem.lw, "solid", scale)

    def _draw_line(self, cr, elem, t, color, alpha, scale):
        reveal = self.reveal(elem, t)
        pts = subpath(self._path(elem), reveal)
        self._stroke(cr, pts, color, alpha, elem.lw, elem.style, scale)
        if elem.arrow and reveal > 0.9:
            full = self._path(elem)
            self._arrow_head(cr, full[-2], full[-1], color, alpha, elem.lw)

    def _arrow_head(self, cr, p0, p1, color, alpha, lw):
        ang = math.atan2(p1[1] - p0[1], p1[0] - p0[0])
        size = 16 + lw
        cr.save()
        cr.set_source_rgba(*color, alpha)
        cr.set_line_width(lw)
        cr.set_line_cap(cairo.LINE_CAP_ROUND)
        for delta in (2.55, -2.55):
            cr.move_to(p1[0], p1[1])
            cr.line_to(p1[0] + size * math.cos(ang + delta), p1[1] + size * math.sin(ang + delta))
            cr.stroke()
        cr.restore()

    def _draw_circle(self, cr, elem, t, color, alpha, scale):
        reveal = self.reveal(elem, t)
        cr.save()
        cr.set_source_rgba(*color, alpha)
        cr.set_line_width(elem.lw)
        cr.set_line_cap(cairo.LINE_CAP_ROUND)
        if elem.style == "dashed":
            cr.set_dash([14 / scale, 10 / scale])
        elif elem.style == "dotted":
            cr.set_dash([0.8 / scale, 8 / scale])
        a0 = -math.pi / 2
        cr.arc(elem.x, elem.y, elem.w, a0, a0 + math.tau * reveal)
        cr.stroke()
        if elem.fill and reveal > 0.85:
            cr.arc(elem.x, elem.y, elem.w * 0.82, 0, math.tau)
            cr.fill()
        cr.restore()

    def _draw_stamp(self, cr, elem, t, color, alpha, scale):
        shown = self.text_shown(elem, t, full=False)
        if not shown:
            return
        tw, th, _lh = self.text_block_size(elem.text, elem.size, elem.max_w)
        pad = 12
        w, h = tw + pad * 2, th + pad * 2
        cr.save()
        cr.translate(elem.x, elem.y)
        cr.rotate(elem.rotation * math.pi / 180)
        cr.translate(-elem.x, -elem.y)
        pts = subpath(
            wobble(
                rect_points(elem.x - w / 2, elem.y - h / 2, w, h, n=4),
                seed_for(elem.id),
                1.2,
            ),
            self.reveal(elem, t),
        )
        self._stroke(cr, pts, color, alpha, 3.0, elem.style, scale)
        # Context is already rotated; don't rotate the glyphs a second time.
        saved = elem.rotation
        elem.rotation = 0
        self._draw_text(cr, elem, t, color, alpha)
        elem.rotation = saved
        cr.restore()

    def _draw_link(self, cr, elem, t):
        target = self.by_id.get(elem.target or "")
        if target is None or not self.visible(target, t):
            return
        alpha = self.opacity_at(elem, t)
        reveal = self.reveal(elem, t)
        tx, ty, tw, th = self.screen_rect(target, t)
        x2, y2 = tx + tw / 2, ty + th / 2
        pts = subpath(line_points(elem.x, elem.y, x2, y2, n=6), reveal)
        self._stroke(cr, pts, elem.color, alpha, 3.0, "solid", 1)
        if reveal > 0.9:
            self._arrow_head(cr, pts[-2] if len(pts) > 1 else (elem.x, elem.y), (x2, y2), elem.color, alpha, 3.0)


def _overlap(a, b) -> bool:
    ax, ay, aw, ah = a
    bx, by, bw, bh = b
    return not (ax + aw < bx or bx + bw < ax or ay + ah < by or by + bh < ay)
