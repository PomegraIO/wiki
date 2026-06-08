---
title: "Economic Profit Valuation"
description: "A framework valuing firms by discounting the profit that remains after charging for all capital used, both debt and equity."
keywords:
  - economic profit
  - residual income valuation
  - nopat
  - abnormal earnings
  - cost of capital
image: "/svg/valuation.svg"
---

*The **economic profit valuation** framework (also called economic value added or EVA valuation) values a firm as the present value of profits earned *after* deducting the full cost of all capital invested—debt and equity alike.*

This approach extends the residual income idea beyond equity to the entire firm. While the [Edwards-Bell-Ohlson model](/edwards-bell-ohlson-model/) values equity using [book equity](/balance-sheet/) and abnormal earnings to shareholders, economic profit valuation values the entire enterprise using invested capital and the profit above the weighted average cost of capital (WACC). It is the framework underlying most consulting-led value-creation mandates and some institutional investment disciplines.

## The core calculation: NOPAT minus capital charge

Economic profit in a given period is:

**Economic Profit = NOPAT − (Invested Capital × WACC)**

Where:
- **NOPAT** is net operating profit after tax: the operating earnings of the firm as if it were entirely equity-financed, before payments to debt or equity holders.
- **Invested Capital** is the net assets deployed (both debt and equity): total assets minus non-interest-bearing liabilities.
- **WACC** is the weighted average cost of capital—the blended required return on all capital, debt and equity combined.

The insight is straightforward: if a firm generates £100m in operating profit, deploys £1bn of capital, and faces a 9% cost of that capital (WACC), then the capital *cost* is £90m. The economic profit is £10m—the surplus above cost, which accrues to investors (implicitly to equity, after debt holders are paid their required return).

This is distinct from [net income](/income-statement/), which deducts interest expense (a cost of debt) but does not deduct the required return on equity. Economic profit is more comprehensive: it is profit *after* paying cost for every pound of capital.

## From period profit to firm value

Economic profit is a period measure. To value the firm, the analyst forecasts economic profit over a planning horizon and discounts it to present value, then adds the continuing (terminal) value:

**Firm Value = PV(Forecast Economic Profit, Years 1–T) + PV(Terminal Economic Profit)**

The discount rate is the WACC itself. The terminal value usually assumes economic profit converges to zero (in competitive equilibrium) or stabilizes at a long-term level (if the firm enjoys durable competitive advantage).

This is similar to free cash flow [DCF](/discounted-cash-flow-valuation/) in spirit but uses a different profit measure. Instead of cash flow, the analyst works with accrual earnings, adjusted to remove capital-related non-cash items and charged a capital cost. This can be cleaner when working with historical accounting data, since capital intensity, depreciation, and working-capital swings are bundled into the capital base and WACC.

## NOPAT construction

Calculating NOPAT requires care. The standard approach is:

1. Start with earnings before interest and tax (EBIT) from the income statement.
2. Multiply by (1 − tax rate) to get NOPAT: EBIT × (1 − Tc), where Tc is the marginal corporate tax rate.

This strips out interest and tax, leaving the operating profit as if the entire firm were equity-financed. Some practitioners start from net income and add back after-tax interest expense (interest × (1 − Tc)), which is equivalent.

The tax rate is critical. Using the statutory rate can be misleading; better to use the firm's effective or marginal tax rate, especially if the firm has loss carryforwards, tax credits, or operates in jurisdictions with varying rates.

## Invested capital: net operating assets

Invested capital is the net operating asset base—everything deployed to run operations, financed by a mix of debt and equity:

**Invested Capital = Operating Assets − Operating Liabilities**

Operating assets include cash needed for operations, accounts receivable, inventory, fixed assets, and goodwill. Operating liabilities include accounts payable and accrued expenses. *Non-operating* items (excess cash, debt, equity) are excluded; they are the financing side, not the investment side.

Alternatively:

**Invested Capital = Debt + Equity − Excess Cash**

Invested capital is typically calculated from the balance sheet, but averaging beginning and ending balances (or using mid-period snapshots) improves accuracy when balance sheets change materially during the year.

