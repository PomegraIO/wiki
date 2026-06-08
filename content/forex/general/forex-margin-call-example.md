---
title: "Forex Margin Call: How It Happens with an Example"
description: "Step-by-step walkthrough of a forex margin call: how leverage amplifies losses and what happens when required capital falls below the threshold."
keywords:
  - forex margin call example
  - margin call forex trading
  - forex leverage risk
  - margin requirement forex
  - forced liquidation forex
  - currency trading margin
---

*A **forex margin call** occurs when your account equity drops below the broker's maintenance requirement due to adverse price moves on your leveraged positions. Understanding how this happens—through a worked example—reveals why leverage amplifies both gains and losses, and why a small move in a currency pair can wipe out your capital.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Forex Margin Call Mechanics</div>

<img src="/svg/forex.svg" alt="An abstract editorial mark for forex trading." />

<div class="wiki-infobox-caption">Leverage cuts both ways; margin requirements enforce the downside.</div>

|   |   |
|---|---|
| **Margin requirement** | Typically 1–5% of position notional value (1:100 to 1:20 leverage) |
| **Maintenance margin** | Often 50% of initial margin; falling below triggers a call |
| **Margin call trigger** | Account equity ÷ used margin < maintenance ratio (e.g., 50%) |
| **Outcome** | Broker closes positions, usually at market, to bring account into compliance |
| **Speed** | Can happen intraday during high volatility or gapping price moves |
| **Recovery** | Depositing cash can halt liquidation; otherwise, forced sale locks in losses |
| **Account blow-up** | Equity can reach zero if losses exceed total capital |

</aside>

## A Concrete Margin Call Scenario

Imagine you open a forex account with a broker offering 100:1 leverage and deposit $5,000. You believe the EUR/USD pair will rise and want exposure to the move.

**Initial trade setup:**

- You buy 1 lot (100,000 euros) of EUR/USD at 1.0800.
- **Notional exposure**: 100,000 EUR × 1.0800 = $108,000.
- **Margin required (at 1% = 100:1 leverage)**: 1% of $108,000 = $1,080.
- **Account equity after trade**: $5,000 (unchanged by the trade itself).
- **Used margin**: $1,080.
- **Available margin**: $5,000 − $1,080 = $3,920.
- **Margin level**: ($5,000 / $1,080) × 100 = 463%.

You're in good shape. Your margin level is well above any threshold (many brokers call a margin call at 100% or lower).

## The Move: Losses Accumulate

EUR/USD begins to fall. You hold the position, expecting a rebound.

**After EUR/USD drops to 1.0750** (a 50-pip move down):

- **Current position value**: 100,000 EUR × 1.0750 = $107,500.
- **Unrealized loss**: $108,000 − $107,500 = −$500.
- **Account equity now**: $5,000 − $500 = $4,500.
- **Used margin**: Still $1,080 (no change; margin requirement is based on position, not value).
- **Available margin**: $4,500 − $1,080 = $3,420.
- **Margin level**: ($4,500 / $1,080) × 100 = 417%.

Still safe. But let's accelerate.

## The Crisis: Equity Erodes Toward the Threshold

**EUR/USD falls further to 1.0500** (a 300-pip total move):

- **Current position value**: 100,000 EUR × 1.0500 = $105,000.
- **Unrealized loss**: $108,000 − $105,000 = −$3,000.
- **Account equity**: $5,000 − $3,000 = $2,000.
- **Used margin**: $1,080 (still tied to the 1-lot position).
- **Available margin**: $2,000 − $1,080 = $920.
- **Margin level**: ($2,000 / $1,080) × 100 = 185%.

Uncomfortable, but still above 100%. Continue.

**EUR/USD falls to 1.0450** (a 350-pip move):

- **Current position value**: 100,000 EUR × 1.0450 = $104,500.
- **Unrealized loss**: $108,000 − $104,500 = −$3,500.
- **Account equity**: $5,000 − $3,500 = $1,500.
- **Used margin**: $1,080.
- **Available margin**: $1,500 − $1,080 = $420.
- **Margin level**: ($1,500 / $1,080) × 100 = 139%.

