---
title: "Residual Income Terminal Value: Perpetuity vs Fade Assumptions"
description: "Residual income terminal value methods contrast perpetuity assumptions with fade formulas. Learn which terminal value assumption affects your valuation most."
keywords:
  - residual income terminal value perpetuity vs fade
  - terminal value assumptions
  - perpetuity growth method
  - fade assumption valuation
  - residual income model
image: /svg/valuation.svg
---

*The **residual income terminal value** problem boils down to a single question: how long does excess profit last? A perpetuity assumes abnormal returns forever; a fade model smooths them toward zero; a reversion model collapses them to book value immediately. Each choice can swing a valuation by 20–40%, making it the single largest driver of long-term value in the model.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Terminal Value in Residual Income — Key Facts</div>

<img src="/svg/valuation.svg" alt="An abstract editorial mark for valuation." />

<div class="wiki-infobox-caption">Terminal assumptions determine what fraction of value comes after year 10.</div>

|   |   |
|---|---|
| **What it is** | The estimated value of cash flows beyond the explicit forecast period |
| **Why it matters** | Often 40–70% of total intrinsic value |
| **Three main methods** | Perpetuity, fade-to-growth, reversion-to-book |
| **Key input** | Steady-state [return-on-equity](/return-on-equity/) vs [cost-of-equity](/cost-of-equity/) |
| **Tax effect** | Terminal assumptions cascade through tax on distributions |
| **Reality check** | Few firms earn excess returns forever; fade or reversion models more defensible |

</aside>

## What Residual Income Means in Terminal Value

In a [discounted-cash-flow-valuation](/discounted-cash-flow-valuation/) model, [residual income](/residual-income-terminal-value-perpetuity-vs-fade/) is the profit a company earns *above* what investors require. If a firm has [equity](/common-stock/) of $100 million, and [cost-of-equity](/cost-of-equity/) is 10%, investors expect $10 million in annual returns. Any profit above that $10 million is "residual." The residual income valuation approach values the firm by predicting that excess income over an explicit forecast period (typically 5–10 years), then applying a terminal value formula to everything beyond.

The challenge is that no one knows whether residual income disappears at year 11, fades gradually, or persists forever. Each assumption yields starkly different answers.

## The Perpetuity Assumption (No Fade)

A perpetuity assumes the company earns abnormal returns *indefinitely*. If residual income stabilizes at $5 million and the cost of equity is 10%, the perpetuity formula is:

**Terminal Value = Residual Income / Cost of Equity**  
**= $5 million / 0.10 = $50 million**

This method is mathematically clean and implicitly assumes competitive advantages never erode. In practice, it is rarely accurate. A pharmaceutical company with a blockbuster drug may earn abnormal returns for years, but the patent eventually expires. A dominant software business may sustain margins longer, but new entrants or disruption typically narrow the moat. Markets punish firms that assume infinite competitive advantage; perpetuities are often flagged in valuation reviews as too optimistic.

Use a perpetuity only when the company has structural defenses (monopoly, global brand, network effects) that genuinely seem impervious to competition. Even then, most practitioners apply a small growth rate or durability adjustment to temper the assumption.

## The Fade Assumption (Gradual Reversion)

A fade model assumes residual income gradually shrinks toward zero over a specified period—typically 20–40 years beyond the forecast period. If residual income is $5 million at year 10 and fades linearly to zero by year 50:

- Year 11–20: 90%, 80%, 70% of $5 million  
- Year 21–30: 60%, 50%, 40% of $5 million  
- Year 31–50: 30%, 20%, 10%, then 0%

Terminal value = PV of this declining stream, discounted at the cost of equity. A fade model is far more intuitive: competition strengthens, efficiency gains plateau, and returns normalize. Over a long enough period, nearly all firms revert to a competitive equilibrium where [return-on-equity](/return-on-equity/) equals [cost-of-equity](/cost-of-equity/).

The fade is sensitive to two parameters:

1. **Fade duration**: 20 years vs 40 years produces very different terminal values. Shorter fades are more conservative.
2. **Fade shape**: Linear (constant dollar decline) vs exponential (constant percentage decline) affects the trajectory. Exponential fades are smoother and slightly less punitive to near-term years.

