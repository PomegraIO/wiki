---
title: "The Margin Call Process in Futures Clearing Step by Step"
description: "What happens when a futures position triggers a variation margin shortfall: the timeline, notifications, and consequences before a clearinghouse forces liquidation."
keywords:
  - margin call process futures clearing
  - variation margin futures
  - futures clearing house procedures
  - margin call timeline
  - clearinghouse margin requirements
  - futures liquidation process
image: /svg/institutions.svg
---

*The **margin call process in futures clearing** unfolds in stages: after market close, a [clearinghouse](/federal-reserve/) marks all positions to market, calculates variation margin owed, notifies the clearing member (usually a [broker](/broker/)), and demands payment by a set deadline—typically before or shortly after the next market open. If the member fails to deposit funds, the clearinghouse liquidates positions, often without warning.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Futures Margin Call — key facts</div>

<img src="/svg/institutions.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Clearinghouses enforce real-time solvency through daily mark-to-market and rapid liquidation of underfunded accounts.</div>

|   |   |
|---|---|
| **Trigger** | Daily settlement loss on an open position that reduces initial margin below requirement |
| **Notification timing** | After market close (4 p.m. ET for stock index futures); payment due next business day by 10 a.m. CT |
| **Responsible party** | Clearing member, who then passes the call down to the customer or covers it themselves |
| **Failure consequence** | Forced liquidation; clearinghouse closes the position at market prices, no negotiation |
| **Initial vs. variation margin** | Initial is the upfront deposit; variation is the daily loss reimbursement owed to the clearinghouse |
| **Related concepts** | [Margin call (forex)](/margin-call-forex/), [leverage ratio](/leverage-ratio-forex/), [counterparty risk](/counterparty-risk/) |

</aside>

## The Daily Mark-to-Market Cycle

Every futures contract is settled daily. At the close of trading, the clearinghouse calculates the profit or loss on each open position based on that day's settlement price. A trader holding a long contract is owed money if the settlement price rose since purchase; owed nothing if it stayed flat; owing money if it fell. This daily realization of gains and losses is called mark-to-market.

For most traders, this is routine: a profitable day credits their account, and a losing day debits it. But if losses are large enough to consume the initial margin deposit, the trader's account balance falls below zero, or more precisely, below the maintenance margin requirement—the minimum amount the clearinghouse demands to remain on the hook for that position.

Clearing members (the main brokers and financial institutions that directly access the clearinghouse) maintain an account there in their own name. Individual traders and smaller firms trade through these clearing members. When a clearing member's account is hit with a large variation margin loss, the clearinghouse immediately demands replenishment.

## The Notification and Payment Deadline

The clearinghouse sends variation margin notices to clearing members electronically, usually late in the trading day or shortly after the market close, sometimes in multiple tranches if losses accumulate. For U.S. equity index futures cleared through the Chicago Mercantile Exchange (CME), the typical deadline is 10 a.m. Central Time the next business day.

This is not a suggestion. If the clearing member does not deposit the shortfall by the deadline, the clearinghouse is authorized to liquidate the member's open positions immediately and without further notice. The clearinghouse acts not out of cruelty but out of necessity: it is holding the risk of the member's positions, and every hour of undercollateralization exposes the clearinghouse—and ultimately every other clearing member—to the risk that the troubled member will default entirely.

## Cascade Down to the Customer

Most individual and institutional customers trade futures through a clearing member, and the member passes margin calls down to them. A customer's broker will send a notice (by email, phone, or platform notification) alerting the customer to the shortfall and demanding a deposit by the clearinghouse deadline, usually phrased as "margin call due by 10 a.m. CT tomorrow."

Some brokers offer a grace period within their own systems—a few hours to respond—but this is a courtesy that has limits. If the customer does not meet the internal deadline, the broker will begin liquidating positions to raise cash. Unlike the clearinghouse's forced liquidation (which liquidates the member's entire position), a broker may liquidate only enough of the customer's positions to cover the shortfall, preserving the rest.

## What Triggers a Margin Call: The Maintenance Margin Floor

The clearinghouse sets two margin levels: initial margin (the deposit required when opening a position) and maintenance margin (the minimum balance required to keep the position open). Initial margin is typically 5–15% of the notional contract value, depending on the contract and volatility. Maintenance margin is usually 60–75% of initial margin.

