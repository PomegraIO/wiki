---
title: "Circular Reference Problem in DCF Models"
description: "Understand how interest expense and debt create circular dependencies in DCF models and the methods to solve them."
keywords:
  - circular reference in dcf interest expense
  - dcf debt schedule
  - iterative solving dcf
  - wacc iteration
image: /svg/valuation.svg
---

*When you value a levered company using DCF, you face a logical trap: to forecast interest expense, you need the debt balance; to forecast the debt balance, you need the net borrowing (or cash returned), which depends on free cash flow; but free cash flow depends on interest expense. The **circular reference in DCF** models arises because the discount rate depends on the target capital structure, which the model is trying to determine. Three practical approaches—iterative solving, WACC iteration, and Adjusted Present Value—break this loop.*

## Why the circularity arises

A straightforward unlevered DCF values a debt-free company: project free cash flow, discount at the unlevered cost of equity, and you have enterprise value. But the moment a firm carries debt, the mechanics tangle.

The debt balance drives interest expense. Interest expense reduces taxable income, creating a tax shield. The tax shield reduces the cost of capital. The reduced cost of capital increases enterprise value. Higher enterprise value might imply a different target debt-to-value ratio, which changes the debt balance, which changes interest expense. Around and around.

In Excel or other spreadsheet models, this typically surfaces as a "circular reference" error: Cell A1 references B1, B1 references C1, and C1 references A1. The software cannot compute a value because it depends on itself.

The circularity is not an error—it is a real feature of valuing a levered firm. The value of a firm with debt depends on the debt level, but the optimal debt level depends on the value. Breaking the loop requires either accepting an iteration, reformulating the problem, or splitting it into pieces.

## The iterative solving approach

The simplest fix in a spreadsheet: enable iterative calculation. Most modern tools (Excel, Google Sheets) can toggle iterative solving under settings. You then set up the model as you naturally would:

1. Assume an opening debt balance (e.g., current debt).
2. Forecast EBIT and tax rates; calculate interest on the opening balance.
3. Project free cash flow: NOPAT (EBIT × (1 − tax rate)) plus depreciation, less capex and working capital changes.
4. Calculate net debt change: FCF minus principal repayment (or plus new borrowing).
5. Update the ending debt balance, which rolls forward as next year's opening balance.
6. Discount the FCF at a WACC derived from the target capital structure.

On the first pass, the model uses the opening debt balance to calculate interest. The result updates the ending debt and feeds into the next year. After 10–50 iterations (depending on convergence settings), the debt schedule stabilizes.

The technique works when the model has a true equilibrium. It fails if you are trying to simultaneously solve for both the target capital structure and the cash flows—or if the cash flows swing wildly based on debt assumptions.

**Pros:** Simple, mirrors real accounting.  
**Cons:** Opaque (you cannot easily see what the converged debt level is), slow on large models, and may not converge if cash flows are highly sensitive to leverage.

## The WACC iteration method

A more transparent approach: instead of iterating the debt balance directly, iterate the WACC. Start with a guessed target [debt-to-equity ratio](/debt-to-equity-ratio/) or [debt-to-value ratio](/debt-to-ebitda-ratio/). Use that to compute an initial WACC.

1. Project unlevered free cash flows (as if the firm were entirely equity-financed).
2. Discount at the guessed WACC.
3. Calculate enterprise value.
4. Apply your target D/V ratio: Debt = Enterprise Value × (D/V), Equity = Enterprise Value × (E/V).
5. Recompute the [cost of debt](/cost-of-debt/) using the implied debt level (or assume it is constant).
6. Recompute WACC.
7. Re-discount the cash flows at the new WACC. If the resulting enterprise value changes, iterate until it converges.

This approach cleanly separates the unlevered cash flow (which does not depend on how you finance it) from the capital structure question. You explicitly control what "target" debt ratio you are assuming. Many practitioners prefer this because it makes assumptions visible.

**Pros:** Transparent assumptions, avoids the circularity of mixing debt and cashflow schedules.  
**Cons:** Adds an extra loop; requires you to make a priori assumptions about target leverage.

## The Adjusted Present Value (APV) approach

APV sidesteps the circularity entirely by splitting valuation into two pieces: the value of an unlevered firm plus the value of the tax shield from debt.

1. Project free cash flow as if the firm were unlevered (no debt, no interest). Discount at the unlevered cost of equity.
2. Separately, calculate the present value of the tax shields. Tax shield in year t = Interest Expense in year t × Tax Rate.
3. Add: Enterprise Value = Unlevered Value + PV(Tax Shields).

