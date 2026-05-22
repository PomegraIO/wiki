---
title: "Macaulay Duration"
description: "Weighted-average time to recover principal from a bond, measured in years; foundational metric for interest rate sensitivity."
keywords:
  - macaulay duration
  - bond duration
  - weighted average maturity
  - bond math
  - time to principal
---

*The **Macaulay duration** of a bond is the weighted-average time in years until all cash flows (coupons and principal) are received, with each cash flow weighted by its present value. It is a measure of when, on average, you recover your investment—and a rough proxy for how much a bond's price moves if interest rates change.*

<aside class="wiki-infobox">

| Aspect | Detail |
|---|---|
| **Inventor** | Frederick Macaulay (1938) |
| **Unit** | Years (decimal) |
| **Formula** | ∑ [t × PV(Cash Flow_t)] / Current Price |
| **Typical Range** | 2–20+ years (higher for long-dated bonds) |
| **Key Use** | Estimating bond price sensitivity to [interest rate](/wiki/interest-rate/) changes |
| **Variation** | [Modified duration](/wiki/modified-duration/) is the market standard; Macaulay duration is the underlying concept |

</aside>

## Intuition and calculation

Imagine a 5-year bond paying 4% annual coupon and yielding 4%. Each year you receive $40, plus $1,000 principal at year 5. Macaulay duration weights each cash flow by its present value and its time to receipt.

Year 1: $40 PV = $38.46, weight = 1 year  
Year 2: $40 PV = $36.98, weight = 2 years  
Year 3: $40 PV = $35.56, weight = 3 years  
Year 4: $40 PV = $34.19, weight = 4 years  
Year 5: $1,040 PV = $854.80, weight = 5 years  

Total PV = $1,000 (the bond price)

Macaulay duration = (1×38.46 + 2×36.98 + 3×35.56 + 4×34.19 + 5×854.80) / 1,000 ≈ 4.64 years.

This bond's cash flows are not evenly distributed. Most of the value comes at year 5 (the principal repayment), so the weighted-average time to get your money back is 4.64 years—less than the full 5-year maturity, but closer to it than to an equal-coupon distribution.

## Relationship to interest rate sensitivity

The reason Macaulay duration matters for bond traders and investors is that it approximates **modified duration**, the percentage price change per 1% move in [yield](/wiki/current-yield/).

Modified duration ≈ Macaulay duration / (1 + yield)

For the 4% bond above:
Modified duration ≈ 4.64 / 1.04 ≈ 4.46 years.

This means if yields rise from 4% to 5% (a 1 percentage point increase), the bond's price falls approximately 4.46%. If yields fall to 3%, the price rises approximately 4.46%.

The relationship is linear and useful for quick estimates. It is why long-duration bonds are more volatile: a 30-year Treasury with duration 15 loses 15% if rates rise 1%; a 2-year Treasury with duration 1.9 loses only 1.9%.

## Duration vs. maturity

Macaulay duration is always *less than* maturity (except for zero-coupon bonds, where they are equal) because coupon payments received before maturity reduce the weighted-average time to final cash recovery.

- **Zero-coupon bond**: Macaulay duration = maturity (all cash comes at the end).
- **Coupon bond**: Macaulay duration < maturity (interim coupons accelerate average recovery time).
- **Higher coupon → lower duration**: A 10% bond has lower duration than a 2% bond of the same maturity because more cash comes early.
- **Higher yield → lower duration**: A bond yielding 8% has lower duration than the same bond yielding 3% because future cash flows are discounted more heavily.

## Application: Portfolio matching and ALM

Asset-liability matching (ALM) in pension funds and insurance companies relies on duration. A pension fund with liabilities (pension payments due) in 10 years might buy bonds with 10-year duration, ensuring that asset values move in lockstep with liability values as rates shift.

If the fund buys a bond with 8-year Macaulay duration, it is short by 2 years: if rates rise, the liability value (present value of future payouts) falls, but the asset value falls more. Duration matching eliminates this mismatch.

## Limitations

Macaulay duration assumes:

1. **Flat yield curve**: If the yield curve is steep (long-term rates much higher than short-term), the approximation breaks down.
2. **No call/put features**: A [callable bond](/wiki/callable-bond/) has negative [convexity](/wiki/convexity/); as rates fall and the bond moves toward being called, duration decreases, not increases. Macaulay duration ignores this optionality.
3. **Parallel shift in yields**: If different parts of the curve move different amounts, duration approximation is less precise.
4. **Small yield changes**: For large moves (>1%), [convexity](/wiki/convexity/) becomes material; the linear approximation errs.

For these reasons, practitioners also compute [modified duration](/wiki/modified-duration/) and [effective duration](/wiki/effective-duration/). Modified duration is the market standard for simple bonds; effective duration handles embedded options.

## Historical context

Frederick Macaulay introduced the concept in 1938 in "Some Theoretical Problems Suggested by the Movements of Interest Rates, Bond Yields and Stock Prices in the United States since 1856." His insight was that a bond's sensitivity to rate changes depends not just on maturity but on when you get paid. This formalization underpinned modern [fixed-income](/wiki/fixed-income-etf/) portfolio management and risk measurement.

Today, the term "duration" (used interchangeably with "modified duration" in practice) is ubiquitous. But Macaulay duration remains the conceptual foundation: it answers the question "when do I get my money back?" Duration answers "how much does my bond's price move if rates change?"—which is what matters to traders but is derived from Macaulay's earlier framework.

## Practical calculation

Most [fixed-income analytics](/wiki/fixed-income-fund-strategy/) platforms (Bloomberg, FactSet, Charles Schwab) compute duration automatically. Bond issuers disclose it in prospectuses. For a portfolio of bonds, [duration](/wiki/duration/) is the weighted average of individual bond durations, making it easy to benchmark against an index (e.g., a [bond fund](/wiki/bond-etf/) might have 5.5-year duration against an index duration of 5.2 years).

<div class="wiki-seealso">

### Closely related

- [Modified duration](/wiki/modified-duration/) — The practical application; Macaulay duration / (1 + yield).
- [Effective duration](/wiki/effective-duration/) — Version handling embedded options and curve shifts.
- [Convexity](/wiki/convexity/) — Second-order price sensitivity; fills in where duration approximation fails.

### Wider context

- [Duration](/wiki/duration/) — Umbrella term; often used to mean modified duration.
- [Interest rate risk](/wiki/interest-rate-risk/) — The risk Macaulay duration helps quantify.
- [Bond price formula](/wiki/bond-price-formula/) — Underlying discounted cash flow math.

</div>
