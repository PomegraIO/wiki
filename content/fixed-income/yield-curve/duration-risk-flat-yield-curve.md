---
title: "Duration Risk When the Yield Curve Is Flat"
description: "Why a flat yield curve reduces reward-per-unit-duration-risk, making extended maturities less attractive and requiring careful position sizing."
keywords:
  - duration risk flat yield curve
  - flattening yield curve
  - bond maturity allocation
  - interest rate risk
  - term premium compression
image: /svg/fixed-income.svg
---

*When the [yield curve](/yield-curve/) is flat, **duration risk**—the interest-rate sensitivity of a bond portfolio—offers little extra reward. In a normal curve, a 10-year bond yields 1–2% more than a 2-year bond, compensating investors for the added price volatility if rates rise. But in a flat curve, that premium narrows to 0–50 basis points or vanishes entirely, meaning investors accept the same duration risk for much less additional [yield](/yield-to-maturity/). This unfavorable risk-return trade-off forces portfolio managers to either shorten [duration](/duration/), accept below-market returns, or hunt for credit or other alternative sources of yield.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Duration in a Flat Curve — key facts</div>

<img src="/svg/fixed-income.svg" alt="An abstract editorial mark for fixed income." />

<div class="wiki-infobox-caption">Flat curves reward extend-the-curve bets poorly; managers must choose between duration drag and credit hunting.</div>

|   |   |
|---|---|
| **Normal curve scenario** | 2-yr: 3%, 10-yr: 4.5%; term premium = +150 bps |
| **Flat curve scenario** | 2-yr: 4.5%, 10-yr: 4.6%; term premium = +10 bps |
| **Duration of 10-yr bond** | ~8.5 years (typical maturity) |
| **Price sensitivity** | –0.85% per 100 bps rate rise (both scenarios) |
| **Risk reward ratio** | High in normal curve; poor in flat curve |
| **Portfolio response** | Shorten [duration](/duration/), increase [credit](/credit-risk/), or tilt to [floating-rate](/duration/) bonds |

</aside>

## The term premium and why it matters

In a normal [yield curve](/yield-curve/), the **term premium** is the extra yield you earn for holding longer-dated bonds. A 10-year Treasury might yield 4.5% when the 2-year yields 3%, offering an extra 150 basis points (1.5%) to compensate you for:

1. **Interest-rate risk**: A bond with 8–10 years of [duration](/duration/) loses much more in price if rates rise than a 2-year bond.
2. **Inflation uncertainty**: Inflation expectations are harder to predict 10 years out, so you demand a cushion.
3. **Liquidity**: 10-year bonds are less liquid than 2-years in some market conditions.
4. **Reinvestment risk**: If you buy a 2-year bond, you'll need to roll it into a new position at an uncertain future rate.

The term premium is the market's way of saying: "Yes, extending [duration](/duration/) is riskier; here's extra yield to compensate." That is the reward side of the risk-reward trade-off.

## What happens when the curve flattens

When the curve flattens—when the gap between 10-year and 2-year yields shrinks to near zero—the term premium disappears. The 10-year might yield 4.6% while the 2-year yields 4.5%. Suddenly, you're accepting an extra 8–10 years of [duration risk](/duration/) (price volatility if rates change) for only 10 basis points of extra annual return.

That 10 bps does not come close to compensating for the additional risk. Here's why:

If rates rise by 100 basis points:
- **2-year bond** (duration ≈ 2 years): Price falls ~2%.
- **10-year bond** (duration ≈ 8–9 years): Price falls ~8–9%.

Over a single year, the 10 bps extra yield barely offsets the additional mark-to-market loss risk. And if rates rise by 200 bps, the 10-year's drawdown is so much larger that the extra yield is almost irrelevant—you've incurred 4–5x more price risk for a 10 bps yield boost.

## Duration risk in a flat curve: the math

Consider two portfolios with $100 million each:

**Portfolio A (short [duration](/duration/), flat-curve environment)**
- Allocation: 100% 2-year bonds at 4.5% yield.
- Duration: ~2 years.
- Annual carry: $4.5 million.

**Portfolio B (extended [duration](/duration/), flat-curve environment)**
- Allocation: 100% 10-year bonds at 4.6% yield.
- Duration: ~8.5 years.
- Annual carry: $4.6 million.

Assuming a +100 bps rate move:
- Portfolio A loses ~$2 million in price (–2%).
- Portfolio B loses ~$8.5 million in price (–8.5%).

