---
title: "Linear vs Non-Linear Derivatives: What the Difference Means for Risk"
description: "Linear vs nonlinear derivatives: understand why futures move point-for-point with the underlying, while options have curved payoffs that create complex risk."
keywords:
  - linear derivatives
  - nonlinear derivatives
  - option payoff
  - delta risk
  - gamma risk
  - derivatives risk measurement
image: "/svg/derivatives.svg"
---

*A **linear derivative** moves dollar-for-dollar with its underlying asset: a crude oil [futures contract](/futures-contract/) gains or loses $100 for every $1 move in the spot price. A **nonlinear derivative**, like an [option](/option/), has a curved payoff: it gains slowly at first, then faster as it moves in-the-money, then flattens again if it soars far above the strike. This curvature creates hidden risks—like [gamma](/gamma/) and [vega](/vega/)—that [linear derivatives](/derivatives-hedging/) do not have, and it breaks the simplifying assumption that your [hedge](/derivatives-hedging/) will move one-to-one with your exposure.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Payoff Curves — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">One is a straight line; the other is a smile or a curve.</div>

|   |   |
|---|---|
| **Linear derivatives** | [Futures](/futures-contract/), [forwards](/forward-contract/) |
| **Payoff shape** | Straight line; 1:1 with underlying |
| **Primary risk** | [Delta](/delta/) (directional move) |
| **Nonlinear derivatives** | [Options](/option/) ([calls](/call-option/), [puts](/put-option/)), [callable bonds](/callable-bond/) |
| **Payoff shape** | Curved; accelerates in-the-money |
| **Primary risks** | [Delta](/delta/), [gamma](/gamma/), [vega](/vega/), [theta](/theta/) |
| **Risk measurement** | [Greeks](/delta/) become essential; linear risk is insufficient |

</aside>

## What Linear Derivatives Are

A **linear derivative** has a payoff that moves in lockstep with the underlying asset. The canonical example is a [futures contract](/futures-contract/).

Suppose you own a [crude oil futures](/futures-contract/) contract at a locked-in price of $50 per barrel, and oil rises to $51. You have made $1 per barrel (or $1,000 on a standard contract of 1,000 barrels). If oil falls to $49, you have lost $1 per barrel. The payoff is a straight line: as the underlying moves, your gain or loss scales proportionally and immediately.

A [forward contract](/forward-contract/) works the same way: you commit to buy or sell a quantity of an asset at a fixed future price. At settlement, you gain or lose dollar-for-dollar with any move in the spot price from your agreed-upon strike.

This linearity makes [futures](/futures-contract/) and [forwards](/forward-contract/) straightforward to [hedge](/derivatives-hedging/) and to measure risk. If you own 100 barrels of crude and want to hedge the downside, you short one [crude futures](/futures-contract/) contract (1,000 barrels). The hedge moves 10:1 with your underlying position, creating a simple ratio.

## What Nonlinear Derivatives Are

An **option** is fundamentally nonlinear. A [call option](/call-option/) gives the right to buy at a strike price. If the strike is $50 and the underlying is at $45, the [call](/call-option/) is worthless (or nearly so)—you would never exercise it. A $1 move down in the underlying barely dents the [call](/call-option/) value. But if the underlying is at $49.50, that same $1 move takes you to $50.50, suddenly making the [call](/call-option/) in-the-money and valuable. The payoff is not straight; it curves upward as you approach and pass the strike.

Far in-the-money, the [call](/call-option/) behaves almost like a [linear](/derivatives-hedging/) asset: a $1 move in the underlying translates nearly to a $1 gain. But that is only because you have already crossed the strike and the [option](/option/) is fully leveraged into the stock.

A [put option](/put-option/) has the reverse curve: it rises in value as the underlying falls, but the relationship is curved, not linear.

