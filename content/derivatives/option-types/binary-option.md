---
title: "Binary Option"
description: "A binary option is a derivative with a predetermined fixed payoff that either occurs in full or not at all, depending on whether the underlying asset crosses a strike price."
keywords:
  - binary option
  - digital option
  - exotic option
  - all-or-nothing payoff
  - derivative
image: "/svg/derivatives.svg"
---

*A **binary option** is an exotic derivative with a simple, binary payoff: if the underlying asset finishes above (call) or below (put) the [strike price](/strike-price/) at [expiration](/expiration-date/), the holder receives a fixed amount of cash; otherwise, the holder receives nothing. Also called a **digital option** or **all-or-nothing option**, binary options are used for definitive bets on direction without exposure to magnitude of move.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Binary Option — key facts</div>

<img src="/svg/derivatives.svg" alt="A binary decision diagram with yes/no outcomes" />

<div class="wiki-infobox-caption">Binary options pay a fixed amount or nothing, based on strike crossing.</div>

|   |   |
|---|---|
| **Payoff structure** | Fixed cash amount (e.g., $100) or $0 |
| **Triggering event** | Underlying above/below strike at expiration |
| **Call payoff** | $K if price > strike; $0 otherwise |
| **Put payoff** | $K if price < strike; $0 otherwise |
| **Price sensitivity** | Non-linear; peaks near strike |
| **Intrinsic value** | $0 or full payoff; no intermediate value |
| **Time value** | Concentrated near strike price |
| **Liquidity** | Lower than vanilla options |
| **Primary use** | Cheap binary bets on direction |

</aside>

## The payoff structure

Unlike a standard [call option](/call-option/) that pays the difference between the spot and strike price at expiration, a binary call pays a fixed amount (e.g., $100) if the underlying finishes above the strike, and $0 if it finishes below.

Suppose a binary call is struck at $100 with a payoff of $100. If the stock closes at $150, the holder receives exactly $100—not $50. If it closes at $99.99, the holder receives exactly $0. The magnitude of the move does not matter; only the direction does.

This all-or-nothing structure is what gives the option its "binary" name. There are only two outcomes: win the full amount or lose the premium paid. No in-between gradations.

## Pricing and cost

Binary options are cheaper than [call option](/call-option/) alternatives because they do not offer unlimited upside. The payoff is capped at a fixed amount. A trader who believes a stock will rise 10% faces a choice: buy a vanilla call (which profits the full amount if the move happens) or a binary call (which profits only the fixed amount, but for less premium).

The value of a binary call is highest when it is at-the-money (near the strike) because there is maximum uncertainty about which way the stock will close. Deep in-the-money or far out-of-the-money binary options are worth less (closer to their intrinsic value of either $K or $0).

[Black-Scholes model](/black-scholes-model/) can price binary options by recognizing the binary call as a steep, narrow bull spread. The value depends on the probability the stock closes above the strike, discounted to present value and multiplied by the payoff amount.

## Use cases

Binary options are useful for traders who want a directional bet without exposure to magnitude. A trader who thinks a biotech stock will jump on FDA approval knows the move will be large, but how large is unknown. A binary call lets the trader cap risk and cost while capturing the binary outcome.

Companies use binaries to hedge binary events. A contractor might buy a binary put struck at $90 with a $100 payoff. If the relevant commodity or currency crashes below $90, the contractor receives $100 cash. This provides a fixed hedge for a catastrophic scenario without spending the premium of a full vanilla put.

## Cash settlement

Most binary options are cash-settled. At expiration, the exchange (or counterparty) observes the closing price, compares it to the strike, and deposits either the fixed amount ($100) or $0 into the holder's account. No physical delivery occurs.

The exact settlement level can matter—some binaries settle on the closing price, others on the volume-weighted average price (VWAP) of the final minutes, and some on a fixing price. Each method has different implications for manipulation risk and final payoff certainty.

## Regulatory and legal status

Binary options occupy a contentious regulatory space. In some jurisdictions (Europe, Australia), they are treated as derivatives and require registered brokers and full disclosure. In others, they were marketed directly to retail consumers with minimal safeguards, leading to widespread fraud and mis-selling. Many countries have restricted or banned binary options outright, particularly for retail investors.

Legitimate binary options trade on regulated exchanges (CME, Nadex in the US; various European exchanges) and are priced fairly based on probability and volatility. Fraudulent ones (offered by unregistered brokers in jurisdiction-free zones) are often rigged, with payoff structures stacked against the retail buyer.

## Greeks and risks

The [delta](/delta/) of a binary call is highest at-the-money and falls to near-zero far from the strike. This creates a sharp edge: tiny moves near the strike trigger large [delta](/delta/) changes, while large moves far from the strike trigger none. This makes [delta](/delta/) hedging binary options tricky.

[Gamma](/gamma/) (the change in [delta](/delta/)) is concentrated at the strike and can be very high, creating instability in hedges. [Theta](/theta/) (time decay) benefits the seller as expiration nears and the option approaches either $0 or $K with certainty. [Vega](/vega/) (sensitivity to [volatility](/historical-volatility/)) is negative for binary options near the strike (higher volatility lowers the probability of finishing exactly in or out) and positive far from the strike.

## Comparison with vanilla options

A trader bullish on a stock could buy a vanilla $100 [call option](/call-option/) for $5, profiting the full amount if the stock soars to $120. Or the trader could buy a binary call at $100 for $2.50, profiting only a fixed amount (say, $10) if the stock finishes above $100.

The vanilla call offers more upside if the stock moves a lot; the binary call offers more upside per dollar of premium and more certainty about maximum loss. The choice depends on the trader's view of the move magnitude.

## See also

<div class="wiki-seealso">

### Closely related

- [Call option](/call-option/) — vanilla right to buy; continuous payoff
- [Put option](/put-option/) — vanilla right to sell; continuous payoff
- [Barrier option](/barrier-option/) — payoff also depends on path crossing
- [Exotic option](/binary-option/) — non-standard payoff structures
- [Strike price](/strike-price/) — determines payoff triggering event

### Pricing & Greeks

- [Black-Scholes model](/black-scholes-model/) — extended for binary pricing
- [Implied volatility](/implied-volatility/) — affects payoff probability
- [Delta](/delta/) — sharply concentrated at strike
- [Gamma](/gamma/) — very high near strike
- [Vega](/vega/) — negative near strike, positive far away

### Deeper context

- [Option](/option/) — the family of derivatives
- Regulatory risk — binary options face restrictions
- [Volatility smile](/volatility-smile/) — binary options have distinct skew patterns

</div>
