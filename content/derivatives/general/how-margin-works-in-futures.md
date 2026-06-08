---
title: "How Margin Works in Futures Contracts"
description: "Step-by-step explanation of initial margin, variation margin, and margin calls in futures; the daily cash mechanics."
keywords:
  - how margin works in futures
  - futures margin requirements
  - variation margin futures
  - margin call futures
image: /svg/derivatives.svg
---

*To trade a [futures contract](/futures-contract/), a trader must post **initial margin** — a performance bond held by the clearinghouse to guarantee the trader can cover daily losses. Each day, the position is marked-to-market, and **variation margin** is credited or debited from the account: profits are paid out, losses are withdrawn. If the account balance falls below the **maintenance margin** threshold, a **margin call** forces the trader to deposit more cash or close the position.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Futures Margin — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives." />

<div class="wiki-infobox-caption">Daily settlement of gains and losses requires continuous cash management; shortfalls trigger forced liquidation.</div>

|   |   |
|---|---|
| **Initial margin** | Cash posted upfront to open a futures position; typically 5–15% of contract notional value |
| **Variation margin** | Daily cash flow based on mark-to-market P&L; credits profits, debits losses |
| **Maintenance margin** | Minimum balance required; usually 70–75% of initial margin |
| **Margin call** | Demand to deposit cash or reduce exposure when balance falls below maintenance level |
| **Settlement** | Daily; the clearinghouse marks positions at day's end and settles cash flows |
| **Leverage** | Futures offer implicit leverage; small margin controls large notional exposure |
| **Counterparty** | Clearinghouse, not the other trader; eliminates bilateral credit risk |

</aside>

## The three layers: initial, variation, and maintenance

A futures margin account operates on three interconnected concepts, each serving a specific function.

**Initial margin** is the amount a trader deposits to open a [futures position](/futures-contract/). It is not a down payment on the contract's notional value; it is a good-faith deposit that guarantees the trader can cover daily losses. On a crude oil futures contract trading at $80 per barrel, controlling 1,000 barrels (notional value $80,000), the exchange might require initial margin of $8,000 — roughly 10%. The trader posts $8,000 to the clearinghouse and gains the right to hold the position.

**Variation margin** is the daily cash settlement. Every trading day, the clearinghouse marks the position to the closing price (or, during the day, to a theoretical mark). If the oil price rises to $81, the trader has an unrealized gain of $1,000 (1,000 barrels × $1 move). The clearinghouse immediately credits that $1,000 to the margin account — it is available cash. If the price drops to $79, the trader has a $1,000 loss; the clearinghouse debits $1,000 from the margin account.

This daily settlement is called **mark-to-market**. Unlike a stock broker account, where gains and losses are unrealized until the position is closed, a futures account realizes P&L every single day. The trader's margin balance is the initial deposit plus all accumulated variation margin (profits and losses).

**Maintenance margin** is a threshold, typically set at 70–75% of the initial margin requirement. If the balance drops below that level, the broker issues a **margin call**: the trader must deposit cash to bring the account back above maintenance, usually within a few hours. Failure to do so triggers automatic liquidation of the position at market price.

## A worked example: long oil futures

Imagine a trader believes oil prices will rise, so she buys one crude-oil futures contract. The contract controls 1,000 barrels. Spot oil is $80/barrel. Notional value: $80,000.

The exchange sets initial margin at $8,000 and maintenance margin at $6,000 (75% of initial). The trader deposits $8,000. Margin balance: $8,000.

**Day 1:** Oil closes at $81. Gain: $1,000. Variation margin: +$1,000 credited. Margin balance: $9,000.

**Day 2:** Oil drops to $78. Loss: $3,000. Variation margin: −$3,000 debited. Margin balance: $6,000.

The account balance has fallen to exactly the maintenance threshold. The trader can still hold but receives a warning. One more adverse move and a margin call will be issued.

**Day 3:** Oil falls further to $76. Loss: $2,000. Variation margin: −$2,000 debited. Margin balance: $4,000.

The balance has fallen below $6,000 maintenance. A margin call is issued: the trader must deposit at least $2,000 before the market opens tomorrow to bring the account above $6,000. If she does not, the broker closes the position at market price (currently showing a $4,000 loss — if the price is $76, the trader was long 1,000 barrels bought (in her head) at $80, now worth $76, net loss of $4,000).

**Day 3 afternoon:** The trader deposits $3,000. Margin balance: $7,000. Margin call is cleared.

**Day 4:** Oil rallies to $79. Gain: $3,000. Variation margin: +$3,000 credited. Margin balance: $10,000. The trader is back in profit.

## Why margin requirements exist

Margin requirements serve two purposes: leverage and risk control.

**Leverage:** A trader who posts $8,000 controls a position worth $80,000. That is 10x leverage. Futures are inherently leveraged; the exchange is lending implicit exposure. The trader risks only the margin posted (in the worst case), but the upside or downside is proportional to the full contract value. A $10 move in oil (from $80 to $90) nets the trader $10,000 on the $8,000 margin — a 125% return. This is why retail traders are often drawn to futures; the leverage is seductive.

