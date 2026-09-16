# Bread and Circuses

Personal blog built with [Eleventy](https://www.11ty.dev/) (11ty). This is Phase 1: a static site ready for GitHub Pages.

The existing Blogger site is unchanged. This repo does not manage DNS for `breadandcircuses.xyz`.

## Preview locally

Requires Node.js 18 or newer (20+ recommended).

```bash
npm install
npm start
```

Open [http://localhost:8080](http://localhost:8080). Eleventy rebuilds on save.

To preview the same path prefix GitHub Pages will use:

```bash
npm run start-ghpages
```

Then open [http://localhost:8080/bread-and-circuses/](http://localhost:8080/bread-and-circuses/).

Production build (no path prefix):

```bash
npm run build
```

Output lands in `_site/`.

## Staging URL (GitHub Pages)

Until a custom domain cutover, the site is meant to live at:

**https://tastethesoup.github.io/bread-and-circuses/**

That is a project site, so the Eleventy Pages build uses `--pathprefix=/bread-and-circuses/`.

### One-time Pages setup

1. Merge this project to `main`.
2. In the GitHub repo: **Settings → Pages → Build and deployment → Source → GitHub Actions**.
3. The **Deploy to GitHub Pages** workflow runs on pushes to `main` (and can be run by hand from the Actions tab). Pull requests build the site but do not deploy.

If the workflow’s deploy job fails with a Pages permissions error, the Source setting above is the usual fix.

## Content

- Posts live in `src/posts/` as Markdown.
- The home page lists posts, newest first.
- Each post uses `src/_includes/layouts/post.njk`.
- LOG newsletter section headings (`## The games`, `## Power rankings`, and so on) render as bold, underlined text.
- Do not use em dashes in posts. Prefer periods, commas, parentheses, or a new sentence. Score lines may use a simple hyphen (`142.8 - 117.3`).

`src/posts/2026-09-16-log-week-1.md` is a sample LOG Week 1 newsletter (League of Ordinary Gentlemen). Replace the sample scores and teams with the live league notes when you have them.

An Atom feed is at `/feed.xml`.

## Optional Phase 2 (custom domain)

Not part of this phase. Do not change DNS for `breadandcircuses.xyz` yet, and do not add a `CNAME` file until you are ready to cut over.

When you do want `breadandcircuses.xyz` on GitHub Pages later:

1. Add a `CNAME` file (or set the custom domain in **Settings → Pages**) for `breadandcircuses.xyz`.
2. Point DNS at GitHub Pages when you intend to leave Blogger.
3. Remove `--pathprefix=/bread-and-circuses/` from the `build-ghpages` script so the site is built for the domain root.

## License

Private project unless otherwise noted.
