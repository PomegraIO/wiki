---
title: "Yield to Worst"
description: "The lowest possible yield an investor can receive on a callable or putable bond, accounting for all early-redemption scenarios."
keywords:
  - callable bond
  - bond yield
  - bond valuation
  - embedded option
image: "/svg/fixed-income.svg"
---

*A **yield to worst** is the lowest [yield](/interest-rate/) that an investor can receive on a [callable bond](/callable-bond/) or putable bond before maturity, computed by evaluating redemption at each date the issuer (or bondholder) can exercise the [embedded option](/option/). It is a conservative measure that assumes the scenario most disadvantageous to the bondholder.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Yield to Worst — key facts</div>

<img src="/svg/fixed-income.svg" alt="An abstract editorial mark for the fixed-income category." />

<div class="wiki-infobox-caption">A conservative yield metric that reflects the issuer's most advantageous redemption scenario.</div>

|   |   |
|---|---|
| **What it is** | The minimum [yield](/interest-rate/) possible on a [callable bond](/callable-bond/) or putable bond across all early-exercise scenarios |
| **Also called** | Worst-case yield |
| **Accounts for** | [Call dates](/callable-bond/), [put dates](/yield-to-put/), maturity |
| **Used by** | Bond investors, portfolio managers, [fixed income](/interest-rate/) analysts |
| **Key insight** | Reflects what investors actually receive in worst-case market conditions |
| **Compared to** | [Yield to call](/callable-bond/), [yield to maturity](/yield-to-maturity/) |

</aside>

## Why yield to worst matters

When a [bond](/bond/) includes [embedded options](/option/)—most commonly a [call option](/call-option/) held by the issuer or a [put option](/put-option/) held by the bondholder—the investor's actual return depends on whether and when those options are exercised. A simple [yield to maturity](/yield-to-maturity/) calculation assumes the bond is held to final maturity, but that assumption may be economically unrealistic.

If interest rates fall sharply, an issuer holding a [call option](/call-option/) will almost certainly refinance: it pays off the bondholder and issues new bonds at lower rates, capturing the economic benefit. The bondholder's return is capped at the [coupon](/coupon-payment/) received up to the call date plus any capital appreciation—less than if the bond had run to maturity. Conversely, if rates rise, the bondholder is stranded holding a below-market coupon. In either case, a naive [yield to maturity](/yield-to-maturity/) figure is misleading.

Yield to worst sidesteps this ambiguity by calculating the yield under each plausible early-redemption scenario and reporting the minimum. It is the floor return: what an investor must be prepared to accept in the worst-case outcome.

## Computing yield to worst

The calculation is straightforward in principle: for each date the bond can be called, put, or (at final maturity) redeemed, compute the [yield](/interest-rate/) assuming redemption on that date. The lowest of these yields is the yield to worst.

For example, consider a [callable bond](/callable-bond/) with a 4% coupon, trading at par (100), callable by the issuer in 3 years at par, and maturing in 10 years. If it is called in 3 years, the investor receives 3 years of 4% coupons plus the principal back at par—a total return of exactly 4% annually. If held to maturity in 10 years, the investor receives 10 years of 4% coupons and principal, also 4% annually. In this example (where price equals par and the call price equals par), [yield to call](/callable-bond/), [yield to maturity](/yield-to-maturity/), and yield to worst all equal 4%.

But consider the same bond trading at 110 (a premium). The [yield to maturity](/yield-to-maturity/) is below 4% because the investor is paying a premium that will be lost at redemption. The [yield to call](/callable-bond/) is even lower because the investor loses the premium in just 3 years rather than 10. In this scenario, yield to worst is the [yield to call](/callable-bond/) figure—the lowest of all possible outcomes.

Conversely, if the bond trades at a discount (say, 95), the [yield to maturity](/yield-to-maturity/) is above 4%, and the [yield to call](/callable-bond/) is higher still because the discount is recouped more quickly. Here, yield to worst is the [yield to maturity](/yield-to-maturity/) because the issuer is unlikely to call if refinancing would be expensive.

## The role of market expectations

Yield to worst is not a prediction; it is a mechanical calculation of the most pessimistic outcome. It assumes nothing about whether the issuer will actually call or refinance. That decision depends on [interest rates](/interest-rate/), [credit spreads](/credit-spread/), and the issuer's funding needs—all unknowable in advance.

