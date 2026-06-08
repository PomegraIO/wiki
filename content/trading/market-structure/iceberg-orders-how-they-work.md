---
title: "Iceberg Orders: How They Work"
description: "How traders use iceberg orders to hide the bulk of a large order by displaying only a small visible quantity, how exchanges manage the reserve, and how market participants detect them."
keywords:
  - iceberg orders trading
  - how iceberg orders work
  - hidden orders stock market
  - reserve orders explained
image: /svg/trading.svg
---

*An **iceberg order** is a large buy or sell order that displays only a small visible quantity on the order book while hiding the bulk in a reserve. When the visible portion fills, the exchange automatically replaces it with the next visible tranche, repeating until all shares are gone. The name captures the idea: only the tip is visible above water, but the mass lies beneath.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Iceberg Orders — key facts</div>

<img src="/svg/trading.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Large order partially hidden to avoid advertising intent and moving the market.</div>

|   |   |
|---|---|
| **Visible quantity** | Small portion shown on order book, e.g., 1,000 of 100,000 shares |
| **Reserve quantity** | Hidden bulk; automatically restocked as visible portion fills |
| **Exchange support** | Nearly all major exchanges allow icebergs; some have minimum visible sizes |
| **Price** | Single limit price for both visible and reserved shares |
| **Detection** | Possible through pattern recognition but not always obvious |

</aside>

## Why Traders Use Icebergs

A large trader with 100,000 shares to sell faces a dilemma. Dumping all 100,000 on the [order book](/limit-order/) at once signals desperation and invites predatory prices. Other traders see the massive supply and assume the price will fall; they pull their bids, and the seller gets worse execution. This is called **market impact**.

An iceberg masks the true order size. A seller posts only 1,000 shares at, say, $50. Buyers execute against this visible tranche. Once those 1,000 are gone, the exchange automatically displays the next 1,000 from the reserve, again at $50. No announcement precedes each refill. To other traders watching the order book in real-time, it looks like a series of small orders from different participants, not one giant seller.

The result: less price pressure. Buyers buying at $50 don't know that 99,000 more shares are waiting to sell at the same price. They don't panic and lower their bids. The seller achieves better-executed price across the entire position.

## How the Mechanics Work

Most modern exchanges (including Nasdaq, NYSE, and international venues) support iceberg orders through their order-entry systems. A trader specifies:

- **Total quantity**: e.g., 100,000 shares
- **Visible quantity** (or "display quantity"): e.g., 1,000 shares
- **Price**: a single limit price, e.g., $50

The exchange's matching engine keeps only the visible 1,000 in the public order book. The remaining 99,000 sits in the exchange's system as reserved, out of sight.

As the visible 1,000 fills:

1. **Partial fill**: If 600 shares execute, the order book shows 400 left visible.
2. **Complete fill of visible**: When all 1,000 are gone, the exchange automatically refreshes the display with the next 1,000 from the reserve.
3. **Timing**: The refresh is nearly instantaneous, but there's a microscopic gap—a few milliseconds—where the order book shows no shares at that price. This gap is sometimes exploited by other traders.
4. **Repeat**: This continues until the reserve is exhausted.

Some exchanges allow traders to set a minimum display size (e.g., never show fewer than 500) so that partial fills near the end of the reserve don't leave tiny visible tranches. Others simply replenish with whatever's left if the reserve is smaller than the display size.

## Limiting Market Impact and Information Leakage

From a practical standpoint, the iceberg solves two problems:

1. **Reduces market impact**: By not broadcasting the full size, the trader avoids panic selling (if a seller) or front-running (if a buyer).
2. **Preserves anonymity**: The seller's intent is unclear. Are they a hedge fund exiting a position, a corporate seller, or a market maker? The gradual appearance of fresh quantity gives no hint.

The trade-off is speed. Executing 100,000 shares in tranches takes longer than dumping the whole order. If the price moves sharply in your favor while you're still filling, you've forgone the opportunity to sell at the higher price. Icebergs are tools for patient traders working toward a target price over hours or a day, not impatient ones.

## Detection and Gaming

