---
title: "Request-for-Quote Platform"
description: "A trading venue where buyers solicit competing dealer quotes for a specific trade size before executing."
keywords:
  - request for quote
  - rfq platform
  - dealer quotes
  - over-the-counter trading
  - institutional trading
image: "/svg/markets.svg"
---

*A **request-for-quote (RFQ) platform** is a trading venue where a buyer specifies a desired security, quantity, and other trade parameters, then solicits competing price quotes from multiple dealers before execution. Unlike continuous bid-ask markets, RFQ platforms operate on demand—quotes appear only when requested—and are built around the dealer's ability to manage balance-sheet risk and inventory. They remain the backbone of institutional trading in fixed income, currencies, and many derivatives.*

## Why RFQ platforms exist

Continuous markets work well for highly liquid instruments where large volumes trade daily and dealers can easily hedge their positions. But institutional investors buying or selling large blocks of less-liquid securities face a dilemma: hitting a single dealer's quote on the screen risks poor execution, yet calling multiple dealers by phone is slow and leaves no transparent record.

RFQ platforms solve this by creating a structured auction. A client submits a single request—"I want to buy £5 million of this bond"—and receives simultaneous price quotes from many dealers. The platform creates competition without requiring phone lines, dealers can reprice as market conditions shift between requests, and the buyer can choose the best fill or negotiate further. For securities that trade infrequently, this is far superior to taking whatever quoted price appears first.

## How they operate in practice

A typical RFQ session unfolds in stages. The buyer (or their sales trader) logs into the platform, selects the security and desired quantity, and hits "send." The system routes the request to a pre-selected list of dealers or broadcasts it to all connected market-makers. Dealers receive the enquiry, check their inventory and risk limits, and respond with their best bid or offer within a set time window—often 30 seconds to 2 minutes depending on the asset class and platform rules.

The buyer then sees all quotes ranked by price and can hit (accept) the best one immediately, or in some platforms, counter-offer to negotiate further. Once a quote is accepted, the trade is binding and settlement details are handled by the platform or by the counterparties directly. The entire process creates an audit trail: timestamps, all quotes received, the quoted price, and execution record—critical for compliance and dispute resolution.

RFQ platforms vary by asset class and geography. [Bond](/bond/) RFQ platforms are standard in corporate and government debt; [currency](/currency-volatility/) platforms serve forex traders; and [derivatives](/option/) platforms allow institutions to request prices on bespoke swaps or structures. Some platforms are dealer-owned consortiums; others are independent operators that charge a fee per quote or per executed trade.

## The balance between anonymity and liquidity

Many RFQ platforms allow a buyer to submit a request anonymously—dealers respond to the price enquiry without knowing who the buyer is. This protects the buyer from tipping off the market that a large position is moving and potentially moving the price against them before all quotes arrive. However, some dealers will quote tighter (better) prices if they know the counterparty is credit-worthy and likely to settle. A trade-off emerges: anonymity prevents information leakage but can widen spreads.

Some platforms offer a hybrid approach: the buyer can remain anonymous during the quote phase, but dealers see their identity only if their quote is selected. Others allow the buyer to reveal themselves if they wish, betting that a known, quality counterparty will trigger better quotes. Dealers manage this by using the buyer's information to assess credit risk and likelihood of settlement.

## Comparison with other venues

RFQ platforms sit between the fully transparent continuous [stock exchange](/stock-exchange/) and the entirely bilateral over-the-counter market. An exchange like the [NYSE](/new-york-stock-exchange/) publishes firm bid and ask prices continuously; a dealer makes a bilateral call to another dealer and negotiates privately. An RFQ platform is a middle ground: structured enough to attract many dealers and create real competition, but still dealer-driven rather than order-book-driven.

Unlike [alternative trading systems](/alternative-trading-system/) (ATS) that match buy and sell orders passively, RFQ platforms require active dealer participation. A dealer must actively quote prices, manage inventory, and take on risk. This is why RFQ platforms dominate fixed income and currencies—sectors where dealers have deep expertise and where trade sizes are large enough to justify active risk-taking.

## Regulatory status and evolution

RFQ platforms are typically lightly regulated compared to exchanges, though they fall under the oversight of bodies like the [SEC](/securities-and-exchange-commission/) (in the US) or FCA (in the UK). Under [MiFID II](/dodd-frank-act/) in Europe, certain RFQ platforms must be classified as systematic internalisers or regulated trading venues, with transparency and execution quality requirements.

The rise of electronic RFQ platforms has accelerated in recent years, partly driven by regulatory pressure for transparency but also by dealers and clients valuing speed and the ability to quote from algorithms rather than human traders. Platforms now increasingly integrate with dealer pricing engines, allowing quotes to be generated and updated in milliseconds. Yet human judgment still matters—a complex [bond](/bond/) situation or market stress event often prompts dealers to stop quoting electronically and revert to phone calls.

## Costs and execution quality

Using an RFQ platform typically incurs a fee: either a flat charge per quote, a per-trade fee, or a percentage of the notional amount. For large, frequent traders these fees are often negotiated. The key execution metric is how tight the spread is—the difference between the best bid and best offer received. Spreads depend on market conditions, the size requested, the liquidity of the security, and how many dealers quote.

In stress or low-liquidity periods, some dealers may withdraw from the platform entirely, shrinking the pool of quotes and widening spreads. Conversely, in normal markets with many dealers competing, RFQ platforms can produce very tight pricing, especially for large sizes that would be hard to execute on an exchange or via a single dealer.

## See also

<div class="wiki-seealso">

### Closely related

- [Alternative trading system](/alternative-trading-system/) — regulated off-exchange venues for matching buy and sell orders
- [Over-the-counter market](/over-the-counter-market/) — bilateral dealer networks for instruments not listed on exchanges
- [Broker](/broker/) — intermediary that routes client orders, often via RFQ platforms
- [Market maker](/market-maker-trading/) — dealer who provides two-sided prices and absorbs inventory risk
- [Bid-ask spread](/bid-ask-spread/) — the difference between dealer quotes, narrowed by RFQ competition
- [Internalization pool](/internalization-pool/) — broker's internal matching engine that competes with RFQ platforms
- [Systematic internaliser](/systematic-internaliser/) — regulated dealer quoting to clients at size

### Wider context

- [Bond](/bond/) — fixed-income instruments where RFQ platforms are most prevalent
- [Currency risk](/currency-risk/) — forex and derivatives trading heavily uses RFQ platforms
- [Price discovery](/price-discovery/) — process by which markets establish fair prices
- [Dodd-Frank Act](/dodd-frank-act/) — US regulation governing venue and dealer conduct

</div>
