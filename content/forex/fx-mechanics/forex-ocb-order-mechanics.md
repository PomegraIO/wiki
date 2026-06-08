---
title: "One-Cancels-the-Other Orders in Forex Explained"
description: "How OCO orders link two pending orders so that filling one automatically cancels the other, common use cases, and execution mechanics in forex markets."
keywords:
  - one cancels the other order forex
  - OCO order forex
  - bracket order forex
  - forex order mechanics
  - stop loss profit target
---

*A **one-cancels-the-other order** (OCO) in forex links two pending orders such that execution of one immediately cancels the other. The most common structure pairs a limit order (profit target) with a stop order (loss limit), so a trader can bracket a position without manually managing both legs; if the price rallies and hits the profit target, the stop order vanishes, and vice versa. OCO orders are native to most forex platforms and essential to risk management for overnight or unmonitored positions.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">OCO Orders — key facts</div>

<img src="/svg/forex.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Two orders, one outcome: execution of one leg kills the other.</div>

|   |   |
|---|---|
| **Order pair** | Limit (profit target) + Stop (loss limit) |
| **Trigger** | Whichever order fills first cancels its sibling |
| **Setup time** | Instant; both legs enter the market simultaneously |
| **Spread impact** | Both orders are live; wider spread increases rejection risk |
| **Partial fill** | Typically cancels or adjusts the sibling order proportionally |
| **Overnight risk** | Protects against gap moves if position is unmonitored |

</aside>

## The Structure: Two Orders, One Outcome

An OCO order is a conditional pair. The trader specifies two orders:

1. **Limit order** (upper leg): Sell at 1.0850 to take profit if price rallies.
2. **Stop order** (lower leg): Sell at 1.0800 to exit if price falls.

Both orders are submitted to the market simultaneously. As price moves, the first to be touched triggers execution, and the second is instantly cancelled. If price hits 1.0850 first, the trader exits with a profit of 50 pips, and the stop at 1.0800 vanishes. If price instead falls to 1.0800, the trader exits with a 50-pip loss, and the profit target is cancelled.

This structure removes the need for the trader to actively monitor the position. In the forex market, where trading spans time zones and high-volatility gaps are common, the ability to lock in risk parameters without sitting at the screen is essential.

## Common Use Case: Bracketing a Long Position

A trader enters a long position at 1.0800 (buying EUR/USD) and wants to define risk and reward upfront:

- Buy at 1.0800
- Place OCO with profit target at 1.0850 (limit order) and stop-loss at 1.0750 (stop order)

If EUR/USD rallies to 1.0850, the trader is filled on the limit, capturing a 50-pip profit. The stop at 1.0750 is cancelled.

If EUR/USD drops to 1.0750, the trader is filled on the stop, accepting a 50-pip loss. The profit target is cancelled.

If price oscillates between 1.0750 and 1.0850 without touching either, both orders remain live, and the trader remains in the position.

This is a true bracket: risk and reward are defined before the trade is entered.

## Execution and Order Priority

When price approaches either leg of an OCO, the [market maker](/market-maker-trading/) or exchange must decide which order fills first. In a normal market, this is straightforward: whichever order's price is touched first executes.

But in a volatile gap or a flash-move scenario, both order prices might be touched within milliseconds. Most brokers have programmed rules:

- **Time priority:** First order to enter the market (in this case, they entered simultaneously, so neither has priority).
- **Broker discretion:** The broker's system fills the order that is most likely to execute cleanly given the direction of the move. If price is dropping sharply, the stop order may execute first; if price is rallying, the limit may fill first.
- **Rejection and retry:** If the broker can't determine clear priority, one or both orders may be rejected, and the trader is left holding a naked position.

In liquid pairs like EUR/USD, execution is nearly instantaneous and deterministic. In illiquid pairs or during news events, ambiguity can arise.

## Spread and Slippage Considerations

An OCO order sits with both legs in the market, exposed to the [bid-ask spread](/bid-ask-spread/). If the spread widens sharply, the executed order may fill at a worse price than expected, and the cancelled order may never have had a chance to execute.

For example:

- Bid/Ask at 1.0800/1.0802
- Trader enters long at 1.0802, places OCO: limit at 1.0850, stop at 1.0750
- Price rallies; bid-ask becomes 1.0849/1.0852 as it approaches the profit target
- Limit order fills at 1.0850, stop is cancelled
- Trader realized 48 pips, not 50, due to slippage

