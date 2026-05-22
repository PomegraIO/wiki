---
title: "Risk Parity Strategy"
description: "Portfolio construction method allocating equal risk contribution across asset classes rather than equal capital weight."
keywords:
  - risk parity
  - portfolio construction
  - asset allocation
  - leverage
  - volatility weighting
---

*A **risk parity strategy** allocates capital to different [asset classes](/wiki/asset-allocation/) so that each contributes equally to the portfolio's total risk. Instead of weighting 60% stocks and 40% bonds by dollar amount, risk parity sizes positions so that stock and bond volatility contribute the same standard deviation to the overall portfolio.*

<div class="wiki-hatnote">
For traditional fixed-weight allocation, see <a href="/wiki/asset-allocation/">/wiki/asset-allocation/</a>. For systematic risk concepts, see <a href="/wiki/systematic-risk/">/wiki/systematic-risk/</a>.
</div>

<aside class="wiki-infobox">

| Aspect | Detail |
|--------|--------|
| **Allocation Principle** | Equal risk contribution, not equal capital weight |
| **Typical Composition** | Stocks, bonds, commodities, alternatives; sized by inverse volatility |
| **Leverage** | Often employs moderate leverage (1.5x to 2x) to reach target risk |
| **Rebalancing** | Quarterly or semi-annual, adjusting for changing [volatility](/wiki/historical-volatility/) |
| **Key Advantage** | Reduces dependence on single asset class; diversifies return sources |
| **Key Challenge** | Requires leverage, higher costs, concentration risk in tail events |
| **Performance** | Most effective in rising-rate or [stagflation](/wiki/stagflation/) environments |
| **Associated Fee** | Higher management fees due to trading and leverage costs |

</aside>

## Why equal dollar weight is inefficient

Traditional [asset allocation](/wiki/asset-allocation/) divides capital by percentage: 60% stocks, 30% bonds, 10% alternatives. This approach has a hidden flaw: it does not account for the risk contributed by each asset class. Stocks are more volatile than bonds, so the 60% stock allocation contributes far more to portfolio volatility than the 30% bond allocation contributes. The portfolio is implicitly tilted to equity risk, despite the ostensible diversification.

Consider a simple portfolio: $60,000 in stocks with 18% annual [volatility](/wiki/historical-volatility/), and $40,000 in bonds with 5% annual volatility. Total portfolio value is $100,000. The dollar amounts are familiar, but the risk is lopsided. The stocks contribute far more to the portfolio's standard deviation, so the portfolio is effectively a 75-80% equity bet, not 60-40. Market moves are dominated by stock behavior.

Risk parity solves this by inverting the logic: instead of allocating capital first and accepting whatever risk that produces, it allocates capital so that each asset class contributes the same amount of risk. If stocks are three times more volatile than bonds, the portfolio holds one-third the dollar amount of stocks relative to bonds. The capital split becomes unequal, but the risk split becomes equal.

## Calculating the risk parity allocation

The math is straightforward algebra. Suppose the portfolio targets equal risk contribution from stocks and bonds, with no correlation between them (a simplification, but illustrative).

Let $w_s$ = weight in stocks, $w_b$ = weight in bonds. Risk contribution is weight times volatility:
- Risk from stocks = $w_s \times \sigma_s = w_s \times 0.18$
- Risk from bonds = $w_b \times \sigma_b = w_b \times 0.05$

Set these equal: $w_s \times 0.18 = w_b \times 0.05$. Rearranging: $w_s = (0.05 / 0.18) \times w_b = 0.278 \times w_b$.

If the portfolio is fully invested and has no leverage (weights sum to 1): $w_s + w_b = 1$, so $0.278 w_b + w_b = 1$, yielding $w_b = 0.783$ and $w_s = 0.217$. The portfolio is 21.7% stocks and 78.3% bonds — far skewed toward bonds in dollar terms, but balanced in risk.

In practice, such a portfolio earns a lower return because bonds yield less than stocks. To improve returns while maintaining equal risk contribution, **leverage** is introduced: the portfolio borrows at a low rate and invests in both stocks and bonds in the risk-parity ratio, amplifying the returns of each. Leverage of 1.5x to 2x is common, making the portfolio economically equivalent to a leveraged, risk-balanced portfolio of multiple asset classes.

## Multi-asset risk parity

The concept extends to four or more asset classes. A portfolio might hold stocks, bonds, commodities (which have intermediate volatility), and real estate or alternatives. Each is sized so its risk contribution is equal.

