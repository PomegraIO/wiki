---
title: "Macaulay Duration: Calculation and Example"
description: "Macaulay duration measures the weighted-average time to receive bond cash flows, expressed in years, with a step-by-step calculation example."
keywords:
  - macaulay duration calculation
  - macaulay duration example
  - bond duration weighted average
  - duration time to cash flows
  - interest rate sensitivity bonds
image: /svg/fixed-income.svg
---

*[**Macaulay duration**](/duration/) is the weighted-average number of years until a bondholder receives the bond's cash flows (coupon payments and principal repayment), expressed in years and often used as a rough measure of how much a bond's price will change if interest rates shift.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Macaulay Duration — Key Facts</div>

<img src="/svg/fixed-income.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">A time-weighted average measuring when investors actually get their money back.</div>

|   |   |
|---|---|
| **Formula** | Weighted average of each cash flow's timing and present value |
| **Units** | Years |
| **Key insight** | Longer duration = greater price sensitivity to rate changes |
| **Typical range** | 2–10 years for most bonds; higher for long-maturity, low-coupon bonds |
| **Relationship to [modified duration](/duration/)** | Modified = Macaulay ÷ (1 + yield to maturity) |
| **Use in practice** | Estimating bond portfolio interest rate risk |

</aside>

## What Macaulay Duration Measures

Imagine you buy a 10-year bond with a 5% coupon. You will not receive all your money at once; instead, you get interest payments every six months and your principal back at maturity. Macaulay duration asks: on average, how long until you receive your money?

It is not simply the 10-year maturity. A bond paying coupons returns some cash earlier—after 1, 2, 3 years, etc. Macaulay duration weights each payment by both its size and when it arrives, then expresses the result as a single number of years. A bond with a high Macaulay duration is more sensitive to interest rate changes; a bond with a low duration feels little price impact from rate swings.

## The Calculation Formula

Macaulay duration is calculated as:

**MD = Σ [t × PV(CF_t)] ÷ Bond Price**

Where:
- t = time period (in years) when cash flow arrives
- CF_t = the cash flow at time t (coupon or principal)
- PV(CF_t) = present value of that cash flow, discounted at the bond's [yield-to-maturity](/yield-to-maturity/)
- Bond Price = the sum of all discounted cash flows (the market price)

The numerator weights each cash flow by the time it arrives; the denominator normalizes by the bond's price, yielding a time value in years.

## Worked Example

Consider a 3-year bond with:
- Par value: $1,000
- Annual coupon: 6% (paid once per year)
- Yield to maturity: 6%
- Current price: $1,000 (trading at par because coupon = yield)

**Step 1: Identify all cash flows**

Year 1: $60 coupon
Year 2: $60 coupon
Year 3: $60 coupon + $1,000 principal = $1,060

**Step 2: Discount each cash flow at the 6% yield**

PV of Year 1 flow: $60 ÷ 1.06¹ = $56.60
PV of Year 2 flow: $60 ÷ 1.06² = $53.40
PV of Year 3 flow: $1,060 ÷ 1.06³ = $890.00

Sum = $1,000 (this equals the bond price, confirming our math)

**Step 3: Weight each present value by its timing**

Year 1: 1 × $56.60 = $56.60
Year 2: 2 × $53.40 = $106.80
Year 3: 3 × $890.00 = $2,670.00

Sum of weighted PVs = $2,833.40

**Step 4: Divide by bond price**

Macaulay duration = $2,833.40 ÷ $1,000 = **2.83 years**

This bond's Macaulay duration is 2.83 years—less than its 3-year maturity because the bondholder receives interest before year 3.

## Interpreting the Result

A Macaulay duration of 2.83 years means that, on average, the bondholder's cash is invested for 2.83 years. If you think of duration as a "weighted average time to payoff," then a 3-year bond paying coupons matures faster (on average) than a 3-year zero-coupon bond, which has a duration of exactly 3 years because no cash arrives until maturity.

Duration also predicts interest rate sensitivity. A bond with a Macaulay duration of 2.83 years will experience approximately a 2.83% price decline for each 1 percentage-point rise in yields (assuming small yield changes and a [modified duration](/duration/) close to Macaulay duration). For example:
- If yields rise from 6% to 7%, the bond's price falls roughly 2.83%.
- If yields fall from 6% to 5%, the bond's price rises roughly 2.83%.

This relationship is approximate and holds best for small rate moves; for larger moves, [convexity](/bond/) effects become material.

## How Coupons and Yields Affect Duration

Macaulay duration depends heavily on coupon payments and the yield curve environment.

**Higher coupons → Lower duration**: A high-coupon bond returns cash earlier, so its weighted-average timing is sooner. A 10-year bond paying 10% annually has a lower duration than a 10-year bond paying 2%, even though both mature in 10 years.

**Lower yields → Higher duration**: When the [yield-to-maturity](/yield-to-maturity/) is low, future cash flows (especially the principal repayment) become very expensive to discount, so their present values are large and their time-weights matter more. A 10-year bond with a 2% yield has higher duration than the same bond with a 6% yield.

**Zero-coupon bonds → Duration = Maturity**: A bond paying no coupons has a Macaulay duration equal to its maturity, because all cash arrives at one point in time.

## Modified Duration and Price Sensitivity

Investors often use **Modified Duration** instead of Macaulay duration when estimating price changes, because it directly converts duration into a percentage price change per basis point of yield move.

Modified duration = Macaulay duration ÷ (1 + yield)

In the example above:
Modified duration = 2.83 ÷ 1.06 = 2.67 years

This means a 1% yield increase causes roughly a 2.67% price decline. For small yield moves, this is accurate; for larger moves, convexity adjustments help.

## Practical Use in Portfolio Management

Bond portfolio managers use Macaulay and modified duration to:

1. **Estimate interest rate risk**: A portfolio with an average duration of 5 years is twice as exposed to rate changes as one with 2.5 years.

2. **Match liabilities**: Pension funds and insurers match the duration of their bond holdings to the timing of their liabilities, reducing the risk of being forced to sell bonds in unfavorable markets.

3. **Guide tactical bets**: If a manager expects rates to fall, increasing portfolio duration (buying longer-maturity or lower-coupon bonds) will amplify gains. If rates are expected to rise, lowering duration reduces losses.

4. **Compare bonds**: Duration allows meaningful comparison across different maturities and coupons. Two 10-year bonds with different coupons will have different durations and thus different interest rate sensitivities.

## Limitations

Macaulay and modified duration assume a flat yield curve and a parallel shift in yields. They also assume the bondholder holds to maturity; if a bond is sold before maturity, actual price changes depend on where yields have moved and how the bond's duration has changed. Additionally, duration assumes fixed cash flows, so it is less useful for callable or floating-rate bonds where future payments are uncertain.

## See also

<div class="wiki-seealso">

### Closely related

- [Duration](/duration/) — the broader concept encompassing Macaulay and modified duration
- [Yield to Maturity](/yield-to-maturity/) — the discount rate used in duration calculations
- [Bond](/bond/) — the instrument whose price sensitivity duration measures
- [Interest Rate Risk](/interest-rate-risk/) — the risk duration quantifies
- [Convexity](/bond/) — the refinement to duration for larger rate moves

### Wider context

- Fixed Income — the broader asset class
- [Coupon Payment](/coupon-payment/) — the cash flows being weighted in duration
- [Price Discovery](/price-discovery/) — how bond prices adjust to rate changes
- [Yield Curve](/yield-curve/) — the broader rate environment
- [Treasury Bond](/treasury-bond/) — a common instrument for duration analysis

</div>
