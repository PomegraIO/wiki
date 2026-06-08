---
title: "Futures Margin Call Mechanics"
description: "A futures margin call occurs when losses push an account below maintenance margin; brokers then demand cash or will liquidate positions."
keywords:
  - futures margin call mechanics
  - how futures margin call works
  - margin call liquidation futures
  - maintenance margin requirements
image: /svg/derivatives.svg
---

*A **futures margin call** is a demand by your broker for immediate cash when your account equity falls below the maintenance margin threshold. Unlike stock [margin](/margin-call-forex/), which allows extended settlement, futures margin calls are intraday events—your broker can liquidate your positions without permission if the shortfall persists. Understanding the timeline and the broker's rights is essential for anyone trading [futures contracts](/futures-contract/).*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Futures Margin Call — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives." />

<div class="wiki-infobox-caption">Futures brokers monitor daily mark-to-market and enforce maintenance margin in near-real time.</div>

|   |   |
|---|---|
| **Trigger** | Account equity falls below maintenance margin percentage |
| **Typical requirement** | 5–10% of contract notional value (varies by commodity) |
| **Timeline** | Within hours or minutes of breach; same trading day |
| **Response needed** | Deposit cash or positions are liquidated at market price |
| **Liquidation** | Broker closes positions automatically if deposit doesn't arrive |
| **Liability** | You are responsible for any losses from liquidation, even if price gaps |

</aside>

## Initial margin versus maintenance margin

Before a margin call can occur, you must post **initial margin**—the cash or securities required to open a position. For a crude oil futures contract, initial margin might be $3,000 per contract. This is your "stake."

[**Maintenance margin**](/futures-margin-call-mechanics/) is the minimum equity you must maintain in your account. If initial margin is $3,000, maintenance is often 75% of that, or $2,250. Once your account balance dips below maintenance, the broker issues a margin call.

The gap between initial and maintenance is the "cushion." If you deposit $3,000 to open a contract and the market moves against you by $750, your equity drops to $2,250, and maintenance margin is breached.

## Daily mark-to-market and the margin call trigger

Every evening (or intraday, depending on the broker and market), futures positions are **marked to market**. The broker revalues your position at the closing price and adjusts your account balance immediately. Gains are credited; losses are deducted.

Say you go long one crude oil contract at $80/barrel with $3,000 initial margin. Crude closes at $79/barrel the next day. You've lost $100. Your account balance is now $2,900. As long as this stays above maintenance margin ($2,250), you're fine.

But if crude drops to $78, you've lost $200, leaving $2,800. Still above maintenance.

At $77.75/barrel, you've lost $250, bringing your balance to $2,750—still above $2,250 maintenance.

At $77.50/barrel, you've lost $500, leaving $2,500. Still OK.

At $77.25/barrel, you've lost $750, bringing your balance to $2,250—exactly at maintenance. You receive a margin call notice: deposit $750 by the next trading open, or your position will be liquidated.

## The margin call notice and timeline

The broker notifies you of the call—typically via email, text, or the trading platform—usually after hours or at market open the next day. You then have a **very short window** (often until noon or early afternoon of the same trading day) to deposit funds.

The timeline is rigid. Unlike stock margin calls, which allow up to five business days to settle, futures margin calls demand same-day or next-morning action. This urgency is because futures are heavily leveraged and markets move fast. Brokers cannot afford to wait.

## What happens if you don't respond

If you fail to deposit by the deadline and the account remains below maintenance, the broker **liquidates positions without further notice or permission**. The law (and the futures exchange rules under the [Commodity Futures Trading Commission](/securities-and-exchange-commission/)) permits this.

The broker will sell your contracts at whatever price is available in the market—potentially at a loss if the market has gapped or become illiquid. If you are long and the broker sells, you lock in the current loss. If you are short and the broker buys to cover, you lock in the loss there. Either way, you bear the market risk.

You are then liable for any shortfall. If liquidation closes you at $77/barrel and you were long at $80, the broker can bill you for the remaining loss of $300 per contract, even after the position is closed.

## A worked example with multiple contracts

You deposit $15,000 and buy five crude oil futures contracts at $80/barrel, using $3,000 initial margin per contract ($15,000 ÷ 5 contracts). Maintenance margin per contract is $2,250, so total account maintenance is $11,250.

Day 1: Crude falls to $78. Loss is $2/barrel × 5 = $10. Account balance: $14,990. Still above $11,250 maintenance. No call.

Day 2: Crude falls to $75. Loss is $5/barrel × 5 = $25. Account balance: $14,975. Still above maintenance. No call.

