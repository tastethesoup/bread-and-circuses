# LOG team logos

Original marks drawn for the League of Ordinary Gentlemen on this site. They are **not** ESPN, NFL, or club trademarks, and the layout does not hotlink ESPN CDN URLs (those break without warning).

## Files

Put one image per team in this folder. The filename should match the team slug in `src/_data/logTeams.json`.

```
src/assets/logos/paper-lions.svg
```

SVG or PNG is fine. Square, about 128px or larger. Keep file size small; these render at ~40px on phones.

Then set the path on the team record:

```json
"paper-lions": {
  "name": "Paper Lions",
  "abbr": "PL",
  "color": "#c45c26",
  "logo": "/assets/logos/paper-lions.svg"
}
```

## Fallback

If the file is missing, the path is wrong, or the image fails to load, the card shows a colored initials avatar (`PL`, `SG`, and so on). The layout does not depend on the image.

## Using a league logo from ESPN

If you export a team logo from your own ESPN league (or a manager-uploaded image you have the right to use), drop it here and point `logo` at that file. Do not paste `espncdn.com` URLs into templates.

These bundled SVGs are original site artwork for Bread and Circuses.
