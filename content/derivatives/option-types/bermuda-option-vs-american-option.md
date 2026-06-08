---
title: "Bermudan Option vs American Option"
description: "A Bermudan option allows exercise on a discrete set of dates, whereas an American option can be exercised any time before expiry—a difference reflected in both value and pricing."
keywords:
  - bermudan option
  - american option
  - early exercise
  - option valuation
  - exotic option
  - exercise dates
  - derivatives
---

*A **Bermudan option** sits between a European option (exercise-at-maturity only) and an American option (exercise anytime). It grants the right to exercise on a predetermined set of dates—quarterly resets, monthly checkpoints, or other agreed intervals—making it cheaper than an American option but more valuable than a European one.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Bermudan vs American — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives." />

<div class="wiki-infobox-caption">The middle ground: fixed early-exercise dates, not continuous choice.</div>

|   |   |
|---|---|
| **Exercise window** | American: any time before expiry; Bermudan: only on preset dates |
| **Number of dates** | Bermudan typically 4–12 exercise points; American: infinite |
| **Option value** | Bermudan > European; American ≥ Bermudan |
| **Premium** | American highest, Bermudan middle, European lowest |
| **Pricing method** | Bermudan requires tree or simulation at each exercise date |
| **Common uses** | Convertible bonds, interest-rate swaps, callable bonds, long-dated employee equity |
| **Holder advantage** | Bermudan provides flexibility at lower cost than full American optionality |

</aside>

## The three exercise regimes

**European option:** You can exercise *only* at maturity. This is the simplest and cheapest. [Call option](/call-option/) payoff is max(0, spot at expiry − strike).

**American option:** You can exercise *any* trading day up to and including expiry. This is the most flexible and most expensive. An American call on a non-dividend-paying stock is worth at least as much as the European version because you have more choices.

**Bermudan option:** You can exercise *only* on a preset schedule—say, the first business day of each month, or the quarterly reset dates of an [underlying index](/index-fund/). The schedule is written into the contract and is non-negotiable.

