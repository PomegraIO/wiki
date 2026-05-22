---
title: "Bond Yield Curve Risk"
description: "The risk that changes in the shape of the yield curve will reduce bond portfolio values, particularly from non-parallel shifts."
keywords:
  - yield curve risk
  - bond risk
  - curve shift
  - duration
---

*Bond Yield Curve Risk is the exposure a bond portfolio faces from changes in the shape of the [yield curve](/wiki/yield-curve/)—the relationship between bond maturities and their yields.* Most bond investors understand that longer-maturity bonds are more sensitive to interest-rate changes than shorter-maturity bonds ([duration](/wiki/duration/) risk). But many miss the subtler risk: the curve itself can reshape. Long-term rates might rise while short-term rates stay flat, or vice versa. A bond portfolio's value depends not just on the absolute level of interest rates but on how the curve moves. A steepening curve can hurt long-bond holders; a flattening curve can hurt those holding medium-duration bonds. Understanding curve risk is essential for [bond portfolio](/wiki/fixed-income-etf/) management.

<aside class="wiki-infobox">

| Key fact | Detail |
|----------|--------|
| **Definition** | Risk from non-parallel changes to the [yield curve](/wiki/yield-curve/) |
| **Source** | Different maturities rising/falling by different amounts |
| **Measurement** | [Duration](/wiki/duration/) and [convexity](/wiki/convexity/); key-rate duration |
| **Parallel shift** | All maturities move by the same amount (duration risk) |
| **Non-parallel shift** | Different maturities move differently (curve risk) |
| **Common shifts** | Steepening (long yields rise more), flattening (long yields rise less) |
| **Protection** | Matching [duration](/wiki/duration/); staying neutral on curve shape |
| **Measurement tool** | Key-rate duration by maturity bucket |

</aside>

## Parallel vs. non-parallel curve shifts

The standard [bond duration](/wiki/bond-duration-risk/) calculation assumes all yields move by the same amount—a **parallel shift** of the yield curve. If the 2-year yield rises by 1%, the 10-year yield also rises by 1%, and a bond's price declines proportionally to its [duration](/wiki/duration/). This is convenient for math but rarely happens in practice.

In reality, the curve **reshapes**. A **steepening** occurs when long-term yields rise faster than short-term yields (or fall slower). A **flattening** occurs when long-term yields rise more slowly (or fall faster). A **butterfly shift** sees the middle of the curve move differently from the ends.

Each non-parallel shift affects bond prices in ways a simple [duration](/wiki/duration/) calculation misses.

## Steepening and effects on different bonds

When the curve steepens, longer-maturity bond yields rise faster than shorter-maturity yields. A 10-year bond held by an investor suffers a larger price drop than a 2-year bond, even though the 10-year bond has higher [duration](/wiki/duration/) to begin with.

Example: The curve steepens when the 2-year yield stays at 4% but the 10-year yield rises from 4% to 5%. A bond portfolio heavy in 10-year bonds gets hammered. An investor who believed the curve would flatten or stay parallel but held 10-year bonds took on unrecognized steepening risk.

Conversely, steepening can be good for investors in short-duration bonds or money-market funds, as their reinvestment opportunities improve (new lending rates are higher).

## Flattening and the squeeze on medium-duration bonds

