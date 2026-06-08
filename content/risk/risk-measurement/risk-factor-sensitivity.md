---
title: "Risk Factor Sensitivity"
description: "Measures how a portfolio's value changes for each unit move in underlying market risk factors like interest rates, equity indices, or spreads."
keywords:
  - risk factor sensitivity
  - duration
  - delta
  - factor exposure
  - market risk
image: /svg/risk.svg
---

*Risk Factor Sensitivity quantifies exactly how much a portfolio's value will move for a given shift in each underlying driver of returns—interest rates, equity indices, credit spreads, exchange rates, or volatility. Rather than asking "what is my portfolio's total downside at 95% confidence?" (the [Value at Risk](/value-at-risk/) question), sensitivity analysis asks "what happens if the 10-year Treasury yield rises 50 basis points?" It is the cornerstone of [market risk](/market-risk/) decomposition.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Risk Factor Sensitivity — key facts</div>

<img src="/svg/risk.svg" alt="An abstract editorial mark for risk measurement." />

<div class="wiki-infobox-caption">Break down portfolio risk into granular, actionable factor moves.</div>

|   |   |
|---|---|
| **What it is** | The dollar or percentage change in portfolio value for a unit move in a risk factor |
| **Also called** | Factor exposure, risk exposure, Greeks (for options) |
| **Key variants** | [Duration](/duration/) (interest rate), delta (equity/options), credit spread duration |
| **Measured as** | DV01 (dollar value of 1bp), vega (per 1% volatility change), rho (per 1% rate change) |
| **Why it matters** | Translates abstract portfolio holdings into concrete hedging and positioning decisions |

</aside>

## Why a single number is not enough

A portfolio manager looking at a single headline risk metric—whether [Value at Risk](/value-at-risk/), [standard deviation](/market-risk/), or expected shortfall—learns the magnitude of total risk but nothing about *where* that risk originates. A fund might have a 2% [Value at Risk](/value-at-risk/), but that number obscures critical questions: Is the risk coming from equity market exposure or from credit spread widening? If equity indices fall 20%, does the portfolio rise or fall? If the Fed raises rates 200 basis points, how much capital is at stake?

Risk Factor Sensitivity answers these. It disaggregates the portfolio's total [market risk](/market-risk/) into its constituent parts—each isolated, each measurable, each hedgeable.

## Duration: the bond world standard

The most familiar example is **duration**, which measures interest-rate sensitivity. A bond portfolio with a [duration](/duration/) of 5 years will lose roughly 5% of its value if yields rise 100 basis points, and gain 5% if yields fall 100 basis points. Duration is not time to maturity; it is a precise measure of the portfolio's exposure to yield changes.

A portfolio manager working with a fixed-income book will spend more time monitoring duration than any other single number. A [central bank](/central-bank/) hiking rates puts the entire fixed-income portfolio at [interest-rate risk](/interest-rate-risk/). By tracking duration in real time, the manager can hedge (e.g., by selling shorter-duration bonds and buying longer ones, or by using [futures contracts](/futures-contract/) on bonds) or accept the risk consciously. Duration gives the decision a numerical spine.

## Delta and the Greeks in options

