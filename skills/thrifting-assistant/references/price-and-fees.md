# Search tiers, sell-through, and wearables net

Shared fees, comp labels, shipping classes, COGS, and the tiered buy rules live in `core-pricing.md`. Thresholds the user can change live in `settings.md`. This file keeps search tiers and the sell-through (STR) lookup, which apply to every category, plus the wearables-only fee math (Poshmark, Vinted, apparel shipping, sneakers).

US marketplace fees, checked November 2026 against eBay's selling-fees help page and Poshmark's and Vinted's published US fee rules. Fees change. Treat every formula here as an estimate and say so.

## Search tiers

Searching every item is slow and costly in a big haul. Match the effort to the item:

| Tier | When | What to do |
| --- | --- | --- |
| None | Obvious pass: generic or fast-fashion brand, kids' basics, heavy stains or damage, no-name graphic tees, mass-market decor, chipped everyday dishes | No search. Label "PASS, no comps pulled". |
| Quick | Likely buy or a clear mid-value item | One search (style code, or brand + model + size). Label the result SOLD, ASKING, or est. |
| Deep | Estimated resale $40+, collector value, frequently faked brand or repro-prone category, metal with melt value, or a verdict that hinges on the price | Look for sold comps specifically, up to three searches. Check the size and condition match. |

With web search available, single-item questions always get at least a quick search.

## Comps and hygiene

- Search the style code first (usually an exact match), then brand + model + size + condition.
- Prefer **SOLD** evidence: eBay sold or completed listings, Poshmark sold listings.
- **eBay sites:** prefer ebay.com. Sold results sometimes come back only through another eBay country site (for example ebay.de showing "US $14,85"). Those are often the same listings shown on another site. Use them, but say "via eBay.de" so the user isn't confused by the formatting.
- **Outliers:** a sold price under about 30% of the other comps' median is likely an auction, bundle, or damaged item. Drop it from the range or flag it as an outlier. Don't let it pull the range down.
- If only active listings turn up, label the range **ASKING** and estimate sold at about 60–80% of asking.
- Match comps on brand + model + size + condition. A size outlier or a flaw can halve the price; say so.
- Say when comps are thin (fewer than about 3 close matches). Sell-through is a number, not an impression: use the Sell-through section below.
- Sneakers: also check StockX or GOAT for a deadstock reference, then discount for used condition, box, and laces or insoles.
- Marketplace pages may block automated reading. If a page doesn't load, say so and use search snippets plus the quick links. Never fill gaps from memory. A price you didn't retrieve is "est.", never "SOLD".

## Sell-through (STR)

STR shows how fast an item sells: the share of recent listings that actually sold. It answers "will this move?", while net answers "is it worth it?". Use both.

**Formula:** STR = eBay sold (last ~90 days) ÷ (sold + currently active) × 100, rounded to a whole percent. Never use sold ÷ active; some tools do, and it reads much higher (104 sold / 301 active is 26% by this formula, not 35%).

**Bands and what they mean for buying** (reseller rule of thumb, not an eBay standard; these are the defaults, and the user can change them in `settings.md`):

| STR | Speed | Buying guidance |
| --- | --- | --- |
| 60%+ | Fast | Buy at normal margins, even slightly thin ones |
| 50–59% | Healthy | Buy if net clears the minimum |
| 30–49% | Moves, slower | Buy only if net clears the minimum comfortably |
| < 30% | Slow, crowded | Min profit doubles (slow factor); else MAYBE or PASS |

**When to look it up:** only items that are already BUY after the price and net rules. Do the quick filtering first, from photos and comps, and never spend an STR lookup on a MAYBE or a PASS; their lines show `STR –`. This applies to single items and haul boards alike. Haul boards: up to 6 BUYs per board, highest expected resale first; list the rest as "STR: skipped (limit)".

**How to get the counts, in this order:**

