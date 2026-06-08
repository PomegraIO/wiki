---
title: "Immediate or Cancel Order"
description: "An order executed instantly for available quantity, with any remainder cancelled rather than held."
keywords:
  - immediate or cancel order
  - ioc order
  - fill-or-kill variant
  - aggressive order
  - execution immediacy
image: "/svg/trading.svg"
---

*An **Immediate or Cancel (IOC) order** is an instruction to a broker to execute your buy or sell immediately for whatever quantity is available at the current [bid-ask spread](/bid-ask-spread/), and to automatically cancel any portion that cannot be filled in that instant. It prioritises speed over patience.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Immediate or Cancel Order — key facts</div>

<img src="/svg/trading.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Instant execution, zero patience for unfilled quantities.</div>

|   |   |
|---|---|
| **What it is** | A time-sensitive order that trades any available quantity immediately, then cancels the rest |
| **Also called** | IOC order, fill-and-cancel |
| **Execution window** | Milliseconds to a second; must trade or disappear |
| **Partial fills** | Allowed; unfilled portion is cancelled automatically |
| **Best for** | High-frequency traders, rapid position adjustments, precise exit timing |
| **Opposite approach** | [Good Till Date Order](/good-till-date-order/), Good Till Cancel Order (patient, standing orders) |

</aside>

## The logic of instant execution

An IOC order embodies a trader's decision to move *now*. Rather than wait for a larger order book to develop or for prices to move in your favour, you accept whatever execution is available in the next moment. The tradeoff is clear: you get speed and certainty of *some* fill, but you abandon the hope of a better price or a larger quantity.

Consider a scenario: a sudden news catalyst moves the market, and you want to cut a position immediately to avoid further loss. An IOC order lets you exit in milliseconds, capturing the current bid price. If only 70% of your shares find buyers at that price, the remaining 30% are simply cancelled—you don't own them anymore. This is fundamentally different from a [limit order](/limit-order/) or [market order](/market-order/) left standing, which would wait passively for execution.

## IOC versus fill-or-kill

IOC is sometimes confused with **fill-or-kill (FOK)**, but they differ in a crucial way. A fill-or-kill order demands 100% of the order size; if the entire quantity cannot be matched immediately, the entire order is cancelled. An IOC is more flexible: it accepts whatever fills it can get and discards the rest.

In practice, FOK is far rarer and more restrictive. IOC is the standard time-sensitive order when partial execution is acceptable. For a trader trying to exit a large position quickly, IOC lets the first 10,000 shares execute while cancelling the remaining 5,000; with FOK, if all 15,000 cannot trade in one millisecond, the whole order dies.

## Where IOC shows its teeth

IOC orders are the domain of [algorithmic traders](/algorithmic-trading/) and high-frequency operations. When a trading algorithm detects a fleeting price anomaly and needs to arbitrage it, the window is measured in microseconds. An IOC order ensures the algorithm doesn't accidentally leave resting orders behind that might execute hours later at the wrong price.

Retail traders also use IOC in volatile moments. During a market crash or a stock's earnings announcement, [volatility](/historical-volatility/) spikes and the bid-ask spread widens. An IOC order guarantees you don't get stranded: you either execute at the current spread or you don't execute at all. There's no ambiguity, no mystery order sitting in the market hours later.

Institutions deploying large blocks of capital sometimes use IOC to gauge market appetite. A trader might submit a 50,000-share IOC buy order; if only 10,000 shares fill, the market is thin and other buyers are scarce. If all 50,000 fill instantly, liquidity is plentiful and the trader knows they can push harder on the next tranch.

## Execution mechanics and exchange rules

When you submit an IOC order, the exchange or [market maker](/market-maker-trading/) matches it against the current order book in a single pass. Any quantity that matches is executed; anything left over is cancelled. The entire lifecycle happens in microseconds, often faster than you could cancel a manual order.

Different venues have different IOC implementations. Stock exchanges like the [New York Stock Exchange](/new-york-stock-exchange/) and [NASDAQ](/nasdaq/) support IOC natively. [Over-the-counter markets](/over-the-counter-market/) and some [alternative trading systems](/alternative-trading-system/) may handle it differently. Always confirm your exchange's specific handling.

IOC orders cannot be modified or cancelled after submission because there's nothing left to modify—if any portion filled, it's already executed, and if nothing filled, the order is dead. This immediacy is the whole point.

## Cost and market impact

Because IOC orders demand instant execution, they often accept worse prices than a patient [limit order](/limit-order/) would eventually receive. If you want to sell 1,000 shares immediately via IOC and the current bid is £50, you'll likely get that bid, even if the offer is £50.05. A limit order at £50.05 might wait hours, but it never hits the bid.

The flip side: IOC orders are transparent and leave no lingering doubt. There are no stale orders sitting for days, no risk of an accidental fill after corporate restructuring. Regulators and compliance teams often prefer IOC over Good Till Cancel orders because the duration risk is eliminated.

## When IOC is not the right tool

IOC makes no sense for patient investors with medium-term conviction. If you believe a stock will eventually reach £55 and you're willing to wait two weeks, an IOC order buying at £55 is pointless—it will just cancel if the price hasn't reached there yet. In this case, a [Good Till Date Order](/good-till-date-order/) or GTC order serves better.

Similarly, IOC is overkill for routine, non-urgent trades. If you're adding to a long-term position and can wait for a better price, you don't need the expense (in terms of potential market impact or foregone price improvement) of an IOC.

## See also

<div class="wiki-seealso">

### Closely related

- [Good Till Date Order](/good-till-date-order/) — a patient order that waits until a specified date
- Good Till Cancel Order — a standing order with no expiration
- [Market Order](/market-order/) — similar immediacy, but no explicit cancellation clause
- [Limit Order](/limit-order/) — patient order waiting for a specific price
- [Market on Open Order](/market-on-open-order/) — time-pegged to opening auction
- [Market on Close Order](/market-on-close-order/) — time-pegged to closing auction
- [Algorithmic Trading](/algorithmic-trading/) — the prime domain for IOC orders
- Order Book — where IOC orders are matched against resting liquidity

### Wider context

- [Market Maker Trading](/market-maker-trading/) — how orders are filled
- [Bid-Ask Spread](/bid-ask-spread/) — the price IOC orders typically accept
- [Stock Exchange](/stock-exchange/) — where IOC orders are routed
- [Price Discovery](/price-discovery/) — role of aggressive orders in market formation
- [Volatility Smile](/volatility-smile/) — markets where IOC orders are most useful

</div>
