---
title: "FX Option Theta Decay: How Time Erodes Premium"
description: "How time decay accelerates in FX options, theta quotation per day, and implications for hedgers holding long option positions."
keywords:
  - fx option theta decay
  - currency option time decay
  - theta time decay options
  - option premium erosion
  - short-dated fx options
  - option greeks
  - currency hedging cost
---

*Time decay—or **theta**—is the daily loss in the value of a currency [option](/option/) as expiration approaches, assuming the exchange rate and [volatility](/historical-volatility/) remain unchanged. For buyers of [FX options](/option/), theta is a constant drag; a one-month call loses value every single day simply because one day of uncertainty has evaporated. Theta accelerates sharply in the final weeks, making short-dated options expensive to hold.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">FX Option Theta Decay — key facts</div>

<img src="/svg/forex.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">The rate at which option premium erodes per day as expiration nears.</div>

|   |   |
|---|---|
| **Definition** | Daily loss in option value, all else equal |
| **Unit of measure** | Premium per day, or per day per unit of underlying |
| **Sign for buyers** | Negative (bad): price falls each day |
| **Sign for sellers** | Positive (good): they pocket decay as price falls |
| **Acceleration pattern** | Minimal at inception; steep in final 7–14 days |
| **Dependency** | Drives [time-value](/time-value/) to zero at expiration |

</aside>

## What Is Theta in FX Options

Theta is one of the [Greeks](/option/)—a sensitivity measure of how an option's value changes with respect to time. Specifically, theta measures the change in option premium per day as expiration approaches, holding all other inputs constant (spot rate, volatility, [interest rates](/interest-rate/)).

An FX call option premium has two components: intrinsic value and time value. Intrinsic value is max(spot − strike, 0)—the immediate profit if the option were exercised. Time value is everything else: the probability that the option moves further in-the-money, plus the volatility of that movement over time.

As days pass, time value shrinks because there is less future. That shrinkage is theta. A one-month option has 30 days of time value; a one-day option has almost none. Theta quantifies the daily loss.

## How Theta Is Quoted and Used

Traders quote theta as a decimal representing the daily decline in option premium. For example, a EUR/USD call option might have a theta of −0.0015. This means that if spot and volatility don't move, the option loses 0.0015 USD per day per notional unit (often one contract = 100,000 units).

On a 10 million unit position, that's 0.0015 × 10,000,000 = 15,000 USD per day in premium loss. Over a month, before accounting for volatility or spot changes, you lose roughly 450,000 USD simply to time decay.

Theta is negative for option buyers (they lose) and positive for option sellers (they gain). A trader who sells short-dated calls collects premium upfront; as theta eats away at the option's value, the seller's unrealized profit grows—assuming no spot or volatility surprise.

## The Shape of Time Decay: Acceleration Near Expiration

Theta is not uniform across the life of the option. It is smallest when the option is far from expiration and far from the strike—say, a 6-month call on a deep out-of-the-money level. As expiration approaches and [volatility](/historical-volatility/) spreads remain wide, the time value decay accelerates.

The effect is especially sharp in the final 7–14 days. A 30-day at-the-money option might lose 1–2 cents daily. A 3-day at-the-money option might lose 5–10 cents daily. This acceleration is because the remaining time window is shrinking and each day represents a larger fraction of the option's remaining life.

This dynamic makes short-dated options extremely costly to hold through to expiration. A hedger who buys a 1-week put to protect against a currency crash faces enormous daily theta drain. If the crash doesn't happen, the put melts away in value each day.

## Theta and At-the-Money vs. Out-of-the-Money

Theta is largest (most negative for buyers) when the option is at-the-money and shortest-dated. An ATM call on 3 days to expiration bleeds value fastest. Out-of-the-money options have smaller time value and thus smaller absolute theta, but the proportional decay is steeper—a 1-cent option losing 0.5 cents daily is a 50% one-day loss.

In-the-money options carry [intrinsic value](/intrinsic-value/), which is not subject to theta. A call 2 cents in-the-money has at least 2 cents of value on expiration day. Only the time value above intrinsic value decays, so ITM options theta-decay more slowly in absolute terms but still lose their remaining time value completely by expiration.

## Theta and the Volatility Trade-Off

