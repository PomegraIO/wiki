---
title: "Dispersion Trading"
description: "A volatility arbitrage selling index variance while buying single-stock variance to exploit correlation overpricing in options markets."
keywords:
  - dispersion trading
  - volatility arbitrage
  - correlation trading
  - options market
  - variance trading
  - index volatility
image: "/svg/strategies.svg"
---

*A **dispersion trade** exploits the tendency for options markets to overprice the correlation between stocks in an index. The trader sells [volatility](/volatility-smile/) on the index itself and buys [volatility](/volatility-smile/) on the constituent stocks, profiting if realised correlations turn out lower than the price implied by option premiums.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Dispersion Trading — key facts</div>

<img src="/svg/strategies.svg" alt="An abstract editorial mark for systematic trading strategies." />

<div class="wiki-infobox-caption">A market-neutral volatility trade betting that index correlation is overpriced relative to single-stock volatility.</div>

|   |   |
|---|---|
| **Core trade** | Short index variance, long constituent stock variance |
| **Implementation** | Sell index [options](/option/), buy a hedged basket of single-stock [options](/option/) |
| **Funding** | Typically requires options market access and derivatives financing |
| **Volatility target** | Realised correlation vs. implied correlation |
| **Holding period** | Days to weeks, or until expiration |
| **Key risk** | Correlation spikes; [gamma](/gamma/) losses; [bid-ask](/bid-ask-spread/) width |

</aside>

## How correlation gets priced into options

The price of a call or put on the S&P 500 index depends on the implied [volatility](/volatility-smile/) of the index itself. But the index is a weighted average of 500 stocks. Its [volatility](/volatility-smile/) is a function of two things: the individual [volatility](/volatility-smile/) of each stock and their correlation with each other.

When stocks move together (high correlation), the index swings more widely for a given set of stock moves. When stocks move independently (low correlation), diversification dampens index swings. Index [volatility](/volatility-smile/) = f(stock volatilities, correlations).

Options on the index are priced using this relationship. Market makers and traders embed assumptions about forward correlation into the index option [premium](/option-premium/). Similarly, single-stock options are priced using their own implied volatilities.

A dispersion trader observes a mismatch: "The index options imply correlation that is too high compared to what I expect realised correlation to be." The profit opportunity: buy individual stock [options](/option/) (which reflect lower [volatility](/volatility-smile/)) and sell index options (which reflect higher implied [volatility](/volatility-smile/), driven by high correlation assumptions), then collect the premium difference if realised moves prove less correlated.

## A simplified example

Suppose the S&P 500 trades at 4,000. Call on the index (one month to expiration) is priced with 12% implied [volatility](/volatility-smile/). The largest constituent stocks (Apple, Microsoft, Tesla, etc.) are each priced with 15–18% implied [volatility](/volatility-smile/).

Naively, you might expect the index [volatility](/volatility-smile/) to be lower than the component stocks (due to diversification), but it is not: the index option is priced at 12%, implying high correlation. The dispersion trader interprets this as correlation overpricing.

The trader might:
1. **Sell** 20 one-month S&P 500 calls (10 delta, sold at 12% IV).
2. **Buy** a hedged basket: long 5 Apple calls, 5 Microsoft calls, 5 Tesla calls, etc., at 16% IV; offset with short positions in lower-volatility names to balance the basket.

If correlations realise lower than priced (stocks move more idiosyncratically), the index option decays fast (no heavy index moves), while single-stock options retain value. The trader profits on the premium difference.

Conversely, if stocks move in lockstep and correlations are high, the index option gains value faster than the hedge, causing losses.

## Why dispersion occurs and when it thrives

**Macro shocks and fear.** During credit crises, geopolitical events, or earnings seasons for mega-cap tech, investors flock to index hedges (index options), bid up index call premiums, and ignore single-stock optionality. Index [volatility](/volatility-smile/) spikes relative to stock [volatility](/volatility-smile/), creating dispersion opportunity.

**Structural demand.** Index funds and passive managers are heavy users of index options for risk management. Pension funds buying index puts to hedge portfolios create persistent demand for index [volatility](/volatility-smile/). This structural bid inflates index option prices relative to single-stock options.

**Crowded flows.** When multiple systematic strategies (CTAs, [volatility](/volatility-smile/) funds, risk-parity funds) all move together, correlations spike, and index [volatility](/volatility-smile/) rises more than single-stock [volatility](/volatility-smile/) would suggest. Dispersion traders benefit as correlations later normalise.