The advantage of APV is that you do not need to iterate or guess a capital structure. If the firm has a fixed debt schedule (contractually committed borrowings), you forecast interest deterministically. If the firm is growing and you assume it will always maintain a fixed [debt-to-value ratio](/debt-to-ebitda-ratio/), you can model the tax shields separately.

For highly leveraged or structurally complex firms (e.g., those with warrants, convertibles, or anticipated recapitalizations), APV can be much cleaner.

**Pros:** Avoids circularity, explicit about tax shields, works for non-standard capital structures.  
**Cons:** Requires more discipline in separating unlevered and levered effects; the tax shield calculation is often underestimated or misunderstood.

## When each method is practical

**Use iterative solving** if the firm has a simple, stable capital structure (fixed debt schedule or a modest target leverage ratio) and your spreadsheet tools support it. It is fast and mirrors real balance sheets.

**Use WACC iteration** if you want to assume a target D/V ratio but avoid the complexity of APV. It is transparent and works well for mature, publicly traded firms where you have good debt-cost estimates.

**Use APV** if:
- The firm's debt schedule is contractually fixed (not dependent on value).
- Leverage is changing materially over time.
- The capital structure is nonstandard (e.g., significant preferred equity, contingent convertible debt).
- You are modeling a leveraged buyout (LBO) with an explicit refinancing or exit plan.

## A worked example: iterative WACC

Suppose a firm has current debt of $100 million, EBIT of $50 million, tax rate of 25%, cost of debt of 5%, unlevered cost of equity of 10%, and you assume a target D/E ratio of 0.5 (meaning D/V = 0.333).

**Year 1:**  
Interest Expense = $100M × 5% = $5M  
NOPAT = $50M × (1 − 0.25) = $37.5M  
Suppose FCF = $35M (after depreciation, capex, and working capital).  
Net Debt Change = $35M − (any principal paid). Assume zero principal paid for simplicity; net debt change = $0.  
Ending Debt Balance = $100M + $0 = $100M.

**Compute WACC with D/V = 0.333:**  
Cost of Equity = Unlevered Cost of Equity + (D/E) × (1 − Tax Rate) × (Cost of Debt − Unlevered Cost of Equity)  
= 10% + 0.5 × (1 − 0.25) × (5% − 10%)  
= 10% + 0.5 × 0.75 × (−5%)  
= 10% − 1.875% ≈ 8.125%

WACC = 0.333 × 5% × (1 − 0.25) + 0.667 × 8.125%  
= 0.333 × 3.75% + 0.667 × 8.125%  
= 1.25% + 5.42% ≈ 6.67%

**Discount $35M at 6.67%:**  
PV (Year 1) = $35M ÷ 1.0667 ≈ $32.81M.

Assuming Year 1 repeats indefinitely (perpetuity), Enterprise Value ≈ $32.81M ÷ 6.67% ≈ $492M.

At D/V = 0.333, Debt = $492M × 0.333 = $164M. But we forecasted Debt = $100M. So our assumed D/V was wrong. Re-iterate with the empirical D/V implied by our cash flows.

This loop typically converges in 3–5 passes for stable firms.

## See also

<div class="wiki-seealso">

### Closely related

- [Adjusted Present Value vs WACC DCF](/adjusted-present-value-vs-wacc-dcf/) — alternative formulations both addressing this circularity
- WACC (Weighted Average Cost of Capital) — the discount rate whose calculation may depend on the debt it is discounting
- [Cost of Debt](/cost-of-debt/) — a component of WACC; changes with leverage
- Capital Structure — the debt/equity mix the model is implicitly solving for
- Tax Shield — how debt's tax benefit interacts with cash flows and valuation
- [Debt-to-Equity Ratio](/debt-to-equity-ratio/) — the leverage metric central to the circularity
- [Discounted Cash Flow Valuation](/discounted-cash-flow-valuation/) — the framework where this problem appears

### Wider context

- [Nominal vs Real Cash Flows in DCF](/nominal-vs-real-dcf/) — another consistency issue in DCF models
- [Interest Rate Risk](/interest-rate-risk/) — shapes the cost of debt assumption
- [Leverage Ratio](/leverage-ratio-forex/) — measures the leverage state the model converges toward
- Present Value — foundational time-value concept
- [Sensitivity Analysis in Valuation](/sensitivity-analysis-valuation/) — how to test sensitivity to target D/V assumptions

</div>
