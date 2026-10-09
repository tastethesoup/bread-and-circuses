import { existsSync } from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { HtmlBasePlugin } from "@11ty/eleventy";
import { feedPlugin } from "@11ty/eleventy-plugin-rss";
import site from "./src/_data/site.json" with { type: "json" };
import {
  chipMeta,
  formatScore,
  formatShortDate,
  movementTone,
  pickResult,
  renderChip,
  renderPullQuote,
  resolveTeam,
  tallyRecord,
  weekWord,
  winnerSide,
} from "./log-lib.js";

const rootDir = path.dirname(fileURLToPath(import.meta.url));

function siteUrl(value) {
  const origin = String(site.url || "").replace(/\/$/, "");
  const raw = String(value ?? "").trim();
  if (!raw) {
    return origin;
  }
  if (/^https?:\/\//i.test(raw)) {
    return raw;
  }
  return `${origin}${raw.startsWith("/") ? raw : `/${raw}`}`;
}

function logOgPath(week) {
  if (week == null || week === "") {
    return "";
  }
  const filename = `log-week-${week}.png`;
  if (!existsSync(path.join(rootDir, "src", "assets", "og", filename))) {
    return "";
  }
  return `/assets/og/${filename}`;
}

/** @param {import("@11ty/eleventy").UserConfig} eleventyConfig */
export default function (eleventyConfig) {
  eleventyConfig.ignores.add("src/assets/**/*.md");
  eleventyConfig.addPassthroughCopy({
    "src/css": "css",
    "src/assets": "assets",
    "src/.nojekyll": ".nojekyll",
    "src/CNAME": "CNAME",
  });
  eleventyConfig.addWatchTarget("src/css/");
  eleventyConfig.addWatchTarget("src/assets/");

  eleventyConfig.addPlugin(HtmlBasePlugin);

  eleventyConfig.addPlugin(feedPlugin, {
    type: "atom",
    outputPath: "/feed.xml",
    collection: {
      name: "posts",
      limit: 20,
    },
    metadata: {
      language: site.language,
      title: site.title,
      subtitle: site.description,
      // Production is the custom domain at root. --pathprefix is only for
      // optional github.io project-pages previews (npm run start-ghpages).
      base: site.url,
      author: {
        name: site.author.name,
      },
    },
  });

  eleventyConfig.addFilter("readableDate", (dateObj) => {
    return new Intl.DateTimeFormat("en-US", {
      year: "numeric",
      month: "long",
      day: "numeric",
      timeZone: "UTC",
    }).format(dateObj);
  });

  // Credit & Fed Desk episodes (any post with `podcast:` front matter), newest first.
  eleventyConfig.addCollection("desk", (api) =>
    api.getFilteredByTag("posts").filter((p) => p.data.podcast).reverse(),
  );

  // LOG weeks (any post with `log:` front matter), newest first.
  eleventyConfig.addCollection("logWeeks", (api) =>
    api.getFilteredByTag("posts").filter((p) => p.data.log).reverse(),
  );

  // "Thursday, October 8, 2026" for the home masthead.
  eleventyConfig.addFilter("longDate", (dateObj) =>
    new Intl.DateTimeFormat("en-US", {
      weekday: "long",
      year: "numeric",
      month: "long",
      day: "numeric",
      timeZone: "UTC",
    }).format(dateObj),
  );

  eleventyConfig.addFilter("shortDate", (dateObj) => formatShortDate(dateObj));
  eleventyConfig.addFilter("weekWord", (n) => weekWord(n));
  eleventyConfig.addFilter("logScore", (value) => formatScore(value));
  eleventyConfig.addFilter("logMove", (move) => movementTone(move));

  eleventyConfig.addFilter("htmlDateString", (dateObj) => {
    return new Date(dateObj).toISOString().slice(0, 10);
  });

  eleventyConfig.addFilter("siteUrl", (value) => siteUrl(value));
  eleventyConfig.addFilter("logOgPath", (week) => logOgPath(week));

  eleventyConfig.addFilter("logTeam", (ref) => resolveTeam(ref));
  eleventyConfig.addFilter("logChip", (kind) => chipMeta(kind));
  eleventyConfig.addFilter("logWinner", (game) => winnerSide(game));
  eleventyConfig.addFilter("logPickResult", (game) => pickResult(game));
  eleventyConfig.addFilter("logRecord", (games) => tallyRecord(games));

  eleventyConfig.addShortcode("logChip", (kind) => renderChip(kind));
  eleventyConfig.addPairedShortcode("pullQuote", (content) =>
    renderPullQuote(content),
  );
}

export const config = {
  templateFormats: ["md", "njk", "html"],
  markdownTemplateEngine: "njk",
  htmlTemplateEngine: "njk",
  dir: {
    input: "src",
    includes: "_includes",
    data: "_data",
    output: "_site",
  },
};
