---
title: "Black-76 Model"
description: "Fischer Black's 1976 extension of Black-Scholes for pricing futures options and interest-rate derivatives."
keywords:
  - futures options
  - interest-rate caps
  - interest-rate floors
  - Black model
  - option pricing
image: "/svg/derivatives.svg"
---

*The **Black-76 model** (or Black model) is Fischer Black's 1976 generalization of [Black-Scholes-model](/black-scholes-model/) that prices options on [futures-contract](/futures-contract/) and interest-rate derivatives. Instead of assuming the underlying follows a geometric Brownian motion with constant drift, Black-76 treats the forward price (or futures price) as the underlying, allowing it to elegantly price caps, floors, and swaptions when interest rates move without an exogenous drift term.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Black-76 Model — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives pricing." />

<div class="wiki-infobox-caption">Black-Scholes adapted to futures and interest rates by replacing spot prices with forward prices.</div>

|   |   |
|---|---|
| **What it is** | An option pricing formula for [futures-contract](/futures-contract/) and interest-rate derivatives using forward prices |
| **Key insight** | Assumes forward price is martingale (driftless); prices options exactly like Black-Scholes, but with F instead of S |
| **Main use** | Pricing interest-rate [call-option](/call-option/) caps, [put-option](/put-option/) floors, swaptions, and Eurodollar options |
| **Also called** | Black model, Black's model |
| **Closed-form price** | Similar Black-Scholes formula, but with forward/futures price F, not spot stock price S |
| **Advantage over Black-Scholes** | No need to model [interest-rate](/interest-rate/) drift separately; forward rate already embeds discounting |

</aside>

## Why Black-Scholes fails for futures and interest rates

The [Black-Scholes-model](/black-scholes-model/) assumes a stock price S(t) that grows at a constant rate r (the risk-free rate) and has a volatility σ. This makes intuitive sense for equities: the stock's expected return equals the risk-free rate, plus a premium for risk.

But futures and interest rates behave differently:

1. **Futures prices have no drift.** A [futures-contract](/futures-contract/) on crude oil, for example, does not have an expected return equal to the risk-free rate. Instead, the futures price already reflects all forward-looking information about supply and demand. Under the risk-neutral measure, it behaves like a martingale—it has no drift at all.

2. **Interest rates can be negative.** Black-Scholes assumes the underlying price is always positive and follows a geometric Brownian motion, which ensures it never goes below zero. But nominal interest rates can (and have, in recent decades) turned negative in some economies. A lognormal distribution does not suit negative rates.

3. **Forward prices embed the discount rate.** When pricing an interest-rate cap (a call option on a future interest rate), the strike and underlying are usually expressed on a forward basis. The forward rate already accounts for time-discounting; there is no separate "expected drift" to add.

Black recognized these issues and reformulated the problem: instead of modeling the spot price with drift, model the forward or futures price as a pure martingale.

## The forward price as the underlying

In Black-76, the underlying variable is the **forward price** F(t, T), defined as the price you agree today to pay for delivery at future date T. Under the risk-neutral measure, F(t, T) is a martingale—its conditional expectation at any future date equals its current value.

Mathematically, the model assumes:

dF = σF dW

Here F is the forward price, σ is a constant volatility, and dW is a Brownian increment. Critically, there is no drift term (no μ dt). This reflects the fact that under the risk-neutral measure, the forward price is expected to neither rise nor fall on average.

This simple change has profound consequences: you can now apply nearly the same Black-Scholes machinery, but with F in place of S, and it works for any underlying whose forward price is a martingale.

## The closed-form formula

The Black-76 price for a [call-option](/call-option/) on a futures contract maturing at T, struck at K, expiring at time t, is:

C = e^(−r(T−t)) [F N(d₁) − K N(d₂)]

where F is the current futures price, r is the [interest-rate](/interest-rate/) (assumed constant), and:

d₁ = [ln(F/K) + (σ²/2)(T−t)] / [σ√(T−t)]
d₂ = d₁ − σ√(T−t)

N() is the cumulative normal distribution. The [put-option](/put-option/) formula follows by put-call parity.

Compare this to Black-Scholes: instead of S and a dividend yield adjustment, you use the forward price F and apply the discount factor e^(−r(T−t)) outside. The result is an exceptionally clean formula that traders memorized and coded into spreadsheets worldwide.

## Applications: caps, floors, and swaptions

Black-76 is the workhorse for interest-rate [option](/option/) pricing:

