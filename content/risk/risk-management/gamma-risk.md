---
title: "Gamma Risk"
description: "The risk that delta accelerates in large moves, forcing costly hedging or locking in losses on short options."
keywords:
  - gamma exposure
  - option delta
  - options risk
  - volatility risk
  - rehedging costs
  - derivative risk
image: /svg/risk.svg
---

*A trader who is short an [option](/option/) benefits from [gamma](/gamma/) only as long as she rehedges perfectly. In reality, **gamma risk** is the cost of that imperfection—the losses that arise when the underlying moves faster than you can hedge, or when the true distribution of returns is fatter than your model assumes. For short [volatility](/implied-volatility/) positions, gamma risk is the risk that [gamma](/gamma/) will eat you.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Gamma Risk — key facts</div>

<img src="/svg/risk.svg" alt="An abstract editorial mark for risk management topics." />

<div class="wiki-infobox-caption">The acceleration of losses when you are short volatility.</div>

|   |   |
|---|---|
| **What it is** | The realised loss from large or sudden moves when your hedge lags the underlying |
| **Short explanation** | If you sold an option and delta jumped, your [dynamic hedge](/dynamic-hedging/) wasn't fast or cheap enough |
| **Source** | Discrete rebalancing, market gaps, wide [bid-ask spreads](/bid-ask-spread/), and fat tails in price moves |
| **Who feels it most** | Option sellers, short [volatility](/volatility-smile/) traders, and leveraged hedging desks |
| **Frequency** | Worst during crises, at [expiry](/expiration-date/), and in illiquid assets |

</aside>

## Why short gamma is a cost, not a benefit

A short [option](/option/) position has positive [gamma](/gamma/)—when the underlying moves, delta increases in your favour if you bought the option, or against you if you sold it. But that benefit is only theoretical if you can't rehedge instantly. The moment you are short [gamma](/gamma/), you are short the ability to buy low and sell high. Instead, you are forced to buy high and sell low: as the underlying rises, your short [call](/call-option/) becomes more in-the-money, so you must buy the underlying (at the higher price) to hedge; as it falls, you must sell (at the lower price). You realise losses on every rehedge.

The longer the moves and the wider the jumps, the worse this becomes. In [volatility](/volatility-smile/) trading, gamma risk is the trader's largest expense. An option desk that sells 100 vega of straddles is short 100 units of implied volatility but positive gamma. If realised [volatility](/historical-volatility/) exceeds implied, the desk profits; but the path matters. Large, discontinuous moves force expensive, urgent hedges even if the total realised volatility ends up below the implied level.

## Gamma accelerates around expiry

[Gamma](/gamma/) is highest when an option is at-the-money and close to [expiration](/expiration-date/). This is the combination every short-gamma trader fears. A small price move changes delta by 50%, 75%, or even more on the final day. If you sold a call strike near the current price with one day left, you are sitting on a hair-trigger hedge. A 0.5% move in the underlying can require you to hedge a 30-contract swing. If the market is illiquid or you are large, that hedge costs real money—perhaps far more than the option is worth.

This is why options markets often spike in volatility the day or week before major corporate events (earnings, central bank decisions). Traders, conscious of ending gamma risk, demand higher [option](/option/) prices as insurance—they are paying for the privilege of avoiding the hedging costs they'd face if they sold.

## Gamma and tail events

A second source of gamma risk is model risk. If you price an [option](/option/) assuming the underlying is [normally distributed](/implied-volatility/), you will underestimate the probability of large moves—the fat tails that reality produces. Real price returns are fat-tailed: 5% down days happen far more often than a bell curve predicts. When a 5% move happens, your [gamma](/gamma/) loss is far larger than your model thought it would be.

During the 2008 financial crisis and the 2020 COVID crash, traders who were short volatility were crushed. Models trained on 30 years of "normal" data failed to price the tail. Short-gamma hedges that seemed profitable on a 1% move were deadly on a 10% move. [Volatility](/historical-volatility/) jumped so fast that dynamic hedges couldn't execute; liquidity dried up; funding evaporated. The lesson: gamma risk includes the risk of model failure.

## Gamma, leverage, and funding stress

A hedge fund or bank running a large short-volatility book will use leverage to maximise returns. But leverage amplifies gamma pain. If you are 10:1 leveraged on a volatility short and [gamma](/gamma/) eats $10 million in rehedging costs, you've wiped out 10% of your capital and face forced selling of hedges. Worse, if your funding is short-term or conditional on posted collateral, a realised gamma loss can trigger a funding squeeze—you can't post collateral fast enough, your lender calls, and you are forced to exit at the worst moment.

This dynamic played a large role in the 2012 Knight Capital disaster, where a trading system left a short-volatility position unhedged overnight. A small market move turned into a $440 million loss within minutes because gamma accelerated losses faster than the system could hedge. [Funding liquidity risk](/funding-liquidity-risk/) turned a recoverable trading loss into a death spiral.

## Hedging gamma is expensive

The only way to avoid gamma risk is to buy [gamma](/gamma/)—in other words, to be long [options](/option/). A portfolio manager worried about downside can buy [puts](/put-option/), which are long gamma and will accelerate gains if the market crashes. A trader who wants to be long volatility can buy [straddles](/put-option/) or [options](/option/) outright. But long [gamma](/gamma/) is expensive: you pay the [option premium](/option-premium/), which includes a markup for the seller's hedging cost plus their profit. The gap between what you pay and what the option eventually costs (via [gamma](/gamma/) losses) is the seller's edge—it is profitable because gamma risk is real.

## Monitoring gamma: the second derivative

Traders track gamma separately from [delta](/delta/) for good reason. [Delta](/delta/) tells you directional exposure; [gamma](/gamma/) tells you the cost of being wrong. A portfolio can be delta-neutral but hugely long gamma (bullish on volatility), or delta-neutral and short gamma (bearish on volatility). The Greeks let you separate these bets. If your risk model shows delta near zero but gamma large and negative, you are a [volatility](/historical-volatility/) short—modest price moves won't hurt you, but big moves will. This distinction is central to derivatives risk management.

## See also

<div class="wiki-seealso">

### Closely related

- [Dynamic Hedging](/dynamic-hedging/) — the rebalancing strategy used to manage gamma risk
- [Delta](/delta/) — the first derivative; gamma is the second
- [Theta](/theta/) — time decay profit that short-gamma traders chase
- [Volatility Smile](/volatility-smile/) — why gamma varies by strike and time
- [Option Premium](/option-premium/) — the price you pay or receive
- [Bid-Ask Spread](/bid-ask-spread/) — the cost of executing hedges
- [Tail Risk](/tail-risk/) — the risk of extreme moves that breach gamma models
- [Funding Liquidity Risk](/funding-liquidity-risk/) — how funding constraints prevent hedging

### Wider context

- [Options](/option/) — the instrument creating gamma exposure
- [Implied Volatility](/implied-volatility/) — the volatility priced into an option
- [Hedge Fund](/hedge-fund/) — institutions managing complex gamma positions
- [Black-Scholes Model](/black-scholes-model/) — the framework for gamma and the greeks

</div>
