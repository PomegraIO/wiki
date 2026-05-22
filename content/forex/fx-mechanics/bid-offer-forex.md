---
title: "Bid-Offer (Forex)"
description: "The price quotes and transaction costs in foreign exchange markets, where the bid is the price you receive when selling and the offer is the price you pay when buying."
keywords:
  - forex spread
  - market microstructure
  - transaction costs
  - currency pricing
---

*In [forex markets](/wiki/foreign-exchange-reserve/), a **bid-offer spread** (or bid-ask spread) is the difference between the price at which a dealer will *buy* a currency (the bid) and the price at which they will *sell* it (the offer). This spread is the primary transaction cost in currency trading and varies by liquidity, volatility, and dealer competition.*

<aside class="wiki-infobox">

| Pair | Typical Bid-Offer | Liquidity | Remarks |
|---|---|---|---|
| EUR/USD | 1–2 pips | Highest | The tightest spreads |
| GBP/USD | 1–3 pips | Very high | Slightly wider than EUR/USD |
| USD/JPY | 1–2 pips | Very high | Asian trading center support |
| USD/INR | 2–5 pips | High | Wider than G10 pairs |
| Exotic pairs | 5–20 pips | Lower | Minimal trading volume |
| EUR/GBP | 1–2 pips | Very high | Tight as a cross pair |

</aside>

## The basic mechanics: bid, offer, and spread

In any financial market, a dealer quotes two prices: a *bid* (the price the dealer pays to buy from you) and an *offer* (the price the dealer charges you to buy from them). The bid is always lower than the offer; the difference is the spread.

If a dealer quotes EUR/USD at 1.0850–1.0851, that means:
- The dealer will *buy* 1 euro from you for $1.0850 (the bid).
- The dealer will *sell* 1 euro to you for $1.0851 (the offer).

If you sell 1 million euros, you receive $1,085,000. If you then immediately buy 1 million euros back, you pay $1,085,100. The $100 loss is the spread—the dealer's profit for providing liquidity.

Spreads are quoted in **pips**, a unit equal to 0.0001 in most currency pairs (one ten-thousandth). The EUR/USD bid-offer of 1.0850–1.0851 is a **1-pip spread**. On the notional $1 million transaction, 1 pip equals $100. On major pairs, spreads range 1–3 pips during normal hours; exotic pairs may be 10–50 pips or wider.

## Market liquidity and spread dynamics

The bid-offer spread is a function of liquidity. During the overlap of U.S. and European trading hours (roughly 1 PM–5 PM UTC), the most active dealers are all in the market simultaneously. Competition drives spreads to their tightest. EUR/USD might trade 1 pip wide; GBP/USD, 1–2 pips wide.

Outside peak hours—during Asian trading or off-hours—dealer participation drops, spreads widen, and execution becomes slower. A trade that executes instantly at 1 pip during New York hours might require 3–5 pips at 3 AM New York time (when only a few Asian dealers are actively quoting).

[Volatility](/wiki/volatility-smile/) also affects spreads. On a calm day, spreads are tight. During market crises—a geopolitical shock, central bank announcement, or risk-off event—spreads widen dramatically. During the March 2020 COVID crash, some currency pairs traded with spreads of 50–100 pips, making transaction costs prohibitive for small traders.

## Competing dealers and the wholesale market

In the wholesale (interbank) market, major banks and dealers compete on spreads. A bank like JPMorgan or Barclays will quote spreads 0.5–1 pip on EUR/USD; dealers compete aggressively because the volume is enormous. A client might negotiate a tighter spread based on relationship and volume.

Retail brokers typically widen spreads beyond the interbank rate to cover their costs and capture a small margin. A retail trader might see EUR/USD quoted as 1.0850–1.0852 (2 pips) even though interbank spreads are 1 pip. The extra 0.5 pip margin is the broker's profit.

Market makers—dealers who actively quote prices and stand ready to buy or sell—earn money on the spread. They buy at the bid and sell at the offer, or vice versa. If they're skilled, they hedge their inventory quickly and lock in the spread as profit. If they're caught on the wrong side of a move (e.g., they bought euros and the euro falls), they lose.

