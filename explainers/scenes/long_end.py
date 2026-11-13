"""The Long End Breaks Loose. One element per storyboard row."""

from __future__ import annotations

import math
from pathlib import Path

from explainers.bb.engine import (
    AMBER,
    CHALK,
    CYAN,
    Board,
    load_storyboard_times,
)

STORY = (
    Path(__file__).resolve().parents[1]
    / "storyboards"
    / "long-end-explainer-storyboard-v2.md"
)

AX0, AX1, AY = 100, 1360, 490
P10, P30 = 620, 1140


def build(duration: float) -> Board:
    b = Board(duration)
    _section1(b)
    _section2(b)
    _section3(b)
    _section4(b)
    _section5(b)
    _section6(b, duration)
    b.t_occupied = [(0.0, duration)]
    b.finalize(load_storyboard_times(STORY))
    return b


def _section1(b: Board):
    z = "s1"
    b.at("1.01", 1.6)
    b.line("axis", AX0, AY, AX1, AY, color=CHALK, zone=z, lw=3.4)
    b.text("axl", "maturity →", AX1 - 150, AY + 16, color=CHALK, size=20, max_w=180, zone=z)

    b.at("1.02", 3.9)
    b.line("stub", AX0, AY, AX0, AY - 36, color=CHALK, zone=z)
    b.text("overnight", "Overnight rate (Fed sets)", AX0 - 10, AY - 78, color=CHALK, size=22, max_w=280, zone=z)

    b.at("1.03", 8.2)
    b.dot("p10", P10, AY, color=CHALK, r=7, zone=z)
    b.text("t10", "10-year", P10 - 40, AY + 18, color=CHALK, size=22, max_w=140, zone=z)
    b.at("1.04", 9.3)
    b.dot("p30", P30, AY, color=CHALK, r=7, zone=z)
    b.text("t30", "30-year", P30 - 40, AY + 18, color=CHALK, size=22, max_w=140, zone=z)
    b.at("1.05", 10.9)
    b.box("mtg", P10 - 70, AY + 70, 160, 48, "Mortgage", color=CHALK, size=22, zone=z)

    b.at("1.06", 12.8)
    b.poly(
        "mkt",
        [
            (P10 - 90, AY + 130),
            (P10 - 90, AY - 70),
            (P30 + 80, AY - 70),
            (P30 + 80, AY + 40),
        ],
        color=CHALK,
        zone=z,
    )
    b.text(
        "mktL",
        "set by buyers and sellers",
        P10 + 20,
        AY - 128,
        color=CHALK,
        size=22,
        max_w=420,
        zone=z,
    )

    b.at("1.07", 21.5)
    b.text("week", "Week of Oct 5, 2026", 480, 150, color=CHALK, size=28, max_w=420, zone=z)

    b.at("1.08", 33.9)
    b.text("odds", "Oct hike odds: ~70% → ~25%", 48, 250, color=CHALK, size=24, max_w=420, zone=z)
    b.arrow("oddsA", 80, 300, 80, 360, color=CHALK, zone=z)

    b.at("1.09", 41.0)
    b.arrow("y10", P10, AY - 24, P10, AY - 130, color=CHALK, zone=z)
    b.text("y10L", "5.364% intraday (Wed Oct 7)", P10 - 80, AY - 210, color=CHALK, size=20, max_w=280, zone=z)
    b.at("1.10", 45.1)
    b.append("y10L", ", 24-yr high")
    b.at("1.11", 46.9)
    b.text("y30L", "~5.7%", P30 - 20, AY - 150, color=CHALK, size=22, max_w=200, zone=z)
    b.at("1.12", 49.7)
    b.append("y30L", ", not seen since ~2002")

    b.at("1.13", 54.2)
    b.text("bes", "Bessent:", 48, 48, color=CHALK, size=24, max_w=640, zone=z)
    b.at("1.14", 56.4)
    b.append("bes", " 'I can't control the bond market.'")

    b.at("1.15", 63.3)
    for i in range(4):
        y = 930 + i * 32
        b.text(f"f{i}", f"{i + 1}.", 48, y, color=CHALK, size=22, max_w=40, zone=z, opacity=0.4)
        line = b.line(f"fl{i}", 96, y + 20, 640, y + 20, color=CHALK, zone=z, lw=2.0, dur=0.3)
        line.base_opacity = 0.4


