#!/usr/bin/env python3
"""Render both blackboard explainers.

One command from the repo root:

    python3 explainers/render.py

Needs the system packages python3-cairo, ffmpeg, and fontconfig. The
handwriting font ships in explainers/assets/fonts. No pip packages.
"""

from __future__ import annotations

import math
import shutil
import subprocess
import sys
from pathlib import Path

import cairo

ROOT = Path(__file__).resolve().parents[1]
EXPLAIN = ROOT / "explainers"
BUILD = EXPLAIN / "build"
FONT = EXPLAIN / "assets" / "fonts" / "PatrickHand-Regular.ttf"
ARTIFACTS = Path("/opt/cursor/artifacts")

from explainers.bb.captions import write_pair
from explainers.bb.engine import H, W
from explainers.scenes.its_over import build as build_its_over
from explainers.scenes.long_end import build as build_long_end

FPS = 30

ITS_OVER_SECTIONS = [
    ("The clash", 0.0),
    ('What "over" means in credit', 86.41),
    ("The financing stack", 347.02),
    ("What would have to change for one side to be right", 535.81),
]
LONG_END_SECTIONS = [
    ("The puzzle", 0.0),
    ("The two parts of a long yield", 71.89),
    ("How Treasury sells debt", 261.65),
    ("The plumbing that can amplify any move", 449.65),
    ("How long rates reach households", 659.93),
    ("Close: a checklist, not a verdict", 752.59),
]

LESSONS = [
    {
        "slug": "its-over",
        "title": "It's Over",
        "audio": EXPLAIN / "audio" / "its-over-explainer-narration-onyx.mp3",
        "timings": EXPLAIN / "timings" / "its-over-word-timings.json",
        "sections": ITS_OVER_SECTIONS,
        "build": build_its_over,
        "stills": [20, 70, 100, 160, 250, 320, 400, 480, 528, 600, 640, 670],
    },
    {
        "slug": "long-end",
        "title": "The Long End Breaks Loose",
        "audio": EXPLAIN / "audio" / "long-end-explainer-narration-onyx.mp3",
        "timings": EXPLAIN / "timings" / "long-end-word-timings.json",
        "sections": LONG_END_SECTIONS,
        "build": build_long_end,
        "stills": [50, 140, 230, 255, 320, 390, 430, 540, 610, 650, 730, 820],
    },
]


def ensure_font():
    listed = subprocess.run(
        ["fc-list", ":family=Patrick Hand", "file"],
        check=False,
        capture_output=True,
        text=True,
    )
    if "PatrickHand" in listed.stdout or "Patrick Hand" in listed.stdout:
        return
    dest_dir = Path.home() / ".local" / "share" / "fonts"
    dest_dir.mkdir(parents=True, exist_ok=True)
    shutil.copy(FONT, dest_dir / FONT.name)
    subprocess.run(["fc-cache", "-f", str(dest_dir)], check=True)


def audio_duration(path: Path) -> float:
    out = subprocess.check_output(
        [
            "ffprobe",
            "-v",
            "error",
            "-show_entries",
            "format=duration",
            "-of",
            "default=noprint_wrappers=1:nokey=1",
            str(path),
        ],
        text=True,
    )
    return float(out.strip())


def render_video(board, audio: Path, dest: Path, duration: float):
    frames = max(1, math.ceil(duration * FPS - 1e-9))
    dest.parent.mkdir(parents=True, exist_ok=True)
    cmd = [
        "ffmpeg",
        "-y",
        "-loglevel",
        "error",
        "-f",
        "rawvideo",
        "-pix_fmt",
        "bgra",
        "-s",
        f"{W}x{H}",
        "-r",
        str(FPS),
        "-i",
        "pipe:0",
        "-i",
        str(audio),
        "-map",
        "0:v:0",
        "-map",
        "1:a:0",
        "-t",
        f"{duration:.3f}",
        "-c:v",
        "libx264",
        "-pix_fmt",
        "yuv420p",
        "-crf",
        "20",
        "-preset",
        "veryfast",
        "-tune",
        "animation",
        "-threads",
        "2",
        "-c:a",
        "aac",
        "-b:a",
        "160k",
        "-movflags",
        "+faststart",
        str(dest),
    ]
    proc = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, W, H)
    assert proc.stdin is not None
    try:
        for index in range(frames):
            t = min(duration, index / FPS)
            board.render(surface, t)
            surface.flush()
            proc.stdin.write(surface.get_data())
            if index and index % 900 == 0:
                print(f"  {dest.name} {index}/{frames}", flush=True)
    finally:
        proc.stdin.close()
    code = proc.wait()
    if code != 0:
        raise SystemExit(f"ffmpeg exited {code} for {dest}")


