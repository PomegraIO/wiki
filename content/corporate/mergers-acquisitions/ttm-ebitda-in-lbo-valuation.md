---
title: "Trailing Twelve Month EBITDA in LBO Valuation"
description: "Why LBO models use trailing twelve-month EBITDA as the entry valuation base and how buyers calculate and adjust it."
keywords:
  - ttm ebitda lbo valuation
  - trailing twelve month ebitda
  - lbo entry multiple
  - leveraged buyout
  - ebitda normalization
  - lbo valuation
---

*In a **leveraged buyout (LBO)**, the buyer values the target company using **trailing twelve-month (TTM) EBITDA** as the starting point. TTM EBITDA is the past twelve months of earnings before interest, taxes, depreciation, and amortization—a measure of normalized cash-generating capacity. The buyer applies a multiple to TTM EBITDA to arrive at an entry valuation, then layers debt and equity to fund the deal.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">TTM EBITDA in LBO — key facts</div>

<img src="/svg/corporate.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">The denominator for calculating entry multiples and leverage ratios in leveraged buyout models.</div>

|   |   |
|---|---|
| **Definition** | Earnings (past 12 months) before interest, taxes, depreciation, amortization. |
| **Time window** | The most recent 12-month period, rolling or calendar-based. |
| **Why used in LBOs** | Reflects current earning power independent of accounting choices; covers a full business cycle. |
| **Entry multiple range** | Typically 4x to 8x TTM EBITDA, depending on industry and company quality. |
| **Typical debt capacity** | 3x to 5x TTM EBITDA, limiting the buyer's leverage based on cash flow. |
| **Adjustment for seasonality** | Buyers often annualize Q1–Q3 run-rate and compare to full prior-year EBITDA. |
| **Post-deal use** | EBITDA growth and leverage paydown are modeled forward to justify returns. |

</aside>

## Why TTM EBITDA, Not Forward?

An LBO sponsor faces a choice: value the company on **trailing EBITDA** (the past twelve months) or **forward EBITDA** (projected next twelve months). The sponsor almost always chooses trailing.

Trailing EBITDA is historical fact. The past year's earnings are audited (or at least reported) and hard to dispute. Forward EBITDA is forecast—dependent on management's projections, the sponsor's assumptions, and market conditions a year or more away. In a competitive auction for a company, buyers who base valuations on aggressive forward projections often overpay.

Moreover, debt capacity is pegged to trailing EBITDA. Lenders assess how much the target can borrow by dividing anticipated annual cash flow (often approximated as EBITDA) by the size of the loan. A buyer cannot justify $400 million in debt based on next year's hoped-for $100 million EBITDA; lenders want to see that the company already generates that cash. TTM EBITDA is proof.

## Calculating TTM EBITDA

The calculation is straightforward in principle but requires attention to timing.

**Most recent full-year EBITDA** is the starting point. If the buyer is closing the deal in June, the most recent full fiscal year (ending December 31 of the prior year) is known: say, $100 million. That is not quite TTM; it is the "LTM" (last twelve months of the prior full year).

To get true **trailing twelve months**, the buyer adds the current year's year-to-date EBITDA (January through May, if closing in June) and subtracts the same period from the prior year. The formula:

```
TTM EBITDA = 
  LTM EBITDA 
  + (Current YTD EBITDA) 
  - (Prior-year YTD EBITDA for same period)
```

**Example:**

- Prior full-year EBITDA (Jan–Dec prior year): $100M
- Current YTD EBITDA (Jan–May current year): $42M
- Prior-year YTD EBITDA (Jan–May prior year): $40M
- **TTM EBITDA = $100M + $42M − $40M = $102M**

This strips out seasonality and gives a forward-looking snapshot of the annual run-rate.

## Adjustments Buyers Commonly Make

Raw TTM EBITDA is rarely the final number used in an LBO model. Sponsors adjust for one-time items and cost savings.

**Add-backs for non-recurring items.** Did the company pay for a litigation settlement or a one-time restructuring in the past twelve months? Buyers add those costs back—arguing they will not recur post-acquisition. The logic: if TTM EBITDA includes a $10M expense that is truly one-time, the normalized earning power is $10M higher. Lenders often scrutinize these add-backs; if the sponsor claims $15M in one-time costs but lenders believe only $5M is truly non-recurring, the justified debt capacity shrinks.

**Normalization for unusual volumes or pricing.** If the target benefited from an exceptional pricing environment or a surge in customer demand in the past year, the sponsor may normalize EBITDA downward. Conversely, if the past year was depressed (recession, strike, supply chain disruption), the sponsor can argue for normalizing upward. This is highly subjective and often the source of tension between buyer and seller.

