---
title: "Basis Risk in Hedging"
description: "Basis risk is the residual exposure when a hedge instrument does not move in lockstep with the underlying asset, leaving the hedger vulnerable to unfavorable price divergences."
keywords:
  - basis risk hedging
  - basis risk definition
  - imperfect hedge
  - cross-hedge
  - spot-forward divergence
image: "/svg/risk.svg"
---

*When you hedge an asset using a different contract or instrument that is not a perfect match, you introduce **basis risk**: the possibility that the hedge and the underlying will not move in sync, leaving you exposed to a loss even though you thought you were protected. Basis is the difference between the price of the cash asset and the price of the futures or derivative used to hedge it; basis risk is the uncertainty in how that gap will widen or narrow.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Basis Risk — key facts</div>

<img src="/svg/risk.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">The gap between what you're hedging and what you hedge with—a source of unintended loss.</div>

|   |   |
|---|---|
| **Root cause** | Imperfect correlation between hedge and underlying |
| **Common sources** | Instrument mismatch, maturity mismatch, geography mismatch |
| **Example** | Hedging aluminum prices with steel futures |
| **Effect on payoff** | Hedge may not fully offset the loss you were trying to prevent |
| **Impossible to eliminate** | Nearly always present unless you hedge with an identical contract |
| **Manageable through** | Better matching, diversification, [delta](/delta/) adjustment, [stress testing](/stress-testing/) |

</aside>

## Basis Risk vs. Market Risk

When you own an asset, you face market risk: if its price falls, you lose money. A hedge is supposed to offset that loss by profiting when the asset falls. If the hedge is perfect—you own the stock and short an identical futures contract—they move in lockstep and losses on one exactly match gains on the other.

In reality, most hedges are imperfect. You might:

- Own a specific asset but hedge with a broadly similar one (a farmer hedges wheat with corn futures because wheat futures are illiquid)
- Own a short-term obligation but hedge with a long-term instrument (a company hedges a 6-month loan with a 2-year [interest rate swap](/interest-rate-swap/))
- Own an asset in one geography and hedge with a contract in another (a European company hedges crude oil with a U.S. [crude oil futures](/crude-oil/) contract)

In each case, the hedge and the underlying are correlated but not identical. When they diverge—when the hedge falls less than the asset, or falls more—you feel the gap. That gap is basis risk.

## The Definition of Basis

**Basis** is defined as:

> Basis = Cash Price − Futures Price

For a [forward contract](/forward-contract/), basis measures the difference between what you can sell the asset for now (spot price) and what you will receive under a forward sold earlier. As delivery approaches, basis converges to zero—the cash price and the futures price must match at expiration, or arbitrage opportunities would be exploited away.

Before expiration, basis can be positive (cash > futures, the asset is in backwardation) or negative (cash < futures, the market is in [contango](/contango/)). Basis changes as time passes, interest rates shift, and supply-demand dynamics evolve. **Basis risk is the uncertainty about how basis will move.**

## Three Classic Basis Risk Scenarios

**Commodity hedging—the cross-commodity problem:**

A corn farmer in Iowa plants a large acreage and fears falling prices. She sells [corn futures](/corn/) contracts to lock in a price floor. But before harvest, a drought hits the region. Local cash corn becomes scarce and trades at a premium to the exchange-traded futures. The futures fall (as expected, reflecting weak demand elsewhere), but her local elevator is still paying her more than the futures price, because of a localized supply shock. She made less on the hedge than she expected, leaving her with less profit than if she had simply waited and sold cash corn without any hedge.

The "basis" here widened from a normal $0.15 premium (local corn typically trades 15 cents above futures, reflecting local storage and logistics) to a $0.50 premium. Her hedge was efficient on the downside but was gapped by a basis move outside her control.

**Interest-rate hedging—the maturity mismatch:**

A bank holds a large portfolio of 7-year mortgages funded by short-term deposits. To hedge [interest-rate risk](/interest-rate-risk/), it enters a 10-year [interest rate swap](/interest-rate-swap/). If 7-year rates and 10-year rates move together, the hedge works. But sometimes long-term rates fall more than short-term rates (the [yield curve](/yield-curve/) flattens), or vice versa. When the 10-year rate falls 40 basis points but the 7-year rate falls only 30 basis points, the bank's swap value rises less than the value of the underlying mortgages—an unhedged loss.

**Currency hedging—the spot-forward divergence:**

