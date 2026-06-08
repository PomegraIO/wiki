---
title: "Selecting the Right LEAPS for a Poor Man's Covered Call"
description: "LEAPS selection for poor man's covered calls requires balancing delta, time decay, and intrinsic value. Learn the guidelines for strike and expiry."
keywords:
  - poor mans covered call leaps selection
  - LEAPS options
  - poor mans covered call
  - option strike selection
  - covered call strategy
image: /svg/derivatives.svg
---

*A **poor man's covered call** is a diagonal spread: a long [LEAPS](/derivatives-hedging/) call (typically lasting 1–3 years) paired with repeatedly sold short-term calls. The strategy replicates the economics of owning stock and selling covered calls, but at lower capital cost. Success depends entirely on choosing a LEAPS that maintains enough value and [delta](/delta/) to behave like real ownership.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">LEAPS Selection — strategy guidelines</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">The long LEAPS is the portfolio base; its delta and expiry determine how much premium you can harvest.</div>

|   |   |
|---|---|
| **Delta target** | 0.70–0.90 (80+ delta preferred for highest intrinsic value) |
| **Time to expiry** | 12–36 months; longer = lower cost, more [time decay](/time-decay-theta/) drag |
| **Strike selection** | 10–30% out-of-the-money (OTM); balance cost vs. upside cap |
| **Intrinsic value** | Most should be [in-the-money](/in-the-money/), especially in first 12 months |
| **Roll frequency** | Sell calls 30–45 days to expiry; repeat every 4–6 weeks |
| **Cost basis** | LEAPS cost 30–60% of stock ownership; leverage at lower capital outlay |
| **Breakeven** | LEAPS cost + short call premiums collected; monitor as rolls proceed |

</aside>

## Why LEAPS Delta Determines Strategy Viability

The **poor mans covered call leaps selection** hinges on one metric: [delta](/delta/). Delta measures how much an option price moves when the underlying stock moves $1. A delta of 0.80 means the LEAPS moves $0.80 when the stock moves $1.

For a poor man's covered call to work, the long LEAPS must behave like stock ownership. Real stock has a delta of 1.0—it moves dollar for dollar with the stock price. A LEAPS with delta of 0.70 or lower will not keep pace. You will own the upside optionality but miss out on 30% of the move.

Traders typically target LEAPS with delta of 0.80–0.90. At these levels, the LEAPS moves almost like stock, capturing the bulk of price appreciation. Critically, high-delta LEAPS are in-the-money (ITM), meaning they have intrinsic value—the portion of the option price that is pure economic worth, regardless of time value.

A LEAPS with delta below 0.70 is too OTM. If the stock rises 20%, a low-delta LEAPS might rise only 8–12%, leaving money on the table. Conversely, excessively high [gamma](/gamma/) at very low strikes means the LEAPS will hemorrhage value quickly if the stock falls, turning a mild decline into a severe drawdown for the strategy.

## Strike Selection: The Capital-Upside Trade-off

Traders choose LEAPS strikes on a spectrum between cost efficiency and upside capture.

**Aggressive selection**: Buy LEAPS 10–15% out-of-the-money. A $100 stock, for example, you buy the $110 call. This is cheaper—perhaps $18–$22 per share—than the $100 call. The delta is lower (maybe 0.70–0.75), so upside capture is weaker. However, capital outlay is reduced. If you had $15,000 to invest, buying $110 LEAPS lets you control more shares' worth of exposure than buying $100 LEAPS, which might cost $35–$40 per share.

**Conservative selection**: Buy LEAPS 5–10% ITM or at-the-money. A $100 stock, you buy the $100 call (or $95 call). This costs more—$40–$50 per share—but the delta is much higher (0.85–0.95). Upside capture is nearly complete. You also have substantial intrinsic value, so the option holds value even if [volatility](/cryptocurrency-exchange/) collapses.

**The leverage insight**: The poor man's covered call works because you are using long-dated option leverage to replace stock capital. A LEAPS costing $20 replaces $100 of stock ownership. That is 5:1 leverage—or 5x capital efficiency. The cost of this leverage is paid via two channels: the [time decay](/time-decay-theta/) on the long LEAPS (which works against you) and the premium from your short calls (which offsets that decay).

## Time-to-Expiry: The Decay Anchor

LEAPS typically expire 12–36 months out. Within that window, traders face a classic trade-off.

