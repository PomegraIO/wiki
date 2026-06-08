---
title: "Put Backspread"
description: "An option strategy that sells fewer near-the-money puts and buys a greater number of out-of-the-money puts to profit from sharp downside moves."
keywords:
  - put option
  - option spread
  - ratio spread
  - directional trading
  - bearish strategy
image: "/svg/derivatives.svg"
---

*A **put backspread** (also called a put ratio spread) sells a smaller number of [at-the-money](/strike-price/) or slightly out-of-the-money puts, then buys a larger number of farther out-of-the-money puts at a lower strike. Like its call-side counterpart, this ratio inversion creates a position that profits most dramatically when the underlying collapses sharply past the long put strike.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Put Backspread — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives." />

<div class="wiki-infobox-caption">A bearish, asymmetrical structure that turns limited downside risk into outsized gains below a breakeven.</div>

|   |   |
|---|---|
| **What it is** | Sell n puts at strike A; buy 2n puts at strike B (B < A) |
| **Also called** | Put ratio spread, put backspread |
| **Max profit** | Theoretically unlimited (below the long put strike) |
| **Max loss** | Limited to initial debit if stock stays above short strike |
| **Ideal market** | Strong bearish conviction; expect a crash or sharp reversal |
| **Key risk** | Capped gains between strikes; unlimited loss if decline stalls near short strike |
| **Legs** | Two (short put, long put) |

</aside>

## Mirror image of the call backspread

The put backspread is the bearish equivalent of the [call backspread](/ratio-spread-backspread/). You sell a smaller number of puts at a higher strike and buy a larger number at a lower strike. For example: sell 1 put at strike $100, buy 2 puts at strike $95. The two long puts are cheaper than the short put you sold, typically yielding a net credit.

If the stock stays above $100, you keep the credit and the position expires worthless. If it drops below $95, your 2 long puts capture exponential profit, generating roughly one dollar of gain per dollar the stock falls below $95. The ratio inversion—selling fewer than you buy—is the defining structural feature.

The put backspread is most useful when you expect a catalyst-driven drop (earnings miss, product recall, sector rotation, macro shock) rather than a slow bleed. The strategy rewards conviction and timing.

## The credit and the squeeze zone

Like the call backspread, a put backspread often generates an initial credit. This credit represents your maximum profit if the underlying stays above the short strike through expiration. It cushions the position against minor upside or sideways moves.

The danger zone is between the two strikes. If the stock falls slightly into that squeeze zone—say, to $98 in our example—both your short and long puts are losing money, but at different rates. The short put gains value faster initially because it has less extrinsic value left. You've surrendered the credit and haven't yet captured the dramatic downside profit. The worst loss often occurs near the short strike itself.

This is why put backspreads, like call backspreads, demand discipline and early management. Holding into the squeeze zone usually means accepting a realized loss or being forced to defend the position by rolling down or closing one leg.

## Implied volatility and the timing advantage

Put backspreads are especially attractive when [implied volatility](/implied-volatility/) is elevated leading into a catalyst. The sold put commands a fat premium, making the spread cheaper to establish or even turning it into a larger credit.

Post-event volatility crush can harm the trade if the stock doesn't move as expected. A drop in IV tightens the sold put's value faster than the bought put, eroding your credit or forcing a loss. This is the backside risk: you sold volatility and the market repriced it lower than you anticipated.

The classic setup is selling a put backspread 1–2 weeks before earnings (when IV is high) with the expectation of a sharp move post-announcement. If the stock crashes and IV stays elevated, you win twice—both from the directional move and from IV staying in your favour.

## Asymmetrical risk and reward

The put backspread is capped on the downside in one sense: you collect a credit and lose it only if the stock enters the squeeze zone. But below the long put strike, the position is theoretically unlimited in profit. Every dollar the stock falls nets you roughly one dollar of gain.

Above the short strike, your loss is limited to the initial debit (if you structured it that way) or zero (if you collected a credit). The asymmetry—defined upside risk, explosive downside profit—makes the strategy naturally bearish.

The trap is the same as with call backspreads: most stock moves are smaller than expected, and many stall exactly where you need them not to. A stock that drops 5% is worse than one that doesn't move at all, because you've given up the credit and gained nothing.

## Structural variations

A 1x2 put backspread (sell 1, buy 2) is the standard. Some traders use 1x3 or 1x4 for more leverage, concentrating both profit and loss around the short strike. Others run a "broken wing" put backspread by selling a fourth put even farther out of the money, capping the maximum loss and converting the trade into a defined-risk position at the cost of reduced upside.

You can also widen the strikes or adjust the ratio to tune the payoff diagram: narrower spreads (strikes closer together) require bigger moves to be profitable; wider spreads are cheaper but offer slower profit acceleration.

## When to deploy a put backspread

Use a put backspread when you have strong bearish conviction and a specific catalyst in mind. Earnings misses, sector downturns, geopolitical shocks, or a technical breakdown are ideal triggers.

Avoid put backspreads when you're uncertain about direction or timing. The strategy punishes wishful thinking: if you sell the backspread expecting a crash and the stock instead trades sideways for two weeks, you're sitting in a loss zone with nothing to show but declining theta.

The strategy is also less suitable for high-volatility securities (cryptocurrencies, biotech stocks in trials) where the gap risk between strikes can be enormous. A gap down can blow past your long puts in seconds, leaving you to absorb the theoretical unlimited loss.

## See also

<div class="wiki-seealso">

### Closely related

- [Call Backspread](/ratio-spread-backspread/) — the upside equivalent for bullish directional moves
- [Double Diagonal Spread](/double-diagonal-spread/) — manages directional risk while selling time on both sides
- [Reverse Calendar Spread](/reverse-calendar-spread/) — exploits short-term volatility ahead of longer-dated exposure
- [Option Premium](/option-premium/) — the time and volatility value that backspread structures exploit
- [Implied Volatility](/implied-volatility/) — the key leverage point for profitably entering put backspreads
- [Strike Price](/strike-price/) — the critical parameter for tuning ratio and profit zones

### Wider context

- [Option](/option/) — the foundational contract for all multi-leg strategies
- [Delta](/delta/) — directional exposure that determines downside profit capture
- [Volatility Smile](/volatility-smile/) — the IV distribution that affects spread economics across strikes
- [Protective Put](/protective-put/) — an alternative way to hedge downside risk

</div>
