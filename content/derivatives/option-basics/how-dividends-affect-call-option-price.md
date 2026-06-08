---
title: "How Dividends Affect Call Option Prices"
description: "Why expected dividends lower call option prices and raise put premiums; early exercise mechanics before ex-dividend dates."
keywords:
  - dividends affect call option price
  - how dividends affect options
  - ex-dividend date option exercise
  - dividend impact options
  - call option dividend adjustment
  - early exercise dividend
image: "/svg/derivatives.svg"
---

*Expected **dividends lower call option prices** and raise put premiums because a [call option](/call-option/) holder does not receive the dividend payment—only the stock owner does. Before an ex-dividend date, a call holder may rationally choose [early exercise](/option/) to capture the dividend, and dividend-paying stocks tend to have lower call [option premiums](/option-premium/) than non-dividend-paying peers.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Dividends and Options — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Option holders miss dividends unless they own stock; this shifts option values.</div>

|   |   |
|---|---|
| **Dividend holder** | Receives payment; option holder does not |
| **Call premium effect** | Lowers call value; raises [put](/put-option/) value |
| **Ex-dividend date** | Last day to own stock and receive dividend |
| **Early exercise incentive** | Present when dividend exceeds call [time value](/time-value/) |
| **Typical impact** | 5–15% of call premium for high-yield stocks |

</aside>

## Why dividends reduce call value

A [call option](/call-option/) gives the holder the right, but not the obligation, to buy 100 shares at a fixed [strike price](/strike-price/). But the right to buy stock does not include the right to any cash distributions that occurred before the purchase. If the underlying stock pays a dividend before you exercise your call, you do not receive that cash.

Consider two identical companies: one pays a 3% annual [dividend yield](/dividend-yield/), the other pays none. Both trade at $100, both have identical volatility. A call option on the non-dividend stock will command a higher premium than the call on the dividend stock—all else equal—because the call buyer knows they will miss the dividend.

The effect scales with the dividend. A utility stock yielding 4% per year will have visibly cheaper calls than a tech stock yielding 0.2%. The higher the expected cash outflow, the less an option to buy the stock is worth.

The intuition is simple: you are paying for an option to own a stock that will pay out cash. If you exercise, you own it after the ex-dividend date, so you own it after the cash leaves. The dividend is a transfer of value from the stock to shareholders; option holders are not shareholders.

## Impact on put value

By symmetry, [put options](/put-option/) become more valuable when dividends are expected. A put gives the right to sell the stock at a fixed price. If the stock is about to pay a large dividend, it may fall in price (by roughly the dividend amount) on or after the ex-date. A put holder who owns the underlying stock benefits from this price drop if they have a put as insurance.

More subtly: a higher dividend makes it more attractive to exercise a [protective put](/protective-put/) early, to receive the dividend as a shareholder.

## Early exercise and the ex-dividend date

American-style [call options](/call-option/) can be exercised at any time before [expiration](/expiration-date/). European-style options can only be exercised at maturity. This distinction becomes material around [ex-dividend](/dividend/) dates.

The [ex-dividend date](/dividend/) is the last day an investor can buy the stock and still receive the next dividend payment. On and after the ex-date, new buyers do not get the dividend. Typically, the stock price falls by roughly the dividend amount on the ex-date (not a true loss, just a rebalancing of value).

A call holder who plans to exercise eventually must decide: do I exercise before the ex-date (to be the shareholder and receive the dividend) or after (to avoid the price drop)?

**Example:** A call option has a $100 strike price. The stock currently trades at $105. A $2 dividend is about to be paid. The option has 2 weeks until expiration and carries $1 of time value.

If you exercise now, you pay $100, own the stock, receive the $2 dividend, and hold stock worth roughly $103 (after the ex-date price drop). Your net cost is $98.

If you wait until after the ex-date, the stock will have fallen to roughly $103. You exercise at $100, own shares worth $103, but miss the $2 dividend. Your net cost is $100.

Early exercise is rational if the dividend exceeds the [time value](/time-value/) of the option. In this case, $2 dividend > $1 time value, so exercise before ex-date.

However, if the option had $3 of time value, waiting is better: the $3 time decay exceeds the $2 dividend, so you'd rather let time work in your favor and exercise later (or let the option expire and buy stock outright).

## Dividend adjustments in option pricing

The [Black-Scholes model](/black-scholes-model/) and most [derivatives](/option/) pricing frameworks include a dividend yield input. Higher yields mechanically reduce call values and raise put values. A model without a dividend adjustment will overprice calls on dividend-paying stocks and underprice puts.

The adjustment assumes dividends are paid continuously at a constant yield. In reality, dividends are discrete and lumpy. A stock paying one large special dividend behaves differently from a stock with four predictable quarterly payments. Close to an ex-date, discrete-dividend models are more accurate than continuous-yield approximations.

## Dividend policy and option values

Companies that change dividend policy affect option markets directly. When a mature company begins a dividend, existing calls lose value and existing puts gain value. When a company suspends a dividend, calls rally and puts fall.

Traders pay attention. A stock that has yielded 3% for years will have calls priced with that expectation. If the company cuts its dividend in half, calls will re-rate upward. Conversely, a surprise dividend hike pushes calls lower.

This interaction creates an incentive: call buyers prefer non-dividend-payers (or low-yield payers), while [dividend-discount model](/dividend-discount-model/) equity investors prefer high-yield stocks. Option positions can hedge dividend risk. A call-selling strategy on a high-yield stock collects [option premium](/option-premium/) that partly offsets the dividend opportunity cost.

## Empirical magnitudes

For a stock with a 2% dividend yield, a 12-month at-the-money call option may carry 5–10% less premium than it would without the dividend. For high-yield stocks (4%+), the effect is 10–20% or more.

Puts exhibit the opposite pattern: put premiums are 5–15% higher on dividend-paying stocks, all else equal.

The effect is largest for:
- Long-dated options (dividend payments occur over a longer period; greater cumulative impact)
- Calls deep out-of-the-money (less intrinsic value relative to dividend; time value is a smaller cushion)
- High-yield stocks (larger cash outflow relative to stock price)

## See also

<div class="wiki-seealso">

### Closely related

- [Call option](/call-option/) — the right to buy; reduced in value by dividends
- [Put option](/put-option/) — the right to sell; increased in value by dividends
- [Option premium](/option-premium/) — the price of the option, adjusted for dividend expectations
- [Ex-dividend date](/dividend/) — the cutoff for receiving the next payment
- [Time value](/time-value/) — the premium paid for optionality; eroded by exercise around dividends
- [Exercise price](/strike-price/) — the fixed price at which the option can be exercised
- [Black-Scholes model](/black-scholes-model/) — incorporates dividend yield in option valuation
- [Dividend yield](/dividend-yield/) — the cash payment as a percentage of stock price

### Wider context

- [Dividend](/dividend/) — the cash distribution to shareholders
- [Stock](/stock/) — the underlying asset for the option
- [Covered call](/covered-call/) — selling calls on dividend stocks to harvest premium and offset dividend opportunity cost
- [Derivatives hedging](/derivatives-hedging/) — using options to manage dividend and price risk

</div>
