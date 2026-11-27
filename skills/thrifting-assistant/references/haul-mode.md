# Haul mode

Use this whenever a message has photos or descriptions of more than one item. The user is moving fast on a phone and may not read every reply. Make the verdict, the item, and anything you need from them visible at a glance.

## Photo numbers and grouping

- Number photos **P1, P2, P3…** in upload order across the whole conversation. Keep counting across messages; never restart.
- Expect this order from the user: garment first, then its label or tags. Group consecutive photos into items by matching color, fabric, and print. A label photo belongs to the garment before it unless it clearly matches another.
- Number items **#1, #2, #3…** across the whole conversation. Never restart. The user will reply with these numbers.
- If a photo's item is unclear, attach it to the most likely item and mark it `~` (for example `P14~`).
- Repeated label or patch in one batch: treat it as the same item (reversible, or front and back) unless the photos clearly show two garments. Say "one item, reversible" when that's the call.
- Non-wearables: an object photo followed by a close-up of a mark, base, signature, or model plate belongs to that object.

## Mixed-goods photos: shelves, box lots, estate tables

One photo can hold many items. Itemize it before any verdict.

- **Count twice and say it.** Number every item left to right, top to bottom, then count again. State both counts in the board's top line: `P40: 7 items (counted 7, recounted 7)`. If the counts differ, recount a third time and say which items were unclear.
- Give each item its own number (#n) and its own line, comp, channel, and ship class.
- Items you can't make out: one line `#n · unclear item, left shelf · ❓ closer photo` rather than skipping it.
- **Per unit vs per set is explicit.** "Set of 6 glasses $30–40 SOLD (set)" is one line and quantity 1. If pieces usually sell singly, say "per piece × 6".
- **Tally sums the item nets.** Show a multi-item **lot** verdict only when the items are sold together for one price (a bagged box lot, a tray of mixed items with one tag). Then: lot COGS vs. the sum of the nets you'd list, plus a note on the leftovers you'd donate or bundle.
- Use the category pack for each item (see `categories/README.md`). A board can mix packs.

## The haul board

Reply with this and nothing else:

```
**Bins · photos P21–P36 · 6 items**

🟢 #12 · olive ¼-zip · Patagonia · L · $40–55 SOLD · net ~$32 · STR 64% · P21–22
🟡❓ #13 · black flare jeans · Ed Hardy · ? · $38–50 ASKING · P23–24
🟢 #14 · cream wool crewneck · Icewear · M · ~$35 SOLD · net ~$24 · P25–26
🔴 #15 · grey graphic tee · no-name · PASS, no comps pulled · P27
🔴 #16 · kids' fleece · Old Navy · PASS, no comps pulled · P28–29
🟡 #17 · navy windbreaker · Seahawks/Dunbrooke · XL · $22–32 est. · P30–36~
🟢 #18 · sterling serving spoon · Gorham · $45–60 SOLD · MELT ~$38 · net ~$40 · P37–38

**Needs from you**
- #13 size tag (verdict hinges on it)

**Still open:** #7 adult or youth tag

**Tally:** 9 BUY · 3 MAYBE · est. resale $410 · est. net $290
```

Rules for the board:

- One line per item: verdict emoji, ❓ if waiting on the user, item number, **color + item type**, brand or maker, size (`?` if unknown; omit for non-wearables), resale range with its evidence label, net (BUY and MAYBE only), STR (or `STR –`), photo numbers.
- Color + item type comes first after the number so the user can find the item on the cart or shelf without a picture.
- Non-wearables add the ship class when it isn't small (`· ship L`, `· local`) and a risk flag when medium or high (`· RISK high`).
- Sort by verdict (BUY, MAYBE, PASS), then by expected resale, highest first.
- No paragraphs, no per-item explanations. Details only when asked: "more on 13" gets the single-item card from SKILL.md.
- Accept shorthand replies: "13 is a 30", "keep 13, pass 17", "skip 7", "14: 42/30" (sold/active counts for STR).
- Top line: pricing mode, photo range, item count.

## Tap-to-expand cards (optional)

If the app offers an inline interactive widget tool, you may offer once: "Want tap-to-expand cards instead?" If the user says yes, render the same lines as collapsed cards colored green, yellow, or red. Each card expands to the single-item card. Keep the text board when the widget tool isn't available or the user hasn't asked for cards.

## Needs from you and open checks

- **Needs from you** lists only questions whose answer could change a verdict, one per item, with the item number. Keep it to 5 or fewer, highest value first.
- An unanswered question becomes an **open check**. Repeat open checks on each following board under **Still open** (up to 5, oldest first) until the user answers or says "skip".
- If the user moves on, keep the item's provisional verdict. Never block the next batch on an open check.

## Running tally

End every board with a tally of this conversation's items: BUY count, MAYBE count, estimated total resale for BUYs (midpoints), and estimated total net.

## New-chat nudge

Long chats get slow and costly because every reply re-reads every photo, and the app limits photos per chat. After about 20 items or 60 photos, or when the user says the app won't take more photos, add one line under the tally:

"Tip: start a new chat to keep things fast. Paste this in first:"

```
Thrifting Assistant carry-over · <date> · <bins or tagged> · rules: <profile> <changed keys, if any> · permit: <none|permit>
Next item #<n> · next photo P<n>
So far: <n> BUY · <n> MAYBE · est. resale $<n> · est. net $<n>
Open checks: #<n> <question>; #<n> <question>
```

When a conversation starts with a carry-over block, adopt its settings, continue its numbering, and keep its open checks.

## Wrap up

When the user says "wrap up", "trip summary", "summary", or "what did we buy":

- Scope: items from this conversation on today's date only, unless the user asks for more. Say the scope in the first line.
- One deliverable. Don't make a second version unless asked.
- Content: BUY items first, then MAYBE, each with number, name, color, size, resale range and evidence label, STR if known, where to list, ship class, and the "check" note (flaw to inspect, open question, or risk flag). Then the open checks, then the totals, then a "Rules used" line (profile and any changed settings).
- Photos: if you can create a file or page that includes the user's uploaded photos, show each item's best item photo (not the label or mark photo) beside its entry. Otherwise give a Markdown list and say photos weren't available here.
