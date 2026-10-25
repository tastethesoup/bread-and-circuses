# Storyboard v2: The Long End Breaks Loose

- **Script:** `long-end-explainer-locked.md` (locked 2026-10-11). No spoken word changed.
- **Audio:** `long-end-explainer-narration-onyx.mp3`, OpenAI tts-1-hd / onyx, 13:50.8 (830.8 s).
- **Word timings:** `long-end-word-timings.json` (whisper-1 word timestamps per TTS chunk, aligned to the locked text).
- **Replaces:** `long-end-explainer-storyboard.md` (v1, left untouched). Revised per the Opus storyboard review (bc-6f006879), section 2.6, and the per-section notes.
- **Status:** storyboard only. No video rendered, nothing published.

## How to read this storyboard (rendering agent: read first)

### Timing
- Every time in the tables is the **start of the cue's first word** in the narration MP3, from `long-end-word-timings.json` (word-level alignment, 0.1 s). The first word of the quoted cue is the trigger word. Section start times are the first spoken word of each section.
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
- Dark digital blackboard (near-black, about #111418). Hand-drawn strokes in step with the voice. No talking head, no stock footage, no logos: names are plain chalk text. On-screen text is labels and numbers only. Every figure on screen is in the locked script.
- **Cyan (#4FC3F7): expected average short rate** (bottom block) and anything that moves it: expected hikes, growth, sticky inflation, the fed funds destination, the Fed path line.
- **Amber (#FFB74D): term premium** (top block) and anything that moves it: deficits, hyperscaler debt, buyback uncertainty, foreign official buyers stepping back, supply.
- **Chalk white (#F2F2F2):** everything else, including all of Section 4's plumbing and Section 5's household chain. Cyan or amber appear in Sections 3–6 only where a point maps back onto one of the two blocks (the Section 3 term-premium inset, the Section 5 dashed inflation-return arrow, which is cyan, and the Section 6 line 1 labels).
- "High yield" in Section 3 always means the auction's clearing yield and is written "High yield (clearing)", so it is not confused with junk credit in the companion lesson.

## Board layout (zones)
- **T, the thumbnail slot:** top-right corner, 22% of board width × 24% of height. Only one T. It holds the two-block yield bar from 2.46 to the end.
- **Main board:** everything outside T. Each section below says how it is divided.
- **Checklist strip:** the lowest 16% of the board. Used in Section 1 (four faint blank lines) and Section 6 (the checklist). It is empty in Sections 2–5.
- **Amplifier strip (Section 4 only):** a narrow column at the right edge below T, holding the three amplifier names.

## Thumbnail slot T: rules
1. T is empty until 2.46 ("so the destination is what counts"), when the two-block bar (bar outline, cyan bottom block and label, amber top block and label, the amber "?") shrinks-to-T. The path line, sorted labels and markers do not go into T.
2. T never changes after that. Its block proportions are fixed. Nothing grows or shrinks inside T.
3. Restores (3.47 and 6.03) draw an enlarged copy on the main board. The copy, and anything dashed drawn on it, is erased by the end of that section. T itself is unchanged.
4. T stays to the end of the audio (830.8 s), beside the checklist in the final hold.

## The four faint lines (decision)
The Section 1 preview lines (1.15) are erased with the rest of the Section 1 board at 2.01. They do not sit on screen through Sections 2–5. They are redrawn faint in the same position at 6.02 ("Ask four questions"), so the viewer recognises them.


## 1. The puzzle (starts 0:00.0, 0.00 s)

**Layout:** a horizontal chalk maturity axis across the middle (left = overnight, right = 30 years, with a small "maturity →" label). The "Mortgage" label sits **below the axis**, not on it. Week labels above the axis; Bessent tag top-left; the checklist strip at the bottom.
**Erase rule:** nothing is erased inside the section. At 2.01 erase the whole Section 1 board (including the four faint lines).

| ID | Time | s | Cue (trigger starts on the first word) | Action |
|---|---|---|---|---|
| 1.01 | 0:01.6 | 1.6 | "The Federal Reserve sets one interest rate:" | Draw the horizontal chalk maturity axis with the small label "maturity →". |
| 1.02 | 0:03.9 | 3.9 | "the overnight rate banks charge each other." | Draw a short stub at the left end of the axis: "Overnight rate (Fed sets)". |
| 1.03 | 0:08.2 | 8.2 | "10-year Treasury note," | Draw a point on the axis: "10-year". |
| 1.04 | 0:09.3 | 9.3 | "or a 30-year bond," | Draw a point further right on the axis: "30-year". |
| 1.05 | 0:10.9 | 10.9 | "or your mortgage." | Write "Mortgage" in a small chalk box **below** the axis, under the 10-year point, not on the axis and not connected. |
| 1.06 | 0:12.8 | 12.8 | "Those are set by buyers and sellers" | Draw one chalk bracket over the 10-year and 30-year points that also takes in the Mortgage box, labelled "set by buyers and sellers". |
| 1.07 | 0:21.5 | 21.5 | "The week of October 5th, 2026" | Write the date label above the axis: "Week of Oct 5, 2026". |
| 1.08 | 0:33.9 | 33.9 | "odds of one fell from around 70 percent" | Draw a small chalk gauge: "Oct hike odds: ~70% → ~25%" with a downward arrow. |
| 1.09 | 0:41.0 | 41.0 | "the 10-year yield touched 5.364 percent" | Over the 10-year point, draw an upward chalk arrow and write "5.364% intraday (Wed Oct 7)". |
| 1.10 | 0:45.1 | 45.1 | "a 24-year high." | Continue the label: ", 24-yr high". The puzzle is now visible: the odds arrow points down while the yield arrow points up. |
| 1.11 | 0:46.9 | 46.9 | "The 30-year sat around 5.7 percent," | Over the 30-year point, write "~5.7%". |
| 1.12 | 0:49.7 | 49.7 | "a range not seen since about 2002." | Continue: ", not seen since ~2002". |
| 1.13 | 0:54.2 | 54.2 | "Treasury Secretary Scott Bessent" | Write a small chalk tag: "Bessent:". |
| 1.14 | 0:56.4 | 56.4 | ""I can't control the bond market."" | Continue the tag: "'I can't control the bond market.'" |
| 1.15 | 1:03.3 | 63.3 | "four questions to ask" | Checklist strip: draw four faint (dimmed) numbered blank lines, 1–4. |

## 2. The two parts of a long yield (starts 1:11.9, 71.89 s)

**Layout:** the bar stands at the centre. Before 2.21, the left side holds Plan A/B and the cyan tags, and the right side holds the amber tags. From 2.21 the zones change: an **unsorted tray** along the top (left of T), a **"bottom block" column** left of the bar (cyan), a **"top block" column** right of the bar (amber). Labels are sorted into these columns, not onto the bar, so the bar stays readable. The cyan path line sits in a lower-left inset.
**Path line shape:** drawn in cyan over a horizontal span labelled "next 10 yrs". It rises to a level ("destination") and then runs flat. **No y-axis values, no numbers on the line** except the markers at 2.43 and 2.44.
**Erase rule:** at 2.01 erase all of Section 1. At 2.21 ("Here's the worked example") erase Plan A/B, the ≈ labels and both first tag sets (cyan and amber). Keep the bar, its block labels, the "rates ↑ → price ↓" stroke, the amber "?" and the path line. At 2.46 the bar shrinks-to-T and everything else in this section is erased.

| ID | Time | s | Cue (trigger starts on the first word) | Action |
|---|---|---|---|---|
| 2.01 | 1:11.9 | 71.9 | "Picture a 10-year yield as one bar" | Erase the Section 1 board. Draw a single vertical chalk bar outline at the centre, labelled "10-year yield". |
| 2.02 | 1:15.9 | 75.9 | "The bottom block is the expected average short rate." | Draw the bottom block filled cyan, labelled "Expected average short rate". No number. |
| 2.03 | 1:19.2 | 79.2 | "The top block is the term premium." | Draw the top block filled amber, labelled "Term premium". No number. |
| 2.04 | 1:26.3 | 86.3 | "You could buy a 10-year note," | Left side, write "Plan A: buy 10-year note". |
| 2.05 | 1:28.1 | 88.1 | "or you could lend overnight" | Write below it: "Plan B: lend overnight, roll daily for 10 yrs". |
| 2.06 | 1:33.9 | 93.9 | "expected to pay about the same," | Write a chalk "≈" between Plan A and Plan B. |
| 2.07 | 1:35.8 | 95.8 | "the 10-year yield should roughly equal" | Draw a cyan arrow to the bottom block, labelled "≈ average expected overnight rate". |
| 2.08 | 1:44.1 | 104.1 | "about the Fed's whole path," | Lower-left inset: draw the cyan path line (rises to a destination, then flat; no y-axis values). Write "whole path, not next meeting". |
| 2.09 | 1:48.2 | 108.2 | "What moves this block is inflation," | Write cyan tag "inflation" by the bottom block. |
| 2.10 | 1:51.2 | 111.2 | "growth, and anything that changes" | Write cyan tag "growth". |
| 2.11 | 1:51.7 | 111.7 | "anything that changes where the Fed" | Write cyan tag "Fed path / how long". |
| 2.12 | 1:58.9 | 118.9 | "Locking up money for ten years" | Highlight the amber top block. |
| 2.13 | 2:02.8 | 122.8 | "If rates rise, your note's price falls" | Draw a small chalk stroke on the amber block: "rates ↑ → price ↓". |
| 2.14 | 2:07.7 | 127.7 | "extra pay for holding long," | Write by the amber block: "extra pay for holding long". |
| 2.15 | 2:18.1 | 138.1 | "heavy government borrowing," | Write amber tag "heavy borrowing". |
| 2.16 | 2:19.5 | 139.5 | "big deficits," | Write amber tag "big deficits". |
| 2.17 | 2:20.9 | 140.9 | "uncertainty about inflation or policy," | Write amber tag "inflation / policy uncertainty". |
| 2.18 | 2:22.9 | 142.9 | "and fewer dependable buyers." | Write amber tag "fewer dependable buyers". |
| 2.19 | 2:26.9 | 146.9 | "it's estimated with models," | Write a small label by the amber block: "model-estimated". |
| 2.20 | 2:31.2 | 151.2 | "so I won't put a number on it." | Draw an amber "?" inside the top block. Continue the label: "; no number given". |
| 2.21 | 2:33.3 | 153.3 | "Here's the worked example." | Erase Plan A/B, the ≈ labels and both tag sets. Draw the column headers: "bottom block" (cyan) left of the bar, "top block" (amber) right of the bar. |
| 2.22 | 2:34.7 | 154.7 | "On October 7th the Fed released minutes" | Tray: write the header "Fed minutes (Oct 7)". |
| 2.23 | 2:41.4 | 161.4 | "expected Fed hikes," | Tray: write chalk label "Expected hikes". |
| 2.24 | 2:42.8 | 162.8 | "the AI build-out," | Tray: write chalk label "AI build-out". |
| 2.25 | 2:43.9 | 163.9 | "and solid growth." | Tray: write chalk label "Solid growth". |
| 2.26 | 2:48.2 | 168.2 | ""uncertainty related" | Tray: write chalk label "Buyback uncertainty". |
| 2.27 | 2:56.7 | 176.7 | "Expected hikes go in the bottom block;" | Slide "Expected hikes" into the bottom-block column; it turns cyan. |
| 2.28 | 3:01.5 | 181.5 | "Solid growth goes there too," | Slide "Solid growth" into the bottom-block column; it turns cyan. |
| 2.29 | 3:06.4 | 186.4 | "The AI build-out straddles both:" | Draw a chalk split line through the "AI build-out" label. |
| 2.30 | 3:08.9 | 188.9 | "growth is bottom block," | Slide a copy "AI build-out (growth)" into the bottom-block column; cyan. |
| 2.31 | 3:10.4 | 190.4 | "borrowing is top block." | Slide the rest, "AI build-out (borrowing)", into the top-block column; amber. The tray copy is gone. |
| 2.32 | 3:12.3 | 192.3 | "Buyback uncertainty is pure top block." | Slide "Buyback uncertainty" into the top-block column; amber. |
| 2.33 | 3:20.0 | 200.0 | "Michael Cembalest of J.P. Morgan" | Tray: write the header "Cembalest (Oct 8)". |
| 2.34 | 3:25.2 | 205.2 | ""sticky inflation," | Tray: write "Sticky inflation". |
| 2.35 | 3:26.3 | 206.3 | "hyperscaler debt issuance" | Tray: write "Hyperscaler debt". |
| 2.36 | 3:28.2 ² | 208.2 | "US GDP growth above expectations."" | Tray: write "GDP above expectations". |
| 2.37 | 3:31.6 | 211.6 | ""for the first time since 1970," | Tray: write "Deficit > 5% of GDP in an expansion (first since 1970)". |
| 2.38 | 3:42.0 | 222.0 | "Sticky inflation and strong growth" | Slide "Sticky inflation" into the bottom-block column; cyan. |
| 2.39 | 3:42.8 | 222.8 | "strong growth go in the bottom block." | Slide "GDP above expectations" into the bottom-block column; cyan. |
| 2.40 | 3:45.3 | 225.3 | "Hyperscaler debt, meaning" | Slide "Hyperscaler debt" into the top-block column; amber. |
| 2.41 | 3:49.6 | 229.6 | "and a big deficit go in the top block:" | Slide the deficit label into the top-block column; amber. |
| 2.42 | 3:52.3 | 232.3 | "more bonds competing for the same buyers." | Write under the top-block column: "more bonds, same buyers". |
| 2.43 | 4:01.5 | 241.5 | "futures still priced the fed funds rate" | On the cyan path line, draw a marker one year out: "fed funds 4.75% (futures)". |
| 2.44 | 4:07.0 | 247.0 | "most officials still saw another hike" | Draw a small cyan tick on the path before year end: "another hike by year end (most officials)". |
| 2.45 | 4:11.6 | 251.6 | "The Fed slowed the pace, not the destination." | Redraw the path's early slope flatter (erase the old slope); the flat destination level stays where it was. Write "pace slowed, destination same". |
| 2.46 | 4:17.9 | 257.9 | "so the destination is what counts." | Shrink-to-T the two-block bar (outline, both blocks and labels, the "?"). Erase everything else from this section. |

## 3. How Treasury sells debt (starts 4:21.6, 261.65 s)

**Layout:** before 3.16, a vertical **yield number line** on the left third (yield increases **upward**; label "yield ↑" at the top), and the bid-to-cover label and three buckets on the right two-thirds. From 3.16, the table fills the centre and the number line stays as a narrow strip at the left edge. From 3.47, the right half holds the enlarged term-premium copy and the holdings bars.
**Erase rule:** at 3.16 ("Here are this week's two") erase the bid-to-cover label and the buckets; keep the number line. At 3.47 ("Why do foreign official holders") erase the table and the number line. At 4.01 erase everything in this section, including the dashed outline and the enlarged copy.

| ID | Time | s | Cue (trigger starts on the first word) | Action |
|---|---|---|---|---|
| 3.01 | 4:24.1 | 264.1 | "The U.S. Treasury sells its bonds at auctions," | Write in chalk: "Treasury → auction → buyers". |
| 3.02 | 4:26.2 | 266.2 | "on a schedule," | Draw a small calendar tick labelled "on schedule". |
| 3.03 | 4:32.4 | 272.4 | "Start with the clearing yield," | Left third: draw the vertical yield number line, with "yield ↑" at the top (higher yield is higher up). |
| 3.04 | 4:33.9 | 273.9 | "called the high yield," | Write a label: "High yield (clearing)". |
| 3.05 | 4:35.6 | 275.6 | "compare it with the when-issued yield," | Draw a tick at the middle of the line: "When-issued". |
| 3.06 | 4:41.3 | 281.3 | "If the auction clears below when-issued," | Draw a tick below When-issued: "clears below = stopped through = strong". |
| 3.07 | 4:49.4 | 289.4 | "If it clears above," | Draw a tick above When-issued: "clears above = tailed = weak". |
| 3.08 | 4:54.1 | 294.1 | "bond prices and yields move in opposite directions," | Write a side note: "price ↑ ⇔ yield ↓". |
| 3.09 | 5:00.0 | 300.0 | "Next, the bid-to-cover:" | Right side: write "Bid-to-cover = $ bid ÷ $ sold". |
| 3.10 | 5:04.6 | 304.6 | "you judge it against recent auctions." | Continue: " (vs recent avg)". |
| 3.11 | 5:07.4 | 307.4 | "Then, who took it." | Draw three empty chalk bucket outlines. |
| 3.12 | 5:09.2 | 309.2 | "Indirect bidders are the bucket" | Label bucket 1: "Indirects (incl. foreign buyers, foreign central banks)". |
| 3.13 | 5:14.5 | 314.5 | "Direct bidders buy for their own accounts." | Label bucket 2: "Directs (own account)". |
| 3.14 | 5:16.1 | 316.1 | "Primary dealers are the banks" | Label bucket 3: "Dealers (hold what's left)". |
| 3.15 | 5:23.2 | 323.2 | "A big dealer share is a warning sign." | Write under Dealers: "big share = warning". |
| 3.16 | 5:26.0 | 326.0 | "Here are this week's two," | Erase the bid-to-cover label and buckets; move nothing. Draw the stage-direction table: a chalk grid, two empty columns, row labels "Size · High yield (clearing) · When-issued · Bid-to-cover vs. recent average · Indirects · Directs · Dealers". |
| 3.17 | 5:28.8 | 328.8 | "These figures come through secondary" | Write the table footnote: "via secondary trackers / relayed Reuters, citing Treasury results". |
| 3.18 | 5:37.1 | 337.1 | "Column one, the 10-year reopening:" | Write column 1 header: "10-year reopening, Wed Oct 7". |
| 3.19 | 5:39.1 | 339.1 | "39 billion dollars" | Cell Size: "$39 bn". |
| 3.20 | 5:39.9 | 339.9 | "at 5.300 percent," | Cell High yield: "5.300%". |
| 3.21 | 5:41.9 | 341.9 | "the highest 10-year auction yield since November 2000." | Continue the cell: " (highest since Nov 2000)". |
| 3.22 | 5:45.3 | 345.3 | "When-issued was 5.317," | Cell When-issued: "5.317%". On the number line, write "5.317" at the When-issued tick and "5.300" at the tick below it. |
| 3.23 | 5:48.1 | 348.1 | "so it stopped through by 1.7 basis points;" | Write the note: "stopped through 1.7 bp". |
| 3.24 | 5:51.3 | 351.3 | "a basis point is a hundredth" | Write a small footnote: "1 bp = 0.01 percentage point". |
| 3.25 | 5:54.4 | 354.4 | "Bid-to-cover 2.77," | Cell Bid-to-cover: "2.77". |
| 3.26 | 5:55.9 | 355.9 | "against a six-auction average of 2.54." | Continue: " vs 2.54 (6-auction avg)". |
| 3.27 | 5:59.5 | 359.5 | "Indirects 80.3 percent," | Cell Indirects: "80.3%". |
| 3.28 | 6:01.3 | 361.3 | "directs 17.1," | Cell Directs: "17.1%". |
| 3.29 | 6:02.9 | 362.9 | "dealers 2.5," | Cell Dealers: "2.5%". |
| 3.30 | 6:05.2 | 365.2 | "the smallest dealer share since" | Continue: " (smallest since post-crisis)". |
| 3.31 | 6:08.9 | 368.9 | "That's a strong auction." | Write the plain word "strong" under column 1 (no check mark). |
| 3.32 | 6:11.0 | 371.0 | "Column two, the 30-year reopening:" | Write column 2 header: "30-year reopening, Thu Oct 8". |
| 3.33 | 6:12.9 | 372.9 | "22 billion dollars" | Cell Size: "$22 bn". |
| 3.34 | 6:14.2 | 374.2 | "at 5.618 percent," | Cell High yield: "5.618%". |
| 3.35 | 6:16.5 | 376.5 | "against 5.617 when-issued," | Cell When-issued: "5.617%". |
| 3.36 | 6:19.3 | 379.3 | "essentially right on it." | Write the note: "on it". |
| 3.37 | 6:20.8 | 380.8 | "Bid-to-cover 2.54," | Cell Bid-to-cover: "2.54". |
| 3.38 | 6:22.1 | 382.1 | "against an average of 2.41." | Continue: " vs 2.41 avg". |
| 3.39 | 6:24.4 | 384.4 | "Indirects 72.3 percent," | Cell Indirects: "72.3%". |
| 3.40 | 6:25.9 | 385.9 | "directs 20.9," | Cell Directs: "20.9%". |
| 3.41 | 6:27.2 | 387.2 | "dealers 6.8," | Cell Dealers: "6.8%". |
| 3.42 | 6:28.2 | 388.2 | "against an average of 10.3." | Continue: " vs 10.3 avg". |
| 3.43 | 6:32.1 | 392.1 | ""in line."" | Write the plain words "in line" under column 2. |
| 3.44 | 6:33.1 | 393.1 | "Decent, not spectacular." | Continue: ": decent". |
| 3.45 | 6:37.0 | 397.0 | "buyers showed up." | Draw a chalk bracket across both columns: "demand there". |
| 3.46 | 6:37.9 | 397.9 | "They just needed a higher yield." | Continue the bracket label: ", at a higher yield". |
| 3.47 | 6:39.3 | 399.3 | "Why do foreign official holders" | Erase the table and the number line. Restore an enlarged copy of the two-block bar from T on the right half, with the amber block emphasised (T is unchanged). |
| 3.48 | 6:45.2 | 405.2 | "are about the least price-sensitive buyers" | Write by the block: "foreign central banks = least price-sensitive buyers". |
| 3.49 | 6:49.1 | 409.1 | "If they step back," | Draw a dashed amber arrow from the label into the enlarged block, and swell the block upward with a dashed amber outline. |
| 3.50 | 6:54.9 | 414.9 | "that shows up in the term premium." | Write on the dashed outline: "if they step back". (The dashed outline is never copied into T.) |
| 3.51 | 6:57.8 | 417.8 | "Ray Dalio made exactly that argument" | Write a chalk quote tag: "Dalio:". |
| 3.52 | 7:02.1 | 422.1 | ""The Chinese don't want" | Continue the tag: "'The Chinese don't want to continue to accumulate.'" |
| 3.53 | 7:16.0 | 436.0 | "That's his view." | Write a small tag on the quote: "his view". |
| 3.54 | 7:18.2 | 438.2 | "come from a secondary relay:" | Write the footnote for the bars: "secondary relay". |
| 3.55 | 7:20.4 | 440.4 | "China around 618 billion dollars" | Draw a chalk bar: "China ~$618 bn (July)". |
| 3.56 | 7:24.0 | 444.0 | "Japan at 1.1 trillion," | Draw a taller chalk bar: "Japan $1.1 tn". |
| 3.57 | 7:25.6 | 445.6 | "down 12.8 billion." | Continue the Japan label: " (−$12.8 bn)". |

## 4. The plumbing that can amplify any move (starts 7:29.6, 449.65 s)

**Layout:** before 4.07, the whole main board. From 4.07: the four-box chain across the upper middle, the two-way switch under box 3, the dashed feedback loop in the lower half. The amplifier strip at the right edge (below T) collects "CTD switch", "crowded shorts" and "convexity hedging". From 4.30, the crowding board; from 4.42, the convexity board.
**Switch layout:** a horizontal lever pivoting under box 3. Left contact "Yields below 6%: shorter bond", right contact "Yields above 6%: longer bond". The solid lever points left (below), because the 30-year is around 5.7%.
**Erase rule:** at 4.01 erase all of Section 3. At 4.07 ("Here's the twist") erase the direction-vs-speed arrows, the futures labels and the duration arcs. At 4.30 ("Second amplifier") erase the chain, switch, loop, quotes and stamp. At 4.42 ("Third: convexity hedging") erase the crowding board. The amplifier strip stays until 5.01.

| ID | Time | s | Cue (trigger starts on the first word) | Action |
|---|---|---|---|---|
| 4.01 | 7:29.6 | 449.6 | "Everything so far explains" | Erase all of Section 3 (T stays). Write the header "Direction vs speed". Draw a short chalk arrow: "direction (Sections 2–3)". |
| 4.02 | 7:35.3 | 455.3 | "explains why they overshoot." | Draw a longer chalk arrow running past the short one: "overshoot (plumbing)". |
| 4.03 | 7:40.8 | 460.8 | "They hold Treasury futures," | Write: "Treasury future = contract to deliver a bond later". |
| 4.04 | 7:49.1 | 469.1 | "asset managers use them to hit a target duration." | Write: "used to hit a target duration". |
| 4.05 | 7:52.6 | 472.6 | "Duration measures how much" | Draw a short bond and a long bond, each with a price-swing arc. |
| 4.06 | 7:56.0 | 476.0 | "longer bonds have more of it." | Draw the long bond's arc bigger. Label: "duration". |
| 4.07 | 7:58.0 | 478.0 | "Here's the twist." | Erase the direction/speed arrows, futures labels and duration arcs. |
| 4.08 | 8:04.2 | 484.2 | "can deliver any bond from a basket," | Draw a basket of several chalk bond sticks, in the position where box 2 of the chain will be. |
| 4.09 | 8:06.9 | 486.9 | "naturally delivers the cheapest one." | Draw a chalk circle around one stick. |
| 4.10 | 8:09.4 | 489.4 | "That's the cheapest-to-deliver bond," | Label the circled stick: "cheapest-to-deliver (CTD)". |
| 4.11 | 8:11.5 | 491.5 | "and the future's price tracks it." | Continue: "; futures price tracks it". |
| 4.12 | 8:14.3 | 494.3 | "Read the chain from the left." | Draw the empty outline of box 1 to the left of the basket. |
| 4.13 | 8:21.2 | 501.2 | "It's priced off a fictitious 20-year Treasury" | Box 1 text: "Futures contract: notional 20-year, 6% bond". Draw the arrow from box 1 to the basket. |
| 4.14 | 8:25.2 | 505.2 | "bonds with 15 to just under 25 years" | Draw box 2's outline around the basket sketch (the sketch becomes box 2). Box 2 text: "Deliverable basket: 15 to under 25 years". |
| 4.15 | 8:30.2 | 510.2 | "Which end of that basket is cheapest" | Draw box 3, "Cheapest-to-deliver bond", with an arrow from the circled stick in box 2. Erase the earlier CTD label on the stick. |
| 4.16 | 8:33.1 | 513.1 | "relative to 6 percent." | Under box 3, draw the two-way switch: the two contacts and the solid lever pointing to "below". |
| 4.17 | 8:36.9 | 516.9 | ""When long-term Treasury interest rates are lower than 6%," | Write under the left contact: "→ acts like a 15-year contract". |
| 4.18 | 8:45.1 | 525.1 | "higher than 6%, it is a 25-year" | Write under the right contact: "→ acts like a 25-year contract". |
| 4.19 | 8:52.3 | 532.3 | "the current cheapest-to-deliver is the 2.5 percent" | Box 3 sub-label (solid): "now: 2.5% Feb 2045". |
| 4.20 | 8:57.8 | 537.8 | "sketched a scenario where" | Write a dashed-outline tag beside the switch: "scenario (Bloomberg)". |
| 4.21 | 9:01.1 | 541.1 | "switches it to a 2050 maturity." | Draw a dashed ghost lever pointing to "above" (the solid lever stays at "below"). Write dashed beside the sub-label: "→ 2050?". "now: 2.5% Feb 2045" stays. |
| 4.22 | 9:04.1 | 544.1 | "Then each contract carries more duration," | Draw box 4 (solid): "Contract's duration", with the arrow from box 3. Swell box 4 with a dashed outline labelled "more duration per contract". |
| 4.23 | 9:10.4 | 550.4 | "and sells futures." | Feedback loop (dashed chalk), step 1→2: dashed arrow from the swell to "managers sell futures". |
| 4.24 | 9:12.2 | 552.2 | "BNP Paribas strategists said" | Write a solid chalk quote tag: "BNP: 'could exacerbate the rise in long-end yields.'" |
| 4.25 | 9:21.8 | 561.8 | "unwind basis trades," | Loop step 3 (dashed): "(Levine) basis trades unwind, sell bonds". |
| 4.26 | 9:27.7 | 567.7 | "Selling pushes yields up," | Loop step 4 (dashed): "yields up". |
| 4.27 | 9:29.1 | 569.1 | "which brings the switch closer." | Loop step 5: dashed arrow from "yields up" back to the ghost lever, labelled "switch closer". |
| 4.28 | 9:32.6 | 572.6 | "managers would hold fewer contracts" | Draw a dashed chalk branch off the loop: "fewer contracts → total duration may not jump, could fall". |
| 4.29 | 9:39.1 | 579.1 | "It's a scenario, not a forecast." | Draw a chalk stamp: "scenario, not a forecast". |
| 4.30 | 9:41.8 | 581.8 | "Second amplifier: crowded positioning." | Erase the chain, switch, loop, quotes and stamp. Amplifier strip: write "1. CTD switch" and "2. crowded shorts". |
| 4.31 | 9:45.6 | 585.6 | "only through a secondary relay," | Write a small footnote: "secondary relay". |
| 4.32 | 9:47.7 | 587.7 | "Citi's David Bieber" | Write: "Citi (Bieber): 'extreme short'". |
| 4.33 | 9:51.8 | 591.8 | "Bank of America said short positions" | Write: "BofA: trend-followers' shorts 'near maximum'". |
| 4.34 | 9:57.5 | 597.5 | "Crowding cuts both ways." | Draw a two-headed vertical arrow: "crowding cuts both ways". |
| 4.35 | 10:00.9 | 600.9 | "bad news pushes yields up fast," | Label the upper head: "bad news: up fast". |
| 4.36 | 10:03.3 | 603.3 | "good news triggers sharp snapbacks" | Label the lower head: "good news: snapback". |
| 4.37 | 10:07.5 | 607.5 | "That fits this week's path:" | Draw a small vertical yield scale with no tick values. Points are spaced in proportion to 5.364, 5.28 and 5.35. |
| 4.38 | 10:09.7 ² | 609.7 | "5.364 intraday on Wednesday," | Plot point 1: "5.364% (Wed intraday)". Same wording as the Section 1 label. |
| 4.39 | 10:11.5 | 611.5 | "settled around 5.28," | Plot point 2, lower: "~5.28 (settle)", joined by a line. |
| 4.40 | 10:13.1 | 613.1 | "back to 5.35 on Thursday morning," | Plot point 3: "5.35 (Thu a.m.)", joined by a line. |
| 4.41 | 10:15.6 | 615.6 | "and lower again that afternoon." | Draw a down-arrow from the 5.35 point (no plotted point, no value): "lower (Thu p.m.)". |
| 4.42 | 10:18.0 | 618.0 | "Third: convexity hedging." | Erase the crowding board. Amplifier strip: write "3. convexity hedging". |
| 4.43 | 10:20.4 | 620.4 | "Some bond holdings get longer in duration" | Write: "some holdings get longer as rates rise". |
| 4.44 | 10:24.3 | 624.3 | "The classic case is mortgage bonds:" | Start the chain: write "mortgage bonds". |
| 4.45 | 10:26.4 | 626.4 | "when rates rise," | Chain: "rates ↑". |
| 4.46 | 10:27.5 | 627.5 | "fewer homeowners refinance," | Arrow: "fewer refinance". |
| 4.47 | 10:28.8 | 628.8 | "so the bonds pay back more slowly" | Arrow: "slower payback". |
| 4.48 | 10:30.5 | 630.5 | "and act like longer bonds." | Arrow: "longer duration". |
| 4.49 | 10:33.0 | 633.0 | "Holders rehedge by selling" | Arrow: "holders sell Treasuries/futures". |
| 4.50 | 10:35.5 | 635.5 | "which pushes rates higher still." | Draw the loop arrow closing back to "rates ↑". |
| 4.51 | 10:37.9 | 637.9 | "The same Bloomberg story named convexity hedging" | Write: "Bloomberg: convexity hedging + futures mechanics making it worse". |
| 4.52 | 10:44.3 | 644.3 | "without sizing either." | Attach to the Bloomberg label: "not sized". |
| 4.53 | 10:48.4 | 648.4 | ""negative convexity profile"" | Write a quote tag: "BNP: 'negative convexity profile'". |
| 4.54 | 10:54.5 | 654.5 | "None of these sets the direction." | Draw a chalk bracket around the three amplifier-strip names, labelled "not direction". |
| 4.55 | 10:56.2 | 656.2 | "They set the speed, and the overshoot." | Continue the bracket label: "speed + overshoot". |

## 5. How long rates reach households (starts 10:59.9, 659.93 s)

**Layout:** the stage-direction chain runs left to right across the middle: "10-year Treasury" → "30-year mortgage rate" → "Home buying and building" → "Rents" → "Inflation". Figures go under the box they belong to. The "30-year mortgage rate" box uses the same small boxed style as the Section 1 "Mortgage" label, and the arrow into it is the connection Section 1 left undrawn.
**Erase rule:** at 5.01 erase all of Section 4, including the amplifier strip. Nothing else is erased in this section. At 6.01 erase everything in it.

| ID | Time | s | Cue (trigger starts on the first word) | Action |
|---|---|---|---|---|
| 5.01 | 10:59.9 | 659.9 | "Why should anyone outside" | Erase all of Section 4 (T stays). |
| 5.02 | 11:03.1 | 663.1 | "The 10-year anchors the biggest loan" | Draw box 1: "10-year Treasury". |
| 5.03 | 11:09.2 | 669.2 | "mortgage rates are priced off the 10-year" | Draw the arrow and box 2: "30-year mortgage rate" (boxed like the Section 1 Mortgage label: mortgage is connected to the 10-year by a spread, not a point on the Treasury curve). |
| 5.04 | 11:11.1 | 671.1 | "plus a spread for the lender's costs" | Write under the arrow: "10-yr + lender spread". |
| 5.05 | 11:18.2 | 678.2 | "Freddie Mac's weekly survey" | Under box 2, write "Freddie Mac:". |
| 5.06 | 11:20.8 | 680.8 | "at 7.40 percent," | Continue: " 7.40%". |
| 5.07 | 11:22.5 | 682.5 | "up from 7.28 a week earlier" | Continue: " (7.28 last wk". |
| 5.08 | 11:24.8 | 684.8 | "and 6.30 a year ago." | Continue: ", 6.30 yr ago)". |
| 5.09 | 11:27.1 | 687.1 | "The Mortgage Bankers Association's measure," | Write below it: "MBA:". |
| 5.10 | 11:30.2 | 690.2 | "hit 7.49 percent," | Continue: " 7.49%, 3-yr high". |
| 5.11 | 11:33.0 | 693.0 | "up from 7.3." | Continue: " (from 7.3)". |
| 5.12 | 11:34.8 | 694.8 | "Two surveys, two numbers," | Write a chalk note: "two surveys, name the source". |
| 5.13 | 11:38.4 | 698.4 | "Next arrow, home buying." | Draw the arrow and box 3: "Home buying and building". |
| 5.14 | 11:41.1 | 701.1 | "a bigger monthly payment" | Under box 3: "bigger monthly payment". |
| 5.15 | 11:43.4 | 703.4 | "so buyers qualify for less," | "buyers qualify for less". |
| 5.16 | 11:45.3 | 705.3 | "and builders pay more to finance" | "builders' financing costs more". |
| 5.17 | 11:50.0 | 710.0 | "MBA purchase applications were down 13 percent" | "MBA purchase apps −13% y/y". |
| 5.18 | 11:53.4 | 713.4 | "on a four-week rolling average." | Continue: " (4-wk avg)". |
| 5.19 | 11:56.0 | 716.0 | "Then rents." | Draw the arrow and box 4: "Rents". |
| 5.20 | 11:59.6 | 719.6 | ""Higher Rates, Higher Rent Doom Loop."" | Write the chain label above: "Slok: Higher Rates, Higher Rent Doom Loop". |
| 5.21 | 12:07.0 | 727.0 | "Higher rents push inflation up," | Draw the arrow and box 5: "Inflation". |
| 5.22 | 12:09.1 | 729.1 | "higher inflation keeps rates high." | Draw a dashed **cyan** arrow curving from "Inflation" back to "10-year Treasury". Highlight the cyan block in T. |
| 5.23 | 12:14.0 | 734.0 | "It matters because owners' equivalent rent," | Write a chalk note under "Rents": "owners' equivalent rent". |
| 5.24 | 12:18.5 | 738.5 | "is about a quarter of the basket." | Continue: " ≈ ¼ of CPI basket". |
| 5.25 | 12:20.5 | 740.5 | "That's Slok's view." | Write a small tag on the chain label: "Slok's view". |
| 5.26 | 12:26.3 | 746.3 | "one reason rates could peak:" | Draw a chalk branch off the chain: "rates could peak". |
| 5.27 | 12:28.1 | 748.1 | "the same chain can slow the economy" | Continue the branch label: "← same chain can slow the economy". |

## 6. Close: a checklist, not a verdict (starts 12:32.6, 752.59 s)

**Layout:** the four checklist lines on the left of the main board (same positions as Section 1's faint lines, moved up to fill the board). A **side-note column** to the right of the lines holds the current line's prompts. A narrow **"this week" column** at the far right (left of T's edge, below T) holds the plain answer labels.
**Erase rule:** each line's side notes are erased when the next line is written (6.09, 6.13, 6.18, 6.22). Line text stays. The enlarged bar copy is erased at 6.09. Final hold: four lines, four plain answer labels, T. No check marks, no verdict text.

| ID | Time | s | Cue (trigger starts on the first word) | Action |
|---|---|---|---|---|
| 6.01 | 12:32.6 | 752.6 | "So next time long yields jump," | Erase all of Section 5 (T stays). |
| 6.02 | 12:36.4 | 756.4 | "Ask four questions." | Draw four faint (dimmed) numbered blank lines, 1–4, as in Section 1. |
| 6.03 | 12:38.1 | 758.1 | "One: which part moved?" | Write line 1 (undim): "1. Which part moved?". Restore an enlarged copy of the two-block bar from T in the side-note column. |
| 6.04 | 12:39.6 | 759.6 | "Is the expected path rising," | Write by the cyan block: "expected path" (cyan). |
| 6.05 | 12:44.1 | 764.1 | "Or is the term premium rising," | Write by the amber block: "term premium" (amber). |
| 6.06 | 12:47.1 | 767.1 | "supply, deficits or uncertainty?" | Continue the amber label: " (supply, deficits, uncertainty)". |
| 6.07 | 12:49.2 | 769.2 | "Fed minutes and futures pricing speak to the first;" | Continue the cyan label: " (Fed minutes, futures)". |
| 6.08 | 12:51.8 | 771.8 | "the second is much of what's left." | Write on the amber block: "≈ what's left". |
| 6.09 | 12:54.2 | 774.2 | "Two: how did the auctions go?" | Erase the enlarged bar copy and its labels. Write line 2: "2. How did the auctions go?". |
| 6.10 | 12:56.4 | 776.4 | "Did the sale tail or stop through" | Side note: "tail / stop-through vs when-issued". |
| 6.11 | 12:59.6 | 779.6 | "Was the bid-to-cover strong" | Side note: "bid-to-cover vs avg". |
| 6.12 | 13:02.3 | 782.3 | "Did indirect and direct buyers take" | Side note: "indirects + directs vs dealers". |
| 6.13 | 13:07.1 | 787.1 | "Three: is the plumbing adding to it?" | Erase line 2's side notes. Write line 3: "3. Is the plumbing adding to it?". |
| 6.14 | 13:09.6 | 789.6 | "Is the cheapest-to-deliver bond about to change?" | Side note: "CTD about to change?". |
| 6.15 | 13:13.4 | 793.4 | "Is duration extending?" | Side note: "duration extending?". |
| 6.16 | 13:15.1 | 795.1 | "Are shorts crowded," | Side note: "shorts crowded?". |
| 6.17 | 13:16.4 | 796.4 | "are convexity hedges adding sales" | Side note: "convexity hedges selling?". |
| 6.18 | 13:20.6 | 800.6 | "Four: are mortgages following?" | Erase line 3's side notes. Write line 4: "4. Are mortgages following?". |
| 6.19 | 13:22.8 | 802.8 | "Are mortgage rates moving with Treasuries?" | Side note: "mortgage rates vs Treasuries". |
| 6.20 | 13:24.9 | 804.9 | "Are purchase applications and construction weakening?" | Side note: "purchase apps + construction". |
| 6.21 | 13:27.6 | 807.6 | "Could less building put later pressure on rents?" | Side note: "later rent pressure?". |
| 6.22 | 13:30.5 | 810.5 | "The checklist won't tell you" | Erase line 4's side notes. Write the "this week" column heading: "this week". |
| 6.23 | 13:34.0 | 814.0 | "Our week had a strong 10-year auction," | Beside line 2, plain chalk label: "strong 10-yr auction". |
| 6.24 | 13:36.5 | 816.5 | "extreme short positioning," | Beside line 3: "extreme short". |
| 6.25 | 13:38.2 | 818.2 | "a Fed slowing its pace but not its destination," | Beside line 1, cyan: "pace slowed, destination same". |
| 6.26 | 13:41.3 | 821.3 | "and mortgage rates at multi-year highs," | Beside line 4: "multi-year highs". |
| 6.27 | 13:46.9 | 826.9 | "It tells you which part of the machine" | Final hold: four lines, four answer labels, T. No check marks, no verdict. Fade to a blank board at the end of the audio (830.8 s). |

---

## What changed from v1 (Opus review, section 2.6)

1. **Conditionals and scenarios are no longer drawn as facts.** "now: 2.5% Feb 2045" stays solid (4.19). The scenario tag, the ghost lever to "above", "→ 2050?" and the duration swell are all dashed (4.20–4.22), and the whole feedback loop is dashed (4.23–4.28). The 6:38 term-premium growth is a dashed swell on an enlarged copy (3.49–3.50), erased with the section, and T never changes (T rule 2). The 13:31 check marks are replaced by plain answer labels in a "this week" column (6.22–6.26). No check marks are used anywhere.
2. **Section 2: the reasoning comes before the answer.** Each minutes label is written on its own words (2.23–2.26). Each sort slides on its own sentence (2.27, 2.28, 2.30–2.32, and Cembalest 2.38–2.41) into flanking "bottom block" / "top block" columns, not onto the bar. "rates ↑ → price ↓" is drawn on the amber block at "If rates rise, your note's price falls" (2.13). Plan A/B and the first tag sets are erased at "Here's the worked example" (2.21). The path redraw is on "The Fed slowed the pace, not the destination" (2.45), and the 4.75% marker is on "futures still priced" (2.43).
3. **"Mortgage" is off the maturity axis.** It is a separate boxed label below the axis in Section 1 (1.05), inside the "set by buyers and sellers" bracket but not on the curve. Section 5 draws the "30-year mortgage rate" box in the same style and connects it to the 10-year with "10-yr + lender spread" (5.03–5.04).
4. **Section 4 cleaned up.** The basket sketch becomes box 2 (4.08, 4.14). Box 4 is drawn on "Then each contract carries more duration" (4.22). The loop is drawn step by step (4.22–4.27). There are erases at "Here's the twist" (4.07), "Second amplifier" (4.30) and "Third: convexity hedging" (4.42), with an amplifier strip that keeps the three names for the 10:54 bracket. "not sized" is on the Bloomberg sentence (4.52), not under BNP. The Thursday-afternoon move is a down-arrow with no plotted point (4.41).
5. **Renderable.** Word-level alignment for every row; a per-section erase rule; the four faint lines' persistence is decided (erased at 2.01, redrawn at 6.02); the verbs are defined in the header legend (slide, highlight, swell, dim, shrink-to-T, restore; "mini-icons" replaced by plain side-note text); each checklist line is written on its own "One/Two/Three/Four" (6.03, 6.09, 6.13, 6.18), so no line needs dimming; the dashed inflation-return arrow is cyan (5.22); and "not seen since ~2002" replaces "highest since ~2002" (1.12).

Other review notes also applied: one "set by buyers and sellers" bracket instead of three labels (1.06); the bar's blocks are keyed to their own sentences (2.02, 2.03); the path line's shape is specified with no y-axis values, and "another hike by year end" is a small marker (2.44); the number line's orientation is stated (yield increases upward, 3.03), with the stop-through and tail ticks on their own clauses (3.06, 3.07); the number line stays through the table, so 5.300 is marked below 5.317 at "When-issued was 5.317" (3.22); the buckets are written on their own words (3.12–3.15); "High yield (clearing)" is used throughout; the zigzag is spaced in proportion to 5.364, ~5.28 and 5.35 and reuses Section 1's "5.364%" wording (4.37–4.40); the Section 5 numbers are written on their own words (5.05–5.12); "Inflation" is drawn on "Higher rents push inflation up" (5.21); and the amber line-1 label includes "≈ what's left" (6.08).

