---
title: "Vega: The Options Greek That Measures Volatility Sensitivity"
description: "Vega quantifies how much an option's price changes when implied volatility shifts by one point, critical for managing volatility exposure."
keywords:
  - vega options greek
  - volatility sensitivity option pricing
  - options greeks vega
  - implied volatility option delta
image: /svg/derivatives.svg
---

*[Vega](/vega-options-greek-volatility-sensitivity/) measures the dollar change in an option's price for each one-point move in implied volatility. Unlike delta or theta, vega is not a true Greek letter in mathematics—it is a professional term for the option's sensitivity to shifts in market expectations of price swings. When volatility rises, both calls and puts become more valuable; when it falls, both lose value. Traders use vega to hedge or harvest volatility risk.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Vega — the volatility Greek</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives." />

<div class="wiki-infobox-caption">Vega quantifies exposure to changes in implied volatility across the option book.</div>

|   |   |
|---|---|
| **Definition** | Dollar change per 1% move in implied volatility |
| **Applies to** | Calls and puts equally (both long vega when buying) |
| **Sign in the Greek letter list** | Not a true Greek; derived from [option pricing models](/black-scholes-model/) |
| **Used by** | Volatility traders, market makers, risk managers |
| **Peak vega** | At-the-money options; vega declines as option moves ITM or OTM |
| **Inverse relationship** | Vega falls as expiration approaches (near-zero at expiration) |

</aside>

## Why Volatility Matters to Option Prices

An option's value depends on two things: how far the underlying asset is from the [strike price](/strike-price/), and how much the underlying is expected to move before expiration. Historical swings tell traders one story; market prices for other options and derivative contracts reveal what traders collectively expect. This expectation is *implied volatility*—the volatility number that, plugged into a theoretical pricing model, produces the market price you see.

When implied volatility is high, option prices swell because the market believes large price swings are likely, giving option buyers more upside. When volatility contracts, option prices fall. A trader holding a large position in call options benefits if volatility rises and loses if volatility falls, even if the underlying stock does not move. Vega quantifies that exposure.

## How Vega Is Calculated and Expressed

Vega is the first derivative of option price with respect to a one-percentage-point change in implied volatility. Professional traders usually express vega as a dollar value: a vega of 0.05 means the option price changes by approximately $0.05 for every 1% shift in implied volatility. If an underlying trades at $100 and a call option has a vega of 0.10, and implied volatility jumps from 20% to 21%, the call will gain roughly $0.10.

The [Black-Scholes model](/black-scholes-model/) and binomial models produce vega as one of the standard risk measures. Because vega is strictly a derivative—it relies on the structure of the pricing model—it is not observed directly from market data the way [historical volatility](/historical-volatility/) is. Instead, traders infer vega from the market prices of options using these models.

Vega is always positive for long options (buying calls or puts) and always negative for short options (selling calls or puts). A trader long vega wants volatility to rise; a trader short vega wants it to fall.

## Vega and Time to Expiration

One of the trickiest aspects of vega is its relationship to time. Vega *peaks* when an option is at the money, but it also declines as the option approaches expiration. This makes intuitive sense: if an option has one week left, implied volatility has little time to move the price. If an option has three months left, the same volatility number has longer to work, so price swings are larger and vega is higher.

This time decay in vega is separate from [theta](/time-decay-theta/), which measures the option price decay due to time passing alone (holding volatility fixed). A calendar spread—longing a far-dated option and shorting a near-dated one—captures the difference in vega decay and can be profitable if volatility persists.

## ATM Vega vs. In-the-Money and Out-of-the-Money

Vega is highest for at-the-money options and declines symmetrically as options move in or out of the money. Deep in-the-money or far out-of-the-money options have negligible vega because their prices are anchored to intrinsic value—a change in volatility does not shift them much.

This property makes vega-neutral hedging possible: a trader holding short vega can buy ATM options to offset it, but must use OTM options in much larger quantity to achieve the same vega hedge. The cost of hedging vega depends on the shape of the [volatility smile](/volatility-smile/), which shows that markets often price OTM options with higher implied volatility than ATM ones.

## Vega Risk in a Changing Market

Implied volatility does not stay constant. Earnings announcements, central bank decisions, geopolitical shocks, or shifts in broad market sentiment can move implied volatility sharply. A trader or desk holding a large vega exposure can suffer losses if volatility drops unexpectedly—even if the underlying asset price is stable.

This is why [volatility traders](/algorithmic-trading/) and market makers pay close attention to vega. They may run a "vega-neutral" book, buying and selling options so that changes in volatility cancel out across the portfolio. Others intentionally build short vega positions in the expectation that implied volatility will fall from elevated levels.

## Vega and Realized vs. Implied Volatility

A subtle but important distinction: vega measures sensitivity to *implied* volatility, not to actual (realized) price swings. An option with high vega can lose money if realized volatility stays low, even if implied volatility was high when you bought it. The difference between implied and realized is the [volatility trader's profit and loss](/algorithmic-trading/).

If a trader buys an option at 25% implied volatility and the underlying realizes only 15% volatility over the holding period, the option loses value even if the price of the underlying does not move far. Conversely, a trader who sells volatility (short vega) profits when realized volatility underperforms the implied level priced in.

## See also

<div class="wiki-seealso">

### Closely related

- [Delta](/delta/) — how much the option price moves with the underlying asset price
- [Gamma](/gamma/) — how much delta itself changes as the underlying moves
- [Theta](/time-decay-theta/) — time decay of the option value
- [Black-Scholes Model](/black-scholes-model/) — the framework used to calculate all Greeks
- [Implied Volatility](/implied-volatility/) — the volatility number implied by market option prices
- [Volatility Smile](/volatility-smile/) — the pattern that implied volatility varies across strikes

### Wider context

- [Option](/option/) — introduction to calls, puts, and option contracts
- [Derivatives Hedging](/derivatives-hedging/) — using options to manage portfolio risk
- [Algorithmic Trading](/algorithmic-trading/) — systematic approaches to volatility and options trading
- [Strike Price](/strike-price/) — how strike relates to option value and Greeks

</div>
