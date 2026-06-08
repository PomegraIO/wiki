---
title: "How to Calculate Alternative Minimum Tax Step by Step"
description: "Detailed walkthrough of the AMT calculation: preference items, exemption, rates, and comparing tentative minimum tax to regular tax."
keywords:
  - how to calculate alternative minimum tax
  - amt calculation worksheet
  - amt income preferences adjustments
  - amt exemption phase-out
  - tentative minimum tax
image: /svg/taxes.svg
---

*Calculating **how to calculate alternative minimum tax** requires running a parallel income-tax computation: add preference items to regular taxable income, apply the exemption, compute tax at AMT rates, then compare the result to regular tax. The higher of the two is what you owe. The process is methodical but not intuitive, and small differences in preference items can swing a taxpayer between regular and minimum tax.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">AMT Calculation — core steps</div>

<img src="/svg/taxes.svg" alt="An abstract editorial mark for taxation." />

<div class="wiki-infobox-caption">AMT is a parallel tax system; you pay whichever is higher.</div>

|   |   |
|---|---|
| **Starting point** | Regular taxable income (or AGI, depending on adjustment) |
| **Add back preference items** | ISOs, SALT, passive losses, tax-exempt bond interest |
| **Apply AMT exemption** | Subtract ~$85K–$90K (2024; indexed) from adjusted income |
| **Compute tentative AMT** | Apply 26%/28% rate brackets to remaining income |
| **Compare to regular tax** | Pay the higher of regular tax or tentative AMT |
| **Result** | Difference is the AMT credit carryforward (if AMT exceeds regular tax) |

</aside>

## Step 1: Start with Regular Taxable Income

Begin with your regular [income-statement](/income-statement/) taxable income for the year—the number you'd use to calculate standard federal-income-tax liability under ordinary rules. This includes wages, interest, dividends, capital gains, business income, and any other ordinary income sources, minus standard or itemized deductions.

For most employees, this is the federal taxable income line on their Form 1040. For self-employed or business owners, it's taxable income after business deductions. Do not start with gross income; AMT builds on the regular-tax framework and modifies it, not replaces it.

## Step 2: Identify and Add Back Preference Items

The **alternative minimum tax** exists because certain deductions and income sources allowed under regular tax are considered "preferences" or "adjustments" that shelter income unfairly. You must add these back dollar-for-dollar into your AMT calculation.

### Common Preference Items

| Item | Add-back | Notes |
|---|---|---|
| **Incentive stock option bargain element** | Full amount of (FMV − strike price) | Exercise-year preference; eliminated on sale if held 2 years |
| **State, local, property taxes (SALT)** | All state/local income, property, and sales taxes | Fully nondeductible under AMT |
| **Passive loss carryforwards** | Full current and prior-year passive losses | [Real estate](/real-estate-investment-trust/), limited partnerships, rental losses |
| **Private activity bond interest** | 100% of tax-exempt interest | Certain municipal bonds; details vary |
| **Depreciation (MACRS excess)** | Excess of MACRS over straight-line | Self-employment or business assets; primarily real estate |
| **Deductible investment losses** | Realized losses used to offset income | Capital losses and passive-loss deductions |
| **Charitable contributions (certain)** | Limited; some conservation easements | Rarely material for salaried employees |

### Working Example

Sarah, a salaried employee, has:
- W-2 income: $250,000
- Itemized deductions: $50,000 (mortgage interest, charitable)
- State and local taxes paid: $35,000
- Regular taxable income: $165,000 (after standard or itemized deductions)

For AMT, she must add back SALT in full:
- SALT add-back: $35,000
- AMT income before exemption: $165,000 + $35,000 = $200,000

If Sarah also exercised ISOs:
- ISO preference: $80,000
- Total AMT income: $200,000 + $80,000 = $280,000

## Step 3: Subtract the AMT Exemption

The **alternative minimum tax exemption** is a floor amount that shields a portion of all taxpayers' income from the AMT rate. The exemption is indexed annually for inflation and varies by filing status.

As of 2024:
- **Single**: ~$85,700
- **Married filing jointly**: ~$134,600
- **Married filing separately**: ~$67,300
- **Head of household**: ~$85,700

Once your AMT income exceeds the exemption by a certain threshold, the exemption begins to phase out. For every dollar of AMT income over the threshold, the exemption reduces by $0.25 (25% phase-out rate). The phase-out thresholds are also indexed:

- Single and head of household: $578,150 (2024)
- Married filing jointly: $865,000 (2024)
- Married filing separately: $432,500 (2024)

### Calculating Phased-Out Exemption

If your AMT income exceeds the threshold:

**Phased-out exemption = Full exemption − (0.25 × (AMT income − phase-out threshold))**

Continuing Sarah's example (single filer, $280,000 AMT income):
- AMT income: $280,000
- Phase-out threshold: $578,150
- AMT income is below the threshold, so no phase-out.
- Usable exemption: $85,700
- **AMT taxable income = $280,000 − $85,700 = $194,300**

