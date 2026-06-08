---
title: "How to Calculate the True Transaction Cost of a Currency Pair"
description: "Calculate forex transaction costs by converting bid–ask spreads to pips, adding commissions, and including holding costs like rollover swaps for multi-day positions."
keywords:
  - forex transaction cost calculation
  - bid ask spread currency pairs
  - round trip cost calculation
  - pip cost fx trading
  - swap cost currency
image: "/svg/forex.svg"
---

*Calculating the true **forex transaction cost** of a [currency pair](/stock-exchange/) requires more than just looking at the quoted [bid-ask spread](/bid-ask-spread/). You must convert the spread to pips and basis points, add any commission or markup, factor in any [swap](/interest-rate-swap/) cost if you hold the position, and compute the round-trip cost to close the trade. A systematic approach reveals whether a trade's potential profit can cover these costs.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Transaction Cost Calculation — key steps</div>

<img src="/svg/forex.svg" alt="An abstract editorial mark for forex pairs." />

<div class="wiki-infobox-caption">Spreads, commissions, and swaps reduce your net return; quantify them before you trade.</div>

|   |   |
|---|---|
| **Spread cost** | (Ask − Bid) ÷ 2 × (units traded) |
| **Commission** | Typically 0–5 pips per round trip (broker-dependent) |
| **Swap cost** | Daily interest differential (%) × position size ÷ 360 |
| **Total round-trip** | Entry spread + exit spread + commission + swap cost |
| **Breakeven move** | Total cost ÷ position size in pips |
| **Key rule** | Spreads are always quoted in the pair's smallest unit |

</aside>

## Understanding the Bid-Ask Spread

The [bid-ask spread](/bid-ask-spread/) is the difference between the price a [broker](/broker/) is willing to buy from you (the bid) and the price at which it is willing to sell to you (the ask). It is always quoted in the pair's smallest unit, which is usually 1 pip (1/10,000 of a dollar, or 0.0001) for major pairs, and 1/100 of a pip (0.00001) for micro-pip spreads.

For example, a typical EUR/USD quote might be:

| Bid | Ask |
|---|---|
| 1.0850 | 1.0852 |

The spread is 1.0852 − 1.0850 = 0.0002, or 2 pips.

This 2-pip spread is the cost you pay the moment you enter a trade. When you sell EUR/USD, the broker buys from you at 1.0850 (you get the bid). When you buy EUR/USD, the broker sells to you at 1.0852 (you pay the ask). The 2 pips you lose on entry are the broker's compensation for providing liquidity and taking counterparty risk.

## Converting Spread to Currency Units

To understand the spread in actual currency cost, multiply the spread (in decimal form) by your position size.

**Example: EUR/USD with a 2-pip spread, 100,000-unit trade**

- Spread in decimal: 0.0002
- Position size: 100,000 EUR
- Cost in USD: 0.0002 × 100,000 = **20 USD**

You lose 20 USD the moment the trade opens, simply because you bought at the ask instead of the bid. This is unavoidable—[market makers](/market-maker-trading/) must profit somehow.

For pairs where the USD is the counter-currency (e.g., EUR/USD), the spread cost is paid in USD. For pairs where another currency is the counter (e.g., EUR/GBP), you calculate the cost in the counter-currency.

## Adding Commission

Many retail brokers charge no commission and make their money purely on the [bid-ask spread](/bid-ask-spread/). However, some brokers (especially those targeting professionals) charge an explicit commission per trade.

Commission is typically quoted in pips or as a percentage of the notional trade size. If a broker charges 1 pip of commission per round trip, that means:

- 0.5 pips on entry
- 0.5 pips on exit

**Example: 100,000 units with 1-pip round-trip commission**

- Commission cost in pips: 1
- Commission cost in currency: 0.0001 × 100,000 = **10 USD**

If the broker's spread is 2 pips and commission is 1 pip, your true all-in cost is 3 pips (2 + 1), or 30 USD on a 100,000-unit trade.

## Calculating Swap (Overnight Holding) Cost

If you hold a currency position overnight, you pay or receive a daily [swap](/interest-rate-swap/) fee based on the interest-rate differential between the two currencies. This is because you are essentially borrowing one currency and lending another.

