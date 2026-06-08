---
title: "Post-Only Order Type"
description: "How post-only orders prevent execution as a taker, allowing traders to collect maker rebates or control transaction costs."
keywords:
  - post-only order
  - maker-only order
  - trading order types
  - maker rebate
  - market maker
  - trading costs
  - limit order
---

*A **post-only order** (also called a maker-only order) is a limit order that is rejected rather than executed if it would immediately fill against existing orders on the opposite side of the book. The trader posts liquidity as a maker—earning rebates or avoiding taker fees—instead of aggressively taking liquidity at an unfavorable price.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Post-Only Order — key facts</div>

<img src="/svg/trading.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">An order type designed to ensure the trader pays maker fees (or earns maker rebates) instead of taker fees.</div>

|   |   |
|---|---|
| **Order behavior** | Rejected if execution as taker is possible; only fills as a maker post. |
| **Counterparty** | Passive—waits for an incoming order to hit the posted price. |
| **Fee structure** | Maker rebate (negative fee) or lower taker fee, not the higher taker cost. |
| **Use case** | Market makers, high-frequency traders, rebate-seeking retail traders. |
| **Timeframe** | Usually day trades or intraday; sometimes longer-term accumulation strategies. |
| **Fills** | Partial fills possible if demand on the opposite side is light; order sits if no takers arrive. |
| **Risk** | May not fill if the price never reaches the posted level or demand is low. |

</aside>

## The Taker-Maker Fee Structure

Most electronic exchanges and brokers charge different fees depending on whether a trader is taking or making liquidity.

**Taker** = the trader who executes immediately against existing orders. A taker hits an ask or lifts a bid, matching against a passive order already on the book. Takers pay a **taker fee** (e.g., 0.05% of the transaction value).

**Maker** = the trader whose order sits on the book waiting to be hit. Makers provide liquidity and typically earn a **maker rebate** (e.g., 0.02% back) or at minimum pay a lower taker fee (e.g., 0.00% or negative).

A post-only order ensures the trader always posts as a maker, never takes.

## How Post-Only Works

When a trader submits a post-only buy order at a specific price:

1. The exchange checks: "Are there sellers willing to fill this order at this price or lower right now?"
2. **If yes**, the order is **rejected**. The trader receives a message saying the order was not posted because it would execute as a taker. No transaction occurs.
3. **If no**, the order is posted to the book at the specified price. The trader now has a maker order waiting for a seller to accept.

When a seller arrives and agrees to the buyer's posted price, the buyer's order fills—and the buyer is credited the maker rebate (or does not pay the taker fee).

Example: An options market maker wants to accumulate 100 contracts of XYZ calls at an ask of $3.50. Instead of clicking "buy 100 at market" (which hits the ask at whatever price, as a taker), the trader submits a post-only buy limit order for 100 at $3.50. If the ask is currently $3.52, the post-only order is rejected—it would fill immediately, triggering taker fees. The trader resubmits at $3.49, which does not cross the current spread, and the order waits. If someone sells 100 contracts at $3.49, the market maker's order fills as a maker and earns the rebate.

## Why Traders Use Post-Only Orders

**Earning rebates.** For high-volume traders and market makers, rebates accumulate. On major exchanges like NYSE Arca or Nasdaq, maker rebates can range from 0.002% to 0.03% per share. A market maker buying and selling 10 million shares per day earns thousands of dollars in rebates alone. Post-only orders are the mechanism to capture them.

**Controlling transaction costs.** A patient trader (say, a hedge fund gradually building a long position over days or weeks) can use post-only orders to buy only at maker prices, avoiding the 0.05% taker fee. Over thousands of transactions, the savings compound.

**Avoiding market impact and slippage.** A taker order (a market order or aggressive limit order) fills immediately but may execute at worse prices as it moves through the order book. A post-only order waits for the market to come to the trader's price. This is slower but often cheaper if the trader is not time-constrained.

