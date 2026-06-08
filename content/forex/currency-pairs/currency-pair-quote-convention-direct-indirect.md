---
title: "Direct vs Indirect Currency Pair Quotes Explained"
description: "How direct and indirect quote conventions reverse the price perspective depending on home currency, and why understanding the difference avoids trading and valuation errors."
keywords:
  - direct vs indirect currency quote
  - direct quote convention
  - indirect quote convention
  - currency pair quotation
  - forex pricing convention
image: /svg/forex.svg
---

*In currency markets, the same exchange rate can be quoted two different ways depending on which currency is domestic. A **direct quote** prices a foreign currency in home-currency terms; an **indirect quote** does the opposite. Confusion between the two causes real errors in valuation, hedging, and trading.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Direct vs Indirect Quotes — key facts</div>

<img src="/svg/forex.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">The distinction hinges on which currency is "home" — the frame of reference for the trader or company.</div>

|   |   |
|---|---|
| **Direct quote** | Units of home currency per one unit of foreign currency (e.g., USD 1.15 per EUR 1) |
| **Indirect quote** | Units of foreign currency per one unit of home currency (e.g., EUR 0.87 per USD 1) |
| **Relationship** | Indirect quote = 1 / Direct quote (they are reciprocals) |
| **Standard usage** | Different by country and convention; U.S. markets often use indirect (USD per unit), others use direct |
| **Risk:** Mixing conventions | Traders can reverse hedge ratios, miscode [forward contracts](/forward-contract/), or misread margin requirements |
| **Key in trading** | Options, [futures](/futures-contract/), and [swaps](/swap/) prices depend heavily on quote convention |

</aside>

## The two conventions defined

### Direct quote (pricing foreign in home terms)

A **direct quote** expresses the price of one unit of a foreign currency in units of home currency. It answers: "How much of my home currency does one unit of foreign currency cost?"

**Example:** A U.S. exporter (home currency = USD) sees a direct quote of **1.15** for the euro. This means 1 EUR costs 1.15 USD. To buy €100, the exporter pays $115.

Direct quotes are common in many countries. The Australian dollar, Canadian dollar, and pound sterling are often quoted directly in their home markets and in Asia.

### Indirect quote (pricing home in foreign terms)

An **indirect quote** expresses the price of one unit of home currency in units of foreign currency. It answers: "How many units of foreign currency does one unit of my home currency buy?"

**Example:** A U.S. exporter sees an indirect quote of **0.87** for the euro. This means 1 USD buys 0.87 EUR. To buy €100, the exporter needs to pay USD 115 (100 / 0.87 ≈ 115).

Indirect quotes are the standard convention in spot foreign exchange markets in the United States. U.S. market data typically quotes non-USD pairs as foreign currency per USD (indirect from the USD perspective).

## The reciprocal relationship

Direct and indirect quotes are mathematical inverses:

$$\text{Indirect Quote} = \frac{1}{\text{Direct Quote}}$$

If the direct quote (USD per EUR) is 1.15, the indirect quote (EUR per USD) is 1 / 1.15 ≈ 0.870.

This means there is no "right" or "wrong" quote — only a convention choice. However, failing to account for which convention is in use can cause critical errors.

## Why the distinction matters in practice

### Currency exposure and hedging

A U.S. company owes €1 million in 30 days. Management must decide whether to hedge using [forward contracts](/forward-contract/) or [options](/option/).

If they receive a forward quote in **direct convention** (1.12 USD/EUR), locking in 1 EUR = 1.12 USD, they know buying €1 million will cost $1.12 million.

If they misread the same quote as **indirect** (1.12 EUR/USD), they might think $1.12 million will buy €1.12 million — off by a factor of 25%, a massive hedging error.

### Valuation of subsidiaries and consolidation

Multinational companies translate foreign subsidiary earnings back to the parent currency at period-end exchange rates. If the consolidation team uses the wrong quote convention, the reported value of earnings and assets shifts meaningfully.

### Option and [futures](/futures-contract/) pricing

Currency [options](/option/) and futures pricing depend critically on the underlying [strike price](/strike-price/) and [spot rate](/spot-rate/) convention. An options trader quoting a 1.10 strike price must clarify: "1.10 USD per EUR (direct) or 1.10 EUR per USD (indirect)?" A mismatch changes the [intrinsic value](/intrinsic-value/) and hedge ratio.

### Bid-ask spread interpretation

In indirect quotation, a wider bid-ask spread appears as a smaller absolute difference but represents the same percentage cost. Comparing liquidity across quote conventions requires normalizing to one framework.

## Market convention by region and pair

Market conventions vary by geography and historical practice:

- **USD pairs in the U.S. spot market:** Indirect (EUR/USD, GBP/USD, etc. quoted as units of foreign currency per 1 USD).
- **Non-USD pairs:** Often direct. EUR/GBP, EUR/AUD, and yen pairs (USD/JPY) are typically quoted so that the more frequently traded pair is in the denominator.
- **Australia, New Zealand, Canada:** AUD/USD, NZD/USD, and CAD/USD are often quoted indirectly (foreign per USD) in global markets, but traders in those countries may think of them directly (home currency per unit of partner currency).
- **Emerging markets:** Conventions vary widely; always clarify with the counterparty or data provider.

The lack of a universal standard is a source of recurring confusion in cross-border deals and trading.

## Worked example: avoiding a mistake

**Scenario:** A German company (EUR home currency) is quoting a price to a U.S. customer (USD home currency) for machinery. The spot rate is 1.15 USD/EUR.

- **Direct quote (EUR perspective):** 1 EUR = 1.15 USD. The German firm prices the machine at €100,000. In USD terms, that is 100,000 × 1.15 = $115,000.
- **Indirect quote (USD perspective):** 1 USD = 0.870 EUR. To find the euro equivalent, the U.S. customer divides $115,000 by 0.870 = €132,184. This is wrong.

The error arises because the USD-side firm applied an indirect quote as if it were direct. The correct inverse is: 1 / 1.15 = 0.870, so $115,000 / 0.870 = $115,000 × (1 / 0.870) = $115,000 × 1.15 (reciprocal) = €100,000. The circular math highlights the pitfall.

To avoid it: decide upfront which convention the rate is in, then apply it consistently. Spot rates should be applied the same way in all downstream calculations (pricing, hedging, consolidation).

## See also

<div class="wiki-seealso">

### Closely related

- Foreign exchange — the global market for currency trading
- [Spot rate](/spot-rate/) — the current exchange rate for immediate settlement
- [Bid-ask spread](/bid-ask-spread/) — the cost of liquidity in FX markets
- [Forward contract](/forward-contract/) — locking in a future exchange rate today
- [Currency risk](/currency-risk/) — exposure to exchange-rate fluctuations
- [Cross rate](/cross-rate/) — exchange rates between pairs not involving a common base currency

### Wider context

- [Leverage ratio forex](/leverage-ratio-forex/) — how FX traders use margin
- [Swap](/swap/) — exchanging cash flows in different currencies
- [Currency volatility](/currency-volatility/) — price fluctuations in FX pairs
- [Central bank](/central-bank/) — policy makers who influence exchange rates through rates and reserves

</div>
