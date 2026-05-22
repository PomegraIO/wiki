---
title: "Equity Hedging"
description: "Risk management techniques to reduce downside exposure in stock portfolios while preserving upside, typically via puts, shorts, or derivatives."
keywords:
  - put option
  - portfolio protection
  - downside risk
  - hedging strategy
---

*An **equity hedge** is a position or strategy designed to reduce the downside risk of a [stock portfolio](/wiki/portfolio-mental-accounting/) while allowing for some or most of the upside, typically through [put options](/wiki/put-option/), [short selling](/wiki/short-selling/), or [derivatives](/wiki/derivative-accounting-hedging/).*

No investor wants to experience the pain of a 40% drawdown. Hedging lets you buy insurance against that outcome. The trade-off: the insurance costs something — either as a direct premium (buying puts), as forgone upside (short a correlated stock), or as opportunity cost (holding cash). The decision to hedge comes down to how much downside protection is worth to you.

<aside class="wiki-infobox">

| Hedge type | Mechanism | Cost | Downside protection | Upside cap |
|-----------|-----------|------|----------|-----------|
| **Protective put** | Buy puts on portfolio | Direct premium | Full (minus premium) | None |
| **Put spread** | Buy puts, sell lower puts | Lower premium | Partial (capped) | None |
| **Short correlation** | Short a correlated stock/index | Negative carry | Partial | Reduced |
| **Long VIX call** | Call on [volatility index](/wiki/fear-index/) | Small premium | Nonlinear (pays in crashes) | None |
| **Collar** | Buy puts, sell calls | Free or near-free | Limited | Capped |
| **Cash reserve** | Hold excess cash | Opportunity cost | Low | Dampened by allocation |

</aside>

## Protective puts

The simplest hedge is a **protective put**: you own a stock and buy a [put option](/wiki/put-option/) that gives you the right to sell it at a fixed price (the strike). If the stock crashes below the strike, you can sell at the strike and limit your loss. If the stock rises, you keep all the gains. The cost is the put premium.

For a $100 stock, buying a $90 put might cost $2. That $2 is your insurance deductible. If the stock falls to $80, your put is worth $10, offsetting the $20 loss. If the stock rises to $120, your put expires worthless, you pocket the $120, and the $2 premium is your only cost.

Protective puts work well for concentrated positions (large holdings you do not want to sell) and over short horizons (a few months, where put premiums are small). Over longer periods, the cumulative cost of puts can be steep.

## Put spreads

A **put spread** (also called a **put debit spread**) reduces the cost of a protective put by selling a lower put to finance the higher one. You buy a $90 put (paying $2) and sell an $80 put (receiving $0.75), for a net cost of $1.25. Now you are protected down to $85 (90 − 5 = 85 after subtracting the initial cost), but you have no protection below $80. The upside is unlimited (as long as you hold the stock), but your downside is capped.

This is the workhorse of institutional hedging: you get meaningful protection for a fraction of the cost of a naked put.

## Collars: the free hedge

A **collar** is a protective put financed entirely by selling a call. You buy a $90 put and sell a $110 call, with the two premiums offsetting. Your cost is zero (or even credits you slightly if the call is worth more). Your downside is protected below $90; your upside is capped at $110.

Collars are popular for hedging concentrated positions in executive stock options or inherited shares. The owner can rest easy knowing the position will not drop below a floor, and the opportunity cost is the capped upside.

## Short-selling as a hedge

Instead of buying puts, you can **short a correlated security**. If you own a concentrated position in Apple, you might short the [Nasdaq-100](/wiki/nasdaq-composite/) or short a rival tech company. If Apple crashes along with the index, the short gain offsets the long loss. If Apple rises, the short loss is (mostly) offset by the long gain.

The advantage: no premium paid upfront (shorts do not cost unless you are borrowing shares at high rates). The disadvantage: the correlation is imperfect, so the hedge may not be perfect. If Apple rises and the Nasdaq falls, you lose on both sides. You also bear [short-squeeze](/wiki/short-squeeze/) risk (being forced to cover at a bad price) and [lending costs](/wiki/stock-lending-market/) if shares are hard to borrow.

## [Futures](/wiki/futures-contract/) and index hedges

An institutional investor with a $100 million stock portfolio might hedge by shorting [index futures](/wiki/index-fund/) (e.g., [S&P 500 futures](/wiki/sp-500-index/)). Each contract represents $100,000+ of the index, so a few contracts provide substantial downside protection for the whole portfolio, with no optionality cost (futures have no premium, just margin). The downside is marked-to-market daily (variation margin), and if the market rises sharply, you have to post cash.

Futures hedges are most useful for temporary protection (a few months) when you are uncertain about selling the underlying stocks.

## Dynamic hedging and [volatility](/wiki/volatility-index/)

**Dynamic hedging** continuously adjusts the hedge as the market moves. As your portfolio falls in value, you buy more put protection; as it rises, you scale back. This rebalancing locks in gains and minimizes premium waste.

Sophisticated investors also hedge [volatility](/wiki/implied-volatility/). A long stock position is short volatility (drawdowns hurt). A [long volatility](/wiki/long-volatility/) hedge (long VIX calls or volatility swaps) pays off in crashes when realized volatility spikes. These are expensive in quiet markets but invaluable during crises.

## Cost-benefit: when to hedge

Hedging makes sense when:
- You have a concentrated position and do not want to sell (tax reasons, belief in the stock, illiquidity).
- You are approaching a milestone (retirement, IPO lockup expiration) and want to protect gains.
- You believe a crash is likely in a specific window (heightened geopolitical risk, earnings recession expected).
- You are using borrowed money and downside risk threatens your solvency.

Hedging is uneconomical when:
- Your time horizon is long and you can tolerate volatility (hedging costs add up).
- You already hold a diversified portfolio (diversification is a free hedge).
- You have low conviction about near-term risk (paying for insurance against an unlikely event).
- Implied volatility is very high (puts are expensive, so you are buying expensive insurance).

## Comparison with diversification

[Diversification](/wiki/diversification/) is often cheaper than hedging. A portfolio of 20 stocks in different sectors and geographies has lower volatility than one concentrated stock plus a put. But diversification does not completely eliminate downside (a market crash affects all stocks), while a put does (up to the strike). For concentrated positions, puts are the only solution.

<div class="wiki-seealso">

### Closely related
- [Put option](/wiki/put-option/) — The security used in protective hedges
- [Protective put](/wiki/protective-put/) — Buying a put to protect a long stock
- [Collar strategy](/wiki/collar-strategy/) — Put + short call for low-cost protection
- [Put spread](/wiki/put-spread/) — Capped downside protection via spread
- [Short selling](/wiki/short-selling/) — Alternative way to hedge via shorting correlates

### Wider context
- [Risk management](/wiki/risk-on-risk-off/) — Broader framework for managing portfolio risk
- [Diversification](/wiki/diversification/) — Cheapest hedge via broad holdings
- [Volatility hedging](/wiki/volatility-hedging/) — Hedging volatility exposure
- [Tail risk](/wiki/tail-risk/) — Protection against extreme downside
- [Derivatives](/wiki/derivative-accounting-hedging/) — The tools used in hedging

</div>
