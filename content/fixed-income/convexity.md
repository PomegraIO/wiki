---
title: "Convexity"
description: "Convexity is the degree to which the relationship between bond prices and yields is curved. Positive convexity means bonds gain more from falling rates than they lose from rising rates."
keywords:
  - convexity
  - bond convexity
  - positive convexity
  - negative convexity
  - duration
image: "https://picsum.photos/seed/convexity/900/600"
---

*The **convexity** of a bond measures the curvature in the relationship between its price and [yield](/yield-to-maturity). The relationship is not linear — bonds with positive convexity gain more in price when yields fall than they lose when yields rise (by the same amount). Negative convexity (seen in [callable bonds](/callable-bond)) means the opposite.*

<div class="wiki-hatnote">

For the linear sensitivity measure, see [duration](/duration). For callable bonds with negative convexity, see [callable bond](/callable-bond).

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Convexity — key facts</div>

<img src="https://picsum.photos/seed/convexity/900/600" alt="A graph showing the curved relationship between bond price and yield" />

<div class="wiki-infobox-caption">Positive convexity creates asymmetric gains: bonds gain more from rate falls than they lose from rate rises.</div>

|   |   |
|---|---|
| **What it is** | Curvature in the price-yield relationship |
| **Positive convexity** | Price gains > price losses (same rate move) |
| **Negative convexity** | Price gains < price losses (same rate move) |
| **Straight bonds** | Positive convexity (most common) |
| **Callable bonds** | Negative convexity (call limits upside) |
| **Duration** | Linear approximation; convexity is the correction |
| **Calculation** | Complex; second derivative of price with respect to yield |

</aside>

## Linear vs. curved relationship

[Duration](/duration) assumes a linear relationship between bond prices and yields: if a bond has duration 5, a 1% yield rise causes a 5% price decline; a 1% yield fall causes a 5% price gain.

In reality, the relationship is curved. A bond's price-yield curve is convex (bowed outward). This means:

- When yields fall 1%, the price rises more than 5% (better than duration predicts)
- When yields rise 1%, the price falls less than 5% (better than duration predicts)

This asymmetry is **positive convexity**, and it benefits bondholders.

## Why convexity exists

Convexity exists because of how compounding and timing work. When yields fall significantly, the impact of lower rates on future cash flows accelerates (non-linearly). When yields rise significantly, the impact decelerates.

For a [zero-coupon bond](/zero-coupon-bond), the convexity effect is powerful because all cash flow is at maturity. For a high-coupon bond, convexity is weaker because coupons are returned early.

## The mathematical measure

Convexity is measured as a positive or negative number. A bond with high positive convexity has a strong curved relationship. A bond with low or negative convexity has a weak or inverted curved relationship.

For practical purposes, convexity is small — typically in the range of 50–200 basis points of additional return for a 100-basis-point yield move. For large rate moves, convexity becomes material.

## Positive vs. negative convexity

**Positive convexity** (straight bonds, most securities):
- Price gains exceed price losses (by the same yield move)
- Favorable for bondholders
- Common in [Treasury securities](/treasury-bond), [corporate bonds](/corporate-bond), [municipal bonds](/municipal-bond)

**Negative convexity** ([callable bonds](/callable-bond), [mortgage-backed securities](/mortgage-backed-security)):
- Price gains are capped or limited
- Price losses can exceed gains
- Unfavorable for bondholders
- Compensated with higher yields

## Callable bonds and negative convexity

[Callable bonds](/callable-bond) have negative convexity because the issuer's call option limits bondholders' upside. When rates fall dramatically and a straight bond would appreciate sharply, the issuer calls the bond at the call price, capping the bondholder's gain.

Conversely, when rates rise, the bond depreciates, but the issuer doesn't call. The bondholder bears full downside.

This asymmetry is why [callable bonds](/callable-bond) yield more than straight bonds — investors demand compensation for negative convexity.

## Mortgage-backed securities and negative convexity

[Mortgage-backed securities](/mortgage-backed-security) also exhibit negative convexity due to [prepayment risk](/mortgage-backed-security). When rates fall and homeowners refinance, the MBS investor receives principal early and must reinvest at lower rates. The upside from falling rates is limited.

This prepayment-driven negative convexity is why MBS yields more than [Treasury securities](/treasury-bond) of comparable duration.

## Portfolio convexity

A portfolio's convexity is the weighted average of its holdings' convexities. A portfolio of 50% straight bonds (positive convexity) and 50% [callable bonds](/callable-bond) (negative convexity) might have near-zero or slightly negative total convexity.

Sophisticated bond managers actively manage portfolio convexity. In low-volatility environments, positive convexity has value; in high-volatility environments, it has more value.

## Using convexity in analysis

For large interest-rate moves (exceeding 1–2%), convexity becomes material. The formula becomes:

**Price change ≈ -duration × yield change + (1/2) × convexity × (yield change)²**

For a small move (0.5%), the convexity term is negligible. For a large move (2%), the convexity term is material.

Professional bond traders and portfolio managers incorporate convexity into their analysis, particularly when they anticipate large rate moves or when evaluating [callable bonds](/callable-bond) or [mortgage-backed securities](/mortgage-backed-security).

## See also

<div class="wiki-seealso">

### Closely related

- [Duration](/duration) — the linear sensitivity measure
- [Callable bond](/callable-bond) — exhibits negative convexity
- [Mortgage-backed security](/mortgage-backed-security) — prepayment creates negative convexity
- [Yield to maturity](/yield-to-maturity) — affects convexity calculations
- [Interest rate](/interest-rate) — moves create convexity effects

### Wider context

- [Bond](/bond) — debt securities in general
- [Portfolio management](/hedge-fund) — convexity is managed actively
- [Central bank](/central-bank) — rate moves create convexity exposure
- [Volatility](/stock) — affects the value of convexity
- [Risk management](/diversification) — convexity is one form of interest-rate risk

</div>
