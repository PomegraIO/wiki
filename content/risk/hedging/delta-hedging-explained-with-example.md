---
title: "Delta Hedging Explained With an Example"
description: "Delta hedging is a technique to neutralize directional risk in options by matching the delta exposure of the option with an offsetting stock position. Here is how it works with a concrete example."
keywords:
  - delta hedging
  - delta hedging example
  - delta neutral
  - hedging options
  - dynamic hedging
  - market maker hedging
---

*A market-maker or options trader uses **delta hedging** to construct a position that is insensitive to small price moves in the underlying stock, isolating the time-value (theta) gain from directional (delta) risk. This requires buying or selling stock to match the option's [delta](/delta/) and rebalancing as the delta drifts.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Delta Hedging — Key Mechanics</div>

<img src="/svg/risk.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Delta hedging turns a directional bet into a time-value bet, converting profit from price movement into profit from decay.</div>

|   |   |
|---|---|
| **Core idea** | Offset option delta with stock position so net delta = 0 |
| **Delta value** | Ranges from 0 to 1 for calls, 0 to −1 for puts; -1 to 0 for short puts |
| **Rebalancing** | Required periodically as delta changes (especially as expiration nears) |
| **Cost source** | [Transaction costs](/bid-ask-spread/), [slippage](/bid-ask-spread/), and potential [[gamma](/gamma/)] losses if market volatility spikes |
| **Benefit** | Profit from [time decay](/time-decay-theta/) (theta) regardless of price direction |
| **Risk remaining** | [Vega risk](/vega/) (volatility changes), [gamma risk](/gamma/) (large moves), execution risk |

</aside>

## What Delta Represents and Why You Hedge It

[Delta](/delta/) measures how much an option's price changes when the underlying stock moves by $1. A call option with a delta of 0.6 gains $0.60 in value if the stock rises by $1. A put option with a delta of −0.4 gains $0.40 if the stock falls by $1.

For a market-maker or trader who has sold an option, this directional sensitivity is risk. If you sold a call and the stock rises sharply, you are suddenly long a position that is losing money. You have sold the option expecting to profit from time decay and (perhaps) from changes in volatility, not to make a bet on the direction of the stock.

Delta hedging removes that directional bet. By taking an offsetting position in the underlying stock, you make your overall position **delta-neutral**: a small move in the stock price leaves your total portfolio value approximately unchanged.

## A Concrete Example: Selling a Call and Hedging

Suppose a trader sells one call option contract (100 shares) on Apple at a strike price of $150, with 30 days to expiration. The stock is currently trading at $150 (at-the-money). The call has a delta of approximately 0.5.

**Initial position:**
- Short 1 call contract (100 shares) with delta = 0.5
- This means the trader is short 0.5 × 100 = 50 deltas.

To be delta-neutral, the trader must be long 50 deltas. The simplest way: buy 50 shares of Apple at the current price of $150.

**Delta-hedged position:**
- Short 1 call (−50 deltas)
- Long 50 shares (+50 deltas)
- **Net delta = 0**

Now, suppose Apple stock rises to $151 (a $1 move). The trader's position behaves as follows:

- The call option becomes deeper in-the-money. Its new delta is approximately 0.65, so the short call now represents −65 deltas.
- The 50 long shares have gained $50 (50 shares × $1).
- The short call has lost approximately $65 in value (the trader is short a position that increased by $65).
- **Net loss: $65 − $50 = −$15.**

Wait—that looks like a loss. But the trader still holds the option, and 29 days of time-value remain. As time passes and the stock stays around $151, the option will decay, and the short call position will recover some of that $65 loss. The trader's profit or loss over the month depends on how much time-value (theta) decay exceeds the [gamma](/gamma/) loss from rehedging.

## Why Rebalancing is Necessary

In the example above, after the stock rose to $151, the trader's delta drifted from 0 to −15. The position is no longer hedged. If the stock rises another $1, the trader will lose money again (because delta is now negative).

To restore delta-neutrality, the trader must rebalance: buy more stock to match the new delta. Since the call's new delta is 0.65, the trader needs 65 deltas long, which means buying 15 more shares.

**After rebalancing at $151:**
- Short 1 call (−65 deltas)
- Long 65 shares (+65 deltas)
- **Net delta = 0** again

Now, if the stock rises another $1 to $152, the trader again breaks even on the directional move and is again exposed only to time decay.

