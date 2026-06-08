---
title: "Swap vs Forward Rate Agreement: Key Differences"
description: "Compare a single-period FRA with a multi-period interest rate swap to understand when each instrument hedges floating-rate exposure."
keywords:
  - swap vs forward rate agreement difference
  - FRA vs swap comparison
  - forward rate agreement vs interest rate swap
  - hedging with swaps and FRAs
  - when to use FRA or swap
image: /svg/derivatives.svg
---

*Both **interest rate swaps** and **forward rate agreements (FRAs)** hedge exposure to rising or falling interest rates, but they operate on different time horizons. A single-period **FRA** locks in a rate for a 3-month or 6-month window; a **swap** extends that protection (or speculation) across multiple years, period by period.*

<div class="wiki-hatnote">

This entry compares the two instruments at a glance. For the detailed mechanics of swap payments, see [Fixed-for-floating swap payment mechanics](/fixed-for-floating-swap-mechanics/). For swap valuation, see [How an interest rate swap is valued after inception](/swap-valuation-mid-life/).

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">FRA vs Swap — Key Differences</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives." />

<div class="wiki-infobox-caption">FRAs cover one future rate period; swaps cover many, usually across years.</div>

|   |   |
|---|---|
| **Time horizon** | FRA: single, short-term period (typically 3 or 6 months). Swap: usually multi-year, multiple periods. |
| **Cash flow** | FRA: one net settlement, typically 2 days into the rate period. Swap: quarterly or semi-annual settlements over life of contract. |
| **Notional exchange** | FRA: notional usually not exchanged. Swap: notional not exchanged (typically). |
| **Pricing** | FRA: based on the forward rate for that specific period. Swap: rates derived from the full forward curve. |
| **Market use** | FRA: short-term hedges, gap filling. Swap: long-term hedges, liability repricing, speculation. |
| **Liquidity** | FRA: less liquid; each period-pair is its own instrument. Swap: more liquid; standardized, widely traded. |
| **Credit exposure** | FRA: minimal after settlement (one cash exchange). Swap: bilateral, varies with mark-to-market. |

</aside>

## What Is a Forward Rate Agreement?

A **forward rate agreement** is a contract between two parties to lock in an interest rate for a short future period, usually 3 months or 6 months ahead. The settlement is simple: one party pays the other a net cash amount equal to the difference between the locked-in rate and the actual floating rate that occurs, applied to the notional.

**Example FRA:** On January 15, you enter a "3x6" FRA (covering the three-month period starting three months from now). You agree that you will pay 4.00% fixed and receive 3-month LIBOR on a $10 million notional for that period.

Three months later (April 15), 3-month LIBOR is published at 4.50%. On April 17 (settlement date), you pay the counterparty the net difference:

$$10,000,000 \times (0.0450 - 0.0400) \times \frac{92}{360} = 10,000,000 \times 0.0050 \times 0.2556 = \$12,778$$

You owe $12,778 because LIBOR came in above your locked-in 4.00%. The contract ends. There are no further obligations.

## What Is an Interest Rate Swap?

A **swap** is a series of FRAs strung together. Rather than locking in one rate for one period, you lock in a rate (the swap rate) that applies to multiple periods, usually every quarter or semi-year for several years.

**Example swap:** On January 15, you enter a 5-year fixed-for-floating swap. You pay 3.50% fixed and receive 3-month LIBOR, on a $10 million notional, settled quarterly.

Over the next five years:
- March 15, June 15, September 15, December 15 of each year, you settle quarterly. On each settlement date, you exchange net payments based on the fixed rate (3.50%) and the floating rate (LIBOR, reset at the start of each period).
- After 20 periods (5 years × 4 quarters), the swap matures and your obligations end.

The swap is economically equivalent to entering twenty sequential 3-month FRAs (a "3x6" FRA on day 1, a "6x9" FRA on day 91, a "9x12" FRA on day 182, and so on). But instead of negotiating twenty separate contracts, you execute one swap and settle it period by period.

## Key Differences in Structure

| Aspect | FRA | Swap |
|--------|-----|------|
| **Number of periods** | 1 | Many (typically 4–40) |
| **Maturity range** | Weeks to months | Months to decades |
| **Rate-setting** | One forward rate for one period | A single swap rate applied to each period |
| **Settlement schedule** | Once, early in the rate period | Multiple times (quarterly, semi-annual) |
| **Notional** | Typically fixed | Fixed (or amortizing/accreting in variants) |

## Why Use an FRA Instead of a Swap?

**Short-dated needs:** If you expect floating-rate exposure for only 6 months—say, a short-term loan maturing soon—an FRA is simpler and cheaper than a 5-year swap.

**Filling gaps:** A company might have a swap covering 2024–2029 and use an FRA to hedge an intermediate 2027 borrowing not fully covered by the swap. This is called a "gap fill."

**Liquidity management:** FRAs settle quickly (within days), freeing up capital. Swaps, especially long-dated ones, tie up collateral (via [CSA](/swap-counterparty-credit-risk/) variation margin) throughout their life.

