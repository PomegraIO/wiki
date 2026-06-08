---
title: "RSU Double-Trigger Vesting and the Tax Event"
description: "How double-trigger RSUs delay the ordinary income tax event until a qualifying liquidity event, and why the timing matters for employees."
keywords:
  - double trigger RSU vesting
  - RSU liquidity event
  - tax event RSU
  - double trigger vesting
  - restricted stock units tax
image: /svg/equity.svg
---

*In a **double-trigger RSU** grant, the ordinary income tax event is deferred until both the vesting schedule is satisfied AND a qualifying liquidity event (typically acquisition, IPO, or change of control) occurs. This timing mismatch — vesting happening gradually while tax crystallization happens suddenly at exit — creates unique tax planning challenges and cash flow risks for employees holding unvested RSUs at the time of acquisition.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Double-Trigger RSUs — key facts</div>

<img src="/svg/equity.svg" alt="An abstract editorial mark for employee equity." />

<div class="wiki-infobox-caption">The tax event is delayed until vesting meets a liquidity trigger, creating exposure to both favorable and adverse timing.</div>

|   |   |
|---|---|
| **Vesting schedule** | Time-based (typically 4 years, 1-year cliff) |
| **Liquidity trigger** | IPO, acquisition, change of control, or similar event |
| **Tax event date** | When both vesting AND liquidity event occur |
| **Income type** | Ordinary income (taxed as wages) on FMV at tax event date |
| **Withholding** | Employer deducts share count or cash from proceeds |
| **Capital gains** | Appreciation from tax event date to sale date = long-term capital gain |
| **If no liquidity** | RSUs remain unvested and typically forfeit (no tax owed) |

</aside>

## Standard vs. double-trigger RSUs

Most RSU grants are **single-trigger**: the ordinary income tax event happens automatically when shares vest, regardless of company status. On vesting date, you owe ordinary income tax on the fair market value of the vested shares. If the company is private and illiquid, you owe the tax but cannot easily sell to pay it — a painful mismatch.

Double-trigger RSUs solve this problem by adding a second condition: taxation happens only when both vesting **and** a liquidity event occur. This is common in private company grants and acquisition packages, where employers want to defer the tax burden until employees can actually liquidate.

A typical grant might vest 25% per year over four years (annual tranches). Under a double-trigger structure:

- **Year 1:** 25% of shares vest but are not yet taxable. Employee owns the vested portion but cannot sell and owes no tax.
- **Year 2:** Another 25% vests. Still no tax event.
- **Year 3:** Another 25% vests. Still no tax event.
- **Year 4:** Final 25% vests. At this point, all 100% are vested.
- **Liquidity event (any time):** Once the company is acquired or goes public, the ordinary income tax event triggers on all vested shares, valued at the sale price (for acquisition) or IPO price (for public offering).

## Tax event timing and cash flow

The timing of the liquidity event relative to vesting heavily influences the employee's tax burden and cash flow.

**Scenario A: Liquidity event before full vesting**

You have a four-year vest; the company is acquired in year two. At acquisition, 50% of your shares are vested, 50% are not. The double-trigger is satisfied for the vested 50%, so you owe ordinary income tax on those shares at the acquisition price. The unvested 50% typically either (a) accelerates under single-trigger acceleration clauses (triggering tax immediately), (b) remains subject to time-based vesting in the acquirer (deferring the tax event further), or (c) is forfeited.

If the acquisition price is $50 per share and you have 50% vested, you owe ordinary income tax on $50 × 50% of your grant. If your marginal tax rate is 40% (federal + state + self-employment), your tax bill is 40% × (50% of your shares) × $50. Depending on your tax bracket, this can consume a meaningful portion of your gross proceeds.

**Scenario B: Liquidity event after full vesting**

All four years vest before the IPO or acquisition. When the liquidity event occurs, 100% of shares trigger the ordinary income tax event at the transaction price. Your tax bill is larger in absolute terms but was "earned" over time and is more predictable.

## Capital gains after the tax event

Once the ordinary income tax event crystallizes, any further appreciation is taxed as [capital gains](/capital-gains-tax-investor/). This matters when there is time between the liquidity event (acquisition valuation, IPO price) and your actual sale.

Example: You receive an RSU grant for 1,000 shares at a private company. The company vests your shares over four years and is acquired by a large tech firm at $60 per share in year three. At acquisition, 75% of your shares (750) are vested and trigger the ordinary income tax event at $60. You owe ordinary income tax on 750 × $60 = $45,000 FMV.

