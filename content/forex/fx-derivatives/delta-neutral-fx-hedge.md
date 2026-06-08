---
title: "Delta-Neutral FX Hedging: How It Works"
description: "Delta-neutral FX hedge explained: dealers hedge currency exposure with options by constantly rebalancing as spot moves, incurring gamma costs."
keywords:
  - delta neutral fx hedge
  - delta hedging currency options
  - gamma cost fx hedging
  - options rebalancing forex
image: "/svg/forex.svg"
---

*A **delta-neutral FX hedge** means adjusting a portfolio of currency [options](/option/) so that its price sensitivity to spot-rate moves is zero—the net [delta](/delta/) equals zero. Market-makers and corporate treasurers do this by selling or buying spot FX contracts or short-dated [forwards](/forward-contract/) every time the underlying rate moves, locking in the option's initial premium but incurring a continuous cost (gamma bleed) from this rebalancing.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Delta-Neutral FX Hedging — key facts</div>

<img src="/svg/forex.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Dealers neutralise their FX options book's spot sensitivity, using forwards to stay flat as rates move, paying the cost of rebalancing.</div>

|   |   |
|---|---|
| **Goal** | Eliminate the directional P&L swing from spot moves; fix the option premium paid upfront |
| **Method** | Sell spot or forwards when delta is positive; buy when delta is negative; rebalance as spot changes |
| **Frequency** | Continuous for active dealers; daily or weekly for corporates |
| **Cost** | Negative gamma cost (the difference between realised and [implied volatility](/implied-volatility/)) |
| **Who uses it** | FX option dealers, corporate treasury hedging flows, private banks managing client [options](/option/) |
| **Key greeks** | [Delta](/delta/) (position sensitivity), [gamma](/gamma/) (delta change rate), [vega](/vega/) (volatility sensitivity) |
| **Time horizon** | Option tenor; rebalancing occurs until expiration or early exercise |

</aside>

## Why dealers delta-hedge options

A foreign-exchange [option](/option/)—say, a EUR/USD call—is not a directional position on the Euro. It is a *leveraged* bet on volatility. A dealer who sells a EUR/USD call to a corporate buyer receives a premium upfront (say, 2% of notional) but is now exposed: if the Euro rallies hard, the call goes deep [in-the-money](/in-the-money/) and the dealer's loss is theoretically unlimited.

To neutralize this directional risk while keeping the premium, the dealer hedges. The simplest approach is delta-hedging: buy spot EUR/USD in the same quantity as the option's initial [delta](/delta/), so that if the Euro rallies, the profit on the spot long position offsets the loss on the short call.

But the hedge is only instantaneously perfect. The moment the spot rate twitches, the option's delta changes ([gamma](/gamma/) effect), and the hedge is no longer neutral. To stay flat, the dealer must rebalance—buy more EUR if the option's delta has become more positive, sell if it has become less positive. This continuous rebalancing is the mechanism of delta-neutral hedging.

## The mechanics of continuous rebalancing

Suppose a dealer sells a one-month EUR/USD call with a [strike price](/strike-price/) of 1.0800 (spot is 1.0750 at sale). The option's [delta](/delta/) is 0.50—meaning the option price moves 0.50 pips for every 1 pip move in spot.

The dealer's initial rebalance:
- Short the call (receive premium, say €2.5m notional)
- Buy €1.25m spot to match the delta (0.50 × €2.5m notional)

Now the position is delta-neutral. If spot does not move, the dealer profits from time decay ([theta](/theta/)) and pockets the premium.

But suppose EUR/USD rises to 1.0800 (the strike price):
- The call is now at-the-money; delta climbs to ~0.55
- The dealer's spot long (€1.25m) is insufficient to hedge the increased call liability
- The dealer must buy an additional €0.125m spot to restore delta neutrality

Conversely, if EUR/USD falls to 1.0700:
- The call is now out-of-the-money; delta falls to ~0.45
- The dealer's long spot is now too large
- The dealer must sell €0.125m spot to rebalance

This rebalancing continues throughout the option's life, multiple times per day for active dealers, until expiration. Each rebalance is transacted at the market [bid-ask spread](/bid-ask-spread/), and the dealer realises a cost.

## The cost of rebalancing: gamma and realised volatility

The rebalancing cost is captured in [gamma](/gamma/) and the difference between implied and realised [volatility](/volatility-smile/).

**Gamma cost**: [Gamma](/gamma/) measures how fast [delta](/delta/) changes as spot moves. A dealer with a [short call](/call-option/) (or any short option) is short [gamma](/gamma/)—meaning that as spot rallies, the dealer is forced to buy higher; as spot falls, the dealer is forced to sell lower. Over time, this buy-high-sell-low dynamic burns capital.

The daily cost is roughly:

> **Gamma Loss = (1/2) × Gamma × (Realised move)²**

