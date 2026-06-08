---
title: "Contingent Claim"
description: "A financial contract whose payoff depends on the realisation of an uncertain future event or market price."
keywords:
  - contingent claim
  - derivative
  - option
  - payoff contingent
  - event-driven payoff
image: "/svg/derivatives.svg"
---

*A **contingent claim** is any financial obligation whose value and payoff are determined by one or more uncertain future events or price movements. [Options](/option/), [bonds](/bond/) with embedded provisions, [insurance](/auto-insurance/), and weather [derivatives](/option/) are all contingent claims—their worth hinges entirely on what the world does next.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Contingent Claim — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract mark representing conditional financial obligations." />

<div class="wiki-infobox-caption">A promise to pay if and only if a condition is met.</div>

|   |   |
|---|---|
| **What it is** | Any payoff that depends on a random or uncertain future event |
| **Also called** | Derivative, derivative claim, derivative security, conditional claim |
| **Key feature** | Value is zero if the condition is not met; positive if the condition is met |
| **Holders** | Investors, [corporations](/corporate-income-tax/), risk managers, [hedge funds](/hedge-fund/) |
| **Price drivers** | [Volatility](/historical-volatility/), time to maturity, the probability of the contingency |
| **Valuation method** | [Risk-neutral pricing](/option-premium/), [Monte Carlo](/discounted-cash-flow-valuation/), [Black-Scholes](/black-scholes-model/) |

</aside>

## Anatomy of contingency

The concept is simple: a contingent claim pays off *if and only if* a specific condition occurs. A [call option](/call-option/) on Apple [stock](/stock/) at a $150 strike is a contingent claim that pays the [stock](/stock/) price minus $150 if the [stock](/stock/) price closes above $150 at maturity, and pays zero otherwise. A [bond](/bond/) with a provision that allows the issuer to redeem early is contingent: the bondholder's right to receive all remaining coupons becomes conditional on the issuer choosing not to exercise. A [knockout option](/option/)—an [option](/option/) that expires worthless if the underlying breaches a barrier—is contingent on the underlying never reaching that barrier.

The payoff structure of a contingent claim is defined by the underlying state at a specified future date. The underlying might be a [stock](/stock/) price, an [interest rate](/interest-rate/), a [currency](/currency-risk/) rate, a commodity price, or even a non-financial event like weather, credit default, or the outcome of an acquisition. For a [weather derivative](/option/), the payoff might be: if average rainfall in a region exceeds 40 inches, the buyer receives $100,000 from the seller; otherwise, nothing. For a [credit default swap](/option/), the seller pays the buyer only if the underlying [bond](/bond/) issuer defaults.

The power of contingent claims lies in their flexibility. By assembling multiple contingent claims with different strikes and maturities, traders and [corporations](/corporate-income-tax/) construct precise [synthetic positions](/synthetic-position/) that replicate any desired payoff. An investor fearing a market downturn can buy [put options](/put-option/)—contingent on a [market decline](/bear-market/)—while selling [call options](/call-option/) contingent on a [market rally](/bull-market/). The portfolio is structured to cap losses below a floor while limiting gains above a ceiling.

## Pricing the contingency

The value of a contingent claim at issuance is the present value of its expected payoff, discounted at the appropriate [risk-free rate](/real-interest-rate/) (plus an adjustment for [risk](/market-risk/), depending on the pricing framework). But because the payoff is binary or path-dependent, standard [discounted cash flow](/discounted-cash-flow-valuation/) does not apply. Instead, traders use [risk-neutral valuation](/option-premium/): they assume that the expected value of the underlying grows at the [risk-free rate](/real-interest-rate/) and compute the contingent claim's value as the [discounted](/discount-rate/) expected payoff under that measure.

The [Black-Scholes model](/black-scholes-model/) is the cornerstone formula for valuing European [options](/option/)—the simplest contingent claims. It expresses the [call option](/call-option/) value as a function of the [stock](/stock/) price, the [strike price](/strike-price/), the [time to expiration](/expiration-date/), the risk-free [interest rate](/interest-rate/), and the [volatility](/historical-volatility/) of the [stock](/stock/). Crucially, the expected return of the [stock](/stock/) does not appear in the formula—only its [volatility](/historical-volatility/) matters. This is because the [risk-neutral pricing](/option-premium/) framework absorbs the expected return into the [discount rate](/discount-rate/). A [stock](/stock/) with a high expected return does not have a higher-priced [option](/option/); rather, the high expected return is already "baked into" the [stock](/stock/) price.

For more complex contingent claims—[American options](/option/) (exercisable early), [exotic options](/option/) (barrier, lookback, Asian), or claims whose payoff depends on multiple underlyings—closed-form solutions are rare. Traders resort to numerical methods like [binomial trees](/option-premium/), [Monte Carlo simulation](/discounted-cash-flow-valuation/), or finite-difference schemes. These approximate the [probability distribution](/option-premium/) of future states and compute the expected payoff in each branch.

## Examples in the wild

Equity [options](/option/)—[calls](/call-option/) and [puts](/put-option/)—are the most visible contingent claims. An investor buys a $30 [call](/call-option/) on a [stock](/stock/) for $2 per share ($200 total for 100 shares). If the [stock](/stock/) closes above $30 at expiration, the [call](/call-option/) is in-the-money; the buyer exercises and pockets the difference. If it closes below $30, the [call](/call-option/) expires worthless, and the buyer loses the $200 premium. The payoff is strictly contingent on the [stock](/stock/) price at a specific moment.