Wider spreads during news or low liquidity increase the likelihood that the executed order fills at an unfavorable price, while the cancelled order might have offered a better exit.

## Partial Fills and the Sibling Order Problem

In forex, most transactions are single-leg fills because the broker is matching a trader's order against the interbank market. But if a trader places an OCO with large size, the limit order might fill partially.

A trader submits an OCO to sell 1 million EUR at 1.0850 (limit) with a stop at 1.0750:

- Price rallies; the limit order receives a fill for 600,000 EUR at 1.0850.
- The trader still holds 400,000 EUR of the original position.
- What happens to the stop order?

Most platforms auto-adjust the sibling order to reflect the remaining position size, canceling the 600,000 EUR worth of stop and leaving 400,000 EUR. However, some platforms require manual intervention, and others may cancel the entire stop order, leaving the remaining 400,000 EUR unhedged.

Traders should confirm their platform's behavior before relying on OCO for large size. Some brokers disable OCO orders for position sizes above a certain threshold to avoid this ambiguity.

## OCO Versus Algorithmic Bracketing

An OCO is a simple, synchronous bracket. But some platforms offer more sophisticated conditional orders:

- **One-Triggers-All (OTA):** Execution of one order automatically places a set of follow-up orders. A trader might execute a market order to enter a position, and the OTA automatically places a profit target and stop. This is OCO-like but with more logic.
- **Algorithmic bracket orders:** Some platforms allow the trader to define rules (e.g., "if price moves 30 pips in my favor, tighten the stop to breakeven"). These are not true OCO orders; they're conditional instructions that the algorithm updates.

Standard OCO orders do not adjust dynamically. Once placed, both legs remain static until one executes or the trader manually cancels.

## Risk: Gap and Limit-Down Scenarios

The biggest risk of OCO orders is a gap through both legs. If a currency pair experiences a sudden drop due to economic data, geopolitical shock, or exchange halt, price might gap from 1.0850 down to 1.0700, skipping both the profit target and the stop order.

In this scenario:

- The trader's position is now underwater by 100 pips.
- Neither OCO order executed, so no exit occurred.
- The trader is left holding an unhedged position in a volatile market.

This risk is why traders often include a market order as a fallback: if a preset time passes and both OCO legs are still unfilled (indicating a gap scenario), a market order executes to get out at any price.

## Overnight Gaps and Weekend Risk

OCO orders are particularly useful for managing overnight and weekend risk in forex. A trader who exits at the US close but wants to participate in London and Asia sessions can place a long position with a tight OCO bracket and sleep without monitoring.

However, over weekends (when forex markets are closed), OCO orders may become inaccessible or may execute with large slippage if trading resumes at a gap. Most brokers cancel all orders before the market close on Friday, so traders must re-enter them Monday morning or use a weekend-aware bracketing system if their broker offers one.

## Platform Variations

Not all forex platforms implement OCO the same way:

- **Professional platforms (TradingView, MetaTrader 5):** Native OCO with real-time syncing between legs.
- **Retail brokers:** Some require manual entry of both orders; others have automated OCO interfaces.
- **Crypto and stock exchanges:** Some do not offer OCO and require algorithmic wrappers to achieve the same effect.

Traders should verify their broker's OCO mechanics and latency before relying on them for risk management.

## See also

<div class="wiki-seealso">

### Closely related

- [Limit Order](/limit-order/) — how profit-taking orders work
- Stop Loss — how stop orders protect against losses
- [Bid-Ask Spread](/bid-ask-spread/) — spread impact on order execution
- [Market Maker Trading](/market-maker-trading/) — how brokers fill orders
- [Leverage Ratio in Forex](/leverage-ratio-forex/) — position sizing and margin impact of bracketed trades
- [Currency Risk](/currency-risk/) — risk management in forex positions

### Wider context

- [Forex](/forex-ocb-order-mechanics/) — broader mechanics of currency trading
- [Spot Exchange Rate](/spot-exchange-rate/) — the price OCO orders are pegged to
- [Over-the-Counter Market](/over-the-counter-market/) — where forex trades settle
- [Counterparty Risk](/counterparty-risk/) — broker solvency during volatile gaps

</div>
