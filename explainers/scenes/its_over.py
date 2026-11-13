"""It's Over vs. the AI Credit Stack. One element per storyboard row."""

from __future__ import annotations

import math
from pathlib import Path

from explainers.bb.engine import (
    AMBER,
    CHALK,
    CORAL,
    CYAN,
    GRAY,
    Board,
    load_storyboard_times,
)

STORY = (
    Path(__file__).resolve().parents[1]
    / "storyboards"
    / "its-over-explainer-storyboard-v2.md"
)

# Main board stays out of the top-right thumbnail slot.
L = 36
MID = 748


def build(duration: float) -> Board:
    b = Board(duration)
    _section1(b)
    _section2(b)
    _section3(b)
    _section4(b)
    b.t_occupied = [(0.0, duration)]
    b.finalize(load_storyboard_times(STORY))
    return b


def _section1(b: Board):
    z = "s1"
    b.at("1.01", 0.0)
    b.line("div", MID, 48, MID, 1020, color=CHALK, zone=z, dur=0.6)

    b.at("1.02", 5.0)
    b.arrow("awayL", MID, 78, MID - 70, 78, color=CHALK, zone=z)
    b.arrow("awayR", MID, 78, MID + 70, 78, color=CHALK, zone=z)

    b.at("1.03", 12.6)
    b.text("h1", "Story 1: research", 56, 118, color=CORAL, size=36, max_w=560, zone=z)

    b.at("1.04", 14.7)
    b.rect("card", 52, 175, 660, 168, color=CORAL, zone=z)
    b.text(
        "card1",
        "Egan-Jones Risk Commentary #220, 'It's Over' (Oct 1, 2026).",
        70,
        196,
        color=CORAL,
        size=26,
        max_w=624,
        zone=z,
    )

    b.at("1.05", 25.6)
    b.text(
        "card2",
        "Research/commentary, not a rating action.",
        70,
        268,
        color=CHALK,
        size=26,
        max_w=624,
        zone=z,
    )

    b.at("1.06", 28.2)
    # Under the phrase "not a rating action" on card2 (size 26, prefix ~223px).
    b.line("ul", 70 + 223, 308, 70 + 223 + 190, 308, color=CHALK, zone=z, dur=0.4)
    b.text("rating", "rating: unchanged", 720, 300, color=CHALK, size=22, max_w=280, zone=z)

    b.at("1.07", 32.3)
    b.text(
        "analysts",
        "not written by credit analysts",
        70,
        360,
        color=CHALK,
        size=24,
        max_w=620,
        zone=z,
    )

    b.at("1.08", 44.2)
    b.text("b1", "Professional services fees", 78, 430, color=CORAL, size=28, max_w=560, zone=z)
    b.at("1.09", 46.4)
    b.text("b2", "Venture capital", 78, 478, color=CORAL, size=28, max_w=560, zone=z)
    b.at("1.10", 47.3)
    b.text("b3", "Housing", 78, 526, color=CORAL, size=28, max_w=560, zone=z)

    b.at("1.11", 48.5)
    b.text("h2", "Story 2: money moving", 800, 118, color=CYAN, size=34, max_w=620, zone=z)

    b.at("1.12", 51.6)
    b.box("banks", 800, 180, 250, 72, "Broadcom's banks", color=CYAN, size=24, zone=z)

    b.at("1.13", 53.7)
    b.arrow("bn", 1062, 216, 1240, 216, "~$60 bn", color=CYAN, size=22, zone=z, tdy=-26)

    b.at("1.14", 56.1)
    b.box("chips1", 1248, 180, 180, 72, "AI chips", color=CYAN, size=26, zone=z)

    b.at("1.15", 57.1)
    b.text("anth", "(Anthropic and others)", 1248, 264, color=CYAN, size=22, max_w=200, zone=z)

    b.at("1.16", 60.3)
    b.box(
        "ipo1",
        1100,
        320,
        320,
        64,
        "IPO: as soon as mid-Nov",
        color=CYAN,
        size=22,
        zone=z,
        style="dotted",
    )

    b.at("1.17", 68.0)
    b.box("lenders", MID - 120, 900, 240, 78, "Lenders", color=CHALK, size=30, zone=z)
    b.arrow(
        "fund",
        MID + 20,
        900,
        900,
        260,
        "fund the buildout",
        color=CYAN,
        size=22,
        zone=z,
        tdx=70,
        tdy=-10,
        max_w=220,
    )

    b.at("1.18", 77.1)
    b.arrow(
        "also",
        MID - 40,
        900,
        200,
        560,
        "also fund",
        color=CORAL,
        size=22,
        zone=z,
        tdx=-30,
        tdy=0,
    )

    b.at("1.19", 78.8)
    b.shrink_to_t("thumb1")


