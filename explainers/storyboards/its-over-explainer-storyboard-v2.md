# Storyboard v2: "It's Over" vs. the AI Credit Stack

- **Script:** `its-over-explainer-locked.md` (locked 2026-10-03). One spoken sentence corrected 2026-10-11 (housing: ~4.3% is the long-run house-price increase, not CPI's); no other spoken word changed.
- **Audio:** `its-over-explainer-narration-onyx.mp3`, OpenAI tts-1-hd / onyx, 11:20.6 (680.6 s). Section 2's first audio chunk (1:26.5–5:05.6) was re-voiced 2026-10-11 for the corrected sentence, so rows 2.01–2.59 are re-timed from the new alignment (−2.1 to +1.0 s); rows 2.60 to the end moved +0.43 s; Section 1 is unchanged.
- **Word timings:** `its-over-word-timings.json` (whisper-1 word timestamps per TTS chunk, aligned to the locked text; see the report at the end).
- **Replaces:** `its-over-explainer-storyboard.md` (v1, left untouched). Revised per the Opus storyboard review (bc-6f006879), section 1.6, and the per-section notes.
- **Status:** storyboard only. No video rendered, nothing published.

## How to read this storyboard (rendering agent: read first)

### Timing
- Every time in the tables is the **start of the cue's first word** in the narration MP3, from `its-over-word-timings.json` (word-level alignment, 0.1 s). The first word of the quoted cue is the trigger word. Section start times are the first spoken word of each section.
- Column "s" is the same time in seconds from the start of the MP3. Use it, not mm:ss, when keying animation.
- Timing marks: no mark = the trigger word was matched directly in the transcript. ² = matched inside a run where the transcript wrote the word differently (usually a number such as "5.300" vs "5.3"); time taken from the paired transcript word, accurate to about ±0.3 s. ³ = not matched; time interpolated from the neighbouring matched words, accurate to about ±0.5 s.
- **Stroke speed rule:** text is written at 14 characters per second; a box, bar, axis or arrow takes 0.6 s; a bracket or underline 0.4 s. An element must finish before the clause that contains its cue ends. If it cannot at that speed, write it faster (never start it earlier). Nothing appears before its cue word.
- When two rows share a cue, they start together.

### Animation verbs (the only verbs used below)
- **draw**: a hand-drawn stroke reveals a shape (box, bar, axis, arrow, bracket, line, circle) along its path at the stroke speed above.
- **write**: text is hand-lettered left to right at 14 characters per second.
- **erase**: a quick wipe (0.3 s) removes the named elements completely. "Erase main" means everything on the board except the thumbnail slot T and any strip the section rules say to keep.
- **dim**: the element drops to 40% opacity and stays in place. Undim returns it to 100%. Dim is never used for the muted-gray credit-market bar (It's Over), which is always full opacity.
- **highlight**: the element's outline is redrawn 2× thicker in its own colour (chalk stays chalk) and it pulses once over 0.5 s, then stays thick until the row that ends it, or until the section ends.
- **slide**: an existing label moves in a straight line (0.6 s) to the named spot without being redrawn. If it changes colour, the colour change happens as it lands.
- **swell**: a dashed outline grows outward from an element to show a possible larger size. The original element does not change. Swell is used only for scenarios and is always dashed.
- **shrink-to-T**: the named group scales down smoothly (0.8 s) into the thumbnail slot T. Elements not named stay where they are or are erased as stated.
- **restore**: an enlarged copy of something already in T is drawn on the main board. T itself does not change.
- Shorthand in the tables: "Continue", "Label", "Cell …", "Side note", "Tray:" and "Box … text" all mean **write** at the stated spot (text is appended right after what is already there). "Plot point" means **draw** a small dot plus **write** its label. "Redraw" means **erase** the stated part, then **draw** its new version. "Undim" reverses **dim**.

### Line styles
- **Solid** = something that has happened or is reported.
- **Dashed** = a scenario, condition, hypothetical or "if". Dashed elements never shrink into T (unless the style notes below name an exception). They are erased before any shrink-to-T and at the end of their section at the latest.
- **Dotted** = something announced or planned but not done (It's Over: the possible IPO equity). Dotted stays dotted for the whole lesson. Nothing ever "turns solid".

## Visual style (locked: Khan Academy look)
- Dark digital blackboard (near-black, about #111418). Hand-drawn strokes in step with the voice. No talking head, no stock footage, no logos: company names are plain chalk text. On-screen text is labels and numbers only. Every figure on screen is in the locked script.
- **Chalk white (#F2F2F2):** structure, neutral labels, arrows, numbers that belong to neither side, all analysis prompts.
- **Coral (#FF6B5B): disrupted borrowers.** Egan-Jones channels, professional services, VC/LPs, mortgaged households, fee cuts, the "compresses billable hours" arrow (the script's "red arrow" is this coral, not a third colour).
- **Cyan (#4FC3F7): AI buildout financing.** Broadcom's banks, Anthropic and others, Amazon, AI chips, the ~$60 bn arrow, the dotted possible-equity box.
- **Muted gray (#8A9099, full opacity):** the shared credit-market bar only. It is never dimmed.
- **Dashed exception:** the Amazon → AI chips arrow is dashed because the locked stage direction says so (an off-balance-sheet structure, not a scenario). It is the only dashed element that stays on the board and goes into T.
- The CCC rung and CCC reading are **chalk**, never coral: the script says it can't tell how much of that stress sits with the disrupted borrowers.

## Board layout (zones)
- **T, the thumbnail slot:** top-right corner, 22% of board width × 24% of height. There is only one T. It holds at most one thumbnail at a time.
- **Main board:** everything outside T. Each section below says how it is divided.
- **Bottom strip:** the lowest 14% of the board, used in Section 3 for the credit-market bar and in Section 4 for the recap lines.

## Thumbnail slot T: rules
1. At 1.19 ("Hold that sentence") the Section 1 board shrinks-to-T. It is the "clash" reminder for Section 2.
2. At 2.67 ("picture a diagram") T is erased with the rest of the board. T stays empty for all of Section 3.
3. At 3.44 ("If you had to referee") the Section 3 diagram shrinks-to-T, replacing nothing (T is empty). Before the shrink, the dashed scenario marks are already gone (erased at 3.41), and the mini-stack and notes are erased (see 3.44).
4. T then stays for all of Section 4 and the final hold. In Section 4 its parts are highlighted when the narration cites them (rows 4.07, 4.21, 4.28, 4.29, 4.31). Nothing in T ever changes style: the equity box stays dotted.


## 1. The clash (starts 0:00.0, 0.00 s)

**Layout:** a vertical chalk divider splits the main board into a left half (Story 1, coral) and a right half (Story 2, cyan). The Lenders box sits bottom-centre, straddling the divider.
**Erase rule:** nothing is erased inside this section. At 1.19 the whole section board shrinks-to-T.

| ID | Time | s | Cue (trigger starts on the first word) | Action |
|---|---|---|---|---|
| 1.01 | 0:00.0 | 0.0 | "In the same week" | Draw the vertical chalk divider down the centre of the main board. |
| 1.02 | 0:05.0 | 5.0 | "pointing in opposite directions." | Draw two small chalk arrows at the top of the divider, pointing away from each other (left and right). |
| 1.03 | 0:12.6 | 12.6 | "The first story is research." | Write the left header in coral: "Story 1: research". |
| 1.04 | 0:14.7 | 14.7 | "On October 1st, 2026, Egan-Jones" | Left half, draw a coral card outline and write its first line (stage direction): "Egan-Jones Risk Commentary #220, 'It's Over' (Oct 1, 2026)." |
| 1.05 | 0:25.6 | 25.6 | "research and commentary, not a rating action." | Write the card's second line: "Research/commentary, not a rating action." |
| 1.06 | 0:28.2 | 28.2 | "No credit rating changed" | Draw a chalk underline under "not a rating action". Write a small chalk tag beside it: "rating: unchanged". |
| 1.07 | 0:32.3 | 32.3 | "not written by credit analysts." | Write a small chalk tag under the card: "not written by credit analysts". |
| 1.08 | 0:44.2 | 44.2 | "professional services fees," | Write coral bullet 1 under the card: "Professional services fees". |
| 1.09 | 0:46.4 | 46.4 | "venture capital, and housing." | Write coral bullet 2: "Venture capital". |
| 1.10 | 0:47.3 | 47.3 | "and housing." | Write coral bullet 3: "Housing". |
| 1.11 | 0:48.5 | 48.5 | "The second story is money moving." | Write the right header in cyan: "Story 2: money moving". |
| 1.12 | 0:51.6 | 51.6 | "Banks working with Broadcom" | Right half, draw a cyan box: "Broadcom's banks". |
| 1.13 | 0:53.7 | 53.7 | "60 billion dollars of fresh financing" | Draw a cyan arrow to the right from the box, labelled "~$60 bn". |
| 1.14 | 0:56.1 | 56.1 | "for AI chips," | Draw a cyan box at the arrow's end: "AI chips". |
| 1.15 | 0:57.1 | 57.1 | "for Anthropic and others." | Write under it in cyan: "(Anthropic and others)". |
| 1.16 | 1:00.3 | 60.3 | "Anthropic is aiming for an IPO" | Draw a cyan dotted-outline tag: "IPO: as soon as mid-Nov". Dotted = not done. |
| 1.17 | 1:08.0 | 68.0 | "Lenders are putting tens of billions" | Draw a chalk box bottom-centre: "Lenders". Draw a cyan arrow from it up to "Broadcom's banks", labelled "fund the buildout". |
| 1.18 | 1:17.1 | 77.1 | "lenders also fund." | Draw a coral arrow from "Lenders" up to the three coral bullets (ending on the bracket of bullets 1–3, not on the research card), labelled "also fund". |
| 1.19 | 1:18.8 | 78.8 | "Hold that sentence." | Shrink-to-T: the whole Section 1 board goes into T (the clash reminder). |

## 2. What "over" means in credit (starts 1:26.4, 86.41 s)

**Layout:** a **question strip** across the top of the main board (left of T) holds the two lender questions and "Whose cash flow does this hit?" for the whole section. Below it is the **channel area**.
**Erase rule:** at each channel header (2.08 Channel 1, 2.29 Channel 2, 2.35 Channel 3) erase the channel area. The question strip and T stay. At 2.50 ("So what would 'over' do") erase the question strip too and divide the main board into three columns. At 2.67 ("picture a diagram") erase everything, including T.

| ID | Time | s | Cue (trigger starts on the first word) | Action |
|---|---|---|---|---|
| 2.01 | 1:32.5 | 92.5 | "A lender cares about two things." | Question strip: write "A lender cares about:" in chalk. |
| 2.02 | 1:34.2 | 94.2 | "Will the borrower's cash flow pay" | Write "1. Paid back on time?" in chalk. |
| 2.03 | 1:37.3 | 97.3 | "And can the borrower borrow again" | Write "2. Can borrow again?" in chalk. |
| 2.04 | 1:44.6 | 104.6 | "whose cash flow does this hit?" | Write "Whose cash flow does this hit?" in **chalk** (not coral) at the right end of the strip. |
| 2.05 | 1:49.0 | 109.0 | ""faster horse versus new paradigm."" | Channel area: write two chalk labels side by side, "Faster horse" and "New paradigm", with "vs" between them. |
| 2.06 | 1:51.1 | 111.1 | "Incumbents use AI" | Under "Faster horse", write: "incumbents run existing operations faster". |
| 2.07 | 1:55.3 | 115.3 | "Egan-Jones thinks the winners" | Under "New paradigm", write: "very few people or none, agentic work around the clock". |
| 2.08 | 2:06.3 | 126.3 | "Now the first channel: professional services." | Erase the channel area. Write the coral header: "Channel 1: professional services". |
| 2.09 | 2:11.3 | 131.3 | "KPMG secured" | Write "KPMG" in chalk with a small role tag under it: "client". |
| 2.10 | 2:12.4 | 132.4 | "14 percent fee cut" | Begin the coral stage-direction card: "KPMG fee cut: 14%". |
| 2.11 | 2:13.6 | 133.6 | "from Grant Thornton UK," | Write "Grant Thornton UK" in chalk to the right of KPMG with a role tag: "firm (its revenue shrank)". Draw a thin chalk arrow from the firm to KPMG labelled "fee". |
| 2.12 | 2:15.0 | 135.0 | "from 416,000 dollars" | Card continues: "($416,000". Draw a coral bar at height 416,000. |
| 2.13 | 2:16.4 | 136.4 | "to 357,000," | Card finishes: " → $357,000)". Erase the top slice of the bar down to 357,000 and leave a dimmed coral outline of the removed slice. |
| 2.14 | 2:33.0 | 153.0 | "IBM shares fell 13 percent" | Write the second coral card (stage direction): "IBM: −13% in one day". |
| 2.15 | 2:36.0 | 156.0 | "worst session since 2000." | Card finishes: ", worst since 2000." |
| 2.16 | 2:38.2 | 158.2 | "Law, investment banking and engineering," | Write small coral tag "Law". |
| 2.17 | 2:39.0 | 159.0 | "investment banking and engineering," | Write small coral tag "Investment banking". |
| 2.18 | 2:39.3 | 159.3 | "and engineering," | Write small coral tag "Engineering". |
| 2.19 | 2:46.9 | 166.9 | "Picture a firm that bills by the hour." | Cushion mini-diagram (all chalk until stated): draw an "Hours" bar and, beside it, a "Revenue (the bill)" bar of equal height. |
| 2.20 | 2:49.1 | 169.1 | "If AI shrinks the hours," | The Hours bar shrinks: erase its top third and leave a dimmed coral outline where it was. |
| 2.21 | 2:53.2 | 173.2 | "the bill shrinks." | The Revenue bar shrinks the same way: erase its top third, leaving a dimmed coral outline of the old top. |
| 2.22 | 2:55.1 | 175.1 | "A fee cut is a revenue cut." | Write under the Revenue bar in coral: "fee cut = revenue cut". |
| 2.23 | 2:56.9 | 176.9 | "But the firm's debt doesn't shrink" | Write "Debt" in chalk beside the Revenue bar. |
| 2.24 | 2:59.4 | 179.4 | "The interest payment stays the same size." | Draw a chalk "Interest" bar next to Revenue, lower than the shrunken Revenue bar. Write "same size" under it. |
| 2.25 | 3:01.7 | 181.7 | "So the cushion between what the firm earns" | Draw a chalk bracket between the old (dimmed) Revenue top and the Interest top, labelled "cushion". |
| 2.26 | 3:04.2 | 184.2 | "gets thinner." | Redraw the bracket so it spans only the shrunken Revenue top to the Interest top. The cushion visibly narrows. |
| 2.27 | 3:07.1 | 187.1 | "notice who kept the savings." | Draw a coral arrow from the dimmed removed slice of the Revenue bar toward the right. |
| 2.28 | 3:08.7 | 188.7 | "The client." | Write the arrow's target label in chalk: "Client (KPMG)". |
| 2.29 | 3:09.9 | 189.9 | "Second channel: venture capital." | Erase the channel area. Write the coral header: "Channel 2: VC". |
| 2.30 | 3:13.2 | 193.2 | "if startups scale with far less human capital," | Write a coral label: "less human capital → capital matters less". |
| 2.31 | 3:24.1 | 204.1 | "leverage and returns compress," | Write a coral label: "leverage and returns compress". |
| 2.32 | 3:29.8 | 209.8 | "haven't priced that yet." | Write a coral label: "LPs: not priced?". |
| 2.33 | 3:32.6 | 212.6 | "speculative." | Draw a dashed chalk stamp: "speculative". |
| 2.34 | 3:33.8 | 213.8 | "It's an argument about the future," | Write under the stamp in chalk: "argument about the future". |
| 2.35 | 3:37.7 | 217.7 | "Third channel: housing," | Erase the channel area. Write the coral header: "Channel 3: housing (via mortgages)". Housing panel layout: price bars left, income-ratio bars centre, forced-sale chain along the bottom. |
| 2.36 | 3:45.1 | 225.1 | "rose 1.6 percent in the year to June," | Draw a coral bar: "Home prices +1.6% (yr to June)". |
| 2.37 | 3:47.4 | 227.4 | "against a long-run average increase" | Directly beside the coral home-price bar, draw a dashed chalk ghost bar (outline only, no fill) at ~4.3% height, labelled "Long-run house-price avg ~4.3%". It is part of the house-price comparison: the coral +1.6% bar sits well below it. Dashed here marks a reference benchmark, not an observed value (a named exception to the dashed-means-"if" rule); it is erased with the channel area at 2.50 and never reaches T. No separate long-run text label. |
| 2.38 | 3:51.3 | 231.3 | "while consumer prices rose 3.5 percent." | After a small gap (a separate comparison, not part of the house-price pair), draw a solid chalk bar: "CPI +3.5%". |
| 2.39 | 3:54.7 | 234.7 | "My arithmetic:" | Draw a chalk bracket between the tops of the home-price and CPI bars, labelled "real prices falling" with a small tag "(my arithmetic)". |
| 2.40 | 4:00.6 | 240.6 | "The median new home cost" | Write the chalk caption for the centre: "median new home ÷ median household income". |
| 2.41 | 4:01.7 | 241.7 | "4.7 times median household income in 2025," | Draw a coral bar: "2025: 4.7×". |
| 2.42 | 4:05.1 | 245.1 | "versus 3.6 times in 1984." | Draw a chalk bar to its left, shorter: "1984: 3.6×". |
| 2.43 | 4:09.1 | 249.1 | "about 60 percent of owner-occupied homes" | Write a chalk label: "~60% of owner-occupied homes have a mortgage". |
| 2.44 | 4:12.8 | 252.8 | "Their worry is the two-income household" | Bottom chain, coral: write "2 incomes, thin cushion". |
| 2.45 | 4:16.6 | 256.6 | "Disrupt one income," | Draw an arrow and write "1 income disrupted". |
| 2.46 | 4:18.0 | 258.0 | "forced sales over six to twelve months:" | Draw an arrow and write "forced sales (6–12 mo)". |
| 2.47 | 4:20.1 | 260.1 | "short-term downward pressure on prices," | Draw an arrow and write "short-term price pressure". |
| 2.48 | 4:23.1 | 263.1 | "long-run scarcity of urban land still holds." | Write a chalk note under the chain: "long run: urban land still scarce". |
| 2.49 | 4:26.7 | 266.7 | "That's forward-looking, and it's theirs." | Draw a dashed chalk stamp matching the VC stamp: "forward-looking (theirs)". |
| 2.50 | 4:29.5 | 269.5 | "So what would "over" do" | Erase the channel area and the question strip (T stays). Divide the main board into three columns. |
| 2.51 | 4:33.3 | 273.3 | "spreads, maturities, and refinancing?" | Write column header "Spread". |
| 2.52 | 4:34.1 | 274.1 | "maturities, and refinancing?" | Write column header "Maturity". |
| 2.53 | 4:34.1 | 274.1 | "and refinancing?" | Write column header "Refinancing". |
| 2.54 | 4:36.0 | 276.0 | "A spread is the extra yield" | Under "Spread": draw a chalk "Treasury yield" bar with a chalk block stacked on top labelled "spread". |
| 2.55 | 4:47.9 | 287.9 | "they demand more compensation." | Swell the spread block upward in dashed coral (the "if" case). |
| 2.56 | 4:50.9 | 290.9 | "Spreads widen." | Write in coral beside the dashed outline: "wider". |
| 2.57 | 4:52.4 | 292.4 | "Maturity is when the loan comes due." | Under "Maturity": draw a chalk timeline arrow and a long bracket on it labelled "loan term". |
| 2.58 | 4:58.8 | 298.8 | "they lend for shorter periods," | Draw a shorter dashed coral bracket under the long one (the "if" case). Dim the long bracket. |
| 2.59 | 5:02.1 | 302.1 | "Shorter is safer for the lender" | Write: "shorter = safer for lender, harder on borrower". |
| 2.60 | 5:05.6 | 305.6 | "Refinancing is where those meet." | Under "Refinancing": draw a chalk "old debt" box. (Sync anchor: this sentence starts audio chunk-02.) |
| 2.61 | 5:10.8 | 310.8 | "They roll it," | Draw a chalk arrow to a "new debt" box, labelled "roll it". |
| 2.62 | 5:14.9 | 314.9 | "If spreads are wider and terms are shorter" | Draw two dashed coral arrows from the Spread and Maturity columns into the join between the boxes. |
| 2.63 | 5:20.4 | 320.4 | "or doesn't happen." | Draw a dashed coral X over the roll arrow. |
| 2.64 | 5:22.3 | 322.3 | "That's when "over" would actually show up" | Write in chalk: "'over' shows up here". |
| 2.65 | 5:32.4 | 332.4 | "Egan-Jones attached no spreads or ratings" | Write a small chalk tag across the top of the columns: "no spreads or ratings attached". |
| 2.66 | 5:37.3 | 337.3 | "That was a mechanism, not a forecast." | Draw a chalk stamp across the three columns: "mechanism, not a forecast". |
| 2.67 | 5:44.6 | 344.6 | "picture a diagram." | Erase everything, including T. The board is blank. |

## 3. The financing stack (starts 5:47.0, 347.02 s)

**Layout (stage-direction diagram):** three columns (Lenders | Borrowers | What's financed) across the upper two-thirds; the dotted equity box above the Borrowers column; the mini-stack just right of the equity box; the **inset** (stage card, line chart, quality ladder) in the lower-left above the bar; the muted-gray credit-market bar in the bottom strip with three reading slots (left, centre, right); the separate coral box at the far right; the scenario box between the AI chips box and the coral box.
**Erase rule:** at 3.28 ("Second reading: Paramount") erase the stage card and the 860→1,007 line chart; keep the bar reading and the ladder. At 3.41 ("Either way") erase the dashed scenario box. At 3.44 erase the mini-stack and the small notes, then shrink-to-T the rest. The main board is then empty.

| ID | Time | s | Cue (trigger starts on the first word) | Action |
|---|---|---|---|---|
| 3.01 | 5:47.0 | 347.0 | "Let's walk the picture left to right." | Draw three empty chalk column outlines. |
| 3.02 | 5:49.1 | 349.1 | "On the left, the lenders." | Write column header "Lenders" (chalk). |
| 3.03 | 5:53.8 | 353.8 | "banks working with Broadcom" | Draw a cyan box in the left column: "Broadcom's banks". |
| 3.04 | 5:55.7 | 355.7 | "60 billion dollars of fresh AI chip financing." | Draw a thick cyan arrow stub out of "Broadcom's banks" toward the middle, labelled "~$60 bn chip financing". It stops short of the middle column. |
| 3.05 | 5:59.0 | 359.0 | "In the middle, the borrowers:" | Write column header "Borrowers" (chalk). |
| 3.06 | 6:00.6 | 360.6 | "Anthropic and others." | Draw a cyan box in the middle column: "Anthropic and others". The thick arrow extends and lands on it. |
| 3.07 | 6:02.8 | 362.8 | "no collateral terms, rate, or maturity," | Write a small chalk note under the box: "collateral / rate / maturity: not reported". |
| 3.08 | 6:11.0 | 371.0 | "what the money buys:" | Write column header "What's financed" (chalk). |
| 3.09 | 6:12.8 | 372.8 | "chips." | Draw a cyan box in the right column: "AI chips". Optional (your call; it goes beyond the stage direction): a thin unlabelled chalk connector from "Anthropic and others" to "AI chips". |
| 3.10 | 6:13.5 | 373.5 | "The second borrower box is Amazon." | Draw a second cyan box in the middle column: "Amazon". |
| 3.11 | 6:19.8 | 379.8 | "asset-light chip financing" | Draw a dashed cyan arrow from "Amazon" to "AI chips", labelled "asset-light". (Dashed here is the locked stage direction for an off-balance-sheet structure, not a scenario; it stays and goes into T.) |
| 3.12 | 6:21.3 | 381.3 | "keeps about 8 billion dollars off its books," | Add to the arrow label: "~$8 bn kept off books". |
| 3.13 | 6:28.2 | 388.2 | "Above the middle sits the equity layer." | Draw a dotted cyan box above the middle column and write its first line: "Possible public equity". |
| 3.14 | 6:31.8 | 391.8 | "an IPO as soon as mid-November," | Write inside the dotted box: "IPO targeted as soon as mid-Nov". |
| 3.15 | 6:34.0 | 394.0 | "valuation chatter up to about 2 trillion" | Write inside the dotted box: "valuation chatter up to ~$2 tn". |
| 3.16 | 6:39.3 | 399.3 | "Equity is paid after debt," | Beside the dotted box, draw a small chalk mini-stack of two labelled cells: "Equity: paid 2nd" and "Debt: paid 1st". Draw them side by side, not stacked, so position carries no meaning. |
| 3.17 | 6:46.2 | 406.2 | "An aim and a valuation rumor" | Write the last line inside the dotted box: "Not raised, so not a cushion yet." The box stays dotted. |
| 3.18 | 6:50.5 | 410.5 | "Now the bar underneath:" | Draw the wide muted-gray bar across the bottom strip: "The same credit market". |
| 3.19 | 6:57.5 | 417.5 | "First reading: the US CCC-and-lower spread," | Write reading 1 header in the bar's left slot (chalk): "CCC spread". |
| 3.20 | 7:02.2 | 422.2 | "closed September 30th at 1,007 basis points." | Reading 1 finishes: "1,007 bp (Sep 30)". Inset: draw the chalk stage-direction card "US CCC-and-lower OAS: 1,007 bp (Sep 30)". |
| 3.21 | 7:06.3 | 426.3 | "That's up from about 860" | Card finishes: ", from ~860 bp early Sep." Draw a small chalk line rising from "860" to "1,007" (two labelled ends; no axis values). |
| 3.22 | 7:10.0 | 430.0 | "the first print above a thousand" | Draw a chalk tick on the line at 1,000, labelled "first above 1,000 since Mar 2023". |
| 3.23 | 7:13.9 | 433.9 | "Odd Lots described the shape:" | Inset: draw a four-rung chalk ladder, top to bottom: "IG", "BB", "B", "CCC". |
| 3.24 | 7:15.6 | 435.6 | "high yield blowing out against investment grade," | Draw a chalk bracket around BB/B/CCC labelled "HY", facing IG, with "vs". |
| 3.25 | 7:19.1 | 439.1 | "CCCs blowing out" | Highlight the CCC rung in **chalk** (not coral). |
| 3.26 | 7:20.3 | 440.3 | "while single-Bs and double-Bs lag." | Write a small chalk tag by BB and B: "lag". |
| 3.27 | 7:22.7 | 442.7 | "That's a quality split." | Write beside the ladder: "quality split". |
| 3.28 | 7:29.0 | 449.0 | "Second reading: Paramount." | Erase the stage card and the line chart (keep reading 1 and the ladder). Write reading 2 header in the bar's centre slot: "Paramount". |
| 3.29 | 7:34.1 | 454.1 | "Paramount's jumbo M&A bonds slumped" | Reading 2 continues: "jumbo bonds slumped". |
| 3.30 | 7:37.4 | 457.4 | "Matt Levine sizes them at 41 billion" | Write a small chalk note under reading 2: "$41 bn (Levine)". |
| 3.31 | 7:40.4 | 460.4 | "Markets Daily at 52 billion," | Note continues: " / $52 bn (Markets Daily)". Both shown; neither is picked. |
| 3.32 | 7:52.7 | 472.7 | "Third reading: the base rate" | Write reading 3 header in the bar's right slot: "10-yr". |
| 3.33 | 7:57.2 | 477.2 | "around 5.23 to 5.24 percent" | Reading 3 continues: "~5.23–5.24%". |
| 3.34 | 8:02.4 | 482.4 | "near a 24-year high." | Write small note under reading 3: "near 24-yr high". |
| 3.35 | 8:10.8 | 490.8 | "The open question is how far down" | Draw a chalk "?" beside the ladder and a downward chalk arrow from IG toward CCC. |
| 3.36 | 8:15.5 | 495.5 | "Last, the red arrow on the right," | Draw a coral arrow starting at "AI chips" heading to the far right. |
| 3.37 | 8:23.6 | 503.6 | "The disrupted borrowers are businesses" | Draw the separate coral box at the far right: "Egan-Jones: disrupted borrowers — professional services, VC/LPs, mortgaged households". The coral arrow lands on it. |
| 3.38 | 8:28.6 | 508.6 | "are exactly what that AI will compress." | Label the coral arrow: "compresses billable hours". |
| 3.39 | 8:31.3 | 511.3 | "If the buildout succeeds," | Draw a small dashed chalk scenario box between "AI chips" and the coral box, with two rows ("builders' debt", "disrupted borrowers' debt") and a first column headed "if AI succeeds": a cyan "+" in row 1, a coral "−" in row 2. |
| 3.40 | 8:37.6 | 517.6 | "If it disappoints," | Add the second column, headed "if AI disappoints": a cyan "−" in row 1, a coral "+" in row 2. Both columns stay visible; nothing swaps. |
| 3.41 | 8:40.4 | 520.4 | "Either way," | Erase the dashed scenario box. |
| 3.42 | 8:40.9 | 520.9 | "both loans hinge on one variable:" | Draw a chalk bracket wrapping the cyan side and the coral box, labelled "one variable: does AI work as advertised?". |
| 3.43 | 8:45.2 | 525.2 | "A lender holding both" | Write under the bracket: "less diversified than it looks". |
| 3.44 | 8:50.5 | 530.5 | "If you had to referee" | Erase the mini-stack, the "not reported" note and the Paramount size note. Shrink-to-T the rest of the diagram (columns, boxes, arrows, dotted equity box, gray bar with its three readings, ladder, coral box and arrow, bracket). |

## 4. What would have to change for one side to be right (starts 8:55.8, 535.81 s)

**Layout:** two columns on the main board: left coral "For 'over' to show up", right cyan "For the buildout lenders". The bottom strip is reserved for the three recap lines. T holds the Section 3 diagram.
**Erase rule:** nothing is erased in this section. At 4.35 ("To recap") both columns dim and the recap strip is written. Hold the final frame (columns dimmed, recap lines, T) to the end of the audio at 11:20.6.

| ID | Time | s | Cue (trigger starts on the first word) | Action |
|---|---|---|---|---|
| 4.01 | 8:55.8 | 535.8 | "Start with Egan-Jones." | Write the left column header in coral: "For 'over' to show up". |
| 4.02 | 9:00.3 | 540.3 | "change in four ways." | Draw four empty numbered lines (1–4) under the coral header. |
| 4.03 | 9:02.3 | 542.3 | "First, the fee cut would have to stop" | Coral line 1: write "Fee cuts spread". |
| 4.04 | 9:07.1 | 547.1 | "is a single contract." | Write a chalk note under line 1: "today: 1 contract (KPMG / Grant Thornton UK)". |
| 4.05 | 9:09.1 | 549.1 | "repricing across audit, consulting, law and banking," | Line 1 continues: ": audit, consulting, law, banking". |
| 4.06 | 9:14.9 | 554.9 | "Second, the spread widening" | Coral line 2: write "Widening lands on the right borrowers?". |
| 4.07 | 9:18.8 | 558.8 | "CCCs are above a thousand," | Write a chalk note under line 2: "CCC > 1,000 bp". Highlight the CCC reading in T. |
| 4.08 | 9:20.8 | 560.8 | "I don't have a sector breakdown" | Note continues: "; sector breakdown: not available". |
| 4.09 | 9:26.1 | 566.1 | "labor-heavy service businesses." | Write after line 2: "(labor-heavy services?)". |
| 4.10 | 9:31.3 | 571.3 | "Third, housing would have to move" | Coral line 3: write "Prices trail inflation". |
| 4.11 | 9:36.1 | 576.1 | "and forced sales appear." | Line 3 continues: " + forced sales". |
| 4.12 | 9:40.4 | 580.4 | "the mortgage rate at 7.28 percent," | Write chalk number under line 3: "Mortgage rate 7.28%". |
| 4.13 | 9:42.5 | 582.5 | "the highest since November 2023." | Continue: " (highest since Nov 2023)". |
| 4.14 | 9:49.6 | 589.6 | "September payrolls added only 29,000," | Write chalk number: "Sep payrolls +29,000". |
| 4.15 | 9:52.6 | 592.6 | "unemployment rose to 4.2 percent." | Write chalk number: "Unemployment 4.2%". |
| 4.16 | 9:55.4 | 595.4 | "nothing in the data attributes that to AI." | Write a chalk note: "not attributed to AI". |
| 4.17 | 9:58.5 | 598.5 | "Fourth, private marks." | Coral line 4: write "Private marks". |
| 4.18 | 10:01.0 | 601.0 | "Apollo is moving to daily marks" | Line 4 continues: ": Apollo daily marks". |
| 4.19 | 10:03.0 | 603.0 | "850 billion dollar credit book" | Continue: ", $850 bn credit book". |
| 4.20 | 10:05.1 | 605.1 | "by the end of October," | Continue: ", by end Oct". |
| 4.21 | 10:08.6 | 608.6 | "what the public CCC tape already shows." | Draw a chalk connector from line 4 to the CCC reading in T, and highlight that reading. |
| 4.22 | 10:14.4 | 614.4 | "KBRA's count-based measure" | Draw chalk gauge 1: "KBRA (count-based) ~3.5%". |
| 4.23 | 10:17.8 | 617.8 | "Fitch's broader measure" | Draw chalk gauge 2, separate from gauge 1: "Fitch (broader) ~6+%". |
| 4.24 | 10:20.9 | 620.9 | "Track each one's direction." | Under each gauge write "direction: ___" with the blank left empty (no arrow, no value). |
| 4.25 | 10:22.1 | 622.1 | "Don't merge them." | Draw a short chalk vertical divider between the two gauges. |
| 4.26 | 10:23.7 | 623.7 | "Now the financing side." | Write the right column header in cyan: "For the buildout lenders". |
| 4.27 | 10:28.1 | 628.1 | "The 60 billion gets placed" | Cyan line 1: write "$60 bn placed without indigestion". |
| 4.28 | 10:30.3 | 630.3 | "Paramount's indigestion." | Highlight the Paramount reading in T. |
| 4.29 | 10:32.4 | 632.4 | "The Anthropic IPO happens," | Cyan line 2: write "if: Anthropic IPO happens" with a dashed cyan underline. Highlight the dotted equity box in T. It stays dotted. |
| 4.30 | 10:34.5 | 634.5 | "putting that equity cushion" | Line 2 continues: " → equity cushion" (still dashed underline). |
| 4.31 | 10:36.8 | 636.8 | "The quality split holds." | Cyan line 3: write "Quality split holds". Highlight the ladder in T. |
| 4.32 | 10:39.9 | 639.9 | "service businesses keep refinancing" | Cyan line 4: write "Service firms refinance at stable spreads and maturities". |
| 4.33 | 10:50.6 | 650.6 | "both sides can be right at once." | Draw a chalk bracket joining the two columns. |
| 4.34 | 10:59.4 | 659.4 | "the same trade." | Label the bracket: "same trade". |
| 4.35 | 11:00.9 | 660.9 | "To recap." | Dim both columns (T stays at full opacity). |
| 4.36 | 11:02.0 | 662.0 | "In credit, "over" means" | Recap strip, coral: write "'Over' = wider spreads, shorter maturities, harder refinancing". |
| 4.37 | 11:08.2 | 668.2 | "The buildout means about" | Recap strip, cyan: write "Buildout = ~$60 bn chip financing, market splitting by quality". |
| 4.38 | 11:14.5 | 674.5 | "And the referee is the data:" | Recap strip, chalk: write "Referee = where widening lands, who can still roll". Hold to the end of the audio (680.6 s). |

---

## What changed from v1 (Opus review, section 1.6)

1. **Equity box stays dotted in Section 4.** Row 4.29 highlights the dotted box in T and writes the IPO line as "if: …" with a dashed underline. Nothing turns solid anywhere. The dotted-means-not-done rule is in the legend.
2. **Section 3 rebuilt in narration order.** Lender box (3.03), arrow stub (3.04), borrower box with the arrow landing (3.06), AI chips (3.09; the thin connector is marked optional, your call). The equity box is written clause by clause and ends on "An aim and a valuation rumor" (3.13–3.17). The mini-stack reads "Debt: paid 1st" and "Equity: paid 2nd", side by side (3.16). The CCC rung is highlighted in chalk (3.25). The card and line chart are erased at "Second reading: Paramount" (3.28). The success and disappointment marks are both shown, dashed, in a two-column scenario box (3.39–3.40) and erased at "Either way" (3.41), so neither reaches T.
3. **The KPMG example teaches its punchline.** KPMG is tagged "client" and Grant Thornton UK "firm (its revenue shrank)" (2.09, 2.11). The arrow target is "Client (KPMG)" (2.28). The cushion diagram is built in seven steps on hours, bill, revenue cut, debt, interest, cushion and "gets thinner" (2.19–2.26), with a bracket instead of a gap.
4. **Boards and recurring elements managed.** The channel area is erased at each channel header (2.08, 2.29, 2.35). There is one thumbnail slot, T, with replace and erase rules (top of file). In Section 4, the CCC reading (4.07, 4.21), the Paramount reading (4.28), the dotted equity box (4.29) and the ladder (4.31) are highlighted in T as the lines that cite them are written. The Section 1 "also fund" arrow ends on the three coral bullets (1.18).
5. **Every element is keyed to its own word.** Every row has a time from word-level alignment, and the bundled v1 rows (1:26, 3:11, 3:45, 9:31, 9:57, 10:21, 11:00) are split into one row per element. The long-run house-price average is drawn as a dashed ghost bar beside the home-price bar, and CPI is a separate comparison (2.37–2.38; see the next section).

Other review notes also applied: the card's "not a rating action" clause is written on its own words (1.05); "not written by credit analysts" is labelled (1.07); "Whose cash flow does this hit?" is chalk, not coral (2.04); the housing caveat gets a dashed "forward-looking (theirs)" stamp matching the VC "speculative" stamp (2.49); "speculative" is written on its word (2.33); the 860 line and the 1,000 tick are keyed to their own words (3.21, 3.22); the ladder brackets HY against IG before singling out CCC (3.24–3.25); the KBRA and Fitch gauges are written on their names (4.22, 4.23), and the blank direction is defined as "direction: ___" (4.24); the Apollo-to-CCC-tape mechanism is drawn as a connector into T (4.21); the cyan header has its own cue (4.26); the recap lines are keyed to 11:02.0, 11:08.2 and 11:14.5 and go in a reserved strip (4.36–4.38); the muted-gray bar is never dimmed; the stroke-speed rule, the defined verbs and a zone plan are in the header. Hypothetical moves in the spread, maturity and refinancing columns (2.55, 2.58, 2.62, 2.63) are drawn dashed, so the dashed-means-"if" rule holds throughout.

## The "~4.3" long-run average (confirmed 2026-10-11)

**Confirmed by the user against the Egan-Jones source on 2026-10-11: the ~4.3% is the long-run average increase in house prices (Case-Shiller), not consumer prices.** The Oct 2 research packet and wire beats had placed "(long-run avg ~4.3%)" right after CPI, so every later file, including the locked script, read it as CPI's average. Both source notes are now corrected.

The locked script sentence now reads: "Case-Shiller's national home price index rose 1.6 percent in the year to June, against a long-run average increase they put at about 4.3 percent, while consumer prices rose 3.5 percent." That sentence's Section 2 audio chunk (chunk-01) was re-voiced with the same settings (tts-1-hd / onyx), the narration re-stitched (680.6 s, +0.43 s), and word timings re-aligned with whisper-1.

On the board, the separate "long-run average (per Egan-Jones)" text label is gone. Row 2.37 draws a dashed chalk ghost bar, "Long-run house-price avg ~4.3%", directly beside the coral Case-Shiller +1.6% bar, keyed to "against a long-run average increase". Row 2.38 draws the CPI +3.5% bar as a separate comparison, keyed to "while consumer prices rose 3.5 percent". The "My arithmetic" bracket (2.39) still compares home prices with CPI. Because the whole first Section 2 chunk was re-voiced, rows 2.01–2.59 were re-timed from the new word alignment (they moved between −2.1 and +1.0 s); rows 2.60 through 4.38 moved +0.43 s; Section 1 did not move.

