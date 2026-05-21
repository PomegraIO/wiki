---
title: "EV Bridge"
description: "A reconciliation schedule that connects equity value to enterprise value by adjusting for net debt and other balance sheet items, essential for converting between valuation approaches."
keywords:
  - EV bridge
  - enterprise value
  - equity value
  - net debt
  - valuation bridge
image: "/svg/valuation.svg"
---

*An **EV bridge** (or enterprise-value bridge) is a simple but essential worksheet that converts between enterprise value and equity value. Most valuation models (DCF, [sum-of-the-parts](/sum-of-the-parts-valuation/)) produce enterprise value. But equity investors care about equity value—what they can actually own. The bridge fills the gap.*

## The simple formula

Equity value = Enterprise value minus Net debt

Where net debt = Total debt minus Cash

## Example

A company has an enterprise value (from a DCF) of 1 billion. Its balance sheet shows:
- Total debt: 300 million
- Cash: 50 million
- Net debt: 250 million
- Equity value: 1,000 minus 250 = 750 million
- Shares outstanding: 75 million
- Implied value per share: 750 / 75 = 10 per share

## Why the bridge is necessary

**DCF typically calculates enterprise value.** The model discounts free cash flow to the firm (available to all investors) at the WACC. The result is what the entire enterprise (debt plus equity) is worth.

**Equity investors want equity value.** They own stock, not the whole enterprise. They care about value available to them after debt holders are paid.

**The bridge reconciles them.** It shows explicitly how the enterprise value flows down to equity value.

## Full bridge structure

A detailed EV bridge is:

Starting point: Enterprise value (from DCF or other method)
Add: Cash and cash equivalents
Less: Total debt
Less: Preferred stock (if any; preferred is senior to common equity)
Less: Noncontrolling interests (if valuing 100% of a subsidiary; subtract the portion that minority owners have)
Equals: Equity value (common equity)

Divide by: Shares outstanding
Equals: Implied value per share

## Common bridge line items

**Cash.** Add back. Debt holders don't own cash; equity holders do.

**Debt.** Subtract. All forms: bonds, bank loans, capitalized leases, pension liabilities, deferred revenue treated as debt.

**Preferred stock.** Subtract if valuing common equity only. Preferred holders have priority over common in liquidation.

**Noncontrolling interests.** If you valued 100% of a company where 10% is owned by minority shareholders, subtract 10% of equity value to get value available to parent-company shareholders.

**Pension liabilities vs. assets.** A pension plan with larger liabilities than assets is a liability (subtract). A plan with excess assets is an asset (add). Or use the funded status from the financial statements.

**Operating leases.** Under recent accounting standards (IFRS 16, ASC 842), operating leases appear on the balance sheet as liabilities. The value of these is embedded in the enterprise value calculation (if you adjusted EBITDA for lease costs); they may require clarification in the bridge.

**Deferred revenue.** If a company has received cash upfront for future services, this liability is already in the balance sheet. Don't double-count in the bridge.

## Practical execution

The bridge is typically a simple table:

| Item | Amount ($ millions) |
|---|---|
| Enterprise value | 1,000 |
| Add: Cash | 50 |
| Less: Debt | (300) |
| Less: Preferred stock | (0) |
| Less: Noncontrolling interests | (0) |
| = Equity value | 750 |
| Shares outstanding (millions) | 75 |
| = Value per share | $10.00 |

## Why it matters

**Clarity.** The bridge makes explicit all adjustments from DCF output to per-share value. No hidden assumptions.

**Prevents errors.** A common mistake is forgetting to subtract debt or adding cash twice. A clear bridge catches these.

**Audit trail.** If someone questions your valuation, the bridge shows your logic step-by-step.

**Sensitivity.** You can show what happens if debt changes: "If the company issues 100 million in new debt, equity value falls by 100 million, to 650 million."

## Special considerations

**Minority interests.** If you valued 100% of a subsidiary but the parent owns 80%, you must subtract 20% for the minority stake.

**Convertible debt.** If the company has convertible bonds, should they be treated as debt or equity? This depends on context. If you assume they convert, treat as equity. If not, treat as debt.

**Options and warrants.** If the company has employee stock options or warrants outstanding, should you dilute the share count? This is typically done via the treasury stock method in valuations and is not part of the bridge itself, but it affects the final per-share value.

**Pension liabilities.** Some companies have pension obligations. If the plan is underfunded, the liability is a cash outflow (included in debt). If overfunded, it is an asset (included in cash). Use the net liability or asset from the balance sheet.

## Forward-looking bridge

For a valuation dated in the future (e.g., "what will the company be worth in 5 years?"), you adjust the bridge items for expected changes:

- Cash might be much lower (used for investment or returning to shareholders).
- Debt might be lower (repaid from cash flow) or higher (incurred for acquisitions).
- Shares outstanding might be lower (repurchases) or higher (issued for acquisitions).

This forward-looking bridge is useful in M&A scenarios and strategic planning.

## See also

<div class="wiki-seealso">

### Closely related

- [Enterprise value](/enterprise-value/) — what valuation models calculate
- Equity value — what shareholders own
- [Net debt](/net-debt/) — the bridge adjustment
- [Market capitalization](/market-capitalization/) — related to equity value

### Valuation frameworks

- [Discounted cash flow valuation](/discounted-cash-flow-valuation/) — produces enterprise value
- [Free cash flow to firm valuation](/free-cash-flow-to-firm-valuation/) — FCFF valuation
- [Sum-of-the-parts valuation](/sum-of-the-parts-valuation/) — segment enterprise values

### Balance sheet items

- Debt — subtracted from EV
- Cash — added to EV
- [Preferred stock](/preferred-stock/) — subtracted from common equity value
- Noncontrolling interests — subtracted from consolidated value

</div>