This continuous rebalancing is the heart of delta hedging: as the delta drifts, you restore neutrality by adjusting the hedge. Each rebalancing locks in a small loss (because you bought stock on the way up and sold it on the way down, or vice versa), but the time-value decay of the option ideally exceeds those losses over the month.

## Gamma: The Hidden Cost of Hedging

[Gamma](/gamma/) is the rate at which delta changes. It represents the cost of dynamic hedging.

In the example above, as the stock rose, delta rose from 0.5 to 0.65—a change of 0.15 deltas per $1 move. The trader had to buy 15 additional shares at $151, locking in a $15 loss relative to the initial hedge at $150. If the stock had fallen instead, the trader would have sold stock at a lower price and realized a similar loss.

This loss is **gamma loss**, and it grows with the magnitude of price moves. In a highly volatile market, a delta-hedged position can lose money rapidly due to gamma, even as time decay (theta) profits accumulate.

For a trader choosing to delta-hedge, understanding this trade-off is critical: you give up directional profit in exchange for eliminating directional risk, but you pay a real cost in the form of rehedging losses (gamma costs) whenever the stock moves significantly.

## Building a Delta-Hedged Portfolio Across Multiple Options

In practice, professional traders manage not one option but dozens or hundreds. A market-maker might be long calls on 50 stocks and short puts on 20 others. Each position carries its own delta. The market-maker computes the total (net) delta across all positions and then hedges it with a single stock-index [futures contract](/futures-contract/) or a basket of stocks.

For example:
- Long 150 call deltas (from various long calls)
- Short 200 call deltas (from short puts and short calls)
- **Net: −50 deltas (short)**

To hedge, buy $X of stock or buy 50 deltas' worth of stock-index futures. This single hedge covers all the directional risk from the entire portfolio, so the trader can focus on managing time-value and volatility (theta and vega) risks.

## Limitations and Risks That Remain

Delta hedging is not a free lunch. Even in a delta-hedged position, several risks remain:

- **Gamma risk**: Large moves in the stock cause rehedging losses that time decay may not fully offset.
- **Vega risk**: Changes in implied volatility affect the option price independently of the stock price. A drop in volatility hurts a position short options, even if delta-hedged.
- **Execution risk**: Rehedging requires buying and selling stock, incurring [bid-ask spreads](/bid-ask-spread/) and commissions. In fast markets, slippage can be severe.
- **Discrete rehedging**: A trader can't rehedge continuously in real time; there is always a lag. In a flash crash, the lag can be deadly.
- **Model risk**: Delta is computed using a model (typically [Black-Scholes](/black-scholes-model/)) based on assumptions about volatility and interest rates. If reality deviates, the hedge is imperfect.

## When Traders Use Delta Hedging

Delta hedging is the standard practice for:

- **Market-makers**: They sell options to retail customers and immediately delta-hedge to neutralize directional risk, profiting only on the bid-ask spread and time-value decay.
- **Proprietary traders**: They may buy options they believe are underpriced and delta-hedge to isolate their view on volatility (vega) from directional noise.
- **Corporate risk managers**: A company holding stock may buy puts and delta-hedge to create a synthetic zero-cost collar, minimizing downside protection costs.

Retail investors rarely delta-hedge manually; most brokers don't provide the tools, and transaction costs would be prohibitive. However, understanding delta hedging illuminates how market-makers price options and why [option premiums](/option-premium/) reflect both time-value and volatility expectations.

## See also

<div class="wiki-seealso">

### Closely related

- [Delta](/delta/) — the fundamental measure of directional sensitivity in options
- [Gamma](/gamma/) — the cost of rehedging as delta changes; gamma risk is the primary residual in delta-hedged positions
- [Theta (time decay)](/time-decay-theta/) — the profit source for delta-hedged short-option positions
- [Vega](/vega/) — volatility risk that persists even in delta-hedged positions
- [Black-Scholes model](/black-scholes-model/) — the framework for computing delta and rehedging
- [Hedge ratio calculation](/hedge-ratio-calculation/) — related technique for minimum-variance hedging with futures

### Wider context

- [Option](/option/) — the instrument being hedged
- [Derivatives hedging](/derivatives-hedging/) — broader category of risk management
- [Call option](/call-option/) — one leg of many delta-hedged strategies
- [Volatility smile](/volatility-smile/) — complications in real-world delta when implied volatility varies by strike

</div>
