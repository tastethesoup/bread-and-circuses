import { HtmlBasePlugin } from "@11ty/eleventy";
import { feedPlugin } from "@11ty/eleventy-plugin-rss";
import site from "./src/_data/site.json" with { type: "json" };

/** @param {import("@11ty/eleventy").UserConfig} eleventyConfig */
export default function (eleventyConfig) {
  eleventyConfig.addPassthroughCopy({
    "src/css": "css",
    "src/.nojekyll": ".nojekyll",
    "src/CNAME": "CNAME",
  });
  eleventyConfig.addWatchTarget("src/css/");

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

  eleventyConfig.addFilter("htmlDateString", (dateObj) => {
    return new Date(dateObj).toISOString().slice(0, 10);
  });
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