def _section2(b: Board):
    bar, tags, path, note = "bar", "tags", "path", "s2note"
    b.at("2.01", 71.9)
    b.erase_all(thumbs=True)
    bx, by, bw, bh = 760, 310, 180, 460
    b.rect("barout", bx, by, bw, bh, color=CHALK, zone=bar, lw=3.2)
    b.text("barL", "10-year yield", bx + 16, by + 8, color=CHALK, size=20, max_w=bw - 24, zone=bar)

    b.at("2.02", 75.9)
    bot_y = by + 190
    b.rect("botb", bx + 8, bot_y, bw - 16, by + bh - bot_y - 8, color=CYAN, zone=bar, fill=True, grow="up")
    b.text(
        "botL",
        "Expected average short rate",
        bx + 16,
        bot_y + 40,
        color=CHALK,
        size=18,
        max_w=bw - 32,
        zone=bar,
    )
    b.at("2.03", 79.2)
    b.rect("topb", bx + 8, by + 36, bw - 16, 146, color=AMBER, zone=bar, fill=True, grow="up")
    b.text("topL", "Term premium", bx + 16, by + 48, color=CHALK, size=20, max_w=bw - 32, zone=bar)

    b.at("2.04", 86.3)
    b.text("planA", "Plan A: buy 10-year note", 40, 300, color=CHALK, size=24, max_w=560, zone=tags)
    b.at("2.05", 88.1)
    b.text(
        "planB",
        "Plan B: lend overnight, roll daily for 10 yrs",
        40,
        348,
        color=CHALK,
        size=22,
        max_w=620,
        zone=tags,
    )
    b.at("2.06", 93.9)
    b.text("approx", "≈", 300, 400, color=CHALK, size=40, max_w=80, zone=tags)
    b.at("2.07", 95.8)
    b.arrow(
        "avg",
        520,
        430,
        750,
        bot_y + 40,
        "≈ average expected overnight rate",
        color=CYAN,
        size=18,
        zone=tags,
        tdy=-30,
        max_w=280,
    )

    b.at("2.08", 104.1)
    b.poly("fpath", [(48, 980), (190, 840), (520, 840)], color=CYAN, zone=path, lw=3.4)
    b.text("fpathL", "whole path, not next meeting", 48, 990, color=CYAN, size=20, max_w=480, zone=path)
    b.text("yrs", "next 10 yrs", 360, 1008, color=CHALK, size=16, max_w=180, zone=path)

    b.at("2.09", 108.2)
    b.text("inf", "inflation", 40, 500, color=CYAN, size=24, max_w=240, zone=tags)
    b.at("2.10", 111.2)
    b.text("gro", "growth", 200, 500, color=CYAN, size=24, max_w=200, zone=tags)
    b.at("2.11", 111.7)
    b.text("fedp", "Fed path / how long", 360, 500, color=CYAN, size=24, max_w=320, zone=tags)

    b.at("2.12", 118.9)
    b.highlight("topb", until=257.9)
    b.at("2.13", 122.8)
    b.text("rp", "rates ↑ → price ↓", bx + 16, by + 150, color=CHALK, size=16, max_w=bw - 28, zone=note)
    b.at("2.14", 127.7)
    b.text("extra", "extra pay for holding long", 1000, 340, color=AMBER, size=22, max_w=420, zone=tags)
    b.at("2.15", 138.1)
    b.text("borr", "heavy borrowing", 1000, 400, color=AMBER, size=22, max_w=400, zone=tags)
    b.at("2.16", 139.5)
    b.text("defic", "big deficits", 1000, 448, color=AMBER, size=22, max_w=400, zone=tags)
    b.at("2.17", 140.9)
    b.text("unc", "inflation / policy uncertainty", 1000, 496, color=AMBER, size=22, max_w=440, zone=tags)
    b.at("2.18", 142.9)
    b.text("few", "fewer dependable buyers", 1000, 560, color=AMBER, size=22, max_w=420, zone=tags)
    b.at("2.19", 146.9)
    b.text("model", "model-estimated", 1000, 250, color=CHALK, size=20, max_w=400, zone=note)
    b.at("2.20", 151.2)
    # Chalk, not amber: an amber glyph disappears on the amber fill.
    b.text("qq", "?", bx + bw / 2, by + 88, color=CHALK, size=40, max_w=50, zone=bar, ax="center")
    b.append("model", "; no number given")

    b.at("2.21", 153.3)
    b.erase(zone=tags)
    b.erase(ids=["model"])
    b.text("bcol", "bottom block", 48, 250, color=CYAN, size=26, max_w=400, zone="col")
    b.text("tcol", "top block", 1080, 250, color=AMBER, size=26, max_w=360, zone="col")

    b.at("2.22", 154.7)
    b.text("trayH", "Fed minutes (Oct 7)", 48, 36, color=CHALK, size=24, max_w=500, zone="tray")
    b.at("2.23", 161.4)
    b.text("hike", "Expected hikes", 48, 84, color=CHALK, size=24, max_w=320, zone="tray")
    b.at("2.24", 162.8)
    b.text("ai", "AI build-out", 380, 84, color=CHALK, size=24, max_w=280, zone="tray")
    b.at("2.25", 163.9)
    b.text("sg", "Solid growth", 680, 84, color=CHALK, size=24, max_w=280, zone="tray")
    b.at("2.26", 168.2)
    b.text("buy", "Buyback uncertainty", 980, 84, color=CHALK, size=24, max_w=420, zone="tray")

    b.at("2.27", 176.7)
    b.slide("hike", 48, 310, color=CYAN)
    b.at("2.28", 181.5)
    b.slide("sg", 48, 370, color=CYAN)
    b.at("2.29", 186.4)
    b.line("split", 380, 78, 560, 120, color=CHALK, zone="tray", lw=2.2)
    b.at("2.30", 188.9)
    b.dup("ai", "aig", "AI build-out (growth)")
    b.slide("aig", 48, 430, color=CYAN)
    b.at("2.31", 190.4)
    b.dup("ai", "aib", "AI build-out (borrowing)")
    b.slide("aib", 1080, 310, color=AMBER)
    b.erase(ids=["ai", "split"])
    b.at("2.32", 192.3)
    b.slide("buy", 1080, 380, color=AMBER)

    b.at("2.33", 200.0)
    b.erase(ids=["trayH"])
    b.text("cH", "Cembalest (Oct 8)", 48, 36, color=CHALK, size=24, max_w=500, zone="tray")
    b.at("2.34", 205.2)
    b.text("sticky", "Sticky inflation", 48, 86, color=CHALK, size=24, max_w=320, zone="tray")
    b.at("2.35", 206.3)
    b.text("hyper", "Hyperscaler debt", 400, 86, color=CHALK, size=24, max_w=320, zone="tray")
    b.at("2.36", 208.2)
    b.text("gdp", "GDP above expectations", 760, 86, color=CHALK, size=24, max_w=400, zone="tray")
    b.at("2.37", 211.6)
    b.text(
        "deficit",
        "Deficit > 5% of GDP in an expansion (first since 1970)",
        48,
        140,
        color=CHALK,
        size=22,
        max_w=900,
        zone="tray",
    )

    b.at("2.38", 222.0)
    b.slide("sticky", 48, 500, color=CYAN)
    b.at("2.39", 222.8)
    b.slide("gdp", 48, 560, color=CYAN)
    b.at("2.40", 225.3)
    b.slide("hyper", 1080, 460, color=AMBER)
    b.at("2.41", 229.6)
    b.slide("deficit", 1080, 530, color=AMBER)
    b.at("2.42", 232.3)
    b.text("more", "more bonds, same buyers", 1080, 660, color=AMBER, size=22, max_w=360, zone="col")

    b.at("2.43", 241.5)
    b.dot("ff", 120, 900, color=CYAN, r=6, zone=path)
    b.text("ffL", "fed funds 4.75% (futures)", 140, 860, color=CYAN, size=18, max_w=280, zone=path)
    b.at("2.44", 247.0)
    b.line("hikeTick", 80, 960, 80, 930, color=CYAN, zone=path, lw=2.6)
    b.text(
        "hikeL",
        "another hike by year end (most officials)",
        100,
        930,
        color=CYAN,
        size=16,
        max_w=360,
        zone=path,
    )
    b.at("2.45", 251.6)
    b.redraw_poly("fpath", [(48, 980), (360, 840), (520, 840)])
    b.text("pace", "pace slowed, destination same", 48, 760, color=CYAN, size=20, max_w=460, zone=path)

    b.at("2.46", 257.9)
    b.shrink_to_t("thumb", keep_zones={"bar"})


