---
title: "FX Gamma Scalping"
description: "Dynamic rehedging of an options book to capture profits when realised volatility exceeds implied volatility; earns the gamma spread."
keywords:
  - gamma scalping
  - gamma trading
  - delta hedging
  - realised volatility
  - implied volatility
image: /svg/forex.svg
---

*FX **gamma scalping** is the art of profiting from the difference between [implied volatility](/implied-volatility/) (the volatility baked into option prices) and [realised volatility](/historical-volatility/) (the actual moves the market makes). A trader buys options when they are cheap relative to expected movement, then rehedges continuously to lock in profits as the market moves, capturing the spread between paid premium and earned rehedging gains.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">FX Gamma Scalping — key facts</div>

<img src="/svg/forex.svg" alt="An abstract editorial mark for currency derivatives." />

<div class="wiki-infobox-caption">Harvest volatility by rehedging dynamically.</div>

|   |   |
|---|---|
| **Core idea** | Buy long [gamma](/gamma/) (optionality), set [delta](/delta/) to zero, profit when realised volatility exceeds implied |
| **Mechanics** | Buy option; repeatedly adjust [delta](/delta/) hedge to stay neutral as underlying moves |
| **Profit source** | The spread between [implied volatility](/implied-volatility/) paid and realised volatility earned through rehedging |
| **Risk** | If realised volatility falls below implied, you lose money; [gamma scalping](/fx-gamma-scalping/) is a volatility bet |
| **Rehedging frequency** | More often (daily or multiple times daily) if moves are large; determines accuracy and transaction cost |
| **Tools** | FX [options](/option/) (calls, puts, straddles); sometimes [swaptions](/fx-swaption/) on long-dated books |

</aside>

## The mechanic: long gamma, zero delta, compound rehedges

The fundamental principle is simple: buy an option, then continuously rehedge its [delta](/delta/) to stay [delta](/delta/)-neutral (i.e., indifferent to the immediate direction of the spot rate). Each time the spot moves, the option's [delta](/delta/) changes. You sell the appreciated side and buy the depreciated side, locking in a small profit. Over time, if the market moves a lot, those small profits compound.

**Concrete example:**
- You buy a 1-year EUR/USD call at a strike of 1.1000 for USD 0.025 per EUR, with an [implied volatility](/implied-volatility/) of 10%.
- The option's [delta](/delta/) is 0.40; you're long EUR exposure.
- To neutralize, you **sell** 40 EUR forward (or sell 40 EUR/USD call equivalents).
- EUR/USD moves to 1.1010. The call is now worth USD 0.028; its [delta](/delta/) is 0.55.
- You **rehedge** by buying back 15 EUR forward to restore your delta-neutral position (from 40 to 55 short).
- You locked in a USD 0.003 profit on the rehedge while the call appreciated USD 0.003.

The profit accrues from the difference between the option's move (governed by [gamma](/gamma/), which is convex) and the linear move of your delta hedge.

## Why realised volatility matters more than direction

The genius of gamma scalping is that it's almost direction-agnostic. Whether EUR/USD rallies or falls doesn't matter—you're [delta](/delta/)-neutral. What matters is *how much it moves*. If EUR/USD swings 5% in a month, you harvest profits by rehedging many times. If it sits flat, you lose money because you paid premium without earning anything back.

This is why [gamma](/gamma/) scalpers live and die by the spread between [implied volatility](/implied-volatility/) and [realised volatility](/historical-volatility/). When you buy an option with 10% implied volatility but the spot subsequently moves with 15% annualized volatility, you're printing money. When implied is 15% and realized is 8%, you're bleeding.

## The cost structure: gamma scalping is expensive

Rehedging constantly incurs costs:

1. **Bid-ask spreads**: Every time you trade EUR/USD forward to rehedge, you pay the spread (even if small).
2. **Slippage**: In volatile markets, your rehedge order hits a worse price than the mid-price.
3. **Transaction costs**: Brokers charge commissions or wider spreads for frequent traders.

These costs eat into the gamma profit. If you rehedge monthly, spreads are tolerable. If you rehedge every 10 minutes, spreads can exceed the daily gamma gain, turning the strategy into a money-loser. The optimal rehedging frequency balances capturing gamma gains against incurring costs.

Most institutional gamma scalpers rehedge once or twice daily for major pairs like EUR/USD, and less frequently for exotics where spreads are wider.

## Practical execution: straddles and strangles

