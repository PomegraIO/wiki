---
title: "In-Arrears Swap"
description: "A floating-rate swap where the reference rate is observed and fixed at the end of each accrual period, rather than at the beginning."
keywords:
  - in-arrears swap
  - floating-rate swap
  - interest rate derivative
  - arrears setting
image: "/svg/derivatives.svg"
---

*An **in-arrears swap** is a variant of a standard [interest rate swap](/interest-rate-swap/) in which the reference [rate](/interest-rate/) is set at the end of each accrual period rather than the beginning. This timing difference creates a payment lag and introduces subtle but economically meaningful changes to [interest rate risk](/interest-rate-risk/), convexity, and dealer pricing compared to a plain-vanilla swap.*

## Standard swaps versus in-arrears

In a conventional (spot-start) swap, the floating rate is fixed on day one of each interest period. A quarterly floating payment might be set on 15 January for the 90-day period running 15 January through 15 April. On 15 April, that rate and the accrued interest are paid.

In an in-arrears swap, the rate is not observed until 15 April—the final day of the accrual period. Only then do both counterparties learn what the payment will be, and it is paid immediately. This creates a one-period lag in knowledge and settlement.

The mechanics sound like a small technicality, but they reshape the derivative's sensitivity to interest rate moves. An in-arrears swap embedded in a floating-rate note or paid by a borrower can materially alter cash flow timing and the effective [duration](/duration/) of the position.

## Why the timing matters: convexity

The key insight is convexity. When a floating rate is set in advance, a rise in short-term rates between setting and payment affects the next period's coupon, not the current one. The interest income is partly insulated from the rate shock, which is the essence of a floating-rate hedge.

In an in-arrears structure, a sudden rise in rates at the end of the period directly increases the coupon being paid *in that same period*. An investor receiving a floating in-arrears coupon benefits from the rate spike *and* earns higher interest on that higher coupon (since it's paid at period end). This creates a small second-order gain—positive convexity.

Conversely, an investor paying a floating in-arrears coupon suffers twice: the higher rate is observed just as it must be paid, and that higher payment is made immediately without any offsetting compensation. This is negative convexity from the payer's perspective.

Mathematically, the convexity adjustment is proportional to the volatility of rates, the length of the accrual period, and the second derivative of the swap's price with respect to rates. It is typically small—perhaps 1–5 basis points for USD [LIBOR](/libor/) swaps—but non-negligible for high-volatility periods or long accrual periods.

## Pricing and valuation

A dealer pricing an in-arrears swap must forecast two things: the expected rate path and the expected convexity cost. The standard approach uses a model such as Black–Karasinski or a [volatility smile](/volatility-smile/) framework that captures how forward rates and rate volatility vary with time and moneyness.

The dealer will quote an in-arrears swap at a slightly different [swap rate](/interest-rate-swap/) than a spot-start swap of the same tenor. If rates are volatile, the convexity cost is higher, and the in-arrears payer's rate will be wider (more expensive to the payer) than a normal swap. A receiver's rate will be tighter (cheaper) because the receiver benefits from the convexity.

Valuation is not straightforward. A simple bond pricing model does not capture the embedded optionality. Monte Carlo simulation is standard, running thousands of interest rate paths and computing the payoff at each period end, then discounting. For practitioners, pre-built analytics from dealers or software vendors (such as Bloomberg or Numerix) are the practical route.

## Real-world applications

In-arrears swaps appear most often in corporate and mortgage financing. A floating-rate note might pay LIBOR-plus-spread in-arrears to simplify administration and reduce the issuer's refunding risk: if rates rise sharply near the end of a coupon period, the issuer does not face an unexpected jump in the *next* payment—it has already been committed. This appeals to treasurers managing liquidity tightly.

Banks also use in-arrears swaps as part of their [asset-liability management](/balance-sheet/). A loan portfolio that pays in arrears naturally pairs with an in-arrears receive-fixed swap, creating an economic hedge without basis risk from a timing mismatch.

Fixed-income traders occasionally use in-arrears forwards on short-term rates (like overnight rates) to express views on period-end rate levels. Because the payoff is determined so late, the convexity adjustment can be a source of relative value: if consensus is too bullish on future volatility, the in-arrears rate will be too wide, and a trader can short it and profit if volatility disappoints.

## Variants and complications

A *daily reset in-arrears swap* resets the reference rate daily but pays only at period end. This introduces even more convexity because the daily rates are path-dependent. A *one-day in-arrears* variant on overnight rates has become increasingly common post-LIBOR reform, as [SOFR](/sofr/) (the replacement for LIBOR) is itself an overnight rate published in arrears.

A *leveraged in-arrears* swap multiplies the floating leg by some factor (say 1.5×). This amplifies both the benefit (if you're receiving) and the cost (if you're paying) of the convexity adjustment.

The in-arrears feature also interacts with [credit risk](/credit-risk/) measurement. Since the cash flow size is not known until the period end, counterparties cannot fully calculate credit exposure mid-period using standard formulas. Risk systems must either assume worst-case rates or run simulations, complicating daily margin calculations and regulatory capital charges.

## Risks and market conditions

In-arrears swaps perform poorly (for payers) during sharp, unexpected rate hikes. The 2022 US Federal Reserve rate hiking cycle saw periods of multiple consecutive 75-basis-point hikes. Investors locked into in-arrears payer swaps faced steadily rising coupons and mounting losses. The convexity cost was no longer theoretical—it was paid in blood.

Conversely, during a rate decline, an in-arrears receiver sees improving economics. The payer sees worse; they pay less because rates have fallen, and they miss the gain from the reduced payment being delivered earlier.

Another consideration is optionality embedded elsewhere. An in-arrears swap embedded in a callable bond or a cap/floor agreement can create unintended interactions if the optionality is also triggered late in the period.

## See also

<div class="wiki-seealso">

### Closely related

- [Interest Rate Swap](/interest-rate-swap/) — The foundational swap, exchanging fixed and floating cash flows.
- [Duration](/duration/) — A bond's sensitivity to interest rate changes, measured as a weighted time to cash flow.
- [Volatility Smile](/volatility-smile/) — The pattern that implied volatility varies with strike price and moneyness.
- [Quanto Swap](/quanto-swap/) — A swap that hedges currency exposure while referencing a foreign index.
- [Dividend Swap](/dividend-swap/) — A swap on realised dividend payments over time.

### Wider context

- [Interest Rate Risk](/interest-rate-risk/) — The exposure that bond and loan values fluctuate with rate changes.
- [LIBOR](/libor/) — The London Interbank Offered Rate, historically the standard floating benchmark.
- [SOFR](/sofr/) — The Secured Overnight Financing Rate, the modern replacement for LIBOR.
- [Credit Risk](/credit-risk/) — The risk that a counterparty defaults on its obligations.
- [Asset-Liability Management](/balance-sheet/) — Managing a firm's balance sheet to match assets and liabilities.

</div>