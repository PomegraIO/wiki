---
title: "Model Risk in Finance"
description: "The danger of relying on flawed or misapplied quantitative models for pricing and risk measurement, and how firms manage it."
keywords:
  - model risk
  - model risk finance
  - model validation
  - pricing model
  - risk model
image: "/svg/risk.svg"
---

*Financial institutions depend on quantitative models to price securities, estimate [value-at-risk](/value-at-risk/), and make trading decisions worth billions. But every model is a simplification of reality—incomplete, based on assumptions that may break, calibrated to historical data that may not repeat. **Model risk** is the danger that a flawed or misapplied model produces incorrect prices, misstated losses, or failed hedges, often in the precise moment when it matters most.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Model Risk — key facts</div>

<img src="/svg/risk.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Arises from simplification, misuse, and assumption failure; invisible until it blows up.</div>

|   |   |
|---|---|
| **Root causes** | Wrong assumptions, poor calibration, misuse |
| **Common culprits** | [Black-Scholes](/black-scholes-model/), correlation models, [VaR](/value-at-risk/) |
| **Detection** | Backtesting, stress testing, expert review |
| **Regulation** | SEC, Federal Reserve, banking agencies require governance |
| **Famous failures** | Long-Term Capital Management, VaR at Bear Stearns |
| **Mitigation** | Independent validation, sensitivity analysis, limits |

</aside>

## Why models fail

The [Black-Scholes model](/black-scholes-model/)—the standard for pricing equity options—assumes log-normal stock price movements, constant volatility, no transaction costs, and perfect liquidity. Real markets violate every assumption. Stock returns have fat tails (more extreme moves than a log-normal distribution predicts). Volatility is dynamic, spiking in crises. Costs matter. Liquidity evaporates.

For decades, this didn't matter much; Black-Scholes worked well enough in normal times. But in August 1998, when Long-Term Capital Management's positions blew up, the gap between model and reality became lethal. LTCM had piled leverage on top of models that assumed convergence and normal correlations. When Russian bonds defaulted and liquidity seized, the correlations they'd modeled at 0.7 jumped to 1.0 overnight. The firm had misjudged not just the numbers but the regime itself.

Model risk takes several forms:

**Conceptual failure** — The model's structure is wrong. Assuming constant volatility in an environment where jumps are frequent systematically misprice options.

**Calibration failure** — The model's inputs (parameters) are wrong. You estimate historical volatility at 15% based on the past three years, but conditions are changing; next year's volatility is 25%.

**Input failure** — You use the right model but feed it bad data. A credit default swap model assumes recovery rates of 40%, but in a severe default, recovery is 15%.

**Misuse** — The model is used outside its intended domain. A credit model built for corporate bonds is applied to mortgage-backed securities without adjustment.

**Governance failure** — No one checks if the model still works. A pricing model hasn't been revalidated since 2015; it's based on stale assumptions.

## Regime changes and tail risk

Models trained on normal market data often fail catastrophically during tail events. The [volatility smile](/volatility-smile/)—the observation that out-of-the-money options are pricier relative to Black-Scholes than at-the-money options—suggests model inadequacy. Yet many traders still use Black-Scholes as a baseline, accepting the smile as a surface adjustment. During a crash, the smile becomes a yawn, and the model's true weakness surfaces.

Correlation is particularly treacherous. Two assets might be uncorrelated in normal times but exhibit near-perfect correlation during liquidity crises or sector shocks. A model that assumes 0.3 correlation between high-yield spreads and equity volatility can catastrophically underestimate [portfolio risk](/concentration-risk-portfolio/) when the relationship flips to 0.8.

## The VaR illusion

[Value-at-risk](/value-at-risk/) models estimate the maximum loss under normal conditions—say, "95% confidence, this portfolio will not lose more than $5 million in a day." This is intuitive and regulators adore it. But VaR models have a fatal flaw: they often assume normally distributed returns, which underestimate tail risk. A portfolio marked as "95% safe" can blow up on days that the model said had less than 5% probability.

The 2008 crisis revealed that banks' VaR models were systematically too optimistic. Positions deemed low-risk under VaR experienced losses five or ten times the model's estimate. The model wasn't just calibrated wrong; the underlying distribution assumption was broken.

## Validation and limits

Prudent institutions run three layers of defense:

**Backtesting** — For past periods, compare model predictions to actual outcomes. Did prices the model generated at mid-year match realized prices? If the model is right, it should explain 80%+ of actual moves. If backtests fail, the model is unfit.

**Stress testing** — Simulate extreme scenarios (a 10% stock market drop, a 200 basis point rate shock, a sector-wide default). Run the model on these scenarios and ask: do the outputs make sense? Can we hedge this risk?

**Sensitivity analysis** — Tweak the assumptions. If volatility is 20% instead of 15%, does the price change 5% or 500%? Does the model behave reasonably as inputs vary?

Large banks employ independent model-risk teams, separate from trading, whose job is to critique and reject bad models before traders use them to deploy billions. The [Federal Reserve](/federal-reserve/) and SEC require governance frameworks: documented assumptions, validation evidence, sign-off from risk officers, and regular recalibration.

## Model risk in credit and correlation

Credit models assume [default probability](/default-rate/) based on historical data and current spreads. But when a firm's peers are failing, the model's historical probabilities become obsolete. The model assigns 2% default risk to a bank; the market suddenly assigns 15% as sentiment shifts and [counterparty risk](/counterparty-risk/) spikes. The model, lagging reality, is dangerously wrong.

Correlation models for [asset allocation](/asset-allocation/) are notoriously fragile. A model calibrated to years of data where bonds and stocks are negatively correlated can break spectacularly when both fall simultaneously (as in 1994, 2008, and 2022). The model's recommendations for portfolio balance turn out to be built on a mirage.

## When models are right—and when humility helps

Models do work, most of the time, for most problems. Black-Scholes still prices vanilla options decently. [Value-at-risk](/value-at-risk/) captures day-to-day risk reasonably. Correlation models predict average behavior. The issue is that traders, risk managers, and boards sometimes forget that models are guides, not oracles.

A healthy institution treats models as tools, not truth. It updates them regularly. It limits their use to the domains and market conditions they were built for. It stress-tests voraciously. It hires smart people to poke holes. And it maintains a healthy skepticism: the model says this trade is safe, but is the model's assumption valid in the current environment?

When major financial crises hit, a common culprit is a firm that outsourced thinking to a model. The 2008 crisis, the VaR failures in 2020, the volatility blowups in 2018—many were model-risk events: good models used outside their scope, bad assumptions embedded and forgotten, or senior management that trusted math over judgment.

## See also

<div class="wiki-seealso">

### Closely related

- [Black-Scholes model](/black-scholes-model/) — the dominant options pricing model; elegant but flawed
- [Value-at-risk](/value-at-risk/) — ubiquitous risk measure with known pitfalls
- [Stress testing](/stress-testing/) — how firms validate models against extreme scenarios
- [Volatility smile](/volatility-smile/) — empirical evidence of Black-Scholes limitations
- [Tail risk](/tail-risk/) — the worst outcomes that models often underestimate

### Wider context

- Risk management — the broader governance of model and operational risk
- [Basis risk](/basis-risk-hedging/) — another form of hedge failure rooted in model assumptions
- [Counterparty risk](/counterparty-risk/) — dynamics that models calibrated in calm times fail to predict
- [Liquidity risk](/liquidity-risk/) — models assume it away, but it matters in crises
- [Correlation](/beta/) — the relationship between assets that models attempt to capture

</div>
