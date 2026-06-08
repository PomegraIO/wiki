---
title: "Margin Level"
description: "The ratio of account equity to used margin, expressed as a percentage; triggers margin calls and forced liquidation when it falls below broker thresholds."
keywords:
  - margin level
  - equity-to-margin ratio
  - margin call trigger
  - forex leverage risk
  - liquidation threshold
  - trading account health
image: /svg/forex.svg
---

*Margin level is a simple ratio: (Account equity ÷ Used margin) × 100. It is the percentage that measures how much equity cushions your open positions relative to the margin they consume. When margin level drops below a threshold—typically 100% or 50%, depending on the [broker](/broker/)—a [margin call](/margin-call-forex/) or forced liquidation is triggered. It is the most direct gauge of account distress in leverage trading.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Margin Level — key facts</div>

<img src="/svg/forex.svg" alt="An abstract editorial mark for finance." />

<div class="wiki-infobox-caption">The ratio that determines when a broker forces position closure to protect its own exposure.</div>

|   |   |
|---|---|
| **What it is** | (Equity ÷ Used margin) × 100; expressed as a percentage |
| **Formula** | Margin level % = (Equity ÷ Used margin) × 100 |
| **Account equity** | Deposit plus or minus floating profit/loss on open positions |
| **Healthy range** | 300–500%+ (trader has room to absorb losses) |
| **Caution zone** | 100–200% (equity is 1–2× used margin; losses are mounting) |
| **Danger zone** | Below 100% (equity is less than used margin; forced liquidation begins) |
| **Key thresholds** | Varies by [broker](/broker/) and currency; commonly 100% (call), 50% (force-close) |
| **Real-time monitoring** | [Brokers](/broker/) monitor continuously during market hours |

</aside>

## The fundamental ratio

Margin level boils down to a single question: how much equity supports each dollar of used margin? 

If a trader has $10,000 equity and $5,000 used margin, margin level is 200%. That trader has $2 in equity for every $1 in margin locked up. If the trader has $10,000 equity and $10,000 used margin, margin level is 100%—equity equals locked capital. If equity drops to $5,000, margin level falls to 50%, and equity is half of the margin consumed.

A high margin level (say, 500%) means the account is safe; it can absorb large adverse moves before losses exceed equity. A low margin level (say, 80%) means losses are already substantial and the account is in danger.

Unlike [free margin](/free-margin-forex/), which is stated in dollars, margin level is a ratio. This makes it easier to compare risk across accounts of different sizes. A $100,000 account at 150% margin level is in the same relative danger as a $1,000 account at 150% margin level.

## How brokers use margin level to manage risk

A [broker](/broker/) does not care about absolute dollar size; it cares about proportional risk. That is why [brokers](/broker/) define thresholds in terms of margin level rather than [free margin](/free-margin-forex/).

Most [brokers](/broker/) operate two thresholds:

| Margin level | Broker action |
|---|---|
| Above 100% | Normal trading; new orders accepted |
| 50–100% | [Margin call](/margin-call-forex/); trader must deposit funds or close positions |
| Below 50% | Force-close (automatic liquidation); [broker](/broker/) closes positions unilaterally |

When margin level falls to 50%, the [broker](/broker/) usually begins closing positions one by one (starting with the largest or most profitable) until margin level is restored above the force-close threshold—often 50–100%, depending on the [broker](/broker/).

The reason for these hard thresholds is that the [broker](/broker/) is managing its own [counterparty risk](/counterparty-risk/). If a trader's margin level falls below 50% and the market continues to gap (especially overnight or on a news event), the trader's losses could exceed the account balance. The [broker](/broker/) would be out the difference. By force-closing early, the [broker](/broker/) limits its loss to the amount of equity remaining.

## The margin call and the forced liquidation cascade