Theta and gamma (the sensitivity of delta to moves in spot) are negatives of each other—a trade-off built into option pricing. When you buy an option, you pay theta drag to get gamma: the convexity that lets you profit from large spot moves. Sell theta, and you get short gamma, meaning you lose on big moves.

A trader who shorts a GBP/USD put to collect theta is betting that sterling will not crash. If sterling drops 2%, the short put delta blows up, offsetting the theta collection. A sophisticated seller hedges gamma dynamically, rehedging as spot moves to remain market-neutral while pocketing time decay.

Hedgers are not neutral on spot. A US exporter buying EUR puts to protect revenue gives up theta (insurance cost) to own gamma. If the euro rallies, the put expires worthless, but the exporter has made money on the cash export. The put loss is the cost of certainty—a form of insurance premium, and theta is the daily insurance fee.

## Interest Rate Carry in FX Option Theta

FX options embeds [interest rate](/interest-rate/) differentials between the home and foreign currency. A USD call on EUR, for example, reflects the carry: USD rates minus EUR rates. If the forward curve is in [contango](/contango/) (forward FX trading at a higher level than spot), the option is slightly more expensive than in a [spot-forward](/spot-rate/) vacuum.

As expiration approaches and the forward converges to spot, that forward premium decays. Some of this decay is captured in theta. A EUR call for a USD-based trader includes a small interest-rate theta boost if EUR interest rates are below USD rates, because the forward is pinned at a premium to spot. The option seller captures that decay passively.

In emerging market pairs with high interest-rate spreads (e.g., USD/BRL), interest-rate carry in options is more pronounced. A 6-month BRL call might carry significant negative carry (high BRL rates mean the forward is lower), increasing theta decay for the buyer.

## Practical Implications for Hedgers

A corporate treasurer hedging foreign exchange exposure with options must account for theta drain. A one-year put protecting a large export is reasonable: theta is small, time decay is slow, and the protection horizon matches the cash exposure. A one-week put is expensive and inefficient; nearly all premium evaporates if the move doesn't happen immediately.

For ongoing hedges, rolling options (selling the near-term option, buying a further-out option) is a common strategy. The sale collects theta and helps offset the cost of the new purchase. A continuous roll trades away the optionality for a future period to pay a net cost closer to the [forward](/forward-contract/) price.

In the options market, theta is managed through:

- **Option rolls**: Selling near-term decay, buying new decay further out
- **Volatility arbitrage**: Hedgers selling short-dated high-volatility options and buying longer-dated cheap-volatility options
- **Delta hedging**: Dynamic rehedging that neutralizes spot sensitivity, leaving only theta and gamma to be managed

## Theta Across Market Conditions

When implied [volatility](/implied-volatility/) rises, theta increases (option values rise, so subsequent daily decay is from a higher level). When implied volatility falls, theta decreases—the option is already cheap, so the daily decay is smaller in absolute terms. A trader long gamma and short theta will lose on both axes if volatility collapses.

Central bank policy shifts, crisis events, and earnings announcements can spike volatility mid-week, changing theta calculations. An option sold before an event hopes to collect the premium decay; an option bought hopes the move will be large enough to overcome theta loss.

In tight range-bound trading with falling volatility, theta sellers flourish: every day the option decays, and spot moves stay small, so gamma losses are minimal. In trending or volatile periods, gamma buyers win; theta losses are offset by large profitable moves.

## See also

<div class="wiki-seealso">

### Closely related

- [Option](/option/) — Fundamentals of currency options and option pricing
- [Implied-volatility](/implied-volatility/) — Forward-looking volatility priced into options; changes interact with theta
- [Time-value](/time-value/) — The non-intrinsic portion of option premium that theta erodes
- [Interest-rate](/interest-rate/) — How carry differentials affect option value and theta
- [Spot-rate](/spot-rate/) — Current FX level; spot moves affect delta, not directly theta
- [Delta](/fx-option-theta-decay-explained/) — Rate of change of option value with respect to spot movement

### Wider context

- [Derivatives-hedging](/derivatives-hedging/) — Using options and forwards for currency risk management
- [Currency-risk](/currency-risk/) — Why firms hedge FX exposure and at what cost
- [Volatility-smile](/volatility-smile/) — How implied volatility varies across strikes; shapes theta profiles
- [Contango](/contango/) — Forward curve structure affecting carry in options
- [Forward-contract](/forward-contract/) — Alternative to options for locking in exchange rates

</div>
