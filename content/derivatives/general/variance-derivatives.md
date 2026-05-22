---
title: "Variance Derivatives"
description: "Contracts that pay off based on realized volatility; used for hedging and directional bets."
keywords:
  - variance derivatives
  - volatility trading
  - variance swap
  - realized volatility
  - vega exposure
---

*A **Variance Derivative** is a contract whose payoff depends on the actual volatility (variance) of an underlying asset—typically a stock index or currency. Rather than betting on direction or level, traders use variance derivatives to isolate and trade volatility itself, hedging market exposure or profiting from volatility moves.*

<aside class="wiki-infobox">

| Aspect | Detail |
|---|---|
| **Primary Payoff** | Based on realized volatility vs. agreed strike |
| **Underlying** | Stock indices (S&P 500), currencies, commodities |
| **Common Forms** | Variance swaps, volatility swaps, variance forwards |
| **Key Input** | Realized variance (squared daily returns) |
| **Users** | Hedge funds, options traders, asset managers |
| **Market Size** | Billions notional; liquid in major indices |

</aside>

## Variance swaps: The core structure

A **variance swap** is the simplest variance derivative. Two parties agree on:

1. **Notional amount**: E.g., $1 million notional "vega" (dollar per 1% volatility point).
2. **Strike volatility**: E.g., 18% annualized [implied volatility](/wiki/implied-volatility/).
3. **Accrual period**: E.g., one year of daily returns.

At maturity, the payout is:

**Payoff = Notional × (Realized Volatility² – Strike Volatility²) × Scaling Factor**

If realized volatility comes in at 22% and the strike was 18%, the long side profits; the short side loses.

### Why variance, not volatility directly?

Variance (volatility squared) is used because it has a critical property: it is **additive across time**. If you have 20% annualized volatility, that's equivalent to roughly √(52) × 20% ÷ √52 ≈ 1.39% per week. This additivity makes pricing and replication via options tractable.

When you replicate a variance swap by buying and selling options across the strike spectrum—[straddles](/wiki/straddle-option/), [butterflies](/wiki/butterfly-spread/)—the math works out cleanly.

## How variance derivatives are used

### Hedging equity portfolios

An asset manager holding $100 million in equities faces [equity risk](/wiki/equity-risk/) but also volatility risk. If markets turn choppy, [portfolio insurance](/wiki/protective-put/) becomes expensive (options are pricier when implied vol is high). A variance swap allows the manager to cap realized volatility at a known cost: pay a small upfront fee to a counterparty and receive protection if actual vol spikes.

### Harvesting volatility term structure

The [volatility](/wiki/implied-volatility/) term structure (near-term vs. far-term implied vols) is not flat. If near-term volatility is 15% and one-year volatility is 20%, a trader might:
- Short a one-year variance swap at 20%.
- Long a three-month variance swap at 15%.
- If realized volatility settles in the middle, the trader profits on the short leg and loses on the long leg—but the short outweighs because it's longer-dated.

### Volatility arbitrage

Sophisticated traders compare:
- **Implied variance** (derived from option prices via [Black-Scholes](/wiki/black-scholes-model/)).
- **Realized variance** (actual daily swings observed in the market).

If implied variance is 22² = 484 (a 22% vol level) and realized is tracking at 18² = 324, the trader shorts variance swaps (betting realized will stay low) and hedges by buying straddles (profiting if the market reprices implied lower as realized comes in).

## Volatility swaps vs. variance swaps

A **volatility swap** directly exchanges realized volatility against strike volatility, not squared. They're conceptually simpler but harder to replicate and price because volatility is non-linear. 

Variance swaps are far more common in liquid markets because:
- They can be replicated by a portfolio of [options](/wiki/option/) at different strikes.
- Pricing is more transparent.
- Daily mark-to-market is more stable.

## Payoff mechanics: A worked example

