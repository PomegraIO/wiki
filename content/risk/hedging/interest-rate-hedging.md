---
title: "Interest Rate Hedging"
description: "Mitigating bond and debt sensitivity to rate changes through derivatives or offsetting positions."
keywords:
  - interest rate hedging
  - rate risk
  - duration hedge
  - interest rate swaps
  - bond hedging
---

*An **interest rate hedge** is any position designed to offset the loss in market value of a bond or floating-rate debt when interest rates rise. Hedges range from simple duration matching to complex derivative strategies like [interest rate swaps](/wiki/interest-rate-swap/) and [swaptions](/wiki/swaption/).*

<aside class="wiki-infobox">

| Aspect | Detail |
|---|---|
| **Core Risk Managed** | [Interest rate risk](/wiki/interest-rate-risk/) on fixed-income positions |
| **Hedging Tools** | Swaps, futures, options, shorter-duration bonds, cash |
| **Key Metric** | [Duration](/wiki/duration/) — primary measure of rate sensitivity |
| **Cost** | Swap spreads, option premiums, opportunity cost of hedging |
| **Unhedger** | [Floating-rate bonds](/wiki/floating-rate-bond/) naturally hedge rising rates |
| **Common User** | Banks, pension funds, mortgage originators |

</aside>

## Why rate hedging matters

A [bond](/wiki/bond/) with 5 years of [duration](/wiki/duration/) loses roughly 5% of its market value if rates rise 1%. A corporation with $100 million of fixed-rate debt on its balance sheet faces the mirror image: if rates rise sharply, its outstanding debt becomes more expensive relative to market rates, and its ability to refinance at comparable terms deteriorates. A pension fund holding a large portfolio of bonds loses assets if rates spike unexpectedly.

Hedging removes or reduces that sensitivity. A pension fund expecting rates to rise might sell [Treasury bond futures](/wiki/treasury-bond/) to neutralize its [interest rate risk](/wiki/interest-rate-risk/). A mortgage originator holding a portfolio of home loans (a natural short position on rates—originations fall if rates rise) might buy swaptions to protect against being forced to sell mortgages at unexpected losses.

## Common hedging tools

**Duration matching**: The simplest hedge. If a pension fund knows it has liabilities due in 15 years, it can match the duration of its assets to 15 years, ensuring that asset and liability values move in parallel with interest rate shifts. This is called [liability-driven investing](/wiki/fixed-income-fund-strategy/).

**Interest rate swaps**: A bond issuer with floating-rate debt can enter a [swap](/wiki/interest-rate-swap/) to pay fixed and receive floating, converting the cash-flow structure to effectively fixed-rate. The swap offsets the rising-rate pain; if rates rise, the issuer pays more on its debt but receives more from the swap counterparty.

**Treasury futures**: A fund holding corporate bonds might short [Treasury futures](/wiki/treasury-bond/) to create a [basis](/wiki/basis/)—the fund benefits if corporate spreads compress relative to Treasuries, but loses if rates spike uniformly. Futures are liquid and low-cost but introduce basis risk.

**Bond futures**: The [CME](/wiki/cme-group/) trades 10-year, 5-year, and 2-year Treasury futures. Shorting the 10-year future is equivalent to a floating-rate position; rising rates deliver a gain.

**Interest rate options**: A portfolio manager can buy [interest rate caplets](/wiki/interest-rate-option/) (calls on rates) or payer swaptions to protect against rising-rate scenarios while retaining upside if rates fall. The trade-off is the cost of the option premium.

**Floating-rate exposure**: Switching portfolio duration from 5 years to 2 years reduces rate sensitivity directly. [Floating-rate bonds](/wiki/floating-rate-bond/) and [floaters](/wiki/floating-rate-note/) reset coupons in line with market rates and have near-zero duration.

## Duration and convexity

[Duration](/wiki/duration/) measures the percentage change in bond price per 100 basis points (1 percentage point) of rate change. A bond with duration 5 loses 5% in value if rates rise 1%—or gains 5% if rates fall.

[Convexity](/wiki/convexity/) captures the non-linear relationship between price and yield. Long-duration bonds exhibit positive convexity: prices fall less when rates rise (asymmetric downside) and gain more when rates fall (asymmetric upside). [Callable bonds](/wiki/callable-bond/) have negative convexity: they don't appreciate as much when rates fall because the issuer is likely to call (refinance). Hedging callable bonds is more complex because the convexity works against you in rallies.

## Application: Banks and mortgage originators

Banks hold mortgages (long duration, prepayment risk) funded by [deposits](/wiki/bank-reserve-injection/) that can be withdrawn anytime. Deposits are effectively short-duration: rates rise, customers flee to [money market funds](/wiki/money-market-fund/), deposits leave. A bank naturally has a [negative duration gap](/wiki/interest-rate-risk/): long assets, short liabilities. Rising rates hurt earnings.

A mortgage originator is even more exposed. Originations are highly interest-rate sensitive; if rates spike after originating mortgages, the mortgagee can refinance elsewhere, and the originator is stuck holding low-rate loans. Many originators use [mandatory-delivery forwards](/wiki/forward-contract/) and [interest rate locks](/wiki/forward-guidance/) to hedge the pipeline. They also may buy [swaptions](/wiki/swaption/) to protect against large rate moves.

## Hedging cost and basis risk

No hedge is free. Buying swaptions costs the option premium upfront, even if rates never rise. Shorting futures locks in opportunity cost: if rates fall sharply (and the hedge profits), the underlying bond portfolio gains even more, but the short futures position offsets those gains.

[Basis risk](/wiki/basis-risk/) is also real. A fund hedging corporate bonds with Treasury futures may be protected against a parallel shift in the yield curve but exposed if corporate spreads blow out independent of rate moves—a 2008-style credit crunch. The hedge protects against rate risk but not [credit risk](/wiki/credit-risk/).

## Macro hedging vs. micro hedging

Micro hedging targets specific positions: a bond portfolio, a floating-rate loan, a mortgage pipeline. Macro hedging addresses enterprise-level duration exposure: a bank or pension fund might hedge the overall interest-rate sensitivity of its entire balance sheet.

Macro hedges use Treasury futures, [curve trades](/wiki/interest-rate-swap/), and cross-currency swaps to adjust the overall [duration gap](/wiki/interest-rate-risk/). They are rebalanced less frequently (quarterly or semi-annually) and often use systematic rules tied to [forward guidance](/wiki/forward-guidance/) or yield curve positioning.

## Regulatory and accounting considerations

Under [ASC 815](/wiki/derivative-accounting-hedging/), companies can designate certain hedges as "hedging relationships" and use [mark-to-market](/wiki/mark-to-market/) accounting asymmetrically—gains and losses on the hedge offset gains and losses on the hedged item through earnings, reducing income volatility. This requires documentation and strict correlation testing.

[Basel III](/wiki/basel-iii/) capital rules also recognize hedging: a bank that hedges interest-rate risk gets favorable risk-weighting on the hedged portion of its portfolio, reducing capital requirements.

<div class="wiki-seealso">

### Closely related

- [Interest rate swap](/wiki/interest-rate-swap/) — Primary derivative used in hedging.
- [Swaption](/wiki/swaption/) — Option to enter a swap; used for tail-risk protection.
- [Interest rate risk](/wiki/interest-rate-risk/) — The underlying risk being hedged.

### Wider context

- [Duration](/wiki/duration/) — Metric measuring rate sensitivity.
- [Convexity](/wiki/convexity/) — Non-linear price-yield relationship.
- [Fixed-income fund strategy](/wiki/fixed-income-fund-strategy/) — Broader portfolio management approach.

</div>
