---
title: "Physical Settlement vs Cash Settlement in Derivatives"
description: "Physical settlement vs cash settlement derivatives: understand how contracts are resolved at expiry, from commodity futures to index options."
keywords:
  - physical settlement derivatives
  - cash settlement derivatives
  - contract settlement methods
  - derivatives expiration
  - futures settlement
  - options settlement
image: "/svg/derivatives.svg"
---

*At expiry, a derivative contract must be resolved in one of two ways: the underlying asset itself changes hands (**physical settlement**), or the parties exchange only the profit or loss in cash (**cash settlement**). Which mechanism applies depends entirely on the instrument and its design, with profound practical differences for hedgers and traders.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Settlement Methods — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">How a derivative gets unwound determines what an investor must own, store, or pay at the end.</div>

|   |   |
|---|---|
| **Physical settlement** | Underlying asset transferred between parties |
| **Cash settlement** | Only the gain or loss is paid in currency |
| **Common in physical** | Commodity [futures](/futures-contract/), equity [options](/option/), [forwards](/forward-contract/) |
| **Common in cash** | Index [futures](/futures-contract/), [interest-rate swaps](/interest-rate-swap/), many [equity-index options](/option/) |
| **Key trade-off** | Delivery logistics vs final cash outflow |

</aside>

## How Physical Settlement Works

In **physical settlement**, the contract-holder receives or must deliver the actual underlying asset. When a crude oil [futures contract](/futures-contract/) expires, the buyer takes possession of the barrels (or the seller arranges their delivery). When you exercise an equity call [option](/option/) on Apple, you must pay the strike price and receive 100 shares in your account.

Physical settlement is the default in agricultural and energy markets, where the underlying—corn, wheat, crude, copper—is the point of the trade. A farmer or refiner enters a futures contract not to speculate on price moves, but to lock in a price for goods they will actually handle. At expiry, the [futures contract](/futures-contract/) forces settlement: the buyer pays the agreed price and receives delivery (or the seller arranges it); the seller receives the price and ships the product.

For equity options, physical settlement is also standard. Holding a call [option](/option/) grants the right to buy 100 shares at the strike price; exercising it means the stock lands in your brokerage account. You must then own or carry it. This creates a real friction: if the stock price has soared, the [option](/option/) is lucrative, but you might not have capital ready to fund the purchase.

## How Cash Settlement Works

In **cash settlement**, no asset changes hands. Instead, the contract is marked to the final market price, and the winner receives the difference in cash. A [futures contract](/futures-contract/) on the S&P 500 index settles to the index's closing value on the last trading day. The buyer or seller walks away with only a cash payment, never touching any stock.

This mechanism is essential for instruments where physical delivery is impossible or impractical. You cannot take delivery of an index—it is a statistical composite, not a warehouse of goods. The same applies to [interest-rate swaps](/interest-rate-swap/), which reference notional principals and floating-rate benchmarks, not physical loans. Many equity [options](/option/) on broad indices are cash-settled for the same reason: the final payoff is the difference between the strike and the index level at expiry, paid in cash.

Cash settlement also streamlines trading. An oil trader can speculate on crude price moves without needing to arrange delivery infrastructure. A pension fund can hedge its S&P 500 exposure using index [futures](/futures-contract/) without owning a single stock until it chooses to.

## Practical Implications: The Holder's Burden

Physical settlement imposes real logistical and capital demands on the contract-holder. Buying a treasury bond [futures contract](/futures-contract/) and holding it to expiry means you become the owner of actual bonds; you must arrange storage (typically at a [custodian](/custodian/)) and pay financing costs. For commodity traders, physical settlement creates the possibility of a squeeze: if supply tightens near expiry, the cost to source and deliver the underlying can explode, forcing early exit or capitulation.

For retail equity [option](/option/) traders, physical settlement can be a trap. Many exchanges allow settlement by assignment: if your short call is exercised, your broker automatically sells 100 shares from your account (or you go short). If you were unprepared for this outcome, the resulting position may not fit your intended hedge or speculation.

