---
title: "Dark Pool vs Lit Exchange: How Each Handles Orders"
description: "Dark pools are off-exchange venues where orders execute without public visibility; lit exchanges display all quotes publicly. Each serves different traders and comes with trade-offs in price and secrecy."
keywords:
  - dark pool vs lit exchange
  - dark pool explained
  - lit exchange
  - off-exchange trading
  - order transparency
  - price discovery
  - execution venue choice
---

*A **dark pool** is a private trading venue where buy and sell orders execute without their prices or volumes being displayed to the public beforehand. In contrast, a **lit exchange** publishes all live bids and offers in real time. Both are regulated venues under U.S. law, but they serve opposite needs: dark pools offer anonymity and reduced market impact; lit exchanges offer transparency and price discovery. Most institutional traders use both.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Dark Pool vs Lit Exchange — key facts</div>

<img src="/svg/markets.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Dark pools hide orders; lit exchanges broadcast them. Each attracts different traders.</div>

|   |   |
|---|---|
| **Visibility** | Dark: hidden until execution. Lit: published live via data feeds |
| **Pricing** | Dark: negotiated or reference; Lit: transparent bid-ask |
| **User type** | Dark: large institutions (hedge funds, mutual funds); Lit: everyone |
| **Regulation** | Both SEC-regulated; dark pools as [ATS](/alternative-trading-system/) |
| **Order book** | Dark: not displayed; Lit: fully disclosed in real time |
| **Execution speed** | Dark: can be slower (manual matching); Lit: microseconds |
| **Price impact** | Dark: reduced (no visibility to predators); Lit: visible immediately |
| **Anonymity** | Dark: yes; Lit: visible to market makers and brokers |

</aside>

## What is a lit exchange?

A **lit exchange** is a traditional, regulated trading venue where all active orders and their prices are displayed in real time. The [New York Stock Exchange](/new-york-stock-exchange/) (NYSE), [NASDAQ](/nasdaq/), the Chicago Mercantile Exchange (CME)—these are lit exchanges. Their order books are public.

When you place a buy order for 1,000 shares of Microsoft at $400, market participants worldwide see that order (or can subscribe to the data feed). Sellers know there's a buyer at $400 and can decide whether to hit that bid. Price discovery happens in the light: real prices, real volumes, real interest.

Lit exchanges run matching engines that execute orders instantly using price-time priority rules. A sell order at the best price hits the waiting buy order with the earliest timestamp. This mechanical fairness is a feature, not a bug.

## What is a dark pool?

A **dark pool** is an off-exchange trading venue operated by a broker, market maker, or investment bank where orders are hidden from public view until (or unless) they execute. You can't see the order book; you can't see unexecuted orders; you can only see that a trade happened *after* it completed.

Citadel, Virtu Financial, and most major brokers operate dark pools. They are regulated as Alternative Trading Systems ([ATS](/alternative-trading-system/)) under SEC Rule 15c2-11 but are exempt from some of the transparency rules that bind lit exchanges. Dark pools serve an important function: they let large institutions move blocks of stock without telegraphing their hand to the market.

Imagine a pension fund needs to sell 5 million shares of Apple over a day. If it shows that order on the NYSE, every [high-frequency trader](/high-frequency-trading/) and predatory algorithm in existence will see incoming selling pressure and front-run the sales, pushing the price down. By routing to a dark pool, the pension fund finds a buyer (or multiple small buyers) in private. When the trade executes, the market sees only the result, not the build-up.

## Price discovery and transparency

Lit exchanges are engines of price discovery. Because all bids and offers are visible, the market-wide consensus on fair value emerges organically. If Apple is trading $150–$150.02 on the NYSE and a dark pool shows a $150.50 print (an executed trade), everyone knows Apple just traded at $150.50 somewhere. But the live quote on the NYSE may not have moved yet; that's a lag.

Dark pools operate as price-takers: they reference lit-exchange prices. Most dark pools execute at the "volume-weighted average price" (VWAP) of the previous hour, or at the current lit-exchange midpoint, or at a negotiated spread off the midpoint. They don't discover new prices; they derive prices from the lit market.

