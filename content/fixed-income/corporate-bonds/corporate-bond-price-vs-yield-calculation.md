---
title: "Corporate Bond Price vs. Yield: The Inverse Relationship Calculated"
description: "How bond prices fall when yields rise through discounted cash flow arithmetic, with worked examples showing the mathematical inverse relationship."
keywords:
  - corporate bond price vs yield calculation
  - bond yield inverse relationship
  - bond pricing formula
  - discounted cash flow bonds
  - yield to maturity calculation
  - bond duration
---

*The **inverse relationship between corporate bond price and yield** arises from the mathematics of discounting: a bond's price equals the present value of all future cash flows (coupon payments and principal repayment) discounted at the bond's [yield to maturity](/yield-to-maturity/). When yields rise, the discount rate increases, compressing present values and lowering the bond's price. A worked numerical example makes the mechanism transparent.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Bond Price-Yield Inverse — Key facts</div>

<img src="/svg/fixed-income.svg" alt="An abstract editorial mark for fixed income." />

<div class="wiki-infobox-caption">Higher discount rates shrink the present value of future cash streams.</div>

|   |   |
|---|---|
| **Core principle** | Price = sum of discounted future cash flows |
| **When yields rise** | Discount rate rises; price falls (always, by definition) |
| **When yields fall** | Discount rate falls; price rises (always, by definition) |
| **Mathematical form** | Non-linear; price decline accelerates at lower yields |
| **Key term** | [Duration](/duration/) measures price sensitivity to yield moves |
| **Numerical example** | 5-year bond, 5% coupon, yield 5% → price 100; yield 6% → price 95.68 |
| **Fixed cash flows** | Coupon and principal repayment are contractual, never change |

</aside>

## The fundamental pricing formula

A [corporate bond](/corporate-bond/) obligates the issuer to pay the bondholder a fixed coupon (interest) each period and repay the principal (face value or "par") at maturity. The price of the bond is the sum of the present values of all these cash flows, discounted at a rate of return (the yield).

The formula is:

**Price = Σ [Coupon / (1 + y)^t] + [Face Value / (1 + y)^n]**

Where:
- **y** = yield to maturity (or the discount rate being applied)
- **t** = time period (1, 2, 3, ... n)
- **n** = years to maturity
- **Coupon** = annual coupon payment in dollars
- **Face Value** = principal repayment amount at maturity

The bond's price is anchored to the contractual cash flows (coupon and principal), which never change. What varies is **y**, the discount rate used to compute present value. As **y** (yield) changes, the denominator in each term grows or shrinks, directly changing the price.

## A concrete example: the inverse relationship at work

Imagine a 5-year corporate bond issued by Acme Corp with a 5% annual coupon and $1,000 face value. We'll calculate its price under three different yield scenarios.

**Scenario 1: Yield = 5% (same as coupon)**

Price = [50/(1.05)^1 + 50/(1.05)^2 + 50/(1.05)^3 + 50/(1.05)^4 + 50/(1.05)^5] + [1000/(1.05)^5]

Price = [47.62 + 45.35 + 43.19 + 41.14 + 39.18] + [783.53]

Price = **$1,000.00** (par)

When the yield equals the coupon rate, the bond trades at par (face value). This is intuitive: if you are earning 5% from coupon payments and the market requires 5% return, you are satisfied; the price is full value.

**Scenario 2: Yield = 6% (market yield rises)**

Price = [50/(1.06)^1 + 50/(1.06)^2 + 50/(1.06)^3 + 50/(1.06)^4 + 50/(1.06)^5] + [1000/(1.06)^5]

Price = [47.17 + 44.50 + 41.99 + 39.63 + 37.41] + [747.26]

Price = **$958.00** (approx.; discount bond)

The bond now trades below par. Why? The market yield is 6%, but the bond only pays 5% coupon. To offer a 6% total return, the bond must be purchased at a discount. The buyer pays $958 for the bond, earns $50 per year in coupons, and receives $1,000 at maturity—the combination delivers a 6% annualized return.

**Scenario 3: Yield = 4% (market yield falls)**

Price = [50/(1.04)^1 + 50/(1.04)^2 + 50/(1.04)^3 + 50/(1.04)^4 + 50/(1.04)^5] + [1000/(1.04)^5]

Price = [48.08 + 46.23 + 44.45 + 42.72 + 41.06] + [821.93]

Price = **$1,044.50** (approx.; premium bond)

The bond now trades above par. The bond pays 5% coupon but the market only requires 4% return. The buyer is willing to pay a premium for the above-market coupon, and the combination of the premium paid plus the 5% coupon yield delivers 4% annualized return.

