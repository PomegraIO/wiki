---
title: "Payment for Order Flow and Venue Routing"
description: "How payment for order flow affects where trades are routed—brokers receive compensation for directing retail orders to specific execution venues, with trade-offs for fill quality."
keywords:
  - payment for order flow
  - order routing
  - execution venue
  - retail order flow
  - broker compensation
  - market maker
  - internalization
---

*When a retail investor places a trade through a broker, that broker doesn't necessarily execute it on a traditional stock exchange. Instead, **payment for order flow** is a system where brokers receive cash compensation for directing orders to specific venues—a practice that subsidizes commission-free trading but creates an inherent conflict of interest in routing decisions.*

## What Payment for Order Flow Is

Payment for order flow (PFOF) is compensation a broker receives from a market maker, alternative trading system, or exchange for the right to execute customer orders. In essence, a broker sells access to its order flow to the highest bidder—often a large market maker like Citadel Securities or Virtu Financial—rather than routing orders directly to a stock exchange.

The broker's revenue stream is often the payment it receives from the execution venue, not (or not solely) from customer commissions. This model has made zero-commission brokers economically viable. A retail investor pays nothing to place a trade, but the broker is paid by whoever executes it.

For the venue receiving the order flow, the economic logic is straightforward: market makers profit by capturing the bid-ask spread. If they can execute a high volume of retail orders—often small, less informed trades—they can monetize the difference between what they pay and what they collect.

## How Venue Routing Decisions Work

A broker's order routing rules specify where customer orders go. These rules must be documented in the [broker's form 4530](https://www.finra.org) filing and made available to customers, but they contain considerable discretion.

The routing algorithm typically considers:

- **Execution quality**: Price improvement, speed, and likelihood of full execution.
- **Payment received**: The amount the venue is willing to pay for the order.
- **Order characteristics**: Size, type (market or limit), and asset class.

In practice, payment for order flow often dominates routing decisions. A market maker paying $0.003 per share for small retail orders can fill them at prices competitive with or slightly better than the exchange, pocket the spread, and still profit handsomely at volume. The broker collects its fee and moves on.

The conflict arises because the broker's incentive (maximize PFOF revenue) and the customer's incentive (best execution price and certainty) do not always align.

## Execution Quality: Trade-Offs and Reality

When a broker directs an order to a PFOF venue, does the customer get a fair price?

Empirically, the answer is mixed. Academic research and regulatory studies have found that:

1. **Price improvement sometimes occurs**: Market makers can and do offer prices better than the national best bid or ask (NBBO) to win order flow. A customer market order might fill at a marginally better price than the public quote.

2. **The spread is internalized**: Rather than competing on a public exchange, the market maker executes against its own inventory. This eliminates the public price discovery process for that order.

3. **Speed and certainty vary**: Orders sent to market makers typically execute faster than exchange orders, which appeals to retail traders. However, a market maker can also reject or partially fill an order if the price moves.

4. **Information leakage is possible**: Because the venue knows the order is retail (small, likely unsophisticated), it can adjust its pricing strategy accordingly, potentially widening spreads on subsequent related orders.

A $100 stock with a $0.01 bid-ask spread on the exchange might execute through a PFOF venue at $99.995 bid or $100.005 ask—a small improvement. But if that market maker's data scientists infer from the order's size and timing that retail demand is rising, they may widen spreads on the next wave of related orders, offsetting the initial gain elsewhere in the market.

## The Regulatory and Competitive Landscape

The [Securities and Exchange Commission](https://www.sec.gov) has intensified scrutiny of PFOF over the past decade. In 2020 and again in 2021, the SEC issued guidance stating that payment for order flow, by itself, does not violate best execution rules—but it does create a heightened obligation for brokers to demonstrate that routing decisions genuinely serve customer interests.

The tension became acute during the 2021 meme stock episode: retail investors discovered that major brokers (most notably Robinhood) had restricted buying in volatile stocks, citing liquidity concerns from their PFOF partners. This sparked congressional interest and SEC reviews questioning whether PFOF creates systemic conflicts.

Some brokers—including [E*TRADE](https://www.etrade.com), [Charles Schwab](https://www.schwab.com), and certain others—have publicly stated they do not accept PFOF or limit it, instead routing to exchanges and charging subscription fees or monetizing other services. This positioning appeals to investors concerned about conflicts of interest.

## Why Brokers and Market Makers Participate

For brokers, PFOF economics are compelling: it enables a business model with zero commissions and minimal customer friction. A broker that must charge per-trade commissions cannot compete against one subsidized by PFOF revenue.

For market makers, the arrangement is profitable if they can consistently execute at or better than public quotes and profit from the spread. The largest beneficiaries have been high-frequency trading firms that can afford sophisticated technology to execute retail orders efficiently and hedge exposure across multiple securities and venues.

## The Fine Print: Disclosure and Opt-Out

Brokers are required to disclose PFOF arrangements to customers and provide regular reporting on where orders are routed and what prices were achieved. However, this disclosure is often buried in terms of service or trading statistics—not front-and-center at account setup.

Customers rarely have a true opt-out: if a broker directs all flow to PFOF venues and does not offer alternative routing, the customer either accepts it or switches brokers. A handful of brokers now offer "directed order routing" for a per-order fee, returning some choice to the customer but at a cost.

## See also

<div class="wiki-seealso">

### Closely related

- [Market Maker Trading](/market-maker-trading/) — How market makers profit from the bid-ask spread and internalize retail order flow
- [Alternative Trading System](/alternative-trading-system/) — Off-exchange venues where PFOF arrangements often concentrate
- [Bid-Ask Spread](/bid-ask-spread/) — The cost embedded in each trade that PFOF venues aim to capture
- [Best Execution](/best-execution/) — The regulatory standard brokers must meet, heightened when PFOF is present
- [Over-the-Counter Market](/over-the-counter-market/) — Where much internalized order flow ultimately settles

### Wider context

- [Stock Exchange](/stock-exchange/) — Traditional venues whose market share has eroded due to PFOF practices
- [Broker](/broker/) — The intermediary balancing customer service against revenue maximization
- [Securities and Exchange Commission](/securities-and-exchange-commission/) — The regulator responsible for overseeing order routing and execution quality
- [Market Capitalization](/market-capitalization/) — The size of companies whose order flow attracts PFOF competition

</div>
