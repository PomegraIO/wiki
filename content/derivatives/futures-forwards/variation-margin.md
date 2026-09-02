---
title: "Variation Margin"
description: "Daily cash settlements of gains and losses on futures and derivatives positions—the mechanism that makes clearing houses risk-free by collecting losses in real time rather than at expiration."
---

*You bought crude oil [futures](/wiki/futures-contract/) at $80. Overnight, crude falls to $78. You did not choose to sell; you are still long. But the clearing house demands cash. This is variation margin: the daily settlement of P&L that keeps [futures](/wiki/futures-contract/) safe.*

## The mechanism

[Futures contracts](/wiki/futures-contract/) are [marked-to-market](/wiki/mark-to-market/) daily. Every trading day at the close, the clearing house calculates the settlement price and determines who owes whom money:

- If you are long a contract at $80 and the settlement price is $78, you have a $2 loss per contract.
- On a standard contract of, say, 100 barrels (crude oil), you owe 100 × $2 = $200.
- By the next morning, you must deposit $200 into your account or the clearing house will force liquidate your position.

If the contract has moved the other way (settling at $82), you receive $200 credit. Either way, **the daily P&L is paid or collected in cash, every single day**.

This is the defining difference between [futures](/wiki/futures-contract/) (which settle variation margin daily) and [forward contracts](/wiki/forward-contract/) (which settle once, at expiration).

## Why variation margin exists

Without daily settlement, the clearing house would face enormous credit risk. A trader who bought 1,000 crude contracts at $80, expecting to close before expiration, could face a 20% move to $64 by the time the contract expires. If the trader becomes insolvent during that period, the clearing house eats the loss—potentially a $16,000 per-contract hole.

By collecting variation margin daily, the clearing house reduces that risk dramatically:

- Each day's loss is small (the daily price move).
- The trader must maintain minimum margin (typically 2-10% of notional contract value) to cover one day's worst-case move.
- If a trader starts losing money, the margin erodes, and the clearing house forces liquidation before the loss exceeds the margin.

This system is why [futures](/wiki/futures-contract/) are safer than [forwards](/wiki/forward-contract/): the clearing house is never on the wrong side of a large, unhedged position for long.

## Margin accounts and calls

Traders maintain margin accounts with their broker. The account has two components:

**Initial margin:** The cash deposit required to open a position. This is typically 5-10% of the notional contract value, set by the exchange and broker. To open a $100,000 oil position (1,000 barrels at $100), you might need $5,000 initial margin.

**Maintenance margin:** The minimum balance the account must maintain. Typically 75% of initial margin. If oil drops to $95, your account has a $5,000 loss. Your $5,000 initial margin drops to $0. If it drops further, you fall below maintenance and receive a **margin call** from your broker: deposit more cash or we liquidate your positions.

Daily settlement adds or subtracts from the margin account:
- Oil rises to $101: you gain $1,000. Margin balance becomes $6,000.
- Oil falls to $98: you lose $2,000. Margin balance falls to $3,000, below maintenance. **Margin call: deposit $2,000 by tomorrow's close or face liquidation.**

## Funding risk and leverage

Variation margin creates funding risk for leveraged positions. A trader using 10x leverage ($100,000 position with $10,000 margin) faces the reality that a 1% adverse move wipes out their margin.

Example: A hedge fund holds $1 billion of crude oil [futures](/wiki/futures-contract/) (10x leverage on a $100 million capital base). Oil drops 2% overnight. The fund has a $20 million loss.

- Variation margin call: $20 million due by close of business.
- The fund has not liquidated; it still owns the position. But it must raise $20 million cash immediately.
- If the fund cannot raise the cash, the broker forces liquidation.

This is why the March 2020 oil crisis was so brutal: oil crashed 20% in weeks, forcing variation margin calls on historic scale. Funds that were underwater on positions faced margin calls for millions while the underlying markets were illiquid (hard to liquidate without moving the price further against them). Some hedge funds blew up not because of long-term value destruction but because they could not meet variation margin calls.

