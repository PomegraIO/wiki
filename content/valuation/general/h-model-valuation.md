---
title: "H-Model Valuation"
seo_title: "H-Model Valuation: Formula for Fading Dividend Growth"
description: "The H-Model values stocks whose dividend growth declines linearly to a stable rate. The Fuller-Hsia formula, when to use it, and what H means."
keywords:
  - H-model
  - two-stage dividend model
  - declining growth
  - dividend discount model
  - valuation method
image: "/svg/valuation.svg"
---

*The **H-Model** is a dividend valuation framework designed for companies transitioning from rapid growth to stability. Rather than assuming constant growth forever (as in a perpetuity) or making sudden jumps (as in typical two-stage models), the H-Model posits that growth *declines linearly* over a specified horizon. This captures the real arc of maturing businesses and reduces the sensitivity to arbitrary "high-growth" vs. "stable-growth" cutoff dates.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">H-Model — key facts</div>

<img src="/svg/valuation.svg" alt="An abstract editorial mark for valuation and pricing." />

<div class="wiki-infobox-caption">Smoother growth decay for businesses leaving their high-expansion phase.</div>

|   |   |
|---|---|
| **What it is** | A two-stage model where growth rate declines linearly to a stable rate |
| **Also called** | Fuller-Hsia model, linear-decline dividend model |
| **Key parameters** | Initial growth rate, stable growth rate, half-life (H) of decline period |
| **Best for** | Mature growth companies, recent IPOs, restructuring firms |
| **Key formula** | Price per share = D₀ × [(1 + gₗ)/(r – gₗ) + H × (gₛ – gₗ)/(r – gₗ)²] |
| **H parameter** | Half the length of the linear decline period in years |

</aside>

## The problem it solves

Standard [dividend discount models](/dividend/) typically use one of two structures. The constant-growth model (Gordon Growth) assumes dividends grow at rate g forever. Simple, elegant—but wildly wrong for young, fast-expanding firms. The two-stage model assumes high growth for n years, then abrupt switch to stable growth. More realistic, but the cutoff is arbitrary: why exactly year 5 for this company?

The H-Model offers a middle path. It acknowledges that growth doesn't switch on a dime. A company growing 20% annually doesn't suddenly drop to 4% in year 6 and stay there. Instead, growth slows gradually as the company matures, faces larger base effects, and loses the ability to reinvest capital at sky-high returns.

The "H" refers to the half-life of the decline. If you model growth decaying linearly over 10 years, H = 5 (half the period). If over 20 years, H = 10. This parameter anchors how long the transition takes.

## The formula and its components

The H-Model value per share is:

**P = D₀ × [(1 + gₗ)/(r – gₗ) + H × (gₛ – gₗ)/(r – gₗ)²]**

where:

- D₀ = current dividend per share
- gₗ = initial (long-term or high) growth rate
- gₛ = stable, perpetual growth rate (typically 2–3%)
- r = [cost of equity](/cost-of-equity/) (discount rate)
- H = half-life of the linear decline (years)

The first term, (1 + gₗ)/(r – gₗ), looks like a perpetuity formula—the value if growth stayed at gₗ forever. The second term, H × (gₛ – gₗ)/(r – gₗ)², is the *adjustment* for the fact that growth will eventually decay to gₛ.

## Interpreting H (the critical parameter)

H is the linchpin. It controls the slope of the growth decline. A large H means the transition is long and gentle; a small H means growth collapses quickly.

For a startup or young company with competitive advantages, H might be 8–15 years: growth is high but you expect it to stay elevated for a decade or so before settling. For a mature company undergoing modest cyclical upswing, H might be 2–3 years: you expect normalisation soon.

The choice of H often reflects industry dynamics and company age. A software-as-a-service (SaaS) company with strong network effects and low churn might justify H = 10; a cyclical industrial firm might warrant H = 3. The model is sensitive to H, so varying it in a range—say, H = 5 to 10—is wise.

## Why linear decline is more realistic than a hard cutoff

Imagine a company growing 15% annually. A traditional two-stage model might say: "15% for five years, then 3% forever." By year 6, growth has dropped from 15% to 3% overnight. That's mechanically discontinuous.

