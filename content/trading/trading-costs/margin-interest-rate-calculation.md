---
title: "Margin Interest Rate Calculation"
description: "How brokers calculate daily margin interest on trades: annualized rates, daily factors, and compound accumulation over holding periods."
keywords:
  - margin interest rate calculation
  - daily margin interest charge
  - margin interest formula
  - how is margin interest calculated
  - interest on margin trades
image: /svg/trading.svg
---

*Brokers charge **margin interest** on borrowed funds used to buy securities. The interest is calculated daily based on your outstanding debit balance, compounded daily or monthly depending on the broker, and accrues continuously until you repay the loan. Understanding how this arithmetic works is essential for anyone using leverage, because margin interest can quickly erode returns on small price movements.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Margin Interest — Daily Calculation Snapshot</div>

<img src="/svg/trading.svg" alt="An abstract editorial mark for trading and costs." />

<div class="wiki-infobox-caption">Interest accrues daily on your debit balance at an annualized rate set by your broker.</div>

|   |   |
|---|---|
| **Basic formula** | Daily Interest = Debit Balance × (Annual Rate / 365) |
| **Typical annual rate** | 4.5–12% depending on balance size and broker |
| **Compounding** | Daily accrual, posted to your account monthly or daily |
| **Debit balance** | Cash borrowed from the broker; starts at zero when you use margin |
| **When it stops accruing** | When you repay the loan or offset the margin debit |

</aside>

## The Daily Accrual Mechanic

Margin interest is calculated daily, not as a one-time charge at settlement. This matters because your debit balance—the amount you owe the broker—changes as positions open, close, and markets move.

Here is how it works:

1. You place $50,000 cash in your account and buy $100,000 of stock, borrowing $50,000 from the broker.
2. Your debit balance is $50,000.
3. The broker charges interest on that $50,000 each day you hold the position.
4. If the stock rises 10%, your position is worth $110,000. Your debit balance is *still* $50,000 (you still owe that original amount).
5. If the stock falls 10%, your position is worth $90,000. Your debit balance is *still* $50,000 (you still owe it).

The debit balance does not change with price movements. It only changes when you repay principal or when the balance of your account shifts due to deposits, withdrawals, or trades.

## The Interest Rate Itself

Brokers set their margin rates based on several factors:

- **Federal Funds Rate**: The base rate for interbank lending, set by the Federal Reserve. Margin rates typically float above this benchmark.
- **Your account size**: Larger accounts ($1M+) often get lower rates. Small accounts may pay a premium.
- **Market conditions**: During crisis or tight credit conditions, brokers raise rates.
- **Your brokerage**: Competition varies. Some brokers undercut others on margin rates to attract traders.

Rates typically range from 4.5% to 12% annually, depending on these factors. A $100,000 debit balance at 7% costs about $70 per month ($7,000 per year).

## The Daily Calculation Example

Let's use a concrete example:

You have a debit balance of $50,000 and your broker's margin rate is 8% per annum.

**Daily interest** = $50,000 × (0.08 / 365)
**Daily interest** = $50,000 × 0.000219
**Daily interest** = $10.96

This $10.96 accrues every single day the debit balance remains at $50,000. Over a 30-day month, that is $328.80 in interest. Over a year, $4,000.

If you add another $25,000 to the debit balance on day 16 of the month, your daily interest doubles:

**New daily interest** = $75,000 × 0.000219
**New daily interest** = $16.44

Over the remaining 15 days of the month, you pay an additional $246.60. Your total month's interest is about $575.40.

## Compounding and Monthly Accrual

Most brokers accrue interest daily but post it to your account monthly. Some post daily. Either way, the effect is the same: interest compounds on top of the debit balance.

If you do not pay down the margin loan, the accrued interest typically gets added to your debit balance (or charged against your cash balance). If added to the debit balance, you begin accruing interest on the interest itself—compounding.

Over a year, compound interest on margin can be significant:

- Month 1: $50,000 balance, $329 interest accrued.
- Month 2: $50,329 balance (interest added), $349 interest accrued.
- Month 3: $50,678 balance, and so on.

By year-end, the total interest owed is higher than the simple yearly rate would suggest, due to compounding.

## Tiered Rates and Broker Discounts

Many brokers offer tiered rates: larger balances get better rates. For example:

| Debit Balance | Annual Rate |
|---|---|
| $0–$25,000 | 9.5% |
| $25,001–$100,000 | 8.5% |
| $100,001–$250,000 | 7.5% |
| $250,001+ | 6.5% |

As you pay down your margin balance, you may move into a lower tier and enjoy a lower rate going forward. Conversely, if you borrow more, you may jump to a higher tier. (This is the opposite of intuition—most would expect larger borrowers to pay more risk premium—but brokers incentivize bigger traders and investors by giving them better rates.)

## Margin Interest vs. Cost Basis

An important note: margin interest is *not* added to the cost basis of your securities for tax purposes. Unlike [loan-origination-fees](/loan-origination-fees/) on some mortgages, which can be capitalized and amortized, margin interest is simply an annual expense.

If you trade in a taxable account, margin interest is deductible as an investment expense (subject to the 2% AGI floor under old rules, or potentially not deductible at all under current law, depending on your status). In a retirement-account like a [traditional-ira](/traditional-ira/) or [401k-plan](/401k-plan/), margin is usually not allowed at all, so this is not a concern.

## The Cost of Leverage Over Time

Margin interest compounds the math of leverage in a way that traders often underestimate. Consider:

You invest $50,000 of your own capital and borrow $50,000 on margin (2:1 leverage) to buy $100,000 of stock. You pay 8% annual interest on the borrowed $50,000.

For your strategy to break even, the stock must earn at least 4% per year (8% interest on the borrowed half). Any return above 4% goes to your profit; any return below 4% is a loss.

- If the stock rises 6%, you earn 12% on your $50,000 equity (6% gain on the full $100,000 position, minus 4% interest cost). 
- If the stock rises 2%, you break even (2% gain minus 4% interest).
- If the stock falls 2%, you lose 6% on your equity (2% loss plus 4% interest cost).

Leverage amplifies both gains and losses, and margin interest is a friction cost that must be overcome.

## Debit Balance Movements and Partial Paydown

Your debit balance shrinks as you repay or when your account gains value. Important distinction:

- **You sell a position at a gain**: The proceeds reduce your debit balance.
- **You sell a position at a loss**: The proceeds reduce your debit balance by the full amount, even though you lost money. (Your net account value fell, but you reduced the borrowed amount.)
- **You deposit cash**: The deposit reduces your debit balance.
- **A dividend or interest is paid on a long position**: This typically credits your cash balance, reducing your debit balance.

Each day the debit balance is lower, you pay less interest. Paydown strategies—focusing on reducing margin debt first, before investing new capital—can save significant interest over time.

## See also

<div class="wiki-seealso">

### Closely related

- Margin Call — When your equity falls and the broker forces you to deposit or close positions
- [Leverage Ratio](/leverage-ratio-forex/) — How leverage magnifies returns (and losses)
- [Broker](/broker/) — Overview of brokers and the services they provide, including margin lending
- [Cost of Debt](/cost-of-debt/) — General principles of borrowing costs
- [Bid-Ask Spread](/bid-ask-spread/) — Another hidden cost of trading

### Wider context

- [Derivatives Hedging](/derivatives-hedging/) — Using options and futures as alternatives to margin leverage
- Trading Costs — Commissions, fees, slippage, and interest
- [Short Selling](/short-selling/) — Margin interest also applies to short positions

</div>