In volatile or uncertain [credit](/credit-rating/) environments, the actual yield received may lie between yield to worst and [yield to maturity](/yield-to-maturity/). An investor who buys a [callable bond](/callable-bond/) at a large premium is implicitly betting that refinancing risk is low, or that the issuer will not call even if it could. This is a valid bet if the issuer is financially stressed and values financial flexibility, or if [interest rates](/interest-rate/) are unlikely to fall. But it introduces [reinvestment risk](/reinvestment-risk/): if the bond is called early, the investor must reinvest [coupon](/coupon-payment/) and principal at lower current rates.

## Yield to worst vs. other metrics

**[Yield to maturity](/yield-to-maturity/)** assumes no early redemption and provides an upper bound on return (for a [callable bond](/callable-bond/)) or a useful baseline (for bullet bonds). It is easy to calculate but can be highly misleading for [callable bonds](/callable-bond/) trading at a premium.

**[Yield to call](/callable-bond/)** assumes immediate exercise of the call option. It is more relevant than [yield to maturity](/yield-to-maturity/) for premium [callable bonds](/callable-bond/) but ignores other redemption dates and may not reflect the issuer's actual incentives.

**[Yield to put](/yield-to-put/)** (relevant for putable bonds) assumes the bondholder exercises the put at the earliest opportunity—usually when rates rise and the bondholder wants to exit a below-market coupon. Like [yield to call](/callable-bond/), it is scenario-specific.

**Yield to worst** encapsulates all three: it is whichever scenario is worst for the bondholder and best for the option holder. It is thus the most defensible conservative estimate of return, though it may be overly pessimistic in benign environments.

## Practical use in portfolio management

Fixed-income managers use yield to worst to compare [callable bonds](/callable-bond/) fairly. A 4% coupon [callable bond](/callable-bond/) with a yield to worst of 3.5% should be compared to a 4% coupon bullet [bond](/bond/) with a [yield to maturity](/yield-to-maturity/) of 3.5%, not to one with a [yield to maturity](/yield-to-maturity/) of 4.5%. The [embedded option](/option/) represents a real economic cost—lower expected return—that must be priced into the comparison.

Portfolio managers also use yield to worst to set [duration](/duration/) and convexity expectations. A [callable bond](/callable-bond/) with positive convexity (in normal scenarios) will exhibit negative convexity if [interest rates](/interest-rate/) fall sharply and the bond is called, capping price appreciation. This [option-adjusted spread](/credit-spread/) dynamic is crucial for risk management.

Institutional investors, [hedge funds](/hedge-fund/), and trading desks in [structured products](/securitization/) use yield to worst as a baseline; they may then apply [stress testing](/stress-testing/) and [sensitivity analysis](/sensitivity-analysis-valuation/) to model outcomes across interest-rate and [credit-spread](/credit-spread/) scenarios.

## Limitations

Yield to worst is a snapshot, not a forecast. It does not account for the [time value](/time-value/) of optionality or how exercising the option affects future [reinvestment](/reinvestment-risk/) rates. It also assumes that at each possible exercise date, the bond is redeemed at the strike price (usually par), ignoring any possibility of default or [restructuring](/debt-restructuring/).

For complex structures—like [mortgage-backed securities](/mortgage-backed-security/) with prepayment options or [convertible bonds](/convertible-bond/) with conversion features—yield to worst must be supplemented by [option-adjusted spread](/credit-spread/) models that account for the [probability](/option/) of exercise and refinancing dynamics. In these cases, a simple scalar yield figure is insufficient.

## See also

<div class="wiki-seealso">

### Closely related

- [Callable bond](/callable-bond/) — a bond the issuer can redeem before maturity
- [Yield to put](/yield-to-put/) — the yield assuming the bondholder exercises a put option at the earliest date
- [Yield to maturity](/yield-to-maturity/) — the total return assuming the bond is held to final maturity
- [Yield to call](/callable-bond/) — the return assuming the bond is called at a specific date
- [Coupon rate](/coupon-rate/) — the stated annual interest paid by the bond issuer

### Wider context

- [Bond](/bond/) — a debt security promising fixed or floating cash flows
- [Option](/option/) — the right to buy or sell an asset at a specified price
- [Duration](/duration/) — a bond's sensitivity to interest-rate changes
- [Credit spread](/credit-spread/) — the yield premium on a [corporate bond](/corporate-bond/) relative to a [risk-free](/treasury-bond/) alternative
- [Embedded option](/option/) — a call, put, or conversion feature embedded in a [bond](/bond/) or other security

</div>
