---
title: "Risk Attribution in a Long-Short Portfolio"
description: "Risk attribution in long-short portfolios decomposes total risk into contributions from gross exposure, net exposure, and factor loadings to understand where systemic risk comes from."
keywords:
  - risk attribution
  - long-short portfolio
  - gross exposure
  - net exposure
  - factor loading
image: "/svg/risk.svg"
---

*Risk attribution in a long-short portfolio breaks down the sources of total portfolio [risk](/market-risk/) by analyzing how gross exposure (the sum of all long and short positions), net exposure (long positions minus short positions), and factor loadings combine to drive volatility and drawdowns. Unlike a traditional long-only portfolio, where risk attribution is straightforward, long-short books face the complexity that large offsetting positions can mask concentrated bets that still drive real losses.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Risk Attribution in Long-Short Portfolios — Key facts</div>

<img src="/svg/risk.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">High gross exposure with low net exposure looks safe until factor correlations spike.</div>

|   |   |
|---|---|
| **Gross exposure** | Sum of absolute values of all positions (always >= net exposure) |
| **Net exposure** | Long positions minus short positions (can be negative if short-heavy) |
| **Leverage** | Gross exposure divided by capital; market-neutral funds often run 2–4x leverage |
| **Beta-adjusted risk** | Contribution of [beta](/beta/) to total portfolio [volatility](/historical-volatility/) |
| **Factor contribution** | Risk from tilts in value, growth, momentum, [quality](/value-investing/), or other factors |
| **Correlation risk** | Danger that hedges break down when factor correlations change |

</aside>

## Why Standard Attribution Breaks Down

A traditional long-only fund's risk attribution is simple: if you hold $100 million in IBM with a beta of 1.2, that position contributes 1.2 units of systematic risk per dollar deployed. Sum across all holdings and you have total systematic risk.

A long-short fund complicates this. Suppose it is long $150 million in technology stocks (beta 1.4) and short $100 million in utilities (beta 0.7). The net exposure is $50 million long (beta-weighted ~1.15). But the gross exposure is $250 million. The fund is running $250 million / $50 million = 5x leverage—meaning it controls a position five times the size of its capital base.

A naive risk calculation might conclude: "Net exposure is small, so risk is small." But that ignores the reality that if both the long and short legs fall in tandem (due to a market-wide shock or a realization that tech stocks and utility stocks move together more than expected), the hedges break and the fund faces catastrophic losses despite low net exposure.

This is where risk attribution for long-short portfolios must decompose risk into components: gross risk, net risk, and factor risk.

## Gross Exposure and Beta

**Gross exposure** is the sum of absolute values of all positions. For the tech-long-utilities-short fund above, it is $150M + $100M = $250M. This tells you the total capital at risk if all positions move in the same direction.

A long-short fund's total portfolio volatility depends heavily on gross exposure. If a fund runs 1x gross exposure (dollar-long equals dollar-short, so net is zero), it cannot lose money in a broad market crash because the long and short positions offset. If it runs 5x gross exposure, a 10% move in the common factor affecting both legs can produce losses of 5% or more relative to capital.

**Beta-adjusted gross exposure** refines this by weighting each position by its sensitivity to the market. A $100M position with beta 1.5 contributes $150M of beta-adjusted gross exposure. The fund's total market risk (assuming minimal correlations elsewhere) is driven by the sum of beta-adjusted absolute values across all holdings.

## Net Exposure and Directional Risk

**Net exposure** is the portfolio's directional tilt: sum of long positions minus sum of short positions (in dollar terms or beta-adjusted). A portfolio with $150M long and $100M short has $50M net exposure. A portfolio with $100M long and $150M short has -$50M net exposure (a net short bet).

Net exposure is the source of **market-directional risk**. If the overall market rises 10%, a portfolio with 2x net leverage (net $100M long in a $50M fund) loses 20% because it amplifies market moves. Conversely, a market-neutral portfolio (net exposure near zero) is hedged against broad market moves.

However, a low net exposure does not mean low risk. A portfolio with $200M long in biotech stocks (high growth, high volatility) and $200M short in large-cap industrials (low growth, low volatility) has zero net exposure but very high gross exposure and significant **factor risk**: it is long growth and short value. If growth stocks underperform, the fund loses on both the long and short sides simultaneously.

## Factor Risk and Correlation Breakdowns

This is the critical insight: long-short portfolios are often designed to isolate a specific factor or theme while hedging out others. A long-short equity fund might run:

