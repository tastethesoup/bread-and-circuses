# Credit & Fed Desk (SKETCH)

This episode layout is a sketch. Publish the October 6, 2026 pilot with it. CoS will lock the template later.

Pages live at `/posts/credit-fed-desk-YYYY-MM-DD/` and use `src/_includes/layouts/podcast.njk`. `src/posts/posts.json` still tags them `posts`, so the usual Open Graph tags in `layouts/base.njk` apply. The home page lists the episode in the normal post list.

The layout prints the title, date, runtime, a native audio player, the Markdown cold open, optional show notes, and links to `/` and `/posts/log-week-3/`.

Audio files live in `src/assets/audio/` and share cards live in `src/assets/og/`. Eleventy already passthrough-copies `src/assets`, so Pages serves `/assets/audio/...` and `/assets/og/...`.

## Front matter

```yaml
title: "Credit & Fed Desk: October 6, 2026"
description: "Short share blurb (1-2 sentences)."
date: 2026-10-06
permalink: /posts/credit-fed-desk-YYYY-MM-DD/
layout: layouts/podcast.njk
ogImage: /assets/og/credit-fed-desk-YYYY-MM-DD.png
podcast:
  show: "Credit & Fed Desk"
  runtime: "19 min"
  audio: /assets/audio/credit-fed-desk-YYYY-MM-DD.mp3
  showNotes:
    - "Bullet from the episode roadmap"
```

`description` is the share blurb. `ogImage` is a root-relative path. The built HTML emits an absolute `og:image`. `podcast.runtime` is the length label (about 19 minutes for this pilot). `podcast.audio` is the root-relative MP3. `podcast.showNotes` is optional. The Markdown body is the cold open only.

## Share card

Cream 1200×630 PNG, title and date, same palette and Instrument Serif as the LOG cards. Not part of `npm run build`. Commit the PNG with the episode.

```bash
python3 scripts/render-podcast-og.py
```

Pillow is required (`pip install pillow`). Fonts are vendored in `scripts/fonts/`.
