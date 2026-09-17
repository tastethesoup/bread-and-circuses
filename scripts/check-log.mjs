#!/usr/bin/env node
import { readFileSync, existsSync } from "node:fs";
import { fileURLToPath } from "node:url";
import path from "node:path";
import logTeams from "../src/_data/logTeams.json" with { type: "json" };
import { pickResult, tallyRecord } from "../log-lib.js";

const root = path.join(path.dirname(fileURLToPath(import.meta.url)), "..");
const site = path.join(root, "_site");
const failures = [];

function fail(message) {
  failures.push(message);
}

function mustExist(rel) {
  if (!existsSync(path.join(site, rel))) {
    fail(`missing ${rel}`);
  }
}

mustExist("index.html");
mustExist("feed.xml");
mustExist("posts/log-week-1/index.html");
mustExist("css/style.css");
mustExist("assets/logos/README.md");
mustExist("assets/logos/prestige-worldwide.jpg");
mustExist("assets/logos/ceedeez-nutz.svg");
mustExist("assets/logos/size-matters.svg");
mustExist("assets/logos/aints-dat-a-b-payola.svg");
mustExist("assets/logos/drake-it-to-you-make-it.svg");
mustExist("assets/logos/sutt-dog.svg");
mustExist("assets/logos/team-robottom.svg");
mustExist("assets/logos/jackmerius-tacktheritrix.png");
mustExist("assets/logos/lock-in-fn.png");

if (!existsSync(path.join(root, "docs/log-week-template.dc.html"))) {
  fail("missing docs/log-week-template.dc.html");
}

if (existsSync(path.join(site, "assets/logos/paper-lions.svg"))) {
  fail("sample Paper Lions logo should not ship");
}

const html = readFileSync(path.join(site, "posts/log-week-1/index.html"), "utf8");
const index = readFileSync(path.join(site, "index.html"), "utf8");
const feed = readFileSync(path.join(site, "feed.xml"), "utf8");
const css = readFileSync(path.join(site, "css/style.css"), "utf8");
const source = readFileSync(
  path.join(root, "src/posts/2026-09-16-log-week-1.md"),
  "utf8",
);

const teamNames = Object.values(logTeams).map((team) => team.name);
if (teamNames.length !== 10) {
  fail(`expected 10 LOG teams, got ${teamNames.length}`);
}

for (const token of [
  "log-paper",
  "log-masthead",
  "log-nav",
  'href="#games"',
  'href="#rankings"',
  'href="#blotter"',
  'href="#next"',
  'href="#gotw"',
  "log-game",
  "log-lede__display",
  "Closest game",
  "Biggest beatdown",
  "Haunted house",
  "Daamn Daniel",
  "Winning lucky counts",
  "Picks 0-0",
  "Our pick - Robottom",
  "199.80",
  "137.80",
  "194.40",
  "131.80",
  "174.60",
  "168.50",
  "168.60",
  "92.00",
  "129.50",
  "120.30",
  "Team Robottom",
  "Pimp Trick Gangsta Clique",
  "Instrument+Serif",
  "Newsreader",
  "Courier+Prime",
  ...teamNames,
]) {
  if (!html.includes(token)) {
    fail(`week 1 HTML missing ${token}`);
  }
}

if (!html.includes("fonts.googleapis.com")) {
  fail("week 1 HTML missing Google Fonts link");
}

if (!css.includes("Instrument Serif") || !css.includes("#f7f4ec")) {
  fail("newspaper CSS missing cream paper or display font");
}

for (const banned of [
  "support.js",
  "<x-dc",
  "</x-dc>",
  "<helmet",
  "matchup-card",
  "log-ticket",
  "log-hero",
  "chip--w",
  "text/x-dc",
]) {
  if (html.includes(banned)) {
    fail(`week 1 HTML still contains ${banned}`);
  }
}

if (html.includes("Paper Lions") || html.includes("Idle Hands")) {
  fail("week 1 HTML still contains sample fake teams");
}

for (const host of [
  "espncdn.com",
  "photobucket.com",
  "mystique-api.fantasy.espn.com",
  "files.wordpress.com",
]) {
  if (html.includes(host)) {
    fail(`week 1 HTML hotlinks ${host}`);
  }
}

if (!index.includes("/posts/log-week-1/") || !index.includes("LOG Week 1")) {
  fail("home page does not list LOG Week 1");
}

if (!feed.includes("LOG Week 1") || !feed.includes("feed")) {
  fail("Atom feed missing LOG Week 1");
}

if (
  source.includes("\u2014") ||
  source.includes("&mdash;") ||
  html.includes("\u2014") ||
  html.includes("&mdash;")
) {
  fail("published LOG copy contains an em dash");
}

if (!html.includes("Game of the Week") || !html.includes("id=\"gotw\"")) {
  fail("GOTW section missing");
}

if (!source.includes("gotw: true") || !html.includes("taking Robottom in this game of the week matchup")) {
  fail("Week 2 GOTW should be Robottom vs Clique from the sent LOG");
}

const games = [
  {
    home: "Team Robottom",
    away: "AINTS dat a B** Payola",
    homeScore: 199.8,
    awayScore: 137.8,
  },
  {
    home: "Size Matters",
    away: "-Sutt-Dog -",
    homeScore: 194.4,
    awayScore: 131.8,
  },
  {
    home: "Lock in fn",
    away: "CeeDeez Nutz",
    homeScore: 174.6,
    awayScore: 168.5,
  },
  {
    home: "Pimp Trick Gangsta Clique",
    away: "Prestige Worldwide",
    homeScore: 168.6,
    awayScore: 92.0,
  },
  {
    home: "Drake It To You Make It",
    away: "Jackmerius Tacktheritrix",
    homeScore: 129.5,
    awayScore: 120.3,
  },
];

if (pickResult(games[0]) !== "nopick") fail("expected NO PICK when pick omitted");
const record = tallyRecord(games);
if (record.label !== "0-0") fail(`expected pick record 0-0 with no picks, got ${record.label}`);
if (!source.includes('home: "Team Robottom"') || !source.includes("199.80")) {
  fail("source post missing Robottom score from the Week 1 LOG");
}
if (!source.includes('away: "Pimp Trick Gangsta Clique"') || !source.includes("gotw: true")) {
  fail("source post missing Week 2 GOTW Robottom vs Clique");
}

if (failures.length) {
  console.error(failures.map((item) => `x ${item}`).join("\n"));
  process.exit(1);
}

console.log("LOG newspaper checks passed.");
