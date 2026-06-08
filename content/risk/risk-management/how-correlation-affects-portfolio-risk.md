---
title: "How Correlation Affects Portfolio Risk"
description: "Correlation determines the diversification benefit of holding multiple assets. Only when correlation is below 1 does variance fall. See the math with examples."
keywords:
  - correlation portfolio risk
  - how correlation affects diversification
  - portfolio variance correlation
  - two-asset portfolio math
  - diversification benefit
---

*Adding a second asset to a portfolio reduces overall variance only if the two assets are not perfectly correlated. A correlation of 1.0 means they move in lockstep; 0.5 or lower means diversification kicks in, cutting risk. Understanding the math reveals why portfolio construction depends entirely on the correlation structure, not just individual volatility.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Correlation and Diversification — the variance formula</div>

<img src="/svg/risk.svg" alt="An abstract editorial mark for risk management." />

<div class="wiki-infobox-caption">Two assets cut variance only if they move differently; perfect correlation provides no benefit.</div>

|   |   |
|---|---|
| **Correlation range** | −1.0 (opposite moves) to +1.0 (identical moves) |
| **Diversification effect** | Begins when correlation < 1.0 |
| **Perfect positive correlation (ρ = 1.0)** | No variance reduction; equivalent to a single asset |
| **Zero correlation (ρ = 0)** | Substantial variance reduction |
| **Negative correlation (ρ < 0)** | Maximum diversification benefit; assets hedge each other |
| **Portfolio variance formula** | σ²_p = w₁²σ₁² + w₂²σ₂² + 2w₁w₂σ₁σ₂ρ |

</aside>

## Why Correlation Matters More Than Volatility Alone

A portfolio manager holding two volatile stocks might assume they're taking on unacceptable risk. But if those stocks move in opposite directions—one rallies when the other falls—the combination can actually be less volatile than either stock alone. Conversely, two mild-mannered stocks that always move together add no diversification benefit, no matter how "calm" each is individually.

This is because **[diversification](/diversification/)** depends not on asset volatility but on correlation—the statistical measure of how two assets move relative to each other. Correlation is the lever that transforms a portfolio from a collection of risky bets into a balanced, risk-reduced position.

A correlation of +1.0 (perfect positive correlation) means the two assets always move together in the same direction and proportion. A correlation of 0 (zero correlation) means their movements are statistically independent. A correlation of −1.0 (perfect negative correlation) means they always move in opposite directions. Most real assets have correlations between 0 and +1.0, which is where the diversification benefit lives.

## The Two-Asset Portfolio Variance Formula

The variance of a two-asset portfolio is given by:

σ²_p = w₁²σ₁² + w₂²σ₂² + 2w₁w₂σ₁σ₂ρ

Where:
- w₁, w₂ = weights of assets 1 and 2 (must sum to 1.0)
- σ₁, σ₂ = standard deviations (volatility) of each asset
- ρ = correlation between the two assets
- σ²_p = portfolio variance

The first two terms (w₁²σ₁² + w₂²σ₂²) are the weighted volatilities of each asset in isolation. The third term (2w₁w₂σ₁σ₂ρ) is the covariance term—the interaction between the two assets. Correlation is embedded in that covariance.

## The Effect of Correlation on Portfolio Variance

Let's work through a concrete example.

**Assets:** Asset A has volatility of 20%, Asset B has volatility of 15%. You allocate 50% to each (w₁ = 0.5, w₂ = 0.5).

**Scenario 1: Perfect Positive Correlation (ρ = 1.0)**

σ²_p = (0.5)² × (0.20)² + (0.5)² × (0.15)² + 2 × 0.5 × 0.5 × 0.20 × 0.15 × 1.0
σ²_p = 0.01 + 0.005625 + 0.015
σ²_p = 0.030625
σ_p = √0.030625 = 17.5%

The portfolio volatility (17.5%) is simply the weighted average of the two asset volatilities (50% × 20% + 50% × 15% = 17.5%). Adding the second asset contributes nothing to risk reduction.

**Scenario 2: Zero Correlation (ρ = 0)**

σ²_p = (0.5)² × (0.20)² + (0.5)² × (0.15)² + 2 × 0.5 × 0.5 × 0.20 × 0.15 × 0
σ²_p = 0.01 + 0.005625 + 0
σ²_p = 0.015625
σ_p = √0.015625 = 12.5%

The portfolio volatility drops to 12.5%—well below the 17.5% weighted average. The diversification benefit is real: two independent assets create a lower-variance portfolio than the individual average.