**Risk control:** The clearinghouse wants assurance that the trader can cover daily losses. If oil plummets $20 overnight, the trader owes $20,000. If the trader has posted only $8,000, the clearinghouse is exposed. By requiring a maintenance buffer and issuing margin calls, the clearinghouse limits its credit exposure to each trader. The clearinghouse does not want to find itself holding an uncovered loss.

## Leverage and risk

The leverage inherent in margin is where fortunes are made and lost. Consider two scenarios with our oil trader.

**Scenario A: Trader posts $8,000 margin, price rises $10 (from $80 to $90).**
- Notional gain: $10,000
- Margin posted: $8,000
- Return on margin: 125% in one day

**Scenario B: Same trader, same margin, price falls $10 (from $80 to $70).**
- Notional loss: $10,000
- Margin posted: $8,000
- Loss exceeds margin. Trader still owes $2,000 beyond the deposit.

In Scenario B, the trader's account is wiped out. The broker issues a margin call for $4,000+ to bring the account back to maintenance. If the trader cannot meet the call, the position is closed at market price ($70), crystallizing the loss.

This is the dark side of leverage: a loss larger than the margin posted can be forced upon the trader. A $10 move against a $80,000 position on $8,000 margin is a total wipeout. Leverage amplifies both gains and losses; the math is ruthless.

## Clearinghouse dynamics

Futures clearinghouses (like the CME Clearing in the US) sit in the middle of every trade. When a trader buys one contract, a seller is matched (or the clearinghouse becomes the counterparty). But the clearinghouse does not hold the credit risk of both traders against each other — it becomes the buyer to the seller and the seller to the buyer. This is called **novation**.

The trader's counterparty risk is now the clearinghouse, not another trader. The clearinghouse collects margin from both sides (the long and the short) and settles variation margin daily. If a trader defaults, the clearinghouse has margin pledged and can liquidate the position, using the proceeds to cover its own loss. In theory, the clearinghouse is protected; in practice, severe market gaps can exceed margin posted.

This structure makes margin requirements paramount. Too low, and the clearinghouse is exposed. Too high, and traders avoid the market. The clearinghouse adjusts requirements based on volatility and tail risk, raising margin in volatile markets to discourage outsized speculation.

## Differences across markets

Initial margin varies wildly by contract and volatility. A liquid S&P 500 futures contract might require only 2–3% of notional value (massive leverage). A volatile emerging-market currency futures contract might require 15–20%. The exchange sets requirements and adjusts them intraday or overnight if market conditions warrant.

Maintenance margin is almost always set as a percentage of initial margin (70–75%), but some firms impose stricter internal minimums. A bank's trading desk might require internal maintenance at 90% of initial, well above the exchange minimum, to cushion against intraday volatility and ensure margin calls are met before positions are forced closed.

Variation margin is standardized: daily mark-to-market, cash settlement. But the timing differs. Some contracts settle at the official close; others use a daily settlement price computed from the closing price range. The detail matters for high-frequency traders, but for longer-term position holders, the daily settlement rhythm is the same.

## Margin in crises

When markets gap sharply — a flash crash, a geopolitical shock, a central bank surprise — variation margin can move violently in hours or minutes. A trader long oil futures during a sudden Saudi announcement faces not a $10 daily move but a $20 overnight move. If his margin account was at $7,000 (above maintenance) before the news, a $20,000 loss brings it to −$13,000. The broker closes the position at market price, crystallizing the loss, and the trader receives a bill for the amount owed above the margin posted.

This is why margin calls are sometimes issued intraday, not just at the close. If a market moves sharply during the trading day, the clearinghouse may demand additional margin before the close to protect itself. A trader not monitoring the account carefully can be forced into unwanted liquidations or face large margin calls requiring immediate cash.

## See also

<div class="wiki-seealso">

### Closely related

- [Futures contract](/futures-contract/) — the underlying instrument; mark-to-market and margined daily
- [Mark-to-market](/mark-to-model-valuation/) — daily revaluation of positions used to compute variation margin
- [Leverage](/leverage-ratio-forex/) — the implicit amplification of returns (and losses) that margin provides
- [Clearinghouse](/federal-reserve/) — institution that collects margin and guarantees settlement
- [Counterparty risk](/counterparty-risk/) — credit risk eliminated by clearinghouse novation
- [Spread](/bid-ask-spread/) — the difference between bid and ask; important for entry and exit costs in futures

### Wider context

- [Derivatives](/derivatives-hedging/) — broad overview; futures are one type of derivative
- [Risk management](/stress-testing/) — strategies to limit losses, including margin monitoring
- [Leverage buyout](/leveraged-buyout/) — a corporate finance application; margin works similarly
- [Volatility](/historical-volatility/) — changes in volatility drive changes in margin requirements

</div>