If Sarah's AMT income were $700,000:
- Amount over threshold: $700,000 − $578,150 = $121,850
- Phase-out reduction: 0.25 × $121,850 = $30,462
- Usable exemption: $85,700 − $30,462 = $55,238
- **AMT taxable income = $700,000 − $55,238 = $644,762**

## Step 4: Apply AMT Tax Rates

The AMT uses two rate brackets (26% and 28%), which are **lower** than ordinary income tax rates but apply to a broader [income-statement](/income-statement/) base (because preferences were added back).

**AMT rate brackets (2024):**
- 26% on the first $230,250 of AMT taxable income (single); $460,550 (married filing jointly)
- 28% on AMT taxable income above those thresholds

### Compute Tentative Minimum Tax

**Tentative AMT = (26% × first bracket income) + (28% × excess over bracket)**

Returning to Sarah's example with $194,300 AMT taxable income (single):
- First $230,250 at 26%: She's entirely in the 26% bracket.
- Tentative AMT = 0.26 × $194,300 = $50,518

If her AMT income were $500,000 (single):
- First $230,250 at 26%: 0.26 × $230,250 = $59,865
- Remaining: $500,000 − $230,250 = $269,750 at 28%: 0.28 × $269,750 = $75,530
- Tentative AMT = $59,865 + $75,530 = $135,395

## Step 5: Calculate Regular Federal Income Tax

For comparison, compute regular federal [income-tax](/income-statement/) liability using standard 2024 [tax-bracket-investor](/tax-bracket-investor/) rules and rates. Sarah's regular taxable income of $165,000 (single) incurs ordinary federal tax at marginal rates—roughly $28,000–$32,000, depending on her exact deductions and applicable tax credits.

## Step 6: Compare and Pay the Higher Amount

Your **alternative minimum tax liability** is the excess of tentative AMT over regular tax, if positive. You pay whichever is higher.

| Scenario | Regular Tax | Tentative AMT | Pay | AMT "Owed" |
|---|---|---|---|---|
| No preferences | $28,000 | $20,000 | $28,000 | $0 |
| Modest preferences | $28,000 | $35,000 | $35,000 | $7,000 |
| Heavy preferences | $28,000 | $65,000 | $65,000 | $37,000 |

## Step 7: AMT Credit Carryforward (Rare)

If you pay AMT in a given year (tentative AMT exceeds regular tax), you may generate an **AMT credit**—a carryforward that reduces future regular tax in years when tentative AMT is less than regular tax. This credit is available only if your AMT resulted from "timing differences" (depreciation, passive losses, ISOs) rather than permanent preferences (SALT, charitable contributions). The credit carryforward was especially valuable pre-2017, when more taxpayers cycled between AMT and regular tax.

Post-2017 tax law, with higher standard deductions and SALT caps, fewer individuals slip in and out of AMT annually, reducing the practical value of AMT credits. However, for high-income employees with significant ISO exercises, AMT credits remain worth tracking.

## Practical Worksheet Template

Use this simplified template to run the calculation:

```
1. Regular taxable income                                 $165,000
2. Add: ISO preferences                                    $80,000
3. Add: SALT (fully nondeductible)                         $35,000
4. AMT income (line 1 + line 2 + line 3)                 $280,000
5. AMT exemption (indexed, per filing status)             $85,700
6. Less: Phase-out (if AMT income > threshold)                 $0
7. Usable exemption (line 5 − line 6)                     $85,700
8. AMT taxable income (line 4 − line 7)                  $194,300
9. AMT at 26% on first bracket                            $50,518
10. AMT at 28% on excess (if any)                              $0
11. Tentative minimum tax (line 9 + line 10)              $50,518
12. Regular federal income tax                             $28,000
13. AMT (greater of line 11 or line 12)                   $50,518
14. AMT liability (line 13 − line 12)                     $22,518
```

Professional tax software (TaxAct, TurboTax Premium, professional software) computes this automatically, but understanding the logic helps identify which preference items matter most and where planning opportunities exist.

## See also

<div class="wiki-seealso">

### Closely related

- [Alternative Minimum Tax for High-Income Employees](/amt-for-high-income-employees/) — Common triggers and planning scenarios
- [AMT Exemption Inflation Adjustments Explained](/amt-exemption-2024-inflation-adjustment/) — Why exemptions change yearly and historical context
- [Private Activity Bond Interest as an AMT Preference Item](/private-activity-bond-amt-preference/) — Municipal bond interest add-backs
- [Tax Bracket for Investors](/tax-bracket-investor/) — Standard income-tax brackets and phase-outs

### Wider context

- [Form 8949](/form-8949/) — Reporting capital losses and gains
- [Capital Gains Tax for Investors](/capital-gains-tax-investor/) — Long-term gain treatment under both regular and AMT
- [Income Statement](/income-statement/) — Financial income vs. taxable income concepts
- Passive Loss Rules — Passive loss add-backs and limitations

</div>
