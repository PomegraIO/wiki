---
title: "Price Improvement"
description: "Execution of a trade at a price better than the current quoted bid or ask."
keywords:
  - price improvement
  - best execution
  - execution quality
  - order execution
---

*A **price improvement** occurs when a trade is executed at a price better than the prevailing [bid-ask spread](/wiki/bid-ask-spread/), allowing an investor to buy below the asking price or sell above the bidding price, reducing transaction costs.*

<aside class="wiki-infobox">

| Metric | Definition |
|--------|-----------|
| Improvement | Better than NBBO* |
| For Buy Orders | Execution below the ask price |
| For Sell Orders | Execution above the bid price |
| Source | Market makers, alternative venues |
| Measurement | Savings in cents per share or basis points |

*NBBO = National Best Bid and Offer

</aside>

## Understanding the quoted spread

In a typical market, the [bid](/wiki/bid-ask-spread/) is the highest price at which someone is willing to buy, and the [ask](/wiki/bid-ask-spread/) is the lowest price at which someone is willing to sell. If Apple is quoted at 150.00 bid × 150.05 ask, an investor sending a market buy order typically executes at the ask ($150.05), and a market sell order executes at the bid ($150.00). The spread (5 cents) is the round-trip cost.

**Price improvement** means the buy executes at less than 150.05 (say, 150.02) or the sell executes above 150.00 (say, 150.03). The improvement can be a few cents (common) or larger (rare but possible in illiquid securities).

## Sources of price improvement

**Market makers** with deep inventory often provide improvement to attract order flow. If a market maker sees a large buy order coming, it might execute part of it at the ask minus 1 cent, earning the spread on the remainder and capturing volume. **Alternative trading systems** (ATSs) and [dark pools](/wiki/dark-pool/) can match orders internally at midpoint (halfway between bid and ask), giving both sides a 2–3 cent improvement versus the lit market.

In [options markets](/wiki/option/), market makers routinely provide improvement; in [equity markets](/wiki/equity-etf/), improvement on highly liquid stocks is smaller (1–2 cents) but still meaningful at scale. Illiquid securities rarely see improvement because few market participants exist to bid/offer better prices.

## Regulatory framework and disclosure

The SEC's [Regulation NMS](/wiki/reg-nms-detail/) requires brokers to execute orders at the **National Best Bid and Offer** (NBBO) — the best prices available across all public venues — unless the customer consents to a different venue. Brokers are prohibited from deliberately sending orders to lower-quality venues to avoid offering improvement.

Brokers must regularly disclose their order-execution quality and price improvement rates (SEC Rule 10b-1). Institutional investors scrutinize these disclosures to compare brokers. A broker that consistently delivers 2 cents of improvement per trade (on millions of shares) saves clients hundreds of thousands annually.

## Payment for order flow and conflicts

Brokers often receive "payment for order flow" (PFOF) from market makers in exchange for sending them orders. A broker sends 100,000 shares to a market maker and receives a rebate of 0.5 cents per share. If the market maker provides 1 cent of improvement, the net cost to the customer is only 0.5 cents — but the broker's incentive is distorted. Regulators scrutinize PFOF for conflicts of interest, and some jurisdictions (EU under MiFID II) ban it outright.

The question is whether PFOF improves execution overall or primarily benefits the broker. Empirical studies find mixed results; price improvement from PFOF is real but sometimes offset by order flow internalization (the market maker matching orders against itself rather than routing to the lit market, reducing competition).

## Institutional vs. retail execution

Large institutional orders often receive negotiated prices well better than the NBBO. An institution selling 1 million shares might negotiate a block price with one market maker at a discount to the midpoint, improving on the spread without exposing the order to the full market. This is [block trading](/wiki/block-trade-mechanics/) — distinct from retail price improvement but same concept.

Retail investors, sending smaller orders, receive smaller improvements on average. A 100-share retail order to buy Apple might improve by 1 cent; a 10,000-share institutional order might improve by 3–5 cents because the market maker commits larger capital.

## Measuring and comparing improvement

Brokers report price improvement as either absolute (pennies per share) or relative (percentage of trades receiving improvement, or average cents per trade). A broker might report: "50% of buy orders received price improvement averaging 1.2 cents per share." Comparing brokers requires looking at volume-weighted improvements across all order sizes and securities.

Execution quality is published quarterly by [FINRA](/wiki/finra/) and available on broker websites. High-volume traders actively compare and may switch brokers if improvement rates lag.

## In electronic and high-frequency markets

[High-frequency trading](/wiki/high-frequency-trading/) and [algorithmic execution](/wiki/algorithmic-trading/) have increased price improvement opportunities by adding liquidity and reducing spreads. Competition among market makers and alternative venues has driven spreads on liquid stocks to historic lows (sub-penny, but regulated to prevent quote lock-in). Price improvement is now more common, but also smaller in absolute terms.

[Latency](/wiki/latency-tier/) and technology infrastructure matter enormously: a broker with fast connections to alternative venues can route orders to capture improvement opportunities faster than slower competitors.

## Long-term cost reduction

Over a career, cumulative price improvement is substantial. An investor trading 1 million shares annually who receives average 1 cent of improvement per trade saves $10,000 annually. Over a 30-year career, the cumulative benefit of using a broker with superior execution quality can be hundreds of thousands of dollars — a reminder that seemingly small execution costs compound.

<div class="wiki-seealso">

### Closely related
- [Bid-Ask Spread](/wiki/bid-ask-spread/) — the gap between buying and selling prices
- [Best Execution](/wiki/best-execution/) — regulatory obligation to execute at best available price
- [Execution Quality Analysis](/wiki/execution-quality-analysis/) — measuring order cost and slippage
- [Order Types](/wiki/order-types/) — different instructions for executing trades

### Wider context
- [Regulation NMS](/wiki/reg-nms-detail/) — SEC rules on best execution
- [Market Maker](/wiki/market-maker-trading/) — provider of liquidity
- [Payment for Order Flow](/wiki/payment-for-order-flow/) — broker compensation from market makers
- [Dark Pools](/wiki/dark-pool/) — alternative venues offering internal matching

</div>
