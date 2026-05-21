---
title: "Basket Option"
description: "A basket option is a derivative whose payoff depends on the performance of multiple underlying assets, often enabling correlation-based strategies at lower cost than owning individual options."
keywords:
  - basket option
  - multi-asset option
  - exotic option
  - portfolio derivative
  - correlation
image: "/svg/derivatives.svg"
---

*A **basket option** is an exotic derivative whose payoff is based on a weighted portfolio (basket) of multiple underlying assets—stocks, indices, currencies, or commodities—rather than a single asset. The holder is exposed to the basket's performance as a whole, and the option is typically cheaper than owning individual [call option](/call-option) or [put option](/put-option) contracts on each underlying due to diversification and [correlation](/diversification) effects.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Basket Option — key facts</div>

<img src="/svg/derivatives.svg" alt="Multiple stocks aggregated into one basket representation" />

<div class="wiki-infobox-caption">A basket option combines multiple assets into a single contract.</div>

|   |   |
|---|---|
| **Basket components** | 2+ stocks, currencies, commodities, indices |
| **Weights** | Equal, capitalization-weighted, or custom |
| **Payoff basis** | Basket value (weighted average) at expiration |
| **Option type** | Call, put, or exotic variants |
| **Price vs. individual** | Cheaper (lower volatility due to diversification) |
| **Correlation impact** | Lower correlation = lower cost |
| **Primary use** | Portfolio hedges, sector bets, currency baskets |
| **Settlement** | Cash or physical delivery of weighted assets |
| **Valuation complexity** | High; requires correlation matrix |

</aside>

## How a basket works

Suppose you want downside protection on a three-stock portfolio: Apple 50%, Microsoft 30%, Google 20%. Rather than buy three separate [put option](/put-option) contracts, you buy a single basket put on a weighted portfolio (50/30/20). The put's payoff is calculated on the basket's value at expiration.

If the basket value is $100 at initiation and $95 at expiration, and the put [strike price](/strike-price) is $100, the payoff is max($100 – $95, 0) = $5. The single contract captures the portfolio's collective move.

This is simpler than managing three separate puts and cheaper than buying them individually, because the basket's volatility is lower than the weighted average of the individual stocks' volatilities due to [diversification](/diversification). When stocks do not move in perfect lockstep (when correlation is less than 1), the basket is smoother than any individual stock.

## Reducing cost through correlation

The pricing benefit comes from [correlation](/diversification). Two stocks with perfect positive correlation (always move together) give a basket with the same volatility as either stock alone. Two stocks with zero [correlation](/diversification) give a basket with much lower volatility.

[Black-Scholes model](/black-scholes-model) extended to baskets requires the correlation matrix between all pairs of assets as an input. Lower average [correlation](/diversification) means lower basket [volatility](/historical-volatility), which means lower [option premium](/option-premium).

A basket put on a diversified set of stocks is cheaper than buying a separate put on the most volatile single stock, because the basket's diversification dampens volatility relative to the worst actor in the portfolio.

## Common basket types

**Multi-currency baskets** are common in FX hedging. A multinational company receives revenue in multiple currencies. A basket put on the weighted currency exposure provides downside protection without having to hedge each currency separately.

**Sector baskets** replicate a sector index. A call on the semiconductor sector (weighted by market cap across 20-30 semicon names) is easier to transact than building and rebalancing a custom portfolio.

**Commodity baskets** are used in energy, agriculture, and metals. An airline might hedge energy exposure with a basket option on crude oil, heating oil, and natural gas weighted by consumption.

**Index-based baskets** replicate a stock index or ETF. A pension fund can buy a basket put on the constituents of the MSCI World Index, capturing global equity downside protection.

## Pricing and valuation

Pricing baskets requires knowing the [volatility](/historical-volatility) of each component and the correlations between all pairs. [Monte-carlo-options-pricing](/monte-carlo-options-pricing) is the standard approach: simulate the joint movement of all assets, calculate the basket value and option payoff on each path, then take the expected value.

For simple baskets (two assets), closed-form approximations exist. For complex baskets (10+ assets), Monte Carlo is preferred because the [correlation](/diversification) structure and non-linear basket payoff are handled naturally.

[Implied volatility](/implied-volatility) for basket options is often lower than the weighted average implied volatility of the individual components, reflecting the correlation discount.

## Greeks and hedging

[Delta](/delta) for a basket option is a weighted sum of the individual deltas, where weights reflect the portfolio's composition. A 50/30/20 basket has a 50% delta to Apple's delta, 30% to Microsoft, and 20% to Google.

Hedging a basket option's [delta](/delta) requires delta-hedging each component appropriately. [Gamma](/gamma) and [vega](/vega) are also weighted sums, making basket options simpler to hedge (componentwise) than exotic single-asset options.

[Theta](/theta) (time decay) is typically close to a vanilla option's theta, since the basket value decays predictably toward expiration.

## Rebalancing and path-dependent variants

Standard basket options are path-independent: only the final basket value matters. But some baskets are rebalanced on fixed dates (monthly, quarterly), creating path-dependent payoffs. These are more complex to value.

**Worst-of-the-basket** and **best-of-the-basket** options are related but distinct: their payoff is based on the worst or best performer in the basket, not the basket's average. These are typically cheaper (worst-of) or more expensive (best-of) than basket options.

## Practical applications

A pension fund with a $100M portfolio in 10 stocks can buy a single basket put at 6-month intervals, reducing hedging costs relative to buying 10 individual puts. The correlation between the stocks dampens volatility and reduces the put [premium](/option-premium).

A currency trader with exposure across five emerging-market currencies can buy a basket put on the weighted currency basket, capturing tail-risk protection without hedging each currency separately.

A commodity producer with exposure to oil, copper, and agricultural crops can buy a basket call on the weighted commodity basket, locking in upside without having to trade three separate commodity options.

## See also

<div class="wiki-seealso">

### Closely related

- [Call option](/call-option/) — right to buy; applied to basket
- [Put option](/put-option/) — right to sell; applied to basket
- [Asian option](/asian-option/) — another exotic with multiple values aggregated
- [Diversification](/diversification/) — the source of basket option cost savings
- [Correlation](/diversification/) — key input to basket pricing

### Pricing & Greeks

- [Monte Carlo options pricing](/monte-carlo-options-pricing/) — standard valuation method
- [Black-Scholes model](/black-scholes-model/) — extended to baskets (requires correlation)
- [Implied volatility](/implied-volatility/) — typically lower for baskets (correlation discount)
- [Delta](/delta/) — weighted sum of component deltas

### Deeper context

- [Option](/option/) — the family of derivatives
- [ETF](/etf/) — basket-like structure for equities
- [Index fund](/index-fund/) — basket-like structure for bonds and equities
- [Portfolio management](/asset-allocation/) — baskets used in hedging

</div>
