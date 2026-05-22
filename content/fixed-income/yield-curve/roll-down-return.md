---
title: "Roll-Down Return"
description: "The return generated when a bond moves to a lower yield as it matures, independent of yield curve changes."
keywords:
  - roll-down return
  - bond returns
  - yield curve positioning
  - bond maturity
  - curve mechanics
---

*A **roll-down return** is the price gain a [bond](/wiki/bond/) generates simply by moving closer to maturity while the [yield curve](/wiki/yield-curve/) remains flat. A 10-year bond paying 3% will appreciate as it becomes a 9-year bond, because the market yields 2.5% to 9-year bonds (further down the curve). The investor "rolls down" the curve and captures the difference.*

<aside class="wiki-infobox">

| Scenario | Mechanics | Return Source |
|---|---|---|
| **Flat curve, 1 year passes** | 10Y @ 3% becomes 9Y @ 2.5% | Roll-down gain: ~0.5% |
| **Bond held to maturity** | Par is recovered | Roll-down embedded in coupon |
| **Curve steepens** | 10Y yields rise while 9Y yields fall | Roll-down gain can be offset or amplified |
| **Curve flattens** | All yields converge | Roll-down drives most of return |
| **Coupon reinvestment** | Coupons invested at new rates | Can help or hurt total return |
| **Typical annual roll** | 0.3–0.7% (varies by curve shape) | Predictable if curve doesn't shift |

</aside>

## The core mechanism

Imagine a [Treasury](/wiki/treasury-bond/) curve where:
- 10-year bonds yield 3.0%
- 9-year bonds yield 2.8%
- 8-year bonds yield 2.6%

