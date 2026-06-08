---
title: "First Chicago Method"
description: "A scenario-weighted valuation approach that blends optimistic, base, and pessimistic outcomes to estimate startup enterprise value."
keywords:
  - startup valuation
  - scenario analysis
  - probability-weighted valuation
  - venture capital
  - private company appraisal
image: "/svg/valuation.svg"
---

*The **First Chicago Method** is a probabilistic valuation framework that synthesizes three distinct scenarios—an upside case, a base case, and a downside or failure case—then weights each by its perceived likelihood to arrive at a single present value. Widely used by early-stage investors and founders, it acknowledges that private company forecasts are inherently uncertain by making that uncertainty explicit.*

## Why scenarios beat single forecasts

Most investors know their startups might succeed spectacularly, stumble along a middle path, or implode. Traditional methods often handle this by applying a blanket risk discount to earnings, but that obscures the actual range of outcomes. The First Chicago Method instead forces the analyst to articulate three distinct futures: what happens if everything goes right, what if market growth matches expectations, what if the company hits trouble. By assigning a probability to each and calculating its value independently, the method clarifies which scenarios drive most of the risk—and where a business plan is weakest.

The term itself references a valuation conference held in Chicago in the 1980s where venture investors formalized this three-scenario framework as a best practice. It has since become a mainstay of [private equity](private-equity-fund) due diligence and [venture capital](venture-capital) investment memos.

<aside class="wiki-infobox">

<div class="wiki-infobox-title">First Chicago Method — key facts</div>

<img src="/svg/valuation.svg" alt="An abstract editorial mark for valuation methodology." />

<div class="wiki-infobox-caption">Scenario-weighted DCF assigns probabilities to upside, base, and downside outcomes.</div>

|   |   |
|---|---|
| **What it is** | Probability-weighted blend of three separately modelled valuation scenarios |
| **Also called** | Scenario analysis, three-way valuation, probability-weighted DCF |
| **When used** | Early-stage private companies, venture investments, turnarounds |
| **Key input** | Discrete forecasts for revenue, margin, and exit multiple in each scenario |
| **Formula** | (Upside × P_up) + (Base × P_base) + (Downside × P_down) |
| **Discount rate** | Often risk-free rate plus venture premium, consistent across scenarios |
| **Output** | Single enterprise value in today's dollars |

</aside>

## Building the three cases

Each scenario requires its own financial model. The analyst projects revenue, expenses, cash flow, and ultimately a terminal value or exit price, then discounts that to present value at a single [discount rate](discount-rate) (usually 30–50% for early-stage companies to reflect risk).

The **upside case** assumes the company captures its target market, achieves pricing power, reaches profitability ahead of plan, and exits at a premium [multiple](price-to-earnings-ratio). Revenue might grow 50%+ annually, operating margins might exceed initial guidance, and the company might be acquired at a 3x or 4x [revenue multiple](price-to-sales-ratio). This case might be assigned a 10–20% probability.

The **base case** reflects the business plan as presented: normal market adoption, competitive pricing, margins inline with industry norms, and a modest [exit multiple](enterprise-value). Revenue grows as forecast, the company reaches sustainable profitability, and the multiple is conservative. This might represent 50–70% of the probability mass.

The **downside case** models failure paths: slower adoption, pricing compression, inability to control costs, or a fire-sale exit at 1x revenue or lower. The company might be acquired cheaply or liquidated for asset value. Some analysts assign this case 10–30% probability, though for very early-stage bets the failure case can be the most likely outcome.

## The weighting question

The mechanics are straightforward: multiply each scenario's present value by its probability, then sum. Yet practitioners disagree sharply on those probabilities. Some argue that early-stage venture bets fail 90% of the time, warranting 90% weight on the downside. Others claim such extremes compress valuations unreasonably and prefer a more balanced 20/60/20 split. The choice reflects the investor's prior beliefs about the business and the market.

A common trap is letting base-case probability equal the sum of upside and downside—that is, 60% for base and 40% split between upside and down. This is not wrong, but it can mask disagreement about whether the downside is "company fails entirely" (10% residual value) or "company succeeds but at lower multiples" (30–40% of base-case value). Clarity here moves the dial significantly.

## Sensitivity and the limits of precision

The method's greatest strength—explicit probability and scenario thinking—is also its weakness: these probabilities are not observable. An investor cannot know in advance whether a scenario will have 15% or 25% odds. As a result, valuations are often run across a range of probability assumptions, or sensitivity is tested by pivoting one or two key parameters (e.g., "what if the exit multiple is 2x instead of 3x?").

The First Chicago Method also assumes the discount rate is constant across scenarios. In reality, an upside scenario might carry lower residual risk (because success de-risks the business), yet changing the discount rate per scenario muddies the analysis and invites second-guessing. Most practitioners therefore hold discount rate fixed and let scenario differences show through cash flows alone.

## Comparing to alternatives

The [guideline public company method](guideline-public-company-method) leans on observable market multiples and applies adjustments for size and control; it works best for established privates with comparables. The [excess earnings method](excess-earnings-method) segregates tangible and intangible asset returns; it suits companies with significant fixed assets. The [capitalization of earnings method](capitalization-of-earnings-method) applies a single cap rate to normalized earnings; it is simple but assumes the company will sustain earnings in perpetuity. First Chicago is most useful when the future is genuinely uncertain and the analyst believes different paths are plausible and deserve explicit modeling.

## See also

<div class="wiki-seealso">

### Closely related

- [Excess Earnings Method](/excess-earnings-method/) — Separately values tangible assets and capitalized intangible earnings.
- [Capitalization of Earnings Method](/capitalization-of-earnings-method/) — Applies a cap rate to normalized earnings for steady-state businesses.
- [Guideline Public Company Method](/guideline-public-company-method/) — Derives value from public-market multiples with private-company adjustments.
- [Discounted Cash Flow Valuation](/discounted-cash-flow-valuation/) — Foundational technique; First Chicago builds three DCF scenarios.
- [Enterprise Value](/enterprise-value/) — The sum of equity and debt value being estimated in all three scenarios.

### Wider context

- [Private Equity Fund](/private-equity-fund/) — Uses scenario analysis in deal underwriting.
- Venture Capital — Early-stage investors routinely employ First Chicago for term-sheet valuations.
- [Alternative Trading System](/alternative-trading-system/) — Secondary markets where startup equity trades at derived valuations.
- Risk Assessment — Probability assignment is inherently subjective; best practice is sensitivity testing.
- [Return on Invested Capital](/return-on-invested-capital/) — Guides the discount rate and base-case margin assumptions.

</div>
