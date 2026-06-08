---
title: "Real Dividend Discount Model"
description: "Restating dividends and discount rate in inflation-adjusted terms for long-horizon equity valuation."
keywords:
  - real returns
  - inflation-adjusted
  - purchasing power
  - real discount rate
  - real dividend growth
image: "/svg/valuation.svg"
---

*A **real dividend discount model** recasts the standard [dividend discount model](/discounted-cash-flow-valuation/) in inflation-adjusted (purchasing-power) terms. Instead of projecting nominal dividends and using a nominal discount rate, the analyst works in constant dollars: real dividends and a real required return. For valuations spanning decades, real framing clarifies whether growth is genuinely robust or merely nominal inflation. It is essential for pension funds and other long-term investors concerned with purchasing power, not headlines.*

## Why real valuation matters for long horizons

The standard dividend discount model works in nominal (current-dollar) terms. Dividends are forecast in future-year dollars, and the discount rate is nominal—the required return in those same nominal terms. For a 5- or 10-year forecast, nominal framing is intuitive and practical.

But for very long horizons—20, 30, or 50 years—the effects of [inflation](/inflation/) become enormous. If inflation averages 2.5% per year, the purchasing power of a pound 30 years out is roughly half of today's. A forecast showing dividend growth of 4% per year looks robust until one realises that 1.5% of that growth is just inflation: real (inflation-adjusted) growth is only 2.5%.

Conversely, a nominal discount rate of 8% in an inflation environment of 2.5% implies a real discount rate of approximately (1.08 / 1.025) – 1 ≈ 5.4%. That real return is what matters for long-term purchasing power. Working in real terms makes these distinctions explicit and guards against phantom growth and returns.

## Converting nominal to real: the Fisher equation

The relationship between nominal rates, real rates, and inflation is captured by the **Fisher equation**:

(1 + Nominal Rate) = (1 + Real Rate) × (1 + Inflation Rate)

Rearranged for real rate:

Real Rate ≈ [(1 + Nominal Rate) / (1 + Inflation Rate)] – 1

Or, for small numbers, the approximation: Real Rate ≈ Nominal Rate – Inflation Rate.

**Example:** A nominal discount rate of 9% in an environment with expected inflation of 2.5% yields a real required return of approximately (1.09 / 1.025) – 1 ≈ 6.34%, or roughly 9% – 2.5% = 6.5% using the linear approximation.

Similarly, dividend growth is often quoted nominally but must be decomposed:

Nominal Growth = Real Growth + Inflation

A firm that nominally grows its dividend 5% per year in a 2.5% inflation environment is growing real dividends by approximately (1.05 / 1.025) – 1 ≈ 2.44%, or roughly 5% – 2.5% = 2.5% using the approximation.

## The real dividend discount model formula

In real terms, the [Gordon growth](/dividend-discount-model/) perpetuity simplifies:

Real Value (in today's pounds) = Real Dividend / (Real Discount Rate – Real Growth Rate)

where:
- Real Dividend is the next expected dividend in today's constant pounds (i.e., what that dividend is worth in purchasing power today).
- Real Discount Rate is the required return in real terms.
- Real Growth Rate is the sustainable growth rate in real (inflation-adjusted) terms.

The formula is identical to the nominal version; only the inputs change. The result is an intrinsic value expressed in today's purchasing power—the "real" value to a long-term holder.

## Consistency: staying in real terms throughout

A critical discipline in real valuation is **never mixing real and nominal**. Common mistakes include:

- Using a **nominal discount rate with real dividends.** This implicitly assumes dividends lose purchasing power while the discount rate captures inflation—nonsensical.
- Using a **real discount rate with nominal dividends.** This double-counts inflation, understating value.
- Using a **real growth rate with nominal terminal value assumptions.** A terminal price-to-earnings multiple (a nominal market measure) should not be applied to real cash flows.

To avoid these errors, build the entire model in one framework. The trade-off is:

**Nominal approach (more common in practice):** Project nominal dividends, use nominal required return, interpret results as market value in future-year dollars. Reconcile to market prices denominated in future dollars.

**Real approach (clearer for long horizons):** Project real (constant-dollar) dividends, use real required return, interpret results as purchasing power value in today's dollars. This is immune to inflation surprises: if inflation turns out higher than expected, both numerator and denominator adjust together, and the real valuation is unaffected.

## Real growth rates: separating substance from inflation

Many dividend-paying firms—utilities, consumer staples, mature industrials—see nominal dividend growth that is largely or entirely inflation. A utility that raises its dividend 3% per year in an inflation environment of 2.5% is growing real dividends by roughly 0.5% per year. This is essential to understand: the investor is not getting wealthy faster (in real terms) by holding the stock; the nominal dividend is rising mainly to preserve purchasing power.

Conversely, a firm in a high-inflation emerging market might show 15% nominal dividend growth, of which only 5% is real growth; the rest is just prices rising. Real analysis exposes whether dividend growth is a genuine operational achievement or a statistical artifact of inflation.

For pension funds and endowments that are concerned with inflation-adjusted returns, this distinction is primary. A 3% real dividend growth rate, locked in, is worth far more than a 5% nominal rate that is half inflation.

## Setting real discount rates

The real required return is trickier to estimate than the nominal rate. The **capital asset pricing model** ([CAPM](/capital-asset-pricing-model/), if you're using it) typically produces a nominal required return. To convert to real, apply the Fisher equation as above.

Alternatively, some practitioners derive real required return from real long-term Treasury yields. If a real long-term TIPS (Treasury Inflation-Protected Securities) yield is 1.5% and the equity risk premium is 4.5%, the real required return on equity is approximately 1.5% + 4.5% = 6%. This approach directly sidesteps the need to forecast inflation.

Over very long horizons, real required returns are usually lower than nominal ones—perhaps 4–6% for equities, depending on risk profile. The reason: much of the nominal return is simply the compensation for inflation eroding purchasing power. A 4% real return on equities is quite high historically; it reflects a strong claim on future economic output.

## Inflation variability and stress testing

One advantage of real valuation is clarity about inflation assumptions. If the base case assumes 2.5% inflation and the valuation is highly sensitive to this (small changes in assumed inflation swing value by 20%), the analyst should stress-test it: what if inflation runs 1% or 4% per year instead?

In real terms, this stress is transparent. Higher inflation means lower real growth rates (nominal growth minus higher inflation) and potentially a lower (higher) real discount rate (depends on real risk premium). The real model makes these trade-offs visible.

Nominal models, by contrast, can obscure inflation sensitivity. A nominal model built assuming 2.5% inflation will give nonsensical results if inflation surprises upwards to 4% and the analyst does not re-model; the real model is more robust to inflation surprises because the real inputs are more stable.

## Multi-stage real models

Real valuation is particularly valuable in multi-stage models. A company in a high-inflation developing country might have nominal growth of 20% in years 1–5, declining to 15% in years 6–10, and 8% perpetually. In real terms (assuming 6% inflation), this becomes 13% real in years 1–5, 8.5% in years 6–10, and 2% perpetually. The second picture is much less flattering and more credible.

Stage-of-life transitions (high growth to moderate to mature) are easier to model in real terms: growth rates naturally narrow. A mature firm in any currency zone will have real growth around 1–3%, with nominal growth equal to that plus the inflation rate of the currency. This consistency is a powerful discipline check.

## Reconciling real valuation to market prices

A subtlety arises when translating real valuations back to market prices (which are quoted nominally). If the real DDM yields an intrinsic value of £50 per share in today's pounds, and inflation runs 2.5% per year, the equivalent nominal value 10 years from now is £50 × (1.025)^10 ≈ £64. The analyst must be careful to either (a) state the valuation in today's pounds and compare to the current market price, or (b) inflate the valuation forward and compare to a forward price.

Most practitioners stick with real values in constant dollars, avoiding the inflation path forward. This is cleaner: today's intrinsic value in today's pounds is compared to today's market price, and the analyst avoids having to forecast inflation explicitly.

## Real dividend discount vs. real free cash flow

The real dividend model is a special case of real discounted cash flow valuation. Some practitioners prefer **real free cash flow** models, which value all cash generated by the firm (whether distributed or retained) in real terms. The dividend model is a simpler subset, suitable for firms with stable, predictable dividend policies. For cyclical or high-growth firms that have inconsistent dividend payout policies, a real FCF model is more flexible.

The principles of real valuation—isolating real growth, real returns, and avoiding nominal-real mixing—apply equally to FCF models.

## See also

<div class="wiki-seealso">

### Closely related

- [Dividend Discount Model](/discounted-cash-flow-valuation/) — nominal version; foundation for the real variant.
- [Terminal Value in Dividend Models](/terminal-value-dividend-model/) — inflation-adjusted perpetuity assumptions.
- [Dividend Growth Rate Estimation](/dividend-growth-rate-estimation/) — decomposing nominal growth into real and inflation components.
- [Inflation](/inflation/) — the macroeconomic variable that makes real valuation necessary.
- [Interest Rate](/interest-rate/) — nominal rates and Fisher equation relationships.

### Wider context

- [Real Interest Rate](/real-interest-rate/) — real discount-rate concept applied to bonds.
- [Discounted Cash Flow Valuation](/discounted-cash-flow-valuation/) — broader DCF framework of which real DDM is part.
- [Payout Ratio as a Valuation Input](/payout-ratio-valuation-input/) — dividend sustainability in real terms.
- [Capital Asset Pricing Model](/capital-asset-pricing-model/) — if using CAPM to derive nominal required return, convert to real.

</div>
