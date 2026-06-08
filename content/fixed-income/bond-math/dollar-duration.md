---
title: "Dollar Duration"
description: "The absolute dollar price change in a bond for a one-basis-point move in yield."
keywords:
  - dollar duration
  - bond price sensitivity
  - basis point
  - interest rate duration
  - fixed income risk
image: "/svg/fixed-income.svg"
---

*The **dollar duration** expresses a bond's [duration](/duration/) in dollar terms: the number of dollars (or cents) the bond's price will change for every basis point move in [yield](/yield-to-maturity/). It converts abstract time-weighted duration into a concrete figure that tells you the immediate stakes of a rate move.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Dollar Duration — at a glance</div>

<img src="/svg/fixed-income.svg" alt="An abstract editorial mark representing fixed-income instruments." />

<div class="wiki-infobox-caption">Quantifies bond price risk in dollars per basis-point yield shift.</div>

|   |   |
|---|---|
| **What it is** | The change in bond price (in dollars) for each basis point of yield movement |
| **Also called** | Dollar value of a 1 bp move, price value of a basis point (PVBP) |
| **Formula** | Dollar Duration = Duration × Bond Price ÷ 10,000 |
| **Units** | Dollars (or dollars per $100 of face value) |
| **Typical range** | $20 to $500+ per 1 bp, depending on maturity and price |
| **Related measure** | [DV01](/dv01/) (often used interchangeably in practice) |

</aside>

## From abstract to concrete

[Duration](/duration/) is elegantly abstract: a 5-year [Treasury bond](/treasury-bond/) has a duration of roughly 4.7 years. But what does that mean in your pocket?

Dollar duration answers precisely. That 4.7-year bond, priced at $98, has a dollar duration of about $4.60. If yields rise 1 basis point, its price falls to $97.9954—a loss of roughly $0.0046, or 0.46 cents per $100 of face value. For a $1 million position, that's a $46 loss.

For a portfolio manager holding hundreds of millions, that granular number is not academic—it dictates real risk exposure and [hedge](/hedge-fund/) sizing.

## The mathematics

The formula is straightforward:

**Dollar Duration = Duration × Bond Price ÷ 10,000**

The division by 10,000 converts basis points (which are hundredths of a percent) to a decimal scale. 

Alternatively, you can express it per $100 of par:

**Dollar Duration (per $100 par) = Duration × 100 ÷ 10,000 = Duration ÷ 100**

A 7-year [coupon bond](/coupon-payment/) with [duration](/duration/) of 6.2 years and priced at $103 per $100 of par has:

- Dollar Duration = 6.2 × 103 ÷ 10,000 = $0.0638 per basis point
- Or: $6.38 per 1 basis point move on a $1 million position

## Real-world application

Fixed-income traders use dollar duration constantly:

**Position sizing** — If a trader wants to hedge a portfolio of corporate bonds with Treasury [futures contracts](/futures-contract/), she needs to know the [futures](/futures-contract/) contract's dollar duration and size the hedge accordingly. If her portfolio has a dollar duration of $100 and each [futures contract](/futures-contract/) has a dollar duration of $50, she might short two contracts.

**Risk reporting** — Portfolio managers report daily risk to clients and risk committees. "We have $500,000 of duration risk" is far more meaningful than "6.3 years of duration" when the portfolio size is $50 billion.

**Marking the portfolio** — In fixed income, [market-to-market](/fair-value/) P&L is relentless. If you own $10 million of a bond and yields move 5 basis points, dollar duration tells you instantly whether you've just gained or lost money: multiply dollar duration by 5 and you have your approximate loss.

## Dollar duration vs. DV01

The terms are often used interchangeably by traders, and the concepts are nearly identical. Strictly speaking:

- **Dollar Duration** is the product of [duration](/duration/) and price: it expresses the bond's mathematical interest-rate sensitivity in dollars.
- **[DV01](/dv01/)** ("dollar value of one basis point") is empirically computed: you bump the yield by 1 basis point, reprice the bond, and measure the difference.

For bonds without [embedded options](/option/) (straight corporates, Treasuries), the two are mathematically equivalent. For [callable bonds](/callable-bond/) or [mortgage-backed securities](/mortgage-backed-security/), [DV01](/dv01/) can diverge because the bond's cash flows themselves change with rates—a phenomenon [duration](/duration/) doesn't capture directly.

In practice, when a trader says "the DV01 is $400," they usually mean the [DV01](/dv01/); when a quant says "dollar duration is $400," they're computing it from [duration](/duration/) and price. The result is the same for plain-vanilla bonds.

## Why it matters more than duration

A bond's [duration](/duration/) is timeless—it describes the shape of the bond's cash-flow stream. But its dollar duration changes as the bond's price changes. A bond bought at par has a different dollar duration than the same bond bought at a premium or discount, even though its [duration](/duration/) is nearly identical.

This matters because portfolio risk is always measured in dollars. You don't care that your bond has 4.5 years of [duration](/duration/) if it costs you $500,000 when rates rise 1 basis point. Dollar duration is the language of actual loss and gain.

## The hedge arithmetic

A [hedge](/hedge-fund/) works when you match dollar durations. Suppose you own $100 million of 10-year corporates with a dollar duration of $750,000 per basis point. Yields rise 10 basis points and you lose $7.5 million.

To offset that risk, you could short $750 million of 2-year [Treasury bills](/treasury-bill/) (which have a much lower dollar duration per dollar notional—say $50,000 per basis point) or sell [Treasury futures](/treasury-bill/) sized to exactly $750,000 of duration. If done correctly, your long corporate and short Treasury exposure offset, and the portfolio becomes duration-neutral.

Dollar duration makes that algebra transparent.

## Limitations

Dollar duration assumes a parallel [yield curve](/yield-curve/) shift. If the 5-year yield rises but the 10-year stays flat, your actual loss may differ from what dollar duration predicts. For precise risk under non-parallel moves, you need [key rate duration](/key-rate-duration/), which decomposes duration into sensitivities at each maturity point.

Also, dollar duration breaks down for bonds with [embedded options](/option/). A [callable bond](/callable-bond/) bought at a high price has less downside [duration](/duration/) than a straight bond (because if rates fall and the bond rallies, the issuer is more likely to call it), but standard dollar duration doesn't account for that optionality. [DV01](/dv01/) becomes more reliable because it's computed from actual repricing.

## See also

<div class="wiki-seealso">

### Closely related

- [Duration](/duration/) — the time-weighted measure of bond price sensitivity
- [DV01](/dv01/) — the empirically computed dollar value of a one-basis-point move
- [Key Rate Duration](/key-rate-duration/) — duration sensitivity at each specific maturity point
- [Basis Point](/alternative-trading-system/) — the unit (0.01%) used to express small yield changes
- [Yield-to-Maturity](/yield-to-maturity/) — the return if held to redemption
- [Price-to-Yield Relationship](/bond/) — the inverse relationship driving price sensitivity

### Wider context

- [Bond](/bond/) — the fundamental fixed-income instrument
- [Interest Rate Risk](/interest-rate-risk/) — the broad category of price volatility
- [Futures Contract](/futures-contract/) — the standard hedging vehicle
- [Callable Bond](/callable-bond/) — a bond whose duration complexity can trip up dollar-duration estimates
- [Treasury Bond](/treasury-bond/) — the benchmark instrument for duration calculations

</div>
