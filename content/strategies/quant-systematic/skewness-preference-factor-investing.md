---
title: "Skewness Preference and Factor Investing"
description: "How investor preference for positively skewed payoffs drives a systematic skewness factor that suppresses lottery-like stock returns and creates a harvest-able alpha opportunity."
keywords:
  - skewness preference factor investing
  - lottery-like stocks
  - positive skew factor
  - skewness anomaly returns
image: /svg/strategies.svg
---

*Many retail and institutional investors exhibit a preference for **positive skewness**—the lopsided upside of a lottery-like payoff with a small chance of a massive win. This preference suppresses the returns of high-skewness stocks and creates a systematic **skewness factor** that [factor investing](/factor-investing/) strategies can capture by going long low-skewness stocks (ordinary, boring names) and shorting or avoiding high-skewness, lottery-like stocks.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Skewness Preference Factor — key facts</div>

<img src="/svg/strategies.svg" alt="An abstract editorial mark for strategies." />

<div class="wiki-infobox-caption">Investors bid up lottery-like stocks despite poor expected returns; quant strategies profit by shorting the overhyped ones.</div>

|   |   |
|---|---|
| **Core mechanism** | Investors overpay for positive skewness; low-skewness stocks underprice their returns |
| **Typical high-skewness stocks** | Penny stocks, microcaps, turnarounds, biotech pre-approval, emerging-growth names |
| **Exploit method** | Long low-skewness, short or avoid high-skewness; capture the spread |
| **Historical spread** | Approximately 1–3% annualized alpha depending on sample period and implementation |
| **Risk factor** | Concentrated, can underperform in booms driven by retail enthusiasm (e.g., meme stocks) |
| **Market timing** | Spreads widen when retail participation rises or economic uncertainty increases |

</aside>

## The Skewness Appetite

All investors care about risk and return. Most also implicitly care about the *shape* of returns—that is, skewness, the degree to which outcomes are lopsided. Positive skewness means a small probability of an enormous gain coupled with a larger probability of modest loss. Negative skewness is the reverse: frequent small gains punctuated by the rare catastrophic loss.

Rational economic theory suggests skewness should not affect pricing, because rational investors should focus only on expected value and variance. But in reality, many investors—particularly retail traders and insurance companies—show a strong appetite for positive skewness. They will overpay for a chance at a 10-bagger, even if the math says the expected return is negative. This is the same psychology that fuels lotteries: people willingly pay $1 for a ticket with an expected value of $0.50 because they love the dream of winning big.

A **low-skewness stock** offers symmetric, ordinary returns—think a boring large-cap utility or a mature, stable industrial company. Its distribution of future outcomes is bell-shaped and predictable. A **high-skewness stock** is a lottery ticket: a penny stock with a 5% chance of tenfold gains and an 80% chance of slow erosion to bankruptcy. Skewness-loving investors bid up the latter, overpaying them relative to fundamental value.

This preference creates a market anomaly: high-skewness stocks are mispriced, trading at prices that imply returns too low to compensate for their true economic risk. The inverse is true for low-skewness stocks—they are undervalued.

## Measuring and Identifying Skewness

Skewness is usually computed from a stock's past returns. It captures the asymmetry of the distribution: if historical returns cluster above the mean with a rare large downside, the stock has negative skewness. If small negative returns are common but enormous positive days occur now and then, it has positive skewness.

In practice, high-skewness stocks are often characterized by:

- **Small size and low liquidity.** Tiny stocks have sparse trading and greater variance, naturally creating longer tails of outcome.
- **High volatility.** Stocks that swing wildly up and down have fatter tail distributions and higher absolute skewness.
- **Leverage or distressed status.** A highly leveraged company close to default has a lottery-like payoff: equity holders get wiped out or catch a recovery. Distressed turnarounds similarly exhibit positive skewness.
- **Biotech or other binary-outcome businesses.** A drug-trial stock has two states: approval (huge gain) or rejection (loss). This binary structure creates high positive skewness.
- **Low institutional ownership.** Retail-favored names tend to exhibit higher skewness, both because retails traders concentrate on small, volatile stocks and because their preference for skew bids up the price.

Researchers measure a stock's skewness by calculating the third moment of returns over a rolling window (typically 12–60 months) or by backing out implied skewness from option prices ([volatility smile](/volatility-smile/)), which reflects investor expectations of future skew.

## The Skewness Factor and Alpha

Studies by Bender, Sun, Wang, and others have documented a **skewness factor** with reliable, economically meaningful alpha. The mechanism is simple: build a portfolio that is long the lowest-skewness decile and short the highest-skewness decile, rebalancing monthly or quarterly. The short side captures overpayment for lottery-like upside; the long side captures undervaluation of boring, stable returns.

