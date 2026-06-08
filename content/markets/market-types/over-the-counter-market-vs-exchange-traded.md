---
title: "OTC Market vs Exchange-Traded Market: Core Differences"
description: "Compare OTC market vs exchange-traded market on counterparty risk, transparency, standardization, and regulation. Learn when bilateral trading is used."
keywords:
  - otc market vs exchange traded market
  - over-the-counter vs exchange-traded differences
  - counterparty risk centralized clearing
  - opaque bilateral trading vs transparent exchange
  - otc derivatives vs listed derivatives
image: /svg/markets.svg
---

*The **OTC market** is a decentralized, bilateral negotiation between two parties with no central exchange; the **exchange-traded market** is a centralized venue with standardized contracts, continuous prices, and a clearinghouse. OTC trades carry [counterparty risk](/counterparty-risk/), offer bespoke terms, and remain opaque; exchange trades are transparent, [marked to market](/fair-value/) continuously, and settled through an intermediary. Each has trade-offs in cost, flexibility, and safety.*

<div class="wiki-hatnote">

This article covers equity, bond, and derivative markets. Specific regulatory treatment varies by asset class (stocks, [bonds](/bond/), commodities, foreign exchange) and jurisdiction.

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">OTC vs Exchange-Traded — Structure and Risk</div>

<img src="/svg/markets.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Decentralized bilateral trading carries hidden risk; centralized exchange trading transfers it to a clearinghouse.</div>

|   |   |
|---|---|
| **Counterparty risk** | OTC: direct exposure to the other party's solvency; Exchange: cleared through a clearinghouse |
| **Pricing transparency** | OTC: prices are private and known only to the two parties; Exchange: all prices are broadcast in real-time |
| **Contract standardization** | OTC: bespoke terms negotiated per deal; Exchange: contracts are standardized by the exchange |
| **Default mechanism** | OTC: bilateral agreement on remedies (litigation or negotiation); Exchange: clearinghouse steps in, liquidates, and absorbs losses within limits |
| **Volume and liquidity** | OTC: lower volume, wider [bid-ask spreads](/bid-ask-spread/); Exchange: high volume, tight spreads, immediate execution |
| **Regulatory oversight** | OTC: light touch, dealer self-regulation; Exchange: SEC, CFTC, exchange-imposed rules |

</aside>

## What OTC Markets Are

An **OTC market** is a network of bilateral negotiations between two parties, usually facilitated by a broker or dealer. There is no central exchange, no posted prices visible to the public, and no clearinghouse standing between buyer and seller. Each trade is a contract between two specific entities.

OTC markets operate in many asset classes:

- **Equities**: Before the [stock exchange](/stock-exchange/) era, all stocks were OTC. Today, smaller or foreign stocks, pink sheets, and bulletin-board securities trade OTC through dealers and brokers.
- **Bonds**: The vast majority of corporate and government [bonds](/bond/) trade OTC. A buyer calls a dealer, the dealer quotes a price for a specific bond, and they negotiate the trade.
- **Foreign exchange**: [Currency](/currency-risk/) trading (dollars, yen, euros) is almost entirely OTC, conducted through banks and forex dealers in a decentralized global network.
- **[Derivatives](/derivatives-hedging/)**: [Options](/option/), [swaps](/swap/), and [forward contracts](/forward-contract/) began as purely OTC instruments, negotiated between two counterparties with custom terms.

In OTC markets, a dealer typically holds inventory. A buyer approaches the dealer, the dealer quotes a price to sell from that inventory, and the buyer accepts or declines. No other buyers see that quote; it is private.

## What Exchange-Traded Markets Are

An **exchange-traded market** is a centralized venue where a clearinghouse mediates all trades. Buyers and sellers do not transact directly with each other; instead, they trade contracts via the exchange, and the clearinghouse becomes the counterparty to both sides.

Major examples:

