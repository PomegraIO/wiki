---
title: "Derivatives Hedging"
description: "The use of derivatives to offset or reduce risk in an underlying asset or liability."
keywords:
  - hedging
  - derivatives hedging
  - hedge ratio
  - risk management
  - hedge effectiveness
image: "/svg/derivatives.svg"
---

*A **derivatives hedge** is a financial transaction using [options](/option/), [futures](/futures-contract/), or [swaps](/derivatives-hedging/) to reduce or eliminate exposure to adverse price or rate movements in an underlying asset, liability, or cash flow. Hedging trades off potential upside for downside protection, stabilising returns and enabling business planning.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Derivatives Hedging — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract mark representing the balance of risk and protection." />

<div class="wiki-infobox-caption">Offsetting risk in one direction by taking controlled risk in another.</div>

|   |   |
|---|---|
| **What it is** | Use of derivatives to reduce undesired [price](/price-discovery/) or [interest-rate risk](/interest-rate-risk/) |
| **Also called** | [Hedging](/derivatives-hedging/), risk management, risk offset |
| **Common tools** | [Futures](/futures-contract/), [options](/option/), [swaps](/derivatives-hedging/), [forwards](/forward-contract/) |
| **Core measure** | [Hedge ratio](/derivatives-hedging/)—the proportion of underlying exposure offset |
| **Accounting** | May qualify for [hedge accounting](/derivatives-hedging/) under [IFRS](/international-financial-reporting-standards/) or [GAAP](/generally-accepted-accounting-principles/) |
| **Tradeoff** | Protection costs; upside is limited |

</aside>

## Why hedging exists

An exporter invoiced in a foreign currency faces [currency risk](/currency-risk/). If the [dollar](/us-dollar/) strengthens before payment arrives, the home-currency value of revenue falls. A farmer planting corn knows the harvest price is uncertain; a sharp decline could erase profit. A pension fund holding long-term [bonds](/bond/) fears [interest-rate](/interest-rate/) rises, which would erode the [present value](/discount-rate/) of future payments. These are genuine economic exposures, and they matter. A [hedge](/derivatives-hedging/) acknowledges that risk and transfers it to someone willing to bear it.

Hedging is not speculation. A speculator bets on price direction. A hedger aims to neutralize exposure to that direction. The exporter who sells [currency forwards](/forward-contract/) is not trying to profit from [exchange-rate](/currency-risk/) moves; they are fixing the home-currency revenue in advance, regardless of where the spot rate drifts. The farmer who buys [put options](/put-option/) on corn futures locks in a minimum price, capping downside while retaining upside if prices rally. The pension fund that sells [bond futures](/futures-contract/) temporarily reduces [duration](/duration/) [risk](/interest-rate-risk/), protecting the [present value](/discount-rate/) of liabilities.

## The mechanics of hedging

The simplest hedge is a [forward](/forward-contract/) contract. An importer due to pay €1 million in three months can enter a [forward](/forward-contract/) to buy euros today at a fixed rate, eliminating [currency risk](/currency-risk/). The cost is that the importer forgoes any gain if the [euro](/currency-risk/) weakens; the benefit is certainty.

[Options](/option/) add flexibility. Instead of a [forward](/forward-contract/), the importer can buy a [call option](/call-option/) on euros. If the [euro](/currency-risk/) strengthens, they exercise the [call](/call-option/), capping their cost at the [strike price](/strike-price/). If it weakens, they let the [call](/call-option/) expire and buy at the lower spot rate, pocketing the saving. The price of this asymmetry is the [option](/option/) premium paid upfront.

[Futures](/futures-contract/) are another workhorse. A farmer with 100,000 bushels of corn to harvest in six months fears a price collapse. Selling [futures](/futures-contract/) now locks in a forward price; gains or losses on the cash position are offset by losses or gains on the [futures](/futures-contract/) leg. As harvest approaches, the basis—the gap between cash price and [futures](/futures-contract/) price—typically narrows, making [futures](/futures-contract/) an effective short-term [hedge](/derivatives-hedging/).

