---
title: "Prepayment Risk in Mortgage-Backed Securities"
description: "How prepayment risk in mortgage-backed securities forces reinvestment at lower rates when borrowers repay early, reducing investor returns."
keywords:
  - prepayment risk
  - mortgage-backed securities
  - early repayment
  - mortgage pools
  - reinvestment risk
  - bond risk
---

*Prepayment risk in mortgage-backed securities arises when homeowners pay off their mortgages ahead of schedule, forcing investors to reinvest principal at potentially lower interest rates. Unlike default risk, which centers on whether a borrower will pay at all, **prepayment risk** is the cost of borrowers paying too well—at exactly the wrong time.*

<div class="wiki-hatnote">

This article covers prepayment as a risk to investors holding mortgage-backed securities. For the corresponding borrower benefit, see refinancing incentives. This is distinct from prepayment penalties, which are borrower-paid fees.

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Prepayment Risk — key facts</div>

<img src="/svg/risk.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Prepayment shortens bond duration and caps upside when rates fall.</div>

|   |   |
|---|---|
| **Also called** | Extension risk (when rates rise and prepayments fall) |
| **Who bears it** | Investors in [mortgage-backed-securities](/mortgage-backed-security/) and [callable-bonds](/callable-bond/) |
| **Trigger** | Mortgage refinancing when rates drop; home sales; lump-sum payoffs |
| **Main consequence** | Forced reinvestment of principal at lower yields |
| **Related risk** | [Reinvestment-risk](/reinvestment-risk/), [duration](/duration/) mismatch |
| **How managed** | Diversification, duration analysis, [derivatives-hedging](/derivatives-hedging/) |

</aside>

## The mechanics of prepayment in mortgage pools

A [mortgage-backed-security](/mortgage-backed-security/) is not a single loan; it's a pool of hundreds or thousands of residential mortgages. The investor buys a [bond](/bond/) backed by the cash flows—principal and interest—from all those mortgages combined. Most mortgages are 30-year fixed-rate instruments, but homeowners are free to pay them off early without penalty.

When a homeowner refinances (taking out a new mortgage at a lower rate to pay off the old one), that portion of principal returns to the security holder immediately. When a homeowner sells their house, the sale proceeds pay off the remaining mortgage balance. When a borrower simply pays extra principal, that accelerates the schedule. All of these are prepayments.

The investor's problem: when rates fall and refinancing becomes attractive, prepayments accelerate. The investor receives a flood of principal just when new bond yields are lowest—the worst possible moment to redeploy that cash. Conversely, when rates rise and refinancing becomes unattractive, prepayments slow and the investor is stuck with a bond that behaves like a much longer-duration instrument than expected. This asymmetry is the heart of prepayment risk.

## Why prepayment risk differs from default risk

[Default risk](/credit-risk/) is the chance a borrower stops paying and never recovers. Prepayment risk is the opposite: it materializes when borrowers pay *too much, too soon*. Both reduce expected return, but the mechanisms differ sharply.

Default risk hits the investor with a loss—principal and interest are forgone. Prepayment risk doesn't destroy capital; it simply returns capital early and leaves the investor underemployed. A $100,000 principal return is still $100,000, but receiving it in year 5 instead of year 15 at a 2% reinvestment rate instead of 4% cuts the lifetime return on that money.

This distinction matters for valuation. A high-yield [mortgage-backed-security](/mortgage-backed-security/) and a high-yield corporate [bond](/bond/) of the same nominal duration are not equivalent: the MBS is worth less because of embedded prepayment optionality. The homeowner, in effect, owns a free [call-option](/call-option/) to refinance—and that option is extracted from the investor's return.

## Duration mismatch and the negative convexity trap

[Duration](/duration/) measures how much a bond's price moves when yields shift. For most bonds, duration works symmetrically: when yields fall 1%, the bond price rises predictably. When yields rise 1%, it falls by roughly the same amount. Not so for mortgage-backed securities.

When yields fall:
- The bond price starts to rise (duration effect).
- But prepayments accelerate, shortening duration unexpectedly.
- The investor's upside is capped because principal comes back early, locked into low reinvestment rates.

When yields rise:
- The bond price falls (duration effect).
- Prepayments slow, extending duration unexpectedly.
- The investor's downside is extended because they're holding the bond longer than anticipated.

