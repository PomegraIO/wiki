---
title: "Matching Bond Duration to Investment Horizon"
description: "How to align a bond portfolio's duration with your spending timeline to neutralize interest-rate and reinvestment risk."
keywords:
  - bond duration matching
  - matching duration investment horizon
  - liability matching bonds
  - immunization portfolio
  - duration risk management
  - fixed-income strategy
image: /svg/strategies.svg
---

*Matching bond **duration to investment horizon** means constructing a fixed-income portfolio so that the weighted-average maturity roughly equals the date you'll need the cash. When done correctly, you lock in a return upfront and sidestep two competing risks: prices falling if rates rise, and reinvestment rates falling if rates drop.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Duration Matching — key facts</div>

<img src="/svg/strategies.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Lock in a return by matching the portfolio's duration to your spending date.</div>

|   |   |
|---|---|
| **Duration definition** | Weighted-average time until cash flows; sensitivity to 1% rate change |
| **Goal** | Portfolio duration ≈ years until spending need |
| **Price risk** | Longer duration = bigger loss if rates rise |
| **Reinvestment risk** | Shorter duration = smaller returns if rates fall |
| **Neutral point** | Duration matching neutralizes both risks |
| **Common horizon** | 3–20 years (bonds, college savings, retirement) |

</aside>

## The two risks that cancel out

Most investors fixate on one risk: if I buy a 10-year bond and rates rise 1%, its price falls roughly 10%. That's **price risk** or **interest-rate risk**. They then conclude, "I should buy short-term bonds to avoid losses."

That logic misses the second half. Suppose you need $100,000 in 10 years. You buy a 1-year Treasury ladder—$100,000 in annual chunks. Rates are 4% today. You pocket $4,000 in year 1 interest. Then rates drop to 2%. You reinvest the principal at 2%, and your final sum falls short of your goal. That's **reinvestment risk**.

A 10-year bond locks in a 4% yield for the full 10 years. No reinvestment guesswork. But if rates fall to 2%, the bond's price rises—and you realize a capital gain if you sell early. If rates rise to 6%, the bond's price falls, and you realize a loss if you sell. That's price risk.

Duration matching is the sleight of hand that lets you ignore both. By matching duration to horizon, you bind the portfolio's sensitivity to rate changes so tightly to your cash-flow date that the two effects wash out. You get your target return regardless of where rates go.

## How duration matching works in practice

Suppose you're 55 and will retire in 12 years at 67. You want to set aside $500,000 that will grow to cover your first three years of retirement spending ($150,000 per year, starting at year 12). You expect 3.5% real returns from bonds.

Do the math: $500,000 growing at 3.5% annually for 12 years yields roughly $734,000—enough for your goal with a small cushion.

Now build a portfolio with **average duration of 12 years**. This typically means a blend of:
- 40% in 10-year Treasury bonds or corporates
- 40% in 15-year Treasury bonds or corporates
- 20% in 20-year bonds

The weighted-average duration works out to roughly 12.

**Scenario A (rates rise 1%)**
- Bond prices fall ~12% (due to 12-year duration).
- But when you reinvest coupons over the next 12 years, you get the higher 4.5% yield instead of 3.5%.
- The gains on reinvestment offset the capital loss. You still hit your $734,000 target.

**Scenario B (rates fall 1%)**
- Bond prices rise ~12%.
- But when you reinvest coupons, you get only 2.5% instead of 3.5%.
- The loss on reinvestment is offset by the capital gain. You still hit your target.

This is the beauty of matching: you've locked in a guaranteed return, and interest-rate moves after purchase become economically neutral.

## Duration matching vs. full immunization

Duration matching is a practical approximation. It assumes:
1. A single, known spending date (not multiple dates).
2. A flat yield curve (rates don't vary wildly by maturity).
3. Small interest-rate moves (duration approximation breaks down in large moves).

**Full immunization** is more sophisticated. It adds a second constraint: **convexity matching**. Convexity measures how the duration relationship itself changes as rates move. A Treasury with positive convexity gains extra upside if rates fall and suffers less downside if rates rise. By matching both duration and convexity, you get an even tighter lock on returns.

For most retail investors, duration matching is good enough. Full immunization is overkill unless you're managing a large pension liability or a dedicated insurance reserve.

## The reinvestment-rate and price-risk duality

Here's the intuition. A short-duration portfolio (e.g., a 2-year bond ladder) has **low price risk** (won't drop much if rates rise) but **high reinvestment risk** (you're constantly rolling cash into new 2-year bonds at unknown future rates). A long-duration portfolio (e.g., 20-year bonds) has **high price risk** but **low reinvestment risk** (you're locked in for 20 years).

Duration matching finds the duration that makes your specific time horizon the indifference point. At that duration, price risk and reinvestment risk are equal and opposite. Move to either shorter or longer duration, and you're making an implicit bet on interest-rate direction—a bet that may or may not pan out.

## Building a matched portfolio in practice

Start with your spending date and work backward:

1. **Identify the liability date**: When do you need the cash?
2. **Calculate required return**: How much must your current portfolio grow to meet that need?
3. **Select a target duration**: Choose a duration equal to the years until your spending date.
4. **Build a ladder or blend**: Mix bonds of varying maturities to achieve the target duration:
   - A true ladder buys equal amounts of bonds maturing each year through your horizon.
   - A blend buys a mix of short, intermediate, and long bonds weighted to hit your target duration.
5. **Monitor drift**: As time passes, durations shorten. Rebalance annually to maintain your duration target (or let it drift down if your horizon shortens).

A common mistake: buying bonds *past* your horizon. If you need $100,000 in 10 years but buy a 30-year bond, you're taking unnecessary interest-rate risk. Your 30-year bond's price will swing wildly; you'll be tempted to sell early, and you've introduced an option you didn't mean to take.

## When duration matching breaks down

Duration matching is weakest in a few scenarios:

- **Multiple spending dates**: If you need $50,000 in year 5 and $100,000 in year 15, you can't match both with a single duration. Solution: decompose the problem into two sub-portfolios, each duration-matched to its respective date.
- **Steep yield curve**: If the curve is sharply inverted or upward-sloping, duration approximation errors grow. Consider convexity-matching or simply holding to maturity.
- **Credit risk**: If your bonds default, the math breaks. Duration matching works best with Treasury or high-grade corporate bonds where default is minimal.
- **Inflation**: If spending needs are inflation-adjusted, nominal bond matching doesn't capture the real return. You may want Treasury Inflation-Protected Securities (TIPS) instead.

## See also

<div class="wiki-seealso">

### Closely related

- [Duration](/duration/) — definition and measurement of bond price sensitivity
- [Interest rate risk](/interest-rate-risk/) — how bond prices respond to rate changes
- [Yield to maturity](/yield-to-maturity/) — the return a bond buyer locks in at purchase
- [Bond ladder](/bond-ladder/) — building a portfolio of staggered maturities
- [Treasury bond](/treasury-bond/) — benchmark instrument for duration matching
- [Reinvestment risk](/reinvestment-risk/) — cost of rolling cash into uncertain future rates
- [Asset allocation](/asset-allocation/) — how fixed income fits in a broader portfolio

### Wider context

- Immunization — advanced liability-matching with convexity
- [Yield curve](/yield-curve/) — how bond yields vary by maturity
- [Corporate bond](/corporate-bond/) — alternative to Treasuries for matching
- [Inflation](/inflation/) — reason to consider TIPS for real purchasing power
- Financial planning — broader framework for aligning investments with life goals

</div>
