---
title: "Negative Gamma Risk Explained"
description: "Negative gamma risk occurs when you are short options and the underlying asset moves sharply. Understand P&L losses and why traders manage this exposure carefully."
keywords:
  - negative gamma risk
  - short gamma risk explained
  - option delta hedging gamma
  - gamma options trading
  - market maker gamma exposure
---

*A **negative gamma risk explained** is the hazard faced by short option positions: as the underlying asset price moves sharply in either direction, the delta of your position accelerates away from you, forcing you to sell low (after a spike down) or buy high (after a spike up) to rehedge. Market makers and premium sellers incur losses that compound with volatility—and they must actively rebalance to control this risk.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Negative Gamma — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Short gamma is a penalty for being wrong about the size of market moves, not the direction.</div>

|   |   |
|---|---|
| **Gamma definition** | Rate of change of an option's delta |
| **Short gamma position** | You are short options; gamma is negative |
| **Directional risk** | None (gamma is neutral to direction) |
| **Volatility risk** | Sharp moves cause cumulative P&L loss |
| **Delta decay** | Your delta drifts as the stock moves |
| **Rehedging cost** | You buy high, sell low (realized losses) |
| **Theta offset** | Time decay helps offset gamma loss |
| **Classic example** | Selling straddles or iron condors |

</aside>

## What gamma is and why it matters

[Gamma](/gamma/) measures the sensitivity of an option's [delta](/delta/) to changes in the underlying asset's price. Delta is the rate at which the option's value changes per unit move in the stock. Gamma is the rate at which *delta* changes.

Suppose you own a call option with a delta of 0.5. If the stock rises $1, the call gains approximately $0.50—that is the delta. But if gamma is 0.05, then after that $1 rise, the new delta is 0.55. If the stock then falls $1 back to its original price, the delta falls back to 0.50. The option's value didn't return to exactly where it started; the asymmetry is gamma's doing.

Gamma is always positive for long options (calls and puts) and always negative for short options. If you *own* a call or put, gamma works in your favor: when the underlying moves your way, delta increases, amplifying your gain; when it moves against you, delta decreases, capping your loss. If you *sell* (short) a call or put, gamma is your enemy: when the underlying moves away from you, delta accelerates in that direction, and your unrealized loss compounds.

## The P&L trap of negative gamma

Here is the P&L profile of negative gamma in practice.

You short an at-the-money straddle (one call and one put) on a stock trading at $100. You collect the [option premium](/option-premium/) upfront—say, $10 total. You hedge by buying 50 shares of stock (the initial delta of the straddle is approximately zero, but the short call's delta of −0.5 and the short put's delta of −0.5 offset). You are now delta-neutral.

The stock then spikes to $110 in a single day. Your 50-share hedge is now underwater. The short call's delta accelerates toward −1.0, and your position is now delta-short by, say, −0.6 (your 50 shares are delta-long 50; short call is delta −0.60; short put is delta near zero now it is out of the money). To rehedge to delta-neutral, you must buy 10 more shares. You do so at $110.

The stock then falls back to $100. Now you are long 60 shares. The short call's delta falls back toward −0.5, and you are delta-long by approximately 10 shares. To rehedge to delta-neutral, you must *sell* 10 shares at $100. You've now sold high ($100) and bought high ($110). Ouch.

This is the essence of negative gamma: every time you rehedge an option short in a volatile market, you are forced to buy high and sell low. The realized loss mounts with the number and amplitude of rehedges. This is distinct from the theta profit (time decay of the option) you earned upfront. If volatility is extremely low, theta wins and you profit. If volatility is high and the underlying moves sharply, gamma losses overwhelm theta gains.

## Why market makers manage it

Market makers and professional premium sellers live with negative gamma risk. They are the ones quoting prices in options markets, holding inventory, and hedging. If a market maker is short a large block of calls and puts, negative gamma is a constant drag.

