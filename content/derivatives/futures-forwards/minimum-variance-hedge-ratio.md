---
title: "Minimum Variance Hedge Ratio"
description: "The futures position size that minimises residual portfolio variance, derived from the correlation between spot and futures prices."
keywords:
  - hedge ratio
  - hedging
  - variance
  - correlation
  - futures
  - risk management
image: "/svg/derivatives.svg"
---

*The **minimum variance hedge ratio** (MVHR) is the optimal number of [futures contracts](/futures-contract/) to short (or long) in order to minimise the variance of a hedged portfolio. Rather than hedging 100% of exposure using a simple 1:1 ratio, the MVHR accounts for imperfect correlation between the spot asset and the futures contract, ensuring the residual risk is as small as possible. It is a cornerstone of quantitative [hedging](/protective-put/) and [risk management](/value-at-risk/).*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Minimum Variance Hedge Ratio — key facts</div>

<img src="/svg/derivatives.svg" alt="A financial contract symbol representing derivatives and leverage." />

<div class="wiki-infobox-caption">A mathematical solution to sizing a hedge when the spot and futures are imperfectly correlated.</div>

|   |   |
|---|---|
| **What it is** | The futures position size (expressed as a ratio or number of contracts) that minimises portfolio variance |
| **Formula** | h* = (ρ × σ_spot) / σ_futures, where ρ is correlation, σ is volatility |
| **Key inputs** | Historical spot and futures price changes; correlation coefficient |
| **Assumption** | Linear relationship between spot and futures (usually holds well) |
| **Output** | A ratio between 0 and 1 (or occasionally > 1 if futures are less volatile than spot) |
| **Practical use** | Portfolio managers, commodity traders, currency hedgers |
| **Limitation** | Assumes past volatility and correlation predict the future; ignores transaction costs |

</aside>

## The intuition: not all hedges are perfect

A portfolio manager holding $10 million of [equity](/common-stock/) can hedge perfectly by selling $10 million of [stock index futures](/stock-index-futures/). If the index and the manager's portfolio move in perfect lockstep (correlation = 1.0), a 1:1 hedge eliminates all risk.

But real portfolios are rarely perfect reflections of an index. A small-cap growth fund, for instance, correlates with the [S&P 500 Index](/sp-500-index/) at maybe 0.85, not 1.0. In a market downturn, the growth fund falls 15% whilst the index falls 10%. Conversely, in a rally, the growth fund might rise 18% whilst the index rises 12%. The extra [idiosyncratic risk](/idiosyncratic-risk/) is the fund's own factor bets and security selection.

A naïve 1:1 futures hedge would over-hedge. It would eliminate all index risk but leave the manager short the growth factor. A better hedge size accounts for the lower correlation and lower volatility impact, allowing some idiosyncratic upside to remain whilst reducing downside.

## The mathematics: correlation and volatility

The MVHR is derived from a simple regression of spot returns on futures returns:

**Spot Return = α + β × Futures Return + ε**

The slope β is the hedge ratio. Under the hood:

**h* = (ρ × σ_spot) / σ_futures**

Where:
- **ρ** = correlation between spot and futures price changes
- **σ_spot** = standard deviation (volatility) of spot returns
- **σ_futures** = standard deviation of futures returns

If the spot asset is as volatile as the futures but perfectly correlated (ρ = 1.0), then h* = 1.0: hedge the full notional value. If the spot is less volatile (σ_spot = 0.5 × σ_futures) but still perfectly correlated, then h* = 0.5: hedge only half the value.

If correlation is imperfect (ρ = 0.8), the ratio shrinks proportionally. An 0.85-correlated, equally-volatile portfolio requires an MVHR of 0.85, meaning you short 85% of notional value in [futures](/futures-contract/), not 100%.

## Why correlation matters more than most hedgers realise

Two assets can be highly volatile individually but have low correlation. A [currency](/currency-risk/) trader might hold a short position in sterling (volatile) and hedge with a sterling/dollar [futures](/futures-contract/) (also volatile), but if the correlation is only 0.6 due to other macroeconomic flows, the MVHR is just 0.6. Hedging 100% would actually *increase* portfolio variance by introducing unhedged futures risk.

Conversely, two assets can be less volatile but highly correlated. An [index fund](/index-fund/) tracking the [S&P 500 Index](/sp-500-index/) often correlates above 0.95 with the index [futures](/futures-contract/), so MVHR is close to 1.0 despite both having similar modest volatility.