Sophisticated traders and algorithms look for telltale patterns of icebergs. If the same price level keeps reappearing with the same visible size (e.g., 1,000 shares), it's likely an iceberg. Patterns might include:

- **Consistent refresh rate**: Orders appearing at the same size and price in quick succession.
- **Round numbers**: Display sizes like 1,000, 5,000, or 10,000 are common and suspicious.
- **Asymmetric fill**: The visible portion fills, but the reserve refills—real small orders wouldn't do this.

Some traders use **iceberg detection algorithms** to spot these patterns and make inferences about the true size. If an iceberg is detected, a predatory trader might try to exhaust the visible quantity repeatedly without intending to trade, pushing the price down and causing the hidden seller to eventually liquidate at a worse price. This is a form of griefing and is theoretically against exchange rules, but enforcement is difficult.

The SEC has published guidance on iceberg order manipulation, and major exchanges have taken steps to randomize refresh timing or hide other details to make detection harder. Some venues support "reserve orders" (an older term for the same concept) with additional privacy protections.

## Regulation and Exchange Rules

Different exchanges have different rules:

- **NYSE and Nasdaq**: Both support iceberg orders and reserve orders. Minimum display sizes vary but are typically 100–1,000 shares per execution. Brokers must ensure customers aren't trying to evade trade reporting or other regulatory obligations by using icebergs.
- **SEC Rule 10b-5 and Rule 11ac1-2**: These rules govern market manipulation and do prohibit using orders to artificially inflate or depress prices or to create false impressions of depth. An iceberg used solely for stealth execution is fine; an iceberg used to manipulate is not.
- **International**: Euronext, the London Stock Exchange, and other exchanges support similar functionality, though naming and minimum size requirements may differ.

Brokers must disclose iceberg use to clients and ensure they understand the risks: slower execution, potential for the order to be gamed, and the cost of market impact if the iceberg is detected.

## Variants and Related Concepts

**Reserve orders** are similar but sometimes refer to orders where only a small portion is visible on the public book, with the reserve hidden from all market participants (even the exchange's market depth display). Some exchanges distinguish between the two.

**Pegged orders** are a different beast: they automatically adjust their price based on the current [bid-ask spread](/bid-ask-spread/). They're not hidden, but they're dynamic.

**Order splitting algorithms** (used by large brokers) are related conceptually: they break a large order into smaller pieces and execute them across multiple venues and times to minimize market impact. But they're not icebergs on a single exchange; they're algorithmic tactics across the entire market.

## Tradeoffs in Modern Liquidity

Icebergs are popular tools for large institutions and [hedge funds](/hedge-fund/), but they're not without controversy. Critics argue that by hiding size, icebergs reduce true market transparency and make it harder for smaller traders to gauge real depth. If an iceberg is large enough, it distorts the visible order book and misleads other market participants into thinking liquidity is thinner than it actually is.

Others counter that transparency is not absolute; traders and institutions have legitimate reasons to execute large positions without moving the market. The existence of icebergs, and the tools to detect them, creates a cat-and-mouse game that adds an element of skill to trading.

In the era of high-frequency trading and machine learning, the game has evolved. Algorithms now compete on their ability to detect hidden orders and on the speed of their refresh responses. Exchange rule changes to protect iceberg users (e.g., randomizing refresh timing) are ongoing.

## See also

<div class="wiki-seealso">

### Closely related

- [Limit Order](/limit-order/) — the base order type underlying an iceberg
- [Bid Ask Spread](/bid-ask-spread/) — the cost an iceberg incurs if it must cross the spread
- [Market Order](/market-order/) — the urgent alternative when speed matters more than price
- [Crossed Market vs Locked Market](/crossed-market-vs-locked-market/) — market conditions that can affect iceberg execution
- [Market Maker Trading](/market-maker-trading/) — how market makers detect and respond to icebergs

### Wider context

- [Alternative Trading System](/alternative-trading-system/) — dark pools where size is always hidden
- [Stock Market](/stock-market/) — the ecosystem where icebergs operate
- [Securities and Exchange Commission](/securities-and-exchange-commission/) — the regulator of iceberg use and manipulation

</div>
