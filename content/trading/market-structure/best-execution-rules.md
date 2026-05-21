---
title: "Best-Execution Rules"
description: "Regulatory requirements that brokers execute customer orders at the best reasonably available prices, considering price, speed, and other factors."
---

*A broker's job is to get customers the best deal possible. The SEC requires brokers to make a "reasonable and diligent effort" to achieve best execution. This means comparing prices across [lit exchanges](/wiki/lit-venue/), [dark pools](/wiki/dark-pools/), and [market makers](/wiki/market-makers/) to find the lowest ask for a buy order or highest bid for a sell order. Best execution is not negotiable—it is a fiduciary duty.*

<aside class="wiki-infobox">
  <div class="wiki-infobox-title">Best-execution rules — key facts</div>
  <table>
    <tr><th>Regulator</th><td>SEC (Rule 10b-1)</td></tr>
    <tr><th>Broker duty</th><td>Execute at the best reasonably available terms</td></tr>
    <tr><th>Factors considered</th><td>Price, speed, likelihood of execution, size, nature, market conditions</td></tr>
    <tr><th>Enforcement</th><td>SEC, FINRA, state regulators</td></tr>
    <tr><th>Tension with</th><td>Payment for order flow</td></tr>
  </table>
</aside>

## What best execution means

Best execution doesn't mean guaranteed best price—a broker cannot know all prices in real-time across all venues. Rather, it means the broker must have a process to achieve best execution:

1. Review available venues (exchanges, [dark pools](/wiki/dark-pools/), [market makers](/wiki/market-makers/)).
2. Route the order to the venue most likely to yield the best execution.
3. Periodically review the process to ensure it's effective.
4. Disclose to customers any conflicts of interest (like [payment for order flow](/wiki/payment-for-order-flow/)).

For large retail brokers with millions of trades per day, this is typically handled by smart-order-routing algorithms. The algorithm checks [national best bid and offer](/wiki/nbbo/) (NBBO) data, splits the order if necessary across multiple venues, and executes.

## The best-execution test

The SEC's test for best execution is whether a broker's execution is as good as, or better than, what the customer could obtain under the circumstances. A broker is not required to achieve the best price under perfect conditions; it must achieve the best price reasonably available at the time of execution, given the order size and market conditions.

Example: A customer wants to buy 50,000 shares of a thinly-traded stock. The [NBBO](/wiki/nbbo/) is $100.00 bid, $100.05 ask. A broker cannot fill the entire order at $100.05 without pushing the price higher. The broker might execute 10,000 at $100.05 and then route the remaining 40,000 to a [dark pool](/wiki/dark-pools/) or use an algorithm to spread the execution over time. This is best execution.

## Conflict: best execution vs. payment for order flow

A major tension exists between best execution and [payment for order flow](/wiki/payment-for-order-flow/). When a retail broker sells an order to a [market maker](/wiki/market-makers/), the [market maker](/wiki/market-makers/) pays the broker a small fee (a fraction of a cent per share). The [market maker](/wiki/market-makers/) profits by selling shares slightly higher (or buying slightly lower) than the price they pay the broker.

The SEC allows this practice as long as:
1. The broker discloses the arrangement.
2. The broker achieves best execution overall—the execution price plus the payment for order flow should be better than routing elsewhere.

In practice, this is murky. The broker gets paid by the [market maker](/wiki/market-makers/), creating an incentive to route orders that way even if another venue might yield a slightly better price. The SEC has called this out repeatedly, fining brokers for failing to achieve best execution in favor of profit.

## Measuring best execution quality

Brokers publish quarterly reports on their best-execution practices. These reports break down volume by venue and discuss any changes to their order-routing logic. However, the reports are largely boilerplate; few brokers disclose detailed execution quality metrics.

Some research firms (like Plexus Group and Abel Noser) specialize in analyzing execution quality for institutional clients, comparing a broker's achieved prices to [VWAP](/wiki/vwap-order/) and other benchmarks.

## Exceptions for size and complexity

Large institutions can negotiate exceptions to best execution for complex orders. An institution trading a very large block of an illiquid stock might accept a wider [bid-ask spread](/wiki/bid-ask-spread/) than the [NBBO](/wiki/nbbo/) in exchange for the broker committing to execute the entire block. This is called a "negotiated trade."

Similarly, a trader who requests execution over time (a [VWAP](/wiki/vwap-order/) or [TWAP](/wiki/twap-order/) algorithm) is explicitly accepting that the executed average price may differ from a single-point-in-time best execution price.

## International variations

Europe's MiFID II directive has stricter best-execution rules than the U.S. SEC. MiFID II requires explicit approval from the customer before a broker can route to a [dark pool](/wiki/dark-pools/), and requires brokers to achieve "best execution in terms of total consideration, representing the best possible result in terms of the total cost and fees involved."

This is more stringent than the U.S. rule, which focuses primarily on price and speed separately rather than total cost.

## Enforcement

The SEC, FINRA, and state regulators can bring enforcement actions against brokers for best-execution failures. Common violations include:
- Routing orders to [dark pools](/wiki/dark-pools/) operated by affiliates to earn fees, even when a lit exchange would be cheaper.
- Failing to monitor execution quality or updating routing logic.
- Failing to disclose conflicts of interest.

Penalties range from fines to restitution to customers. In recent years, the SEC has brought cases against major retail brokers (Robinhood, E-Trade) for order-routing conflicts.

<div class="wiki-seealso">
<h2>See also</h2>
<h3>Closely related</h3>
<ul>
  <li><a href="/wiki/payment-for-order-flow/">Payment for order flow</a> — the main conflict with best execution.</li>
  <li><a href="/wiki/national-best-bid-and-offer/">National best bid and offer</a> — the benchmark for best execution.</li>
  <li><a href="/wiki/smart-order-router/">Smart order router</a> — technology for achieving best execution.</li>
</ul>
<h3>Wider context</h3>
<ul>
  <li><a href="/wiki/broker/">Broker</a> — subject to best-execution duties.</li>
  <li><a href="/wiki/dark-pools/">Dark pools</a> — alternative venue for best-execution routing.</li>
  <li><a href="/wiki/sec/">SEC</a> — enforcer of best execution rules.</li>
</ul>
</div>
