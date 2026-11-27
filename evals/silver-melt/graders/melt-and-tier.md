---
type: llm
weight: 2
---

PASS if the reply (a) names the category as silver / metals, (b) shows a MELT or est. MELT figure with a spot price that is dated and attributed to a retrieved source (or says spot couldn't be retrieved and labels melt est.), (c) asks for the weight (or says weight would change the verdict), (d) applies the < $20 COGS tier (3× and $15 profit) to a COGS of about $6 plus tax, and (e) gives a verdict consistent with its own numbers (BUY only if net ≥ 3× COGS and profit ≥ $15).
FAIL if melt is missing, a spot price appears with no date or source, weight isn't mentioned, a different rule is applied without the user asking, or the verdict contradicts its own numbers.