An investor buys a 10-year bond at 3.0% on Day 1. One year later (assuming the curve shape hasn't changed), that bond is now a 9-year bond. By the curve's definition, 9-year bonds yield 2.8%. The bond's yield drops from 3.0% to 2.8%, and its price rises to reflect the lower yield. That price gain is the **roll-down return**.

The magnitude depends on:
1. **Curve slope** — how much yields differ at adjacent maturities (steeper curve = bigger roll-down)
2. **Time held** — roll-down accrues as you move down the curve; longer holds accumulate larger gains
3. **Curve stability** — the return only materializes if the curve shape doesn't shift; if the entire curve rises, the price gain is erased

## A worked example

A 10-year [Treasury bond](/wiki/treasury-bond/) with 3.0% coupon, purchased at par ($100).

**Day 1:**
- Price: $100
- Yield: 3.0%
- Maturity: 10 years

**1 year later (curve unchanged):**
- The bond is now a 9-year security.
- The market yields 2.8% on 9-year Treasuries.
- The bond's price rises to reflect 2.8% yield (roughly $101.90, depending on coupon accrual and compounding details).
- The investor also received one year of coupon (3.0% = $3).

**Total return:** (~1.90% price gain + 3.0% coupon) ≈ 4.9% in one year, even though the investor's original 10-year expectation was 3.0% per year.

The extra ~1.9% is the **roll-down return**.

## Why roll-down exists

Roll-down exists because the [yield curve](/wiki/yield-curve/) is normally upward-sloping (longer maturities yield more than shorter ones). This slope reflects:
- **Liquidity premium** — longer bonds are less liquid and riskier to hold
- **Expectation of rising rates** — the market expects short rates to rise
- **Inflation risk** — longer maturities face more inflation uncertainty

Once you own a bond, time's passage is mechanical—you *will* move one year closer to maturity, and if the curve slope persists, you *will* capture the roll-down.

## Roll-down and curve flattening/steepening

Roll-down assumes the curve shape is stable. But curves shift constantly:

**Curve flattening** (long-end yields rise relative to short-end) — erodes roll-down gains. You bought a 10-year expecting to roll to 9Y at a lower yield, but the 9-year yield *rises*, canceling the roll-down.

**Curve steepening** (long-end yields fall) — amplifies roll-down. You roll down the curve *and* the yield at your new maturity (9Y) falls, doubling the gain.

A [bond portfolio](/wiki/bond-yield-curve-risk/) manager who bets on roll-down is implicitly betting the curve will stay flat or steepen—but not flatten.

## Curve positioning and active management

Bond managers use roll-down as a tool:

- **Bullet strategy** — buy bonds at a single maturity (e.g., all 10Y) and hold, collecting roll-down until the bonds shorten to 5Y or so, then rotate to longer bonds. Simple, mechanical, low-cost.

- **Barbell strategy** — buy long-duration bonds (to capture high coupon and curve position) and short-duration bonds (for liquidity) while avoiding the middle, where roll-down payoff is steady but unspectacular.

- **Ladder strategy** — distribute holdings across a range of maturities (one bond maturing each year) so roll-down is continuously realized as each rung shortens.

The bullet strategy is popular in [bond ladders](/wiki/bond-ladder/) because the roll-down is easy to forecast if you believe the curve won't shift.

## Roll-down vs. carry and price appreciation

Total bond return = **coupon (carry) + roll-down + [duration](/wiki/bond-duration-risk/) (yield change effect)**.

For a buy-and-hold investor on a stable curve:
- **Coupon** is the stated yield (3% on a 3% bond)
- **Roll-down** adds 0.3–0.7% depending on curve slope
- **Duration effect** is zero if yields don't change

If yields *do* change:
- **Curve flattening** (yields rise) — duration loss dominates; roll-down doesn't offset
- **Curve steepening** (yields fall) — duration gain combines with roll-down

## Reinvestment risk and roll-down

When you collect a coupon, you face [reinvestment risk](/wiki/reinvestment-risk/): the new cash must be invested at current yields, which may be lower than your original bond's yield. If the bond yields 3% but new 9Y bonds yield only 2.5%, reinvesting the coupon at 2.5% is a drag on returns.

Roll-down does *not* account for coupon reinvestment. A manager expecting steep roll-down should also forecast where coupon reinvestment rates will be.

## Implementation in ETFs and mutual funds

[Bond ETFs](/wiki/bond-etf/) implicitly capture roll-down because they constantly rebalance to maintain target duration or maturity. A fund targeting "7-year duration" will automatically shed shorter-maturity bonds and shift to longer bonds as time passes and holdings shorten, locking in roll-down gains on a rolling basis.

[Ladder funds](/wiki/bond-ladder/) and [bullet strategies](/wiki/bullet-strategy/) are explicit roll-down plays. They are most popular when the curve is steep (roll-down payoff is large) and interest rates are expected to stay stable.

## Limitations and risks

1. **Curve shifts surprise** — the biggest risk. If the long end yields rise while the short end falls (curve flattening), roll-down evaporates and you suffer a duration loss.

2. **Reinvestment friction** — coupon cash must be reinvested; if reinvestment yields are low, total returns fall short of the coupon + roll-down forecast.

3. **Credit spread changes** — for [corporate bonds](/wiki/corporate-bond/), roll-down assumes [credit spreads](/wiki/credit-spread/) stay constant. If the issuer's [credit rating](/wiki/credit-rating/) deteriorates, spreads widen and the roll-down benefit shrinks.

4. **Opportunity cost** — if you lock in roll-down by holding steady, you miss the chance to rotate to higher-yielding or higher-momentum positions.

<div class="wiki-seealso">

### Closely related
- [Bond yield curve](/wiki/yield-curve/) — the curve shape that drives roll-down
- [Yield curve shape](/wiki/yield-curve-shape/) — understanding slope and twist
- [Bond duration risk](/wiki/bond-duration-risk/) — the other major source of bond return
- [Bond ladder](/wiki/bond-ladder/) — portfolio strategy built around roll-down
- [Bullet strategy](/wiki/bullet-strategy/) — concentrated maturity approach for roll-down capture

### Wider context
- [Bond basics](/wiki/bond-basics/) — foundational concepts
- [Reinvestment risk](/wiki/reinvestment-risk/) — interaction with roll-down
- [Curve flattening](/wiki/curve-flattening/) — risk to roll-down positioning
- [Curve steepening](/wiki/curve-steepening-commodity/) — can amplify roll-down gains
- [Fixed-income fund strategy](/wiki/fixed-income-fund-strategy/) — how funds implement roll-down

</div>
