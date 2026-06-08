---
title: "Short Straddle"
description: "An options strategy that sells both a call and put at the same strike, collecting premium when the underlying price stays flat, but facing unlimited risk on the upside."
keywords:
  - short straddle
  - options strategy
  - premium selling
  - naked call
  - naked put
image: "/svg/derivatives.svg"
---

*A **short straddle** is an options strategy in which an investor sells (writes) both a [call option](/call-option/) and a [put option](/put-option/) at the same [strike price](/strike-price/) and [expiration date](/expiration-date/). The position profits if the underlying asset stays flat or moves only modestly, collecting the [option premium](/option-premium/) as income, but faces unlimited loss if the asset moves sharply.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Short Straddle — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark representing derivatives and structured products." />

<div class="wiki-infobox-caption">Sell both call and put at the same strike; collect premium if price stays flat; lose if it moves sharply.</div>

|   |   |
|---|---|
| **Strategy type** | Premium collection; [volatility](/implied-volatility/) short (bets on low movement) |
| **Components** | Short [call option](/call-option/) + short [put option](/put-option/) at identical strike |
| **Maximum profit** | The total [option premium](/option-premium/) collected; realized only if expiration at strike |
| **Maximum loss** | Unlimited upside (theoretically); substantial downside (strike minus premium) |
| **Breakeven points** | Strike + total premium received (upside); strike - total premium received (downside) |
| **Best market outlook** | Low volatility; price expected to drift near strike; earnings or events unlikely to shock the market |
| **Time decay exposure** | Favourable; short options gain as expiration nears and value decays |

</aside>

## The mechanics of premium collection

A short straddle is the inverse of a [long straddle](/long-straddle/). Instead of buying both options, you sell them, immediately collecting the premium. Suppose you sell a call at a $100 strike for $3 and a put at the same strike for $2. You pocket $5 per share, or $500 on a 100-share contract, with no immediate outlay.

The catch is obligation. By selling these options, you are promising that if the stock rises above $103 (strike plus premium), you will buy it at $103 and sell it to the call holder at $100, locking in a loss. Or if the stock falls below $97 (strike minus premium), you will sell it to the put holder at $100 and buy it at $97, again locking in a loss. The maximum profit is $5 (the premium collected); the losses are theoretically unlimited upward and substantial downward.

This makes short straddles fundamentally a bet that the underlying will stay calm. Traders use them during low-volatility periods when large price moves are deemed unlikely.

## Why the upside risk is unlimited

The upside risk is the most dangerous feature of a short straddle. If you sell a naked (uncovered) call, there is theoretically no limit to how high the stock can rise. Your obligation to deliver shares at $100 becomes costlier the higher the price climbs. If the stock soars to $200, you are obligated to deliver at $100, realizing a $100 loss per share. At $500, the loss is $400 per share. There is no floor.

The downside risk is bounded by zero (the stock cannot fall below $0), but the loss is still substantial. If the stock crashes to $50, you are obligated to buy it at $100 from the put holder, realizing a $50 loss per share.

For most traders, the asymmetric risk is manageable only if the position is sized appropriately and monitored closely. Casual investors or those underestimating tail risk have been ruined by short straddles.

## Volatility and margin requirements

Short straddles are not for everyone. Most brokers require that the seller maintain sufficient margin (collateral) to cover potential losses. The margin requirement is often set as a percentage of the strike price, adjusted for implied volatility and time to expiration. In high-volatility environments, margin requirements spike, making short straddles expensive to maintain.

When [implied volatility](/implied-volatility/) is high, option premiums are higher, so a short straddle collected premium is larger, offering better compensation for risk. But brokers also demand more margin because the probability of large moves is elevated. Conversely, low volatility periods offer lower premiums but also lower margin requirements, making short straddles more accessible and capital-efficient.

This creates a paradox: traders would prefer to sell straddles when implied volatility is high (better premium, better risk-reward), but margin requirements are also high, eating into the capital efficiency of the trade.

## Time decay works in your favour

Where a [long straddle](/long-straddle/) suffers from [time decay (theta)](/time-decay-theta/), a short straddle benefits from it. As expiration approaches and the underlying does not move, both the call and put lose value. The seller pockets the difference: premium originally collected minus the (lower) cost to buy back the options at expiration. In the ideal scenario—where the stock is exactly at the strike on expiration—both options expire worthless, and the seller keeps the full premium.

This makes short straddles attractive to income-focused traders. They collect yield from the options they sell, and theta decay is an ally. However, this benefit is entirely conditional on the stock staying calm.

## When short straddles blow up: earnings and shocks

Short straddles are most profitable in stable environments but most dangerous when uncertainty suddenly spikes. An earnings announcement, regulatory decision, or geopolitical shock can trigger a large move that both legs of the straddle did not anticipate. The position that was "nearly certain" to expire with minimal loss suddenly requires margin to cover unrealised losses. Brokers may force closure at unfavourable prices.

The 2020 COVID crash is instructive: traders who had sold short straddles ahead of the earnings season faced margin calls as equity volatility spiked and portfolio value plummeted. Many were forced to cover positions at steep losses. The psychological pressure is intense: a profitable position quickly turns into a large loss, and emotion can override discipline.

## Iron condors and spreads as safer alternatives

Many traders uncomfortable with the unlimited upside risk of a short straddle use a [spread](/long-straddle/) instead. An iron condor, for example, combines selling a call and put (as in a straddle) but buys further out-of-the-money options to cap losses. This turns an unlimited-risk strategy into a defined-risk strategy at the cost of reduced maximum profit.

Similarly, some traders sell a straddle but immediately buy further out-of-the-money options (a "short strangle" ratio spread) to protect the upside. The protection is costly—it reduces the premium collected—but it converts a tail-risk strategy into something more moderately leveraged.

## Capital efficiency and professional use

Short straddles are common among professional option traders and market makers. They have the capital, risk management systems, and emotional discipline to run these positions. Professional traders monitor positions constantly, adjust hedges, and exit before losses become catastrophic. They also accept that some positions will blow up—it is part of the business—and size positions accordingly.

For retail investors, short straddles are genuinely dangerous. They require deep understanding of options, market microstructure, and tail risk. A single large move can wipe out months or years of collected premiums.

## See also

<div class="wiki-seealso">

### Closely related

- [Call Option](/call-option/) — the short-call component of the straddle
- [Put Option](/put-option/) — the short-put component of the straddle
- [Long Straddle](/long-straddle/) — the opposite strategy; buys call and put to profit from large moves
- [Option Premium](/option-premium/) — the income collected upfront in a short straddle
- [Time Decay (Theta)](/time-decay-theta/) — the daily erosion of option value that favours short straddles
- [Implied Volatility](/implied-volatility/) — high IV increases premium collected but also margin requirements

### Wider context

- [Option](/option/) — the foundational derivative underlying the strategy
- [Strike Price](/strike-price/) — the price at which both options are sold in a straddle
- [Tail Risk](/tail-risk/) — the extreme market moves that short straddles are poorly positioned to handle

</div>