[Callable bonds](/callable-bond/) are also nonlinear. A bond issuer has the embedded [call option](/call-option/) to redeem the bond if rates fall. If rates fall sharply, the bondholder loses the upside—the bond does not appreciate as much as a non-callable bond—creating a ceiling on gains. The payoff curve is kinked, not straight.

## The Greeks: Measuring Nonlinear Risk

Because [options](/option/) do not move one-to-one with the underlying, risk managers and traders use the **[Greeks](/delta/)** to measure and manage their exposure.

**[Delta](/delta/)** measures how much the [option](/option/) price changes for a $1 move in the underlying. An at-the-money [call](/call-option/) might have a [delta](/delta/) of 0.5, meaning for every $1 the underlying rises, the [call](/call-option/) gains roughly $0.50. This [delta](/delta/) is not constant; as the [call](/call-option/) moves deeper in-the-money, [delta](/delta/) approaches 1.0. As it moves farther out-of-the-money, [delta](/delta/) approaches zero.

**[Gamma](/gamma/)** measures how much [delta](/delta/) itself changes. A large [gamma](/gamma/) means that small moves in the underlying cause large swings in [delta](/delta/), which means large swings in your effective exposure. [Gamma](/gamma/) is highest when the [option](/option/) is at-the-money (the curve is steepest there) and falls to near-zero far in or out of the money (the curve flattens).

**[Vega](/vega/)** measures sensitivity to [implied volatility](/implied-volatility/)—the market's expectation of future price swings. A [call option](/call-option/) is worth more when volatility is expected to be high (more upside room); a [put option](/put-option/) is worth more when volatility is high. [Linear derivatives](/derivatives-hedging/) have zero [vega](/vega/) because volatility does not affect their payoff.

**[Theta](/theta/)** measures time decay: how much the [option](/option/) loses value per day as it approaches expiration with no move in the underlying. All [options](/option/) lose value as expiration approaches (unless far out-of-the-money [puts](/put-option/)), and this decay accelerates near the end.

## Why Nonlinearity Matters: A Hedging Problem

Imagine you own a [callable bond](/callable-bond/) and want to [hedge](/derivatives-hedging/) against a drop in bond prices (a rise in [interest rates](/interest-rate/)). You might use Treasury bond [futures](/futures-contract/) as a [hedge](/derivatives-hedging/). If the bond and the [futures](/futures-contract/) move one-to-one, you are protected: you win on the short [futures](/futures-contract/) what you lose on the bond.