Empirically, this long-low-short-high-skewness strategy has delivered approximately 1–3% annualized excess return (after costs) over multi-decade windows across developed markets. The spread is larger in periods of high retail participation and in smaller-cap universes where idiosyncratic volatility is higher.

The alpha is robust to controlling for other known factors like [size](/market-capitalization/), [value](/value-investing/), [momentum](/momentum-investing/), and volatility. Even after removing the influence of those factors, the skewness spread persists, suggesting investors' preference for skewness is an independent economic force.

## Why the Spread Persists

If high-skewness stocks are systematically overpriced and low-skewness stocks underpriced, why don't arbitrageurs immediately correct the gap?

**Costs and constraints.** Shorting high-skewness stocks is expensive (hard-to-borrow, high short-borrow fees) and risky (sudden momentum reversals can blow out a short position). Going long low-skewness stocks in sufficient size to balance a short book requires capital and capacity. The friction between the two sides prevents instant arbitrage.

**Behavioral persistence.** The preference for skewness is deeply rooted in investor psychology and repeated across billions of retail investors globally. Each market cycle brings new participants who are drawn to lottery-like names, repeatedly rejuvenating the mispricing.

**Institutional constraints.** Many investment funds are mandated to hold only large-cap, liquid names—they cannot effectively short small, illiquid high-skewness stocks. Index-tracking mandates exclude the skewness factor entirely.

**Time-varying risk.** The skewness factor is not smooth. When retail interest surges (e.g., during IPO booms or after a major win in a hype stock), high-skewness names can rally hard, creating a window of loss for shorts. The strategy's volatility (draw-downs can exceed 20%) deters many capital allocators.

## Implementing the Skewness Factor

Quant practitioners harvest skewness in several ways:

**Direct skewness ranking.** Compute historical skewness (third moment of returns) for each stock in the universe, rank, and long the bottom decile while shorting the top decile. Rebalance quarterly or monthly to avoid stale signals.

**Volatility and tail metrics.** Use proxies for lottery-like behavior: stocks with extreme realized or implied [tail risk](/tail-risk/), high [beta](/beta/) combined with low correlation, or very high idiosyncratic volatility relative to systematic risk. These tend to exhibit high skewness.

**Fundamental filters.** Screen for characteristics correlated with high skewness: penny stocks, microcaps, highly leveraged firms, pre-revenue biotech, distressed debt. The combination of small size, high leverage, and low profitability correlates strongly with positive skewness.

**Volatility smile arbitrage.** Use option-implied skewness from [option](/option/) markets. If implied skewness is high (reflected in a pronounced volatility smile, with out-of-the-money calls relatively expensive), that signals the market is pricing in lottery-like payoff; short the underlying stock.

**Cross-sectional momentum with skewness overlay.** Some strategies combine momentum factor with skewness: go long momentum stocks with low skewness and avoid short-side candidates that are also high-skewness (to avoid catching a rally in lottery tickets).

## Risks and Limitations

The skewness factor is real but not riskless:

**Regime shifts.** In meme-stock environments (e.g., 2021 retail boom), high-skewness stocks can outperform explosively, blowing through shorts. The factor inverts. Drawdowns during such regimes can be severe (−20% or more).

**Non-linearity.** The factor works best in the cross-section of hundreds of stocks; single-name decisions can be noise. A concentrated short position in one lottery stock that suddenly rallies is extremely painful.

**Illiquidity and borrow costs.** Shorting high-skewness stocks is expensive and risky due to borrow scarcity. The full spread may not be achievable after borrowing fees and slippage.

**Structural change.** As more capital targets the factor (or if index providers begin offering skewness-based indices), the spread may compress. Factors are not permanent; they depend on persistent investor bias.

## See also

<div class="wiki-seealso">

### Closely related

- [Factor investing](/factor-investing/) — broad category of strategies harvesting systematic return premiums
- [Momentum investing](/momentum-investing/) — harvesting the tendency of winners to keep winning
- [Value investing](/value-investing/) — harvesting undervaluation and mean reversion
- [Volatility smile](/volatility-smile/) — implied skewness from option markets
- [Tail risk](/tail-risk/) — the probability and magnitude of extreme adverse events

### Wider context

- [Quantitative investing](/quantitative-investing/) — systematic, data-driven approach to portfolio construction
- Behavioral finance — how psychology shapes pricing anomalies
- Arbitrage — exploiting price mispricings between related securities
- [Alpha](/alpha/) — risk-adjusted excess return

</div>