def _section3(b: Board):
    num, buck, tbl = "num", "buck", "tbl"
    b.at("3.01", 264.1)
    b.text("auc", "Treasury → auction → buyers", 48, 36, color=CHALK, size=28, max_w=520, zone=buck)
    b.at("3.02", 266.2)
    b.line("cal", 390, 28, 390, 72, color=CHALK, zone=buck, lw=2.4)
    b.text("calL", "on schedule", 408, 36, color=CHALK, size=22, max_w=240, zone=buck)

    b.at("3.03", 272.4)
    b.line("nline", 44, 150, 44, 720, color=CHALK, zone=num, lw=3)
    b.text("yup", "yield ↑", 60, 112, color=CHALK, size=20, max_w=140, zone=num)
    b.at("3.04", 273.9)
    b.text("hyname", "High yield (clearing)", 68, 156, color=CHALK, size=18, max_w=250, zone=num)
    b.at("3.05", 275.6)
    b.line("wiTick", 32, 400, 60, 400, color=CHALK, zone=num, lw=2.6)
    b.text("wiL", "When-issued", 68, 384, color=CHALK, size=18, max_w=220, zone=num)
    b.at("3.06", 281.3)
    b.line("below", 32, 530, 60, 530, color=CHALK, zone=num, lw=2.6)
    b.text(
        "belowL",
        "clears below = stopped through = strong",
        68,
        542,
        color=CHALK,
        size=16,
        max_w=250,
        zone=num,
    )
    b.at("3.07", 289.4)
    b.line("above", 32, 270, 60, 270, color=CHALK, zone=num, lw=2.6)
    b.text(
        "aboveL",
        "clears above = tailed = weak",
        68,
        236,
        color=CHALK,
        size=16,
        max_w=250,
        zone=num,
    )
    b.at("3.08", 294.1)
    b.text("opp", "price ↑ ⇔ yield ↓", 68, 740, color=CHALK, size=18, max_w=280, zone=num)

    b.at("3.09", 300.0)
    b.text("btc", "Bid-to-cover = $ bid ÷ $ sold", 640, 130, color=CHALK, size=24, max_w=780, zone=buck)
    b.at("3.10", 304.6)
    b.append("btc", " (vs recent avg)")
    b.at("3.11", 307.4)
    b.rect("bk1", 640, 230, 340, 120, color=CHALK, zone=buck, lw=2.4)
    b.rect("bk2", 1000, 230, 200, 120, color=CHALK, zone=buck, lw=2.4)
    b.rect("bk3", 1220, 230, 240, 120, color=CHALK, zone=buck, lw=2.4)
    b.at("3.12", 309.2)
    b.text(
        "bk1t",
        "Indirects (incl. foreign buyers, foreign central banks)",
        652,
        250,
        color=CHALK,
        size=16,
        max_w=316,
        zone=buck,
    )
    b.at("3.13", 314.5)
    b.text("bk2t", "Directs (own account)", 1012, 268, color=CHALK, size=16, max_w=176, zone=buck)
    b.at("3.14", 316.1)
    b.text("bk3t", "Dealers (hold what's left)", 1232, 258, color=CHALK, size=16, max_w=216, zone=buck)
    b.at("3.15", 323.2)
    b.text("warn", "big share = warning", 1232, 370, color=CHALK, size=18, max_w=240, zone=buck)

    b.at("3.16", 326.0)
    b.erase(zone=buck)
    # Row labels and an empty two-column grid. The number line stays.
    labels = [
        "Size",
        "High yield (clearing)",
        "When-issued",
        "Bid-to-cover vs. recent average",
        "Indirects",
        "Directs",
        "Dealers",
    ]
    for i, label in enumerate(labels):
        b.text(f"rl{i}", label, 400, 150 + i * 48, color=CHALK, size=16, max_w=250, zone=tbl)
        b.line(f"rg{i}", 400, 178 + i * 48, 1460, 178 + i * 48, color=CHALK, zone=tbl, lw=1.4, dur=0.2)
    b.line("cg", 980, 128, 980, 500, color=CHALK, zone=tbl, lw=1.6)

    b.at("3.17", 328.8)
    b.text(
        "fn",
        "via secondary trackers / relayed Reuters, citing Treasury results",
        400,
        520,
        color=CHALK,
        size=14,
        max_w=1000,
        zone=tbl,
    )
    b.at("3.18", 337.1)
    b.text("h10", "10-year reopening, Wed Oct 7", 680, 108, color=CHALK, size=16, max_w=290, zone=tbl)
    b.at("3.19", 339.1)
    b.text("c10size", "$39 bn", 680, 150, color=CHALK, size=18, max_w=280, zone=tbl)
    b.at("3.20", 339.9)
    b.text("c10hy", "5.300%", 680, 198, color=CHALK, size=18, max_w=280, zone=tbl)
    b.at("3.21", 341.9)
    b.append("c10hy", " (highest since Nov 2000)")
    b.at("3.22", 345.3)
    b.text("c10wi", "5.317%", 680, 246, color=CHALK, size=18, max_w=280, zone=tbl)
    b.text("n5317", "5.317", 2, 384, color=CHALK, size=14, max_w=42, zone=num)
    b.text("n5300", "5.300", 2, 514, color=CHALK, size=14, max_w=42, zone=num)
    b.at("3.23", 348.1)
    b.text("stp", "stopped through 1.7 bp", 680, 560, color=CHALK, size=18, max_w=360, zone=tbl)
    b.at("3.24", 351.3)
    b.text("bp", "1 bp = 0.01 percentage point", 400, 600, color=CHALK, size=16, max_w=400, zone=tbl)
    b.at("3.25", 354.4)
    b.text("c10btc", "2.77", 680, 294, color=CHALK, size=18, max_w=280, zone=tbl)
    b.at("3.26", 355.9)
    b.append("c10btc", " vs 2.54 (6-auction avg)")
    b.at("3.27", 359.5)
    b.text("c10i", "80.3%", 680, 342, color=CHALK, size=18, max_w=200, zone=tbl)
    b.at("3.28", 361.3)
    b.text("c10d", "17.1%", 680, 390, color=CHALK, size=18, max_w=200, zone=tbl)
    b.at("3.29", 362.9)
    b.text("c10dl", "2.5%", 680, 438, color=CHALK, size=18, max_w=280, zone=tbl)
    b.at("3.30", 365.2)
    b.append("c10dl", " (smallest since post-crisis)")
    b.at("3.31", 368.9)
    b.text("strong", "strong", 680, 650, color=CHALK, size=26, max_w=240, zone=tbl)

    b.at("3.32", 371.0)
    b.text("h30", "30-year reopening, Thu Oct 8", 1020, 108, color=CHALK, size=16, max_w=400, zone=tbl)
    b.at("3.33", 372.9)
    b.text("c30size", "$22 bn", 1020, 150, color=CHALK, size=18, max_w=320, zone=tbl)
    b.at("3.34", 374.2)
    b.text("c30hy", "5.618%", 1020, 198, color=CHALK, size=18, max_w=200, zone=tbl)
    b.at("3.35", 376.5)
    b.text("c30wi", "5.617%", 1020, 246, color=CHALK, size=18, max_w=120, zone=tbl)
    b.at("3.36", 379.3)
    b.text("onit", "on it", 1160, 246, color=CHALK, size=18, max_w=120, zone=tbl)
    b.at("3.37", 380.8)
    b.text("c30btc", "2.54", 1020, 294, color=CHALK, size=18, max_w=280, zone=tbl)
    b.at("3.38", 382.1)
    b.append("c30btc", " vs 2.41 avg")
    b.at("3.39", 384.4)
    b.text("c30i", "72.3%", 1020, 342, color=CHALK, size=18, max_w=200, zone=tbl)
    b.at("3.40", 385.9)
    b.text("c30d", "20.9%", 1020, 390, color=CHALK, size=18, max_w=200, zone=tbl)
    b.at("3.41", 387.2)
    b.text("c30dl", "6.8%", 1020, 438, color=CHALK, size=18, max_w=280, zone=tbl)
    b.at("3.42", 388.2)
    b.append("c30dl", " vs 10.3 avg")
    b.at("3.43", 392.1)
    b.text("inline", "in line", 1020, 650, color=CHALK, size=26, max_w=240, zone=tbl)
    b.at("3.44", 393.1)
    b.append("inline", ": decent")
    b.at("3.45", 397.0)
    b.poly(
        "dem",
        [(680, 720), (680, 744), (1380, 744), (1380, 720)],
        color=CHALK,
        zone=tbl,
    )
    b.text("demL", "demand there", 760, 756, color=CHALK, size=20, max_w=560, zone=tbl)
    b.at("3.46", 397.9)
    b.append("demL", ", at a higher yield")

    b.at("3.47", 399.3)
    b.erase(zone=tbl)
    b.erase(zone=num)
    b.restore("thumb", (980, 300, 440, 680), "rest1", emphasise=("topb",))
    b.at("3.48", 405.2)
    b.text(
        "least",
        "foreign central banks = least price-sensitive buyers",
        48,
        320,
        color=CHALK,
        size=22,
        max_w=860,
        zone="hold",
    )
    b.at("3.49", 409.1)
    b.arrow("step", 200, 380, 1040, 360, color=AMBER, zone="hold", style="dashed")
    # Dashed swell above the enlarged amber block. Never copied into T.
    b.rect("swell", 1060, 250, 280, 160, color=AMBER, zone="hold", style="dashed", grow="up")
    b.at("3.50", 414.9)
    b.text("ifback", "if they step back", 1080, 260, color=AMBER, size=20, max_w=280, zone="hold")
    b.at("3.51", 417.8)
    b.text("dalio", "Dalio:", 48, 430, color=CHALK, size=22, max_w=860, zone="hold")
    b.at("3.52", 422.1)
    b.append("dalio", " 'The Chinese don't want to continue to accumulate.'")
    b.at("3.53", 436.0)
    b.text("his", "his view", 48, 500, color=CHALK, size=18, max_w=200, zone="hold")
    b.at("3.54", 438.2)
    b.text("relay", "secondary relay", 48, 546, color=CHALK, size=16, max_w=240, zone="hold")
    b.at("3.55", 440.4)
    b.bar("china", 80, 860 - 140, 70, 140, color=CHALK, zone="hold")
    b.text("chinaL", "China ~$618 bn (July)", 40, 880, color=CHALK, size=16, max_w=220, zone="hold")
    b.at("3.56", 444.0)
    b.bar("japan", 280, 860 - 230, 70, 230, color=CHALK, zone="hold")
    b.text("japanL", "Japan $1.1 tn", 250, 880, color=CHALK, size=16, max_w=200, zone="hold")
    b.at("3.57", 445.6)
    b.append("japanL", " (−$12.8 bn)")


