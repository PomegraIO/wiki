---
title: "Interest Rate Swaps for Retirees and Pension Funds"
description: "How pension funds and retirees use interest rate swaps to hedge long-dated liabilities and lock in predictable cash flows through receive-fixed agreements."
keywords:
  - interest rate swaps pension funds
  - liability-driven investing
  - receive-fixed swap
  - pension fund hedging
  - long-duration liability matching
  - duration matching
  - pension cash flow risk
image: "/svg/derivatives.svg"
---

*Pension funds and retirees use **interest rate swaps** to convert variable-rate assets into fixed cash flows, matching the long-dated, predictable obligations they owe to beneficiaries. A retiree or pension plan typically receives a fixed rate and pays a floating rate, locking in spending power for decades.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Interest Rate Swaps for Pension Funds — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives and hedging." />

<div class="wiki-infobox-caption">Pension funds swap floating returns for fixed cash flows to predictably fund retirement obligations.</div>

|   |   |
|---|---|
| **Core mechanic** | Pension receives fixed rate; pays floating (typically SOFR or bond yield) |
| **Primary goal** | Hedge [duration](/duration/) mismatch between assets and long-term liabilities |
| **Typical counterparty** | Bank or large swap dealer |
| **Typical tenor** | 10–30 years (matching benefit-payout schedules) |
| **Key risk** | Counterparty [credit risk](/credit-risk/); basis risk if swap and liabilities drift apart |
| **Cost** | Bid-ask spread; often embedded in swap pricing |

</aside>

## Why Pension Funds Use Receive-Fixed Swaps

A pension plan faces a simple structural mismatch: it promises to pay retirees a stream of benefit checks for decades, often guaranteed at a fixed amount. Its assets—stocks, bonds, real estate—generate returns that fluctuate with markets and interest rates. The goal of **liability-driven investing** is to make those asset returns predictable enough to cover known liabilities without shortfalls.

Interest rate swaps are a linchpin of this strategy. Instead of hoping bond yields stay high enough to fund future payouts, a pension can enter a swap and *lock in* a fixed return. If the plan receives 4% fixed on the swap and the market moves, the pension still earns that 4%—decoupling the liability hedge from market timing.

This is especially important for underfunded pension plans. A small utility or manufacturing company with $500 million in liabilities but only $400 million in assets has minimal margin for error. A steep decline in interest rates, which increases the present value of those liabilities on the balance sheet, can force the sponsor to contribute cash immediately. A receive-fixed swap reduces that tail risk.

## Matching Duration and Cash Flow Timing

Duration matters because a pension's liabilities have a specific, long timeline. A plan paying out $100 million in year 2035 needs certainty about its year-2035 purchasing power. If all its assets are stocks (short duration, unpredictable), a sudden equity crash a year before that payout is painful.

By swapping into a fixed-rate hedge, the pension effectively buys a synthetic bond. The swap's fixed leg gives the plan a known cash inflow on a known schedule. That cash can be set aside, earning its guaranteed rate, until the benefit check is written.

The matching works like this:

- Pension holds $100 million of floating-rate bonds yielding SOFR + 1%.
- Pension enters a 10-year swap: receives 4% fixed on $100 million notional; pays SOFR on the same.
- Net result: the pension's asset now pays a fixed 5% (4% from swap + 1% from bond spread), which is locked in regardless of where SOFR moves.

For pension funds managing dozens of liability tranches across decades, the portfolio often includes hundreds of small swaps, each calibrated to a specific year's expected outflows.

## Receive-Fixed vs. Pay-Fixed: Why Retirees Don't Pay Fixed

In a swap market, there are always two sides. A pension receives fixed by paying floating; someone else (usually a bank or hedge fund betting rates will fall) pays fixed and receives floating. It is critical not to confuse the pension's leg with the swap's overall structure.

