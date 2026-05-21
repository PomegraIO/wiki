---
title: "Intrinsic Value"
description: "Intrinsic value is the amount by which an option is in-the-money—the immediate profit if exercised—independent of any time premium."
keywords:
  - intrinsic value
  - option value
  - in-the-money
  - exercise value
  - derivative pricing
image: "/svg/derivatives.svg"
---

*The **intrinsic value** of an option is the profit that would be realized if the option were exercised immediately. For a [call option](/call-option), intrinsic value is max(stock price − [strike price](/strike-price), 0). For a [put option](/put-option), it is max([strike price](/strike-price) − stock price, 0). Intrinsic value represents the [in-the-money](/in-the-money) amount and is the floor below which an option's market price cannot fall (excluding transaction costs).*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Intrinsic Value — key facts</div>

<img src="/svg/derivatives.svg" alt="Immediate profit from option exercise" />

<div class="wiki-infobox-caption">Intrinsic value is the profit from immediate exercise.</div>

|   |   |
|---|---|
| **Call formula** | max(spot − strike, 0) |
| **Put formula** | max(strike − spot, 0) |
| **[Out-of-the-money](/out-of-the-money)** | Zero intrinsic value |
| **[In-the-money](/in-the-money)** | Positive intrinsic value |
| **[At-the-money](/at-the-money)** | Zero intrinsic value |
| **Floor price** | Option value ≥ intrinsic value |
| **Changes over time** | Only with stock price; not affected by time decay |
| **Time value** | Total value = intrinsic + time value |
| **Early exercise** | Often optimal for deep ITM |
| **Exercise profit** | Call = intrinsic value; put = intrinsic value |

</aside>

## How intrinsic value works

If you own a [call option](/call-option) struck at $100 and the stock is currently at $110, the option has $10 of intrinsic value. You could immediately exercise, buy shares at $100, and sell them for $110, netting $10 per share (before commissions).

If the stock falls to $90, the call's intrinsic value drops to zero. You would not exercise (why buy at $100 when you can buy at $90 in the market?). The call might still be worth something if there is time to expiration, but that value is [time value](/time-value), not intrinsic.

For a [put option](/put-option) struck at $100 with the stock at $85, the intrinsic value is $15. You could immediately exercise, sell shares at $100, and buy them back at $85, netting $15 per share. If the stock rises to $105, the put's intrinsic value is zero.

## Intrinsic value never goes negative

By definition, intrinsic value is the maximum of the exercise profit and zero. It can never be negative. A call can never have negative intrinsic value; it bottoms at zero when [out-of-the-money](/out-of-the-money). This is why options are sometimes called "limited downside" investments—the option holder can simply walk away if the intrinsic value is zero and let the option expire worthless.

## The relationship to total option value

An option's market price is always at least its intrinsic value (ignoring transaction costs). An option cannot trade below intrinsic value because any rational trader would exercise immediately and capture the intrinsic value.

Total option value breaks into two pieces:

**Option price = Intrinsic value + Time value**

For an [in-the-money](/in-the-money) call with $10 intrinsic value trading at $12, the $2 difference is [time value](/time-value). That $2 reflects the remaining chance that the option will be even more profitable by expiration.

For an [at-the-money](/at-the-money) or [out-of-the-money](/out-of-the-money) option, intrinsic value is zero, so the entire option value is [time value](/time-value).

## Intrinsic value and early exercise

For [american-option](/american-option) options, early exercise is optimal if the option is very deep [in-the-money](/in-the-money) and there is little [time value](/time-value) left. An American call struck at $100 with the stock at $150 and only 1 day to expiration has $50 of intrinsic value and almost no time value. Exercising captures the $50; holding risks the stock falling $1 overnight and wiping out a dollar of gain.

For [european-option](/european-option) options, early exercise is not permitted, so you must hold and hope to sell for the [in-the-money](/in-the-money) intrinsic value plus any remaining [time value](/time-value).

## Intrinsic value vs. market price: opportunities and risks

If an option is trading below its intrinsic value, it is a mispricing. For example, if a call with $10 intrinsic value trades at $8, you can buy it, immediately exercise, and pocket $2 (minus commissions). This arbitrage opportunity is rare in liquid markets but can appear in illiquid or exotic options.

If an option trades significantly above intrinsic value in the days before expiration, the [time value](/time-value) is about to evaporate. An [in-the-money](/in-the-money) option that falls [out-of-the-money](/out-of-the-money) on expiration day sees its value drop from intrinsic to zero.

## Intrinsic value and the Greeks

Intrinsic value does not change with volatility, interest rates, or [theta](/theta). It changes only when the [stock](/stock) price moves. This is why an option's [vega](/vega) and [theta](/theta) apply only to the [time value](/time-value) component, not the intrinsic value.

For a deep [in-the-money](/in-the-money) option, the [delta](/delta) is close to 1.0, meaning the option moves nearly dollar-for-dollar with the stock. The intrinsic value captures most of that movement; the [time value](/time-value) is small.

## Deep in-the-money vs. shallow

A call struck at $100 with the stock at $150 (50% ITM) has $50 intrinsic value and very little [time value](/time-value). The option is almost a perfect substitute for owning the stock itself.

A call struck at $100 with the stock at $105 (5% ITM) has $5 intrinsic value but also meaningful [time value](/time-value), because the stock could easily fall below $100 by expiration.

## See also

<div class="wiki-seealso">

### Closely related

- [Time value](/time-value/) — the other component of option price
- [In-the-money](/in-the-money/) — has positive intrinsic value
- [Out-of-the-money](/out-of-the-money/) — zero intrinsic value
- [At-the-money](/at-the-money/) — zero intrinsic value
- [Strike price](/strike-price/) — determines intrinsic value (with spot price)

### Valuation

- [Call option](/call-option/) — intrinsic value = max(spot − strike, 0)
- [Put option](/put-option/) — intrinsic value = max(strike − spot, 0)
- [Option premium](/option-premium/) — total price = intrinsic + time
- [Black-Scholes model](/black-scholes-model/) — calculates intrinsic + time value

### Greeks

- [Delta](/delta/) — linked to intrinsic value sensitivity
- [Theta](/theta/) — affects time value, not intrinsic
- [Vega](/vega/) — affects time value, not intrinsic
- [Gamma](/gamma/) — how delta changes with intrinsic value shifts

### Deeper context

- [Option](/option/) — the family of derivatives
- Exercise and assignment — realizes intrinsic value
- [Arbitrage](/alpha/) — exploiting intrinsic value mispricings

</div>
