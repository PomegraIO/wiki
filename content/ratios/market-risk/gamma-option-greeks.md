---
title: "Gamma (Option Greeks)"
description: "The rate of change of delta with respect to the underlying asset price, measuring curvature of option value."
keywords:
  - gamma
  - option greeks
  - delta change
  - option convexity
  - gamma-option-greeks
---

*A **gamma** (one of the [option Greeks](/wiki/options-greeks/)) measures how much [delta](/wiki/delta-option-greeks/) changes when the underlying asset price moves by one unit. High gamma means delta is sensitive to price shifts; low gamma means delta is stable. Gamma is the hedge fund trader's obsession and the retail option buyer's blind spot.*

<aside class="wiki-infobox">

| Aspect | Detail |
|--------|--------|
| **Symbol** | Γ (Gamma) |
| **Definition** | Rate of change of delta |
| **Units** | Delta change per 1-unit asset price move |
| **Sign** | Always positive for long options |
| **Peak Gamma** | At-the-money options, near expiration |

</aside>

## Why delta changes: gamma explained visually

[Delta](/wiki/delta-option-greeks/) is the slope of the option value curve relative to the underlying price. [Gamma](/wiki/gamma-option-greeks/) is the curvature of that curve—the second derivative. Imagine a call option's value graphed against the stock price. When the stock is deeply out-of-the-money, the curve is nearly flat (delta ≈ 0, gamma ≈ 0). When the stock is deeply in-the-money, the curve is nearly a 45-degree line (delta ≈ 1, gamma ≈ 0). But right at the strike, the curve is steepest and most curved—delta is 0.5, and small price moves cause large delta changes. That curvature is gamma.

Here's the trader's version: if you buy a $100 call struck at $100 (at-the-money) on a $100 stock, your delta is roughly 0.5 (you win 50 cents for every $1 move up). If the stock rises to $101, your delta jumps to, say, 0.6 (you win 60 cents per $1 move). The delta changed by 0.1 for a $1 move—that is gamma of 0.1. The deeper into the money your option swings, the more delta approaches 1 and gamma falls; the more out-of-the-money it swings, delta approaches 0 and gamma falls. Gamma is highest right at the strike.

## The convexity trade: gamma as optionality value

Option traders obsess over gamma because it is the value of optionality itself. When you buy an option, you are betting that the underlying will move—but delta alone does not capture that. A [call option](/wiki/call-option/) with delta 0.5 on a $100 stock benefits from a $5 move up *far more* than you lose from a $5 move down (you make $2.50 from the move up; you lose $2.50 in delta but recover via [theta](/wiki/theta-option-greeks/) decay and [convexity](/wiki/gamma-convexity/)). That asymmetry is gamma.

Suppose a stock is trading $100, and you buy a $100 call expiring in 3 months. Stock rises to $105: your call is now worth roughly $5 + intrinsic upside, earning more than the 0.5 delta alone would predict. Stock falls to $95: your call is worth roughly 0 + some time value, losing only 0.5 × $5 = $2.50 to delta, not $5. The excess gain on the upside minus the cushioned loss on the downside equals the [gamma](/wiki/gamma-option-greeks/) P&L. This is why [convexity](/wiki/positive-convexity/) is so valuable: you own a free bet on volatility.

## Gamma and hedging: the rebalancing trap

A portfolio manager delta-hedging a position must rebalance as gamma changes delta. Suppose you own 100 call options (delta 0.5 each, total delta 50) and you sell 50 shares to hedge. If the stock rises to $101, delta jumps to 0.6, so your calls now have delta 60. You are long delta 60 and short 50 shares—you are unhedged by 10 shares. You must sell 10 more shares to re-hedge. If the stock falls to $99, delta falls to 0.4, total call delta is 40, and you are short 50 shares against delta-40 calls. You must buy back 10 shares.

This dynamic—selling into rallies and buying into declines—locks in losses on every rebalance. High gamma means frequent rebalancing and higher hedging costs. Low gamma means delta is stable and hedges hold longer. This is why [negative convexity](/wiki/negative-convexity/) is so toxic for mortgage holders: as rates fall and prepayment risk rises, duration expands, and hedging costs soar. Why gamma matters for traders: trading vol profitably depends on buying gamma (low vol regimes) and selling gamma (high vol regimes), then betting vol reverts.