def _section4(b: Board):
    early, chain, crowd, conv, amp = "s4e", "s4c", "crowd", "conv", "amp"
    b.at("4.01", 449.6)
    b.erase_all(thumbs=False)
    b.text("dvs", "Direction vs speed", 48, 300, color=CHALK, size=30, max_w=600, zone=early)
    b.arrow("dirA", 48, 380, 280, 380, "direction (Sections 2–3)", color=CHALK, size=18, zone=early, tdy=-24)
    b.at("4.02", 455.3)
    b.arrow("overA", 48, 460, 520, 460, "overshoot (plumbing)", color=CHALK, size=18, zone=early, tdy=-24)
    b.at("4.03", 460.8)
    b.text(
        "fut",
        "Treasury future = contract to deliver a bond later",
        48,
        520,
        color=CHALK,
        size=24,
        max_w=900,
        zone=early,
    )
    b.at("4.04", 469.1)
    b.text("duruse", "used to hit a target duration", 48, 580, color=CHALK, size=24, max_w=700, zone=early)
    b.at("4.05", 472.6)
    b.rect("shortB", 48, 660, 70, 28, color=CHALK, zone=early)
    b.arc("shortArc", 83, 650, 36, math.pi * 1.15, math.pi * 1.85, color=CHALK, zone=early)
    b.rect("longB", 200, 640, 120, 28, color=CHALK, zone=early)
    b.arc("longArc", 260, 630, 50, math.pi * 1.1, math.pi * 1.9, color=CHALK, zone=early)
    b.at("4.06", 476.0)
    b.arc("longArc2", 260, 620, 78, math.pi * 1.05, math.pi * 1.95, color=CHALK, zone=early, lw=3.4)
    b.text("durL", "duration", 360, 660, color=CHALK, size=22, max_w=200, zone=early)

    b.at("4.07", 478.0)
    b.erase(zone=early)

    # Basket sits where box 2 will be.
    b.at("4.08", 484.2)
    for i in range(5):
        x = 470 + i * 28
        h = 46 if i != 2 else 64
        b.line(f"stick{i}", x, 400, x, 400 - h, color=CHALK, zone=chain, lw=3)
    b.at("4.09", 486.9)
    b.circle("ctdC", 526, 372, 22, color=CHALK, zone=chain)
    b.at("4.10", 489.4)
    b.text("ctdL", "cheapest-to-deliver (CTD)", 430, 448, color=CHALK, size=16, max_w=280, zone=chain)
    b.at("4.11", 491.5)
    b.append("ctdL", "; futures price tracks it")

    b.at("4.12", 494.3)
    b.rect("box1", 40, 300, 300, 90, color=CHALK, zone=chain, lw=2.6)
    b.at("4.13", 501.2)
    b.text(
        "box1t",
        "Futures contract: notional 20-year, 6% bond",
        52,
        318,
        color=CHALK,
        size=16,
        max_w=276,
        zone=chain,
    )
    b.arrow("a12", 340, 345, 430, 345, color=CHALK, zone=chain)
    b.at("4.14", 505.2)
    b.rect("box2", 430, 280, 250, 160, color=CHALK, zone=chain, lw=2.6)
    b.text(
        "box2t",
        "Deliverable basket: 15 to under 25 years",
        442,
        288,
        color=CHALK,
        size=14,
        max_w=226,
        zone=chain,
    )
    b.at("4.15", 510.2)
    b.erase(ids=["ctdL"])
    b.rect("box3", 760, 300, 280, 80, color=CHALK, zone=chain, lw=2.6)
    b.text("box3t", "Cheapest-to-deliver bond", 772, 324, color=CHALK, size=16, max_w=256, zone=chain)
    b.arrow("a23", 680, 360, 758, 340, color=CHALK, zone=chain)

    b.at("4.16", 513.1)
    b.dot("swL", 700, 500, color=CHALK, r=6, zone=chain)
    b.dot("swR", 1040, 500, color=CHALK, r=6, zone=chain)
    b.line("lever", 860, 470, 700, 500, color=CHALK, zone=chain, lw=3.4)
    b.text("swLt", "Yields below 6%: shorter bond", 520, 516, color=CHALK, size=14, max_w=280, zone=chain)
    b.text("swRt", "Yields above 6%: longer bond", 900, 516, color=CHALK, size=14, max_w=280, zone=chain)
    b.at("4.17", 516.9)
    b.text("act15", "→ acts like a 15-year contract", 500, 560, color=CHALK, size=16, max_w=340, zone=chain)
    b.at("4.18", 525.1)
    b.text("act25", "→ acts like a 25-year contract", 900, 560, color=CHALK, size=16, max_w=360, zone=chain)
    b.at("4.19", 532.3)
    b.text("now", "now: 2.5% Feb 2045", 772, 350, color=CHALK, size=16, max_w=200, zone=chain)
    b.at("4.20", 537.8)
    b.text("scen", "scenario (Bloomberg)", 1040, 600, color=CHALK, size=16, max_w=280, zone=chain)
    # Dashed outline on the tag.
    b.rect("scenBox", 1028, 592, 230, 36, color=CHALK, zone=chain, style="dashed", lw=2)
    b.at("4.21", 541.1)
    b.line("ghost", 860, 470, 1040, 500, color=CHALK, zone=chain, style="dashed", lw=3)
    b.text("y2050", "→ 2050?", 900, 350, color=CHALK, size=16, max_w=120, zone=chain)
    # Keep the dashed phrase visually dashed.
    b.line("y2050u", 900, 376, 990, 376, color=CHALK, zone=chain, style="dashed", dur=0.3)

    b.at("4.22", 544.1)
    b.rect("box4", 1120, 300, 250, 70, color=CHALK, zone=chain, lw=2.6)
    b.text("box4t", "Contract's duration", 1132, 322, color=CHALK, size=16, max_w=226, zone=chain)
    b.arrow("a34", 1040, 340, 1118, 335, color=CHALK, zone=chain)
    b.rect("moreBox", 1108, 250, 274, 140, color=CHALK, zone=chain, style="dashed", grow="up")
    b.text("moreL", "more duration per contract", 1120, 258, color=CHALK, size=14, max_w=250, zone=chain)
    b.at("4.23", 550.4)
    b.arrow("loop1", 1420, 400, 1420, 680, "managers sell futures", color=CHALK, size=16, zone=chain, style="dashed", tdx=-110, max_w=200)
    b.at("4.24", 552.2)
    b.text(
        "bnp",
        "BNP: 'could exacerbate the rise in long-end yields.'",
        48,
        700,
        color=CHALK,
        size=18,
        max_w=700,
        zone=chain,
    )
    b.at("4.25", 561.8)
    b.text(
        "loop3",
        "(Levine) basis trades unwind, sell bonds",
        48,
        760,
        color=CHALK,
        size=18,
        max_w=560,
        zone=chain,
    )
    b.line("loop3u", 48, 788, 480, 788, color=CHALK, zone=chain, style="dashed", dur=0.3)
    b.at("4.26", 567.7)
    b.text("loop4", "yields up", 560, 760, color=CHALK, size=20, max_w=200, zone=chain)
    b.line("loop4u", 560, 788, 700, 788, color=CHALK, zone=chain, style="dashed", dur=0.25)
    b.at("4.27", 569.1)
    b.arrow("loop5", 700, 760, 1000, 510, "switch closer", color=CHALK, size=16, zone=chain, style="dashed", tdx=10, tdy=-16)
    b.at("4.28", 572.6)
    b.text(
        "branch",
        "fewer contracts → total duration may not jump, could fall",
        48,
        830,
        color=CHALK,
        size=18,
        max_w=800,
        zone=chain,
    )
    b.line("branchu", 48, 858, 700, 858, color=CHALK, zone=chain, style="dashed", dur=0.3)
    b.at("4.29", 579.1)
    b.stamp("notf", "scenario, not a forecast", 900, 860, color=CHALK, size=20, zone=chain, style="solid", rot=-3)

    b.at("4.30", 581.8)
    b.erase(zone=chain)
    b.text("a1", "1. CTD switch", 1520, 300, color=CHALK, size=18, max_w=340, zone=amp)
    b.text("a2", "2. crowded shorts", 1520, 340, color=CHALK, size=18, max_w=340, zone=amp)

    b.at("4.31", 585.6)
    b.text("crel", "secondary relay", 48, 300, color=CHALK, size=16, max_w=300, zone=crowd)
    b.at("4.32", 587.7)
    b.text("citi", "Citi (Bieber): 'extreme short'", 48, 360, color=CHALK, size=24, max_w=800, zone=crowd)
    b.at("4.33", 591.8)
    b.text("bofa", "BofA: trend-followers' shorts 'near maximum'", 48, 420, color=CHALK, size=24, max_w=1000, zone=crowd)
    b.at("4.34", 597.5)
    b.line("both", 200, 560, 200, 760, color=CHALK, zone=crowd, lw=3)
    b.line("bothU", 200, 560, 184, 584, color=CHALK, zone=crowd, lw=3)
    b.line("bothU2", 200, 560, 216, 584, color=CHALK, zone=crowd, lw=3)
    b.line("bothD", 200, 760, 184, 736, color=CHALK, zone=crowd, lw=3)
    b.line("bothD2", 200, 760, 216, 736, color=CHALK, zone=crowd, lw=3)
    b.text("bothL", "crowding cuts both ways", 230, 640, color=CHALK, size=20, max_w=360, zone=crowd)
    b.at("4.35", 600.9)
    b.text("bad", "bad news: up fast", 230, 530, color=CHALK, size=20, max_w=360, zone=crowd)
    b.at("4.36", 603.3)
    b.text("good", "good news: snapback", 230, 780, color=CHALK, size=20, max_w=360, zone=crowd)

    b.at("4.37", 607.5)
    b.line("scale", 800, 520, 800, 860, color=CHALK, zone=crowd, lw=2.4)
    # Points spaced by yield: 5.364 high, 5.35 close below, 5.28 much lower.
    b.at("4.38", 609.7)
    b.dot("z1", 800, 540, color=CHALK, r=6, zone=crowd)
    b.text("z1L", "5.364% (Wed intraday)", 820, 520, color=CHALK, size=18, max_w=320, zone=crowd)
    b.at("4.39", 611.5)
    b.dot("z2", 800, 820, color=CHALK, r=6, zone=crowd)
    b.line("z12", 800, 540, 800, 820, color=CHALK, zone=crowd, lw=2.2)
    b.text("z2L", "~5.28 (settle)", 820, 800, color=CHALK, size=18, max_w=240, zone=crowd)
    b.at("4.40", 613.1)
    b.dot("z3", 800, 590, color=CHALK, r=6, zone=crowd)
    b.line("z23", 800, 820, 800, 590, color=CHALK, zone=crowd, lw=2.2)
    b.text("z3L", "5.35 (Thu a.m.)", 820, 570, color=CHALK, size=18, max_w=240, zone=crowd)
    b.at("4.41", 615.6)
    b.arrow("lower", 760, 600, 760, 700, "lower (Thu p.m.)", color=CHALK, size=16, zone=crowd, tdx=-150, tdy=20)

    b.at("4.42", 618.0)
    b.erase(zone=crowd)
    b.text("a3", "3. convexity hedging", 1520, 390, color=CHALK, size=18, max_w=360, zone=amp)

    b.at("4.43", 620.4)
    b.text("hold", "some holdings get longer as rates rise", 48, 320, color=CHALK, size=22, max_w=800, zone=conv)
    b.at("4.44", 624.3)
    b.text("mb", "mortgage bonds", 48, 400, color=CHALK, size=22, max_w=280, zone=conv)
    b.at("4.45", 626.4)
    b.text("ru", "rates ↑", 300, 400, color=CHALK, size=22, max_w=160, zone=conv)
    b.at("4.46", 627.5)
    b.arrow("cv1", 430, 416, 520, 416, color=CHALK, zone=conv)
    b.text("fr", "fewer refinance", 530, 400, color=CHALK, size=20, max_w=240, zone=conv)
    b.at("4.47", 628.8)
    b.arrow("cv2", 780, 416, 860, 416, color=CHALK, zone=conv)
    b.text("slow", "slower payback", 870, 400, color=CHALK, size=20, max_w=240, zone=conv)
    b.at("4.48", 630.5)
    b.arrow("cv3", 1100, 416, 1160, 480, color=CHALK, zone=conv)
    b.text("ld", "longer duration", 48, 500, color=CHALK, size=20, max_w=260, zone=conv)
    b.at("4.49", 633.0)
    b.arrow("cv4", 280, 516, 400, 516, color=CHALK, zone=conv)
    b.text("sell", "holders sell Treasuries/futures", 410, 500, color=CHALK, size=20, max_w=420, zone=conv)
    b.at("4.50", 635.5)
    b.poly(
        "cvloop",
        [(700, 540), (760, 620), (200, 620), (160, 430), (280, 400)],
        color=CHALK,
        zone=conv,
        arrow=True,
    )
    b.at("4.51", 637.9)
    b.text(
        "bbg",
        "Bloomberg: convexity hedging + futures mechanics making it worse",
        48,
        700,
        color=CHALK,
        size=20,
        max_w=1100,
        zone=conv,
    )
    b.at("4.52", 644.3)
    b.append("bbg", " — not sized")
    b.at("4.53", 648.4)
    b.text("bnp2", "BNP: 'negative convexity profile'", 48, 770, color=CHALK, size=22, max_w=700, zone=conv)
    b.at("4.54", 654.5)
    b.rect("ampb", 1504, 284, 380, 150, color=CHALK, zone=amp, lw=2.4)
    b.text("nd", "not direction", 1520, 450, color=CHALK, size=18, max_w=340, zone=amp)
    b.at("4.55", 656.2)
    b.append("nd", " · speed + overshoot")


