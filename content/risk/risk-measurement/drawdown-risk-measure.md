---
title: "Drawdown Risk Measures"
description: "Peak-to-trough declines used to assess portfolio performance volatility and loss severity."
keywords:
  - drawdown
  - maximum drawdown
  - underwater peak
  - portfolio volatility
---

*A **drawdown** is the decline from a portfolio's peak value to its subsequent trough, measured in dollars or percentage terms. **Maximum drawdown** is the largest peak-to-trough loss a portfolio has experienced over a given period. This metric captures the investor's worst-case loss if they bought at the peak and sold at the trough—a valuable complement to [volatility](/wiki/historical-volatility/) statistics because it directly measures loss severity rather than price oscillation.*

<aside class="wiki-infobox">

| Metric | Definition |
|---|---|
| **Drawdown** | Current decline from the nearest prior peak |
| **Maximum drawdown** | Largest peak-to-trough loss in historical data |
| **Underwater duration** | Time spent below prior peak |
| **Recovery time** | Months or years to regain prior peak |
| **Volatility vs. drawdown** | Volatility is symmetric; drawdown is asymmetric (only down) |

</aside>

## Why drawdown matters more than volatility

[Volatility](/wiki/historical-volatility/) measures price oscillation—how much a return bounces around its average. A stock with high volatility might swing ±20% monthly but end the year flat. An investor who cares only about volatility might view this as risky; an investor who cares about loss recovery might view it as acceptable if the swings offset.

Drawdown, by contrast, measures actual loss: the gap between where you bought and where the price fell. A portfolio that peaks at $100 and falls to $80 has a 20% drawdown—a real loss. Volatility alone doesn't capture this. Two portfolios with identical volatility might have very different drawdowns if one experiences a sudden crash (large drawdown) while the other oscillates smoothly around its trend (small drawdown).

## Calculating drawdown

**Running maximum** is the highest value the portfolio has reached up to the current date. For each date, the running maximum is either yesterday's running maximum or today's value, whichever is higher. Once a peak is set, it doesn't reset upward until a new all-time high is achieved.

**Drawdown** is then calculated as: `(Current Value - Running Maximum) / Running Maximum`.

If a portfolio is at $100, then rises to $120, then falls to $96, the drawdown at $96 is `(96 - 120) / 120 = -20%`. The portfolio has not recovered to its peak of $120.

**Maximum drawdown** is the worst (most negative) drawdown over the entire lookback period. If a portfolio experienced a -20% drawdown, then recovered, then fell -15%, the maximum drawdown is -20%.

## Interpreting drawdowns

A maximum drawdown of -20% means the portfolio lost 20% from its peak to trough. Recovering from a -20% drawdown requires a 25% gain (because $80 × 1.25 = $100). A -50% drawdown requires a 100% gain to recover. This non-linear recovery window is critical: large drawdowns are disproportionately damaging because they demand outsized percentage gains to reverse.

This asymmetry explains why drawdown is psychologically and practically important. An investor can tolerate modest volatility and oscillation; they cannot tolerate large permanent losses. Drawdown directly measures the latter.

## Drawdown duration and recovery time

Beyond the size of the drawdown, investors care about duration: how long the portfolio stayed underwater, and how long until recovery to the prior peak. A -30% drawdown that recovers in three months is less damaging than a -30% drawdown followed by years of sideways movement. This is partly psychological—investors' patience erodes with duration—and partly financial—opportunity cost accrues while capital is trapped.

The S&P 500 experienced a -57% drawdown from peak to trough in 2008–2009; it took until 2013 to recover to the prior peak. Investors who entered in 2007 had zero returns for five years despite a strong 2010–2012 run. A drawdown duration metric captures this pain.

## Drawdown vs. volatility in asset allocation

A [volatility](/wiki/historical-volatility/)-minimizing portfolio might look very different from a drawdown-minimizing one. Bonds reduce volatility but don't eliminate drawdowns (bond prices fall when rates rise). A portfolio of uncorrelated assets reduces volatility but not necessarily maximum drawdown if they all crash in unison during a crisis (as they did in March 2020).

[Risk parity strategies](/wiki/risk-parity-strategy/) often target equal drawdown contribution rather than equal volatility. The logic: an investor's true concern is loss, not price bounce. A 20% drawdown in stocks and a 10% drawdown in bonds both matter; equal volatility weighting might allow the stock component to dominate in a crisis, creating a portfolio drawdown larger than intended.

## Tail risk and fat tails

Drawdown is particularly sensitive to [tail risk](/wiki/tail-risk/)—the probability of extreme events. Historical volatility assumes returns are normally distributed; reality involves occasional large moves. A portfolio with historically normal distributions might suddenly experience a -40% drawdown during a market panic that was statistically "impossible" under normal assumptions. Hedge funds and risk managers use drawdown limits as a backstop: if a portfolio experiences a drawdown larger than some threshold (say, -15%), the strategy is shut down or rebalanced, regardless of expected returns.

This is why [value-at-risk](/wiki/value-at-risk/) (VaR) and [conditional value-at-risk](/wiki/conditional-value-at-risk/) (CVaR) are complementary to simple drawdown analysis. VaR estimates the probability of a drawdown of a given size; CVaR estimates the expected loss if you exceed the VaR threshold. Together, these provide a fuller picture of downside risk.

## Limitations of drawdown analysis

Drawdown is backward-looking. Historical maximum drawdown tells you the worst loss that has occurred, not the worst loss that *could* occur. A portfolio that has never experienced a -40% drawdown might be vulnerable to one if market conditions change structurally.

Drawdown also doesn't account for the *timing* of a drawdown relative to the investor's horizon. A retiree cannot afford a large drawdown; a 25-year-old with steady income can recover from it. A drawdown that occurs near retirement is far more damaging than an identical drawdown early in the accumulation phase, a distinction drawdown statistics alone don't capture.

## Practical use in portfolio management

Portfolio managers use maximum drawdown limits as a constraint. A hedge fund might promise investors: "Maximum historical drawdown: -15%." This sets expectations and provides a governance guardrail. A retail investor might use drawdown as a rebalancing trigger: if the portfolio falls more than 15% from its recent peak, buy dips to restore the target allocation.

Systematic traders monitor drawdown real-time and implement [stop-losses](/wiki/stop-order/) if drawdown exceeds a threshold. This is more aggressive than long-term investing but essential for strategies with leverage or concentrated positions where a large drawdown erodes capital faster than could be offset by future gains.

<div class="wiki-seealso">

### Closely related
- [Value-at-Risk](/wiki/value-at-risk/) — Probability-based loss estimate
- [Conditional Value-at-Risk](/wiki/conditional-value-at-risk/) — Expected loss beyond VaR threshold
- [Volatility](/wiki/historical-volatility/) — Price oscillation, distinct from drawdown

### Wider context
- Risk Management — Broader framework
- [Risk Parity](/wiki/risk-parity-strategy/) — Portfolio construction using drawdown concepts
- [Tail Risk](/wiki/tail-risk/) — Extreme event exposure

</div>