1. **The user's browser (preferred).** If Claude in Chrome tools (`mcp__claude-in-chrome__*`) are available in this conversation, possibly as deferred tools you load first, use them. A browser signed into eBay avoids eBay's bot checks.
   - Load the tools in one ToolSearch call: `tabs_context_mcp`, `tabs_create_mcp`, `navigate`, `find`, `get_page_text`, `browser_batch`, `tabs_close_mcp`, `list_connected_browsers`, `select_browser`.
   - Call `tabs_context_mcp` (createIfEmpty true). If exactly one browser is connected, use it. If several are connected and the tool asks you to choose, ask once with every connected browser as an option; if the user's own instructions name a preferred browser or device ID, list that one first marked (Recommended). Use the chosen browser for the rest of the conversation without asking again. If none is connected, go to step 3.
   - Open one new tab for the whole batch. For each item, in one `browser_batch`: navigate to the eBay sold URL, `find` "results count heading", navigate to the eBay active URL, `find` "results count heading". **One pair of searches per item, no more.** Don't run a second, broader search when counts are low; if sold is under 5, show the STR marked "thin" and leave the verdict alone.
   - Read the heading "N results for …". Parse "6,300+" as 6300 and mark the STR "~" (eBay rounds large counts). "0 results" or a "No exact matches found" notice means 0 for that side; if both are 0, STR is "n/a, no matches". If the heading is missing, the page may still be loading: wait a moment and read it once more.
   - Close the tab when done.
   - **Stop conditions:** a CAPTCHA, a "verify yourself" page, a sign-in page, or two failed tool calls. Never solve a CAPTCHA or sign in. If another connected browser exists, say "this browser got an eBay check" and offer to switch once; a browser that isn't signed into eBay usually gets the check. Otherwise write "STR: browser blocked (eBay check)" or "STR: browser not connected" and continue with the verdict. Retry once per board at most.
   - Only open ebay.com search and Seller Hub Research pages. Never click buy, bid, offer, watch, message, listing, or account controls. Put only item keywords in the URLs.
2. **Terapeak (optional).** If the user says their account has Seller Hub on, you may open `https://www.ebay.com/sh/research?marketplace=EBAY-US&keywords=KEYWORDS&dayRange=90&tabName=SOLD` in the same tab and read its sell-through %, total sold, and average sold price. If it redirects to a Seller Hub signup or landing page, skip it and use step 1's counts. Label Terapeak figures "Terapeak".
3. **No browser.** Write "STR: not checked (no browser)". Don't ask for screenshots in a haul. Accept counts if the user sends them anyway ("14: 42/30").

**Keywords for STR:** tighter than comp searches, so the counts match the item: brand + model + gender + size (for example `patagonia synchilla snap-t mens L`). For non-wearables: maker + pattern or model + item type (`gorham chantilly sterling serving spoon`). Brand-level STR is too broad; always add the model or pattern. Use the same KEYWORDS for sold and active. If the counts are clearly a whole category (thousands of loose matches for a size-driven item), say "broad" and treat the STR as rough. For uncommon sizes (2XL+, petite, tall), also note when that size makes up a much bigger share of active listings than of sold ones: it sells slower than the overall STR suggests.

**Display:**
- Single-item card: `STR 58% · 420 sold / 300 active · 90d · eBay (healthy)`. Add `~` when counts were rounded.
- Haul board: append `· STR 58%` after net. Use `· STR –` when not checked.

**Effect on the verdict:** apply the bands after the price and net rules. Slow STR (below the `slower` band, default < 30%) multiplies the minimum profit (or the bins minimum net) by the slow factor (default 2×); a BUY that no longer clears it drops to MAYBE. STR never overrides a fake-risk or condition PASS. When STR changes a verdict, say so in the verdict line ("BUY → MAYBE, STR 22%").

**Speed:** about 10–15 seconds per BUY item. Run the lookups after you've worked out the verdicts, then post the board once with STR included. Don't post a board and then a second update.

## Net per platform (US), wearables

For other categories use the eBay formula and shipping classes in `core-pricing.md`.

Defaults assume the buyer pays shipping on every platform, and $1 packaging per item. eBay charges its fee on the shipping the buyer pays too, so that comes out of the payout.

| Platform | Net estimate | Basis |
| --- | --- | --- |
| eBay, most clothing and shoes | price × 0.853 − $0.40 − 0.147 × shipping − $1 | 13.6% final value fee on the total sale, which includes shipping and sales tax (13.6% × 1.08 ≈ 14.7%), plus a $0.40 per-order fee ($0.30 if the order is $10 or less), plus packaging |
| eBay, men's or women's athletic shoes sold at $150+ | price × 0.914 − 0.086 × shipping − $1 | 8% final value fee on the total including shipping and tax (≈ 8.6%), no per-order fee, plus packaging |
| Poshmark, sale $15+ | price × 0.80 − $1 | 20% commission, plus packaging. Buyer pays shipping |
| Poshmark, sale under $15 | price − $2.95 − $1 | Flat fee, plus packaging. Buyer pays shipping |
| Vinted US | price − $1 | No seller fee; packaging only. Buyer pays a protection fee and shipping |

