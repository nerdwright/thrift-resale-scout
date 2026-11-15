# Thrifting Assistant by Nerdwright

![Thrifting Assistant icon](.claude-plugin/icon.png)

Thrifting Assistant helps you discover the hidden gems.

Standing in a thrift store with a jacket in your hand, you need one answer fast: is this worth buying to resell? Thrifting Assistant gives Claude a reseller's checklist for clothing and shoes. Send a photo of the tag (or type the brand, size, condition, and tag price) and get a phone-sized answer:

- **VERDICT:** BUY, MAYBE, or PASS, with the reason
- **What it is:** brand, model, style code, era, size, material
- **Confidence**, plus the one next photo that would raise it
- **Resale range** from live searches, labeled sold comps or asking-only
- **Net profit** on eBay, Poshmark, and Vinted, and the multiple on your tag price
- **Best platform**, fake risk, value-killing flaws, and collector value
- **Quick links** to eBay sold, Poshmark sold, Vinted, StockX, and Grailed searches

Built by [Nerdwright](https://nerdwright.com) for US resellers. Product page: [nerdwright.com/products/thrifting-assistant](https://nerdwright.com/products/thrifting-assistant/). Version 0.3.0.

## Try it

- "Patagonia Synchilla snap-T, men's M, style 25450, good condition, $6.99 at Goodwill. Buy?"
- Upload a photo of a sneaker's inside tongue tag and say "$12, worth it?"
- "My rule is 4× and $20 net. Vintage Levi's trucker jacket, big E tag, size 40, $18."
- Upload a photo of a rack and ask "Anything here worth flipping?"

## Default buy rule

BUY needs a 3× multiple on the tag price, at least $15 net, and Medium or High confidence. Frequently faked brands need High confidence. Say your own rule ("my rule is 4× and $20 net") and Claude uses it for the rest of the conversation.

Fee math uses US fees as of November 2026: eBay 13.6% final value fee on the total including sales tax plus a $0.30–$0.40 per-order fee (8% and no per-order fee for athletic shoes at $150+), Poshmark 20% ($2.95 flat under $15), Vinted no seller fee. Fees change; the plugin labels every figure as an estimate. This is a buying aid, not financial advice.

## What this plugin runs, fetches, sends, and stores

- **Runs:** nothing. The plugin is instructions only: one skill and four reference files. No code, hooks, scripts, MCP servers, or connectors.
- **Fetches:** Claude uses its own built-in web search and web fetch, when they're turned on in your account, to read public marketplace and price pages.
- **Sends:** item details only (brand, model, style code, size, material) go into those searches and into the quick links. Photos stay in your conversation and are never sent to another service by the plugin. Nerdwright receives nothing.
- **Stores:** nothing. The plugin doesn't save finds, prices, or your buy rule, and asks Claude not to save them to memory unless you ask. Conversation retention follows your Claude account settings.
- **Links:** quick links open public search pages on ebay.com, poshmark.com, vinted.com, stockx.com, and grailed.com. Thrifting Assistant isn't affiliated with or endorsed by any of them.

## Limits

- It can't authenticate items from photos. It tells you which checks passed or failed and passes on likely fakes.
- Marketplace pages sometimes block automated reading. When that happens, Claude says so and gives you the links instead of guessing.
- Without web search, Claude can't check live prices; the verdict becomes MAYBE with links.
- Built for clothing and shoes in the US. Other categories and markets get a low-confidence best effort.

## Install

- **Claude directory:** search for Thrifting Assistant once it's listed.
- **Claude Code:** `/plugin marketplace add nerdwright/thrift-resale-scout`, then `/plugin install nerdwright-thrifting-assistant@nerdwright-thrifting-assistant`.
- **claude.ai upload:** Customize > Plugins > Add > Upload plugin, with a ZIP of this repository.

## Evals

`evals/` holds five cases for `claude plugin eval`. They need web access granted: `claude plugin eval . --allow-tools WebSearch,WebFetch`.

## Support

support@nerdwright.com · [Issues](https://github.com/nerdwright/thrift-resale-scout/issues)

## License

MIT. See [LICENSE](LICENSE).
