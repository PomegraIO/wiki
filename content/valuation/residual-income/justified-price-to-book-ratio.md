---
title: "Justified Price-to-Book Ratio"
description: "A theoretically derived P/B multiple from fundamentals—ROE, cost of equity, and growth—that anchors valuation in residual income logic."
keywords:
  - justified price to book
  - price to book multiple
  - residual income valuation
  - return on equity
  - cost of equity
image: "/svg/valuation.svg"
---

*The **justified price-to-book ratio** is a theoretical [P/B multiple](/price-to-book-ratio/) derived analytically from a firm's [return on equity (ROE)](/return-on-equity/), [cost of equity](/cost-of-equity/), and long-term growth expectations.*

Instead of using observed market multiples as a starting point for valuation, this approach works backwards from fundamentals. It answers the question: given what we know about a firm's profitability, capital cost, and growth, what P/B multiple is theoretically justified? If the market trades the stock at a P/B below that justified level, it is cheap; above, it is dear. This framework grounds valuation in the [Edwards-Bell-Ohlson model](/edwards-bell-ohlson-model/) and residual income thinking.

## The basic formula

The simplest form, assuming stable growth and no change in profitability, is:

**Justified P/B = (ROE − g) / (Re − g)**

Where:
- **ROE** is return on equity, the firm's net income divided by book equity.
- **Re** is the required return on equity (the cost of equity).
- **g** is the long-term growth rate of the firm.

The formula is intuitive: if ROE exceeds the cost of equity, the firm generates abnormal earnings, justifying a P/B above 1. The larger the spread (ROE − Re), the higher the justified multiple. Higher growth increases the justified P/B because abnormal earnings are compounded forward and then discounted—more growth means those future earnings are larger when discounted back.

The denominator (Re − g) is the "spread" between cost of equity and growth. This is always positive in a sustainable valuation; if Re ≤ g, the formula breaks (growth cannot exceed the cost of capital indefinitely without some value destruction mechanism).

## Where it comes from: residual income logic

The justified P/B emerges naturally from the [Edwards-Bell-Ohlson model](/edwards-bell-ohlson-model/) under simplifying assumptions. If abnormal earnings grow at a constant rate g and perpetually (or near-perpetually), the present value of abnormal earnings equals:

**PV(Abnormal Earnings) = (ROE − Re) × Book Equity / (Re − g)**

Adding this to current book equity and dividing by book equity:

**P/B = 1 + (ROE − Re) / (Re − g) = (ROE − g) / (Re − g)**

This derivation shows that the justified P/B is not arbitrary; it is the direct translation of abnormal earnings into a multiple.

## Interpreting the drivers

Each input shapes the justified P/B clearly:

- **Higher ROE** increases P/B. A firm earning 15% on equity when the cost is 10% justifies a higher multiple than one earning 12%.

- **Higher cost of equity (Re)** decreases P/B. A riskier firm must generate more abnormal earnings to justify any given P/B.

- **Higher growth (g)** increases P/B. Faster growth extends the runway of abnormal earnings, raising their discounted sum.

- **ROE = Re** implies P/B = 1. If the firm earns exactly its cost of capital, it creates no abnormal earnings and the book value, not a premium, is fair.

- **ROE < Re** implies P/B < 1. The firm destroys value, justifying a discount to book. Conversely, if g > ROE, the firm is not sustainable—growth is coming at the cost of future profitability.

## From simple to more realistic models

The simple formula assumes constant ROE, cost of equity, and growth forever. Real analysts adjust:

1. **Forecast explicit abnormal earnings periods.** Instead of assuming perpetual abnormal earnings at current ROE, forecast the next 5–10 years with expected ROE, then assume a terminal ROE (often closer to the cost of equity, reflecting mean reversion).

2. **Adjust for leverage and risk.** ROE can be inflated by leverage; a levered firm's ROE is not comparable to an unlevered peer's. Some practitioners strip out the leverage effect or forecast ROE net of changing leverage.

3. **Use explicit forecasts of dividend payout and growth.** Sustainable growth is closely tied to retention: g = ROE × (1 − payout ratio). If a firm is paying out 50% of earnings and earning 12% on equity, long-term growth is roughly 6%, not the cost of equity. The formula implicitly assumes this link.

