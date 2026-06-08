---
title: "Quanto Option vs Standard Cross-Currency Option"
description: "Learn how a quanto option locks in an exchange rate while a standard cross-currency option exposes you to both underlying and currency moves."
keywords:
  - quanto option
  - cross-currency option
  - currency risk derivatives
  - FX option
  - option valuation currency
  - quanto structure
---

*A **quanto option** bakes an exchange rate into the contract, fixing the currency conversion and leaving the buyer exposed only to the underlying asset. A **standard cross-currency option** exposes the buyer to both the underlying and the exchange rate. The choice between them hinges on whether you want to isolate currency risk or trade both the asset and the currency together.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Quanto vs Cross-Currency — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives." />

<div class="wiki-infobox-caption">Quanto locks the exchange rate; standard cross-currency leaves it floating.</div>

|   |   |
|---|---|
| **Quanto option** | Exercise and payoff in one currency; FX rate fixed at initiation |
| **Cross-currency option** | Exercise in one currency; underlying in another; FX rate floats |
| **Currency risk** | Quanto: zero; Cross-currency: full exposure to FX moves |
| **Payoff formula** | Quanto: (underlying move) × fixed FX rate; Cross-currency: (underlying move) × spot FX rate |
| **Who uses** | Quanto: exporters/importers hedging asset, not currency; Cross-currency: traders betting on both |
| **Typical cost** | Quanto: may be cheaper (less risk); Cross-currency: reflects FX volatility too |
| **Common example** | Quanto: Japanese investor buying S&P 500 call in yen; Cross-currency: same investor leaving the yen/dollar rate open |

</aside>

## The core structure: quanto fixed, cross-currency floating

A **quanto option** (short for "quantity-adjusted option") is an exotic [derivative](/derivatives-hedging/) that separates the underlying asset from the currency of payoff. You buy a call on the S&P 500, but the payoff is in euros at a fixed EUR/USD rate set at inception. No matter how the euro moves against the dollar between now and expiration, your gain or loss is converted at that locked-in rate.

A **standard cross-currency option** is a simpler structure: you buy a call on the S&P 500, and the payoff is in euros, but it converts at the *spot* EUR/USD rate on the exercise date. If the euro weakens against the dollar, your euro payoff is worth fewer dollars. If it strengthens, you gain from both the stock rally and the currency move.

The key difference is *when* and *at what rate* the currency conversion happens. In a quanto, the rate is set day one. In a standard cross-currency, the rate is determined on exercise day.

## Payoff comparison: a concrete example

Imagine you are a European investor, and today the EUR/USD rate is 1.10 (1 euro = 1.10 dollars). You want exposure to a $100 stock. Assume the stock rallies to $110.

**Scenario 1: Quanto call on the stock, payoff in euros, fixed FX rate of 1.10**

Your call is in-the-money by $10. The payoff in euros is fixed: ($110 − $100 strike) × 1.10 FX rate = 11 euros, no matter what EUR/USD does next.

- If EUR/USD moves to 1.05 by exercise: you still get 11 euros.
- If EUR/USD moves to 1.15 by exercise: you still get 11 euros.

The currency move is *completely hedged out*.

**Scenario 2: Standard cross-currency call on the stock, payoff in euros, FX rate floating**

Your call payoff in dollars is $10. You convert this at the *spot* EUR/USD rate on exercise day.

- If EUR/USD is 1.05 at exercise: $10 ÷ 1.05 = 9.52 euros. You lose from the currency move.
- If EUR/USD is 1.15 at exercise: $10 ÷ 1.15 = 8.70 euros. You actually lose *more* because the euro is stronger (fewer euros per dollar).

Wait—that second case looks wrong. Let me recalculate. If EUR/USD moves from 1.10 to 1.15, the euro *weakened*, so $10 converts to fewer euros: $10 ÷ 1.15 ≈ 8.70 euros. If EUR/USD moves to 1.05, the euro *strengthened*, so $10 becomes more euros: $10 ÷ 1.05 ≈ 9.52 euros.

So in a standard cross-currency call, a euro *strengthening* helps you (more euros per dollar), and a euro *weakening* hurts you. You cannot separate the stock move from the currency move.

## Why quantos exist: isolating currency exposure

Corporations and institutional investors often need to hedge one specific risk—the asset—and not the currency. A European exporter selling to the U.S. might want to lock in the price of a commodity without betting on euro/dollar moves. A Japanese pension fund might want exposure to U.S. tech stocks without currency risk.

A quanto option solves this by pre-specifying the FX rate. The investor gets the upside or downside of the stock in the home currency, with no currency tail risk.

Conversely, a speculator who wants to bet on *both* the stock and the euro's strength would use a standard cross-currency option (or just buy dollars and stock separately).

## Pricing and volatility: why quantos are different

