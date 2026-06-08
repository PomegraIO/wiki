---
title: "Clearly Erroneous Trade Cancellation Rules"
description: "How exchanges bust or adjust trades executed at prices far outside the market under clearly erroneous trade cancellation rules."
keywords:
  - clearly erroneous trade
  - trade busting rules
  - exchange trade cancellation
  - erroneous execution
  - market trading rules
image: /svg/regulation.svg
---

*When a stock executes at a price wildly out of line with the market—say, a $100 stock trading at $1 for a split second—exchanges have rules allowing them to cancel or adjust that trade. **Clearly erroneous trade cancellation** is the mechanism that lets exchanges unwind these mistakes, protecting both market integrity and trader confidence by establishing objective thresholds rather than subjective judgment calls.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Clearly Erroneous Trade — Key Facts</div>

<img src="/svg/regulation.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Exchanges can bust or adjust trades that miss the market by a defined threshold.</div>

|   |   |
|---|---|
| **Who decides** | The exchange where the trade occurred |
| **Trigger** | Execution price deviates from the NBBO by percentage or absolute amount |
| **Typical percentage threshold** | 10% for most equities (varies by exchange and security type) |
| **Time window** | Trades must be reviewed within minutes; decisions posted quickly |
| **Parties notified** | Both the buyer and seller; impact on fill status published to market |
| **Appeal** | Traders may request review of the decision; exchanges have internal procedures |

</aside>

## The Problem Clearly Erroneous Trades Solve

Automated trading and network delays can create situations where an order executes at a price that no rational trader would accept or offer. A software glitch, a fat-finger order entry mistake, or a data feed interruption might result in a stock trading at 10, 20, or even 50 percent away from where it was trading milliseconds before or after. Without a cancellation mechanism, traders would either accept devastating losses or flood the market with offsetting trades, amplifying volatility.

Exchanges need a way to unwind these trades and restore confidence that executions reflect genuine supply and demand, not system errors. Early in equity market trading, exchanges relied on vague language and post-hoc judgment to break trades. This created uncertainty: was a trade truly erroneous, or was an unlucky trader just trying to escape a bad fill? Exchanges now publish explicit, numeric thresholds so traders know in advance which trades are vulnerable.

## Numeric Thresholds and Bid-Ask Deviations

Each exchange publishes its own clearly erroneous trade criteria, but the logic is consistent: a trade is flagged for review if the execution price deviates too far from the **National Best Bid and Offer (NBBO)** at the time of execution.

For most U.S. equities traded on NYSE, Nasdaq, or CBOE, the threshold is typically a **10 percent deviation** from the NBBO. On the NYSE, for example, a trade may be busted if the execution price is more than 10 percent away from the mid-point of the NBBO (or, in some cases, 10 percent from the last-sale price). For options, thresholds are often tighter—sometimes 5 percent or tied to the option's intrinsic value and time decay.

Some exchanges use **percentage-based thresholds that scale** with price. A $50 stock might use 10 percent (triggering at $45–$55), while a $10 stock might use 15 percent ($8.50–$11.50) to account for wider spreads in lower-priced securities. Over-the-counter (OTC) and pink-sheet trades may not have formal cancellation rules, leaving both parties to negotiate.

## The Review and Decision Process

When a trade prints at a price far from the NBBO, the executing exchange's operations team is typically alerted automatically. The exchange then:

1. **Confirms the NBBO** at the exact moment of execution using time-stamped market data.
2. **Calculates the deviation** to see if it breaches the exchange's published threshold.
3. **Reviews context**—was the NBBO itself corrupted? Was the executing venue's own system at fault?
4. **Makes a determination**: cancel the trade entirely, adjust it to a fair price (often the NBBO mid-point at execution), or let it stand.

The exchange posts its decision to market participants, usually within 10 to 30 minutes of the trade. If a trade is cancelled, the positions are unwound as if the trade never occurred; if adjusted, the new execution price replaces the original.

## Exceptions and Edge Cases

Not all erroneous trades meet the numeric threshold. An exchange has discretion to break trades **below the percentage threshold** if other factors point to a genuine error:

- **System or data-feed failure**: if the exchange's own technology malfunctioned or an external data feed went bad, trades may be busted even if the price deviation is small.
- **Corporate actions**: if a stock split, dividend, or spinoff confused routing algorithms, the exchange may cancel trades in the old or new security.
- **Open or halt**: trades executed during a market-open period (when the NBBO may be stale) or after a trading halt was supposed to begin may be busted at the exchange's discretion.

Conversely, exchanges **do not** bust trades simply because one party regrets the execution. Even if a trader claims they hit the wrong button, if the trade was within the published threshold, it stands. This protects market integrity: otherwise, every trader would contest every bad fill.

## Who Bears the Cost

When a trade is busted, the economic impact varies:

- **Both parties**: typically lose the execution and their opportunity to profit from the move that followed.
- **Market maker or broker**: if the exchange's own system caused the error, the exchange may pay a modest settlement or credit; this is rare and usually involves regulatory pressure.
- **Trader**: bears the consequence. This is why stop-loss orders and risk controls matter—a flash crash can break dozens of trades, and traders are not made whole.

[Market makers](/market-maker-trading/) and high-frequency traders often carry "fat finger" insurance or include error reserves in their capital, because busting is an inherent cost of electronic trading.

## How Traders Spot Erroneous Execution Risk

A trader can reduce exposure to erroneous-trade busting by:

- **Monitoring the NBBO** in real time; if an execution prints far outside it, immediately check whether it will be reviewed.
- **Using limit orders** instead of market orders; a limit order that executes far outside the NBBO is more likely to be an error, while a limit fill near the best bid or offer is safer.
- **Knowing the exchange rules** for the security they trade. Options, international stocks, and OTC securities have different thresholds.
- **Checking trade reports** shortly after execution; most busts are published within 15–30 minutes, so traders can adjust their hedge or exit within the trading day.

## Reg SHO and Other Rule Intersections

[Short selling](/short-selling/) trades are not exempt from clearly erroneous-trade rules. A short sale that executes at an erroneous price is subject to the same busting criteria. However, if the short sale is cancelled, the seller's obligation to deliver shares is unwound as well.

Trades executed in violation of [Reg SHO locate requirement](/reg-sho-locate-requirement/) may also be flagged for busting if the locate was improperly obtained, adding a compliance layer on top of the pure price-deviation test.

## See also

<div class="wiki-seealso">

### Closely related

- [Market Maker Quoting Obligations](/market-maker-quoting-obligations/) — continuous two-sided quotes that reduce the risk of erroneous trades
- [Reg SHO Locate Requirement](/reg-sho-locate-requirement/) — broker-dealer obligation to locate shares before short sale
- [Consolidated Audit Trail (CAT) Reporting](/consolidated-audit-trail-cat-reporting/) — SEC system capturing all order and trade details for surveillance
- [Price Discovery](/price-discovery/) — the process by which markets arrive at fair prices; erroneous trades distort it temporarily
- [Market Order](/market-order/) — unpriced order vulnerable to execution at erroneous prices

### Wider context

- [Stock Exchange](/stock-exchange/) — venues where busting rules are enforced
- [Securities and Exchange Commission](/securities-and-exchange-commission/) — regulator that enforces uniform standards
- [Bid-Ask Spread](/bid-ask-spread/) — the normal range from which erroneous trades deviate
- Trading Halt — another remedy for market disruptions
- [Systemic Risk](/systemic-risk/) — why error controls protect the broader market

</div>