**Lower credit exposure:** Because an FRA settles once and you never exchange notional, the credit risk is minimal. A swap carries ongoing bilateral default exposure that evolves as rates move.

## Why Use a Swap Instead of an FRA?

**Efficiency:** Executing one 5-year swap is far less costly in time and legal documentation than executing twenty separate FRAs (one for each quarter over 5 years).

**Standardization:** Swaps are standardized, liquid instruments. FRAs for every period-pair are less liquid; dealer bid-ask spreads are often wider.

**Curve control:** By using one swap rate, you lock in a consistent cost of funding (or receiving). Using sequential FRAs exposes you to changes in the forward curve; each FRA's rate is set at deal time for its specific period, but the rates vary across periods. A swap, by contrast, applies the same rate to all periods, giving you a uniform hedge.

**Valuation simplicity:** If you want to exit a swap early, there's a single market quote for a 5-year swap rate. Unwinding multiple FRAs requires pricing each one and negotiating separately.

**Long-term hedging:** Companies with long-dated floating-rate debt or receivables naturally use swaps to match the duration of their exposure. An FRA is too short-lived.

## Pricing Relationship

The FRA rates for successive periods, derived from the market's forward rate curve, are embedded in the swap rate. A 5-year swap rate is roughly a weighted average of the forward rates for each of the twenty quarters—calculated so that the present value of paying fixed equals the present value of receiving the expected floating rates.

If you quote FRA rates for periods 3x6, 6x9, 9x12, etc., and discount them properly, you should recover the 5-year swap rate. Conversely, if swap rates move, FRA rates move in concert (though sometimes liquidity or supply-demand imbalances create small dislocations).

## Credit Risk Comparison

**FRA:** Once the FRA settles (typically 2 days after the rate is published), the contract is done. The creditor has received (or will receive) cash, and the debtor has paid. Credit exposure is minimal and only for the settlement cash—usually a small fraction of notional.

**Swap:** The swap remains bilateral and alive for its entire term. As rates move, the swap's mark-to-market swings, and so does each party's [counterparty credit risk](/swap-counterparty-credit-risk/). If the swap has a positive value to you and your counterparty defaults, you lose that value. However, in modern markets, collateral posted daily via a CSA limits that loss.

## Market Usage in Practice

**Banks and dealers** use FRAs to hedge short-term funding gaps and to take short-dated bets on rate movements. They use swaps for longer-term liability hedging, asset repricing, and speculation.

**Corporates** typically use swaps when they've issued floating-rate debt lasting multiple years and want to lock in a fixed cost. They might use an FRA if they expect a temporary floating-rate exposure (e.g., a bridge loan lasting 6 months).

**Mortgage servicers and banks** use swaps and swaptions to manage prepayment risk and refinancing exposure on their balance sheets.

**Hedge funds and proprietary traders** use both, often on a relative-value basis: if the 5-year swap rate seems expensive, they might go short the swap and long a ladder of FRAs, betting that the curve repositions.

## Example: FRA vs Swap for a Corporation

A company takes on a $50 million floating-rate loan for 3 years, paying LIBOR + 1.5% quarterly. It wants to lock in a fixed cost.

**Option 1 (FRA strategy):** Buy twelve 3-month FRAs, one for each quarter, locking in, say, 4.20% for quarter 1, 4.15% for quarter 2, etc. (rates differ slightly because each FRA locks in a different forward period). Total cost: twelve separate trades, twelve ongoing settlement obligations, complex record-keeping. Total effective fixed rate: roughly 4.18% (an average of the forward rates). Plus 1.5% loan spread = 5.68% total cost.

**Option 2 (swap strategy):** Enter a single 3-year, $50 million fixed-for-floating swap at 4.25% fixed, paying LIBOR. One trade, one counterparty, one confirmation, quarterly settlements. Effective fixed rate: 4.25% + 1.5% = 5.75% total cost.

The swap is slightly more expensive (5.75% vs. ~5.68%) because its all-in rate is determined at trade date, whereas the FRA ladder's effective rate reflects the forward curve at each FRA's inception. But the swap's simplicity, liquidity, and ease of early termination usually justify the small cost premium for corporate hedgers.

## See also

<div class="wiki-seealso">

### Closely related

- [Fixed-for-floating swap payment mechanics](/fixed-for-floating-swap-mechanics/) — How each swap settlement is calculated
- [How an interest rate swap is valued after inception](/swap-valuation-mid-life/) — Pricing and mark-to-market
- [Counterparty credit risk in swaps](/swap-counterparty-credit-risk/) — Bilateral default exposure in swaps
- [Forward contract](/forward-contract/) — General framework for forward-starting derivatives

### Wider context

- [Interest rate swap](/interest-rate-swap/) — Broader overview of the swap market
- [Derivatives hedging](/derivatives-hedging/) — Why entities use swaps and FRAs
- [LIBOR](/libor/) — The floating-rate benchmark in most swaps and FRAs
- [SOFR](/sofr/) — The new benchmark post-LIBOR
- Spread — The loan spread added to floating rates

</div>
