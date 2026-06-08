---
title: "409A Valuation Explained for Startup Employees"
description: "409A valuation explained: what it is, why startups must refresh it, how it affects stock option strike prices, and the tax consequences of non-compliance."
keywords:
  - 409a valuation explained for startup employees
  - stock option strike price
  - startup equity
  - 409a valuation requirement
  - iso non-qualified options
image: /svg/valuation.svg
---

*A **409A valuation** is an independent estimate of a private company's fair market value, required for tax purposes. It determines the strike price of employee stock options: if the 409A is $10/share and you receive options at $3/share, the IRS treats that spread as taxable income. Startups must refresh their 409A annually (or after major events) to stay compliant. Get it wrong—or skip it—and both the company and employees face penalties, including accelerated tax on deferred equity compensation.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">409A Valuation — Key Facts</div>

<img src="/svg/valuation.svg" alt="An abstract editorial mark for valuation." />

<div class="wiki-infobox-caption">IRS rules that lock in the tax basis for private equity.</div>

|   |   |
|---|---|
| **What it is** | Fair market value of company stock as determined by a qualified appraiser |
| **Legal name** | IRC Section 409A valuation |
| **Why it matters** | Sets the strike price floor for non-qualified and ISO options |
| **Refresh frequency** | Annually; also after seed/Series round, significant milestones |
| **Cost** | $2,000–$8,000 per valuation depending on company complexity |
| **Timing** | Must be completed within 120 days of the valuation date (or no safe harbor) |
| **Non-compliance risk** | Immediate [income](/income-statement/) inclusion, penalties, back taxes on all optionees |
| **Appraisers** | Big Four (Deloitte, PwC, EY, KPMG) or boutique valuation firms |

</aside>

## Why 409A Valuations Exist

The IRS created Section 409A valuation rules to prevent tax avoidance. Without independent valuations, a startup could tell employees their stock is worth $1/share while insiders knew it was $50/share, allowing employees to buy deep in-the-money options without immediate tax liability. Once the company exits, that spread would be taxed as a long-term capital gain rather than ordinary income.

A 409A valuation closes that loophole by requiring an independent third-party appraisal to set "fair market value," which becomes the baseline for option strikes. If the 409A says the stock is worth $20/share, you cannot grant options at $5/share without creating immediate [Section 409A](/409a-valuation-explained-startup-employees/) income tax issues.

## The Strike Price Connection

The relationship between 409A and strike price is direct:

**If 409A Fair Market Value = $20/share, and you grant options at:**
- $20/share (at-the-money): No tax consequence at grant; tax on spread only upon exercise or sale
- $15/share (in-the-money): $5/share × shares granted = immediate ordinary income tax
- $25/share (out-of-the-money): Technically violates safe harbor (though some argue discounts are defensible)

The safe harbor is that options must be granted at or above fair market value on the grant date. Grants below FMV are treated as bonus compensation and trigger immediate [income](/income-statement/) tax for the employee—even if they never exercise. This is a major problem for employees: they owe tax now, without selling a share.

## The 120-Day Safe Harbor

The IRS affords a 120-day safe harbor: if a 409A is completed within 120 days of the valuation date, the valuation is deemed reasonable for tax purposes. A valuation dated January 1 must be completed by April 30 to qualify.

If you miss the 120-day window, the valuation loses its safe harbor status. The IRS can challenge it in an audit, potentially reclassing the strike price and creating back-tax liability for employees. Startups take the 120-day deadline seriously; missing it is a material compliance failure.

## When a 409A Must Be Updated

A startup should commission a fresh 409A:

1. **Annually**: Standard practice; valuations are typically valid for one year.
2. **After a financing round**: A seed round, Series A, or Series B dramatically shifts valuation. A new 409A after each round resets the fair market value baseline.
3. **Significant business changes**: New major customer, major contract loss, significant pivot, major liability or lawsuit.
4. **Option refresh grants**: If a company does an option refresh (repricing existing options), a new 409A is prudent to justify the new strike.
5. **Near-exit scenarios**: If a company is in M&A conversations or heading toward IPO, a recent 409A supports the exit pricing.

Skipping a 409A update is risky. If the company raises Series B at a $100M valuation but the last 409A was at $30M (six months old), the IRS may argue the strike prices were unreasonably low, triggering employee tax exposure after the deal.

## How 409A Valuations Are Calculated

An independent appraiser uses one or more methods:

**Income approach**: Forecast future cash flows, discount to present value.  
**Market approach**: Compare to comparable company public multiples or recent private sales.  
**Cost approach**: Assess tangible and intangible assets; less common for software/tech.  

