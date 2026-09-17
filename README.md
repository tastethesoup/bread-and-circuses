# Bread and Circuses

Personal blog built with [Eleventy](https://www.11ty.dev/) (11ty). Production is GitHub Pages at the custom domain **https://breadandcircuses.xyz/**.

The existing Blogger site is unchanged until DNS is cut over. **This repo does not change Squarespace DNS.** A human or agent must set the records below later. Do not invent or commit secrets (registrar logins, API tokens, or verification codes).

## Preview locally

Requires Node.js 18 or newer (20+ recommended).

```bash
npm install
npm start
```

Open [http://localhost:8080](http://localhost:8080). That root preview matches production on the custom domain. Eleventy rebuilds on save.

To preview the old GitHub Pages *project site* path (`/bread-and-circuses/`), if you need it:

```bash
npm run start-ghpages
```

Then open [http://localhost:8080/bread-and-circuses/](http://localhost:8080/bread-and-circuses/).

Production build (custom domain at `/`, no path prefix):

```bash
npm run build
```

Output lands in `_site/`, including a `CNAME` file for `breadandcircuses.xyz`.

Optional project-pages build (same path prefix as `start-ghpages`):

```bash
npm run build-ghpages
```

## Production URL

**https://breadandcircuses.xyz/**

`www.breadandcircuses.xyz` should redirect to the apex once both DNS records and the GitHub custom-domain setting are in place.

Until then, the project-pages staging URL is:

**https://tastethesoup.github.io/bread-and-circuses/**

After the custom domain is configured on the GitHub Pages site, that `github.io` URL may keep working as a redirect to `https://breadandcircuses.xyz/`.

Production deploys with `npm run build` (root `/`). Do not use `--pathprefix=/bread-and-circuses/` for production; that prefix is only for the optional local preview / `build-ghpages` scripts.

### One-time Pages + custom domain setup

1. Merge this project to `main`.
2. In the GitHub repo: **Settings → Pages → Build and deployment → Source → GitHub Actions**.
3. In **Settings → Pages → Custom domain**, enter `breadandcircuses.xyz` and save. (Publishing is GitHub Actions, so a `CNAME` in the built site does not apply the domain by itself. GitHub still needs this setting.)
4. After DNS below is live and GitHub's DNS check succeeds, select **Enforce HTTPS**. It can take up to 24 hours to become available.
5. The **Deploy to GitHub Pages** workflow runs on pushes to `main` (and can be run by hand from the Actions tab). Pull requests build the site but do not deploy.

If the workflow’s deploy job fails with a Pages permissions error, the Source setting above is the usual fix.

## Content

- Posts live in `src/posts/` as Markdown.
- The home page lists posts, newest first.
- Each post uses `src/_includes/layouts/post.njk`.
- LOG newsletter section headings (`## The games`, `## Power rankings`, and so on) render as bold, underlined text.
- Do not use em dashes in posts. Prefer periods, commas, parentheses, or a new sentence. Score lines may use a simple hyphen (`142.8 - 117.3`).

`src/posts/2026-09-16-log-week-1.md` is a sample LOG Week 1 newsletter for the 10-team League of Ordinary Gentlemen (ESPN leagueId 856379). It is laid out for phones: stacked matchup cards, sticky section nav, blotter tickets, a pull quote, and pick/result chips. Scores and roasts are illustrative. Team names, owners, and logos come from the live roster map.

Author notes for weekly LOG posts (front matter, pull quotes, logos, chips) are in [docs/log.md](docs/log.md). Cached logos live in `src/assets/logos/` with a short README there (Pimp Trick Gangsta Clique still falls back to initials).

An Atom feed is at `/feed.xml`.

## Custom domain DNS (Squarespace) — set later, not in this PR

DNS for `breadandcircuses.xyz` is at [Squarespace Domains](https://account.squarespace.com/domains). **This pull request does not edit those records.** Keep Blogger on the domain until you are ready to cut over.

IPs and CNAME targets below match [GitHub Pages custom domain docs](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site) (A `185.199.108.153` through `185.199.111.153`, optional AAAA `2606:50c0:8000::153` through `2606:50c0:8003::153`, www CNAME to `USERNAME.github.io`).

### Where to add records

1. Open the Squarespace **domains dashboard**.
2. Click **breadandcircuses.xyz**.
3. Click **DNS**.
4. Remove existing **apex** (`@`) A / AAAA / ALIAS records and any **www** CNAME that still point at Squarespace parking, Squarespace hosting, Blogger, or another host. Leave unrelated email MX/TXT records unless they actually conflict.
5. Add the records in the table you choose. Squarespace fields are **Type**, **Name**, and **Data**. Leave **TTL** at the default (4 hours) unless you have a reason to change it. Do not put a trailing path on CNAME/ALIAS data. Use `tastethesoup.github.io`, not `tastethesoup.github.io/bread-and-circuses`.

Squarespace will not save an A or AAAA record and an ALIAS on the same **Name**. Pick **either** the A records **or** the ALIAS for `@`, not both.

### Apex A records (recommended) + www CNAME

Use this unless you specifically want an ALIAS at the apex.

| Type | Name | Data |
| --- | --- | --- |
| A | `@` | `185.199.108.153` |
| A | `@` | `185.199.109.153` |
| A | `@` | `185.199.110.153` |
| A | `@` | `185.199.111.153` |
| CNAME | `www` | `tastethesoup.github.io` |

### Apex ALIAS alternative + www CNAME

GitHub also accepts an ALIAS (or ANAME) at the apex pointing at the Pages default host. Squarespace supports ALIAS. Use this **instead of** the four A records above, not in addition to them.

| Type | Name | Data |
| --- | --- | --- |
| ALIAS | `@` | `tastethesoup.github.io` |
| CNAME | `www` | `tastethesoup.github.io` |

### Optional IPv6 (AAAA)

Add these only with the A-record setup (not with ALIAS on `@`). Squarespace rejects compressed IPv6 (`::`). Use the fully expanded addresses:

| Type | Name | Data |
| --- | --- | --- |
| AAAA | `@` | `2606:50c0:8000:0000:0000:0000:0000:0153` |
| AAAA | `@` | `2606:50c0:8001:0000:0000:0000:0000:0153` |
| AAAA | `@` | `2606:50c0:8002:0000:0000:0000:0000:0153` |
| AAAA | `@` | `2606:50c0:8003:0000:0000:0000:0000:0153` |

### Check DNS after it is changed

```bash
dig breadandcircuses.xyz +noall +answer -t A
dig www.breadandcircuses.xyz +nostats +nocomments +nocmd
```

Apex A answers should be the four `185.199.10x.153` addresses. The www name should CNAME to `tastethesoup.github.io`. Propagation can take 24-48 hours.

## License

Private project unless otherwise noted.