## Price impact and the order book

In electronic trading, the bid-offer spread reflects supply and demand at a given moment. A deep [order book](/wiki/order-book-depth/) (many buy orders near the bid and many sell orders near the offer) indicates tight spreads. A thin order book (few counterparties) widens spreads.

The bid-offer can also widen predictably at certain times. At the release of economic data (employment figures, inflation reports, central bank decisions), bid-offers widen because dealers are uncertain about where prices will move. Immediately after the data, if it's unambiguous, the spread tightens as price discovery occurs and dealers rebalance inventory.

## Impact on different trader types

For a long-term investor, the forex spread is a minor nuisance. Buying EUR/USD at 1.0851 versus 1.0850 is a 0.01% cost on a transaction; over a multi-year holding period, this cost is negligible.

For a day trader or scalper, the spread is the primary hurdle. A scalper might make 10 trades per hour, each trying to capture 5–10 pips of price movement. If the spread is 2 pips, the scalper needs 2 pips of favorable move just to break even. A spread widening from 2 pips to 5 pips during volatile hours can make scalping unprofitable.

For a corporation hedging foreign currency exposure, the spread is part of the hedging cost. A U.S. exporter receiving 1 million euros in 3 months might sell euro forward today to lock in the exchange rate. If the forward market spread is 2 pips, that cost is passed through to the exporter's overall hedging expense.

## Comparison across trading venues

The spread varies by venue. Interbank markets (where banks trade directly via electronic communications networks (ECNs) or over the phone) have the tightest spreads. Retail brokers (typically market makers) offer wider spreads but more convenience. Futures markets (e.g., CME currency futures) have tighter spreads than spot OTC forex but are not 24-hour and have contract specifications.

A retail forex broker might offer EUR/USD at 1–2 pips; a bank's wholesale forex desk at 0.5 pips; a CME futures contract at roughly 1 pip in notional spread. The choice depends on the trader's volume, relationship, and needs.

## Hedging with currency forwards and the all-in cost

Currency forwards and [options](/wiki/currency-option/) also have bid-offer spreads, but they're quoted differently. A forward might be quoted as +50/+40, meaning the dealer will buy euros at spot plus 50 pips (forward points) and sell at spot plus 40 pips. The 10 pip difference is the spread in the forward market.

The all-in cost of hedging a currency exposure using forwards includes both the spot bid-offer spread and the forward spread. A corporation might decide that the total cost is acceptable if it eliminates the risk, or it might reject hedging if the cost is too high relative to the exposure.

## Electronic communication networks and algorithmic execution

Modern forex trading is dominated by electronic networks and algorithms that execute large orders in smaller pieces to minimize [market impact](/wiki/market-impact-cost/). An algorithm executing a 10 million EUR buy order might break it into 100,000 EUR chunks, submitting orders to multiple venues to achieve the best blended price.

Spreads on ECNs are typically tighter than on single-dealer venues because multiple market makers are quoting simultaneously. Some ECNs charge a small fee (0.5–1 pip) in addition to a tighter spread. The effective cost might be similar to a single dealer with a wider spread but no fee.

<div class="wiki-seealso">

### Closely related
- [Forex Spread](/wiki/forex-spread/) — the bid-ask spread in currency markets
- [Bid-Ask Spread](/wiki/bid-ask-spread/) — the spread in stock markets and other assets
- [Market Impact Cost](/wiki/market-impact-cost/) — cost of executing large orders
- [Electronic Communication Network](/wiki/electronic-communication-network-market/) — trading platform

### Wider context
- [Currency Hedging](/wiki/currency-hedging/) — strategies to reduce currency risk
- [Order Book Depth](/wiki/order-book-depth/) — liquidity available at different price levels
- [Market Maker](/wiki/market-makers/) — dealer providing liquidity by quoting bid-offer
- [Execution Quality](/wiki/execution-quality-analysis/) — how well an order was executed

</div>