The H-Model allows growth to decline smoothly: 15% in year 1, 13% in year 2, 11% in year 3, and so on, reaching 3% by year 11 (if H = 5). This tracks real-world patterns more closely. Businesses rarely hit a wall; instead, competitive pressures, market saturation, and reinvestment constraints gradually erode returns.

This smoothness also reduces the model's sensitivity to the arbitrary "forecast horizon" problem. In a standard two-stage model, moving the cutoff from year 5 to year 7 can meaningfully change value. The H-Model is more forgiving because the transition is continuous.

## Practical application: valuing a growth-stage company

Suppose a dividend-paying tech company currently yields $2.00 per share and is growing dividends at 12% annually. You believe that over time, it will mature and settle at 3% growth. The cost of equity is 9%.

Using the H-Model, you might assume:
- gₗ (initial growth) = 12%
- gₛ (stable growth) = 3%
- r (cost of equity) = 9%
- H = 7 (you expect the transition to take roughly 14 years, with half-life of 7)
- D₀ = $2.00

Plugging in:

P = $2.00 × [(1.12)/(0.09 – 0.12) + 7 × (0.03 – 0.12)/(0.09 – 0.12)²]

The math: (1.12 / –0.03) = –37.33 (perpetuity with negative denominator means high value), and the adjustment term adds incremental value from the expected dividend growth during the transition phase. The result might be, say, $95 per share.

(Note: the numerator being negative is odd here; this example illustrates why r must exceed gₗ for the model to work smoothly—cost of equity must be higher than initial growth.)

## Comparison with other models

The H-Model sits between pure [constant-growth dividend models](/dividend-discount-model/)—which ignore growth decay—and [free cash flow DCF approaches](/discounted-cash-flow-valuation/). It's simpler than a full multi-stage DCF because it requires fewer explicit forecast years, yet more nuanced than a single-rate perpetuity.

It's also a dividend-focused model, so it's most naturally applied to dividend-paying stocks. For non-dividend payers, use [free cash flow](/free-cash-flow/) or [earnings](/earnings-per-share/) as a proxy for payable cash, or resort to a full DCF.

## When the H-Model works best

The H-Model excels when:
- The company pays (or is expected to pay) steady, growing dividends
- Growth is elevated today but expected to normalize over a medium horizon (5–15 years)
- The industry is mature enough that you can estimate a stable long-run growth rate
- You want to avoid the mechanical sharp-cutoff assumption of traditional two-stage models

It works less well when:
- Growth is unpredictable or volatile
- The company is in a nascent, uncertain market where the long-term stable rate is unknowable
- Dividends are irregular or reinvestment needs are opaque

## Sensitivity and stress-testing

Because the H-Model depends on gₗ, gₛ, r, and H, varying each reveals how robust your valuation is:
- If initial growth drops from 12% to 10%, does the value change by 5% or 50%? (High sensitivity means you must be confident in growth assumptions.)
- If the cost of equity rises from 9% to 10%, how much does value decline? (This tests the discount rate assumption.)
- If H shifts from 7 to 5 years, does the conclusion hold? (Short-term uncertainty around the transition pace.)

A responsible H-Model valuation presents a range: base case, upside, and downside, each with defensible assumptions.

## See also

<div class="wiki-seealso">

### Closely related

- [Dividend Discount Model](/dividend-discount-model/) — the foundational framework the H-Model extends
- [Cost of Equity](/cost-of-equity/) — the discount rate in the H-Model valuation formula
- [Dividend Yield](/dividend-yield/) — current yield of the dividend base
- [Dividend Payout Ratio](/dividend-payout-ratio/) — sustainability of the dividend stream
- [Terminal Value Estimation](/terminal-value-estimation/) — the perpetual stable-rate value analogous to the H-Model's endgame
- [Franchise Value Approach](/franchise-value-approach/) — alternative decomposition of growth value

### Wider context

- [Discounted Cash Flow Valuation](/discounted-cash-flow-valuation/) — the broader DCF family
- [Business Cycle](/business-cycle/) — economic context for growth normalization
- [Earnings Quality](/earnings-quality/) — ensuring dividends reflect sustainable earnings
- [Price-to-Earnings Ratio](/price-to-earnings-ratio/) — alternative valuation multiple

</div>
