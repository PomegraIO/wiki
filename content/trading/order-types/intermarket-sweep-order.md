---
title: "Intermarket Sweep Order"
description: "A Reg NMS order that sweeps multiple venues at once, bypassing the traditional best-price protection requirement to fill large orders across markets."
keywords:
  - intermarket sweep order
  - ISO order
  - regulation NMS
  - best execution
  - venue routing
image: "/svg/trading.svg"
---

*An **intermarket sweep order** (ISO) is a form of order that allows a trader to sweep multiple venues simultaneously without being bound by the national best bid and offer (NBBO). Rather than waiting to interact with the best displayed price on a single market, an ISO executes across multiple venues in a controlled, predefined sequence—making it a tool for large traders who need rapid cross-venue access.*

## Why the NBBO rule exists

The NBBO is the cornerstone of modern US equity market structure. When you submit an order, brokers are required to route it in a way that satisfies the national best bid or offer—meaning they must first check whether a better price is available elsewhere before executing. This [order protection rule](/regulation-sho/) (subregulated under [Regulation National Market System](/regulation-sho/)) prevents traders from being disadvantaged by fragmented venue coverage.

But the protection comes with a cost: it introduces latency. A trader who needs to fill 100,000 shares and sees the best bid at one exchange must technically respect orders queued at other exchanges, even if those queues are shallow or moving slowly. For large institutional orders, that delay can mean slippage or, worse, being "picked off" by faster algorithms.

## How an ISO sweeps

An intermarket sweep order solves this latency problem by obtaining an express exception to the NBBO rule. To be valid, an ISO must:

- Be marked or otherwise identified as an ISO in the [order routing](/price-discovery/) system
- Actively sweep through multiple markets in a single execution attempt, without delay between legs
- Execute simultaneously or near-simultaneously across venues, rather than sequentially

Practically, this means a trader can submit a 100,000-share buy order as an ISO and have it simultaneously query the best offer on NASDAQ, NYSE, and several alternative venues, filling from the most attractive quotes in one fast sweep. The broker does not need to queue behind orders at the national best price; instead, it can execute the entire sweep in milliseconds.

## Key distinctions from standard orders

A standard [market order](/market-order/) or [limit order](/limit-order/) respects the NBBO passively: the broker routes to the best venue and waits its turn. An ISO is active and aggressive—it bypasses the queue at the national best price in favour of speed and certainty of fill.

An ISO is also different from a [dark pool](/over-the-counter-market/) order. Dark pools are lit venues where prices are not publicly displayed; an ISO can be used *to* a dark pool, but the ISO itself is the execution method, not the venue. A trader might submit an ISO to a combination of lit exchanges and dark pools simultaneously.

## Execution constraints

ISOs are strictly regulated. The [Securities and Exchange Commission](/securities-and-exchange-commission/) permits ISOs only when:

- The broker can demonstrate that the order is being swept to multiple venues in a single attempt
- The sweep respects each venue's displayed offer (or bid, if selling)
- The issuing broker marks the order properly so clearing and compliance teams can audit it

This last point is critical. Improperly marking an order as an ISO when it is not, or marking a sequential multi-leg order as an ISO, is a violation. Compliance departments at major brokers have entire teams dedicated to order-marking audits.

## Who uses ISOs and why

ISOs are the domain of large institutional traders, algorithmic desks, and HFT firms. A retail investor with a 1,000-share order has no real need for an ISO—the NBBO protection is already fast enough, and the latency savings are not material.

But a pension fund executing a $50 million block position can shave basis points off its average price by using an ISO to simultaneously access all liquid venues. Over a single trade, that might save $5,000 to $50,000, depending on market conditions. Aggregated across thousands of large trades a year, the savings are substantial.

Proprietary trading firms use ISOs to react to market events in microseconds. If a large seller appears on NASDAQ and an HFT algorithm detects an arbitrage between NASDAQ and NYSE, an ISO allows the firm to sweep both venues before the pricing dislocation closes—something that would be impossible under purely sequential NBBO routing.

## Risks and criticism

The downside of ISOs is that they erode the NBBO protection for smaller orders on any given venue. If a large ISO sweeps across five venues simultaneously, the smallest quotes on each venue get filled first, and the remaining volume has to wait. For a [market maker](/market-maker-trading/) or smaller trader with a resting order, that can mean a filled order at a worse price than the national best offer.

Some critics argue that ISOs, combined with [latency arbitrage](/algorithmic-trading/) and high-frequency trading, have fragmented the market and made it harder for ordinary traders to find truly fair prices. Defenders counter that ISOs are essential for efficient large-order execution and that the speed they enable actually improves price discovery overall.

The debate mirrors a broader tension in market structure: speed and efficiency for large traders versus protection and transparency for smaller ones. ISOs tilt the market toward the former—and they do so deliberately.

## See also

<div class="wiki-seealso">

### Closely related

- [Regulation National Market System](/regulation-sho/) — the framework that defines best execution and the NBBO
- [Market Order](/market-order/) — the simplest order type; respects NBBO passively
- [Limit Order](/limit-order/) — allows traders to specify a price; queued in NBBO respect
- [Dark Pool](/over-the-counter-market/) — non-lit venues where ISOs are often routed
- [Order Protection Rule](/regulation-sho/) — the NBBO rule that ISOs are designed to bypass
- [Price Discovery](/price-discovery/) — the mechanism by which markets set fair prices

### Wider context

- [Stock Exchange](/stock-exchange/) — venues that ISOs interact with
- [Algorithmic Trading](/algorithmic-trading/) — the trading method that most uses ISOs
- [Market Maker Trading](/market-maker-trading/) — liquidity providers affected by ISO sweeps
- [Bid-Ask Spread](/bid-ask-spread/) — the gap that ISOs navigate
- [Securities and Exchange Commission](/securities-and-exchange-commission/) — regulator that defined ISO rules

</div>