- **[Stock exchanges](/stock-exchange/)**: [NYSE](/new-york-stock-exchange/), [NASDAQ](/nasdaq/), [LSE](/london-stock-exchange/) list equities with continuous, transparent pricing.
- **Futures and options exchanges**: [CME](/futures-contract/), [ICE](/futures-contract/), [CBOE](/option/) handle [futures contracts](/futures-contract/) and [options](/option/) on commodities, indices, and rates.
- **Bond exchanges**: Some government [bonds](/bond/) (U.S. Treasuries, Gilts) trade on exchanges; most corporate bonds remain OTC.

On an exchange, all orders flow into a central **order book**. Buyers submit bids at various prices; sellers submit offers. When a bid and offer match, a trade executes at that price, and the clearinghouse becomes the buyer to the seller and the seller to the buyer. Prices are transparent and updated continuously.

## Counterparty Risk: The Critical Difference

The most important operational difference is **counterparty risk**.

In an **OTC trade**, you owe the other party or they owe you. If the other party fails to pay or deliver, you have an unsecured claim against their bankruptcy estate — you may recover cents on the dollar, or nothing. This is why OTC trading demands credit-worthiness screening, collateral agreements ([CSA](/credit-default-swap/) — Credit Support Annex), and ongoing monitoring.

During the 2008 financial crisis, this risk became catastrophic. **Lehman Brothers**, a major OTC derivatives dealer, failed and left counterparties holding unsecured claims worth tens of billions. **AIG**, another dealer, faced collapse because counterparties demanded immediate cash collateral to offset mark-to-market losses on [swaps](/swap/) and other [derivatives](/derivatives-hedging/).

In an **exchange-traded market**, the clearinghouse steps in. If a buyer defaults, the clearinghouse buys back the position at market price, using the defaulter's collateral (variation margin) to cover the loss. The clearinghouse is typically capitalized with a large insurance fund and access to emergency credit lines, insulating the other party from counterparty failure.

This clearinghouse guarantee carries a cost: trading fees, clearing fees, and margin requirements. But it transfers default risk to a well-capitalized, regulated entity rather than leaving it bilateral.

## Transparency and Price Discovery

**OTC markets lack price transparency.** When two dealers negotiate a bond trade or forex transaction, the price is known only to them. A buyer next door may be offered a very different price by another dealer, depending on their creditworthiness or negotiating power. Large institutional buyers pay less than small ones for the same asset.

This opacity can hide [market manipulation](/market-timing/) and allows dealers to earn wider margins. A dealer that buys a bond at 99.50 and sells it at 100.00 may never publicly disclose either transaction; the spread disappears into the dealer's profit.

**Exchange-traded markets are transparent.** Every bid, every offer, and every executed trade is broadcast to the market within seconds. This forces [price discovery](/price-discovery/) — the market collectively discovers the fair value of an asset because thousands of buyers and sellers submit competing bids and offers. The best bid and best offer are always visible.

Transparency also prevents large hidden positions. A dealer who accumulates a large short position on an exchange must disclose it if they exceed reporting thresholds; on the OTC market, the position can be hidden.

## Standardization vs Customization

**OTC contracts are bespoke.** A corporate bond might have unusual call provisions, step-up coupons, or conversion features tailored to the issuer's needs. A [swap](/swap/) might specify an unusual reset frequency, non-standard notional, or embedded options. This flexibility allows sophisticated structures but increases complexity and operational risk (settlements can fail if one party interprets the contract differently).

**Exchange-traded contracts are standardized.** An exchange specifies the exact contract specifications: size, settlement method, delivery location, margin requirements. A [futures contract](/futures-contract/) on corn is identical whether you buy from the floor or online. This standardization reduces confusion and makes fungibility possible — one buyer's long position can be offset by any seller's short position because the contracts are identical.

Standardization also enables [marked-to-market accounting](/fair-value/). Because contracts are identical and continuously traded, an accurate market price exists at the end of each day. An exchange-traded [option](/option/) position is valued using the closing [settlement price](/spot-rate/); an OTC option must be valued using a [model](/black-scholes-model/) or a dealer quote, both of which carry subjectivity.

## Liquidity and Trading Costs

**OTC markets are less liquid.** If you want to unwind a large OTC position quickly, you must find a dealer willing to buy, and you will likely pay a wide spread. For some assets (e.g., corporate bonds or bespoke [swaps](/swap/)), there may be few dealers willing to quote, and execution can take hours or days.

