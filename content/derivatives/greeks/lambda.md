---
title: "Lambda"
description: "Percentage change in option value per percentage move in the underlying asset price."
keywords:
  - option greeks
  - leverage ratio
  - sensitivity analysis
  - option valuation
  - elasticity
---

*A **lambda** is the percentage change in an [option's](/wiki/option/) value for every 1% change in the underlying asset's price. It measures leverage: how many dollars of option value swing for each percentage move in the stock or index. It is also called *elasticity* or *gearing* and is crucial for traders sizing position risk.*

<div class="wiki-hatnote">Not to be confused with <a href="/wiki/lambda/">lambda</a> (the jump-risk parameter in asset pricing).</div>

<aside class="wiki-infobox">

| Aspect | Detail |
|--------|--------|
| **Formula** | (Δ × S) / P, where Δ = delta, S = stock price, P = option price |
| **Interpretation** | Percentage change in option value per 1% stock move |
| **Also called** | Elasticity, gearing, effective leverage |
| **Context** | In-the-money options | Out-of-the-money options |
| **ITM call example** | Lower lambda (less leverage) | Higher lambda (more leverage) |
| **Derives from** | Delta, stock price, and option premium |
| **Use case** | Position sizing for fixed-dollar [risk](/wiki/risk-on-risk-off/) |

</aside>

## Why lambda matters: leverage made visible

Suppose a [call option](/wiki/call-option-equity/) on a stock trading at $100 costs $5, and the option has a [delta](/wiki/delta/) of 0.50. If the stock moves 1%, the option moves roughly $0.50, or 10% in percentage terms: that is a lambda of 10. An investor holding the option gets 10 times the percentage upside of a stock holder with the same dollar amount deployed—but at 10 times the risk if the stock falls. Lambda quantifies this multiple.

This is the reason [options](/wiki/option-adjusted-spread/) exist. Traders with a bullish thesis buy out-of-the-money [calls](/wiki/call-option/) because they offer higher lambda: more bang per dollar risked. But that leverage is a double-edged sword. When the thesis fails, the option loses 10% while the stock loses only 1%, wiping out the position faster.

## The calculation is deceptively simple

Lambda is computed as:

```
Lambda = Delta × (Stock Price / Option Price)
```

This formula reveals the mechanics. A [call option](/wiki/call-option-equity/) with high [delta](/wiki/delta/) (near 1.0) and a low [premium](/wiki/option-premium/) relative to the stock price has very high lambda. That is, out-of-the-money options—which have low premiums and low deltas—often have even higher lambdas than in-the-money options, because the premium is small.

For instance: a $100 stock, a $105 call trading at $1.50 (deep [out-of-the-money](/wiki/out-of-the-money/)), with delta 0.15:

```
Lambda = 0.15 × (100 / 1.50) = 0.15 × 66.67 = 10.0
```

The same stock, a $100 call trading at $5, with delta 0.70 (in-the-money):

```
Lambda = 0.70 × (100 / 5) = 0.70 × 20 = 14.0
```

Both offer leverage, but the out-of-the-money option is cheaper to enter; the in-the-money option offers more absolute [gamma](/wiki/gamma-option-greeks/) (convexity) but lower percentage return per dollar.

## Lambda across the [Greeks](/wiki/options-greeks/)

Lambda is downstream from [delta](/wiki/delta/) and [gamma](/wiki/gamma-convexity/). Because [delta](/wiki/delta/) changes as the stock moves—that is what [gamma](/wiki/gamma-option-greeks/) measures—so does lambda. An [out-of-the-money](/wiki/out-of-the-money/) [call](/wiki/call-option/) starts with high lambda and low delta; as the stock rises, delta increases and lambda falls (the option becomes less leveraged, closer to behaving like the stock itself). Near expiration, this effect accelerates: [gamma](/wiki/gamma-option-greeks/) is highest, so delta and lambda gyrate wildly with tiny stock moves.

[Vega](/wiki/vega-option-greeks/) and [theta](/wiki/theta-option-greeks/) interact with lambda in complex ways. A drop in [volatility](/wiki/implied-volatility/) crushes [option](/wiki/option-premium/) prices, raising lambda (fewer dollars of option value for the same dollar stock move). Rising [theta](/wiki/theta-option-greeks/) decay also eats [premium](/wiki/option-premium/), raising effective lambda for remaining time to [expiration](/wiki/option-expiration/).

## Why traders use lambda instead of just looking at delta

A trader holding a $100k portfolio might own both 100 shares of a $100 stock (worth $10k) and 200 [call](/wiki/call-option-equity/) [options](/wiki/option-adjusted-spread/) (worth $2k). The [delta](/wiki/delta/) of the [calls](/wiki/call-option/) is high, but the positions feel very different in risk. Lambda clarifies: the $2k in [calls](/wiki/call-option/) might have a lambda of 15, equivalent to $30k in stock leverage. The $10k in shares has lambda of 1. The trader is unknowingly 2.5× long in percentage terms, not 1.1× long (as delta alone might suggest).

This matters for [value-at-risk](/wiki/value-at-risk/) (VaR) calculations. A [portfolio](/wiki/portfolio-mental-accounting/) manager says, "I can tolerate a 10% daily loss." In dollars, that is $10k. But if they deploy $8k in out-of-the-money [calls](/wiki/call-option/) with a lambda of 20, a 10% stock move causes a 200% loss in option value: $1.6k gone from an $8k position, a 20% portfolio loss—exceeding the risk budget. Lambda catches this; delta-only analysis might miss it.

## Lambda in [hedging](/wiki/inflation-hedging/) strategies

A fund manager holding $100M in equities wants to hedge tail risk with [put](/wiki/put-option-equity/) [options](/wiki/option-adjusted-spread/). Should they buy deep [out-of-the-money](/wiki/out-of-the-money/) [puts](/wiki/put-option/) (low cost, high lambda) or near-the-money [puts](/wiki/put-option-equity/) (high cost, lower lambda)? Lambda informs the choice. Deep [out-of-the-money](/wiki/out-of-the-money/) [puts](/wiki/put-option/) offer more portfolio [protection](/wiki/protective-put/) per dollar spent—they are cheaper—but they have higher lambda. A small move in the wrong direction early causes large losses in the [hedge](/wiki/hedge-fund/) value, creating false signals. Near-the-money [puts](/wiki/put-option-equity/) move more steadily, tracking portfolio losses [dollar](/wiki/us-dollar/)-for-[dollar](/wiki/us-dollar/).

## Lambda and position sizing: the practical rule

Traders often use lambda to set position limits. A rule might be: "No single position may have a notional lambda exceeding 50% of the portfolio's total lambda budget." This prevents any one bet from creating unintended leverage. For a $1M portfolio with a lambda limit of 5 (5% gain per 1% market move), a trader can hold $100k in stock (lambda 1) or $20k in an [option](/wiki/option-adjusted-spread/) with lambda 5, but not $200k in [calls](/wiki/call-option/) with lambda 25.

## When lambda fails: discontinuities and jumps

Lambda is a first-order approximation, like [delta](/wiki/delta/) itself. In calm markets, a 1% stock move causes an approximately 10×1% = 10% [option](/wiki/option-adjusted-spread/) move (for a lambda-10 [option](/wiki/option-adjusted-spread/)). In a [gap](/wiki/overnight-gap/) opening or [flash crash](/wiki/flash-crash-2010/), the stock gaps 5% and there is no continuous trading; the [option](/wiki/option-adjusted-spread/) price [jumps](/wiki/flash-loan/) to match, and historical lambda is unreliable. Traders who rely on lambda during extreme moves often find their [hedge](/wiki/hedge-fund/) ineffective. This is why [tail-risk](/wiki/tail-risk-hedging/) hedges often use [out-of-the-money](/wiki/out-of-the-money/) [puts](/wiki/put-option-equity/) at deep strikes: they are cheap and provide [convexity](/wiki/convexity/) that lambda cannot capture.

## Conclusion: lambda is delta times leverage

A [call option](/wiki/call-option-equity/) with lambda 10 behaves like a 10:1 leveraged stock bet: 10% gain on a 1% stock move, 10% loss on a 1% down move. Lambda makes that leverage visible and measurable. Traders who ignore lambda often discover it painfully: a small portfolio move causes a large [option](/wiki/option-adjusted-spread/) loss because the leverage was hidden. Using lambda to size positions, set risk limits, and design [hedges](/wiki/hedge-fund/) is a mark of disciplined [risk](/wiki/market-risk/) management.

<div class="wiki-seealso">

### Closely related
- [Delta](/wiki/delta/) — directional sensitivity to stock price
- [Gamma](/wiki/gamma-option-greeks/) — convexity and delta sensitivity
- [Vega](/wiki/vega-option-greeks/) — sensitivity to volatility
- [Theta](/wiki/theta-option-greeks/) — time decay
- [Options Greeks](/wiki/options-greeks/) — full Greek taxonomy

### Wider context
- [Option](/wiki/option-adjusted-spread/) — underlying instrument
- [Call option](/wiki/call-option-equity/) — bullish bet with leverage
- [Put option](/wiki/put-option-equity/) — bearish hedge with leverage
- [Value at risk](/wiki/value-at-risk/) — risk measurement framework
- [Protective put](/wiki/protective-put/) — downside hedge structure

</div>
