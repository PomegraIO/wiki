---
title: "Bermuda Option"
description: "A Bermuda option can be exercised on specific dates (not just at expiration), sitting between the flexibility of American options and the simplicity of European options."
keywords:
  - bermuda option
  - exercise dates
  - option style
  - hybrid option
  - derivative
image: "https://picsum.photos/seed/bermudan-option/900/600"
---

*A **Bermuda option** (also **Bermudan option**) is a [call option](/call-option) or [put option](/put-option) that can be exercised on a set of predefined dates, typically quarterly or semi-annually, rather than on any date like an [american-option](/american-option) or on a single date like a [european-option](/european-option). Bermuda options are common in interest-rate products and represent a middle ground between exercise flexibility and pricing simplicity.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Bermuda Option — key facts</div>

<img src="https://picsum.photos/seed/bermudan-option/900/600" alt="A calendar showing specific predetermined exercise dates" />

<div class="wiki-infobox-caption">Bermuda options allow exercise on specific scheduled dates.</div>

|   |   |
|---|---|
| **Exercise timing** | Predefined dates only |
| **Early exercise** | On scheduled dates only |
| **Pricing complexity** | Moderate (discrete decision points) |
| **Typical underlying** | Interest-rate swaps, bonds, callable bonds |
| **Price vs. American** | Lower (less flexibility) |
| **Price vs. European** | Higher (more flexibility) |
| **Exercise lattice** | Modified binomial tree |
| **Settlement** | Cash or physical |
| **Common frequency** | Quarterly, semi-annually |

</aside>

## A hybrid option style

The name "Bermuda option" is a playful reference to Bermuda's location between America and Europe. The option itself is a compromise: more flexible than a [european-option](/european-option) (which allows exercise only at expiration) but less flexible than an [american-option](/american-option) (which allows exercise any day).

In practice, the holder receives a schedule of exercise dates—for example, the 15th of each quarter for the next three years. The holder can exercise on any of those dates or wait for the next scheduled date. If the holder does not exercise by the final date, the option expires.

This structure is particularly useful for interest-rate [swap](/swap) products. A callable bond, for example, might give the issuer the right to redeem (call) the bond on the coupon dates—quarterly or semi-annually. That right is a Bermuda-style option embedded in the bond. Similarly, a swaption (an option to enter a [swap](/swap)) might be exercisable on a series of monthly dates rather than a single date.

## Pricing Bermuda options

Bermuda option pricing is more complex than [european-option](/european-option) pricing but simpler than [american-option](/american-option) pricing. Because exercise can happen on only a discrete set of dates, the binomial or trinomial tree approach works, but you only compute optimal exercise at those specified nodes, not at every node.

At each scheduled exercise date, the algorithm asks: is it optimal to exercise now, or is the option worth more if I hold and wait for the next opportunity? The decision is based on the current [intrinsic value](/intrinsic-value) (profit if exercised today) versus the value of waiting (the discounted [time value](/time-value) from now until the next exercise date).

The math is less tractable than [Black-Scholes model](/black-scholes-model) but avoids the full Monte Carlo complexity sometimes needed for [american-option](/american-option) pricing.

## When Bermuda options appear

Bermuda-style options are standard in interest-rate derivatives. A callable bond is issued with the right to be called on coupon dates. A swaption might allow the holder to enter a [swap](/swap) on the first Wednesday of each month for a year. Interest-rate floors and caps often come with Bermuda-style exercise schedules.

In equity markets, Bermuda options are less common, because [american-option](/american-option) contracts are standardized and highly liquid. But in bespoke or over-the-counter trades, Bermuda exercise can be negotiated to match the business need. For example, a company might want to hedge a quarterly cash flow by buying an option exercisable only on the days it receives the cash.

## Early exercise decisions

The Bermuda option holder's exercise decision is simpler than the [american-option](/american-option) holder's (only a few dates per year to consider) but more complex than the [european-option](/european-option) holder's (no decision at all until expiration). The optimal exercise rule is: if the option is sufficiently in-the-money on a scheduled date, exercise; otherwise, hold and wait for the next opportunity.

For interest-rate products, the "sufficiently in-the-money" threshold depends on interest-rate expectations. A swaption holder might exercise if rates have risen and the fixed leg of the swap has become attractive, or hold if rates are still falling and waiting promises more gain.

## Valuation intuition

A Bermuda option is worth less than an [american-option](/american-option) on the same underlying with the same strike, because there are fewer exercise opportunities. The fewer the exercise dates, the closer the Bermuda option's value approaches that of a [european-option](/european-option).

A Bermuda option is worth more than a [european-option](/european-option) with the same expiration, because at least one earlier exercise date typically offers some optionality.

The precise gap depends on the frequency of exercise dates, the underlying's volatility, and the time to expiration. High volatility widens the gap because the early exercise opportunities become more valuable.

## Callable bonds as embedded Bermuda options

A classic application is the callable bond. The bondholder owns a bond (long [bond](/bond)) but the issuer owns an embedded Bermuda option—the right to call (redeem) the bond on coupon dates.

From the issuer's perspective, they have the right to buy back the bond at par. If rates fall and the bond's market value rises above par, the issuer exercises the option (calls the bond) and refinances at lower rates. The bondholder loses the upside. This is why callable bonds offer higher [yield](/yield-curve) than non-callable bonds—the issuer owns an option that can hurt the bondholder.

## See also

<div class="wiki-seealso">

### Closely related

- [American option](/american-option/) — exercise anytime
- [European option](/european-option/) — exercise at expiration only
- [Call option](/call-option/) — right to buy
- [Put option](/put-option/) — right to sell
- [Expiration date](/expiration-date/) — the final exercise date
- [Strike price](/strike-price/) — the fixed exercise price
- [Swaption](/swaption/) — option on a swap

### Pricing & Greeks

- [Binomial option pricing](/binomial-option-pricing/) — valuation for discrete exercise dates
- [Options Greeks](/options-greeks/) — delta, gamma, theta, vega, rho
- [Implied volatility](/implied-volatility/) — affects option value
- [Time value](/time-value/) — value between now and next exercise date

### Deeper context

- [Option](/option/) — the family of derivatives
- [Swap](/swap/) — often the underlying
- [Interest rate swap](/interest-rate-swap/) — common swaption underlying
- [Bond](/bond/) — callable bonds embed Bermuda options

</div>
