---
title: "Term Structure of Volatility and Risk Horizons"
description: "How volatility varies across different time horizons and why forecasting multi-period risk requires understanding term structure of volatility, not just daily fluctuations."
keywords:
  - term structure of volatility
  - risk horizons
  - volatility scaling
  - volatility term premium
  - realized volatility measurement
image: /svg/risk.svg
---

*The **term structure of volatility** describes how price fluctuations differ depending on the time window over which you measure them—a day, a month, a year. Volatility does not scale uniformly as time extends, and treating a one-month forecast as a simple multiple of daily volatility produces systematically wrong risk estimates.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Term Structure of Volatility — key facts</div>

<img src="/svg/risk.svg" alt="An abstract editorial mark for risk and measurement." />

<div class="wiki-infobox-caption">Multi-period volatility forecasts depend critically on the time horizon, not just recent daily swings.</div>

|   |   |
|---|---|
| **Core concept** | Volatility varies by measurement horizon; longer periods do not scale as simple multiples of short-term volatility |
| **Why it matters** | Risk forecasts and [hedge-fund](/hedge-fund/) margin calls depend on the time horizon chosen |
| **Key pattern** | Volatility term premiums; volatility clustering and mean reversion interact across time scales |
| **Common error** | Annualizing daily volatility via the √T rule ignores regime shifts and mean reversion |
| **Investment use** | Option pricing, [value-at-risk](/value-at-risk/) horizon choice, rebalancing frequency decisions |

</aside>

## Volatility Does Not Scale as the Square Root of Time

The textbook relationship states that if daily volatility is σ, then monthly volatility should be σ × √21 (approximately, for 21 trading days). In practice, this rule often fails. A stock exhibiting 1% daily volatility over a month does not automatically deliver 15% (1% × √21) realized monthly volatility. The mismatch arises from mean reversion, volatility clustering, and regime changes that flatten or steepen the [term-structure](/implied-volatility/) of volatility in ways the √T assumption ignores.

Empirically, longer-term volatility is often *lower* than the square-root rule would predict, especially in developed equity markets. If you calculate rolling 1-month realized volatility from daily returns, then 3-month realized volatility, and then annual, you typically find that the 3-month figure does not equal 1-month volatility × √3. Instead, the term structure curves—sometimes upward (longer horizons more volatile), sometimes downward (mean reversion dominates), sometimes flat.

## Mean Reversion and Volatility Clustering

Two forces shape the term structure. **Volatility clustering** means that if today is turbulent, tomorrow is likelier to be turbulent too. This creates autocorrelation in squared returns, making the sum of near-term squared returns higher-than-random. Over longer periods, this clustering matters less because you are averaging across multiple calm and turbulent regimes.

**Mean reversion in volatility** pulls the opposite direction: after a spike, volatility tends to settle back toward its long-term average. Investors who lived through the 2008 crash saw extreme daily moves; on a one-month rolling basis, volatility was extreme. But three months later, as panic eased, the longer-horizon realized volatility—which includes those calmer weeks—was lower than extrapolating from the worst week would suggest.

The net result: a negatively sloped volatility term structure is common (short-term volatility higher than medium-term), especially immediately after a shock. A flat or upward-sloping structure signals either stable conditions or expectations of future turmoil.

## Implied vs. Realized Term Structure

Options markets provide a forward-looking term structure through [implied-volatility](/implied-volatility/) prices across strike and expiration date. A one-month [option](/option/) on a stock might carry 20% implied volatility; a six-month option, 18%. This downward slope signals that the market expects elevated near-term turbulence to fade. Conversely, if six-month volatility exceeds one-month, investors expect renewed unease ahead.

**Realized volatility**, calculated from historical returns, reveals what actually happened. Comparing realized volatility curves before and after a crisis shows how regimes shift. In stable periods, realized volatility term structures are often gently upward (longer periods collect more independent shocks and hence more total variation). In crisis periods, they plunge as mean reversion dominates.

The gap between implied and realized term structures is itself a source of return. A [hedge-fund](/hedge-fund/) or volatility trader who believes the market overprices six-month volatility relative to one-month can exploit the discrepancy if the term structure indeed flattens.

## Practical Implications for Risk Measurement

**Value-at-risk ([VAR](/value-at-risk/))** models must specify a horizon: a 95% one-day VAR is far different from a 95% 10-day VAR, and not purely because of the √T relationship. A portfolio of liquid stocks might have a one-day VAR of $100,000 but a 10-day VAR closer to $250,000 (not $316,000, which √10 would suggest) if mean reversion and reduced liquidity over the longer window are factored in.

**Margin systems** at brokerages and clearinghouses use VAR-like models to set haircuts and margin calls. If the system assumes √T scaling on a day when the term structure is unusually steep, it underestimates true multi-day risk and may not hold sufficient buffer. Conversely, if it overestimates (as happened in some 2020 flash-crash scenarios), it imposes unnecessary margin calls.

**Rebalancing frequency** decisions also hinge on the term structure. A fund manager who rebalances monthly faces volatility risk over that month that is not simply 1/21st of annual volatility. If the term structure is downward-sloping (mean-reverting), less frequent rebalancing is tolerable; if upward-sloping, more frequent rebalancing might be warranted to manage risk.

## Modeling the Term Structure

Practitioners use several approaches:

- **Parkinson volatility** and other high-low estimators capture intraday swings and are less dependent on closing price discretization, producing different term structures than daily closing-to-closing volatility.
- **GARCH and stochastic volatility models** parameterize mean reversion and clustering explicitly, allowing forecast volatility to vary by horizon in a structured way.
- **Realized variance** (summing squared high-frequency returns) and **realized quarticity** (related to jump risk) refine the realized volatility term structure by isolating continuous vs. jump components.

Long-term investors often care less about the precise shape and more about the robustness of their estimates. A simple stress test—computing volatility over multiple historical sub-periods and observing the range—often proves more reliable than trusting a single model's term structure prediction.

## See also

<div class="wiki-seealso">

### Closely related

- [Volatility smile](/volatility-smile/) — Why option-implied volatility varies by strike price and how the term structure interacts with moneyness
- [Historical volatility](/historical-volatility/) — Measuring realized volatility from past returns and interpreting rolling windows
- [Value-at-risk](/value-at-risk/) — Risk measurement framework where horizon choice drives the term structure of estimated losses
- [Implied volatility](/implied-volatility/) — Forward-looking volatility from option prices and how it compares to realized term structures

### Wider context

- [Derivatives hedging](/derivatives-hedging/) — Using derivatives to manage risk across different time horizons
- [Options](/option/) — Contracts whose value and implied volatility vary by expiration horizon
- [Stress testing](/stress-testing/) — Multi-scenario risk assessment that spans different market conditions and time windows

</div>
