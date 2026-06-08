---
title: "One-Sided Market"
description: "A market condition where only bids or only asks exist, signalling severe imbalance, liquidity withdrawal, or trading suspension."
keywords:
  - bid-ask spread
  - market imbalance
  - liquidity crisis
  - order book
  - trading halt
image: "/svg/markets.svg"
---

*A **one-sided market** exists when only buying interest (bids) or only selling interest (asks) appears on an order book—the opposite side is empty. This extreme imbalance signals severe liquidity pressure, loss of confidence, or a temporary breakdown in price discovery, often preceding trading halts or [market maker](/market-maker-trading/) withdrawal.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">One-Sided Market — key facts</div>

<img src="/svg/markets.svg" alt="An abstract editorial mark for market structure and trading venues." />

<div class="wiki-infobox-caption">A red light in market structure; shows when confidence breaks down and [market makers](/market-maker-trading/) retreat.</div>

|   |   |
|---|---|
| **What it is** | Order book with bids or asks but no opposite side |
| **Also called** | No-bid market, no-ask market, asymmetric order book |
| **Duration** | Seconds to minutes; longer in crisis or delisted stocks |
| **Cause** | Liquidity collapse, [market maker](/market-maker-trading/) withdrawal, news shock |
| **Trading implication** | No execution possible; [limit orders](/limit-order/) must wait for opposite side |
| **Market maker duty** | In some stocks, [market makers](/market-maker-trading/) must maintain both sides |
| **Resolution** | [Market maker](/market-maker-trading/) re-entry, halt and repricing, or stock delisting |

</aside>

## The anatomy of a one-sided market

A functioning market has both bids and asks. The bid side shows buyers willing to purchase at specified prices; the ask side shows sellers willing to sell. The [bid-ask spread](/bid-ask-spread/) is the distance between the highest bid and the lowest ask. When that spread tightens—say, to one cent on a $100 stock—the market is efficient. When it widens, [market makers](/market-maker-trading/) are less confident and demand more compensation for the risk of holding inventory.

A one-sided market is the extreme: one side of the order book is empty. Imagine Apple stock showing $150.00 bid (with substantial size) but no ask—no one is willing to sell at any price. Alternatively, $152.00 ask with size but no bid—no one will buy. In either case, meaningful trading is impossible. A seller cannot execute against the bid without posting an ask below it and hitting their own order. A buyer cannot execute against the ask without posting a bid above it.

This condition is rare in large-cap, heavily traded stocks but common in distressed situations. A stock undergoing a corporate crisis—a failed takeover, accounting scandal, or regulatory action—can experience one-sided markets as one side (sellers, in most crises) overwhelms the other (buyers, who retreat). Similarly, stocks with poor liquidity, thinly traded securities, or those nearing delisting often show one-sided markets.

## Why [market makers](/market-maker-trading/) withdraw

The root cause is [market maker](/market-maker-trading/) risk management. A [market maker](/market-maker-trading/) is an intermediary that buys at the bid and sells at the ask, holding inventory at risk. If the market maker buys 10,000 shares at $150, it is betting the price will not fall substantially below $150 before it can resell. That bet is usually safe in a normal market; the price drifts slowly, and the [market maker](/market-maker-trading/) can exit near the entry price.

But when confidence collapses—when new information suggests the stock is worth much less—[market makers](/market-maker-trading/) refuse to buy. They pull their bids. Simultaneously, holders of the stock panic and want to sell, pushing the ask side down. If sellers dominate and [market makers](/market-maker-trading/) are absent, the ask side remains visible but the bid side evaporates. No one will quote a bid because the risk of being left holding shares is too high.

In some cases, the opposite occurs: the bid side remains while the ask side disappears. This is less common but happens when a stock is viewed as deeply undervalued or in a squeeze situation. No one wants to sell at any price because insiders or short-covering buyers are aggressively bidding. Outside sellers vanish, and the ask side clears.

[Market makers](/market-maker-trading/) are not altruistic; they withdraw when the risk-to-reward ratio tilts against them. If they quote a bid of $150 and the stock is likely to fall to $140, they lose $10 per share. They manage this risk by widening the [bid-ask spread](/bid-ask-spread/) or simply stepping back, waiting for the market to stabilize.

## The regulatory obligation to maintain markets

Regulations and [market maker](/market-maker-trading/) agreements attempt to prevent complete one-sided markets in major stocks. The SEC's Regulation SHO and self-regulatory organization (SRO) rules require [market makers](/market-maker-trading/) assigned to certain stocks to maintain "continuous two-sided quotes"—both a bid and an ask at reasonable sizes and prices, even during volatility.

For the largest stocks (S&P 500 constituents), this obligation is strong. A [market maker](/market-maker-trading/) cannot simply vanish when the stock swings 10%. They must post quotes on both sides, accepting some loss if they are caught on the wrong side of a move. This obligation prevents the most liquid stocks from becoming one-sided under normal circumstances.

