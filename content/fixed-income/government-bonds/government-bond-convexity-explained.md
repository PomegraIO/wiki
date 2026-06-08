---
title: "Government Bond Convexity Explained"
description: "How convexity causes bond price sensitivity to change with yield moves, and why it benefits long-duration Treasury holders."
keywords:
  - government bond convexity explained
  - bond convexity duration
  - convexity treasury bonds
  - positive convexity benefit
  - yield and convexity relationship
image: "/svg/fixed-income.svg"
---

*A bond's **convexity** describes how its price sensitivity accelerates or decelerates as yields shift. While **duration** tells you the bond's average time to cash flows—and estimates price change for a 1% yield move—convexity fine-tunes that estimate by accounting for the fact that the relationship is not linear. Government bonds typically have positive convexity, meaning they gain more when yields fall than they lose when yields rise by the same amount.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Bond Convexity — key facts</div>

<img src="/svg/fixed-income.svg" alt="An abstract editorial mark for fixed-income markets." />

<div class="wiki-infobox-caption">Convexity corrects duration's straight-line assumption and reveals why long-term Treasuries outperform in volatile rate environments.</div>

|   |   |
|---|---|
| **Definition** | Curvature of the price-yield relationship; second derivative of bond price |
| **Units** | Expressed as a percentage change per 1% yield move, squared |
| **Positive convexity** | Bond prices accelerate upward when yields fall; decelerate downward when yields rise |
| **Negative convexity** | Callable bonds lose this advantage; upside is capped as yields fall |
| **Typical non-callable bond** | Positive; a free option to bondholders |
| **Duration limitation** | Linear approximation breaks down for large yield moves |
| **Interest-rate environment** | High volatility regimes reward positive convexity heavily |

</aside>

## Duration alone is incomplete

Most fixed-income professionals think of bond price sensitivity through **duration**: a simple number (e.g., 7 years) that estimates how much the bond price will fall if yields rise by 1%. If a 10-year Treasury has a duration of 8.5 years, a 1% rise in yield is expected to drop the price by about 8.5%.

But that estimate is only approximately correct. It works well for small yield changes. For larger moves—say, a 2% rise or fall—duration's linear approximation accumulates error. The reality is that the bond price-yield relationship is not a straight line; it is a curve. That curve is what convexity measures.

## The price-yield curve and why it bends

Imagine a bond paying a fixed coupon and maturing in 10 years. As yields rise, the present value of all those future cash flows declines, so the bond price falls. But the relationship is not 1:1. Here is why:

When yields are already high (say, 6%), a further 1% increase (to 7%) reduces the present value of future coupons by a smaller percentage than when yields are low (say, 2%), because the starting discount rate was already steep. Conversely, when yields are low and you fall 1% further (from 2% to 1%), the discount rate halves, so present values nearly double—a much larger percentage gain.

This is the essence of convexity: the bond price does not fall in a straight line as yields rise, and it does not rise in a straight line as yields fall. The curve is convex—it bends upward, especially for long-duration bonds.

## Quantifying convexity

**Convexity** is formally the second derivative of bond price with respect to yield. In simpler terms, it is the rate of change of duration itself as yields move. A bond with high convexity experiences duration that shortens significantly when yields rise (reducing the downside) and lengthens when yields fall (amplifying the upside).

For a non-callable bond, convexity is always positive. The market prices this in: a bond with higher convexity tends to trade at a higher price relative to pure duration-based models, reflecting the value of that asymmetry.

The magnitude of convexity depends on the **maturity** and **coupon** of the bond:

- **Long-maturity bonds** have higher convexity. A 30-year zero-coupon bond has enormous convexity because the entire cash flow sits at the end; small yield moves cause massive percentage swings in the present value.
- **Low-coupon bonds** have higher convexity. When coupons are small relative to par, the bond behaves more like a zero-coupon bond, with all the convexity risk concentrated in the maturity payment.
- **High-coupon bonds** have lower convexity. More cash flows come early, reducing the tail risk and dampening the yield-price curve.

