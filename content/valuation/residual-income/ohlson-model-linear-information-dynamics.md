---
title: "Ohlson Model Linear Information Dynamics Explained"
description: "How the Ohlson model uses autoregressive processes to forecast abnormal earnings and hidden information over time."
keywords:
  - ohlson model linear information dynamics
  - abnormal earnings forecast
  - autoregressive dynamics
  - edwards-bell-ohlson framework
  - residual income valuation
image: /svg/valuation.svg
---

*The **Ohlson model** assumes that abnormal earnings and other financial information evolve over time according to simple autoregressive rules. These dynamics tell us how quickly abnormal profit decays back to zero, and how long-lived the valuation impact of today's good news is—which is crucial for forecasting residual income many years forward.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Ohlson Model Linear Information Dynamics — key facts</div>

<img src="/svg/valuation.svg" alt="An abstract editorial mark for valuation." />

<div class="wiki-infobox-caption">Autoregressive assumptions govern how earnings surprise and other information decay into the future.</div>

|   |   |
|---|---|
| **Core model** | Ohlson (1995) extends residual income valuation by forecasting abnormal earnings via linear autoregressive processes. |
| **Key inputs** | Book value, abnormal earnings, an "other information" variable capturing news not yet in earnings, and three persistence parameters (ω, γ, α). |
| **Linear dynamics** | Abnormal earnings follow AR(1) with mean reversion toward zero; other information follows AR(1) with independent decay. Their interaction drives long-term value. |
| **Valuation impact** | Persistence parameters determine how much of today's surprise flows through to future earnings and thus to intrinsic value. |
| **Practical use** | Forces disciplined forecasting; decay assumptions can be backtested against historical data to set parameter estimates. |

</aside>

## The Ohlson framework at a glance

The Edwards-Bell-Ohlson (EBO) residual income model values equity as:

**Intrinsic Value = Book Value + PV of Future Abnormal Earnings**

Ohlson's 1995 contribution was to specify exactly *how* abnormal earnings evolve, so that forecasting them becomes mechanical rather than ad hoc. Instead of assuming abnormal earnings disappear at year 5 (or using a stable growth rate), Ohlson proposed that abnormal earnings and other information variables follow autoregressive processes governed by a small number of parameters.

## The two-variable system

Ohlson's core model has two information drivers:

1. **Abnormal Earnings (X_t):** Realised earnings in year t, minus the [cost of equity](/cost-of-equity/) times opening book value. This is the true economic surplus earned by the firm.

2. **Other Information (V_t):** A catch-all for value-relevant news not yet reflected in current earnings—e.g., analyst forecasts of future revenue growth, news of a major contract win, or management guidance. It represents market intelligence about long-term competitive advantage.

Both follow linear autoregressive (AR) rules:

**X_{t+1} = ω · X_t + ε_t**

**V_{t+1} = γ · V_t + η_t**

where:
- **ω** (omega) is the persistence of abnormal earnings (0 < ω < 1). If ω = 0, abnormal earnings vanish immediately. If ω is near 1, they decay slowly.
- **γ** (gamma) is the persistence of other information. By assumption, γ is typically lower than ω, meaning surprises fade faster.
- **ε_t** and **η_t** are random shocks (innovations) uncorrelated across time and with each other.

In addition, abnormal earnings are influenced by lagged other information:

**X_{t+1} = ω · X_t + γ · V_t + ε_t**

This coupling means that good news captured in V_t gradually flows into realised abnormal earnings over time. If V_t is high (e.g., the market learns of a durable competitive advantage), that news will feed into X_{t+1}, X_{t+2}, and beyond, enhancing abnormal returns.

## Why these dynamics matter

The parameters ω and γ determine the entire trajectory of future earnings and therefore the present value of the firm.

**High ω (e.g., 0.8):** Abnormal earnings are sticky. A €1 abnormal profit earned this year translates into large earnings surpluses in future years. The firm's competitive advantage decays slowly. Intrinsic value is high.

**Low ω (e.g., 0.3):** Abnormal earnings revert to zero quickly. Competition erodes the advantage. A €1 abnormal profit this year has minimal long-term impact. Intrinsic value is lower.

**Example:** Suppose a software company earns abnormal earnings of €10m today. If ω = 0.7:
- Year 1: €10m
- Year 2: €10m × 0.7 = €7m
- Year 3: €7m × 0.7 = €4.9m
- Year 4: €4.9m × 0.7 = €3.4m
- ... eventually €0

