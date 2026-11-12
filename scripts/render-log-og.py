#!/usr/bin/env python3
"""Render a LOG Open Graph card (1200x630) for one week.

Writes src/assets/og/log-week-{n}.png. Not part of the Eleventy build.
Commit the PNG so CI does not need fonts or network access.

Usage:
  python3 scripts/render-log-og.py 2

The italic line under "LOG / Week N" is that week's title line, read from
the week's post front matter in this order: log.ogTitleLine, pullQuote,
log.pullQuote, log.lede. If all are blank, the card uses the shared
two-line newsletter subtitle.

Requires Pillow (`pip install pillow`). Instrument Serif is vendored in
scripts/fonts/ (SIL Open Font License, see OFL.txt). The week word comes
from log-lib.js so the card matches the masthead.
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FONT_DIR = ROOT / "scripts" / "fonts"
OUT_DIR = ROOT / "src" / "assets" / "og"
POSTS_DIR = ROOT / "src" / "posts"

WIDTH = 1200
HEIGHT = 630
# Measured from the Week Two sample. Close to the requested ~#F8F5F2.
BG = (0xF6, 0xF4, 0xEC)
INK = (0x1B, 0x19, 0x14)
MUTED = (0x59, 0x53, 0x47)
DISPLAY_SIZE = 170
ITALIC_SIZE = 58
ITALIC_MIN = 44
LEFT = 72
RIGHT = 72
MAX_WIDTH = WIDTH - LEFT - RIGHT
LOG_BASELINE = 168
SUB_BASELINE = 430
BOTTOM_PAD = 36
MAX_LINES = 3
SUBTITLE = (
    "League of Ordinary Gentlemen fantasy football",
    "newsletter",
)


def week_word(week: int) -> str:
    script = (
        "import { weekWord } from './log-lib.js';"
        f"process.stdout.write(String(weekWord({week})));"
    )
    result = subprocess.run(
        ["node", "--input-type=module", "-e", script],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    word = result.stdout.strip()
    if not word:
        raise SystemExit(f"weekWord({week}) returned an empty label")
    return word


def unquote(value: str) -> str:
    text = value.strip()
    if len(text) >= 2 and text[0] == text[-1] and text[0] in ('"', "'"):
        quote = text[0]
        text = text[1:-1]
        text = text.replace("\\" + quote, quote).replace("\\n", "\n")
    return text.strip()


def top_scalar(front_matter: str, key: str) -> str:
    match = re.search(rf"^{re.escape(key)}:\s*(.*)$", front_matter, re.M)
    if not match:
        return ""
    return unquote(match.group(1))


def log_scalar(front_matter: str, key: str) -> str:
    in_log = False
    for line in front_matter.splitlines():
        if re.match(r"^log:\s*$", line):
            in_log = True
            continue
        if not in_log:
            continue
        if line and not line.startswith(" ") and not line.startswith("\t"):
            in_log = False
            continue
        match = re.match(rf"^  {re.escape(key)}:\s*(.*)$", line)
        if match:
            raw = match.group(1).strip()
            if raw in ("", "|", ">", ">-", "|-"):
                return ""
            return unquote(raw)
    return ""


def find_week_post(week: int) -> Path | None:
    matches = sorted(POSTS_DIR.glob(f"*-log-week-{week}.md"))
    if not matches:
        return None
    return matches[-1]


def title_line_from_post(week: int) -> tuple[str, str]:
    """Return (line, source). Source is the field name, or empty if fallback."""
    path = find_week_post(week)
    if path is None:
        return "", "fallback"
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return "", "fallback"
    parts = text.split("---", 2)
    if len(parts) < 3:
        return "", "fallback"
    front = parts[1]
    candidates = (
        (log_scalar(front, "ogTitleLine"), "log.ogTitleLine"),
        (top_scalar(front, "pullQuote"), "pullQuote"),
        (log_scalar(front, "pullQuote"), "log.pullQuote"),
        (log_scalar(front, "lede"), "log.lede"),
    )
    for value, source in candidates:
        if value:
            return value, source
    return "", "fallback"


def text_width(font, text: str) -> int:
    left, _top, right, _bottom = font.getbbox(text)
    return right - left


def greedy_wrap(text: str, font, max_width: int) -> list[str]:
    words = text.split()
    lines: list[str] = []
    current = ""
    for word in words:
        trial = word if not current else f"{current} {word}"
        if text_width(font, trial) <= max_width:
            current = trial
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def wrap_title(text: str, font, max_width: int) -> list[str]:
    if text_width(font, text) <= max_width:
        return [text]
    if ", " in text:
        idx = text.find(", ")
        left = text[: idx + 1]
        right = text[idx + 2 :]
        if (
            left
            and right
            and text_width(font, left) <= max_width
            and text_width(font, right) <= max_width
        ):
            return [left, right]
    return greedy_wrap(text, font, max_width)


def layout_title(text: str):
    from PIL import ImageFont

    size = ITALIC_SIZE
    while size >= ITALIC_MIN:
        font = ImageFont.truetype(str(FONT_DIR / "InstrumentSerif-Italic.ttf"), size)
        lines = wrap_title(text, font, MAX_WIDTH)
        if len(lines) <= MAX_LINES and all(
            text_width(font, line) <= MAX_WIDTH for line in lines
        ):
            return font, lines, size, False
        size -= 2
    font = ImageFont.truetype(str(FONT_DIR / "InstrumentSerif-Italic.ttf"), ITALIC_MIN)
    lines = greedy_wrap(text, font, MAX_WIDTH)
    truncated = False
    if len(lines) > MAX_LINES:
        kept = lines[:MAX_LINES]
        last = kept[-1].rstrip()
        while last and text_width(font, last + "...") > MAX_WIDTH:
            last = last.rsplit(" ", 1)[0] if " " in last else last[:-1]
        kept[-1] = (last + "...").rstrip()
        lines = kept
        truncated = True
    return font, lines, ITALIC_MIN, truncated


def render(week: int, out_path: Path) -> dict:
    try:
        from PIL import Image, ImageDraw, ImageFont
    except ModuleNotFoundError as error:
        raise SystemExit("Pillow is required: pip install pillow") from error

    regular = ImageFont.truetype(
        str(FONT_DIR / "InstrumentSerif-Regular.ttf"), DISPLAY_SIZE
    )
    label = week_word(week)
    image = Image.new("RGB", (WIDTH, HEIGHT), BG)
    draw = ImageDraw.Draw(image)
    draw.text((LEFT, LOG_BASELINE), "LOG", font=regular, fill=INK, anchor="ls")
    draw.text(
        (LEFT, LOG_BASELINE + round(DISPLAY_SIZE * 0.9)),
        f"Week {label}",
        font=regular,
        fill=INK,
        anchor="ls",
    )

    line, source = title_line_from_post(week)
    info = {
        "week": week,
        "source": source,
        "line": line,
        "size": ITALIC_SIZE,
        "lines": [],
        "shrunk": False,
        "truncated": False,
        "fallback": source == "fallback" or not line,
    }

    if line:
        font, lines, size, truncated = layout_title(line)
        ratio = 1.62 if len(lines) <= 2 else 1.35
        advance = round(size * ratio)
        _ascent, descent = font.getmetrics()
        last_baseline = HEIGHT - BOTTOM_PAD - descent
        first = last_baseline - advance * (len(lines) - 1)
        if len(lines) <= 2:
            first = SUB_BASELINE
        for index, wrapped in enumerate(lines):
            draw.text(
                (LEFT, first + index * advance),
                wrapped,
                font=font,
                fill=MUTED,
                anchor="ls",
            )
        info.update(
            {
                "size": size,
                "lines": lines,
                "shrunk": size < ITALIC_SIZE,
                "truncated": truncated,
                "fallback": False,
            }
        )
    else:
        italic = ImageFont.truetype(
            str(FONT_DIR / "InstrumentSerif-Italic.ttf"), ITALIC_SIZE
        )
        draw.text((LEFT, SUB_BASELINE), SUBTITLE[0], font=italic, fill=MUTED, anchor="ls")
        draw.text(
            (LEFT, SUB_BASELINE + round(ITALIC_SIZE * 1.62)),
            SUBTITLE[1],
            font=italic,
            fill=MUTED,
            anchor="ls",
        )
        info["lines"] = list(SUBTITLE)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    image.save(out_path, "PNG", optimize=True)
    return info


def main() -> None:
    parser = argparse.ArgumentParser(description="Render a LOG week Open Graph card.")
    parser.add_argument("week", type=int, help="LOG week number, for example 2")
    parser.add_argument(
        "--out",
        type=Path,
        help="Output PNG. Default: src/assets/og/log-week-{n}.png",
    )
    args = parser.parse_args()
    if args.week < 1:
        raise SystemExit("week must be 1 or greater")
    out_path = args.out or (OUT_DIR / f"log-week-{args.week}.png")
    if not out_path.is_absolute():
        out_path = ROOT / out_path
    info = render(args.week, out_path)
    print(out_path.relative_to(ROOT) if out_path.is_relative_to(ROOT) else out_path)
    status = info["source"]
    extras = []
    if info["fallback"]:
        extras.append("fallback subtitle")
    if info["shrunk"]:
        extras.append(f"shrunk to {info['size']}pt")
    if info["truncated"]:
        extras.append("truncated")
    extra = f" ({', '.join(extras)})" if extras else ""
    print(f"week {info['week']}: {status}, {info['size']}pt, {len(info['lines'])} line(s){extra}")
    for wrapped in info["lines"]:
        print(f"  {wrapped}")


if __name__ == "__main__":
    main()
