---
title: "Choosing the Risk-Free Rate for a DCF"
description: "How to select the appropriate risk-free rate for a DCF model, including maturity alignment and whether to use spot or normalized rates."
keywords:
  - risk-free rate selection DCF
  - discount rate
  - government bond maturity
  - treasury yield curve
  - cost of capital
---

*Selecting the **risk-free rate** is the first step in building any [discount rate](/discount-rate/), yet practitioners often gloss over it. The choice is not trivial: it sets the floor for the entire valuation. The core decision hinges on matching the maturity of the government bond to the [holding period](/holding-period/) of the asset being valued, and on choosing between current market yields (spot) and long-run historical norms (normalized). Get this wrong, and a DCF model will systematically misprize the [enterprise value](/enterprise-value/) or [equity value](/return-on-equity/) of the firm.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Risk-Free Rate — key facts</div>

<img src="/svg/valuation.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">The floor beneath all cost-of-equity estimates.</div>

|   |   |
|---|---|
| **Definition** | Interest rate on the safest sovereign bond, typically US [Treasury bill](/treasury-bill/) or [Treasury bond](/treasury-bond/) |
| **Common choices** | 10-year yield (typical for equity DCF) or 20–30-year yield (longer-duration assets) |
| **Spot vs. normalized** | Current yield vs. historical average; affects valuation in low-rate or high-rate regimes |
| **Maturity matching** | Choose bond maturity ≈ forecast horizon or asset life; 10-year Treasury standard for stock valuations |
| **Risk-free assumption** | Requires stable sovereign credit; US Treasury is the global reference |
| **Adjustment in crisis** | Consider term premiums; overnight rates (SOFR, fed funds) are not risk-free rates |

</aside>

## The Maturity Question: Matching Horizons

The first rule of [risk-free rate](/risk-free-rate-selection-dcf/) selection is **maturity alignment**. A 10-year-old company with a 5-year cash flow forecast should theoretically use a 5-year risk-free rate, not a 10-year rate. A mature utility with a 30-year concession should use a 30-year bond yield. The logic is straightforward: the rate you use as a discount rate should reflect the time horizon over which you are valuing cash flows.

In practice, however, most equity analysts use the **10-year US Treasury yield** as the risk-free rate for stock valuations. This has become a convention, justified loosely by the assumption that equity dividends are perpetual (or very long-dated), so a medium-to-long maturity bond is appropriate. A 10-year yield is available, widely quoted, liquid, and understood by investors.

**But the convention breaks down in specific cases:**

- **High-growth technology or biotech** with a 5-year explicit forecast period might use a 5-year or 7-year Treasury, since the perpetuity assumption is less defensible for young firms.
- **Long-duration assets** like infrastructure, real estate (especially land), or utilities with 30+ year concessions should anchor to a 20–30 year Treasury yield. Using a 10-year rate will overstate the [discount rate](/discount-rate/) and undervalue stable, long-cash-flow assets.
- **Short-term debt or bond valuations** should use bond-equivalent maturity: a 5-year corporate bond should be discounted at a 5-year Treasury rate plus a [credit spread](/credit-spread/), not a 10-year rate.

Many valuation errors stem from misaligned maturities. A real estate investor using a 10-year Treasury to discount a 50-year lease will systematically compress property values, incorrectly marking down yields and [cap rates](/cap-rate/).

## Spot Rates vs. Normalized Rates: The Timing Problem

Once maturity is chosen, the second decision is whether to use the **current (spot) yield** or a **normalized (long-run historical average) yield**.

### Spot Rate Approach
Use today's Treasury yield. If the 10-year Treasury is trading at 4.2%, that is your risk-free rate. Advantage: reflects market conditions *now*, avoiding the appearance of arbitrary historical adjustment. Disadvantage: in regimes of extreme rates (very low after a financial crisis, very high during inflation), your valuation will be out of sync with long-run economic returns. A DCF built with a 0.5% risk-free rate in 2012 would have massively overvalued most stocks relative to their long-run earnings potential.