def contact_sheet(board, times: list[float], dest: Path, title: str):
    cols = 4
    thumb_w, thumb_h = 460, 259
    pad = 14
    label_h = 26
    header = 40
    sheet_w = cols * thumb_w + (cols + 1) * pad
    rows = math.ceil(len(times) / cols)
    sheet_h = header + rows * (thumb_h + label_h) + (rows + 1) * pad
    sheet = cairo.ImageSurface(cairo.FORMAT_ARGB32, sheet_w, sheet_h)
    cr = cairo.Context(sheet)
    cr.set_source_rgb(0.07, 0.08, 0.09)
    cr.paint()
    cr.select_font_face("Patrick Hand", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
    cr.set_font_size(28)
    cr.set_source_rgb(0.95, 0.95, 0.95)
    cr.move_to(pad, 30)
    cr.show_text(title)
    frame = cairo.ImageSurface(cairo.FORMAT_ARGB32, W, H)
    for index, t in enumerate(times):
        board.render(frame, t)
        col = index % cols
        row = index // cols
        x = pad + col * (thumb_w + pad)
        y = header + pad + row * (thumb_h + label_h + pad)
        cr.save()
        cr.translate(x, y)
        cr.scale(thumb_w / W, thumb_h / H)
        cr.set_source_surface(frame, 0, 0)
        cr.paint()
        cr.restore()
        cr.set_font_size(18)
        cr.set_source_rgb(0.85, 0.85, 0.85)
        minutes = int(t // 60)
        seconds = int(t % 60)
        cr.move_to(x, y + thumb_h + 18)
        cr.show_text(f"{minutes}:{seconds:02d}")
    dest.parent.mkdir(parents=True, exist_ok=True)
    sheet.write_to_png(str(dest))


def main():
    ensure_font()
    BUILD.mkdir(parents=True, exist_ok=True)
    ARTIFACTS.mkdir(parents=True, exist_ok=True)
    captions_dir = EXPLAIN / "captions"
    captions_dir.mkdir(parents=True, exist_ok=True)
    only = set(sys.argv[1:])
    for lesson in LESSONS:
        if only and lesson["slug"] not in only:
            continue
        duration = audio_duration(lesson["audio"])
        n_cues = write_pair(
            lesson["timings"],
            captions_dir / f"{lesson['slug']}.vtt",
            captions_dir / f"{lesson['slug']}-chapters.vtt",
            lesson["sections"],
            duration,
        )
        print(f"{lesson['slug']}: {n_cues} caption cues, audio {duration:.3f}s", flush=True)
        board = lesson["build"](duration)
        problems = board.overflow_report()
        if problems:
            raise SystemExit(f"{lesson['slug']} overflow:\n" + "\n".join(problems[:12]))
        video = BUILD / f"{lesson['slug']}.mp4"
        print(f"rendering {video}", flush=True)
        render_video(board, lesson["audio"], video, duration)
        sheet = BUILD / f"{lesson['slug']}-contact-sheet.png"
        contact_sheet(board, lesson["stills"], sheet, lesson["title"])
        if ARTIFACTS.is_dir():
            shutil.copy(video, ARTIFACTS / video.name)
            shutil.copy(sheet, ARTIFACTS / sheet.name)
        print(f"done {video} ({video.stat().st_size} bytes)", flush=True)


if __name__ == "__main__":
    main()
