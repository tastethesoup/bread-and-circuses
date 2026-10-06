#!/usr/bin/env python3
"""Render a Credit & Fed Desk Open Graph card (1200x630).

Writes src/assets/og/credit-fed-desk-YYYY-MM-DD.png. Not part of the
Eleventy build. Commit the PNG so CI does not need fonts.

Usage:
  python3 scripts/render-podcast-og.py
  python3 scripts/render-podcast-og.py --date "October 6, 2026" --slug 2026-10-06

Requires Pillow (`pip install pillow`). Instrument Serif is vendored in
scripts/fonts/ (SIL Open Font License, see OFL.txt). Colors match the LOG cards.
"""

import argparse
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FONT_DIR = ROOT / "scripts" / "fonts"
OUT_DIR = ROOT / "src" / "assets" / "og"

WIDTH = 1200
HEIGHT = 630
BG = (0xF6, 0xF4, 0xEC)
INK = (0x1B, 0x19, 0x14)
MUTED = (0x59, 0x53, 0x47)
TITLE = "Credit & Fed Desk"
TITLE_SIZE = 108
DATE_SIZE = 52
LEFT = 72
TITLE_BASELINE = 292
MAX_TEXT = WIDTH - LEFT * 2


def render(date_label: str, out_path: Path) -> None:
    try:
        from PIL import Image, ImageDraw, ImageFont
    except ModuleNotFoundError as error:
        raise SystemExit("Pillow is required: pip install pillow") from error

    regular = ImageFont.truetype(str(FONT_DIR / "InstrumentSerif-Regular.ttf"), TITLE_SIZE)
    italic = ImageFont.truetype(str(FONT_DIR / "InstrumentSerif-Italic.ttf"), DATE_SIZE)
    image = Image.new("RGB", (WIDTH, HEIGHT), BG)
    draw = ImageDraw.Draw(image)
    title_width = draw.textlength(TITLE, font=regular)
    date_width = draw.textlength(date_label, font=italic)
    if title_width > MAX_TEXT or date_width > MAX_TEXT:
        raise SystemExit("title or date does not fit the card")
    draw.text((LEFT, TITLE_BASELINE), TITLE, font=regular, fill=INK, anchor="ls")
    draw.text(
        (LEFT, TITLE_BASELINE + round(TITLE_SIZE * 1.15)),
        date_label,
        font=italic,
        fill=MUTED,
        anchor="ls",
    )
    out_path.parent.mkdir(parents=True, exist_ok=True)
    image.save(out_path, "PNG", optimize=True)


def main() -> None:
    parser = argparse.ArgumentParser(description="Render a Credit & Fed Desk Open Graph card.")
    parser.add_argument("--date", default="October 6, 2026", help="Date line on the card")
    parser.add_argument(
        "--slug",
        default="2026-10-06",
        help="Date slug for the default filename",
    )
    parser.add_argument("--out", type=Path, help="Output PNG path")
    args = parser.parse_args()
    out_path = args.out or (OUT_DIR / f"credit-fed-desk-{args.slug}.png")
    if not out_path.is_absolute():
        out_path = ROOT / out_path
    render(args.date, out_path)
    print(out_path.relative_to(ROOT))


if __name__ == "__main__":
    main()
