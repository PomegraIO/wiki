---
title: "Horizon Return vs Yield to Maturity: What Changes the Outcome"
description: "Why a bond's realized return over a holding period differs from YTM: reinvestment rates, sale price changes, and duration effects explained with examples."
keywords:
  - horizon return vs yield to maturity
  - bond horizon return
  - realized return bond
  - yield to maturity difference
  - reinvestment risk bonds
image: "/svg/fixed-income.svg"
---

*A bond's **yield to maturity** (YTM) is the annual return if you hold it until it matures and reinvest every [coupon payment](/coupon-payment/) at the same rate; **horizon return** is the actual realized return over a specific holding period (say, 3 years) when you sell before maturity. The two often diverge because reinvestment rates change, the bond's price fluctuates, and interest-rate environments shift—all factors YTM assumes will remain constant.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Horizon Return vs Yield to Maturity — key facts</div>

<img src="/svg/fixed-income.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Realized return differs from YTM when rates, prices, or reinvestment rates change mid-hold.</div>

|   |   |
|---|---|
| **YTM definition** | Annual return assuming hold-to-maturity and reinvestment at YTM rate |
| **Horizon return** | Actual return realized over a specific holding period, then sold |
| **Key difference driver** | [Interest rate](/interest-rate/) movements, reinvestment rates, sale price |
| **Reinvestment risk** | Falling rates mean lower returns on reinvested coupons |
| **Price risk** | Rising rates erode bond value if sold before maturity |
| **[Duration](/duration/) effect** | Longer bonds more sensitive to rate changes mid-hold |

</aside>

## Why YTM Is Not a Guarantee

YTM is an *promised* return only if two conditions hold:

1. You hold the bond until [maturity](/expiration-date/).
2. Every coupon reinvested earns the same yield-to-maturity rate.

In reality, neither is guaranteed. A 10-year corporate bond with a 5% YTM assumes that each semi-annual $25 coupon (on a $1,000 par bond) will be reinvested at 5% annually. But if rates fall to 3% next year, you'll reinvest coupons at 3%, dragging down your total return. If you need to sell the bond before maturity and rates have risen, the bond's market value has fallen, further reducing your realized return.

YTM is useful as a *snapshot* comparison—it tells you what yield the bond market is offering today relative to others. It is not a return forecast.

## A Worked Example: Rising Rates and Selling Early

Consider a 5-year corporate bond with a 4% coupon, par value of $1,000, and a YTM of 4.0%. The bond pays $40 in interest annually (or $20 semi-annually).

**Scenario A: Hold to maturity**
If you hold all five years and reinvest coupons at exactly 4%, your total proceeds are:
- Five coupon payments (including reinvestment): ~$216.65
- Repayment of principal: $1,000
- **Total return**: 4% annualized

**Scenario B: Sell after 2 years; rates have risen to 5%**
After 2 years, you receive 4 coupons ($40 × 2 = $80) and sell the bond. Because rates have risen from 4% to 5%, the remaining 3-year bond with a 4% coupon is now worth less. Using the present-value formula, the bond is worth approximately $971 (the present value of 3 more $40 coupons and $1,000 principal, discounted at 5%).

Your realized return:
- Coupons received: $80
- Sale proceeds: $971
- Total proceeds: $1,051
- On a $1,000 investment over 2 years: ~2.5% annualized

The horizon return (2.5%) is *lower* than the YTM (4.0%) because rates rose, eroding the bond's market value.

**Scenario C: Sell after 2 years; rates have fallen to 3%**
Now the remaining 3-year bond with a 4% coupon trades above par. At 3% discount rates, it's worth approximately $1,029.

Your realized return:
- Coupons received: $80
- Sale proceeds: $1,029
- Total proceeds: $1,109
- On a $1,000 investment over 2 years: ~5.3% annualized

The horizon return (5.3%) exceeds the YTM (4.0%) because rates fell, boosting the bond's market value.

## Reinvestment Risk for Longer Bonds

Reinvestment risk is especially acute for longer-duration bonds and higher coupon bonds, which generate more cash to reinvest. A 30-year bond with a 6% coupon pays $60 per year; over 30 years, you reinvest 29 coupon payments. If rates drop from 6% to 2% within the first year, the bulk of your coupons are reinvested at 2%, severely depressing your horizon return.

