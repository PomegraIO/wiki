---
title: "Swap Duration and DV01 Explained"
seo_title: "Swap DV01 & Duration: Measuring Rate Risk in Swaps"
description: "DV01 is the dollar change in a swap's value per 1 basis-point rate move. How to calculate swap DV01 and duration and use them for hedging and risk limits."
keywords:
  - swap dv01 duration explained
  - dv01 interest rate swap
  - swap duration calculation
  - basis point sensitivity
  - derivatives hedging
  - interest rate risk
image: /svg/derivatives.svg
---

*A **DV01** (dollar value of one basis point) and **modified duration** are the essential tools for measuring and managing interest-rate risk in [interest rate swaps](/interest-rate-swap/). DV01 tells you precisely how much a swap position gains or loses when rates move by one basis point; duration expresses that same sensitivity as a time-weighted measure. These metrics underpin how traders [hedge](/derivatives-hedging/) exposures, how risk managers set limits, and how portfolio managers understand what their swap positions actually own.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Swap DV01 & Duration — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">DV01 quantifies price sensitivity; duration expresses it in years-equivalent terms.</div>

|   |   |
|---|---|
| **DV01** | Dollar change per 1 basis-point rate move |
| **Formula** | DV01 = (PV of 1 bp move in swap value) |
| **Modified duration** | % price change per 1% rate move (closely related to DV01) |
| **Typical calculation** | Bump-and-reprice: calculate value at rate ±1 bp, take difference |
| **Units** | DV01 in dollars; duration in years |
| **Used for** | Hedging, risk limits, position sizing, portfolio rebalancing |
| **Key insight** | Higher duration = greater rate sensitivity |

</aside>

## Understanding DV01 (Dollar Value of 1 Basis Point)

A **basis point** is 1/100th of a percentage point (0.01%). A rate move from 5.00% to 5.01% is a one-basis-point move. DV01 measures the dollar impact of such a move on your swap position.

