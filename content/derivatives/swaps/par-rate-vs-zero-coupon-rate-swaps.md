---
title: "Par Rate vs Zero-Coupon Rate in Swap Pricing"
description: "Par rate vs zero coupon rate in swap pricing: par rates are quoted market rates where the swap has zero value at initiation, while zero-coupon rates are discount factors used to value future cash flows."
keywords:
  - par rate vs zero coupon rate swap pricing
  - zero coupon discount factors swaps
  - swap curve bootstrapping
  - par swap rates quoted
---

*The **par swap rate** is the fixed rate that makes a swap worth zero to both parties at inception—the rate quoted in the market and agreed between dealers and clients. The **zero-coupon (or spot) discount rate** is the underlying mathematical curve used to value each individual cash flow on that swap. Every par swap rate embeds a unique set of zero-coupon rates. Understanding the relationship between them is essential to pricing swaps, bootstrapping the discount curve, and comparing swaps with different tenors and payment frequencies.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Par Rate vs Zero-Coupon Rate — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives." />

<div class="wiki-infobox-caption">Par rates are quoted; zero-coupon rates are the underlying discount factors.</div>

|   |   |
|---|---|
| **Par swap rate** | The fixed rate at which the swap's fair value equals zero at inception |
| **Zero-coupon rate** | The discount factor for cash flows at a single point in time (e.g., 3-month, 1-year, 5-year) |
| **Market input** | Par rates are observable market quotes; zero-coupon rates are derived through bootstrapping |
| **Maturity structure** | One par rate per tenor; many zero-coupon rates across the curve |
| **Pricing use** | Par rates define the swap contract; zero-coupon rates discount the cash flows |
| **Volatility** | Par rate moves drive changes in zero-coupon rates across the curve |
| **Relationship** | A single par rate is a weighted average of the zero-coupon rates underneath it |

</aside>

## The Par Swap Rate: What Is Quoted

When a dealer quotes a 5-year [interest-rate swap](/interest-rate-swap/) at 4.2%, that 4.2% is the **par swap rate**. It is the fixed rate that makes the swap's fair value zero if both parties sign at that rate right now.

Here is what "fair value zero" means: If Party A agrees to pay fixed 4.2% and receive floating SOFR, and Party B pays floating and receives fixed, then neither party owes the other an upfront payment. The discounted value of the fixed payments exactly matches the discounted expected value of the floating payments (using the forward curve for SOFR).

Par swap rates are:
- **Observable**: Every dealer and trading platform quotes them in real time.
- **Negotiable**: A client might pay 4.2% fixed and receive SOFR, or receive 4.2% and pay SOFR, depending on the deal.
- **Used as the contract rate**: Once the par rate is agreed, it becomes the fixed rate on the swap.

Par swap rates exist for standard tenors: 2-year, 3-year, 5-year, 7-year, 10-year, 20-year, and 30-year swaps are liquid and actively quoted. Longer tenors (15-year) and shorter tenors (6-month, 1-year) are less standard and wider in bid-ask spread.

## Zero-Coupon Rates: The Discount Curve

A **zero-coupon rate** (or **spot rate**) is the discount rate applicable to a single future date. It answers: *What is $1 received 3 years from now worth in today's dollars?*

If the 3-year zero-coupon rate is 3.8%, then $1 received in 3 years is worth:

$$\text{Present Value} = \frac{1}{(1 + 0.038)^3} \approx 0.891$$

So it is worth about $0.89 today.

A complete **discount curve** is a set of zero-coupon rates across all maturities: 0.25 years, 0.5 years, 1 year, 2 years, 3 years, and so on, out to 30+ years. This curve is the backbone of swap valuation. It is derived from market data, not quoted directly.

## Bootstrapping: Deriving Zero-Coupon Rates from Par Rates

If par swap rates are quoted but zero-coupon rates are not, how do we find the zeros? The answer is **bootstrapping**, a mechanical process that backs out zero-coupon rates from observable par rates.

### A simplified example

Suppose the following par rates are observed:

| Tenor | Par Swap Rate |
|-------|---------------|
| 1-year | 3.0% |
| 2-year | 3.5% |
| 3-year | 4.0% |

**Step 1: 1-year zero rate**

A 1-year par swap is annual, so the fixed payment is made once, one year from now. For fair value to equal zero:

$$\text{Fixed Payment} \times \text{Discount Factor}_1 = \text{Expected Floating Payment} \times \text{Discount Factor}_1$$

Simplifying:
$$\text{Fixed Rate} = \text{Expected Floating Rate}$$

If the par rate is 3.0%, the 1-year zero-coupon rate is approximately 3.0% (this is exact for a 1-year swap with one payment).

$$\text{Discount Factor}_1 = \frac{1}{1.030} \approx 0.9709$$

**Step 2: 2-year zero rate**

A 2-year par swap has two annual payments: one in 1 year, one in 2 years. The fair-value equation is:

$$\text{Fixed} \times (\text{DF}_1 + \text{DF}_2) = \text{Floating}_1 \times \text{DF}_1 + \text{Floating}_2 \times \text{DF}_2$$