For a diversified industrial company or consumer staple, a 20–30 year fade is standard. For tech or biotech with genuine uncertainty, a 10–15 year fade is more prudent.

## The Reversion-to-Book Assumption (Immediate Collapse)

The most conservative approach assumes residual income collapses to zero *at the terminal date*. This means [return-on-equity](/return-on-equity/) drops instantly to cost of equity, and terminal value equals the book value of equity at that date. If the forecast ends at year 10 and projected book equity is $150 million:

**Terminal Value = Book Value (year 10) = $150 million**

This is defensible for mature, cyclical industries (steel, auto, real estate) where excess returns are temporary and competition is brutal. It is also the most conservative, and therefore the easiest to defend in a disputed valuation.

The reversion method has a peculiar asymmetry: it assumes *zero* abnormal returns forever, yet most practitioners using it also assume the company generates positive residual income in years 1–10. This disconnect is intentional—it reflects the belief that the current environment is abnormally favorable, but abnormality does not persist.

## Quantifying the Impact

Consider a firm with:
- Year 1–10 residual income = $5 million annually  
- Cost of equity = 10%  
- Book value at year 10 = $100 million  

**Perpetuity (no fade):**  
Terminal Value = $5 million / 0.10 = $50 million

**Fade over 30 years (exponential 5% annual fade rate):**  
Terminal Value ≈ $15–18 million (depending on calculation method)

**Reversion to book:**  
Terminal Value = $100 million

The perpetuity yields 5× the value of the fade, and 2× the value of reversion. Over a typical [discounted-cash-flow-valuation](/discounted-cash-flow-valuation/), terminal value often represents 50–70% of total value, so the choice between perpetuity and fade can swing the final answer by 30–50%.

## Choosing the Right Terminal Value Assumption

**Perpetuity**: Use only if the company has durable competitive advantages unlikely to erode (network effects, brand strength, regulatory moats). Even then, consider a sub-perpetuity formula that assumes growth tapers after 10–20 years.

**Fade**: Standard for most mature companies—industrials, utilities, consumer staples. Use a 20–30 year fade for stable, moderate-growth firms. Shorter (10–15 year) fades for cyclical or tech-exposed businesses.

**Reversion to book**: Best for commodity-like industries, turnaround situations, or any valuation where the forecast period reflects abnormally high returns. Also the safest choice when defending a valuation to skeptics.

A common hybrid approach is to apply a fade from year 10 to 30, then assume a stable but modest growth rate (1–2%) thereafter, splitting the difference between perpetuity optimism and reversion pessimism.

## Sensitivity and Stress Testing

Because terminal value dominates the valuation, always run three scenarios: base case (fade), bull case (perpetuity or long fade), and bear case (short fade or reversion). Document which assumption you chose and why. If a 5–10 year change in fade duration moves the valuation by >20%, the result is fragile and the story is weak.

The most credible valuations are those where terminal value makes sense *as a sanity check*—that is, the implied steady-state [return-on-equity](/return-on-equity/) or market share at year 30 passes the laugh test. If a fade model implies a mature tech company still earning 15% excess returns at year 25, the terminal value is still too optimistic, even if it appears conservative on paper.

## See also

<div class="wiki-seealso">

### Closely related

- [Discounted Cash Flow Valuation](/discounted-cash-flow-valuation/) — Core method using terminal value to estimate intrinsic value
- [Return on Equity](/return-on-equity/) — The excess spread (ROE minus cost of equity) that drives residual income
- [Cost of Equity](/cost-of-equity/) — Required return that defines what counts as "residual"
- Perpetuity Growth — Mathematical foundation for perpetuity terminal value formulas
- Book Value — The equity balance that grounds reversion-to-book terminal assumptions

### Wider context

- [Intrinsic Value](/intrinsic-value/) — The target valuation per share that terminal value components determine
- Competitive Advantage — How durable moats justify or deflate perpetuity assumptions
- [Fair Value](/fair-value/) — Standard for comparing model outputs to market price
- Valuation Methods — Alternative approaches beyond residual income models

</div>