**Exchange-traded markets are highly liquid.** Thousands of buyers and sellers are continuously trading the same contract. A large position can often be liquidated instantly at the best bid or offer, sometimes with no movement in price (if the daily volume is large enough).

Liquidity translates to cost. An OTC bond trade might have a [bid-ask spread](/bid-ask-spread/) of 0.5 to 2 points (percentage terms), reflecting the dealer's hedging costs and profit margin. An exchange-traded [stock](/stock/) ETF might have a spread of 0.01 points or less because the bid-ask is set by competing market makers and the market is very deep.

## Regulatory Treatment

**OTC markets** are lightly regulated. Dealers must register with the [SEC](/securities-and-exchange-commission/) or [CFTC](/futures-contract/) (depending on asset class) and follow broad rules on advertising and conflicts of interest. However, OTC dealers have wide latitude in how they price, who they trade with, and what collateral they demand. The [Dodd-Frank Act](/dodd-frank-act/) imposed some post-trade reporting and clearing requirements for standardized [derivatives](/derivatives-hedging/), but many OTC derivatives still avoid clearing.

**Exchange-traded markets** are tightly regulated. Exchanges are self-regulatory organizations (SROs) subject to SEC or CFTC oversight. Every rule change, every listing, every margin requirement is subject to approval. Price limits, trading halts, and circuit breakers are prescribed. This reduces operational risk and manipulation but reduces flexibility.

## When OTC Trading Is Used

Certain transactions favor OTC because of customization, scale, or regulatory advantage:

- **Large institutional positions**: A pension fund wanting to purchase a large block of a specific bond will negotiate OTC rather than accept the market price on an exchange (which might move against them during execution).
- **Bespoke structures**: A [swap](/swap/) with a custom tenor, currency pair, or embedded option cannot be replicated on an exchange; it must be negotiated OTC with a dealer.
- **Illiquid assets**: Emerging-market bonds, fine art, or private equity stakes trade OTC because there is no exchange for them.
- **Credit-based trading**: A party with strong credit wants to exploit that advantage; an OTC dealer may offer better terms to a AAA-rated counterparty than to a speculative-grade one.

## The Post-2008 Shift

Before 2008, [derivatives](/derivatives-hedging/) markets were dominated by OTC trading. After the crisis, regulatory changes mandated central clearing for standardized derivatives. Interest-rate [swaps](/swap/), [credit default swaps](/credit-default-swap/), and [futures](/futures-contract/) are now routinely cleared through clearinghouses. This has reduced counterparty risk in the financial system but increased clearing costs.

OTC trading persists for non-standardized derivatives, foreign exchange, and less-regulated assets. The choice between OTC and exchange-traded reflects a trade-off: OTC offers customization and optionality at the cost of counterparty risk; exchange-traded offers safety and transparency at the cost of standardization and scale constraints.

## See also

<div class="wiki-seealso">

### Closely related

- [Counterparty risk](/counterparty-risk/) — credit exposure when trading with a bilateral counterparty
- [Bid-ask spread](/bid-ask-spread/) — how trading costs differ between liquid and illiquid markets
- [Marked-to-market](/fair-value/) — daily valuation of exchange-traded vs. OTC positions
- [Clearinghouse and central clearing](/securities-and-exchange-commission/) — how exchanges isolate counterparty risk
- [Swap](/swap/) — most common OTC derivative and how clearing is changing the market
- [Futures contract](/futures-contract/) — standardized, exchange-traded contracts with daily settlement
- [Credit default swap](/credit-default-swap/) — OTC derivative increasingly pushed into clearing

### Wider context

- [Price discovery](/price-discovery/) — how markets uncover fair value through competition
- [Market maker trading](/market-maker-trading/) — dealers and market makers in OTC and exchange contexts
- [Derivatives hedging](/derivatives-hedging/) — what derivatives are and why they are used
- [Alternative trading system](/alternative-trading-system/) — electronic OTC platforms and dark pools

</div>
