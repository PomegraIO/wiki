---
title: "Basis Point Sensitivity"
description: "DV01 and duration as the standard measures of how much a bond or portfolio loses (or gains) when interest rates move by one basis point."
keywords:
  - dv01
  - dollar value of a basis point
  - duration
  - interest rate risk
  - portfolio sensitivity
  - bond risk
image: "/svg/monetary.svg"
---

*A **basis point** is 0.01% of yield; **basis point sensitivity** (or DV01, the dollar value of one basis point) quantifies the dollar loss a bondholder faces if rates tick upward by that amount. For a portfolio manager, it is the most concrete answer to the perpetual question: how much do I stand to lose if the [interest-rate](/interest-rate/) environment shifts?*

## Why one basis point, not one percent?

Interest rates are typically quoted to hundredths of a percent: 4.35%, 4.87%, 5.12%. A single percentage point—from 4% to 5%—is a coarse unit and masks important distinctions. A basis point, also called a **bip**, is one-hundredth of a percent. It lets traders and portfolio managers discuss tiny but real moves with precision. Bond markets turn on basis-point moves. A 10 basis point rally—say, from 5.00% to 4.90%—can mean millions of dollars in profit or loss across a large portfolio, even though the change looks microscopic.

## DV01: dollar value of one basis point

DV01 is the standard measure of basis point sensitivity. It answers: if yields rise by one basis point, how many dollars does this position lose? Conversely, if yields fall by one basis point, how many dollars of gain?

For a simple bond with a [price](/interest-rate-risk/) of $1 million, a DV01 of $80 means that a 1 basis point rise in yield costs $80, and a 1 basis point fall gains $80. Scale matters: a $10 million position with the same DV01 per unit would have a total position DV01 of $800,000.

DV01 is calculated from [duration](/duration/), a bond's sensitivity to yield shifts. For most bonds, DV01 approximates:

DV01 ≈ (Bond Price × Modified Duration × 0.0001)

A bond worth $1,000,000 with a modified duration of 8 years would have a DV01 of roughly $800: each basis point move is worth $800. This is a shorthand; the precise value depends on the bond's [coupon-rate](/coupon-rate/), time to maturity, and the current yield environment.

## Why DV01 matters more than duration alone

Duration is useful: it tells you how many years of price movement you suffer per 1% yield move. But portfolio managers think in dollars, not years. DV01 converts duration into concrete risk—the amount an investor actually stands to lose. A 10-year bond with 7 years of duration looks different when expressed as "$700 per basis point" on a $1 million holding.

DV01 also scales intuitively across a mixed portfolio. If you own $50 million of bonds with an average DV01 of $300 per basis point per $1 million face value, your total portfolio DV01 is $15 million—meaning a 1 basis point move in yields costs or gains $15 million. Traders use this to hedge: if you're long $15 million of DV01, you can offset half by shorting $7.5 million of DV01 in [Treasury-bill](/treasury-bill/) or [Treasury-bond](/treasury-bond/) [futures-contract](/futures-contract/).

## Basis point sensitivity across different securities

DV01 is not unique to bonds. Stocks with high [dividend-yield](/dividend-yield/) can carry interest-rate risk. An [equity-etf](/equity-etf/) that holds dividend-payers may have a small positive DV01 (it benefits when rates fall, because dividend yields become more attractive relative to risk-free returns). [Interest-rate-risk](/interest-rate-risk/) derivatives—[interest-rate](/interest-rate/) swaps, swaptions, and [callable-bond](/callable-bond/) positions—have DV01 as their primary risk metric.

Traders often hedge DV01 in isolation, assuming that only rates move. In practice, [credit-spread](/credit-spread/) and other risks may dominate. A corporate bond's DV01 tells you only about rate sensitivity; it says nothing about the issuer's creditworthiness. That is why risk managers calculate both rate risk (DV01) and [credit-risk](/credit-risk/) (via spread duration) separately.

## Basis point moves in historical context

Over the past two decades, a typical daily move in U.S. 10-year [Treasury-bond](/treasury-bond/) yields is 2–5 basis points. A month of rising rates might see 40–80 basis points of moves. Rare crisis episodes can produce 100+ basis point shifts in a day. An investor holding $100 million of long-dated bonds with a portfolio DV01 of $80,000 per basis point could face a swing of $8 million in a single month of sustained rate rises.

Longer-duration portfolios have larger DV01 per dollar of assets. A [hedge-fund](/hedge-fund/) with aggressive [leveraged-etf](/leveraged-etf/) positions or long-dated [bond](/bond/) strategies can run DV01 in the hundreds of millions, meaning a 10 basis point move swings the fund's value by millions—a key reason why [interest-rate-risk](/interest-rate-risk/) is the first risk many managers check each morning.

## Limits of DV01

DV01 is a first-order measure: it assumes a parallel shift in the [yield-curve](/yield-curve/)—that all rates rise or fall together by the same number of basis points. In reality, the curve often tilts: short rates may rise while long rates stay flat, or vice versa. A portfolio DV01 of zero does not guarantee immunity from [interest-rate-risk](/interest-rate-risk/) if the curve steepens or flattens.

Moreover, DV01 is linear. For extreme moves—a 500 basis point rally—the true price change becomes nonlinear and DV01 overstates gains. This is why sophisticated risk-management teams also track [convexity](/convexity/) and other higher-order sensitivities.

DV01 also ignores embedded options. A [callable-bond](/callable-bond/) appears to have a fixed duration until rates fall sharply and the issuer calls the bond, eliminating the expected upside. [Value-at-risk](/value-at-risk/) and scenario analysis are needed to capture these tail scenarios.

## See also

<div class="wiki-seealso">

### Closely related

- [Duration](/duration/) — weighted average time to cash flow, the theoretical foundation for DV01
- [Interest Rate Risk](/interest-rate-risk/) — the broader category of losses from adverse yield moves
- [Yield Curve](/yield-curve/) — the shape across maturities that underlies basis point sensitivity
- [Convexity](/convexity/) — nonlinear price sensitivity beyond duration
- [Modified Duration](/modified-duration/) — duration adjusted for yield level, used to calculate DV01
- Bond Price — why basis point moves matter in practice

### Wider context

- [Interest Rate](/interest-rate/) — the fundamental price of borrowed money
- [Bond](/bond/) — the security whose value changes with every basis point
- [Futures Contract](/futures-contract/) — contracts used to hedge DV01 exposure
- [Hedge Fund](/hedge-fund/) — institutional managers tracking DV01 daily
- [Treasury Bond](/treasury-bond/) — the benchmark security for rate risk measurement

</div>