**Setup:**
- Variance swap: $500k notional, 20% strike volatility, S&P 500 underlying.
- Duration: 1 year (252 trading days).

**Calculation:**
If realized volatility over the year is 23%:
- Realized variance = 23² = 529.
- Strike variance = 20² = 400.
- Variance difference = 529 – 400 = 129.
- Payout = $500k × (529 – 400) ÷ 100 = $500k × 1.29 = $645k.

The long variance position receives $645k; the short pays. (Scaling factor of ÷100 is conventional.)

If realized vol is only 17%:
- Realized variance = 17² = 289.
- Variance difference = 289 – 400 = –111.
- Payout = $500k × (–111) ÷ 100 = –$555k.

The long variance position loses $555k.

## Relation to the VIX

The [VIX](/wiki/fear-index/) is a measure of 30-day implied volatility of S&P 500 index options. It is *not* a variance derivative itself, but it's closely tied to variance derivatives:

- **VIX futures** are notional bets on the VIX level itself; changes in the VIX affect variance derivative valuations.
- **Variance swaps on the S&P 500** roughly track realized 30-day volatility, which pulls the VIX down if realized is lower than priced.
- Many volatility traders use both VIX instruments and variance swaps to construct multi-leg hedges.

## Hedging challenges

### Gap risk

If markets gap overnight (close at 100, open at 95), a variance swap accrues the realized volatility from that gap. A portfolio can gap and leave a variance hedge incomplete. True hedging requires options (which have convexity and limited loss) or dynamic [rebalancing](/wiki/asset-rebalancing/).

### Liquidity

Variance swap markets are liquid for major indices (S&P 500, Euro Stoxx 50) but far less so for individual stocks or emerging market indices. Bid-ask spreads widen significantly for less popular underlyings.

### Funding costs

A variance swap is not cash-settled at inception; it's typically a binding OTC contract. If mark-to-market swings against you, you may face collateral calls. Funding costs can materially erode returns.

## Comparison to options for volatility exposure

| Tool | Pros | Cons |
|---|---|---|
| **Variance swaps** | Pure vol exposure, scalable | Requires liquid OTC market, funding risk |
| **Straddles** | Standardized, exchange-traded | Exposed to gamma decay, theta bleed |
| **VIX futures** | Liquid, exchange-cleared | Track spot vol imperfectly (vol of vol) |
| **Variance ETFs** | Passive volatility tilt | Decay over time in contango markets |

## Market cycles and variance trading

Variance derivatives are most valuable during periods of:
- **Complacency**: When implied vol is low but potential catalysts (earnings, Fed decisions) loom, implied vol may be too cheap relative to realized. Traders buy variance swaps.
- **Panic**: When implied vol spikes (VIX above 30), variance swaps become expensive insurance; hedgers pay up.
- **Regime shifts**: Transitions from low to high volatility regimes often catch variance hedges out of alignment, forcing rebalancing.

## Pricing and replication

Variance swaps are typically repliced using a portfolio of out-of-the-money options:
- Buy puts below the underlying price.
- Buy calls above the underlying price.
- The replicating portfolio "feels" market moves in both directions.
- As the market moves, the hedge portfolio accrues gains/losses that mimic realized variance.

This replication is the foundation of modern variance derivative pricing and is why variance swaps can be fairly priced even in illiquid markets by reference to option prices.

<div class="wiki-seealso">

### Closely related
- [Variance swap](/wiki/variance-swap/) — primary instrument
- [Implied volatility](/wiki/implied-volatility/) — strikes against this
- [Volatility swap](/wiki/volatility-swap/) — simpler alternative
- [Vega](/wiki/vega-option-greeks/) — Greeks exposure in options

### Wider context
- [Options](/wiki/option/) — foundational derivatives for replication
- [Derivatives](/wiki/derivatives/) — broader class
- [Hedge fund](/wiki/hedge-fund/) — major users
- [Volatility index](/wiki/fear-index/) — related market measure

</div>
