# Core pricing: comps, fees, channels, shipping, buy rules

Shared by every category pack. Wearable-only detail (Poshmark and Vinted math, apparel shipping, sneaker fees, STR lookup steps) stays in `price-and-fees.md`. Every number below is a **default**; the user's settings override it (see `settings.md`).

## Comp labels

Label every price, everywhere:

| Label | Means |
| --- | --- |
| **SOLD** | A sold or completed listing you retrieved in this conversation. |
| **ASKING** | Live listings only. Estimate sold at about 60–80% of asking. |
| **MELT** | Metal value: weight (ozt) × purity × spot. Spot must come from a source retrieved in this conversation, with its date ("spot $X/ozt, <source>, <date>"). |
| **est. MELT** | MELT with an estimated weight (no scale reading). Say how the weight was estimated. |
| **est.** | Your estimate, no usable comps. Never presented as a comp. |

Comp hygiene (all categories):

- Match comps on maker + model or pattern + size + condition. Say when comps are thin (fewer than ~3 close matches).
- Drop or flag any sold price under ~30% of the others' median (auction, bundle, damage).
- **Per unit vs per set is explicit.** A range is per piece unless it says "set of N". A set sold as one listing is quantity 1.
- Prefer ebay.com sold. Say "via eBay.<cc>" when sold results only came through another eBay site.
- A price you didn't retrieve is "est.", never SOLD. Never fill gaps from memory.

Purity factors for MELT: sterling .925, coin silver ~.900 (verify the mark), 800 silver .800, 14K .585, 18K .750, 10K .417. Silverplate, EPNS, "Sheffield" without sterling marks, and gold-filled/GF/RGP have **no** melt value worth pricing. Weighted sterling (candlesticks, some hollowware handles) is mostly filler: melt only the stated or reasonable net silver, and say so.

## eBay final value fee (no eBay Store)

Checked 2026-11-27 against eBay's "Selling fees" help page (ebay.com/help, id 4822). **Re-verify before each release and update this date.**

| eBay category | FVF |
| --- | --- |
| Most categories (incl. Pottery & Glass, Art, Collectibles, Home & Garden, Cameras, Consumer Electronics, Clothing) | 13.6% up to $7,500 per item, 2.35% above |
| Jewelry & Watches (except Watches, Parts & Accessories) | 15% if the sale is ≤ $5,000; 9% above |
| Watches, Parts & Accessories | 15% up to $1,000; 6.5% on $1,000–$7,500; 3% above |
| Women's Bags & Handbags | 15% if ≤ $2,000; 9% above |
| Books & Magazines, Movies & TV, Music (except vinyl) | 15.3% up to $7,500 |
| Coins & Paper Money > Bullion | 13.6% if ≤ $7,500; 7% above |

- The fee base is the **total sale**: item + shipping the buyer pays + sales tax.
- Per-order fee: **$0.40** for orders over $10, **$0.30** at $10 or less.
- The page does not list Pottery & Glass, Art, or Cameras separately; they fall under "most categories". If eBay later lists them, use eBay's number.

**eBay net formula** (buyer-paid shipping, tax rate *t* from settings, default 8%):

`net = price × (1 − f × (1 + t)) − f × (1 + t) × shipping − per-order fee − packaging`

Quick multipliers at t = 8%: 13.6% → price × 0.853, shipping × 0.147 · 15% → price × 0.838, shipping × 0.162 · 15.3% → price × 0.835, shipping × 0.165.

## Other channels

| Channel | Use for | Fee (est.) |
| --- | --- | --- |
| Poshmark | Wearables only | 20% at $15+; $2.95 flat under $15 (see `price-and-fees.md`) |
| Vinted US | Wearables | No seller fee (see `price-and-fees.md`) |
| Local (FB Marketplace, OfferUp, Craigslist) | Heavy, fragile, bulky, furniture, large framed art | No fee; no shipping; packaging $0 |
| Specialist auction house | High-end Asian art, export silver, textiles, fine art, important studio pottery | ~30% commission all-in (est.); slow (weeks to months) |

Say which channel the net assumes. If the best comps are from a specialist auction, compute net at 30% off and say "specialist channel, est.".

## Shipping classes

Buyer pays shipping; eBay's fee still applies to it. Use the class to estimate the shipping figure in the fee formula and the packaging cost.

| Class | Est. shipping | Packaging | Typical |
| --- | --- | --- | --- |
| small | $8 | $1 | Apparel, flatware, jewelry, small books, small electronics |
| medium | $15 | $3 | Shoes boxed, cameras with lens, small framed art, a few dishes, clocks under ~12 in |
| large | $30 | $6 | Big framed art, lamps, sets of dishes, mantel clocks, small appliances |
| local | — | — | Furniture, mirrors, oversized glass, anything over ~70 lb or too fragile to ship |

- Framed art, glass, and ceramics are **never small**: medium at minimum.
- Wearables keep their apparel defaults ($8 apparel, $10 bulky, $14 shoes, $1 packaging) from `price-and-fees.md`.
- Show it in PROFIT as `ship: medium`.

## COGS

**COGS** = all-in cost of the item = price paid × (1 + sales tax), unless the user has a reseller permit (see below). In bins mode there is no item price, so there is no COGS and no multiple.

For a group sold as one price (a $10 box of 6 ornaments), split COGS across the items you'd actually list, evenly unless one item clearly carries the value; say how you split it.

## Buy rules by COGS (defaults)

Tagged mode. The rule set is a **user setting**; these are the `default` profile. The rule names the tier from the item's COGS.

| COGS | Multiple (net ÷ COGS) | Min profit (net − COGS) |
| --- | --- | --- |
| < $20 | 3× | $15 |
| $20–$100 | 2× | $25 |
| > $100 | 2× | $100 |

- **Net** = the realistic payout after fees, shipping effect, and packaging on the best realistic channel.
- **Profit** = net − COGS.
- **BUY** needs the multiple **and** the min profit **and** Confidence Medium or High.
- **Slow sell-through** (STR below the slow threshold, default < 30%, on the item that carries ≥ 50% of the net) multiplies the min profit by the slow factor (default 2×).
- At 2× the > $100 tier's $100 floor never binds (2× COGS already leaves profit ≥ COGS > $100). That is intentional for now; see `settings.md` to try 1.75×.
- **Bins mode:** no tag price, so no multiple and no COGS. BUY needs net ≥ the bins minimum net (default $15, same as the < $20 tier's min profit). Slow STR doubles it.
- Always say the rule used in PROFIT: `rule: default · tier <$20 (3× / $15)`.

## Reseller permit

| Setting | COGS |
| --- | --- |
| `none` (default) | Price × (1 + sales tax) |
| `permit` | Price only; tax drops out |

When the permit would change the verdict (the item is within the tax amount of a threshold), show both: `COGS $8.64 (no permit) · $8.00 (with permit)`. In Washington a reseller permit requires a business license first; mention it once if the user asks how to get one, and point them to the Washington Department of Revenue rather than giving filing steps.

## Ask only what changes the verdict

| Category | The one question that usually matters |
| --- | --- |
| Metal | Weight in grams or ozt (a kitchen scale is fine) |
| Electronics, cameras, clocks | "Does it power on / run?" |
| Art | Photo of the signature and the back |
| Ceramics and glass | Photo of the base or mark, and any chips |
| Sets | How many pieces, and are any missing? |