**Longer LEAPS (24–36 months)**: Cheaper to buy because [time value](/time-value/) is spread across more days. A 3-year LEAPS on a $100 stock might cost $22 per share; a 1-year LEAPS costs $28. Over a 3-year horizon, the longer LEAPS costs less. However, theta (time decay) is more insidious over 3 years. The strategy must generate enough premium from short calls to overcome 36 months of decay. If you sell covered calls but only harvest 3–4% of premium per month, you will lag the long-term theta bleed.

**Shorter LEAPS (12–18 months)**: More expensive upfront but decay more slowly per calendar month. A 1-year LEAPS expires faster, so you are forced to roll the long leg sooner—either sell it at a loss or buy a new 1-year LEAPS and lock in losses. This creates friction. However, the shorter timeline is simpler to model and control.

Most practitioners settle on 18–24 months as the sweet spot: long enough that the initial cost is manageable, short enough that [time decay](/time-decay-theta/) per month is predictable and surmountable via short call premiums.

## Intrinsic Value as a Safety Guardrail

The **intrinsic value**—the ITM portion of the option price—is your hedge against [volatility](/cryptocurrency-exchange/) collapse. If you buy a $100 call on a $105 stock for $35, you have $5 of intrinsic value and $30 of [time value](/time-value/). If volatility crashes, that $30 time value might evaporate, but the $5 intrinsic value is locked in. Your loss is capped.

For a poor man's covered call, owning high intrinsic value is critical. If you buy a deeply OTM LEAPS (say, $120 strike on a $100 stock), it is mostly time value. If the stock stalls for 6 months, volatility declines, and implied volatility falls, your LEAPS could lose 50% of value even if the stock price is unchanged. You would then sell short calls against a depressed LEAPS base, unable to recover.

Traders targeting 0.80+ delta LEAPS are also ensuring they own meaningful intrinsic value. The relationship is direct: higher delta = more ITM = more intrinsic value = better downside protection.

## Rolling and Maintenance: Balancing Cost and Frequency

Once you own the LEAPS, you sell short-term calls (30–45 days to expiry) against it, typically every 4–6 weeks. The premiums collected offset your cost basis and the LEAPS' time decay.

The choice of short call strike is separate from the LEAPS strike. You might own a $100 LEAPS and sell a $110 call, creating a defined-risk vertical spread for that month. If the stock rises above $110, you keep the stock (or keep the LEAPS' $110 value cap).

Over time, rolls can become expensive. If you are forced to buy back a profitable short call early to avoid assignment, transaction costs compound. High-delta LEAPS (like the $100 strike) mean your short calls will be ITM more often, triggering earlier assignment and forcing faster rolls.

Mid-range delta LEAPS ($110 strike with 0.70–0.75 delta) allow short calls to be sold further OTM more often, extending the holding period and reducing friction.

## Monitoring Breakeven and Unwinding

The true cost basis of a poor man's covered call is the LEAPS cost minus cumulative short call premiums collected. If you buy a 18-month $100 LEAPS for $35 per share and sell $110 calls 5 times over 18 months for a total of $15 per share in premiums, your real cost is $35 − $15 = $20 per share.

If the stock rises from $100 to $120, your LEAPS is worth $120 (or close to it, depending on time value). You profit $120 − $20 = $100 per share. If the stock falls to $95, your LEAPS is worth $95 and you have lost $25 per share (5 points on a $100 position, less the cumulative premium hedging).

As the LEAPS approaches expiry (say, 3–6 months out), you have a choice: roll into a new LEAPS, accepting a new cost basis, or close the position and realize the gain or loss. Rolling keeps the strategy alive but locks in new leverage costs.

## See also

<div class="wiki-seealso">

### Closely related

- [Poor Man's Covered Call](/poor-mans-covered-call-leaps-selection/) — strategy overview and mechanics
- [Delta](/delta/) — option sensitivity metric governing intrinsic value capture
- [Time Decay (Theta)](/time-decay-theta/) — cost of holding long-term options
- [Covered Call](/covered-call/) — underlying single-leg strategy
- [Intrinsic Value](/intrinsic-value/) — the in-the-money cushion protecting position value

### Wider context

- [Option](/option/) — foundational derivative instrument
- [Derivatives Hedging](/derivatives-hedging/) — broader hedging and income strategies
- [Volatility Smile](/volatility-smile/) — volatility dynamics affecting LEAPS pricing
- [Vega](/vega/) — volatility sensitivity that impacts LEAPS repricing
- [Call Option](/call-option/) — foundational option type used in the strategy

</div>