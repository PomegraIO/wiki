---
title: "Value Momentum Blend"
description: "A portfolio strategy combining value-factor (cheap) and momentum-factor (trendy) stocks."
keywords:
  - value momentum blend
  - factor combination
  - multi-factor investing
  - value momentum rotation
---

*A **value momentum blend** is a portfolio strategy that combines two successful stock-selection factors: [value](/wiki/value-investing/) (buying underpriced companies) and [momentum](/wiki/momentum-investing/) (buying stocks in uptrends). Rather than choosing one factor exclusively, the blend owns stocks that rank high on both value and momentum, or uses a weighted combination of both, aiming to capture [alpha](/wiki/alpha/) from both sources while reducing [volatility](/wiki/historical-volatility/) through diversification.*

<aside class="wiki-infobox">

| Approach | Weighting |
|----------|-----------|
| **Pure value** | 100% value factor; momentum ignored |
| **Pure momentum** | 100% momentum factor; value ignored |
| **Blend (equal)** | 50% value, 50% momentum |
| **Blend (dynamic)** | Weights shift based on factor performance |
| **Intersection** | Stocks scoring high on both (stricter filter) |
| **Separate sleeves** | Two portfolios (value and momentum) combined |

</aside>

## Why combine value and momentum: complementary factors

[**Value stocks**](/wiki/value-investing/) (cheap on P/E, P/B, P/S ratios) have historically outperformed the market by ~3–5% annualized, but with periods of severe underperformance (2010–2020, when tech mega-caps soared while value lagged). [**Momentum stocks**](/wiki/momentum-investing/) (stocks in uptrends, high [relative strength](/wiki/relative-strength-investing/)) have outperformed by ~5–8% annualized, but also with drawdowns (momentum crashes are violent; June 2022 saw a 20%+ drop in momentum factors as central banks tightened). The two factors are weakly correlated (sometimes even negatively correlated), so holding both reduces portfolio [volatility](/wiki/portfolio-mental-accounting/). A portfolio that is 50% value + 50% momentum has lower standard deviation than a portfolio that is 100% either one. Fama-French research (Carhart, 1997; Blitz et al., 2010) shows that a blend outperforms either factor alone on a risk-adjusted basis, because the factors' uncorrelated downturns smooth total portfolio return.

## The Carhart four-factor model and momentum as a fifth

The [**Carhart four-factor model**](/wiki/carhart-four-factor-model/) extends Fama-French's three factors (market, size, value) by adding momentum as a fourth systematic factor. Carhart showed that a portfolio long high-momentum stocks + short low-momentum stocks earned ~12% annualized alpha from 1963–1995. Momentum is thus one of the most robust and long-lived asset-pricing anomalies. However, adding momentum to a pure value strategy is not always profitable: during value rallies (2003–2006, 2022–2024), momentum can drag returns if momentum stocks are growth (expensive) names while value stocks are cheaper. A blend acknowledges this trade-off and captures both sources of return, accepting that neither is always best.

## Practical implementation: stock picking versus factor investing

A **stock-picking blend** uses both value and momentum screens: a portfolio manager ranks all stocks on value (lowest P/E, highest FCF yield), ranks all stocks on momentum (52-week high, relative strength), and combines the ranks into a composite score. A stock ranked 1st on value but 500th on momentum gets a blended score depending on weights. This requires fundamental analysis and frequent rebalancing. Conversely, a **factor-based ETF blend** owns two [**factor ETFs**](/wiki/factor-etf/): a value ETF (such as VTV, iShares U.S. Value) and a momentum ETF (such as MTUM, Vanguard U.S. Momentum), in equal or weighted proportions. This is passive, transparent, and easy to implement; the investor is essentially running a two-asset portfolio of factor sleeves. A third approach is a dedicated blend ETF (such as VBLAX, Vanguard U.S. Value Momentum ETF), which applies blended scoring internally.

## Seasonality and market regimes: when blends shine

Blends are most valuable when both value and momentum are available simultaneously (both scoring well). This is common in mid-cycle economic expansions and during low-volatility regimes. Conversely, blends suffer during:
- **Growth booms** (2015–2019, 2021): momentum wins (growth stocks soar), value lags (value stocks stagnate); a blend realizes less upside than 100% momentum.
- **Value rallies** (2003–2006, 2022–2024): value wins, momentum lags; a blend realizes less upside than 100% value.
- **Momentum crashes** (June 2022, October 2008): momentum collapses 20%+, value is neutral or positive; a blend limits losses but still underperforms 100% value.
- **Value traps** (a value stock is cheap because it is deteriorating, not because it is underpriced): momentum acts as a filter, excluding stale names that are falling.

## The diversification benefit: lower volatility, smoother returns

Empirically, a 50–50 value-momentum blend has lower volatility than either pure factor. If value has 12% annual volatility, momentum has 14%, and correlation is 0.4, the blend has ~10% volatility—lower than either alone because their downturns are partially offset. This is powerful for risk-averse investors who prefer steadier returns; a blend will outperform either pure factor on a Sharpe-ratio basis (return per unit of volatility) even if total return is slightly lower. For individuals in retirement who need steady dividend income, a value-momentum blend is more palatable than a high-volatility momentum-only portfolio.

