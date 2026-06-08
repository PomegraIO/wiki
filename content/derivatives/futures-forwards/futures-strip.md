---
title: "Futures Strip"
description: "A simultaneous position across consecutive delivery months of a futures contract, used to lock in average prices or hedge rolling exposures."
keywords:
  - futures strip
  - rolling hedge
  - consecutive contracts
  - commodity hedging
  - average price
image: /svg/derivatives.svg
---

*A **futures strip** is a collection of [futures contracts](/futures-contract/) stacked across sequential delivery months—say, January through December of the same year, or even multiple years. Instead of betting on a single maturity, the trader simultaneously holds or sells a ladder of expiries. It is the standard way producers, consumers, and financiers lock in average prices over an extended period.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Futures Strip — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives." />

<div class="wiki-infobox-caption">A portfolio of contracts spanning time; used to hedge long-term exposures.</div>

|   |   |
|---|---|
| **What it is** | A collection of futures contracts with sequential expiry dates for the same underlying asset |
| **Also called** | Futures ladder; rolling hedge; stack of futures |
| **Why use it** | Locks in average prices; neutralises [inflation](/inflation/) or [interest rate](/interest-rate/) risk over months or years |
| **Most common in** | Energy (oil, gas, power), agriculture (grain, livestock), metals, interest rates |
| **Trade mechanics** | Buy all contracts in the strip (to hedge or speculate on price), or sell them all (to hedge future production) |
| **Key risk** | Each leg has its own [expiration date](/expiration-contracts/); [rolling](/contango/) near-expiry contracts into distant months incurs slippage |

</aside>

## The mechanics: building a strip

Imagine a natural gas producer that will pump steady volumes for the next two years. Rather than hedge each month individually—and face the risk of missing a market move or getting the timing wrong—the company buys a strip of 24 consecutive monthly natural gas [futures contracts](/futures-contract/). Month 1 locks in the price for January delivery; month 2 for February, and so on through December of year 2.

The purchase price of each contract is the market [futures price](/futures-contract/) for that month, which sits somewhere on the [forward curve](/forward-curve/). If the curve is in [contango](/contango/), distant months cost more than near months; the producer pays a cumulative premium for that certainty. If the curve is in [backwardation](/backwardation/), the producer gets a discount on distant prices and might feel it captured good value.

Once the strip is in place, the producer's revenue is locked in. Spot prices can plummet or soar, but the hedged volumes are safe. This is [risk management](/market-risk/) in its most straightforward form.

## Average-price hedging

Strips excel at average-price hedging. A company does not care if January prices spike—it cares about the average price it receives over the full hedging horizon. By selling a strip of 12 contracts (say, crude oil, one month each), the firm locks in the average of 12 different market prices. The actual spot price for each month may surprise, but the [hedge](/hedge-fund/) dampens the volatility of total revenue.

This is superior to picking a single month to hedge or trying to time the market. A manager who hedges only December delivery faces the risk that prices collapse in other months. One who hedges naively by selling spot might miss profitable rallies. A strip smooths returns across the entire period and is intellectually honest: the company says, "We sell steady volumes each month, so we hedge steady volumes each month."

## Rolling hedges and the cost of contango

As time passes, the strip "rolls forward." January contracts expire, and the producer must close out that position (capturing whatever gain or loss from the move in spot prices). The producer then buys a new contract further out the curve—for example, in year 2 or year 3.

If the [forward curve](/forward-curve/) is in contango, rolling is costly. The new contract is more expensive than the old one, creating a slippage in the average price locked in. Over time and across many rolls, contango can erode the hedging gains of a strip, especially for long-dated exposures. This is why energy producers closely monitor [contango](/contango/) steepness; a very steep curve signals that rolling hedges will be expensive.

Conversely, in [backwardation](/backwardation/), rolling is profitable. The producer closes the expiring contract at a gain and buys the new contract at a discount. Backwardation rewards those holding inventory and rolling hedges forward.

## The strip in practice: commodities and rates

In crude oil and natural gas markets, strips are ubiquitous. A [futures commission merchant](/futures-commission-merchant/) might handle dozens of strips for energy firms on any given day. The mechanics are straightforward but the economics are subtle: the producer must choose a strip length (one year, three years, five years?), decide whether to hedge 100% of production (risky if volumes change) or a percentage (adds complexity), and monitor the cost of rolling.

In interest rate markets, [futures strips](/futures-strip/) serve a similar role. A bank borrows short-term repeatedly, facing interest rate risk each time it rolls. By buying a strip of [Eurodollar futures](/libor/) or Treasury futures, the bank locks in a chain of rates and neutralises [interest rate risk](/interest-rate-risk/). The economics are identical to commodity hedging: the strip locks in an average cost of funds.

## Risks and complications

A strip is not a perfect hedge. First, there is **basis risk**—the difference between the [futures price](/futures-contract/) and the actual spot price at delivery. A producer selling a crude oil strip is hedged against the futures price moving, but not against the local spot basis (the premium or discount of Brent crude vs. WTI, for example) shifting. This is usually small but real.

Second, there is **volume risk**. The producer assumes steady production. If drought cuts grain output or a refinery closes unexpectedly, the producer is over-hedged—it must sell physical at spot prices while holding excess futures positions. Conversely, if production surges, the producer is under-hedged and exposed. Sophisticated hedgers build flexibility into their strips, leaving a percentage unhedged.

Third, there is **liquidity risk**. Contracts near the front of the curve are highly liquid; distant contracts (say, five years out) may have sparse order books. Entering or exiting a large strip on a thin market can move prices against the trader.

Finally, there is the **mark-to-market** effect. As prices move, the strip's value changes daily, creating cash flow demands via [margin calls](/margin-call-forex/). A producer that sells a crude oil strip and prices rally must post margin to keep the position open. This can stress cash flow if not managed properly.

## Strips versus other hedging strategies

A strip is simpler and more transparent than buying a single far-dated [forward contract](/forward-contract/) (which requires finding a counterparty willing to lock in a two-year price, and entails [counterparty risk](/counterparty-risk/)). Strips are also more flexible than options; a producer paying for protective put options on each month sacrifices gains to the upside.

In practice, many hedgers combine strategies. A producer might sell a strip of futures (locking in a floor), then buy out-of-the-money call options to retain upside above the strip price. This creates a "collar"—defined risk, defined opportunity cost, and a cap on profit. It is more expensive than a pure strip but matches the risk appetite of management.

## See also

<div class="wiki-seealso">

### Closely related

- [Futures Contract](/futures-contract/) — the building block of any strip
- [Forward Curve](/forward-curve/) — the curve that determines the price of each leg in the strip
- [Contango](/contango/) — when strips become expensive to roll forward
- [Backwardation](/backwardation/) — when rolling is profitable for the strip holder
- [Basis Risk](/spread-risk/) — the difference between futures and spot prices
- [Counterparty Risk](/counterparty-risk/) — a risk strips avoid relative to forward contracts

### Wider context

- [Hedging](/hedge-fund/) — the broader discipline of protecting against price or rate moves
- [Margin Call](/margin-call-forex/) — the daily cash flow impact of holding strips
- Commodity Markets — where strips are most commonly used
- [Price Discovery](/price-discovery/) — how the market arrives at strip prices

</div>