- Long: $150M in undervalued stocks (value factor)
- Short: $100M in overvalued stocks (growth factor)

Net exposure is positive, but the core bet is on **value outperforming growth**. The risk attribution must show that the portfolio's volatility comes primarily from the value-growth spread, not from broad market moves.

During normal periods, this decomposition works. Value and growth have a correlation around 0.8–0.9, and the spread has low volatility (2–4% annualized). But in crisis periods, correlations can jump toward 1.0 as investors sell all risky assets indiscriminately. A value-long-growth-short bet that seemed low-risk suddenly becomes correlated and volatile. This is **correlation risk**, and it is often the largest source of long-short portfolio losses.

Similarly, a [momentum](/momentum-investing/)-focused long-short portfolio might be long 12-month winners and short 12-month losers. This isolates the momentum factor. But when sentiment reverses (often during liquidity crises), momentum crashes across the board, and the long and short legs move together, eliminating the hedge.

## Calculating Factor Risk Contribution

A formal approach decomposes portfolio returns and risk into factor contributions:

**Portfolio Return = (Net Exposure × Market Beta) + Sum of (Factor Tilt × Factor Return)**

For risk:

**Portfolio Variance = (Net Exposure × Market Beta)² × Market Variance + Sum of (Factor Tilt)² × Factor Variance + 2 × Cross-Terms (Covariances)**

The fund calculates the covariance between each factor and every other factor (and the market). A portfolio long value and short momentum has positive tilts on two factors with typically negative covariance—they tend to move in opposite directions. That negative covariance reduces total portfolio variance.

But if covariances shift—for example, in a 2020-style crisis where all growth-adjacent factors (momentum, quality, low volatility) rallied together—the diversification benefit evaporates. Risk attribution must account for these scenarios via stress testing or historical scenario analysis.

## Applying Risk Attribution to Portfolio Management

Portfolio managers use risk attribution to:

1. **Identify concentrated bets**: If the portfolio's volatility is driven 80% by a single factor, the manager is running a highly concentrated strategy. That may be intentional, but it must be monitored.

2. **Uncover hidden leverage**: A portfolio that appears low-risk (low net exposure) but has very high gross exposure is hiding leverage. In a stress event, that leverage can amplify losses.

3. **Validate hedges**: If a portfolio is long a specific sector and short another to hedge, risk attribution confirms whether the short actually reduces sector volatility or whether it is being swamped by other factors.

4. **Stress-test covariance assumptions**: By calculating how portfolio risk changes if correlations spike or factor volatilities increase, the manager can model "what if" scenarios and size positions accordingly.

## Measuring and Monitoring

Risk attribution is typically calculated using factor models—often a multi-factor regression or a well-known factor suite like the Fama-French five factors or a vendor model like MSCI Barra. The process:

1. Decompose each holding's returns into factor returns (market, value, growth, size, momentum, etc.).
2. Sum the factor exposures across all holdings to derive net portfolio factor tilts.
3. Project portfolio volatility by multiplying each factor tilt by the factor's historical volatility and covariance.
4. Compare the projection to actual portfolio volatility; the difference reveals model error or non-linear risks.

A fund might find that its risk model predicts 8% annualized volatility but actual volatility is 12%. That discrepancy often signals that the fund's true leverage is higher than the model assumes, or that factor correlations are higher than historical averages, or that there are non-linear (tail) risks the model misses.

## See also

<div class="wiki-seealso">

### Closely related

- [Beta](/beta/) — Sensitivity to market moves; core input to risk attribution
- [Factor investing](/factor-investing/) — The framework underlying most long-short risk decomposition
- [Hedge fund](/hedge-fund/) — The fund type that typically runs long-short strategies and uses risk attribution
- [Correlation](/currency-risk/) — The covariance structure that determines diversification benefits
- [Volatility smile](/volatility-smile/) — Non-linear risk that factor models often miss

### Wider context

- [Value at risk](/value-at-risk/) — A summary risk metric that risk attribution feeds into
- [Stress testing](/stress-testing/) — Scenario analysis that tests attribution assumptions
- [Return on invested capital](/return-on-invested-capital/) — Risk-adjusted return metric
- [Sharpe ratio](/sharpe-ratio/) — Risk-adjusted performance measure that depends on accurate risk attribution
- [Portfolio diversification](/diversification/) — The strategy that risk attribution aims to optimize

</div>