## Dynamic blends: adjusting weights based on factor performance

A **dynamic blend** adjusts the weights of value and momentum based on forward-looking indicators. For example:
- **If value is cheap relative to momentum**: (value dividend yield is high, value P/E is low relative to historic levels, value has underperformed for 5+ years), increase value weight to 60–70% and reduce momentum to 30–40%.
- **If momentum is strong** (uptrend in [relative strength](/wiki/relative-strength-investing/), [breadth](/wiki/market-breadth-advances-declines/) positive, earnings revision momentum is high), increase momentum weight.
- **If both are in drawdown**: reduce total allocation to factors and increase cash or defensive stocks.

This requires market timing and adds complexity; most practitioners use a static 50–50 split or follow a simple rule (e.g., "rebalance quarterly to equal weight").

## Value-momentum intersection: the stricter approach

Instead of a weighted blend, some strategies use an **intersection** approach: own only stocks that rank high on *both* value *and* momentum simultaneously. This is a strict filter; it screens out "value traps" (cheap but falling) and "momentum bubbles" (rallying but overvalued). The resulting portfolio is smaller and more concentrated, but it may have lower dispersed value and momentum alpha. A stock that is top decile in value but bottom decile in momentum gets excluded entirely, losing the value benefit. This is useful for tactical allocation (concentrating into the highest-conviction ideas) but sacrifices diversification.

## Sector and style rotation: complementary overlays

Value and momentum factor tilts often translate to sector tilts. Value tilts toward banks, energy, utilities (cyclical, mature sectors); momentum tilts toward tech, healthcare, consumer discretionary (high-growth sectors). A blend that is 50–50 value-momentum will have exposure to both groups, providing implicit sector diversification. However, during sector rotations, a pure momentum or pure value tilt often outperforms: in a growth rotation, momentum-heavy (tech-heavy) portfolios surge; in a value rotation, value-heavy (financial-heavy) portfolios surge. A blend lags both but provides more stable returns.

## Implementation costs and turnover

Value strategies typically have low turnover: the companies stay undervalued for years, and annual rebalancing swaps <20% of holdings. Momentum strategies have higher turnover: a stock that was top decile in 52-week returns might drop to bottom decile within months, requiring portfolio reconstruction. A value-momentum blend has turnover between the two: value positions roll slowly, momentum positions are trimmed and refreshed quarterly. For an active manager, turnover costs matter; a 20% annual turnover at 5 basis points per trade (entry and exit) costs ~20 basis points—meaningful drag. This is why passive factor-blend ETFs are attractive; they standardize turnover and minimize costs.

## Backtesting pitfalls: look-ahead and survivorship bias

Many published studies show that value-momentum blends outperform because of subtle backtesting biases. **Look-ahead bias** occurs if the study computes factors using data not available at decision time (e.g., using year-end earnings to compute a P/E ratio at mid-year). **Survivorship bias** excludes companies that went bankrupt or delisted; these were often value traps, and excluding them inflates measured returns. A properly constructed backtest rebalances on a clear date using only then-available data, includes dead stocks, and accounts for transaction costs. Real-world blends underperform published backtests by 2–5% annualized due to these biases.

## Examples: MSCI and Russell indices

The **MSCI Value Momentum Index** weights stocks on a blend of value metrics (P/B, forward earnings yield, dividend yield) and momentum metrics (price momentum, earnings momentum, sales momentum), selling the least attractive on each dimension. It has outperformed the pure value or pure momentum index by 0.5–1.5% annualized over recent decades, though with periods of underperformance. The **Russell Value Momentum Index** applies similar logic using Russell's proprietary factor definitions. These indices underpin factor ETFs and institutional allocation decisions.

## Combining blends with other factors: size and quality

A more sophisticated approach blends value and momentum with **size** and **quality** factors. A portfolio might weight value (40%), momentum (30%), [quality](/wiki/quality-factor/) (20%), and size (10%), creating a multi-factor portfolio. This adds complexity but can improve diversification and reduce single-factor timing risk. For example, if value is in a painful drawdown, quality and momentum might still be positive, offsetting losses. Vanguard's multi-factor ETFs (such as VUU, VTV) combine multiple factors using proprietary optimization.

<div class="wiki-seealso">

### Closely related
- [Value Investing](/wiki/value-investing/) — The value leg of the blend
- [Momentum Investing](/wiki/momentum-investing/) — The momentum leg
- [Factor Investing](/wiki/factor-investing/) — The broader framework
- [Alpha](/wiki/alpha/) — The excess return factors aim to capture

### Wider context
- [Carhart Four-Factor Model](/wiki/carhart-four-factor-model/) — Academic foundation for momentum as a factor
- [Fama-French Three-Factor Model](/wiki/fama-french-three-factor-model/) — Earlier framework; value is a factor
- [Factor ETF](/wiki/factor-etf/) — Vehicle for implementing the blend
- [Smart Beta](/wiki/smart-beta/) — A class of strategies including blends
- [Relative Strength Investing](/wiki/relative-strength-investing/) — A form of momentum assessment
- [Sector Rotation](/wiki/sector-rotation/) — Related tactical allocation strategy

</div>