Close now. Let's assume your broker's maintenance margin is 50% of initial margin. That means when margin level falls below **50%**, a margin call is triggered.

**EUR/USD falls to 1.0370** (a 430-pip move):

- **Current position value**: 100,000 EUR × 1.0370 = $103,700.
- **Unrealized loss**: $108,000 − $103,700 = −$4,300.
- **Account equity**: $5,000 − $4,300 = $700.
- **Used margin**: $1,080.
- **Available margin**: $700 − $1,080 = −$380 (NEGATIVE).
- **Margin level**: ($700 / $1,080) × 100 = 65%.

The margin level is now below the threshold (typically around 50% maintenance margin). **Margin call triggered.**

## What Happens Next: Forced Liquidation

At this point, your broker has the right—and the contractual obligation to clients—to close your position to restore the account to compliance. 

**The forced close:**

The broker closes your 1-lot long EUR/USD position at the **current market price**, which let's say is 1.0370 (or worse, if the market gaps further in the seconds it takes to execute).

- **Realized loss on close**: $108,000 − $103,700 = −$4,300.
- **Final account equity**: $5,000 − $4,300 = $700.
- **New used margin**: $0 (position closed).
- **Margin level**: Infinity (no open positions).

You've locked in a $4,300 loss (86% of your initial $5,000 capital) and have $700 left. Your account is now in compliance with margin rules because you have no open positions.

## The Cascading Risk: Why Margins Matter

Here's the crucial insight: leverage amplified your loss. Without the 100:1 leverage, you would have bought ~463 EUR at $1.0800 ($5,000 ÷ 1.0800). The same 430-pip move would have cost you $24 (463 EUR × 0.0430 pips). Leverage turned a manageable dip into capital obliteration.

The margin call was the broker's safety valve. Without forced liquidation rules, your loss could have exceeded your $5,000 if the currency kept falling (and some brokers, during flash crashes, have allowed negative balances). The call prevents that catastrophic overflow but locks in losses for the trader.

## Key Variables: Margin and Volatility

Different brokers set different maintenance margins. Some use a fixed 50% rule; others use tiered maintenance (higher for larger accounts). Volatility also matters: if EUR/USD is choppy (high intraday swings but range-bound), you might never hit the call. If it gaps overnight (e.g., political shock), you wake up to a margin call and a forced close at a terrible price.

## What an Account Holder Can Do

**Before a call:**
- Tighten risk management by setting stop-losses above the margin call threshold.
- Reduce position size or leverage to lower the margin requirement.
- Monitor margin level in real-time and close positions preemptively if it trends downward.

**During a call:**
- Deposit cash to increase equity and bring the margin level above the maintenance threshold.
- Manually close positions to free up margin (and cut losses on your terms, not the broker's).
- Call the broker—some will grant a brief grace period, though most will not.

**After a call:**
- If it happened, it's a flashing signal that your [leverage](/leverage-ratio-forex/) was too high for your capital or risk tolerance.

## See also

<div class="wiki-seealso">

### Closely related

- [Margin call (forex)](/margin-call-forex/) — General definition and mechanics
- [Leverage ratio (forex)](/leverage-ratio-forex/) — How to calculate and manage leverage exposure
- Forex trading — Overview of the market and mechanics
- [Bid-ask spread](/bid-ask-spread/) — Execution cost that worsens margin call fills
- [Currency volatility](/currency-volatility/) — What drives the price moves that trigger calls

### Wider context

- Risk management — Framework for avoiding margin calls altogether
- [Liquidity risk](/liquidity-risk/) — Why forced liquidations happen at bad prices
- Stop-loss order — Tool to prevent margin calls
- [Counterparty risk](/counterparty-risk/) — Broker reliability in a margin call situation

</div>
