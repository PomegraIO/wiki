---
title: "Bond Price Formula"
description: "Present value calculation of coupon payments and principal repayment discounted at market yield."
keywords:
  - bond valuation
  - present value
  - coupon payment
  - discount rate
  - yield to maturity
---

*The bond price formula calculates the present value of all future cash flows—coupon payments and final principal repayment—by discounting them at the market's required yield, establishing the fair price a bond should trade at today.*

<aside class="wiki-infobox">

| Component | Role |
|-----------|------|
| **Coupon payments (C)** | Regular interest, typically semi-annual |
| **Par value (FV)** | Principal repaid at maturity |
| **Discount rate (y)** | Market yield, annualized |
| **Time periods (n)** | Years or half-years to maturity |
| **Price result** | Present value of all cash flows |
| **Inverse relationship** | Higher yield → lower price |

</aside>

## The core formula

The bond price is:

**P = C × [1 − (1 + y)^−n] / y + FV / (1 + y)^n**

Where:
- **P** = Bond price today
- **C** = Annual coupon payment (or semi-annual if using semi-annual yield)
- **y** = Yield to maturity (market discount rate), expressed as a decimal
- **n** = Number of periods to maturity
- **FV** = Face (par) value, typically $1,000

The first term values the annuity of coupon payments. The second term discounts the final principal repayment. Together, they represent the present value of the bond's entire cash stream.

## Why the inverse: price and yield move opposite

When market yields rise, bond prices fall. This is not a market anomaly; it is mathematical necessity. If you bought a bond yielding 3% and market yields climb to 4%, your 3% bond is worth less. A buyer would demand a discount to accept a below-market coupon. Conversely, if yields fall, existing higher-coupon bonds become attractive, and buyers bid prices up. This inverse relationship is why bond traders obsess over yield moves—a 1% shift in yield can move a 10-year bond's price by 8–10%.

## The annuity component

The first half of the formula values the stream of coupon payments. Coupons are typically paid semi-annually. If a $1,000 bond has a 5% annual coupon, the holder receives $25 twice a year for as long as they hold it. The formula discounts each of these payments to present value. As time progresses, later coupons are worth less today because of the time value of money. The market yield determines the discount rate.

## The principal repayment component

The second term, **FV / (1 + y)^n**, discounts the par value back to today. At maturity, the issuer repays the full $1,000 (or whatever the par value). The longer the maturity, the lower this discounted value. A 30-year bond's repayment is worth far less in present-value terms than a 2-year bond's repayment, because that cash is so far in the future.

## A worked example

A $1,000 bond with a 5% annual coupon, 10 years to maturity, trading at a 4% market yield:

- Annual coupon: C = $50
- Annuity of coupons: 50 × [1 − (1.04)^−10] / 0.04 = 50 × 8.1109 ≈ **$405.55**
- Principal repayment: 1,000 / (1.04)^10 ≈ **$675.56**
- **Bond price ≈ $1,081.11**

The bond trades above par (premium) because its 5% coupon exceeds the 4% market yield. Buyers pay extra to lock in above-market coupons.

## The relationship to duration and convexity

As yields change, the bond price does not move linearly. [Duration](/wiki/duration/) tells you the average time to receive cash flows, weighted by present value—it is a simplified estimate of price sensitivity. A 10-year bond with a high coupon might have a duration of 7 years, meaning a 1% yield change moves the price by roughly 7%. [Convexity](/wiki/convexity/) captures the curvature: as yields fall, bond prices rise faster than duration predicts, and as yields rise, prices fall slower. The bond price formula is always precise; duration is an approximation for traders and portfolio managers.

## Par, premium, and discount bonds

When the coupon rate equals the market yield, the formula yields a price equal to par ($1,000)—a **par bond**. When the coupon exceeds the yield, the bond sells at a **premium** (above par). When the coupon is below the yield, it trades at a **discount** (below par). The gap between coupon and yield determines how far the price deviates from par.

<div class="wiki-seealso">

### Closely related
- [Duration](/wiki/duration/) — Weighted average time to cash flows
- [Convexity](/wiki/convexity/) — Curvature in the price-yield relationship
- [Coupon payment](/wiki/coupon-payment/) — Periodic interest income
- [Yield to maturity](/wiki/yield-to-maturity/) — Market discount rate for bonds

### Wider context
- [Bond basics](/wiki/bond/) — Debt instrument and fixed-income markets
- [Discount rate](/wiki/discount-rate/) — Present value of future cash
- [Present value](/wiki/discounted-cash-flow-valuation/) — Fundamental valuation principle

</div>