Quanto options are priced using multi-dimensional valuation models, like the [Black-Scholes model](/black-scholes-model/), but with extra terms. The key insight is that quanto options are cheaper than a simple cross-currency option *when* the underlying asset and exchange rate are uncorrelated or negatively correlated.

Here's the intuition: suppose U.S. stocks rally hard when the dollar is weak (a negative correlation). A European investor buying a standard cross-currency call gets two upside scenarios (stock up, euro strong) and two downside scenarios (stock down, euro weak). But the correlation between them is unfavorable: if the stock rally happens, the dollar strengthens, so the euro payoff is *less* valuable. This correlation drag makes the cross-currency option more expensive.

A quanto option avoids this problem: it locks the FX rate and prices only the stock move. If the stock rally is likely to coincide with a strong dollar, the quanto call is significantly cheaper than the cross-currency equivalent.

The valuation formula for a quanto call on an underlying with value S, in currency H (home), with a fixed FX rate of F, is approximately:

**Quanto call value ≈ Black-Scholes(S, strike, vol, r, T) × F**

where F is the fixed exchange rate. Additional terms account for the correlation between the underlying and FX moves, but the core principle is: lock the rate, price the stock move alone.

## When to use each structure

**Use a quanto option if:**

- You have a clear forecast for the *underlying asset* but want to hedge currency risk entirely
- You are a corporation with foreign earnings in a specific currency and want to isolate operational hedges
- You face recurring cash flows in one currency and don't want FX volatility to widen your P&L noise
- The correlation between the asset and your home currency is unfavorable (as in the U.S. stocks + EUR example)

**Use a standard cross-currency option if:**

- You want to bet on *both* the underlying and the currency
- You believe the correlation between the asset and FX is favorable (e.g., emerging-market stocks and the local currency tend to move together)
- You want maximum transparency: a standard option is simpler and easier to value
- You plan to hedge the FX separately using currency forwards or other [currency risk](/currency-risk/) tools

## Real-world use cases

A **Japanese pension fund** holding U.S. Treasury bonds might buy quanto calls on the S&P 500 in yen. If they wanted to increase U.S. equity exposure without gambling on the yen/dollar rate, a quanto structure lets them do that. The fixed FX rate means they get "pure" equity upside in their reporting currency.

A **Brazilian exporter** selling coffee to U.S. buyers might use quanto futures or options on coffee prices. By locking the reais/dollar rate, they isolate the commodity risk and ignore currency speculation.

An **options trader at a hedge fund** might notice that U.S. stocks and the euro are uncorrelated. They could buy a standard cross-currency call on the S&P 500 in euros (betting the stock goes up and the euro stays firm), selling a quanto call to monetize the fact that the quanto is cheaper due to unfavorable correlation. This is a relative-value trade.

## Execution and counterparty risk

Quanto options are typically traded over-the-counter (OTC) between financial institutions, not on exchanges. This means:

- No standardization (terms are customized)
- Wider bid-ask spreads
- Exposure to [counterparty risk](/counterparty-risk/) (the bank quoting you the option might fail)
- Better pricing if you have scale (a large corporation can negotiate)

Standard cross-currency options are also usually OTC, though some vanilla options on stocks and currencies trade on exchanges.

## The correlation angle: why it matters to pricing

The price gap between a quanto and a standard cross-currency option depends entirely on the correlation between the underlying asset and the exchange rate. If a U.S. stock and the euro/dollar rate are *highly positively correlated* (when stocks rally, the euro strengthens), then the standard cross-currency call is cheaper than the quanto, because the FX move is a tailwind. If they are *negatively correlated* (stocks rally, euro weakens), the quanto is cheaper.

This is why the choice of structure is not purely about hedging philosophy—it's also about getting the math right. A sophisticated hedger calculates the realized and implied correlation, then chooses the structure that minimizes cost while achieving the desired risk profile.

## See also

<div class="wiki-seealso">

### Closely related

- [Option](/option/) — The foundational derivative right to buy or sell at a set price
- [Call option](/call-option/) — The right to buy; used in both quanto and cross-currency structures
- [Currency risk](/currency-risk/) — FX volatility and how to hedge it
- [Currency volatility](/currency-volatility/) — FX moves affect cross-currency option pricing
- [Black-Scholes model](/black-scholes-model/) — The pricing framework, extended to multi-asset options

### Wider context

- [Derivatives hedging](/derivatives-hedging/) — Overview of using derivatives to manage risk
- [Counterparty risk](/counterparty-risk/) — Risk of OTC option counterparty failure
- [Spot rate](/spot-rate/) — The exchange rate on any given day; used in cross-currency option payoff
- [Forward contract](/forward-contract/) — A simpler way to lock in FX rates (used often alongside options)
- Correlation — Statistical relationship between two assets; critical to quanto pricing
- [Volatility smile](/volatility-smile/) — Option pricing adjustments for skew, relevant to multi-asset derivatives

</div>
