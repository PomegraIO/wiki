---
title: "Negative Convexity in Mortgage-Backed Securities"
description: "Why mortgage-backed securities exhibit negative convexity as rates fall due to prepayment acceleration, creating asymmetric price behavior."
keywords:
  - negative convexity mortgage backed securities
  - mortgage prepayment risk
  - convexity mbs bond
  - interest rate risk mortgages
image: /svg/fixed-income.svg
---

*Mortgage-backed securities have **negative convexity**—an asymmetric price behavior where they rise less than conventional [bonds](/bond/) when rates fall (because borrowers prepay), but fall similarly when rates rise. This "heads the investor loses, tails the investor loses" dynamic arises from the embedded [call option](/call-option/) that homeowners have: the right to refinance and escape the bond whenever it suits them.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Negative Convexity in MBS — key facts</div>

<img src="/svg/fixed-income.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">When rates fall, prepayments surge, locking in the MBS holder's return; when rates rise, investors are stuck with a below-market coupon.</div>

|   |   |
|---|---|
| **What it is** | Price appreciation capped by prepayment risk; losses unrestricted |
| **Cause** | Embedded borrower refinancing option (call option on the bond) |
| **Upside scenario** | Rates fall → borrowers refinance → bondholder loses future coupons |
| **Downside scenario** | Rates rise → borrowers stay put → bondholder holds below-market security |
| **Price behavior** | Lower duration extension when rates rise, faster duration contraction when rates fall |
| **Contrast with plain bonds** | Plain vanilla bonds: convex price curve (accelerating gains, decelerating losses) |
| **Historical example** | 2003–2004 refinancing wave: MBS prices flat while plain bonds rallied sharply |

</aside>

## How convexity works in plain vanilla bonds

Before understanding MBS, recall how a standard [bond](/bond/) behaves as rates change. A bond's price is inversely related to yields: when yields fall, bond prices rise. The relationship is *convex*, meaning it curves upward. 

The first 100 basis points of yield decline produces a certain price gain—say, $5 per $100 of par. The *next* 100 basis points of decline produces an even larger gain, say $5.50, because the dollar value of the cashflows extends further into a lower-discount-rate future. This accelerating gain with larger moves is positive convexity. It is mathematically a second-order effect, but it is the defining feature of bond investing: you win big when rates crash.

Conversely, when rates rise 100 bps, the bond loses money—but loses *less* than the initial decline gained. A 100 bps rise might cause a $4.50 loss (smaller than the $5 gain from 100 bps down). This is still positive convexity—the price curve is convex, limiting losses.

## The embedded option in mortgages

A mortgage-backed security pools thousands of home loans. Each homeowner has an embedded option: the right to refinance and prepay the loan at par whenever convenient. Economically, each homeowner is *short a call option* on rates. The MBS investor, owning the pool of mortgages, is effectively *long those calls*—or more precisely, the investor has written call options on the security.

When rates fall 200 basis points, homeowners exercise their refinancing option. Instead of a bondholder enjoying a 20-point price gain (as a plain bond would), the mortgages pay off at par, and the bondholder receives cash back at par, not the appreciated price. The MBS investor then faces reinvestment risk: the cash must be reinvested at the new, lower rates, cutting expected forward returns.

In the most extreme case, a homeowner who locked in a 4% mortgage when rates were 5% will immediately refinance when rates drop to 3%, prepaying the bond and ending the investor's income stream abruptly. The MBS investor misses the future coupons, which were attractive relative to new 3% market rates.

## Negative convexity in action: asymmetric price response

**Scenario 1: Rates fall by 200 basis points**

- Plain vanilla 5-year bond yielding 4%: Price appreciates by ~18–22 points (positive convexity means more gain).
- MBS with 4% coupon: Borrowers refinance in droves. The MBS does not appreciate much beyond ~10 points, because the mortgages prepay and the investor gets par back. The bondholder is locked in and cannot capture the full rate-decline windfall. This is the negative convexity "cap."

**Scenario 2: Rates rise by 200 basis points**

- Plain vanilla 5-year bond: Price depreciates by ~16–20 points (positive convexity means less loss).
- MBS with 4% coupon: Borrowers stay put (it is not rational to refinance into a 6% market). The MBS declines by ~18–22 points, nearly as much as the plain bond, but without the convexity cushion. The bondholder is stuck holding a below-market coupon security. The negative convexity is *symmetric downside*.

**Result:** The MBS can lose as much as a plain bond in a rising-rate scenario, but gain *less* than a plain bond in a falling-rate scenario. Investors call this "negative convexity"—the price curve is *concave* rather than convex.

## Why this is a form of call risk

From a financial engineering perspective, the MBS holder has sold a call option to the mortgagors. When rates fall, the option is in-the-money, and the mortgagors exercise (prepay). The MBS investor receives the strike price (par), not the appreciated market value of the bond.

