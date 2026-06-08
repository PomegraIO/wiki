---
title: "Currency Risk in Cross-Border DCF Valuation"
description: "How to handle currency risk in cross-border DCF valuation by forecasting in consistent currency and matching discount rate assumptions."
keywords:
  - currency risk in cross-border dcf
  - cross-border dcf valuation
  - foreign currency dcf
  - currency conversion dcf
  - international company valuation
  - fx risk valuation
  - dcf in multiple currencies
image: /svg/valuation.svg
---

*When valuing a foreign company, **currency risk in cross-border DCF valuation** emerges because cash flows are earned in one currency while the acquirer or investor operates in another. The fix is not to hide the risk—it is to forecast and discount in a single, consistent currency, and to ensure the discount rate matches that currency.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Cross-Border DCF — key facts</div>

<img src="/svg/valuation.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Currency consistency is the core rule: forecast cash flows in one currency and discount them using a WACC denominated in that same currency.</div>

|   |   |
|---|---|
| **Core principle** | Forecast and discount in the same currency; never mix |
| **Two consistent approaches** | Local currency path or hard currency path |
| **Where errors creep in** | Forecasting in local currency, discounting in USD (or vice versa) |
| **Terminal value sensitivity** | Currency choices amplify terminal value risk |
| **Practical convention** | Most analysts forecast in local currency, then convert final equity value |

</aside>

## The currency mismatch trap

The mechanical flaw that derails many cross-border deals is straightforward: an analyst forecasts cash flows in the local currency (say, Indian rupees) but then discounts them using a WACC calculated in US dollars. Or the reverse. The result is a valuation that conflates currency appreciation with operational performance and overstates or understates the true [enterprise value](/enterprise-value/).

The [discount rate](/discount-rate/) reflects the cost of capital in a particular currency. A 10% dollar-denominated WACC is not equivalent to a 10% rupee-denominated WACC—the difference is tied to inflation expectations, fiscal risk, and currency stability in each region. When cash flows and discount rate are denominated in different currencies, the formula produces a number that is simultaneously in two currencies and in neither.

Mismatching currency and discount rate is not a small rounding error. It can inflate a valuation by 20–40% or deflate it by similar margins, depending on the direction of the mismatch and the relative stability of the currencies involved.

## Approach 1: Forecast and discount in local currency

The first consistent path is to stay in local currency throughout. Forecast all cash flows (NOPAT, capex, working capital changes, and [free cash flow](/free-cash-flow/)) in the foreign company's home currency. Build a WACC using local-currency cost of debt and cost of equity. Discount the entire cash flow stream at that local-currency WACC. The result is enterprise value in the local currency.