Cash settlement, by contrast, eliminates these concerns. You settle only in currency. No delivery vehicles, no warehousing fees, no surprise short stock positions. This is why institutional investors often prefer cash-settled [futures](/futures-contract/) for hedging: the mechanics are cleaner and more predictable.

## Which Instruments Use Which Method?

The choice of settlement method reflects the nature of the underlying and market conventions.

**Typically physical settlement:**
- Commodity [futures](/futures-contract/) ([crude oil](/crude-oil/), [natural gas](/natural-gas/), [copper](/copper/), grains)
- Equity [options](/option/) (especially on single stocks)
- Currency [forwards](/forward-contract/) and traditional [currency](/currency-risk/) [futures](/futures-contract/)
- Treasury bond [futures](/futures-contract/) in some markets

**Typically cash settlement:**
- Index [futures](/futures-contract/) (S&P 500, Nasdaq, etc.)
- Equity-index [options](/option/)
- [Interest-rate swaps](/interest-rate-swap/) and interest-rate [futures](/futures-contract/)
- [Credit default swaps](/credit-default-swap/)
- Volatility [derivatives](/derivatives-hedging/) ([VIX](/vega/) futures and options)

Some instruments offer a choice. A eurodollar [futures contract](/futures-contract/), referencing a [LIBOR](/libor/)-like rate, settles in cash. But a Treasury bill [futures](/futures-contract/) can be physically delivered or cash-settled, depending on exchange rules and the specific contract month.

## Settlement Disruptions and Market Stress

When a commodity moves sharply, physical settlement can become a flashpoint. In early 2020, oil [futures](/futures-contract/) prices went negative partly because holders of May contracts faced imminent physical delivery, forcing urgent liquidation. Cash-settled index [futures](/futures-contract/) do not create such bottlenecks: only a cash payment is due, and the market can absorb it.

Similarly, in the silver market squeeze of early 2021, large traders holding [options](/option/) that would require physical delivery faced extraordinary costs to acquire the underlying metal. Cash-settled [options](/option/) avoid this scenario entirely.

## Expiration, Exercise, and Timing

The settlement method also affects how investors interact with expiration. An equity [call option](/call-option/) can be exercised early (American style) or only at expiry (European style). If physical settlement is required, early exercise may be worthwhile: you get the stock, you can hold it, and you capture dividends. With cash settlement, early exercise is moot—the [option](/option/) is worth only its intrinsic value at expiry anyway, so there is no advantage to closing early.

For [futures](/futures-contract/), the expiration mechanism is automatic and binary: the contract ends on the specified date, and settlement (physical or cash) occurs by exchange rule, not by trader choice. A holder who wants to avoid physical delivery must close the position before expiry or roll to a later contract month.

## See also

<div class="wiki-seealso">

### Closely related

- [Futures contract](/futures-contract/) — leveraged derivative committing both sides to buy or sell the underlying at a future date
- [Option](/option/) — contract granting the right, but not the obligation, to buy or sell at a set price
- [Forward contract](/forward-contract/) — privately negotiated agreement to exchange an asset at a future date
- [Interest-rate swap](/interest-rate-swap/) — exchange of fixed and floating interest-rate streams, typically cash-settled
- [Credit default swap](/credit-default-swap/) — insurance-like contract against bond default, usually cash-settled
- [Custodian](/custodian/) — financial institution holding assets on behalf of investors
- [Derivatives hedging](/derivatives-hedging/) — using futures, options, and swaps to reduce market risk

### Wider context

- [Crude oil](/crude-oil/) — energy commodity with futures settled physically
- [Natural gas](/natural-gas/) — volatile commodity often physically settled
- [Copper](/copper/) — industrial metal with major physical futures markets
- [S&P 500 index](/sp-500-index/) — benchmark stock index underlying cash-settled contracts
- [LIBOR](/libor/) — short-term interest-rate benchmark referenced in many derivatives

</div>
