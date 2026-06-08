---
title: "How Passive Activity Losses Interact With AMT"
description: "Passive activity losses are recomputed under AMT rules using different depreciation methods, potentially creating two different allowed loss amounts — one for regular tax and one for AMT purposes."
keywords:
  - passive activity losses and alternative minimum tax
  - passive loss amt
  - passive activity deduction amt
  - real estate loss amt
  - depreciation adjustment passive loss
image: /svg/taxes.svg
---

*A **passive activity loss** computed under regular tax rules may produce a different allowable deduction when recalculated under [AMT](/form-6251-line-by-line/) rules. This happens because the AMT uses different [depreciation](/accumulated-depreciation/) methods — typically straight-line depreciation rather than accelerated depreciation — which can change both the size of the loss and the amount you are permitted to use in a given year, creating what amounts to two separate passive-loss calculations for the same property.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Passive Losses & AMT — key facts</div>

<img src="/svg/taxes.svg" alt="An abstract editorial mark for tax topics." />

<div class="wiki-infobox-caption">The same rental property or partnership investment can produce different loss amounts under regular and AMT calculations.</div>

|   |   |
|---|---|
| **The core issue** | [Depreciation](/accumulated-depreciation/) adjustments under AMT can reduce (or expand) the economic loss in a passive activity |
| **Depreciation used for AMT** | Straight-line method; no bonus depreciation or [Section 179](/section-179-deduction/) |
| **Result** | A smaller net loss under AMT, meaning less loss available to offset [passive](/passive-loss-amt-interaction/) income |
| **Key form** | [Form 6251](/form-6251-line-by-line/) Part I, and [Form 8582](/passive-loss-amt-interaction/) (Passive Activity Loss Limitations) |
| **When it matters** | Rental real estate, limited partnerships, real-estate development ventures |
| **Impact** | Can reduce the tax benefit of passive losses, sometimes creating AMT liability despite regular-tax losses |

</aside>

## Why Passive Losses Must Be Recomputed for AMT

Under regular tax rules, passive activity losses are subject to annual limitations: you can use a passive loss to shelter passive income, and up to $25,000 of passive loss can offset active (wages, salary) or portfolio income if your modified AGI is below certain thresholds (with a phase-out beginning at $100,000). Excess losses are carried forward indefinitely.

The amount of that annual loss, however, depends on how you calculated depreciation on the underlying assets. If you used [accelerated depreciation](/accumulated-depreciation/) or [Section 179](/section-179-deduction/) deductions on equipment or [bonus depreciation](/accumulated-depreciation/) on real estate, your regular-tax loss will be larger than if you used straight-line depreciation.

Under AMT rules, you must recompute the passive loss using **straight-line depreciation only**. This adjustment is made on [Form 6251](/form-6251-line-by-line/) as an AMT adjustment, but it cascades backward into the passive-loss limitation calculation itself. The result: a different passive loss amount, and therefore a different amount available to use in the current year or carry forward.

## How Depreciation Creates the Adjustment

Suppose you own a rental house purchased for $300,000, of which $225,000 is allocable to the building. Under regular tax, using straight-line depreciation over 27.5 years (residential rental property), your annual depreciation deduction is approximately $8,182.

However, if the property qualifies for bonus depreciation or you claimed [Section 179](/section-179-deduction/) deductions on improvements, you might have claimed significantly more. For example, a $50,000 qualifying improvement might generate a $50,000 Section 179 deduction in the year it is made, rather than being spread over 27.5 years.

For AMT purposes, you must **recalculate using straight-line depreciation with no Section 179 or bonus**. The difference between accelerated and straight-line is a positive AMT adjustment.

**Example:**
- Regular tax depreciation (with Section 179): $65,000
- AMT depreciation (straight-line only): $8,200
- **Adjustment: $56,800 positive adjustment to AMTI**

This $56,800 is added back in computing your alternative minimum taxable income — but it also affects the passive loss calculation. If the property otherwise had a $70,000 loss under regular rules, the AMT recalculation might show only a $13,200 loss.

## The Two-Calculation Consequence

You now have two separate passive-loss scenarios:

| | Regular Tax | AMT |
|---|---|---|
| **Annual depreciation** | $65,000 | $8,200 |
| **Other deductions (interest, taxes, etc.)** | $50,000 | $50,000 |
| **Gross rental income** | $80,000 | $80,000 |
| **Net passive loss** | $35,000 | $22,200 |
| **Allowable under limitation** | $25,000 (or more if AGI is low) | $25,000 (if AMT applies) |
| **Loss carryforward** | $10,000 | Loss is smaller; carryforward is smaller |

