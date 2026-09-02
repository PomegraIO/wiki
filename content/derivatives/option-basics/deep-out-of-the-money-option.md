---
title: "Deep Out-of-the-Money Option"
description: "Cheap, high-leverage options with low probability of profit but extreme payoffs if the underlying move is large enough; lottery-ticket structures in derivatives trading."
keywords:
  - out-of-the-money option
  - lottery ticket
  - leverage
  - call spread
  - delta
image: "/svg/derivatives.svg"
---

*A **deep out-of-the-money option** is an option whose [strike price](/strike-price/) is so far from the current market price that the contract has virtually no [intrinsic value](/intrinsic-value/) and trades almost entirely on [time value](/option-premium/). These options are cheap—often pennies per contract—but require a massive move in the underlying asset to become profitable. They are the speculator's tool: low cost, high leverage, extreme odds.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Deep Out-of-the-Money Option — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives and contracts." />

<div class="wiki-infobox-caption">Cheap contracts that pay off only if a dramatic move occurs; used for speculative leverage and income strategies.</div>

|   |   |
|---|---|
| **What it is** | An option with strike far above (call) or below (put) the stock price |
| **Also called** | Far OTM, lottery ticket, speculative option |
| **Delta range** | 0.01–0.20 for calls; −0.20 to −0.01 for puts |
| **Probability of profit** | 5–20%, depending on time to [expiration](/expiration-date/) and implied [volatility](/volatility-smile/) |
| **Time decay rate** | Rapid, especially near expiration |
| **Primary use** | Speculative leverage; income generation through premium collection |
| **Cost versus stock** | Cheap upfront, but needs violent move to profit |

</aside>

## Why deep out-of-the-money options cost almost nothing

An option's price has two components: [intrinsic value](/intrinsic-value/) (the profit if exercised today) and [time value](/option-premium/) (the probability of that option moving into profit before [expiration](/expiration-date/)). A deep out-of-the-money option has zero intrinsic value. It trades on time value alone, and a remote time value at that.

Consider a stock at $100 with a call option at a $150 strike expiring in one month. For the call to be worth anything at [expiration](/expiration-date/), the stock must rally 50% to $150 or higher—a move that happens roughly once per decade for most securities. The market prices this microscopic probability into the [premium](/option-premium/): perhaps $0.05 per share, or $5 per contract (100 shares).

This is the appeal and the trap. You can control 100 shares of upside exposure for $5. If the stock rallies to $151, your $5 call is now worth at least $100—a 20-fold return on capital. But the stock needs to do something extraordinary. Most of the time, the option expires worthless and you lose your $5 entirely. The odds are stacked hard against you.

The deeper the option sinks out-of-the-money, the cheaper it gets. A $200 call on a $100 stock is nearly free—a fraction of a cent—because it requires a 100% gain to break even. But that same near-zero cost means it can deliver a 100-to-1 return if lightning strikes.

## Probability, leverage, and the math of lottery-ticket options

The mathematics of deep out-of-the-money options is brutal and clear. A researcher studying option returns consistently finds that buyers of deep out-of-the-money calls or puts lose money over time. The [time decay](/time-decay-theta/) is so relentless, and the probability of a move large enough to overcome it is so small, that the expected value is negative.

But within that crowd, a tiny fraction of bets hit. A trader who bought deep out-of-the-money calls on a stock before a takeover announcement (which can drive a 25% rally overnight) makes a fortune. The same trader who buys deep OTM calls in 99 other boring stocks loses $5 per contract each time.

The leverage is real but conditional. Suppose you have $10,000 to deploy. You could buy 100 shares at $100, giving you $100 in upside per $1 rally. Or you could buy 2,000 contracts of deep out-of-the-money calls at $0.05 each, controlling 200,000 shares notionally. If the stock rallies $1, your call position is worthless (since $101 is still far from the $150 strike). But if the stock gaps to $160, your $5,000 position becomes worth $200,000 or more.

This convexity—zero profit in normal markets, enormous profit in tail events—is what draws speculators. It is why traders buy deep out-of-the-money puts before earnings; they are betting on a gap down. It is why retail option traders flock to deep OTM calls on high-[volatility](/volatility-smile/) stocks; they are chasing 50-to-1 shots.

## Implied volatility and the mirage of "cheap" options

A deep out-of-the-money option's price depends heavily on implied [volatility](/volatility-smile/)—the market's expectation of how much the stock will move. In a calm market, that option costs $0.05. Before an earnings announcement, when [volatility](/volatility-smile/) spikes, the same option might cost $0.20. Even though the odds have not really improved much, the cost has quadrupled.

