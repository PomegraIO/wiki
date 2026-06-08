---
title: "Weighted Average Cost of Capital"
description: "The blended discount rate combining debt and equity costs, weighted by their market values, used in discounted cash flow valuations."
keywords:
  - wacc
  - cost of capital
  - cost of debt
  - cost of equity
  - dcf valuation
image: "/svg/valuation.svg"
---

*The **weighted average cost of capital** (WACC) is the average rate of return required across all sources of a firm's financing—both debt and equity—weighted by their market values. It serves as the discount rate in [discounted cash flow valuation](/discounted-cash-flow-valuation/), reflecting the true opportunity cost of capital deployed in the business.*

## The role of WACC in valuation

Any firm is financed by some mix of [debt financing](/debt-financing/) (bonds, bank loans) and [equity financing](/equity-financing/) (shares issued to investors). Each source carries its own cost. [Debt](/bond/) holders demand a specific [interest rate](/interest-rate/); [equity](/stock/) investors demand a specific return on invested capital.

WACC blends these costs into a single discount rate. Why blend them? Because when you estimate the firm's future [free cash flow](/free-cash-flow/), you're asking: what is this cash stream worth to *all* investors collectively—debt and equity holders together? The discount rate must reflect the blended cost of serving both groups.

A firm financed 50% by debt and 50% by equity, where debt costs 5% and equity costs 10%, has a WACC of 7.5%. That is the threshold return the firm must generate on its assets to satisfy both creditors and shareholders. A project returning less than WACC is value-destructive; above WACC is value-creating.

## Calculating WACC: the formula

The standard formula is:

```
WACC = (E/V × Re) + (D/V × Rd × (1 – Tc))
```

Where:
- **E** = market value of equity
- **D** = market value of debt
- **V** = E + D (total firm value)
- **Re** = [cost of equity](/cost-of-equity/)
- **Rd** = cost of debt (interest rate)
- **Tc** = corporate income tax rate

The tax adjustment matters: interest payments are tax-deductible for the firm. A firm paying 5% on debt in a 25% tax environment effectively pays only 3.75% after tax relief. The debt component thus shrinks, reducing overall WACC.

Example: a $100 million firm with $60 million in equity (value) and $40 million in debt. If equity investors demand 12% return, debt holders demand 6%, and the tax rate is 21%:

```
WACC = (60/100 × 0.12) + (40/100 × 0.06 × (1 − 0.21))
     = 0.072 + 0.01896
     = 0.0910 or 9.10%
```

This firm must generate a 9.1% annual return on its assets to satisfy both stakeholders.

## Estimating cost of equity

The tricky component is **cost of equity** (Re). Unlike debt, where the interest rate is contractual and known, equity cost is implicit. Investors require a return based on risk, but they don't specify it formally.

The standard approach uses the capital asset pricing model (CAPM):

```
Re = Rf + β(Rm − Rf)
```

Where:
- **Rf** = risk-free rate (typically the yield on government bonds)
- **β** = the stock's beta, measuring volatility relative to the market
- **Rm** = expected market return
- **Rm − Rf** = market risk premium (typically 5–7% historically)

A stock with β of 1.5 in a market with 5% risk premium and 3% risk-free rate:

```
Re = 3% + 1.5(7% − 3%) = 3% + 6% = 9%
```

The higher the beta, the higher the cost of equity, reflecting greater risk.

## Estimating cost of debt

Cost of debt is more straightforward: it is the yield-to-maturity on the firm's outstanding bonds, or the blended [interest rate](/interest-rate/) on all debt instruments. For a firm with several bond issues, weight each by its market value.

If a firm has $20 million in bonds yielding 4% and $20 million in loans at 6%, the blended cost of debt is 5%.

A subtlety: use the *market value* of debt, not book value. A bond issued at par (say, $100) but now trading at $110 because interest rates fell has a current cost of debt based on its yield at $110, not the historical $100 issue price.

## Market values matter, not book values

WACC uses **market values**, not balance-sheet book values. A firm with $100 million equity at book value but trading at $200 million market cap should use $200 million in the calculation. Book values are historical artifacts; market values reflect current investor sentiment and opportunity cost.

This creates a logical circularity: to value the firm's [cash flows](/cash-flow-statement/) using DCF, you need WACC, which depends on the firm's equity market value, which is what you're trying to calculate. In practice, analysts iterate: assume a current market value, calculate WACC, run the DCF, and check if the result converges to a consistent value. Most spreadsheet models solve this automatically.

## Sector and risk variations

WACC varies dramatically across sectors. Utilities—stable, low-growth businesses with high debt—might have a WACC of 5–6%. Biotech startups—high-risk, high-cost equity—might have a WACC of 15–20%. The difference reflects real differences in underlying risk: utilities have predictable cash flows and low beta; biotech firms have lumpy cash flows and high beta.

Mature, stable firms can afford more debt because their cash flows support it; startups cannot. WACC embeds this constraint: as a firm takes on more debt, debt becomes riskier (higher Rd), and equity becomes riskier (higher β), so WACC doesn't decline indefinitely as debt increases. There is an optimal capital structure, somewhere in the middle, where WACC is minimized.

## Common WACC mistakes

**Using the wrong tax rate**: Always use the marginal corporate tax rate for the relevant jurisdiction, not the average effective rate. And always deduct it from the debt component, not the whole WACC.

**Ignoring preferred stock**: Firms with preferred shares should treat them as a third financing source, with their own cost, weighted by market value.

**Stale data**: Using historical betas or outdated bond yields is a common error. Recalculate WACC annually, or more often if capital structure changes materially.

**Confusing cost of debt with yield-to-maturity on a single bond**: A firm's cost of debt is the weighted average across all debt instruments, not the rate on one recent issuance.

## WACC as a decision filter

Beyond valuation, WACC is a capital allocation tool. Companies often use a hurdle rate (frequently WACC plus a premium) when evaluating internal projects. A project must exceed WACC to be worth undertaking; anything below just returns the cost of capital—not growth.

For investors, WACC provides a benchmark. If a firm's [return on invested capital](/return-on-invested-capital/) (ROIC) consistently exceeds WACC, it is creating value. If ROIC trails WACC, it is destroying value despite possibly being profitable on an [income statement](/income-statement/) basis.

## See also

<div class="wiki-seealso">

### Closely related

- [Discounted cash flow valuation](/discounted-cash-flow-valuation/) — the primary application of WACC
- [Cost of equity](/cost-of-equity/) — the equity component of WACC
- [Cost of debt](/cost-of-debt/) — the debt component of WACC
- [Unlevered cost of equity](/unlevered-cost-of-equity/) — equity cost stripped of financial leverage

### Wider context

- [Debt financing](/debt-financing/) — use of leverage in firm capitalization
- [Equity financing](/equity-financing/) — use of shares in firm capitalization
- [Return on invested capital](/return-on-invested-capital/) — metric for comparing to WACC
- [Debt-to-equity ratio](/debt-to-equity-ratio/) — capital structure metric

</div>
