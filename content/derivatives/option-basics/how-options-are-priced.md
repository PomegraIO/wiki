---
title: "How Options Are Priced: Intrinsic and Extrinsic Value"
description: "How are options priced? The option premium equals intrinsic value (in-the-money gain) plus time value (extrinsic). Volatility, time, and rates determine the extrinsic component."
keywords:
  - how are options priced
  - intrinsic value option
  - time value option
  - extrinsic value
  - option premium
  - option valuation
image: "/svg/derivatives.svg"
---

*An **option premium**—the price a buyer pays for an [option](/option/)—equals two components: **intrinsic value**, the profit if exercised immediately, and **extrinsic** (or **time**) **value**, the probability-weighted profit from future moves. Understanding this split explains why options lose value as expiration nears and why volatility spikes drive premiums up.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">How Options Are Priced — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Option price = intrinsic value + time value; most of an out-of-the-money premium is time.</div>

|   |   |
|---|---|
| **Intrinsic value** | Current in-the-money profit; zero if out-of-the-money |
| **Time value** | Probability and magnitude of profitable move before expiry |
| **Option premium** | Total price: intrinsic + time |
| **Key driver of time value** | [Volatility](/historical-volatility/), [time to expiration](/expiration-date/), [interest rates](/interest-rate/) |
| **At-expiration** | Premium = intrinsic value (time value = zero) |

</aside>

## Intrinsic value: the profitable floor

**Intrinsic value** is the profit a buyer would pocket by exercising the option immediately.

For a [call option](/call-option/), intrinsic value is the current stock price minus the [strike price](/strike-price/), floored at zero. If a stock trades at $105 and the call [exercise price](/exercise-price/) is $100, intrinsic value is $5. If the stock is $95, intrinsic value is zero—the option is [out-of-the-money](/in-the-money/), and immediate exercise would lose money.

For a [put option](/put-option/), intrinsic value is strike minus stock price, floored at zero. A put struck at $100 on a $95 stock has $5 of intrinsic value. A put struck at $100 on a $105 stock has zero intrinsic value.

An option with intrinsic value is said to be **in-the-money**. One with zero intrinsic value is **out-of-the-money** or **at-the-money** if the stock price equals the strike.

Intrinsic value is a floor: an option can never sell below its intrinsic value for long, because arbitrageurs would buy it, exercise it, and pocket the difference. On the day of expiration, when there is zero time remaining, the option price equals its intrinsic value exactly—no more, no less.

## Time value: the volatility premium

**Time value** (also called **extrinsic value**) is everything above intrinsic. It reflects the buyer's bet that the stock will move far enough before expiration to push the option deeper in-the-money (or back to profitability if currently out-of-the-money).

A call option struck at $100 on a stock trading at $99 with one month to expiration might trade at $2. It has zero intrinsic value (it's out-of-the-money), so the entire $2 premium is time value. The buyer is betting the stock will climb above $101 (strike + premium paid) in the next month. If the stock stalls at $100.50 on expiration day, the option is worthless—the buyer loses the entire $2.

Time value decays over the life of the option. As expiration approaches, the probability window narrows. An option with one day left has far less time value than one with 90 days left, even if both are equally out-of-the-money. This erosion is called **theta** (time decay); it accelerates near expiration, a fact traders use constantly.

## What drives time value: the Black–Scholes factors

Option pricing models—most famously the [Black–Scholes model](/black-scholes-model/)—decompose time value into three main drivers.

**Volatility** is the dominant force. High-volatility stocks have fat-tailed distributions; the chance of a large move is higher, so calls and puts both fetch higher premiums. A stock swinging ±3% daily has more option premium than one moving ±1%, all else equal. This is **[implied volatility](/implied-volatility/)**: the volatility the market is pricing in. When stock prices gyrate, [implied volatility](/implied-volatility/) spikes, and option prices rise, even if the stock price itself hasn't moved.

**Time to expiration** directly affects time value. More time = more windows for the stock to move favorably. A 6-month option carries 24 times as many calendar days as a 1-week option, yet its time value is not 24 times larger, because the probability of huge moves is not linear. Still, going from 60 days to 30 days typically shrinks time value by 30–40%, depending on moneyness and volatility. Options follow a [square-root rule](/duration/) roughly: doubling the time scales time value by the square root of 2, or about 41%.

**Interest rates** matter, though subtly. A higher [risk-free rate](/interest-rate/) increases the value of calls (because the buyer defers $cash$ outlay) and decreases the value of puts. The effect is usually small—a few cents per contract unless rates are extreme—but it is real.

**Dividends** subtract from call value (holders of options don't collect dividends, but stock holders do) and add to put value. A stock paying a 3% dividend yield reduces call premium relative to a non-dividend stock.

## The shape of time value

An out-of-the-money call struck far from the current price has low time value, because the stock must move a lot to make the option profitable. A call struck $10 out of the money has a smaller probability of ending in-the-money than one struck $2 out, so it carries less time value.

An at-the-money call (strike = stock price) carries the most time value per contract, because it is the most sensitive to moves in either direction. Very deep in-the-money calls have little time value left—the option is almost certain to be exercised, so the buyer is paying mostly intrinsic value plus a small margin for the stock falling.

As expiration nears, time value collapses in a non-linear way. An option with 6 months left loses time value slowly; one with 6 days loses it in hours. This asymmetry is why [covered call](/covered-call/) writers (who sell calls) love expiration week—the caller's edge (time decay) accelerates.

## A worked example

A tech stock trades at $150. The 3-month $150 call (at-the-money) trades at $8.50. The 3-month $160 call (out-of-the-money) trades at $3.00.

The $150 call: intrinsic = $0 (stock price = strike), time value = $8.50 (the whole premium).

The $160 call: intrinsic = $0, time value = $3.00 (the whole premium).

Why is the out-of-the-money call cheaper? It requires a $10 move (150 to 160) to be profitable, whereas the ATM call only needs a move above $150. The OTM call is longer-odds, so its time value is smaller.

Now, suppose implied volatility doubles (perhaps due to pending earnings). The $150 call might jump to $12.50, and the $160 call to $5.50. Neither option is deeper in-the-money, but both gained time value because the distribution has fatter tails. The stock hasn't moved, but the option prices did.

Weeks pass. With 1 week left to expiration, the stock is still at $150. The $150 call now trades at $0.80 (time value collapsed from $8.50). The $160 call is worth $0.10 or less. Time decay, accelerating near expiration, has shriveled the extrinsic component.

## See also

<div class="wiki-seealso">

### Closely related

- [Option](/option/) — the derivative contract itself
- [Call option](/call-option/) — the right to buy
- [Put option](/put-option/) — the right to sell
- [Intrinsic value](/intrinsic-value/) — immediate exercise profit
- [In-the-money](/in-the-money/) — option with positive intrinsic value
- [Strike price](/strike-price/) — the [exercise price](/exercise-price/)
- [Expiration date](/expiration-date/) — when time value hits zero
- [Implied volatility](/implied-volatility/) — the volatility the market is pricing in
- [Historical volatility](/historical-volatility/) — realized volatility from past price moves

### Wider context

- [Black–Scholes model](/black-scholes-model/) — the canonical pricing formula
- [Theta](/time-decay-theta/) — time decay component of option premium
- [Vega](/vega/) — sensitivity to changes in implied volatility
- [Delta](/delta/) — sensitivity to stock price moves
- [Gamma](/gamma/) — second-order sensitivity
- [Volatility smile](/volatility-smile/) — how implied volatility varies by strike

</div>