## Gamma's sensitivity: time decay and moneyness

Gamma is highest for at-the-money options with short time to expiration. An ATM call with 1 day to expiration has extreme gamma—a $0.50 move changes delta dramatically. An ATM call with 6 months to expiration has low gamma—delta changes slowly across price ranges. This is why [theta](/wiki/theta-option-greeks/) and gamma are frenemies: long options have positive theta when you are short (you decay into profit), but negative theta when you are long (you bleed value). The exception is at-the-money, short-expiration options, where high gamma compensates for high theta decay.

Moneyness (how in or out of the money an option is) also shapes gamma. Deep ITM and deep OTM options have low gamma; delta is pinned at 1 and 0, respectively, and won't change much. A call struck $10 ITM has delta 1.0 and will stay near 1 even if stock falls; very low gamma. A call struck $10 OTM has delta 0 and will stay near 0 unless the stock rallies huge; very low gamma. Only at-the-money or near-the-money options have material gamma.

## Gamma risk for option writers and naked traders

Selling options creates negative gamma exposure. A call seller (or the seller side of a [call spread](/wiki/call-spread/)) has short gamma: as the stock rallies, delta increases but you don't participate in that increase (you are short the call and short gamma). You are forced to sell rallies and buy declines to rebalance—the opposite of optimal. This is why option sellers must carefully monitor gamma and limit position sizes; unchecked gamma exposure can blow up.

Naked option sellers are particularly vulnerable. A naked call writer (short 100 calls, long 0 shares) is short 5,000 gamma (very roughly). If the stock gaps up 10%, delta instantly jumps to 0.9, and the seller must cover losses and buy shares at any price to hedge. This is how [short squeezes](/wiki/short-squeeze/) happen and why regulators restrict naked option sales to professionals.

## Gamma in option pricing models

The [Black-Scholes model](/wiki/black-scholes-model/) and other [option](/wiki/option/) pricing frameworks compute gamma analytically or numerically. Gamma is the second partial derivative of option value with respect to the underlying price. In simple terms, the formula shows gamma rises with volatility and time-to-maturity (counterintuitively, longer-dated options have *lower* gamma because the slope is shallower over a wider range), and peaks at the strike. The model confirms the intuition: short-dated ATM options are gamma mines.

Practitioners also use gamma to estimate P&L from [realized volatility](/wiki/historical-volatility/). If you are long gamma with daily rebalancing, your P&L is roughly 0.5 × gamma × (daily price move)². High realized volatility feeds high gamma P&L. This is the "vol trader's dream": you are long [vega](/wiki/vega-option-greeks/) (betting vol will rise) and you collect gamma P&L when realized vol exceeds the implied vol you paid for the option.

## Practical takeaways for traders and investors

Retail option buyers often overlook gamma decay. Buying a call with low gamma (deep OTM, long time to expiration, or far from strike) feels cheap, but you are paying for time decay without benefiting from gamma convexity. The option decays to worthlessness with little vol cushion. Buying a call with high gamma (ATM, short time to expiration) feels expensive, but you own the convexity—you reap the asymmetric payoff if the stock moves.

Portfolio managers hedging long equity positions often short calls to reduce cost. Selling calls creates short gamma exposure, meaning the hedge works less well in market rallies (precisely when you need it most). [Collar strategies](/wiki/collar/) (long call, short call, long put, short put) are designed to manage gamma risk: you pay for long-put protection by selling expensive calls, balancing gamma costs.

<div class="wiki-seealso">

### Closely related
- [Delta (Option Greeks)](/wiki/delta-option-greeks/) — First derivative; sensitivity to price moves
- [Theta (Option Greeks)](/wiki/theta-option-greeks/) — Time decay; change in value per day
- [Vega (Option Greeks)](/wiki/vega-option-greeks/) — Volatility sensitivity; change per 1% vol move

### Wider context
- [Option Greeks](/wiki/options-greeks/) — Set of risk measures for options
- [Black-Scholes Model](/wiki/black-scholes-model/) — Foundation for option pricing
- [Convexity](/wiki/convexity/) — Non-linear price sensitivity; curvature of the price-yield curve

</div>
