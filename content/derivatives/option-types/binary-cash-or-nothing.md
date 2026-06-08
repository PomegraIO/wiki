---
title: "Cash-or-Nothing Option"
description: "A digital option that pays a fixed cash amount if the underlying finishes in-the-money, or nothing otherwise."
keywords:
  - cash-or-nothing option
  - digital option
  - binary option
  - fixed payoff
  - all-or-nothing option
  - option derivatives
image: /svg/derivatives.svg
---

*A **cash-or-nothing option** is a [digital option](/option/) with a binary payoff: it delivers a fixed cash amount if the underlying asset finishes above (for a [call](/call-option/)) or below (for a [put](/put-option/)) the [strike price](/strike-price/), and pays zero otherwise. There is no continuous gradation of profit—only a cliff from complete payout to total loss.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Cash-or-Nothing Option — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives and options." />

<div class="wiki-infobox-caption">Binary simplicity: a fixed payment, not the asset itself.</div>

|   |   |
|---|---|
| **What it is** | A [digital option](/option/) paying fixed cash if condition is met, zero otherwise |
| **Also called** | Binary option (in some jurisdictions), all-or-nothing, cash digital |
| **Payoff structure** | $K if [in-the-money](/in-the-money/), $0 otherwise (where K is fixed) |
| **Common payoff sizes** | Often $1, $100, or a percentage of spot price |
| **Strike sensitivity** | Extreme [gamma](/gamma/); delta near zero away from strike, vertical spike at strike |
| **Typical use** | Betting on direction; event-driven strategies; speculation |
| **Regulation** | Heavily restricted in many jurisdictions as a speculative product |

</aside>

## The cliff between winning and losing

A standard [call option](/call-option/) on a stock worth $100 with a $100 strike has continuous value: if the stock rises to $101, the option is worth roughly $1; at $105, it's worth $5; at $110, it's $10. Profit scales with movement.

A cash-or-nothing $100 [call](/call-option/), by contrast, is indifferent to the gap. If the stock finishes anywhere above $100—whether at $100.01 or $150—the buyer collects exactly $100. If it finishes at $99.99, the buyer collects zero. The option has no intermediate states. This discontinuous payoff creates exotic behaviour in Greeks and pricing dynamics.

The simplicity is appealing to certain traders. Instead of worrying about *how much* an asset might move, they focus on a binary question: does it close above or below the strike? For a journalist betting that a currency will weaken by the end of the week without caring *how much* it weakens, a cash-or-nothing [put](/put-option/) is perfectly efficient—cheaper than a vanilla [put](/put-option/), because there's no value to protecting against a move of, say, 10% versus 2%.

## Pricing and the strike boundary problem

Vanilla [options](/option/) can be priced using the [Black-Scholes model](/black-scholes-model/) or equivalent frameworks. Cash-or-nothing options can be valued the same way—but the results are unintuitive. The [option](/option/) value equals the discounted probability of finishing in-the-money, multiplied by the payout amount.

If volatility is high, the probability of finishing in-the-money (even for an out-of-the-money [call](/call-option/)) is higher, so the [option](/option/) is more valuable. If there's little time left and the [option](/option/) is deeply out-of-the-money, the value approaches zero—but it falls in a discontinuous way as time decays and volatility drops.

This discontinuity matters most at the strike price. For a vanilla [call](/call-option/), [delta](/delta/) (the rate of change of option value per unit of underlying movement) is gradual. For a cash-or-nothing [call](/call-option/), [delta](/delta/) is nearly zero when the underlying is well below the strike, then spikes—theoretically to infinity—at the strike price, then falls back toward zero above the strike. [Gamma](/gamma/) (the rate of change of delta) becomes a knife-edge peak at the strike. This behaviour is why dealers who sell cash-or-nothing [options](/option/) face acute [gamma](/gamma/) risk: a small move in the underlying around the strike creates enormous position drift.

Pricing also depends heavily on [volatility](/volatility-smile/). A cash-or-nothing [option](/option/) is essentially a leveraged bet on the tail probability of reaching the strike. If [implied volatility](/implied-volatility/) is very high, the tail probability is higher, and the [option](/option/) is more valuable even if the current spot price is far from the strike.

