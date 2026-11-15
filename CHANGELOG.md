# Changelog

## 0.3.0 — 2026-11-14

First Claude plugin release. Ported from the Thrift Scout v0.2 ChatGPT project (`nerdwright/gpt-plugin-archive/thrift-assist`).

- Packaged as a skills-only Claude plugin named Thrifting Assistant by Nerdwright (`nerdwright-thrifting-assistant`): one skill, four references.
- Fees revalidated for November 2026. eBay's final value fee now counts sales tax in the fee base (net multiplier 0.853, was 0.864); athletic shoes at $150+ use 0.914.
- Buy rule (3×, $15 net), shipping labels, and tax rate are user-overridable in conversation.
- Added rack mode (one line per item), no-web-search fallback, out-of-scope handling, privacy and memory rules, and counterfeit handling (PASS, no listing help).
- Added `evals/` with five cases.
