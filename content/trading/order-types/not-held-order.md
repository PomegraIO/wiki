---
title: "Not-Held Order"
description: "A discretionary instruction that releases the broker from liability for execution timing and price, granting them latitude in execution strategy."
keywords:
  - not held order
  - discretionary order
  - broker discretion
  - execution timing
  - block trading
image: "/svg/trading.svg"
---

*A **not-held order** is an instruction to buy or sell a security that explicitly authorizes the broker to exercise discretion over both timing and price, with the understanding that the client will not hold the broker liable for the execution outcome. In essence, the client trades certainty of execution for the broker's flexibility to work the order at optimal market conditions, free from the legal obligation to execute immediately or at a specific price.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Not-Held Order — key facts</div>

<img src="/svg/trading.svg" alt="An abstract editorial mark for trading mechanics." />

<div class="wiki-infobox-caption">Discretion swapped for latitude in execution.</div>

|   |   |
|---|---|
| **What it is** | A broker-discretionary order where client releases standard execution guarantees |
| **Also called** | Discretionary order, work order, at-best order (in some markets) |
| **Broker discretion** | Timing, price, and routing; no obligation to execute immediately |
| **Client liability** | Client accepts outcome; cannot claim execution failure or slippage as breach |
| **Common use** | Large block trades, illiquid securities, volatile periods requiring flexibility |
| **Regulatory requirement** | Broker must still act in client's best interest; discretion is not a license to abuse |

</aside>

<div class="wiki-hatnote">

For the conditional order that activates based on specified market events, see [Conditional Order](/conditional-order/).

</div>

## The principle of release and flexibility

A not-held order inverts the standard risk allocation between broker and client. In a normal [market order](/market-order/) or [limit order](/limit-order/), the broker assumes responsibility for execution: they must execute the market order immediately at best available prices, or fill the limit order when the price is reached. If execution fails or slippage is substantial, the client has recourse.

A not-held order, by contrast, releases the broker from these contractual obligations. The client is saying: "I authorize you to use your judgment about when and at what price to execute this, and I will not hold you liable for the result." This freedom is especially valuable when dealing with large orders, illiquid securities, or volatile markets where immediate execution would either be impossible or catastrophically expensive.

The not-held instruction is typically written as "NHO" or "DNH" (do not hold) in order tickets, signalling to the executing broker or trader that they may use discretion.

## Why a client would grant discretion

The primary motivation is **execution quality in difficult circumstances**. Suppose an institutional investor wants to buy 500,000 shares of a stock with a daily volume of 2 million shares. A market order of that size would move the price significantly—a phenomenon called market impact. By handing the order to a broker with not-held status, the client implicitly trusts the broker to "work" the order over time, using various tactics: splitting it into smaller batches, using alternative venues and dark pools, timing around natural order flow, even pausing if sentiment turns adverse.

A broker armed with not-held discretion can make judgment calls that a client-constrained market order cannot. They might execute half the order aggressively, then pause for 20 minutes to let momentum fade. They might use algorithms to route pieces to [alternative trading systems](/alternative-trading-system/) where the order will incur less market impact. In a volatile market, they might wait for a temporary liquidity flush to execute quickly, knowing they are not liable if the window closes.

This is especially important in **block trading** and **over-the-counter** markets, where price discovery is opaque and immediate execution often forces the trader into a dealer's quoted spread. A not-held order gives the block trader permission to negotiate, shop the order discreetly, and execute pieces at varying prices and times—strategies that would violate the terms of a market order.

## The liability trade-off

The cost of this flexibility is explicit: the client waives the right to sue or claim damages if execution is unfavourable. If a broker executes a not-held order at a worse price than the market price that existed moments before, the client cannot claim breach. If the broker waits and a price gap occurs before execution, the client cannot claim the broker should have acted faster.

However, this waiver has limits. The broker still operates under a **best execution** obligation—they must still execute in a manner that is reasonably consistent with the client's interests. A not-held order is not a license to deliberately execute poorly or to fill the order against the broker's own inventory at an unfair price. Regulators (particularly the SEC and FINRA in the US) have made clear that brokers cannot use the not-held designation as cover for conflicts of interest or obvious self-dealing.

## Operational mechanics

A not-held order typically goes to a specific trader or desk at the broker, rather than to a standard electronic routing system. The trader then becomes an agent with discretion to execute over a period of time—usually the trading day, though the client can specify a longer or shorter window.

The trader might use several execution tactics:
- **Time-weighted averaging**: execute portions proportionally throughout the day to minimize market-impact cost.
- **Volume participation**: execute on spikes of natural buy-side or sell-side volume.
- **Price-responsive execution**: accelerate during price moves that are favourable, decelerate or pause during unfavourable moves.
- **Venue routing**: split pieces among lit markets, dark pools, and broker crossing networks to optimize prices and liquidity.

At the end of the trading day or window, the broker reports back to the client with the filled quantity, average price, and execution report. The client has no recourse to object on execution grounds; the trade is final once confirmed.

## When not-held orders are preferred

Not-held orders are standard in **institutional block trading**, where a pension fund, mutual fund, or [hedge fund](/hedge-fund/) is managing a large position change. They are also common in **trading desk operations**, where a trader wants to exit a large inventory position over a few hours without crashing the market.

Not-held orders are less useful—and rarely granted—in retail trading or small orders. The benefit of discretion diminishes when the order is small relative to market volume; the cost of releasing liability remains the same. A retail client placing a 100-share order has little to gain by allowing the broker discretion, since the order will likely execute as a market order instantly anyway.

They are also less relevant in highly liquid, actively traded securities (such as large-cap stocks or ETFs) where [market impact](/price-discovery/) is minimal and execution risk is low. Their value increases sharply as liquidity decreases or order size relative to volume increases.

## Regulatory framework and best execution

In many jurisdictions, brokers are required to inform clients that a not-held order releases them from certain execution guarantees. Some regulators (such as FINRA) have specific requirements about how not-held orders must be documented and how the client's consent must be obtained.

The US SEC's Regulation SHO and Regulation FD also impose constraints: a not-held order cannot be used to circumvent short-selling rules or to execute on material non-public information. The broker's discretion is bounded by law and regulation, even though the client has waived contractual recourse.

In institutional settings, not-held orders are often governed by side letters or standing instructions between the client and the broker, specifying the exact conditions under which the discretion may be exercised.

## Not-held vs. other discretionary approaches

A not-held order differs from a [conditional order](/conditional-order/), which remains dormant until a specified event; a not-held order is active immediately but with the broker's execution timing and price unrestricted. It also differs from algorithmic or "algorithms-as-a-service" orders, where a client selects a specific execution algorithm (e.g., TWAP, VWAP) and the broker commits to following that algorithm—less discretion, more specificity.

## See also

<div class="wiki-seealso">

### Closely related

- [Market Order](/market-order/) — immediate execution at best available prices
- [Limit Order](/limit-order/) — execution only at specified price or better
- [Conditional Order](/conditional-order/) — order activated by a specified market condition
- [Algorithmic Trading](/algorithmic-trading/) — automated execution strategies with pre-defined logic
- Block Trading — large off-market or negotiated trades between institutions

### Wider context

- [Market Maker Trading](/market-maker-trading/) — how brokers internalize and execute orders
- [Market Impact](/price-discovery/) — cost of large orders on equilibrium prices
- [Alternative Trading System](/alternative-trading-system/) — venues outside lit exchanges for execution
- [Over-the-Counter Market](/over-the-counter-market/) — markets for negotiated trades without centralized pricing

</div>
