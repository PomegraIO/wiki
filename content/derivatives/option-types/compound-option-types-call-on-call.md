---
title: "Compound Option Types: Call on Call, Put on Call, and Beyond"
description: "Compound option types include call on call, put on call, call on put, and put on put. These nested derivatives allow hedging and cost-efficient staged betting on price."
keywords:
  - compound option types call on call
  - call on call option
  - put on call option
  - call on put option
  - put on put option
  - nested derivatives
image: "/svg/derivatives.svg"
---

*A **compound option type** gives the holder the right to buy or sell another option at a future date and specified strike price. The four basic varieties—call on call, put on call, call on put, and put on put—each embed a decision point that lets investors stage their exposure or reduce upfront costs.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Compound Option Types — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives." />

<div class="wiki-infobox-caption">Nested options that trade the immediate strike for a staged premium and later decision.</div>

|   |   |
|---|---|
| **Also known as** | Options on options; nested derivatives |
| **Number of strikes** | Two: outer (exercise to acquire the inner option) and inner (exercise the acquired option itself) |
| **Decision points** | Two: whether to pay the second premium and own the inner option; then, whether to exercise the inner option |
| **Main payoff driver** | [Volatility](/volatility-smile/) of the underlying; greater sensitivity to the inner option's strike |
| **Common use** | Staged currency hedges; interest-rate speculation; acquisition-protection strategies |
| **Premium cost** | Typically 20–40% of a plain vanilla option on the same underlying |

</aside>

## The four compound option types

A compound option starts with a choice: you pay a smaller premium upfront for the right to acquire a second option later. That second option is the "inner" option; your right to acquire it is the "outer" option. At the outer option's expiration, you decide whether to exercise—whether to pay the inner strike and take ownership of the inner option itself.

**Call on call:** You hold the right to buy a call option. If you exercise the outer call at its expiration, you pay the outer strike and receive a call on the underlying. You then have a second window to decide whether to exercise that call.

**Put on call:** You hold the right to sell a call option back to the issuer. This is a hedge: if the underlying rises, your call becomes less valuable, and you exercise your put on call to unload it at the agreed strike.

**Call on put:** You hold the right to buy a put option. Used when you expect increased downside risk but want to defer the cost.

**Put on put:** You hold the right to sell a put option. Exposes you to a decline in the underlying put's value if volatility or risk appetite shifts.

In practice, call on call and put on put are most common in [currency](/currency-risk/) and [interest-rate](/interest-rate/) hedging. The two-strike structure lets a borrower, say, lock in a worst-case loan cost without paying for protection immediately.

## How the dual-premium structure works

When you buy a compound option, you pay a smaller premium upfront—the outer premium. This reserves your right to acquire the inner option at a future date.

If you exercise the outer option, you pay a second amount: the inner strike price. In exchange, you own the inner option. That inner option itself has a strike (the strike of the underlying asset when you finally exercise).

**Worked example:** An importer expects to need euros in six months but is uncertain about whether hedging is worthwhile. He could buy a call option on euros now (expensive, three-month or six-month hedge). Instead, he buys a call on call: he pays a small premium ($0.02 per euro) for the right to buy a three-month euro call at a strike of 1.10 euros per dollar in three months' time. In three months, if his forecast has not changed, he exercises the outer call (paying perhaps 1.08 to acquire the inner call). He then holds a call on euros at 1.10. When the inner option expires, he either exercises it (converting dollars to euros at 1.10) or lets it lapse.

The key advantage: he paid only for the first premium upfront. The second premium is incurred only if he exercises, and only at that time.

## Volatility and strike sensitivity

The value of a compound option depends critically on two [volatility](/historical-volatility/) measures: the volatility of the underlying asset and the volatility of the inner option's price itself.

If you own a call on call, you benefit from two sources of upside. First, a rise in the underlying increases the value of the inner call, making it worth more to acquire at the outer strike. Second, if volatility rises, the inner call becomes more expensive, so your right to buy it at a fixed outer strike becomes more valuable. This dual sensitivity makes compound options cheaper to buy but also more sensitive to shifts in implied [volatility](/implied-volatility/).

The outer strike is often set at-the-money or slightly out-of-the-money. The inner strike is usually set deeper out-of-the-money because the holder of the compound option is buying time to decide.

## Practical use cases in hedging

**Currency hedging:** A multinational firm with uncertain cash flows in a foreign currency can use a call on put: a right to buy a put option on that currency. It reserves the hedge without locking in a premium, and exercises only if actual cash flows materialize.

**Interest-rate protection:** A bank planning a large borrowing in two quarters uses a call on call to lock in its maximum future borrowing cost. The initial premium is minimal; the bank pays the inner strike only if it proceeds with the borrowing decision.

**Acquisition contingencies:** A firm bidding on a target in another currency can protect against currency moves during due diligence using a call on call. If the deal falls through, it abandons the outer option, losing only the small upfront premium.

**Corporate financing:** A company considering a bond issuance in three months buys a put on call—the right to dump a call option on interest rates—to hedge the risk that rates fall (making its call less valuable as a hedge). If rates do fall and the company issues, it exercises the put on call to offset.

## Pricing and valuation

Compound options are priced using nested [Black-Scholes](/black-scholes-model/) models or binomial trees. The outer option's value depends on the expected value of the inner option at the outer option's expiration. The inner option's value is computed as of that future date, accounting for uncertain [volatility](/volatility-smile/) and the underlying asset's range of possible prices.

Because two layers of [uncertainty](/historical-volatility/) are embedded, compound options are sensitive to skew and term structure of volatility. A volatility spike can raise the value of the inner option sharply, making the outer option more valuable. This makes them useful for traders betting on changes in the volatility surface itself.

The cost to the buyer is typically much lower than buying two options separately. A call on call might cost 20–40% of the premium for a plain vanilla call option with the same outer strike and expiration. The trade-off is that the holder must actively exercise the outer option to acquire the inner one; there is no automatic roll-forward.

## When not to use compound options

Compound options add complexity and require precise forecasting of two separate decision points. They are best suited to situations where:
- Uncertainty exists about whether you will need the hedge at all.
- The underlying asset has two distinct decision horizons.
- Upfront cost is a constraint.

In liquid, highly traded markets, buying a plain vanilla option now and selling it back later if you change your mind often works just as well and requires fewer calculations.

## See also

<div class="wiki-seealso">

### Closely related

- [Call Option](/call-option/) — the single-layer foundation of compound options
- [Put Option](/put-option/) — the downside hedge from which put on call and put on put derive
- [Implied Volatility](/implied-volatility/) — the critical driver of compound option value
- [Option Premium](/option-premium/) — the two-stage payment structure in compound types
- [Black-Scholes Model](/black-scholes-model/) — pricing method extended to nested structures
- [Currency Risk](/currency-risk/) — primary use case in multinational hedging

### Wider context

- [Derivatives Hedging](/derivatives-hedging/) — broader category of risk management
- [Interest Rate Swap](/interest-rate-swap/) — alternative interest-rate hedge
- [Forward Contract](/forward-contract/) — simpler way to commit to a future purchase
- [Volatility Smile](/volatility-smile/) — strike-dependent volatility that affects compound pricing

</div>
