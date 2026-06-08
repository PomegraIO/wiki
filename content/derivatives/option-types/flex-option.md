---
title: "FLEX Option"
description: "An exchange-listed option contract allowing customization of strike, expiration, settlement method, and exercise style beyond standard terms."
keywords:
  - FLEX option
  - flexible option
  - customized strike
  - exchange-traded
  - OTC alternative
  - cboe
image: "/svg/derivatives.svg"
---

*A **FLEX option** (Flexible Exchange option) is an [option](/option/) listed and cleared by a major exchange—typically the CBOE in the United States—that permits non-standard terms including bespoke [strike prices](/strike-price/), [expiration dates](/expiration-date/), [exercise styles](/option/), and settlement methods. FLEX options blend the exchange safety of [listed options](/option/) with the customizability of [over-the-counter](/over-the-counter-market/) contracts.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">FLEX Option — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives." />

<div class="wiki-infobox-caption">Exchange-traded optionality with bespoke strike and expiry terms.</div>

|   |   |
|---|---|
| **What it is** | Customized [option](/option/) contract listed on an exchange |
| **Underlying** | Equities, indices, currencies, commodities |
| **Customizable terms** | Strike, expiry, exercise style, settlement |
| **Exchange** | Primarily CBOE; limited availability elsewhere |
| **Clearing** | Central counterparty (CBOE Clearing Corporation) |
| **Minimum contract size** | Typically 100 units or $100,000 notional |
| **Advantage over OTC** | Transparent pricing, lower [counterparty risk](/counterparty-risk/), regulatory oversight |

</aside>

## The middle ground between vanilla and OTC

Standard exchange-listed [options](/option/) come in fixed strikes and expirations, often at monthly or quarterly intervals. An investor seeking a call at strike 147.50 expiring in 73 days must either settle for the nearest available strike and date or go [over-the-counter](/over-the-counter-market/). Over-the-counter options offer precision but carry [counterparty risk](/counterparty-risk/): the dealer is your counterparty, and if the dealer fails, your trade is at risk.

FLEX options occupy the middle. You specify the exact strike, expiry, and style you want—a call at 147.50 expiring in 73 days, American-style exercise—and the exchange matches you with another trader or market-maker. The CBOE then clears the trade through a central counterparty, eliminating counterparty default risk. You get customization without the credit exposure.

## Typical users and applications

Asset managers use FLEX options to hedge customized portfolio risks. A fund holding a $50 million position in a large-cap index may need protection at a non-standard price level or over an unusual time horizon. Buying a FLEX put with a bespoke strike and expiry is faster and cheaper than negotiating an OTC contract.

Corporate treasurers deploy FLEX options to hedge [currency](/currency-risk/) or commodity exposures with real-world cash-flow dates. A U.S. exporter expecting a payment in Swiss francs in 98 days can buy a FLEX put option at a strike reflecting their break-even rate, expiring on the payment date. Standard options (monthly) force a choice: over- or under-hedge.

Volatility arbitrageurs and options desks use FLEX options to trade [implied volatility](/implied-volatility/) at strikes where listed options have wide [bid-ask spreads](/bid-ask-spread/) or sparse liquidity. FLEX options on major indices (SPX, VIX) are particularly liquid for this purpose.

## How FLEX options are priced and traded

Unlike standard options, which display a live market with market-makers posting continuous [bids and offers](/bid-ask-spread/), FLEX options operate on a request-for-quote (RFQ) mechanism. You submit your desired terms, and market-makers respond with a [premium](/option-premium/). You then accept or reject the quote. This is slower than clicking a buy button on a vanilla option but much faster and more transparent than phoning a dealer for an OTC quote.

Pricing follows [Black-Scholes](/black-scholes-model/) or similar models, adjusted for the custom strike and expiry. Because FLEX options are exchange-listed and cleared, [implied volatility](/implied-volatility/) is observable and consistent across participants. A FLEX call at strike 150 three months out will trade at prices that bear a logical relationship to nearby vanilla options and other FLEX quotes—absent arbitrage opportunities.

The exchange publishes [implied volatility](/implied-volatility/) surfaces, making price discovery more transparent than OTC markets where each dealer quotes independently.

## Mechanics of exercise and settlement

FLEX options use the same settlement logic as standard listed options. American-style FLEX options allow exercise at any point up to [expiration](/expiration-date/). European-style exercise only on expiration. Cash settlement and physical delivery are both available depending on the underlying and exchange rules.

For index FLEX options (e.g., on the S&P 500 or Russell 2000), settlement is cash-only, reflecting that you cannot physically hold an index. For equity FLEX options, settlement can be physical (shares delivered) or cash (difference between spot and strike).

This flexibility extends to exotics: some FLEX options allow [settlement](/option/) in a currency other than USD, useful for cross-border hedges. A multinational corporation can strike a call in euros and settle in dollars at a fixed fx conversion, eliminating separate currency risk.

## Constraints and practical limits

Minimum contract sizes are the main barrier. Most FLEX options require notional exposure of at least $100,000 or 100 units of the underlying. A retail trader wanting a small, bespoke hedge will find this prohibitive. Institutional investors have no issue.

Liquidity is second. FLEX options on major underlyings (large-cap stocks, broad indices) are actively traded. FLEX options on small-cap stocks or obscure indices are sparse. You may wait hours or days for a quote and face wide spreads if dealers view your request as illiquid.

A third friction is minimum holding periods or exercise restrictions. Some FLEX options lock in pricing for a minimum period (e.g., 10 minutes after your RFQ is accepted) to prevent quote stuffing and give market-makers breathing room.

## FLEX options versus OTC options

The key difference is counterparty and infrastructure. An OTC option is a private contract between you and a dealer; if the dealer fails, you are an unsecured creditor. A FLEX option is cleared by the exchange, so the exchange's clearinghouse is your counterparty, and clearing funds backstop your protection.

OTC options offer unlimited customization: any exotic feature, any payoff structure, any settlement currency. FLEX options are flexibly customizable but within bounds set by the exchange.

FLEX options trade at published [implied volatility](/implied-volatility/) surfaces; OTC dealers quote independently. FLEX options are transparent; OTC quotes are opaque.

For plain-vanilla-ish customization—shifting a strike or expiry—FLEX is cheaper and safer. For exotic payoffs (gap calls, variance swaps, autocallables), you need OTC.

## See also

<div class="wiki-seealso">

### Closely related

- [Option](/option/) — foundational mechanics of calls, puts, exercise, and settlement
- [Strike Price](/strike-price/) — the reference price for option payoff
- [Expiration Date](/expiration-date/) — when the option right expires
- [Option Premium](/option-premium/) — price paid for the option contract
- [Implied Volatility](/implied-volatility/) — market expectation of future volatility
- [Black-Scholes Model](/black-scholes-model/) — mathematical pricing framework
- [Gap Option](/gap-option/) — non-standard exotic option structure

### Wider context

- [Over-the-Counter Market](/over-the-counter-market/) — bilateral dealer market for custom derivatives
- [Bid-Ask Spread](/bid-ask-spread/) — difference between buy and sell prices
- [Counterparty Risk](/counterparty-risk/) — risk of dealer failure
- [Volatility Smile](/volatility-smile/) — non-flat implied volatility curve
- [Futures Contract](/futures-contract/) — exchange-traded leveraged exposure

</div>