Retirees and pension funds almost universally *receive* fixed because they are naturally long-duration liability holders. They want to reduce interest-rate risk, not increase it. A retiree who owns a floating-rate REIT or emerging-market bond already has interest-rate sensitivity baked in; swapping to fixed de-risks that exposure.

Pay-fixed swaps are typically used by corporations refinancing fixed-rate debt cheaply, or by banks and traders betting on rate cuts. Neither is the pension fund's use case.

## Counterparty Risk and Collateral

When a pension enters a swap with a major bank, it faces [credit risk](/credit-risk/) from the bank. If rates move sharply—say, rates spike 200 basis points—the pension's swap becomes valuable (the fixed rate it receives is now well above market). Suddenly the bank owes the pension money. If the bank fails before paying, the pension loses.

To mitigate this, swap counterparties (especially large pension funds) post collateral. Typically, the party in the money posts cash or treasury bonds daily or weekly, reducing the bank's exposure. During the 2008 financial crisis, pension funds learned this lesson harshly; many had to post collateral they didn't have on hand when rate moves went against them.

Large pension funds now:

- Use multiple swap dealers to avoid single-counterparty concentration
- Negotiate central clearing (moving swaps onto clearinghouses like the CME) to reduce bilateral default risk
- Maintain liquidity buffers specifically for collateral calls

## Basis Risk: When the Swap Doesn't Perfectly Hedge

A swap's fixed rate is usually pegged to Treasury yields or SOFR; a pension's liabilities may be tied to inflation or mortality tables. If inflation picks up, retirees' purchasing power needs rise, but the swap's fixed leg stays fixed. This is **basis risk**—the mismatch between the hedge instrument and the thing being hedged.

A pension managing this risk might:

- Use multiple swap structures (inflation swaps on top of nominal swaps) to layer hedges
- Dynamically rebalance as demographics shift
- Accept small basis-risk trade-offs in exchange for operational simplicity

Basis risk is rarely zero, but professional pension asset managers spend considerable effort minimizing it.

## Cost and Pricing

Pension funds don't swap for free. The bid-ask spread on a 20-year swap can be 5–15 basis points; on a heavily traded 10-year, maybe 2–5 basis points. Dealers also bake in a small profit margin for bearing the counterparty risk.

A pension managing $10 billion in liabilities and running a continuous hedge might pay $500,000 to $2 million per year in aggregate swap costs. That's a real expense, but far cheaper than being forced to contribute large sums to cover an underfunding event triggered by a rate shock.

## When and How Pension Funds Exit Swaps

Swaps are not permanent. A pension might:

- Let the swap mature naturally as liabilities are paid down
- Unwind the swap early if the pension becomes overfunded (de-risking no longer necessary)
- Roll the swap into new tenors if the liability schedule shifts

Unwinding early is costly if market conditions have moved against the pension (i.e., rates have fallen and the pension's receive-fixed position is now valuable). The pension must pay the dealer to exit, or find a buyer to take on the other side.

Sophisticated pension funds treat swaps as living contracts, reviewed quarterly and adjusted alongside liability forecasts, mortality assumptions, and funding ratios.

## See also

<div class="wiki-seealso">

### Closely related

- [Interest-rate-swap](/interest-rate-swap/) — mechanics of vanilla swaps and how fixed and floating legs are priced
- [Duration](/duration/) — why pension assets and liabilities must be duration-matched
- [Credit-risk](/credit-risk/) — counterparty default risk and collateral management in derivatives
- [Derivative-hedging](/derivatives-hedging/) — broader hedging strategies beyond swaps
- [Liability-driven-investing](/liability-driven-investing/) — the full pension fund investment framework

### Wider context

- Pension-obligations — how pension liabilities are measured and funded
- [Floating-rate-bond](/floating-rate-bond/) — assets often hedged via swap into fixed returns
- [Treasury-bond](/treasury-bond/) — reference rate for many fixed-leg pricing
- [SOFR](/sofr/) — modern floating-rate benchmark for swap pricing

</div>
