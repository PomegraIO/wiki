---
title: "Crypto OTC Trading"
description: "Large off-exchange block trades in cryptocurrency designed to minimise market impact and slippage on substantial orders."
keywords:
  - OTC trading
  - over-the-counter
  - block trades
  - institutional trading
  - market impact
  - price discovery
image: "/svg/crypto.svg"
---

*In cryptocurrency **OTC trading**, large orders are executed directly between a buyer and seller (or via an intermediary broker) rather than through a public order book. A major trade might move the market sharply—causing **slippage**—if executed on an exchange. OTC dealers offer fixed prices for large blocks, avoiding the friction and price deterioration of exchange execution.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Crypto OTC Trading — key facts</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for cryptocurrency concepts." />

<div class="wiki-infobox-caption">Negotiated bilateral trades away from the public order book for large institutional orders.</div>

|   |   |
|---|---|
| **What it is** | Bilateral or brokered trades executed off-exchange at negotiated prices |
| **Typical size** | $1 million to $100+ million per trade |
| **Participants** | Institutions, [hedge funds](/hedge-fund/), family offices, large traders |
| **Price discovery** | Usually benchmarked to spot exchange prices; premium/discount negotiated |
| **Clearing** | Can be same-day or multi-day; often involves settlement delays |
| **Regulation** | Less stringent than exchange trading; varies by jurisdiction |
| **Cost** | Spread (bid-ask differential), potential prime broker fees |

</aside>

## Why large orders can't use public exchanges

On a centralized [exchange](/cryptocurrency-exchange/), buy and sell orders form a public order book. When a $50 million bitcoin buy order hits the market instantly, it overwhelms available sell liquidity at the best prices. The buyer must accept progressively higher prices as they move down the order book—a phenomenon called **market impact** or **slippage**.

If the book's best offer is $45,000 per bitcoin and only 10 bitcoin are available at that price, the buyer gets those 10 coins. The next 5 bitcoin are available at $45,100, the next 10 at $45,300, and so forth. A $50 million buy executed entirely on-exchange might average $45,500, not the $45,000 opening price. The trader paid an extra $250,000 due to market impact alone.

For smaller retail trades, this slippage is negligible. For an institution moving $100 million, it is catastrophic. OTC trading solves this by fixing the price in advance and not broadcasting the order.

## The dealer model

