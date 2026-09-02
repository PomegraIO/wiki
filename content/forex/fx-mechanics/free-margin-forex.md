---
title: "Free Margin"
description: "Available capital remaining after accounting for used margin, showing how much a forex trader can deploy to open new positions."
keywords:
  - free margin
  - available margin
  - used margin
  - margin trading forex
  - trading leverage
  - account equity
image: /svg/forex.svg
---

*Free margin is the portion of a trader's account equity that is not locked up in open positions. It is calculated as equity minus used margin, and it represents the real purchasing power remaining to open new trades. When free margin hits zero, no new positions can be opened; when it turns negative, the [broker](/broker/) typically triggers a [margin call](/margin-call-forex/) or forced liquidation.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Free Margin — key facts</div>

<img src="/svg/forex.svg" alt="An abstract editorial mark for finance." />

<div class="wiki-infobox-caption">The amount of equity available to open new positions before hitting margin requirements.</div>

|   |   |
|---|---|
| **What it is** | Equity minus used margin; available capital for new trades |
| **Formula** | Free margin = Account equity − Used margin |
| **Account equity** | Deposit + Floating profit/loss on open positions |
| **Used margin** | Capital locked by [broker](/broker/) to support current open positions |
| **Key threshold** | Zero free margin = no new positions allowed |
| **Broker enforcement** | Monitored in real time; violations trigger [margin calls](/margin-call-forex/) or forced closes |
| **Leverage link** | Higher leverage amplifies both profit potential and free-margin depletion |

</aside>

## The three components: equity, used, and free

Understanding free margin requires three numbers:

1. **Equity** — your deposit plus or minus the floating profit and loss (P&L) of open positions. If you deposited $10,000 and have $500 unrealised gains, equity is $10,500.

2. **Used margin** — the capital your broker requires you to lock up to support open positions. On a standard [broker](/broker/) with 50:1 leverage, a $100,000 position in EUR/USD requires $2,000 used margin ($100,000 ÷ 50). If you have three open positions totalling $500,000, used margin is $10,000.

3. **Free margin** — the difference. In the example above, if your equity is $10,500 and used margin is $10,000, free margin is $500. That $500 is all you can use to open new positions.

This is the real constraint in leverage trading. A [broker](/broker/) does not lend you infinite capital; it lends you up to a multiple of your equity (the leverage ratio), but requires you to maintain minimum free margin. As soon as free margin vanishes, the [broker](/broker/) stops you from taking on more risk.

## Why brokers enforce free margin limits

A [broker](/broker/) enforces free margin rules because its own [risk](/operational-risk/) depends on it. If a trader deposits $10,000 and receives 50:1 leverage, the [broker](/broker/) can in theory accommodate up to $500,000 in notional exposure. But if the market moves against the trader, that $10,000 equity will erode.

The free margin requirement is the [broker](/broker/)'s guard rail. Most brokers require at least 2% used margin, meaning free margin must stay above 2% of all open positions. On a $100,000 position with 50:1 leverage, that is $2,000 used margin. If a trader deposits only $10,000 and wants a $500,000 position, $10,000 used margin is needed, leaving zero free margin and no buffer for losses.

If market moves cause unrealised losses to exceed free margin, the [broker](/broker/) either issues a [margin call](/margin-call-forex/) (demanding more deposit) or automatically liquidates positions to restore free margin. The goal is to prevent the trader's losses from exceeding the deposit, which would leave the [broker](/broker/) exposed.

## How free margin shrinks and recovers

Free margin swings dramatically in leverage trading. Suppose a trader has:

- Deposit: $10,000
- Unrealised P&L: +$2,000 (good day)
- Used margin: $5,000
- **Free margin: $7,000**

Next hour, the market moves hard against the position:

- Deposit: $10,000
- Unrealised P&L: −$3,000 (bad turn)
- Used margin: $5,000
- **Free margin: $2,000**

Free margin fell by $5,000 (the swing in losses). If the market moves another $2,000 against the trader, free margin hits zero and the [broker](/broker/) stops new orders. Another $1,000 loss triggers a [margin call](/margin-call-forex/) or forced close.

Conversely, when a winning trade is closed, the profit flows into equity and free margin jumps. If the trader closes the losing position with a $1,000 loss, equity drops to $9,000, but used margin also drops (say, to $3,000), so free margin is $6,000. This recovery of free margin is psychologically powerful—it gives traders the illusion of a "second chance" to trade again—which is why many over-leverage accounts blow up in rebounds.

## Free margin and risk management

Experienced traders use free margin as their primary risk gauge. A [margin level](/margin-level-forex/) of 200% is the mathematical minimum most brokers allow; at that point, free margin is 50% of equity. But most professionals never get close.

A rule of thumb: keep free margin at least 30–50% of equity. This buffer means:

- Market swings of 2–5% against your position do not threaten your account
- You can open new positions without gambling on [liquidation](/liquidation/)
- You have breathing room to hold trades through intraday volatility

Brokers also use free margin to calculate [margin level](/margin-level-forex/) and determine when to force-close positions. A typical trigger is [margin level](/margin-level-forex/) below 50%, which means used margin is double equity. At that point, free margin is either zero or negative (in which case the account is already being liquidated).

## The leverage trap

Free margin is where the leverage trap springs. With 100:1 leverage, a $10,000 account can control $1,000,000 in notional currency. But used margin is only $10,000, leaving the entire deposit as free margin. A single adverse 1% move erases half of free margin. A 2% move wipes it out.

New traders often misunderstand leverage. They see that their $10,000 is "buying power" of $1,000,000 and imagine they can trade that full amount. In reality, free margin is the binding constraint. The account can hold maybe $50,000–$100,000 notional before free margin becomes dangerously low.

Casinos would recognize this mechanic: the [broker](/broker/) is not betting against the trader, but it is ensuring the trader has "skin in the game." Free margin is the mechanism that forces traders to be conservative. When free margin is nearly gone, the trader's emotions are heightened and risk appetite vanishes—and that is often when the market rebounds and wipes out the rest.

## Free margin vs. [margin level](/margin-level-forex/)

Free margin and [margin level](/margin-level-forex/) are related but distinct. Free margin is an absolute dollar amount. [Margin level](/margin-level-forex/) is a ratio (equity ÷ used margin × 100), expressed as a percentage. A trader might have:

- Equity: $10,000
- Used margin: $5,000
- Free margin: $5,000 (dollars)
- [Margin level](/margin-level-forex/): 200% (ratio)

Both are monitored by the [broker](/broker/). Free margin tells you how many dollars you can still deploy. [Margin level](/margin-level-forex/) tells you how close you are to forced liquidation. Most traders think in terms of [margin level](/margin-level-forex/), but free margin is often more intuitive: "I have $2,000 left to trade with."

## See also

<div class="wiki-seealso">

### Closely related

- [Margin level](/margin-level-forex/) — the equity-to-used-margin ratio that determines forced liquidation
- [Margin call](/margin-call-forex/) — triggered when free margin falls too low or [margin level](/margin-level-forex/) breaches a threshold
- [Leverage](/leverage-ratio-forex/) — the multiple of equity a [broker](/broker/) allows; directly affects used margin
- Used margin — the component of equity locked by open positions
- [Liquidation](/liquidation/) — forced closure of positions when free margin is depleted

### Wider context

- [Broker](/broker/) — the institution enforcing free margin limits
- Foreign exchange markets — where leverage and margin are primary tools
- [Counterparty risk](/counterparty-risk/) — the [broker's](/broker/) hazard when managing margined accounts

</div>
