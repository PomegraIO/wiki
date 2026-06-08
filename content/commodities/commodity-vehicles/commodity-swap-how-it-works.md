---
title: "How a Commodity Swap Works"
description: "Commodity swap mechanics explained: over-the-counter pricing contracts where parties exchange fixed commodity prices for floating prices, settlement, and uses."
keywords:
  - how commodity swap works
  - commodity price swap structure
  - commodity swap settlement
  - over-the-counter commodity contract
image: /svg/commodities.svg
---

*A **commodity swap** is an over-the-counter contract in which two parties agree to exchange cash flows tied to commodity prices. One party pays a fixed price per barrel (or ton, or bushel) while the other pays the market (floating) price, settled monthly or quarterly over years. Unlike exchange-traded [futures contracts](/futures-contract/) or [ETFs](/etf/), commodity swaps are privately negotiated, customized for term and volume, and enable hedging or speculation without the leverage, margin calls, and daily settlement of futures. Oil producers use them to lock in revenue; refiners use them to cap costs; traders use them to exploit price forecasts—all without posting collateral against daily mark-to-market moves.*

<div class="wiki-hatnote">

Not to be confused with [interest-rate swaps](/interest-rate-swap/) (which exchange interest payments) or equity swaps (which exchange stock returns). Commodity swaps are price-based, not rate-based.

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Commodity Swap — key facts</div>

<img src="/svg/commodities.svg" alt="An abstract editorial mark for commodities." />

<div class="wiki-infobox-caption">Bespoke OTC contract allowing hedging or speculation on commodity prices without leverage or daily margin calls.</div>

|   |   |
|---|---|
| **Structure** | Fixed price leg exchanged for floating (market) price leg on notional commodity volume |
| **Settlement** | Cash payments only (no physical delivery); typically monthly or quarterly |
| **Term** | Months to years; customizable (unlike standardized futures) |
| **Counterparties** | Producers, refiners, traders, institutional investors; arranged via dealers |
| **No daily mark-to-market** | Unlike futures, no daily settlement or margin calls; credit risk is bilateral |
| **Pricing** | Fixed leg set at initiation; floating leg referenced to published index (WTI, Brent, etc.) |
| **Use case** | Hedging revenue or costs; speculation without leverage; multi-year planning |

</aside>

## The Mechanics: Fixed vs. Floating

A commodity swap is conceptually simple: Party A and Party B agree on a notional quantity (say, 10,000 barrels of crude oil) and a period (24 months). Each month, they calculate cash flows based on two prices:

1. **Fixed leg:** $70 per barrel (locked in at swap initiation).
2. **Floating leg:** The current market price (say, WTI closing price for that month).

If oil closes the month at $75, the party paying floating owes the party receiving floating $50,000 that month (5 dollars per barrel × 10,000 barrels). If oil falls to $60, the party paying floating receives $100,000 (the fixed receiver now pays the floating payer).

No physical oil changes hands. Only net cash moves. The swap dealer (typically an investment bank) facilitates the trade and may take the other side of one party's position, hedging the risk in futures or with another counterparty.

## Fixed-for-Floating vs. Other Structures

The classic fixed-for-floating commodity swap is most common, but variations exist:

**Floating-for-floating:** Both legs reference different price indexes. An airline might swap jet-fuel prices (volatile, volatile) for heating-oil prices (less volatile but correlated) to smooth fuel budgets. Less common than fixed-for-floating because the economics are more complex.

**Option-embedded:** A swap with a collar (e.g., fixed at $70 but floating capped at $80 and floored at $60) adds asymmetry. Used when one party wants partial protection but accepts some downside/upside.

**Quantity-contingent:** The notional volume varies based on production or sales. A mine might swap copper output, but the volume swaps only to the extent copper is actually produced, protecting against production shortfalls.

## Why Not Futures or ETFs?

Commodity swaps, [futures](/futures-contract/), and [commodity ETFs](/commodity-etf/) all expose you to price moves, but they serve different needs.

**Futures** are exchange-traded, standardized (fixed contract size, expiry dates), and subject to daily mark-to-market settlement. A trader holding a long crude futures contract sees daily gains or losses in their account; a $5 price move on a 1,000-barrel contract is an immediate $5,000 liability or credit. This requires daily monitoring and cash management. Futures also offer leverage—you can control 1,000 barrels with far less than 1,000 barrels' worth of capital deposited. That amplifies both gains and losses.

**ETFs** hold physical commodities or commodity futures. They're liquid, tradeable, and require no credit vetting, but they charge annual expense ratios (often 0.5–1.5%), incur tax-inefficient rebalancing, and may not precisely track spot prices due to contango or backwardation.