def _section2(b: Board):
    q, ch, cols = "q", "ch", "cols"

    b.at("2.01", 92.5)
    b.text("q0", "A lender cares about:", 48, 28, color=CHALK, size=28, max_w=700, zone=q)
    b.at("2.02", 94.2)
    b.text("q1", "1. Paid back on time?", 48, 74, color=CHALK, size=28, max_w=520, zone=q)
    b.at("2.03", 97.3)
    b.text("q2", "2. Can borrow again?", 48, 118, color=CHALK, size=28, max_w=520, zone=q)
    b.at("2.04", 104.6)
    b.text(
        "q3",
        "Whose cash flow does this hit?",
        860,
        74,
        color=CHALK,
        size=26,
        max_w=560,
        zone=q,
    )

    b.at("2.05", 109.0)
    b.text("fh", "Faster horse", 80, 200, color=CHALK, size=32, max_w=420, zone=ch)
    b.text("vs", "vs", 560, 200, color=CHALK, size=28, max_w=80, zone=ch)
    b.text("np", "New paradigm", 680, 200, color=CHALK, size=32, max_w=500, zone=ch)
    b.at("2.06", 111.1)
    b.text(
        "fhb",
        "incumbents run existing operations faster",
        80,
        260,
        color=CHALK,
        size=26,
        max_w=460,
        zone=ch,
    )
    b.at("2.07", 115.3)
    b.text(
        "npb",
        "very few people or none, agentic work around the clock",
        680,
        260,
        color=CHALK,
        size=26,
        max_w=720,
        zone=ch,
    )

    b.at("2.08", 126.3)
    b.erase(zone=ch)
    b.text("c1", "Channel 1: professional services", 48, 190, color=CORAL, size=32, max_w=800, zone=ch)

    b.at("2.09", 131.3)
    b.text("kpmg", "KPMG", 56, 250, color=CHALK, size=32, max_w=200, zone=ch)
    b.text("krole", "client", 56, 294, color=CHALK, size=20, max_w=200, zone=ch)

    b.at("2.10", 132.4)
    b.rect("feecard", 250, 246, 430, 92, color=CORAL, zone=ch)
    b.text("fee", "KPMG fee cut: 14%", 266, 268, color=CORAL, size=26, max_w=400, zone=ch)

    b.at("2.11", 133.6)
    b.text("gt", "Grant Thornton UK", 720, 250, color=CHALK, size=26, max_w=400, zone=ch)
    b.text("grole", "firm (its revenue shrank)", 720, 292, color=CHALK, size=20, max_w=420, zone=ch)
    b.arrow("feeA", 700, 268, 250, 280, "fee", color=CHALK, size=20, zone=ch, tdy=-22)

    b.at("2.12", 135.0)
    b.append("fee", " ($416,000")
    b.bar("feebar", 1180, 230, 64, 240, color=CORAL, zone=ch)

    b.at("2.13", 136.4)
    b.append("fee", " → $357,000)")
    b.set_fill("feebar", 357 / 416, ghost=1.0)

    b.at("2.14", 153.0)
    b.rect("ibmcard", 56, 430, 520, 78, color=CORAL, zone=ch)
    b.text("ibm", "IBM: −13% in one day", 72, 452, color=CORAL, size=26, max_w=490, zone=ch)
    b.at("2.15", 156.0)
    b.append("ibm", ", worst since 2000.")

    b.at("2.16", 158.2)
    b.text("law", "Law", 620, 450, color=CORAL, size=24, max_w=220, zone=ch)
    b.at("2.17", 159.0)
    b.text("ib", "Investment banking", 760, 450, color=CORAL, size=24, max_w=320, zone=ch)
    b.at("2.18", 159.3)
    b.text("eng", "Engineering", 1140, 450, color=CORAL, size=24, max_w=260, zone=ch)

    # Cushion mini-diagram. Bottoms align at y=860.
    b.at("2.19", 166.9)
    b.bar("hours", 80, 560, 70, 250, color=CHALK, zone=ch)
    b.text("hoursL", "Hours", 72, 824, color=CHALK, size=22, max_w=120, zone=ch)
    b.bar("rev", 250, 560, 70, 250, color=CHALK, zone=ch)
    b.text("revL", "Revenue (the bill)", 200, 824, color=CHALK, size=22, max_w=240, zone=ch)

    b.at("2.20", 169.1)
    b.set_fill("hours", 2 / 3, ghost=1.0, ghost_color=CORAL)
    b.at("2.21", 173.2)
    b.set_fill("rev", 2 / 3, ghost=1.0, ghost_color=CORAL)
    b.at("2.22", 175.1)
    b.text("eq", "fee cut = revenue cut", 190, 868, color=CORAL, size=22, max_w=280, zone=ch)
    b.at("2.23", 176.9)
    b.text("debt", "Debt", 430, 760, color=CHALK, size=26, max_w=120, zone=ch)
    b.at("2.24", 179.4)
    # Interest top (700) sits below the shrunken revenue top (560+83).
    b.bar("intr", 560, 700, 70, 160, color=CHALK, zone=ch)
    b.text("intrL", "Interest", 540, 824, color=CHALK, size=22, max_w=140, zone=ch)
    b.text("same", "same size", 520, 868, color=CHALK, size=20, max_w=160, zone=ch)

    b.at("2.25", 181.7)
    b.brace("cush", 360, 560, 700, color=CHALK, zone=ch)
    b.text("cushL", "cushion", 390, 600, color=CHALK, size=22, max_w=160, zone=ch)
    b.at("2.26", 184.2)
    b.erase(ids=["cush", "cushL"])
    b.brace("cush2", 360, 643, 700, color=CHALK, zone=ch)
    b.text("cushL2", "cushion", 390, 650, color=CHALK, size=22, max_w=160, zone=ch)

    b.at("2.27", 187.1)
    b.arrow("save", 330, 600, 900, 560, color=CORAL, zone=ch)
    b.at("2.28", 188.7)
    b.text("client", "Client (KPMG)", 910, 530, color=CHALK, size=24, max_w=280, zone=ch)

    b.at("2.29", 189.9)
    b.erase(zone=ch)
    b.text("c2", "Channel 2: VC", 48, 200, color=CORAL, size=34, max_w=600, zone=ch)
    b.at("2.30", 193.2)
    b.text(
        "vc1",
        "less human capital → capital matters less",
        80,
        280,
        color=CORAL,
        size=30,
        max_w=1100,
        zone=ch,
    )
    b.at("2.31", 204.1)
    b.text("vc2", "leverage and returns compress", 80, 360, color=CORAL, size=30, max_w=900, zone=ch)
    b.at("2.32", 209.8)
    b.text("vc3", "LPs: not priced?", 80, 440, color=CORAL, size=30, max_w=700, zone=ch)
    b.at("2.33", 212.6)
    b.stamp("spec", "speculative", 980, 400, color=CHALK, size=28, zone=ch, style="dashed")
    b.at("2.34", 213.8)
    b.text("specn", "argument about the future", 760, 470, color=CHALK, size=24, max_w=460, zone=ch)

    b.at("2.35", 217.7)
    b.erase(zone=ch)
    b.text(
        "c3",
        "Channel 3: housing (via mortgages)",
        48,
        186,
        color=CORAL,
        size=30,
        max_w=900,
        zone=ch,
    )

    # Price bars share a baseline at y=470. Heights track 1.6 / 4.3 / 3.5.
    base = 470
    h_max = 200
    b.at("2.36", 225.1)
    h16 = h_max * (1.6 / 4.3)
    b.bar("hp", 70, base - h16, 54, h16, color=CORAL, zone=ch)
    b.text("hpL", "Home prices +1.6% (yr to June)", 40, 486, color=CORAL, size=18, max_w=200, zone=ch)

    b.at("2.37", 227.4)
    b.bar("ghost", 150, base - h_max, 54, h_max, color=CHALK, zone=ch, style="dashed")
    b.text(
        "ghostL",
        "Long-run house-price avg ~4.3%",
        130,
        250,
        color=CHALK,
        size=18,
        max_w=200,
        zone=ch,
    )

    b.at("2.38", 231.3)
    h35 = h_max * (3.5 / 4.3)
    b.bar("cpi", 360, base - h35, 54, h35, color=CHALK, zone=ch)
    b.text("cpiL", "CPI +3.5%", 340, 486, color=CHALK, size=20, max_w=160, zone=ch)

    b.at("2.39", 234.7)
    b.brace("realb", 430, base - h16, base - h35, color=CHALK, zone=ch, width=14)
    b.text("real", "real prices falling", 460, 360, color=CHALK, size=22, max_w=280, zone=ch)
    b.text("arith", "(my arithmetic)", 460, 396, color=CHALK, size=18, max_w=240, zone=ch)

    b.at("2.40", 240.6)
    b.text(
        "med",
        "median new home ÷ median household income",
        760,
        210,
        color=CHALK,
        size=22,
        max_w=640,
        zone=ch,
    )
    b.at("2.41", 241.7)
    b.bar("y2025", 1080, 470 - 200, 50, 200, color=CORAL, zone=ch)
    b.text("y2025L", "2025: 4.7×", 1040, 486, color=CORAL, size=20, max_w=180, zone=ch)
    b.at("2.42", 245.1)
    h84 = 200 * (3.6 / 4.7)
    b.bar("y1984", 900, 470 - h84, 50, h84, color=CHALK, zone=ch)
    b.text("y1984L", "1984: 3.6×", 860, 486, color=CHALK, size=20, max_w=180, zone=ch)

    b.at("2.43", 249.1)
    b.text(
        "mort",
        "~60% of owner-occupied homes have a mortgage",
        760,
        540,
        color=CHALK,
        size=22,
        max_w=660,
        zone=ch,
    )

    b.at("2.44", 252.8)
    b.text("ch1", "2 incomes, thin cushion", 48, 640, color=CORAL, size=24, max_w=360, zone=ch)
    b.at("2.45", 256.6)
    b.arrow("chA1", 400, 656, 500, 656, color=CORAL, zone=ch)
    b.text("ch2", "1 income disrupted", 510, 640, color=CORAL, size=24, max_w=320, zone=ch)
    b.at("2.46", 258.0)
    b.arrow("chA2", 860, 656, 960, 656, color=CORAL, zone=ch)
    b.text("ch3", "forced sales (6–12 mo)", 970, 640, color=CORAL, size=24, max_w=360, zone=ch)
    b.at("2.47", 260.1)
    b.arrow("chA3", 48, 720, 48, 760, color=CORAL, zone=ch)
    b.text("ch4", "short-term price pressure", 70, 760, color=CORAL, size=24, max_w=420, zone=ch)
    b.at("2.48", 263.1)
    b.text(
        "land",
        "long run: urban land still scarce",
        48,
        830,
        color=CHALK,
        size=24,
        max_w=560,
        zone=ch,
    )
    b.at("2.49", 266.7)
    b.stamp(
        "fwd",
        "forward-looking (theirs)",
        1100,
        820,
        color=CHALK,
        size=24,
        zone=ch,
        style="dashed",
    )

    b.at("2.50", 269.5)
    b.erase(zone=ch)
    b.erase(zone=q)
    b.line("cdiv1", 520, 40, 520, 1000, color=CHALK, zone=cols, lw=2.2)
    b.line("cdiv2", 1000, 40, 1000, 1000, color=CHALK, zone=cols, lw=2.2)

    b.at("2.51", 273.3)
    b.text("spH", "Spread", 80, 70, color=CHALK, size=32, max_w=360, zone=cols)
    b.at("2.52", 274.1)
    b.text("maH", "Maturity", 560, 70, color=CHALK, size=32, max_w=380, zone=cols)
    b.at("2.53", 274.1)
    b.text("rfH", "Refinancing", 1040, 70, color=CHALK, size=32, max_w=380, zone=cols)

    b.at("2.54", 276.0)
    b.bar("tsy", 120, 280, 70, 220, color=CHALK, zone=cols)
    b.text("tsyL", "Treasury yield", 70, 520, color=CHALK, size=20, max_w=200, zone=cols)
    b.rect("spread", 120, 200, 70, 80, color=CHALK, zone=cols, fill=True)
    b.text("spreadL", "spread", 200, 220, color=CHALK, size=22, max_w=180, zone=cols)

    b.at("2.55", 287.9)
    b.rect("swell", 112, 120, 86, 170, color=CORAL, zone=cols, style="dashed", grow="up")
    b.at("2.56", 290.9)
    b.text("wider", "wider", 220, 130, color=CORAL, size=24, max_w=160, zone=cols)

    b.at("2.57", 292.4)
    b.arrow("time", 560, 420, 960, 420, color=CHALK, zone=cols)
    b.brace("term", 640, 360, 470, color=CHALK, zone=cols, width=12)
    # Horizontal-feeling bracket: a line over the timeline plus the label.
    b.line("termL", 620, 360, 900, 360, color=CHALK, zone=cols, dur=0.4)
    b.text("termT", "loan term", 680, 310, color=CHALK, size=22, max_w=220, zone=cols)

    b.at("2.58", 298.8)
    b.dim(ids=["term", "termL", "termT"])
    b.line("shortL", 620, 400, 760, 400, color=CORAL, zone=cols, style="dashed", dur=0.4)
    b.line("shortA", 620, 392, 620, 408, color=CORAL, zone=cols, style="dashed", dur=0.2)
    b.line("shortB", 760, 392, 760, 408, color=CORAL, zone=cols, style="dashed", dur=0.2)

    b.at("2.59", 302.1)
    b.text(
        "safer",
        "shorter = safer for lender, harder on borrower",
        540,
        470,
        color=CHALK,
        size=20,
        max_w=440,
        zone=cols,
    )

    b.at("2.60", 305.6)
    b.box("old", 1040, 240, 160, 64, "old debt", color=CHALK, size=22, zone=cols)
    b.at("2.61", 310.8)
    b.arrow("roll", 1210, 272, 1320, 272, "roll it", color=CHALK, size=20, zone=cols, tdy=-24)
    b.box("new", 1328, 240, 120, 64, "new debt", color=CHALK, size=20, zone=cols)

    b.at("2.62", 314.9)
    b.arrow("fromS", 300, 280, 1240, 340, color=CORAL, zone=cols, style="dashed")
    b.arrow("fromM", 760, 420, 1260, 340, color=CORAL, zone=cols, style="dashed")
    b.at("2.63", 320.4)
    b.line("x1", 1248, 250, 1304, 306, color=CORAL, zone=cols, style="dashed", lw=4)
    b.line("x2", 1304, 250, 1248, 306, color=CORAL, zone=cols, style="dashed", lw=4)

    b.at("2.64", 322.3)
    b.text("over", "'over' shows up here", 1040, 360, color=CHALK, size=24, max_w=400, zone=cols)
    b.at("2.65", 332.4)
    b.text(
        "nospr",
        "no spreads or ratings attached",
        200,
        24,
        color=CHALK,
        size=22,
        max_w=700,
        zone=cols,
    )
    b.at("2.66", 337.3)
    b.stamp("mech", "mechanism, not a forecast", 740, 860, color=CHALK, size=26, zone=cols, style="solid")

    b.at("2.67", 344.6)
    b.erase_all(thumbs=True)