## The difference from [initial margin](/wiki/initial-margin/) and [maintenance margin](/wiki/maintenance-margin/)

Variation margin is the **daily P&L settlement.** [Initial margin](/wiki/initial-margin/) and [maintenance margin](/wiki/maintenance-margin/) are the **minimum account balance requirements.** These are three separate concepts:

- **Initial margin:** "You must deposit $5,000 to open this position."
- **Maintenance margin:** "Your account balance must stay above $4,000 or you face liquidation."
- **Variation margin:** "Your $5,000 balance is adjusted daily for P&L; if you lose $2,000, your new balance is $3,000, triggering a margin call."

## Settlement timing and calendars

Variation margin typically settles T+1 (one business day after trading). You trade on Monday; Monday's P&L is due Tuesday morning. This lag creates cash flow management challenges for large traders: Monday's $50 million loss means you need $50 million in the bank Tuesday, even though Monday's trading has not yet finalized.

Weekend and holiday gaps create concentration risk. A position marked-to-market on Friday with a loss faces no variation margin call until Tuesday (no trading Saturday, Sunday, Monday-holiday). A 5% move over the weekend becomes a 10% loss by Tuesday's mark. This is why traders closely monitor positions before extended weekends.

## The impact on portfolio management

Variation margin forces daily rebalancing psychology. A trader on the wrong side of a move faces daily evidence of losses. This is psychologically brutal, especially for leveraged positions:

- Monday: lose $100,000. Margin call. Deposit cash or liquidate.
- Tuesday: prices stabilize, then recover. Your position is up $50,000.
- But you already paid $100,000 in variation margin Monday.

Long-term traders who are ultimately correct must survive the daily variation margin settlement road to get there. Some cannot, forcing early liquidation.

## Variation margin pro and con

**Pro:** Clearing houses are made safe. Counterparty risk is minimal; the clearing house is never exposed to a trader's full P&L.

**Con:** Variation margin creates leverage risk for traders and funding risk for funds. A position that is fundamentally sound can be forced to liquidate due to variation margin calls during temporary adverse moves. This is especially acute in illiquid [futures](/wiki/futures-contract/) markets where no one wants to buy when you must liquidate.

Some argue this is a feature, not a bug—variation margin enforces discipline. Others argue it creates unnecessary pro-cyclical selling: when positions are under stress (bear markets, crises), variation margin forces sales, exacerbating the move.

The 2008 financial crisis and 2020 COVID crisis both created variation margin storms, as leveraged funds faced calls they could not meet, forcing fire sales. Central banks and regulators later recognized that sudden variation margin calls can destabilize markets, leading to discussions about smoother margin structures or virtual currency settlement to reduce cash-flow shocks.

<div class="wiki-seealso">
<h2>See also</h2>
<h3>Closely related</h3>
<ul>
<li><a href="/wiki/mark-to-market/">Mark-to-market</a> — daily revaluation of positions, the process that determines variation margin amounts.</li>
<li><a href="/wiki/initial-margin/">Initial margin</a> — the minimum deposit required to open a [futures](/wiki/futures-contract/) position.</li>
<li><a href="/wiki/maintenance-margin/">Maintenance margin</a> — the minimum account balance required to keep a position open.</li>
<li><a href="/wiki/futures-contract/">Futures contract</a> — the primary vehicle using variation margin as its daily settlement mechanism.</li>
<li><a href="/wiki/forward-contract/">Forward contract</a> — the OTC alternative, settled once at expiration (no daily variation margin).</li>
<li>Leverage — related to how variation margin creates funding risk for amplified positions.</li>
</ul>
<h3>Wider context</h3>
<ul>
<li>Derivatives — the broader category of hedging and risk-transfer instruments.</li>
</ul>
</div>
