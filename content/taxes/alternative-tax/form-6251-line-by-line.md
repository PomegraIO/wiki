---
title: "IRS Form 6251 Line-by-Line Walkthrough"
description: "A plain-English explanation of each section of Form 6251, the Alternative Minimum Tax Computation form, so taxpayers understand what each adjustment represents."
keywords:
  - form 6251 line by line instructions
  - form 6251 amt calculation
  - alternative minimum tax form 6251
  - amt adjustments form 6251
  - how to fill out form 6251
image: /svg/taxes.svg
---

*[Form 6251](/form-6251-line-by-line/) is the IRS form used to calculate whether you owe the **alternative minimum tax (AMT)** and, if so, how much. Each section and line-item adjustment represents a specific deduction disallowance or preference that the AMT does not permit. Understanding what each line measures — and why — turns what looks like a worksheet into a logical flow: regular taxable income → deduction adjustments → preference items → alternative minimum taxable income → AMT tax → comparison with regular tax → amount owed.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Form 6251 Sections — key facts</div>

<img src="/svg/taxes.svg" alt="An abstract editorial mark for tax topics." />

<div class="wiki-infobox-caption">The form calculates AMTI, applies the AMT rate, and compares the result to regular tax.</div>

|   |   |
|---|---|
| **Part I** | Starting point and deduction adjustments |
| **Part II** | Preferences that inflate AMTI |
| **Part III** | Additional adjustments based on itemized deductions |
| **Line 1** | Modified Taxable Income (starting point from Form 1040) |
| **Lines 2–11** | Depreciation, Section 179, passive losses, interest, miscellaneous adjustments |
| **Lines 12–17** | Tax preferences (accelerated depreciation, tax-exempt interest, oil/gas, etc.) |
| **Lines 18–27** | Deduction adjustments (state taxes, miscellaneous items, home-equity interest) |
| **Line 28** | Alternative Minimum Taxable Income (AMTI) |
| **Line 29** | AMT exemption amount (indexed annually; phase-out begins at higher income levels) |

</aside>

## Part I: Adjustments Based on Income

### Line 1: Modified Taxable Income

This line begins with your **taxable income** from [Form 1040](/form-6251-line-by-line/). It is not your gross income; it is your taxable income after all regular deductions, both above-the-line (e.g., IRA contributions, business losses) and itemized or standard deductions.

The word "modified" is important: it is your regular taxable income, but the form will then add back or remove certain items specific to AMT.

### Lines 2–6: Depreciation Adjustment

These lines reconcile the difference between depreciation claimed on your regular tax return (using accelerated methods like MACRS) and the straight-line depreciation allowed for AMT purposes.

**Line 2** typically shows depreciation on personal property (vehicles, equipment) using regular-tax methods.

**Line 3** shows the straight-line depreciation that would have been allowed under AMT.

**Line 4** is the difference: if accelerated depreciation exceeded straight-line, this is a **positive adjustment** (added to AMTI). If straight-line exceeded accelerated (unusual in early years), this is negative and reduces AMTI.

**Line 5** handles depreciation on real property (buildings, rental homes). Residential and commercial property generally use straight-line depreciation even for regular tax, so there is often no line-5 adjustment. However, if you claimed bonus depreciation or recovered property on a shorter schedule, an adjustment appears here.

**Line 6** accumulates all depreciation adjustments from prior years, ensuring that the "catch-up" depreciation (where AMT eventually allows more than regular tax) is properly reflected.

### Line 7: Section 179 Deduction Adjustment

If you claimed a **[Section 179](/section-179-deduction/) deduction** on [Schedule C](/form-6251-line-by-line/) (self-employed) or elsewhere, that deduction is **not allowed** for AMT purposes. Instead, the property must be depreciated.

Line 7 asks: What [Section 179](/section-179-deduction/) deduction did you claim for regular tax? That amount is entered here as a positive adjustment. In subsequent years, as the property is depreciated under AMT rules, you gradually recover the deduction (through depreciation), and later-year line-7 entries may be smaller or negative.

**Example:** You claimed a $100,000 [Section 179](/section-179-deduction/) deduction in 2024. Line 7 shows +$100,000. In 2025, if you depreciate that property at $20,000 per year for AMT, line 7 shows +$80,000 (the remaining carryforward of disallowed deduction). The form automatically reduces it as depreciation "replaces" the disallowed deduction.

### Line 8: Passive Activity Losses

If you have **passive activities** (typically rental real estate or a business in which you do not materially participate), [passive activity losses](/passive-loss-amt-interaction/) must be recalculated using AMT depreciation.