def _section3(b: Board):
    z = "s3"
    b.at("3.01", 347.0)
    b.rect("colL", 28, 188, 300, 300, color=CHALK, zone=z, lw=2.4)
    b.rect("colM", 400, 188, 340, 300, color=CHALK, zone=z, lw=2.4)
    b.rect("colR", 820, 188, 300, 250, color=CHALK, zone=z, lw=2.4)

    b.at("3.02", 349.1)
    b.text("lH", "Lenders", 48, 200, color=CHALK, size=26, max_w=250, zone=z)
    b.at("3.03", 353.8)
    b.box("bbanks", 48, 250, 250, 68, "Broadcom's banks", color=CYAN, size=22, zone=z)
    b.at("3.04", 355.7)
    b.arrow(
        "stub",
        300,
        284,
        390,
        284,
        "~$60 bn chip financing",
        color=CYAN,
        size=18,
        zone=z,
        tdy=-28,
        max_w=220,
        lw=6,
    )

    b.at("3.05", 359.0)
    b.text("bH", "Borrowers", 420, 200, color=CHALK, size=26, max_w=280, zone=z)
    b.at("3.06", 360.6)
    b.erase(ids=["stub", "stub.t"])
    b.box("anth2", 430, 248, 280, 64, "Anthropic and others", color=CYAN, size=22, zone=z)
    b.arrow("full", 300, 284, 428, 280, color=CYAN, zone=z, lw=6)

    b.at("3.07", 362.8)
    b.text(
        "norep",
        "collateral / rate / maturity: not reported",
        420,
        418,
        color=CHALK,
        size=18,
        max_w=340,
        zone="note",
    )

    b.at("3.08", 371.0)
    b.text("wH", "What's financed", 836, 200, color=CHALK, size=24, max_w=280, zone=z)
    b.at("3.09", 372.8)
    # The optional thin connector is not drawn: it is beyond the stage direction.
    b.box("chips", 860, 250, 200, 64, "AI chips", color=CYAN, size=24, zone=z)

    b.at("3.10", 373.5)
    b.box("amz", 430, 340, 280, 60, "Amazon", color=CYAN, size=24, zone=z)
    b.at("3.11", 379.8)
    b.arrow(
        "asset",
        712,
        370,
        900,
        300,
        "asset-light",
        color=CYAN,
        size=18,
        zone=z,
        style="dashed",
        tdx=10,
        tdy=16,
        max_w=200,
    )
    b.at("3.12", 381.3)
    b.append("asset.t", " ~$8 bn kept off books")

    b.at("3.13", 388.2)
    b.rect("equity", 400, 28, 340, 150, color=CYAN, zone=z, style="dotted", lw=3.2)
    b.text("eq1", "Possible public equity", 414, 40, color=CYAN, size=20, max_w=312, zone=z)
    b.at("3.14", 391.8)
    b.text("eq2", "IPO targeted as soon as mid-Nov", 414, 72, color=CYAN, size=18, max_w=312, zone=z)
    b.at("3.15", 394.0)
    b.text("eq3", "valuation chatter up to ~$2 tn", 414, 102, color=CYAN, size=18, max_w=312, zone=z)
    b.at("3.16", 399.3)
    b.box("miniE", 760, 36, 200, 58, "Equity: paid 2nd", color=CHALK, size=18, zone="mini")
    b.box("miniD", 976, 36, 190, 58, "Debt: paid 1st", color=CHALK, size=18, zone="mini")
    b.at("3.17", 406.2)
    b.text("eq4", "Not raised, so not a cushion yet.", 414, 136, color=CYAN, size=18, max_w=312, zone=z)

    b.at("3.18", 410.5)
    b.rect("bar", 28, 948, 1860, 108, color=GRAY, zone=z, fill=True, grow="right", lw=2.4)
    b.text("barL", "The same credit market", 48, 956, color=CHALK, size=18, max_w=360, zone=z)

    b.at("3.19", 417.5)
    b.text("ccc_h", "CCC spread", 48, 984, color=CHALK, size=22, max_w=280, zone=z)
    b.at("3.20", 422.2)
    b.text("ccc_val", "1,007 bp (Sep 30)", 48, 1016, color=CHALK, size=20, max_w=320, zone=z)
    b.rect("ocard", 36, 620, 640, 78, color=CHALK, zone="card")
    b.text(
        "ocardt",
        "US CCC-and-lower OAS: 1,007 bp (Sep 30)",
        50,
        642,
        color=CHALK,
        size=20,
        max_w=610,
        zone="card",
    )
    b.at("3.21", 426.3)
    b.append("ocardt", ", from ~860 bp early Sep.")
    b.poly("chart", [(70, 860), (280, 760)], color=CHALK, zone="card", arrow=False)
    b.text("c860", "860", 40, 868, color=CHALK, size=18, max_w=80, zone="card")
    b.text("c1007", "1,007", 250, 728, color=CHALK, size=18, max_w=100, zone="card")
    b.at("3.22", 430.0)
    # 1000 sits between 860 and 1007 on the rising line.
    b.line("tick", 230, 792, 250, 772, color=CHALK, zone="card", lw=2.4)
    b.text(
        "tickL",
        "first above 1,000 since Mar 2023",
        36,
        700,
        color=CHALK,
        size=16,
        max_w=360,
        zone="card",
    )

    b.at("3.23", 433.9)
    for i, name in enumerate(("IG", "BB", "B", "CCC")):
        y = 700 + i * 48
        b.line(f"rung_{name}", 470, y, 620, y, color=CHALK, zone=z, lw=3.4)
        b.text(f"lab_{name}", name, 630, y - 16, color=CHALK, size=22, max_w=80, zone=z)
    b.at("3.24", 435.6)
    b.brace("hy", 450, 748, 892, color=CHALK, zone=z, width=14)
    b.text("hyL", "HY", 360, 800, color=CHALK, size=22, max_w=80, zone=z)
    b.text("vsig", "vs", 390, 700, color=CHALK, size=20, max_w=60, zone=z)
    b.at("3.25", 439.1)
    b.highlight("rung_CCC", until=535.8)
    b.highlight("lab_CCC", until=535.8)
    b.at("3.26", 440.3)
    b.text("lag", "lag", 720, 760, color=CHALK, size=20, max_w=80, zone=z)
    b.at("3.27", 442.7)
    b.text("qsplit", "quality split", 760, 820, color=CHALK, size=22, max_w=200, zone=z)

    b.at("3.28", 449.0)
    b.erase(zone="card")
    b.text("para_h", "Paramount", 640, 984, color=CHALK, size=22, max_w=280, zone=z)
    b.at("3.29", 454.1)
    b.text("para_v", "jumbo bonds slumped", 640, 1016, color=CHALK, size=20, max_w=360, zone=z)
    b.at("3.30", 457.4)
    b.text("pnote", "$41 bn (Levine)", 640, 900, color=CHALK, size=18, max_w=360, zone="note")
    b.at("3.31", 460.4)
    b.append("pnote", " / $52 bn (Markets Daily)")

    b.at("3.32", 472.7)
    b.text("ten_h", "10-yr", 1180, 968, color=CHALK, size=20, max_w=240, zone=z)
    b.at("3.33", 477.2)
    b.text("ten_v", "~5.23–5.24%", 1180, 1004, color=CHALK, size=20, max_w=280, zone=z)
    b.at("3.34", 482.4)
    b.text("ten_n", "near 24-yr high", 1180, 1036, color=CHALK, size=16, max_w=240, zone=z)

    b.at("3.35", 490.8)
    b.text("qmark", "?", 800, 680, color=CHALK, size=40, max_w=60, zone=z)
    b.arrow("downq", 660, 700, 660, 880, color=CHALK, zone=z)

    b.at("3.36", 495.5)
    b.arrow("red", 1064, 282, 1560, 360, color=CORAL, zone=z, lw=4)
    b.at("3.37", 503.6)
    b.rect("coral", 1508, 340, 380, 168, color=CORAL, zone=z, lw=3.2)
    b.text(
        "coralT",
        "Egan-Jones: disrupted borrowers — professional services, VC/LPs, mortgaged households",
        1522,
        356,
        color=CORAL,
        size=18,
        max_w=352,
        zone=z,
    )
    b.at("3.38", 508.6)
    b.text("redL", "compresses billable hours", 1120, 300, color=CORAL, size=20, max_w=360, zone=z)

    b.at("3.39", 511.3)
    b.rect("scen", 1088, 420, 400, 140, color=CHALK, zone="scen", style="dashed")
    b.text("scenh", "if AI succeeds", 1174, 438, color=CHALK, size=16, max_w=150, zone="scen")
    b.text("srow1", "builders' debt", 1174, 468, color=CHALK, size=16, max_w=150, zone="scen")
    b.text("srow2", "disrupted borrowers' debt", 1174, 500, color=CHALK, size=14, max_w=160, zone="scen")
    b.text("splus", "+", 1340, 468, color=CYAN, size=22, max_w=40, zone="scen")
    b.text("sminus", "−", 1340, 498, color=CORAL, size=22, max_w=40, zone="scen")
    b.at("3.40", 517.6)
    b.text("dminus", "−", 1410, 468, color=CYAN, size=22, max_w=40, zone="scen")
    b.text("dplus", "+", 1410, 498, color=CORAL, size=22, max_w=40, zone="scen")
    b.line("scol", 1384, 436, 1384, 548, color=CHALK, zone="scen", style="dashed", lw=2)
    b.text("scenh2", "if AI disappoints", 1394, 438, color=CHALK, size=14, max_w=150, zone="scen")

    b.at("3.41", 520.4)
    b.erase(zone="scen")

    b.at("3.42", 520.9)
    b.poly(
        "wrap",
        [
            (24, 16),
            (1468, 16),
            (1468, 288),
            (1904, 288),
            (1904, 530),
            (24, 530),
            (24, 16),
        ],
        color=CHALK,
        zone=z,
        lw=2.6,
    )
    b.text(
        "one",
        "one variable: does AI work as advertised?",
        48,
        486,
        color=CHALK,
        size=22,
        max_w=900,
        zone=z,
    )
    b.at("3.43", 525.2)
    b.text(
        "less",
        "less diversified than it looks",
        48,
        548,
        color=CHALK,
        size=22,
        max_w=700,
        zone=z,
    )

    b.at("3.44", 530.5)
    b.erase(zone="mini")
    b.erase(zone="note")
    b.shrink_to_t("thumb3")


