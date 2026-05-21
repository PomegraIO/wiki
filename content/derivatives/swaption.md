---
title: "Swaption"
description: "A swaption is an option to enter a swap contract at a future date, allowing the holder to lock in swap terms conditionally."
keywords:
  - swaption
  - swap option
  - interest rate
  - option on swap
  - derivatives
image: "https://picsum.photos/seed/swaption/900/600"
---

*A **swaption** is an [option](/option) contract giving the holder the right—but not obligation—to enter a [swap](/swap) (usually an [interest-rate-swap](/interest-rate-swap)) at a predetermined rate on a future date. Swaptions are used by corporates and bond investors to obtain optional interest-rate protection: if rates move unfavorably, the holder exercises and locks in the predetermined rate; if rates move favorably, the holder lets the option expire. A swaption has an [option premium](/option-premium) upfront and the [strike](/strike-price) is the fixed swap rate.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Swaption — key facts</div>

<img src="https://picsum.photos/seed/swaption/900/600" alt="Right to enter swap at predetermined rate" />

<div class="wiki-infobox-caption">Swaption: optional interest-rate hedge.</div>

|   |   |
|---|---|
| **Type** | Payer swaption (exercise to pay fixed) or receiver (receive fixed) |
| **Underlying** | Interest-rate swap |
| **Exercise type** | Often European (exercise date only) |
| **Strike** | Fixed swap rate |
| **Premium** | Paid upfront |
| **Exercise decision** | Compare strike to market swap rate at exercise date |
| **Contingent protection** | Only pay premium if exercised; flexible |
| **Typical use** | Corporates with uncertain liabilities |
| **Pricing** | Black model or Monte Carlo |
| **Liquid** | Major tenors (5-into-5, 10-into-10) |

</aside>

## How swaptions work

A company expects to refinance debt in 6 months but is unsure if it will need the funds. It buys a 6-month **payer swaption** (right to pay fixed) on a 5-year [interest-rate-swap](/interest-rate-swap):

- Strike: 4% fixed
- Premium: 0.5% of notional ($50K on $10M)

**Scenario 1 (rates rise to 5%):** In 6 months, the company exercises the swaption, entering the swap to pay 4% (now cheaper than market 5%). The company has locked in favorable terms. Cost: premium paid ($50K) plus 4% on debt (1% cheaper than market 5%).

**Scenario 2 (rates fall to 3%):** In 6 months, the company does not exercise (market rate 3% is better than strike 4%). It can refinance at 3% directly. Cost: premium paid ($50K).

The option premium is the price of flexibility.

## Payer vs. receiver swaptions

**Payer swaption:** Right to pay fixed (receive floating). Bought by those expecting rates to rise; protects them from rising fixed rates.

**Receiver swaption:** Right to receive fixed (pay floating). Bought by those expecting rates to fall; protects them from falling fixed rates.

## Valuation

Swaptions are priced using the **Black model** (extension of [Black-Scholes model](/black-scholes-model)) applied to forward swap rates:

Swaption price = Bond PV × Black(forward rate, strike, volatility, time)

Inputs:
- **Bond PV:** Present value of the annuity of swap payments
- **Forward rate:** Swap rate implied by the yield curve
- **Strike:** Exercise rate (the locked-in swaption rate)
- **Volatility:** [Implied volatility](/implied-volatility) of swap rates
- **Time:** Time to exercise date

## Greeks

Swaptions have [vega](/vega) (sensitivity to interest-rate [volatility](/historical-volatility)), [delta](/delta) (sensitivity to rate level changes), and [theta](/theta) (time decay like other options).

[Vega](/vega) is high when the swaption is at-the-money (strike equals forward rate); [delta](/delta) changes as rates move.

## Contingent protection and cost savings

A key advantage is **contingency**: you pay a premium only if you use the option. This is cheaper than buying a swap outright (which costs nothing upfront but commits you).

For uncertain needs (pending M&A, conditional refinancing), swaptions offer cost-effective protection.

## See also

<div class="wiki-seealso">

### Closely related

- [Swap](/swap/) — underlying instrument
- [Interest rate swap](/interest-rate-swap/) — typical underlying
- [Option](/option/) — the outer layer
- [Strike price](/strike-price/) — the locked-in swap rate
- [Option premium](/option-premium/) — upfront cost

### Valuation and pricing

- [Black model](/black-scholes-model/) — swaption pricing standard
- [Implied volatility](/implied-volatility/) — of swap rates
- [Options Greeks](/options-greeks/) — delta, vega, theta
- [Forward rates](/forward-contract/) — determine swaption value

### Uses and strategies

- [Hedging](/hedge-fund/) — conditional interest-rate protection
- [Interest-rate risk](/interest-rate/) — what swaptions manage
- [Refinancing](/bond/) — timing of debt decisions
- [Callable bonds](/bond/) — embedded swaptions

### Deeper context

- [Derivative](/option/) — the family of instruments
- [Interest rates](/interest-rate/) — underlying market
- [Fixed income](/bond/) — swaptions dominate here

</div>
