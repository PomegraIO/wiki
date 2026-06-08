---
title: "Cross-Hedging"
description: "Using a correlated but different instrument to manage exposure when a direct hedge is unavailable, unwieldy, or too expensive."
keywords:
  - cross-hedge
  - proxy hedge
  - basis risk
  - imperfect hedge
  - commodity hedging
  - correlated instruments
image: "/svg/risk.svg"
---

*A **cross-hedge** is a risk-management technique in which a firm or investor hedges an exposure using a financial instrument that is correlated with, but not identical to, the underlying exposure. When a perfect hedge is unavailable, too expensive, or too illiquid, traders use a proxy. An airline unable to buy [futures contracts](/futures-contract/) on the specific jet fuel it consumes might hedge with [crude oil](/crude-oil/) futures instead, because crude and refined fuel prices move together. The airline sacrifices perfect protection for practical accessibility. The residual risk — the possibility that the two prices will diverge — is called [basis risk](/basis-risk/).*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Cross-Hedging — key facts</div>

<img src="/svg/markets.svg" alt="An abstract editorial mark for financial markets." />

<div class="wiki-infobox-caption">Using a correlated stand-in when the ideal hedge is unavailable or too costly.</div>

|   |   |
|---|---|
| **What it is** | Hedging an exposure with a different but correlated instrument |
| **Also called** | Proxy hedge, indirect hedge, surrogate hedge, cross-hedge ratio |
| **Typical motivation** | Unavailable direct hedge, illiquidity, cost, or regulatory restrictions |
| **Residual risk** | Basis risk; the price divergence between the hedge and the underlying exposure |
| **Correlation coefficient** | Key factor: higher correlation = more effective hedge, lower basis risk |
| **Common examples** | Crude oil futures for jet fuel; stock-index futures for a portfolio; Treasury futures for credit spreads |
| **Hedge ratio** | Often derived from regression; ratio of underlying to hedge instrument to minimise basis risk |

</aside>

## When a direct hedge is not available

The simplest hedge is a perfect match: a firm short (exposed to the downside of) a specific commodity buys a [futures contract](/futures-contract/) on that exact commodity. But the financial world often lacks perfect matches. A regional utility that buys natural gas from a small producer might find no liquid [futures contract](/futures-contract/) on that specific gas stream. The utility can buy [natural gas](/natural-gas/) futures on the NYMEX, which are highly correlated with the price it pays, but the correlation is not perfect — basis risk exists.

A small-cap equity investor concerned about portfolio [downside](/value-at-risk/) might want to hedge his individual stocks directly, but options on a micro-cap stock are nonexistent or prohibitively expensive. The investor can buy [put options](/put-option/) on the [S&P 500](/sp-500-index/), which is correlated with his portfolio but not identical. The hedge is imperfect, but it provides meaningful protection.

Cross-hedging is a pragmatic response to reality: perfect hedges are often unavailable, and the cost of achieving perfection (through custom derivatives or illiquid instruments) is not worth it.

## Basis risk: the cost of approximation

A cross-hedge introduces **basis risk** — the risk that the hedge instrument and the underlying exposure do not move in lockstep. Basis is the difference between the price of the underlying asset and the price of the hedge instrument. If an airline is long (exposed to high prices of) jet fuel and short (protected by owning) crude oil futures, the basis is the spread between the two. If the airline's hedge is perfect, the basis is constant and known; but in a true cross-hedge, the basis varies, and that variation can work for or against the airline.

Consider a specific scenario. Jet fuel is currently trading at $3 per gallon, crude oil at $80 per barrel (roughly 42 gallons). The airline buys crude futures to hedge anticipated jet fuel purchases. The crude-to-jet-fuel spread is stable at historically normal levels. Then, a refinery strike reduces jet fuel supply sharply, and jet fuel spikes to $4 per gallon, but crude stays at $80. The crude hedge has not risen by the same amount, so the airline's protection is incomplete. The airline faces basis risk — the exposure that refined products will move differently from the crude feedstock.

Basis risk is the price of using an imperfect hedge. A firm must decide whether the cost of basis risk is acceptable relative to the benefit of lower hedge cost or higher liquidity.

## Calculating the optimal hedge ratio

When hedging with a correlated instrument, the hedger often faces a choice: how many units of the hedge instrument should I buy to offset my exposure? This is the **hedge ratio problem**. If the underlying and hedge are perfectly correlated, the answer is straightforward (1:1, adjusted for contract size). If they are imperfectly correlated, the hedge ratio can be derived from regression analysis.

