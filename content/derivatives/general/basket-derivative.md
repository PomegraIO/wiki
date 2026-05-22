---
title: "Basket Derivative"
description: "Derivative instrument with multiple underlying assets, allowing hedging or speculation on asset-class relationships."
keywords:
  - basket derivative
  - multiple underlyings
  - correlation risk
  - structured products
---

*A **basket derivative** is a [derivative](/wiki/option/) contract whose payoff depends on the performance of multiple underlying assets — usually equities, indices, or commodities — combined through a single instrument, enabling exposure to asset-class relationships and correlation risk.*

<aside class="wiki-infobox">

| Feature | Description |
|--------|-------------|
| Underlyings | 2 to 100+ stocks, indices, commodities |
| Payoff | Function of all constituents (weighted, averaged, max/min) |
| Common Types | Basket options, basket swaps, index products |
| Use Cases | Hedging sector risk; correlation bets |
| Pricing Complexity | High; requires multivariate modeling |

</aside>

## Structure and payoff mechanics

A basket derivative bundles multiple assets into a single contract. The simplest form is a [basket option](/wiki/basket-option/) — a call or put on a weighted average of stocks. For example, a "tech sector basket call" might be struck on a portfolio of Apple, Microsoft, NVIDIA, and Nvidia with equal weights. On expiration, the payoff is determined by the average price of the four stocks, not any individual stock.

Alternatively, the payoff might be the **minimum** stock price in the basket, the **maximum**, a **geometric average**, or a weighted combination reflecting sector tilts. Each payoff structure creates different sensitivities and hedging implications.

## Uses in hedging and portfolio management

An investor long a diversified portfolio of European bank stocks can hedge sector risk with a basket put — a single contract protecting the entire sector position without buying 25 individual puts. The basket approach is cheaper because [correlation](/wiki/correlation-coefficient/) within the sector is high; the bank stocks move together, so the basket is less volatile than individual stocks, and the option [premium](/wiki/option-premium/) is lower.

[Hedge funds](/wiki/hedge-fund/) use baskets to bet on **relative outperformance** — a long/short basket position on, say, high-dividend European banks (long) versus low-dividend ones (short), capturing pure correlation and sector alpha without broad market risk.

## Correlation and pricing complexity

The value of a basket derivative depends not just on the individual underlying prices but on their **correlations**. If the underlying stocks are perfectly correlated (all move identically), a basket call is nearly identical to a call on the average. But imperfect correlation introduces optionality — the more stocks in the basket and the lower their correlations, the lower the payoff volatility, and thus the lower the option value relative to a single-stock option.

Pricing basket derivatives requires multivariate stochastic models. A vanilla [Black-Scholes](/wiki/black-scholes-model/) model suffices for a single option, but a basket requires a covariance matrix of all underlyings, [volatility surfaces](/wiki/volatility-smile/) for each, and assumptions about joint distributions. [Monte Carlo](/wiki/monte-carlo-options-pricing/) simulation is the industry standard.

## Basis risk and hedging imperfection

A basket derivative hedges **portfolio risk** but not **idiosyncratic risk** within the portfolio. A bank holding 30 European bank stocks and hedging with a 5-stock basket will not be protected against a shock specific to one stock in the portfolio but not in the hedge basket. This mismatch is a form of [basis risk](/wiki/basis-risk/).

## Index products as baskets

Most [index funds](/wiki/index-fund/) and [ETFs](/wiki/etf/) are implicitly basket derivatives — their payoffs replicate a weighted combination of 500 or 3,000 constituents. [Total return swaps](/wiki/total-return-swap/) on indices are explicit basket derivatives: one counterparty pays the total return of an index; the other pays fixed or floating cash flows. A [equity swap](/wiki/equity-swap/) on an equal-weighted basket of technology stocks is another variant.

## Structured products and exotic baskets

Investment banks create exotic basket structures. A "worst-of" basket call pays based on the **worst-performing** underlying — capturing tail risk, these are cheaper than individual calls because diversification dampens downside. A "phoenix note" or "trigger note" might reset the basket composition if certain conditions occur, or apply differential weights based on historical performance. These structures often obscure their true [tail risk](/wiki/tail-risk/) and [liquidity risk](/wiki/liquidity-risk/).

## Regulatory and transparency concerns

Basket derivatives, especially structured products, can hide complexity. An investor buying a "5-year autocallable basket note" on 10 emerging market equities might not fully appreciate the leverage, currency risk, [barrier option](/wiki/barrier-option/) mechanics, or the issuer's [credit risk](/wiki/credit-risk/) embedded in the product. Regulators have pushed for clearer disclosures, particularly for retail investors.

## Advantages over single-asset derivatives

A basket derivative can be significantly cheaper than buying individual derivatives on each underlying. An investor hedging a $100M portfolio of 50 stocks might pay 50–60% less for a single basket put than for 50 individual puts, because diversification reduces the basket's volatility and thus its hedging cost. This economy of scale has made basket swaps and puts standard tools in institutional fixed-income and equity businesses.

<div class="wiki-seealso">

### Closely related
- [Basket Option](/wiki/basket-option/) — call or put on multiple underlyings
- [Index](/wiki/sp-500-index/) — standardized basket of stocks
- [Total Return Swap](/wiki/total-return-swap/) — derivative delivering index or basket payoff
- [Correlation Risk](/wiki/correlation-risk/) — dependence structure among assets

### Wider context
- [Derivative](/wiki/option/) — contracts whose value derives from underlyings
- [Hedging](/wiki/currency-hedging/) — risk reduction using derivatives
- [Monte Carlo Valuation](/wiki/monte-carlo-options-pricing/) — simulation method for complex derivatives
- [Basis Risk](/wiki/basis-risk/) — imperfect hedge protection

</div>
