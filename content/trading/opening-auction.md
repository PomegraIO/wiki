---
title: "Opening auction"
description: "The opening auction is the process by which stock exchanges (like NYSE and NASDAQ) determine opening prices at the start of each trading day. Orders accumulate before the market opens, and the exchange finds the price that matches the most shares."
keywords:
  - opening auction
  - market opening
  - opening price
  - auction process
image: "https://picsum.photos/seed/opening-auction/900/600"
---

*The **opening auction** is the mechanism used by stock exchanges to determine opening prices at the start of each trading day (9:30 a.m. ET for U.S. equities). Before the market officially opens, traders and algorithms submit orders to buy and sell. The exchange's auction algorithm finds the price that matches the most shares and causes the least imbalance, setting the opening price. This process ensures orderly trading and prevents the first trade from moving the price sharply.*

<div class="wiki-hatnote">

For the closing process, see closing auction. For trading throughout the day, see [lit venue](/lit-venue). For price discovery, see order book.

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Opening auction — key facts</div>

<img src="https://picsum.photos/seed/opening-auction/900/600" alt="Stock exchange opening bell at 9:30 a.m." />

<div class="wiki-infobox-caption">Opening auction: orders accumulate before 9:30 a.m.; price set at the cross.</div>

|   |   |
|---|---|
| **Timing** | 9:30 a.m. ET (U.S. equities); 8 a.m.–9:30 a.m. pre-market |
| **Process** | Orders accumulate during pre-market; exchange calculates opening price |
| **Price discovery** | Price that matches the most shares at the open |
| **Execution** | All opening auction orders typically execute at the opening price |
| **Volume** | Often 10–20% of daily volume happens in the first minute |

</aside>

## How the opening auction works

**Before 9:30 a.m.:**
- Traders submit orders electronically (many overnight or at the market open).
- Brokers and traders place buy orders (bids) and sell orders (asks).
- The order book accumulates orders but no trades occur.

**At 9:30 a.m.:**
- The exchange's auction algorithm calculates the opening price.
- The algorithm finds the price at which:
  - The number of shares bid equals (or nearly equals) the shares offered.
  - The number of trades (shares that can match) is maximized.
  - The price is usually at or near the previous close or the reference price.

**Opening cross:**
- All matching orders execute simultaneously at this price.
- A single print (the opening price) is announced.
- Regular (continuous) trading then begins.

## Example opening auction

**Pre-market orders accumulate:**

| Side | Price | Shares |
|---|---|---|
| Buy | $150.05 | 5,000 |
| Buy | $150.00 | 10,000 |
| Buy | $149.95 | 15,000 |
| Sell | $150.05 | 8,000 |
| Sell | $150.10 | 10,000 |
| Sell | $150.15 | 12,000 |

**Exchange calculates:** At what price do buys and sells best match?

- At $150.05: 15,000 shares of buy interest (the two buy orders below $150.05) vs. 8,000 shares of sell interest. 8,000 shares can match.
- At $150.00: 10,000 shares of buy interest vs. 18,000 shares of sell interest (all sell orders). Only 10,000 can match.
- At $150.10: 25,000 shares of buy interest (all three buy orders) vs. 10,000 shares of sell interest. 10,000 can match.

**Conclusion:** The price that maximizes matching is $150.05–$150.10 depending on the algorithm. Let's say the exchange settles on $150.05 (a reasonable midpoint).

**Opening trade:**
- 15,000 shares offered for sale at $150.05.
- 8,000 shares buy at $150.05 (from sellers).
- 7,000 shares buy at next-best price ($150.00).
- First trade: 8,000 shares at $150.05 (the opening price).
- Remaining orders in the book for continuous trading.

## Pre-market vs. post-market trading

**Pre-market (8 a.m.–9:30 a.m.):**
- Limited liquidity; wide spreads.
- Orders accumulate for the opening auction.
- Most pre-market trades are thin.

**Opening auction (9:30 a.m.):**
- Concentrated liquidity; tighter spreads.
- All accumulated orders match simultaneously.

**Regular trading (9:30 a.m.–4:00 p.m.):**
- Continuous auction (orders match as they arrive).
- Most daily volume occurs here.

**After-hours (4:00 p.m.–8:00 p.m.):**
- Limited liquidity again.

## Why auctions?

**Prevents volatility:** An opening without an auction would see the first trade move the price sharply (e.g., if a big seller hits, the price would plummet). The auction smooths this by matching large orders at a fair price.

**Fair price discovery:** The auction price reflects supply and demand for the entire pre-market accumulation, not just the first trade that happens to execute.

**Orderly opening:** Institutions can submit large orders knowing they will be treated fairly and executed at the same price (not gamed by being first or last).

## Opening auctions and events

Opening auctions can be volatile or orderly depending on overnight news:

**Quiet nights:** Opening auctions are smooth; pre-market price ≈ opening price ≈ previous close.

**Earnings surprises or news:** If a company reports terrible earnings overnight, the opening auction might see a sharp gap down (opening price far below previous close). This is normal and reflects the new information.

**Trading halts:** If the stock is halted due to an announcement, the opening auction is delayed until the halt is lifted.

## Closing auction

The closing auction (4:00 p.m. ET) works similarly: orders accumulate in the final minutes, and the exchange calculates a closing price that matches the most shares. This closing price is important for index calculations and fund NAV calculations.

## Opening auctions and high-frequency traders

HFTs often participate in opening auctions, submitting orders just before 9:30 a.m. and pulling them immediately after (if they are not filled). This can cause:
- Large opening order imbalances.
- Sharp opening prices if the imbalance is large.
- Volatility in the first minute.

Regulators monitor for abusive opening auction activity (e.g., orders designed to mislead about true supply/demand).

## International opening auctions

Different exchanges have different auction mechanisms:

- **NYSE (U.S. equities):** Electronic auction; human input from designated market makers (DMMs) if needed.
- **NASDAQ (U.S. equities):** Electronic auction.
- **LSE (London):** Opening auction 8 a.m. GMT.
- **Euronext (Europe):** Opening auction 9 a.m. CET.

All use variants of the same principle: match the most shares at the fairest price.

## Trading strategies around openings

**Gap traders:** Buy or short based on overnight news and expect the opening auction to move sharply.

**Opening range traders:** Trade the first 30 minutes and look for breakouts.

**Volatility scalpers:** Expect opening volatility and capture short-term moves.

**Arbitrage:** Compare pre-market (thinly traded) with opening auction prices and trade the difference.

## See also

<div class="wiki-seealso">

### Closely related

- Closing auction — counterpart at 4:00 p.m.
- Order book — where opening orders accumulate
- Market opening — the broader opening process
- [Lit venue](/lit-venue) — exchanges that run auctions

### Price discovery and trading

- Price discovery — opening auctions contribute to this
- Opening price — result of the auction
- Gap — when opening price differs sharply from prior close
- Liquidity — opening auctions provide this

### Trading styles

- Gap trading — trade opening gaps
- Opening range breakout — trade first 30 minutes
- [High-frequency trading](/high-frequency-trading) — participant in opening auctions
- [Day trading](/day-order) — traders participate in opening

### Market mechanics

- Auction mechanism — price-setting mechanism
- Imbalance — buy-sell imbalance at opening
- Designated market maker — NYSE DMMs facilitate opening
- [After-hours trading](/after-hours-trading) — post-close venue

</div>
