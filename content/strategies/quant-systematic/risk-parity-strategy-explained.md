---
title: "Risk Parity Strategy Explained"
description: "Risk parity allocates capital so each asset class contributes equally to portfolio volatility, rather than allocating by dollar weight. This reweighting favors lower-volatility assets and tends to concentrate in bonds."
keywords:
  - risk parity
  - risk parity strategy
  - volatility-weighted allocation
  - systematic portfolio allocation
  - equal-risk-contribution
  - bonds stocks allocation
---

*Risk parity is a rules-based portfolio construction method that sizes each asset class inversely to its volatility so that all holdings contribute equally to total portfolio risk. Rather than holding 60% stocks and 40% bonds (dollar-weight), a risk parity portfolio might hold 30% stocks, 70% bonds, and 10% commodities, chosen so each position has the same marginal impact on the portfolio's overall volatility. The result is a portfolio that tends to be longer bonds and shorter equities than traditional allocation, with materially different return and drawdown characteristics.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Risk Parity — key facts</div>

<img src="/svg/strategies.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Weighting by volatility, not by dollars, changes the portfolio character.</div>

|   |   |
|---|---|
| **Allocation principle** | Inverse to volatility; all positions have equal risk contribution |
| **Typical equity weight** | 30–40% (much lower than 60-40 stocks) |
| **Typical bond weight** | 50–60% (much higher than 60-40 bonds) |
| **Leverage** | Often used to boost returns to competitive levels |
| **Annual returns** | 6–10% in live funds; returns depend on leverage and cost structure |
| **Downside behavior** | Lower volatility; still suffers in crisis periods |
| **Rebalancing need** | Frequent, because volatility regimes shift; monthly or quarterly typical |

</aside>

## The logic: equal risk contribution

Traditional asset allocation is dollar-weighted. A 60-40 portfolio holds 60% of dollars in stocks and 40% in bonds. This is intuitive but skews risk toward the higher-volatility asset. If stocks are 15% volatile and bonds are 5%, the stock position drives 85–90% of the portfolio's total risk, even though it is only 60% of capital.

Risk parity inverts that logic. If stocks are three times as volatile as bonds, a risk parity portfolio holds stocks at one-third the weight of bonds (in dollars). If stocks are 15% volatile and bonds are 5%, a risk parity portfolio might hold 33% stocks and 67% bonds. With those weights, each position contributes equally (roughly 50% each) to total portfolio volatility.

The calculation requires understanding each asset's individual volatility and how assets correlate with one another. A simplified example: stocks are 15% annual volatility, bonds are 5%, and they have zero correlation. To equalize risk contribution, the stock allocation gets scaled down by the volatility ratio (5% / 15% = 0.33). Normalizing to 100% capital, that gives 33% stocks and 67% bonds.

In reality, risk parity portfolios usually include more than two assets—equities, bonds, commodities, real assets, and sometimes alternatives—and the correlation structure among them is complex and time-varying. The principle remains: weight each asset inversely to its marginal contribution to portfolio volatility.

## The portfolio shift relative to 60-40

The most striking feature of risk parity is how much weight it allocates to bonds. A traditional balanced portfolio (60 stocks, 40 bonds) overweights equities because most investors assume equities should drive returns. A risk parity portfolio, constrained by volatility, drastically underweights equities because their volatility is so high.

This reallocation has profound consequences:

- **Lower total volatility**: A risk parity portfolio's realized volatility is typically 8–11% annually, vs. 10–13% for a 60-40 portfolio. It experiences gentler ups and downs.
- **Lower expected return**: With less exposure to equities (the higher-returning asset over long periods), risk parity expects lower returns before leverage. A 60-40 portfolio might target 6–7% annual returns; a 100% risk parity portfolio might expect 4–5%.
- **Different drawdown behavior**: During equity crashes, risk parity still declines (it holds 30–40% equities), but losses are moderated. In bond rallies, risk parity outperforms.

## Leverage: the critical mechanism

To compete with traditional balanced portfolios on returns, risk parity funds typically use leverage. A 100% risk parity portfolio with expected 4% returns can be leveraged to 1.5x notional exposure, targeting 6% returns with the same volatility profile as a 60-40 portfolio.

Leverage is both the strategy's strength and its weakness. With leverage, risk parity can achieve returns comparable to traditional 60-40 allocations while maintaining lower volatility. Without leverage, risk parity generates lower returns, appealing only to very conservative investors.

But leverage introduces hidden risks. In a sharp credit event, when the cost of financing leverage spikes or lenders demand immediate repayment, a leveraged risk parity fund may be forced to sell assets at the worst time. The 2022 UK pension fund crisis illustrated this: liability-driven investment funds using leverage in bonds and swaps faced margin calls and fire sales when rates rose unexpectedly.

## Volatility regime shifts and rebalancing burden

