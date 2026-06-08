---
title: "Reinvestment Risk in Fixed Income"
description: "Reinvestment risk fixed income explains how falling rates force bondholders to reinvest coupons and principal at lower yields, reducing total return below the promised yield-to-maturity."
keywords:
  - reinvestment risk fixed income
  - bond reinvestment risk
  - coupon reinvestment
  - yield-to-maturity assumption
  - interest rate risk bonds
---

*When you buy a bond, its yield-to-maturity assumes you'll reinvest every coupon at that same rate. In reality, as interest rates fall, you'll reinvest at lower yields—and your actual return will lag what the bond promised you on the day you bought it. This is **reinvestment risk in fixed income**, and it's the hidden drag that separates theory from practice.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Reinvestment Risk in Fixed Income — key facts</div>

<img src="/svg/risk.svg" alt="An abstract editorial mark for risk." />

<div class="wiki-infobox-caption">YTM assumes reinvestment at par; reality is messier. Falling rates hurt coupon reinvestment; rising rates hurt principal reinvestment.</div>

|   |   |
|---|---|
| **Root cause** | Bond coupons and principal must be reinvested at market rates, which change |
| **Direction of impact** | Falling rates = lower reinvestment yields; rising rates = higher yields |
| **Who's exposed** | All bondholders, especially those holding to maturity |
| **Size of effect** | Often 0.1–0.5% per year of total return; larger for longer-duration bonds |
| **Mitigation** | Laddering maturities, [duration matching](/duration/), zero-coupon bonds, callable bonds (worse) |
| **Related risk** | [Prepayment risk](/prepayment-risk/) (coupons and principal returned early at lower reinvestment rates) |

</aside>

## The yield-to-maturity assumption

When a bond is quoted with a [yield-to-maturity](/yield-to-maturity/) (YTM) of 4%, that number embeds an assumption: you'll hold the bond to maturity and reinvest every coupon at exactly 4% until the final principal payment. In practice, this assumption almost never holds.

Buy a 10-year Treasury yielding 4% and receive a $40 coupon every six months. The YTM calculation says: "If you reinvest each of those coupons at 4%, your total return will be 4% annually." But six months later, [interest rates](/interest-rate/) have fallen to 3%, so new Treasuries yield 3%. Your next coupon of $40 goes into a 3% instrument, not 4%. Over the next nine-and-a-half years, that shortfall compounds. Your actual realized return falls below 4%.

The damage compounds: every coupon paid into a lower-yield environment means reinvestment drag. For a 10-year bond with semi-annual coupons, that's 20 coupon payments—20 opportunities for rates to have fallen, creating friction.

## Why this happens

Bond pricing and YTM are mathematical constructs. The YTM tells you the discount rate that makes the bond's cash flows worth its current price. It's a useful comparative metric, but it's silent on reinvestment reality. The market price doesn't assume you'll magically reinvest coupons at that same rate; it's merely a tool to compare bonds and estimate returns under idealized conditions.

When rates fall, two things happen to bondholders:
1. The bond's market value rises (price risk, a benefit).
2. Coupons must be reinvested at lower rates (reinvestment risk, a cost).

These two forces partially offset. A longer-duration bond's price appreciates more when rates fall, but it also has more coupons to reinvest at lower rates. The balance depends on how far rates fall and how long your time horizon is.

## Worked example: a 10-year bond

You buy a $1,000 par bond with a 4% annual coupon, yielding 4% to maturity. You expect annual coupons of $40 for 10 years, then the $1,000 principal back. The YTM formula says: invest $1,000 today, get $40 per year for 10 years plus $1,000 at year 10, and your annualized return is 4%.

But in year 1, interest rates fall to 3%. Your year 1 coupon ($40) now earns 3%, not 4%. By year 10, that $40 has grown to about $52.09 (at 3%) instead of $59.05 (at 4%). The loss on reinvestment of just that one coupon is roughly $7.

Across all 10 coupons reinvested into a falling-rate environment, the shortfall might total 0.3–0.5% annually—not huge, but enough to reduce your realized return from 4% to 3.5–3.7%.

| Scenario | Coupon reinvestment rate | Bond price change | Net return |
|----------|---|---|---|
| Rates stay at 4% | 4% | Flat | 4.0% |
| Rates fall to 3% | 3% | Price rises | ~3.6% (price gain offsets some reinvestment drag) |
| Rates rise to 5% | 5% | Price falls | ~4.5% (reinvestment gain offsets some price loss) |

## Duration and reinvestment risk trade-off

Longer-duration bonds (those with coupons spread further into the future) face more reinvestment risk because they have more coupons and a longer reinvestment horizon. Conversely, short-duration bonds face less reinvestment risk but more principal redeployment risk: if you hold a 2-year note to maturity and rates have fallen, you're forced to reinvest $1,000 principal into a lower-yield instrument for the remaining years.

[Duration](/duration/) mismatch is the crux: if your time horizon is longer than your bond's duration, you care about reinvestment risk. If your time horizon is shorter, you care more about price risk (the bond might trade down before maturity).

## Zero-coupon bonds and prepayment risk

Zero-coupon bonds sidestep coupon reinvestment risk entirely—they pay nothing until maturity, so there's no cash flow to reinvest. But they're vulnerable to principal reinvestment risk: the entire payment arrives at maturity all at once, and you must reinvest a large lump sum at whatever rates prevail then.

[Callable bonds](/callable-bond/) and [mortgage-backed securities](/mortgage-backed-security/) introduce prepayment risk: if rates fall, the issuer may call the bond or borrowers may refinance, returning your principal early at a time when reinvestment rates are lowest—the worst possible timing.

## Mitigation strategies

**Laddering**: Buy bonds across a range of maturities (one maturing each year). Coupons and maturing principal get reinvested into new rungs of the ladder at prevailing rates, smoothing out market timing risk.

**Bullet maturity matching**: If you know you'll need $100,000 in five years, buy bonds that mature in five years. No reinvestment needed; principal arrives when you need it.

**Immunization**: Structure a bond portfolio so that [duration](/duration/) matches your time horizon. Price risk and reinvestment risk offset, locking in the YTM as realized return.

**Accept higher reinvestment risk for higher initial yield**: A 10-year bond yielding 4.5% exposes you to more reinvestment risk than a 2-year yielding 3.5%, but the premium compensates you if rates don't fall too sharply.

## See also

<div class="wiki-seealso">

### Closely related

- [Yield-to-Maturity](/yield-to-maturity/) — the return assumption embedded in a bond's price
- [Duration](/duration/) — how sensitive a bond is to rate changes; also the "average" reinvestment window
- [Prepayment Risk](/prepayment-risk/) — when bonds are called or principal returned early, forcing reinvestment at inopportune times
- [Coupon Payment](/coupon-payment/) — the periodic interest the bondholder receives
- [Interest Rate Risk](/interest-rate-risk/) — how rate changes affect bond prices

### Wider context

- [Bond](/bond/) — fixed-income instruments and their mechanics
- [Callable Bond](/callable-bond/) — bonds that issuers can redeem before maturity, magnifying reinvestment risk
- [Mortgage-Backed Security](/mortgage-backed-security/) — pools of mortgages where prepayment (refinancing) is a major reinvestment risk
- [Treasury Note](/treasury-note/) — government bonds with moderate duration and lower credit risk

</div>