def _section4(b: Board):
    left, right, recap = "s4l", "s4r", "recap"
    b.at("4.01", 535.8)
    b.text("overH", "For 'over' to show up", 40, 24, color=CORAL, size=30, max_w=640, zone=left)

    b.at("4.02", 540.3)
    for i, y in enumerate((88, 250, 430, 640)):
        b.text(f"num{i}", f"{i + 1}.", 40, y, color=CHALK, size=24, max_w=40, zone=left)
        b.line(f"rule{i}", 78, y + 28, 680, y + 28, color=CHALK, zone=left, lw=2.0, dur=0.3)

    b.at("4.03", 542.3)
    b.text("l1", "Fee cuts spread", 84, 80, color=CORAL, size=24, max_w=600, zone=left)
    b.at("4.04", 547.1)
    b.text(
        "l1n",
        "today: 1 contract (KPMG / Grant Thornton UK)",
        84,
        140,
        color=CHALK,
        size=18,
        max_w=600,
        zone=left,
    )
    b.at("4.05", 549.1)
    b.append("l1", ": audit, consulting, law, banking")

    b.at("4.06", 554.9)
    b.text("l2", "Widening lands on the right borrowers?", 84, 242, color=CORAL, size=22, max_w=600, zone=left)
    b.at("4.07", 558.8)
    b.text("l2n", "CCC > 1,000 bp", 84, 300, color=CHALK, size=18, max_w=600, zone=left)
    b.highlight("ccc_val")
    b.highlight("ccc_h")
    b.at("4.08", 560.8)
    b.append("l2n", "; sector breakdown: not available")
    b.at("4.09", 566.1)
    b.append("l2", " (labor-heavy services?)")

    b.at("4.10", 571.3)
    b.text("l3", "Prices trail inflation", 84, 422, color=CORAL, size=24, max_w=600, zone=left)
    b.at("4.11", 576.1)
    b.append("l3", " + forced sales")
    b.at("4.12", 580.4)
    b.text("mrate", "Mortgage rate 7.28%", 84, 480, color=CHALK, size=20, max_w=600, zone=left)
    b.at("4.13", 582.5)
    b.append("mrate", " (highest since Nov 2023)")
    b.at("4.14", 589.6)
    b.text("pay", "Sep payrolls +29,000", 84, 520, color=CHALK, size=20, max_w=400, zone=left)
    b.at("4.15", 592.6)
    b.text("unemp", "Unemployment 4.2%", 360, 520, color=CHALK, size=20, max_w=300, zone=left)
    b.at("4.16", 595.4)
    b.text("noai", "not attributed to AI", 84, 558, color=CHALK, size=20, max_w=400, zone=left)

    b.at("4.17", 598.5)
    b.text("l4", "Private marks", 84, 632, color=CORAL, size=24, max_w=600, zone=left)
    b.at("4.18", 601.0)
    b.append("l4", ": Apollo daily marks")
    b.at("4.19", 603.0)
    b.append("l4", ", $850 bn credit book")
    b.at("4.20", 605.1)
    b.append("l4", ", by end Oct")
    b.at("4.21", 608.6)
    b.link("tape", 200, 680, "ccc_val", color=CHALK, zone=left)
    b.highlight("ccc_val")

    b.at("4.22", 614.4)
    b.arc("g1", 130, 760, 26, math.pi, math.tau, color=CHALK, zone=left)
    b.line("g1n", 130, 760, 148, 742, color=CHALK, zone=left, lw=2.4)
    b.text("g1t", "KBRA (count-based) ~3.5%", 48, 800, color=CHALK, size=16, max_w=250, zone=left)
    b.at("4.23", 617.8)
    b.arc("g2", 500, 760, 26, math.pi, math.tau, color=CHALK, zone=left)
    b.line("g2n", 500, 760, 484, 742, color=CHALK, zone=left, lw=2.4)
    b.text("g2t", "Fitch (broader) ~6+%", 360, 800, color=CHALK, size=16, max_w=250, zone=left)
    b.at("4.24", 620.9)
    b.text("d1", "direction: ___", 48, 832, color=CHALK, size=16, max_w=240, zone=left)
    b.text("d2", "direction: ___", 360, 832, color=CHALK, size=16, max_w=240, zone=left)
    b.at("4.25", 622.1)
    b.line("gdiv", 330, 730, 330, 870, color=CHALK, zone=left, lw=2.2)

    b.at("4.26", 623.7)
    b.text("finH", "For the buildout lenders", 760, 24, color=CYAN, size=28, max_w=660, zone=right)
    b.at("4.27", 628.1)
    b.text("r1", "$60 bn placed without indigestion", 760, 100, color=CYAN, size=24, max_w=660, zone=right)
    b.at("4.28", 630.3)
    b.highlight("para_h")
    b.highlight("para_v")
    b.at("4.29", 632.4)
    b.text("r2", "if: Anthropic IPO happens", 760, 180, color=CYAN, size=24, max_w=660, zone=right)
    b.line("r2ul", 760, 214, 1120, 214, color=CYAN, zone=right, style="dashed", dur=0.4)
    b.highlight("equity")
    b.at("4.30", 634.5)
    b.append("r2", " → equity cushion")
    b.line("r2ul2", 1120, 214, 1320, 214, color=CYAN, zone=right, style="dashed", dur=0.35)
    b.at("4.31", 636.8)
    b.text("r3", "Quality split holds", 760, 260, color=CYAN, size=24, max_w=660, zone=right)
    for name in ("IG", "BB", "B", "CCC"):
        b.highlight(f"rung_{name}")
        b.highlight(f"lab_{name}")
    b.highlight("hy")
    b.at("4.32", 639.9)
    b.text(
        "r4",
        "Service firms refinance at stable spreads and maturities",
        760,
        330,
        color=CYAN,
        size=22,
        max_w=660,
        zone=right,
    )

    b.at("4.33", 650.6)
    b.brace("join", 720, 80, 420, color=CHALK, zone=right, width=18)
    b.at("4.34", 659.4)
    b.text("sameT", "same trade", 760, 460, color=CHALK, size=24, max_w=300, zone=right)

    b.at("4.35", 660.9)
    b.dim(zone=left)
    b.dim(zone=right)

    b.at("4.36", 662.0)
    b.text(
        "rec1",
        "'Over' = wider spreads, shorter maturities, harder refinancing",
        40,
        960,
        color=CORAL,
        size=26,
        max_w=1800,
        zone=recap,
    )
    b.at("4.37", 668.2)
    b.text(
        "rec2",
        "Buildout = ~$60 bn chip financing, market splitting by quality",
        40,
        1004,
        color=CYAN,
        size=26,
        max_w=1800,
        zone=recap,
    )
    b.at("4.38", 674.5)
    b.text(
        "rec3",
        "Referee = where widening lands, who can still roll",
        40,
        1046,
        color=CHALK,
        size=26,
        max_w=1800,
        zone=recap,
    )
