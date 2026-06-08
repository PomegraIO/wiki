---
title: "Rainbow Option"
description: "An exotic option whose payoff depends on the best or worst performing of multiple underlying assets."
keywords:
  - rainbow option
  - exotic option
  - multiple underlyings
  - option payoff
  - derivatives
  - portfolio hedging
image: "/svg/derivatives.svg"
---

*A **rainbow option** is an [exotic option](/option/) whose payoff depends on the relative performance of multiple underlying assets. Unlike a standard [option](/option/) tied to a single stock or index, a rainbow option's value hinges on the best or worst performer among a basket of assets—hence "rainbow," capturing all hues at once.*

<div class="wiki-hatnote">

For basic option mechanics, see [Option](/option/); for more exotic variants, see [Chooser Option](/chooser-option/).

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Rainbow Option — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives and structured instruments." />

<div class="wiki-infobox-caption">Payoff tied to multiple assets in a single contract.</div>

|   |   |
|---|---|
| **What it is** | [Option](/option/) whose payoff depends on the best-performing, worst-performing, or average-performing asset in a basket |
| **Key variants** | Best-of call, worst-of call, best-of put, worst-of put |
| **Typical underlyings** | Equities, currencies, commodities, equity indices (usually 2–10 assets) |
| **Payoff structure** | Max(S₁, S₂, …, Sₙ) or Min(S₁, S₂, …, Sₙ) relative to [strike price](/strike-price/) |
| **Pricing challenge** | Requires modelling correlation between assets; [Monte Carlo simulation](/discounted-cash-flow-valuation/) common |
| **Cost advantage** | Often cheaper than buying separate [options](/option/) on each asset |
| **Primary users** | Portfolio managers, [hedge funds](/hedge-fund/), structured product issuers |

</aside>

## Basic structure and payoff

The simplest rainbow option is a **best-of call**. Suppose you hold a basket of three stocks: Tech, Healthcare, and Energy. A best-of call with a [strike price](/strike-price/) of $100 entitles you to buy whichever asset appreciates most, at $100. If Tech rallies to $130, Healthcare stagnates at $105, and Energy falls to $85, you exercise on Tech and pocket the $30 payoff.

The mathematical expression:

Payoff = Max(S₁ – K, S₂ – K, …, Sₙ – K, 0)

where S₁, S₂, etc. are the final prices of each underlying, K is the [strike price](/strike-price/), and you take the maximum across all assets (or zero if all underperform).

A **worst-of call** inverts the logic: you buy the right to purchase whichever asset performed worst. Its payoff is Max(Min(S₁, S₂, …, Sₙ) – K, 0). This is cheaper than a best-of call because the worst performer usually yields less value.

**Put versions** flip the direction. A best-of put gives you the right to sell the best performer at a fixed [strike](/strike-price/), capturing if the strongest asset declines. A worst-of put lets you sell the laggard, gaining if the weakest asset falls further.

## Why rainbow options matter

Creating a portfolio to capture the best of multiple assets via separate [options](/option/) is expensive and complex. You'd need to buy a [call option](/call-option/) on each stock. Rainbow options achieve similar exposure at lower cost. The issuer can quote a single [premium](/option-premium/), hedging the multi-asset correlation internally.

For hedgers, rainbow options provide tailored insurance. A European fund holding USD, GBP, and JPY liabilities might buy a worst-of put on those three currencies, insuring its largest forex loss—rather than hedging each currency separately. A [private equity](/private-equity-fund/) firm financing acquisitions across multiple geographies might use a best-of call to profit from the best-performing acquisition target without committing upfront.

The cost advantage stems from correlation. If the three stocks in your basket tend to move together (high correlation), buying three separate [call options](/call-option/) is wasteful; you're paying for three independent insurance policies when outcomes are linked. A single rainbow [option](/option/) pools that risk.

## Pricing and correlation sensitivity

