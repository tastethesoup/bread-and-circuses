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

  eleventyConfig.addFilter("shortDate", (dateObj) => formatShortDate(dateObj));
  eleventyConfig.addFilter("weekWord", (n) => weekWord(n));
  eleventyConfig.addFilter("logScore", (value) => formatScore(value));
  eleventyConfig.addFilter("logMove", (move) => movementTone(move));

  eleventyConfig.addFilter("htmlDateString", (dateObj) => {
    return new Date(dateObj).toISOString().slice(0, 10);
  });

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