def _section5(b: Board):
    z = "s5"
    b.at("5.01", 659.9)
    b.erase_all(thumbs=False)
    b.at("5.02", 663.1)
    b.box("k1", 36, 400, 220, 64, "10-year Treasury", color=CHALK, size=18, zone=z)
    b.at("5.03", 669.2)
    b.arrow("k12", 258, 432, 330, 432, color=CHALK, zone=z)
    b.box("k2", 340, 400, 250, 64, "30-year mortgage rate", color=CHALK, size=16, zone=z)
    b.at("5.04", 671.1)
    b.text("spr", "10-yr + lender spread", 250, 478, color=CHALK, size=16, max_w=280, zone=z)
    b.at("5.05", 678.2)
    b.text("fm", "Freddie Mac:", 340, 530, color=CHALK, size=18, max_w=300, zone=z)
    b.at("5.06", 680.8)
    b.append("fm", " 7.40%")
    b.at("5.07", 682.5)
    b.append("fm", " (7.28 last wk")
    b.at("5.08", 684.8)
    b.append("fm", ", 6.30 yr ago)")
    b.at("5.09", 687.1)
    b.text("mba", "MBA:", 340, 590, color=CHALK, size=18, max_w=300, zone=z)
    b.at("5.10", 690.2)
    b.append("mba", " 7.49%, 3-yr high")
    b.at("5.11", 693.0)
    b.append("mba", " (from 7.3)")
    b.at("5.12", 694.8)
    b.text("two", "two surveys, name the source", 340, 650, color=CHALK, size=16, max_w=300, zone=z)

    b.at("5.13", 698.4)
    b.arrow("k23", 592, 432, 660, 432, color=CHALK, zone=z)
    b.box("k3", 670, 400, 280, 64, "Home buying and building", color=CHALK, size=16, zone=z)
    b.at("5.14", 701.1)
    b.text("paym", "bigger monthly payment", 670, 480, color=CHALK, size=16, max_w=300, zone=z)
    b.at("5.15", 703.4)
    b.text("qual", "buyers qualify for less", 670, 512, color=CHALK, size=16, max_w=300, zone=z)
    b.at("5.16", 705.3)
    b.text("bfin", "builders' financing costs more", 670, 544, color=CHALK, size=16, max_w=320, zone=z)
    b.at("5.17", 710.0)
    b.text("apps", "MBA purchase apps −13% y/y", 670, 584, color=CHALK, size=16, max_w=320, zone=z)
    b.at("5.18", 713.4)
    b.append("apps", " (4-wk avg)")

    b.at("5.19", 716.0)
    b.arrow("k34", 952, 432, 1020, 432, color=CHALK, zone=z)
    b.box("k4", 1030, 400, 160, 64, "Rents", color=CHALK, size=22, zone=z)
    b.at("5.20", 719.6)
    b.text(
        "slok",
        "Slok: Higher Rates, Higher Rent Doom Loop",
        360,
        250,
        color=CHALK,
        size=20,
        max_w=800,
        zone=z,
    )
    b.at("5.21", 727.0)
    b.arrow("k45", 1192, 432, 1260, 432, color=CHALK, zone=z)
    b.box("k5", 1270, 400, 180, 64, "Inflation", color=CHALK, size=22, zone=z)
    b.at("5.22", 729.1)
    b.poly(
        "back",
        [(1360, 400), (1400, 300), (200, 300), (120, 400)],
        color=CYAN,
        zone=z,
        style="dashed",
        arrow=True,
    )
    b.highlight("botb", until=752.6)
    b.at("5.23", 734.0)
    b.text("oer", "owners' equivalent rent", 1030, 480, color=CHALK, size=16, max_w=400, zone=z)
    b.at("5.24", 738.5)
    b.append("oer", " ≈ ¼ of CPI basket")
    b.at("5.25", 740.5)
    b.text("sview", "Slok's view", 360, 328, color=CHALK, size=16, max_w=200, zone=z)
    b.at("5.26", 746.3)
    b.text("peak", "rates could peak", 1030, 560, color=CHALK, size=16, max_w=400, zone=z)
    b.at("5.27", 748.1)
    b.append("peak", " ← same chain can slow the economy")


