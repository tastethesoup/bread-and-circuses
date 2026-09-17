# LOG newsletter guide

Weekly League of Ordinary Gentlemen posts are ordinary Markdown posts plus a `log` (and optional `pullQuote`) block in front matter. The post layout draws the phone-first UI: week strip, sticky section nav, matchup cards, blotter tickets, and pick chips. Regular posts without `log` are unchanged.

Do not use em dashes in copy. Prefer periods, commas, parentheses, or a new sentence. Scores may use a simple hyphen (`142.8 - 117.3` in prose). Section headings stay **bold and underlined** (`h2` in the layout and in Markdown).

See `src/posts/2026-09-16-log-week-1.md` for a full example.

## Front matter

```yaml
title: LOG Week 2
description: League of Ordinary Gentlemen fantasy football newsletter.
pullQuote: The best line from the cold open.
log:
  week: 2
  record: 3-2          # optional; otherwise counted from scored games
  gamesIntro: Optional sentence above the cards.
  games:
    - home: "Prestige Worldwide"
      away: "CeeDeez Nutz"
      homeScore: 142.8
      awayScore: 117.3
      pick: "Prestige Worldwide"   # omit for NO PICK
      roast: One sentence. No need for a photo.
  rankingsIntro: Optional.
  rankings:
    - team: "Drake It To You Make It"
      record: 1-0
  blotter:
    - team: "AINTS dat a B** Payola"
      charge: Sitting the wrong tight end
      evidence: One line of evidence.
  slate:
    - home: "Prestige Worldwide"
      away: "Drake It To You Make It"
      pick: "Prestige Worldwide"
      gotw: true
  gotw:
    home: "Prestige Worldwide"
    away: "Drake It To You Make It"
    pick: "Prestige Worldwide"
    gotw: true
    blurb: Why this is the game of the week.
```

Team names can be the full name or the slug (`prestige-worldwide`). Quote names that start with a hyphen (like `"-Sutt-Dog -"`). Unknown names still render, with initials instead of a logo. The league has 10 teams.

The Markdown body is the cold open (and any extra notes). Games, rankings, blotter, slate, and GOTW come from `log` so you are not maintaining two copies.

## Pull quote

Three equivalent ways. Use one.

1. Top-level front matter (preferred):

   ```yaml
   pullQuote: Week 1 is a noisy, incomplete picture, and we will treat it that way.
   ```

   `log.pullQuote` works too.

2. A paired shortcode in Markdown:

   ```njk
   {% pullQuote %}
   Week 1 is a noisy, incomplete picture, and we will treat it that way.
   {% endpullQuote %}
   ```

3. HTML class, if you want it inline:

   ```html
   <blockquote class="pull-quote">Week 1 is a noisy, incomplete picture, and we will treat it that way.</blockquote>
   ```

It renders larger, italic, with a left bar. It is meant to break up the cold open without a photo.

## Matchup cards

Each `log.games` item is one stacked card: logos, names, a score line with a separate W/L pill, one roast line, and a pick-result chip (HIT, MISS, or NO PICK). Winner is the higher score. Scores sit on their own row under the team name, not beside it.

`log.slate` items are the same card without scores. Put `pick:` on the team you like. Add `gotw: true` for the Game of the Week chip. Cards are a single column. They do not scroll sideways.

## Crime blotter tickets

Each `log.blotter` item is a dashed "ticket": team logo (or initials), **charge** in bold, one **evidence** line. Player headshots are optional and unused by default. A team logo is enough.

## Pick / result chips

Every chip has a text label. Color is never the only signal (filled vs outline, hatch vs solid).

| Chip | When |
| --- | --- |
| PICK | Next-week (or GOTW) selection |
| GOTW | Game of the Week |
| W / L | Final on a scored card |
| HIT / MISS | Last week's pick, scored against the winner |
| NO PICK | No `pick` on that game |

The hero strip shows **Week N** and the pick record (`hits-misses`). No-picks are not wins or losses.

In Markdown you can also drop a chip with `{% logChip "HIT" %}`.

## Logos

Team records live in `src/_data/logTeams.json` (10 teams, ESPN leagueId 856379). Artwork lives in `src/assets/logos/`. Read that folder's README for the cache vs initials fallback table.

If the file is missing, the path is wrong, `logo` is omitted, or the image 404s, the card shows a colored initials avatar. Do not hotlink ESPN CDN, Photobucket, WordPress, or Mystique URLs.

## Sticky nav

When `log` has games, rankings, blotter, slate, or GOTW, a compact chrome bar sticks to the top of the viewport: Games, Rankings, Blotter, Next week, GOTW. It is one slim bar (smaller type, tighter padding, light background, bottom border), not a second row of large tap-target pills. Anchors use `#games`, `#rankings`, `#blotter`, `#next-week`, `#gotw`.