But the bond is embedded with a [call option](/call-option/) (the issuer's right to call it). When [interest rates](/interest-rate/) fall and bond prices rise, the embedded [call](/call-option/) becomes valuable to the issuer, and it dampens your upside. Your [callable bond](/callable-bond/) does not gain as much as a [futures](/futures-contract/) contract that moves linearly with the bond price. Your [hedge](/derivatives-hedging/) over-hedges on a rates-down move, and you lose money even though your [hedge](/derivatives-hedging/) was constructed correctly on a linear basis.

This is the curse of nonlinearity: the hedge that is right on average (in a linear sense) can fail spectacularly in extreme scenarios.

## Gamma Bleed and Realized vs Implied Volatility

For [option](/option/) traders, the most consequential nonlinearity risk is [gamma](/gamma/). Suppose you are short a [call option](/call-option/) to collect [premium](/option-premium/). If the underlying meanders sideways, you profit from [time decay](/time-decay-theta/) ([theta](/theta/)) as the [option](/option/) loses value. But if the underlying whipsaws—up, then down, then up again—each large move increases [gamma](/gamma/) losses. Even if the underlying ends the day where it started, your [short call](/call-option/) can lose money because you are effectively short [gamma](/gamma/): you sold the right to the upside, but not the right to be protected downside.

Conversely, if you are long [gamma](/gamma/) (long [options](/option/)), large realized moves are profitable, but sideways markets kill you via [theta](/theta/) decay.

This dynamic explains why [implied volatility](/implied-volatility/) (the volatility priced into [options](/option/)) differs from [realized volatility](/historical-volatility/) (the actual moves that occur). If [implied volatility](/implied-volatility/) is 30% but realized volatility is 50%, short [option](/option/) sellers lose money on [gamma](/gamma/); if realized is 10% but implied is 30%, [option](/option/) buyers lose money to [theta](/theta/).

## Linear in Parallel, Nonlinear Across Strikes

An interesting nuance: a single [option](/option/) is nonlinear in the underlying. But a *portfolio* of [options](/option/) at different strikes can be linear in a narrow band around current prices. A [straddle](/option/) (long [call](/call-option/) and [put](/put-option/) at the same strike) is long [gamma](/gamma/) and long [vega](/vega/), making money on big moves or volatility spikes. An [iron condor](/option/) (short [call](/call-option/) spread and short [put](/put-option/) spread) is short [gamma](/gamma/), profiting from low realized volatility and time decay but losing on large moves.

This is why [option](/option/) traders spend much of their time thinking in [Greeks](/delta/) and curves rather than simple direction. The nonlinearity opens a whole second dimension of trading and hedging.

## Comparing Hedging Cost and Efficacy

A [futures](/futures-contract/) [hedge](/derivatives-hedging/) against a commodity is linear: it costs nothing upfront (ignoring margin and financing), and it moves one-to-one. A [put option](/put-option/) [hedge](/derivatives-hedging/) against a stock decline is nonlinear: it costs an upfront [premium](/option-premium/), but it flexes; you pay for the right to walk away on the downside. On the upside, the [put](/put-option/) is a free rider—you participate fully if the stock soars.

This is why financial institutions often use [options](/option/) for tail-risk [hedging](/derivatives-hedging/). You sacrifice some upside (the [premium](/option-premium/) paid) to eliminate [tail risk](/tail-risk/). A [linear](/derivatives-hedging/) [futures](/futures-contract/) [hedge](/derivatives-hedging/) eliminates upside entirely—you are flat either way.

## See also

<div class="wiki-seealso">

### Closely related

- [Futures contract](/futures-contract/) — linear derivative; payoff moves point-for-point with underlying
- [Forward contract](/forward-contract/) — linear commitment to buy or sell at future date
- [Option](/option/) — nonlinear derivative; payoff curves upward in-the-money
- [Call option](/call-option/) — nonlinear right to buy; gains accelerate as underlying rises
- [Put option](/put-option/) — nonlinear right to sell; gains accelerate as underlying falls
- [Delta](/delta/) — Greeks measure nonlinear sensitivities; measures price sensitivity
- [Gamma](/gamma/) — Greeks measure; curvature of the option payoff
- [Vega](/vega/) — Greeks measure; volatility sensitivity of option value
- [Theta](/theta/) — Greeks measure; time decay of option value
- [Callable bond](/callable-bond/) — bond with embedded [call option](/call-option/); nonlinear payoff

### Wider context

- [Derivatives hedging](/derivatives-hedging/) — using [linear](/futures-contract/) and nonlinear [options](/option/) to manage risk
- [Option premium](/option-premium/) — price of an [option](/option/); driven partly by [implied volatility](/implied-volatility/)
- [Implied volatility](/implied-volatility/) — forward-looking volatility priced into [options](/option/)
- [Historical volatility](/historical-volatility/) — actual realized price swings; differs from implied
- [Tail risk](/tail-risk/) — extreme market moves; [options](/option/) are effective [hedge](/derivatives-hedging/) against them
- [Interest rate risk](/interest-rate-risk/) — affects [callable bond](/callable-bond/) payoff and [bond option](/option/) value
- [Interest-rate swap](/interest-rate-swap/) — [linear](/derivatives-hedging/) [derivative](/derivatives-hedging/); commonly [hedged](/derivatives-hedging/) with [options](/option/)

</div>
