---
title: "Risk Budgeting"
description: "The process of allocating a portfolio's total risk allowance across sub-strategies, asset classes, or positions to achieve a target risk level."
keywords:
  - risk budgeting
  - portfolio risk
  - risk allocation
  - risk limits
  - portfolio construction
  - factor risk
image: "/svg/risk.svg"
---

*[Risk budgeting](/risk-budgeting/) is the practice of deciding how much total portfolio risk you can tolerate, then dividing that budget across strategies, markets, or positions. It transforms an abstract tolerance for loss into concrete position limits that govern every trade.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Risk Budgeting — key facts</div>

<img src="/svg/risk.svg" alt="An abstract editorial mark for risk allocation and portfolio management." />

<div class="wiki-infobox-caption">The difference between a risk target and a risk blow-up is discipline in divvying it up.</div>

|   |   |
|---|---|
| **What it is** | Allocating a portfolio's total allowable risk across sub-strategies or factors |
| **Also called** | Risk allocation, risk limits, risk framework |
| **Common metrics** | [Value at Risk](/value-at-risk/) (VaR), [volatility](/historical-volatility/), maximum drawdown |
| **Typical approach** | Calculate total risk, assign limits to strategies, monitor against limits |
| **Key challenge** | Correlations change; strategies that diversify calmly may tank together in crisis |
| **Enforcement** | Position limits, trading restrictions, automated stops if risk limit approaches |

</aside>

## The portfolio-wide risk perspective

Most traders focus on the risk of individual positions. They size each trade, place a [stop-loss](/stop-loss-orders/), and move on. But a portfolio that respects individual position limits can still explode if those positions are correlated. Five uncorrelated 2% positions are a manageable 10% portfolio risk. Five correlated 2% positions in the same sector are a concentrated 10% sector bet that could lose 30% in a downturn.

Risk budgeting flips the viewpoint: start with the total risk you can afford, then work backward. Decide that your portfolio can tolerate, say, a 15% annual [volatility](/historical-volatility/) or a maximum 20% drawdown. That becomes your total risk budget. Now allocate it: perhaps 8% to [equity](/equity-financing/), 5% to [fixed-income](/corporate-bond/), 2% to alternatives. Within equities, perhaps 3% to US large-cap, 3% to international, 2% to emerging markets. Within each bucket, individual positions are then sized to fit the sub-budget.

This ensures that your portfolio's aggregated risk reflects your actual tolerance, not just the sum of individual prudences. It also prevents the common mistake of oversizing in the area you're most confident in, at the expense of diversification.

## Volatility, Value at Risk, and drawdown

The metric you choose to define risk matters enormously. Most institutional portfolios measure risk as [volatility](/historical-volatility/): the standard deviation of daily or monthly returns. A portfolio with 15% annualized volatility typically experiences moves of about 1% on an average day (15% / √250 trading days ≈ 1%). This is intuitive and easy to calculate.

But volatility does not capture tail risk. A 15% volatility portfolio can have a rare but devastating 50% drop if that drop is concentrated in a few catastrophic days. For this reason, many risk managers also calculate [Value at Risk](/value-at-risk/) (VaR): the maximum loss expected on a bad day with a certain confidence level (e.g., 95% or 99%). A 95% VaR of 3% means that on 1 in 20 days, the portfolio could lose 3% or more. It's a riskier picture than volatility alone implies.

Maximum drawdown—the largest peak-to-trough decline from any date to any future date—is another common metric. A portfolio might have 12% annualized volatility but a 25% maximum drawdown, meaning one horrible stretch wiped out a quarter of cumulative gains. Some investors care more about drawdown than volatility, because drawdowns determine whether they can psychologically stay invested.

Effective risk budgeting uses multiple metrics. You might target 15% volatility, a 95% VaR of 2.5%, and a maximum drawdown no worse than 20%. These constraints pull in different directions, forcing you to build a portfolio that is robust across multiple definitions of risk.

## Concentrated bets and diversification limits

Within a risk budget, you must decide how concentrated or diversified to be. A hedge fund with a £1 billion portfolio and a 10% annual volatility budget (£100 million of risk) could allocate all £100 million to a single bet, creating a concentrated portfolio. Or it could spread it across 20 uncorrelated bets of £5 million each.

Concentration creates larger winners and larger losers; diversification smooths the ride. The choice depends on conviction. If the manager has a few very high-confidence bets and high conviction in their edge, concentration may maximise expected returns for the risk taken. If the manager has many moderate-confidence ideas with uncorrelated drivers, diversification reduces [idiosyncratic risk](/idiosyncratic-risk/) and improves the risk-return trade-off.

Most institutional portfolios use position limits to prevent over-concentration. A position can be no more than 5% of the portfolio; a strategy can be no more than 20%. These are arbitrary caps, but they prevent the scenario where one idea dominates the portfolio's risk and return.

## Correlations as the hidden budget-breaker

Risk budgeting rests on the assumption that the bets you've sized for separately will behave as you expect. But correlations are unstable. Three [equity](/stock/) strategies that have a 0.3 correlation in normal times may jump to 0.8 correlation during a market crash, when all equities tank together. A portfolio that allocated 8% risk to equities based on a diversified split across sub-strategies finds itself with a 15% equity drawdown that violates the entire risk budget.

This is the eternal frustration of risk budgeting: it is most violated exactly when it is most needed. In a crisis, correlations spike, and previously diversified bets become correlated bets. The risk budget that made sense in backtests becomes fiction in live markets.

The practical response is to stress-test the risk budget against historical crises and to be more conservative than the data suggests. If historical correlations are 0.3 but worst-case is 0.8, you might allocate as if correlations were 0.5. You also monitor correlations in real time and adjust if they drift.

## See also

<div class="wiki-seealso">

### Closely related

- [Position Sizing](/position-sizing/) — the individual-position-level enforcement of the risk budget
- [Stop-Loss Order](/stop-loss-orders/) — an automated enforcement mechanism if risk limits are approached
- [Kelly Criterion](/kelly-criterion/) — mathematical optimization of position sizing given an edge
- [Value at Risk](/value-at-risk/) — one metric for measuring the portfolio's tail-risk budget
- [Diversification](/diversification/) — spreading positions to respect the risk budget across uncorrelated bets
- [Asset Allocation](/asset-allocation/) — the strategic split of capital across classes within the risk budget

### Wider context

- [Volatility](/historical-volatility/) — the daily price swings that risk budgeting constrains
- [Correlation](/diversification/) — the linkages between positions that make correlations shift in crises
- [Leverage Ratio](/leverage-ratio-forex/) — borrowing to increase bets within a fixed risk budget (dangerous)
- [Hedge Fund](/hedge-fund/) — institutional application of systematic risk budgeting

</div>