## WACC as the discount rate

The weighted average cost of capital is:

**WACC = (E / V) × Re + (D / V) × Rd × (1 − Tc)**

Where:
- E is market value of equity, D is market value of debt, V = E + D.
- Re is the required return on equity (often estimated via CAPM).
- Rd is the cost of debt (often approximated by the yield on the firm's bonds).
- Tc is the marginal tax rate.

WACC is both the discount rate and the hurdle rate: if economic profit is positive, the firm is creating value; if negative, it is destroying value. This dual role makes WACC central to the framework.

## Economic profit vs. accounting profit

Economic profit differs from both net income and operating profit:

- **Net income** includes interest expense, which is a cost of debt, not capital cost. A highly leveraged firm with negative net income can still generate positive economic profit if operating earnings exceed the WACC hurdle.

- **Operating profit (EBIT)** ignores both tax and the required return on capital. It can be high without creating economic value.

- **Economic profit** deducts both tax and the full cost of all capital. Only true surplus profit survives.

This distinction is the source of the framework's power. It forces management focus on the spread between return on capital and cost of capital—the true measure of value creation.

## Sensitivity to WACC and capital base

Economic profit valuation is highly sensitive to assumptions about WACC and the capital base forecast. Small changes to the cost of capital compound heavily over a long forecast horizon. If WACC is 8% and the analyst re-estimates it as 8.5%, the present value of future economic profits falls sharply.

Similarly, forecasting invested capital is crucial but often difficult. Capital intensity, depreciation policy, and growth rates all affect the capital base. Mature, stable firms with modest capital needs are easier to forecast than rapidly growing or cyclical businesses.

Terminal value assumptions are especially critical. If the analyst assumes economic profit persists indefinitely, the terminal value can dominate the intrinsic valuation. Most practitioners assume economic profit reverts to zero (competitive advantage fades) or stabilizes at a low perpetual level, which is more conservative.

## When the framework works best

Economic profit valuation shines in capital-intensive industries with relatively stable profitability: utilities, railroads, telecommunications, and mature financial institutions. It also works well for conglomerates with multiple business units, each with a distinct capital base and return profile, because the framework naturally disaggregates value by unit.

It is less natural for high-growth technology or biotech firms, where the capital base may be tiny (mostly human capital, not balance-sheet assets) and forecasting long-term competitive advantage is speculative.

## Link to P/B and other multiples

Economic profit valuation also grounds the [justified price-to-book ratio](/justified-price-to-book-ratio/). If a firm's expected economic profit, discounted and amortized against invested capital, implies a value 1.5× invested capital, then the P/B multiple should be 1.5. This link is powerful because P/B multiples are observable and comparable across peers—the framework provides theoretical justification for market-traded multiples.

## See also

<div class="wiki-seealso">

### Closely related

- [Edwards-Bell-Ohlson Model](/edwards-bell-ohlson-model/) — the equity-focused residual income framework
- [Clean Surplus Relation](/clean-surplus-relation/) — the accounting link enabling consistent profit measurement
- [Justified Price-to-Book Ratio](/justified-price-to-book-ratio/) — deriving P/B multiples from economic profit
- [Weighted Average Cost of Capital](/weighted-average-cost-of-capital/) — the discount rate and hurdle in the framework
- [Return on Invested Capital](/return-on-invested-capital/) — the return metric compared against cost of capital
- [Cost of Equity](/cost-of-equity/) — component of WACC
- [Cost of Debt](/cost-of-debt/) — component of WACC

### Wider context

- [Discounted Cash Flow Valuation](/discounted-cash-flow-valuation/) — an alternative fundamental framework
- [Net Operating Income](/net-operating-income/) — operating profit before capital charges
- [Balance Sheet](/balance-sheet/) — where invested capital is measured
- [Price-to-Book Ratio](/price-to-book-ratio/) — the market multiple the framework explains
- [Value Investing](/value-investing/) — investment philosophy aligned with fundamental value frameworks

</div>