| Yield | Price | Relationship |
|-------|-------|------------------|
| 4% | $1,044.50 | Yield falls → Price rises |
| 5% | $1,000.00 | Yield = Coupon → Par |
| 6% | $958.00 | Yield rises → Price falls |

The inverse relationship is plain: every time yield moves up 1%, price drops roughly $40–50 on this 5-year bond. Every time yield falls, price rises.

## Why the relationship is non-linear

Notice that the price change from 5% to 4% yield (+1 percentage point) is $44.50 in the bond's favor; the price change from 5% to 6% yield (−1 percentage point) is $42 against. The magnitudes are not identical. This is because the discount factor is non-linear.

When yields are low, a small rise has a larger impact on discounted values. When yields are high, a small rise has a smaller impact. This non-linearity is captured by [duration](/duration/), which measures the effective sensitivity of bond price to yield moves. Longer-dated bonds and bonds with lower coupons have higher duration, meaning they are more price-sensitive to yield moves.

## The mechanism: why does the market price respond?

A natural question arises: if the bond's coupon is fixed at 5%, why does its market price change when the economy moves and yields shift?

The answer: the bond trades in a secondary market. Once issued, the bond can be bought and sold before maturity. If you own a bond yielding 5% and the market rate for similar bonds rises to 6%, you now hold an asset that is unattractive relative to new issues. To sell your bond, you must discount the price so that the buyer's total return (coupon received plus capital gain/loss on sale) equals the market rate of 6%. That discount in price is what makes the bond attractive again.

Conversely, if market rates fall to 4%, new bonds issued only 5% coupon is above-market attractive. You can sell your bond at a premium. That premium is what equilibrates the secondary market.

## The yield to maturity (YTM) concept

The [yield to maturity](/yield-to-maturity/) is the discount rate that makes the bond's price equal to the sum of its discounted future cash flows. It is the uniform annualized return an investor realizes if they buy at today's market price, hold to maturity, and reinvest coupons at the YTM rate.

In the examples above, when we calculated price at 5% yield, the bond trades at par and the YTM is 5%. When we calculated price at 6% yield, the YTM is 6%. YTM and price are two sides of the same coin: specify one, and the other is determined by the formula.

This is why news of Federal Reserve rate hikes or economic data affects bond prices instantly. When the market perceives higher risk or inflation, required yields rise, prices fall immediately. The discount rate bakes in both the risk-free rate and the [credit spread](/credit-spread/) specific to the issuer.

## Current yield vs. yield to maturity

Note the distinction: the bond's **coupon** (5% per year on $1,000 = $50 per year) remains fixed for life. This $50 payment is contractual. The bond's **current yield** is simply coupon divided by current price (e.g., $50 / $958 = 5.22% if the bond is trading at $958). The **yield to maturity** includes both the coupon stream and the capital gain or loss realized at maturity, and it is the rate that solves the present-value formula.

When you see "bonds yielding 6%" in financial news, the figure refers to YTM, not current yield, unless specified. YTM is the economically meaningful measure because it accounts for the final maturity payoff.

## Practical implications for investors

Understanding the price-yield inverse relationship is essential for bond portfolio management. A portfolio of longer-duration bonds (more years to maturity, or lower coupons) experiences larger price swings for a given move in yields. A rising-rate environment means mark-to-market losses on bonds; a falling-rate environment means mark-to-market gains.

This is why bond managers care about [duration](/duration/) and watch central bank policy closely. A 1% rise in 10-year Treasury yields can wipe 10% off a long-duration bond portfolio. The mathematical inverse relationship is not an abstraction; it directly affects realized returns.

## See also

<div class="wiki-seealso">

### Closely related

- [Yield to Maturity](/yield-to-maturity/) — the discount rate in the pricing formula
- [Duration](/duration/) — measures price sensitivity to yield changes
- [Coupon Payment](/coupon-payment/) — the fixed cash flow component
- [Bond](/bond/) — the fundamental instrument
- [Coupon Rate](/coupon-rate/) — the contracted interest rate
- [Current Yield](/current-yield/) — simplified yield measure (coupon / price)
- [Discounted Cash Flow Valuation](/discounted-cash-flow-valuation/) — the underlying present-value math

### Wider context

- [Corporate Bond](/corporate-bond/) — the specific security type discussed
- [Credit Spread](/credit-spread/) — the yield premium for issuer-specific risk
- [Interest Rate Risk](/interest-rate-risk/) — the core risk driving price moves
- Bond Market — the secondary market where prices fluctuate
- Fixed Income — the asset class
- [Federal Reserve](/federal-reserve/) — primary driver of risk-free rates

</div>
