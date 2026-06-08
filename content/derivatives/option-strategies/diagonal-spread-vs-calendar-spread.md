---
title: "Diagonal Spread vs Calendar Spread"
description: "How diagonal spreads and calendar spreads differ in strike prices, delta exposure, and directional bias—and when to use each strategy."
keywords:
  - diagonal spread vs calendar spread
  - diagonal spread strategy
  - calendar spread options
  - option spreads
  - delta-neutral strategies
  - time decay trading
image: "/svg/derivatives.svg"
---

*A **diagonal spread vs calendar spread** comparison hinges on one critical difference: a calendar spread (horizontal spread) uses the same strike price across different expirations; a diagonal spread varies both strike and expiration, introducing directional exposure that a calendar spread lacks. Understanding this distinction is essential because it changes your [delta](/delta/) exposure, profit asymmetry, and the directional thesis you are implicitly betting on.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Diagonal Spread vs Calendar Spread — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives." />

<div class="wiki-infobox-caption">Both bet on [time decay](/time-decay-theta/); diagonal spreads add directional risk that calendars avoid.</div>

|   |   |
|---|---|
| **Strike structure** | Calendar: same strike; Diagonal: different strikes |
| **Expiration difference** | Both use multiple expirations (e.g., 30 days and 60 days) |
| **Delta exposure** | Calendar: near zero (delta-neutral); Diagonal: non-zero (directional) |
| **Profit driver** | Calendar: pure [time decay](/time-decay-theta/); Diagonal: time decay + direction |
| **Payoff shape** | Calendar: butterfly-like peak; Diagonal: asymmetric, tilted left or right |
| **Complexity** | Calendar: simple to construct; Diagonal: more moving parts |
| **Best for** | Calendar: volatility forecasting; Diagonal: directional conviction + time decay |

</aside>

## The fundamental structure: strikes and expirations

A **calendar spread** (also called a horizontal or time spread) sells a short-term option and buys a longer-term option at the *same strike price*. For example:

- Sell one 30-day call at $100 strike
- Buy one 60-day call at $100 strike
- Net cost: typically a debit (long call premium minus short call premium)

A **diagonal spread** sells a short-term option and buys a longer-term option at *different strikes*. For example:

- Sell one 30-day call at $100 strike
- Buy one 60-day call at $95 strike (below the sold strike for a bearish diagonal)
- Net cost: often lower debit or even a credit, depending on volatility

The strike difference is where the directional bet enters. In the example above, the diagonal is implicitly bearish: the longer-dated protection is positioned below current price, and the short call above is vulnerable to upside loss.

## Delta and directional exposure

Calendar spreads are **delta-neutral by design**. When you sell and buy calls (or puts) at the same strike, the deltas offset:

- Long 60-day $100 call: delta ≈ +0.55 (increases in value as stock rises)
- Short 30-day $100 call: delta ≈ −0.55 (decreases in value as stock rises, but you are short, so it is +0.55 in your position)
- Net delta: ≈ 0

The profit comes purely from time decay ([theta](/time-decay-theta/)) and [volatility](/historical-volatility/) contraction, not from price movement.

Diagonal spreads have **non-zero net delta**, which depends on the strike selection:

- **Bullish diagonal**: Long call is out-of-the-money (OTM) above the sold call. You are net long delta—you profit if the stock rises. Net delta: +0.20 to +0.40 (example).
- **Bearish diagonal**: Long call is out-of-the-money below the sold call (or long put is below short put). You are net short delta—you profit if the stock falls. Net delta: −0.20 to −0.40 (example).

This directional exposure means diagonal spreads are not pure time-decay plays; they are time decay *plus* a directional bet.

## Profit mechanics and [time decay](/time-decay-theta/)

Both strategies profit from time decay, but the shape of the profit curve differs markedly.