**Low realised correlation regimes.** In periods when stocks genuinely diverge (selective sector strength, idiosyncratic news), realised correlations fall, and dispersion trades prosper.

## Implementation and hedge mechanics

A dispersion trade is not simply a pair bet. The mechanics are more sophisticated.

**Variance reduction.** A trader selling the index call is short index [gamma](/gamma/)—exposed to large moves. To isolate correlation risk, the trader buys single-stock [options](/option/) to offset this [gamma](/gamma/). The result: a position that is roughly [gamma](/gamma/)-neutral but short correlation.

**Hedging and rehedging.** As prices move, [gamma](/gamma/) exposures drift. Active dispersion traders rebalance daily (or more often), buying and selling stock calls and puts to stay market-neutral. This is labour-intensive and costly in [bid-ask spreads](/bid-ask-spread/).

**Correlation swaps and variance swaps.** Modern dispersion traders often use exotic derivatives (correlation swaps, variance swaps) to implement the trade more cleanly. A [variance swap](/variance-swap/) on the index minus a weighted basket of variance swaps on components replicates the trade with less rehedging.

**Position sizing.** Dispersion is a vega trade (sensitivity to [volatility](/volatility-smile/)), not a delta trade. Traders size positions by [vega](/vega/), not delta, aiming for constant [volatility](/volatility-smile/) exposure across the book.

## Risks and failure modes

**Correlation spike.** The biggest risk is a sudden jump in correlation when you are short the index. March 2020 saw all stocks selloff together; correlations approached 1.0. Dispersion traders short the index lost heavily.

**Gamma whipsaw.** Short [gamma](/gamma/) positions lose money if the underlying moves sharply either way. A trader can be right on correlation (stay low) but lose on [gamma](/gamma/) bleed from large daily moves.

**[Bid-ask spread](/bid-ask-spread/) and funding costs.** Building and rebalancing a hedged dispersion portfolio requires buying and selling many [options](/option/) at wide spreads, especially single-stock options on illiquid names. Over weeks or months, friction erodes the premium collected.

**Model risk.** Dispersion traders use correlation models to price the trade (often assuming a specific correlation structure or decay). If the model is wrong (e.g., correlation does not decay as expected), P&L differs from plan.

**Crowding.** Many sophisticated traders use dispersion models. If the trade becomes crowded, index option premiums compress, single-stock premiums rise, and the attractiveness of the trade evaporates.

## When dispersion works best

**Earnings seasons.** Earnings surprises are often idiosyncratic. Dispersion trades placed before earnings often profit as stocks move differently.

**Sector rotations.** When some sectors outperform others sharply, correlation falls. Dispersion thrives.

**Volatility regime changes.** Transitions from calm to stressed markets (or vice versa) often see correlation repricing.

**Structural shifts.** Passive index flows and [factor](/factor-investing/) flows can create persistent correlation distortions, creating sustained dispersion opportunity.

## Dispersion as part of a volatility book

Dispersion trading is typically one component of a broader [volatility](/volatility-smile/) trading desk. A hedge fund or bank running [volatility](/volatility-smile/) strategies might simultaneously:
- Trade [volatility](/volatility-smile/) term structure (buying near-term vol, selling longer-dated)
- Trade [volatility](/volatility-smile/) surface (exploiting [volatility smile](/volatility-smile/) shapes)
- Trade dispersion (short index correlation)

The net result is a diversified [volatility](/volatility-smile/) portfolio with multiple sources of edge.

## See also

<div class="wiki-seealso">

### Closely related

- [Volatility smile](/volatility-smile/) — the curve of implied volatilities across strikes; dispersion exploits the term structure
- [Variance swap](/variance-swap/) — a derivative for betting on realised vs. implied [volatility](/volatility-smile/)
- [Option](/option/) — the instrument underlying dispersion trades
- [Vega](/vega/) — sensitivity to [volatility](/volatility-smile/); the key Greek in dispersion
- [Gamma](/gamma/) — the curvature risk dispersion traders hedge out
- Correlation — the market variable dispersion traders exploit
- [Factor timing](/factor-timing/) — another systematic strategy; similar pricing model concepts

### Wider context

- [Hedge fund](/hedge-fund/) — typical vehicle for dispersion traders
- Volatility index — the VIX; a key benchmark for index [volatility](/volatility-smile/) moves
- [Carry strategy](/carry-strategy/) — another premium-harvesting trade; subject to similar tail risks
- Risk management — hedging demand that creates dispersion opportunity
- [Black-Scholes model](/black-scholes-model/) — the framework for pricing index and single-stock options

</div>