For early-stage startups (pre-revenue or low revenue), the cost or market approach is typical. The appraiser might benchmark against recent seed/Series A rounds. For growth-stage companies with revenue, the income approach (DCF) dominates.

The output is a single "fair market value per share" and, often, a detailed methodology memo that explains how the appraiser arrived at the number. A larger company with preferred shares (from VCs) might have multiple valuations: one for common stock, one for preferred. The common stock valuation is what applies to employee options.

## The Illiquidity Discount

A key component of 409A methodology is the **illiquidity discount**, which reduces the valuation to reflect that private shares cannot be sold immediately. While VC-backed preferred shares are partially liquid (investors can exit in future rounds), common employee shares are fully illiquid until an exit.

Appraisers often apply a 25–40% illiquidity discount to common stock, even if the company is valued at $1B on a VC round. This means employee options have an intrinsic value well below what VCs are paying for preferred equity. A company valued at $1B Series C at $100/share for Series C preferred might be valued at $40–60/share for common stock, accounting for illiquidity.

This is intentional: it reflects reality. Employee options are riskier and less marketable than VC preferred, so they should be cheaper.

## Tax Consequences of 409A Violations

If a 409A is done wrong or missing, the penalties are severe:

1. **Immediate income inclusion**: Employees must recognize ordinary income equal to the excess of FMV over the strike at the time the 409A violation is discovered. If you were granted options at $5/share and the "true" FMV was $20/share, you owe tax on $15/share × your shares *now*, even if you haven't exercised.

2. **20% penalty**: Plus a 20% accuracy-related penalty on the underpaid taxes.

3. **Interest**: Back-interest accrues from the grant date.

4. **Personal liability for optionees**: The employee bears the tax hit, not the company (though often a company will indemnify, creating legal conflict).

Example: You were granted 10,000 options at $3/share in 2021. The valuation should have been $15/share. In 2023, an audit discovers the error. You owe tax on (15 - 3) × 10,000 = $120,000 of ordinary income, plus penalties and interest. If your marginal rate is 40%, you now owe ~$60,000+ in back taxes for an equity grant you may not have even exercised.

This is why careful 409A compliance is critical, especially as a company scales.

## Preferred vs Common Stock Valuations

A later-stage startup often has two 409A valuations:
- **Preferred stock**: What VCs paid in the most recent round (based on the round valuation).
- **Common stock**: What employee options are worth (usually 40–60% of preferred, accounting for preference rights and illiquidity).

The IRS requires that employee options be granted at or above the common stock valuation, not the preferred valuation. A company that grants options at the preferred valuation is artificially deflating the strike, which the IRS will challenge.

Some founders try to argue that common and preferred are equivalent, but appraisers and tax counsel reject this. Preferred shares have liquidation preferences, conversion rights, and investor protection; common shares do not.

## Practical Considerations for Employees

If you are joining a startup and receiving options:

1. **Ask for the 409A report**: Review the per-share valuation and the refresh date. A 409A from two years ago is not current.
2. **Compare strike to FMV**: Your grant strike should be at or above the 409A FMV to avoid immediate tax. If it is below, clarify in writing why (and expect complications).
3. **Track the valuation over time**: Each year the company should update the 409A. If it jumps 5x one year, your next grant will be at a much higher strike, reducing near-term in-the-money value.
4. **Plan for taxes**: When you exercise, you will owe tax on the spread. Have the cash. Negotiate secondary sales (partial liquidity events) if the company offers.

## Startups' 409A Checklist

- Commission initial 409A within 120 days of founding or first financing.
- Update annually, at minimum.
- Update within 30 days of each funding round.
- Maintain the appraisal report and methodology memo for audit defense.
- Use the 409A FMV as the strike price floor for all option grants.
- Communicate the valuation transparently to employees (avoid surprises).
- Review the appraisal method: does it make sense for your stage?

## See also

<div class="wiki-seealso">

### Closely related

- Stock Option — The equity instrument whose strike is set by 409A
- [Equity Compensation](/equity-compensation/) — Broader context for employee stock grants
- [Fair Value](/fair-value/) — The FMV concept underlying 409A
- [Tax Loss Harvesting](/tax-loss-harvesting/) — How option exercises interact with capital gains tax
- [Discounted Cash Flow Valuation](/discounted-cash-flow-valuation/) — Appraisal method used in 409A income approach

### Wider context

- [Private Equity Fund](/private-equity-fund/) — VCs and their valuations drive 409A indirectly
- [Acquisition](/acquisition/) — Exit events that reset employee equity value
- [Initial Public Offering](/initial-public-offering/) — IPO removes illiquidity; 409A no longer applies post-IPO
- [Cost Basis](/cost-basis/) — Strike price becomes your basis for tax purposes

</div>