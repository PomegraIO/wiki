---
title: "After-Tax Cost of Debt"
description: "The effective cost of debt to a company after accounting for the tax deductibility of interest payments, lower than the nominal interest rate."
keywords:
  - after-tax cost of debt
  - tax shield
  - cost of debt
  - WACC
  - tax rate
image: "/svg/valuation.svg"
---

*The **after-tax cost of debt** is what debt truly costs a company on an after-tax basis. A company might pay 5% interest, but if it has a 25% tax rate, the after-tax cost is only 3.75%. The difference—1.25 percentage points—is the tax shield: the government is effectively subsidizing the debt. This tax effect is why [weighted average cost of capital](/weighted-average-cost-of-capital/) always uses after-tax cost of debt, not the bare interest rate.*

## The formula and the intuition

After-tax cost of debt = Cost of debt × (1 minus Tax rate)

If cost of debt is 5% and the company's tax rate is 30%, after-tax cost is 5% × 0.70, or 3.5%.

The logic is that interest is tax-deductible. When a company pays 100 dollars in interest, it reduces taxable income by 100 dollars. At a 30% tax rate, that saves 30 dollars in taxes. So the net cost is 70 dollars, not 100.

For valuation, this matters enormously. Leverage appears cheaper on an after-tax basis, which is why companies use debt. All else equal, a company with 50% debt-to-value has a lower WACC than an all-equity company.

## How the tax shield arises

When a company borrows at 5%, it incurs an interest expense. This expense is deducted before calculating taxable income. Every dollar of interest saved is a dollar of tax shield:

Tax shield = Interest paid × Tax rate = Cost of debt × Debt outstanding × Tax rate

For a company with 100 million of debt at 5% and a 30% tax rate: Tax shield = 5 million × 0.30 = 1.5 million per year.

This 1.5 million is a real, tangible benefit of leverage. It is why financial structures matter: debt is cheaper than equity precisely because of this tax effect.

## Which tax rate to use

Use the company's **marginal tax rate**, not the average or effective tax rate. The marginal rate is the rate on the next dollar of income.

For a profitable US corporation, this is typically 21% (federal) plus state taxes, for a combined rate of 25–27%. For a company in a high-tax country (Europe, Japan), it might be 35–40%.

For a company with losses (pre-tax), the marginal rate is zero—no tax benefit from interest deductions until the company returns to profitability.

## The perpetual tax shield

In perpetuity-based valuation, the annual tax shield continues forever. The present value of a perpetual tax shield is:

PV of tax shield = Tax rate × Cost of debt × Debt outstanding / Cost of debt = Tax rate × Debt outstanding

In other words, the value of the debt tax shield is simply the tax rate times the amount of debt. A company with 500 million of debt and a 30% tax rate receives 150 million of tax shield value.

This is why highly leveraged structures create value (on paper): they extract massive tax shields. But they also create financial distress risk—the higher the leverage, the greater the risk of default, which eventually erodes the tax benefit.

## A key assumption in WACC

In the [weighted average cost of capital](/weighted-average-cost-of-capital/) formula:

WACC = (E / D+E) × r_e + (D / D+E) × r_d × (1 - T_c)

The term (1 minus T_c) applies only to the cost of debt, not to cost of equity. This reflects that equity returns are not tax-deductible (dividends and capital gains are taxed at the shareholder level, not the corporate level, but the company does not deduct them).

Using pre-tax cost of debt in this formula is a common mistake. It overstates WACC and undervalues leverage.

## Tax shield changing over time

If a company's tax rate changes—say, due to a change in tax law or the company's profitability—the tax shield changes:

1. A profitable company that becomes unprofitable loses the tax shield until it returns to profitability.

2. A company in a country that raises tax rates experiences lower tax shields on new debt.

3. A company with large tax loss carryforwards cannot deduct new interest immediately, reducing the shield.

For a precise valuation, you might model these changes explicitly. For simplicity, assume the tax rate is stable.

## Tax shields and debt paydown

If a company is explicitly paying down debt (as in a leveraged buyout scenario), the tax shield declines as debt declines. If debt falls from 500 million to 0 over 10 years, the annual tax shield declines proportionately.

This is why highly leveraged companies have significant refinancing risk: once debt is paid down, the tax shield shrinks, reducing the cash available to service new or remaining debt.

## The discount rate for tax shields

One thorny question: should the tax shield be discounted at the cost of debt or some other rate? This matters for the exact present value.

Academic consensus is split. Some argue tax shields should be discounted at the cost of debt (the rate at which the tax shield cash flows are risky). Others argue they should be discounted at a lower rate (because they are less risky—they depend on the company being profitable, but if the company is profitable, the debt is likely safe).

For practical valuation, the difference is small. Use the cost of debt as the discount rate for tax shields, which is simpler.

## See also

<div class="wiki-seealso">

### Closely related

- [Cost of debt](/cost-of-debt/) — the pre-tax cost
- [Weighted average cost of capital](/weighted-average-cost-of-capital/) — always uses after-tax cost
- Tax rate — determines the shield magnitude
- Tax shield — the underlying concept

### Valuation impact

- [Free cash flow to firm valuation](/free-cash-flow-to-firm-valuation/) — uses WACC with after-tax cost
- [Discounted cash flow valuation](/discounted-cash-flow-valuation/) — parent method
- Capital structure — determines debt amount and thus shield value

### Related concepts

- [Interest rate](/interest-rate/) — drives cost of debt
- [Bond](/bond/) — the source of debt cost
- Leverage — creates the tax shield benefit

### Sensitivity and analysis

- [Sensitivity analysis](/sensitivity-analysis-valuation/) — testing tax-rate sensitivity
- [Football field valuation](/football-field-valuation/) — ranges across tax and leverage assumptions

</div>