A U.S. company signs a contract to pay a European supplier 1 million euros in 90 days. It hedges by buying euros 90 days forward at a locked-in rate (e.g., 1.10 dollars per euro). But in those 90 days, [interest rate differentials](/interest-rate/) between the U.S. and Europe shift, changing the expected forward rate. The spot rate at payment day might be 1.12 dollars per euro, but the company is locked in at 1.10. The hedge worked. But what if the company's cash-flow forecast changes, and it only needs 750,000 euros? It must buy the full 1 million (or unwind at a cost), creating an unhedged long position in euros it no longer needs. The basis between the forward hedge and the actual cash need has widened.

## Why Basis Risk Cannot Be Eliminated (But Can Be Managed)

Basis risk is a fundamental feature of any hedge that is not a perfect replication. Perfect replication—owning the asset and shorting an identical futures contract—is rare:

1. **Liquidity:** The most liquid futures contract might be a different maturity or grade than what you need.
2. **Availability:** Your specific asset might not have a futures or swap market (a private company's stock, a unique real estate property).
3. **Regulation or convention:** You might be restricted from shorting certain instruments.
4. **Timing:** You hedge now, but the actual cash transaction is uncertain or variable in timing.

Given these constraints, you select the best available hedge—one highly correlated with your exposure—and accept that basis will shift.

## Measuring and Managing Basis Risk

Prudent hedgers monitor basis risk in several ways:

**Historical basis analysis:** Examine the history of the cash price and the hedging instrument. How wide and narrow has the basis been? What drove large basis movements? A basis that has ranged from -2 to +8 cents over 10 years is predictable; one that has occasionally jumped 50 cents is riskier and warrants deeper investigation.

**Cross-correlation:** Measure the correlation coefficient between the asset and the hedge. A correlation of 0.95 is strong (most moves are synchronized); 0.70 is moderate (larger divergences are possible); below 0.50 is weak and suggests the hedge is not suitable.

**[Stress testing](/stress-testing/):** Model scenarios—a sharp rate move, a supply shock, a currency crisis—and see how the basis behaves. If under stress the basis widens sharply, the hedge might amplify losses rather than prevent them.

**[Delta](/delta/) adjustment:** For derivatives, adjust the quantity of the hedge to account for imperfect correlation. If the underlying is 20% less volatile than the hedging instrument, reduce the hedge quantity by 20% to avoid over-hedging (and amplifying losses on the hedge side when the move goes the other way).

## The Cost-Benefit of Better Hedging

One way to reduce basis risk is to hedge with a better-matched instrument—at higher cost and lower liquidity. A farmer could hedge wheat with wheat futures (if liquid) rather than corn futures, or could use over-the-counter commodity swaps that are customized to the exact harvest date and grade. Each adds cost and complexity, but reduces basis risk.

The decision is economic: Does the cost of a tighter hedge (in commissions, bid-ask spreads, or structural complexity) justify the benefit of a narrower basis risk band? For a small farmer with 500 bushels, a customized OTC contract might cost $500 in embedded fees—a disproportionate expense. For a large producer with 50,000 bushels, the same $500 absolute cost is 0.1% of the commodity value, so the tighter hedge is worth it.

## Basis Risk in Real Time

When markets are calm and correlated, basis risk feels abstract. When a tail risk hits, basis risk becomes visceral. During the 2008 financial crisis, supposed hedges (like credit-hedging positions in "safe" instruments) suddenly diverged sharply from the underlying risks they were meant to offset—basis widened dramatically, leaving hedgers stunned by losses they thought they had eliminated.

This is why financial professionals distinguish between **theoretical hedge effectiveness** (how well the instruments correlate on average) and **stressed hedge effectiveness** (how well they move together in a crisis, when correlation often breaks down). A hedge that is 95% effective in normal times might be 60% effective in a market panic.

## See also

<div class="wiki-seealso">

### Closely related

- [Derivatives hedging](/derivatives-hedging/) — general framework for using contracts to offset risk
- [Delta](/delta/) — a measure of sensitivity that informs hedge ratios
- [Contango](/contango/) — when futures prices are higher than spot, affecting basis
- [Backwardation](/backwardation/) — when futures prices are lower than spot
- [Interest rate risk](/interest-rate-risk/) — a common context for basis risk in fixed-income hedges
- Correlation — how closely two price series move together
- [Stress testing](/stress-testing/) — evaluating hedge performance in extreme scenarios
- Cross-hedge — hedging with an imperfect but correlated instrument

### Wider context

- [Counterparty risk](/counterparty-risk/) — another form of residual risk in hedged positions
- [Volatility smile](/volatility-smile/) — why hedging costs differ across strike prices
- [Forward contract](/forward-contract/) — the simplest form of hedge, and a source of basis risk

</div>