The present value of this stream, discounted at the [cost of equity](/cost-of-equity/) (say 10%), is the contribution to intrinsic value. A lower ω (faster decay) yields a smaller PV.

## Interaction with other information

Other information V_t creates an additional channel for surprise. Suppose the market learns that the software company has signed a multi-year enterprise deal (boosting V_t). With γ = 0.5, that information decays as:
- Year 1: V_t contributes to year-2 abnormal earnings.
- Year 2: V_t × 0.5 feeds into year-3 earnings.
- Year 3: V_t × 0.5^2 feeds into year-4 earnings.
- And so on.

The coupling parameter (often called α in extensions) determines how much of V_t flows into X_{t+1}. This lets abnormal earnings spike in response to good news, then revert according to its own persistence ω.

In valuation, the price-to-book ratio is sensitive to both ω and γ. If good news (high V_t) is persistent (high γ), then book value is a poor measure of intrinsic value because future earnings will be inflated for years. If ω is high, those abnormal earnings stick around and compound the value lift.

## Empirical application and parameter estimation

Ohlson's framework is elegant, but the analyst must estimate ω and γ from data or theory.

**Historical approach:** Regress abnormal earnings on their lagged values and extract ω. Many studies find ω in the range 0.5–0.8 for mature industrial firms, lower (0.2–0.4) for cyclical industries, and higher (>0.8) for software and high-margin franchises.

**Forecast-based approach:** Use analyst consensus forecasts of earnings growth to infer how quickly the market expects abnormal earnings to fade. This ties ω to forward-looking market opinion.

**Sensitivity analysis:** Rather than commit to a single ω, analysts often compute valuation at three scenarios: ω = 0.5, 0.7, 0.9. This stress-tests the valuation to decay assumptions.

**Stability:** Over long periods, ω should be relatively stable for a given industry. A firm facing disruption may experience a step-down in ω (competitive advantage shortens). Regulators capping returns (e.g., utilities) would see ω artificially low (returns revert to cost of equity quickly).

## Extensions and refinements

Later work extended Ohlson's original model:

- **Multifactor dynamics:** Instead of two variables, add more state drivers (e.g., asset growth, R&D spending, operating margins). Each gets its own persistence parameter.
- **Time-varying parameters:** ω and γ can shift with industry maturity or firm life cycle. Startups have high decay (low ω); mature monopolies have slow decay (high ω).
- **Non-linear dynamics:** Some models allow ω to depend on the level of abnormal earnings, capturing threshold effects (e.g., if abnormal earnings are negative, reversion is faster).
- **Connections to [free cash flow](/free-cash-flow/):** Later researchers linked Ohlson dynamics to unlevered [discounted cash flow](/discounted-cash-flow-valuation/), showing that the two approaches yield equivalent valuations if parameters are calibrated consistently.

## Interpretation and limitations

The linear autoregressive structure is a simplification. In reality:

- **Shocks are not always random.** Competitive actions, regulatory changes, or technological disruption can cause step-level changes in ω.
- **Parameters are estimated with noise.** Small sample sizes or regime shifts make ω estimates unreliable.
- **Coupling assumptions are arbitrary.** The model assumes other information influences abnormal earnings in a particular way; the true relationship may be more complex.
- **Book value can be stale.** If accounting depreciation or write-ups don't match economic value, the book-value anchor (the base for abnormal earnings) is misprised.

Despite these caveats, the Ohlson framework is widely taught and applied because it forces discipline into earnings forecasting. Rather than guessing how long good news lasts, the analyst must make explicit decay assumptions and defend them.

## See also

<div class="wiki-seealso">

### Closely related

- Residual Income — abnormal earnings; the foundation of the Ohlson valuation model
- [Cost of Equity](/cost-of-equity/) — the discount rate used to present-value abnormal earnings
- Book Value — equity's accounting anchor; abnormal earnings are measured relative to cost of equity times opening book value
- Abnormal Earnings — the core valuation driver in the Ohlson framework
- [Dividend Discount Model](/dividend-discount-model/) — a parallel residual-income approach to valuation

### Wider context

- [Discounted Cash Flow Valuation](/discounted-cash-flow-valuation/) — alternative to residual income; equivalent when parameters align
- [Price-to-Book Ratio](/price-to-book-ratio/) — Ohlson dynamics explain P/B multiples
- [Earnings Quality](/earnings-quality/) — persistence of abnormal earnings depends on earnings quality
- [Return on Equity](/return-on-equity/) — abnormal earnings are tied to ROE above cost of equity

</div>