**Cost synergies.** In a [leveraged buyout](/leveraged-buyout/), the buyer may have identified ways to cut costs—consolidating back-office functions, eliminating redundancies, renegotiating supplier contracts. These "run-rate synergies" are added to EBITDA to calculate "synergy-adjusted EBITDA" or "pro-forma EBITDA." Lenders may allow the sponsor to include some synergies in debt calculations if the buyer has a credible plan, but conservative lenders stick to TTM EBITDA as-is.

## Entry Multiple and Entry Enterprise Value

Once TTM EBITDA is established, the buyer applies a multiple to derive the **entry enterprise value**.

**Entry EV = TTM EBITDA × Entry Multiple**

The entry multiple reflects:
- **Industry and company quality.** A growing, best-in-class company might command a 7–8x multiple. A mature, cyclical business might trade at 4–5x.
- **Market conditions.** In boom periods, multiples expand. In recessions, they compress.
- **Financing cost.** The lower the cost of debt, the more a sponsor can pay (higher multiple) and still meet return targets.
- **Competitive bid pressure.** In an auction, multiples are driven up by rival bidders.

A sponsor targeting a company with $100M in TTM EBITDA and acquiring it at a 6.5x multiple pays an entry enterprise value of $650M.

## Leverage Ratios and Debt Sizing

The entry enterprise value is split between **debt** and **equity**. A typical LBO is financed ~60% debt and ~40% equity (though this varies widely).

Lenders assess the loan size by reference to a **leverage ratio**: how many times annual EBITDA the debt represents.

**Leverage Ratio = Total Debt / TTM EBITDA**

If the company has $100M in TTM EBITDA and the sponsor wants to borrow at a 4.5x leverage ratio, the target can support $450M in debt. If entry enterprise value is $650M and the sponsor borrows $450M, the equity check is $200M.

Lenders typically cap leverage at 4.5x to 5.5x depending on the industry, with stronger companies and stable cash flows justifying higher multiples. A company with volatile EBITDA or high capital intensity may be capped at 3.5x.

## From Entry to Exit: The LBO Model's Arc

An LBO model projects forward and assumes EBITDA will grow over a 5–7 year holding period. The sponsor uses the model to forecast returns.

| Year | TTM EBITDA | Exit Multiple | Exit Enterprise Value | Debt Remaining | Equity Value | MOIC |
|---|---|---|---|---|---|---|
| 0 (Entry) | $100M | 6.5x | $650M | $450M | $200M | — |
| 5 (Exit) | $150M | 7.0x | $1,050M | $350M | $700M | 3.5x |

The sponsor entered at $200M in equity and exits at $700M, a 3.5x multiple on invested capital (MOIC)—a strong return for five years of risk.

This model is built on assumptions: EBITDA growth, exit multiple, debt paydown. Entry EBITDA (TTM) is the anchor; if it is overstated, the entire model unravels. Debt capacity is blown; the company cannot support the financing. Returns are compromised.

This is why buyers and lenders scrutinize TTM EBITDA so carefully. Understating it is safer but lowers the entry price. Overstating it allows a higher bid but invites default risk. The tension is constant in LBO negotiations.

## Variations Across Industries

**Cyclical businesses** (mining, construction, automotive). Sponsors often adjust TTM EBITDA down if the company is in a cyclical peak. Lenders may use a normalized EBITDA figure based on mid-cycle assumptions.

**Seasonal businesses** (retail, agriculture). TTM EBITDA captures the seasonal pattern, which is appropriate. However, the buyer and lender may discuss whether the upcoming year is expected to be similar or abnormal.

**Growth companies.** Young, fast-growing firms may have minimal EBITDA but strong revenue growth. Lenders typically insist on strong EBITDA or high-margin revenue to support debt. If TTM EBITDA is near zero, leverage is capped near zero—the deal is mostly equity-financed.

**Consolidated roll-ups.** A sponsor acquiring multiple small companies and consolidating them under one roof will sum the TTM EBITDA of each acquired company to create a pro-forma TTM figure. This is the baseline for leverage and valuation.

## See also

<div class="wiki-seealso">

### Closely related

- [Leveraged buyout](/leveraged-buyout/) — the LBO structure in which TTM EBITDA plays a central role
- [EBITDA](/ebitda/) — definition and uses across valuation
- [Enterprise value](/enterprise-value/) — the valuation metric being sized by TTM EBITDA × multiple
- [Debt-to-EBITDA ratio](/debt-to-ebitda-ratio/) — leverage metric grounded in TTM EBITDA
- [Discounted cash flow valuation](/discounted-cash-flow-valuation/) — alternative valuation method sometimes used to check LBO entry prices

### Wider context

- [Merger](/merger/) — the transaction context in which LBOs often occur
- [Acquisition](/acquisition/) — buyer perspective on target valuation
- [Private equity fund](/private-equity-fund/) — sponsor type that executes LBOs
- [Due diligence](/due-diligence/) — the process by which EBITDA is verified and adjusted

</div>
