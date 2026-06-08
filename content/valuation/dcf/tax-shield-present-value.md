---
title: "Present Value of the Tax Shield"
description: "The financial value of interest deductions in a DCF, quantified by discounting future tax savings from debt financing."
keywords:
  - tax shield
  - debt financing
  - interest deductions
  - dcf valuation
  - cost of debt
  - corporate taxation
image: /svg/valuation.svg
---

*The **tax shield** is the tax saving a company gets because interest on debt is deductible, unlike dividend payments on equity. In a DCF, this becomes a present-value figure—the sum of discounted future tax savings from borrowing—and can meaningfully lift enterprise value.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Tax Shield — value of deductible interest</div>

<img src="/svg/valuation.svg" alt="An abstract editorial mark for valuation and finance mechanics." />

<div class="wiki-infobox-caption">Debt is cheaper than equity partly because the tax code subsidises interest expenses.</div>

|   |   |
|---|---|
| **What it is** | Annual interest expense × tax rate, discounted to present value |
| **Also called** | Interest tax shield, debt tax benefit, tax advantage of leverage |
| **Formula (perpetual debt)** | (Debt Amount × Interest Rate × Tax Rate) / Discount Rate |
| **Driver** | Corporate tax rate and cost of debt |
| **Affects** | Enterprise value, weighted average cost of capital (WACC) |
| **Caveat** | Only applies if the company has taxable profit to offset |

</aside>

## Why debt interest creates a tax benefit

Under most national tax codes, a corporation deducts [interest expense](/interest-rate/) from revenue before calculating taxable profit. If a company borrows $100 million at 5% interest ($5 million annually) and faces a 25% tax rate, it saves $1.25 million per year in taxes—because that $5 million lowers its tax base by $5 million, and 25% of $5 million is $1.25 million.

Dividends to equity holders receive no such deduction. A company cannot deduct the $1 million dividend it pays to shareholders. The result: interest is effectively cheaper than equity returns, all else equal.

A **tax shield** quantifies this subsidy in dollar terms. Year one: $1.25 million of tax savings. Year two, if debt and interest rates are unchanged: another $1.25 million. These savings stretch into the future, and their present value belongs in a DCF model.

## Two approaches: perpetual and finite

The simplest formula assumes the company will carry the debt forever (or until the end of time in the DCF terminal period):

> **Tax Shield PV (perpetual debt)** = (D × r_d × T) / r_d = D × T
>
> Where D = debt amount, r_d = interest rate, T = tax rate

Notice that the interest rate cancels out. The PV equals debt times the tax rate. If a company borrows $100 million and the tax rate is 25%, the perpetual tax shield is worth $25 million in present value—a one-time boost to value.

This approach is elegant but assumes static debt and steady-state taxes forever. Reality is messier.

A more realistic model assumes the company will pay off (or refinance) debt on a known schedule. If debt matures in year 10, the tax shield expires then. The formula becomes:

> **Tax Shield PV (finite debt)** = Σ [(D × r_d × T) / (1 + r_d)^t] for t = 1 to maturity

Here, each year's tax saving is discounted individually. If the company repays $10 million of a $100 million loan each year, the tax saving shrinks year by year, and the final year's shield (10% of the original) is smallest.

## Choosing the discount rate for the tax shield

This is where DCF practitioners divide. One camp argues the tax shield should be discounted at the *cost of debt*—the same rate used to value the debt itself. The intuition: the tax shield is as risky as the debt that generates it. If the borrower defaults, both vanish.

Another camp discounts at the *cost of equity*, reasoning that tax shields reduce financial risk and benefit equityholders proportionally.

A third approach uses the [cost of equity](/cost-of-equity/) or a blended rate, because the tax shield ultimately transfers wealth to equity. This is common in academic DCF texts but less common in practice.

Most practitioners in industry use the **cost of debt** for simplicity and because it aligns the shield's risk with the liability. If you are less certain about the company's ability to sustain debt, using a higher discount rate (moving toward the cost of equity) is defensible.

## Tax shields only work if the company is profitable

A critical caveat: tax shields exist only if the company has sufficient taxable profit to offset the interest deduction. A company that is loss-making cannot use the deduction in the year it occurs; it must carry the loss forward (under most tax codes). The timing of the tax benefit delays and may reduce its present value.

In a DCF, if the company is projected to lose money, assume zero tax shields until profitability resumes. Some models use a "tax shield benefit factor" of less than 100%—say, 70%—to account for the risk that deductions are lost, carried forward, or expire.

## Tax shields in a WACC DCF

Many practitioners bundle the tax shield into the [discount rate](/discount-rate/) itself via the weighted average cost of capital. WACC already embeds a tax adjustment:

> WACC = (E/V) × r_e + (D/V) × r_d × (1 − T)

The term (1 − T) is the tax adjustment on the debt leg. It lowers the effective cost of debt because of the tax deduction. When you discount free cash flow at this adjusted WACC, you are implicitly capturing the tax shield—no need to add it separately.

This is clean and avoids double-counting, but it assumes you have the capital structure (D and E weights) locked in.

## Unlevered and levered FCF methods

Some DCF models value the company at its *unlevered* free cash flow—the cash before interest and taxes—then subtract debt and add the tax shield separately. Others use *levered* free cash flow, which already deducts interest and taxes, leaving cash available to equity only.

If using unlevered FCF, you must *add* the present value of the tax shield (and subtract debt, add net cash) to reach equity value. If using levered FCF, the tax shield is already embedded in the cash flows, so do not add it again. Mixing the two is a common DCF error.

## Terminal value and sustainable tax shields

In the terminal value period, assume tax shields continue indefinitely at the steady-state debt level. If the company's debt is projected to stabilise at $500 million and the tax rate is 24%, the terminal-year tax shield is $500 million × 24% = $120 million per year, growing at the terminal growth rate (usually 2–3%) thereafter.

For a cleaner model, some analysts assume debt as a percentage of enterprise value stabilises, then back into an absolute debt level based on the terminal enterprise value—a circular calculation that requires iteration.

## See also

<div class="wiki-seealso">

### Closely related

- [Cost of debt](/cost-of-debt/) — the interest rate paid on borrowed funds
- Weighted average cost of capital — the blended discount rate that often embeds tax shield adjustments
- [Discounted cash flow valuation](/discounted-cash-flow-valuation/) — the framework into which tax shields feed
- [Interest coverage ratio](/interest-coverage-ratio/) — whether the company can afford debt and sustain tax benefits
- Capital structure — the mix of debt and equity that determines tax shield magnitude
- [Debt financing](/debt-financing/) — the mechanics of borrowing

### Wider context

- [Corporate income tax](/corporate-income-tax/) — the tax rate that sets shield value
- Leverage ratio — how much debt relative to assets or equity
- [Cost of equity](/cost-of-equity/) — the return demanded by equity investors
- Valuation — the broader discipline of pricing companies

</div>