**Calendar spread profit curve**: Peaks near the sold strike. As the sold option expires, the long option (still 30 days out) retains significant value due to [theta](/time-decay-theta/). The spread widens, and you can close for a profit. Maximum profit is often realized when the stock remains near the sold strike at expiration; large moves in either direction reduce profit (because the long option's value also decays asymmetrically). The payoff resembles a flattened bell curve.

**Diagonal spread profit curve**: Tilted toward the direction of the long strike. If you sold a $100 call and bought a $95 call (bearish diagonal), the payoff is asymmetric:

- Large downside move: Both short and long calls expire worthless; you keep the credit. Profit is capped.
- Small downside or sideways move: The short call expires OTM; the long call still has value. You close for a wider spread. Profit is capped but higher than the downside limit.
- Upside move: The long call ($95) is ITM; the short call ($100) is ITM as well. You are pinned—loss is capped at the width of the strikes ($5) minus the net credit received.

The asymmetry means diagonal spreads reward moves in one direction and penalize the opposite.

## Volatility sensitivity

Calendar spreads are sensitive to implied [volatility](/implied-volatility/) changes:

- Rising IV: The long option (30 days out) gains value faster than the short option (already short, shrinking from 30 to 20 days). Spreads widen; profit increases.
- Falling IV: The long option loses value; the short option loses value slightly slower (due to gamma effects). Spreads narrow; profit decreases.

A calendar spread is, in effect, a **long [vega](/vega/)** position—you profit from volatility rising.

Diagonal spreads have a more complex volatility profile. The directional strike difference introduces [vega](/vega/) mismatches:

- A bearish diagonal with a lower long call benefits from IV rising (the long call is further OTM and gains less value per IV point), which partially hedges the long vega of the long call.
- The net vega exposure is smaller than a calendar spread but typically still positive (long longer-dated option, short shorter-dated).

## When to use each strategy

**Choose a calendar spread when:**
- You expect the stock to stay near a specific price but are unsure whether it will rise or fall.
- You want to express a view on implied [volatility](/implied-volatility/) (you believe it will rise) without taking directional risk.
- You are comfortable with the asymmetry—large moves reduce profit regardless of direction.
- You want simplicity: pick a strike, sell the front month, buy the back month.

**Choose a diagonal spread when:**
- You have a directional bias (bullish or bearish) and want to reduce the cost of your [long option](/option/) hedge.
- You want to profit from both time decay and a modest move in your favored direction.
- You can tolerate capped risk at a specific strike width.
- You are willing to manage the extra complexity—the long and short strikes require active selection and adjustment.

## Practical management and adjustments

Calendar spreads are managed passively: hold to near expiration of the short leg, then roll the short call (sell another shorter-dated call at the same or new strike) to reset the trade.

Diagonal spreads require more active management:

- If the stock moves toward your long strike, the long option gains intrinsic value; you may close early to lock in profit, or roll the short call to a new strike further away.
- If the stock moves against the diagonal (toward or past the short call), losses approach the maximum; you may cut the position or adjust by selling another call (converting to a ratio spread, which introduces new risks).

Adjustments are easier in calendar spreads (simple roll) and more involved in diagonal spreads (re-strike, ratio expansion, or unwind).

## See also

<div class="wiki-seealso">

### Closely related

- [Time decay (theta)](/time-decay-theta/) — how theta affects multi-leg options strategies
- [Delta and directional exposure](/delta/) — understanding net position delta
- [Call option](/call-option/) — mechanics of long and short calls
- [Implied volatility](/implied-volatility/) — how IV changes affect option spreads
- [Put option](/put-option/) — diagonal and calendar spreads using puts as well

### Wider context

- [Option premium and pricing](/option-premium/) — what drives option values
- [Greeks (delta, gamma, vega, theta)](/delta/) — sensitivity metrics for options
- [Covered call](/covered-call/) — another spread-like strategy for income
- [Protective put](/protective-put/) — downside insurance using puts and calls

</div>
