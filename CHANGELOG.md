# Changelog

## 0.4.4 — 2026-11-20

Brings the plugin in line with the Thrifting project instructions (v0.4.1–v0.4.3) and adds fixes from the first live browser test.

- **Sell-through (STR)** in `references/price-and-fees.md`: STR = sold ÷ (sold + active), last ~90 days on eBay. Bands: 60%+ fast, 50–59% healthy, 30–49% slower, < 30% slow. Slow STR drops BUY to MAYBE unless net ≥ 2× the minimum; fast STR can lift a thin-comps MAYBE. New SELL-THROUGH line on the single-item card and `STR n%` on haul-board lines.
- **Automatic STR lookup through Claude in Chrome** for BUY items (and MAYBEs STR could flip), up to 6 per board, in one tab that's closed afterward. Stops on any CAPTCHA, verify, or sign-in page and never solves them. Only eBay search and Seller Hub Research pages.
- **Browser choice:** when several browsers are connected, ask once, list the user's named preferred browser first, and keep it for the conversation. If one browser gets an eBay check, offer to switch once.
- **Uncommon sizes:** note when 2XL+, petite, or tall makes up a bigger share of active than sold listings.
- **Formula guard:** explicitly never sold ÷ active (reads ~10 points high).
- **Buyer-paid shipping on every platform** (was seller-paid on eBay). eBay's fee now includes shipping (−0.147 × shipping); $1 packaging per item on all platforms; $10 estimate for bulky items. Worked examples updated.
- **Quick links:** eBay active link alongside eBay sold, using the same keywords.
- **Project instructions** are now generated from the plugin: `instructions/thrifting-assistant-project.md`, built by `tools/build_project_instructions.py`. The plugin is the one source of truth.
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
