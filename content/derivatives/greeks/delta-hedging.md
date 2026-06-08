---
title: "Delta Hedging"
description: "The practice of continuously rebalancing an offsetting position to neutralize directional risk in an option."
keywords:
  - delta hedging
  - option hedging
  - rebalancing
  - directional exposure
  - greeks
image: "/svg/derivatives.svg"
---

*A **delta hedge** is a rebalancing strategy in which a trader offsets the directional exposure of an option (or options book) by trading the underlying asset—buying when delta is negative, selling when positive—to maintain a neutral net delta. Since delta itself changes as the underlying price moves, hedging requires continuous adjustment and is more of a trading process than a set-it-and-forget-it insurance policy.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Delta Hedging — rebalancing for neutrality</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives and hedging." />

<div class="wiki-infobox-caption">The core tool for managing short-volatility exposure.</div>

|   |   |
|---|---|
| **What it is** | Adjusting underlying holdings to offset an option's [delta](/delta/) exposure |
| **Also called** | Delta-neutral rebalancing, dynamic hedging |
| **Key frequency** | Continuous or periodic, depending on market moves |
| **Primary user** | Options market makers and volatility traders |
| **Friction cost** | Bid-ask spreads, slippage, commissions—compounds with rebalancing frequency |

</aside>

## Why delta matters for hedging

An option's [delta](/delta/) measures the expected change in its value per unit move in the underlying asset. A call option with delta 0.6 should gain approximately £0.60 if the stock rises £1. A trader long that call is exposed to the stock's upside; if the stock crashes 10%, the long call loses money (mitigated somewhat by [theta](/theta/), depending on time decay and [volatility](/historical-volatility/)).

The simplest hedge: sell 60 shares. Now, if the stock moves up £1, the long call gains £0.60 while the short stock position loses £0.60—net result, zero (ignoring costs). The position is **delta-neutral**. But as soon as the stock price moves, delta changes. A call's delta rises above 0.6 if the stock rallies, meaning the hedge is no longer balanced. The trader must rebalance: sell more stock, or buy some back.

This continuous adjustment is delta hedging.

## The mechanics of rebalancing

In practice, delta hedging happens on a schedule set by the trader. Options market makers might rehedge their books multiple times per day if volatility is high and positions are large. A large pension fund or insurance company might rehedge daily or weekly. The decision hinges on portfolio size, transaction costs, and acceptable slippage.

At each rebalancing point, the trader calculates the total delta of all option positions. Suppose a book is long 100 call options, each with delta 0.5—total delta is 50. To hedge, the trader short-sells 50 shares. If the underlying rises and the 100 calls' delta shifts to 0.55 each (total 55), the trader must short an additional 5 shares to maintain neutrality. If the underlying falls and delta drops to 0.45 per call (total 45), the trader buys back 5 shares.

Each rebalancing trade incurs a [bid-ask spread](/bid-ask-spread/), potentially slippage, and commissions. Over a week with five rehedges, those costs add up. This is why delta hedging is often called a "cost of being short volatility"—the trader pays the spread multiple times over, funding the hedge passively.

## The Greeks and delta hedging

Delta hedging is incomplete. Selling shares to offset [delta](/delta/) eliminates directional risk, but it does nothing for [gamma](/gamma/). Gamma measures how quickly delta changes; a short gamma position loses money to large price swings (both up and down) because the hedge becomes increasingly stale. A short-gamma trader must rehedge more frequently as volatility rises, paying more spreads.

[Vega](/vega/) measures sensitivity to [volatility](/historical-volatility/) itself. If the trader is short vega (sold an option), higher [implied volatility](/implied-volatility/) erodes the position's value regardless of underlying price. Delta hedging does nothing to offset this.

[Theta](/theta/), time decay, often works in favour of the delta hedger. A short-option position typically has positive theta, meaning it profits as the option expires—a natural offset to the cost of rebalancing.

In practice, a trader manages all four Greeks together. Delta hedging is the foundation, but monitoring gamma, vega, and theta determines profitability over time.

## When delta hedging fails

Delta hedging assumes you can trade the underlying instantly at a known price. On liquid stocks and index futures, this is mostly true. On thinly traded assets—some commodities, [corporate bonds](/corporate-bond/), or exotic [currencies](/currency-risk/)—liquidity evaporates when you need it, and large positions move the market.

Hedging also breaks down during gaps and limit moves. If a stock gaps down 20% overnight, no amount of delta hedging overnight prevented the loss (though the option's delta would have adjusted as the market opened). In the 2020 volatility spike, many delta hedging strategies failed because [realized volatility](/historical-volatility/) exploded beyond the strikes traders were hedging for.

## The paradox of profitability

A perfect delta hedge should make zero. You neutralize directional risk, pocket theta, and pay spreads—a slow bleed. Only if you forecast volatility better than the market prices it into the option do you profit. If you're long gamma (long a [put](/put-option/) or [call](/call-option/)), you profit when the stock moves more than the [implied volatility](/implied-volatility/) assumed—delta hedging harvests that edge by rebalancing into strength and out of weakness.

Conversely, a [short volatility](/implied-volatility/) trader (seller of options) uses delta hedging as a cost of doing business. The goal is to collect the [option premium](/option-premium/) in excess of the cost of hedging and [realized volatility](/historical-volatility/) (or, rather, the difference between [implied](/implied-volatility/) and realized). Delta hedging turns an options book into a tidy, scaled bet on volatility mismatch rather than a directional bet.

## See also

<div class="wiki-seealso">

### Closely related

- [Delta](/delta/) — the option greek measuring price sensitivity to the underlying
- [Gamma](/gamma/) — the rate of change of delta; controls hedging frequency and scalp profits
- [Gamma Scalping](/gamma-scalping/) — profiting from realized volatility by delta-hedging a long-gamma position
- Greeks — the four sensitivity measures that drive option trading
- [Vega](/vega/) — exposure to changes in implied volatility
- [Theta](/theta/) — time decay; often positive for delta hedgers
- [Implied Volatility](/implied-volatility/) — the volatility priced into an option; the hedge's risk target

### Wider context

- [Option](/option/) — the derivative contract being hedged
- [Hedge Fund](/hedge-fund/) — professional managers who use delta hedging at scale
- [Volatility Smile](/volatility-smile/) — non-linear pricing that complicates delta hedging
- [Black-Scholes Model](/black-scholes-model/) — the framework that defines delta and other greeks

</div>
