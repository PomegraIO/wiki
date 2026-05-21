---
title: "Yield Curve Swap"
description: "A swap that isolates exposure to the shape of the yield curve, letting traders bet on curve steepening or flattening."
---

*A yield curve swap is a contract where the two legs are tied to different tenors (time horizons) on the yield curve. Instead of a standard swap with one short-term and one long-term leg, both legs reference different points on the curve, isolating changes in the curve's shape. Traders use yield curve swaps to position on curve steepness, flattening, or twists.*

## Why yield curve swaps exist

Imagine a trader believes the **curve is too flat**. The 2-year rate is 4.0% and the 10-year rate is 4.2%. The trader thinks the spread should be wider (say, 50 bps) because the curve is inverted. But buying a 10-year bond and shorting a 2-year bond is messy (different maturities, different reinvestment profiles, different carry).

A yield curve swap lets the trader isolate **curve positioning** without worrying about the absolute level of rates. The trader can bet that the 10-year rate will rise relative to the 2-year rate (steeper curve) or vice versa (flatter curve).

## Structure and mechanics

A yield curve swap has two floating legs, each tied to a different tenor:

**Leg A**: Pays the 2-year swap rate (reset periodically as the new 2-year rate).

**Leg B**: Receives the 10-year swap rate (reset periodically as the new 10-year rate).

The notional is the same on both legs, but the floating rates are different:
- If the 2-year rate is 4% and the 10-year rate is 4.2%, the receiver of Leg B (the long 10-year leg) gets a net of 0.2% per period.
- If the curve flattens (10-year falls to 4.1%), the long 10-year leg's advantage shrinks to 0.1%.
- If the curve steepens (10-year rises to 4.5%), the advantage grows to 0.5%.

The P&L depends on how the **spread between the two legs** changes, not on the absolute level of rates. If both the 2-year and 10-year rates rise by 0.5%, the spread is unchanged, and the P&L is zero.

## Common yield curve structures

**2-10 curve trade**: Long the 10-year, short the 2-year. The trader receives the 10-year swap rate and pays the 2-year swap rate. If the curve steepens, the trader profits.

**10-30 curve trade**: Long the 30-year, short the 10-year. Focuses on the long end of the curve.

**2-5-10 butterfly**: A more complex structure where the trader is long the 5-year and short the 2-year and 10-year in a ratio (e.g., long 2x of the 5-year, short 1x of the 2-year and 1x of the 10-year). The trader bets that the belly of the curve (5-year) is out of line with the wings (2-year and 10-year).

**Curve twist**: A trader might believe the curve will steepen at the short end (2-5-year) while flattening at the long end (10-30-year). They can structure a swap to capture this.

## Valuation and pricing

Yield curve swaps are priced as a spread between two different-maturity swap rates. The "swap curve spread" or "curve swap rate" is the fixed spread that makes both legs equal in present value.

For a 2-10 curve swap:
$$ \text{Curve Spread} = R_{10y} - R_{2y} $$

where R_{10y} is the 10-year swap rate and R_{2y} is the 2-year swap rate at inception.

But the valuation of future resets is complex:
1. **Project forward rates**: Using the forward curve, estimate the 2-year and 10-year rates at each reset date.
2. **Discount**: Discount the net cash flows (difference between the two swap rates) back to present.
3. **Solve for the curve spread**: Find the fixed spread that makes the present value of both legs equal.

The curve spread is typically close to the current yield spread (10-year minus 2-year), but there can be adjustments for:
- **Convexity**: The 10-year rate is more volatile; adjustments account for this.
- **Liquidity**: The 10-year swap market is more liquid; dealers might price the 10-year leg more tightly.
- **Credit spreads**: Both swaps are OTC; the combined credit exposure affects pricing.

## Uses

**Curve flattener strategy**: A trader who believes the curve is too steep enters a "curve flattener" (short the 10-year, long the 2-year swap). If the curve flattens (spread shrinks), the trader profits. This is often a bet that the Fed will hike short-term rates while long-term rates stay anchored.

**Curve steepener strategy**: The opposite. The trader believes the curve will steepen (long 10-year, short 2-year). This is often a bet that growth will accelerate and long-term rates will rise faster than short-term rates, or that a recession is coming and the curve will steepen (short rates falling faster than long rates).

**Yield curve normalization**: During periods of unusual yield curve shapes (e.g., inversion), traders use curve swaps to bet on normalization. A trader might bet that an inverted curve will steepen back to normal.

**Risk hedging**: A portfolio manager with long-duration assets might enter a curve swap to hedge curve risk without changing the absolute duration of the portfolio. This is a sophisticated hedge for institutional investors.

**Relative value trading**: A dealer might identify a mispricing in the curve—say, the 7-year rate is too high relative to the 5-year and 10-year. The dealer can use a butterfly or other curve swap to arbitrage the mispricing.

## Risks

**Curve reversal risk**: If the trader is right about the curve's direction but the timing is wrong, the position can lose money before being profitable. A "steepener" that bets the curve will steepen might be wrong for months, even if eventually right.

**Parallel shift risk**: If all rates rise or fall together (a parallel shift in the curve), the shape doesn't change, and the trader's curve swap P&L is zero. But the underlying exposure (duration risk) is not hedged.

**Model and carry risk**: Valuation models and assumptions about future rates can differ from reality. Carry (the benefit of holding the position over time if the curve shape is stable) can work against the trader if the market moves against the trade.

**Liquidity and basis risk**: While individual swap rates (2-year, 10-year) are liquid, the curve swap might not be. A dealer might quote tight bid-ask on the 2-year and 10-year separately, but a wider spread on the curve swap.

**Convexity risk**: Because longer-dated rates are more volatile, the 10-year leg of a curve swap has more convexity than the 2-year. Large rate moves can cause unexpected P&L.

## Curve swap rates and Fed expectations

Yield curve swaps are used to read market expectations about the Fed:

- **Steeper curve spreads**: Often indicate expectations of economic growth or inflation (the Fed will keep short rates low but long rates will rise).
- **Flatter spreads**: Often indicate recession fears (the Fed will cut short rates, but long rates are anchored by low growth expectations).
- **Inverted curve**: Can signal a recession risk (markets expect short rates to fall and long rates to stay high).

These market signals are closely watched by central banks and policymakers.

<div class="wiki-seealso">
<h2>See also</h2>
<h3>Closely related</h3>
<ul>
<li><a href="/wiki/swap/">Swap</a> — the foundational structure.</li>
<li><a href="/wiki/interest-rate-swap/">Interest-rate swap</a> — the standard swap; yield curve swaps are a variant.</li>
<li><a href="/wiki/constant-maturity-swap/">Constant maturity swap</a> — another variant that isolates curve exposure.</li>
<li><a href="/wiki/basis-swap/">Basis swap</a> — a similar structure but for different indices, not different tenors.</li>
</ul>
<h3>Wider context</h3>
<ul>
<li><a href="/wiki/yield-curve/">Yield curve</a> — the underlying curve that shape changes are measured on.</li>
<li><a href="/wiki/duration/">Duration</a> — the interest-rate sensitivity of each leg differs by tenor.</li>
<li><a href="/wiki/federal-reserve/">Federal Reserve</a> — policy expectations drive curve shape.</li>
<li><a href="/wiki/counterparty-risk/">Counterparty risk</a> — present in all OTC swaps.</li>
</ul>
</div>
