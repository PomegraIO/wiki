---
title: "Asset Swap"
description: "A package combining a fixed-coupon bond with an interest-rate swap to convert it into a synthetic floating-rate instrument."
keywords:
  - asset swap
  - fixed-coupon bond
  - interest-rate swap
  - synthetic floating rate
  - bond derivatives
  - repo market
image: "/svg/derivatives.svg"
---

*An **asset swap** combines ownership of a fixed-coupon bond with an [interest-rate swap](/interest-rate-swap/) to synthetically convert the bond into a floating-rate instrument. The buyer receives the bond's fixed coupons and a funding payment, then pays back floating interest through the swap, creating an economic position that behaves like a floating-rate note.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Asset Swap — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives and structured products." />

<div class="wiki-infobox-caption">A market device to repurpose a bond's cashflow profile without selling it.</div>

|   |   |
|---|---|
| **What it is** | A fixed bond plus an interest-rate swap, packaged to mimic floating-rate debt |
| **Also called** | Cashflow swap, bond swap |
| **Key participants** | Bond holders, swap dealers, institutional investors |
| **Underlying** | A physical bond and a [swap contract](/interest-rate-swap/) |
| **Typical maturity** | Matches the bond's life (2–30 years) |
| **Primary use** | Convert bond coupons to floating-rate exposure |
| **Reference rate** | Usually [LIBOR](/libor/), [SOFR](/sofr/), or other benchmarks |

</aside>

## The mechanics: bond plus swap

An asset swap is straightforward in structure. You purchase a fixed-coupon bond—say, a corporate bond paying 3.5% annually. To convert this into floating-rate income, you simultaneously enter an [interest-rate swap](/interest-rate-swap/) with a dealer.

In the swap, you pay a fixed leg (say, 3.4%) to the dealer and receive the floating leg (say, [SOFR](/sofr/) plus a spread). The bond coupons (3.5%) and the fixed leg of the swap (3.4%) largely offset each other, leaving you with the floating leg plus a net fixed spread.

The result: you own a bond economically equivalent to a floating-rate note, even though the legal instrument remains a fixed bond. This is the essence of synthetic rate conversion. Asset swaps became a cornerstone of post-2008 fixed-income markets because they allowed investors to reshape existing portfolios without trading.

## Why investors use them

The primary motivation is **rate repricing**. If you hold a fixed bond but expect [interest rates](/interest-rate/) to rise sharply, an asset swap lets you convert to floating without selling the bond and realizing a potential loss. This is particularly valuable in flat or inverted [yield curves](/yield-curve/).

A second reason is **relative value**. A particular bond might trade cheaply relative to floating-rate alternatives. An asset swap lets you buy the bond and swap its fixed coupons into floating at a better net spread than buying a floating-rate note outright. This "asset swap spread"—the difference between the swap rate and the bond's all-in yield—captures mispricings across market segments.

Banks and asset managers also use asset swaps for **hedging**. A portfolio heavy in fixed-rate mortgages or loans can be hedged against rising rates via a packaged asset swap without disrupting the underlying assets.

## Asset swap spreads

The asset swap spread is the market's primary measure of relative value. It is expressed as a basis-point premium or discount to [LIBOR](/libor/) (or another reference rate) and tells you whether the bond is "cheap" or "rich" on a floating-rate basis.

For example, if a corporate bond trades at a 3.5% coupon but the asset swap spread is +80 basis points over [SOFR](/sofr/), you are synthetically receiving SOFR + 0.80% by owning the bond and swapping it. Compare this to a floating-rate note of the same credit that might offer only SOFR + 0.60%: the bond is the better value.

These spreads vary with credit conditions, supply and demand, and the shape of the [swap curve](/swap-curve/). In stress periods, they widen sharply as investors demand more compensation for holding bonds.

## Role in the repo and financing markets

Asset swaps are intimately tied to repo and short-term financing. Many asset swaps are funded via repo: an investor borrows cash by pledging the bond as collateral, then uses the proceeds to fund the swap initially. The repo spread (the difference between the cash-borrowing rate and the [SOFR](/sofr/) or other floating rate) determines the net economics.

In normal markets, funding is cheap and asset swaps make economic sense. During stress—say, a credit crunch—repo rates spike, funding dries up, and the economics collapse. This is why asset swap spreads blew out during the 2008 crisis and again during March 2020.

## Standard conventions

Most asset swaps are executed under ISDA documentation and reference standardized floating benchmarks. Modern swaps typically reference [SOFR](/sofr/) in the US, SONIA in sterling markets, or EURIBOR in euros. Legacy portfolios still carry [LIBOR](/libor/) references, but these are being transitioned away.

The swap's fixed leg is usually quoted as a tightly defined spread over par, making the comparison to the bond's yield clean. Dealers quote asset swap spreads in basis points, and execution is fast—often within the same day as bond purchase.

## Risk considerations

Investors in asset swaps assume multiple risks. **Counterparty risk** is significant: the swap dealer might default, leaving you with the bond and an unwound position. Central clearing has reduced this risk for standardized swaps, but bespoke asset swaps still carry [counterparty risk](/counterparty-risk/).

**Spread risk** is another factor. Asset swap spreads widen in stress, creating mark-to-market losses if you need to exit. **Basis risk** arises because the bond's actual coupons may not match the fixed leg of the swap perfectly; you carry a small timing or rate-reset mismatch.

Finally, there is **funding risk**. If the asset swap is funded via repo, repo rates can spike unexpectedly, making the position uneconomical or forcing you to liquidate at a loss.

## Modern evolution

Post-Dodd-Frank, many asset swaps (and larger interest-rate swaps) now novate to central counterparties, reducing [counterparty-risk](/counterparty-risk/) but adding margin requirements and clearing costs. This has made some asset swaps more expensive to execute but more transparent and safer.

Asset swaps remain a key tool for relative-value traders and portfolio managers navigating an increasingly complex fixed-income market. They are a reminder that synthetic rate conversion is often cheaper and faster than buying a new instrument outright.

## See also

<div class="wiki-seealso">

### Closely related

- [Liability Swap](/liability-swap/) — the inverse approach, converting floating debt to fixed
- [Interest-rate Swap](/interest-rate-swap/) — the derivative core of asset swaps
- [Swap Curve](/swap-curve/) — the benchmark pricing surface for swap rates
- [Central Clearing of Swaps](/central-clearing-swaps/) — post-2008 regulation governing swap execution
- [SOFR](/sofr/) — the modern replacement for LIBOR in US swap benchmarks
- [Credit Spread](/credit-spread/) — the yield premium driving asset swap economics

### Wider context

- [Bond](/bond/) — the underlying fixed-income instrument
- [Counterparty Risk](/counterparty-risk/) — the primary risk in uncleared swaps
- Repo — the short-term funding mechanism for asset swaps
- [Yield Curve](/yield-curve/) — influences relative value across maturities

</div>