An OTC crypto dealer (Galaxy Digital, Jump Trading, Wintermute) maintains large inventory in popular assets—bitcoin, ethereum, stablecoins. When an institution calls a dealer with a buy interest, the dealer quotes a price: "I'll sell you 1,000 bitcoin at $45,200 each." This price is slightly above the current spot exchange price (the dealer's markup) but far better than the worst-case market-impact price.

The dealer profits from the spread between the price they offer the buyer and the price they can execute on the broader market (or against other counterparties). If the dealer buys at $45,000 and sells at $45,200, they keep $200 per bitcoin.

Unlike a [broker](/broker/) (who simply matches buyers and sellers without taking inventory), a dealer is a principal: they own the asset temporarily and assume price risk. If they sell 1,000 bitcoin at $45,200 and the price drops to $45,100 before they buy back, they lose $100,000.

## Bilateral vs. brokered OTC

In a bilateral trade, the buyer and seller negotiate directly or via a private call with a dealer. Terms are agreed verbally or via email, then documented in a trade ticket. Settlement is arranged separately—often with a [custodian](/custodian/) or [prime broker](/crypto-prime-brokerage/) handling the actual asset transfer.

Brokered OTC is slightly more formal. An institution calls an OTC broker (Bloomberg, Tradeweb), who works the order: they canvas dealers, negotiate terms, and execute on the client's behalf. The broker earns a commission (often $0.01–$0.05 per dollar transacted) without taking principal risk.

The bilateral and brokered models have different transparency: bilateral trades are entirely private. Brokered trades are recorded (at least by the broker) and sometimes aggregated into public data feeds, though with significant delay and anonymization.

## Price benchmarking and discovery

An OTC price is almost always referenced to a **spot** or index price. A dealer might say: "I'll sell you 1,000 bitcoin at spot plus 0.3%," where spot is defined as the volume-weighted average price (VWAP) on major exchanges (Coinbase, Kraken, Bitstamp) at 2 PM New York time. This anchors the price to something observable and reduces the dealer's risk that they're selling too cheap.

The OTC market is not independent; it follows the exchange market. When the spot price jumps 10% on news, OTC dealers adjust their marks immediately. Large institutional trades can, however, establish micro-price discovery: if multiple dealers are quoting $45,200 and one quotes $45,100, that $45,100 quote reveals information about dealer inventory and competition.

In volatile markets, OTC bid-ask spreads widen. If the exchange market is moving 1% per minute, a dealer might demand a 0.5% spread to protect against adverse price movement while executing the trade. In calm markets, spreads compress to 0.1% or less.

## Settlement and custody logistics

Once an OTC trade is agreed, settlement usually occurs within 1–2 business days. The buyer instructs their bank or custodian to wire funds; the seller instructs theirs to send the cryptocurrency. If both use the same [prime broker](/crypto-prime-brokerage/) (e.g., Genesis), settlement is internal—the broker transfers the asset on-ledger, and the trade is final within hours.

If the buyer and seller use different custodians, settlement is slower. The blockchain must confirm the transaction (which takes seconds for bitcoin, longer for ethereum), and both custodians must reconcile their records. Disputes—"I sent the bitcoin but didn't receive the USD"—are arbitrated by custom agreements, not by an exchange's clearing system.

This settlement friction is why large institutions prefer OTC via a common prime broker. It reduces [operational risk](/operational-risk/) and legal ambiguity.

## Advantages and disadvantages vs. exchange trading

**OTC advantages:**
- No slippage from market impact; price is locked in advance.
- Privacy: large trades don't broadcast intent to other traders.
- Flexibility: settlement timing can be negotiated; special terms (escrow, contingencies) are possible.
- Better pricing on massive orders (e.g., $100+ million).

**OTC disadvantages:**
- Higher cost on small orders: the dealer's spread is fixed, not dependent on size.
- Less price transparency: no public order book; harder to verify execution was fair.
- [Counterparty](/counterparty-risk/) risk: the dealer might fail mid-settlement (though this is rare with large dealers).
- Regulatory fragmentation: OTC trades are less uniformly regulated than exchange trades.

For an institution buying $1 million worth of bitcoin, exchange execution is likely cheaper (tighter spreads, lower fees). For $50 million, OTC is essential to avoid catastrophic slippage.

## Market microstructure and information leakage

One subtle advantage of OTC is that it prevents information leakage during order execution. On an exchange, a massive buy order is visible to all participants and can trigger frontrunning: other traders buy ahead of the large order, pushing the price up and forcing the large buyer to pay more.

An OTC dealer can hide the order entirely. The dealer agrees to a price with the buyer without showing the order to other market participants. However, once the dealer begins buying inventory on the exchange to hedge their position, the market can infer a large order is being worked.

Sophisticated dealers use algorithmic techniques to minimize this inference: they buy in small increments across multiple exchanges and venues, disguising their accumulation activity. Some institutional OTC trades are split across multiple dealers to further reduce signal.

## Growth and regulation

In traditional finance, OTC markets are enormous: trademarks, corporate bonds, and derivatives trade far more in OTC markets than on exchanges. Crypto OTC is younger but growing as institutional participation increases.

By the mid-2020s, OTC is a significant portion of large-scale crypto trading. Brokers like Alameda Research (pre-collapse) generated substantial revenues from OTC commissions. Post-FTX, larger and more transparent dealers dominate: Galaxy, Genesis, Jump Trading.

Regulatory treatment remains uneven. The EU's MiCA directive imposes some OTC disclosure requirements; the US has no unified OTC standard (yet). Most institutions treat OTC trades as bilateral contracts under existing commodity laws, with limited regulatory oversight compared to exchange trading.

## See also

<div class="wiki-seealso">

### Closely related

- [Crypto Prime Brokerage](/crypto-prime-brokerage/) — Institutional platform where OTC trades are often settled
- [Market Maker](/market-maker-trading/) — OTC dealers act as principal market makers
- [Cryptocurrency Exchange](/cryptocurrency-exchange/) — The on-exchange alternative to OTC
- [Bid-Ask Spread](/bid-ask-spread/) — How OTC dealers price trades
- [Over-the-Counter Market](/over-the-counter-market/) — Traditional OTC structure adapted to crypto

### Wider context

- Slippage — The market-impact cost that OTC avoids
- Block Trade — Equities analogue to crypto block trades
- [Market Order](/market-order/) — Exchange order type that OTC trading circumvents
- Settlement — Logistics of finalizing OTC trades
- [Hedge Fund](/hedge-fund/) — Typical participant in OTC markets

</div>
