---
title: "Excess Return Approach to Dividend-Based Valuation"
description: "Use excess return dividend models to decompose value into asset value plus returns on future dividends, bridging dividend discount and residual income approaches."
keywords:
  - excess return dividend valuation model
  - dividend valuation excess returns
  - asset value plus growth
  - residual income dividend
  - retained earnings valuation
image: "/svg/valuation.svg"
---

*An **excess return dividend model** decomposes a stock's value into two parts: the value of assets already in place plus the present value of excess returns on future investment—making it easier to see whether a company creates value or merely harvests existing value.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Excess Return Dividend Model — key facts</div>

<img src="/svg/valuation.svg" alt="An abstract editorial mark for valuation." />

<div class="wiki-infobox-caption">Value = Assets-in-place + PV of excess returns on growth.</div>

|   |   |
|---|---|
| **Core equation** | V = Book value + PV(excess returns on retained earnings) |
| **Key insight** | Separates mature cash generation from growth value creation |
| **When to use** | Stable dividend companies with steady reinvestment |
| **Excess return** | (Return on equity − Required return) × Retained earnings |
| **Ties to** | [Dividend discount model](/dividend-discount-model/), residual income valuation |

</aside>

## The Bridge Between Two Valuation Worlds

The standard [dividend discount model](/dividend-discount-model/) treats dividends as a fixed stream and discounts them backward. The residual-income framework values a company by starting with its [book value](/balance-sheet/) and adding the present value of "excess returns"—returns above the cost of capital. The excess return dividend model fuses these two approaches, using dividends and retention to link them.

Here's the economic logic: A company's shareholders own net assets on the balance sheet. Those assets generate earnings. Part of earnings flows out as dividends; part is retained and reinvested. Retained earnings belong to shareholders, but only create value if they earn more than the cost of capital. This model makes that split explicit and quantifiable.

## The Core Formula

The simplest form is:

**V = B₀ + Σ[(ROE − r) × Rₑ / (1 + r)ᵗ]**

Where:
- **B₀** = current book value per share
- **ROE** = expected return on equity (what the firm earns on its assets)
- **r** = cost of equity (required return)
- **Rₑ** = retained earnings per share in period t
- The sum extends to perpetuity

The first term, B₀, is what you'd pay if the company created no value—you'd simply be buying its existing asset base at book value. The second term is the capitalized value of excess returns. If ROE exceeds the cost of equity, the firm converts retained earnings into shareholder value. If ROE falls short, retention destroys value.

## A Concrete Example

Imagine a financial company with:
- Current book value: $50 per share
- Expected ROE: 12%
- Cost of equity: 10%
- Dividend payout ratio: 60%
- Earnings per share (stable): $5.00
- Implied retention ratio: 40%

First, identify the excess return per dollar of retained earnings:
- ROE − r = 12% − 10% = 2% (excess spread)
- Annual retained earnings = $5.00 × 40% = $2.00 per share
- Annual excess return = 2% × $2.00 = $0.04 per share

If earnings, ROE, and retention remain constant, retained earnings grow steadily, and excess returns compound. Assuming they grow at the payout ratio's implied rate (40% of 5%, or 2% in simplified form), the present value of perpetual excess returns is:

**PV(excess returns) = $0.04 × 1.02 / (0.10 − 0.02) = $0.04 × 1.02 / 0.08 = $0.51 per share**

Intrinsic value = $50 + $0.51 = $50.51 per share. The company trades near book value because its excess spread is modest. If ROE were 15% (a 5% spread), the excess return would balloon to:

**($5 × 0.40) × 0.05 × 1.025 / 0.08 ≈ $1.28 per share**, lifting fair value to $51.28—still not dramatic because the earnings base is small relative to book value.

## Reconciling Excess Returns with the Dividend Discount Model

You might ask: doesn't this double-count? The [dividend discount model](/dividend-discount-model/) values future dividends directly; doesn't the excess return model also capture the same cash?

