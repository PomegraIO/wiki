---
title: "Gordon Growth Model Assumptions and Limitations"
description: "Understanding the core assumptions behind the Gordon Growth Model, including constant growth rates and why they often break down in real markets."
keywords:
  - gordon growth model assumptions
  - constant growth model
  - dividend discount model limitations
  - terminal value calculation
  - growth rate stability
image: /svg/valuation.svg
---

*The **Gordon Growth Model** simplifies company valuation by assuming dividends grow at a perpetual, unchanging rate—but this assumption has sharp limits, and the model breaks entirely when growth approaches or exceeds the discount rate. Understanding where it works and where it fails is essential for anyone applying this formula to real stocks.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Gordon Growth Model — Key Facts</div>

<img src="/svg/valuation.svg" alt="An abstract editorial mark for valuation." />

<div class="wiki-infobox-caption">A perpetuity formula that values a company by one unchanging dividend-growth assumption.</div>

|   |   |
|---|---|
| **Formula** | P = D₁ / (r − g) |
| **Core assumption** | Dividends grow at constant rate g forever |
| **Discount rate** | r (required return); must exceed g |
| **Fatal flaw** | Breaks when g ≥ r |
| **Best for** | Mature, stable firms with predictable payout policy |
| **Worst for** | Growth companies, cyclicals, payout uncertainty |

</aside>

## The Three Bedrock Assumptions

The Gordon Growth Model rests on three assumptions that rarely hold perfectly in practice. First, the company will continue paying dividends indefinitely. Second, those dividends will grow at a constant, stable rate (g) in perpetuity. Third, the required return (discount rate, r) will remain constant and exceed the growth rate.

Strip away these assumptions and the formula crumbles. Yet many analysts apply it anyway, either forgetting the conditions or hoping small violations don't matter much. They often do.

## Constant Growth Rate: The First Problem

Real companies do not grow at the same rate forever. A firm expanding at 15% per year in its prime reaches saturation, slows to 8%, then eventually matches the broader economy at 3% or less. The Gordon Model ignores this arc entirely—it bakes in a single growth rate from now until the end of time.

This works least badly for genuinely mature firms: utilities, REITs, staple consumer goods makers with stable market share and predictable reinvestment. For a utility paying 4% dividend yield growing at 2.5% annually, assuming that 2.5% persists for decades is a reasonable shorthand. The business itself changes little; regulated rates and steady costs make cash flows visible.

But apply the same perpetuity formula to a software company currently growing at 25% and the absurdity becomes clear. Nothing grows at 25% forever. Using that single rate ignores the near-certain slowdown, overstating intrinsic value. This is why [multi-stage dividend discount models](/multi-stage-dividend-discount-model-example/) exist—they let growth decline in stages before settling to a stable long-term rate.

## The Discount Rate Must Exceed Growth

The Gordon Model equation is P = D₁ / (r − g). Notice the denominator: (r − g). 

When g approaches r, the denominator shrinks, and price explodes to infinity. When g exceeds r mathematically, the formula spits out a negative value—nonsense. Economically, this means the company is growing faster than the overall return investors demand. That is not sustainable forever; it violates the model's very premise of perpetual stability.

This limitation is not a minor edge case. Any analyst assuming a growth rate within 0.5% of the discount rate is living in a fantasy. The buffer must be real and material. For a large-cap stock with a 9% cost of equity, assuming a 8.5% perpetual dividend growth rate is reckless; the model cannot handle it and should not be used.

## Dividend Stability and Payout Policy

The model assumes the company's payout ratio—the fraction of earnings paid out as dividends—remains constant. In reality, boards adjust or eliminate dividends when cash flow turns rough, redirect capital to share buybacks or acquisitions, or increase payouts when profits soar.

During a recession, a bank might cut its dividend 30% overnight. A high-growth tech firm might decide it no longer fits the dividend-paying profile and suspend distributions entirely. These policy shifts are real and material to shareholders, yet the Gordon Model treats payout as carved in stone.

