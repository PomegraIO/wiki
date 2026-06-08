---
title: "Forex Cross Rate Calculation: How Non-USD Pairs Are Priced"
description: "Learn how forex cross rates like EUR/JPY are calculated from USD pairs using the triangular arbitrage relationship."
keywords:
  - forex cross rate calculation
  - cross rate formula
  - triangular arbitrage
  - currency pair pricing
  - non-usd pairs
image: "/svg/forex.svg"
---

*A **forex cross rate** is the exchange rate between two currencies neither of which is the US dollar — such as EUR/JPY (euros to Japanese yen). Instead of being quoted directly in the market, cross rates are calculated by dividing or multiplying two separate USD-based rates, a relationship rooted in arbitrage that keeps all three pairs in alignment.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Forex Cross Rate Calculation — key facts</div>

<img src="/svg/forex.svg" alt="An abstract editorial mark for forex." />

<div class="wiki-infobox-caption">Cross rates link three pairs into one consistent triangle.</div>

|   |   |
|---|---|
| **Formula** | Cross = Pair A / Pair B (both priced in USD) |
| **Example** | EUR/JPY = (EUR/USD) ÷ (JPY/USD) |
| **Triangular Test** | If A/B, B/C, C/A don't multiply to 1.0, arbitrage exists |
| **Common Crosses** | EUR/GBP, GBP/JPY, AUD/NZD, EUR/CHF |
| **Who Uses Them** | Global corporates, hedge funds, banks, arbitrageurs |

</aside>

## Why Cross Rates Exist

When a Japanese importer must pay a European supplier in euros, the importer does not need to trade JPY to USD and then USD to EUR. Instead, the importer can buy a **forex cross rate** directly: JPY/EUR or EUR/JPY. This is more convenient and, in theory, should cost no more than the two-leg path.

The central market, however, does not quote every possible currency pair. The most liquid and widely quoted pairs are those against the US dollar: EUR/USD, GBP/USD, JPY/USD, AUD/USD, and so on. These are the anchor pairs from which all other rates derive. Cross rates — any pair that excludes the dollar — are calculated from these anchor pairs using a simple arithmetic relationship.

This relationship is not arbitrary; it is a consequence of [arbitrage](/capital-flows/). If a cross rate trades at a price inconsistent with the two USD-based rates, a trader can buy one set of pairs, sell the other, and lock in a risk-free profit. The existence of such arbitrage keeps the prices in lockstep.

## The Basic Formula

The **forex cross rate calculation** formula is straightforward. If you have two currency pairs both quoted against the US dollar, you can derive the rate between the two non-dollar currencies by division.

For example, suppose:
- EUR/USD = 1.1050 (one euro buys 1.1050 dollars)
- JPY/USD = 0.0095 (one yen buys 0.0095 dollars, or roughly 105 yen per dollar)

To find EUR/JPY, divide:
- EUR/JPY = EUR/USD ÷ JPY/USD
- EUR/JPY = 1.1050 ÷ 0.0095
- EUR/JPY ≈ 116.32

This means one euro buys roughly 116.32 yen. The logic is intuitive: if one euro buys 1.1050 dollars, and one yen buys 0.0095 dollars, then euros are worth 1.1050 ÷ 0.0095 times as much as yen.

## Reversed Pairs and Quotation Conventions

Currency pairs can be quoted in either direction. If EUR/JPY = 116.32, then JPY/EUR = 1 ÷ 116.32 ≈ 0.0086. Both are correct; the choice depends on convention and which currency is the base (the unit being quoted) and which is the quote currency (what it is worth).

When calculating cross rates, pay attention to the direction. If you have:
- GBP/USD = 1.3000
- USD/CAD = 1.2500 (note: this is quoted with USD as the base)

The cross GBP/CAD is not simply 1.3000 ÷ 1.2500. You must first convert USD/CAD to CAD/USD (flip it: 1 ÷ 1.2500 = 0.8000), then calculate:
- GBP/CAD = GBP/USD ÷ CAD/USD = 1.3000 ÷ 0.8000 = 1.6250

Always ensure both USD-based pairs have the USD in the same position (numerator or denominator) before dividing.

## Triangular Arbitrage and Consistency

The relationship among three currency pairs forms a triangle. If the triangle is in balance, the three rates multiply to 1.0 (or their reciprocals do). If the triangle is out of balance, **triangular arbitrage** becomes possible.

