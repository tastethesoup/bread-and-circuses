# LOG newsletter guide

Weekly League of Ordinary Gentlemen posts are ordinary Markdown posts plus a `log` (and optional `pullQuote`) block in front matter. Posts with `log:` render as a phone-column newspaper: cream paper, Instrument Serif / Newsreader / Courier Prime, score stacks, blotter titles, Week N+1 picks, and GOTW. Regular posts without `log` are unchanged.

Do not use em dashes in copy. Prefer periods, commas, parentheses, a hyphen, or a new sentence. Ranking movement with no change is a hyphen (`-`), not an em dash.

The blank Design Components week template lives at `docs/log-week-template.dc.html` (for composing future weeks in DC). The live site does not load `support.js`, `<x-dc>`, or other DC runtime markup.

See `src/posts/2026-09-16-log-week-1.md` for a full example.

## Front matter

```yaml
title: LOG Week 2
description: League of Ordinary Gentlemen fantasy football newsletter.
pullQuote: Opening line. One sentence that sets the week.
log:
  week: 2
  record: 3-2          # optional; otherwise counted from scored games
  rankingsKicker: After Week 2
  rankingsNote: Record, then movement against last week's rank.
  games:
    - home: "Prestige Worldwide"   # winner on top
      away: "CeeDeez Nutz"
      homeScore: 142.80
      awayScore: 117.30
      roast: One or two sentences on this game.
      callout: Closest game        # optional; also Biggest beatdown
      calloutMargin: "+6"          # rounded ribbon; decimals stay on the scoreboard
  rankings:
    - team: "Drake It To You Make It"
      record: 2-0
      move: "-"                    # or ▲1 / ▼1 starting Week 2
      blurb: One line on this team.
  blotter:
    - team: "AINTS dat a B** Payola"
      charge: Sitting the wrong tight end
      evidence: What they did. Player points rounded, no decimals.
  slate:
    - home: "Prestige Worldwide"
      away: "Drake It To You Make It"
      pick: "Prestige Worldwide"   # omit for NO PICK
      gotw: true
      roast: One line on the matchup and the pick.
  gotw:
    home: "Prestige Worldwide"
    away: "Drake It To You Make It"
    pick: "Prestige Worldwide"
    pickLabel: Prestige            # short name on the OUR PICK banner
```

Team names can be the full name or the slug (`prestige-worldwide`). Quote names that start with a hyphen (like `"-Sutt-Dog -"`). Unknown names still render. The league has 10 teams.

The Markdown body is the rest of the cold open (paragraphs under the display lede). Games, rankings, blotter, slate, and GOTW come from `log` so you are not maintaining two copies.

Decimals belong on the scoreboard only. Round callout margins, blotter player points, and ranking copy.

## Masthead and lede

`pullQuote` (or `log.lede`) is the display lede in Instrument Serif. The Markdown body is Newsreader copy under it. The masthead prints **LOG / Week {word}**, the post description as the italic kicker, and **Picks {record}** in the section nav.

## The games

Each `log.games` item is a stacked scoreboard: winner on top (bold), loser under a dotted rule, then the roast. Attach `callout` / `calloutMargin` only to the closest game and the biggest beatdown.

## Power rankings

Number, team, record, movement, one blurb. Top five numbers are gold; six through ten are muted. Movement starts in Week 2 (`▲` green, `▼` red, hyphen for no change).

## Crime blotter

Number, team in small caps, **charge** as the title, evidence in Courier Prime. Player points rounded.

## Week slate and GOTW

`log.slate` is next week's card, in schedule order. The gold check sits on the picked row. Omit `pick` for **No pick**. Add `gotw: true` on the Game of the Week row.

`log.gotw` is the display closer: both names, a initials box, and **Our pick - {pickLabel}**.

## Logos

Team records live in `src/_data/logTeams.json` (10 teams, ESPN leagueId 856379). Artwork lives in `src/assets/logos/` for when a mark is useful. The newspaper layout prints names (and GOTW initials from `abbr`). Do not hotlink ESPN CDN, Photobucket, WordPress, or Mystique URLs.

## Section nav

Anchors are `#games`, `#rankings`, `#blotter`, `#next`, `#gotw`. The next-week link label is `Week {n+1}`.