**Interest-rate caps.** A cap is a series of [call-option](/call-option/) on future short rates. Each caplet (the component option) has a payoff at reset time T₁ based on the rate from T₁ to T₂. Black-76 prices each caplet by treating the forward LIBOR rate (or, today, [SOFR](/sofr/)) as the underlying, and the cap strike as the option strike. The cap value is the sum of all caplet values.

**Interest-rate floors.** A floor is a series of put options on short rates. Each floorlet is priced as a [put-option](/put-option/) using Black-76, with the floor strike replacing the option strike.

**Swaptions.** A swaption is an option to enter an [interest-rate](/interest-rate/) swap at a future date. Black-76 treats the swap's forward annuity value (the present value of all swap cash flows) as the underlying, and the [strike-price](/strike-price/) is the fixed rate at which you have the right to enter the swap. A payer swaption (right to pay fixed, receive floating) is a call on the forward swap rate.

In each case, the key insight is the same: express the underlying (a forward rate, a forward swap rate) as a martingale, apply Black-76, and you get a closed form.

## Constant volatility and the smile

Like Black-Scholes, Black-76 assumes a single constant [volatility](/volatility-smile/) σ. In practice, interest-rate markets exhibit a [volatility smile](/volatility-smile/): near-the-money caps and floors trade at lower [implied volatility](/implied-volatility/) than far out-of-the-money contracts.

Traders respond by using a local volatility or smile-adjusted variant of Black-76 for precise pricing. But for risk management and rough pricing, the constant-volatility Black-76 formula remains standard. Quants also extend it using stochastic volatility models (e.g., SABR) to fit the smile while retaining the martingale structure of forward rates.

## Why Black-76 succeeded in practice

Black-76 succeeded because:

1. **Simplicity.** The closed-form formula is just as easy to implement as Black-Scholes. No numerical integration or Monte Carlo is required for vanilla caps and floors.

2. **Fit to market convention.** Interest-rate markets already quote forward rates. Black-76 uses the same quotes directly, with no adjustment.

3. **No need for a dividend yield.** Unlike [Black-Scholes-model](/black-scholes-model/), which requires a separate dividend yield for stocks, Black-76 needs only the forward price (which already accounts for cash-flow timing) and a [interest-rate](/interest-rate/).

4. **Martingale intuition.** Once you accept that a forward price should be a martingale, the formula is almost inevitable. It builds on the same no-arbitrage principles that underlie all derivatives pricing.

## Limitations and modern extensions

Black-76 assumes constant interest rates and constant volatility. Modern markets relax both:

- **Stochastic interest rates.** If rates themselves are random (as in the [Hull-White model](/hull-white-model/) or Libor Market Models), you need a multi-dimensional framework. Black-76 is a special case where rates are held constant.

- **Volatility smiles.** Real interest-rate markets show smile effects (out-of-the-money options trade richer). Local-volatility and stochastic-volatility extensions (SABR being the most popular) are now standard for swaption pricing.

- **Negative rates.** Black-76 can price below-zero strikes, but the lognormal assumption still forbids negative futures prices. In negative-rate environments, traders often switch to the [Bachelier-model](/bachelier-model/), which uses a normal distribution instead.

Despite these refinements, Black-76 remains the pedagogical starting point for interest-rate option pricing and is still used for rough risk calculations and quoting conventions.

## See also

<div class="wiki-seealso">

### Closely related

- [Black-Scholes-model](/black-scholes-model/) — The foundational option pricing model that Black-76 extends to futures and forward rates
- [Futures-contract](/futures-contract/) — The underlying derivative for which Black-76 prices options
- [Interest-rate](/interest-rate/) — The key variable in Black-76 pricing for caps, floors, and swaptions
- [Call-option](/call-option/) and [put-option](/put-option/) — The option types Black-76 prices
- [Bachelier-model](/bachelier-model/) — An alternative model using normal distributions, preferred for negative interest rates
- [Strike-price](/strike-price/) — The fixed rate or price in a Black-76 option contract
- [Volatility-smile](/volatility-smile/) — The empirical pattern (higher vol for OTM contracts) that Black-76 constant-volatility assumption does not capture

### Wider context

- [Option](/option/) — The fundamental derivative that Black-76 prices
- [Implied volatility](/implied-volatility/) — The input parameter to Black-76; market-implied from traded option prices
- [Interest-rate](/interest-rate/) derivatives — The broad class of instruments (caps, floors, swaptions) priced using Black-76
- [Forward-guidance](/forward-guidance/) — How central banks communicate expectations that affect forward rates
- [Yield-curve](/yield-curve/) — The schedule of forward interest rates that provide inputs to Black-76 pricing

</div>
