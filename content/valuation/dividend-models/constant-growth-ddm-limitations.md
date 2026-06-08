---
title: "Constant-Growth DDM Limitations"
description: "Where the Gordon Growth Model fails: hyper-growth firms, declining dividends, and when growth rate approaches required return."
keywords:
  - constant growth dividend discount model limitations
  - Gordon Growth Model problems
  - DDM when growth approaches discount rate
  - dividend model limitations
  - two-stage dividend discount model
---

*The **constant-growth dividend discount model** (the Gordon Growth Model) values a stock as the next dividend divided by the discount rate minus the growth rate: P = D₁ / (r – g). It is simple and intuitive, but breaks down—often catastrophically—when its core assumptions fail. If the perpetual growth rate approaches or exceeds the discount rate, the formula explodes to infinity or negative values. If a firm is in hyper-growth, pays irregular dividends, or is in terminal decline, the constant-growth framework produces misleading valuations. Understanding when and why the model fails is essential to avoiding trap valuations.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Constant-Growth DDM Limitations — when it breaks</div>

<img src="/svg/valuation.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">A simple formula works only when its assumptions hold.</div>

|   |   |
|---|---|
| **Critical condition** | Growth rate (g) must be less than discount rate (r); if g ≥ r, the model is invalid |
| **Hyper-growth problem** | Firms growing faster than the economy indefinitely are rare; assuming perpetual growth > 3% is often unrealistic |
| **Non-dividend payers** | Firms that reinvest all earnings (growth stocks) must be valued on a two-stage or free-cash-flow model instead |
| **Irregular dividend history** | Dividends that fluctuate, decline, or stop break the constant-growth assumption |
| **Terminal value misguidance** | If g is too high or r is poorly estimated, terminal value overstates or understates the true value drastically |
| **When to use alternatives** | Multi-stage models (two-stage, H-model, three-stage), [free cash flow](/free-cash-flow/) models, or [earnings-based](/earnings-per-share/) valuation |

</aside>

## The mathematical boundary: when g approaches r

The Gordon Growth Model is:

> P = D₁ / (r – g)

Where D₁ is the next dividend, r is the required return, and g is the perpetual growth rate.

The formula has a built-in singularity: as g approaches r, the denominator shrinks, and price approaches infinity. If g equals or exceeds r, the model is mathematically undefined (division by zero or negative denominator).

**In practice, this is catastrophic.** Suppose you estimate:
- Next dividend: \$2.
- Required return: 10%.
- Growth rate: 9.5%.

Price = \$2 / (0.10 – 0.095) = \$2 / 0.005 = **\$400 per share**.

A tiny 0.5% gap between r and g produces an enormous valuation. Move g to 9.8%, and price jumps to **\$1,000**. Move it to 9.9%, and it reaches **\$2,000**. The formula is _hypersensitive_ near the boundary.

This is not a feature; it is a flaw. In reality, no firm grows at 9.9% forever without the economy eventually catching up or competitive advantage eroding. The model's extreme sensitivity reveals that it is making an unrealistic assumption: **perpetual growth at a rate nearly as high as the required return**.

## Hyper-growth firms and the perpetual growth assumption

Mature, dividend-paying firms in stable industries (utilities, REITs, some banks) can plausibly grow at 2–4% indefinitely, roughly in line with long-term GDP growth. For these firms, the Gordon Growth Model is reasonable.

But high-growth firms—tech startups, biotech companies, emerging-market telecoms—often grow at 15%, 30%, or higher for 5–10 years. The constant-growth model tempts you to assume this continues forever.

**Example: A high-growth software firm.**
- Current dividend: \$0.50 per share.
- Recent growth: 20% per year.
- Analyst estimates perpetual growth: 8% (a step down, but still optimistic).
- Required return: 12%.

Price (constant model) = \$0.50 × 1.08 / (0.12 – 0.08) = \$0.54 / 0.04 = **\$13.50**.

But this assumes the firm grows 8% _forever_. In reality, the firm will eventually saturate its market, face competition, and mature. Perpetual 8% growth might be achievable in the first five years, but not in years 6–30. A more realistic model would assume 8% growth for ten years, then a step-down to 3% perpetual growth. This **two-stage model** would produce a much lower valuation, because most cash flows are discounted over a longer horizon and at a lower growth rate.

The constant-growth model, by ignoring the inevitable slowdown, overstates value. The error is largest for firms with the highest growth rates, precisely where the formula is most tempting to use.

## Non-dividend payers and the zero-dividend trap

The Gordon Growth Model requires dividends. But many (if not most) high-growth firms do not pay dividends. Amazon, Meta, and Tesla historically reinvested all earnings; they issued no dividends for years. Applying the constant-growth DDM to a zero-dividend stock is nonsensical.

**Option 1: Assume a future dividend.** You could assume the firm begins paying a dividend in five years and apply the model from that point. But this introduces another layer of assumption (when dividends start, how much, what growth rate), compounding the forecast uncertainty.

**Option 2: Use free cash flow instead of dividends.** The dividend discount model is a special case of the discounted cash flow model. If dividends are not paid, value what cash flows the firm _could_ return to shareholders: its **[free cash flow](/free-cash-flow/)**. The formula becomes:

> P = FCF₁ / (r – g)

Where FCF₁ is next year's free cash flow. This generalizes the model and applies to all firms, not just dividend payers. But it also requires estimating free cash flow, which is more complex than dividing reported earnings.

**Option 3: Use two-stage DDM with a dividend initiation date.** Assume the firm grows without paying dividends for n years, then begins paying 30% of earnings as a dividend at a lower growth rate. This is more flexible but requires more inputs.

