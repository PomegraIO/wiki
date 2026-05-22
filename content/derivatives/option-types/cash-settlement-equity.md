---
title: "Cash Settlement (Equity)"
description: "Equity options settlement where the buyer and seller exchange cash equal to intrinsic value rather than physically delivering shares."
keywords:
  - cash settlement
  - equity options
  - options settlement
  - cash-settled option
---

*A **cash-settled equity option** is an [option contract](/wiki/option/) where the seller settles with the buyer by paying cash equal to the option's intrinsic value at [expiration](/wiki/option-expiration/), rather than delivering (or receiving) the underlying shares. This is the standard settlement method for index [options](/wiki/option/) and many individual equity options.*

<aside class="wiki-infobox">

| Aspect | Details |
|---|---|
| **Settlement Type** | Cash payment, not stock transfer |
| **Payoff at Expiration** | Max(0, S − K) for calls; Max(0, K − S) for puts |
| **Delivery** | None; only cash changes hands |
| **Margin** | No risk of forced stock borrowing/delivery |
| **Liquidity** | Higher (no logistics, no short-sale constraints) |

</aside>

## Cash settlement vs. physical delivery

**Physical settlement (stock delivery):** Buyer pays the strike price and receives shares; seller delivers shares. This is how equity options once worked and how [futures contracts](/wiki/futures-contract/) still work. Logistics are complex: the seller must have (or borrow) the shares; the buyer must accept delivery and settle the cost.

**Cash settlement:** At expiration, the seller pays the buyer the intrinsic value in cash. If a $100 call on Apple expires when Apple is at $110, the cash-settled call pays $10 per share (the intrinsic value). No shares change hands.

Example: You buy 1 call option contract (= 100 shares of underlying) for $3 strike price $100 on Apple. At expiration, Apple is $110. With cash settlement, you receive $10 × 100 = $1,000 cash (the intrinsic value). You paid $300 for the contract (call premium × 100), so your profit is $1,000 − $300 = $700. No shares are involved.

## Why exchanges prefer cash settlement

**Eliminates physical logistics.** No one needs to locate shares, borrow them, arrange delivery, or deal with failed settlements.

**Avoids short-sale complications.** If an option writer (seller) is short the underlying stock, they can close the short by cash settlement instead of navigating [short-sale rules](/wiki/short-sale-rules/) and borrowing constraints.

**Cleaner for index options.** An [index option](/wiki/stock-market/) (like the [VIX](/wiki/fear-index/) or [S&P 500](/wiki/sp-500-index/) index) cannot be physically delivered—you cannot hold "the S&P 500." Cash settlement is the only option.

**Reduces counterparty risk.** The clearinghouse (e.g., [CBOE](/wiki/cboe-options-exchange/), [OCC](/wiki/options-clearing-corporation/)) can calculate the cash payoff at expiration and instantly credit/debit both sides. No settlement failures.

## How cash settlement works mechanically

**At expiration (3rd Friday of the month for standard US equity options):**

1. The exchange calculates the intrinsic value: Max(0, Stock Price − Strike) for calls; Max(0, Strike − Stock Price) for puts.

2. The clearinghouse credits the account of call buyers (or put sellers) and debits the account of call sellers (or put buyers) by this intrinsic value per share, times the contract multiplier (100 for US equity options).

3. The transaction settles in cash, usually T+1 (next business day).

**Example:** You are short (sold) 5 SPY (S&P 500 ETF) call contracts at strike $450. At expiration, SPY closes at $455. The intrinsic value per share is $455 − $450 = $5. You owe $5 × 100 shares × 5 contracts = $2,500 cash to the call buyers. Your broker deducts this from your account; the buyers' accounts are credited.

## Advantages for traders

**No forced stock borrow.** If you sell a call, you do not have to own or borrow the shares (unlike physical settlement or [covered calls](/wiki/covered-call/)). You can be naked short the call and settle in cash.

**Flexibility for spreads.** Complex [option spreads](/wiki/spread-position/) (butterflies, iron condors) are easier to manage with cash settlement—no one worries about assignment or share delivery.

**Index options are only cash-settled.** Traders in [VIX options](/wiki/volatility-index-option/), [SPY options](/wiki/sp-500-index/), or Russell 2000 options rely on cash settlement because the underlying is an index, not a single stock.

## Disadvantages and edge cases

**No optionality in how to close.** With physical settlement, an options trader can sometimes negotiate the timing or price of share delivery. With cash settlement, the intrinsic value at expiration is deterministic—no room for negotiation.

**Assignment behavior differs.** Sellers of calls and puts cannot be assigned early (before expiration) under cash settlement, reducing the need for active management. However, some equity options still permit [early exercise](/wiki/early-exercise/) (American-style, physically settled), creating a small risk of surprise assignment.

**Taxes and wash-sales.** Cash settlement of an equity option does not trigger a physical transaction, but for tax purposes, it counts as a closing transaction. If you sell a call that expires worthless, the IRS treats this as a [short-term capital gain](/wiki/short-term-capital-gain-tax/) or loss (assuming you held the option less than a year).

## Cash-settled vs. physically-settled: practical comparison

Most **US equity options** (e.g., Apple, Tesla, IBM) are physically settled (if holders exercise or at expiration, they receive shares). But many **index options** and **equity-linked derivatives** (e.g., swaps) are cash-settled.

**European options** (vs. American) are always cash-settled on many exchanges, reflecting the convention that European options cannot be exercised early.

**Cryptocurrency derivatives** (e.g., Bitcoin options on CME) are predominantly cash-settled because holding physical cryptocurrency delivery is logistically complex.

## Settlement and margin implications

**Margin for short calls.** If you sell a naked call, you must maintain margin (collateral) equal to the potential loss. With cash settlement, your loss is capped at the intrinsic value (never more), so margin requirements are more predictable. With physical settlement, short sellers face additional risk of forced short-covering if shares are unavailable.

**Buying power usage.** Your broker uses less buying power for cash-settled positions because the risk is finite and calculable.

## See also

<div class="wiki-seealso">

### Closely related
- [Option](/wiki/option/) — the underlying contract
- [Call option](/wiki/call-option-equity/) — the buyer's right to buy at the strike
- [Put option](/wiki/put-option-equity/) — the buyer's right to sell at the strike
- [Option exercise and settlement](/wiki/option-exercise-settlement/)

### Wider context
- [Options clearing](/wiki/options-clearing-corporation/)
- [Options Greeks](/wiki/options-greeks/)
- [Covered call](/wiki/covered-call/)
- [Intrinsic value](/wiki/intrinsic-value/)

</div>
