import { existsSync } from "node:fs";
import path from "node:path";
import logTeams from "./src/_data/logTeams.json" with { type: "json" };

export const CHIP_KINDS = {
  pick: { label: "PICK", className: "chip--pick" },
  gotw: { label: "GOTW", className: "chip--gotw" },
  w: { label: "W", className: "chip--w" },
  l: { label: "L", className: "chip--l" },
  hit: { label: "HIT", className: "chip--hit" },
  miss: { label: "MISS", className: "chip--miss" },
  nopick: { label: "NO PICK", className: "chip--nopick" },
};

export function slugifyTeam(name) {
  return String(name || "")
    .trim()
    .toLowerCase()
    .replace(/&/g, "and")
    .replace(/[^a-z0-9]+/g, "-")
    .replace(/^-+|-+$/g, "");
}

export function teamInitials(name) {
  const cleaned = String(name || "")
    .trim()
    .replace(/^(the)\s+/i, "");
  const words = cleaned.split(/\s+/).filter(Boolean);
  if (words.length === 0) {
    return "?";
  }
  if (words.length === 1) {
    return words[0].slice(0, 2).toUpperCase();
  }
  return (words[0][0] + words[1][0]).toUpperCase();
}

function logoOnDisk(logoPath) {
  if (!logoPath) {
    return null;
  }
  const rel = String(logoPath).replace(/^\//, "");
  const diskPath = path.join("src", rel);
  return existsSync(diskPath) ? `/${rel}` : null;
}

export function resolveTeam(ref, teams = logTeams) {
  if (ref && typeof ref === "object") {
    const name = ref.name || "Unknown";
    const slug = ref.slug || slugifyTeam(name);
    return {
      slug,
      name,
      abbr: ref.abbr || teamInitials(name),
      logo: logoOnDisk(ref.logo),
      color: ref.color || "#5e574e",
    };
  }

  const raw = String(ref || "").trim();
  if (!raw) {
    return {
      slug: "unknown",
      name: "Unknown",
      abbr: "?",
      logo: null,
      color: "#5e574e",
    };
  }

  const slug = slugifyTeam(raw);
  const direct = teams[slug];
  if (direct) {
    return {
      slug,
      name: direct.name,
      abbr: direct.abbr || teamInitials(direct.name),
      logo: logoOnDisk(direct.logo),
      color: direct.color || "#5e574e",
    };
  }

  for (const [id, team] of Object.entries(teams)) {
    if (
      slugifyTeam(team.name) === slug ||
      String(team.name).toLowerCase() === raw.toLowerCase()
    ) {
      return {
        slug: id,
        name: team.name,
        abbr: team.abbr || teamInitials(team.name),
        logo: logoOnDisk(team.logo),
        color: team.color || "#5e574e",
      };
    }
  }

  return {
    slug,
    name: raw,
    abbr: teamInitials(raw),
    logo: null,
    color: "#5e574e",
  };
}

export function normalizeChip(kind) {
  const key = String(kind || "")
    .trim()
    .toLowerCase()
    .replace(/[\s_-]+/g, "");

  if (!key) {
    return null;
  }
  if (key === "none" || key === "np") {
    return "nopick";
  }
  if (key === "gameoftheweek" || key === "gameofweek") {
    return "gotw";
  }
  if (key === "win") {
    return "w";
  }
  if (key === "loss") {
    return "l";
  }
  return CHIP_KINDS[key] ? key : null;
}

export function chipMeta(kind) {
  const key = normalizeChip(kind);
  return key ? { key, ...CHIP_KINDS[key] } : null;
}

export function winnerSide(game) {
  const homeScore = Number(game?.homeScore);
  const awayScore = Number(game?.awayScore);
  if (Number.isNaN(homeScore) || Number.isNaN(awayScore)) {
    return null;
  }
  if (homeScore === awayScore) {
    return "tie";
  }
  return homeScore > awayScore ? "home" : "away";
}

export function pickResult(game, teams = logTeams) {
  if (!game?.pick) {
    return "nopick";
  }
  const winner = winnerSide(game);
  if (!winner || winner === "tie") {
    return "nopick";
  }
  const pick = resolveTeam(game.pick, teams);
  const champ =
    winner === "home"
      ? resolveTeam(game.home, teams)
      : resolveTeam(game.away, teams);
  return pick.slug === champ.slug ? "hit" : "miss";
}

export function tallyRecord(games, teams = logTeams) {
  let hits = 0;
  let misses = 0;
  for (const game of games || []) {
    const result = pickResult(game, teams);
    if (result === "hit") {
      hits += 1;
    }
    if (result === "miss") {
      misses += 1;
    }
  }
  return { hits, misses, label: `${hits}-${misses}` };
}

export function escapeHtml(value) {
  return String(value ?? "")
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;");
}

export function renderChip(kind) {
  const meta = chipMeta(kind);
  if (!meta) {
    return "";
  }
  return `<span class="log-chip ${meta.className}">${escapeHtml(meta.label)}</span>`;
}

export function renderPullQuote(text) {
  const body = String(text || "").trim();
  if (!body) {
    return "";
  }
  return `<blockquote class="pull-quote">${escapeHtml(body)}</blockquote>`;
}
