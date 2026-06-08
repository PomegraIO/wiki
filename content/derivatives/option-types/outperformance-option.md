---
title: "Outperformance Option"
description: "An exchange option that pays the positive difference in returns between two assets, allowing a bet on relative strength."
keywords:
  - outperformance option
  - exchange option
  - relative value
  - spread option
  - comparative performance
image: /svg/derivatives.svg
---

*An **outperformance option** is an [option](/option/) that pays off based on the outperformance of one asset relative to another. The holder gains if the first asset beats the second; if it does not, the option expires worthless or pays a minimum. It is a pure bet on comparative strength, not absolute price movement.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Outperformance Option — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives and exotic contracts." />

<div class="wiki-infobox-caption">A payoff tied to the relative performance of two assets.</div>

|   |   |
|---|---|
| **What it is** | An [option](/option/) that pays max(Asset A return − Asset B return, 0) |
| **Also called** | Exchange option, outperformance swap (if settled periodically) |
| **Payoff** | Positive difference in returns if Asset A outperforms |
| **Underlying** | Two [stocks](/stock/), [indices](/sp-500-index/), currencies, or [commodities](/crude-oil/) |
| **Exercise** | Usually European (at expiration) |
| **Use case** | Bet on relative value without absolute price bets |
| **Similar** | [Spread options](/credit-spread/), [calls](/call-option/) on [spreads](/credit-spread/) |

</aside>

## The structure: comparing two horses

Imagine an investor believes that Microsoft will outperform Apple over the next six months, but does not want to take a directional bet on the overall tech sector or the stock market. A straightforward pair trade—long Microsoft, short Apple—works, but ties up capital in a directional [hedge](/hedge-fund/) that neutralizes if both rise or both fall together.

An outperformance option removes that friction. The option pays off only if Microsoft's return exceeds Apple's, and the amount of profit is the difference. If Microsoft returns +20% and Apple returns +15%, the option holder pockets the 5% spread. If both return +25%, the option expires worthless (neither outperforms). If Microsoft returns +10% and Apple returns +25%, the option is out of the money and pays nothing.

This structure is pure relative value: the payoff ignores absolute market levels and sector movements. A investor can express a conviction about which company is cheaper, higher-quality, or better positioned without gambling on whether stocks in general go up or down.

## Why relative-value bets matter

Professional investors constantly form views on pairs of assets. A [hedge fund](/hedge-fund/) manager might believe an international [stock](/stock/) is cheaper than its US peer, or that a longer-dated [bond](/bond/) offers more upside than a shorter one. Historically, they would implement these bets through pair trades (long/short) or by buying one and shorting the other. But pair trades have drawbacks:

- They require margin or leverage, magnifying costs and risks.
- They assume the two assets move independently, which they often do not.
- An error in the hedge ratio can create hidden directional exposure.
- Borrowing to short the second asset (or bonds) can be expensive and unstable.

An outperformance option sidesteps these problems. The investor pays a single, known [premium](/option-premium/) upfront and has capped risk (the premium) while enjoying leveraged exposure to the relative move. If the outperformance happens, the payoff can be many times the cost.

## Pricing and the two-dimensional problem

Pricing an outperformance option requires modeling two correlated assets. If the underlying [stocks](/stock/) are perfectly correlated (they always move together), the option has no value—the difference in returns is always zero. If they are uncorrelated, there is high probability of outperformance, and the option is more valuable. The correlation is the key input.

Most quants use [Black-Scholes](/black-scholes-model/) variants for two assets, or Monte Carlo simulation for more complex scenarios. The [premium](/option-premium/) depends on:

- The [volatility](/historical-volatility/) of each asset
- The [volatility](/historical-volatility/) of their spread (difference in returns)
- The [correlation](/market-risk/) between them
- The [interest rate](/interest-rate/) (discounting)
- The time to expiration

A positive correlation lowers the option's value (less chance of large outperformance); negative correlation raises it. Investors with a bullish view on the correlation itself can profit by being long outperformance when correlations are expected to fall, making the relative move more likely.

## Real-world applications

