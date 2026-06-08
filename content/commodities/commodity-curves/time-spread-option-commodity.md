---
title: "Time Spread Option (Commodities)"
description: "An option on the calendar spread between two futures expirations, allowing traders to profit from or hedge curve-shape changes."
keywords:
  - spread option
  - calendar spread option
  - commodity curve volatility
  - contango bet
  - curve structure
image: /svg/commodities.svg
---

*A **time spread option** is an [option](/option/) on the price difference (or "spread") between two [futures](/futures-contract/) contracts at different delivery dates. Rather than betting on the absolute price of oil or copper, a spread option bets on whether the curve will steepen, flatten, invert, or shift its shape. It is a direct way to trade [contango](/contango/) vs. [backwardation](/backwardation/) or to hedge the [risk](/currency-risk/) that your [hedge ratio](/delta/) between two maturities becomes unprofitable.*

## The spread as an underlying

A standard commodity option has one futures contract as the underlying—the [strike price](/strike-price/) and [expiration date](/expiration-date/) are fixed to that single maturity. A time spread option uses the *spread itself* as the underlying. If you own a call option on the spread between, say, December and June crude, you own the right to receive the difference (December price minus June price) if it exceeds your strike at expiration.

The spread value changes for two reasons. First, both legs drift with market prices. Second, the *curve shape* changes—the months converge, diverge, or invert relative to each other. A trader who believes the curve will steepen can buy a spread call and profit if the near month strengthens relative to the far month. A trader who thinks contango will collapse can sell the call or buy a spread put.

## Why traders use them

Time spread options are essential tools in three scenarios.

**Hedging curve risk.** A producer of a commodity often hedges against price drops by buying [calls](/call-option/) on future production. But if storage costs shift or seasonal demand changes, the [curve](/commodity-forward-curve-bootstrapping/) flattens and the hedge's effectiveness against inventory moves degrades. A spread option protects against this curve-shape shift separately from the outright price move.

**Monetizing [curve kinks](/commodity-curve-kink/).** When a sharp bend appears in the forward curve—signalling a seasonal storage transition or supply shock at one maturity—a nimble trader can buy a spread call or put positioned to capture the kink if it moves. As fundamentals evolve, kinks travel. A spread option on the exact spread where the kink sits can be enormously profitable.

**Relative value and [curve fitting](/commodity-forward-curve-bootstrapping/).** Trading desks build models of "fair" curve shapes based on storage costs, interest rates, and convenience yields. When the actual curve deviates from the model, they trade spreads—and spread options—to bet that the curve will revert or that the mispricing will widen further. A spread option amplifies that bet, since [leverage](/leverage-ratio-forex/) comes from [optionality](/time-decay-theta/).

## Pricing: the [volatility smile](/volatility-smile/) of spreads

A time spread option is priced using variants of the [Black-Scholes model](/black-scholes-model/), adapted for two underlying futures legs. The key challenge is capturing *spread volatility*—how much the difference between two maturities typically moves.

Spread volatility is typically *lower* than the average volatility of the individual legs. This is because the two maturities often move together (if crude rallies, both December and June rally). The spread is the *difference*, so common movements cancel out. Only the relative change—the curve shift—drives spread volatility. This makes spread options cheaper than you might naïvely expect from simply averaging the [implied volatilities](/implied-volatility/) of the two legs.

However, spread volatility is not constant. When a [commodity curve kink](/commodity-curve-kink/) is nearby, volatility often spikes, because traders anticipate that the kink might move sharply or that the curve shape might transform. Some spread options are expensive near seasonal turning points for this reason.

## Strike and intrinsic value

A spread option's [strike price](/strike-price/) is denominated in the units of the spread. For crude oil, a December–June spread option might have a strike of $1.50 per barrel. If the spread at expiration is $2.00, a call is in-the-money by $0.50, and the holder receives that amount.

[Intrinsic value](/intrinsic-value/) is the spread value minus the strike (for a call) or strike minus spread (for a put). Unlike a vanilla option, a spread's intrinsic value can be negative in an informative way—it tells you by how much the curve is inverted relative to your bet.

## [Greeks](/delta/) for spread options

**Delta** behaves differently for a spread option. A time spread option typically has a lower [delta](/delta/) than a comparable vanilla option because the two legs partly offset. Buying a December call and selling a June call (the spread position itself) has a net delta somewhere between the two individual deltas, not the sum. This makes spread options useful for traders who want directional exposure to the curve's *shape* without taking as much [market risk](/market-risk/).

**[Gamma](/gamma/)** and **[theta](/theta/)** follow similar logic. Spread options gamma is lower (curves are less sharp in the spread space than in absolute price space), and theta decay is more muted. This can be an advantage if you are purely betting on a curve shift and want to avoid rapid time decay eating your premium.

**[Vega](/vega/)** measures sensitivity to changes in spread volatility. If you think the curve is about to become less volatile—perhaps the seasonal kink is flattening and uncertainty is falling—you can sell spread options to capture that collapse in [volatility](/currency-volatility/).

## Calendar spreads vs. spread options

A related but simpler instrument is the *calendar spread* itself—a direct position (buy near month, sell far month) with no optionality. Calendar spreads are levered bets on curve shape and are extremely cheap (no premium to pay), but they can incur losses if the curve moves against you. Spread options buy you the right to abandon the position if you are wrong—you pay [option premium](/option-premium/) for that choice. For hedgers and risk-conscious traders, the premium is often worth the downside protection.

## Liquidity and execution

Time spread options are most liquid in the largest commodity markets (crude oil, natural gas, precious metals). Agricultural and soft-commodity spread options exist but may have wider [bid-ask spreads](/bid-ask-spread/) and require dealer negotiation. Unlike vanilla options, which trade on exchanges, many spread options are [over-the-counter](/over-the-counter-market/) (OTC) structures quoted by investment banks or specialized brokers.

## See also

<div class="wiki-seealso">

### Closely related

- [Commodity Curve Kink](/commodity-curve-kink/) — sharp bends in the forward curve where spread options are often positioned
- [Contango](/contango/) — sustained upward curve slope, a state many spread bets capture
- [Backwardation](/backwardation/) — inverted curve, the opposite of contango
- [Implied Storage Rate](/implied-storage-rate/) — the storage cost locked into a contango curve
- [Forward Curve Bootstrapping (Commodities)](/commodity-forward-curve-bootstrapping/) — techniques to extract a continuous curve from discrete futures
- [Futures Contract](/futures-contract/) — the underlying delivery contracts at each maturity

### Wider context

- [Option](/option/) — general option mechanics and definitions
- [Option Premium](/option-premium/) — the price paid for an option's embedded right
- [Volatility Smile](/volatility-smile/) — distortions in implied volatility across strikes, analogous to spread volatility effects
- [Call Option](/call-option/) — the right to buy at a fixed strike
- [Put Option](/put-option/) — the right to sell at a fixed strike
- [Over-the-Counter Market](/over-the-counter-market/) — where bespoke options are traded

</div>
