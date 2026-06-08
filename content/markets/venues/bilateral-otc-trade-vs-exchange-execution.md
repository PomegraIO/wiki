---
title: "Bilateral OTC Trade vs Exchange Execution"
description: "A bilateral OTC trade is a privately negotiated deal between two counterparties, contrasting with exchange execution where a central matching engine and clearing house mediate all trades."
keywords:
  - bilateral otc trade
  - otc execution
  - exchange vs otc
  - counterparty negotiation
  - trade settlement
image: /svg/markets.svg
---

*A **bilateral OTC trade** is a privately negotiated transaction between two counterparties without a central matching engine, order book, or clearing intermediary—the buyer and seller directly agree on price, quantity, and terms. This contrasts sharply with [exchange execution](/stock-exchange/), where a centralized venue matches orders and a clearing house interposes itself between all parties to guarantee performance.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Bilateral OTC vs Exchange — key facts</div>

<img src="/svg/markets.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Two distinct market structures with different price discovery, reporting, and credit mechanics.</div>

|   |   |
|---|---|
| **Price discovery** | Bilateral negotiation; no central order book |
| **Clearing agent** | Direct counterparty (credit risk) vs clearing house (guaranteed) |
| **Trade reporting** | Customary for equities, mandatory for swaps ([SEFs](/swap-execution-facility-how-it-works/)) |
| **Settlement** | Direct between parties (T+1, T+2, custom) vs exchange default |
| **Order matching** | Manual/phone negotiation vs automatic matching engine |
| **Typical products** | FX, commodities, bonds, swaps, derivatives |
| **Regulation** | Less stringent; no exchange rulebook |

</aside>

## The bilateral OTC structure

In a bilateral OTC trade, two parties—say, a hedge fund and a commercial bank—telephone or message each other directly and negotiate the terms of a trade. The hedge fund wants to buy 100,000 barrels of crude oil for delivery in three months at a fixed price. The bank's oil trading desk quotes a price, the hedge fund accepts (or counters), and within seconds they have a binding agreement. No order is posted to an order book. No exchange operator is involved. No clearing house interposes itself. The buyer and seller are now directly liable to each other for the contract.

Settlement occurs directly between the two parties according to whatever terms they agreed. If it is a FX trade, the hedge fund and bank settle by delivering the two currencies to each other on the agreed settlement date. If it is a commodity futures trade, they may settle by physical delivery or via a cash-settlement mechanism they have negotiated. There is no standardized settlement timeline, no standardized clearinghouse, and no standardized contract specifications—every deal is bespoke.

This bilateral structure has been the norm for decades in markets like foreign exchange, commodities, and over-the-counter derivatives. A major commercial bank's FX trading desk will execute millions of bilateral OTC trades with clients and other banks each week, with each trade documented separately and settled bilaterally.

## Exchange execution: the alternative model

On an exchange—the NYSE, NASDAQ, [CME](/derivatives-hedging/), or ICE—an order arrives at a central matching engine. The engine compares buy and sell orders by price and time priority, and automatically executes them against each other. Once matched, the exchange's [clearing house](/broker/) (in the US, typically a third party like OCC for options or DTCC for equities) interposes itself and becomes the counterparty to both the buyer and seller.

From the moment the trade is cleared, the buyer's credit risk is no longer with the original seller; it is with the clearing house. The clearing house guarantees performance (it will pay the buyer if the seller fails) because it collects margin from both sides and has the financial resources to cover a default. Settlement happens on a standardized date (T+1 for equities, T+0 or T+1 for many futures) using standardized infrastructure (Fedwire, DTCC, or equivalent).

The exchange operator publishes all trades in real time (or with a brief delay), making the order book and recent trade history visible to all participants. This transparency enables [price discovery](/price-discovery/) and allows new participants to enter the market with confidence that they understand recent prices and available liquidity.

## Price discovery and negotiation

Bilateral OTC trading has no transparent order book. Price discovery occurs through phone calls, dealer quotes, and market talk. If you want to buy a large block of a corporate bond, you call several banks, each quotes a price, you pick the best bid, and you execute. You do not see a central order book showing all bids and offers. This makes bilateral markets less transparent and slower to adjust to new information.

However, bilateral OTC trading also allows for highly customized deals. If you want to buy a 10-year interest rate [swap](/swap/) with a unique structure (unusual reset frequency, bespoke notional schedule, non-standard coupon), you can negotiate it directly with a bank. An exchange cannot accommodate such customization; it only matches standard contracts.