Line 8 captures the difference between the passive loss allowed for regular tax and the recalculated passive loss under AMT depreciation. If the AMT loss is smaller (as it often is, because straight-line depreciation is smaller), a positive adjustment appears here.

More complex scenarios — such as carryforward of disallowed passive losses — are also tracked here.

### Line 9: Loss Limitations

This line can address net-operating-loss (NOL) carryforwards or loss limitations that differ between regular tax and AMT. Most taxpayers leave this blank unless they have a specific AMT adjustment for NOL timing.

### Line 10: Long-Term Contracts

For contractors or construction companies using the **percentage-of-completion method**, line 10 captures the difference in income recognition between regular and AMT methods. This is rarely used by individuals but can be significant for businesses.

### Line 11: Mining Costs

If you have income from mining or mineral extraction, line 11 adjusts for the difference between regular-tax deduction methods and AMT allowances. Most individual taxpayers skip this line.

## Part II: Tax Preferences

Tax preferences are tax benefits that Congress explicitly excluded from AMT. Unlike deduction adjustments (which add back disallowed deductions), preferences are entirely separate items not claimed on your regular return.

### Line 12: Accelerated Depreciation (Property Placed in Service After 1986)

This line captures **accelerated depreciation on tangible personal property** in excess of straight-line depreciation, where the property was placed in service after 1986. This is similar to line 2–6 but targets a specific subset.

The preference is the **excess** of accelerated depreciation over straight-line. If you claimed $100,000 of MACRS but straight-line was $60,000, the preference is $40,000.

### Line 13: Tax-Exempt Interest

Interest from **private-activity bonds** (also called "private-purpose bonds") issued after August 7, 1986, is tax-exempt for regular tax but is **treated as income for AMT purposes**. Municipal bonds (general-obligation bonds) issued to fund public infrastructure are exempt from this rule.

If you hold private-activity bonds, line 13 asks for the tax-exempt interest. That interest is added to AMTI.

**Example:** You own $1 million of private-activity bonds yielding 4% tax-free interest. Line 13 captures $40,000 of tax-exempt interest, which is included in AMTI.

### Line 14: Depletion Deduction

If you have income from oil, gas, minerals, or timber, line 14 captures excess **depletion deductions** taken for regular tax. Depletion is a cost-recovery mechanism similar to depreciation. For AMT, the allowable depletion may be lower, and the excess is a preference item.

### Line 15: Intangible Drilling Costs (IDCs)

For taxpayers with oil and gas drilling activities, line 15 addresses **intangible drilling costs** — costs for labor, materials, and similar expenses incurred in drilling. For regular tax, these costs are often deducted; for AMT, they may be capitalized and recovered over time. The difference is a preference.

### Line 16: Other Preferences

This catch-all line covers other less-common preferences, such as certain research credits or other tax benefits that Congress has excluded from AMT.

### Line 17: Total Preferences

The sum of lines 12–16.

## Part III: Adjustments Based on the Way You Figure Taxable Income

This section adds back deductions that are allowed for regular tax but **not allowed** for AMT purposes.

### Lines 18–27: Itemized Deduction Adjustments

**Line 18: State and Local Income Taxes**
If you deducted state income tax (or state sales tax) on your regular return, line 18 asks: How much did you deduct? That amount is entered here as a positive adjustment, because the AMT does not permit this deduction. If you deducted property tax alongside income tax (combined up to $10,000 under regular rules), line 18 captures the entire disallowed amount.

**Line 19: Real Estate Taxes**
Separate from income tax, if you paid property tax on real estate, that amount is also disallowed under AMT. (Note: Some instructions combine lines 18 and 19 into a single SALT adjustment; the effect is the same.)

**Line 20: Personal Property Taxes**
Taxes on vehicles and other personal property, deducted under regular rules, are also disallowed for AMT.

**Line 21: Home-Equity Loan Interest**
Home-mortgage interest on debt used to acquire or improve the home is allowed for both regular and AMT. However, interest on **home-equity loans or lines of credit** borrowed for other purposes (debt consolidation, investments) is allowed for regular tax but **not** for AMT.

Line 21 asks: How much home-equity interest did you deduct? If it was all on acquisition debt, enter zero. If any was on non-acquisition debt, enter that amount as a positive adjustment.

**Line 22: Miscellaneous Itemized Deductions**
These are the former "miscellaneous deductions subject to the 2% AGI floor": professional development, union dues, job-search costs, and (until 2026) investment advisory and custodial fees. For regular tax, any excess over 2% of AGI is deductible. For AMT, **none of these are allowed**.