Suppose we have:
- EUR/USD = 1.1050
- USD/JPY = 105.26 (the reciprocal of JPY/USD = 0.0095)
- EUR/JPY = 116.32 (the cross rate calculated above)

The triangle closes if: (EUR/USD) × (USD/JPY) = EUR/JPY
- 1.1050 × 105.26 ≈ 116.32 ✓

If the market quoted EUR/JPY at 115.00 instead, the three rates would not close, and an arbitrageur could exploit the gap:
1. Buy EUR/USD at 1.1050 (spend 1.1050 dollars to get 1 euro).
2. Sell EUR/JPY at 115.00 (receive 115 yen per euro).
3. Sell USD/JPY at 105.26 (sell 105.26 yen per dollar, receiving 1 dollar per 105.26 yen).

The arbitrageur converts the initial dollar outlay through the circle and receives slightly more dollars back, risk-free. This action — buying the underpriced EUR/JPY and selling it through the two USD legs — drives the cross rate up to 116.32.

This arbitrage is instantaneous and automated by trading algorithms. It ensures that cross rates remain consistent with the USD anchors, even though they are rarely quoted by dealers. The market maintains the triangle relationship without explicit quoting.

## Common Cross Rates and Market Convention

While the formula works for any currency pair, some crosses are more liquid and actively quoted than others. The most common include:

| Cross | Typical Use | Drivers |
|-------|-----------|---------|
| EUR/GBP | European trade | ECB vs. Bank of England rate differentials |
| GBP/JPY | Hedge funds, carry trade | High interest-rate differential |
| AUD/NZD | Regional trade | Commodity and regional flows |
| EUR/CHF | Hedging, safe-haven flows | Swiss franc strength in risk-off periods |
| CAD/JPY | Commodity-linked | Oil prices and BOJ policy |

Some crosses, like AUD/NZD, are quoted directly by banks and exchanges because the volume is high enough. Others, like USD/THB (US dollar to Thai baht) with a less liquid non-dollar leg, are calculated on-the-fly from the USD pairs.

## Practical Application for Corporates and Traders

A treasurer at a multinational company with revenue in multiple currencies uses cross rates to manage [currency risk](/currency-risk/) and optimize settlement. If the company receives payment in GBP but has expenses in JPY, the treasurer can either:

1. Convert GBP to USD, then USD to JPY (two transactions, potentially higher fees).
2. Convert GBP to JPY directly using the GBP/JPY cross rate (one transaction, often tighter execution).

The cross rate option is often cheaper if the bank or electronic communication network can provide tight pricing. However, for very illiquid crosses, the effective spread may be wider because the bank quotes it by calculating the two USD legs and marking them up.

Traders also use cross rates for [algorithmic trading](/algorithmic-trading/), [momentum investing](/momentum-investing/), and mean-reversion strategies. A trader who believes EUR/JPY is overvalued relative to its fundamental drivers can buy GBP/JPY and sell EUR/GBP, capturing the misprice if the cross rates converge.

## Central Bank and Peg Dynamics

Some countries peg their currency to a major currency or basket. For example, many Middle Eastern nations peg to the US dollar. Understanding cross rates becomes critical when multiple pegged currencies interact: if the UAE dirham is pegged to the dollar and the Saudi riyal is also pegged to the dollar, the AED/SAR cross rate is mathematically fixed. But if one peg breaks or moves, the cross rate grid shifts, and traders must recalibrate.

Similarly, the [European Central Bank](/european-central-bank/) does not directly quote EUR/JPY, but the rate emerges from the ECB's EUR/USD interventions and the Bank of Japan's JPY/USD operations. Central bank policy levers affect cross rates indirectly through the two USD legs.

## See also

<div class="wiki-seealso">

### Closely related

- [Spot rate](/spot-rate/) — the base exchange rate from which cross rates derive
- Triangular arbitrage — the mechanism keeping cross rates consistent
- [Currency risk](/currency-risk/) — why corporates use cross rates to hedge
- [Bid-ask spread](/bid-ask-spread/) — cross-rate spreads may be wider than USD pairs
- [Carry trade](/carry-trade/) — interest differentials affect cross rate levels

### Wider context

- [Forex mechanics](/forex-value-date-vs-settlement-date/) — broader context on currency markets
- [Algorithmic trading](/algorithmic-trading/) — how systems exploit cross-rate mispricings
- [European Central Bank](/european-central-bank/) — influences EUR-based crosses
- [Bank of Japan](/central-bank/) — influences JPY-based crosses

</div>