A pure gamma scalp often uses a **straddle** (buy both a call and a put at the same strike) or **strangle** (call and put at different strikes). Both give long [gamma](/gamma/) with minimal initial [delta](/delta/)—the option is agnostic about direction.

For a 1-year EUR/USD at-the-money straddle:
- Buy 1-year EUR/USD call at 1.1000.
- Buy 1-year EUR/USD put at 1.1000.
- Combined [gamma](/gamma/): approximately 2× a single option's [gamma](/gamma/).
- Initial [delta](/delta/): near zero.
- Cost: two premiums.

As the spot moves in either direction, both legs contribute [gamma](/gamma/), and you rehedge the delta. The straddle is pricier upfront but captures volatility regardless of direction.

A strangle—buying out-of-the-money options—is cheaper but requires larger moves before [gamma](/gamma/) kicks in meaningfully.

## The volatility surface and [delta](/delta/) conventions

Gamma scalping interacts tightly with the [volatility smile](/volatility-smile/). Options further from the money have higher [gamma](/gamma/) but lower [vega](/vega/), making them more sensitive to realized moves but less sensitive to changes in [implied volatility](/implied-volatility/) itself.

Additionally, FX markets quote options using [delta conventions](/fx-delta-conventions/): spot delta, forward delta, or premium-adjusted. A gamma scalper must choose which [delta](/delta/) convention to use for rehedging. Forward delta is often preferred for longer-dated books, because it captures interest-rate carry effects that affect the true hedge ratio.

## Real-world constraints: gaps and overnight risk

Theory assumes continuous rehedging; reality is messier. Currency markets close on weekends; geopolitical shocks or central-bank surprises can cause overnight gaps. A EUR/USD position gapped 2% on Brexit news, wiping out weeks of accumulated gamma scalping gains in a few seconds.

Gamma scalpers must size their positions to survive a 1-2% overnight gap. Larger positions mean larger rehedging profits on normal days but also mean larger potential losses if the unhedged gap is large. Insurance—via out-of-the-money [options](/option/) that protect your gamma position—is expensive.

## When gamma scalping is profitable

Gamma scalping works best when:

- **Realised volatility is systematically higher than implied.** Some markets, notably emerging-currency pairs, trade with implied volatility well below realised, creating a sustained spread.
- **You have a low-cost trading infrastructure.** Tight bid-ask access and fast execution systems matter. Retail traders typically can't compete.
- **Liquidity is high.** Major pair FX markets (EUR/USD, GBP/USD) trade around the clock with tight spreads; emerging-market pairs are harder to scalp profitably.
- **Your carry costs are low.** If you're borrowing money to finance the long [gamma](/gamma/) position, high interest rates erode your edge.

Central banks and large hedge funds have the scale and infrastructure to gamma scalp profitably. Retail traders and small prop shops often find the spreads too wide.

## Gamma scalping and options pricing models

The [Black-Scholes model](/black-scholes-model/) assumes continuous rehedging with zero transaction costs and constant [volatility](/historical-volatility/). Gamma scalping is the strategy that most closely mirrors these assumptions—buy an option, rehedge continuously, capture the mathematical edge. When real-world frictions (spreads, slippage) are small relative to the gamma edge, the strategy works. When frictions are large, it doesn't.

## See also

<div class="wiki-seealso">

### Closely related

- [Gamma](/gamma/) — the rate of change of [delta](/delta/); core to gamma scalping profit and loss
- [Delta](/delta/) — rehedging target; must stay near zero to isolate [gamma](/gamma/) exposure
- [FX Option Delta Conventions](/fx-delta-conventions/) — choosing spot vs. forward delta affects rehedging frequency and cost
- [Implied volatility](/implied-volatility/) — the volatility you pay for the option; you profit if realised exceeds it
- [Realised volatility](/historical-volatility/) — the actual volatility the market delivers; the source of gamma scalping profit

### Wider context

- [Option](/option/) — the underlying instrument; gamma scalping is an options strategy
- [Vega](/vega/) — sensitivity to changes in [implied volatility](/implied-volatility/); orthogonal to gamma scalping
- [Theta](/time-decay-theta/) — time decay; works against long gamma positions, must be overcome by realised volatility
- [Volatility smile](/volatility-smile/) — shows [gamma](/gamma/) distribution across strikes
- [FX Swaption](/fx-swaption/) — long-dated gamma can also be traded via swaptions on cross-currency swaps

</div>