## Estimating the inputs: the practical difficulty

Correlation and volatility must be estimated from historical data. A portfolio manager typically uses one year of daily (or weekly) returns, regresses spot changes on futures changes, and extracts the slope. The slope is the MVHR.

The problem: past correlation and volatility are not guarantees of the future. In a market crisis, correlations can spike (all assets fall together), rendering a historical MVHR obsolete. A portfolio manager often uses multiple lookback windows (3-month, 6-month, 1-year) and monitors the hedge ratio, rebalancing if the relationship shifts.

## Example: hedging a commodity position

A refinery holds 1 million barrels of [crude oil](/crude-oil/), worth $70 million at $70 per barrel. It expects to sell in three months but fears the price will fall. It can hedge by selling [crude oil futures](/crude-oil/).

Historically, the refinery's inventory (a mix of light and heavy crude) correlates at 0.92 with light sweet crude [futures](/futures-contract/). The refinery's inventory volatility is $65 million / 1 million barrels = $65 per barrel (in standard deviation); futures volatility is $70 per barrel.

**MVHR = (0.92 × 65) / 70 = 0.855**

The refinery should short futures worth **0.855 × $70 million = $59.85 million**, or about 856,000 barrels of futures. It leaves 144,000 barrels unhedged, retaining some upside if the basis (spread between inventory and futures) widens in its favour—a reasonable trade-off.

## Beta as MVHR in equity markets

In [equity](/common-stock/) markets, the MVHR is closely related to [beta](/beta/). If a portfolio has a [beta](/beta/) of 1.2 relative to the [S&P 500 Index](/sp-500-index/), it means it correlates with the index at a high level and is 1.2× as volatile. To hedge all index risk, the portfolio manager would short 1.2 units of notional [index futures](/stock-index-futures/) per unit of portfolio—a ratio of 1.2. This is exactly the MVHR: it scales both correlation and relative volatility.

A low-beta, defensive portfolio (ρ = 0.95, beta = 0.7) would MVHR at 0.7: hedge only 70% of notional value.

## Transaction costs and the rebalance decision

Once a hedge is in place, the MVHR drifts as correlation and volatility change. A portfolio manager must decide: rebalance now (incurring transaction costs), or wait? If rebalancing costs 10 basis points and the hedge ratio has drifted from 0.85 to 0.84, rebalancing is not worth it. But if it has drifted to 0.70, rebalancing may be justified.

This is why large institutional managers use quantitative frameworks to trigger rebalance bands. They might rebalance only when the hedge ratio deviates by more than 0.05 from target.

## Limitations and the real world

The MVHR assumes:

1. **Linear relationship:** Spot and futures changes are linearly related. Usually true; sometimes breaks in crises.
2. **Constant correlation and volatility:** Historical relationships persist. Often false during stress events.
3. **No transaction costs:** Hedging is free. It is not.
4. **Normal distributions:** Returns are normally distributed, so variance minimisation is the right objective. Real returns have fat tails.

Despite these caveats, the MVHR is widely used and serves as a robust starting point. Many managers refine it with macroeconomic overlays, [value-at-risk](/value-at-risk/) constraints, or stress tests before executing.

## See also

<div class="wiki-seealso">

### Closely related

- [Futures Contract](/futures-contract/) — the derivative instrument used in the hedge
- [Stock Index Futures](/stock-index-futures/) — the primary equity hedging vehicle
- [Beta](/beta/) — the correlation-scaled sensitivity of a portfolio to an index
- [Protective Put](/protective-put/) — an alternative (non-linear) hedging approach using options
- [Idiosyncratic Risk](/idiosyncratic-risk/) — the portfolio risk not explained by the index, left unhedged
- [Value-at-Risk](/value-at-risk/) — a complementary risk measure combining volatility and correlation

### Wider context

- Correlation — the statistical foundation of the hedge ratio
- [Volatility Smile](/volatility-smile/) — how volatility varies; relevant to option hedges
- [Hedging](/protective-put/) — the broader goal of offsetting portfolio risk
- [Asset Allocation](/asset-allocation/) — the strategic decision underlying tactical hedges
- [Diversification](/diversification/) — reducing risk through low-correlation holdings rather than hedging

</div>