This creates a trap for undisciplined buyers. A trader sees a cheap $0.05 call and buys 100 contracts for $500. Two days later, an earnings date approaches and [volatility](/volatility-smile/) jumps; the call is now worth $0.15 without the stock moving at all. The trader is tempted to hold longer, chasing the $150 strike with renewed hope. Then earnings misfire, [volatility](/volatility-smile/) collapses, and the call drops back to $0.02, wiping out most of the trader's capital.

Shrewd traders sell deep out-of-the-money options into volatility spikes—locking in inflated [time value](/option-premium/) before expiration erodes it. This is known as selling [volatility](/volatility-smile/), and it is on the other side of the lottery-ticket trade. Most retail traders are buyers (losing side); professionals are sellers (winning side).

## The short seller's game: collecting premium on deep OTM strikes

If deep out-of-the-money options are a bad bet for buyers, they are a great bet for sellers. A trader who sells a deep out-of-the-money call collects the $5 [premium](/option-premium/) upfront and keeps it if the stock fails to reach $150 by [expiration](/expiration-date/)—which it will 95% of the time or more.

This is the basis of [income](/dividend/) strategies like the "wheel" in retail trading: sell deep OTM calls against a stock you own, collect the premium, and keep it. If the stock explodes higher and your shares are called away, you sell and pocket the gains. If the stock trades sideways or down, you keep the premium and sell another call the next month.

Professional traders build entire strategies around selling deep OTM options—collecting small, reliable premiums across hundreds of positions, confident that the law of large numbers will beat the rare tail event that moves sharply against them. The [risk](/operational-risk/) is hidden: one catastrophic move can wipe out months of collected premium. But for traders with capital reserves and [discipline](/market-timing/), it works.

## When deep out-of-the-money options make sense

For buyers, deep out-of-the-money options are appropriate only in specific circumstances:

**Tail-risk hedges**: A portfolio manager concerned about a market crash might buy deep out-of-the-money puts on the [S&P 500](/sp-500-index/). If the market plunges 20%, those pennies-per-contract puts might be worth thousands. The expected value is negative, but the insurance payoff justifies the cost.

**Catalyst-driven bets**: A trader expecting a takeover, earnings surprise, or regulatory ruling that could move a stock 20%+ might buy deep out-of-the-money calls. The odds are still bad, but the information advantage might swing the bet.

**Leverage on small capital**: A trader with $1,000 cannot buy even one share at $100. Deep OTM calls give her exposure to 100+ shares' worth of moves for that same $1,000—with zero upside if the stock goes sideways.

For sellers, the calculus is clearer: sell deep out-of-the-money options consistently, collect premium, and manage risk by never letting the position exceed a certain notional value. This is how professional options traders profit.

## The seductive trap and the importance of position sizing

The danger of deep out-of-the-money options is psychological. They are so cheap that traders oversize. A trader who would never risk $10,000 on a single stock will happily deploy $10,000 across 200 contracts of $0.05 calls, reasoning, "I can only lose $5." But that $5 loss repeats 200 times, and in 18 months of bad bets, the trader has blown through $20,000 in capital.

Successful speculators treat deep OTM options like insurance: a small, budgeted loss in the name of a rare outsized gain. Unsuccessful ones treat them like lottery tickets, chasing the fantasy of a 100-to-1 return without accepting that the ticket is a loser 99 times.

## See also

<div class="wiki-seealso">

### Closely related

- Option — foundational contract types and core mechanics
- [Delta](/delta/) — the probability-weighted sensitivity of out-of-the-money options
- [Theta](/theta/) — time decay and why OTM options vanish into worthlessness
- [Volatility smile](/volatility-smile/) — how implied [volatility](/volatility-smile/) inflates and deflates OTM prices
- [Deep in-the-money option](/deep-in-the-money-option/) — the opposite strategy with real intrinsic value
- [Option premium](/option-premium/) — what you pay and why deep OTM contracts are cheap
- [Covered call](/covered-call/) — selling deep OTM calls for income

### Wider context

- [Call option](/call-option/) — the mechanics of outright bullish bets
- [Put option](/put-option/) — the mechanics of bearish bets and hedge positions
- [Strike price](/strike-price/) — defining the distance to "deep"
- [Expiration date](/expiration-date/) — how time accelerates the decay of OTM options
- [Gamma](/gamma/) — explosive delta swings as OTM options approach in-the-money
- [Leverage ratio (forex)](/leverage-ratio-forex/) — the conceptual parallel in currency trading

</div>
