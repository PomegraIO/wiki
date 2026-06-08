---
title: "Negative Roll Yield in Commodity ETFs"
description: "Why commodity ETFs holding front-month futures repeatedly sell low and buy high in contango, creating structural drag versus spot prices."
keywords:
  - negative roll yield commodity etfs
  - contango roll yield
  - commodity futures rolling
  - structural commodity etf loss
image: /svg/derivatives.svg
---

*A **negative roll yield** is the cost a commodity [ETF](/etf/) incurs when it holds front-month [futures contracts](/futures-contract/) and repeatedly rolls them forward into later-dated contracts. In a [contango](/contango/) market (where future prices are higher than spot), the fund buys expensive far-month contracts and sells cheap near-month ones, locking in losses on every roll—a structural drag that can compound into annual underperformance of 5–20% or more relative to the spot commodity price.*

## How Commodity ETFs Track Spot (and Fail)

A crude oil ETF cannot hold physical barrels of crude in a warehouse; instead, it holds a portfolio of [crude oil futures contracts](/crude-oil/). But futures expire. A contract trading in March expires in March; to maintain continuous exposure, the ETF must "roll" by selling the March contract and buying the April contract before March expires.

If the ETF were trading at the same price in both months, rolling would be costless. But in [contango](/contango/)—the normal state of commodity futures markets—the April contract always costs more than the March contract. The ETF is forced to:

1. Sell the March contract (the cheaper one).
2. Buy the April contract (the more expensive one).
3. Pocket the loss: if March is $60 and April is $62, the ETF locks in a $2 per-barrel loss on each roll.

Over a year, rolling every month means absorbing this loss 12 times. If the average roll loss is $1 per barrel and the spot price is $60, that is 1.67% annual drag. For markets in steeper contango, the drag can exceed 15% annually.

## Contango and the Term Structure of Futures Prices

[Contango](/contango/) occurs when far-month futures are priced higher than near-month contracts, reflecting the convenience yield of holding the physical commodity and the cost of carry (storage, insurance, financing). A typical commodity futures curve might look like:

| Month | Price |
|-------|-------|
| Spot | $60.00 |
| 1-month | $60.50 |
| 2-month | $61.10 |
| 3-month | $61.80 |
| 6-month | $63.50 |

The ETF rolling from 1-month to 2-month sells at $60.50 and buys at $61.10, losing $0.60 per unit. It is trading down the curve—moving to more expensive contracts and realizing losses.

Over long periods, if spot prices are stable, the total roll losses across 12 months can be substantial. In volatile markets, spot prices often rise or fall sharply, which can offset some roll losses (if spot price rallies, the gain from spot appreciation can outweigh the roll cost), but the roll yield drag remains a structural cost.

## Why Contango Persists

Contango exists because:

1. **Storage cost**: Holding physical oil, natural gas, or agricultural commodities in warehouses costs money (rent, insurance, inventory carrying charges).
2. **Cost of capital**: Financing the purchase of physical commodity ties up capital that could otherwise earn returns elsewhere.
3. **Convenience yield**: The economic benefit of holding physical stock (availability, ability to meet immediate demand, operational flexibility) has a value that is priced into the futures curve.

In most years, these factors outweigh any shortage risk, pushing futures into contango. The slope of the curve varies with inventory levels, production, and demand, but a market in contango is the baseline.

## The Opposite Case: Backwardation

When a commodity is in shortage or high demand, the term structure can invert into [backwardation](/backwardation/): near-month prices are higher than far-month prices. In backwardation, rolling generates gains instead of losses. The ETF sells the expensive near-month contract and buys the cheaper far-month one, locking in a profit.

Backwardation typically occurs during supply disruptions (a hurricane knocks out oil production, crop failures tighten grain inventories) or when spot demand is urgent. It is usually temporary; once supply normalizes or demand cools, the curve returns to contango.

During backwardation, commodity ETFs outperform the underlying spot price because the roll yield is positive. But backwardation is the exception, not the rule.

## Measuring Roll Yield Over Time

The **roll yield** for a single roll is simply:

$$\text{Roll Yield} = \text{Price}_{\text{sell}} - \text{Price}_{\text{buy}}$$

If positive (backwardation), the fund gains. If negative (contango), it loses. Over a year with 12 monthly rolls, the cumulative roll yield can be estimated as the sum of individual roll yields, though the actual effect depends on contract sequencing and the precise timing of the rolls.

A rough annual roll yield for a commodity ETF in typical contango might be:

$$\text{Annual Roll Yield} \approx -2\% \text{ to } -5\%$$

In steeper contango (as seen in oil markets during 2015–2016), it can reach −15% or more. In backwardation, it can be positive.

## Why Investors Still Hold Commodity ETFs

Despite roll yield drag, investors hold commodity ETFs for three reasons:

1. **Spot price exposure**: If crude oil rises from $60 to $75, the ETF likely rises nearly in proportion, capturing the gain. A 25% spot rally overwhelms a 2–5% annual roll drag.
2. **Inflation hedge**: Many investors use commodity ETFs as a hedge against unexpected inflation; the roll cost is the price of that insurance.
3. **Portfolio diversification**: Commodities have low correlation with stocks and bonds, so the roll drag is justified by improved [portfolio risk-adjusted returns](/sharpe-ratio/).

But for a holder with a multi-year horizon in a strongly contangoing market, roll losses can compound to 10–20% of the initial investment.

## Investor Implications and Alternatives

Investors aware of roll yield should consider:

- **Timing commodity exposure**: Buy at the start of a supply shortage (when backwardation is high) and sell when supply recovers (before contango deepens).
- **Using longer-duration contracts**: Some commodity ETFs hold a blend of far-month futures, reducing roll frequency and sometimes capturing a different part of the curve.
- **Collateralized commodity indices**: Products like fully collateralized commodity [indexes](/index-fund/) that hold Treasury bills alongside futures can smooth the effect of roll losses by earning Treasury returns.
- **Physical commodities**: For certain assets (gold, silver), [ETFs](/etf/) that hold the actual metal eliminate roll yield entirely, though storage costs still apply (usually 0.2–0.4% annually).
- **Commodity-linked bonds or certificates**: Some investment-grade structured products embed commodity exposure with different roll mechanics.

The key insight is that an ETF's total return—its price appreciation plus dividends or roll yields—diverges from the spot commodity's price due to these structural forces.

## See also

<div class="wiki-seealso">

### Closely related

- [Contango](/contango/) — the futures curve shape that drives negative roll yield.
- [Backwardation](/backwardation/) — the inverted curve that generates positive roll yield.
- [Futures contract](/futures-contract/) — the rolling mechanism underlying commodity ETF tracking.
- [Crude oil](/crude-oil/) — the flagship commodity where roll yield effects are most visible.
- [Natural gas](/natural-gas/) — exhibits extreme roll yield variation with seasonal demand.
- [ETF](/etf/) — the vehicle through which retail investors gain commodity exposure.
- [Convenience yield](/contango/) — the economic driver of contango.

### Wider context

- [Commodity exchange](/cryptocurrency-exchange/) — where spot and futures prices are discovered.
- [Carry trade](/carry-trade/) — the broader principle of profiting from cost-of-carry differences.
- [Basis risk](/basis-risk/) — the divergence between futures and spot prices.
- [Expense ratio](/expense-ratio/) — another drag on ETF returns, often invisible alongside roll yield drag.
- [Derivative hedging](/derivatives-hedging/) — why farmers and producers use futures and face roll costs.

</div>
