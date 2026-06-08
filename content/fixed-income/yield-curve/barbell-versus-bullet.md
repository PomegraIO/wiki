---
title: "Barbell vs. Bullet Strategy"
description: "Two portfolio constructions for bonds: concentrating at curve extremes (barbell) or the middle (bullet), each with distinct yield, duration, and convexity trade-offs."
keywords:
  - bond portfolio strategy
  - barbell strategy
  - bullet strategy
  - yield curve positioning
  - convexity
  - duration management
image: "/svg/fixed-income.svg"
---

*A barbell strategy concentrates [bond](/bond/) holdings at the short and long ends of the [yield curve](/yield-curve/), skipping the middle maturities. A bullet strategy concentrates near one point. The choice determines yield, [duration](/duration/) sensitivity, [convexity](/volatility-smile/), and reinvestment risk in ways that matter for portfolio performance.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Barbell vs. Bullet — key facts</div>

<img src="/svg/fixed-income.svg" alt="An abstract editorial mark for fixed income." />

<div class="wiki-infobox-caption">How you arrange bonds on the curve shapes how your portfolio moves, reinvests, and profits.</div>

|   |   |
|---|---|
| **Barbell** | Holdings at short and long ends; underweight middle |
| **Bullet** | Concentrated holdings near a single maturity |
| **Barbell yield** | Usually lower (more 2-year, less 10-year exposure) |
| **Bullet yield** | Usually higher (steady pickup across curve) |
| **Barbell convexity** | Positive (profits from large rate moves either direction) |
| **Bullet convexity** | Neutral (less upside from curve twists) |
| **Barbell use case** | When [volatility](/historical-volatility/) is expected; curve shape bets |
| **Bullet use case** | Income focus; neutral on curve shape; ladder approach |

</aside>

## The core trade-off: yield versus positioning

Imagine you manage a portfolio with a 5-year average [duration](/duration/) target. You must fill that duration with something. You can:

1. Buy 5-year [bonds](/bond/) (bullet): concentrated near your target maturity
2. Buy 2-year and 10-year bonds in equal proportion (barbell): same duration average, but split between extremes
3. Buy 3-year and 7-year bonds (a narrower barbell)

All three reach the same duration. But they do not deliver the same returns or risk profile.

A bullet—especially if concentrated in liquid, liquid [on-the-run Treasuries](/treasury-bond/)—offers simplicity and a steady income stream. Coupons arrive predictably; you do not have to think about reinvestment at different points on the curve.

A barbell gives up some near-term yield (the 2-year is lower than the 5-year) but buys you something precious: **positive convexity**. If rates fall sharply, the long-end bonds (the 10-year position) soar in price. If rates rise sharply, the short-end position (the 2-year) does not fall as far, so the portfolio still profits from the curve shape adjustment. You win either direction.

## Why convexity matters

Convexity measures how bond prices accelerate as yields change. A perfectly linear relationship would be a duration-matched bond that rises exactly 5% for a 100-basis-point yield drop. But bonds are nonlinear. A long-duration bond rises *more than* 5% because of convexity; a short-duration bond rises *less*.

The barbell captures this spread. By owning both short and long bonds, you get the short bond's stable floor (no massive drawdown in a rate spike) and the long bond's ceiling (massive gains in a rate plunge). A bullet owns neither extreme, so it sits in the middle of both.

Convexity is worth money, especially in volatile environments. A [hedge fund](/hedge-fund/) or [private equity](/private-equity-fund/) manager betting on a [recession](/recession/) (where rates fall hard and fast) might build a barbell to capture this convexity payoff. An insurance company or pension fund with stable liabilities might choose a bullet to keep things simple.

## The barbell's hidden cost: reinvestment risk

A barbell has a subtle vulnerability. The short-end bonds mature and get reinvested at whatever rates prevail then. If you buy 2-year bonds yielding 3% and rates fall to 2% before maturity, you reinvest at a loss.

A bullet in the middle (say, 7-year bonds at 4%) avoids this lottery. You capture 4% for seven years, then reinvest. The reinvestment date is further out and your decision point is locked in for longer.

This is why the barbell shines in high-rate environments. When short rates are already 5% and the market expects them to fall (recession coming), the barbell locks in 5% for the short end while also owning long bonds that will rally if rates fall. But if rates stay high, the barbell loses to a bullet because it is constantly reinvesting at high rates (good for the barbell, but only if the bullet yield is lower, which is usually true).