This is called [negative convexity](/convexity/). The investor loses in both directions relative to what they planned. Mortgage-backed securities with high coupon rates (especially when yields have fallen below those coupons) carry extreme negative convexity.

## The role of refinancing incentives

Prepayment speed depends almost entirely on whether refinancing makes economic sense. If the current mortgage rate is 3% and market rates have dropped to 2%, homeowners rush to refinance (absent obstacles like poor credit or high closing costs). If rates have risen to 4%, few refinance.

Mortgage servicers track this quantitatively via the **Conditional Prepayment Rate (CPR)**—an annualized estimate of the percentage of remaining principal that will be prepaid in a given month. When rates fall below the mortgage coupon by a meaningful margin (typically 0.5% to 1%), the CPR can jump from 6% annually to 60% or higher. Market participants price mortgage-backed securities expecting a curve of CPR assumptions; if reality diverges sharply, investors face marked losses.

Complications include:
- Borrower inertia and refinancing friction (closing costs, appraisals, lock-in psychology).
- Demographic factors (elderly borrowers less likely to refinance; movers more likely).
- Regional variation in mortgage origination practices.

These factors create some stickiness in prepayment, but they do not eliminate the core risk.

## How investors manage prepayment risk

**Duration analysis:** Investors compute duration under multiple prepayment scenarios. If base-case CPR is 20% annually but could reach 60%, they model option-adjusted duration to see how the bond behaves in each state. This informs whether the yield is sufficient compensation.

**Hedging:** Investors use [interest-rate-swap](/interest-rate-swap/) or buy swaptions (options on swaps) to offset prepayment risk. Some use [Treasury-bill](/treasury-bill/) futures or bond futures to short duration if they fear a yield decline will trigger runaway prepayments.

**Diversification:** A portfolio of mortgage-backed securities from different regions, vintages (origination years), and coupon rates will have heterogeneous prepayment profiles. Some may experience fast prepayments while others extend, partially offsetting losses.

**Callable bond substitutes:** Some investors avoid mortgage-backed securities entirely and buy other assets with different risk profiles—equities, corporate [bond](/bond/) pools, or [real-estate-investment-trust](/real-estate-investment-trust/) for yield exposure without embedded prepayment options.

**Ladder and bucketing:** Segmenting a mortgage-backed portfolio by WAM (weighted average maturity) or timing cohorts allows managers to control the timing of cash inflows and reduce reinvestment risk on large lumpy prepayments.

## The cost of prepayment risk in pricing

Mortgage-backed securities trade at a [yield-to-maturity](/yield-to-maturity/) that is lower than an equivalent-duration Treasury or investment-grade [corporate-bond](/corporate-bond/) of the same stated maturity. Much of that spread reflects compensation for prepayment risk. High-coupon MBS (trading at a premium above par value) command even tighter valuations because their negative convexity is most severe.

A mortgage-backed security issued at par with a 3% coupon, held by an investor who bought it at par, is unlikely to deliver a true 3% return if rates fall by 200 basis points—the bulk of principal will return early, forced into 1% reinvestment. The market prices this mathematically via option-adjusted spread (OAS), which assumes a path of future prepayments and discounts cash flows accordingly.

## See also

<div class="wiki-seealso">

### Closely related

- [Mortgage-backed-security](/mortgage-backed-security/) — pooled residential mortgages and cash-flow mechanics
- [Callable-bond](/callable-bond/) — similar embedded optionality in corporate bonds
- [Reinvestment-risk](/reinvestment-risk/) — cost of deploying returned capital at lower yields
- [Duration](/duration/) — how bond price sensitivity changes with prepayment speed
- [Negative convexity](/negative-convexity/) — asymmetric price response to rate moves
- [Interest-rate-risk](/interest-rate-risk/) — broader interest-rate exposure
- [Option-adjusted-spread](/option-adjusted-spread/) — pricing that accounts for embedded options

### Wider context

- [Yield-to-maturity](/yield-to-maturity/) — stated return and reinvestment assumptions
- [Federal-reserve](/federal-reserve/) — controls short rates, influences mortgage refinancing
- [Real-interest-rate](/real-interest-rate/) — economic environment driving refinancing cycles
- [Bond](/bond/) — core instrument mechanics and risk taxonomy

</div>
