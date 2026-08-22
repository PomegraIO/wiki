---
title: "Synthetic Currency Pair Construction"
description: "Learn how to construct synthetic currency pairs by combining two dollar-based pairs to trade illiquid cross rates with tighter spreads and deeper liquidity."
keywords:
  - synthetic currency pair
  - how to construct a synthetic currency pair
  - synthetic cross rate
  - illiquid currency pairs
  - forex pair construction
  - currency pair trading
  - cross rate trading
image: /svg/forex.svg
---

*A **synthetic currency pair** is a constructed trade that mimics an illiquid or exotic currency pair by combining two liquid pairs—typically both involving the [US dollar](/us-dollar/) as an intermediary. Instead of trading EUR/GBP (a less liquid cross), a trader might buy EUR/USD and sell GBP/USD simultaneously, achieving the desired exposure with lower transaction costs and wider [price discovery](/price-discovery/).*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Synthetic Currency Pairs — key facts</div>

<img src="/svg/forex.svg" alt="An abstract editorial mark for foreign exchange." />

<div class="wiki-infobox-caption">Engineering liquidity by trading two dollar pairs instead of an illiquid cross.</div>

|   |   |
|---|---|
| **Method** | Buy or sell one dollar pair; sell or buy the other dollar pair |
| **Typical structure** | Long base currency vs USD, short quote currency vs USD (or vice versa) |
| **Primary advantage** | Tighter [bid-ask spreads](/bid-ask-spread/), deeper liquidity than native cross |
| **Common use case** | Trading illiquid crosses (e.g., EUR/GBP, AUD/NZD, emerging market pairs) |
| **Construction cost** | Two [market-maker](/market-maker-trading/) spreads instead of one; offsetting by tighter USD pair spreads |
| **Execution complexity** | Two orders; minor timing risk between legs |
| **Profit/loss symmetry** | P&L identical to direct cross trade if prices move proportionally |

</aside>

## Why Synthetic Construction Exists

The [forex market](/stock-market/) is highly fragmented by [currency pair](/currency-volatility/) liquidity. The most liquid pairs—those involving the US dollar or the euro—trade with tight [bid-ask spreads](/bid-ask-spread/), deep order books, and instant execution. Crosses like AUD/JPY, GBP/CAD, or emerging-market pairs trade with much wider spreads and volatile quoted prices, reflecting fewer participants and less active hedging demand.

Rather than accept those wider spreads and slippage, traders construct synthetics. This works because most currency pairs inherit their pricing from the two-pair chain. If EUR/USD is 1.0850 and GBP/USD is 1.2650, the implicit EUR/GBP rate is 1.0850 / 1.2650 ≈ 0.8584. A direct EUR/GBP quote might wander from that fair value due to thin liquidity, but the synthetic keeps the trader pegged to fair value with tighter overall costs.

## The Mechanics: A Worked Example

Suppose a trader wants **long EUR/GBP exposure** (betting the euro will strengthen against sterling) but finds the native EUR/GBP bid-ask spread is 2.5 pips wide. Instead, she could:

1. **Buy EUR/USD** at the offered price (e.g., 1.0850) — this goes long euros versus dollars
2. **Sell GBP/USD** at the bid price (e.g., 1.2650) — this goes short pounds versus dollars

Together, these two legs create a long EUR/GBP position:
- **Leg 1:** EUR/USD long + **Leg 2:** GBP/USD short = **EUR long, GBP short**

The effective cross rate she achieves is 1.0850 / 1.2650 = 0.8584 EUR/GBP, with a combined spread of (say) 1 pip on EUR/USD + 1 pip on GBP/USD, totaling an effective 2 pips versus 2.5 pips on the direct cross—and in a more liquid venue.

**Conversely, for short EUR/GBP**, the trader would:
1. Sell EUR/USD
2. Buy GBP/USD

Same pairs, opposite direction.

## When Synthetics Beat Native Crosses

A synthetic is preferable when:

**The native cross spread is unusually wide.** Emerging-market pairs, thinly-traded commodity currencies, or exotic combinations often quote at 3–5 pips or wider. A synthetic using two tight USD pairs (0.5–1 pip each) cuts total transaction cost substantially.

**Execution urgency is high.** Two liquid pairs fill instantly and in size; a native cross might slip badly or only partially fill. The trader accepts two spreads to get certainty of execution.

**Market hours matter.** During Asian or European sessions, some crosses trade thin liquidity while both its component USD pairs remain liquid. A trader in Tokyo can synthetically trade EUR/GBP even when sterling crosses are slow.

**Hedging or portfolio balancing.** A hedge fund with long EUR exposure and short GBP exposure can execute both legs as separate dollar trades rather than forcing a synthetic into a cross-rate venue.

## When Native Crosses Are Better

A direct cross trade is superior when:

**The native cross is tight and liquid.** Major pairs like EUR/GBP or EUR/CHF often trade with competitive spreads in major forex hubs. The single bid-ask is narrower than two spreads combined.

**Timing is critical.** Synthetic construction introduces a few milliseconds of execution slippage between legs. High-frequency traders or very short-term speculators may lose the edge from the tighter overall spread.

**[Counterparty risk](/counterparty-risk/) matters.** Trading two separate legs with a [broker](/broker/) means two counterparties or two separate credit lines. A single cross trade concentrates exposure.

## The No-Arbitrage Relationship

In an efficient market, the synthetic and native cross prices must align (or the small difference should not exceed round-trip costs). If EUR/USD is 1.0850, GBP/USD is 1.2650, and the native EUR/GBP cross is quoted at 0.8500 (much lower than the synthetic fair value 0.8584), an arbitrageur could instantly:
- Buy EUR/GBP at 0.8500
- Sell the synthetic (sell EUR/USD, buy GBP/USD) at 0.8584
- Lock in 84 pips with zero directional risk

In practice, this [price discovery](/price-discovery/) mechanism is not instantaneous. Stale quotes on the cross, high trading costs, or credit lines may prevent arb execution, so small mispricings persist—but large ones are rare among the most liquid crosses.

## Execution Considerations

**Timing of legs.** Ideally, both legs execute within milliseconds to avoid interim [currency risk](/currency-risk/). Many traders use a [limit order](/limit-order/) on one leg and a [market order](/market-order/) on the other, accepting slight price differences to reduce the chance of a partial fill.

**Position size.** Synthetics work best for mid-sized positions. Very large trades may move USD pair prices, negating the liquidity advantage.

**Reversal and profit-taking.** To close a synthetic position, the trader reverses both legs. Price slippage on exit can be as material as on entry, particularly if the cross has tightened in the interim.

## See also

<div class="wiki-seealso">

### Closely related

- [Bid-Ask Spread](/bid-ask-spread/) — transaction cost that synthetic construction seeks to minimize
- [Price Discovery](/price-discovery/) — how synthetic and cross prices converge in liquid markets
- [Counterparty Risk](/counterparty-risk/) — exposure when trading with a single broker or venue
- [Spot Exchange Rate](/spot-exchange-rate/) — cash rate for currency pairs; basis for synthetic construction
- [Market Maker (Trading)](/market-maker-trading/) — liquidity provider that quotes tighter spreads on major pairs
- [Currency Risk](/currency-risk/) — directional risk a synthetic is designed to hedge or express

### Wider context

- Foreign Exchange — global decentralized market where synthetics serve as liquidity bridges
- [Limit Order](/limit-order/) — precise execution tactic for multi-leg synthetic trades
- [Fragmented Market](/fragmented-market/) — characteristic of forex that motivates synthetic construction
- [Execution Risk](/execution-risk/) — slippage on fills when synthetics are used

</div>
