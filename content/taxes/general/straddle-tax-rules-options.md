---
title: "Straddle Tax Rules for Options and Futures"
description: "How IRS straddle rules defer losses on offsetting options and futures positions until the offsetting gain is closed, preventing artificial loss harvesting."
keywords:
  - straddle tax rules
  - straddle tax rules options
  - offsetting positions tax
  - wash sale alternatives
  - tax loss deferral
  - section 1092
---

*The IRS **straddle tax rules** prevent investors from locking in a loss on one side of an offsetting [options](/option/) or [futures](/futures-contract/) position while retaining economic upside on the other. Under Section 1092 of the tax code, when you close a leg of a straddle at a loss, the loss is deferred until you unwind the offsetting position. This rule exists to block a specific tax-planning maneuver: harvesting losses in December to reduce current-year taxes while maintaining the same economic exposure into the new year.*

<div class="wiki-hatnote">

This article covers the mechanics of straddle loss deferral. For the broader strategy of recognizing losses to offset gains, see [tax loss harvesting](/tax-loss-harvesting/). For the related ban on losses from offsetting trades, see [wash sale](/wash-sale/).

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Straddle Tax Rules — key facts</div>

<img src="/svg/taxes.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">A rule that prevents paper losses from masking economic profit.</div>

|   |   |
|---|---|
| **Rule name** | Section 1092 offsetting positions rule (straddle rules) |
| **What triggers it** | Closing a [call](/call-option/) or [put](/put-option/) at a loss while holding the opposite leg (or closing a futures short at a loss while holding a long futures contract) |
| **Loss treatment** | Loss is deferred; carried forward and netted against gains when the offsetting position is closed |
| **When loss is recognized** | When the remaining leg is closed at a [gain](/capital-gains-tax-investor/), the deferred loss is recognized simultaneously |
| **Types of positions** | Applies to [options](/option/), [futures](/futures-contract/), currency positions, and certain hedges |
| **Exemptions** | Certain hedges, some identified positions, and [qualified covered calls](/covered-call/) may be exempt |
| **Reporting** | Form 8949 and Schedule D; deferred losses tracked until offset leg closes |

</aside>

## The Problem the Rule Solves

Imagine an investor in late December who is sitting on a large [gain](/capital-gains-tax-investor/) from equity holdings. She wants to lock in the profit but fears the market will rally further in the new year. She could sell the stock, but that forces a decision in the new year about how to reinvest. Instead, she considers a tax maneuver:

1. Buy a [put option](/put-option/) on the stock, locking in a minimum price (the put's [strike price](/strike-price/)).
2. Sell a [call option](/call-option/) on the same stock at a higher strike, capping her upside but collecting a premium.
3. If the stock falls sharply, the put is in-the-money and loses money, while the call expires worthless and generates a loss.
4. She recognizes the loss on the call, reducing her current-year taxes by thousands.
5. In January, she closes the put at a profit and continues holding the stock.

In this scenario, she has harvested a loss in year one while retaining the economic benefit of the put protection and the stock ownership in year two. She has not sacrificed the potential for gain; she has merely deferred it to a higher tax bracket or lower-income year. The straddle rules are designed to prevent this.

## What Is a Straddle?

A straddle, in tax terms, is a set of offsetting positions—typically a long [call](/call-option/) and a long [put](/put-option/) on the same underlying asset at the same strike price and expiration (a "classic" straddle), or any pair of positions that are economically opposite. The key feature is that they offset each other: if one position gains, the other loses (approximately) by the same amount.

Common straddle structures include:

- **Long call + long put** at the same strike: the investor profits if the stock moves significantly in either direction; if it stays flat, both expire worthless.
- **Long call + short call** (collar): the investor owns the stock, buys protection (long put), and sells a call to finance it. This locks in a range of outcomes.
- **Long futures + short futures**: buying a contract month while selling the next month, betting on price convergence.
- **Currency hedge**: holding a foreign investment while hedging the currency risk with a forward contract.

The unifying feature: the positions are designed such that losses on one are (nearly) offset by gains on the other.

## How the Deferral Works

When an investor closes one leg of a straddle at a loss, the IRS defers the loss. The loss does not disappear; it is held in suspension. When the investor later closes the offsetting leg, the deferred loss is recognized at that time.

**Example:**

- February: Buy a call on stock XYZ with a $100 strike (pay $5 premium, cost = $500).
- February: Buy a put on XYZ with a $100 strike (pay $4 premium, cost = $400). Total investment = $900.
- Stock rallies to $110 by May.
- May: Sell the put. The put is out-of-the-money and worthless; you recognize a $400 loss on the put.
- Under the straddle rule, the $400 loss is deferred. It does not reduce your May income.
- July: Stock falls back to $95. Sell the call. The call is out-of-the-money and worthless; you recognize a $500 loss on the call.
- The $400 deferred loss from the put is now recognized, along with the $500 loss on the call, for a total $900 loss in July.

The net economic outcome is the same (you paid $900 and got nothing back), but the loss is pushed to July rather than recognized in May.

## When the Rule Applies and Exemptions

The straddle rule applies automatically to most [options](/option/) and [futures](/futures-contract/) positions. However, some positions are exempt:

**Qualified covered calls**: If you hold 100 shares of stock and sell an out-of-the-money call, the call may be treated as "qualified" and the loss deferral rule does not apply to the stock-call pairing. The call is seen as a way to finance the stock holding, not a speculative straddle.

**Identified positions**: A taxpayer can elect to identify a position as a hedge of a specific business purpose (e.g., a farmer hedging crop prices). If properly documented at inception, the hedging transaction may be exempted from the straddle rules.

**Currency hedges**: Some foreign currency positions used to hedge business operations (not speculation) may qualify for relief.

**Mixed straddles**: A straddle mixing [Section 1256 contracts](/straddle-tax-rules-options/) (futures, certain options) with non-Section 1256 property may be subject to modified rules.

For the vast majority of retail options traders, the rule applies without exception.

## Section 1256 Contracts and Mark-to-Market

Futures contracts and certain index options are classified as "Section 1256 contracts." These contracts are subject to special rules: they are marked to market annually (gains and losses are calculated as if the position were closed on December 31), and 60% of gains are treated as long-term [capital gains](/capital-gains-tax-investor/) (taxed at preferential rates) while 40% are short-term. This is attractive.

However, if a Section 1256 contract is part of a straddle, the mark-to-market and 60/40 treatment are suspended in favor of the straddle deferral rule. The straddle rule takes precedence, ensuring that losses cannot be harvested to reduce taxes while deferring mark-to-market gains.

## Hedging Anti-Straddle Arguments

Some traders argue that their offsetting positions are not tax-motivated straddles but genuine hedges of business operations or prior positions. To qualify for an exemption, the taxpayer must identify the hedge at inception—before or contemporaneously with opening the position. After-the-fact identification is not allowed. For example, if you own a stock and later buy a protective put to hedge downside, the put-stock pair may be treated as a hedge, and the straddle rules may not apply to both legs equally.

However, the burden of proof is on the taxpayer. The IRS is skeptical of retroactive hedge claims, particularly when the timing is suspiciously close to year-end.

## Reporting Straddle Losses

When you close a leg of a straddle at a loss, you must report the transaction on Form 8949 (Sales of Capital Assets) and Schedule D (Capital Gains and Losses). The form allows you to designate a position as part of a straddle or as subject to Section 1092 deferral.

If you fail to disclose the straddle relationship, the IRS may disallow the loss entirely or impose penalties. Proper documentation—dates of entry, strike prices, offsetting pairs, and the order in which legs are closed—is essential.

## Why This Matters for Tax Planning

For investors who trade options or futures regularly, the straddle rule significantly constrains tax-loss harvesting strategies. You cannot simply close a losing side of a position in December to harvest the loss and then close the winning side in January (or later) at a higher gain. The loss will be deferred and netted against the later gain anyway, so the tax benefit is postponed.

Instead, successful tax planning typically involves closing both legs in the same tax year (to allow net losses to offset other income) or spacing the closures across multiple years in a way that minimizes total tax across years. Some traders redesign their positions to avoid straddle triggers altogether—for instance, by shifting from options to outright stock ownership or by unwinding positions entirely and re-entering with unrelated positions.

## See also

<div class="wiki-seealso">

### Closely related

- [Tax loss harvesting](/tax-loss-harvesting/) — the broader strategy of recognizing losses to offset gains
- [Wash sale](/wash-sale/) — a related rule that prevents deductions for loss sales of substantially identical securities
- [Section 179 deduction](/section-179-deduction/) — another tax rule that defers benefits under certain conditions
- [Call option](/call-option/) — one leg of a straddle
- [Put option](/put-option/) — the other leg
- [Futures contract](/futures-contract/) — commonly part of straddles
- [Capital gains tax investor](/capital-gains-tax-investor/) — the rates affected by straddle timing
- [Form 8949](/form-8949/) — where straddle losses are reported

### Wider context

- [Internal Revenue Service](/taxes/general/) — creator and enforcer of Section 1092
- [Option](/option/) — the foundational derivative contract
- [Derivatives hedging](/derivatives-hedging/) — the economic purpose of many straddles
- [Tax bracket investor](/tax-bracket-investor/) — the context in which straddle timing matters
- [Counterparty risk](/counterparty-risk/) — a risk of offsetting positions with multiple counterparties

</div>