Day 3: Crude gaps down to $72 on geopolitical news. Loss is $8/barrel × 5 = $40. Account balance: $14,960. Still above maintenance.

Day 4: Crude falls to $70. Loss is $10/barrel × 5 = $50. Account balance: $14,950. Still above maintenance.

Day 5: Crude closes at $65. Loss is $15/barrel × 5 = $75. Account balance: $14,925. Still above $11,250.

Day 6: Crude gaps down to $60 at the open. Loss is $20/barrel × 5 = $100. Account balance: $14,900. Still above $11,250—barely.

Day 7: Crude falls to $55. Loss is $25/barrel × 5 = $125. Account balance: $14,875. Still OK.

Day 8: Crude closes at $50. Loss is $30/barrel × 5 = $150. Account balance: $14,850. Maintenance requires $11,250, and you have $14,850, so you're fine.

Day 9: Crude collapses to $40. Loss is $40/barrel × 5 = $200. Account balance: $14,800. Still above maintenance.

Day 10: Crude slides to $30. Loss is $50/barrel × 5 = $250. Account balance: $14,750. Still above $11,250.

Day 11: Crude plummets to $20. Loss is $60/barrel × 5 = $300. Account balance: $14,700. Maintenance is $11,250 ($2,250 × 5 contracts). You're still above it, but the cushion is now just $3,450. A further drop of $0.69/barrel triggers the call.

Day 12: Crude opens at $19.31. Loss is $60.69/barrel × 5 = $303.45. Account balance: $14,696.55. Still above maintenance—but if the market continues to tank, the call is imminent.

Day 13: Crude closes at $18. Loss is $62/barrel × 5 = $310. Account balance: $14,690. At this point, a $4.50 move against you ($0.90/barrel per contract) brings you below $11,250 maintenance, triggering the call.

Day 14: Crude opens at $17. Loss is $63/barrel × 5 = $315. Account balance: $14,685. Still above $11,250, but only by $3,435. A further $687.50 loss triggers liquidation.

Day 15: Crude falls to $15.86. Loss is $64.14/barrel × 5 = $320.70. Account balance: $14,679.30. Maintenance breached. Margin call issued.

You have until noon (or the broker's cutoff) to deposit $320.70 or more. If you don't, the broker sells all five contracts at market price—whatever crude is trading at that moment. If it's $15, you've locked in the loss. If it has rallied to $20 in the meantime, you might recover some. But you have no control.

## Forced liquidation mechanics

When the broker liquidates, it does so "at market" or "at best available price." In liquid markets like crude oil or the [S&P 500 index](/sp-500-index/), this is straightforward. In less liquid or exotic contracts, the liquidation price could be significantly worse than the last quoted price.

If the position is large or the market is thin, the broker's sale of your contracts could push the price lower, worsening your loss. You bear this additional slippage.

Once liquidated, your account is closed or reset depending on the shortfall. If the broker took a loss beyond your available cash, you may owe the broker money, which it will pursue through collections or litigation.

## Preventing margin calls

- **Post excess margin**: Deposit more cash than the minimum initial margin. A larger cushion means deeper losses before a call occurs.
- **Reduce position size**: Trade fewer contracts for the same capital. If you had bought three contracts instead of five, your maintenance requirement would be $6,750 instead of $11,250, delaying a call significantly.
- **Set stop-loss orders**: Automatically close positions at a predetermined loss, preventing excessive drawdowns.
- **Monitor intraday**: Some traders watch prices in real time and close positions before a call is issued, accepting a smaller loss than forced liquidation might inflict.
- **Use options** instead of outright futures, capping your loss to the [premium](/option-premium/) paid.

## See also

<div class="wiki-seealso">

### Closely related

- [Futures Contract](/futures-contract/) — the leveraged instrument requiring margin
- [Margin Call (Forex)](/margin-call-forex/) — similar mechanics in currency trading
- [Forward Contract vs Futures Contract](/forward-contract-vs-futures-contract/) — understanding daily settlement
- [Leverage Ratio (Forex)](/leverage-ratio-forex/) — how margin amplifies returns and losses
- [Option](/option/) — an alternative with capped downside
- [Contango Cost for Long Futures Holders](/contango-cost-for-long-futures-holder/) — why account draws persist

### Wider context

- [Derivatives Hedging](/derivatives-hedging/) — responsible position sizing
- [Risk Management](/value-at-risk/) — stress-testing account capacity
- [Commodities](/crude-oil/) — the markets with tightest margin requirements
- [Broker](/broker/) — choosing a broker with favorable margin terms

</div>
