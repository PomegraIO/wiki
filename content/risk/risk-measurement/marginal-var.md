---
title: "Marginal Value at Risk"
description: "The change in total portfolio VaR if a single position is added or removed, measuring the marginal risk contribution of that holding."
keywords:
  - value at risk
  - portfolio risk
  - risk attribution
  - marginal contribution
  - risk management
image: "/svg/risk.svg"
---

*The **marginal value at risk** (or marginal VaR) is the additional [value at risk](/value-at-risk/) that a portfolio incurs by holding one more unit of a given asset. It answers the question: how much does my total portfolio risk increase if I add a position to this equity, bond, or derivative? Unlike [component VaR](/component-var/), which calculates the risk already embedded in a position you own, marginal VaR forecasts the incremental risk of a proposed trade.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Marginal Value at Risk — key facts</div>

<img src="/svg/risk.svg" alt="An abstract editorial mark for risk measurement." />

<div class="wiki-infobox-caption">The sensitivity of portfolio VaR to changes in position size.</div>

|   |   |
|---|---|
| **Formula basis** | Change in total VaR per unit added to a position |
| **Time horizon** | 1 day to 10 days (risk model dependent) |
| **Confidence level** | 95% or 99% (model assumption) |
| **Compared to** | [Component VaR](/component-var/); [Delta](/delta/) in options |
| **Key use** | Position-sizing decisions; risk budgeting |
| **Limitation** | Assumes linear (delta) relationship; breaks down for tail risk |

</aside>

## Definition and formula

Marginal VaR is mathematically the derivative of total portfolio VaR with respect to a position size. If your portfolio's current VaR is EUR 1 million at a 95% confidence level over one day, and you add 100 units of an asset, marginal VaR tells you how many additional euros of risk you incur per unit. If marginal VaR is EUR 500 per unit, adding 100 units increases portfolio VaR to approximately EUR 1.05 million.

The general form is:

**Marginal VaR = ∂VaR(portfolio) / ∂Position**

In practice, risk systems compute this by first calculating total VaR using historical simulation or a variance-covariance model, then re-running the calculation with a slightly larger position in the target asset. The difference, divided by the position increase, yields marginal VaR.

Because most portfolio models assume linear relationships (a strong assumption for nonlinear instruments like options), marginal VaR often proxies to the beta or correlation-weighted sensitivity of the candidate position to the entire portfolio. A stock with high correlation to existing holdings has high marginal VaR; an uncorrelated asset has low marginal VaR, even if it is volatile in isolation.

## Why marginal VaR matters: the diversification lens

A position can be volatile in standalone terms yet add very little risk to a well-diversified portfolio if it is uncorrelated with existing holdings. Marginal VaR captures this insight: it is the only risk metric that accounts for how a new position interacts with what you already own.

A trader at an investment bank, for example, might propose a large position in a currency pair. Its standalone volatility is high; naive risk managers might reject it outright. But marginal VaR can reveal that the currency pair is negatively correlated with existing equity and bond risk, so adding it actually reduces portfolio VaR. Marginal VaR thus provides a quantitative argument for diversification.

Conversely, a "safe" equity in a quiet sector might have low standalone volatility but very high marginal VaR if it is highly correlated with the rest of the equity book. Adding it concentrates risk rather than dispersing it.

## The mechanics: delta approximation

Because VaR is expensive to recalculate from scratch, most practitioners use the delta approximation. This assumes that a small change in position size produces a proportional change in VaR. Under this simplification, marginal VaR is roughly equivalent to the position's weighted beta or factor sensitivity within the portfolio.

If a stock's [beta](/beta/) to the portfolio is 1.2, and the portfolio's overall [volatility](/historical-volatility/) is 12%, then adding that stock increases portfolio risk, all else equal, at a rate proportional to 1.2 × 12%. This is faster than the portfolio's baseline drift, so the stock has positive marginal VaR.

The delta approach works well for linear instruments (stocks, bonds, currencies) and short risk horizons. It breaks down for options, where [gamma](/gamma/) (the curvature of the price–delta relationship) becomes material, and for tail events, where correlations collapse and the linear assumption fails.

## Risk budgeting and position limits

Marginal VaR is the primary input to [risk budgeting](/). A portfolio manager with a total VaR limit—say EUR 2 million per day—must allocate sub-limits to traders and desks. Marginal VaR tells the risk manager how much of the total budget each trader is consuming per unit of notional exposure.

A trader who can add a position with low marginal VaR (high diversification) consumes less of the risk budget per euro of notional than a trader proposing a concentrated bet. This creates an incentive to diversify: traders with smart marginal VaR profiles get larger position limits.

Position-limit frameworks, in practice, often set an upper limit on the absolute notional a trader can hold, a limit on [gross exposure](/), and a limit on the marginal VaR they can incur on proposed new trades. This third constraint is the most forward-looking: it prevents a trader from gradually turning a diversified book into a correlated, concentrated one.

## Limitations: linearity and tail events

The greatest weakness of marginal VaR, in practice, is its reliance on linear approximation and historical correlations. During market dislocations—panics, credit events, forced selling—correlations soar. An asset with low historical correlation to the rest of the portfolio can suddenly become highly correlated when stress arrives. This is [tail dependence](/tail-dependence-coefficient/), and marginal VaR, calculated on calm-market data, is blind to it.

Options present another challenge. A long call option far out of the money has low [delta](/delta/) and thus appears to have low marginal VaR. But if the underlying asset approaches the strike, the call's delta accelerates. Marginal VaR computed using delta alone misses this non-linearity. A second-order correction using [gamma](/gamma/) helps, but introduces complexity.

Furthermore, marginal VaR is a backward-looking metric when based on historical simulation or sample correlations. It assumes that future correlations match those observed in past data. Regime changes—a shift in economic cycle, a structural policy change—can make historical marginal VaR estimates dangerously optimistic.

## Relation to component VaR and risk attribution

Marginal VaR and [component VaR](/component-var/) are complementary but distinct. Component VaR asks: of my current portfolio VaR, how much is contributed by the positions I already own? Marginal VaR asks: if I were to add a new position, how much additional VaR would I incur?

For an existing position, the sum of all positions' component VaRs equals total portfolio VaR. Marginal VaR, by contrast, does not aggregate; it applies to a hypothetical new trade.

In practice, a desk using a [risk limit](/value-at-risk/) framework will use component VaR to monitor the breakdown of existing risk, and marginal VaR to vet proposals for new trades. A trader's daily report shows component VaR by position or desk; when the trader proposes to add to a position, risk management evaluates the marginal VaR of that increment.

## See also

<div class="wiki-seealso">

### Closely related

- [Value at risk](/value-at-risk/) — the foundational risk metric of which marginal VaR is a sensitivity
- [Component VaR](/component-var/) — decomposes existing portfolio risk into position-level contributions
- [Delta](/delta/) — the linear sensitivity to price changes; forms the basis of marginal VaR approximation
- [Gamma](/gamma/) — the curvature correction to delta; becomes material for options and tail risk
- [Tail dependence coefficient](/tail-dependence-coefficient/) — quantifies correlation breakdown in extreme events, a blind spot for marginal VaR
- [Risk budgeting](/risk-budgeting/) — uses marginal VaR to allocate risk limits across desks

### Wider context

- [Portfolio risk](/market-risk/) — the broader framework in which marginal VaR sits
- [Volatility smile](/volatility-smile/) — illustrates non-linearity in derivatives pricing
- [Stress testing](/stress-testing/) — complements marginal VaR by testing tail outcomes

</div>