For derivatives portfolios, sensitivity is expressed using the **Greeks**: [delta](/delta/) (sensitivity to the underlying's price), [gamma](/gamma/) (sensitivity of delta itself), [vega](/vega/) (sensitivity to volatility), and [theta](/theta/) (time decay). A portfolio of [call options](/call-option/) might have a delta of +50, meaning for every dollar the underlying stock rises, the portfolio gains 50 cents. If the stock falls $1, the portfolio loses 50 cents.

These Greeks are not just risk metrics; they are the language of [hedging](/hedge-fund/). A trader holding long call options with a delta of +50 might hedge by short-selling 50% of the underlying, creating a [delta-neutral](/delta/) position that profits from [volatility](/volatility-smile/) moves but not from directional stock movement.

## Building the sensitivity grid

In practice, a risk manager assembles a sensitivity matrix with one row per risk factor and one column per impact measure (dollar change, percentage change, or marginal [Value at Risk](/value-at-risk/)).

Consider a portfolio that holds equities, bonds, and credit-exposed loans:

- **Equity index sensitivity**: For each 1% move in the [S&P 500](/sp-500-index/), portfolio value changes by $X.
- **Interest rate sensitivity** ([duration](/duration/)): For each 1 basis point rise in the 10-year Treasury, portfolio value changes by $Y.
- **Credit spread sensitivity**: For each 1 basis point widening of the high-yield spread, portfolio value changes by $Z.
- **Currency sensitivity**: For each 1% appreciation of the US dollar, portfolio value changes by $W.

These sensitivities are often expressed in units tailored to the factor. Equity sensitivity might be reported as "beta" (systematic sensitivity to the equity market). Bond sensitivity is [duration](/duration/). Currency exposure is often the notional amount of foreign currency held. The units vary, but the logic is identical: quantify how much portfolio value moves per unit factor move.

## Static vs. dynamic sensitivity

The catch: sensitivities are not constant. A bond's [duration](/duration/) falls slightly as its price rises and rises as it falls—a phenomenon called *convexity*. An equity [call option](/call-option/) has a [delta](/delta/) of 0.5 when the stock is at-the-money, but a delta closer to 1 when the stock is deep in-the-money and closer to 0 when deep out-of-the-money. These non-linearities mean sensitivity estimates are only valid over small factor moves.

For small shifts (10 basis points in rates, 1% in equity indices), the sensitivity remains roughly constant and the linear approximation holds. For large moves, [gamma](/gamma/) (second-order sensitivity) becomes material. A trader might report, "My delta is +100 with a gamma of +20. If the stock rises another 5%, my delta will shift to +200." That gamma term captures the curvature that linear sensitivity misses.

## Aggregating across factors

A sophisticated portfolio typically has exposure to dozens of risk factors. Building and maintaining the sensitivity grid becomes a technical challenge: data pipelines must pull prices and volumes for each factor, revalue the portfolio, compute sensitivities, and aggregate them. Errors propagate—miscoded sensitivities can lead to misjudged hedges or false confidence in risk offsets that don't actually exist.

This is why large institutions invest heavily in risk systems. The sensitivity grid is only useful if it is accurate and current. A bank's overnight risk reporting system might compute sensitivities for 100+ factors across a portfolio of 10,000+ positions, aggregating them into a single dashboard the chief risk officer reviews at 7 a.m. every business day.

## Sensitivity vs. correlation

Risk Factor Sensitivity assumes factors move independently or according to their historical correlations. When correlations break (as they reliably do in crises), sensitivities can mislead. During the 2008 financial crisis, normally uncorrelated assets—equities, bonds, credit, currencies—all crashed in the same direction. A portfolio that looked well-hedged (long equities, short bonds, expecting them to move oppositely) was devastated because the hedge became useless just when it was needed.

This is why Risk Factor Sensitivity is always paired with [stress-testing](/stress-testing/) and scenario analysis. A manager computes sensitivities under normal conditions, then stress-tests the portfolio under extreme scenarios (rates up 200bp, credit spreads widen 500bp, equity indices down 30%) to see whether the linear sensitivities remain valid and whether hidden correlations create new risks.

## See also

<div class="wiki-seealso">

### Closely related

- [Duration](/duration/) — the quintessential risk-factor sensitivity for bonds
- [Delta](/delta/) — sensitivity of derivatives to underlying price movement
- [Market Risk](/market-risk/) — the aggregate risk that factor sensitivities decompose
- [Stress-Testing](/stress-testing/) — validates sensitivities under extreme scenarios
- [Hedge Fund](/hedge-fund/) — uses sensitivity analysis to construct hedges and factor bets

### Wider context

- [Modified Value at Risk](/modified-var/) — combines risk factors with distributional adjustments
- [Interest Rate Risk](/interest-rate-risk/) — a key risk factor in most portfolios
- [Credit Spread](/credit-spread/) — another primary risk factor for credit-exposed books

</div>