**Equity long/short funds** use outperformance options as a cost-effective way to lever relative value convictions. Instead of short-selling a stock, they buy an outperformance option on a target stock versus a benchmark [index](/sp-500-index/).

**Credit analysts** use them on [bond](/bond/) [spreads](/credit-spread/). A trader convinced that a high-yield [bond](/bond/) will outperform a [Treasury](/treasury-bond/) over six months can buy an outperformance option on the issuer's [spread](/credit-spread/)—tighter [spreads](/credit-spread/) = outperformance.

**Currency traders** employ them to bet on relative currency strength. An outperformance option on the euro versus the pound, for example, pays if the euro rises more (or falls less) than the pound against a baseline.

**Commodity strategists** use them for relative-value bets within a sector: crude oil versus natural gas, copper versus gold. These pairs often have tactical misalignments, and an outperformance option lets the investor play the correction without short-selling.

**Asset allocation** at endowments or pension funds: a portfolio manager might buy an outperformance option on emerging-market [equities](/equity-etf/) versus US equities if they are tilting toward EM but want capped downside relative to the home market.

## Comparison with other relative-value derivatives

**Spread options** (e.g., [call options](/call-option/) on the spread itself) are similar but technically distinct. A spread option on the difference (A − B) can be struck at any level, not just zero. An outperformance option is a spread option with a strike of zero—it captures any positive difference.

**Ratio spreads** (buying more calls at one strike than selling at another) are a vanilla-option equivalent, but they require precise hedging and are sensitive to gamma risk.

**Pairs trading** via cash or [futures](/futures-contract/) is the simplest alternative: just go long one asset and short the other. But it ties up capital and requires active hedging.

**Outperformance swaps** are the longer-dated cousins of outperformance options; they often pay the cumulative outperformance over multiple periods.

## Risks and limitations

An outperformance option has a non-linear payoff. Small differences in returns pay nothing; large differences pay off linearly. This means the option is worthless if the two assets happen to perform nearly identically, even if both move sharply. An investor convinced of a large relative move must time or size the bet carefully.

Liquidity is another constraint. These options are less liquid than [standard options](/option/) on single assets. Bid-ask [spreads](/bid-ask-spread/) are wider, especially for unusual pairs. Retail investors almost never see them; they are primarily a wholesale, institutional product sold by investment banks.

**Model risk** is real. The [option](/option/) price is highly sensitive to correlation assumptions. If the true correlation differs from the market's assumption, both buyer and seller can suffer losses even if the relative prices move as expected.

And there is the **dividend/coupon problem**. If one of the underlying [stocks](/stock/) pays a dividend during the option's life, does the option measure total return (including dividends) or price return alone? This must be specified in the contract and affects pricing.

## Valuation insights

The [value](/fair-value/) of an outperformance option increases with the [volatility](/historical-volatility/) of the spread. If the historical spread between two [stocks](/stock/) is stable (low [volatility](/historical-volatility/)), the option is cheap because large outperformance is unlikely. If the spread is noisy and wide-ranging, the option is more expensive.

In periods of [market stress](/systemic-risk/), correlations tend to rise (all [stocks](/stock/) move together), and outperformance options become cheaper. In calm markets, correlations fall, spreads widen, and options become more expensive. This is the opposite of directional options, which are cheapest in low-volatility regimes—a useful asymmetry for portfolio hedging.

## See also

<div class="wiki-seealso">

### Closely related

- [Option](/option/) — the foundational derivative
- [Call Option](/call-option/) — a basic option type
- [Spread Option](/credit-spread/) — a payoff on the difference between two underlying prices
- [Exchange Option](/option/) — pays the higher of two assets at maturity
- [Futures Contract](/futures-contract/) — an alternative for directional bets
- [Volatility](/historical-volatility/) — a key driver of option pricing
- [Correlation](/market-risk/) — critical for pricing multi-asset derivatives

### Wider context

- [Hedge Fund](/hedge-fund/) — major users of relative-value derivatives
- [Pair Trading](/hedge-fund/) — the simpler alternative to outperformance options
- [Relative Valuation](/relative-valuation/) — the investment philosophy behind the bet
- [Capital Flows](/capital-flows/) — the macroeconomic driver of spread changes

</div>
