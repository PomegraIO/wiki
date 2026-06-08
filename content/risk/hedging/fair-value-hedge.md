---
title: "Fair Value Hedge"
description: "Derivative strategy that offsets changes in the fair value of a recognised asset, liability, or firm commitment."
keywords:
  - fair value hedge
  - asset hedge
  - liability hedge
  - fixed-rate debt
  - fair value accounting
image: "/svg/risk.svg"
---

*A **fair value hedge** is a derivative contract that reduces balance-sheet exposure to price or rate movements on an existing asset, liability, or binding commitment. Unlike a [cash flow hedge](/cash-flow-hedge/)—which protects future uncertain cash flows—a fair value hedge offsets swings in the market value of something already on the books. A bank holding a fixed-rate mortgage portfolio hedges it with [interest-rate swaps](/interest-rate/) to prevent rising rates from eroding the value of those loans; a manufacturer holding inventory locks in the cost with [futures](/futures-contract/) to prevent a price drop from wiping out gross margin. The gain or loss on the derivative flows directly into net income, offsetting the loss or gain on the hedged item itself.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Fair Value Hedge — key facts</div>

<img src="/svg/risk.svg" alt="An abstract editorial mark for financial risk and protection." />

<div class="wiki-infobox-caption">Neutralising the balance-sheet risk that an existing asset or liability will decline in fair value.</div>

|   |   |
|---|---|
| **What it is** | A derivative (swap, forward, option, future) that offsets fair-value changes in a recognised asset, liability, or binding commitment |
| **Typical use** | Banks hedging fixed-rate loan portfolios, manufacturers protecting inventory, treasuries hedging bond holdings, corporates locking in debt repayment risk |
| **Hedging instrument** | [Interest-rate swaps](/interest-rate/), [forwards](/forward-contract/), [options](/call-option/), [futures](/futures-contract/) |
| **Accounting treatment** | Both the hedged item and the hedge are marked to [fair value](/fair-value/) each period; gains/losses go directly to net income |
| **Effectiveness required** | 80–125% hedge effectiveness; ineffective portions go to net income |
| **Scope** | Existing, recognised items on the balance sheet; also binding commitments not yet on the books |

</aside>

## The core idea: matching gains and losses

A company owns an asset or liability whose value changes with market conditions. A bank made a $100 million loan at 3% fixed; if market [interest rates](/interest-rate/) rise to 5%, that loan is now worth less (no borrower would pay par to assume a below-market rate). The bank's balance sheet suffers. A fair value hedge transfers that loss to a derivative that gains when rates rise, so the two cancel out.

The key difference from a [cash flow hedge](/cash-flow-hedge/): in a fair value hedge, the hedged item is already on the balance sheet and already generating stated cash flows. The hedge does not protect future uncertain cash; it protects the current market value of something real and present.

## Fair value vs. cash flow: the right hedge for each situation

**A fixed-rate loan (asset or liability)** is best hedged with a fair value hedge. The bank has committed to paying or receiving a fixed rate. If rates move, the loan's fair value changes; the hedge (usually an [interest-rate swap](/interest-rate/)) offsets that change. The company marks both the loan and the swap to market every quarter, netting out the P&L.

**A floating-rate loan** is best hedged with a [cash flow hedge](/cash-flow-hedge/). The rate is unknown until each reset date; the company is protecting uncertain future cash flows, not a current balance-sheet value.

**Inventory held for sale** is often fair-value-hedged. A manufacturer buys raw materials—copper, wheat, oil—expecting to process and sell them. If the commodity price drops before the sale, profit suffers. The company buys [futures](/futures-contract/) contracts that gain when the commodity price falls, offsetting the inventory loss. Both the inventory and the futures are marked to fair value; the gains and losses net.

**A binding commitment to buy or sell an asset** can be fair-value-hedged before it hits the balance sheet. A retailer commits to buy 10,000 units at a fixed price three months from now (commitment is binding but units are not yet on the books). If the market price drops, the commitment is now a liability—the retailer must pay more than market. A fair value hedge locks in a derivative to offset that loss.

## The accounting: immediate P&L offset

Under [GAAP](/generally-accepted-accounting-principles/) and [IFRS](/international-financial-reporting-standards/), fair value hedges receive straightforward treatment: both the hedged item and the derivative are revalued to fair value each reporting period, and both gains and losses flow to net income.

Example: A bank holds a $100M fixed-rate loan portfolio at 3%. Over one quarter:
- Market rates rise from 4% to 5%.
- The fair value of the loan portfolio falls by, say, $8 million (lower rate means lower value).
- The bank simultaneously holds an [interest-rate swap](/interest-rate/) paying fixed 4% and receiving floating; as floating rates rise, this swap gains $7.9 million.
- Net P&L impact: −$8M + $7.9M = −$0.1M (the small gap is hedge ineffectiveness; most of the loss is offset).
- Both amounts hit net income immediately, creating minimal earnings volatility.