In this scenario, your regular tax return shows a $25,000 passive loss deduction and a $10,000 carryforward. But when you compute AMT, your passive loss is only $22,200, so the carryforward is even smaller, or you might have no carryforward at all.

## Passive Loss Disallowance Under AMT

Here is a subtler issue: under regular tax, if you have $25,000 of disallowed passive loss, you carry it forward indefinitely, and you can use it against future passive income or (in the year you dispose of the property) against active/portfolio income.

Under AMT, the passive loss limitation **still applies**, but using the AMT depreciation amount. If the AMT passive loss is smaller because straight-line depreciation is smaller, you have less loss to carry forward — even though the regular-tax carryforward is larger. This means you may not be able to fully offset future income using the regular-tax loss carryforward, because only the smaller AMT amount is usable in computing alternative minimum taxable income.

## Real-World Scenario: When This Creates an AMT Bill

Consider a high-income investor with passive real-estate holdings and limited passive income:

- **Passive income:** $15,000 (from a partnership)
- **Regular-tax passive loss:** $45,000 (including accelerated depreciation and Section 179)
- **Allowable passive loss, regular tax:** $25,000 (up to the limitation)
- **Regular tax:** Loss shelters $15,000 of passive income and $10,000 of active income

Now compute AMT:
- **AMT passive loss** (using straight-line only): $20,000
- **Allowable passive loss, AMT:** $20,000
- **Passive income under AMT:** $15,000 (unchanged)
- **Unused passive loss under AMT:** $5,000

This $5,000 difference means that under AMT, $5,000 of passive income is not sheltered. If that $5,000 is taxable at the 20.8% AMT rate (37% plus 3.8% surtax), it generates $1,040 of extra AMT liability for that year alone. Over multiple years, this compounds.

## Coordinating With Form 6251

On [Form 6251](/form-6251-line-by-line/) Part I, line 7 or nearby, you calculate depreciation adjustments. The difference between regular and AMT depreciation is entered as a positive adjustment. This adjustment percolates through to AMTI.

However, the passive loss limitation itself is calculated separately. The Internal Revenue Service does not automatically recompute passive losses on Form 6251; the burden falls on you to:
1. Recalculate the passive loss using straight-line depreciation (as if you had used only that method from inception).
2. Apply the passive loss limitation rules using that recalculated loss.
3. Use the AMT-calculated passive loss in computing AMTI.

Many taxpayers and even some tax preparers miss this step, which can result in an understated AMT liability or, conversely, an overstated loss carryforward.

## Reconciliation With Form 8582

[Form 8582](/passive-loss-amt-interaction/) (Passive Activity Loss Limitations) is the standard form used to compute how much passive loss you can use in a given year. Most filers complete Form 8582 once, using regular tax depreciation. However, for AMT purposes, if depreciation adjustments are large, you may need to prepare a **separate** Form 8582 calculation using AMT depreciation, then reconcile the two.

Some tax software does this automatically; others require manual adjustment. If you have substantial passive losses and accelerated depreciation, this step deserves careful attention.

## Passive Losses From Partnerships and S-Corporations

The same issue arises if you are a partner or S-corporation shareholder with passive activity allocations. The partnership or S-corporation computes its taxable income using its depreciation methods. That income (or loss) flows through to your return. You then must adjust it for AMT purposes if the entity has used accelerated depreciation, bonus, or Section 179.

If the partnership or S-corporation has no passive-loss limitation issues itself (because it is not subject to passive-loss rules), you still face the adjustment at your individual level if your individual circumstances trigger passive-activity treatment.

## See also

<div class="wiki-seealso">

### Closely related

- [Form 6251 Line-by-Line Walkthrough](/form-6251-line-by-line/) — How depreciation adjustments flow into the AMT calculation
- [Which Itemized Deductions Are Disallowed Under AMT](/amt-and-itemized-deductions/) — Other deduction disallowances that can trigger AMT
- [Alternative Minimum Tax for the Self-Employed](/amt-for-self-employed/) — How sole proprietors navigate depreciation adjustments
- [Section 179 Deduction](/section-179-deduction/) — The accelerated deduction that creates AMT adjustments

### Wider context

- [Depreciation](/accumulated-depreciation/) — Core concepts of cost recovery and depreciation methods
- [Real Estate Investment Trust](/real-estate-investment-trust/) — An alternative to direct ownership that avoids passive-loss limitations
- [Depreciation Recapture Investor](/depreciation-recapture-investor/) — How depreciation affects gain on sale
- [Basis](/basis/) — How cost basis and adjustments interact with depreciation and AMT

</div>