We know DF₁ from Step 1 (0.9709) and the par rate (3.5%). We can solve for DF₂ (the 2-year discount factor), and from DF₂, derive the 2-year zero-coupon rate.

Rearranging (assuming floating roughly equals par rates):

$$0.035 \times (0.9709 + \text{DF}_2) = 0.030 \times 0.9709 + \text{Forward}_2 \times \text{DF}_2$$

This is solved iteratively to find DF₂, from which the 2-year zero rate is extracted.

**Step 3: 3-year zero rate**

Repeat: use the known 1- and 2-year discount factors and the 3-year par rate to solve for the 3-year discount factor, then the zero rate.

This process continues up the curve. Each new tenor depends on all the prior tenors, which is why it is called **bootstrapping**: you pull yourself up by your bootstraps, one rung at a time.

## Par Rate as a Weighted Average

A useful insight: the par swap rate for a tenor is a weighted average of the zero-coupon rates underlying it. A 5-year swap's par rate is not the 5-year zero rate; it is a blend of the 0.5-year, 1-year, 1.5-year, 2-year, ..., 5-year zero rates, weighted by the discount factors.

This is why par rates and zero rates are often different. If zero rates are steep (rising sharply with maturity), the par rate for a long-tenor swap will be closer to the long-dated zero rate because those discounted cash flows carry less weight. Conversely, in a flat yield curve, par and zero rates converge.

## Practical Pricing Workflow

Here is how par and zero rates work together in practice:

1. **Market data**: Dealers observe the par rates for 2-year, 3-year, 5-year, 10-year, and 30-year swaps.
2. **Bootstrap the curve**: Use the par rates to derive the full zero-coupon discount curve.
3. **Value a swap**: Given a client's swap (say, pay fixed 4.2% in a 5-year contract), discount every payment (fixed and floating) using the zero-coupon curve, then net the discounted cash flows to find the market value.
4. **Adjustments**: Add spreads for credit risk, funding cost, and bid-ask to the zero curve to get the rate to quote to the client.

## Curve Shapes and Par vs. Zero Rates

### Normal (upward-sloping) curve

When longer-dated zeros are higher than shorter-dated zeros:
- Par rates are also upward-sloping.
- The par rate for each tenor lies *below* the terminal zero rate of that tenor (on average), because shorter-dated zero rates (which are lower) are weighted in.

### Inverted curve

When longer-dated zeros are lower than shorter-dated zeros:
- Par rates are also inverted, but less steeply.
- Inversion in par rates is typically less dramatic than in zero rates because par rates mix short and long zeros.

### Flat curve

When zeros are roughly constant across maturities:
- Par rates are also flat.
- Par and zero rates are nearly identical.

## Why This Matters for Traders and Risk Managers

1. **Curve risk**: Changes in the zero-coupon curve drive mark-to-market gains and losses on swaps. A trader hedging [interest-rate risk](/interest-rate-risk/) must understand how parallel shifts, twists, and butterfly moves in the zero curve affect the fair value of each swap in the portfolio.

2. **Pricing and quotation**: Dealers quote par rates, but they use zero-coupon curves internally. A discrepancy between the zero curve implied by market par rates and a dealer's own estimates can create arbitrage opportunities.

3. **Swap valuation after inception**: Once a swap is signed, its fair value changes daily as the zero-coupon curve evolves. The mark-to-market P&L is the change in the discounted present value of the fixed and floating legs, using the updated zero curve.

4. **Bootstrapping as risk management**: Risk managers regularly bootstrap the zero curve from market data to ensure that internal valuations are current and match the market.

## Multi-Curve Frameworks

Modern swap valuation is more complex. Since 2008, the assumption that a single discount curve works for all cash flows has broken down. Practitioners now use:

- **OIS (Overnight Index Swap) curve**: For discounting cash flows, reflecting funding cost.
- **Forward SOFR curve**: For projecting floating LIBOR-like payments (post-LIBOR reform, SOFR is standard in USD swaps).

A 5-year par swap is now priced using:
- The zero-coupon **OIS curve** to discount all cash flows.
- The zero-coupon **SOFR forward curve** to estimate future floating payments.

The par rate quoted in the market reflects both curves. Traders must maintain and understand both curves separately to manage [interest-rate risk](/interest-rate-risk/) accurately.

---

## See also

<div class="wiki-seealso">

### Closely related

- [Interest-rate swap](/interest-rate-swap/) — the primary swap type on which par rates are quoted
- [Discounted cash flow valuation](/discounted-cash-flow-valuation/) — the mathematical foundation for zero-coupon pricing
- [Yield curve](/yield-curve/) — the par rate and zero-coupon curves that define swap pricing
- [Duration](/duration/) — how par and zero rates drive duration-based risk measures
- [Notional principal in swaps](/notional-principal-swap/) — the underlying amount scaled by par rates to compute payments

### Wider context

- [Bond pricing](/bond/) — another context where par and zero rates are used
- [Forwards and futures](/futures-contract/) — contracts priced using zero-coupon curves
- [Fair value](/fair-value/) — how zero curves determine fair value of swaps
- [Interest-rate risk](/interest-rate-risk/) — the primary risk managed using par and zero rate curves

</div>
