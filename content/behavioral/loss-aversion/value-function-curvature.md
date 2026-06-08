---
title: "Value Function Curvature"
description: "The S-shaped utility curve in prospect theory and what its concave and convex segments predict about decisions."
keywords:
  - prospect theory
  - value function
  - concavity
  - risk aversion
image: "/svg/behavioral.svg"
---

*In [prospect-theory](/prospect-theory/), preferences are not linear. The value of money is encoded in an S-shaped curve: diminishing sensitivity to both gains and losses, with an inflection point at the reference level. This shape predicts when investors will be risk-averse and when risk-seeking.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Value Function Curvature — key facts</div>

<img src="/svg/behavioral.svg" alt="An abstract editorial mark for behavioural finance." />

<div class="wiki-infobox-caption">The shape of the value function determines risk preferences in gains and losses.</div>

|   |   |
|---|---|
| **What it is** | The mathematical relationship between objective outcomes and subjective utility in prospect theory |
| **Shape** | S-shaped: concave in gains, convex in losses, kinked at the reference point |
| **Implication of concavity** | Risk aversion in gains; diminishing sensitivity to larger gains |
| **Implication of convexity** | Risk-seeking in losses; willingness to gamble to avoid further losses |
| **Drives** | [Asymmetric risk appetite](/asymmetric-risk-appetite/) and [loss aversion](/loss-aversion/) |
| **Discovered** | Kahneman and Tversky (1979); remains the core of behavioural finance |

</aside>

## The S-Shaped Preference

Classical economics assumes that utility is linear (or smooth and concave everywhere). A dollar is a dollar; twice the money is twice as good. Under this model, an investor with a given level of risk aversion will maintain consistent preferences regardless of whether they are rich or poor, or whether they recently gained or lost.

Prospect theory overturns this. Kahneman and Tversky observed that real people value outcomes according to an S-shaped curve. The curve has two critical features:

1. **Concavity in gains**: Each additional dollar of gain contributes less utility than the previous one. Going from $0 to $100 of gain feels better than going from $100 to $200. This creates risk aversion — the investor prefers a sure $100 to a 50–50 gamble on $0 or $200.

2. **Convexity in losses**: Each additional dollar of loss causes less additional pain than the previous dollar lost. The first $100 loss stings more than the second. This creates risk-seeking — facing a loss, the investor prefers a 50–50 gamble on $0 or $200 loss to a sure $100 loss.

At the reference point (typically zero, or the current wealth level), the curve kinks sharply. This kink is the seat of [loss-aversion](/loss-aversion/): the curve is steeper below the reference point than above it. A loss of $100 looms larger than a gain of $100 feels good.

## Why Concavity Produces Risk Aversion in Gains

Imagine a trader holding a position worth $10,000 above their entry price. The position might rise to $15,000 (a gain of $5,000) or fall back to $8,000 (a loss of $2,000), each with 50% probability. The expected value is neutral (expected movement is $1,500 gain). Yet most investors would find this unattractive and would prefer to crystallize the $10,000 gain.

The reason is the concave shape of the value function above the reference point. The additional utility from gaining $5,000 is less than the utility lost by dropping $2,000. Due to the curve's flatness at higher gain levels, the upside is "less valuable" than the downside is "costly." The rational choice, given non-linear preferences, is to lock in the bird in hand.

This concavity also explains wealth effects. As wealth grows, the marginal utility of additional dollars declines. A million-dollar gain to a billionaire creates less utility than a million-dollar gain to a middle-income person. But in the context of trading, the concavity is about the shape of preferences at any reference level, not absolute wealth.

## Why Convexity Produces Risk-Seeking in Losses

Now reverse the scenario. A trader is underwater, down $10,000 from entry. They can either cut the loss (lock in the $10,000 loss) or hold for a 50–50 gamble: the position might recover $5,000 or fall another $2,000.