**Providing liquidity and collecting a spread.** In less liquid markets (penny stocks, thinly traded options, FX), market makers post both a bid and an ask, using post-only orders on both sides. When traders hit the bid or lift the ask, the market maker collects the [bid-ask spread](/bid-ask-spread/) plus the maker rebate.

## Post-Only vs. Regular Limit Orders

A regular limit order is passive (it does not execute immediately) but will fill as a taker if the market moves to the order's price. Example: A trader posts a buy limit at $99 for a stock currently at $100. If the stock drops to $99 and there are sellers there, the limit order fills—as a taker against those sellers. The trader pays the taker fee.

A post-only limit order will not fill as a taker under any circumstances. If the market comes to the order's price but the order would be filled against an existing order, it is cancelled or rejected instead. The trader must resubmit if they want to buy at that price; the rebate opportunity is preserved.

## Real-World Examples

**High-frequency trading (HFT) firm.** An HFT outfit runs algorithms on a major stock exchange. The algorithm posts small orders on both sides of the spread across hundreds of stocks, earning rebates. Every order is post-only to lock in rebate economics. The firm may fill 10,000 trades per day, earning $0.001 per share: $10,000 in rebates.

**Retail options trader chasing rebates.** A self-directed trader using a broker that offers maker rebates (e.g., some brokers provide 0.002% rebates on options) submits post-only limit orders when accumulating long-dated call spreads. Over months, the rebates cover a fraction of commissions.

**Crypto exchange market maker.** On a blockchain-based exchange (e.g., a DEX with order books), a market maker posts limit orders on both sides of a trading pair, earning a small spread and sometimes platform rewards. Post-only orders ensure no slippage against existing orders.

**Accumulation phase in swing trading.** A swing trader building a position in a thinly traded microcap stock uses post-only orders to buy only at the bid (maker rebate) rather than hitting the ask. This reduces the cost basis and improves entry quality.

## Execution Risk and Non-Execution

The downside of post-only is non-execution. If a post-only order is never touched, it does not fill.

A trader posts a buy order for 1,000 shares at $50 on a stock that trades 500 shares per day. The order sits. Days pass. The stock price never falls to $50. The order is cancelled. The trader either raises the price (moving closer to taker territory) or abandons the trade.

This is acceptable for patient, long-term accumulation but risky for time-sensitive strategies. A trader with a strong technical signal who needs to enter *today* cannot use post-only; they must pay the taker fee to guarantee execution.

## Post-Only Across Market Types

**Stock exchanges.** NYSE, Nasdaq, and other stock exchanges support post-only orders. Retail brokers often call the equivalent feature "reduce or cancel" or simply check a "post only" box.

**Crypto spot and futures.** Major exchanges (Binance, Kraken, Coinbase Pro, FTX before its collapse) all support post-only orders on spot and perpetual futures trading pairs. Rebates vary; some exchanges offer zero maker fees or taker credits.

**Options markets.** Post-only is standard for professional options traders; retail brokers may offer it but sometimes hide it under an advanced options menu.

**Forex.** Most retail FX brokers do not support post-only (they use market-maker execution). Professional FX platforms and ECNs (electronic communication networks) offer it.

## See also

<div class="wiki-seealso">

### Closely related

- [Limit order](/limit-order/) — the foundation order type; post-only is a limit order variant
- [Market order](/market-order/) — the opposite: guaranteed execution, guaranteed taker fees
- [Bid-ask spread](/bid-ask-spread/) — what market makers earn and post-only traders help tighten
- [Market maker trading](/market-maker-trading/) — the primary use case for post-only strategies
- [Limit order](/limit-order/) — interaction of pricing and execution timing

### Wider context

- [Stock exchange](/stock-exchange/) — venue where post-only orders are executed
- [Broker](/broker/) — intermediary that may or may not offer post-only functionality
- [Alternative trading system](/alternative-trading-system/) — modern venues supporting post-only
- [Algorithmic trading](/algorithmic-trading/) — HFT and high-volume strategies that deploy post-only at scale

</div>