This creates a subtle risk for retail investors. If you're trading on a lit exchange and you see a tight spread, you might assume that's the fairest price available. But unseen dark-pool trades might be executing at better prices for insiders. You never see them, so your perception of market conditions is incomplete.

## The case for dark pools: institutional size and stealth

For large institutions, dark pools are essential infrastructure. A $10-million equity block order cannot be executed on the lit market without significant market impact. Here's why:

1. **Information leakage**: Market makers see the order and front-run the likely direction.
2. **Adverse selection**: If you're selling a block, informed traders know you're a likely seller and push prices down.
3. **Execution risk**: A 100,000-share order split across a lit exchange's order book can take hours to fill, meanwhile the market moves against you.

Dark pools solve this by allowing brokers to "cross" orders internally—matching a buy and sell from different clients—or by matching against algorithmic iceberg orders that hide real size. When a large buyer and large seller both use the same dark pool, they meet without the rest of the market knowing.

Execution quality on dark pools, despite the lack of transparency, can be excellent for block trades. Spreads are often tighter than lit markets for large sizes, and execution is faster because there's no priority queue—just a matching system.

## The case against dark pools: price discovery and fairness

Critics argue that dark pools erode price discovery and fairness. A few key concerns:

**Fragmentation**: If a large percentage of trading migrates to dark pools, the lit-market quote becomes less representative. Retail traders see the lit market and think it's the "real" market, but much trading—and much information—is happening in private.

**Predatory behavior**: Some dark pools have been accused of giving certain high-frequency trading firms early visibility into pending orders, an advantage over other pool participants. The SEC has fined Citadel, UBS, and other operators for this.

**Information asymmetry**: Institutional traders know about dark-pool execution options; retail traders typically don't. A retail order might execute at a lit exchange at $100.02 while an institutional block with the same liquidity need gets $100.00 in a dark pool.

**Conflicts**: Brokers who operate dark pools have an incentive to route orders into them (via [payment for order flow](/payment-for-order-flow-mechanics/)) rather than seeking the best price on a lit venue.

## Regulation and transparency reports

Dark pools are not unregulated. They operate under SEC oversight as ATSs and must file regular reports disclosing:
- Volume handled by the pool.
- Execution quality metrics (average spreads, size fills, price improvement vs. NBBO).
- Order routing practices.

These reports are public (quarterly), but they're dense and rarely scrutinized by retail investors. The SEC has used them to identify and fine dark pools with sketchy practices.

In 2010, Regulation SHO required publication of "dark pool volume" in near-real time, increasing transparency. But details remain opaque to most traders.

## How to choose: dark pool vs. lit exchange

For a **retail investor**, the question is mostly moot. Your broker routes your order; you don't choose the venue. If your broker uses PFOF, your order likely lands in a dark pool operated by the market maker. If your broker routes to best execution, your order might execute on both—part on the lit market, part in a dark pool—depending on where the best price is at that instant.

For an **institutional trader** (hedge fund, pension fund), the choice is strategic:
- **Lit market**: for standard-size orders where transparency and fair price are paramount.
- **Dark pool**: for large blocks or when you want to minimize market impact and avoid predatory detection.

Many institutions use both. They might place a primary order in a dark pool and, if it doesn't fill quickly, peel off a portion to the lit market at a worse price rather than wait.

## See also

<div class="wiki-seealso">

### Closely related

- [Alternative Trading System](/alternative-trading-system/) — The regulatory category dark pools fall under
- [Market Maker Trading](/market-maker-trading/) — Who operates dark pools and profits from order flow
- [Stock Exchange](/stock-exchange/) — Lit venues that compete with dark pools
- [Payment for Order Flow](/payment-for-order-flow-mechanics/) — How dark pools receive retail orders via PFOF
- [Price Discovery](/price-discovery/) — The role lit exchanges play that dark pools lack
- [How Trade Matching Engines Work](/how-trade-matching-engines-work/) — Mechanisms both dark pools and lit exchanges use

### Wider context

- [Securities and Exchange Commission](/securities-and-exchange-commission/) — Regulates both dark pools and lit venues
- Market Transparency — The broader debate about information asymmetry in trading
- Institutional Investor — The primary users of dark pools
- Order Routing — How brokers decide between dark and lit venues

</div>
