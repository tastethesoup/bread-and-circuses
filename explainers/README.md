# Blackboard explainers

Two Credit & Fed Desk lessons, drawn as a Khan Academy dark blackboard in time with locked narration.

- **The Long End Breaks Loose** is the episode that publishes first. The site stub in `src/posts/` is excluded from the build (`permalink: false` and `eleventyExcludeFromCollections: true`), so merging this branch does not put it on the live site.
- **It's Over** is held for a later date. It has no page and no index entry in this branch.

Scripts, narration, and storyboards are locked. The scene files follow the storyboard rows. They do not rewrite spoken words.

## Build

From the repo root, with system `python3-cairo`, `ffmpeg`, and `fontconfig` (no pip packages):

```bash
python3 explainers/render.py
```

That installs the vendored Patrick Hand font if Fontconfig does not already see it, writes WebVTT captions and chapters, and renders both lessons to `explainers/build/` as 1920×1080, 30 fps H.264 with the narration as the only audio track. MP4s are gitignored.

To render one lesson: `python3 explainers/render.py long-end` or `python3 explainers/render.py its-over`.

## What is committed

- `explainers/bb/` — Cairo scene engine and caption packer
- `explainers/scenes/` — one function per storyboard row
- `explainers/audio/` — locked narration
- `explainers/storyboards/` and `explainers/timings/` — locked inputs
- `explainers/captions/` — WebVTT captions and chapters
- `explainers/assets/fonts/` — Patrick Hand (OFL)

## Deliberate drawing choices

- It's Over row 3.09 allows an optional thin chalk connector from "AI chips" back to the fee. It is not drawn.
- The Long End question mark inside the amber block is chalk. An amber glyph on the amber fill would disappear.
- At Long End row 2.33 the new tray header replaces the October 7 header on the same line.
