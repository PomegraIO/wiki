---
title: "Price Value of a Basis Point vs DV01"
description: "Clarify the conceptual and sign differences between PVBP and DV01, and when the distinction matters in fixed-income hedging and risk."
keywords:
  - price value of a basis point vs dv01
  - pvbp dv01 difference
  - dv01 bond risk metric
  - pvbp fixed income hedging
  - basis point price value
image: "/svg/fixed-income.svg"
---

*The **price value of a basis point** (PVBP) and **DV01** (dollar value of 1 basis point) are both metrics that measure how much a bond's price changes when yields shift by one basis point. Though practitioners often treat them interchangeably, they differ subtly in definition, sign convention, and practical application. Understanding the distinction prevents hedging errors and clarifies intent in risk conversations.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">PVBP vs DV01 — key facts</div>

<img src="/svg/fixed-income.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Both measure bond price sensitivity to a 1 bp yield move; sign and scope differ subtly.</div>

|   |   |
|---|---|
| **PVBP definition** | Absolute dollar change in bond price for a 1 bp parallel shift in yield curve. Often unsigned. |
| **DV01 definition** | Dollar value change per 1 bp move, often signed to show direction: negative if yields rise and price falls. |
| **When they're same** | For many purposes, practitioners treat PVBP and DV01 as identical; both measure the same [duration](/duration/) effect. |
| **When they differ** | Sign convention, scope (single bond vs. portfolio), and whether convexity is factored in explicitly. |
| **Alternative name** | PVBP is sometimes called "basis point value" (BPV) or "price value of 1 bp" (PV01). |
| **Practical use** | Both are shortcuts for [duration](/duration/)-based [sensitivity analysis](/sensitivity-analysis-valuation/); DV01 is more common in trading desks and hedge funds. |

</aside>

## Definitions and the sign question

**Price Value of a Basis Point (PVBP)** is most precisely defined as the absolute dollar change in a bond's price when the yield-to-maturity (or yield curve) shifts by exactly 1 basis point (0.01%), holding all other factors constant. Because it is expressed as a dollar amount without a sign, PVBP is inherently a magnitude: it tells you "the bond's price will move by X dollars per 1 bp of yield shift," but does not specify direction.

Example: A 10-year corporate bond with a PVBP of USD 850 means the bond price changes by USD 850 when yields move 1 bp. If yields fall 1 bp, price rises USD 850; if yields rise 1 bp, price falls USD 850.

**DV01** (dollar value of 1 basis point) is conceptually identical but often carries a sign. Under the sign convention most common on trading floors, DV01 is negative if yields rise, and the bond's price falls. A bond with DV01 of –USD 850 explicitly signals that a 1 bp increase in yield causes a USD 850 loss (price decline). Conversely, a long bond position might be quoted as DV01 = +USD 850, indicating that a 1 bp yield decrease is a gain.

In practice, however, many traders and risk managers use "DV01" and "PVBP" interchangeably and specify direction separately: "DV01 is 850; duration is 8.5 years; price risk is down 850 per 1 bp of yield increase." The sign convention is context-dependent.

## Calculation and the duration approximation

Both PVBP and DV01 are easiest to calculate using [duration](/duration/), a first-order measure of price sensitivity.

For a bond with modified [duration](/duration/) D (in years), the approximate price change per 1 basis point move in yield is:

**ΔPrice ≈ –D × Price × 0.0001**

Rearranging to isolate the dollar change per 1 bp:

**DV01 (or PVBP) ≈ D × Price / 10,000**

**Example:** A bond trading at USD 102 per USD 100 of par (102% of par, or USD 1,020 per bond) with modified duration of 8.5 years has:

DV01 = 8.5 × 1,020 / 10,000 = 0.8670 per bond, or approximately USD 867 per million dollars of face value.

This calculation assumes a parallel shift in yields (all maturities move by the same amount) and ignores convexity (the nonlinear second-order effect). For small yield moves, the approximation is tight; for large moves, convexity becomes material, and DV01 / PVBP alone understates price sensitivity if the bond is short (convex, so it benefits from big moves either direction) or overstates it if the bond is long and far out-of-the-money.

## When the distinction matters

**Sign convention in portfolios.** If you hold USD 10 million of a bond with DV01 = –USD 850 (per USD 1 million of face), your portfolio DV01 is –USD 8,500. A 1 bp yield rise costs you USD 8,500. If you want to hedge, you might sell short USD 10 million of a shorter-duration bond with DV01 = –USD 500 per USD 1 million, giving you DV01 = +USD 5,000. Your net portfolio DV01 is now –USD 3,500, reducing (but not eliminating) your interest-rate risk.

