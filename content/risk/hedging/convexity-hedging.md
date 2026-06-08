---
title: "Convexity Hedging"
description: "Neutralising the second-order interest-rate sensitivity of bond portfolios, guarding against duration-matching failures in non-parallel yield-curve shifts."
keywords:
  - convexity hedging
  - negative convexity
  - swaptions
  - interest-rate sensitivity
  - bond risk management
image: "/svg/risk.svg"
---

*A **convexity hedge** addresses the curvature in a bond's price-yield relationship. When yield-curve movements are large or non-uniform, [duration](/duration-hedging/) alone no longer protects. Convexity hedging uses swaptions and other [interest-rate derivatives](/interest-rate/) to neutralise the second-order sensitivity that duration ignores.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Convexity Hedging — key facts</div>

<img src="/svg/risk.svg" alt="An abstract editorial mark for risk and hedging." />

<div class="wiki-infobox-caption">Going beyond first-order risk; the difference between safe and brittle.</div>

|   |   |
|---|---|
| **What it is** | Hedging the second-order (convexity) risk in bond or interest-rate portfolios |
| **Also called** | Gamma hedging in fixed income, convexity management |
| **Why it matters** | Negative convexity can amplify losses in large yield moves; long convexity protects |
| **Key instrument** | Swaptions, caps and floors, [callable bonds](/callable-bond/) |
| **Typical holder** | Mortgage servicers, [bond portfolios](/corporate-bond/), [banks](/central-bank/) with rate risk |
| **Risk managed** | Non-parallel yield shifts, large moves beyond duration assumption |

</aside>

## The hidden non-linearity

A bond's price falls when yields rise, but the relationship is not linear. A 1% yield rise causes a larger price drop than a 1% yield fall causes a price gain, holding duration constant. This asymmetry is **negative convexity**, and it hits hardest in volatile markets or when yield moves are large.

[Duration](/duration-hedging/) is the first derivative: it measures the sensitivity of bond price to a small, parallel shift in yields. If a portfolio has a duration of 5 years, a 1 basis-point yield rise drops the price by approximately 5 basis points. But this approximation only holds for small moves. A 100 basis-point yield move will cause a loss that is noticeably worse than the duration model predicts, because the price-yield curve is convex (bends upward), not straight.

Most bond portfolios are naturally short convexity. A holder of fixed-rate bonds loses more when yields rise sharply than they gain when yields fall sharply. Mortgage servicers are especially exposed: borrowers refinance when rates fall (locking in losses for the servicer), but when rates rise, prepayments slow and the servicer collects low coupons on a longer portfolio. This is embedded negative convexity, and it is costly.

## When duration hedging fails

Suppose a portfolio manager has matched the duration of her bond portfolio to the duration of her liabilities, creating a [duration hedge](/duration-hedging/). If all yields move together (a parallel shift), the hedge works: assets and liabilities decline by roughly the same amount. But if yields do not shift in parallel—if short rates rise more than long rates, or vice versa—the duration match is no longer sufficient. The convex curvature of both assets and liabilities magnifies the divergence.

Consider a bank with a 5-year duration liability (a retail deposit base repricing in ~5 years) and a 5-year duration asset (a portfolio of corporate bonds). A 1% parallel yield rise drops both the asset and liability values proportionally, and the hedge is intact. But if instead short yields rise by 2% and long yields rise by 0.5%, the duration assumption breaks down. The assets (long-duration bonds) fall less than expected; the liabilities (short-duration deposits) reprice faster. The mismatch appears, and convexity becomes material.

Similarly, negative convexity can turn a seemingly neutral position into a loss-maker. If a hedge uses [interest-rate swaps](/interest-rate/) (which are linear and thus convexity-neutral) to offset a negative-convexity asset, the position is duration-hedged but convexity-exposed. A sharp yield move will leave the swap unhedged against the convex loss in the underlying bond.

## The convexity hedge tools

**Swaptions** (options on interest-rate swaps) are the standard instrument. A payer swaption gives the right to enter a swap and pay fixed; a receiver swaption gives the right to receive fixed. A portfolio short convexity can buy receiver swaptions, which gain value if yields fall sharply (and the portfolio's negative convexity loss is severe). This is expensive insurance; swaption premiums are material, especially in low-volatility environments.

**Caps and floors** on floating-rate liabilities also provide convexity protection. A borrower with a floating-rate loan can buy a cap (a series of [call options](/call-option/) on the floating rate) to limit losses if rates spike. The cap has positive convexity: it gains more when rates rise sharply than it loses when rates stay stable.

Callable bonds themselves embody convexity hedges, albeit in reverse. The issuer of a callable bond has sold an embedded option to the bondholder, meaning the issuer is short convexity. The bondholder is long convexity and profits if rates fall sharply and the issuer exercises the call.

## The calculation and cost

Convexity is measured as the second derivative of price with respect to yield, or equivalently as the percentage change in duration for a 1% change in yield. A bond with a duration of 5 and a convexity of 50 will have a modified duration of roughly 4.5 when yields rise by 1% (because the higher yield causes duration to shorten), but a modified duration of 5.5 when yields fall by 1%.

To hedge convexity, a portfolio manager estimates the portfolio's net convexity (long or short), then sizes an offsetting position in swaptions or other convexity instruments to bring it to neutral. The cost is the option premium, which varies with volatility and time to expiry.

In a low-volatility environment, swaption premiums are cheap, and buying convexity protection is relatively inexpensive. In a high-volatility environment, premiums spike, and hedging convexity becomes costly. Many portfolio managers therefore buy convexity hedges opportunistically—when premiums are cheap—and scale back when volatility abates.

## Who bears convexity risk

Mortgage servicers, by law and by economics, are natural short-convexity players. They do not own the mortgages outright; they service them for a fee. When rates fall, borrowers prepay, and the servicer loses the future fee stream. The servicer is hedged neither by duration nor by rate floors, because the loss is in *optionality*, not in interest income. Many servicers therefore maintain a standing position in receiver swaptions or other convexity hedges.

Banks holding mortgage-backed securities (MBS) also carry embedded negative convexity, though less acute than servicers. The MBS has a negative-convexity pass-through: when rates fall and borrowers prepay, the bank loses the remaining duration hedge and is exposed to reinvestment risk.

Insurers and pension funds holding long-duration liabilities often hedge convexity implicitly by holding some equities or inflation-linked assets that behave differently in the large yield-move scenarios where convexity matters most.

## See also

<div class="wiki-seealso">

### Closely related

- [Duration hedging](/duration-hedging/) — matching interest-rate sensitivity across asset and liability portfolios
- [Gamma hedging](/gamma-hedging/) — managing second-order price sensitivity in options portfolios
- [Callable bond](/callable-bond/) — a bond with an embedded option allowing the issuer to call it early
- Swaptions — options granting the right to enter or exit an interest-rate swap
- [Interest rate risk](/interest-rate-risk/) — the sensitivity of bond portfolios to changes in yields
- [Yield-curve](/yield-curve/) — the relationship between bond yields and time to maturity

### Wider context

- [Mortgage-backed security](/mortgage-backed-security/) — securities backed by pools of mortgages with embedded prepayment risk
- [Interest-rate swap](/interest-rate/) — exchange of fixed for floating payments or vice versa
- [Option pricing](/black-scholes-model/) — valuation of interest-rate derivatives
- Risk management — systematic identification and mitigation of financial risk
- Portfolio hedging — offsetting risk across asset and liability portfolios

</div>
