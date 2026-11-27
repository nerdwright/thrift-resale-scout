# Changelog

## 0.5.0 — 2026-11-27

Broadens the scope from wearables to general thrift and estate goods, and makes the buy rules a setting you can tune.

- **Category packs** in `references/categories/`: wearables, silver & metals, watches & jewelry, art & prints, ceramics & glass, holiday decor, electronics/cameras/clocks, household/cookware/tools, books & ephemera, Asian art & textiles, furniture (local only). Every pack uses the same six headings (ID cues, Fakes & repros, Value drivers, Value killers, Comps, Channel & ship) so other Nerdwright plugins can reuse them. `categories/README.md` routes items to a pack; no match falls back to a general workflow at Low confidence.
- **Shared core** (`references/core-pricing.md`): comp labels now include **MELT** and **est. MELT** (weight × purity × dated spot), eBay fees by category re-checked 2026-11-27 (13.6% most; 15% jewelry, watches up to $1,000, and women's handbags; 15.3% books; $0.40/$0.30 per order), local and specialist channels, shipping classes (small / medium / large / local; framed art, glass, and ceramics never small), COGS, and the reseller-permit setting.
- **Tiered buy rules by COGS** (tagged mode): < $20 3× and $15 profit · $20–$100 2× and $25 · > $100 2× and $100. Profit = net − COGS. COGS includes sales tax unless you have a reseller permit. Slow STR doubles the minimum profit. Bins mode is unchanged: $15 minimum net.
- **User-configurable rules** (`references/settings.md`): a `thrift_scout_settings` YAML block (project instructions, carry-over, or chat) sets tiers, profit basis, bins minimum, STR bands and slow factor, tax, permit, and shipping costs. Built-in profiles `default`, `legacy-0.4.5`, and `tight-high-end`. "What if…" and "compare A vs B" re-score a board without new searches. PROFIT always names the rule used.
- **Price, then flag:** likely fakes and repros are priced as if genuine (labeled), with a risk flag (none / low / medium / high + reason) and a PASS recommendation at high risk. Still never calls anything authentic and never helps list a likely fake as genuine. New non-wearable traps (jade vs soapstone, "Tiffany", export silver marks, Lladró lookalikes, luxury watches, prints sold as originals, Murano labels).
- **Single-item card:** new CATEGORY line, MELT inside RESALE for metals, SHIP CLASS and the rule inside PROFIT, BEST CHANNEL (was BEST PLATFORM), RISK in WATCH-OUTS.
- **Haul mode:** shelf, box-lot, and estate-table photos are itemized, counted twice with both counts stated, priced per unit or per set explicitly, and tallied by item net; a lot verdict only when items sell together.
- **Identify:** a general workflow for every category (category → every photo → marks → maker → era → material → condition).
- **Quick links:** category-scoped eBay links, price-guide and hallmark search links (links only), AbeBooks for books.
- **Description** now covers non-wearables and excludes listing requests and auction links (Listing Assistant and Auction Scout).
- **Behavior changes vs 0.4.5:** tagged multiples are measured against COGS (tag + 8% tax by default), and the minimum is profit (net − COGS) rather than net payout, so items near the 3× / $15 line can move from BUY to MAYBE. Use the `legacy-0.4.5` profile to reproduce 0.4.5 verdicts.
- **Evals:** 12 new cases (silver melt, jade vs soapstone, holiday shelf, Seiko watch, framed print, untested camera, reseller permit, Levi's regression, bins housewares, list-this handoff, settings what-if, settings block). Existing graders accept COGS-based multiples; the Jordan case now also checks it was priced and flagged.
- **Project instructions** (`instructions/thrifting-assistant-project.md`) regenerated for 0.5.0.

## 0.4.5 — 2026-11-20

From the first live STR test at the bins.

- **STR for BUY items only.** Quick filtering first; MAYBE and PASS items never get an STR lookup (`STR –`). Fast STR no longer lifts a MAYBE.
- **One pair of searches per item** (sold + active, same keywords). No second, broader search; sold under 5 is shown as "thin" and doesn't change the verdict. Keeps bulk hauls fast.

## 0.4.4 — 2026-11-20

Brings the plugin in line with the Thrifting project instructions (v0.4.1–v0.4.3) and adds fixes from the first live browser test.

- **Sell-through (STR)** in `references/price-and-fees.md`: STR = sold ÷ (sold + active), last ~90 days on eBay. Bands: 60%+ fast, 50–59% healthy, 30–49% slower, < 30% slow. Slow STR drops BUY to MAYBE unless net ≥ 2× the minimum; fast STR can lift a thin-comps MAYBE. New SELL-THROUGH line on the single-item card and `STR n%` on haul-board lines.
- **Automatic STR lookup through Claude in Chrome** for BUY items (and MAYBEs STR could flip), up to 6 per board, in one tab that's closed afterward. Stops on any CAPTCHA, verify, or sign-in page and never solves them. Only eBay search and Seller Hub Research pages.
- **Browser choice:** when several browsers are connected, ask once, list the user's named preferred browser first, and keep it for the conversation. If one browser gets an eBay check, offer to switch once.
- **Uncommon sizes:** note when 2XL+, petite, or tall makes up a bigger share of active than sold listings.
- **Formula guard:** explicitly never sold ÷ active (reads ~10 points high).
- **Buyer-paid shipping on every platform** (was seller-paid on eBay). eBay's fee now includes shipping (−0.147 × shipping); $1 packaging per item on all platforms; $10 estimate for bulky items. Worked examples updated.
- **Quick links:** eBay active link alongside eBay sold, using the same keywords.
- **Project instructions** are now generated from the plugin: `instructions/thrifting-assistant-project.md`, generated from the skill files. The plugin is the one source of truth.
- **Evals:** new `str-no-browser` case.

## 0.4.0 — 2026-11-15

From the first field test: about 90 items across a Value Village rack and a Goodwill bins haul.

- **Pricing mode.** Settles bins (by the pound) vs. tagged prices once per conversation. Bins is assumed when photos show no price tags. Bins verdicts use minimum net only: no tag-price questions, ceilings, or multiples.
- **Haul board** for batches (new `references/haul-mode.md`): one numbered line per item with 🟢 BUY / 🟡 MAYBE / 🔴 PASS, ❓ when waiting on the user, color and garment type, brand, size, resale and evidence label, net, and photo numbers (P1, P2… across the conversation). Details on request ("more on 12"). Optional tap-to-expand cards where the app supports interactive widgets.
- **Questions:** only ones that would change the verdict, collected in one "Needs from you" list. Unanswered ones carry forward under "Still open".
- **Running tally**, a new-chat nudge about every 20 items with a paste-in carry-over block, and a "wrap up" trip summary (today's items only, one deliverable, garment photos when available).
- **Search tiers:** no search for obvious passes ("no comps pulled"), one quick search for likely buys, deeper sold-comp checks for $40+, collectible, fake-risk, or close calls.
- **Comp hygiene:** prefer ebay.com, say when sold comps came via another eBay site, drop or flag outliers under ~30% of the median. A price not retrieved in the conversation is "est.", never SOLD.
- **No unsourced facts** about brands, eras, or companies in verdict notes.
- **Same-item detection** for front/back and reversible photos; ask about ambiguous price tags; restate dictation slips in one line.
- **Tag QR codes:** one decode attempt when code execution is available, then a flat, no-flash retake. Supporting evidence only.
- **Fixed verdict vocabulary** (BUY / MAYBE / PASS) everywhere, including summaries.
- **Scope** now names hats, bags, belts, swimwear, and kids' clothing. New hats and youth-sizing guidance.
- **README:** haul tips (shooting order, 12 MP, batch size, new chats), QR disclosure.
- **Evals:** three new cases (bins-mode, haul-board, reversible-one-item); verdict regexes accept the new color emoji.

## 0.3.0 — 2026-11-14

First Claude plugin release. Ported from the Thrift Scout v0.2 ChatGPT project (`nerdwright/gpt-plugin-archive/thrift-assist`).

- Packaged as a skills-only Claude plugin named Thrifting Assistant by Nerdwright (`nerdwright-thrifting-assistant`): one skill, four references.
- Fees revalidated for November 2026. eBay's final value fee now counts sales tax in the fee base (net multiplier 0.853, was 0.864); athletic shoes at $150+ use 0.914.
- Buy rule (3×, $15 net), shipping labels, and tax rate are user-overridable in conversation.
- Added rack mode (one line per item), no-web-search fallback, out-of-scope handling, privacy and memory rules, and counterfeit handling (PASS, no listing help).
- Added `evals/` with five cases.