No—they're two views of the same economic reality. Under a DDM, a $5 annual dividend growing at 2% (the retention-based growth rate) with a 10% discount rate values the stock at $5.10 / 0.08 = $63.75. But the DDM assumes the retained earnings are reinvested and enhance future dividends. The excess return model makes that assumption transparent: reinvested earnings create value only if ROE exceeds the cost of capital.

If you build both models with the same assumptions, they converge to the same value. The excess return framework is simply more anatomical—it shows you *why* the value emerges, not just *what* the value is.

## When Excess Returns Flip Negative

If ROE falls below the cost of equity, the company destroys shareholder value by retaining earnings. A bank earning 8% ROE with a 10% cost of equity that retains 40% of earnings is burning value with every dollar it plows back in. In such cases, intrinsic value is actually *below* book value unless management reverses course. This framework makes value-destructive retention impossible to miss.

Many mature, slow-growth industries cluster near this trap. If a utility earns 9% returns on a 10% cost of capital, it should pay out close to 100% of earnings as dividends rather than reinvest. The excess return model flags this immediately.

## Extending to Multi-Stage Growth

Real companies transition from high-growth to mature states. A two-stage excess return model might assume:

- Years 1–5: ROE of 14%, cost of equity 10%, retention 50% (excess spread 4%)
- Year 6+: ROE of 11%, cost of equity 10%, retention 30% (excess spread 1%, declining value creation)

You calculate excess returns for each explicit period, then a terminal value using the stable-state formula. The model naturally captures the reality that young, high-ROE companies create value through retention, while mature, lower-ROE firms don't.

## Linking to Residual Income

The excess return dividend model is a close cousin of **residual income valuation**, which values a firm as book value plus discounted residual profits. Residual profit = (ROE − r) × book value. For a stable dividend company, this becomes nearly identical to the excess return approach. The excess return model simply emphasizes the role of retention and growth, making it especially intuitive for dividend analysis.

## Practical Limitations

**ROE stability is heroic**: The model assumes ROE remains constant (or follows a predictable path). Real ROEs cycle with competition, capital intensity, and industry health. A cyclical firm earning 15% ROE in a boom year but 6% in a trough year resists this kind of analysis.

**Book value may not reflect economic value**: For asset-light tech or brand-driven consumer companies, book value is near useless. Equity is intangible or highly marked up. The model works best for asset-intensive, stable-margin businesses: utilities, banks, insurance, mature industrials.

**Retention ratios change**: Dividends are policy choices, not economic laws. A company might retain less when growth slows, or harvest cash if ROE declines. Building in changing retention assumptions adds realism but complexity.

## Using Excess Returns for Screening

In practice, excess return models excel at screening. Calculate B₀ + one year of excess returns for a peer group. Firms trading well below intrinsic value under reasonable ROE assumptions are candidates. Conversely, stocks trading well above book value with modest excess spreads are priced for near-permanent high ROE—a risky assumption. The model forces you to articulate what ROE the market is pricing in.

## See also

<div class="wiki-seealso">

### Closely related

- [Dividend Discount Model](/dividend-discount-model/) — perpetual-growth framework valuing dividends as a stream
- [Dividend Discount Model Sensitivity Analysis](/dividend-discount-model-sensitivity-analysis/) — stress-testing DDM inputs and assumptions
- [Return on Equity](/return-on-equity/) — the core metric linking earnings to shareholder capital
- [Cost of Equity](/cost-of-equity/) — the discount rate that defines excess returns
- [Dividend Discount Model for Cyclical Companies](/dividend-discount-model-cyclical-companies/) — adapting dividends when ROE swings with the cycle

### Wider context

- Valuation — frameworks for estimating intrinsic stock value
- Residual Income — earnings above the cost of capital as a value driver
- Book Value — the accounting net asset base underlying this model
- [Retained Earnings](/retained-earnings/) — the profits reinvested rather than distributed

</div>
