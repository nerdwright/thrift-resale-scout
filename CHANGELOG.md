# Changelog

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