[Swaps](/derivatives-hedging/) allow more complex rebalancing. A [corporation](/corporate-income-tax/) with floating-rate debt fears [interest-rate](/interest-rate/) rises. Entering a [swap](/derivatives-hedging/) to pay fixed and receive floating converts the effective liability to a fixed rate. The [swap](/derivatives-hedging/) [counterparty](/counterparty-risk/)—often a [bank](/bank-of-america/)—bears the opposite [interest-rate risk](/interest-rate/), and both parties reduce their exposure to rate shocks.

## Measuring hedge effectiveness

A hedge is useful only if it actually reduces risk. The **[hedge ratio](/derivatives-hedging/)** quantifies this: it is the ratio of the [derivative](/derivatives-hedging/) notional to the underlying exposure. If a firm holds $10 million of [stocks](/stock/) and sells $5 million of [futures](/futures-contract/), the ratio is 0.5—a 50% hedge. A ratio of 1.0 is a full, or "perfect," hedge (in theory); ratios above 1.0 are over-hedges, reversing exposure.

The **beta** of the underlying relative to the [futures](/futures-contract/) contract matters. If the firm's stock portfolio has a [beta](/beta/) of 1.2 relative to the [index](/sp-500-index/) that the [futures](/futures-contract/) track, then to achieve a 1:1 offset, the [futures](/futures-contract/) position must be 1.2 times the notional value of the stock. Ignoring [beta](/beta/) leaves the hedge imperfect, with residual [market risk](/market-risk/).

A hedge's **effectiveness** is tested regularly—quarterly, or monthly for major positions. The [variance](/interest-rate-risk/) of the hedged portfolio should be lower than the unhedged portfolio. If a [hedge](/derivatives-hedging/) intended to offset [interest-rate risk](/interest-rate-risk/) actually leaves [interest-rate risk](/interest-rate-risk/) largely intact, accounting rules may disallow [hedge accounting](/derivatives-hedging/) benefits, forcing mark-to-market of the [derivative](/derivatives-hedging/) and potentially large earnings swings.

## The types of hedges in practice

**Macro hedges** protect entire portfolios or balance sheets against broad market moves. A [hedge fund](/hedge-fund/) with net long [equity](/stock/) exposure might buy [put options](/put-option/) on a broad [index](/sp-500-index/) or sell [index futures](/futures-contract/) to reduce [systemic risk](/systemic-risk/). A [REIT](/real-estate-investment-trust/) manager might hedge [interest-rate risk](/interest-rate-risk/) across the whole portfolio using [bond](/bond/) [futures](/futures-contract/).

**Micro hedges** protect specific positions. A [mutual fund](/mutual-fund/) holding one [technology](/sp-500-index/) stock with high [volatility](/historical-volatility/) might buy [put options](/put-option/) on that single name. An exporter with a one-off invoice in a foreign currency buys a [forward](/forward-contract/) to lock in [exchange rates](/currency-risk/).

**Natural hedges** exploit correlations without [derivatives](/derivatives-hedging/). A company with revenues in [euros](/currency-risk/) and costs in [euros](/currency-risk/) is naturally hedged against [currency moves](/currency-risk/); [euro](/currency-risk/) [volatility](/historical-volatility/) impacts both arms equally. Similarly, a [bank](/bank-of-america/) holding both [fixed-rate mortgages](/fixed-rate-mortgage-personal/) and [time deposits](/interest-rate/) is partly hedged if rates move in tandem.

**Dynamic hedges** are rebalanced frequently. A dealer selling an [option](/option/) continuously buys and sells the underlying stock to remain [delta](/delta/)-neutral (immune to small underlying price moves). As the [option](/option/) [delta](/delta/) changes, so does the hedge ratio. This is expensive in [commissions](/bid-ask-spread/) and [bid-ask spreads](/bid-ask-spread/), but is essential for managing short [option](/option/) positions.