More subtly, the payout ratio interacts with the [sustainable growth rate](/sustainable-growth-rate-dividend-valuation/). If a firm retains 40% of earnings and earns a 15% return on retained capital, its sustainable growth rate is 6%. But if the board then raises the payout to 60%, only 40% of earnings are retained, growth drops to 4%, and the model's growth assumption becomes instantly obsolete. Analysts must update their inputs, but many do not.

## What the Model Gets Right

Despite its flaws, the Gordon Model offers genuine insight for the right application. It forces clarity on the relationship between required return, growth, and valuation. It shows concretely why a mature, slow-growth firm must be cheap (low price relative to dividends) or investors would not buy it. It explains why dividend-paying stocks attract income-focused investors: the formula shows explicitly that *lower* required return (from lower risk or preference for current cash) justifies *higher* valuation multiples.

For valuing a [REIT](/real-estate-investment-trust/) distributing 95% of taxable income, or a steady utility with predictable rate increases, the simplicity is an asset. The assumptions are nearly true, the inputs are observable, and the result is quick and defensible.

## Terminal Value and Model Sensitivity

In practice, most analysts use the Gordon Growth Model as a plug for terminal value in a [discounted cash flow](/discounted-cash-flow-valuation/) or [multi-stage DDM](/multi-stage-dividend-discount-model-example/) model. They forecast dividends explicitly for 5 or 10 years, then apply perpetuity growth to value the rest of the firm.

This hybrid approach weakens—but does not eliminate—the constant-growth problem. A 5-year explicit forecast captures cyclicality and change. The terminal value formula is a smaller fraction of total value (often 60–75%). Still, terminal value is enormous; tiny changes in g or r swing the answer wildly.

Sensitivity analysis is non-negotiable. If changing the perpetual growth rate by 0.5% or the discount rate by 1% moves valuation by 20% or more, the model is too fragile for confidence. That fragility signals the assumptions are stretched.

## When the Model Should Not Be Used

Avoid the Gordon Growth Model—even as a terminal value—for companies with uncertain or suspended dividends, firms in transition or restructuring, growth stocks where payouts are years away, or markets where dividend policy is volatile or unclear. The model cannot gracefully handle [multiple stages of growth](/multi-stage-dividend-discount-model-example/) without becoming a different, more complex tool. For cyclical or distressed firms, option-based approaches or [relative valuation](/relative-valuation/) methods are more honest about uncertainty.

The Gordon Model's simplicity is both its charm and its trap. It feels like precision—one formula, a few inputs, an answer. But that appearance of precision masks three fragile assumptions. Use it as a sanity check on other methods or for genuinely stable firms. Do not mistake simplicity for accuracy.

## See also

<div class="wiki-seealso">

### Closely related

- [Dividend Discount Model](/dividend-discount-model/) — The broader framework of which Gordon Growth is the simplest form
- [Multi-Stage Dividend Discount Model Explained With an Example](/multi-stage-dividend-discount-model-example/) — Relaxing the constant-growth assumption for realistic forecasts
- [Sustainable Growth Rate in Dividend Valuation](/sustainable-growth-rate-dividend-valuation/) — How payout policy and ROE bound the growth rate
- [Dividend Distribution](/dividend-distribution/) — How dividends are actually set and paid
- [Terminal Value](/terminal-value/) — Using perpetuity formulas as part of DCF valuation
- [Discounted Cash Flow Valuation](/discounted-cash-flow-valuation/) — The broader valuation framework

### Wider context

- [Cost of Equity](/cost-of-equity/) — How the discount rate (r) is derived
- [Dividend Yield](/dividend-yield/) — The yield payout relative to price
- [Return on Equity](/return-on-equity/) — The driver of sustainable growth
- [Intrinsic Value](/intrinsic-value/) — What valuation models attempt to find

</div>