Line 22 asks: How much miscellaneous itemized deduction did you claim on [Schedule A](/form-6251-line-by-line/)? That amount is entered here as a positive adjustment.

**Line 23: Alternative Tax Net Operating Loss (ATNOL) Deduction**
If you have a carryforward of an **alternative tax net operating loss** from prior years, line 23 limits how much of that loss you can use in the current year. Most taxpayers leave this blank.

**Line 24: Capital Gain and Qualifying Dividend Amount**
Long-term capital gains and qualifying dividends are taxed at preferential rates (0%, 15%, or 20%) for regular tax. For AMT, the computation is more complex. Line 24 captures information about long-term capital gains and dividends so that the AMT can calculate tax on them at the correct rate. For most taxpayers, this is handled automatically by tax software.

**Line 25: Other Adjustments**
Other disallowances or adjustments not covered above.

**Line 26: Total Adjustments**
The sum of lines 18–25.

**Line 27: Alternative Minimum Taxable Income (AMTI)**
This is the critical line: your regular taxable income (line 1) plus all positive adjustments (lines 2–11 and 12–26). This is what you will owe AMT on, if your AMTI exceeds the exemption threshold.

## Part IV: AMT Tax Calculation

### Line 28: AMT Exemption Amount

The AMT exemption is an amount of income excluded from the AMT calculation, indexed annually for inflation. For 2024, the exemption is approximately:
- **Single filers:** $85,975
- **Married filing jointly:** $135,900
- **Married filing separately:** $67,950

However, the exemption **phases out** (is reduced) as your AMTI increases above a threshold income. The phase-out is 25% — for every $1 of AMTI above the threshold, the exemption is reduced by $0.25.

**Thresholds for 2024:**
- **Single:** Phase-out begins at $579,100
- **Married filing jointly:** Phase-out begins at $870,000

Line 28 shows your allowable exemption after factoring in the phase-out.

### Line 29: AMTI Less Exemption

This is line 27 minus line 28. This is the income subject to AMT tax.

### Line 30: Tentative Minimum Tax

The AMT tax rate is a flat **26% on the first $231,250 of taxable income** (in 2024, indexed) and **28% on income above that**. 

Line 30 calculates: (Portion of line 29 under $231,250) × 26% + (Portion above $231,250) × 28%.

For long-term capital gains and qualifying dividends, special rates apply (0%, 15%, or 20%, depending on your regular-tax rate), handled on a separate worksheet.

### Lines 31–34: Credit and Final AMT

If you have **AMT foreign tax credits** or other credits, they are applied here. Most individuals skip these.

**Line 35: AMT or Regular Tax**
This compares your tentative AMT (line 30) to your regular tax liability. You pay the **greater of the two**:
- Your regular income tax (from Form 1040), or
- Your tentative AMT (line 30).

The difference, if AMT is larger, is the **AMT liability** you owe.

## The Bottom Line: What Form 6251 Tells You

When you complete Form 6251, you are performing a complete alternative tax calculation in parallel with your regular tax. The goal is straightforward: determine whether depreciation adjustments, preference items, and deduction disallowances push your taxable income (on an AMT basis) to a level where the AMT rate exceeds your regular tax rate.

For high-income earners, those with substantial business depreciation, and those in high-tax states, Form 6251 often shows that AMT is owed. For lower-income taxpayers and those with minimal adjustments, the form typically shows zero AMT liability.

The form does not tell you whether AMT is "fair" or whether you should have planned differently. It simply calculates the amount you owe under the law.

## See also

<div class="wiki-seealso">

### Closely related

- [Which Itemized Deductions Are Disallowed Under AMT](/amt-and-itemized-deductions/) — Details on state tax, miscellaneous, and home-equity interest disallowances
- [How Passive Activity Losses Interact With AMT](/passive-loss-amt-interaction/) — How passive losses are recalculated on Form 6251
- [Alternative Minimum Tax for the Self-Employed](/amt-for-self-employed/) — Depreciation and Section 179 adjustments common in business
- [Section 179 Deduction](/section-179-deduction/) — The immediate expensing that creates large Form 6251 adjustments

### Wider context

- [Depreciation](/accumulated-depreciation/) — Cost recovery methods and straight-line vs. accelerated depreciation
- [Basis](/basis/) — How basis and depreciation interact
- [Tax Bracket Investor](/tax-bracket-investor/) — Understanding marginal tax rates, including AMT effective rates
- [Return on Equity](/return-on-equity/) — Performance metrics that inform whether accelerated deductions are worth the AMT risk

</div>
