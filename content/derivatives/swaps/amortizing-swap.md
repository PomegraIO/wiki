---
title: "Amortizing Swap"
description: "A swap with a notional principal that decreases over time, matching the repayment schedule of a declining debt."
---

*An amortizing swap is a swap in which the notional principal amount declines over time according to a preset schedule. Unlike a vanilla swap, where the principal stays flat, an amortizing swap mirrors the declining balance of a loan or bond that is being paid down.*

## What makes amortizing swaps different

In a standard [swap](/wiki/swap/), both parties exchange cash flows based on a fixed notional amount—say, $100 million—for the entire life of the deal. With an amortizing swap, the notional shrinks month by month or year by year. If you're hedging a mortgage or an auto loan, this architecture matches reality: as the borrower pays down principal, the outstanding exposure gets smaller.

For example, a company with a $100 million amortizing debt might use an amortizing [interest-rate swap](/wiki/interest-rate-swap/) to convert floating-rate payments to fixed. In month one, they swap interest on $100 million; by month six, they swap only $90 million; by maturity, they're swapping nearly zero.

This seemingly small difference—amortizing the notional—has large consequences for valuation, [counterparty risk](/wiki/counterparty-risk/), and hedging efficiency.

## Why amortizing swaps matter

Most corporate debt is amortizing. Mortgages have a declining principal schedule. Government bonds are redeemed at par. If a company or bank uses a flat-notional vanilla swap to hedge an amortizing liability, there is a duration mismatch: the swap's average [duration](/wiki/duration/) doesn't align with the loan's average duration, creating slippage in the hedge. An amortizing swap eliminates that misalignment.

Consider a bank funding a $500 million mortgage portfolio. Each month, borrowers pay down principal. If the bank uses a vanilla swap with a flat $500 million notional, it is over-hedged early and under-hedged late. An amortizing swap contracts along with the loan portfolio, keeping the hedge tight.

## Structure and mechanics

An amortizing swap works like a vanilla [interest-rate swap](/wiki/interest-rate-swap/) except the notional decreases. The amortization schedule is set at inception—say, 10% annual reduction, or a schedule that mirrors a specific loan's repayment curve.

Two legs:
- **Fixed leg**: pays a fixed rate on the declining notional.
- **Floating leg**: pays a floating rate (SOFR, LIBOR, or another reference) on the declining notional.

As the notional drops, so do the dollar amounts of each payment. Both legs shrink in tandem. The [counterparty](/wiki/counterparty-risk/) that is long fixed and short floating gets smaller exposure to [interest-rate risk](/wiki/interest-rate-risk/) over time, which is exactly what a bank funding amortizing debt needs.

## Pricing and valuation

Amortizing swaps are harder to value than vanilla swaps because each payment is pegged to a different notional. A [dealer](/wiki/broker/) pricing an amortizing swap must:

1. Project the outstanding notional at each payment date.
2. Discount each future cash flow (fixed and floating) using appropriate [zero-coupon discount factors](/wiki/zero-coupon-bond/) for that date.
3. Solve for the fixed rate that makes the present value of both legs equal.

In practice, dealers use curves of swap rates and bootstrap the discount factors from observed [swap](/wiki/swap/) prices, then apply the amortization schedule to arrive at a mid-market rate.

The fixed rate on an amortizing swap is typically slightly higher than on an equivalent vanilla swap. Why? An amortizing swap exposes the fixed-rate payer to less reinvestment risk and less [interest-rate risk](/wiki/interest-rate-risk/) later in the trade, but dealers build in a small premium to offset the complexity of administration and valuation.

## Common uses

**Mortgage lenders** use amortizing swaps to hedge floating-rate mortgage portfolios. As mortgages are prepaid or paid down, the swap notional shrinks, keeping the hedge ratio stable.

**Corporate borrowers** with amortizing term loans or bonds use them to convert floating-rate debt to synthetic fixed-rate debt without leaving a hedge surplus at the end.

**Banks and thrifts** routinely enter amortizing swaps to manage [interest-rate risk](/wiki/interest-rate-risk/) on their loan books, which naturally amortize.

**Project finance** deals often feature amortizing debt (principal is repaid from project cash flow), and sponsors use amortizing swaps to lock in a fixed all-in cost of debt.

## Risks and considerations

**Complexity**: Amortizing swaps are more complex to trade, price, and risk-manage than vanilla swaps. The [bid-ask spread](/wiki/etf-bid-ask-spread/) is wider because dealers must revalue the entire path of declining notionals when market rates move.

**Prepayment risk**: For mortgage-hedging, if borrowers prepay ahead of schedule, the amortizing swap may not match the loan balance any longer. Hedgers must monitor prepayment speeds and adjust.

**Valuation disagreement**: Because amortization schedules can be customized, two dealers might price the same trade differently if they disagree on the schedule's interpretation or the relevant discount curve.

**Administrative burden**: Each cash flow is tied to a specific notional, so settlement and reconciliation are more error-prone than with a vanilla swap.

<div class="wiki-seealso">
<h2>See also</h2>
<h3>Closely related</h3>
<ul>
<li><a href="/wiki/swap/">Swap</a> — the foundational agreement to exchange cash flows.</li>
<li><a href="/wiki/interest-rate-swap/">Interest-rate swap</a> — the most common swap type, often amortizing in practice.</li>
<li><a href="/wiki/zero-coupon-swap/">Zero-coupon swap</a> — a swap where one or both legs are deferred until maturity.</li>
<li><a href="/wiki/cross-currency-swap/">Cross-currency swap</a> — a swap between two currencies, often amortizing.</li>
</ul>
<h3>Wider context</h3>
<ul>
<li><a href="/wiki/duration/">Duration</a> — the measure of interest-rate sensitivity that amortizing swaps help align.</li>
<li><a href="/wiki/interest-rate-risk/">Interest-rate risk</a> — the primary risk managed by an amortizing swap.</li>
<li><a href="/wiki/counterparty-risk/">Counterparty risk</a> — reduced over time as the notional declines.</li>
</ul>
</div>