Interest-rate [options](/option/) and [swaptions](/option/) allow [corporations](/corporate-income-tax/) and [banks](/bank-of-america/) to hedge [rate risk](/interest-rate-risk/). A [swaption](/option/) grants the holder the right to enter a [swap](/derivatives-hedging/) at a fixed rate; it is contingent on whether [interest rates](/interest-rate/) have moved enough to make the swap valuable. [Bond](/bond/) issuers often include a [call option](/call-option/) (callable [bond](/bond/)), making the bondholder's future coupons contingent on the issuer choosing not to refinance at a lower rate.

[Credit default swaps](/option/) are contingent on the issuer entering default. The protection buyer pays a regular [premium](/option-premium/); the seller pays the buyer a lump sum only if a defined credit event occurs. Until default, the [swap](/derivatives-hedging/) has value proportional to the [default probability](/default-rate/); upon default, the payoff crystallizes.

[Equity-linked notes](/option/) blend a [bond](/bond/) with an embedded equity [option](/option/). The bondholder receives the principal back at maturity, plus an additional payment contingent on the performance of an underlying [index](/sp-500-index/) or [stock](/stock/). If the [index](/sp-500-index/) rises 20%, the note-holder receives a bonus; if the [index](/sp-500-index/) falls, the bonus is zero (but principal is preserved). The contingency is entirely in the upside payment.

## The path-dependency problem

Not all contingent claims are simple: some are **path-dependent**. An Asian [option](/option/) pays off based on the average price of the underlying over a period, not the final price. A lookback [option](/option/) pays based on the highest (or lowest) price reached during the option's life. These complicate pricing: the future payoff depends not just on where the underlying ends up, but on the trajectory it took to get there. [Monte Carlo simulation](/discounted-cash-flow-valuation/) is the standard tool; analytical solutions are rare.

Barrier [options](/option/) are contingent on the underlying never (or always) touching a certain level. A knockout [call](/call-option/) expires worthless if the underlying ever breaches a barrier; an in-barrier [call](/call-option/) becomes active only if the underlying touches a barrier. The probability of the underlying hitting the barrier is path-dependent and requires sophisticated stochastic models to compute.

## Trading and replication

Contingent claims are traded actively in [options markets](/option/), both [listed](/stock-exchange/) and [over-the-counter](/over-the-counter-market/). A [call option](/call-option/) bought on a [listed exchange](/stock-exchange/) has transparent [bid-ask spreads](/bid-ask-spread/) and [clearing](/central-bank/) via a central counterparty. Bespoke contingent claims—rare [options](/option/), [credit derivatives](/option/), [insurance](/auto-insurance/)-linked [securities](/securities-and-exchange-commission/)—are often negotiated bilaterally and carry [counterparty risk](/counterparty-risk/).

The ability to replicate a contingent claim is central to pricing. A [dealer](/market-maker-trading/) who sells a [call option](/call-option/) buys stock and borrows funds such that the [delta](/delta/)—the sensitivity of the [option](/option/) to moves in the [stock](/stock/)—is perfectly hedged. As the [stock](/stock/) price moves, the dealer adjusts the [hedge](/derivatives-hedging/); the cost of this rebalancing, amortized over the [option's](/option/) life, is the [option's](/option/) fair value. If [dealers](/market-maker-trading/) cannot replicate, pricing becomes subjective, and [risk premiums](/value-at-risk/) widen.

## Regulation and accounting

Contingent claims held as investments must be marked-to-market under [IFRS](/international-financial-reporting-standards/) and U.S. [GAAP](/generally-accepted-accounting-principles/). A [corporation](/corporate-income-tax/) holding a [call option](/call-option/) on foreign exchange records it at fair value each quarter; gains and losses flow through the [income statement](/income-statement/). [Derivatives](/option/) held as [hedges](/derivatives-hedging/) may qualify for [hedge accounting](/derivatives-hedging/), deferring gains and losses to other comprehensive income.

[Regulators](/securities-and-exchange-commission/) are attentive to the [systemic risk](/systemic-risk/) contingent claims can create. If many [corporations](/corporate-income-tax/) have sold [call options](/call-option/) on the same [stock](/stock/) and own the [hedge](/derivatives-hedging/) through the same [dealer](/market-maker-trading/), a sharp [rally](/bull-market/) could force simultaneous [hedge unwinds](/derivatives-hedging/), amplifying [market moves](/market-risk/). [Capital adequacy](/capital-adequacy/) rules require [banks](/bank-of-america/) to hold [capital](/capital-adequacy/) against the [market risk](/market-risk/) of contingent claims they hold.

## See also

<div class="wiki-seealso">

### Closely related

- [Option](/option/) — the fundamental type of contingent claim
- [Call Option](/call-option/) — contingent on underlying price exceeding the strike
- [Put Option](/put-option/) — contingent on underlying price falling below the strike
- [Synthetic Position](/synthetic-position/) — portfolios built from contingent claims
- [Derivatives Hedging](/derivatives-hedging/) — using contingent claims to manage risk
- [Forward Contract](/forward-contract/) — non-contingent; a deterministic obligation

### Wider context

- [Black-Scholes Model](/black-scholes-model/) — framework for pricing contingent claims
- [Strike Price](/strike-price/) — the condition that determines payoff
- [Volatility Smile](/volatility-smile/) — affects the value of [out-of-the-money](/option/) contingent claims
- [Counterparty Risk](/counterparty-risk/) — risk in holding [over-the-counter](/over-the-counter-market/) contingent claims
- [Time Value](/time-decay-theta/) — a key component of contingent claim pricing
- [Option Premium](/option-premium/) — the price paid for a contingent claim

</div>