**Scenario 3: Moderate Positive Correlation (ρ = 0.5)**

σ²_p = (0.5)² × (0.20)² + (0.5)² × (0.15)² + 2 × 0.5 × 0.5 × 0.20 × 0.15 × 0.5
σ²_p = 0.01 + 0.005625 + 0.0075
σ²_p = 0.023125
σ_p = √0.023125 = 15.2%

The portfolio volatility is 15.2%—between the zero-correlation case (12.5%) and the perfect-correlation case (17.5%). Diversification works, but not as powerfully as with lower correlation.

## The Covariance Term as the Lever

The key insight is in the covariance term (2w₁w₂σ₁σ₂ρ). As correlation *decreases*, this term shrinks. At ρ = 1.0, the term is at its maximum. At ρ = 0, the term vanishes entirely. At ρ < 0 (negative correlation), the term becomes negative, actually *reducing* portfolio variance below the simple weighted average.

This is why [alternative assets](/alternative-trading-system/) such as [commodities](/crude-oil/), [bonds](/bond/), or [real estate](/commercial-real-estate/) are often included in equity portfolios: they have lower (or negative) correlation with equities. A portfolio of 100% stocks is more volatile than a portfolio of 70% stocks and 30% bonds, even though bonds are individually "safer"—because stocks and bonds correlate below 1.0.

## The Catch: Correlation Isn't Constant

Correlation is estimated from historical data, but it's not stationary. In normal markets, equities and bonds might have a correlation near 0.2, providing genuine diversification. During financial crises—exactly when diversification is most needed—correlations spike toward 1.0. All assets crash together, and the diversification benefit evaporates.

This is why portfolio managers distinguish between correlation in normal times and correlation in [tail risk](/tail-risk/) or [systemic risk](/systemic-risk/) scenarios. A stress test that assumes correlation remains at 0.2 during a market crash is dangerously optimistic. Historical stress tests or [value-at-risk](/value-at-risk/) models that account for regime changes in correlation are more reliable.

## Optimal Diversification and the Frontier

The [capital asset pricing model](/capital-asset-pricing-model/) and [mean-variance optimization](/mean-variance-optimization/) rest on correlation. An efficient portfolio—one that minimizes variance for a given return target—always exploits low-correlation pairs. If you're targeting an 8% return and can achieve it with two low-correlation assets, your variance will be lower than with two high-correlation assets.

Conversely, if all assets in a market are highly correlated (as sometimes occurs during a [liquidity crisis](/liquidity-risk/)), the efficient frontier shrinks, and diversification provides little comfort. This is a key reason why buying an [index fund](/index-fund/) works well in normal times but leaves you exposed to systematic [market risk](/market-risk/) in crashes.

## Practical Rules for Using Correlation

1. **Correlation below 0.7** is generally considered "low" and provides meaningful diversification. 
2. **Correlation above 0.8** is "high" and provides little diversification benefit.
3. **Negative correlation** (common between stocks and government bonds, or gold and equities) is the holy grail; it cuts portfolio variance the most.
4. **Sector correlations within equities** tend to be 0.5–0.8, so [sector diversification](/sector-rotation/) helps but isn't a silver bullet.
5. **In crises**, assume correlations spike to 0.9 or higher. Plan for that scenario when stress testing.

## The Takeaway

Adding a second asset to a portfolio always looks beneficial in isolation: more diversification, more exposure, more options. But mathematically, it reduces portfolio variance *only if correlation is below 1.0*. With perfect correlation, you're not adding diversification—you're just doubling down. Understanding the math lets you see through marketing ("own 500 stocks for diversification") and focus on what matters: the correlation structure and whether it holds in the conditions when you need it most.

## See also

<div class="wiki-seealso">

### Closely related

- [Diversification](/diversification/) — the principle of combining low-correlation assets to reduce risk
- [Capital Asset Pricing Model](/capital-asset-pricing-model/) — the framework for understanding systematic and idiosyncratic risk
- Efficient Frontier — the set of optimal portfolios that minimize variance for each return target
- [Beta](/beta/) — the measure of an asset's correlation with the overall market
- [Value-at-Risk](/value-at-risk/) — a quantified tail risk metric that accounts for correlation changes

### Wider context

- [Market Risk](/market-risk/) — the unavoidable risk from systematic correlation across all assets
- [Tail Risk](/tail-risk/) — the correlation spike in extreme scenarios where diversification fails
- [Asset Allocation](/asset-allocation/) — the strategic distribution of capital across asset classes
- [Volatility](/historical-volatility/) — the building block of variance alongside correlation

</div>