If [gamma](/gamma/) is 0.01 and the daily move is 0.5%, the dealer loses roughly 0.01 × 0.25 / 2 = 0.00125, or 0.125% of notional per day.

**Implied vs. realised volatility**: The dealer sold the call at an implied [volatility](/volatility-smile/) of, say, 12% annualised. This implied vol is baked into the premium. But the actual realised [volatility](/volatility-smile/)—the standard deviation of daily spot moves—might be lower (say, 8%) or higher (say, 16%).

If realised vol is lower than implied, the dealer profits; the gamma losses are smaller than the premium collected. If realised vol is higher, the dealer loses; the gamma cost exceeds the premium.

Over the life of the option, the dealer's total profit or loss is:

> **P&L = Premium received − (realized vol pnl − implied vol pnl)**

Or more simply: profit if realised volatility is low (call premium decays faster than gamma bleeds), loss if realised volatility is high (gamma cost accelerates).

## Practical rebalancing frequencies and hedging costs

No dealer rebalances infinitely often. Transaction costs and operational complexity constrain the frequency. In practice:

- **High-touch trading desks** (major banks) rebalance EUR/USD, GBP/USD, and other liquid pairs 10–50 times per day, incurring basis-point spreads.
- **Corporate treasurers** managing a single hedge of, say, a three-month receivable, might rebalance weekly or monthly, accepting some residual delta.
- **Small dealers** in exotic pairs (e.g., MXN/ZAR) rebalance only when spot has moved >2–3%, owing to wide spreads.

The wider the bid-ask spread and the more volatile the pair, the greater the incentive to reduce rebalancing frequency—and the greater the residual gamma risk. Dealers typically quantify this trade-off: "If we rebalance daily, our hedging cost is X bps; if weekly, it's Y bps but we're exposed to intra-week moves."

## The broader portfolio context

A single option is rarely delta-hedged in isolation. Most dealers run a **portfolio of options** (calls, puts, all tenors, all strike prices) and delta-hedge the *entire book*.

A dealer's FX options book might have:
- 500m EUR/USD calls (strike 1.0800, 1m tenor): net delta = +150m
- 300m EUR/USD puts (strike 1.0700, 1m tenor): net delta = −90m
- 200m GBP/USD straddles: net delta = ~0 (by construction)
- Etc.

The portfolio net delta might be +100m EUR/USD. To stay delta-neutral, the dealer buys 100m EUR/USD spot (or a rolling [forward](/forward-contract/) ladder). As new client trades arrive, this net delta shifts, and the dealer rebalances.

## Residual risks in a delta-neutral book

Staying delta-neutral eliminates directional risk but introduces other exposures:

**Vega risk**: The dealer still profits or loses based on the [implied volatility](/implied-volatility/) at which the book was sold vs. the realised volatility. On busy trading days when implied vol jumps, a delta-neutral book can suffer large P&L swings.

**Tail risk**: Extremely large moves (e.g., SNB unwind in Jan 2015, Brexit) break the assumption that [delta](/delta/) and [gamma](/gamma/) capture the relationship between option and spot. Dealers incur larger gamma losses than models predicted.

**Credit and [counterparty risk](/counterparty-risk/)**: Rebalancing via spot trades or [forwards](/forward-contract/) requires a credit line with a counterparty. During stress periods (e.g., 2020 COVID sell-off), credit lines tighten, and dealers cannot rebalance efficiently.

**Operational risk**: Systems failures, failed trades, or delayed settlements can leave a dealer unhedged for hours or days.

## Corporate use: fixing the effective cost of options

Corporates sometimes delta-hedge purchased options to lock in the effective cost and reduce uncertainty. A company that buys a EUR/USD put to protect a €50m receivable might:
1. Buy the put at 2% premium (cost €1m upfront).
2. Delta-hedge by selling some spot EUR/USD immediately.
3. Rebalance weekly.

The upshot: the company knows the net cost is roughly the put premium plus the gamma bleed (or gain, if realised vol is low). This is more predictable than a bare put, which can still lose value if spot moves sideways and implied vol collapses.

## See also

<div class="wiki-seealso">

### Closely related

- [Delta](/delta/) — the rate of change of option price relative to spot
- [Gamma](/gamma/) — the rate of change of delta; the cost of delta-hedging
- [Vega](/vega/) — option sensitivity to volatility; orthogonal to delta hedging
- [Option](/option/) — the underlying instrument being hedged
- [Implied volatility](/implied-volatility/) — the vol priced into the option premium
- [Forward contract](/forward-contract/) — the hedging instrument dealers use for rebalancing

### Wider context

- [Currency risk](/currency-risk/) — the FX exposure corporates and dealers face
- [Derivatives hedging](/derivatives-hedging/) — the conceptual framework
- [Market maker trading](/market-maker-trading/) — how dealers operate and profit
- [Bid-ask spread](/bid-ask-spread/) — the cost of rebalancing

</div>