When the curve flattens, long-term yields rise more slowly (or fall more) than short-term yields. A 5-year bond, caught in the middle, can be hit from both sides: yields near the short end are rising (pushing the bond's yield up), but the bond's price-yield relationship is being squeezed as the curve flattens.

A [ladder strategy](/wiki/ladder-strategy/) (evenly spaced holdings across maturities) can suffer disproportionately in curve flattening because the middle rungs lose value. An investor who built a ladder expecting parallel shifts but the curve flattens will see losses in the 5–7 year part of the portfolio, even if their overall [duration](/wiki/duration/) was matched to the benchmark.

## Key-rate duration and curve positioning

To measure exposure to curve risk, portfolio managers use **key-rate duration**—the sensitivity of the portfolio to changes at specific points on the curve (2-year, 5-year, 10-year, 30-year, etc.).

A bond portfolio might have:
- 2-year key-rate duration of 0.5 (1% yield change at 2-year point causes 0.5% portfolio change)
- 5-year key-rate duration of 1.2
- 10-year key-rate duration of 2.1
- 30-year key-rate duration of 0.3 (minimal exposure at long end)

This profile tells the manager exactly which part of the curve the portfolio is exposed to. If flattening is expected (long yields unchanged, intermediate yields up), the portfolio can be rebalanced to reduce 5–10 year duration and accept 2-year or 30-year duration instead.

## The [butterfly spread](/wiki/butterfly-shift/) and curve trades

A [butterfly spread](/wiki/butterfly-shift/) is a deliberate bet on how the curve will reshape. An investor might:
1. Buy 2-year bonds.
2. Sell (go short) 5-year bonds.
3. Buy 10-year bonds.

This position benefits if the 5-year point underperforms (the "body of the butterfly wings are pinched"). If the curve flattens such that 5-year yields rise while 2-year and 10-year yields stay flat, the position profits from the short 5-year and losses on the long 2-year and 10-year offset each other, netting a gain on the short.

## Duration matching as curve-neutral strategy

A [bond fund](/wiki/bond-etf/) manager who is uncertain about curve movements but confident about overall interest-rate levels can match the portfolio's [duration](/wiki/duration/) to the benchmark. If the portfolio has the same overall [duration](/wiki/duration/) as the Bloomberg Aggregate Bond Index, then parallel yield shifts will not hurt or help relative to the benchmark.

However, non-parallel shifts still create relative losses. If the manager expected the curve to stay flat but it steepens, the fund will underperform if it is heavy in long bonds.

## Hedging curve risk with [swaptions](/wiki/swaption/) and [interest-rate swaps](/wiki/interest-rate-swap/)

A bond manager exposed to steepening risk (long-duration bonds, worried long rates will spike) can hedge using [interest-rate swaptions](/wiki/swaption/)—the right to enter a [swap](/wiki/interest-rate-swap/) at a fixed rate. Or, the manager can simply short [interest-rate swaps](/wiki/interest-rate-swap/) of longer maturity, reducing duration at the long end.

These hedges are expensive and complex, so most investors instead actively manage curve positioning through portfolio rebalancing.

## The yield curve slope and economic signals

Curve shape conveys economic expectations. A steep curve (long yields much higher than short yields) signals growth expectations and inflation premium. A flat or inverted curve signals recession fears.

For bond investors, understanding what the curve slope signals is useful. An inverted curve has often preceded recessions, so investors holding bonds during inversion may benefit from falling yields. But the timing and magnitude are uncertain, making curve bets risky.

## Ladders, barbells, and bullets in light of curve risk

Three classic [bond portfolio](/wiki/fixed-income-etf/) structures handle curve risk differently:

1. **Ladder**: Equal holdings across maturities (2, 4, 6, 8, 10 years). Diversifies across curve points but concentrates in the middle, vulnerable to flattening.

2. **Barbell**: Heavy holdings at short and long ends; minimal in the middle. Reduces exposure to middle-curve flattening risk but takes more long-duration risk.

3. **Bullet**: Concentrated around one maturity (e.g., all 5-year bonds). Maximizes predictability of [duration](/wiki/duration/) but ignores curve shape.

The choice depends on curve outlook and risk tolerance.

---

<div class="wiki-seealso">

### Closely related
- [Yield Curve](/wiki/yield-curve/) — The relationship between maturity and yield
- [Duration](/wiki/duration/) — Sensitivity to parallel yield shifts
- [Convexity](/wiki/convexity/) — The curve of the price-yield relationship
- [Interest Rate Risk](/wiki/interest-rate-risk/) — General bond risk from rate changes

### Wider context
- [Bond Duration Risk](/wiki/bond-duration-risk/) — Price sensitivity to parallel rate moves
- [Interest Rate Swap](/wiki/interest-rate-swap/) — Tool for managing curve exposure
- [Swaption](/wiki/swaption/) — Option on a swap; used for curve hedging
- [Ladder Strategy](/wiki/ladder-strategy/) — Bond portfolio structure across maturities
- [Butterfly Spread](/wiki/butterfly-spread/) — Bet on middle-of-curve moves
- [Yield Curve Inversion](/wiki/yield-curve-inversion/) — Long yields below short yields, recession signal

</div>
