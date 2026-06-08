---
title: "Deferred Tax Treatment in DCF Models"
description: "How to treat deferred taxes in DCF: whether to discount liabilities, offset against equity value, or embed in NOPAT."
keywords:
  - deferred tax treatment in dcf
  - deferred tax asset valuation
  - deferred tax liability dcf
  - how to treat deferred taxes dcf
  - deferred tax in valuation
  - dcf adjustments deferred taxes
  - tax shield dcf
image: /svg/valuation.svg
---

*When modeling a company's value using **deferred tax treatment in DCF**, the analyst must decide whether deferred tax assets (DTAs) and liabilities (DTLs) belong in the numerator (cash flows), as a separate discount, or as an add-back or reduction at the enterprise-value level. The consensus approach is to exclude them from the DCF and adjust for them below the line—but assumptions vary, and mistakes are common.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Deferred Taxes in DCF — key facts</div>

<img src="/svg/valuation.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Deferred taxes are balance-sheet timing differences, not cash; they should be removed from enterprise value, not embedded in cash flows.</div>

|   |   |
|---|---|
| **Core rule** | Deferred taxes are balance-sheet items; exclude from DCF, adjust below the line |
| **NOPAT treatment** | Use current tax rate; deferred taxes do not reduce operating cash flow |
| **DTA and DTL at valuation** | Add-back DTAs, subtract DTLs from enterprise value |
| **Why exclude from DCF** | Deferred taxes reverse; cash impact is indirect and already in future tax rates |
| **Risk with recapture** | Some DTAs may never reverse; apply a probability haircut |

</aside>

## The conceptual foundation

A deferred tax asset or liability arises because accounting profit differs from taxable income. Classic examples include [depreciation](/depreciation/) methods (accelerated for tax, straight-line for books), [amortization](/amortization/) of goodwill (deductible tax, not for books), and provisions that are not immediately tax-deductible.

These timing differences create a debt or asset on the balance sheet. A deferred tax **liability** means the company will owe taxes later (when the timing difference reverses). A deferred tax **asset** means the company has overpaid taxes now and will recover cash later, or (more commonly) will offset future tax obligations.

The central question: should deferred taxes be baked into the cash flows you discount, or handled separately?

**The answer: almost always separately.** Here is why.

## Why exclude deferred taxes from DCF cash flows

The [discounted cash flow](/discounted-cash-flow-valuation/) method values **future operating cash**, not accounting accruals. Deferred taxes are a timing difference, not a current cash outflow. When you calculate NOPAT (Net Operating Profit After Tax), you apply the **current statutory tax rate**—not a deferred or blended rate.

**Example:**
- A company has pre-tax operating profit of USD 100.
- Taxable income is only USD 80 (because accelerated depreciation for tax purposes is higher than book depreciation).
- Current tax rate: 25%.
- **Current cash tax paid:** 0.25 × 80 = USD 20.
- **NOPAT (for DCF):** 100 × (1 − 0.25) = USD 75.

The deferred tax liability is created (or reduced) by the USD 20 difference (100 − 80). But that liability will **reverse** in future years when the depreciation methods converge. At that point, taxable income will be higher than operating profit, and the company will use its deferred liability to reduce that year's cash tax outflow.

If you tried to add a "deferred tax cash impact" to the DCF, you would be double-counting: once when the liability accrues (overstating cash flow) and again when it reverses (understating cash flow). The cleanest approach is to use a consistent current tax rate throughout, and treat the deferred tax position as a balance-sheet adjustment.

## Treatment in NOPAT

Most analysts calculate NOPAT as:

```
NOPAT = EBIT × (1 − Tax Rate)
```

where the tax rate is the **current or expected marginal tax rate**, not a GAAP or book tax rate.

This implicitly assumes:
- The company pays taxes on a cash basis equal to the statutory rate applied to operating profit.
- Deferred tax accruals are **excluded** because they do not affect current cash tax.

If the company faces a one-time tax rate change (e.g., a jurisdiction raising the corporate rate from 21% to 28%), you would update the forward tax rate in your forecast—that change is expected to affect **future** cash taxes. But the accumulated deferred tax balance on the balance sheet is a separate item: it reflects the **past** timing of deductions, not the future cash impact.

## Handling deferred tax assets and liabilities at valuation

Once you have calculated enterprise value from the DCF, you adjust for the net deferred tax position:

**Enterprise Value (from DCF) + DTA − DTL = Equity Value (before other adjustments)**

In other words:
- A **deferred tax asset** (e.g., USD 50 million of unused tax loss carryforwards) is an economic asset that reduces future cash taxes. Add it to enterprise value.
- A **deferred tax liability** (e.g., USD 100 million owed to taxing authorities in future years) is a future cash outflow. Subtract it from enterprise value.