The downside of this opacity is that the pricing of bilateral OTC trades can vary widely depending on counterparty relationships, negotiating skill, and market conditions. One buyer may pay $100.50 per bond while another pays $100.75 for the same bond from different dealers. On an exchange, the price is unified—everyone trades at the same price in the same instant (within the bid-ask spread). This price transparency is one reason institutional traders prefer exchanges when they want to verify they received competitive execution.

## Settlement and counterparty credit risk

In a bilateral OTC trade, the buyer and seller must trust each other to settle. If you buy $10 million of crude oil from a counterparty, you rely on that counterparty to deliver the oil (or cash equivalent) on the agreed date. If the counterparty fails before settlement, you are creditor in its bankruptcy and may recover cents on the dollar.

This is [counterparty risk](/counterparty-risk/). Over decades, many bilateral OTC markets developed extensive credit documentation (ISDA master agreements for derivatives, standard credit-line arrangements for FX) to mitigate the risk. But the risk never fully disappears. During the 2008 financial crisis, the failure of Lehman Brothers left many counterparties with billions in losses on bilateral OTC derivatives trades that Lehman had not yet settled.

Exchange settlement eliminates this risk because the clearing house is the counterparty. If you buy 1,000 shares on the NYSE and the seller goes bankrupt between trade and settlement, the clearing house still delivers the shares to you. You have credit exposure only to the exchange's clearing house, which is heavily capitalized and regulated to maintain sufficient resources for any plausible default.

This credit guarantee has a cost: clearing fees, margin requirements, and regulatory overhead. But institutional traders often accept these costs as worthwhile insurance against counterparty failure.

## Trade reporting and regulatory transparency

Bilateral OTC trades in equities are typically reported to FINRA's Trade Reporting Facilities (TRF) within seconds, allowing the trades to be published to the public via consolidated market data feeds. This preserves some transparency even though the trade was negotiated bilaterally.

However, many bilateral OTC markets (especially commodities, currencies, and older swaps contracts) had no real-time reporting requirement. A bilateral commodities trade might not be reported publicly until days or weeks after execution, or not at all.

This gap prompted regulatory change. The Dodd-Frank Act mandated that standardized swaps be executed on [swap execution facilities](/swap-execution-facility-how-it-works/) (SEFs) and reported to swap data repositories. The goal was to bring post-trade transparency to a major bilateral OTC market that had become systemically risky.

Exchange trades, by contrast, are reported and published in real time by the exchange itself and market data consolidators. There is no ambiguity: every trade is visible moments after execution.

## Customization vs standardization trade-off

Bilateral OTC markets thrive in products where standardization is difficult or unwanted. A multi-leg commodities hedge, a bespoke currency option, or a structured swap—these are negotiated bilaterally because the buyer and seller have unique needs that a standard exchange contract cannot meet.

But this customization comes with a cost. Bilateral markets are less liquid (fewer participants for each specific deal), slower to settle, harder to value, and carry higher counterparty risk. They also tend to have larger bid-ask spreads because dealers bear inventory risk and credit risk for each position.

Exchange markets standardize contracts to maximize liquidity. A [futures contract](/futures-contract/) on crude oil has one specification—a standard notional size, delivery point, and quarterly expiration. Thousands of participants can trade the same contract, leading to deep liquidity, tight spreads, and rapid [price discovery](/price-discovery/). But you cannot customize it; you take what the exchange offers.

Large institutions often operate in both venues. They use exchange markets for liquid, standardized exposures, and negotiate bilateral OTC trades for customized risks they cannot hedge on exchanges.

## See also

<div class="wiki-seealso">

### Closely related

- [Over-the-counter market](/over-the-counter-market/) — OTC structure and regulation
- [Counterparty risk](/counterparty-risk/) — bilateral settlement risk
- [Swap execution facility](/swap-execution-facility-how-it-works/) — exchange-like platform for swaps
- [Midpoint order book venue](/midpoint-order-book-venue/) — alternative trading system for equities
- [Stock exchange](/stock-exchange/) — centralized matching and clearing

### Wider context

- [Clearing house](/broker/) — how exchange settlement works
- [Price discovery](/price-discovery/) — order book vs bilateral pricing
- [Futures contract](/futures-contract/) — standardized exchange products
- [Derivatives hedging](/derivatives-hedging/) — OTC vs exchange hedging

</div>