A low-coupon, short-duration bond faces the opposite problem: less cash to reinvest, but greater exposure to price appreciation or depreciation if rates move. A 2-year zero-coupon bond generates no coupons but experiences sharp price swings if rates change.

This trade-off—reinvestment risk vs. [price risk](/call-risk/)—is core to bond portfolio management. Longer bonds lock in high coupons (good for reinvestment in a rising-rate world) but face downside if you sell before maturity (bad if rates rise further).

## Duration and the Rate-Sensitivity Link

[Duration](/duration/) quantifies a bond's sensitivity to rate changes. A bond with a 5-year duration falls roughly 5% in value if rates rise 1%. This formula directly links duration to the difference between YTM and horizon return.

If a bond has a 5-year duration and you plan a 3-year horizon:
- If rates stay flat, your horizon return will equal YTM (barring reinvestment rate drift).
- If rates rise 1%, the price decline will roughly offset 3 years of the duration effect (50% of the 5-year sensitivity), dragging horizon return below YTM.
- If rates fall 1%, the price gain will enhance your return, pushing horizon return above YTM.

The magnitude of the gap depends on both the magnitude of the rate move and the duration mismatch (how far your horizon is from the bond's duration).

## Reinvestment Rates and Coupon Income

A more subtle driver of horizon return is the reinvestment rate on intermediate coupons. Suppose you buy a 10-year bond with a 5% YTM and a 4% coupon. The YTM calculation bakes in an assumption: you reinvest each $40 coupon at 5%.

If rates fall to 2% in year 3, your coupons earned in years 1–2 (before the rate drop) will be reinvested at 2% for the remainder of your holding period. You lose the compounding benefit of reinvestment at 5%, reducing your horizon return.

Conversely, if rates rise to 8%, you reinvest coupons at 8%, boosting compounding and potentially exceeding the YTM—if the price appreciation (from early coupons already collected) or the reinvestment gains outweigh any mark-to-market loss on the bond itself.

## The Horizon Return Framework

To calculate horizon return instead of relying on YTM, you need:

1. **Starting price**: What you paid (usually par or a price off par).
2. **Holding period**: Your intended sale date (e.g., 3 years).
3. **Expected reinvestment rate**: Forecast or assumption for coupons (often the current yield curve).
4. **Ending price**: The bond's market price at your sale date, driven by the rate environment at that time.

A simple approximation is:

Horizon Return = [ (Ending Value + Coupons Reinvested) / Starting Price ] ^ (1 / Years Held) − 1

This mirrors the [time-value](/time-value/) calculation but uses actual forward-looking coupons and price movements instead of the flat YTM assumption.

## Why Investors Should Care

YTM is quoted because it's a standardized, easy-to-compare number. But it is a marketing metric, not a personal return forecast. When deciding whether to hold a bond or sell, you must consider:

- **Your actual horizon**: If you need cash in 3 years, YTM on a 10-year bond is irrelevant.
- **Rate outlook**: If you expect rates to fall, long-duration bonds will appreciate, potentially beating their YTM. If you expect rates to rise, short-duration is safer.
- **Reinvestment rate environment**: In a low-rate world, reinvestment risk is real; the bond's coupon may be your best available rate.

Professional bond managers optimize for horizon return, not YTM, because it directly answers the question: "What will I actually earn?"

## See also

<div class="wiki-seealso">

### Closely related

- [Yield to Maturity](/yield-to-maturity/) — Standard calculation that assumes hold-to-maturity
- [Duration](/duration/) — Measures bond price sensitivity to rate moves
- [Coupon Payment](/coupon-payment/) — Cash flows reinvested at uncertain future rates
- [Call Risk](/call-risk/) — Issuer may redeem early, cutting off expected coupons
- [Reinvestment Risk](/reinvestment-risk/) — Explicit risk of falling coupon reinvestment rates
- [Interest Rate Risk](/interest-rate-risk/) — Price changes if sold before maturity

### Wider context

- [Bond](/bond/) — Fundamental security whose return depends on horizon
- [Current Yield](/current-yield/) — Alternative yield metric for short holding periods
- [Price Discovery](/price-discovery/) — How bond prices adjust to rate changes
- [Sensitivity Analysis](/sensitivity-analysis-valuation/) — Tool to model horizon returns across rate scenarios

</div>