## Declining dividends and the sign-reversal problem

Some firms cut dividends when profitability falls. A bank's dividend might drop 50% in a recession; a commodity company's dividend might halve if prices collapse.

If you apply the constant-growth model to a declining-dividend firm, the formula can produce negative or nonsensical results. Suppose:
- Current dividend: \$1.00.
- Estimated perpetual growth: –2% (declining 2% per year).
- Required return: 10%.

Price = \$1.00 × 0.98 / (0.10 – (–0.02)) = \$0.98 / 0.12 = **\$8.17**.

This assumes dividends shrink forever at 2% per year. In reality, dividends cannot shrink forever; they would reach zero and then… what? The model does not handle the boundary condition of hitting zero dividends. A declining-dividend firm is usually in distress and requires a different valuation approach: either a turnaround scenario (dividends stabilize and recover), a liquidation value (firm is shrinking), or explicit modeling of when dividends go to zero.

## High required return and misestimation of r

The required return, r, is typically estimated using the [capital asset pricing model](/capital-asset-pricing-model/) (CAPM):

> r = rf + β(rm – rf)

Where rf is the risk-free rate, β is the stock's beta, and (rm – rf) is the equity risk premium.

A 1% error in r can drastically change the valuation. Using the earlier example:
- If r = 10%, price = \$13.50.
- If r = 11%, price = \$27 / 0.09 = ... wait, that's wrong. Let me recalculate: \$0.54 / (0.11 – 0.08) = \$0.54 / 0.03 = **\$18**.
- If r = 9%, price = \$0.54 / (0.09 – 0.08) = \$0.54 / 0.01 = **\$54**.

A ±1% error in r causes the valuation to double or halve. This sensitivity is yet another reason the constant-growth model is fragile: it relies on a single, often-imprecise estimate of required return.

## Dividend payout ratio and sustainability

The constant-growth model does not explicitly account for whether the dividend is sustainable. It assumes the firm can grow at rate g while paying out D₁ year after year.

Implicitly, the model rests on a growth constraint. If a firm grows at rate g, it must reinvest (g × earnings) back into the business. The remainder can be paid out as dividends. If the firm pays out more than it can sustain, the growth rate will fall (because there is less reinvestment for growth) or the dividend will eventually be cut.

Formally:

> g = ROE × Retention Ratio
>
> Dividend Payout Ratio = 1 – Retention Ratio

If a firm has a 15% return on equity (ROE) and retains 70% of earnings, g = 10.5%. If it then pays out 50% of earnings as dividends, the math is inconsistent: it cannot retain 70% and pay 50% simultaneously. A more careful model reconciles the payout ratio, retention, growth, and ROE.

Many analysts apply the constant-growth model without checking this internal consistency, leading to valuations that assume unrealistic dividend and growth combinations.

## When constant-growth DDM is appropriate

The model works well for:

- **Mature, stable firms** with a long history of consistent, growing dividends (e.g., utilities, municipal water authorities, mature REITs).
- **Terminal value estimation** in multi-stage models, where you assume the firm has reached stable growth by year 10 or 15.
- **Back-of-envelope valuations** to check if a stock is in a reasonable range before detailed analysis.
- **Firms with low growth rates** (2–4%), where the assumption of perpetual growth is close to long-term GDP growth and is less obviously violated.

The model fails for high-growth firms, non-dividend payers, irregular-dividend firms, and any situation where g is close to r.

## Alternatives to constant-growth DDM

**Two-stage model:**
Assume high growth for n years (e.g., 10 years at 10%), then stable growth thereafter (e.g., 3% perpetually). Compute present value of dividends in stage 1, plus terminal value at the end of stage 1. This is more realistic for growth firms.

**H-model (half-life model):**
Assumes growth linearly declines from a high initial rate to a stable long-term rate over a decade. More flexible than two-stage, less data-hungry than three-stage.

**Free cash flow to equity (FCFE) model:**
Value the firm's free cash flow available to shareholders, rather than dividends. Applies to all firms, regardless of payout policy.

**Multiples-based valuation:**
Use [price-to-earnings](/price-to-earnings-ratio/), [price-to-book](/price-to-book-ratio/), or [price-to-sales](/price-to-sales-ratio/) ratios of comparable firms to triangulate value. Avoids the perpetual-growth assumption entirely.

**Intrinsic value frameworks:**
Value the firm based on competitive advantages, market size, and return-on-invested-capital. More qualitative but less mechanical.

## See also

<div class="wiki-seealso">

### Closely related

- [Dividend Discount Model](/dividend-discount-model/) — the broader DDM framework of which constant-growth is one variant
- [Gordon Growth Model](/dividend-discount-model/) — the formal name for the constant-growth formula
- [Two-Stage Dividend Discount Model](/dividend-discount-model/) — a more flexible extension for firms with distinct growth phases
- [Dividend Yield](/dividend-yield/) — the dividend-to-price ratio, inversely related to valuation
- [Dividend Payout Ratio](/dividend-payout-ratio/) — the percentage of earnings paid as dividends; constrains sustainable growth

### Wider context

- [Discounted Cash Flow Valuation](/discounted-cash-flow-valuation/) — the general principle underlying dividend models
- [Cost of Equity](/cost-of-equity/) — the required return (r) that enters the formula
- [Capital Asset Pricing Model](/capital-asset-pricing-model/) — the standard method to estimate required return
- [Free Cash Flow](/free-cash-flow/) — an alternative to dividends for valuation
- [Terminal Value](/discounted-cash-flow-valuation/) — the estimated value at the end of an explicit forecast period

</div>
