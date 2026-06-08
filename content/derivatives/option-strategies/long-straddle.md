---
title: "Long Straddle"
description: "An options strategy that buys both a call and put at the same strike and expiration, profiting from large moves in either direction while remaining neutral on direction."
keywords:
  - long straddle
  - options strategy
  - call option
  - put option
  - volatility trading
image: "/svg/derivatives.svg"
---

*A **long straddle** is an options strategy in which an investor buys both a [call option](/call-option/) and a [put option](/put-option/) at the same [strike price](/strike-price/) and [expiration date](/expiration-date/). The position profits if the underlying asset moves sharply in either direction, making it a bet on volatility rather than direction.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Long Straddle — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark representing derivatives and structured products." />

<div class="wiki-infobox-caption">Buy both call and put at the same strike; profit from large moves; lose if the asset stays flat.</div>

|   |   |
|---|---|
| **Strategy type** | [Volatility](/implied-volatility/) trade; direction-neutral |
| **Components** | Long [call option](/call-option/) + long [put option](/put-option/) at identical strike |
| **Maximum profit** | Unlimited (theoretically, if price rises sharply); limited on downside by strike price minus [option premium](/option-premium/) |
| **Maximum loss** | The total [option premium](/option-premium/) paid for both options |
| **Breakeven points** | Strike + total premium paid (upside); strike - total premium paid (downside) |
| **Best market outlook** | High [volatility](/implied-volatility/) or uncertain moves; earnings announcements, regulatory decisions |
| **Time decay exposure** | High; the position loses value daily if the asset does not move |

</aside>

## Why buy both call and put?

A long straddle is fundamentally a bet that the underlying asset will move significantly but with no conviction about direction. If you buy a call, you profit if the price rises—but if it falls, you lose your premium. If you buy a put, you profit if the price falls—but if it rises, you lose that premium too. A straddle combines both: whichever direction the asset moves, one leg becomes profitable while the other expires worthless.

The strategy shines during periods of uncertainty. Before earnings announcements, a company's stock often trades in a tight range as traders await the news. An options trader who believes the earnings will trigger a large move—but is uncertain whether it will be positive or negative—can buy a long straddle. If the stock surges on strong earnings, the call becomes [in-the-money](/in-the-money/); if the earnings disappoint and the stock crashes, the put becomes in-the-money. Either outcome profits.

This makes the long straddle an ideal vehicle for volatility trading. It is not a bet on the direction of the market or the stock; it is a bet that the [implied volatility](/implied-volatility/) and subsequent realized volatility will exceed the premium paid upfront.

## The cost and the breakeven calculation

Both a call and a put have a non-zero premium. Buying a straddle requires paying both premiums, which is the strategy's core cost. Suppose you buy a call and put, both at a $100 strike, paying $3 for the call and $2 for the put. Your total outlay is $5 per share, or $500 for a 100-share contract.

For the position to break even, the stock must move $5 away from the strike in either direction. The upside breakeven is $105 (strike plus total premium), and the downside breakeven is $95 (strike minus total premium). The stock can move anywhere within the range $95–$105 and the position will lose money. Only moves beyond those boundaries generate profit.

This is the straddle's defining trade-off: unlimited profit potential (theoretically, upward) or substantial downside (downward to zero), but breakeven requires a move larger than the premium cost. In high-volatility environments, large moves are more likely, justifying the premium. In calm markets, the premium becomes dead weight.

## Time decay and gamma

A long straddle is vulnerable to [time decay](/time-decay-theta/)—the erosion of option value as expiration nears. Each day that passes, both the call and put lose value if the underlying asset remains unchanged. This is a daily drag on the position, quantified by "theta" in options markets. A straddle's theta is always negative because both long options bleed value over time.

Offsetting this is [gamma](/gamma/)—the rate at which an option's delta changes. A long straddle has positive gamma, meaning that large moves generate disproportionately large gains. If the stock jumps $10 in a day, the option values spike, more than compensating for theta decay. But if the stock drifts sideways, theta wins and the straddle decays.

The tension between positive gamma and negative theta is central to straddle trading. Traders in straddles are essentially betting that gamma will outpace theta—that the stock will move enough, soon enough, to offset time decay.

## Volatility crush and the perils of post-earnings

A long straddle is often deployed just before earnings announcements or major news events, when [implied volatility](/implied-volatility/) is elevated. Options are most expensive when uncertainty is highest. However, implied volatility often collapses after the event, even if the stock has moved. If earnings are announced and the stock surges 8 percent, the call is [in-the-money](/in-the-money/) but the put's premium has collapsed as volatility shrinks. The position may still be profitable (because the call gained more than the put lost), but less so than anticipated.

This "volatility crush" is a classic straddle pitfall. A trader who bought a straddle expecting a massive move after earnings but did not account for the volatility collapse might find that the realized profit is far smaller than expected. The stock moved, but option prices did not move as much because the uncertainty that inflated them has been resolved.

## Comparison to other volatility strategies

A long straddle is one of several ways to bet on volatility. A [long-strangle](/long-straddle/) (buying a call and put at different strikes, further out of the money) is cheaper but requires an even larger move to profit. A long [volatility](/implied-volatility/) strategy using variance swaps or [volatility](/implied-volatility/) indices directly is less path-dependent. An [iron condor](/long-straddle/) or similar spread strategy collects premium by selling further out-of-the-money options while holding straddle-like long options.

Most straddle traders do not hold to expiration. Instead, they close the position once the stock has moved sufficiently that the profitable leg has compensated for the premium paid and theta decay. This is active management of gamma and theta, trying to capture gains before time decay erodes them.

## Sizing and risk management

A long straddle's maximum loss is defined and limited—it equals the total premium paid. This is a feature that attracts traders: risk is bounded. However, the probability of reaching maximum loss is high in calm markets, and the expected loss (accounting for theta decay and the cost of being wrong on timing) can be substantial.

Many traders limit straddle positions to a small portion of their portfolio, treating them as tactical bets on specific events rather than core holdings. Position sizing is critical: a trader might allocate only 2–3 percent of capital to any single straddle because the probability of profit depends heavily on the timing and magnitude of the move.

## See also

<div class="wiki-seealso">

### Closely related

- [Call Option](/call-option/) — the long-call component of the straddle
- [Put Option](/put-option/) — the long-put component of the straddle
- [Short Straddle](/short-straddle/) — the inverse strategy: selling both call and put to collect premium
- [Option Premium](/option-premium/) — the cost paid for both options in the straddle
- [Implied Volatility](/implied-volatility/) — the expected future volatility priced into options; high IV makes straddles expensive
- [Time Decay (Theta)](/time-decay-theta/) — the daily erosion of option value that works against long straddles

### Wider context

- [Option](/option/) — the foundational derivative instrument underlying the strategy
- [Volatility Smile](/volatility-smile/) — the pattern of option prices across strikes that affects straddle costs
- [Strike Price](/strike-price/) — the price at which both the call and put are struck in a straddle

</div>
