---
title: "Market on Close Order"
description: "An order guaranteed to execute at the official closing auction price at the end of the trading session."
keywords:
  - market on close order
  - moc order
  - closing auction
  - closing price
  - order execution timing
image: "/svg/trading.svg"
---

*A **Market on Close (MOC) order** is an instruction to a broker to buy or sell a security at the official closing [auction](/stock-exchange/) price, executed as the trading session closes. It guarantees execution at the closing price, the reference point used for end-of-day valuations, corporate dividends, and regulatory reporting.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Market on Close Order — key facts</div>

<img src="/svg/trading.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Locks in the official day's closing price; no price discretion.</div>

|   |   |
|---|---|
| **What it is** | A [market order](/market-order/) routed to the closing auction, guaranteed to fill at the session's official closing price |
| **Also called** | MOC order, at-close order, on-close order |
| **Execution time** | At the closing auction (typically 3:59–4:00 pm US time for equity markets) |
| **Price certainty** | Guaranteed closing price; no limit applied |
| **Counterpart** | [Market on Open Order](/market-on-open-order/) (opening auction) |
| **Typical use** | Fund rebalancing, benchmark tracking, portfolio realignment at session end |

</aside>

## Why traders route orders to the closing auction

The closing price is not arbitrary. For equities, it's the reference price used in index calculations, corporate earnings reports, fund valuations, and regulatory filings. A mutual fund or pension plan holding a stock reports its end-of-day value using the closing price. Margin calls and [maintenance requirements](/margin-call-forex/) are calculated using closing prices. Corporate dividends are paid based on shareholding at close. Consequently, executing at the close carries profound administrative and accounting significance.

A MOC order taps into the liquidity concentrated in the closing auction. Most exchanges have a formal close: the [New York Stock Exchange](/new-york-stock-exchange/) runs a closing auction in the final seconds of the session where buyers and sellers converge, often with massive order imbalances. A MOC order routes your entire purchase or sale to this auction, ensuring you trade at the session's official closing price, whatever it turns out to be.

## The mechanics of the closing auction

In the US equity market, the closing auction typically runs from 3:59 to 4:00 pm. Before 3:50 pm, traders can submit or modify MOC orders. At 3:50 pm, the exchange begins broadcasting the "imbalance"—how many more buy orders than sell orders (or vice versa) are waiting. The imbalance price is the price at which supply and demand would clear if the auction ended immediately. As more orders arrive, the imbalance price updates.

At 4:00 pm sharp, the auction concludes and a single price is determined at which all MOC orders (and eligible limit orders near the close) are matched. This unified price is the closing price. All MOC orders execute at that price, regardless of the wide range of prices bid in the final seconds.

Different exchanges handle closing mechanics differently. The [London Stock Exchange](/london-stock-exchange/) has its own closing call. [Tokyo Stock Exchange](/tokyo-stock-exchange/) uses a call auction at close. Even within the US, after-hours trading continues, but the official closing price is set during the primary auction.

## When MOC orders are essential

[Index funds](/index-fund/) and [passively managed funds](/actively-managed-fund/) rely on MOC orders. If a fund tracks the [S&P 500](/sp-500-index/), it must rebalance its holdings to match the index's composition. These rebalancing trades often happen at close so that the fund's net asset value (NAV) is calculated using the same prices as the index itself. MOC orders ensure the fund doesn't mismatch prices between its trades and its benchmark.

Institutional traders use MOC orders to avoid market timing risk. Instead of trying to judge whether morning, midday, or 3:30 pm is the "best" time to exit a position, they simply commit to the closing price. This removes discretion and takes the emotion out of timing—you know in advance you'll execute at close.

Portfolio managers often submit a batch of MOC orders to rebalance across multiple securities simultaneously. All orders fill at their respective closing prices within the same instant, ensuring the portfolio's weights are correct as of day-end.

## Price unpredictability and risk

The critical trade-off is that MOC orders do *not* specify a price limit. You are committed to executing at whatever the closing price turns out to be, even if it is wildly unfavourable. On a day of extreme volatility or late-session news shock, the closing price can diverge substantially from intraday prices.

Imagine a stock trading at £50 for most of the day, then a damaging news release hits at 3:55 pm. By the closing auction, the stock has plummeted to £42. An investor with a pre-set MOC sell order will sell at £42, not £50. This is the risk of market-on-close execution: you have price certainty in the sense of knowing it's the official close, but no certainty about what that price will be.

Sophisticated traders sometimes submit both a MOC order (as a fallback) and a [limit order](/limit-order/) at a price close to the expected close. If the limit order fills earlier in the day at an acceptable price, it's executed and the MOC order is cancelled. If the limit order doesn't fill, the MOC order ensures the position is still executed at close.

## Cancellation and modification rules

MOC orders can usually be modified or cancelled up until 3:50 pm on most US exchanges. After that window, the order is locked in—you cannot change your mind. This cutoff is necessary to allow the exchange to compile the final imbalance and calculate clearing prices.

If a stock halts (due to a trading pause or corporate action), the closing auction may be postponed or cancelled. In such cases, your MOC order may be rerouted to the next day's close or converted to a cancelled order, depending on your broker's procedure. Always confirm your broker's exact policy.

## Comparison with other time-based orders

MOC is often paired with [Market on Open (MOO)](/market-on-open-order/) orders, which execute at the opening auction. Together, they frame the beginning and end of the trading day. Neither specifies a price—both are [market orders](/market-order/) pegged to an auction.

[Good Till Date Orders](/good-till-date-order/) and Good Till Cancel Orders are far more patient; they sit in the market indefinitely (or until a specified date) and execute whenever the [limit](/limit-order/) or [bid-ask spread](/bid-ask-spread/) allows. MOC is the antithesis: it is completely time-bound, executing at one fixed moment regardless of price.

## See also

<div class="wiki-seealso">

### Closely related

- [Market on Open Order](/market-on-open-order/) — pegged to the opening auction instead of the close
- [Market Order](/market-order/) — an unpriced instruction to execute immediately
- [Limit Order](/limit-order/) — specifies a price, but no execution timing guarantee
- [Good Till Date Order](/good-till-date-order/) — a patient, time-bound order with price discretion
- Good Till Cancel Order — stands indefinitely until filled or cancelled
- Order Book — where orders rest before the closing auction
- [Immediate or Cancel Order](/immediate-or-cancel-order/) — opposite philosophy: instant execution or cancel
- [Stock Exchange](/stock-exchange/) — operates the closing auction

### Wider context

- [Index Fund](/index-fund/) — primary user of MOC orders for rebalancing
- [Net Asset Value](/net-asset-value/) — calculated using closing prices
- [Price Discovery](/price-discovery/) — the closing auction's role in market price formation
- [Volatility Smile](/volatility-smile/) — can cause closing prices to diverge sharply from midday
- [Trading Volume](/stock-market/) — concentrated at open and close

</div>