## Cash-or-nothing calls and puts

A **cash-or-nothing [call](/call-option/)** pays a fixed amount (say, $100) if the underlying finishes at or above the strike. A call with strike $50 and payout $100 is worth less if spot is at $45 than if spot is at $49, because the probability of reaching $50 is steeper near the strike. But the value cap is always $100; it will never pay more, no matter how far the underlying rallies.

A **cash-or-nothing [put](/put-option/)** pays the fixed amount if the underlying finishes at or below the strike. The mechanics are identical; only the direction inverts.

Traders combine these. A long cash-or-nothing [call](/call-option/) at $50 with payout $100, plus a short cash-or-nothing [call](/call-option/) at $55 with payout $100, creates a digital [bull call spread](/call-option/): the trader profits if the underlying lands between $50 and $55, and the profit is capped. This is a common way to play a narrow expected range in a cost-effective way.

## Event-driven use and retail speculation

Cash-or-nothing options exploded in retail trading around 2008–2012 when unregulated offshore platforms offered them as a vehicle for betting on economic data releases, political outcomes, and binary events. A trader might buy a cash-or-nothing $100 [call](/call-option/) on the EUR/USD pair betting that the European Central Bank will announce a rate cut; if it does and the pair moves above a strike within an hour, they collect $100. If the cut is delayed or the pair stays below the strike, they lose their premium.

This appeal—"bet on an outcome, collect a fixed sum"—is why regulators in the US, UK, and EU have increasingly classified and restricted cash-or-nothing [options](/option/). The US SEC and CFTC limit retail access, and the UK Financial Conduct Authority has effectively banned them to consumers. The risk is that retail buyers underestimate the odds of finishing exactly at or beyond the strike, leading to excessive losses on repeated small bets. From a dealer's perspective, the problem is the inverse: the gamma risk at the strike boundary is so extreme that legitimate hedging costs can exceed the premium collected.

## Comparison to asset-or-nothing options

Where a cash-or-nothing [call](/call-option/) pays a fixed dollar amount, an [asset-or-nothing option](/asset-or-nothing-option/) pays the underlying asset itself. A cash-or-nothing $100 [call](/call-option/) pays $100 if in-the-money; an [asset-or-nothing call](/asset-or-nothing-option/) pays one share of the stock (or the equivalent spot value). The [asset-or-nothing call](/asset-or-nothing-option/) is riskier for a buyer betting on direction alone—if the underlying rallies sharply, they get that asset at spot, not a capped payout—but it's valuable for hedgers or those seeking equity exposure.

## Practical constraints and hedging

Because the payoff is binary, market-makers hedge cash-or-nothing [options](/option/) by maintaining a position in the underlying that rebalances constantly as the underlying price approaches the strike. Close to expiry, with the strike imminent, [gamma](/gamma/) spikes and the cost of continuous rebalancing becomes unsustainable. This is why cash-or-nothing [options](/option/) are rarely traded with long expirations or in low-[liquidity](/liquidity-risk/) underlying markets. The bid-ask spread widens dramatically as expiry nears and spot approaches the strike, often making the product effectively untradeable at retail prices.

## See also

<div class="wiki-seealso">

### Closely related

- [Asset-or-nothing option](/asset-or-nothing-option/) — delivers the underlying asset instead of fixed cash
- [Digital option](/option/) — the broader class of binary-payoff derivatives
- [Binary option](/option/) — synonym in casual usage, though now heavily regulated
- [Option](/option/) — the parent class of all these derivatives
- [In-the-money](/in-the-money/) — the condition that triggers payout
- [Strike price](/strike-price/) — the boundary between payoff and zero

### Wider context

- [Black-Scholes model](/black-scholes-model/) — used to price cash-or-nothing [options](/option/) via tail probabilities
- [Implied volatility](/implied-volatility/) — drives the probability of reaching the strike
- [Gamma](/gamma/) — peaks dangerously at the strike price
- [Delta](/delta/) — exhibits cliff-like behaviour across the strike boundary

</div>