### Normalized Rate Approach
Use a long-run historical average (e.g., 10-year Treasury's 60-year mean, roughly 4–4.5%). Advantage: insulates valuations from temporary rate swings, producing comparable [relative valuations](/relative-valuation/) across cycles. Disadvantage: requires defensible historical data and judgment about what counts as "normal" in a changing world (interest rates and [inflation expectations](/inflation-expectations/) have shifted over decades).

**When to use spot:** In a stable [interest rate](/interest-rate/) regime with normal [yield curve](/yield-curve/) shape and minimal [inflation](/inflation/) surprises. Most practitioners use spot rates as default; it is the market rate and reflects current opportunity cost of capital.

**When to use normalized:** In obvious regime shifts—deep [recession](/recession/) with emergency rate cuts, or [inflation](/inflation/) shock with rapid [central bank](/central-bank/) tightening. A normalized rate helps avoid anchoring on unsustainable extremes. Institutional long-term investors (pension funds, insurance companies) often default to normalized rates to smooth valuations across [business cycles](/business-cycle/).

A practical compromise: use the spot rate for near-term forecasts (years 1–5), but assume the [interest rate](/interest-rate/) normalizes in later forecast years. For example, if the 10-year Treasury is 3.0%, but you expect [Federal Reserve](/federal-reserve/) tightening, assume 4.5% in your terminal-value [discount rate](/discount-rate/).

## The "Risk-Free" Assumption in Practice

The term "risk-free" is a convention, not a literal truth. No bond is completely free of risk:

- **Sovereign default risk:** Even US Treasuries carry infinitesimal default risk (though so low that markets treat them as risk-free). Weaker sovereigns' bonds must be adjusted for credit spread.
- **Inflation risk:** A real (inflation-adjusted) risk-free rate is lower than the nominal rate. If [inflation](/inflation/) spikes, a fixed-rate bond loses purchasing power. Inflation-protected bonds ([TIPS](/tips/)) offer one solution.
- **Term risk:** Longer-maturity bonds carry more interest-rate risk. A 30-year Treasury can swing 20%+ on a 100 bp [interest rate](/interest-rate/) move; this is why it commands a term premium over shorter bonds.

For equity valuations, practitioners use **nominal risk-free rates** (current Treasury yields), which implicitly assume a forward [inflation](/inflation/) rate baked into the yield curve. Adjustments for inflation risk are made in the **[equity risk premium](/capital-asset-pricing-model/)** (the [alpha](/alpha/) on top of the risk-free rate), not the risk-free rate itself.

## Practical Selection: A Decision Tree

1. **Identify the asset's cash flow duration.** Is this a 5-year forecast, 10-year concession, or perpetual dividend? Choose a Treasury maturity in the ballpark.
2. **Check the yield curve.** If the curve is normal (upward sloping), a 10-year Treasury will be higher than a 5-year; if inverted, vice versa. This matters for relative value.
3. **Assess the interest rate regime.** If current rates are near historical extremes (very high or very low), consider averaging with a historical norm. If rates are in a typical range, spot rates are defensible.
4. **Cross-check against peer valuations.** If peers use 4.5% risk-free rates and you use 2.5%, you need a strong reason (different maturity, normalized assumption) to explain the gap.
5. **Document and stress-test.** Explicitly state which rate you chose and why. Run a sensitivity table: "if risk-free rate is +/- 1%, [enterprise value](/enterprise-value/) changes by X%." This makes the assumption transparent.

## Currency and Sovereign Considerations

The risk-free rate must be in the same currency as the cash flows being discounted. A US dollar DCF uses the US Treasury; a euro-denominated valuation uses the German Bund or ECB rate. For a firm with [consolidated revenues](/cash-flow-statement/) across currencies, this requires a judgment call: use the currency of the [parent company](/board-of-directors/) or the functional operating currency.

If valuing a subsidiary in an emerging market, the risk-free rate is *not* the local sovereign bond yield (which embeds [sovereign default](/sovereign-default/) risk). Instead, use the US Treasury as the risk-free floor, and layer on a country-risk premium. This is the [capital asset pricing model](/capital-asset-pricing-model/) approach.

## See also

<div class="wiki-seealso">

### Closely related

- [Discount Rate](/discount-rate/) — the full cost of capital; risk-free rate is the foundation
- [Capital Asset Pricing Model](/capital-asset-pricing-model/) — standard framework for deriving cost of equity above risk-free rate
- [Treasury Bond](/treasury-bond/) — the source instrument; yield curves and term structure matter
- [Interest Rate](/interest-rate/) — determines risk-free rate level
- [Cost of Equity](/cost-of-equity/) — how risk-free rate feeds into equity valuation
- [Yield Curve](/yield-curve/) — maturity structure of Treasury yields

### Wider context

- [Discounted Cash Flow Valuation](/discounted-cash-flow-valuation/) — how risk-free rate is used in practice
- [Federal Reserve](/federal-reserve/) — sets short-term rates; influences the whole curve
- [Inflation Expectations](/inflation-expectations/) — embedded in nominal Treasury yields
- [Credit Spread](/credit-spread/) — added to risk-free rate for non-Treasury debt

</div>
