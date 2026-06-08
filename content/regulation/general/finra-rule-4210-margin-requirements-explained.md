---
title: "FINRA Rule 4210: Margin Maintenance Requirements Explained"
description: "FINRA Rule 4210 sets minimum equity maintenance margins: 25% for long positions, 30% for short positions. A margin call triggers when equity falls below these thresholds."
keywords:
  - finra rule 4210
  - margin maintenance requirements
  - margin call
  - maintenance margin threshold
  - equity cushion
  - leveraged trading
image: "/svg/regulation.svg"
---

*The **FINRA Rule 4210 margin maintenance requirements** define the minimum equity level a trader must maintain in a brokerage account to avoid a margin call. For long positions, that floor is 25%; for short positions, it's 30%. When account equity drops below either threshold, the broker issues a margin call demanding cash or collateral to restore the cushion.*

## What is FINRA Rule 4210?

FINRA Rule 4210 is the regulatory standard that governs maintenance margin—the percentage of account equity a trader must hold relative to borrowed funds. It applies to all securities lending and borrowing in the United States and sets enforceable minimums that brokers cannot undercut, though they may impose stricter house rules.

The rule exists because margin amplifies both gains and losses. Without a maintenance floor, a trader could theoretically lose the entire borrowed amount plus the initial deposit; the margin requirement acts as a financial circuit breaker, forcing deleveraging when account equity shrinks to dangerous levels.

## The 25% Floor for Long Positions

When a trader buys on margin—borrowing money to purchase more shares than cash alone would allow—FINRA requires that the account maintain at least 25% equity in the position at all times.

To illustrate: suppose a trader deposits $10,000 and borrows $30,000, purchasing $40,000 of stock. The initial equity is $10,000 / $40,000 = 25%, so this meets the minimum. If the stock rises to $50,000, the equity becomes $20,000 / $50,000 = 40%, well above the floor. But if the stock falls to $30,000, the equity drops to $0 / $30,000 = 0%, and the account has already triggered a call. 

The triggering point is when equity reaches 25% of current market value. At that moment, the broker will demand deposit of additional cash or securities to restore equity to the minimum. Failure to meet the call within the specified time frame (typically two business days) gives the broker the right to liquidate positions to recover the borrowed amount.

## The 30% Floor for Short Positions

Short sales—borrowing shares and selling them, hoping to buy them back cheaper—face a higher maintenance requirement of 30% equity. This reflects the asymmetric risk: while long stock losses are capped at 100% of capital (the stock cannot go below zero), short stock losses are theoretically unlimited (a stock can rise indefinitely).

Example: a trader sells short 100 shares at $100 each, depositing $10,000 in margin. Initial equity is $10,000 / $10,000 = 100%. If the stock rises to $120, the short position loses $2,000 in unrealized loss, and equity becomes $8,000 / $12,000 = 67%. The position is still safe. But if the stock rises to $143, the equity drops to $7,000 / $14,300 ≈ 49%. At $154, equity hits 30% ($10,000 - $5,400 = $4,600 / $15,400 ≈ 30%), triggering a margin call. The trader must deposit additional capital or cover part of the short sale.

## How Equity is Calculated

Account equity under FINRA Rule 4210 is the total market value of all positions plus cash, minus all borrowed amounts.

**Equity = (Market Value of Holdings + Cash) − Debt**

For a margin account holding multiple securities and cash:
- Mark all positions to current market price (real-time or closing price, depending on broker policy).
- Subtract the outstanding loan balance.
- The result is the equity cushion.

Some brokers calculate this intra-day; others at market close. The more frequent the calculation, the tighter the monitoring. During rapid market moves, an account can swing between compliant and margin call within minutes.

## Margin Call Mechanics

When equity falls below the regulatory minimum, the broker issues a margin call specifying the amount of cash or marginable securities needed to restore equity to a comfortable level—often 40% or higher, depending on broker policy.

The call typically allows 2–5 business days to meet it. Options include:

- **Deposit cash**: The fastest method; directly increases equity.
- **Deposit marginable securities**: Securities with high loan-value ratios (typically established stocks and ETFs) can satisfy a call.
- **Liquidate positions**: The trader can sell holdings to generate cash and reduce debt, thus raising equity.
- **Do nothing**: If the deadline passes, the broker has the right to liquidate positions unilaterally to meet the requirement. This forced liquidation is costly and unwanted—the broker executes at market prices without negotiation.

## Maintenance Margin vs. Initial Margin

Beginning traders often confuse two separate FINRA standards. **Initial margin** (Regulation T, typically 50%) is the deposit required to open a position. **Maintenance margin** (Rule 4210) is the ongoing floor to avoid a call.

A trader must deposit 50% to initiate a long stock purchase but only maintain 25% to keep it open. This gap creates a risk: if the stock drops 50%, it might liquidate your position to meet maintenance, even though you had sufficient initial capital.

## Broker Discretion and House Rules

FINRA sets the floor, but brokers can impose stricter standards. Many large firms maintain 30% for long positions and 40% for short, adding safety margin and reducing operational risk. Brokers can also vary requirements by:

- **Stock liquidity**: Penny stocks and micro-caps often carry 50%+ maintenance requirements.
- **Market volatility**: In sharp downturns, brokers may tighten margins preemptively.
- **Account size**: Larger accounts sometimes receive preferential treatment; very small accounts face higher hurdles.
- **Customer profile**: Professional traders, pattern-day traders, and institutional accounts may have different rules than retail customers.

Always check the broker's margin agreement before opening an account; never assume FINRA minimums apply to your account.

## Risk and Volatility Implications

The 25%/30% rule means a relatively small loss can trigger a call. In a long position, a 75% decline erases equity entirely; a 50% move is often enough to approach the threshold. Short positions are even more vulnerable to rapid moves, which is why the 30% requirement exists.

High-volatility names—tech stocks during earnings, commodity stocks in commodity crashes—pose greater margin risk. A trader carrying a full-margin position in a volatile stock faces constant call risk during uncertain market periods.

## Position Adjustment Strategies

Experienced margin traders adjust position size to stay well above minimums. Some rules of thumb:

- Maintain 40% or higher equity as a personal buffer.
- Avoid full leverage (using the maximum borrowed capital allowed).
- Keep marginable securities that you can quickly liquidate without disrupting your core strategy.
- Monitor intra-day price moves on volatile holdings and be ready to deposit cash if needed.

## See also

<div class="wiki-seealso">

### Closely related

- [Margin call forex](/margin-call-forex/) — how margin calls operate in currency trading
- [Leverage ratio forex](/leverage-ratio-forex/) — understanding leverage limits in forex accounts
- [Loan-to-value ratio](/loan-to-value-ratio/) — the equity cushion concept applied to real estate and collateralized lending
- [Broker](/broker/) — roles and obligations of a securities broker
- [Debt financing](/debt-financing/) — using borrowed capital in investment and business
- [Counterparty risk](/counterparty-risk/) — the risk that a broker defaults or fails to meet obligations

### Wider context

- [Securities and Exchange Commission](/securities-and-exchange-commission/) — regulatory authority over broker-dealers
- [FINRA](/finra/) — self-regulatory organization that issues Rule 4210
- [Stock market](/stock-market/) — the broader ecosystem where margin trading occurs
- [Risk weighted assets](/risk-weighted-assets/) — how banks measure capital adequacy, a related concept

</div>
