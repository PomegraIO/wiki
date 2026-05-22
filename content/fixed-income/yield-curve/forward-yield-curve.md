---
title: "Forward Yield Curve"
description: "The yield curve implied by current spot rates, showing the market's expectation of what interest rates will be in future periods."
keywords:
  - forward yield curve
  - forward rates
  - yield curve dynamics
  - spot rates
  - interest rate expectations
---

***The forward yield curve** is a theoretical curve showing the implied short-term interest rates for each future period, derived from current [spot yield curve](/wiki/yield-curve/) prices. It reveals what the market is pricing in regarding future rate levels and is essential for pricing long-term bonds, [swaps](/wiki/interest-rate-swap/), and [forwards](/wiki/forward-contract/).*

<div class="wiki-hatnote">
For the spot curve, see [Yield curve](/wiki/yield-curve/). For practical trading applications, see [Forwards contract](/wiki/forward-contract/).
</div>

<aside class="wiki-infobox">

| Attribute | Detail |
|-----------|--------|
| **Derived from** | Spot yield curve (zero-coupon bond prices) |
| **Horizon** | Any future period (1-year forward, 5-year forward, etc.) |
| **Formula** | (1 + y₅)⁵ ÷ (1 + y₂)² = (1 + f₂₅)³ |
| **Interpretation** | Expected future short-term rates under expectations hypothesis |
| **Application** | Pricing forwards, swaps, and long-dated bonds |
| **Usage** | Central banks, hedge funds, fixed-income portfolios |

</aside>

## Understanding forward rates through an example

Suppose the spot yield curve shows:
- **1-year rate**: 2% annually
- **2-year rate**: 2.5% annually

What is the market implying about the 1-year rate one year from now (called the "1-year forward rate, one year out" or "1y1y")?

Using no-arbitrage pricing:
- Invest $1 at 2% for 1 year: you have $1.02.
- Alternatively, invest $1 at 2.5% for 2 years: you have $1.02502.

The two must be equivalent (ignoring tiny transaction costs). If you are willing to invest at 2% for 1 year, you are also willing to lock in the rate for year 2. The forward rate equalizes the two strategies:

$$\text{1y1y forward} = \frac{(1.025)^2}{1.02} - 1 = 3.00\%$$

In other words, the market is pricing the 1-year rate next year at approximately 3.0%.

## Constructing the full forward curve

The forward curve is a continuous function. From the spot curve, we extract forward rates for every future period:

- **0y1y** (current 1-year rate): 2.0%
- **1y1y** (1-year rate, one year from now): 3.0%
- **2y1y** (1-year rate, two years from now): 3.2%
- **3y1y** (1-year rate, three years from now): 3.0%

Plotting these yields a curve showing how the market expects short-term rates to evolve.

## Spot vs. forward: two views of the same market

The **spot curve** answers: "What is today's annual return for a bond maturing in N years?"

The **forward curve** answers: "What is the market pricing as the return for a bond starting N years from now and maturing 1 year later?"

Both are equivalent views of the same discount function. A steep spot curve (long-term rates much higher than short-term) implies forward rates are rising, meaning the market expects future short-term rates to climb. A flat spot curve implies stable forward rates.

## Upward-sloping forward curve signals

A upward-sloping forward curve (forward rates rising over time) typically indicates:

1. **Monetary tightening ahead**: Investors expect the [central bank](/wiki/central-bank/) to raise rates because inflation is a concern.
2. **Economic normalization**: After a crisis or recession, forward rates rise as the economy heals.
3. **Term premium compensation**: Investors demand higher rates for locking in long-term capital.

Conversely, a downward-sloping forward curve signals:
- Recession expectations (central bank will cut rates).
- Deflationary pressures.
- Risk-off sentiment (investors willing to accept lower future rates for safety).

## Application to pricing forwards and swaps

A [forward contract](/wiki/forward-contract/) to buy a bond one year from now is priced using the forward curve:

**Example**: A bond has a 3% coupon and matures in 3 years. What is the 1-year forward price?