The acquirer locks up your shares for a standard six-month lockup period. During that six months, the acquirer's stock appreciates from $60 to $75. When lockup expires and you sell, the $15 per share gain (on 750 shares = $11,250) is long-term capital gain, taxed at preferential rates (typically 15% to 20% federally, depending on your income).

If the stock declined to $45 during the lockup, your $15 per share loss is a capital loss, usable to offset other capital gains or up to $3,000 of ordinary income per year.

## Withholding and net settlement

When the tax event occurs, your employer is required to withhold taxes. In a stock-for-stock acquisition, the buyer typically withholds shares to cover the employee's tax liability. In a cash merger, the acquirer withholds cash from the merger proceeds.

Example: You have 1,000 shares vesting at acquisition, with FMV of $60. Your ordinary income tax liability is $60,000 × 40% = $24,000. If the withholding rate is 40%, you receive 600 shares (1,000 × 60%) and the acquirer keeps 400 shares to remit as your tax withholding.

This is a net settlement: you do not receive all the shares upfront and then remit tax; the employer deducts it directly.

## The unvested trap at acquisition

A critical detail: if you have unvested shares at the time of acquisition and those shares do **not** accelerate, they continue to vest under the acquirer's rules. This creates several risks:

1. **Continued employment requirement:** Unvested shares may require you to stay employed by the acquirer. If you are laid off before they vest, those shares forfeit.
2. **New vesting clock:** The acquirer may reset the vesting clock or change the terms. A two-year vest remaining may become a three-year vest under the new employer.
3. **Deferred tax event:** If your unvested shares eventually vest under the acquirer and the stock has appreciated or depreciated, the tax event will reflect the new (often higher) price, increasing your tax bill.

For this reason, [equity](/equity-compensation-leaving-company/) packages in acquisitions often include accelerated vesting clauses — single-trigger acceleration (all unvested shares vest at close) or double-trigger with a change-of-control definition (vesting accelerates if you are terminated without cause within a set period post-acquisition, typically 12–24 months).

## Double-trigger vs. IPO reality

For companies planning a public offering, the double-trigger language often specifies that an IPO is a qualifying liquidity event. When the company goes public, all vested RSUs trigger ordinary income taxation at the IPO price.

A founder or early employee with a large grant may face an enormous single-day ordinary income tax bill. If you have 100,000 shares vesting at a $100 IPO price, your ordinary income is $10 million, and at a 40% effective rate (including federal, state, and potentially alternative minimum tax), you owe $4 million in taxes. The company typically registers your shares for resale, but the lockup period (usually 180 days for insiders) prevents immediate selling.

Many IPO employees rely on:

- Cashless exercises or secondary sales during lockup (if permitted).
- Loans against future share sales.
- Sale of non-restricted shares or other assets to cover the tax bill.
- Tax planning (e.g., charitable donations of appreciated shares, if available).

## If no liquidity event occurs

Double-trigger RSUs are only valuable if the liquidity event eventually happens. If the company remains private indefinitely, the shares never trigger taxation but also never become liquid. Employees hold appreciated but untradeable equity on their balance sheet indefinitely.

Some private companies attempt secondary sales (selling shares to new investors or secondary platforms), which may trigger a tax event depending on the RSU agreement. Others may repurchase shares at each financing round, allowing employees to take some gains off the table.

But in the absence of an exit or secondary market, double-trigger RSUs are speculative assets: significant upside potential paired with the risk of permanent illiquidity.

## See also

<div class="wiki-seealso">

### Closely related

- [Equity Compensation Leaving a Company](/equity-compensation-leaving-company/) — How unvested RSUs are treated at termination
- [Early Exercise and the 83(b) Election for Stock Options](/early-exercise-83b-election/) — Tax timing for stock options
- [NQSO vs ISO: Tax Treatment Compared](/nqso-vs-iso-tax-treatment/) — Comparing option and RSU tax frameworks
- Vesting — How grants earn out over time
- [Capital Gains Tax for Investors](/capital-gains-tax-investor/) — Long-term vs. short-term rates

### Wider context

- Ordinary Income vs Capital Gain — Tax rate differences
- [Restricted Stock Units](/restricted-stock-units/) — RSU grant mechanics
- Employee Stock Option — Alternative equity vehicle
- [Acquisition and Merger](/acquisition/) — Exit definitions
- [Initial Public Offering](/initial-public-offering/) — IPO as a liquidity event

</div>
