---
title: "Options Greeks in an Iron Condor Strategy"
description: "An iron condor sells near-the-money puts and calls, leaving a net-delta neutral position with short gamma, positive theta, and short vega. Learn how each Greek shifts as the underlying moves."
keywords:
  - options greeks iron condor strategy
  - iron condor delta gamma theta vega
  - short volatility options strategy
  - iron condor greek profile
  - delta-neutral options strategy
image: /svg/derivatives.svg
---

*An [iron condor](/option/) is a four-leg options strategy that sells a near-the-money [call spread](/option/) and a near-the-money [put spread](/option/), aiming for profit if the underlying stays quiet. Its **greek profile**—net-[delta](/delta/) neutral, [short gamma](/gamma/), positive [theta](/theta/), short [vega](/vega/)—reveals exactly why it works and when it breaks.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Iron Condor Greeks — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives." />

<div class="wiki-infobox-caption">Short gamma, positive theta: profitable decay in a range.</div>

|   |   |
|---|---|
| **Delta** | Near zero at entry (range-bound neutral) |
| **Gamma** | Negative (accelerating losses if underlying breaks out) |
| **Theta** | Positive (time decay works for you) |
| **Vega** | Negative (rising volatility hurts) |
| **Best market view** | Low volatility, range-bound underlying |
| **Max profit** | Width of spreads minus net premium paid |

</aside>

## The iron condor structure and initial greeks

An iron condor combines two [spreads](/option/):

**Call spread (upper wing):**
- Sell an out-of-the-money call (e.g., strike 110)
- Buy an out-of-the-money call (e.g., strike 115)

**Put spread (lower wing):**
- Sell an out-of-the-money put (e.g., strike 90)
- Buy an out-of-the-money put (e.g., strike 85)

Suppose the underlying is trading at 100. Your short 110 call has a small positive [delta](/delta/), maybe +0.20. Your long 115 call has a smaller positive delta, maybe +0.10, so the call spread has a net delta of +0.10.

Your short 90 put has a small negative delta, maybe −0.20. Your long 85 put has a smaller negative delta, maybe −0.10, so the put spread has a net delta of −0.10.

Combined: +0.10 + (−0.10) = **0 delta**. The position is neutral to small moves in the underlying. If the stock rises 2%, you neither gain nor lose from directional movement.

## Gamma: the accelerator of losses

While delta is near zero, **[gamma](/gamma/)** is decidedly negative. Gamma measures how much delta changes when the underlying moves 1%. An iron condor is short gamma because you sold near-the-money calls and puts, which have the highest gamma.

When the underlying starts moving away from your short strikes:
- If it rallies above 110, the short call's delta accelerates toward −1.00 (you lose more per tick).
- If it falls below 90, the short put's delta accelerates toward +1.00 (you lose more per tick).

This is the **iron condor's greatest risk**. You start delta-neutral and profitable from [theta](/theta/) decay, but a sharp move in either direction causes gamma to compound your losses. A 10-point rally takes your call spread from a small loss to a large loss, not linearly but at an accelerating rate.

**Gamma increases as expiration approaches and the underlying nears a short strike.** This is why iron condors are typically closed or rolled 7–14 days before expiration if the underlying is within the short strikes. Staying in during the final week, gamma spikes, and a small adverse move can blow through your max loss in minutes.

## Theta: the clock is your friend (until it isn't)

**[Theta](/theta/)** (time decay) is the daily profit from the passage of time. An iron condor is short both calls and puts, so you own the [time-decay benefit](/time-decay-theta/).

On day one, maybe theta is worth +$50 per day (depends on position size and days to expiration). Each day that passes, your option legs lose value. The far-out-of-the-money 115 call and 85 put decay the fastest.

**Time decay accelerates near expiration**, so theta is not constant—it ramps up in the final two weeks. If the underlying stays within the short strikes, theta alone can carry the position to full profitability.

But theta is worthless if the underlying moves against you before expiration. A 3-point drop in the first day might trigger a gamma loss that takes a week of theta decay to recover. This is the central tension: theta wants to hold the position and let time work; gamma wants to exit quickly if the market moves.

## Vega: the short volatility bet