The option has no stated premium: mortgagors get it for free as part of the mortgage contract. Economically, this free option is reflected in the mortgage interest rate—mortgagees pay slightly less for a mortgage than for an equivalent Treasury because the lender has granted them a prepayment option.

From the MBS investor's perspective, negative convexity is the cost of owning mortgages. It is not a flaw; it is an inherent feature.

## Duration instability and effective duration

Conventional bonds have stable [duration](/duration/)—a measure of interest-rate sensitivity. A 5-year bond's duration changes slowly as rates move. MBS duration, by contrast, is *option-adjusted*. It shrinks as rates fall (because prepayment risk rises and the mortgage-backed security shortens), and it lengthens as rates rise (because prepayments dry up and the mortgagees are stuck).

This is called *negative duration convexity*. When an investor is hedging an MBS position with Treasury futures, the hedge ratio must change dynamically as rates move. A 1% rate decline that was supposed to flatten in a hedge suddenly causes faster prepayments, reducing the MBS duration and making the hedge ratio wrong. This forces constant rebalancing, a costly drag in volatile markets.

## Historical context: the 2003–2004 refinancing wave

In 2003–2004, as mortgage rates dropped from 6% to 4%, a massive refinancing wave swept the MBS market. Homeowners from coast to coast refinanced, prepaying mortgages en masse. MBS yields remained stuck around 4–4.5% (the coupon), even as Treasury rates fell to 3.5%. The spread, or [option-adjusted spread](/credit-spread/) (OAS), widened dramatically—the market was compensating investors for negative convexity risk.

A plain vanilla corporate bond maturing in 5 years would have appreciated significantly during this period. An MBS investor found their position was crushed by prepayments, losing the higher coupon stream to reinvestment at depressed rates. This episode made negative convexity viscerally real to fixed-income managers.

## Measuring and pricing negative convexity

The [option-adjusted spread](/credit-spread/) (OAS) is the standard tool to account for negative convexity. Instead of a simple [yield-to-maturity](/yield-to-maturity/), an MBS is priced using a probabilistic model of prepayment speeds (CPR, or conditional prepayment rate) across different interest-rate scenarios. The OAS reflects the yield premium needed to compensate for the embedded call option.

A typical MBS in normal conditions has an OAS of 75–150 basis points over Treasuries. In periods of high prepayment risk or market stress, the OAS widens to 200+ basis points, pricing in the deeper negative convexity exposure.

## Strategies to manage negative convexity

**1. Duration matching**
Investors pairing MBS with short-duration instruments (money-market funds, Treasury bills) can dampen interest-rate sensitivity. But this sacrifices yield and does not solve the asymmetry problem.

**2. Swaptions and cap/floor hedges**
A portfolio manager holding MBS can buy a [cap](/interest-rate-swap/) or swaption, which gains value if rates fall and prepayments accelerate. This hedge offsets the MBS losses from refinancing, but hedges cost money and reduce net yield.

**3. Duration management**
As rates move, managers adjust the duration and weighted-average-life assumption of their MBS. Rising rates → extend duration expectations. Falling rates → contract duration. Active rebalancing can improve returns, but it requires skill and costs transaction fees.

**4. Sector rotation**
Investors may shift MBS allocations toward TBAs (to-be-announced mortgage pass-throughs that are more liquid for dynamic hedging) or toward adjustable-rate MBS (ARMs), where prepayment is less of a concern because coupons reset with market rates.

## The investor's perspective: is MBS worth it?

Negative convexity is why MBS offer higher yields than comparable-duration Treasuries or even corporate [bonds](/corporate-bond/). The OAS compensates for the hidden call option granted to homeowners. Whether MBS is attractive depends on the investor's view of the macroeconomic environment:

- **In a declining-rate environment** (recession, monetary easing): MBS underperform because of prepayments. Better to hold plain bonds or Treasuries.
- **In a stable or rising-rate environment**: MBS outperform because prepayments stay low and the investor collects the above-Treasury yield.
- **In a high-volatility environment**: The option value swells, and the OAS typically widens, creating less appealing risk-adjusted returns.

Professional mortgage investors therefore treat MBS as a tactical allocation, rotating in and out of the sector based on rate forecasts and prepayment risk.

## See also

<div class="wiki-seealso">

### Closely related

- [Mortgage-Backed Security](/mortgage-backed-security/) — the full asset class
- [Call Option](/call-option/) — the embedded prepayment right
- [Convexity](/duration/) — the general concept (plain bonds have positive)
- [Duration](/duration/) — the primary interest-rate sensitivity measure
- [Option-Adjusted Spread](/credit-spread/) — pricing tool for embedded optionality

### Wider context

- [Interest Rate Risk](/interest-rate-risk/) — the macroeconomic driver
- [Prepayment Risk](/prepayment-risk/) — the specific risk in MBS
- [Bond](/bond/) — the base asset class
- [Securitization](/securitization/) — the broader framework
- [Yield Curve](/yield-curve/) — the market environment for rate expectations

</div>
