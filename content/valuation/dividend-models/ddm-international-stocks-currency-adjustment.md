---
title: "DDM for International Stocks: Currency Adjustment"
description: "How to apply dividend discount model valuation to international stocks, accounting for foreign currency dividends and exchange-rate expectations."
keywords:
  - dividend discount model international stocks currency
  - ddm foreign currency valuation
  - international equity valuation
  - currency-adjusted dividend discount model
  - foreign dividend valuation
  - home currency equity valuation
---

*The **dividend discount model** for international stocks requires a critical choice: whether to forecast dividends in the local currency or convert them to your home currency, and how to reflect exchange-rate expectations in the discount rate. Get this wrong, and you double-count or ignore currency risk entirely.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Currency-Adjusted DDM — key facts</div>

<img src="/svg/valuation.svg" alt="An abstract editorial mark for valuation." />

<div class="wiki-infobox-caption">Foreign currency dividends must be reconciled with discount-rate assumptions.</div>

|   |   |
|---|---|
| **Core principle** | Work entirely in one currency (local or home) and keep discount-rate assumptions consistent |
| **Two valid approaches** | (1) Forecast local dividends, discount at local rate; (2) Convert forecasts to home currency, adjust rate for currency expectations |
| **Critical error** | Mixing currencies between numerator and denominator—local dividends with home-currency discount rate |
| **Exchange-rate assumption** | Usually PPP (purchasing-power parity) or forward rates; affects both expected dividends and required return |
| **Why it matters** | Currency movements can dominate total returns; ignoring them overstates or understates intrinsic value by 10–50% |

</aside>

## The core problem: dividend currency mismatch

A Japanese utility pays 500 yen per share annually. A German-based investor wants to value it using the [dividend discount model](/dividend-discount-model/). Should she forecast yen dividends and discount at a yen rate? Or should she convert everything to euros?

The temptation is to mix: keep the dividend in yen but discount it at her euro-denominated cost of equity. This is fatal. The discount rate embeds assumptions about returns in the currency it is stated in. A 7% euro cost of equity assumes returns measured in euros; it does not apply to yen cash flows.

The solution is methodological consistency. You must choose one of two paths, then stick to it throughout.

## Path 1: Local-currency valuation

Forecast dividends in the company's reporting currency (yen, for the Japanese utility), and discount them at a cost of equity calculated for investors in that market.

The formula becomes:

<div style="background: #f5f5f5; padding: 12px; margin: 12px 0; border-left: 4px solid #ccc; font-family: monospace;">
Value (in yen) = D₁ / (r_local – g)
</div>

Where D₁ is the next expected yen dividend, r_local is the cost of equity for a yen-based investor, and g is the expected long-term dividend growth rate in yen.

Then convert the final valuation to your home currency at the current spot rate.

**Advantages:**
- Simplest conceptually; you value the company "as seen from its home market."
- Uses local market data (borrowing costs, equity risk premiums) directly.

**Disadvantages:**
- Requires estimating a local cost of equity, which demands local market parameters (risk-free rate, market risk premium, beta estimates for the local market).
- The currency conversion at the end is a point estimate—you get only today's spot rate, not any forward-looking adjustment.

## Path 2: Home-currency valuation

Convert expected local-currency dividends to your home currency at each forecasting step (or at least in steady state), then discount using your home-currency cost of equity.

The formula becomes:

<div style="background: #f5f5f5; padding: 12px; margin: 12px 0; border-left: 4px solid #ccc; font-family: monospace;">
Value (in home currency) = [D₁ × (1 + X) / (1 + r_home) – g]
</div>

Where X is the expected annual change in the exchange rate (e.g., if you expect yen to appreciate 2% per year, X = 0.02), and r_home is your home-currency cost of equity.

Alternatively, many practitioners fold the expected currency movement into the discount rate itself:

<div style="background: #f5f5f5; padding: 12px; margin: 12px 0; border-left: 4px solid #ccc; font-family: monospace;">
Value (in home currency) = D₁ / (r_home – g_adjusted)
</div>

Where g_adjusted includes both the yen dividend growth rate AND the expected yen appreciation rate (if the two are roughly independent).

