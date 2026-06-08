---
title: "Key Rate Duration and Non-Parallel Yield Curve Shifts"
description: "Key rate duration measures bond sensitivity to changes at specific maturities on the yield curve, enabling precise hedging when rates don't shift uniformly."
keywords:
  - key rate duration
  - non-parallel yield curve shift
  - bond interest rate risk
  - duration ladder
  - yield curve sensitivity
  - fixed-income hedging
---

*A **key rate duration** measures how much a bond's price will change when yields shift at a single point along the yield curve, rather than assuming all maturities move together. This framework captures what actually happens in markets: the 2-year, 5-year, and 10-year rates often move by different amounts, and key rate durations tell a bond manager or hedger exactly where the real exposure lives.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Key Rate Duration — key facts</div>

<img src="/svg/fixed-income.svg" alt="An abstract editorial mark for fixed income." />

<div class="wiki-infobox-caption">Breaks down a bond's interest-rate sensitivity across the maturity spectrum.</div>

|   |   |
|---|---|
| **Single number** | [Duration](/duration/) assumes parallel shifts; misses real risk |
| **Multiple numbers** | Key rates capture sensitivity at 2y, 5y, 10y, 30y, and others |
| **Real-world use** | Portfolio managers use key rate durations to pinpoint hedges |
| **Calculation** | Shock yields at each key maturity; measure price impact |
| **Common tenors** | 2, 5, 10, 30 years; some models use finer grids |
| **Advantage** | Reveals mismatches [duration ladder](/duration/) cannot capture |

</aside>

## Why traditional duration falls short

A single [duration](/duration/) number—say 5.2 years—tells you how sensitive a bond is to a 1% change in yield, but it silently assumes every maturity on the yield curve moves by the same amount. In reality, the Federal Reserve might hike short-term rates sharply while long-term markets price in slower future hikes, leaving the 10-year yield relatively flat. A bond manager holding long-dated bonds faces real price risk at the 10-year tenor, yet a traditional duration figure doesn't distinguish between risk at different maturities.

**Key rate duration** splits this single number into pieces. Instead of saying "this bond has 5.2 years of duration," you say "it has 0.3 years of duration to the 2-year rate, 1.8 years to the 5-year, 2.9 years to the 10-year, and 0.2 years to the 30-year." Each slice quantifies exposure to rate moves at a specific maturity. If the 10-year yield jumps 50 basis points while others stay still, the bond with 2.9 years of 10-year key rate duration loses roughly 2.9% of its market value.

## How non-parallel shifts happen in real markets

The yield curve is not a single lever. It bends, twists, and steepens based on where supply, demand, and expectations concentrate. A central bank tightening cycle often flattens the curve—short rates rise more than long rates—because markets expect lower growth and inflation later. A recession scare can invert it, pushing long-term yields below short-term ones. A new debt issuance glut at a particular maturity (say, 5-year Treasuries) can create a local bump, leaving 2-year and 10-year rates largely unchanged.

This means a simple [duration](/duration/) hedge misses the mark. A pension fund with a large allocation to 10-year bonds might try to hedge interest-rate risk by shorting Treasuries. If it hedges using 2-year Treasuries because that's what has deep liquidity, it could hedge only the 2-year key rate duration—essentially hedging the wrong risk. When the 10-year rises sharply (perhaps due to inflation fears) while the 2-year stays flat, the short position in 2-year Treasuries provides no offset, and the portfolio suffers large losses.

## Computing key rate durations

A key rate duration is calculated by bumping—shifting up by a small amount, typically 1 basis point—the yield at one maturity, holding neighboring yields roughly constant, then measuring the bond's price change. The calculation is mechanical: if the price falls by 0.029% when the 10-year yield rises 1 basis point, the 10-year key rate duration is 2.9.

In practice, practitioners use software or pre-built models that include the yield curve and the bond's [cash flows](/cash-conversion-cycle/). The model applies the shift, interpolates across maturities (since you can't really isolate a single point without affecting neighbors), and reports the sensitivity. Some models use a coarse grid (2, 5, 10, 30 years), while sophisticated traders might use a finer one (1, 2, 3, 5, 7, 10, 20, 30 years) to catch nuances.

A bond's key rate durations sum roughly to its effective duration. So if a bond's 2-year KRD is 0.3, 5-year KRD is 1.8, 10-year KRD is 2.9, and 30-year KRD is 0.2, the total is roughly 5.2—matching the traditional duration figure. This is reassuring: key rates refine the picture without contradicting the old measure.

## Using key rate durations to hedge

Suppose a bond portfolio manager holds €50 million par of a 7-year German Bund with a 10-year key rate duration of 2.5. The manager believes the 10-year rate will rise and wants to hedge that specific exposure without betting against the entire curve. She can short 10-year Bunds in an amount such that the short position's 10-year KRD offsets the long position's 10-year KRD.

If a 10-year Bund has 10-year KRD of 8.5, she needs to short roughly €50m × 2.5 / 8.5 = €14.7m par. This hedge isolates the 10-year risk, leaving the 2-year, 5-year, and 30-year exposures untouched. If her conviction is that the 5-year rate will fall while the 10-year rises, she now has that positioning: long 5-year risk, short 10-year risk, neutral overall [duration](/duration/).

Without key rate durations, she might have tried a naive hedge (shorting equal par amounts or equal notional), only to find that her risk profile hadn't shifted at all, or had worsened.

## Practical limits and model risk

Key rate durations depend on assumptions about how the yield curve moves. If the model assumes that a 1 basis point shift at the 10-year doesn't affect the 5-year, but in reality correlations are high, the model understates true risk. Similarly, if the yield curve's behavior changes—say, central banks start rigidly pegging certain maturities, or geopolitics fractures normal correlations—historical models can lag.

A portfolio with many bonds across different issuers and credit qualities also faces [basis risk](/basis-risk/). A corporate bond's price depends not only on Treasury yield changes but also on credit-spread widening or tightening. Its key rate duration applies to the Treasury component only. A flight to quality might cause spreads to blow out even as Treasuries rally, leaving the hedge incomplete.

## See also

<div class="wiki-seealso">

### Closely related

- [Duration](/duration/) — the single-number measure of interest-rate sensitivity
- [Yield curve](/yield-curve/) — the full map of yields across maturities, the foundation for key rate analysis
- [Interest-rate risk](/interest-rate-risk/) — the main source of price risk in fixed income
- [Bond](/bond/) — the fundamental instrument whose sensitivity we measure
- [Hedging](/derivatives-hedging/) — how managers use key rate durations to offset unwanted risk
- [Basis risk](/basis-risk/) — the gap between hedging instrument and actual risk exposure

### Wider context

- [Fixed-rate mortgage](/fixed-rate-mortgage-personal/) — mortgages are bonds, subject to the same duration mechanics
- [Treasury bill](/treasury-bill/) — short-term rate reference point on the yield curve
- [Treasury bond](/treasury-bond/) — long-term rate reference point
- [Mortgage-backed security](/mortgage-backed-security/) — complex bonds with their own curve risks
- [Market timing](/market-timing/) — using yield-curve views to position portfolios

</div>
