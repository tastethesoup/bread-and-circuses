#!/usr/bin/env node
import { readFileSync, existsSync } from "node:fs";
import { fileURLToPath } from "node:url";
import path from "node:path";
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
mustExist("assets/logos/paper-lions.svg");
mustExist("assets/logos/README.md");

const html = readFileSync(path.join(site, "posts/log-week-1/index.html"), "utf8");
const index = readFileSync(path.join(site, "index.html"), "utf8");
const feed = readFileSync(path.join(site, "feed.xml"), "utf8");
const source = readFileSync(
  path.join(root, "src/posts/2026-09-16-log-week-1.md"),
  "utf8",
);

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
  "team-avatar",
  "Paper Lions",
]) {
  if (!html.includes(token)) {
    fail(`week 1 HTML missing ${token}`);
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
  { home: "Paper Lions", away: "Idle Hands", homeScore: 142.8, awayScore: 117.3, pick: "Paper Lions" },
  { home: "Sunday Gentlemen", away: "The Commons", homeScore: 131.6, awayScore: 128.9, pick: "The Commons" },
  { home: "Bread Line", away: "Quiet Luxury", homeScore: 119.4, awayScore: 101.2, pick: "Bread Line" },
  { home: "Circus Maximus", away: "False Nine", homeScore: 156.1, awayScore: 110.8, pick: "Circus Maximus" },
  { home: "Second Breakfast", away: "Harmless Fun", homeScore: 124.0, awayScore: 122.7 },
  { home: "The Backbench", away: "Municipal Waste", homeScore: 108.5, awayScore: 97.6, pick: "Municipal Waste" },
];

if (pickResult(games[0]) !== "hit") fail("expected HIT on Paper Lions");
if (pickResult(games[1]) !== "miss") fail("expected MISS on Commons pick");
if (pickResult(games[4]) !== "nopick") fail("expected NO PICK on Second Breakfast");
const record = tallyRecord(games);
if (record.label !== "3-2") fail(`expected pick record 3-2, got ${record.label}`);
if (!html.includes("Picks 3-2")) fail("hero strip missing computed Picks 3-2 record");

if (failures.length) {
  console.error(failures.map((item) => `x ${item}`).join("\n"));
  process.exit(1);
}

console.log("LOG layout checks passed.");
