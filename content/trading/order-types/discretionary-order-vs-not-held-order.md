---
title: "Discretionary Order vs Not-Held Order"
description: "Discretionary limit orders let traders set price, not timing; not-held orders let brokers choose both timing and price. Learn when execution responsibility shifts."
keywords:
  - discretionary order vs not held order
  - discretionary limit order
  - not-held order
  - broker discretion trading
  - order execution responsibility
---

*A **discretionary order** lets the trader lock in a maximum price while a broker handles timing; a **not-held order** gives the broker complete discretion over both price and timing. The distinction matters because it shifts who bears the risk if the market moves between when the order enters and when it fills.*

## The core difference

The two orders solve different trader problems. A discretionary limit order is the simpler: you set a price floor (for selling) or ceiling (for buying), and the broker can wait or act immediately—but the fill price stays protected. A not-held order removes that protection entirely. You're telling the broker, "Execute this on your own timing and at whatever price you think best." It's a handoff of both timing and price authority to the trading desk.

In practice, discretionary orders appear on many retail platforms under generic "Limit Order" labels, though the discretionary window varies. Not-held orders were historically used in block trades and institutional markets; they're rarer in modern retail trading but still used in OTC and direct institutional negotiations.

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Order Execution — Key Differences</div>

<img src="/svg/trading.svg" alt="An abstract editorial mark for the trading topic." />

<div class="wiki-infobox-caption">Discretion and responsibility rest differently in each order type.</div>

|   |   |
|---|---|
| **Trader sets price** | Discretionary: Yes. Not-held: No. |
| **Broker controls timing** | Discretionary: Yes. Not-held: Yes. |
| **Broker can cross the price** | Discretionary: No. Not-held: Yes. |
| **Trader bears slippage risk** | Discretionary: Limited. Not-held: Full. |
| **Common use** | Retail limit orders. Block trades, institutional OTC. |
| **Regulatory notation** | "DNR" (Do Not Reduce), "DTC." | "Not Held" or "Disregard Tape" field. |

</aside>

## Why a trader chooses a discretionary order

A discretionary limit order appeals to traders who want to cap their downside (or upside) but don't care when the fill happens. If you're selling 1,000 shares of XYZ and you'll accept $50 or better, but not $49.99, a discretionary order protects that floor. The broker can execute the moment $50 hits, or wait if they think $50.50 is coming. Your price constraint is rock-solid.

The "discretionary" part historically meant the trader gave the broker a discretionary band—say, "I want $50, but use your judgment within $0.25 of that"—but modern usage has narrowed it. Most retail discretionary orders are simply limit orders with a note that the broker can time the execution. The trader still controls the price.

## Why a trader might use a not-held order

Not-held orders appear when a trader prioritizes speed or concealment over price certainty. In block trading, a client might tell a broker, "I need to move 500,000 shares quietly. I don't want to move the market. Execute at the best price you can get without broadcasting the full size." The broker then becomes the decision-maker on fill price, potentially breaking the block across multiple executions to minimize market impact.

A not-held order also makes sense when you trust your broker's execution algorithm more than you trust your own timing. Some traders use them in after-hours or over-the-counter markets where the price discovery process is less transparent anyway.

## Execution responsibility and market risk

The legal and practical difference hinges on responsibility. With a discretionary order, the trader accepts the risk that the price might never hit, but if it does, they get it. With a not-held order, the trader hands off the judgment call. If the broker executes at a worse price than the market offered, the trader usually has no recourse—the broker was "not held" to the market's best available price.

This matters in volatile or gapped markets. If you place a not-held order to sell, and the market gaps down before the broker decides to execute, you absorb the gap. The broker's only obligation is to act in good faith, not to hit a pre-specified price level.

## Modern context and decline of not-held

The SEC and FINRA have long scrutinized not-held orders because they create agency ambiguity. In modern electronic markets, where order routing is heavily regulated and time stamps are microsecond-precise, true not-held orders have become less common in retail. Most stock brokers now offer only limit orders (a type of discretionary order) or market orders, which execute immediately at the best current price.

Not-held orders persist in less transparent venues: bonds, forex, commodities, and institutional equity blocks. They also exist in equities as a negotiation tool between institutional traders and their brokers, often documented in trade affirmation rather than appearing as a standard order type on a platform.

## When to use each

Use a discretionary order (limit order) if you have a price in mind and can wait for it to hit, or if you want to set a strict entry or exit target. Use a not-held order only if you trust your broker's execution judgment, are in an institutional or OTC context where the broker's algorithms or relationships matter, and you prioritize execution velocity or anonymity over price certainty.

For most retail traders, the distinction is academic. Your broker likely offers limit orders (with timing discretion) or market orders. Asking for a true not-held order will likely result in confusion or a market order instead.

## See also

<div class="wiki-seealso">

### Closely related

- [Limit Order](/limit-order/) — Trader-set price boundary that the broker respects.
- [Market Order](/market-order/) — Immediate execution at the best current price, no price protection.
- [Execution Risk](/execution-risk/) — The danger that your order fills at a worse price than you expected.
- [Market Maker Trading](/market-maker-trading/) — How brokers and intermediaries execute large blocks.
- [Over-the-Counter Market](/over-the-counter-market/) — Where not-held orders are still common.

### Wider context

- [Order Types](/order-types/) — The full taxonomy of standing and immediate orders.
- [Broker](/broker/) — The intermediary who executes your orders.
- [Price Discovery](/price-discovery/) — How markets establish fair value over time.
- [Block Trade](/block-trade/) — Large institutional trades where not-held orders often appear.

</div>
