---
title: "Discretionary Limit Order"
description: "A limit order with a visible minimum size and a hidden order quantity, allowing size to be revealed at the trader's discretion."
keywords:
  - discretionary order
  - iceberg order
  - hidden size
  - order display
---

*A **discretionary limit order** is a [limit order](/wiki/limit-order/) that displays only a fraction of the total size to the market ([iceberg order](/wiki/iceberg-order/)), while the remainder stays hidden, allowing the trader to execute large orders without advertising their full intention and inviting [market impact](/wiki/market-impact-cost/).*

A trader wants to sell 500,000 shares of a stock trading at $50 with daily volume of 1M shares. Dumping 500k on the order book immediately would depress the price—other traders see the huge ask, assume the seller is distressed, and pull their bids down to $49, $48. The trader would face significant market impact. Instead, the trader places a discretionary limit order: "Sell 50,000 at $50 (visible), 450,000 hidden." The market sees only the 50,000-share ask at $50. As buy orders fill the visible tranche (50,000 shares get executed), the system automatically displays another 50,000 from the hidden portion, and so on, until the entire 500,000 is sold.

This structure allows large institutions to execute block sales without telegraphing their intentions to the entire market—a crucial tool in equity and [futures markets](/wiki/futures-contract/) where [information leakage](/wiki/rule-10b-5/) can be costly.

<aside class="wiki-infobox">

| Feature | Detail |
|---|---|
| **Visible size** | Minimum portion shown to market (e.g., 50,000 shares) |
| **Hidden size** | Remainder known only to exchange and broker (e.g., 450,000) |
| **Price** | Single limit price for entire order (e.g., $50) |
| **Execution** | Visible tranche fills; hidden re-displayed progressively |
| **Advantage** | Minimizes market impact and front-running |
| **Disadvantage** | Slower execution; may miss fast-moving market |
| **Disclosure** | Some venues (NYSE, CBOE) disclose hidden-order counts in reports |
| **Aliases** | Iceberg, reserve order, partially-hidden order |

</aside>

## Mechanics and execution

A discretionary order operates on most venues under specific rules:

1. **Display threshold**: The visible portion is set by the trader or broker algorithm. Common thresholds are 10%, 20%, or a fixed quantity (e.g., 50,000 shares). The exchange publishes only this visible tranche to the [order book](/wiki/order-book-depth/).

2. **Hidden queue**: The exchange system holds the hidden portion and ranks it based on the order's entry time. When the visible portion is fully filled by incoming buy orders, the system automatically replenishes the visible side with the next batch from the hidden portion.

3. **Price priority**: All shares execute at the same limit price, regardless of visible/hidden distinction. If the visible 50,000 sells at $50, the hidden 450,000 is also marketed for sale at $50 (until the limit is lifted or the order is cancelled).

4. **Cancellation**: The trader can cancel at any time, removing all remaining (visible and hidden) shares.

## Market impact and information leakage

The primary advantage is **avoiding market impact**. If 500,000 shares suddenly appear on the ask side, the [bid-ask spread](/wiki/bid-ask-spread/) widens, buy-side liquidity dries up, and the offer is perceived as a forced sale. With a discretionary order showing only 50k, the market remains calm—the apparent supply is modest, and the spread tightens. The buyer sees orderly flow, not a desperate seller.

**Front-running** is also reduced. If a [high-frequency trading](/wiki/high-frequency-trading/) firm sees a 500k ask, they might position ahead of it, selling their own shares first to depress price and force the large seller to accept worse fills. With a discretionary order, the HFT doesn't know the true size, so they cannot exploit it.

## Discretionary orders vs. pegged and stop orders

A **discretionary order** is distinct from a **pegged order** (which automatically adjusts its price based on the best bid/offer) and a **stop order** (which is inactive until a trigger price is hit). A discretionary order has a fixed limit price but variable visibility. A **[pegged order](/wiki/peg-order/)** might display 50,000 at the best bid, and if the best bid moves, the order reprices and re-displays at the new best bid.

An **iceberg order** is synonymous with a discretionary order in U.S. equities, but terminology varies globally. Some venues use "reserve order" (the hidden portion is a "reserve" to replenish the displayed portion). Futures markets often call them "iceberg" orders.

## Regulatory and disclosure considerations

U.S. exchanges ([NYSE](/wiki/new-york-stock-exchange/), [NASDAQ](/wiki/nasdaq/), [CBOE](/wiki/cboe-options-exchange/)) allow discretionary orders under [Regulation SHO](/wiki/regulation-sho/) and [Rule 10b-5](/wiki/rule-10b-5/) guidelines. The order must be marked "iceberg" or "reserve" in the order flow and is handled transparently—the exchange knows the hidden size, and if the hidden portion is very large relative to typical daily volume, the exchange may require special handling or disclosure.

**FINRA** and the **SEC** have periodically investigated discretionary orders for potential manipulation. For instance, if a trader places a 1,000,000-share discretionary order with a 1,000-share visible portion, the intent might be to create a false sense of low supply and artificially elevate the price (spoofing). Modern exchanges have circuit-breakers and algorithms that flag such orders for review.

Some exchanges (particularly non-U.S.) restrict discretionary orders. The **MiFID II** rules in Europe have tightened rules around dark and semi-dark orders to improve price transparency.

## Practical example

A pension fund manager holds 1M shares of a large-cap index stock and wants to trim the position by 300k shares. Selling in the open market at once would incur $500k–$1M in market-impact cost (the price would drop 1–2% due to the large seller notification). Instead, the fund's broker:

1. Places a discretionary sell order: "300,000 shares at $100 limit, display 30,000 at a time."
2. Over the next 2–3 hours, buy-side interest fills the visible 30k; the system displays the next 30k.
3. The entire 300k is sold at or above $100, with far less market impact.

The fund might pay a slightly higher brokerage fee for the algorithm, but saves 1–2% on execution—a net win of $300k–$600k.

## Limitations and risks

**Execution speed** is slower. A market that moves rapidly (a news event causes a sharp 5% move) may outpace the discretionary order. The visible 30k might sell, but by the time the next 30k is displayed, the market has moved and price has dropped. The trader may be tempted to lift the limit price or cancel and accept market impact—negating the discretionary order's benefit.

**Adverse selection** can occur: if the market suspects a very large hidden order, counterparties might avoid trading with the visible tranche, knowing more is coming. This can actually *worsen* execution vs. a direct large order (at least signaling the true size upfront and allowing the best counterparties to respond).

<div class="wiki-seealso">

### Closely related
- [Limit Order](/wiki/limit-order/) — foundational order type
- [Iceberg Order](/wiki/iceberg-order/) — synonym for discretionary order
- [Order Types](/wiki/order-types/) — broader taxonomy
- [Block Trading Platform](/wiki/block-trading-platform/) — venue for large orders

### Wider context
- [Market Impact Cost](/wiki/market-impact-cost/) — what discretionary orders minimize
- [High-Frequency Trading](/wiki/high-frequency-trading/) — front-running threat
- [Regulation SHO](/wiki/regulation-sho/) — SEC rule governing short sales and order marking
- [Order Book Depth](/wiki/order-book-depth/) — visible liquidity layers

</div>
