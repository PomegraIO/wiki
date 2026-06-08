---
title: "Gamma Scalping"
description: "A trading strategy that harvests profits from realized volatility by repeatedly delta-hedging a long-gamma position."
keywords:
  - gamma scalping
  - gamma trading
  - realized volatility
  - delta hedging
  - options strategy
image: "/svg/derivatives.svg"
---

*A **gamma scalper** is a trader or market maker who profits from the difference between [realized volatility](/historical-volatility/) and [implied volatility](/implied-volatility/) by holding a long-[gamma](/gamma/) position (typically long calls or puts) and [delta-hedging](/delta-hedging/) it repeatedly as the underlying price moves. Each rebalancing locks in a small profit if the market moved more than the option's pricing assumed—a process known as "rebalancing into movement."*

<div class="wiki-hatnote">

For the broader relationship between gamma and hedging costs, see [Delta Hedging](/delta-hedging/).

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Gamma Scalping — harvesting realized volatility</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives and trading." />

<div class="wiki-infobox-caption">A market-neutral bet on realized exceeding implied volatility.</div>

|   |   |
|---|---|
| **What it is** | Buying options and rehedging [delta](/delta/) to profit from volatility realizations |
| **Also called** | Gamma trading, volatility harvesting, gamma bleed |
| **Profit source** | [Realized volatility](/historical-volatility/) minus [implied volatility](/implied-volatility/) |
| **Primary cost** | Bid-ask spreads and commissions from frequent rehedging |
| **Key risk** | Directional moves larger than a single rehedge interval can capture |

</aside>

## The core mechanism

Imagine you buy a call option struck at-the-money. The underlying trades at £100, [implied volatility](/implied-volatility/) is 20%, and the option costs £5. You immediately [delta-hedge](/delta-hedging/) by selling 50 shares (assuming [delta](/delta/) is roughly 0.5).

Your position is now:
- Long 1 call (cost £5, delta +0.5)
- Short 50 shares (proceeds £5,000)
- Net delta: zero

The stock bounces to £101. Your call's [delta](/delta/) is now 0.52, so you're long 0.02 shares' worth of delta. You hedge by selling 0.02 shares for £2.02. Profit: £0.02. Later, the stock falls to £99.50. Your call's [delta](/delta/) drops to 0.48; you now have short 0.02 delta. You buy back £1.99 worth of shares. You lock in another small profit.

Over time, if the stock moves enough and you rehedge enough times, these tiny profits accumulate. They come from the gap between the [realized volatility](/historical-volatility/) (actual swings) and the [implied volatility](/implied-volatility/) (what the option priced in). If the stock swings widely, you rehedge many times and collect many small profits. If it sits flat, you accumulate almost nothing but lose the £5 premium over time to [theta](/theta/).

## Why it's called scalping

Each rehedge is a "scalp"—a tiny profitable trade executed dozens or hundreds of times. The trader is indifferent to direction: up or down, if the stock moves, gamma scalping works. The bet is purely on the *size* of moves, not their direction.

This is the inverse of being short an option. A short-[call](/call-option/) seller suffers from large movements in either direction (high [realized volatility](/historical-volatility/)) and profits from stillness (low [realized volatility](/historical-volatility/)). A gamma scalper flips this: they profit from jumps and volatility spikes.

## The math of rehedging frequency

Profit per rehedge cycle is proportional to [gamma](/gamma/) × (price move)² ÷ 2. [Gamma](/gamma/) is highest for at-the-money options and decays away from the strike. A small [gamma](/gamma/) position needs large moves to accumulate profit; a large [gamma](/gamma/) position profits from small, frequent moves.

Rehedging frequency amplifies these profits—but only if the option is mispriced. If you buy an option at exactly fair [implied volatility](/implied-volatility/), your expected profit from gamma scalping is zero after costs. It's only the difference between what the market implied and what actually occurred that pays. This is why gamma scalping is really a bet on volatility forecasting: you're long realized, short implied, betting you know volatility better.

## Practical execution challenges

Rehedging incurs [bid-ask spreads](/bid-ask-spread/). On a liquid stock, a 50-share sale and 48-share buy-back might cost 2 or 3 cents in spread. Over hundreds of rehedges, these add up to hundreds or thousands of pounds in friction. The strategy only works if [realized volatility](/historical-volatility/) exceeds [implied volatility](/implied-volatility/) by more than the cumulative spread cost.

Rehedging also assumes liquidity. If the stock gaps up 15% overnight, gamma scalping can't rehedge fast enough; the hedge becomes stale and the position suffers a large directional loss. Options market makers use gamma scalping on highly liquid stocks and indices where gaps are rare; they avoid it on thinly traded names where a single large trade moves the price.

## Scaling and portfolio context

Market makers don't scalp one call at a time. They run books of hundreds or thousands of options positions, all delta-hedged together. The portfolio's total [gamma](/gamma/) tells them how much profit they stand to make from realized volatility relative to what they paid for the options. If their aggregate [gamma](/gamma/) is positive and [realized volatility](/historical-volatility/) is running high, profits flow. If it's negative or [realized volatility](/historical-volatility/) drops, losses mount.

Portfolio-level gamma scalping often involves [gamma-scalping](/gamma-scalping/) alongside [vega bucketing](/vega-bucketing/) and broader greeks monitoring, because a large book is never single-greek-exposure—[vega](/vega/) (volatility surface changes), [theta](/theta/) (time decay), and even [rho](/rho/) (interest-rate risk) all matter.

## When gamma scalping breaks down

High [realized volatility](/historical-volatility/) doesn't guarantee profit if [implied volatility](/implied-volatility/) is *also* rising. You may scalp gamma profitably, but losses on your short [vega](/vega/) exposure (the [implied volatility](/implied-volatility/) you paid for the option) can overwhelm the gains. The 2020 volatility spike saw many gamma scalpers humbled because [realized volatility](/historical-volatility/) exploded, but [implied volatility](/implied-volatility/) rose *faster*, leaving them underwater despite rehedging profits.

Discrete rehedging intervals also create gaps. A stock might swing sharply and reverse within a single rehedge cycle. A manual trader rehedging once daily might miss that move entirely. Automated gamma scalpers, rehedging continuously or multiple times per second, are better positioned to harvest that volatility—but pay higher costs and face technology risk.

## See also

<div class="wiki-seealso">

### Closely related

- [Gamma](/gamma/) — the second-order greek that drives scalping profits
- [Delta Hedging](/delta-hedging/) — the rebalancing process that enables gamma scalping
- [Realized Volatility](/historical-volatility/) — the actual volatility traders aim to harvest
- [Implied Volatility](/implied-volatility/) — the volatility priced into options; the scalp bet
- [Theta](/theta/) — time decay; a cost for long-gamma positions held unhedged

### Wider context

- [Option](/option/) — the derivatives contract used to gain gamma exposure
- Greeks — the sensitivities that drive options trading
- [Black-Scholes Model](/black-scholes-model/) — the framework for calculating gamma and its profits
- [Hedge Fund](/hedge-fund/) — professional traders who run gamma scalping at scale
- [Market Maker](/market-maker-trading/) — often gamma scalps as part of providing liquidity

</div>
