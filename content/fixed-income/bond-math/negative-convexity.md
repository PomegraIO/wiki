---
title: "Negative Convexity"
description: "When bond prices gain less from falling interest rates due to embedded call options, creating asymmetric price behavior."
keywords:
  - bond convexity
  - callable bonds
  - interest rate risk
  - bond mathematics
  - call option
  - price appreciation limit
  - bond pricing
---

*A [callable bond](/wiki/callable-bond/) exhibits **negative convexity** when its price appreciation slows as [interest rates](/wiki/interest-rate-risk/) fall, because the [call option](/wiki/call-option/) embedded in the bond becomes in-the-money and the issuer is likely to redeem it. The bondholder captures gains from falling rates only up to the call price; beyond that, the bond's upside is capped while downside remains full. This creates lopsided, asymmetric risk.*

<div class="wiki-hatnote">
See also [Positive Convexity](/wiki/positive-convexity/) for bonds without embedded options, where price gains accelerate as rates fall.
</div>

<aside class="wiki-infobox">

| Aspect | Detail |
|--------|--------|
| **Definition** | Price gain from falling rates is dampened by call exercise |
| **Cause** | Embedded call option becomes more likely to be exercised |
| **Who holds** | Investors in callable corporates, mortgage-backed securities, preferreds |
| **When it matters** | In falling-rate environments; steep bull flatteners |
| **Measurement** | Negative effective duration at low rate levels |
| **Cost to bondholder** | Lost upside captured by issuer refinancing profit |

</aside>

## How negative convexity arises

A typical corporate [callable bond](/wiki/callable-bond/) might have a 5% coupon and be callable at par ($100) after 5 years. If [interest rates](/wiki/federal-funds-rate/) are 4%, the bond trades above par because its coupon exceeds the current [yield curve](/wiki/yield-curve/). As rates fall to 3%, the bondholder expects the bond price to rise to $110 or higher. But the issuer now has an incentive to call the bond—refinancing at 3% saves them money. Once rates fall far enough, the issuer will call, and the bondholder's bond is redeemed at $100, not $110. The price curve flattens.

Mathematically, this is a **short call position**. When you buy a callable bond, you are implicitly short a call option to the issuer. As rates fall (increasing the value of that call to the issuer), the call moves in-the-money and the bondholder's gain is capped. The bond's [price-rate relationship](/wiki/bond-price-formula/) becomes concave—the curve bends downward at low rates—instead of the convex curve of a straight bond.

## Measuring the effect

[Convexity](/wiki/convexity/) is the second derivative of bond price with respect to yield—how much the [duration](/wiki/duration/) changes as rates move. For a non-callable bond, convexity is positive: as yields fall, [duration](/wiki/bond-duration-risk/) lengthens (more rate sensitivity), amplifying upside. For a callable bond, convexity turns negative: as yields fall and the call gets closer to the money, duration shortens (the bond behaves like it will be taken away), dampening upside.

The [option-adjusted spread](/wiki/option-adjusted-spread/) (OAS) captures this cost. A callable bond trading at the same [yield](/wiki/yield-to-maturity/) as a non-callable bond of the same maturity is mispriced. The callable bond's OAS should be wider (higher yield) to compensate for negative convexity. A typical [mortgage-backed security](/wiki/mortgage-backed-security/) (MBS) might be quoted at +100 basis points OAS while a non-callable agency bond is at +40 bps—that 60-bp spread is the cost of negative convexity and [prepayment risk](/wiki/prepayment-risk/).

## When it bites hardest

Negative convexity is most painful in steep bull-flattening scenarios. In 2011, when the [Federal Reserve](/wiki/federal-reserve/) held rates near zero and long-term yields collapsed further on safe-haven demand, callable corporates underperformed straight bonds significantly. The market repriced for call exercise; callable bond prices stalled while non-callables rallied.

[Mortgage-backed securities](/wiki/mortgage-backed-security/) experience acute negative convexity. Homeowners refinance when rates fall, turning the MBS holder's investment into cash that must be reinvested at lower rates. In the 2020 rally (10-year yield fell from 1.9% to 0.5%), MBS pools experienced waves of prepayments, and MBS holders' total returns lagged comparable-maturity Treasuries by 2–3 percentage points.

[Preferred shares](/wiki/preferred-stock/), especially those [callable](/wiki/callable-preferred/) by the issuer, also exhibit this dynamic. A bank might call 5% preferred shares if rates fall to 3%, capping the bondholder's capital appreciation.

## Impact on portfolio management

Investors holding callable bonds face a dilemma. If you believe rates will fall sharply, callable bonds are a poor choice—you'll underperform the [bull market](/wiki/bull-market/). If you're wrong and rates rise, callable bonds protect you only partially because the call option loses value, so you get the full downside. The payoff is skewed.

Some managers actively trade this asymmetry. They buy straight bonds in a falling-rate scenario, short callable bonds (or sell them against longs), and profit from the negative convexity widening. This is a relative-value or [basis trade](/wiki/basis-and-bond-trades/).

Alternatively, investors can buy [interest rate options](/wiki/interest-rate-option/) (swaptions, caps) to hedge their call risk, but the cost of this insurance often exceeds the yield benefit of the callable bond, so it's rarely done at scale.

## Integration into portfolio analytics

Modern [bond analysis](/wiki/bond-basics/) always decomposes [option-adjusted duration](/wiki/effective-duration/) and convexity separately. A callable bond might have a stated [duration](/wiki/duration/) of 4 years in a flat-rate scenario but effective duration of 2.5 years when rates are 200 basis points below the call strike. Risk models must account for this nonlinearity. A 100-basis-point yield shock that would normally move a 4-year bond by 4% might move a callable by only 2% if the call is deep in-the-money.

Portfolio managers use [stress tests](/wiki/stress-testing/) to evaluate negative convexity exposure under various rate scenarios. A portfolio of mortgage securities or callable corporates needs to understand the tail risk of a sharp rate rally—not just the expected return but the maximum pain.

<div class="wiki-seealso">

### Closely related
- [Positive Convexity](/wiki/positive-convexity/) — price acceleration when rates fall on non-callable bonds
- [Callable Bond](/wiki/callable-bond/) — bonds the issuer can redeem before maturity
- [Option-Adjusted Spread](/wiki/option-adjusted-spread/) — yield adjustment for embedded options
- [Duration](/wiki/duration/) — first-order rate sensitivity; negative convexity shortens it in rallies

### Wider context
- [Bond Price Formula](/wiki/bond-price-formula/) — the yield-to-price relationship underlying convexity
- [Interest Rate Risk](/wiki/interest-rate-risk/) — how bonds respond to rate changes
- [Mortgage-Backed Security](/wiki/mortgage-backed-security/) — the most common vehicle for negative convexity
- [Prepayment Risk](/wiki/prepayment-risk/) — homeowner refinancing behavior under falling rates

</div>