def _section6(b: Board, duration: float):
    lines, side, week = "s6", "side", "week"
    b.at("6.01", 752.6)
    b.erase_all(thumbs=False)
    b.at("6.02", 756.4)
    ys = (70, 250, 440, 640)
    for i, y in enumerate(ys):
        b.text(f"c{i}", f"{i + 1}.", 40, y, color=CHALK, size=26, max_w=560, zone=lines, opacity=0.4)
        rule = b.line(f"cr{i}", 90, y + 42, 640, y + 42, color=CHALK, zone=lines, lw=2.0, dur=0.25)
        rule.base_opacity = 0.4

    b.at("6.03", 758.1)
    b.undim("c0")
    b.by_id["cr0"].opacity_keys.append((758.1, 1.0, 0.25))
    b.append("c0", " Which part moved?")
    b.restore("thumb", (760, 90, 240, 400), "rest6")

    b.at("6.04", 759.6)
    b.text("ep", "expected path", 1020, 320, color=CYAN, size=18, max_w=420, zone=side)
    b.at("6.05", 764.1)
    b.text("tp", "term premium", 1020, 100, color=AMBER, size=18, max_w=420, zone=side)
    b.at("6.06", 767.1)
    b.append("tp", " (supply, deficits, uncertainty)")
    b.at("6.07", 769.2)
    b.append("ep", " (Fed minutes, futures)")
    b.at("6.08", 771.8)
    b.text("left", "≈ what's left", 790, 242, color=CHALK, size=16, max_w=190, zone=side)

    b.at("6.09", 774.2)
    b.erase(zone=side)
    b.erase(group="rest6")
    b.undim("c1")
    b.by_id["cr1"].opacity_keys.append((774.2, 1.0, 0.25))
    b.append("c1", " How did the auctions go?")
    b.at("6.10", 776.4)
    b.text("s2a", "tail / stop-through vs when-issued", 700, 250, color=CHALK, size=18, max_w=420, zone="side2")
    b.at("6.11", 779.6)
    b.text("s2b", "bid-to-cover vs avg", 700, 290, color=CHALK, size=18, max_w=400, zone="side2")
    b.at("6.12", 782.3)
    b.text("s2c", "indirects + directs vs dealers", 700, 330, color=CHALK, size=18, max_w=420, zone="side2")

    b.at("6.13", 787.1)
    b.erase(zone="side2")
    b.undim("c2")
    b.by_id["cr2"].opacity_keys.append((787.1, 1.0, 0.25))
    b.append("c2", " Is the plumbing adding to it?")
    b.at("6.14", 789.6)
    b.text("s3a", "CTD about to change?", 700, 440, color=CHALK, size=18, max_w=400, zone="side3")
    b.at("6.15", 793.4)
    b.text("s3b", "duration extending?", 700, 480, color=CHALK, size=18, max_w=400, zone="side3")
    b.at("6.16", 795.1)
    b.text("s3c", "shorts crowded?", 700, 520, color=CHALK, size=18, max_w=400, zone="side3")
    b.at("6.17", 796.4)
    b.text("s3d", "convexity hedges selling?", 700, 560, color=CHALK, size=18, max_w=420, zone="side3")

    b.at("6.18", 800.6)
    b.erase(zone="side3")
    b.undim("c3")
    b.by_id["cr3"].opacity_keys.append((800.6, 1.0, 0.25))
    b.append("c3", " Are mortgages following?")
    b.at("6.19", 802.8)
    b.text("s4a", "mortgage rates vs Treasuries", 700, 640, color=CHALK, size=18, max_w=420, zone="side4")
    b.at("6.20", 804.9)
    b.text("s4b", "purchase apps + construction", 700, 680, color=CHALK, size=18, max_w=420, zone="side4")
    b.at("6.21", 807.6)
    b.text("s4c", "later rent pressure?", 700, 720, color=CHALK, size=18, max_w=400, zone="side4")

    b.at("6.22", 810.5)
    b.erase(zone="side4")
    b.text("weekH", "this week", 1280, 36, color=CHALK, size=20, max_w=190, zone=week)
    b.at("6.23", 814.0)
    b.text("w2", "strong 10-yr auction", 1100, 250, color=CHALK, size=18, max_w=340, zone=week)
    b.at("6.24", 816.5)
    b.text("w3", "extreme short", 1100, 440, color=CHALK, size=18, max_w=340, zone=week)
    b.at("6.25", 818.2)
    b.text("w1", "pace slowed, destination same", 1100, 70, color=CYAN, size=16, max_w=340, zone=week)
    b.at("6.26", 821.3)
    b.text("w4", "multi-year highs", 1100, 640, color=CHALK, size=18, max_w=340, zone=week)
    b.at("6.27", 826.9)
    b.fade_out(duration - 0.8, duration)
