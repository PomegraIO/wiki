---
title: "Hedge Ratio Calculation Explained"
description: "Learn how to calculate hedge ratio—the fraction of a position to hedge using futures or options—with formulas and worked examples."
keywords:
  - how to calculate hedge ratio
  - hedge ratio formula
  - futures hedge ratio
  - basis risk hedging
  - partial hedging
  - commodity hedging
---

*A **hedge ratio** is the fraction of a position you protect by taking an offsetting [futures](/futures-contract/) or [options](/option/) position. Calculating it tells you exactly how many contracts or options to buy (or sell) so that losses in the underlying position are offset by gains in the hedge, without over-hedging or leaving yourself exposed. The formula depends on whether you are hedging a physical commodity, an equity position, or a financial risk—and whether you are using financial instruments that track the underlying perfectly or have [basis risk](/basis-risk/).*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Hedge Ratio Calculation — key facts</div>

<img src="/svg/risk.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Determine what size futures or options position offsets your underlying exposure without over- or under-hedging.</div>

|   |   |
|---|---|
| **Core formula** | Hedge Ratio = (Size of underlying position) ÷ (Size of hedge instrument) |
| **Perfect hedge** | Ratio of 1.0; losses and gains offset completely |
| **Partial hedge** | Ratio < 1.0; intentionally leave some risk unhedged for cost or opportunity reasons |
| **Over-hedge** | Ratio > 1.0; introduce directional exposure or increase losses if underlying moves favorably |
| **Basis risk** | Hedge instrument (e.g., crude oil futures) may not move 1:1 with underlying (e.g., jet fuel); adjust ratio downward |
| **Key inputs** | Notional size, price sensitivity (beta/delta), correlation between hedge and underlying |
| **Common mistakes** | Ignoring [basis risk](/basis-risk/), using contract size without adjusting for price changes, not accounting for [margin](/margin-call-forex/) costs |

</aside>

## The Core Formula

The simplest hedge ratio is:

$$\text{Hedge Ratio} = \frac{\text{Notional Value of Position}}{\text{Notional Value of One Futures Contract}}$$

**Example:** You own 100,000 barrels of heating oil worth $3.00/barrel = $300,000 total. Heating oil futures contracts are 42,000 barrels each. One contract is worth 42,000 × $3.00 = $126,000. To hedge all 100,000 barrels:

$$\text{Hedge Ratio} = \frac{300,000}{126,000} = 2.38$$

You need 2.38 heating oil futures contracts (you would buy 2 or 3 contracts, depending on how much precision you want). If you sell 2 contracts, you cover $252,000 of the $300,000 exposure, leaving 16% unhedged (a partial hedge).

## When Perfect Hedges Don't Exist

The calculation above assumes the hedge instrument tracks your underlying 1:1. In reality, basis risk often arises: the futures price moves differently from your actual holding.

**Example: Airline hedging jet fuel.**

An airline consumes 100 million gallons of jet fuel annually, costing roughly $3.00/gallon = $300 million. Jet fuel futures do not exist, but crude oil futures (in barrels) do. Crude oil has moved roughly 0.8 correlation with jet fuel prices over the past 5 years.

One crude oil futures contract is 1,000 barrels. At $80/barrel, one contract notional = $80,000. Without adjusting for basis risk:

$$\text{Naive Hedge Ratio} = \frac{300,000,000}{80,000} = 3,750 \text{ contracts}$$

But crude oil is not jet fuel. When crude falls 10%, jet fuel typically falls 8% due to different refining costs and demand. The airline's true hedging demand is:

$$\text{Adjusted Hedge Ratio} = 3,750 \times 0.8 = 3,000 \text{ contracts}$$

This smaller position still substantially offsets jet fuel price risk without over-hedging.

## Hedge Ratio with Beta or Delta

For equity portfolios, hedge ratios often use [beta](/beta/)—the sensitivity of a stock or portfolio to moves in the broader market. If your stock has a beta of 1.2 (moves 20% more than the market), a 1:1 hedge is too small.

**Example: Hedging a $5 million equity portfolio with beta 1.2 using S&P 500 futures.**

