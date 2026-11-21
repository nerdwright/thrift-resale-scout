# Thrifting Assistant by Nerdwright

![Thrifting Assistant icon](.claude-plugin/icon.png)

Thrifting Assistant helps you discover the hidden gems.

You're at the bins or a thrift rack with a cart filling up, and you need fast answers: what is this, and is it worth flipping? Thrifting Assistant gives Claude a reseller's playbook for clothing, shoes, hats, and other wearables. Send photos of the garment and its tags, one item or a whole batch, and get answers sized for a phone.

**One item** gets a card:

- **Verdict:** 🟢 BUY, 🟡 MAYBE, or 🔴 PASS, with the reason
- **What it is:** brand, color, model, style code, era, size, material
- **Resale range** from live searches, labeled SOLD, ASKING, or est.
- **Net profit** on eBay, Poshmark, and Vinted
- Fake risk, value-killing flaws, collector value, and search links

**A batch** gets a numbered haul board:

```
🟢 #12 · olive ¼-zip · Patagonia · L · $40–55 SOLD · net ~$32 · P21–22
🟡❓ #13 · black flare jeans · Ed Hardy · ? · $38–50 ASKING · P23–24
🔴 #15 · grey graphic tee · no-name · PASS, no comps pulled · P27

Needs from you
- #13 size tag
Tally: 9 BUY · 3 MAYBE · est. resale $410 · est. net $290
```

Reply "more on 12" for details, "13 is a 30" to answer, or "wrap up" for a trip summary.

Built by [Nerdwright](https://nerdwright.com) for US resellers. Product page: [nerdwright.com/products/thrifting-assistant](https://nerdwright.com/products/thrifting-assistant/). Version 0.4.4.

## Try it

- "At the bins. Patagonia Synchilla snap-T, men's M, good shape. Grab it?"
- "Patagonia Synchilla snap-T, men's M, style 25450, $6.99 at Goodwill. Buy?"
- Upload 10 photos (each garment, then its label) and say "bins haul".
- "My rule is 4× and $20 net. Vintage Levi's trucker jacket, big E tag, size 40, $18."

## Bins or tagged prices

- **Bins (by the pound):** BUY means at least $15 net and Medium or High confidence. No price math per item. Claude assumes bins when your photos show no price tags, or when you say "bins".
- **Tagged:** BUY also needs 3× the tag price.
- Frequently faked brands need High confidence. Say your own rule ("my rule is 4× and $20 net") and Claude uses it for the rest of the conversation.

## Sell-through (STR)

After a quick first pass, Claude checks how fast each BUY item sells (MAYBE and PASS items are skipped, so bulk hauls stay fast): eBay sold in the last ~90 days ÷ (sold + active). 60%+ is fast, 50–59% healthy, 30–49% slower, under 30% slow. Slow sellers drop to MAYBE unless net is at least 2× your minimum.

STR needs Claude in Chrome connected to a browser that's signed into eBay, so the counts come from your own session without bot checks. It only opens eBay search pages and never clicks buy, bid, offer, or account controls. Without a connected browser, the card says "STR: not checked" and the verdict still goes out.

Shipping math assumes the buyer pays shipping on every platform, plus $1 packaging per item. Say "I offer free shipping" to change it.

Fee math uses US fees as of November 2026: eBay 13.6% final value fee on the total including shipping and sales tax plus a $0.30–$0.40 per-order fee (8% and no per-order fee for athletic shoes at $150+), Poshmark 20% ($2.95 flat under $15), Vinted no seller fee. Fees change; every figure is labeled as an estimate. This is a buying aid, not financial advice.

## Tips for a big haul

- **Shoot the garment, then its label, in that order.** Flip the label out into the garment shot when you can; one photo per item is faster and cheaper.
- **12 MP is plenty.** Claude shrinks large photos anyway. On iPhone, turn off 48 MP and ProRAW in Settings > Camera > Formats.
- **Send batches of 10–20 photos.** The Claude app takes up to 20 per message.
- **Start a new chat about every 20 items.** Long chats slow down and use more of your plan, because every reply re-reads every photo. Claude gives you a short carry-over block to paste so numbering and open questions continue.
- **Watch the ❓.** Those items are waiting on one answer from you. Unanswered questions stay listed under "Still open".

## What this plugin runs, fetches, sends, and stores

- **Runs:** nothing of its own. The plugin is instructions only: one skill and five reference files. No code, hooks, scripts, MCP servers, or connectors. If code execution is turned on in your Claude account, Claude may use it once to read a QR code on a garment tag in your photo.
- **Fetches:** Claude uses its own built-in web search and web fetch, when they're turned on in your account, to read public marketplace and price pages.
- **Sends:** item details only (brand, model, style code, size, material) go into those searches and into the search links. Photos stay in your conversation and are never sent to another service by the plugin. Nerdwright receives nothing.
- **Stores:** nothing. The plugin doesn't save finds, prices, or your buy rule, and asks Claude not to save them to memory unless you ask. Conversation retention follows your Claude account settings.
- **Links:** search links open public pages on ebay.com, poshmark.com, vinted.com, stockx.com, and grailed.com. Thrifting Assistant isn't affiliated with or endorsed by any of them.

## Limits

- It can't authenticate items from photos. It tells you which checks passed or failed and passes on likely fakes. A tag QR code that leads to the brand's site is supporting evidence only.
- Marketplace pages sometimes block automated reading. When that happens, Claude says so and labels the price "est." instead of guessing.
- Without web search, Claude can't check live prices; verdicts become MAYBE with links.
- Obvious passes get no price search, to keep big hauls fast. They're labeled "no comps pulled".
- Built for wearables in the US. Other categories and markets get a low-confidence best effort.

## Install

- **Claude directory:** search for Thrifting Assistant once it's listed.
- **Claude Code:** install it from the directory listing. See the [Claude Code plugin docs](https://code.claude.com/docs/en/plugins) for other install options.
- **claude.ai upload:** Customize > Plugins > Add > Upload plugin, with a ZIP of this repository.

## Evals

`evals/` holds eight test cases. They need web search and web fetch allowed. See the [Claude Code plugin docs](https://code.claude.com/docs/en/plugins) for how to run plugin evals.

## Support

support@nerdwright.com · [Issues](https://github.com/nerdwright/thrift-resale-scout/issues)

## License

MIT. See [LICENSE](LICENSE).
