---
title: "Option Series"
description: "A class of options sharing the same underlying, expiration date, and strike price; contracts in a series trade and settle as a single security."
keywords:
  - option classification
  - strike price
  - expiration date
  - option contracts
  - derivatives trading
image: "/svg/derivatives.svg"
---

*An **option series** is the complete set of identical [option](/option/) contracts, defined by three fixed parameters: the underlying asset, the [expiration date](/expiration-date/), and the [strike price](/strike-price/). Every call with those coordinates belongs to one series; every put with those coordinates to another. All contracts within a series have identical rights, risks, and pricing.*

## What defines a series

A series is determined by exactly three dimensions:

**The underlying.** IBM common stock, the S&P 500 index, crude oil, EUR/USD—the asset you can buy or sell via the option.

**The expiration date.** Typically the third Friday of the month for equity options; quarterly for index options; or monthly and weekly variants on many exchanges. All contracts expiring on the same calendar date belong to the same series.

**The strike price.** The fixed price at which the option buyer can exercise. A £50 strike, a £55 strike, and a £45 strike are three different series.

Once all three parameters align, every contract is fungible. One [call option](/option/) with underlying XYZ, expiry in March, strike £50 is interchangeable with every other such call. You can buy 10 contracts and sell 5 without naming which specific certificates you're trading—they're all identical.

## Series vs. class vs. the entire option chain

The terminology is nested:

**Class.** All options on a single underlying (e.g., "Apple options" or "crude oil options").

**Series.** The slice defined by expiry + strike + right (e.g., "Apple March £150 calls").

**The option chain.** The full menu of available series on a given underlying. On a major stock, this might run to dozens of expirations and dozens of strike prices per expiry, yielding hundreds of series.

## Why series structure matters

Series structure enables price transparency and [price discovery](/price-discovery/). All participants—market makers, floor traders, algorithm engines—trade contracts within the same series at the same [bid-ask spread](/bid-ask-spread/), creating a unified market price. A trader checking the bid on Apple March £150 calls gets the live consensus of all open interest in that exact series.

Fungibility also powers [margin](/leverage-ratio-forex/) and [leverage](/leverage-ratio-forex/). You can buy 100 shares and sell a covered call in the same series; the [broker](/broker/) knows the series perfectly offsets your stock risk if the call is exercised. Exchanges and clearing houses can net positions across the same series, reducing counterparty exposure.

## Open interest per series

[Open interest](/open-interest/) is the total number of contracts outstanding in a series at any given moment. A heavily traded series (e.g., Apple near-month at-the-money options) might have millions of contracts open. A far-out expiry at an exotic strike might have zero.

Liquidity pools by series. If you want to sell 1,000 contracts, the series with the highest open interest offers the tightest [spread](/bid-ask-spread/) and fastest execution. A thinly-traded series might have a spread of 25 cents; the popular one might be 1 cent.

## Standard vs. non-standard series

U.S. equity options follow standardized series: expirations on the third Friday of named months, monthly and now weekly expirations, and strikes set at fixed intervals (typically £1 or £2.50 apart for stocks trading under £200). This standardization reduces confusion and maximizes liquidity.

[Over-the-counter](/over-the-counter-option/) options or bespoke structures might skip standard series altogether. A derivatives dealer and a client might negotiate a custom expiry (any date they choose) and custom strike (any price), creating an entirely non-standard series of one. That one-off contract is still a series—just with no other members.

## Expiration cascades

On any given day, multiple series of the same underlying expire in sequence: front-month (nearest), then second month, then quarterly months out to a year or more. As the front-month series nears expiry and [time decay](/time-decay-theta/) accelerates, traders often roll positions—closing the near-month series and opening the same strike in the next series out. This practice keeps liquidity fresh in the front-month series and smooths the transition from one series to the next.

## Series and contract specifications

The exchange (or OTC counterparty) defines each series's fine print: multiplier (how many shares one option contract represents, typically 100 for equity options), settlement method (cash or physical delivery), and whether the option is [American-style](/american-option/) (exercisable anytime) or [European-style](/european-option/) (exercisable only at expiry). These specifications apply uniformly to all contracts in the series.

## See also

<div class="wiki-seealso">

### Closely related

- [Option](/option/) — the fundamental right-to-buy or right-to-sell contract
- [Strike Price](/strike-price/) — the fixed price embedded in every series
- [Expiration Date](/expiration-date/) — the end date for the series, when all contracts in it expire or settle
- [Option Break-Even Price](/option-break-even-price/) — the underlying price where a series position reaches zero profit or loss
- [In the Money](/in-the-money/) — how contracts in a series become profitable relative to their strike

### Wider context

- [Bid-Ask Spread](/bid-ask-spread/) — liquidity measure affecting how tightly series trade
- [Open Interest](/open-interest/) — the count of outstanding contracts in a series
- [Over-the-Counter Option](/over-the-counter-option/) — non-standard series negotiated bilaterally
- [FLEX Options](/flex-options/) — customisable series on regulated exchanges

</div>