A margin call is a demand: deposit more money, or positions will be closed. It is the [broker's](/broker/) last soft warning. Many traders ignore margin calls or cannot meet them fast enough. When a margin call is not answered and margin level keeps falling, the [broker](/broker/) moves to automatic liquidation.

Force-closing is brutal. Positions are closed at market price—often the worst prices of the day, especially if the market is moving fast. A trader with three open positions might see one closed automatically, then another, then a third, each time suffering slippage. [Free margin](/free-margin-forex/) shrinks faster as the account is dismantled because the equity is often negative by the time liquidation starts.

Once force-close has begun, the trader has no control. The [broker's](/broker/) algorithm closes positions algorithmically until margin level is restored. In extreme cases—a currency gap at market open, a central bank surprise—the trader's equity can be completely wiped out and the [broker](/broker/) may demand payment for the deficit. This is the ultimate risk in leverage trading.

## Margin level during the trading day

Margin level is not static. It changes minute by minute as prices move and floating P&L swings.

Consider a trader with $10,000 equity and $9,000 used margin (margin level = 111%). The market moves favourably, and unrealised profit climbs to $5,000. Equity becomes $15,000, and margin level jumps to 167% (15,000 ÷ 9,000). The account just moved out of danger.

Now the market reverses hard. Unrealised loss reaches $8,000. Equity drops to $2,000, and margin level plummets to 22% (2,000 ÷ 9,000). A [margin call](/margin-call-forex/) is issued or force-close begins. Everything depends on how fast the market moves relative to the [broker's](/broker/) ability to liquidate.

This volatility is why margin level is monitored in real time. A [broker's](/broker/) risk management system recalculates margin level continuously and is programmed to trigger actions—[margin calls](/margin-call-forex/), e-mail alerts, or automatic liquidation—when thresholds are crossed.

## Margin level vs. [free margin](/free-margin-forex/)

Margin level and [free margin](/free-margin-forex/) describe the same situation from different angles.

- **[Free margin](/free-margin-forex/)** tells you how many dollars you have left to deploy. A trader with $10,000 equity, $7,000 used margin has $3,000 free margin.
- **Margin level** tells you the proportional cushion. The same trader has a margin level of 143% (10,000 ÷ 7,000).

A trader with $1,000,000 equity and $900,000 used margin has $100,000 free margin and a margin level of 111%—a lot of free margin in dollars, but proportionally tight. Conversely, a trader with $10,000 equity and $500 used margin has $9,500 free margin but a margin level of 2,000%—tiny risk.

Professional traders think in both terms, but [brokers](/broker/) enforce margin level thresholds because they are unambiguous and scalable across all account sizes.

## Manipulation and gaming margin level

Some traders attempt to game margin level in ways that [brokers](/broker/) do not allow:

- **Hedging both sides** — Opening offsetting positions (long and short) to keep used margin high while reducing [free margin](/free-margin-forex/), hoping losses on one side cancel the other. Most [brokers](/broker/) do not count offsetting positions as fully reduced used margin if they are in the same instrument.

- **Holding positions overnight** — Keeping positions open to avoid realising losses, hoping tomorrow's move restores equity. If the market gaps overnight, margin level can collapse before the trader can react.

- **Rapid re-entry** — Closing a losing position and immediately reopening it at a "better" level. This does not change the mathematical risk, but it can provide temporary relief from margin monitoring if the [broker](/broker/) has a lag in position reporting.

None of these strategies work long-term. Margin level is a brute-force measure of solvency. You cannot hide from it by accounting tricks; you can only manage it by reducing used margin (closing positions) or raising equity (depositing more money).

## Margin level in different markets and [brokers](/broker/)

Margin level thresholds are not universal. They vary by:

- **[Broker](/broker/) policy** — A tight [broker](/broker/) might force-close at 100% margin level. A loose one at 20%. (The loose broker is taking more risk.)
- **Currency pair volatility** — Exotics (low-liquidity pairs like USD/ZAR) might have tighter margin requirements and lower force-close thresholds.
- **Time of day** — Some [brokers](/broker/) tighten margin level thresholds during volatile open hours (US, European open) and relax them during quiet periods.
- **Regulatory environment** — In the US, retail FX [brokers](/broker/) are required to maintain certain minimum margin levels by the CFTC. In less regulated jurisdictions, [brokers](/broker/) have more freedom.

Traders should always check their [broker's](/broker/) specific thresholds before opening an account. A [margin level](/margin-level-forex/) of 200% might be safe with one [broker](/broker/) but at the edge of danger with another.

## See also

<div class="wiki-seealso">

### Closely related

- [Free margin](/free-margin-forex/) — the dollar amount underlying the margin level ratio
- [Margin call](/margin-call-forex/) — issued when margin level falls below the call threshold
- [Liquidation](/liquidation/) — forced position closure triggered by low margin level
- Used margin — the denominator in the margin level calculation
- [Leverage](/leverage-ratio-forex/) — determines how much used margin a given position requires
- [Broker](/broker/) — the institution that sets margin level thresholds and enforces them

### Wider context

- Foreign exchange markets — where margin level is a critical control
- Risk management — margin level is a front-line risk measure
- [Counterparty risk](/counterparty-risk/) — the [broker's](/broker/) hazard when a trader's account hits zero

</div>