The market maker's game is:
1. Collect the [bid-ask spread](/bid-ask-spread/) as customers buy and sell options.
2. Pocket the [theta](/theta/) (time decay) as the options lose value.
3. Keep gamma losses small by rehedging frequently and staying close to fair value.

In calm markets with low implied volatility, gamma losses are small and theta dominates. In choppy markets, gamma losses can swamp theta, turning a profitable position into a money-loser in a single session. Market makers adjust their bids and offers (widening the spread) when volatility is high to compensate for the expected gamma loss.

Smart market makers also monitor skew and [implied volatility](/implied-volatility/). If you sold puts and the stock starts to collapse, the put you sold becomes further in the money and the implied volatility of that put spikes. Your gamma loss is compounded by the fact that the option's value is rising not only because it is deeper in the money but also because volatility is increasing. This is [vega](/vega/) risk on top of gamma risk.

## Hedging and rehedging frequency

The speed and cost of hedging negative gamma depend on several factors:

**Bid-ask spread:** The wider the spread on the underlying or the option, the more it costs to rehedge. If you must buy stock to rehedge and you have to cross a wide spread, you are immediately underwater. Illiquid underlyings are therefore dangerous for short option positions.

**Transaction costs and slippage:** In high-frequency rehedging, commissions and slippage add up. This is one reason why retail traders often avoid short options and why professional market makers use electronic execution and have negotiated very low commissions.

**Realized volatility vs. implied volatility:** If the stock's actual (realized) volatility is lower than the implied volatility you sold, you make money: the option decays faster than you expected, and gamma losses are small. If realized volatility exceeds implied volatility, you lose: the option decays slower, gamma losses accelerate, and you pay dearly to rehedge.

Some traders use a [vega](/vega/) hedge—owning longer-dated options or a different strike to cap gamma loss—but this is expensive and ties up margin.

## The role of theta

It is crucial to note that short gamma is paired with long theta. The option premium you collected *includes* a theta decay component. Each day that passes, your short option decays slightly in value, and you pocket that decay. In a calm market, this theta income can exceed gamma losses, yielding a net profit.

But theta decays by the *square root* of time (roughly), while gamma losses scale with the *square* of the realized stock move. In a market that gyrates wildly over several days, gamma losses quickly eclipse theta gains.

This is why professional traders obsess over realized vs. implied volatility. If you sell an option when [implied volatility](/implied-volatility/) is high (say, 35%) and then realized volatility falls to 20%, you profit: theta decay proceeds faster than gamma losses, and you win. Conversely, if you sell when implied volatility is low (say, 15%) and realized volatility explodes to 40%, you lose: gamma losses dwarf theta decay.

## Common short-gamma strategies

- **Covered calls and cash-secured puts:** These are implicitly short gamma. You collect the call premium or put premium and pocket theta, but if the underlying moves sharply, gamma losses arise.
- **Iron condors and short straddles:** Deliberately short gamma; profitable in low-volatility environments, dangerous in explosive ones.
- **Short put spreads:** Same profile—long theta, short gamma.

Retailers attempting these strategies often underestimate gamma risk, especially in overnight gaps or during earnings announcements when volatility can double in minutes.

## See also

<div class="wiki-seealso">

### Closely related

- [Gamma](/gamma/) — the rate of change of delta; always negative for short positions
- [Delta](/delta/) — the option's sensitivity to the underlying price; drives rehedging decisions
- [Theta](/theta/) — time decay of options; positive for short positions, offsets gamma losses
- [Vega](/vega/) — sensitivity to implied volatility; can compound gamma losses in a vol spike
- [Option](/option/) — the fundamental derivative contract
- [Volatility Smile](/volatility-smile/) — how implied volatility varies by strike; affects gamma profiles across strikes

### Wider context

- [Derivatives Hedging](/derivatives-hedging/) — managing risk in derivatives positions
- [Historical Volatility](/historical-volatility/) — the actual volatility of past price moves
- [Implied Volatility](/implied-volatility/) — the market's forecast of future volatility, embedded in option prices
- Greeks — collective name for delta, gamma, theta, vega, rho

</div>
