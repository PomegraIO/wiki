---
title: "Triangular Arbitrage in Forex: Example and Mechanics"
description: "Walk through a triangular arbitrage forex example showing how traders exploit currency mispricings across three pairs to lock in risk-free profit."
keywords:
  - triangular arbitrage forex example
  - currency arbitrage three pairs
  - forex mispricing exploitation
  - covered arbitrage forex
image: "/svg/forex.svg"
---

*A **triangular arbitrage** in forex is a trade that locks in profit from a temporary mispricing across three currency pairs without taking on currency risk. The trader converts cash through three consecutive exchange rates, and if those rates don't multiply perfectly, the trader ends up with more base currency than they started with.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Triangular Arbitrage — quick facts</div>

<img src="/svg/forex.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">A mechanical trade exploiting rate inconsistencies across three pairs.</div>

|   |   |
|---|---|
| **Core idea** | Convert A → B → C → A; if rates are inconsistent, you profit |
| **Risk** | Execution slippage, latency, fees |
| **Execution** | Algorithmic; requires speed and tight spreads |
| **Availability** | Rare in liquid markets; more common on exotic pairs or smaller venues |
| **Typical profit** | Microfractions of a percent; scaled by capital deployed |

</aside>

## The Basic Setup

Triangular arbitrage works because currency prices are quoted independently across markets and venues. The trader exploits the fact that the three rates in a triangle (say, USD/EUR, EUR/GBP, and GBP/USD) should multiply to exactly 1.0 if they're perfectly consistent. If they don't, the triangle is "broken" and profit is possible.

Here's the essential principle: start with $1 million. Convert through three pairs on the quoted rates. If the math doesn't work out perfectly, you end up with more than $1 million.

## Worked Example

Suppose you observe the following rates on a trading platform:

- **USD/EUR**: 1 USD = 0.92 EUR (you get 0.92 euros per dollar)
- **EUR/GBP**: 1 EUR = 0.85 GBP (you get 0.85 pence per euro)
- **GBP/USD**: 1 GBP = 1.20 USD (you get 1.20 dollars per pound)

Start with $1,000,000.

**Leg 1: USD → EUR**
- You sell $1,000,000 at 0.92 EUR/USD.
- You receive: 1,000,000 × 0.92 = 920,000 EUR.

**Leg 2: EUR → GBP**
- You sell 920,000 EUR at 0.85 GBP/EUR.
- You receive: 920,000 × 0.85 = 782,000 GBP.

**Leg 3: GBP → USD**
- You sell 782,000 GBP at 1.20 USD/GBP.
- You receive: 782,000 × 1.20 = 938,400 USD.

**Result**: You started with $1,000,000 and ended with $938,400. You *lost* money. This triangle was not profitable. (In reality, you'd need the third leg to quote a higher USD/GBP rate, say 1.28, to make money.)

### Profitable Example

Change the third leg to **GBP/USD: 1 GBP = 1.30 USD**:

**Leg 3 (revised): GBP → USD**
- Sell 782,000 GBP at 1.30 USD/GBP.
- Receive: 782,000 × 1.30 = 1,016,600 USD.

**Result**: You started with $1,000,000 and ended with $1,016,600. Profit: $16,600, or **1.66% on your capital**.

In real trading, such gross mispricings rarely persist more than fractions of a second. The profit on a single $1 million cycle might be closer to 0.01% or 0.02%—pennies in aggregate—but executed thousands of times per second across huge capital bases, the cumulative yield adds up.

## Why It Works (and Why It's Rare)

The mispricings exist because:

- **Quoted rates on different venues differ slightly**. EUR/USD on one exchange might be 1.0850, while on another it's 1.0852.
- **Latency between markets**: by the time you read a price on one venue and act on another, the rates have shifted.
- **Imperfect information flow**: not all traders see all quotes instantly.

The profit window closes the instant enough traders spot the same inconsistency and transact. High-frequency trading firms use algorithms to detect these windows in milliseconds and execute the three-leg trade automatically.

Costs eat into the margin: bid-ask spreads, settlement fees, and slippage when you try to execute all three legs. For the arbitrage to be worth executing, the mispricing must be larger than the combined friction cost.

## The Role of Execution Speed and Capital

The traders who consistently profit from triangular arbitrage are those with:

- **Direct market access**: latency to multiple exchanges measured in microseconds.
- **Large capital bases**: because the per-cycle profit is tiny as a percentage, you need to move billions to make real money.
- **Proprietary algorithms**: automated detection and execution, so you spot and close the window before others do.

A retail trader sitting at a computer cannot compete. By the time you manually check three pairs and place three trades, the rates have moved and the arbitrage has evaporated.

## Practical Constraints

**Execution sequencing** matters. You need to execute all three legs nearly simultaneously; if you complete leg 1 and there's a long delay before leg 2, the intervening rate moves can wipe out your edge or turn profit into loss.

**Settlement and transfer** also carry hidden costs. Money moves through bank ledgers take time. On modern platforms, settlement is largely instant, but fees can still add up.

**Regulation and access**: Some small trading venues don't have the same liquidity or quote consistency as major exchanges, which is why arbitrage opportunities may be more visible on exotic currency pairs or offshore platforms. However, the risks of executing on thinner markets—wider spreads, limited depth, counterparty risk—often offset the higher apparent mispricing.

## Relationship to Other Arbitrage Types

Triangular arbitrage is a form of statistical arbitrage in the sense that it exploits temporary mispricings. It differs from [carry trade](/carry-trade/) (which bets on interest rate differentials over time) and from statistical arbitrage more broadly (which may involve many assets and probabilistic relationships rather than pure mechanical relationships).

When interest rate differentials are large and stable, [interest rate parity](/interest-rate-parity/) should hold. Triangular arbitrage is one mechanism by which traders enforce those no-arbitrage bounds: when rates deviate too far, arbitrageurs step in and the profits are competed away.

## See also

<div class="wiki-seealso">

### Closely related

- [Carry Trade](/carry-trade/) — exploiting persistent interest rate differentials, not short-term mispricings
- [Currency Risk](/currency-risk/) — how exchange rate moves affect unhedged positions
- [Bid-Ask Spread](/bid-ask-spread/) — the friction that often erases arbitrage profit
- [Market Maker Trading](/market-maker-trading/) — how dealers profit from spreads and order flow
- [Price Discovery](/price-discovery/) — how mispricings are corrected by trader action

### Wider context

- Forex Market — structure and participants in currency trading
- [Forward Exchange Rate](/forward-exchange-rate/) — pricing that embeds interest rate differentials
- [Spot Exchange Rate](/spot-exchange-rate/) — the quoted rate for immediate settlement
- [Algorithmic Trading](/algorithmic-trading/) — automation that powers modern arbitrage
- [Central Bank](/central-bank/) — intervention that can create transient mispricings

</div>