Commodities introduce complexity because they have low [correlation](/wiki/correlation-coefficient/) with stocks and bonds, especially during supply shocks or inflationary periods. A commodity allocation that contributes equal risk to a stock allocation can amplify the portfolio's resilience to inflation, where stocks and bonds both underperform. This made risk parity popular during the 2010s, when central banks held [interest rates](/wiki/central-bank-interest-rates/) near zero and inflation seemed dormant.

**Cross-asset correlation** matters enormously. During the 2008 financial crisis, correlations between stocks, bonds, and commodities spiked toward 1.0, and most "diversification" evaporated. A risk-parity portfolio that was balanced ex-ante became concentrated in equity risk ex-post, because all assets fell together.

## Leverage: the unavoidable consequence

Risk parity mandates leverage because high-volatility assets (stocks) require capital allocation inversely proportional to volatility, while low-volatility assets (bonds) require larger allocations. To reach a target portfolio risk (say, 10% annual volatility) without starving the portfolio of equity return, leverage is introduced.

Instead of 21.7% stocks and 78.3% bonds with no leverage, the portfolio borrows and invests in, say, 33% stocks and 120% bonds (net long 153% of assets, financed by borrowing 53% at the risk-free rate). The portfolio's risk is still balanced, but total capital deployed is higher.

Leverage introduces costs:
- **Borrowing costs**: The interest paid on leverage reduces net returns, especially when risk-free rates are high.
- **Margin requirements and collateral haircuts**: Some assets carry higher collateral requirements, raising the effective cost of leverage.
- **Tail risk**: In extreme markets, leverage amplifies losses. A 20% crash in a leveraged portfolio becomes a 30-40% loss.

These costs and risks are why risk parity strategies typically charge higher fees than passive index funds: the complexity of managing multi-asset leverage is non-trivial, and the drawdowns can be severe.

## When risk parity thrives and when it falters

Risk parity performed well in the 2010s, when inflation was contained, [interest rate](/wiki/interest-rate/) volatility was moderate, and asset correlations were low. In an environment where stocks and bonds move independently, a risk-balanced portfolio captures equity upside while dampening downside through bond hedges. [Commodity](/wiki/commodity-currency-pairs/) allocations added value during commodity super-cycles.

Risk parity faltered after 2021, when inflation spiked and the Federal Reserve raised [interest rates](/wiki/federal-funds-rate/) aggressively. Both stocks and bonds fell simultaneously — stocks because higher discount rates reduced equity valuations, and bonds because rising yields drove down bond prices. The negative correlation that risk parity relied on evaporated. A 50% leverage multiple made losses catastrophic. Funds marketing risk parity suffered significant drawdowns.

The strategy is most effective in **rising-rate or [stagflation](/wiki/stagflation/) environments** where equity, bond, and commodity returns are uncorrelated and assets move on their own fundamentals. It is most dangerous in synchronized macro shocks (financial crises, pandemics, geopolitical events) where everything sells off at once.

## Risk parity funds and variants

Several hedge funds and asset managers run risk parity strategies, including Bridgewater Associates (through its All Weather Fund, a related concept) and managed futures funds that use risk-parity weighting. The strategy is also available through risk-parity ETFs, though these typically use more modest leverage (1.2-1.5x) to reduce tail risk.

Variants include **equal volatility weighting** (a lighter version that rebalances to equalize volatility without leverage) and **equal-contribution risk parity**, which also accounts for [correlation](/wiki/correlation-coefficient/) between assets. The basic principle remains: allocate capital inversely to volatility to balance risk.

<div class="wiki-seealso">

### Closely related
- <a href="/wiki/asset-allocation/">/wiki/asset-allocation/</a> — Core portfolio structure and diversification
- <a href="/wiki/diversification/">/wiki/diversification/">/wiki/diversification/</a> — Spreading risk across uncorrelated assets
- <a href="/wiki/correlation-coefficient/">/wiki/correlation-coefficient/</a> — Measuring co-movement between assets
- <a href="/wiki/leveraged-etf/">/wiki/leveraged-etf/</a> — Amplified equity and commodity exposure

### Wider context
- <a href="/wiki/historical-volatility/">/wiki/historical-volatility/</a> — Measuring asset price swings
- <a href="/wiki/commodity-etf/">/wiki/commodity-etf/</a> — Access to commodity exposure
- <a href="/wiki/interest-rate-risk/">/wiki/interest-rate-risk/</a> — Bond sensitivity to rate changes
- <a href="/wiki/systematic-risk/">/wiki/systematic-risk/</a> — Market-wide risk sources
- <a href="/wiki/rebalancing-discipline/">/wiki/rebalancing-discipline/</a> — Maintaining target allocations over time

</div>