The [S&P 500 index](/sp-500-index/) contract (E-mini) is worth roughly $50 × the index value. If the index is at 5,000, one contract = $250,000 notional.

$$\text{Hedge Ratio} = \frac{\text{Portfolio Value} \times \text{Beta}}{\text{Contract Notional}} = \frac{5,000,000 \times 1.2}{250,000} = 24 \text{ contracts}$$

Selling 24 S&P 500 contracts will offset roughly 100% of the portfolio's downside. If the portfolio falls 10%, gains on the short futures position nearly cancel the loss (assuming the portfolio beta is truly 1.2).

For options, [delta](/delta/) plays the same role: it quantifies how much the option price moves for a 1% move in the underlying. A call option with delta 0.6 moves $0.60 for every $1.00 move in the stock.

## When to Partial-Hedge: Cost and Opportunity

Many firms do not hedge 100%; they accept some residual risk to save on hedging costs (futures [margin](/margin-call-forex/), options premiums) or preserve upside if prices move favorably.

**Example: A wheat farmer with 50,000 bushels of wheat expected to harvest in 3 months.**

Wheat futures are 5,000 bushels per contract. A perfect hedge is 10 contracts (10 × 5,000 = 50,000). But wheat futures [premiums](/option-premium/) are high, eating into profit margins. The farmer decides to hedge 70%:

$$\text{Partial Hedge Ratio} = 10 \times 0.70 = 7 \text{ contracts}$$

If wheat prices fall 20%, the farmer loses 20% × 30% unhedged = 6% of total crop value. If prices rise 20%, the farmer gains 20% × 30% = 6% upside. This trades off full protection for lower costs and shared upside.

## Adjusting for Duration and Convexity (Bonds)

For bond portfolios, hedging with bond futures requires accounting for [duration](/duration/)—how much a bond's price changes when interest rates shift.

**Example: Hedging a $10 million corporate bond portfolio with duration 5 (meaning a 1% interest rate rise causes a 5% price decline).**

10-year Treasury futures have duration ~8. One contract is 100,000 notional ($100,000 face value).

$$\text{Hedge Ratio} = \frac{\text{Portfolio Value} \times \text{Portfolio Duration}}{\text{Futures Notional} \times \text{Futures Duration}} = \frac{10,000,000 \times 5}{100,000 \times 8} = 62.5 \text{ contracts}$$

This accounts for the fact that Treasury futures are longer-duration than the corporate bond portfolio; you need more of them to offset the same interest-rate risk.

## Real-World Complications

**Margin requirements:** Selling 62.5 futures contracts requires cash margin, typically 5–10% of notional. With $10 million in bond hedges, expect to post $500,000–$1,000,000 in margin. This capital is locked up, increasing the hedge's opportunity cost.

**Slippage and rebalancing:** As positions change—bonds mature, prices move, new purchases arrive—the hedge ratio drifts. Rebalancing contracts and adjusting positions incurs trading costs.

**Cross-hedging basis:** If you hedge a European stock portfolio using US S&P 500 futures, currency fluctuations introduce basis risk. You may want to hedge currency separately or size down the equity hedge ratio.

**Liquidity and execution:** Large hedge ratios (hundreds of contracts) may move market prices during execution, blunting the hedge's effectiveness.

## See also

<div class="wiki-seealso">

### Closely related

- [Futures Contract](/futures-contract/) — mechanics of standardized commodity and financial contracts
- [Basis Risk](/basis-risk/) — when the hedge instrument and underlying move imperfectly together
- [Beta](/beta/) — measure of stock portfolio sensitivity to market moves
- [Delta](/delta/) — option price sensitivity to moves in the underlying
- [Duration](/duration/) — bond price sensitivity to interest rate changes
- [Options](/option/) — calls and puts as hedging instruments

### Wider context

- [Derivatives Hedging](/derivatives-hedging/) — broad strategy of using derivatives to reduce risk
- [Margin Call (Forex)](/margin-call-forex/) — cost of maintaining futures positions
- [Volatility Smile](/volatility-smile/) — complications in option pricing at extremes
- [Over-the-Counter Market](/over-the-counter-market/) — custom hedges outside exchange-traded contracts

</div>
