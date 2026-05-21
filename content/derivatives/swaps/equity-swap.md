---
title: "Equity Swap"
description: "A swap where one party receives stock returns and the other pays them, allowing parties to gain equity exposure or finance purchases without owning stock."
---

*An equity swap is a contract where one party pays the return on a stock or stock index and the other pays a fixed or floating interest rate. The equity-return payer gains stock price upside (and downside), while the interest-rate payer gets leveraged equity exposure without buying shares. No shares change hands; the contract settles in cash.*

## Why equity swaps exist

An investor who wants equity exposure faces choices: buy the stock, buy call options, use margin, or use an equity swap. Each has costs and trade-offs.

**Buying stock directly**: You own it, pay the full notional upfront, and get [dividends](/wiki/dividend/). But you use lots of capital, you pay tax on dividends, and you bear full price risk.

**Buying calls**: You get leverage (control lots of stock with small premium), but options decay over time and have limited lives.

**Margin**: You borrow to buy stock, getting leverage, but you face [margin calls](/wiki/initial-margin/), and the lender can demand repayment.

**Equity swap**: You pay a known financing cost (like SOFR + 50 bps) and receive all of the stock's price appreciation and dividend. You control the notional with minimal upfront capital, no margin calls, and you defer dividends (the swap payer sends the dividend to you, but you don't receive it as cash, so you avoid the tax event). For a long-term holder, this is often cheaper than any alternative.

## Structure

An equity swap has two legs:

**Equity leg**: One party receives the total return on an equity asset (price appreciation plus [dividends](/wiki/dividend/)). They receive this as a floating quantity that resets periodically, e.g., quarterly.

**Financing leg**: The other party receives a fixed or floating interest rate payment, typically SOFR + spread. This is the cost the equity payer bears to deliver the equity return.

The two parties exchange net cash flows at each reset. If the stock appreciates, the equity payer sends cash to the equity receiver. If the stock declines, the equity receiver sends cash to the equity payer. Dividends are included in the equity return and are paid to the receiver of the equity leg (so the receiver captures the dividend, even if they don't own the stock).

## Example

A hedge fund wants $50 million of Apple stock exposure but doesn't want to put up $50 million in capital. It enters a 5-year equity swap with an investment bank:

- **Apple notional**: $50 million.
- **Equity leg**: The hedge fund receives the total return on Apple (price appreciation + dividends).
- **Financing leg**: The hedge fund pays SOFR + 60 bps annually.

Each quarter, the swap resets. If Apple stock rose 5% in the quarter, the bank sends the hedge fund $2.5 million (5% of $50 million). If Apple fell 3%, the hedge fund sends the bank $1.5 million (3% of $50 million). The hedge fund also pays the quarterly financing cost (SOFR + 60 bps) to the bank.

The hedge fund gains full Apple exposure with minimal capital outlay, no margin calls, and can hold the position for the full 5-year life without rolling contracts or buying shares.

## Common variations

**Index equity swaps**: The equity leg is tied to a broad index like the [S&P 500](/wiki/sp-500-index/) rather than a single stock. This lowers volatility and is liquid.

**Leveraged equity swaps**: The equity return is multiplied by a factor. For example, you might receive 2x the S&P 500 return. This amplifies both gains and losses.

**Dividend-protected swaps**: In some deals, dividends are excluded or reduced, lowering the equity receiver's return but also lowering the financing cost.

**Currency-quanto swaps**: You receive the return on a foreign equity index but are hedged to a specific exchange rate, removing currency risk.

## Valuation and pricing

An equity swap is valued as the present value of its two legs:

**Equity leg present value**:
1. Project the expected returns on the equity (stock price plus dividends).
2. Discount back to present using the risk-free rate (typically SOFR) plus an equity risk premium.
3. For a single stock, this is complex because future prices are unknown. For an index, dealers use valuation models or mark-to-market against observable index futures.

**Financing leg present value**:
1. Project SOFR forward using the SOFR curve.
2. Discount using SOFR discount factors.

The swap is priced so the two legs have equal value at inception. The "swap rate" is the SOFR + spread that makes this true.

The spread embedded in the financing cost depends on:
- The cost to the dealer to hedge the equity exposure (often by buying the stock or index futures).
- The [cost of carry](/wiki/cost-of-carry/) (financing cost to hold the stock, minus dividend yield).
- The dealer's credit spread (the compensation for [counterparty risk](/wiki/counterparty-risk/)).

## Uses

**Leverage without margin**: Hedge funds and prop traders use equity swaps to get leveraged equity exposure without margin accounts and their associated daily mark-to-market and margin calls.

**Tax efficiency**: An investor that holds a losing stock might enter an equity swap to lock in gains if the stock recovers, deferring the tax event.

**Financing for acquisitions**: A company acquiring another might use equity swaps on its own stock to finance the deal, swapping its future stock returns for upfront cash.

**Short selling alternative**: Instead of borrowing stock to short, a trader can go short an equity swap (paying the equity return and receiving financing). This avoids borrow constraints and short-sale restrictions.

**Liability hedging**: A portfolio manager that has short exposure (e.g., a short position financed with borrowed cash) can hedge by going long an equity swap.

## Risks

**Volatility risk**: The equity value can swing sharply. An adverse market move can wipe out the equity receiver's position.

**Counterparty risk**: The other party might default. If the equity receiver defaults while the stock is up, the equity payer loses the position.

**Leverage risk**: Because swaps can be leveraged with minimal capital, a small market move can cause large percentage losses. Hedge funds have failed due to leveraged equity swap positions.

**Dividend uncertainty**: Projected dividends can be cut (especially during crises), and the equity receiver bears this risk.

**Financing cost risk**: If SOFR rises sharply, the financing leg becomes more expensive. The equity receiver's returns may be eaten away by rising financing costs.

**Operational risk**: Equity swaps are complex and involve multiple reset dates, dividend adjustments, and cash settlement mechanics. Errors are possible.

<div class="wiki-seealso">
<h2>See also</h2>
<h3>Closely related</h3>
<ul>
<li><a href="/wiki/swap/">Swap</a> — the foundational derivative structure.</li>
<li><a href="/wiki/total-return-swap/">Total-return swap</a> — similar structure, often used interchangeably with equity swaps.</li>
<li><a href="/wiki/option/">Option</a> — another way to gain leveraged equity exposure.</li>
<li><a href="/wiki/call-option/">Call option</a> — a bullish alternative to equity swaps.</li>
</ul>
<h3>Wider context</h3>
<ul>
<li><a href="/wiki/leverage/">Leverage</a> — the main advantage of equity swaps.</li>
<li><a href="/wiki/counterparty-risk/">Counterparty risk</a> — the primary risk in equity swaps.</li>
<li><a href="/wiki/cost-of-carry/">Cost of carry</a> — determines the financing cost in the swap.</li>
<li><a href="/wiki/dividend/">Dividend</a> — included in the equity return the swap payer delivers.</li>
</ul>
</div>
