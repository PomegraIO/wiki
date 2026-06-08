---
title: "Gamma Hedging"
description: "Rebalancing a delta-neutral portfolio to keep it hedged as prices move, offsetting the decay or gain from gamma."
keywords:
  - gamma hedging
  - delta neutral
  - rehedging
  - gamma risk
  - portfolio rebalancing
image: "/svg/risk.svg"
---

*A **gamma hedge** is not a position you buy once and hold. It is the continuous rebalancing needed to keep a [delta-neutral](/delta/) portfolio in balance as prices move. Gamma—the rate of change of delta—forces you to buy as prices rise and sell as prices fall, or vice versa, depending on your exposure.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Gamma Hedging — key facts</div>

<img src="/svg/risk.svg" alt="An abstract editorial mark for risk and hedging." />

<div class="wiki-infobox-caption">A dynamic hedge; static is a mirage.</div>

|   |   |
|---|---|
| **What it is** | Rebalancing a [delta](/delta/)-neutral portfolio to remain hedged as the underlying price moves |
| **Also called** | Rehedging, dynamic hedge, gamma management |
| **Why it matters** | Without rehedging, a delta-neutral position drifts and becomes exposed to large price moves |
| **Key risk** | Transaction costs reduce net profit; poor rehedging timing locks in losses |
| **Time frame** | Continuous or frequent, depending on market volatility and position size |
| **Typical setting** | [Options](/option/) portfolios, [hedged equity](/equity-financing/) strategies, market-making |

</aside>

## Delta moves; therefore gamma exists

To understand gamma hedging, you must first accept that no delta-neutral position remains delta-neutral. The moment price moves, delta changes. If you are short [calls](/call-option/) against a long stock position, a price rise makes you more short (more negative delta), and you must buy stock to rebalance. A price fall makes you less short (less negative delta), and you must sell stock. This mechanical rebalancing process is gamma hedging.

[Gamma](/gamma/) is the Greek that measures how much delta changes for a unit move in the underlying price. It is positive for long [options](/option/) positions and negative for short options. A portfolio with positive gamma becomes more profitable as volatility drives larger price swings, because you are forced to buy low and sell high. A portfolio with negative gamma bleeds money during volatile price moves, because you are forced to sell low and buy high.

A gamma-neutral portfolio—built carefully with a mix of long and short options at different [strikes](/strike-price/)—does not need constant rehedging. But most trading desks do not construct portfolios from scratch to be gamma-neutral. They build them to be delta-neutral at inception, then they manage gamma as a separate risk.

## The rhythm of rebalancing

A typical scenario: you sell [covered calls](/covered-call/) against a stock holding. At inception, delta is zero (the short calls are offset by the long stock). The stock price rises 5%. Delta is now positive—you own more optionality than you've sold. You must sell stock to re-neutralise. The stock price then falls 10%. Delta is now negative—your sold calls are now deeper out of the money, and your stock position is unhedged. You must buy stock back.

Each rebalance incurs transaction costs: commissions, [bid-ask spreads](/bid-ask-spread/), market impact. In calm markets, rehedging costs are small, and the gains from gamma can exceed them. In volatile markets, rehedging costs rise, and a short-gamma position bleeds noticeably.

The frequency of rehedging is a tactical choice. Rehedge daily, and you capture more small moves but pay more in transaction costs. Rehedge weekly, and you reduce costs but risk being forced into a large rehedge if volatility spikes. The optimal frequency depends on the [volatility](/volatility-smile/) regime, the size of the position, and the liquidity of the underlying.

## Who benefits and who pays

A long-gamma trader is long [volatility](/historical-volatility/). They profit if the underlying price swings widely, because they rehedge at favourable prices. An option buyer—someone long calls or puts—has positive gamma. A market maker who is long options to hedge customer flow is long gamma. As prices move, they rehedge, locking in small profits from the spread between adjacent rehedges.

A short-gamma position is short volatility. If you sell straddles or strangles, or if you are a market maker short options without a long-option hedge, you are short gamma. As prices move, you are forced to rehedge unfavourably—buy after the stock has risen, sell after it has fallen. Over many rehedges, your losses accumulate.

Central to this is the [time-value](/theta/) tension: short options earn theta (time decay) but lose from gamma (rehedging costs). Long options lose theta but win from gamma. The interaction between these Greeks is where options traders make or lose money. A trader with both a long-gamma position and positive theta (earned from selling options elsewhere) is in the enviable position of profiting from both time decay and volatility.

## The cost of staying flat

Delta-neutral positions are expensive to maintain. Every rehedge costs money in spread and commission, and every rehedge locks in a decision at a particular price. If you rehedge after a sharp move and the move reverses, you have sold high or bought low only to have the benefit wiped out by the reversal.

Worse, in truly illiquid markets, rehedging may be impossible at reasonable prices. A dealer holding a large long options position may find that rehedging a negative gamma shift requires selling a large amount of stock at a wide spread. The cost of neutralising is higher than the position can absorb. This is a form of [liquidity risk](/liquidity-risk/), and it is real.

Over time, successful gamma management comes down to buying volatility when it is cheap and selling when it is rich, then rehedging through the subsequent price moves. If you misjudge—selling volatility that turns out to be cheap or buying volatility that turns out to be expensive—rehedging costs will overwhelm your profit.

## The practise: simulation and stress-testing

Professional options traders use Monte Carlo simulations to forecast the cost of gamma under various volatility and price-move scenarios. They might simulate 10,000 paths of the underlying price, rehedge along each path at their chosen frequency, and estimate the distribution of profit and loss. This reveals whether their [option premium](/option-premium/) is enough to cover expected rehedging costs, transaction friction, and idiosyncratic bad luck.

They also stress-test against past crises: what if the stock gaps up 10% overnight, and I cannot rehedge immediately? What if volatility spikes from 20% to 80% and every rehedge is forced at the widest spread? These stress scenarios are where real trading desks distinguish themselves from textbook theory.

## See also

<div class="wiki-seealso">

### Closely related

- [Delta](/delta/) — the sensitivity of an option or portfolio to the underlying price
- [Theta](/theta/) — time decay in an [option](/option/) position
- [Volatility smile](/volatility-smile/) — variation in implied volatility across strike prices
- [Proxy hedging](/proxy-hedging/) — substituting a correlated instrument when direct hedging is impractical
- [Duration hedging](/duration-hedging/) — maintaining constant interest-rate sensitivity
- [Convexity hedging](/convexity-hedging/) — managing second-order interest-rate sensitivity

### Wider context

- [Options pricing](/black-scholes-model/) — the mathematics of fair option value
- [Implied volatility](/implied-volatility/) — the volatility implied by an option's market price
- Greeks — sensitivity measures for derivatives
- Hedging — offsetting risk via financial instruments
- Dynamic replication — continuously rebalancing to replicate a derivative payoff

</div>