1. Calculate the bond's value at year 1 using spot rates.
2. Discount back 1 year using the 1y1y forward rate.

This ensures the forward price is consistent with no-arbitrage—you cannot profit by simultaneously buying a forward and hedging with the spot market.

[Interest-rate swaps](/wiki/interest-rate-swap/) are priced similarly. A 5-year swap at "par" (both legs have equal value) is set so the fixed rate equals the [par swap rate](/wiki/par-swap/)—the weighted average of forward 1-year rates over the swap's life.

## Expectations hypothesis vs. reality

The **expectations hypothesis** assumes the forward curve represents unbiased expectations of future short-term rates. If the 1y1y forward is 3%, the hypothesis predicts the 1-year rate next year will actually be 3%.

In practice, this is often wrong. Forward rates typically overestimate future short-term rates, especially at longer horizons. Possible reasons:

1. **Term premium**: Investors demand extra compensation for locking in long-term rates, inflating forward rates.
2. **Risk aversion**: During stress, investors accept lower future rates for safety, compressing the forward curve despite recession expectations.
3. **Central bank guidance**: Forward guidance from central banks can suppress future rates below what "natural" market prices might suggest.

## Yield curve dynamics: movements in the forward curve

The forward curve shifts with expectations of [monetary policy](/wiki/monetary-policy/) and growth. Key scenarios:

| Scenario | Forward curve | Spot curve |
|----------|---------------|-----------|
| **Fed hiking cycle** | Forward rates rise across tenors | Steepens at short end, may flatten overall |
| **Growth scare** | Forward rates fall | Inverts (long < short) |
| **Inflation surprise** | Long-term forwards rise more | Steepens overall |
| **Taper tantrum** | Forward rates across curve spike | Parallel shift upward |

A trader monitoring the forward curve watches for:
- **Curve flattening**: Shorter-term forward rates falling relative to longer-term (suggests near-term economic softness).
- **Curve steepening**: Longer-term forward rates rising relative to shorter-term (suggests longer-run inflation expectations rising).
- **Parallel shifts**: All forward rates moving together (broad macro shift in rate expectations).

## Bootstrap method: extracting forwards from bond prices

Central banks and traders construct the forward curve using the **bootstrap method**:

1. Start with the shortest-maturity bond (e.g., 1-year Treasury). Its yield is the 0y1y forward (current 1-year rate).
2. Use that to back out the discount factor for year 1.
3. Move to the next bond (2-year), solve for the year-2 forward rate.
4. Repeat, working up the curve.

This is how [zero-coupon yield curves](/wiki/zero-coupon-economics/) are extracted from coupon-bearing bond prices, and the forward curve emerges naturally.

## Use in managing duration risk

Portfolio managers use the forward curve to model interest-rate scenarios:

- If I think the Fed will hold rates longer than the forward curve implies, the curve will steepen, and long-dated bonds will appreciate.
- If I think inflation will surprise higher, forward rates will rise across the board, and bonds will depreciate.

By understanding the forward curve's positioning relative to their own views, investors can structure duration exposure (short vs. long bonds) accordingly.

<div class="wiki-seealso">

### Closely related

- [Yield curve](/wiki/yield-curve/) — The spot curve that underlies the forward curve.
- [Forward contract](/wiki/forward-contract/) — Instrument priced using forward rates.
- [Interest-rate swap](/wiki/interest-rate-swap/) — Swap rates derived from forward curve.
- [Par swap](/wiki/par-swap/) — Swap fixed rate derived from forwards.
- [Term premium](/wiki/term-premium/) — Why forward rates may diverge from expectations.

### Wider context

- [Spot-yield-curve-dynamics](/wiki/spot-yield-curve-dynamics/) — How the spot curve shifts over time.
- [Constant maturity swap](/wiki/constant-maturity-swap/) — Swaps linked to forward tenors.
- [Monetary policy transmission](/wiki/monetary-transmission-mechanism/) — How policy shapes forward expectations.
- [Bond pricing](/wiki/bond-price-formula/) — Fundamental valuation using discount factors.

</div>
