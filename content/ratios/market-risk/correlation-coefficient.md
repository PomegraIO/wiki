---
title: "Correlation Coefficient"
description: "Statistical measure of how two assets move together, ranging from -1 (perfect inverse) to +1 (perfect together)."
keywords:
  - correlation
  - asset correlation
  - diversification
  - covariance
  - pearson coefficient
  - portfolio risk
---

*The **correlation coefficient** measures the degree to which two assets move together. A correlation of +1 means they move in lockstep; −1 means they move in opposite directions; 0 means no linear relationship. Investors use correlation to understand [diversification](/diversification/) benefits and to hedge [systematic risk](/systematic-risk/).*

<aside class="wiki-infobox">

| Attribute | Value |
|-----------|-------|
| **Symbol** | ρ (rho) or r |
| **Range** | −1.0 to +1.0 |
| **Perfect positive** | +1.0 (moves up together) |
| **Perfect negative** | −1.0 (moves opposite) |
| **No relationship** | 0.0 (independent) |
| **Common stock-stock** | 0.5–0.8 (same market) |
| **Stock-bond** | −0.1 to +0.3 (often negative) |
| **Formula** | Cov(A, B) / (σ_A × σ_B) |

</aside>

## Interpreting the coefficient

The correlation coefficient is a normalized measure of covariance. If you have two assets A and B with daily returns over 252 trading days:

- **Correlation near +1**: The assets tend to move in the same direction. If A rises 2%, B typically rises 1.5%. Buying both offers little diversification benefit.
- **Correlation near 0**: The assets move independently. A might be up while B is down. This is valuable for [diversification](/diversification/).
- **Correlation near −1**: The assets tend to move opposite. If A is down 3%, B might be up 2%. This is a classic hedge.

Most stocks in the same market have correlations between 0.5 and 0.8: they all respond to [business cycle](/business-cycle/) changes, interest rates, and sentiment, so they cannot be independent, but they also have firm-specific risks that cause divergence.

## Diversification and correlation

The main use of correlation is in portfolio construction. If an investor holds two assets with correlation 0, the [standard deviation](/standard-lot/) of their portfolio is lower than either asset alone—pure diversification. If correlation is +1, there is no diversification benefit; the portfolio's volatility is a weighted average of the two.

The formula for a two-asset portfolio's variance is:

**σ_p² = w₁²σ₁² + w₂²σ₂² + 2w₁w₂ρ₁₂σ₁σ₂**

The last term is the correlation effect. When ρ₁₂ is negative, that term becomes negative, lowering portfolio variance. When ρ₁₂ is zero, that term drops out, and diversification comes purely from the first two terms (the assets' individual variances).

This is why investors buy [stocks and bonds](/bond-equity-allocation/): historically, their correlation has been near zero or slightly negative. In normal times, bonds gain value when stocks fall (flight to safety), so a 60/40 equity-bond portfolio is less volatile than 100% stocks.

## Time-varying and regime-dependent correlation

Correlation is not constant. It changes over time and, critically, changes *when you need it most*. During financial crises, correlations between risky assets tend to spike toward +1—[stock market crashes](/black-monday-1987/), [credit spreads](/credit-spread/) widen, and everything correlated with [risk appetite](/risk-on-risk-off/) falls together. The [correlation risk](/correlation-risk/) is that a hedge (e.g., short selling) assumed to have ρ = −0.5 suddenly has ρ = +0.7 when markets blow up.

The 2008 financial crisis demonstrated this starkly. Investors who thought they were diversified with stocks, bonds, and commodities watched all three fall together (or bonds and stocks decouple differently than expected). Correlation breakdowns are a known pitfall in [tail risk](/tail-risk/) management.

## Correlations in different markets

- **Equities in the same country**: 0.6–0.75 (all respond to macro, but firms have idiosyncratic risk).
- **Equities across developed markets**: 0.5–0.7 (high because global capital flows, but some home-country bias).
- **U.S. stocks and bonds**: 0.0 to −0.3 (often negative; bonds rally when stocks sell off).
- **Stocks and commodities**: 0.1–0.4 (weak, commodity prices are driven partly by supply and partly by inflation risk).
- **Stocks and [volatility index (VIX)](/vix-volume-indicator/)**: −0.5 to −0.8 (inverse; when stocks drop, volatility spikes).
- **Gold and stocks**: −0.2 to +0.1 (gold often rallies when stocks fall, but relationship is weak).

Currency pairs have low correlations to equities but can move together in [risk-off](/risk-on-risk-off/) regimes (safe-haven currencies like the Swiss franc rally as stocks fall).

## Estimating correlation: rolling windows and models

Correlation is usually estimated from historical returns. A common method is to use the last 252 trading days (one year) of daily returns and calculate the Pearson correlation coefficient. But the choice of lookback window matters.

- **Short window** (1–3 months): Noisy, but responsive to current market regime.
- **Long window** (2–5 years): Smoother, but may embed regime shifts (e.g., a crisis followed by recovery).

Some models use exponential weighting to give more recent returns higher weight, reasoning that recent correlation is more predictive. Others use multivariate GARCH models to estimate time-varying correlations and covariance matrices.

For options and risk models, implied correlations (backed out of [basket options](/basket-option/) or [variance swaps](/variance-swap/)) are sometimes used, as they reflect market expectations rather than backward-looking data.

## Correlation and hedging

A trader holding a long equity position might sell index [puts](/put-option/) to finance the position. The value of that hedge depends on the correlation between the held stocks and the index. If the stocks have ρ = 0.9 with the index, the put sell is an effective hedge. If ρ = 0.3, the put is a poor hedge; the stocks might fall while the index rises.

Similarly, a fixed-income manager holding corporate bonds might short [Treasuries](/treasury-bond/) as a hedge against [interest rate risk](/interest-rate-risk/). The hedge's effectiveness relies on the [basis](/basis/)—the spread between corporate and Treasury yields—and the correlation of their durations.

## Limitations of correlation

Correlation assumes a linear relationship. Two assets might have zero Pearson correlation but still be dependent in tail events (captured by measures like [copula](/copula-dependence-strategy/) or [tail dependence](/tail-dependence/)). 

Correlation is also symmetrical: if A and B have ρ = 0.6, B and A have ρ = 0.6. It does not capture direction or causation. A high correlation could reflect common factors (both stocks respond to GDP) or coincidence.

---

<div class="wiki-seealso">

### Closely related

- [Diversification](/diversification/) — Reducing risk via uncorrelated assets
- Covariance — Unnormalized correlation measure
- [Standard Deviation](/historical-volatility/) — Asset volatility measure
- [Portfolio Risk](/idiosyncratic-risk/) — Systematic and unsystematic components
- [Beta](/beta/) — Correlation-like measure with market index

### Wider context

- [Tail Dependence](/tail-dependence/) — Correlation breakdown in crises
- [Correlation Risk](/correlation-risk/) — Risk that correlation changes unfavorably
- [Risk-on Risk-off](/risk-on-risk-off/) — Regime shifts affecting correlations
- [Variance Swap](/variance-swap/) — Trades correlation and volatility
- [Copula](/copula-dependence-strategy/) — Dependence structure beyond correlation

</div>
