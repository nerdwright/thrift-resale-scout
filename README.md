# Thrifting Assistant by Nerdwright

![Thrifting Assistant icon](.claude-plugin/icon.png)

Thrifting Assistant helps you discover the hidden gems.

You're at the bins, a thrift shelf, or an estate-sale table with a cart filling up, and you need fast answers: what is this, and is it worth flipping? Thrifting Assistant gives Claude a reseller's playbook for clothing, shoes, and bags, plus housewares, silver, art, ceramics, glass, holiday decor, tools, electronics, clocks, and books. Send photos of the item and its tags or marks, one item, a batch, or a whole shelf, and get answers sized for a phone.

**One item** gets a card:

- **Verdict:** 🟢 BUY, 🟡 MAYBE, or 🔴 PASS, with the reason
- **What it is:** brand or maker, model or pattern, mark, era, size, material, and its **category**
- **Resale range** from live searches, labeled SOLD, ASKING, MELT (for metals), or est.
- **Net profit** on eBay, Poshmark, Vinted, or local, with a shipping class and the buy rule used
- Fake and repro risk flag, value-killing flaws, collector value, and search links

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

Built by [Nerdwright](https://nerdwright.com) for US resellers. Product page: [nerdwright.com/products/thrifting-assistant](https://nerdwright.com/products/thrifting-assistant/). Version 0.5.0.

## Try it

- "At the bins. Patagonia Synchilla snap-T, men's M, good shape. Grab it?"
- "Patagonia Synchilla snap-T, men's M, style 25450, $6.99 at Goodwill. Buy?"
- Upload 10 photos (each garment, then its label) and say "bins haul".
- "My rule is 4× and $20 net. Vintage Levi's trucker jacket, big E tag, size 40, $18."
- "Goodwill, $6: sterling serving spoon stamped Gorham. Buy?"
- One photo of a shelf of holiday decor: "what should I grab?"

## Bins or tagged prices

- **Bins (by the pound):** BUY means at least $15 net and Medium or High confidence. No price math per item. Claude assumes bins when your photos show no price tags, or when you say "bins".
- **Tagged:** the rule depends on what the item costs you all-in (COGS = tag price + sales tax):

  | COGS | Needs |
  | --- | --- |
  | under $20 | 3× and $15 profit |
  | $20–$100 | 2× and $25 profit |
  | over $100 | 2× and $100 profit |

- Slow sellers (sell-through under 30%) need double the profit.
- Have a reseller permit? Say so, and tax drops out of COGS.

## Tune the rules

Every threshold is a setting. Say your rule in chat ("my rule is 4× and $20 net"), switch profiles ("use legacy-0.4.5 rules"), or paste a block into your Claude Project instructions:

```yaml
thrift_scout_settings:
  profile: my-test
  buy_rules:
    tiers:
      - { cogs_below: 20,   multiple: 3,   min_profit: 15 }
      - { cogs_below: 100,  multiple: 2,   min_profit: 25 }
      - { cogs_below: null, multiple: 1.75, min_profit: 100 }
  str:
    bands: { fast: 60, healthy: 50, slower: 30 }
  costs:
    sales_tax_rate: 0.08
    reseller_permit: none
```

Ask "what if my rule were 2.5× and $12?" or "compare default vs legacy-0.4.5" and Claude re-scores the board without new searches, listing only the items whose verdict changes. Every PROFIT line names the rule it used. Full schema: `skills/thrifting-assistant/references/settings.md`.

## Fakes and reproductions

Claude prices a suspect item as if genuine (labeled "if genuine"), and as the likely alternative when clear (soapstone instead of jade, plate instead of sterling), then adds a risk flag (none / low / medium / high + why). High risk comes with a PASS recommendation. You decide. It never calls an item authentic and won't help list a likely fake as genuine.

## Sell-through (STR)

After a quick first pass, Claude checks how fast each BUY item sells (MAYBE and PASS items are skipped, so bulk hauls stay fast): eBay sold in the last ~90 days ÷ (sold + active). 60%+ is fast, 50–59% healthy, 30–49% slower, under 30% slow. Slow sellers drop to MAYBE unless profit clears double your minimum.

STR needs Claude in Chrome connected to a browser that's signed into eBay, so the counts come from your own session without bot checks. It only opens eBay search pages and never clicks buy, bid, offer, or account controls. Without a connected browser, the card says "STR: not checked" and the verdict still goes out.

Shipping math assumes the buyer pays shipping on every platform, plus $1 packaging per item. Say "I offer free shipping" to change it.

Fee math uses US fees as of November 2026: eBay 13.6% final value fee for most categories (15% jewelry, watches up to $1,000, and women's handbags; 15.3% books; 8% and no per-order fee for athletic shoes at $150+) on the total including shipping and sales tax, plus a $0.30–$0.40 per-order fee; Poshmark 20% ($2.95 flat under $15); Vinted no seller fee; local sales no fee. Shipping uses classes: small $8, medium $15, large $30 (plus $1 / $3 / $6 packaging), or local only for furniture and very fragile items. Fees change; every figure is labeled as an estimate. This is a buying aid, not financial advice.

## Tips for a big haul

- **Shoot the garment, then its label, in that order.** Flip the label out into the garment shot when you can; one photo per item is faster and cheaper.
- **12 MP is plenty.** Claude shrinks large photos anyway. On iPhone, turn off 48 MP and ProRAW in Settings > Camera > Formats.
- **Send batches of 10–20 photos.** The Claude app takes up to 20 per message.
- **Start a new chat about every 20 items.** Long chats slow down and use more of your plan, because every reply re-reads every photo. Claude gives you a short carry-over block to paste so numbering and open questions continue.
- **Watch the ❓.** Those items are waiting on one answer from you. Unanswered questions stay listed under "Still open".

## What this plugin runs, fetches, sends, and stores

- **Runs:** nothing of its own. The plugin is instructions only: one skill, seven reference files, and eleven category packs. No code, hooks, scripts, MCP servers, or connectors. If code execution is turned on in your Claude account, Claude may use it once to read a QR code on a garment tag in your photo.
- **Fetches:** Claude uses its own built-in web search and web fetch, when they're turned on in your account, to read public marketplace and price pages.
- **Sends:** item details only (brand, model, style code, size, material) go into those searches and into the search links. Photos stay in your conversation and are never sent to another service by the plugin. Nerdwright receives nothing.
- **Stores:** nothing. The plugin doesn't save finds, prices, or your buy rules or settings, and asks Claude not to save them to memory unless you ask. Conversation retention follows your Claude account settings.
- **Links:** search links open public pages on ebay.com, poshmark.com, vinted.com, stockx.com, grailed.com, abebooks.com, and google.com (price-guide and hallmark searches). Thrifting Assistant isn't affiliated with or endorsed by any of them.

## Limits

- It can't authenticate items from photos. It tells you which checks passed or failed, flags the risk, and recommends passing on likely fakes. A tag QR code that leads to the brand's site is supporting evidence only.
- Marketplace pages sometimes block automated reading. When that happens, Claude says so and labels the price "est." instead of guessing.
- Without web search, Claude can't check live prices; verdicts become MAYBE with links.
- Obvious passes get no price search, to keep big hauls fast. They're labeled "no comps pulled".
- Built for US resellers. Items outside the category packs get a low-confidence best effort, flagged. Online auction bidding and creating listings are out of scope (see Nerdwright's Auction Scout and Listing Assistant).
- Melt values need a spot price retrieved in the conversation and the item's weight; without weight, melt is an estimate.

## Install

- **Claude directory:** search for Thrifting Assistant once it's listed.
- **Claude Code:** install it from the directory listing. See the [Claude Code plugin docs](https://code.claude.com/docs/en/plugins) for other install options.
- **claude.ai upload:** Customize > Plugins > Add > Upload plugin, with a ZIP of this repository.

## Evals

`evals/` holds twenty test cases. They need web search and web fetch allowed. See the [Claude Code plugin docs](https://code.claude.com/docs/en/plugins) for how to run plugin evals.

## Support

support@nerdwright.com · [Issues](https://github.com/nerdwright/thrift-resale-scout/issues)

## License

MIT. See [LICENSE](LICENSE).