Suppose you enter a 10-year [fixed-rate](/fixed-rate-mortgage-personal/) [interest rate swap](/interest-rate-swap/) as the fixed-rate payer on a $10 million notional. You pay fixed at 4.50%; you receive floating (SOFR or another benchmark). If SOFR-based rates rise by 1 basis point across the entire curve, your fixed-rate obligation is now less attractive (you're paying 4.50% when the market pays 4.51%). The value of your swap position deteriorates.

How much? That depends on the swap's [duration](/duration/) (its time-weighted sensitivity). A rough calculation: a 10-year swap has a duration of roughly 7–8 years. The DV01 would be approximately 0.07 to 0.08% × $10 million = $7,000 to $8,000.

More formally, DV01 = Modified Duration × Position Size × 0.0001.

If the modified duration is 7.5 years:
DV01 = 7.5 × $10,000,000 × 0.0001 = $7,500

This means a 1 basis-point rise in rates costs you $7,500 on that position. A 10 basis-point move costs $75,000. A 100 basis-point (1%) move costs $750,000.

## How Swap Duration Is Calculated

A swap's **duration** is not the time to maturity, but rather a weighted average of when you receive and pay each leg's cash flows, discounted at current rates.

For a fixed-rate payer swap receiving floating:
- The fixed leg has positive duration (you lock in a fixed cash flow; rate rises hurt you).
- The floating leg has near-zero duration (it resets frequently, staying close to par).
- Net duration ≈ duration of the fixed leg.

A 10-year fixed-rate swap has a modified duration typically between 7 and 8 years, depending on the [coupon](/coupon-payment/) rate and the [yield curve](/yield-curve/) shape. A 2-year swap might have 1.9 years of duration. A 30-year swap might have 18–20 years.

Duration is also called **[DV01](/interest-rate-swap/) sensitivity** or **rate sensitivity**. It tells you the swap's price sensitivity per basis point of yield change, expressed in years.

## Modified Duration vs. Macaulay Duration

**Macaulay duration** is the raw time-weighted average (in years) of when you receive cash flows.

**Modified duration** adjusts Macaulay duration for the present-value effect: how much the price changes as a percentage when yields move by 1%.

Modified Duration = Macaulay Duration / (1 + Yield)

For swaps and bonds, modified duration is the practical one. It tells you: "If yields rise by 1%, this swap's value falls by X%."

Example: A swap with a modified duration of 7.5 years means a 1% rate rise (100 basis points) causes a ~7.5% decline in the swap's mark-to-market value.

For calculating DV01, modified duration is used because we care about small moves (1 bp) and need the percentage change, then multiply by notional to get dollar DV01.

## Computing DV01: The Bump-and-Reprice Method

The standard approach to DV01 is **bump-and-reprice**:

1. Calculate the current value of your swap position (typically 0, since swaps are usually initiated at par).
2. Bump the yield curve by 1 basis point (raise all rates by 0.01%).
3. Recalculate the swap value using the new curve.
4. The difference is the DV01.

Example: A 5-year fixed-rate payer swap, $5 million notional, 3% fixed rate.

| Scenario | 5-year rate | Swap value |
|----------|------------|-----------|
| Base case | 3.00% | $0 |
| Rates up 1 bp | 3.01% | −$385 |
| DV01 | — | **$385** |

A 1 basis-point rise costs you $385. If the curve moves up 25 basis points, you lose $385 × 25 = $9,625.

## Negative vs. Positive DV01

Your DV01 sign depends on which side of the swap you're on:

- **Fixed-rate payer** (you pay fixed, receive floating): Positive DV01 when rates *fall*, negative DV01 when rates *rise*. Rate increases hurt you.
- **Fixed-rate receiver** (you receive fixed, pay floating): Negative DV01 when rates fall, positive DV01 when rates rise. Rate increases help you.

This can be confusing. Some traders flip the sign to align with an intuitive convention: "How much does my position gain if rates rise?"

If you're a fixed-rate payer and rates rise, your swap loses value (negative return). So from that perspective, your DV01 is negative with respect to rate moves.

Most practitioners state DV01 as an absolute dollar amount and note the direction separately: "I'm long DV01" (benefit from rate falls) or "I'm short DV01" (benefit from rate rises).

## Using DV01 for Hedging

Suppose you issue $100 million of 10-year bonds at 4.5%. You're now exposed to falling interest rates (your debt stays at 4.5%, but market rates may fall, and you refinance cheaper). You're "long bonds"—you benefit if rates fall.

To hedge, you enter a 10-year fixed-rate payer swap with the same notional ($100 million). Now:
- If rates fall: your bond value rises (good), but your swap value falls (bad). The two offset.
- If rates rise: your bond value falls (bad), but your swap value rises (good). Again, offset.

By matching the DV01 of the swap to the DV01 of the bond, you achieve a [duration](/duration/)-neutral position. Rate moves don't hurt you—they roughly offset.

The bond might have a DV01 of $8,000 per basis point. The swap is sized to also have a DV01 of $8,000 per basis point. Any rate move leaves you roughly flat.

## Curve Risk Beyond DV01

DV01 assumes parallel shifts in the yield curve (all rates move by the same amount). In reality, the curve can twist: the short end rises while the long end falls, or vice versa.

A more sophisticated framework uses multiple DV01s—one for each point on the curve (2-year, 5-year, 10-year, etc.). This captures exposure to [curve steepening](/yield-curve/) or flattening.

Similarly, [credit spread](/credit-spread/) movements on corporate and mortgage swaps add another layer. A corporate fixed-rate payer swap is also short [credit risk](/credit-risk/) on the counterparty. But DV01 isolates the interest-rate component.

## DV01 vs. Duration: When to Use Each

**DV01** is best for:
- Hedging and position sizing (how many dollars move per bp).
- Risk monitoring and limit setting ($X limit on DV01 per desk).
- Day-to-day P&L attribution (this move cost us $Y).

**Duration** is best for:
- Comparing sensitivity across instruments (this swap is longer duration than this bond).
- Conveying intuition (a 7-year duration means a 7% loss per 100 bp move).
- Academic and theoretical work.

In practice, traders use both interchangeably, converting one to the other as needed.

## Common Pitfalls

- **Confusing notional with value:** A $10 million notional swap is not worth $10 million. The mark-to-market might be $200,000. DV01 is based on notional sensitivity, not current value.
- **Ignoring basis risk:** Hedges are never perfect. The bond and swap might track differently (basis risk), leaving some unhedged exposure.
- **Assuming static duration:** As time passes and rates move, a swap's duration changes. A 10-year swap in 2 years becomes a 8-year swap. DV01 drifts.
- **Asymmetric rate moves:** DV01 assumes small moves in normal conditions. In stress, convexity (the second derivative of price with respect to rates) becomes material.

## See also

<div class="wiki-seealso">

### Closely related

- [Interest Rate Swap](/interest-rate-swap/) — fundamental swap mechanics and use cases
- [Duration](/duration/) — detailed definition and application across assets
- [Derivatives Hedging](/derivatives-hedging/) — hedging strategies with derivatives
- [Yield Curve](/yield-curve/) — the curve upon which rates move
- [Fixed-Rate Mortgage](/fixed-rate-mortgage-personal/) — duration in lending
- [Bond](/bond/) — bond duration and [DV01](/basis/) basics

### Wider context

- [Counterparty Risk](/counterparty-risk/) — credit exposure in swaps
- [Interest Rate Risk](/interest-rate-risk/) — managing rate sensitivity
- [Basis Risk](/basis-risk/) — imperfect hedges
- [Sensitivity Analysis](/sensitivity-analysis-valuation/) — broader risk measurement

</div>
