---
title: "Form 8606 and the Pro-Rata Rule in a Backdoor Roth"
description: "Form 8606 calculates the taxable portion of a backdoor Roth when pre-tax IRA money exists, applying the pro-rata rule across all traditional IRAs."
keywords:
  - form 8606 backdoor roth pro-rata rule
  - form 8606
  - backdoor roth
  - pro-rata rule
  - nondeductible contribution
image: /svg/taxes.svg
---

*When you do a backdoor [Roth](/roth-ira/) conversion, **Form 8606** and the **pro-rata rule** determine how much is taxable. If you have pre-tax money in a [traditional IRA](/traditional-ira/), the IRS treats all your IRAs as one pool; you cannot cherry-pick the nondeductible contribution to convert. Part of your conversion is taxed as ordinary income.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Form 8606 and the Pro-Rata Rule — key facts</div>

<img src="/svg/taxes.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Filing and tax math when existing pre-tax IRAs block a tax-free backdoor Roth.</div>

|   |   |
|---|---|
| **Form section** | Part I: nondeductible contributions and IRD; Part II: conversion math; Part III: distribution basis |
| **Pro-rata rule** | All IRAs (traditional, SEP, SIMPLE) aggregate for tax calc; cannot isolate Roth conversion |
| **Taxable portion** | (Pre-tax balance / total IRA balance) × conversion amount |
| **Timing** | Form 8606 filed with 1040; conversion reported on IRS Form 8949 |
| **State tax** | Conversions are federally taxable; some states also tax the conversion |
| **Key variable** | Pre-tax IRA balance as of 12/31 of conversion year (year-end snapshot) |
| **Backdoor eligibility** | Income limits block direct Roth contributions; backdoor has no income limit |

</aside>

## The backdoor Roth in three steps

1. **Nondeductible contribution:** You contribute $7,000 (or $8,000 if age 50+) to a traditional IRA. You do not deduct it on your taxes; you file Form 8606 Part I to report it as basis.

2. **Conversion:** Weeks or months later, you convert that entire $7,000 traditional IRA balance to a Roth IRA.

3. **Tax treatment:** If you have no other pre-tax IRA money, the conversion is tax-free (you already paid tax on the $7,000 contribution). But if you have pre-tax IRA balances—a [SEP-IRA](/), a [rollover IRA](/), or another traditional IRA—the pro-rata rule applies, and part of the conversion becomes taxable.

## What is the pro-rata rule?

The **pro-rata rule** is an IRS rule that prevents cherry-picking. The IRS does not allow you to say, "I'll convert only my nondeductible $7,000 contribution; I'll leave my pre-tax money alone." Instead, it treats all your IRAs as one big account for tax purposes.

**The calculation:**

<pre>
Taxable portion = (Total pre-tax balance / Total IRA balance) × Conversion amount

where:
- Total pre-tax balance = all traditional, SEP, and SIMPLE IRA balances at year-end
- Total IRA balance = pre-tax balance + nondeductible basis + earnings on nondeductible
- Conversion amount = the money you are converting to Roth in that year
</pre>

## Example: the pro-rata rule in action

**Scenario:** You have $100,000 in a traditional IRA (pre-tax) from a prior rollover. You contribute $7,000 nondeductible to a separate traditional IRA. A month later, you convert the $7,000 to a Roth.

Your total IRA balances at year-end:
- Traditional IRA (rollover): $100,000 pre-tax
- Traditional IRA (new): $7,000 nondeductible

Total IRA balance = $107,000
Pre-tax portion = $100,000
Nondeductible basis = $7,000
Conversion amount = $7,000

Pro-rata calculation:
Taxable = ($100,000 / $107,000) × $7,000 = 0.9346 × $7,000 = $6,542

Result: Of the $7,000 converted, $6,542 is taxable as ordinary income in the year of conversion. Only $458 is tax-free (your nondeductible basis proportion). Your Roth now holds $7,000; your tax bill is higher by roughly $1,700 (at 25% [marginal tax rate](/marginal-tax-rate-investor/)).

## Form 8606 Part I: reporting the nondeductible contribution

You file Form 8606 Part I in the year you make a nondeductible contribution (even if you do not convert that year).

**Part I captures:**
- Line 1: Traditional IRA contributions made during the year
- Line 2: Contributions you deducted (if any)
- Line 3: Nondeductible contributions (the difference)
- Line 4: Your basis (cumulative nondeductible contributions, not yet converted)
- Line 5: Conversions or distributions of traditional IRA money during the year
- Line 7: Ending basis for next year

Part I builds a running total of your nondeductible basis across all years. If you contributed $7,000 nondeductible in Year 1 and $7,000 in Year 2, your cumulative basis is $14,000.

## Form 8606 Part II: converting to Roth

Part II calculates the taxable portion of a conversion using the pro-rata rule.

**Part II asks:**
- Conversion amount: $7,000 (or however much you converted)
- Total pre-tax IRA balance at year-end
- Total nondeductible basis at year-end
- Total of all IRA balances

The form then computes:
Taxable conversion = (Pre-tax balance / Total IRA balance) × Conversion amount

This is the key line: it determines how much of your conversion is taxed as ordinary income.

## Year-end valuation: the critical snapshot

The pro-rata rule uses **year-end balances** (December 31 of the conversion year). This is important:

- If your IRA balances grow during the year (market gains), the denominator grows, and the pro-rata fraction shrinks—less is taxable.
- If your IRA balances fall (market losses), the denominator shrinks, and the pro-rata fraction grows—more is taxable.
- You cannot time the conversion to avoid a market downturn in your IRA balances; the rule applies to the 12/31 snapshot regardless.

Example: Your rollover IRA had $100k at Jan 1. By July (conversion month), it has grown to $110k. You convert $7,000 that month. But 12/31, the account is back at $105k. The pro-rata rule uses $105k, not $110k, because that is the year-end balance. This can increase the tax cost if the account recovered late in the year.

## Cannot avoid with partial conversions

A common question: "If I convert only half of my nondeductible contribution, will the pro-rata rule apply to just that half?"

**Answer: No.** The pro-rata rule aggregates all IRAs for the year. If you have $100k pre-tax and $7k nondeductible, converting $3,500 of the nondeductible IRA triggers pro-rata:

Taxable = ($100k / $107k) × $3,500 = $3,271

You cannot isolate or "protect" the nondeductible portion; the rule spreads the tax across all conversions in the calendar year.

**Workaround:** Some use the "same-year deduction" strategy—deducting the nondeductible contribution on the same return to immediately reduce taxable income. But this is rare and requires specific circumstances.

## Interaction with rollovers

If you have a [Simplified Employee Pension (SEP) IRA](/sep-ira/) or [SIMPLE IRA](/simple-ira/) in addition to traditional IRAs, they all count toward the pro-rata pool. A $100k SEP-IRA plus a $7k traditional IRA contribution triggers the same pro-rata rule.

If you have old employer [401(k)](/401k-plan/) balances and you have not rolled them into your IRA, they do **not** count toward the pro-rata rule. But if you roll them over to a traditional IRA *before* or *during* the year of conversion, they immediately become part of the pool and worsen your pro-rata position.

Strategy: Some execute rollovers of pre-tax workplace plans *after* the calendar year ends (but before the return deadline) to keep those balances out of the prior year's pro-rata calculation. Consult a tax advisor to confirm current rules.

## Reporting on the 1040 and Schedule 1

The amount you owe on the backdoor Roth conversion is reported as ordinary income on your 1040 or Schedule 1 (Form 1040, Schedule 1, Part I, line 4). It is added to your other income for the year.

State income taxes also apply in most states that have income tax. Some states (like Pennsylvania) do not tax retirement income, including Roth conversions, but federal taxes always apply.

## Record-keeping over many years

If you plan a series of backdoor Roths, track your cumulative nondeductible basis on Form 8606 Part I, line 4. Your basis carries forward year after year. If you contributed $7,000 nondeductible for 5 years, your basis is $35,000. In year 6, if you convert any traditional IRA money, the pro-rata rule uses the full $35,000 in the numerator.

## Example: multi-year backdoor

**Year 1:** Contribute $7,000 nondeductible → Basis $7,000 → Convert immediately → Pro-rata with other pre-tax IRAs (if any).

**Year 2:** Contribute $7,000 nondeductible → Basis now $14,000 → Convert immediately → Pro-rata applies again.

**Year 3:** Contribute $7,000 nondeductible → Basis now $21,000 → Convert immediately → Pro-rata applies again.

By year 3, your nondeductible basis is $21,000, but every conversion triggers pro-rata against your entire pre-tax IRA pool. The basis does not shield you; it only tracks how much of your cost basis is nondeductible.

## Common mistake: "stacking" conversions in one year

A mistake: converting large pre-tax IRA balances to Roth in the same calendar year as your nondeductible contribution. This pushes you into a higher [tax bracket](/tax-bracket-investor/) and worsens the pro-rata tax hit.

Example: You normally earn $150k. You contribute $7k nondeductible and also convert $50k pre-tax IRA to Roth, all in the same year. The pro-rata rule applies to that $50k conversion, and the entire conversion is reported as income, pushing you into a much higher bracket and increasing overall tax. Better to spread conversions across years or wait until you have more nondeductible basis to dilute the pro-rata ratio.

## Form 8606 Part III: distributions from Roth

Part III is used only if you take distributions from a Roth IRA before age 59½. It calculates how much of your distribution is earnings (taxable/subject to penalty) vs. basis (tax-free). Most backdoor Roth users never file Part III unless they need early access.

## See also

<div class="wiki-seealso">

### Closely related

- [Roth IRA](/roth-ira/) — the destination account; tax-free growth and withdrawals
- [Traditional IRA](/traditional-ira/) — the source account for backdoor conversions; pre-tax contributions
- [Backdoor Roth](//) — the technique using nondeductible contributions and conversions
- [Marginal Tax Rate](/marginal-tax-rate-investor/) — determines the cost of the taxable conversion
- [SEP-IRA](//) — Simplified Employee Pension; counts toward pro-rata
- [401(k) Plan](/401k-plan/) — rollovers to IRA trigger pro-rata if executed before year-end

### Wider context

- [Tax Bracket](/tax-bracket-investor/) — income from conversions can push you into higher brackets
- [Ordinary Income](//) — conversions are taxed as ordinary income, not capital gains
- [Cost Basis](/cost-basis/) — Form 8606 tracks the tax-free portion of IRA distributions
- [Qualified Dividend](/qualified-dividend/) — unlike conversion income, some portfolio income gets favorable rates
- [Tax-Loss Harvesting](/tax-loss-harvesting/) — a different strategy to manage tax liability

</div>