An iron condor is **short volatility** because you sold calls and puts. [Vega](/vega/) measures the position's sensitivity to changes in [implied volatility](/implied-volatility/).

If implied volatility rises 1 percentage point, the value of your short calls and puts increases, which *costs* you (because you sold them). A 10-point rise in implied volatility might cost you 5–10% of your max profit, even if the underlying doesn't move.

Conversely, if implied volatility **falls**, you profit. Volatility crush at earnings or major announcements helps iron condors if the underlying stays within the strikes.

This is why iron condors work best in **low-volatility environments**:
- Stable sectors (utilities, consumer staples)
- Periods of range-bound trading
- Post-uncertainty (earnings announced; catalyst passed)

In high-volatility environments (earnings run-up, broad-market selloff), implied volatility is expensive, but the underlying is also more likely to break your strikes. You may profit from high vega at entry (collecting fat premiums), but lose that gain to gamma losses when the underlying moves.

## How greeks shift as the underlying moves

**Scenario: Underlying rallies from 100 to 107.**

- **Delta:** Your short 110 call now has delta ~+0.40; your short 90 put has delta ~−0.05. Net delta is now ~+0.35 (you are long-biased and would profit from further rallies, but you have already lost money).
- **Gamma:** The 110 call's gamma increases as it approaches strike; your gamma is now strongly negative. A further 2-point rally accelerates losses.
- **Theta:** Theta is now lower because the call spread is in-the-money. Only the out-of-the-money 90 put spread still decays in your favor.
- **Vega:** Your short call is now more vega-sensitive (near-the-money options have the highest vega). A volatility spike hits you harder.

**Result:** You are underwater on the call spread. Theta is working slower. Gamma is working against you hard. A further move to 110 triggers assignment on the short call. Most traders close the position now, taking a loss.

**Scenario: Underlying stays at 102.**

- **Delta:** Drifts slightly positive or negative, but remains near zero.
- **Gamma:** Remains negative but constant (gamma is highest at-the-money, so as the underlying moves slightly away from 100, gamma actually lessens a bit).
- **Theta:** Remains the main driver of profit. Each day, theta decay increases. By expiration, theta compounds to full max profit.
- **Vega:** Works for you—implied volatility hasn't spiked, so the short vega position is profitable.

**Result:** Position drifts to max profit as time passes.

## Managing an iron condor with greeks

**Entry:** Use vega to your advantage. Sell the iron condor when implied volatility is high (above the 50–75th percentile for the underlying). High IV means the premiums you collect are fatter, giving you a larger margin of safety.

**Exit:** Watch gamma and delta. If the underlying breaches a short strike, close the position immediately (or convert to a smaller spread). Letting gamma run in hopes that the underlying reverses is how small losses become max losses.

**Roll:** If the underlying trends toward a short strike early in the expiration cycle, roll the threatened spread up or down (sell the same spread one or more strikes farther out, use the credit to buy back the threatened strike). Rolling resets theta, locks in gains, and avoids assignment.

**Sizing:** The negative gamma is why position size matters. A gamma loss is proportional to the move squared, so a 5-point move is 25× worse than you'd expect from a simple delta calculation. Size accordingly.

## See also

<div class="wiki-seealso">

### Closely related

- [Delta](/delta/) — directional sensitivity to the underlying
- [Gamma](/gamma/) — the acceleration of delta; the iron condor's principal risk
- [Theta](/theta/) — time decay; the iron condor's profit engine
- [Vega](/vega/) — volatility sensitivity; short in an iron condor
- [Call Option](/call-option/) — one leg of the call spread
- [Put Option](/put-option/) — one leg of the put spread
- [Option](/option/) — the foundational derivatives
- [Implied Volatility](/implied-volatility/) — the market's expectation of future price swings

### Wider context

- [Call Risk](/call-risk/) — assignment risk on the short call
- [Covered Call](/covered-call/) — a simpler single-leg short-call strategy
- [Protective Put](/protective-put/) — insurance via long puts (opposite of short puts)
- [Volatility Smile](/volatility-smile/) — why different strikes have different implied vols
- [Derivatives Hedging](/derivatives-hedging/) — conceptual framework for options strategies
- [Time Decay Theta](/time-decay-theta/) — the decay mechanism underlying theta profit

</div>