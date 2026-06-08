---
title: "Swap Curve"
description: "The yield curve constructed from par interest-rate swap rates across maturities, used as a benchmark for corporate and institutional pricing."
keywords:
  - swap curve
  - interest-rate swap
  - swap rates
  - par curve
  - pricing benchmark
  - yield curve
image: "/svg/derivatives.svg"
---

*The **swap curve** is a yield curve derived from the fixed rates quoted in [interest-rate swaps](/interest-rate-swap/) across maturities, typically ranging from one month to thirty years. It serves as a pricing benchmark for corporate bonds, mortgages, and other floating-rate instruments, and has become the primary reference for financial pricing in developed markets since the 2008 crisis.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Swap Curve — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives and structured products." />

<div class="wiki-infobox-caption">The market's preferred risk-free benchmark for long-term corporate pricing.</div>

|   |   |
|---|---|
| **What it is** | A curve of fixed swap rates plotted against maturity |
| **Also called** | Par swap curve, interest-rate swap curve |
| **Key reference** | US dollar, euro, sterling, yen, and CAD curves most liquid |
| **Typical maturities** | 1M, 3M, 6M, 1Y, 2Y, 3Y, 5Y, 7Y, 10Y, 15Y, 20Y, 30Y |
| **Underlying rate** | [LIBOR](/libor/) (legacy) or [SOFR](/sofr/) (modern US curve) |
| **Primary use** | Pricing corporate bonds, mortgages, and loans |
| **Relationship to Treasuries** | Often lies above the Treasury [yield curve](/yield-curve/) by a spread |

</aside>

## Definition and construction

The swap curve is built from the fixed rates at which [interest-rate swaps](/interest-rate-swap/) trade at par (i.e., with zero present value). At each maturity point, dealers quote the fixed rate they will pay in exchange for receiving the floating reference rate.

For instance, a dealer might quote: "Five-year pay-fixed at 2.45%." This means in a five-year swap, you pay 2.45% fixed annually and receive the floating benchmark (say, [SOFR](/sofr/) plus a small fixed spread). The curve is the collection of these fixed rates for all maturities.

The swap curve differs from the Treasury [yield curve](/yield-curve/) because it includes the credit risk and liquidity premium of swap dealers. A swap is only as good as the dealer's credit; it carries [counterparty risk](/counterparty-risk/). Treasuries, backed by the US government, carry no such risk. This is why swap rates typically lie above Treasury yields—the **TBA spread** (the spread between swap rates and Treasuries).

## Why swaps became the benchmark

Before 2008, many institutions used [LIBOR](/libor/) as their risk-free benchmark for long-term pricing. But when the financial crisis hit and [LIBOR](/libor/) soared due to bank credit stress, it became clear that [LIBOR](/libor/) was not truly risk-free. It embodied bank credit risk.

Simultaneously, the government-insured deposit base widened to include vast assets (money-market funds, short-term borrowing), and banks became less dependent on unsecured [LIBOR](/libor/) funding. As [LIBOR](/libor/) volatility decoupled from true short-term funding costs, swap dealers began quoting off alternative benchmarks.

The swap curve, being the aggregation of dealer quotes across many maturities, became the natural consensus benchmark. Corporate bond issuers and mortgage lenders increasingly priced off the swap curve rather than Treasuries or [LIBOR](/libor/).

Post-2021, as [LIBOR](/libor/) was formally phased out, the transition accelerated. Modern US swap curves reference [SOFR](/sofr/) (the Secured Overnight Financing Rate), a transaction-based rate with no credit component. This makes the curve cleaner but has required a massive market-wide transition.

## The curve's shape and interpretation

Like any [yield curve](/yield-curve/), the swap curve can be upward-sloping, flat, or inverted. An upward slope reflects expectations of future rate increases and a premium for holding longer-duration risk. An inverted curve (short rates above long rates) historically signals recession risk.

The slope also encodes liquidity preferences. Longer-maturity swaps are less liquid than short-maturity ones (fewer dealers, wider bid-ask spreads), so the curve typically has a kink where liquidity drops—often around the five-year or ten-year point.

In normal markets, the five-to-ten-year portion of the curve is most heavily traded and most reliable. The 2Y–10Y swap spread (the difference between ten-year and two-year swap rates) is a widely quoted metric of economic growth expectations.

## Pricing off the swap curve

When a corporate bond is issued, the pricing typically references the swap curve. A BBB-rated industrial bond might be priced at "swap + 150 basis points." This means its yield is the interpolated ten-year swap rate plus 1.50%.

Similarly, adjustable-rate mortgages often reset based on swap rates (or, historically, [LIBOR](/libor/)). A mortgage might be ARM (adjustable at swap + 250 bps). Commercial loans frequently use swap-curve anchors as well.

This is true across many non-Treasury securities. Because the swap curve is liquid, transparent, and observable in real time, it serves as the foundation for all corporate and institutional pricing. A portfolio manager can instantly compare a new bond issuance to the curve and decide if it offers adequate value.