Rationally, this gamble has negative expected value relative to cutting the loss; it only prolongs pain. Yet the convex shape of the value function in the loss domain makes the gamble attractive. The marginal pain of an additional $2,000 loss is small relative to the utility of a $5,000 recovery from the current underwater state. The curve flattens as losses grow deeper, so the prospect of recovering from $10,000 down to $5,000 down feels more valuable than the prospect of losing another $2,000.

In extreme form, this is the leverage trap. A trader down significantly may make riskier and riskier bets, not out of overconfidence or irrationality per se, but because the convex value function at extreme losses makes high-variance strategies the "rational" choice given their preferences.

## The Kink and Loss Aversion

The sharp inflection at the reference point — the kink — is where loss aversion lives. The slope of the value function is steeper for losses than for gains. In dollar terms, the pain of losing $100 exceeds the pleasure of gaining $100. Empirically, the ratio is around 2:1, though it varies across studies and populations.

This kink is why people are willing to pay an insurance premium (accepting a sure small loss) to avoid the risk of a large one. It is also why [stock-options](/option/) buyers often lose money on average — they are paying a premium (a sure loss) for the convex payoff on the loss side, which feels valuable despite negative expected value.

## Portfolio-Level Implications

At the portfolio level, the S-shaped value function predicts specific behaviour. A portfolio that has risen sharply will see risk-averse behaviour — rebalancing, trimming winners, raising cash. The concavity means the investor values the sure thing of realized gains. A portfolio deep in the red will see risk-seeking behaviour — averaging down, taking on leverage, chasing volatile opportunities. The convexity means the investor values a small chance of a large recovery over a certain additional loss.

Over time, this can create whipsaw dynamics: aggressive accumulation in downturns (when the value function is convex and the investor is risk-seeking), followed by defensive trimming in upturns (when the value function is concave and the investor is risk-averse). The result is buying near the lows and selling near the highs — the opposite of buy-and-hold discipline.

## Diminishing Sensitivity

A secondary property of the S-shaped curve is diminishing sensitivity overall. The curve grows flatter as you move further into gains or losses. This means that the difference between a $1,000 gain and $2,000 gain matters more than the difference between $10,000 and $11,000, even though both are $1,000 differences. Similarly, a $1,000 loss stings more than a $10,000 loss hurts incrementally.

This property helps explain why people often take bad hedges or insurance deals. They overweight small risks (the utility gap between a small and a moderate loss is large) and underweight large risks (where the curve has flattened). A rare tail event that would wipe out wealth receives less mental attention than a frequently occurring small drawdown.

## Implications for Option Pricing and Speculation

The convex-in-losses segment of the value function provides a utility-based rationale for why retail traders and speculators buy out-of-the-money calls and puts, despite negative expected value. The convex payoff — a small bet that can return many times the stake if you win — aligns with the convex value function. The trader is not irrational; they are purchasing a utility-increasing gamble, even if the math is against them.

Similarly, the concave-in-gains segment explains why investors over-sell covered calls or trim winners prematurely. The sure premium or lock-in feels more valuable than the risky prospect of larger gains.

## See also

<div class="wiki-seealso">

### Closely related

- [Loss aversion](/loss-aversion/) — the kink in the value function that makes losses loom larger than gains
- [Asymmetric risk appetite](/asymmetric-risk-appetite/) — the reversal of risk preferences explained by curvature shape
- [Loss framing effect](/loss-framing-effect/) — how the location of a choice relative to the reference point affects the shape of the relevant value function
- [Pain of regret in trading](/pain-of-regret-trading/) — how the desire to escape loss (convexity) drives regret-averse decisions
- [Prospect theory](/prospect-theory/) — the foundational model incorporating value function curvature
- Diminishing marginal utility — the classical precursor to diminishing sensitivity

### Wider context

- Behavioral finance — the field studying how preference shapes distort financial decisions
- Risk tolerance — how reference dependence and curvature determine actual risk appetite
- Portfolio construction — how design can smooth out the effects of value function curvature
- Options strategies — how curvature explains the appeal and pricing of convex payoffs

</div>
