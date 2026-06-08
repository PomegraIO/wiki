---
title: "Asset-or-Nothing Option"
description: "A digital option that delivers the underlying asset itself rather than a fixed cash amount when in-the-money."
keywords:
  - asset-or-nothing option
  - digital option
  - binary payoff
  - equity delivery
  - all-or-nothing option
  - option derivatives
image: /svg/derivatives.svg
---

*An **asset-or-nothing option** is a [digital option](/option/) that pays the underlying asset (e.g., one share of stock) if the option finishes [in-the-money](/in-the-money/), or nothing if it finishes out-of-the-money. Unlike a [cash-or-nothing option](/binary-cash-or-nothing/), the payoff is not a fixed dollar amount but the full market value of the asset at expiry.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Asset-or-Nothing Option — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives and options." />

<div class="wiki-infobox-caption">Binary delivery: the asset itself replaces the option contract at expiry.</div>

|   |   |
|---|---|
| **What it is** | A [digital option](/option/) delivering one unit of the underlying if in-the-money |
| **Also called** | Asset digital, equity-or-nothing, binary asset payoff |
| **Payoff structure** | Spot price at expiry if condition met, zero otherwise |
| **Strike sensitivity** | High [gamma](/gamma/) at strike, similar to [cash-or-nothing](/binary-cash-or-nothing/) |
| **Key advantage** | Payoff scales with market price; more natural for hedgers |
| **Primary use** | Converting directional bets into asset positions; hedging with asset delivery |
| **Liquidity** | Lower trading volume than vanilla [options](/option/); mostly bespoke |

</aside>

## The payoff: from option to possession

A vanilla [call option](/call-option/) on a stock struck at $50 allows the buyer to purchase one share at $50. If the stock rises to $70 at expiry, the buyer exercises, pays $50, and owns the stock. The gain is $20—the intrinsic value.

An asset-or-nothing [call](/call-option/) works differently. There is no exercise decision. If the stock finishes above $50, the buyer *automatically receives* one share of stock worth its spot price at expiry (say, $70). No additional payment; no choice to decline delivery. The buyer simply takes possession. If the stock finishes at $45, the buyer gets nothing.

This structure is mathematically simpler than it first appears. An asset-or-nothing [call](/call-option/) struck at $50 is economically equivalent to owning the stock *plus* a short [cash-or-nothing call](/binary-cash-or-nothing/) with the same strike and payout of $50. The combination: you own the asset (gaining its full upside), but if the underlying finishes above the strike, $50 is paid out, netting to delivery of the asset worth spot.

## Pricing via continuous payoff

The key insight is that an asset-or-nothing [option](/option/) has a payoff that's continuous at the strike, unlike a [cash-or-nothing option](/binary-cash-or-nothing/). An asset-or-nothing [call](/call-option/) struck at $50 pays:
- $0 if spot ≤ $50 at expiry
- Spot price if spot > $50 at expiry

As spot approaches $50 from below, the payoff approaches $0. As it crosses above, the payoff smoothly increases to spot value. There's no cliff, no infinite [gamma](/gamma/) spike—the derivative of payoff with respect to spot is well-behaved.

This continuity means asset-or-nothing [options](/option/) are easier to price and hedge than [cash-or-nothing options](/binary-cash-or-nothing/). The option value can be expressed in closed form: it's the present value of the expected spot price at expiry, conditional on finishing in-the-money. For a stock with known [volatility](/volatility-smile/), this reduces to a probability-weighted calculation using the [Black-Scholes model](/black-scholes-model/) framework.

The Greeks behave more smoothly too. [Delta](/delta/) is non-zero away from the strike (unlike [cash-or-nothing](/binary-cash-or-nothing/), where delta is near-zero until the strike boundary), and [gamma](/gamma/) is elevated but not singular. A dealer selling an asset-or-nothing [call](/call-option/) can hedge by holding a portion of the underlying; as the underlying price fluctuates, that hedge ratio adjusts gradually rather than violently.

## Asset-or-nothing calls and puts

An **asset-or-nothing [call](/call-option/)** struck at $50 delivers one share (or the notional asset) if the stock finishes above $50. The buyer is essentially making a bet that the stock will rally above the strike, and if correct, they take possession at no further cost. This is attractive when the buyer wants asset exposure conditional on a bullish move—they avoid paying the [strike price](/strike-price/) in cash; instead, they take the asset at its market price.

An **asset-or-nothing [put](/put-option/)** struck at $50 delivers one share if the stock finishes *below* $50. This is conceptually the inverse: a bearish directional bet that grants asset possession on a downward move. Asset-or-nothing puts are rarer in liquid trading but appear in structured products and hedges where the payoff logic is more intuitive inverted.

## Comparison to vanilla options and cash-or-nothing