**Advantages:**
- Requires only your own home-market parameters; no need to estimate a foreign cost of equity.
- Forces explicit, testable assumptions about future exchange rates.

**Disadvantages:**
- Requires you to forecast currency movements, which is extremely difficult and often unreliable.
- Small errors in exchange-rate assumptions can swing valuation by 10–20%.

## How exchange-rate expectations interact with the discount rate

The key insight is that currency appreciation or depreciation is *part* of your total return. If you own a yen-denominated dividend stream and the yen appreciates against your home currency, you benefit twice: once from the dividend in yen terms, and again from the favorable exchange move.

This means your required return in home-currency terms can be lower than the local yen return if you expect yen to appreciate. Conversely, if you expect yen to depreciate, you need a higher home-currency return to compensate for the currency headwind.

In the long run, economists often assume [purchasing-power parity](/): currencies move to offset inflation differentials, so a currency with higher expected inflation depreciates over time. Under PPP, a Japanese investor (facing low inflation and low nominal rates) should expect the yen to gradually strengthen against currencies of higher-inflation economies. A German investor valuing a yen stock should expect the yen to strengthen against the euro, which acts as a modest tailwind on returns.

But PPP is a long-run tendency, not a law. Over a 5- or 10-year forecast horizon, currency moves can be large and arbitrary.

## Practical implications for valuation

**If you choose Path 1 (local currency):**
- Use Japanese government bond yields (or corporate spreads in that market) to estimate r_local.
- Assume dividend growth matches yen GDP growth or Japanese inflation over the long term.
- Convert the final value to home currency at today's spot rate only.
- Sensitivity-test your valuation against a range of future spot rates to see how currency moves would affect your return.

**If you choose Path 2 (home currency):**
- Estimate your home cost of equity using your own [capital asset pricing model](/capital-asset-pricing-model/) parameters.
- Forecast local dividends in yen, then explicitly convert them using forward exchange rates (if available) or your own exchange-rate assumptions.
- For steady-state perpetual growth, decide whether to assume PPP (currency drifts with inflation) or a constant real exchange rate.
- Be aware that valuation is sensitive to small changes in your currency forecast; model several scenarios.

## Dividends and currency in the formula

If a company pays dividends partly in the local currency and partly repatriates to the home country, the treatment depends on your ownership and tax status. A [custodian](/custodian/) may withhold foreign taxes on the dividend; this reduces the effective dividend in home-currency terms. Any [dividend withholding tax](/dividend-distribution/) is currency-agnostic—it applies whether you value in local or home currency, but you must net it out consistently in the numerator (lower dividend) or the discount rate (higher required return).

Most valuations assume the investor receives the full dividend as forecast and apply home-country tax treatment separately, outside the valuation model.

## When currency becomes dominant

In extreme cases—high-inflation economies, [credit-event](/credit-event-sovereign/) risk, or sharp currency devaluation—exchange-rate movements can overwhelm dividend yield. A stock yielding 8% in Turkish lira becomes worthless if the lira depreciates 20% per year. Conversely, a stable currency with 2% dividend yield and 3% annual appreciation can deliver 5% total return in home-currency terms.

This is why international equity valuations often require scenario analysis. A base case might assume PPP or stable real rates; a downside case models currency depreciation; an upside case assumes currency appreciation. The spread in outcomes reflects both business risk and [currency risk](/currency-risk/).

## See also

<div class="wiki-seealso">

### Closely related

- [Dividend discount model](/dividend-discount-model/) — core valuation formula for all dividend-paying stocks
- [Capital asset pricing model](/capital-asset-pricing-model/) — how to estimate cost of equity in any currency
- [Foreign exchange and interest-rate parity](/): macroeconomic foundations for exchange-rate forecasting
- [Purchasing-power parity](/): long-run currency adjustment via inflation differentials
- [Currency risk](/currency-risk/) — how exchange-rate uncertainty affects portfolio returns
- [Dividend withholding tax](/dividend-distribution/) — tax treatment of foreign dividends

### Wider context

- [Relative valuation](/relative-valuation/) — comparing price multiples across currencies
- [Emerging market equity valuation](/): special considerations for high-inflation, high-risk economies
- [Proxy statement](/proxy-statement/) — how foreign companies disclose dividend policy

</div>