Without careful sign tracking, a hedge can become a double bet instead. Losing the sign is a common operational risk on trading desks.

**Scope and aggregation.** PVBP historically referred to a single bond; DV01 is more flexible and often applied to a portfolio or strategy. When discussing portfolio risk, "our FX-hedged corporate bond fund has a DV01 of +USD 2 million" is clearer than "PVBP is USD 2 million," because DV01 explicitly conveys net directional exposure across multiple holdings.

**Convexity and large moves.** A bond with positive convexity (most plain-vanilla bonds) benefits from large yield moves in either direction. PVBP / DV01 captures only duration, the linear effect. For a position that must be hedged against a 100 bp move (not just 1 bp), separately accounting for convexity is prudent. An explicitly convexity-adjusted risk metric (sometimes called "gamma" on trading floors, borrowing from options terminology) quantifies the nonlinear gain or loss.

## Practical usage across markets

**Equity-linked and credit derivatives.** In credit [default swap](/credit-default-swap/) markets, DV01 is the standard. A CDS position is quoted as "DV01 = USD 1,000 per 1 bp of spread move," meaning a 1 bp widening of the credit spread costs USD 1,000. This is directional by default: long a CDS is long volatility / long credit spread, so DV01 is naturally negative from the perspective of credit improvement.

**Treasury and government bond trading.** DV01 is ubiquitous on government bond desks. "The 10-year is trading at DV01 of 860" is shorthand. Risk managers aggregate DV01 across the entire portfolio (treasuries, corporates, emerging-market debt) to understand net duration exposure and hedge via [futures contracts](/futures-contract/) (Treasury futures have standardized DV01 per contract).

**Municipal and corporate bond markets.** Smaller bond desks may use "PVBP" as the older terminology, but the meaning is identical. Both terms are acceptable; the real requirement is clarity about whether the metric is signed or unsigned and what basis (parallel shift, key-rate duration, etc.) underlies the calculation.

## Common pitfalls and best practices

**Confusing absolute and signed metrics.** A trader who says "the bond has a DV01 of 850" without specifying sign or context can cause confusion. Clarify: "The bond is long; a 1 bp yield decline gains USD 850" is unambiguous. "Long 850 DV01 in the 10-year" is also clear (position is long duration risk).

**Forgetting to scale for position size.** DV01 / PVBP is often quoted per USD 1 million of face value or per individual bond. Always scale to your actual position size. If you hold USD 50 million of a bond with DV01 = USD 850 per USD 1 million, your total DV01 is USD 42.5 million, not USD 850.

**Ignoring convexity for large moves.** A 1 bp move is small; DV01 is accurate. A 100 bp parallel shift is large; convexity becomes material. A bond with positive convexity (price accelerates upward as yields fall) outperforms DV01-based estimates. A bond or liability with negative convexity (price decelerates; e.g., a [mortgage-backed security](/mortgage-backed-security/) facing [prepayment risk](/prepayment-risk/)) underperforms.

**Treating PVBP as a hedge ratio directly.** If you want to hedge a USD 10 million long bond position (DV01 = USD 8,500) using Treasury [futures contracts](/futures-contract/) (each contract has DV01 ≈ USD 800), you need to short roughly 10–11 contracts, not use DV01 as a raw weight. Account for basis risk, daily [mark-to-market](/mark-to-market/), and the convexity mismatch between the position and the hedge.

## See also

<div class="wiki-seealso">

### Closely related

- [Duration](/duration/) — The foundational measure of bond price sensitivity to yield changes.
- [Modified Duration](/duration/) — Duration adjusted for yield level; basis of DV01 / PVBP calculation.
- Convexity — The second-order price sensitivity that DV01 alone does not capture.
- [Sensitivity Analysis](/sensitivity-analysis-valuation/) — Broader framework for understanding how prices respond to parameter shifts.
- [Yield-to-Maturity](/yield-to-maturity/) — The discount rate underlying bond pricing and duration.

### Wider context

- [Bond](/bond/) — Overview of bond mechanics and pricing.
- Fixed Income — Bond market fundamentals and strategies.
- [Interest Rate Risk](/interest-rate-risk/) — How rate changes affect bond portfolios.
- [Hedging](/derivatives-hedging/) — Using futures and swaps to manage interest-rate exposure.
- [Credit Default Swap](/credit-default-swap/) — Where DV01 is the standard risk metric.

</div>