4. **Two-stage models.** A two-stage justified P/B assumes high abnormal earnings (and high P/B) in years 1–5, then reversion to stable-growth P/B thereafter:

   **Justified P/B = PV(Abnormal Earnings, Years 1–5 at forecast ROE) / Book Equity + PV(Terminal P/B × Book Equity in Year 5) / Book Equity**

   The terminal P/B is often calculated using the simple formula with lower ROE and lower growth.

## Comparison with market P/B

Practitioners use justified P/B as a valuation check. If a stock trades at P/B = 2.5 but fundamentals justify only P/B = 1.8, the stock is overvalued by about (2.5 − 1.8) / 1.8 ≈ 39%.

This comparison is powerful because P/B multiples are observable, comparable across peers, and less noisy than earnings-based multiples in cyclical industries. It also forces the analyst to articulate assumptions about ROE, cost of equity, and growth in a single, transparent metric.

## Sensitivity and limits

The justified P/B is sensitive to all three inputs, but especially to cost of equity and long-term growth. Small changes to Re or g can swing the justified multiple widely. In practice:

- A 1% rise in cost of equity (from 10% to 11%) can halve the justified P/B, depending on ROE and g.
- Uncertainty about terminal ROE (will competitive advantage persist, or will it fade to the cost of capital?) is often the largest source of valuation disagreement.

The formula also assumes the firm pays dividends or retains earnings consistently with the growth rate. If dividend policy is erratic or capital structure is shifting, the mechanical link between growth and retention breaks.

The model works poorly for firms with negative equity (debt exceeds assets) or negative earnings, where ROE and P/B are both undefined or inverted. High-growth, pre-profitability firms also strain the model, because current ROE is often negative or near-zero, making the formula problematic.

## Sector and industry patterns

Justified P/B multiples vary dramatically by industry:

- **Utilities and REITs** often have P/B near 1, since ROE is close to the cost of equity and growth is modest.
- **Banks** have P/B typically in the range 1–2, reflecting modest spreads between ROE (often 10–12%) and cost of equity (also often 10–12%).
- **Technology and growth companies** can have justified P/B of 5, 10, or higher if ROE is very high (20%+) and growth is strong.
- **Cyclical industrials** have lower justified P/B on average, since normalized ROE is often only marginally above the cost of capital.

Comparing a stock's justified P/B to sector peers is a useful reality check; if one firm's multiple is a stark outlier, it signals either an exceptional investment case or a forecast error.

## Relation to other valuation approaches

The justified P/B is a sibling of the [economic profit valuation](/economic-profit-valuation/) framework and the [Edwards-Bell-Ohlson model](/edwards-bell-ohlson-model/). All three value equity using fundamentals and abnormal returns. They differ in starting point and accounting treatment:

- **EBO** starts with book equity and adds the PV of abnormal earnings.
- **Economic profit** starts with invested capital and the PV of economic profit above WACC.
- **Justified P/B** works backward from P/B to infer the implied abnormal earnings and ROE assumptions.

All three should converge to the same valuation if assumptions are consistent.

## See also

<div class="wiki-seealso">

### Closely related

- [Edwards-Bell-Ohlson Model](/edwards-bell-ohlson-model/) — the theoretical framework underlying justified P/B
- [Economic Profit Valuation](/economic-profit-valuation/) — the enterprise-wide version of residual income valuation
- [Clean Surplus Relation](/clean-surplus-relation/) — the accounting link enabling consistent valuation
- [Return on Equity](/return-on-equity/) — the ROE driver of justified P/B
- [Cost of Equity](/cost-of-equity/) — the discount rate and hurdle
- [Price-to-Book Ratio](/price-to-book-ratio/) — the observable multiple being justified
- Residual Income — the economic concept underlying the formula

### Wider context

- [Price-to-Earnings Ratio](/price-to-earnings-ratio/) — an alternative valuation multiple
- [Discounted Cash Flow Valuation](/discounted-cash-flow-valuation/) — the DCF alternative
- [Value Investing](/value-investing/) — investment philosophy aligned with fundamental valuation
- [Growth Investing](/growth-investing/) — investment style emphasizing ROE and growth
- Competitive Advantage — the source of persistent abnormal earnings

</div>
