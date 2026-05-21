---
title: "Accreting Swap"
description: "A swap with a notional principal that increases over time, matching the growing size of an expanding debt or investment."
---

*An accreting swap is a contract in which the notional principal amount increases over time according to a preset schedule. It is the opposite of an [amortizing swap](/wiki/amortizing-swap/). The swap is useful for hedging or financing obligations that grow, such as construction projects, staged acquisitions, or expanding business lines.*

<div class="wiki-hatnote">Accreting swaps are less common than amortizing swaps because most debt schedules decline (through repayment), not grow. But for growing liabilities, they are essential.</div>

## Why accreting swaps exist

Most corporate debt is static or declining in principal. But some obligations grow:

**Staged acquisitions**: A private equity firm plans to acquire a company in stages over three years, with increasing payments. The total debt will grow from year to year.

**Construction projects**: A contractor finances a multi-year project, with debt increasing as the project expands (land, labor, equipment costs mount).

**Emerging market sovereigns**: A country issuing dollar debt to fund growing infrastructure might increase the notional over time as tax revenue grows and it can afford larger payments.

**Merchant banking**: A bank making staged investments in a project increases its exposure over time, needing to hedge growing interest-rate risk.

In each case, the exposure (and the hedging need) grows over time. A vanilla swap with flat notional would leave the company under-hedged as its debt grows. An accreting swap solves this by growing the hedging notional in lockstep with the debt.

## Structure

An accreting swap is identical to a vanilla [interest-rate swap](/wiki/interest-rate-swap/) except the notional increases:

**Fixed leg**: Party A pays a fixed rate on the accreting notional.

**Floating leg**: Party B pays SOFR (or another reference) on the accreting notional.

The notional on each payment date is pre-specified:
- Year 1: $100 million.
- Year 2: $120 million.
- Year 3: $150 million.

Both legs are discounted using zero-coupon curves. The fixed rate is set so the present value of both legs is equal at inception.

## Example

A private equity firm is acquiring a company in three tranches:
- **Tranche 1** (today): Pay $100 million, financed with a $100 million term loan at SOFR + 2.5%.
- **Tranche 2** (year 1): Pay $50 million, financed with an additional $50 million term loan at SOFR + 2.5%.
- **Tranche 3** (year 2): Pay $75 million, financed with an additional $75 million term loan at SOFR + 2.5%.

The firm wants to hedge the interest-rate risk. It enters a 3-year accreting swap:
- **Year 1**: Notional = $100 million. Fixed 3.75% on $100M, floating SOFR on $100M.
- **Year 2**: Notional = $150 million. Fixed 3.75% on $150M, floating SOFR on $150M.
- **Year 3**: Notional = $225 million. Fixed 3.75% on $225M, floating SOFR on $225M.

If SOFR is 2.5%, the firm pays 3.75% fixed and receives 2.5% floating, netting a payment of 1.25% on each year's notional. This locks in the all-in borrowing cost at approximately SOFR + 1.25% (the fixed swap rate less SOFR), or about 3.75%, close to the 2.5% spread.

## Variations

**Step-up accreting swaps**: The notional increases in steps at specified dates. Most common type.

**Linear accreting swaps**: The notional increases smoothly over time (e.g., 5% per month). Less common because less natural for most use cases.

**Customized schedules**: The notional can follow any pre-agreed schedule (tied to construction milestones, transaction closings, etc.).

## Valuation and pricing

An accreting swap is valued like an amortizing swap, but in reverse:

1. **Project each payment**: Calculate the cash flow on each payment date using the appropriate notional for that date.

2. **Discount each cash flow**: Use zero-coupon discount factors for the respective dates.

3. **Solve for the fixed rate**: Find the fixed rate that equates the two legs in present value.

The fixed rate on an accreting swap is typically **lower** than on an equivalent vanilla swap (and lower than on an amortizing swap), because:
- The bulk of the notional (and thus the bulk of [interest-rate risk](/wiki/interest-rate-risk/)) is in later periods, when [discount rates](/wiki/zero-coupon-bond/) are lower.
- The fixed-rate payer bears more long-term risk, so the market compensates by offering a lower rate.

## Risks

**Execution risk**: If the stagings don't happen as planned (e.g., Tranche 2 is delayed or cancelled), the hedge is misaligned. The firm has a notional mismatch.

**Basis risk**: The notional schedule is fixed, but actual borrowing might differ. If the firm borrows less than planned, it is over-hedged.

**Liquidity risk**: Accreting swaps are bespoke and hard to exit. If the firm needs to unwind the swap before maturity, dealers may quote wide spreads or decline to trade.

**Counterparty risk**: Long-dated and bespoke swaps carry meaningful [counterparty risk](/wiki/counterparty-risk/). The firm is exposed to the dealer's creditworthiness over years.

**Convexity and rate volatility**: If rates move sharply, the swap's value can swing unpredictably, especially if rates move in the direction opposite to the firm's anticipation (e.g., rates fall, making fixed payments look expensive in hindsight).

## When accreting swaps are used

**Leveraged buyouts (LBOs)**: PE firms financing acquisitions with staged tranches commonly use accreting swaps.

**Project finance**: Developers financing multi-phase projects (e.g., real estate, infrastructure) use them.

**Securitizations**: Issuers of structured finance with staged funding often hedge with accreting swaps.

**Growth-mode companies**: Startups or firms in rapid growth might issue accreting debt and use swaps to hedge.

Less common than amortizing swaps because most debt is static or declining, but essential for the use cases where notional grows.

<div class="wiki-seealso">
<h2>See also</h2>
<h3>Closely related</h3>
<ul>
<li><a href="/wiki/swap/">Swap</a> — the foundational swap structure.</li>
<li><a href="/wiki/amortizing-swap/">Amortizing swap</a> — the opposite: notional declines over time.</li>
<li><a href="/wiki/interest-rate-swap/">Interest-rate swap</a> — the vanilla swap on which accreting swaps are based.</li>
<li><a href="/wiki/zero-coupon-swap/">Zero-coupon swap</a> — another swap variant for specialized use cases.</li>
</ul>
<h3>Wider context</h3>
<ul>
<li><a href="/wiki/duration/">Duration</a> — the interest-rate sensitivity grows as the notional grows.</li>
<li><a href="/wiki/interest-rate-risk/">Interest-rate risk</a> — what accreting swaps manage.</li>
<li><a href="/wiki/counterparty-risk/">Counterparty risk</a> — the primary risk in long-dated OTC swaps.</li>
<li><a href="/wiki/leveraged-buyout/">Leveraged buyout</a> — a common context for accreting swap use.</li>
</ul>
</div>