## Yield differences: the slope of the curve

The yield pick-up from a bullet versus a barbell depends on how steep the curve is. In a very steep curve (short rates 2%, long rates 5%), a bullet at the 5-year point (say, 3.5%) is vastly superior for income than a barbell split 50/50 between 2% and 5%, which averages only 3.5%—no benefit.

But in a flat or inverted curve (short rates 4.5%, long rates 4%), the barbell becomes more attractive. You get nearly the same average yield (4.25%) but with upside convexity. And if the curve is very steep (short rates 1%, long rates 5%), the bullet begins to look expensive in real terms—you are sacrificing 4% of yield for the convenience of staying in one place.

The curve's shape is the determinant. Investors obsessively track whether the [2s10s spread](/2s10s-spread/) is steep, flat, or inverted because that determines whether to barbell or bullet. A steep curve rewards bullets; a flat curve rewards barbells.

## Practical variations: the ladder and the dumbbell

A **ladder** is a barbell lite: you buy bonds across all maturities (1-year, 2-year, 3-year, ..., 10-year) in equal proportions. This removes the art of picking the "best" short and long bonds. As each bond matures, you reinvest at the long end, continuously rolling. Ladders are popular with individual investors because they are mechanical and reduce timing risk.

A **dumbbell** is a tight barbell: you own short bonds and long bonds but within a narrower range—say, 2-year and 5-year. This avoids the reinvestment lottery of a super-short position while still capturing some convexity.

## When barbells win

1. **Volatility is high.** If [interest rate](/interest-rate/) volatility is expected to spike ([VIX](/historical-volatility/) is climbing, economic data is chaotic), convexity is valuable. The barbell profits from large moves; the bullet is blind to them.

2. **The Fed is at an inflection.** When [monetary policy](/monetary-policy/) is about to shift dramatically (peak tightening, about to cut), the barbell is more profitable. You own short bonds that are already pricing a policy peak and long bonds that will rally if cuts come.

3. **You think rates will curve-steepen.** If short rates are expected to stay high but long rates are expected to fall (classic recession signal), the barbell wins. You own the 2-year that stays high and the 10-year that rallies.

## When bullets win

1. **The curve is very steep.** If short rates are 2% and long rates are 5%, a 5-year bullet at 3.5% gives you compelling income. A barbell earning 3.5% average is not worth the complexity.

2. **You have a known liability.** A pension fund owing $100 million in 7 years should buy 7-year bonds (a bullet at 7) to match the liability exactly. A barbell creates reinvestment and timing risk with no upside.

3. **You value simplicity.** A bullet is easier to manage, explain, and rebalance. Transaction costs are lower. For passive or retail investors, complexity is not rewarded.

## Central banks and curve control

During the 2010s, central banks bought bonds in specific maturity buckets to control the curve shape. The [Federal Reserve](/federal-reserve/) used its balance sheet like a barbell manager: buying longer-dated bonds while letting short rates be set by [monetary policy](/monetary-policy/). The effect was to steepen the curve and boost long-duration bond prices. This "Operation Twist" logic is pure barbell.

The opposite happened in 2022–23, when the Fed allowed its balance sheet to run off (shrink) and short-term rates to rise faster than long-term rates. The curve flattened, and barbell strategies underperformed.

## See also

<div class="wiki-seealso">

### Closely related

- [Yield curve](/yield-curve/) — the structure that barbell and bullet strategies exploit
- [Bond](/bond/) — the fundamental security; both strategies own them
- [Duration](/duration/) — the portfolio risk measure both strategies target
- [Convexity](/volatility-smile/) — the payoff the barbell captures that the bullet does not
- [2s10s spread](/2s10s-spread/) — determines whether the curve favours barbells or bullets
- [Reinvestment risk](/reinvestment-risk/) — the hidden cost the barbell bears

### Wider context

- [Interest rate](/interest-rate/) — what moves both strategies' holdings
- [Volatility](/historical-volatility/) — when convexity becomes most valuable
- [Monetary policy](/monetary-policy/) — the driver of curve shape shifts
- [Federal Reserve](/federal-reserve/) — whose actions flatten or steepen the curve
- [Recession](/recession/) — often preceded by curve flattening, which favours barbells
- [Asset allocation](/asset-allocation/) — the higher-level framework containing these tactical bets

</div>
