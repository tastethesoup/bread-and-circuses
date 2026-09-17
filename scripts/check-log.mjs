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

if (existsSync(path.join(site, "assets/logos/paper-lions.svg"))) {
  fail("sample Paper Lions logo should not ship");
}

const html = readFileSync(path.join(site, "posts/log-week-1/index.html"), "utf8");
const index = readFileSync(path.join(site, "index.html"), "utf8");
const feed = readFileSync(path.join(site, "feed.xml"), "utf8");
const source = readFileSync(
  path.join(root, "src/posts/2026-09-16-log-week-1.md"),
  "utf8",
);

const teamNames = Object.values(logTeams).map((team) => team.name);
if (teamNames.length !== 10) {
  fail(`expected 10 LOG teams, got ${teamNames.length}`);
}

for (const token of [
  "log-nav",
  'href="#games"',
  'href="#rankings"',
  'href="#blotter"',
  'href="#next-week"',
  'href="#gotw"',
  "matchup-card",
  "log-ticket",
  "pull-quote",
  "log-hero",
  "chip--hit",
  "chip--miss",
  "chip--nopick",
  "chip--pick",
  "chip--gotw",
  "chip--w",
  "chip--l",
  "matchup-team__scoreline",
  "team-avatar",
  ...teamNames,
]) {
  if (!html.includes(token)) {
    fail(`week 1 HTML missing ${token}`);
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

if (source.includes("\u2014") || source.includes("&mdash;")) {
  fail("sample post contains an em dash");
}

const games = [
  {
    home: "Prestige Worldwide",
    away: "CeeDeez Nutz",
    homeScore: 142.8,
    awayScore: 117.3,
    pick: "Prestige Worldwide",
  },
  {
    home: "Size Matters",
    away: "AINTS dat a B** Payola",
    homeScore: 131.6,
    awayScore: 128.9,
    pick: "AINTS dat a B** Payola",
  },
  {
    home: "Drake It To You Make It",
    away: "-Sutt-Dog -",
    homeScore: 156.1,
    awayScore: 110.8,
    pick: "Drake It To You Make It",
  },
  {
    home: "Lock in fn",
    away: "Team Robottom",
    homeScore: 119.4,
    awayScore: 101.2,
    pick: "Lock in fn",
  },
  {
    home: "Pimp Trick Gangsta Clique",
    away: "Jackmerius Tacktheritrix",
    homeScore: 124.0,
    awayScore: 122.7,
    pick: "Jackmerius Tacktheritrix",
  },
];

if (pickResult(games[0]) !== "hit") fail("expected HIT on Prestige Worldwide");
if (pickResult(games[1]) !== "miss") fail("expected MISS on AINTS pick");
if (pickResult(games[4]) !== "miss") fail("expected MISS on Jackmerius pick");
const record = tallyRecord(games);
if (record.label !== "3-2") fail(`expected pick record 3-2, got ${record.label}`);
if (!html.includes("Picks 3-2")) fail("hero strip missing computed Picks 3-2 record");

if (failures.length) {
  console.error(failures.map((item) => `x ${item}`).join("\n"));
  process.exit(1);
}

console.log("LOG layout checks passed.");