Without the hedge, the P&L would be −$8M—a big hit. With an effective hedge, volatility is reduced to the ineffectiveness portion.

## Fair value hedges in practice: three scenarios

**Scenario 1: The bank's mortgage portfolio.**
A bank has $500 million of fixed-rate mortgages at 4%, most funded by [deposit](/federal-deposit-insurance-corporation/) liabilities (which can be withdrawn or repriced). If rates rise to 6%, the mortgages fall in value but the bank's funding costs rise, creating a squeeze. The bank hedges by receiving fixed and paying floating in a [swap](/interest-rate/); as rates rise, the swap gains (narrowing the margin loss). The swap and mortgage portfolio are both marked to market; the P&L is smoothed.

**Scenario 2: The copper producer.**
A mining company processes copper ore and holds 10,000 tonnes of refined copper inventory awaiting sale. The spot price is $9,000/tonne; the company carries the inventory at fair value, $90 million. The company fears a price drop (say, due to economic slowdown). It sells 10,000 tonnes of copper [futures](/futures-contract/) at $9,000, locking in that price. If the price falls to $8,500:
- Inventory fair value drops to $85 million (−$5 million P&L).
- The [futures](/futures-contract/) contract gains $5 million (company locked in $9,000 but can now buy at $8,500).
- Net P&L: $0 (offset).

**Scenario 3: The utility's debt.**
A regulated utility has $200 million of fixed-rate debt at 5%. Under regulatory rules, it must eventually refinance, and rates may be higher by then. The utility enters a [swap](/interest-rate/) paying fixed and receiving floating. If rates rise:
- The fair value of the debt increases (higher cash outflow to repay at maturity, bad for the utility as a debtor).
- Wait—this seems backwards. In fact, for a debt holder, higher rates mean the liability is worth less to the creditor (lower fair value), so the company's balance-sheet liability *decreases*. The swap, meanwhile, gains.
- Both effects offset in the P&L.

The accounting is subtle: on a liability, a loss in fair value (lower amount owed on the balance sheet) is actually a gain to the company. The hedge gains when rates rise, offsetting the smaller "loss" (actually a gain) on the liability side.

## The effectiveness hurdle

For a hedge to qualify for fair value hedge accounting, it must be "effective"—meaning the derivative's gain or loss should closely offset the hedged item's loss or gain. [GAAP](/generally-accepted-accounting-principles/) sets the bar at 80–125% effectiveness.

If a company hedges a $100M loan portfolio and market rates rise, the loan drops $10M but the hedge only gains $7M (70% effective), the accounting treatment changes: $7M of the $10M loss is offset in net income (as normal), but $3M of the loss is left unhedged. Some companies choose not to qualify for hedge accounting if the hedge is not perfect, accepting the volatility in exchange for simplicity.

## Why companies sometimes accept fair-value volatility

Not every asset needs a fair value hedge. A bank holding a $10M position in [Treasury bonds](/treasury-bond/) for a short period might accept the mark-to-market loss (it will be temporary) rather than paying the cost of a hedge. A manufacturer might hold raw-material inventory for only a few weeks; hedging might be overkill. Fair value hedges are most valuable when:
- The company holds a large position for a long time.
- The underlying value is volatile (interest rates, commodity prices).
- The company's reporting system or regulatory environment penalises earnings volatility.

Central banks and large financial institutions use fair value hedges constantly; small businesses use them sparingly.

## See also

<div class="wiki-seealso">

### Closely related

- [Cash Flow Hedge](/cash-flow-hedge/) — hedging uncertain future cash flows, distinct from fair value hedges on existing items
- [Net Investment Hedge](/net-investment-hedge/) — hedging the equity value of a foreign subsidiary
- [Macro Hedging](/macro-hedging/) — portfolio-level protection against broad macro shocks versus transaction-specific hedges
- [Interest-Rate Swap](/interest-rate/) — the primary fair-value-hedging tool for banks and borrowers
- [Forward Contract](/forward-contract/) — customised derivative used in fair value hedges
- [Futures Contract](/futures-contract/) — standardised, exchange-traded version of forwards; common in commodity and equity hedges
- [Fair Value](/fair-value/) — the market price used to revalue hedged items each period
- [Option](/call-option/) — another hedging instrument; can be used in fair value hedges to set a price floor or ceiling

### Wider context

- [Generally Accepted Accounting Principles (GAAP)](/generally-accepted-accounting-principles/) — US standard defining fair value hedge accounting rules
- [International Financial Reporting Standards (IFRS)](/international-financial-reporting-standards/) — global standard with similar framework
- [Derivative](/forward-contract/) — general category of financial instruments used in hedges
- [Counterparty Risk](/counterparty-risk/) — risk that the bank or counterparty providing the hedge defaults
- [Risk Management](/operational-risk/) — broader discipline; fair value hedging is one tactic

</div>