**Example:** A Brazilian manufacturer is valued at BRL 2 billion using a 9% local-currency WACC (reflecting Brazil's inflation and credit spread). Once you have the BRL enterprise value, convert it to your home currency (USD, EUR, or whatever) using the spot exchange rate.

This approach works well because:
- Operating metrics and margins naturally sit in the local currency.
- The local WACC reflects the true cost of capital for a business operating in that jurisdiction.
- Currency exposure is confined to the terminal point (the conversion of final equity value).
- It parallels how local analysts already think about the company.

The drawback is that all [currency risk](/currency-risk/) is pushed into that single spot-rate conversion at the end. If the rupee depreciates 15% between now and acquisition close, the USD value falls by 15%, even if the business's operational cash flows were strong. That is the correct economic outcome—the investor owns rupee cash, not dollars—but it can surprise those who treat a valuation as a point estimate rather than a probabilistic range.

## Approach 2: Forecast in local currency, discount in hard currency

The second consistent approach is to forecast cash flows in local currency, then discount them using a hard-currency (home-currency) WACC that already bakes in expected currency depreciation.

**Example:** A Thai subsidiary earns THB cash flows. Instead of using a local Thai WACC, you use a USD WACC that is higher—say, 12% instead of 8%—because the 4% premium reflects the expected baht-to-dollar depreciation over the valuation horizon.

This approach is trickier because it requires estimating long-run currency drift. Over short 5–10 year horizons, major currencies do not reliably converge to purchasing-power parity. A home-currency WACC must account for:
- The local real [interest rate](/interest-rate/) (the cost of capital in the foreign country, inflation-adjusted).
- The [inflation rate differential](/inflation/) between the two countries (expected to drive currency movement over time).

The advantage is that all cash flows and the discount rate are now in the same currency (USD, EUR, etc.), so the output is denominated in that currency without further conversion. The disadvantage is that the WACC calculation becomes more complex, and small errors in estimating long-run depreciation amplify across a 10–30 year valuation horizon.

## Why the mismatch happens

Practitioners slip into mismatches because:

1. **Institutional habit.** A US acquirer may have an internal WACC formula (calculated in dollars) and apply it globally without adjustment. Conversely, a valuation tool may be hardcoded to accept "WACC" and "growth rate" without flagging currency.

2. **Ambiguous cash flow projections.** If management guidance is silent on currency assumptions, an analyst may assume local currency is implied—then discount at a hard-currency rate that was already embedded in a template.

3. **Complexity avoidance.** Building two distinct WACCs (one local, one adjusted for currency) requires extra work. The one-size WACC is faster but wrong.

## Practical workflow

Most professional analysts follow this sequence:

1. **Forecast in local currency.** Get the operational projections from management, local competitors, and industry reports. All in the home currency of the target company.

2. **Build a local-currency WACC.** Use local equity risk premium (or estimate beta using local comps), local cost of debt, and local tax rate. Discount the cash flows.

3. **Convert enterprise value.** Take the final EUR, GBP, JPY, or MXN number and convert to your reporting currency at the spot rate.

4. **Stress terminal value.** Because the terminal value comprises 60–80% of total enterprise value and is denominated in local currency, test sensitivity to a ±10–20% move in the exchange rate. This isolates currency risk from operational risk.

Alternatively, if you have a strong view on long-run currency paths, you can embed that into the hard-currency WACC. But be explicit: document the inflation differential and depreciation assumption so that anyone reading the model knows what currency bet is embedded in the 12% discount rate.

## Terminal value and currency exposure

Because the [terminal value](/enterprise-value/) is typically 60–80% of enterprise value in a DCF, currency assumptions disproportionately affect the final number. A small change in the assumed terminal growth rate or exit exchange rate can swing equity value by 25–40%.

If you forecast in local currency and convert at the terminal year, you are implicitly assuming the perpetual growth rate applies in the local currency—meaning the company's real cash generation stays constant, but its currency-adjusted value can fluctuate. That is the correct frame: the operator cares about real rupee cash; the investor's dollar value depends on where the rupee trades in year 10 and beyond.

## Consistency checklist

Before finalizing any cross-border DCF:

- Verify that all cash flow projections are in **one currency** (and note which one in the model header).
- Confirm that the WACC or discount rate is **denominated in that same currency**.
- If forecasting in local currency and discounting at a hard-currency WACC, document the **expected inflation differential and currency depreciation assumption**.
- Stress the **terminal exchange rate** independently from operational sensitivity.
- Show conversions explicitly so stakeholders can challenge currency assumptions separately from valuation assumptions.

The cost of mixing currencies is visible: an enterprise value that is simultaneously too high and too low, depending on who reads it. The payoff for being consistent is clean, defensible valuation that isolates operational value from currency exposure.

## See also

<div class="wiki-seealso">

### Closely related

- [Discount Rate](/discount-rate/) — how to calculate the rate that matches your forecast currency
- [Enterprise Value](/enterprise-value/) — the output of the DCF that needs currency clarity
- [Free Cash Flow](/free-cash-flow/) — the metric you forecast in local terms
- WACC — the discount rate that must match your cash flow currency
- [Terminal Value](/terminal-value/) — the largest component and most sensitive to currency bets
- [Currency Risk](/currency-risk/) — the underlying exposure you are modeling

### Wider context

- [Discounted Cash Flow Valuation](/discounted-cash-flow-valuation/) — the parent methodology
- [Sensitivity Analysis Valuation](/sensitivity-analysis-valuation/) — how to isolate currency swings from operational risk
- [Foreign Exchange Risk](/currency-risk/) — the market mechanism driving currency movements
- [International Financial Reporting Standards](/international-financial-reporting-standards/) — accounting rules that differ by country and affect NOPAT

</div>