A firm might regress historical price changes of the underlying (say, jet fuel) against price changes of the hedge instrument (crude oil). The regression coefficient is the optimal hedge ratio that minimises basis risk. If the regression coefficient is 0.95, the firm should buy 0.95 units of the hedge for every unit of exposure. This ratio minimises expected basis risk.

In practice, hedge ratios are adjusted for contract specifications and the time horizon. A hedge of one month's purchases may use a different ratio than a hedge of one year, because correlations can shift over longer periods.

## Common cross-hedge examples

**Commodity producers and energy markets:** A small gold mine in a developing country may lack a [futures contract](/futures-contract/) specific to its deposit, so it hedges using gold futures on the COMEX (a global benchmark). The mine faces basis risk if its ore grade, purity, or production costs differ from COMEX assumptions, but the hedge is still vastly cheaper than a custom bilateral contract.

**Equity market hedges:** A portfolio manager holding stocks in Company A but concerned about a near-term market decline might buy [put options](/put-option/) on the S&P 500 rather than on Company A (whose options are illiquid). If Company A moves with the market, the hedge is effective; if Company A is uncorrelated, the hedge fails. This is a classic cross-hedge, with basis risk measured by the stock's [beta](/beta/) relative to the index.

**Interest-rate hedges:** A small bank lending to small businesses at floating rates faces [interest rate risk](/interest-rate-risk/). It may not have access to derivatives on small-business loan rates, so it hedges with Treasury futures or interest-rate swaps on benchmark rates (SOFR, federal funds). The correlation is high but not perfect; if credit spreads tighten or widen, basis risk materializes.

**Currency hedges:** A company importing from a small country might face no liquid [forwards](/forward-contract/) in that country's currency. It can hedge the exposure using a correlated major currency forward (e.g., if the small country's currency co-moves with the euro, hedge with euro forwards). Again, basis risk exists, but it may be acceptable.

## When cross-hedging makes economic sense

A cross-hedge is justified when the cost savings or liquidity gain outweigh the basis risk. If crude oil futures are 100 times more liquid than jet-fuel-specific derivatives, and the correlation is 0.95, the airline likely prefers the crude hedge. The 5% basis risk is the cost of accessing a deep, efficient market.

Cross-hedging is also common when a direct hedge would require an onerous accounting or regulatory burden. A bank might cross-hedge certain exposures using derivatives on highly correlated indices, rather than using bespoke instruments that would trigger complex ASC 815 accounting rules. The simplicity and regulatory clarity of using standardized instruments (even as a proxy) can be worth the basis risk.

Conversely, if the correlation is weak (below 0.8 or so) and the expense of a direct hedge is reasonable, a firm should pursue the direct hedge. A 20% mismatch in protection is not worth the savings.

## Dynamically managing basis risk

Sophisticated hedgers do not just set a cross-hedge and forget it. They monitor basis actively. If the correlation between the underlying and the hedge breaks down, the hedge ratio should be adjusted. If basis widens to historically unusual levels, the hedger might partially unwind the cross-hedge and replace it with a more direct (if more expensive) instrument.

Some firms use [dynamic hedging](/delta/), adjusting the hedge ratio continuously as the correlation and basis evolve. This is costly and is typically reserved for large exposures where the benefit is clear. A small regional utility might not dynamically rehedge a natural gas cross-hedge, accepting wider basis risk; an investment bank managing tens of billions in exposure would almost certainly do so.

## See also

<div class="wiki-seealso">

### Closely related

- [Natural hedging](/natural-hedging/) — operational matching; a different hedging approach that avoids basis risk entirely
- [Futures contract](/futures-contract/) — the instrument typically used in cross-hedges
- [Forward contract](/forward-contract/) — an alternative instrument for cross-hedging
- [Basis risk](/basis-risk/) — the core risk introduced by using a correlated substitute
- [Put option](/put-option/) — a tool for cross-hedging equity or index exposure

### Wider context

- [Correlation](/beta/) — the statistical relationship underlying a cross-hedge's effectiveness
- [Interest-rate risk](/interest-rate-risk/) — often managed through cross-hedges using Treasury instruments
- [Currency risk](/currency-risk/) — frequently hedged via correlated currency forwards
- [Volatility](/implied-volatility/) — impacts the cost of cross-hedging with options
- [Option premium](/option-premium/) — the cost of using puts in an equity cross-hedge

</div>