Volatility is not constant. In quiet markets, stocks might be 12% volatile; in crises, they are 40% volatile. As volatility regimes shift, the ideal risk parity weights shift too. A strategy optimized when stocks were 15% volatile may be wildly misaligned when stocks hit 35% volatility.

This means risk parity portfolios must rebalance frequently—monthly or quarterly—to stay aligned to current volatility. Each rebalance incurs transaction costs and may force the portfolio to buy high (when assets have just become more volatile and risky) and sell low (when they have stabilized).

Because volatility tends to spike during downturns, rebalancing risk parity often means selling the asset that has just crashed (stocks) when it is cheapest and buying bonds when they have rallied into safety. This is the opposite of market-timing discipline and can hurt returns in extended rallies.

## Historical performance and diversification benefits

Academic studies and live performance data show that risk parity typically delivers:
- **Realized volatility** in the 8–11% range (vs. 10–13% for 60-40)
- **Sharpe ratios** roughly equal to or slightly better than balanced portfolios when costs and leverage are fairly applied
- **Drawdowns** slightly smaller in most markets; less advantage during equity crashes

The diversification benefit is real but modest. By holding more bonds, risk parity provides ballast when equities fall (bonds often rise). But the diversification fades in true crisis periods when correlations spike: all assets fall together.

Some of risk parity's appeal lies in its systematic discipline and lack of human judgment. It mechanically rebalances when volatility shifts, without trying to time markets or predict returns. This consistency has attracted large institutional investors, especially those uncomfortable with traditional active management.

## Multi-asset risk parity

Pure risk parity (equities, bonds, commodities, currency hedges) allocates meaningfully to commodities and sometimes real estate because their volatility is high and their correlation with traditional assets is useful for diversification.

A typical multi-asset risk parity portfolio might hold:
- 30–35% equities (global mix)
- 45–55% fixed income (governments, corporate, longer-duration)
- 10–15% commodities
- 5–10% real assets or alternatives

Each position is sized so that none dominates portfolio volatility. The result is a globally diversified portfolio, but one that looks very different from the 60% stocks + 40% bonds default.

## Costs and implementation challenges

Risk parity funds typically charge higher fees than passive index funds but lower than active hedge funds. Fees range from 0.3% to 1.0% annually, depending on leverage and rebalancing frequency.

Implementation challenges include:
- **Leverage costs**: Financing leverage can add 0.5–1.5% annually depending on credit spreads.
- **Rebalancing costs**: Frequent rebalancing incurs bid-ask spreads and commissions.
- **Volatility forecasting**: Estimating volatility accurately is nontrivial. Errors lead to misallocation.
- **Correlation assumptions**: If correlations break down (as they often do in crises), the diversification benefits evaporate.

## When risk parity underperforms

Risk parity excels in environments where volatility is stable and correlations hold. It struggles when:

- **Equities rally strongly over long periods**: A 60-40 portfolio outperforms because it holds more of the appreciating asset.
- **Inflation hits unexpectedly**: Leverage becomes expensive and bonds decline, but risk parity still has heavy bond allocation.
- **Credit stress emerges**: Leveraged risk parity funds face margin calls and forced selling.

The 2000s (equity bear market, bond rally) were favorable for risk parity. The 2010s (massive equity rally, declining rates) were poor for risk parity. Relative performance depends heavily on whether the current regime favors equities or bonds.

## Comparison to factor investing and alternatives

Risk parity is a systematic allocation method but not a factor strategy in the traditional sense. It does not attempt to capture equity risk premia or momentum. It is purely a volatility-constrained rebalancing rule.

Some practitioners view risk parity as an alternative to active management—a disciplined, low-cost way to allocate across asset classes without trying to pick winners. Others see it as a liability-management tool, especially useful for pension funds that need predictable drawdowns and stable volatility.

## See also

<div class="wiki-seealso">

### Closely related

- [Walk-Forward Optimization](/walk-forward-optimization/) — A validation method for testing whether risk parity parameters are robust
- [Rebalancing Frequency Effect on Returns](/rebalancing-frequency-effect-on-returns/) — Risk parity requires frequent rebalancing due to volatility shifts
- [Backtest Overfitting Explained](/backtest-overfitting-explained/) — Risk parity's simplicity makes it less prone to overfitting than complex strategies
- [Asset Allocation](/asset-allocation/) — The broader context of portfolio weighting
- Volatility — The core input to risk parity calculations
- [Diversification](/diversification/) — Risk parity's central principle

### Wider context

- [Leverage Ratio](/leverage-ratio-forex/) — How risk parity uses leverage to boost returns
- [Factor Investing](/factor-investing/) — Alternative systematic approach to portfolio construction
- Hedging — Some risk parity portfolios hedge tail risk
- [Sharpe Ratio](/sharpe-ratio/) — Metric used to compare risk parity to traditional portfolios

</div>