## A numeric example

Suppose you hold a hypothetical 10-year, 3% coupon Treasury with par value 100, currently yielding 3% (trading at par). The bond has an estimated **modified duration** of approximately 8.9 years.

**Scenario 1: Yields rise to 4%**

Duration estimate: Price change ≈ −8.9 × 1% = −8.9%, so predicted price ≈ 91.1.

Actual price (computed as PV of future coupons and par): The coupons (3.0 per year) and final par (100) discounted at 4% yield a price of approximately 90.8.

The **duration estimate overstated the loss by 0.3 percentage points** because convexity partially cushioned the downside.

**Scenario 2: Yields fall to 2%**

Duration estimate: Price change ≈ +8.9 × 1% = +8.9%, so predicted price ≈ 108.9.

Actual price (discounted at 2%): Approximately 109.3.

The **actual gain exceeded the duration estimate by 0.4 percentage points** because convexity added upside.

Over a 2% yield swing, the asymmetry is small but visible. For a 30-year bond or in a 5% rate environment, the convexity correction becomes material. This is why traders and portfolio managers explicitly price convexity when managing interest-rate risk.

## Positive convexity as an embedded option

Convexity for a non-callable bond is a free option: the bondholder benefits if rates fall sharply and rates rise sharply in equal measure. The bondholder wins both ways, and loses less in the up-rate scenario.

**Callable bonds** (many government bonds, including some Treasuries, and most corporate bonds) have negative convexity embedded. When yields fall, the issuer calls the bond away, capping the bondholder's upside. The price curve flattens at the top, reversing the convexity to negative. Investors demand a higher yield (lower price) to compensate for this embedded short call.

## Government bonds and convexity in practice

U.S. Treasury bonds are not callable (except for the oldest issues), so they carry positive convexity. This is one reason longer-dated Treasuries outperform during large rate rallies: the convexity gain amplifies the duration gain. In contrast, when rates rise sharply, the convexity loss is smaller (because duration works against the bondholder more than convexity can offset), so longer bonds underperform less than a pure duration model would predict.

Central banks and bond traders explicitly manage convexity. A portfolio heavily skewed to long bonds will have high convexity; a barbell portfolio (short and long maturity bonds, no middle) will have even higher convexity. Conversely, a bullet portfolio (all bonds clustered at one maturity) has lower convexity.

During high-volatility rate environments—such as the inflation shock of 2021–2022—convexity became visible to the broader market. Traders who owned long Treasuries with positive convexity benefited disproportionately from both the up and down rate moves. Conversely, strategies that had sold convexity (e.g., selling long-dated puts or owning callable bonds) suffered.

## Measuring and hedging convexity

Bond traders use **convexity numbers** in basis points of price change per 1% yield move, squared. A typical 10-year Treasury might have a convexity of 80–90 basis points. This means that for every 1% move in yields beyond the duration effect, price sensitivity increases or decreases by that convexity amount.

To hedge convexity risk, traders might adjust the duration of their portfolio or use swaptions and bond options to offset the embedded convexity of their positions. A portfolio manager with excess positive convexity might sell long-dated calls; one with negative convexity might buy them.

## See also

<div class="wiki-seealso">

### Closely related

- [Duration](/duration/) — the linear approximation convexity corrects
- [Bond](/bond/) — foundational instrument whose price convexity affects
- [Yield-to-Maturity](/yield-to-maturity/) — the discount rate that drives the price-yield relationship
- [Treasury Bond](/treasury-bond/) — government bonds with textbook positive convexity
- [Interest-Rate Risk](/interest-rate-risk/) — the core risk convexity measures and adjusts

### Wider context

- Fixed-Income Markets — where convexity trading occurs
- [Central Bank](/central-bank/) — rate moves that create convexity trading opportunities
- [Callable Bond](/callable-bond/) — bonds with negative convexity due to the issuer's embedded call
- [Yield Curve](/yield-curve/) — the environment where convexity interacts with curve positioning

</div>