The swap is calculated as:

**Daily swap = (interest differential in %) × position size ÷ 360**

Where interest differential = (counter-currency rate − base-currency rate) as an annual percentage.

**Example: holding 100,000 EUR/USD for 1 day**

- EUR 1-year deposit rate: 3.75%
- USD 1-year deposit rate: 5.25%
- Differential: 5.25% − 3.75% = 1.50%
- Daily swap = 1.50% × 100,000 ÷ 360 = **41.67 USD** (debit)

Since the USD rate is higher, you pay 41.67 USD per day to hold EUR/USD overnight. If you held the position for 5 days, the total swap cost would be about 208 USD. Some brokers add a markup or charge a separate overnight fee on top of the interest differential.

Swap is not negotiable and varies with market rates. If you close the position intraday, you pay zero swap. If you hold for weeks or months, swap becomes a material cost.

## Working Example: Full Round-Trip Cost

Suppose you trade 100,000 EUR/USD as a swing trade:

| Component | Value |
|---|---|
| Entry spread | 2 pips = 20 USD |
| Commission (round-trip) | 1 pip = 10 USD |
| Exit spread | 2 pips = 20 USD |
| Swap (2-day hold) | 41.67 USD/day × 2 = 83.34 USD |
| **Total cost** | **133.34 USD** |

For a 100,000-unit trade, this is roughly 3.3 pips of all-in cost. If your price target was a 10-pip move in your favor, you would need that 10-pip move just to break even after costs. Your actual profit margin is only 6.7 pips.

## Calculating Breakeven Move

To know whether a trade is worth taking, calculate the breakeven move: the number of pips the price must move in your favor just to cover all costs.

**Breakeven pips = total cost ÷ position size (in pips)**

**Example (continuing above):** 

- Total cost: 133.34 USD
- Position size: 100,000 EUR
- Cost per pip: 0.01 × 100,000 = 1,000 USD per pip (this is standard for a 100,000-unit euro lot)

Wait—we need to convert 133.34 USD back to pips. On EUR/USD:

- 1 pip = 0.0001 EUR, which costs 0.0001 × 100,000 × current rate in USD ≈ 10 USD (at a 1.10 rate, exactly 11 USD)

So the breakeven is 133.34 USD ÷ 10–11 USD per pip ≈ **12–13 pips**.

For a 2-day swing trade, needing the price to move 13 pips in your favor is steep—that's a 1.2% move on EUR/USD. If you only expect a 5-pip move, the trade is not worth the risk-reward.

## Comparing Brokers and Market Conditions

Spreads vary dramatically by broker, market condition, and pair liquidity:

- **Tight spreads**: Major pairs (EUR/USD, GBP/USD) in peak liquidity hours often have spreads of 0.5–1.5 pips
- **Wide spreads**: Exotic pairs or during low-liquidity hours might have 5–20 pip spreads
- **Markup during volatility**: When market volatility spikes (central bank announcements, geopolitical shocks), brokers widen spreads to 3–5 pips or more

Before committing to a strategy, compare the spread cost across 2–3 brokers at different times of day. A 0.5-pip improvement in spread saves 50 USD on every 100,000-unit trade—significant over hundreds of trades.

## See also

<div class="wiki-seealso">

### Closely related

- [Bid-Ask Spread](/bid-ask-spread/) — the cost of market liquidity
- [Interest Rate Swap](/interest-rate-swap/) — mechanics of overnight holding costs
- [USD/SGD: The Dollar–Singapore Dollar Pair](/usd-sgd-dollar-singapore-pair/) — example of a tight-spread pair
- [Broker](/broker/) — selecting a trading platform
- [Market Maker Trading](/market-maker-trading/) — who profits from spreads
- [Pip](/pip/) — the smallest unit of currency-pair movement

### Wider context

- [Currency Pair](/stock-exchange/) — pair structure and conventions
- [Forward Contract](/forward-contract/) — locking in rates without daily spread hits
- [Currency Risk](/currency-risk/) — why traders hedge and incur costs
- [Forex Trading](/stock-exchange/) — market structure and participants

</div>