However, the obligation has limits. During a [limit-up limit-down](/limit-up-limit-down-market/) halt, [market makers](/market-maker-trading/) are excused from quoting. During a trading halt imposed by regulators, the duty is suspended. And if a [market maker](/market-maker-trading/) determines that quoting is impossible without incurring unacceptable losses (e.g., during a market crash), they can apply for relief from the SEC.

For smaller stocks, the obligation is weaker or absent. A stock outside the major indexes may have a [market maker](/market-maker-trading/) assigned, but their duty is less strict, and they can withdraw during stress. One-sided markets are more tolerable in that context.

## Order book dynamics during imbalance

When a one-sided market emerges, the order book reveals the imbalance starkly. A heavily bid market might show:

- Bid: $149.95, 100,000 shares
- Bid: $149.90, 50,000 shares
- Bid: $149.85, 25,000 shares
- Ask: (empty)

Traders with shares to sell can place a market order at any price and execute immediately against the highest bid. But the price is likely to tumble because there is no ask side to provide price support. If 100,000 shares execute at $149.95 and exhaust the size, the next seller hits $149.90. A trader with 500,000 shares to sell faces a cascading collapse through the bid stack.

Conversely, in a one-sided ask market with no bids:

- Ask: $150.05, 100,000 shares
- Ask: $150.10, 50,000 shares
- Ask: $150.15, 25,000 shares
- Bid: (empty)

A buyer placing a market order to buy 500,000 shares executes at escalating prices, moving up through the ask stack. The price spikes sharply because there is no bid side to provide resistance.

In both cases, the lack of the opposite side exacerbates price moves. The lack of competition between [market makers](/market-maker-trading/) on one side removes the price stability that competition usually provides.

## Resolution and normalization

One-sided markets resolve through several mechanisms. Most often, a new [market maker](/market-maker-trading/) or dealer enters, spotting an opportunity. If the stock is massively oversold and showing no bids, a savvy trader might post a bid at a low price, knowing some value exists and sellers will eventually emerge. That first counter-order can break the ice; other [market makers](/market-maker-trading/) follow, and the order book normalizes.

Second, corporate action can restore confidence. If a distressed company announces a strategic transaction, files a restructuring plan, or brings in new leadership, confidence may return and both sides of the market revive.

Third, trading halts can reset a one-sided market. When the SEC or an exchange halts trading in a stock due to news or volatility, the halt gives the company and [market makers](/market-maker-trading/) time to absorb information and reconsider valuations. When trading resumes, a repricing mechanism (opening auction) establishes new bids and asks on both sides.

Fourth, if the fundamental situation is truly dire, the stock may be delisted. A company that cannot maintain [market maker](/market-maker-trading/) interest and exhibits persistent one-sided markets is often removed from the exchange, and trading shifts to the [over-the-counter market](/over-the-counter-market/), where quotes are even wider and one-sided markets are common.

## The investor experience in one-sided markets

For holders of a stock in one-sided markets, the experience is frustrating and expensive. A shareholder who wants to sell but sees no bids must either wait for buyers to emerge (and the stock may fall further) or place a limit order far below the last traded price to attract counter-orders. The effective execution price is usually worse than what the stock would command in a normal market.

For buyers attracted to a one-sided ask market, the situation is equally poor: the lack of selling interest may reflect genuine supply constraint, but it also often reflects desperation on one side. By the time a one-sided market is evident, much of the damage (or opportunity) has already been priced in.

Most retail brokers and institutions avoid transacting in one-sided markets when possible. They either wait for normalization or route orders to [alternative trading systems](/alternative-trading-system/) and [dark pools](/dark-pools/) in search of hidden liquidity. Large institutional trades are often negotiated off-market rather than executed through a one-sided public order book.

## See also

<div class="wiki-seealso">

### Closely related

- [Bid-ask spread](/bid-ask-spread/) — the difference between bid and ask in normal markets
- [Market maker](/market-maker-trading/) — the intermediary who maintains two-sided markets
- [Order book](/price-discovery/) — the visual representation of bid and ask imbalance
- [Market order](/market-order/) — immediate execution vulnerable to one-sided conditions
- [Limit order](/limit-order/) — resting order in search of opposite-side liquidity

### Wider context

- [Liquidity risk](/liquidity-risk/) — the broader risk of inadequate trading demand
- [Over-the-counter market](/over-the-counter-market/) — where one-sided markets are more common
- [Alternative trading system](/alternative-trading-system/) — venues where traders seek liquidity alternatives
- [Locked market](/locked-market/) — the opposite extreme of symmetry
- [Limit-up limit-down market](/limit-up-limit-down-market/) — circuit breaker addressing extreme volatility

</div>