Rainbow [options](/option/) are priced using numerical simulation, most commonly [Monte Carlo methods](/discounted-cash-flow-valuation/). You model the joint distribution of the underlying assets—how they move together, their volatilities, their [drift](/discounted-cash-flow-valuation/)—then simulate thousands of price paths. For each path, you calculate the payoff, then discount the average payoff back to present value.

Correlation is everything. If the underlyings are independent, the worst performer tends to underperform more, raising the worst-of [option](/option/) value. If they're perfectly correlated, all underlyings move as one, and best-of and worst-of [options](/option/) behave like standard [options](/option/) on a single asset. Issuers of rainbow [options](/option/) are betting on correlation assumptions—if actual correlation drops and assets diverge, a best-of call becomes more valuable (the best one rises farther), and the issuer loses.

## Practical deployment

**Structured products** commonly embed rainbow [options](/option/). A note might offer: "Receive a 6% return, plus 80% of the gains of the best-performing of five indices, capped at 20%." The bank buys a capped best-of call and funds the 6% coupon from the note's premium.

**Portfolio managers** use worst-of puts as portfolio insurance for multi-asset strategies. Rather than hedging each position separately, a manager holds a worst-of put on the bottom-performing asset, saving cost.

**Hedge funds** in relative value or statistical arbitrage strategies exploit mispricings in rainbow [option](/option/) correlation assumptions. If the market prices the [option](/option/) assuming 60% correlation but the manager believes true correlation is 40%, they can profit by trading the [option](/option/) against hedges in the underlying assets.

## Valuation pitfalls

Because rainbow [options](/option/) depend on correlation, small model changes yield large price swings. Two traders using different [Monte Carlo](/discounted-cash-flow-valuation/) assumptions—slightly different correlation matrices or drift estimates—can quote wildly different [premiums](/option-premium/). This illiquidity makes rainbow [options](/option/) less liquid than vanilla [options](/option/) on single assets.

The worst-of put is particularly treacherous. In a crisis, all assets may fall sharply—and the worst performer falls hardest. The worst-of put is supposed to protect you, but its payoff is determined by the asset that's been hit most, which may be where your protection is thinnest. In 2008, many investors holding worst-of [options](/option/) learned this painful lesson.

**Correlation breakdown** is another trap. During calm markets, correlations are stable and models reliable. In crises, correlations spike toward 1—everything falls together. The diversification [benefit](/hedge-fund/) of a rainbow [option](/option/) on multiple assets evaporates. A best-of call that seemed to cover your risks becomes worthless when all underlyings collapse in tandem.

## See also

<div class="wiki-seealso">

### Closely related

- [Option](/option/) — the fundamental derivative contract; rainbow is an exotic variant
- [Strike Price](/strike-price/) — the price at which a rainbow [option](/option/) can be exercised
- [Call Option](/call-option/) — the right to buy; best-of and worst-of [calls](/call-option/) are rainbow variants
- [Put Option](/put-option/) — the right to sell; best-of and worst-of [puts](/put-option/) are rainbow variants
- [Chooser Option](/chooser-option/) — another exotic [option](/option/) with exotic appeal
- [Option Premium](/option-premium/) — the cost of buying a rainbow [option](/option/)
- [Exotic Option](/option/) — the broader category including rainbow [options](/option/)
- [Hedge Fund](/hedge-fund/) — investor type that deploys rainbow [options](/option/) for relative value trading

### Wider context

- [Discounted Cash Flow Valuation](/discounted-cash-flow-valuation/) — Monte Carlo simulation used for pricing
- [Correlation](/diversification/) — the hidden driver of rainbow [option](/option/) value
- [Portfolio Hedging](/protective-put/) — why investors buy rainbow [options](/option/)
- [Private Equity Fund](/private-equity-fund/) — sophisticated user of exotic [options](/option/)
- [Volatility Smile](/volatility-smile/) — pricing anomaly that affects rainbow [options](/option/) too

</div>