Default shipping estimates: $8 apparel, $10 bulky or heavy, $14 shoes. Packaging: $1. Use the user's numbers when given.

Platform notes for BEST PLATFORM:

- **eBay:** largest buyer pool; best for men's, workwear, vintage, sneakers, sports, uniforms, and anything searched by style code. With buyer-paid shipping, some buyers who filter for free shipping won't see it; suggest Best Offer to offset.
- **Poshmark:** strong for women's mall and premium brands; the 20% fee bites on higher prices.
- **Vinted US:** keeps 100% of the price, but a smaller US buyer pool means slower sales. Best for $15–$45 mall brands where speed matters less.

## Verdict by pricing mode

**Best realistic net** = the net on the channel whose comps support the price, not the highest price on any platform.

The thresholds come from the active rule set: the COGS tiers in `core-pricing.md`, as changed by the user in `settings.md`.

Bins mode (by the pound, no item prices):

- **BUY:** best realistic net ≥ the bins minimum net (default $15) **and** confidence Medium or High.
- **MAYBE:** net is close to the minimum, comps are thin, confidence is Low, no live price check was possible, or one answer from the user would decide it.
- **PASS:** net under the minimum, or condition kills the value. A high fake or repro risk gets a PASS **recommendation** after pricing (see `fakes-and-niche.md`).
- Then apply the STR effect, if STR was checked.
- No multiple. No "BUY at $X or less" ceilings. Don't ask for a price.

Tagged mode (each item priced):

- **COGS** = tag price × (1 + sales tax), or the tag price alone with a reseller permit.
- **Tier** from the COGS. **Multiple** = best realistic net ÷ COGS. **Profit** = net − COGS.
- **BUY:** multiple ≥ the tier's multiple **and** profit ≥ the tier's min profit **and** confidence Medium or High.
- **MAYBE:** close numbers, thin comps, Low confidence, no live check, or one answer would decide it.
- **PASS:** below the multiple or the min profit, or condition kills the value.
- Then apply the STR effect, if STR was checked.

Use the user's own rule when they give one (see `settings.md`).

## Worked examples

Illustrative numbers only; always search for real comps.

Tagged: Patagonia Synchilla Snap-T, men's M, good condition, tag $6.99. Suppose sold comps cluster at $40–$50; use $45.

- eBay: 45 × 0.853 − 0.40 − 0.147 × 8 − 1 = **$35.81**
- Poshmark: 45 × 0.80 − 1 = **$35.00**
- Vinted: 45 − 1 = **$44** if it sells at $45, but expect a slower sale
- COGS: 6.99 × 1.08 = **$7.55** → tier < $20 (3× / $15)
- Best realistic net: Poshmark $35 → 35 ÷ 7.55 = **4.6×**, profit $27.45 → BUY

> **PROFIT:** eBay ~$36 · Posh ~$35 · Vinted ~$44 (slow) · **4.6×** on COGS $7.55 · profit ~$27 (rule: default · tier <$20 (3× / $15), buyer-paid shipping, $1 packaging, fees as of Nov 2026)

Sell-through via the browser: `patagonia synchilla snap-t mens M` → sold 420, active 300 → 420 ÷ 720 = **58%** (healthy) → stays BUY.

> **SELL-THROUGH:** STR 58% · 420 sold / 300 active · 90d · eBay (healthy)

If the counts were 120 sold / 480 active → **20%** (slow). The min profit doubles to $30; profit $27.45 misses it → "BUY → MAYBE, STR 20%". At a $40 net (profit $32) it would stay BUY with a slow-seller note.

Bins: same jacket from the bins.

> **PROFIT:** eBay ~$36 · Posh ~$35 · Vinted ~$44 (slow) · clears $15 net (rule: default · bins $15 net, buyer-paid shipping, $1 packaging, fees as of Nov 2026)