**Commodity swaps** are customized, with no daily settlement (reducing cash-flow stress), no leverage (you pay the notional amount only at the end, and only if you've lost), and terms tailored to your hedging horizon. A producer with 50,000 barrels to sell over the next two years can use a swap covering exactly that volume and timeline, rather than rolling standardized futures contracts monthly. The tradeoff: swaps are illiquid (harder to exit early) and carry [counterparty risk](/counterparty-risk/) (the dealer must be creditworthy; if the dealer fails, you may not recover your position).

## Real-World Example: An Oil Producer's Hedge

A mid-sized oil producer expects to extract 50,000 barrels over the next year. Current WTI price: $65/barrel. Projected revenue: $3.25 million. But the CFO is worried: if oil falls to $55, revenue drops to $2.75 million—a $500,000 shortfall that strains cash flow and debt covenants.

The producer enters a 1-year commodity swap with a dealer: fixed price $63/barrel, notional 50,000 barrels. If oil falls to $55, the producer still receives $63 per barrel from the swap dealer (a net gain of $8 per barrel versus market = $400,000), offsetting the lower market revenue. If oil rallies to $75, the producer pays the dealer $12 per barrel ($600,000 net loss), but also receives $75 from sales—locking in $63 economics. Revenue is now predictable at $3.15 million (50,000 barrels × $63), allowing confident debt service and capex planning.

The swap costs nothing upfront (unlike buying a call option). The dealer profit comes from the bid-ask spread: they might offer the producer $63 and simultaneously swap with a financial counterparty (or another producer) at $63.05, pocketing $2,500 annually.

## Pricing: Why the Fixed Price Is Fair

When a swap initiates, the fixed price is set so the swap has zero net present value. The dealer prices the fixed leg to equal the expected present value of future floating-price cash flows, using forward curves (the market's consensus on future prices) and credit risk adjustments.

If the forward curve for oil is $60 next year and $58 in year two, a two-year swap might fix at $59 (a blended forward rate adjusted for the dealer's credit costs). The producer locks in $59; the dealer has hedged with futures or other offsetting swaps. If oil prices then rally unexpectedly, the producer has foregone upside—but that's the cost of certainty.

## Settlement and Cash Flow Risk

Swaps are settled purely in cash, not physical delivery. Each settlement period (often monthly), the parties compute the difference between the fixed and floating rates and pay net. If the producer has locked at $63 and spot is $75, the producer owes the dealer $12 per barrel × 50,000 = $600,000 (a monthly cash outflow). This can strain working capital if prices move sharply against you.

This is why counterparty credit is critical. A large oil company swapping with an investment bank has little credit worry; the bank is rated and regulated. But if a smaller company or marginal producer engages a weaker dealer, and that dealer becomes insolvent, the producer might not recover their position, leaving them exposed to the market price they had intended to hedge.

## Exiting a Swap Early

Commodity swaps are illiquid—there's no central market to sell your position. If a producer enters a 5-year swap but needs to exit after two years, they must either:

1. **Find a dealer to unwind:** The dealer quotes a buy-back price reflecting current market conditions and remaining term. If prices have risen since initiation, the producer has a paper gain and will receive cash. If prices have fallen, the producer has a loss and will pay.

2. **Enter an offsetting swap:** Take the opposite position with another counterparty, effectively locking in a loss or gain while maintaining the original hedge.

3. **Hold to maturity:** Accept the lock-in and let the swap settle fully.

Unwinding costs (dealer spreads) can be significant, so swaps are best suited to entities with committed long-term price exposure.

## Distinction from Exchange-Traded Futures

| Aspect | Commodity Swap | Futures Contract |
|--------|---|---|
| **Marketplace** | Over-the-counter, bilateral | Standardized exchange (NYMEX, ICE, etc.) |
| **Contract size** | Customizable (1,000 bbl, 500 oz, etc.) | Fixed (e.g., 1,000 bbl per contract) |
| **Expiry** | Any date; typically years | Specific monthly expirations |
| **Pricing** | Fixed at initiation; floating leg references index | Daily mark-to-market; settled via clearinghouse |
| **Daily settlement** | No; cash flows at intervals (monthly/quarterly) | Yes; margin account adjusted daily |
| **Leverage** | None (notional amount owed only if loss occurs) | Yes (control large quantity with small deposit) |
| **Credit risk** | Bilateral (depends on dealer quality) | Cleared by exchange; minimal counterparty risk |
| **Liquidity** | Illiquid (hard to exit early) | Highly liquid (can sell anytime market is open) |
| **Use** | Hedging, long-term planning, avoiding margin calls | Speculation, short-term trading, leverage |

## Who Uses Commodity Swaps

**Producers (oil, gas, metals):** Lock in revenue to fund operations and debt service.

**End-users (refineries, utilities, manufacturers):** Cap input costs for multi-year business plans.

**Traders and hedge funds:** Speculate on price moves without posting daily margin or managing leverage.

**Governments and development banks:** Hedge commodity-dependent economies' export revenue.

**Corporates with commodity exposure:** Airlines hedging fuel, chocolate makers hedging cocoa, utilities hedging natural gas input costs.

## See also

<div class="wiki-seealso">

### Closely related

- [Futures Contract](/futures-contract/) — standardized exchange alternative with daily settlement and leverage
- [Interest Rate Swap](/interest-rate-swap/) — structural parallel but for interest rates, not commodity prices
- [Commodity ETF](/commodity-etf/) — passive, tradeable commodity exposure without customization
- [Forward Contract](/forward-contract/) — bilateral, over-the-counter commodity price agreement; similar to a swap but single-settlement
- Hedging — the broader strategy of reducing price risk via derivatives

### Wider context

- [Derivatives Hedging](/derivatives-hedging/) — how swaps fit into corporate risk management
- [Counterparty Risk](/counterparty-risk/) — credit exposure inherent in OTC swaps
- [Contango](/contango/) — why forward prices exceed spot; affects swap pricing
- Commodity Price Volatility — the underlying driver of hedging demand
- [Price Discovery](/price-discovery/) — how markets establish fair value for floating-leg settlement

</div>