## Par swap curve construction and interpolation

The swap curve is constructed by fitting a smooth curve through observed swap rates at standard maturities (1Y, 2Y, 5Y, 10Y, etc.). Between quoted maturities, rates are interpolated.

The curve construction is not trivial. Dealers use various methodologies (cubic spline, Nelson-Siegel models, bootstrap methods) to ensure the curve is smooth, arbitrage-free, and consistent with the forward-rate structure implied by swaps at different points.

An improperly constructed curve can create pricing errors. If the curve has a discontinuity or inconsistency at the five-year point (say, jumping unexpectedly), traders will exploit it, and the curve will re-equilibrate. This is why major dealers spend significant effort on accurate curve construction.

## Multiple curves for different bases

Modern post-2008 markets have introduced **multi-curve frameworks**. A single discount curve is no longer sufficient; there are multiple curves for different floating-rate benchmarks.

In US dollars, there is now a [SOFR](/sofr/) curve (for discounting and floating-rate swaps), a [LIBOR](/libor/) curve (for legacy contracts still in transition), and historical [LIBOR](/libor/) curves split by tenor (3M, 6M LIBOR curves for swaps tied to those specific rates).

European dealers quote EURIBOR curves and SONIA curves for sterling. Each curve is constructed independently, reflecting the supply and demand for swaps tied to that specific benchmark.

This multiplicity has increased operational complexity but better reflects true funding costs and credit differentials across benchmarks.

## Curve dynamics and trading

The swap curve is not static. It moves daily as interest-rate expectations shift, credit spreads widen or tighten, and supply and demand for swaps change.

Traders exploit curve moves in several ways. A **curve flattener** might sell long-dated swaps (betting the long end will underperform) and buy short-dated swaps. A **curve steepener** does the opposite. These trades are common bets among fixed-income portfolio managers.

In stressed markets, the curve can shift dramatically. During the March 2020 COVID crisis, swap curves became dislocated: the spread between swap rates and Treasuries widened sharply as liquidity dried up. The Federal Reserve had to intervene in swap markets to restore stability.

## Role in central clearing and standardization

The liquidity and standardization of the swap curve made it an ideal candidate for [central clearing](/central-clearing-swaps/). The most liquid swap contracts (those priced off the curve at standard maturities) are now cleared through central counterparties.

This clearing requirement, in turn, has increased the curve's prominence. Because cleared swaps are observable and reported, the curve has become more transparent. Regulators and market participants can see flows and pricing in real time.

## Limitations and criticisms

The swap curve is not flawless. It reflects dealer quoting, which can be influenced by inventory, balance-sheet constraints, and temporary supply-demand imbalances. In thin markets (e.g., the 30-year swap rate during quiet periods), quotes can be less reliable.

Historically, the [LIBOR](/libor/) curve was plagued by manipulation. In the years before 2012, major banks were accused of understating their [LIBOR](/libor/) submissions to hide funding stress. The swap curve inherited some of this distrust, though [SOFR](/sofr/) and other transaction-based rates are more resistant to manipulation.

Additionally, the curve reflects dealer credit risk, not a true risk-free rate. A shift in banking-sector creditworthiness can move the curve independent of macro economic shifts. During the 2008 crisis, when Lehman collapsed, the curve spiked not because of inflation expectations but because counterparty risk surged.

## Relationship to expectations and monetary policy

The swap curve is a key input to market expectations of future [monetary policy](/monetary-policy/). A steep curve (long rates well above short rates) suggests investors expect rising rates. A flat or inverted curve signals rate cuts or economic recession.

Central banks pay close attention to the curve. The [Federal Reserve](/federal-reserve/) uses swap curve data to gauge market pricing of future policy moves, and compares it to the Fed's own forward guidance. Discrepancies can trigger communication adjustments.

## See also

<div class="wiki-seealso">

### Closely related

- [Interest-rate Swap](/interest-rate-swap/) — the underlying contracts that define the curve
- [Yield Curve](/yield-curve/) — the Treasury counterpart, usually lying below the swap curve
- [SOFR](/sofr/) — the modern risk-free benchmark for USD swap curves
- [LIBOR](/libor/) — the legacy benchmark, now deprecated but still present in legacy contracts
- [Central Clearing of Swaps](/central-clearing-swaps/) — standardization that enhanced the curve's role
- [Credit Spread](/credit-spread/) — the TBA (swap-Treasury spread) reflects dealer credit risk

### Wider context

- [Corporate Bond](/corporate-bond/) — priced directly off swap-curve benchmarks
- [Monetary Policy](/monetary-policy/) — the curve encodes market expectations of future policy
- [Federal Reserve](/federal-reserve/) — monitors swap curve pricing as a market-expectations gauge
- Risk Management — the curve is foundational to hedge pricing and valuation

</div>
