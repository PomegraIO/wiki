---
title: "Theta Decay in Options: How Time Erosion Works"
description: "Theta decay in options explains how time value erodes daily from an option premium, accelerating sharply in the final weeks before expiration."
keywords:
  - theta decay options how it works
  - time decay options
  - theta time value
  - option premium decay
  - time decay acceleration
image: "/svg/derivatives.svg"
---

*Theta decay in options is the daily erosion of an option's time value, the portion of premium that exists purely because time remains until expiration. An option loses value simply by the passage of a day, regardless of whether the underlying stock moves, and this decay accelerates as expiration approaches.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Theta Decay — Time Value Bleeding Out</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Every passing day strips an option of value; the last weeks are when the loss becomes acute.</div>

|   |   |
|---|---|
| **What decays** | Time value component of the option premium |
| **Decay acceleration** | Exponential in the final 2–4 weeks before expiration |
| **Who loses** | Buyers of options; sellers benefit |
| **Intrinsic vs. time value** | Intrinsic (in-the-money cushion) does not decay; time value does |
| **Impact on strategy** | Short sellers and holders of covered calls collect theta; long option buyers pay it |

</aside>

## The Two Parts of an Option Premium

An option's price has two components: [intrinsic value](/intrinsic-value/) and time value.

Intrinsic value is the amount by which the option is [in-the-money](/in-the-money/). A call option on a stock trading at $105 with a strike of $100 has $5 of intrinsic value—you could exercise it immediately, sell the stock, and pocket $5. That intrinsic value does not decay; it will always be there as long as the stock stays above $100.

Time value is everything else. If that same option is trading for $8, then $3 is time value ($8 premium − $5 intrinsic = $3). That $3 exists because there are still weeks or months left until expiration. The stock could move higher, increasing the option's worth. Or the market could price in volatility, widening the option's range of outcomes. Time value is the market's bet on future possibilities.

But as time passes and possibilities shrink—when there are only three days left instead of three weeks—that $3 of time value decays. On the morning of expiration, if the option is still $5 in-the-money, it is worth $5, not $8. The entire $3 time value has vanished.

## Why Time Value Decays

An option is a bet on the future. The longer the future stretches before you, the more potential moves you have room to capture. A call buyer with six months can wait for the stock to climb; with six days, the window is tiny.

From the option seller's perspective, they are taking on the risk of being wrong. The longer the expiration is away, the longer they must hold that risk. As days pass and fewer remain, their risk shrinks—the stock has fewer opportunities to move against them. Therefore, the seller's compensation (the time value they keep) diminishes.

This is not market friction or inefficiency; it is the mathematical reality of optionality. The value of a choice declines as the window in which you can exercise it narrows.

## The Acceleration Effect in the Final Weeks

Theta decay is not linear. An option with 100 days to expiration loses a certain amount of time value each day—call it $0.02. That slow bleed is tolerable for option buyers.

But as expiration approaches, the decay accelerates exponentially. With 30 days to expiration, the option might lose $0.05 per day. With 7 days left, it might lose $0.15 per day. In the final day or two, an out-of-the-money option can lose 50% of its remaining value in a single session.

This acceleration is visible in the shape of the theta curve. Imagine a graph with time until expiration on the horizontal axis and option premium on the vertical. The line slopes downward gradually at first, then bends sharply as it approaches zero. That sharp bend is where the buyer of a multi-month option gets squeezed.

The mathematical reason is that an option's value is tied to the range of possible outcomes—captured by [volatility](/implied-volatility/). As time shrinks, the cone of possible outcomes narrows. With only a week left, the stock is unlikely to move 20%; with six months, it might. The probability weights shift, and the option becomes worth less.

## Intrinsic vs. Time Value in Decay

Only time value decays. Intrinsic value is guaranteed; it is the cushion you already have.

An option that is $10 in-the-money with one day left is still worth at least $10 at expiration. If it is trading for $12, that extra $2 is time value and will disappear. But the $10 is safe.

