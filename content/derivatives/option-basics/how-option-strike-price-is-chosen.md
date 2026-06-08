---
title: "How Option Strike Prices Are Set by Exchanges"
description: "How option strike prices are set by exchanges using standardized intervals and adjustment rules that balance trader accessibility and liquidity."
keywords:
  - option strike prices
  - how option strike prices are set
  - strike price intervals
  - exchange strike listing rules
  - option contract standardization
image: /svg/derivatives.svg
---

*How option strike prices are set is determined by exchange rules that specify standard intervals based on the [underlying asset's](/stock/) price and contract type. As the underlying moves, new strike prices are automatically added to maintain consistent spacing and trading access across the expiration ladder.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Option Strike Prices — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives." />

<div class="wiki-infobox-caption">Exchanges set standardized strike intervals that adjust with the underlying price to keep options accessible.</div>

|   |   |
|---|---|
| **Who sets them** | Stock exchanges via automated rules (not the underlying company) |
| **Spacing rule** | Depends on underlying price and asset class (stocks: $1–$5 intervals) |
| **When new strikes appear** | Automatically when underlying crosses preset trigger points |
| **Automatic delisting** | Yes, far out-of-the-money strikes are removed to reduce clutter |
| **Special adjustments** | Occur after stock splits, dividends, mergers (manual or automatic) |
| **Who profits from spacing** | Market makers benefit from wider spreads on fewer strike points |

</aside>

## Why Exchanges Don't Leave Strike Placement to Chance

Strike prices cannot be chosen randomly. If every trader could demand a [call option](/call-option/) or [put option](/put-option/) at any price level, options markets would fragment into thousands of illiquid, disparate contracts. Exchanges impose standardized spacing rules—sometimes called the "strike price grid"—so that buyer demand and seller supply concentrate on a manageable list of discrete strike levels.

This standardization accomplishes two competing goals: it makes options accessible across a wide price range (so traders can hedge or speculate at multiple levels), while keeping each individual strike price liquid enough to trade efficiently. The [bid-ask spread](/bid-ask-spread/) on an illiquid strike can be ruinously wide; pools of liquidity form when traders know exactly where to look.

## The Mechanics of Strike Spacing Rules

The standard rule for U.S. equities, set by the [Securities and Exchange Commission](/securities-and-exchange-commission/) and implemented by exchanges like the [New York Stock Exchange](/new-york-stock-exchange/) and [NASDAQ](/nasdaq/), is graduated by price:

- **Under $25**: $2.50 intervals  
- **$25 to $200**: $5 intervals  
- **Over $200**: $10 intervals

Meaning if Apple trades at $150, the exchange lists calls and puts at $145, $150, $155, $160, and so on in $5 increments. If Tesla trades at $280, strikes appear at $270, $280, $290, $300 (in $10 steps).

For [index options](/stock-market/) and some other derivatives, spacing may be wider: the [S&P 500 index](/sp-500-index/) often has $5 intervals instead of $1. [Futures options](/futures-contract/) and currency [options](/option/) on major pairs use their own rules, often tied to the [tick size](/bid-ask-spread/) of the underlying [futures](/futures-contract/) contract.

The options clearing houses—in the U.S., the Options Clearing Corporation—do not choose strikes individually; they follow a rules-based formula that adapts when the underlying price crosses defined thresholds.

## How New Strikes Are Added as the Underlying Moves

As the underlying asset's price climbs or falls, the exchange automatically adds new strikes at the edge of the range to keep the market frontloaded with accessible options. 

For example, assume Google trades at $120, and the lowest listed strike is $100 and the highest is $140. If Google rallies to $145, triggering a new strike threshold, the exchange automatically adds $145 and possibly $150 strikes. Conversely, if Google falls to $95, the lowest strikes shift down.

This system is fully automated. A human trader does not file a request; software at the exchange monitors the underlying price and inserts fresh strikes when the price moves beyond historical control limits. The timing depends on the expiration cycle; monthly and weekly options may update at different frequencies.

The rule is not uniform across all markets. The [Cboe Options Exchange](/option-premium/)—the largest U.S. options marketplace—publishes detailed specifications for which strikes appear at which price levels and expiration dates. Strips with very short time to expiration (0–7 days) may have denser strike grids to serve scalpers and short-dated hedgers.

## Dealing With Gaps: When Strikes Jump Across a Price Level

When the underlying rallies sharply—say, a tech stock jumps 8% in a single day—the new equilibrium price may land between existing strike prices. If Meta stock trades at $347 and the nearest strikes were $340 and $350, traders who want exposure at $347 face a choice: buy the $350 call (overpriced relative to intrinsic value) or buy the $340 call (too far in the money). 

The exchange does not insert mid-gap strikes retroactively; traders must wait until the next scheduled batch of new strikes is added, which typically happens when the market opens the following day or at a defined refresh interval. This is a source of minor friction: large overnight gaps can create a period where options are priced further from the cash level than normal.

## Adjustments and Special Cases

When a stock undergoes a [stock split](/stock/), merges, or pays a large special [dividend](/dividend/), the exchange does not simply reprice all outstanding contracts. Instead, the Options Clearing Corporation issues a notice detailing how each contract is adjusted—how many shares it represents and at what strike price.

A 2:1 stock split, for example, doubles the share count and halves the strike price. A 100-share [call option](/call-option/) at $100 becomes a 200-share option at $50. These adjustments are automatic and applied uniformly. The exchange then resumes normal strike-adding rules based on the new underlying price.

Similarly, if a company acquires another and the deal restructures the stock, the Options Clearing Corporation issues detailed adjustment notices to market participants.

## Why Liquidity Clusters at Round Numbers

In practice, the tightest [bid-ask spreads](/bid-ask-spread/) and highest trading volumes cluster at strikes that are round multiples of the spacing rule—most often at even $5 and $10 levels rather than $1. This happens because traders and algorithms naturally gravitate toward psychologically "clean" prices, and brokers and market makers front-load liquidity there.

An exchange's spacing rule ensures these clusters have enough strikes to serve all price levels, but does not guarantee equal trading volume across all strikes. The first $10-wide strike below and above the current price typically trades far more heavily than strikes three or four levels away, where [time decay](/time-decay-theta/) and theta effects become harder to offset against [intrinsic value](/intrinsic-value/).

This clustering has an important implication for traders: wide spacing (say, $10 intervals on a $300 stock) may reduce costs for a hedge but narrows the precise price level you can lock in.

## See also

<div class="wiki-seealso">

### Closely related

- [Option](/option/) — the contract itself and basic mechanics
- [Call option](/call-option/) — right to buy at the strike
- [Put option](/put-option/) — right to sell at the strike
- [Strike price](/option/) — definition and role in option profit/loss
- [Intrinsic value](/intrinsic-value/) — the in-the-money gain or loss
- [Exercise price](/exercise-price/) — synonymous with strike price

### Wider context

- [Bid-ask spread](/bid-ask-spread/) — why wider spacing affects trading costs
- [Market maker](/market-maker-trading/) — who provides liquidity at each strike
- [Derivatives hedging](/derivatives-hedging/) — why strike choices matter for risk management
- [Securities and Exchange Commission](/securities-and-exchange-commission/) — the regulator setting the framework
- [Options Clearing Corporation](/option-premium/) — manages the clearing and adjustment process

</div>