Three options on the same stock, all struck at $50, all expiring in one month:
- **Vanilla [call](/call-option/)**: allows the buyer to purchase one share at $50 if exercised. If spot is $70, the buyer exercises, pays $50, nets $20 profit.
- **[Cash-or-nothing call](/binary-cash-or-nothing/)**: pays fixed $50 cash if spot finishes above $50. If spot is $70, buyer collects $50 regardless.
- **Asset-or-nothing [call](/call-option/)**: delivers one share if spot finishes above $50. If spot is $70, buyer takes one $70 share.

The vanilla [call](/call-option/) is the most flexible—it grants a choice (exercise or not) and can be understood as leveraged asset ownership. The [cash-or-nothing](/binary-cash-or-nothing/) is the most speculative—pure direction, capped payout. The asset-or-nothing sits between: it forces automatic delivery, but the payoff grows with spot, reducing the speculative leverage of a [cash-or-nothing](/binary-cash-or-nothing/) while avoiding the choice and commission friction of vanilla exercise.

## Practical use cases

**Equity compensation plans** sometimes use asset-or-nothing [options](/option/) as a hedging layer. A company granting stock to employees can structure a collar: grant an asset-or-nothing [call](/call-option/) struck near the vesting price (upside participation) paired with a short [cash-or-nothing put](/binary-cash-or-nothing/) (downside protection). The net effect: employees get the stock if it rallies, but are protected if it falls.

**Commodity hedging** uses asset-or-nothing structures when a producer's objective is to ensure delivery, not to cap price. A farmer might buy an asset-or-nothing [put](/put-option/) on corn struck at a floor price; if corn falls below that floor at harvest, the farmer takes possession of the physical commodity (or a futures contract equivalent), avoiding a cash shortfall while keeping upside exposure.

**Structured products** and exchange-traded notes embed asset-or-nothing [options](/option/) to define conditions under which underlying assets are delivered to investors. An autocallable note might deliver shares only if a trigger condition is met; that trigger is often modeled as an asset-or-nothing barrier option.

**Leverage and gearing** in leveraged ETF strategies sometimes use asset-or-nothing mechanics to control when investors take on additional asset exposure or when exposure is reset.

## Hedging and model risk

Asset-or-nothing [options](/option/) are typically found in bespoke or semi-custom markets, not in exchange-traded, standardized form. This means pricing is less transparent and [liquidity](/liquidity-risk/) is lower. A dealer pricing an asset-or-nothing [call](/call-option/) must make assumptions about [volatility](/volatility-smile/), interest rates, and dividend yields (for equity options). A 1% error in [implied volatility](/implied-volatility/) can translate to a 10–20% error in option value, especially near the strike and for near-dated expirations.

Model risk is significant. If the underlying is illiquid or has structural breaks (e.g., a merger or delisting), the payoff of delivering the asset becomes fraught: what is the asset worth, and can it even be delivered? For a dealer, this makes asset-or-nothing options riskier to warehouse than [cash-or-nothing options](/binary-cash-or-nothing/), where the payout is purely monetary.

## Asset-or-nothing and option replication

A clever insight: you can replicate an asset-or-nothing [call](/call-option/) by holding the asset and financing it with a [cash-or-nothing put](/binary-cash-or-nothing/). If you own one share (worth $70) and are short a [cash-or-nothing put](/binary-cash-or-nothing/) struck at $50 paying $50 cash (if the stock finishes below $50), then:
- If stock finishes above $50: you own the $70 share, no put payout due. Net = $70 share.
- If stock finishes below $50: you own the $70 share, but must pay $50 cash. Net = $70 share minus $50 cash.

This replication demonstrates that the pricing of asset-or-nothing [options](/option/) is not independent; it's locked to vanilla and [cash-or-nothing](/binary-cash-or-nothing/) pricing via no-arbitrage relationships.

## See also

<div class="wiki-seealso">

### Closely related

- [Cash-or-nothing option](/binary-cash-or-nothing/) — pays fixed cash, not the asset
- [Digital option](/option/) — the parent class of binary-payoff structures
- [Option](/option/) — the fundamental derivative contract
- [Binary option](/option/) — casual synonym, though regulated differently
- [In-the-money](/in-the-money/) — the condition triggering asset delivery
- [Strike price](/strike-price/) — the barrier between delivery and zero payoff

### Wider context

- [Black-Scholes model](/black-scholes-model/) — used to price asset-or-nothing [options](/option/)
- [Implied volatility](/implied-volatility/) — critical input for pricing near the strike
- [Delta](/delta/) — smoother gradient than in [cash-or-nothing](/binary-cash-or-nothing/) due to continuous payoff
- [Gamma](/gamma/) — elevated at strike but not singular, unlike [cash-or-nothing](/binary-cash-or-nothing/)

</div>
