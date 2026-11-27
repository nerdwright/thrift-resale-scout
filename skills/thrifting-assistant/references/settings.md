# Settings: user-configurable buy rules, STR, and costs

The buy rules, sell-through thresholds, and cost assumptions are settings, not constants, so the user can experiment to find the values that work for them. Read this file whenever the user states a rule, pastes a settings block, asks "what rules are you using", or asks a what-if ("what if it were 2.5×?").

## Where settings come from (highest wins)

1. **This conversation:** what the user says ("my rule is 4× and $20", "STR slow under 25%", "use legacy rules"). Applies for the rest of the conversation.
2. **A settings block** in the user's project instructions, a carry-over block, or a message: a fenced `yaml` block whose top key is `thrift_scout_settings`.
3. **Plugin defaults** (the `default` profile below).

Only the keys the user sets change; everything else keeps its default. When a message only says "my rule is 4× and $20 net", apply it to **every** COGS tier and to the bins minimum net (one flat rule), and say so once. Read "$20 net" or "$20 profit" in a flat rule as the minimum profit (net − COGS) unless the user says "payout" or picks `legacy-0.4.5`; state the reading in PROFIT. "Small-item rule" means the lowest COGS tier.

## Schema and defaults

```yaml
thrift_scout_settings:
  profile: default            # a label shown in PROFIT so experiments are traceable
  buy_rules:
    tiers:                    # tagged mode; first tier whose cogs_below the COGS is under
      - { cogs_below: 20,   multiple: 3, min_profit: 15 }
      - { cogs_below: 100,  multiple: 2, min_profit: 25 }
      - { cogs_below: null, multiple: 2, min_profit: 100 }   # null = no upper bound
    profit_basis: profit      # profit = net − COGS (default) | net = net payout, ignoring cost (0.4.x behavior)
    bins_min_net: 15          # bins mode: no COGS, net payout only
    min_confidence: Medium    # BUY needs at least this confidence
  str:
    bands: { fast: 60, healthy: 50, slower: 30 }   # % thresholds; below `slower` is slow
    window_days: 90
    slow_profit_factor: 2     # slow STR multiplies the min profit (and bins_min_net) by this
    lookup: buy_only          # buy_only | buy_and_close_maybe | off
    lookup_limit: 6           # per haul board
  costs:
    sales_tax_rate: 0.08      # used in COGS (no permit) and in eBay's fee base
    reseller_permit: none     # none | permit
    packaging: { small: 1, medium: 3, large: 6 }
    shipping:  { small: 8, medium: 15, large: 30 }
    wearables_shipping: { apparel: 8, bulky: 10, shoes: 14 }
  market: US
```

## Built-in profiles

The user can switch with "use <profile> rules".

| Profile | What it is |
| --- | --- |
| `default` | The table above (v0.5 tiered rules, profit = net − COGS, tax in COGS). |
| `legacy-0.4.5` | One flat rule: 3× and $15, `profit_basis: net`, `sales_tax_rate` still 8% for eBay's fee but **not** added to COGS (multiple = net ÷ tag price). Reproduces v0.4.5 verdicts. |
| `tight-high-end` | Same as `default` but the > $100 tier is 1.75× / $100, so the $100 floor binds between $100 and ~$133. |

## Validation

Before using a user value, check it. If one fails, keep the previous value for that key and say so in one line ("Ignored multiple 0.8: a multiple below 1 means buying at a loss; keeping 3×").

- `multiple` ≥ 1. `min_profit`, `bins_min_net` ≥ 0.
- Tiers sorted by `cogs_below`, last one `null`.
- STR bands: 0 < slower < healthy < fast ≤ 100. `slow_profit_factor` ≥ 1.
- `sales_tax_rate` between 0 and 0.15. `reseller_permit` is `none` or `permit`.
- Unknown keys: ignore and name them once.

## Showing which rules applied

- PROFIT always ends with the rule in short form: `rule: default · tier $20–$100 (2× / $25)` or `rule: my 4× / $20` or `rule: legacy-0.4.5 (3× / $15 net)`.
- When the permit or a slow STR changed the threshold, say it: `min profit $50 (slow STR ×2)`.
- Carry-over blocks (see `haul-mode.md`) include the profile name and any keys the user changed, so a new chat keeps the same rules.

## What-if and A/B (for tuning the rules)

The user may want to compare rule sets to find the right values. Support it without new searches:

- **"What if <change>?"** Re-score the current item or board with the change, reusing the comps, nets, and STR already retrieved. Show only the items whose verdict changes: `#14 🟡 → 🟢 (2.5× clears; was under 3×)`. Then say whether the new rule stays for the conversation (default: no, unless the user says "use it").
- **"Compare <A> vs <B>"** (two profiles or two rules): one line per item with both verdicts, then a one-line count: `A: 9 BUY · B: 12 BUY · 3 differ (#4, #9, #14)`.
- **Wrap up** adds a "Rules used" line with the profile and changed keys.
- Never re-run searches just to compare rules. Never save rules to memory unless the user asks.

## Precedence against project instructions

Project instructions that state rules in prose (for example "Minimum net $15; buy multiple 3× (tagged)") count as a settings source at level 2. If they state a flat rule, it replaces the tier table, like a flat rule typed in chat. If they also include a `thrift_scout_settings` block, the block wins over the prose.
