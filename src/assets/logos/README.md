# LOG team logos

League of Ordinary Gentlemen marks for ESPN league **856379** (roster via Chief Of Staff, 2026-09-16). Files in this folder are cached copies of the league logos. Templates point at these local paths only. They do **not** hotlink ESPN CDN, WordPress, Photobucket, or Mystique URLs (those break without warning).

## Files

Put one image per team in this folder. The filename should match the team slug in `src/_data/logTeams.json`.

```
src/assets/logos/prestige-worldwide.jpg
```

SVG, PNG, or JPEG is fine. Square, about 128px or larger. Keep file size small; these render at ~40px on phones.

Then set the path on the team record:

```json
"prestige-worldwide": {
  "name": "Prestige Worldwide",
  "owner": "Sean Lockovich",
  "abbr": "PW",
  "color": "#2a6b73",
  "logo": "/assets/logos/prestige-worldwide.jpg"
}
```

If a download fails, omit `logo` so the card uses the initials avatar.

## Cached vs fallback (league 856379)

Tried once from the provided logo map. Cached files are the ones that downloaded as real images.

| Team | Owner | Result | Local file / notes |
| --- | --- | --- | --- |
| Prestige Worldwide | Sean Lockovich | Cached | `prestige-worldwide.jpg` (WordPress JPEG, resized to 256px for phone cards) |
| CeeDeez Nutz | Eric Bunn | Cached | `ceedeez-nutz.svg` (espncdn logo pack) |
| Size Matters | Nick Harper | Cached | `size-matters.svg` (espncdn Marvel Hulk) |
| AINTS dat a B** Payola | Micah Goins | Cached | `aints-dat-a-b-payola.svg` (ESPN default logo 19) |
| Drake It To You Make It | James D | Cached | `drake-it-to-you-make-it.svg` (espncdn Disney pack) |
| -Sutt-Dog - | Chris Sutton | Cached | `sutt-dog.svg` (espncdn Crazy Helmets pack) |
| Lock in fn | Reggie B | Fallback (initials `LI`) | Mystique API returned 401 (`Credentials are missing`). Source: `https://mystique-api.fantasy.espn.com/apis/v1/domains/lm/images/d80e7c60-9e47-11f0-b1c3-bf61c28fbeb9` |
| Team Robottom | Chad Robottom | Cached | `team-robottom.svg` (ESPN default logo 6) |
| Pimp Trick Gangsta Clique | Bernard Ford | Fallback (initials `PT`) | Photobucket returned a watermarked "Groups by photobucket" overlay, not a clean logo. Do not hotlink. Source: `https://i925.photobucket.com/albums/ad94/tjondo/Presentation1.jpg` |
| Jackmerius Tacktheritrix | Brandon Sims | Cached | `jackmerius-tacktheritrix.png` (espncdn Guardians shield) |

## Fallback

If the file is missing, the path is wrong, or the image fails to load, the card shows a colored initials avatar (`PW`, `SM`, and so on). The layout does not depend on the image.

## Using a league logo from ESPN

If you export a team logo from your own ESPN league (or a manager-uploaded image you have the right to use), drop it here and point `logo` at that file. Do not paste `espncdn.com`, `photobucket.com`, `wordpress.com`, or `mystique-api` URLs into templates.
