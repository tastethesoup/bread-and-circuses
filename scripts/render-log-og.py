#!/usr/bin/env python3
"""Render a LOG Open Graph card (1200x630) for one week.

Writes src/assets/og/log-week-{n}.png. Not part of the Eleventy build.
Commit the PNG so CI does not need fonts or network access.

Usage:
  python3 scripts/render-log-og.py 2

Requires Pillow (`pip install pillow`). Instrument Serif is vendored in
scripts/fonts/ (SIL Open Font License, see OFL.txt). The week word comes
from log-lib.js so the card matches the masthead.
"""

import argparse
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FONT_DIR = ROOT / "scripts" / "fonts"
OUT_DIR = ROOT / "src" / "assets" / "og"

WIDTH = 1200
HEIGHT = 630
# Measured from the Week Two sample. Close to the requested ~#F8F5F2.
BG = (0xF6, 0xF4, 0xEC)
INK = (0x1B, 0x19, 0x14)
MUTED = (0x59, 0x53, 0x47)
DISPLAY_SIZE = 170
ITALIC_SIZE = 58
LEFT = 72
LOG_BASELINE = 168
SUB_BASELINE = 430
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


def render(week: int, out_path: Path) -> None:
    try:
        from PIL import Image, ImageDraw, ImageFont
    except ModuleNotFoundError as error:
        raise SystemExit("Pillow is required: pip install pillow") from error

    regular = ImageFont.truetype(
        str(FONT_DIR / "InstrumentSerif-Regular.ttf"), DISPLAY_SIZE
    )
    italic = ImageFont.truetype(
        str(FONT_DIR / "InstrumentSerif-Italic.ttf"), ITALIC_SIZE
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
    draw.text((LEFT, SUB_BASELINE), SUBTITLE[0], font=italic, fill=MUTED, anchor="ls")
    draw.text(
        (LEFT, SUB_BASELINE + round(ITALIC_SIZE * 1.62)),
        SUBTITLE[1],
        font=italic,
        fill=MUTED,
        anchor="ls",
    )
    out_path.parent.mkdir(parents=True, exist_ok=True)
    image.save(out_path, "PNG", optimize=True)


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
    render(args.week, out_path)
    print(out_path.relative_to(ROOT))


if __name__ == "__main__":
    main()