Portfolio B's extra $0.1 million in annual yield does not remotely compensate for the $6.5 million additional loss. On a risk-adjusted basis, Portfolio A is superior.

This is the central insight: **in a flat curve, extending [duration](/duration/) is a poor trade.** The asymmetry is worst when the curve is nearly flat (0–25 bps term premium) and slightly better when the curve has just begun flattening (still 75–100 bps premium), but the fundamental problem persists.

## How managers respond

Portfolio managers facing a persistently flat curve make several strategic choices:

**1. Shorten duration**
Hold shorter-dated bonds or floating-rate notes. Accept lower absolute yield but reduce interest-rate risk. This is the most common response in institutional portfolios, especially for liability-matched strategies.

**2. Reach for credit**
Instead of extending maturity, increase [credit risk](/credit-risk/). A 5-year [investment-grade bond](/investment-grade-bond/) might yield 3.8%, while a 5-year [high-yield bond](/high-yield-bond/) yields 5.5%—a 170 bps pick-up with less [duration risk](/duration/) than a 10-year IG bond. The trade-off: [default risk](/default-rate/) instead of rate risk.

**3. Move into floating-rate or asset-backed structures**
[Floating-rate bonds](/duration/) have near-zero duration and [money-market funds](/money-market-fund/) offer steady, near-risk-free income when short-term rates are elevated. These cushion portfolios from rate-risk losses.

**4. Tilt to [inflation-protected bonds](/tips/) if breakeven inflation rates are attractive**
[TIPS](/tips/) (Treasury Inflation-Protected Securities) have built-in inflation hedges; in a low-[real-interest-rate](/real-interest-rate/) regime, they can offer better value than nominal bonds.

**5. Use the curve for tactical positioning**
Some managers will short the 10-year and long the 2-year, betting the curve will steepen—a "curve flattener" trade. If successful, the trade profits regardless of the absolute level of rates.

## Historical flat-curve environments

Flat and inverted yield curves often precede recessions:
- **2006–2007**: The curve inverted before the 2008 financial crisis; investors who shortened [duration](/duration/) and avoided [subprime](/mortgage-backed-security/) credit preserved capital.
- **2019**: The curve briefly inverted; a year later, the COVID-19 crash hit; managers who had shifted to shorter [duration](/duration/) and defensive credit fared better than those extended.
- **2022–2023**: The curve flattened sharply after the Fed raised rates; managers who had hugged shorter maturities and higher-quality credit avoided the worst drawdowns.

The economic intuition is sound: a flat curve often signals that the market is pricing in slower economic growth and the possibility of [recession](/recession/). Extending [duration](/duration/) just before a downturn—when spreads are about to widen, rates are about to fall, and [defaults](/default-rate/) will rise—is a poor trade, even if the curve steepens afterward.

## Quantifying duration position sizing

A formal approach uses the **reward-to-risk ratio** for extending [duration](/duration/):

(10-year yield − 2-year yield) / (10-year duration − 2-year duration)

In a normal curve (150 bps premium, 6-year duration difference):
Ratio = 150 / 6 = 25 bps of extra yield per year of extra [duration](/duration/)—acceptable.

In a flat curve (10 bps premium, 6-year duration difference):
Ratio = 10 / 6 = 1.67 bps per year of extra [duration](/duration/)—unacceptable.

Managers set threshold ratios (often 10–15 bps minimum) below which extending [duration](/duration/) is "off the menu." This discipline prevents portfolio drift into excessive maturity extension when the yield curve cannot justify it.

## See also

<div class="wiki-seealso">

### Closely related

- [Duration](/duration/) — measures interest-rate sensitivity of a bond.
- [Yield curve](/yield-curve/) — the relationship between bond yields across maturities.
- [Interest rate risk](/interest-rate-risk/) — how rising rates erode bond prices.
- [Term premium](/duration/) — the extra yield for extending maturity.
- [Credit risk](/credit-risk/) — the alternative risk source when extend-the-curve no longer pays.
- [Real interest rate](/real-interest-rate/) — what drives [yield curve](/yield-curve/) slope in real terms.

### Wider context

- [Recession](/recession/) — flat and inverted curves often precede downturns.
- [Treasury bond](/treasury-bond/) — core holdings in duration-managed portfolios.
- [Money market fund](/money-market-fund/) — short-[duration](/duration/) alternative when the curve is flat.
- [TIPS](/tips/) — inflation-protected alternative in low-[real-interest-rate](/real-interest-rate/) environments.
- [Floating-rate bond](/duration/) — zero [duration](/duration/) option to avoid rate risk.

</div>
