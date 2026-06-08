---
title: "Conditional Order"
description: "An order that remains dormant until a specified market condition is met, then activates as a regular order."
keywords:
  - conditional order
  - contingent order
  - triggered order
  - order routing
  - trading mechanics
image: "/svg/trading.svg"
---

*A **conditional order** is an instruction to buy or sell a security that only becomes active when a specified market event occurs. Unlike a standing [limit order](/limit-order/), which sits in the market waiting to execute, a conditional order exists as a "sleeping" instruction—a standing indication of interest that converts to a live order only when the broker or exchange detects that the trigger condition has been satisfied.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Conditional Order — key facts</div>

<img src="/svg/trading.svg" alt="An abstract editorial mark for trading mechanics." />

<div class="wiki-infobox-caption">An order awakened by market conditions, not time.</div>

|   |   |
|---|---|
| **What it is** | An order that activates upon a triggering event or price level |
| **Also called** | Contingent order, triggered order, indication of interest |
| **Common trigger types** | Price level (bid-ask cross, specific price reached), volume threshold, news event |
| **Execution when triggered** | Converts to a live [market order](/market-order/) or [limit order](/limit-order/) depending on type |
| **Primary use** | Automating entries or exits tied to market milestones without constant monitoring |
| **Risk consideration** | Execution is not guaranteed once triggered; market may gap past trigger level |

</aside>

## The problem it solves

Traders often face a dilemma: sit in front of the screen watching for a specific price or condition, or submit a live order and accept the risk of premature or unwanted execution. A conditional order bridges this gap by allowing the client to specify an "if this happens, then do that" instruction. When the broker detects that the condition has been met—a stock touches a price, a volume spike occurs, or a related security moves—the order automatically activates. This is purely mechanical; no human intervention is required once the condition is satisfied.

The appeal lies in *automation without exposure*. Unlike a live [market order](/market-order/) that risks immediate execution at an unfavourable price, a conditional order remains inert until the specified event materializes. A trader might say: "Buy 500 shares of Bank X when Bank Y breaks above 45 dollars"—locking in the logic of their trade idea without babysitting the screen.

## Common trigger mechanisms

A conditional order's trigger can take several forms. **Price-based triggers** are the most straightforward: activate when the security or a linked benchmark crosses a threshold. A trader might place a conditional order to buy stock ABC if the [S&P 500](/sp-500-index/) reaches a certain level, or to sell covered calls if the underlying rallies 5% above entry.

**Cross triggers** are particularly common in algorithmic and block trading. A conditional buy order might activate only when the bid and ask prices in a linked security intersect—an indication that liquidity or sentiment has shifted. This is especially valuable in illiquid or thinly traded names where price action in a correlated instrument signals broader market opportunity.

**Volume triggers** activate an order when trading volume in the security or its options crosses a threshold, often interpreted as a signal that institutional interest has arrived. **News-triggered** conditional orders—though requiring manual broker intervention or specialized platforms—activate after an earnings release, regulatory announcement, or corporate action.

## How execution typically works

Once triggered, the conditional order becomes a live order, usually as a [market order](/market-order/) or a limit order at a pre-specified price. The key distinction is timing: the trigger event *awakens* the order, but execution is still subject to market conditions at that moment. If the market has moved significantly between the trigger and the moment of execution, the order may fill at a different price than anticipated, or in volatile conditions, may not fill at all.

Brokers differ in how they handle partial or slipped executions. Some firms guarantee best execution once triggered; others explicitly disclaim liability if the market gaps past the trigger level before the order reaches the market. This is particularly relevant in overnight gaps or around economic data releases, where a conditional order might trigger during the pre-market or gap-open period when liquidity is thin.

## Risk and limitations

A conditional order is a *passive* tool, not a guarantee. The broker or exchange must actively monitor for the trigger condition. In periods of extreme volatility, system overload, or when dealing with smaller or OTC securities, the trigger may execute with slippage or delay. Conversely, a market that reverses sharply after the trigger but before execution may result in a fill that violates the trader's original intent.

There is also the risk of trigger conflicts. A trader might place multiple conditional orders with different triggers, only to find that two activate simultaneously during a fast market, creating unexpected portfolio imbalance. Some traders use conditional orders in combination with a [stop-loss](/stop-order/) to define both the entry point and the maximum loss, but this layering can create execution complexity if either order fills during volatile periods.

Additionally, conditional orders often incur slightly higher commissions or fees than passive limit orders, since brokers bear a modest operational cost in monitoring conditions and routing the activated order to execution.

## Regulatory and operational nuances

The mechanics of conditional orders vary by venue and asset class. Equity exchanges, [futures](/futures-contract/) markets, and options venues each have slightly different rules about which types of triggers are allowed and how orders are prioritized once activated. Some [market makers](/market-maker-trading/) accept conditional orders on a principal basis, taking on the risk themselves; others strictly route them as agency orders. 

Professional traders and [hedge funds](/hedge-fund/) often use conditional orders as part of algorithmic strategies, combining them with passive pricing and dynamic rebalancing logic. Retail investors, conversely, typically encounter conditional orders through brokers as "if/then" order templates, often limited to simple price or volume triggers.

## When conditional orders matter most

Conditional orders are most valuable in trending or mean-reverting markets where identifiable inflection points exist. A trader might use them to scale into a position after a 2% pullback, or to exit entirely if a key support level breaks. They are also common in earnings season, when a trader wants to establish a position only *after* the earnings surprise is known, reducing the risk of front-running a reaction.

In low-liquidity or overnight markets, conditional orders are less reliable, since the broker's ability to monitor and execute is constrained. They also add little value in high-frequency or short-term trading, where timing windows are measured in milliseconds and the cost of manual entry is negligible.

## See also

<div class="wiki-seealso">

### Closely related

- [Limit Order](/limit-order/) — standing order to buy or sell at a specified price or better
- [Market Order](/market-order/) — immediate execution at current market prices
- [Stop Order](/stop-order/) — conditional sell order triggered by a price drop (loss mitigation)
- [Algorithmic Trading](/algorithmic-trading/) — automated execution strategies often layering conditional logic
- [Not-Held Order](/not-held-order/) — discretionary instruction granting the broker flexibility in timing and price

### Wider context

- [Order Routing](/order-types/) — how broker directs orders to execution venues
- [Market Maker Trading](/market-maker-trading/) — how conditional orders interact with liquidity provision
- [Price Discovery](/price-discovery/) — how conditional orders contribute to finding equilibrium prices
- [Liquidity Risk](/liquidity-risk/) — execution risk when conditional order triggers in thin markets

</div>