## Costs and tradeoffs

Every [hedge](/derivatives-hedging/) has a cost. [Futures](/futures-contract/) and [forwards](/forward-contract/) have [bid-ask spreads](/bid-ask-spread/) and potentially [margin](/leverage-ratio-forex/) or [collateral](/counterparty-risk/) requirements. [Options](/option/) demand upfront [premiums](/option-premium/). [Swaps](/derivatives-hedging/) embed dealer markups and [counterparty risk](/counterparty-risk/). Over a year, [hedging](/derivatives-hedging/) costs can reduce returns by 0.5% to 2%, depending on the instrument and [volatility](/historical-volatility/).

A hedger also faces the **regret tradeoff**. If the [hedge](/derivatives-hedging/) kicks in and the adverse move never occurs, the hedger has paid for insurance that was not needed. An exporter who buys [currency forwards](/forward-contract/) and the [currency](/currency-risk/) declines feels regret; they would have been better off unhedged. This is rational: [hedging](/derivatives-hedging/) is insurance, and insurance has a cost.

Basis risk—the gap between the [hedge](/derivatives-hedging/) instrument and the underlying exposure—is also ever-present. A farmer hedging corn with [corn futures](/futures-contract/) may find that local cash prices diverge from [futures](/futures-contract/) prices due to local supply or transport costs. The [hedge](/derivatives-hedging/) may not be 1:1 effective. More exotic exposures, such as [company-specific credit risk](/credit-risk/), are harder to hedge, and bespoke [swaps](/derivatives-hedging/) may be the only option—at high cost.

## Accounting and disclosure

Under [IFRS 9](/international-financial-reporting-standards/) and [ASC 815](/generally-accepted-accounting-principles/), a [hedge](/derivatives-hedging/) that meets strict criteria can qualify for [hedge accounting](/derivatives-hedging/). The [derivative](/derivatives-hedging/) gain or loss is deferred in other comprehensive income and released to the [income statement](/income-statement/) alongside the gain or loss on the hedged item. This reduces earnings volatility. Non-qualifying [hedges](/derivatives-hedging/), by contrast, are marked-to-market with gains and losses hitting net income each period—often creating large, seemingly erratic swings.

Documentation and testing are mandatory. A firm must formally identify the relationship between the [hedge](/derivatives-hedging/) and the underlying, measure [hedge](/derivatives-hedging/) effectiveness, and reassess periodically. Failure to maintain documentation can trigger derecognition, forcing all accumulated gains and losses to [income](/income-statement/) in one period. For large [hedges](/derivatives-hedging/), this can be material.

## See also

<div class="wiki-seealso">

### Closely related

- [Option](/option/) — primary hedging tool for asymmetric protection
- [Futures Contract](/futures-contract/) — workhorse for macro and commodity hedges
- [Forward Contract](/forward-contract/) — simplest hedging instrument for specific exposures
- [Synthetic Position](/synthetic-position/) — combines hedges to engineer desired payoff profiles
- [Contingent Claim](/contingent-claim/) — the class of [derivatives](/derivatives-hedging/) used in hedges
- [Delta](/delta/) — key measure for dynamic [option](/option/) hedging

### Wider context

- [Volatility Smile](/volatility-smile/) — impacts the cost of [option](/option/) hedges
- [Counterparty Risk](/counterparty-risk/) — consideration for [swap](/derivatives-hedging/) hedges
- [Interest-Rate Risk](/interest-rate-risk/) — major target of [bond](/bond/) and [swap](/derivatives-hedging/) hedges
- [Currency Risk](/currency-risk/) — hedged via [forwards](/forward-contract/) and [options](/option/)
- [Market Risk](/market-risk/) — offset by [index](/sp-500-index/) [futures](/futures-contract/) and [options](/option/)
- [Value at Risk](/value-at-risk/) — used to quantify [hedging](/derivatives-hedging/) effectiveness

</div>
