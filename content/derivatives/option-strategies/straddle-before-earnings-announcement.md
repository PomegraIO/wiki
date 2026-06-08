---
title: "Straddle Before an Earnings Announcement"
description: "Buying a straddle before earnings bets on volatility expansion, but implied volatility crush after earnings often decimates long positions. Here's why."
keywords:
  - buying straddle before earnings
  - straddle earnings strategy
  - implied volatility crush
  - options volatility contraction
---

*A **straddle before an earnings announcement** is a bet that price will move far enough after earnings to offset the cost of the options premium you paid upfront. Traders buy a call and a put at the same strike price, expecting a large move in either direction. The problem: [implied volatility](/implied-volatility/) typically expands before earnings, inflating option prices and the straddle's cost, then collapses after earnings no matter which direction price moved. This **volatility crush** often defeats the strategy even when price moves as much as the trader expected.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Straddle Before Earnings — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives." />

<div class="wiki-infobox-caption">High premium before earnings kills the straddle; buyers need a truly large move to compensate.</div>

|   |   |
|---|---|
| **Setup** | Buy call + put at same strike before earnings |
| **Bet** | Price will move far in either direction |
| **Cost** | Total premium: call + put (high before earnings) |
| **Breakeven** | Strike ± (call premium + put premium) |
| **Enemy** | Implied volatility crush after results |
| **Payoff** | Profit only if price move > total premium paid |
| **Risk** | Unlimited loss if you sold to open (illegal for most) |

</aside>

## Why implied volatility makes straddles expensive

Before a company reports earnings, uncertainty is at its peak. Analysts do not know whether the company will beat or miss estimates. Traders do not know whether the stock will gap up or down. This uncertainty manifests as elevated [implied volatility](/implied-volatility/)—the market's collective guess about how much the stock will move in the future.

Elevated [implied volatility](/implied-volatility/) makes both calls and puts more expensive, because each one has a higher probability of finishing in-the-money and a larger expected payoff. If implied vol is 30% on a normal day and jumps to 60% the day before earnings, the premium you pay for your call and put both double (roughly). This is the straddle buyer's first hurdle: you are paying top dollar for options right when they are most expensive.

## The mechanics of volatility crush

Here is the cruel part: implied volatility does not stay elevated after earnings. The moment results are announced, uncertainty is resolved. The market now knows the earnings figure, the guidance, and the forward outlook. Traders have new information and can make updated bids. The stock might gap up, gap down, or barely move. But whichever it does, the resolved uncertainty causes implied volatility to crater.

Imagine a stock trading at \$100 the day before earnings:
- Call premium: \$4
- Put premium: \$4
- Total straddle cost: \$8
- Breakevens: \$92 and \$108

After earnings, the stock moves to \$106—a significant 6% move, well within what traders expected. The stock is now \$6 above the call strike, so the call is worth \$6 intrinsic value. But because [implied volatility](/implied-volatility/) has crushed from 60% down to 30%, the call also has much less time value. The entire option might now be worth \$6.50 instead of \$7.

The put, meanwhile, is now out-of-the-money by \$6. With crushed volatility, it might be worth only \$0.10 instead of \$1. So your straddle position, which is now short 1 put (\$0.10) and long 1 call (\$6.50 intrinsic), is worth \$6.40 total. You paid \$8, so you are down \$1.60 on a move that should have been profitable.

## Why this matters: the expected move trap

Before earnings, [implied volatility](/implied-volatility/) is saying "the stock could realistically move 5% either way," or whatever the market's consensus is. But traders often assume that the size of the implied move is the size the stock *will* move. It is not. The implied move is just the market's expectation of price volatility; actual earnings moves are highly variable. Some companies gap 15%, others move 1% despite earnings surprises.

If you are buying a straddle at \$8 premium before earnings, your breakeven requires the stock to move \$8 from the strike, or 8% in absolute terms. If the implied move is only 5%, you are already betting against the market's own volatility forecast. You are paying for an 8% move, but the market thinks a 5% move is more likely.

## The calendar effect and time decay

The day before earnings, both your options are very short-dated—perhaps one or two days to expiration or the next earnings report. Even if you buy options on a date after earnings (say, the following week), [time decay](/time-decay-theta/) accelerates as the earnings announcement approaches and passes. You are fighting two enemies at once: short time value and impending volatility crush.

## When straddles work despite the odds

Long straddles before earnings do sometimes pay off, but only when the actual move is *significantly* larger than implied volatility suggested. If the implied move is 5% but the stock gaps 12%, then yes, you have captured enough intrinsic value to overcome volatility crush and time decay. But this requires either:

1. **An earnings surprise larger than the market expected**, or
2. **Buying the straddle when implied vol is suppressed** (unlikely before earnings, more common after a quiet period).

Sophisticated traders sometimes sell volatility before earnings (short a straddle or shorter-dated calls/puts) instead of buying it, pocketing the premium from the elevated [implied volatility](/implied-volatility/). Long straddle buyers are betting against the market's own volatility forecast—a difficult edge to sustain.

## Measuring your true cost and payoff

Before entering a long straddle, calculate:

- **Total premium paid:** Call premium + put premium
- **Implied move (if you can find it):** Often published by brokers; equals roughly 0.6 × [implied volatility](/implied-volatility/) × \[current stock price\] × sqrt(days to event / 365)
- **Your breakeven points:** Strike price ± total premium
- **The math:** If implied move is smaller than your breakeven distance, the market is already telling you the odds are against you

## Strategic alternatives

Some traders enter a straddle only *after* earnings, when implied volatility has crushed but the stock is still making its post-earnings move. This avoids the pre-earnings premium inflation. Others use a [strangle](/strangle/) (wider out-of-the-money call and put) to reduce the upfront cost, though this requires a larger move to profit. Still others skip earnings volatility plays entirely and focus on volatility trading between earnings events, where the implied-realized volatility disconnect is more subtle and arguably more tradeable.

## See also

<div class="wiki-seealso">

### Closely related

- [Straddle](/straddle/) — long call + long put strategy fundamentals
- [Strangle](/strangle/) — wider-strike variant to reduce premium
- [Implied Volatility](/implied-volatility/) — the market's volatility forecast
- Volatility Crush — post-event volatility contraction
- [Time Decay (Theta)](/time-decay-theta/) — how options lose value over time
- Implied Move — calculating expected price swing from options

### Wider context

- Option Strategies — overview of directional and volatility bets
- Earnings Volatility Trading — specialized earnings plays
- Greeks (Options) — delta, gamma, theta, vega explained
- Volatility Trading — trading volatility as an asset class

</div>