The net effect is that deferred taxes are treated like any other non-operating balance-sheet item: cash, securities, pensions, or environmental reserves.

## When deferred tax assets are at risk

Not all DTAs have equal value. A DTA based on accelerated depreciation (which will reverse as the asset ages) is reliable. A DTA based on **loss carryforwards** is at risk: the company must be profitable to use them, and many jurisdictions have restrictions (e.g., if ownership changes materially, carryforwards may be forfeited).

Best practice: apply a **probability haircut** to questionable DTAs.

**Example:**
- The company has accumulated loss carryforwards of USD 200 million (creating a DTA of USD 50 million at a 25% tax rate).
- The company has been loss-making for the past 5 years; profitability is not certain.
- You estimate a 60% probability the DTA is realized.
- **Adjusted DTA in valuation:** 50 × 0.60 = USD 30 million.

This approach is common in acquisition modeling, where loss carryforwards are scrutinized by tax counsel before being valued.

## Practical complications

### Tax rate changes

If a new law changes the corporate tax rate, deferred tax balances must be **revalued** to reflect the new rate. A company with a USD 100 million DTA calculated at 21% now has USD 95.24 million if the rate drops to 20%, because the tax savings when that DTA reverses will be smaller.

Most companies revalue deferred taxes when tax law changes; the gain or loss flows through the tax line on the income statement. For a DCF, you would use the **new** statutory rate going forward and revalue the deferred tax asset/liability on the balance sheet.

### Valuation allowances

The company's own financial statements may include a **valuation allowance** against a DTA, signaling that management doubts the asset will be realized. This is a red flag: if the company itself does not believe the DTA is collectable, neither should your valuation. Use the allowance as a guide, or apply your own probability haircut.

### Acquisition scenarios

When an acquirer buys a company, deferred tax items can trigger special rules:
- **Section 338(h)(10) election** (US) allows the buyer to step up the basis of acquired assets, potentially creating new deferred tax liabilities.
- **Change-of-control restrictions** may limit the use of loss carryforwards.

These are deal-specific and sit outside the DCF itself, but they are critical to the final purchase price allocation. Always involve tax counsel.

## Worked example

| Metric | Value |
|--------|-------|
| **Enterprise Value (from DCF)** | USD 1,000 million |
| **Add: DTA (loss carryforwards, 80% haircut)** | USD 40 million |
| **Less: DTL (future tax on built-in gains)** | (USD 60 million) |
| **Net Deferred Tax Position** | (USD 20 million) |
| **Implied Equity Value (before other adjustments)** | USD 980 million |

The deferred tax liability of USD 60 million reduces equity value because the company will owe taxes when it realizes those gains. The DTA of USD 50 million (gross) is valued at USD 40 million (applying an 80% probability) and adds back value.

## Summary: the checklist

1. **Use current tax rate in NOPAT.** Do not try to project deferred tax swings into free cash flow.
2. **Exclude deferred taxes from the DCF.** They are balance-sheet timing differences, not operating cash flows.
3. **Adjust at the enterprise-value line.** Add DTAs, subtract DTLs.
4. **Haircut uncertain DTAs.** Loss carryforwards and intangible asset amortization deserve skepticism.
5. **Revalue if tax rates change.** A new statutory rate changes the worth of future tax savings.
6. **Flag change-of-control risks.** Acquisitions often trigger restriction on DTA use; involve tax counsel.

Deferred taxes are a source of valuation confusion because they live in two worlds: the accounting income statement and the tax return. By treating them as a balance-sheet adjustment rather than an operating assumption, you keep the DCF clean and the deferred tax analysis explicit.

## See also

<div class="wiki-seealso">

### Closely related

- [Discounted Cash Flow Valuation](/discounted-cash-flow-valuation/) — the parent DCF framework
- NOPAT — the operating profit metric that excludes tax adjustments
- Tax Rate — the current rate used in DCF, not deferred or blended
- [Enterprise Value](/enterprise-value/) — where deferred taxes are adjusted below the line
- [Depreciation](/depreciation/) — the most common source of deferred tax differences
- [Amortization](/amortization/) — goodwill amortization creates deferred taxes on acquisitions

### Wider context

- [Generally Accepted Accounting Principles](/generally-accepted-accounting-principles/) — GAAP allows deferred tax accounting
- [International Financial Reporting Standards](/international-financial-reporting-standards/) — IFRS defers taxes similarly
- [Leveraged Buyout](/leveraged-buyout/) — LBO models closely track deferred taxes and change-of-control restrictions
- [Acquisition](/acquisition/) — acquisitions trigger 338(h)(10) and basis-step-up planning

</div>