If a trader enters a long position in a $100,000 E-mini S&P 500 contract and initial margin is $5,000, the maintenance margin might be $3,500. If the position loses $2,000, the account drops to $3,000. The account is now below maintenance margin, and a margin call is issued for $2,000 (to bring the account back to initial margin levels, not just to maintenance).

This threshold is set conservatively: the clearinghouse wants a buffer to absorb intraday swings without triggering constant margin calls. But in volatile markets, it is easy to breach. A sharp overnight gap at the open can wipe out a month's expected profit in minutes.

## Forced Liquidation: The Clearinghouse's Last Resort

If payment is not received by the deadline, the clearinghouse's risk management team is authorized to liquidate the member's entire position. For an individual trader, this often happens through the broker first, but if the broker itself defaults, the clearinghouse steps in directly.

Forced liquidation is not a negotiation. The clearinghouse will sell the positions at the best available market prices, which in a distressed market may be significantly worse than the settlement price used to calculate the margin call. In an extreme gap, the liquidation loss can exceed the original margin deposit, creating a deficit the customer owes to the broker.

A historical example: during the 2020 COVID-19 market crash, the S&P 500 fell approximately 34% from peak to trough. Traders holding short (bearish) equity index futures had margin calls exceed their deposits. Some who could not meet the call saw positions liquidated at severe losses, and a few were left owing money to their brokers well after the liquidation was complete.

## Intraday Margin Calls and Real-Time Risk

While the formal variation margin deadline is daily, the clearinghouse and brokers monitor positions in real-time. If a single move during the trading day causes a large loss, the clearinghouse may issue an intraday margin call, demanding payment before the market close. This is less common for stable markets but standard during crises.

For example, on March 16, 2020—the height of the pandemic panic—CME issued intraday margin calls to clearing members, effectively widening the initial margin requirements on major stock index contracts by 15–40% mid-day. Members were forced to liquidate or deposit hundreds of millions in additional collateral before the 4 p.m. close. Brokers then scrambled to push these calls to customers with just hours to respond.

## The Clearinghouse's Defense Chain

The clearinghouse operates a defense chain: initial margin, mark-to-market, variation margin calls, and liquidation. Each stage is designed to prevent contagion. If a single trader or even a single clearing member fails, the system is meant to absorb the loss before it spreads to other participants.

In normal markets, this works smoothly. In systemic crises, it is tested. The 2008 financial crisis and the 2020 pandemic panic both triggered extreme margin calls and forced liquidations. Some clearing members faced insolvency; the U.S. Federal Reserve and foreign central banks deployed emergency lending to prevent cascading defaults.

## Payment Methods and Collateral

Variation margin can be paid in cash or, often, in approved securities. A clearing member with excess collateral (Treasury bonds, for example) can pledge these to the clearinghouse instead of wiring cash. This flexibility helps avoid liquidity crunches when cash is scarce.

For retail customers, however, most brokers demand cash deposits. Some allow liquidation of other holdings in the customer's brokerage account, but this is typically slower and subject to settlement delays. The pressure to deposit cash by the deadline is the reason many traders are forced to liquidate long-standing positions—not because the margin call itself exhausted their net worth, but because they cannot move cash fast enough.

## See also

<div class="wiki-seealso">

### Closely related

- [Margin call (forex)](/margin-call-forex/) — similar dynamic in foreign exchange leverage accounts
- Clearinghouse — the institution that guarantees futures contracts and demands margin
- [Counterparty risk](/counterparty-risk/) — the risk that a clearing member defaults and the clearinghouse absorbs the loss
- [Futures contract](/futures-contract/) — the daily-settled derivative being margined
- [Leverage ratio (forex)](/leverage-ratio-forex/) — how brokers cap the ratio of leverage to margin

### Wider context

- [Broker](/broker/) — the intermediary through which customers submit margin to the clearinghouse
- [Systemic risk](/systemic-risk/) — how a single member's failure threatens the whole system
- [Monetary policy](/monetary-policy/) — central bank interventions that prevent clearinghouse crises
- Financial crises — historical events that stress-tested margin procedures

</div>
