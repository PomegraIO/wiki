---
title: "FX Roll Forward"
description: "Renewing a forward contract to extend its maturity date without closing the original position."
keywords:
  - fx forward renewal
  - contract maturity extension
  - currency hedging extension
  - forward roll mechanics
---

*An **FX roll forward** is the process of closing an expiring currency forward contract and simultaneously entering a new forward contract at a later date, effectively extending a hedging position without physical settlement. Rather than taking delivery or making delivery of the foreign currency at the original maturity, the trader rolls the position into the future.*

<aside class="wiki-infobox">

| Aspect | Detail |
|--------|--------|
| **Purpose** | Extend currency hedge beyond original maturity |
| **Mechanics** | Close original forward, open new forward simultaneously |
| **Cost driver** | Interest rate differential (carry cost) |
| **Common in** | Corporate hedging, fund rebalancing |
| **Market participants** | Corporations, hedge funds, central banks |
| **Timing** | Usually days or weeks before original maturity |

</aside>

## Why forward contracts need rolling

A [forward contract](/wiki/forward-contract/) locks in an exchange rate for a specific settlement date—typically 30, 60, or 180 days out. When that date approaches and a company's underlying exposure (payables, receivables, or investment position) remains unhedged, the treasurer faces a choice: settle the contract, or extend the hedge into the future. Rolling forward avoids the disruption of unwinding and re-hedging at potentially worse prices.

## The mechanics of a roll

Rolling a forward is executed as a simultaneous two-leg transaction. First, the bank or trader [closes the original forward](/wiki/forward-contract/) by entering an offsetting contract at the original maturity date. This crystallizes any gain or loss. Simultaneously, a new forward contract is initiated at the desired new maturity date. From the trader's perspective, this looks like one seamless continuation rather than a liquidation-and-restart.

The spread between the original [forward rate](/wiki/forward-exchange-rate/) and the new forward rate captures the cost of extending the hedge. Because interest rates differ between currencies (the [interest rate parity](/wiki/interest-rate-parity/) principle), a [currency pair](/wiki/currency-pair/) may have positive or negative [carry](/wiki/carry-trade/). A trader extending a position in a high-carrying pair (e.g., USD/JPY, where US rates exceed Japanese rates) usually pays a cost; rolling into a negative-carry pair generates a credit.

## Operational advantages

Rolling avoids the need for actual delivery of cash or collateral at the original maturity date. For a company managing a large [hedging portfolio](/wiki/currency-hedging/), settling ten contracts and re-hedging ten new ones creates operational friction, resets credit lines, and exposes the trader to gap risk if settlement and re-trading don't align. A roll executes both legs in a single transaction, often with a single pricing quote from the counterparty.

Corporate treasurers frequently roll forwards to match the payable or receivable they are hedging. If a contract for a foreign subsidiary's three-month earnings is due in 60 days, but the earnings won't be received for 90 days, a roll ensures continuous protection without a 30-day unhedged window.

## Cost: the roll spread

The cost of rolling is the difference in [forward points](/wiki/fx-points-spread/) between the old maturity and the new one. Most banks quote a single all-in spread: the ask price at which they will buy back the old forward and sell the new one. On a bid-ask basis, both legs embed the bank's [bid-ask spread](/wiki/bid-ask-spread-forex/), so the total roll cost is typically 2–4 pips on major pairs.

For large corporate positions, the roll spread is negotiable and often depends on relationship, volume, and tenor. High-frequency traders and hedge funds may pay tighter spreads; retail or infrequent customers accept wider ones. The roll spread is separate from the interest rate differential (carry); they compound but are usually quoted as one composite figure.

## When rolling makes sense versus alternative strategies

Traders and treasurers weigh rolling against other approaches. **Outright settlement and re-hedge** is simpler if rates have moved sharply and the trader wants to capture gains or adjust the [hedge ratio](/wiki/currency-hedging/). **Rolling into a longer tenor** (e.g., from 3 months out to 6 months) keeps the position in place longer but locks in carry costs. **Using a [currency option](/wiki/currency-option/)** instead avoids the forced re-trade at maturity but costs premium upfront.

Rolling is most economical for traders who are confident their hedging horizon is stable and who face modest roll spreads due to size or relationship strength. A multinational corporation rolling a position every quarter, year after year, typically views the roll spread as a small operational cost against the benefit of uninterrupted hedging.

## Roll mechanics at different tenors

Banks typically offer rolling windows for forwards ranging from 1 month to 5 years, with the narrowest spreads on [major currency pairs](/wiki/major-currency-pair/) (EUR/USD, GBP/USD, USD/JPY) and tenors out to 2 years. Rolling a 6-month forward into another 6-month forward is routine; rolling out to 10 years or into illiquid pairs requires a wider spread and sometimes manual pricing.

Emerging-market currency forwards are harder to roll beyond 1–2 years due to thinner markets and higher funding costs. A company with long-dated exposure in a [commodity currency](/wiki/commodity-currency-pairs/) (AUD, CAD, BRL) may find rolling economical only in shorter tranches, then accepting re-trade risk or opting for [options](/wiki/currency-option/) to cap but not fix the rate.

<div class="wiki-seealso">

### Closely related
- [Forward Exchange Rate](/wiki/forward-exchange-rate/) — the price of a forward contract, reflecting interest rate parity and market conditions
- [Interest Rate Parity](/wiki/interest-rate-parity/) — principle explaining why forward rates differ from spot by the interest rate differential
- [Currency Hedging](/wiki/currency-hedging/) — strategies to protect against foreign exchange risk
- [Carry Trade](/wiki/carry-trade/) — strategy that profits from interest rate differentials between currencies
- [Forward Contract](/wiki/forward-contract/) — the base instrument being rolled

### Wider context
- [FX Swap](/wiki/fx-swap/) — alternative instrument combining spot and forward in a single trade, often used for shorter-term rolls
- [Basis Risk](/wiki/basis-risk/) — the gap between a hedge and the underlying exposure, relevant when rolling timings drift
- [Foreign Exchange Risk](/wiki/currency-risk/) — the exposure that rolling is designed to manage
- [Currency Option](/wiki/currency-option/) — alternative hedging instrument with optionality instead of obligation

</div>