Conversely, an option that is $5 out-of-the-money (the stock is below the strike) has zero intrinsic value. All of its premium is time value. With each passing day, that time value decays toward zero. At expiration, if the stock is still below the strike, the option expires worthless.

This asymmetry is crucial. An option buyer in a profitable position (in-the-money) experiences theta decay on the time value only. An option buyer in an unprofitable position experiences decay on the entire premium—a much sharper erosion.

## How Traders Exploit Theta Decay

Theta decay benefits the option seller. A seller of an out-of-the-money [call option](/call-option/) or [put option](/put-option/) collects the full premium upfront. As time passes and the option loses value without the underlying moving, the seller's position improves. They can buy back the option for less than they sold it, locking in a profit.

This is the engine of [covered call](/covered-call/) strategies. A stock owner sells a call option against their shares, collects the premium, and hopes the stock stays flat or declines slightly. Each day that passes, the time value decays in their favor. If the stock does not breach the strike by expiration, they keep the full premium and can sell another call against the same shares.

[Theta decay](/time-decay-theta/) is also a factor in [spread strategies](/spread/), where a trader simultaneously buys and sells options at different strikes or expirations. By selling a nearer-term option and buying a longer-term one, the trader collects the faster decay of the short leg against the slower decay of the long leg, capturing the difference.

Option buyers, by contrast, fight theta daily. If you buy a call hoping the stock will rise, time is working against you. The stock must move enough to overcome both the decay of time value and the cost of your [option premium](/option-premium/). This is why option buyers are often directionally bullish or bearish, not neutral; they need the stock to move to justify the cost of theta.

## The Role of Volatility

Implied volatility interacts with theta in a counterintuitive way. High implied volatility inflates option premiums, making time value larger. In a high-volatility environment, the cone of possible outcomes is wider, so the option is worth more.

But high volatility also means faster theta decay, because the premium is larger to begin with. An option trading for $5 with a theta of $0.10 per day is losing 2% per day. The same option in a high-volatility regime might trade for $8, with a theta of $0.20 per day—still 2.5% per day, but on a larger base.

Conversely, when implied volatility collapses—say after an earnings announcement passes—time value shrinks suddenly. This can offset theta's daily contribution and hurt sellers unexpectedly.

## A Practical Example

Consider a stock trading at $100. A call option with a $105 strike and 30 days to expiration is trading for $2.50. The option is out-of-the-money; all $2.50 is time value.

Each day that passes, that $2.50 decays. The rate is not uniform: with 30 days left, it might lose $0.08 per day. With 10 days left, it might lose $0.18 per day. With 3 days left, it might lose $0.30 per day.

A buyer of this option has already paid $2.50. For the trade to be profitable, the stock must rally to $107.50 or higher by expiration (to recover the premium and earn a gain). But if the stock stays at $100, the option is worthless at expiration. The buyer's loss is accelerated by theta in the final weeks; they watch their position decay from $1.50 to $0.50 to $0.05 in a matter of days, even if the stock does not move.

A seller of this same option collects $2.50 immediately. As days pass and the option decays toward zero (assuming the stock stays below $105), the seller's gain compounds. They could buy back the option for $1.20, realizing a $1.30 profit, or hold until expiration and keep the full $2.50.

## See also

<div class="wiki-seealso">

### Closely related

- [Intrinsic value](/intrinsic-value/) — The guaranteed portion of an option's worth, unaffected by decay
- [Option premium](/option-premium/) — What buyers pay and sellers collect for the right to buy or sell
- [Call option](/call-option/) and [Put option](/put-option/) — The two types of options and how decay affects each
- [Implied volatility](/implied-volatility/) — How market expectations of future volatility inflate or deflate option prices
- [Covered call](/covered-call/) — A strategy that exploits theta decay by selling call options
- [Vega](/vega/) — How option value changes with shifts in implied volatility

### Wider context

- [Option](/option/) — The fundamentals of derivatives and option contracts
- [Time value](/time-value/) — The broader concept of value tied to the passage of time
- Greeks — The full set of option sensitivity measures
- [Derivatives hedging](/derivatives-hedging/) — Using options to reduce portfolio risk

</div>