A Bermudan option gives the holder more optionality than a European option (you can exercise early) but less than an American option (you can't exercise on *every* trading day). Its price falls between the two.

## When Bermudan exercise dates matter

### Callable bonds and convertible securities

A [corporate bond](/corporate-bond/) issued as convertible—swappable into shares at the issuer's discretion—is often structured with Bermudan calls. The issuer might be able to call the bond on the 1st of January, April, July, and October each year, not on arbitrary dates.

If you own the convertible bond as a holder, you face the risk that the issuer will call it on a scheduled date when it's advantageous to the issuer (shares are deep in-the-money, interest rates have fallen). The restriction to specific dates reduces the issuer's advantage slightly, making the bond worth more to you.

### Interest-rate swaps

A [swap](/swap/) allowing early termination on quarterly reset dates is a Bermudan swaption. The holder can unwind the position on March 31, June 30, September 30, or December 31—but not on May 15. This fits the cash-flow calendars of most corporations and funds, while keeping the product cheaper than a full American swaption.

### Employee equity grants

A company granting vesting shares or [employee stock options](/option/) often ties exercise windows to quarterly earnings releases or annual review cycles. A Bermudan structure lets employees exercise on those dates only, aligning the timing with their information flow and reducing administrative load.

## Pricing the Bermudan advantage

Imagine a European call with a strike of $50 on a stock trading at $52:

- **European:** priced with [Black-Scholes](/black-scholes-model/) or a similar model; let's say $2.50.
- **Bermudan** (exercisable quarterly, say): $3.00–$3.50, depending on [volatility](/historical-volatility/), [time to expiry](/expiration-date/), and how far the stock is in-the-money.
- **American:** $3.50–$4.00 or higher, depending on how likely early exercise is.

The Bermudan premium over European reflects the value of having *some* early-exercise dates. The American premium over Bermudan reflects the value of *all* possible early-exercise dates.

If volatility is very high, the American option's extra flexibility is worth a lot (you can bail out on a spike). If volatility is low and the option is deep in-the-money, the three exercise points per year might capture most of the value anyway, so the Bermudan and American prices converge.

## The binomial tree approach to Bermudan valuation

European options are closed-form ([Black-Scholes](/black-scholes-model/)). American options require numerical methods like **binomial trees** or **trinomial trees** because at each node, the holder must decide whether to exercise or continue.

A Bermudan option simplifies this: you build a tree, but you only allow exercise decisions at the preset dates. Between exercise dates, you simply propagate values forward without the early-exercise check. This reduces computational load compared to an American option while maintaining the path-dependent logic.

**Example tree logic (quarterly Bermudan call, 1-year horizon):**

1. Build a binomial tree with daily steps.
2. At day 90 (quarter 1 exercise date): for each node, compute max(value if you hold, payoff if you exercise now).
3. Between day 90 and day 180: propagate without exercise choice; just update probabilities.
4. At day 180 (quarter 2): check exercise condition again.
5. Repeat through day 365.

The result is a price that properly accounts for optionality on the allowed dates.

## Practical differences in markets

### Liquidity and trading

American options on stocks are highly liquid—you can buy and sell S&P 500 calls at tight spreads. Bermudan options are bespoke, usually negotiated in OTC markets for [swaps](/swap/), [convertible bonds](/convertible-bond/), or large structured products. Trading them is harder and costlier.

### Reset and adjustment mechanics

Bermudan exercise dates often align with **reset dates** in structured products. For example, a [mortgage-backed security](/mortgage-backed-security/) might reset its [coupon rate](/coupon-rate/) quarterly. The Bermudan feature lets an investor or issuer react to new market conditions on those reset dates, not on arbitrary dates.

### Regulatory and tax treatment

In some jurisdictions, Bermudan optionality receives different [accounting treatment](/asc-606/) than American optionality. If you're hedging an accounting liability, the discrete exercise dates might align with your reporting calendar, simplifying disclosures.

## Real-world example: convertible bond

A tech company issues a $1,000 convertible bond:
- 5-year maturity.
- [Coupon](/coupon-payment/): 2%.
- Conversion price: $80 per share.
- **Call feature:** Bermudan, exercisable on the first business day of each quarter, starting Q2 of year 1.

If shares rally to $120 by Q1 of year 2, the company can call the bond on the next quarterly date (say, April 1). The bondholder then has the choice to convert into shares or accept a cash payment. The restriction to quarterly dates gives the bondholder a reprieve: if shares spike in February, the issuer can't call until April, allowing time to lock in gains or roll into a new position.

Had the call been American (exercisable any day), the issuer could call immediately after the spike, forcing conversion at the worst time from the holder's perspective. The Bermudan structure is worth something to the bondholder—reflected in a higher [bond price](/bond/) or lower [coupon](/coupon-rate/) than a fully American convertible.

## Bermudan swaptions in interest-rate markets

A 5-year [swap](/swap/) with a Bermudan swaption (right to unwind) exercisable on 20 quarterly reset dates is a common instrument in [fixed-income](/bond/) portfolios. The holder can:
- Exit if [interest rate](/interest-rate/) markets move sharply (e.g., [Fed](/federal-reserve/) rate hike triggers).
- Refinance at better rates if [credit spreads](/credit-spread/) tighten.
- Restructure a mismatched portfolio on a known schedule.

A full American swaption would give this flexibility on *any* day, but it's much more expensive and rarely offered. The Bermudan strike (pun intended) the balance: meaningful optionality at reasonable cost.

## See also

<div class="wiki-seealso">

### Closely related

- [Option](/option/) — foundational payoff and mechanics
- [Call option](/call-option/) — upside bet structure
- [Put option](/put-option/) — downside protection structure
- [Strike price](/strike-price/) — the exercise level
- [Expiration date](/expiration-date/) — option life and settlement timing
- [Black-Scholes model](/black-scholes-model/) — theory for European options

### Wider context

- [Derivatives hedging](/derivatives-hedging/) — why optionality matters
- [Convertible bond](/convertible-bond/) — where Bermudan calls are common
- [Swap](/swap/) — interest-rate and currency swaps with embedded optionality
- [Early exercise](/in-the-money/) — the strategic decision to exit before expiry

</div>
