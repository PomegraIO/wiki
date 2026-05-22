---
title: "Call Spread"
description: "Options strategy of buying a call at a lower strike and selling a call at a higher strike for net reduced premium cost."
keywords:
  - call option
  - vertical spread
  - debit spread
  - premium reduction
  - covered call variation
---

*A **call spread** (or bull call spread) is a [vertical spread](/wiki/vertical-spread/) where a trader buys a [call option](/wiki/call-option/) at one strike price and simultaneously sells a call at a higher strike, cutting the net premium paid and capping maximum profit. The long call preserves upside; the short call funds the purchase and caps the gain.*

<aside class="wiki-infobox">

| Aspect | Detail |
|--------|--------|
| **Structure** | Long call + short call, same expiration |
| **Net position** | Debit (cost to open) |
| **Max profit** | Strike width minus net debit |
| **Max loss** | Net debit paid |
| **Breakeven** | Long strike plus net debit |
| **Volatility bet** | Short leg benefits from falling IV |

</aside>

## Why traders use call spreads instead of naked long calls

Buying a single [call option](/wiki/call-option/) is straightforward: you pay the full premium and profit if the stock rises past the strike plus the premium at expiration. But that premium can be expensive for at-the-money or slightly out-of-the-money calls, especially when [implied volatility](/wiki/implied-volatility/) is high.

A call spread cuts that cost by funding the purchase with the premium from a short call. If you buy a 100 strike call and sell a 105 strike call on the same stock expiring in 30 days, you collect the 105-strike premium and pay less for the 100-strike call overall. The trade-off: your profit is capped at the 5-point spread between strikes, minus what you paid net.

This makes call spreads attractive to traders with limited capital or high-volatility stocks. You reduce outlay, define maximum loss, and keep defined upside in a narrow range.

## Setting strikes and width

A typical call spread is one point or five points wide, depending on the stock price and risk tolerance. A narrower spread (1–2 points) costs less to open but caps profits tightly. A wider spread (5–10 points) costs more but allows more upside. Most traders choose the width based on: (a) the stock's likely range over the hold period, and (b) how much premium they want to risk versus collect.

On a stock trading at 100, you might buy the 100 call and sell the 105 call if you expect the stock to end between 102 and 105 at expiration. If it closes at 108, your profit is capped at the 5-point spread.

## Call spreads as a [covered-call](/wiki/covered-call/) variant

A [covered call](/wiki/covered-call/) (owning stock and selling a call against it) is sometimes replaced by a [bull call spread](/wiki/bull-call-spread/) when the trader doesn't want to hold the shares. The spread replicates the short call's premium collection and profit cap but replaces stock ownership with a long call that behaves similarly if the underlying rallies.

The economics differ: a covered call gives you dividends and downside loss; a call spread gives you defined max loss (the net debit) and no dividends. For stocks about to pay dividends, the spread can be more efficient.

## [Implied volatility](/wiki/implied-volatility/) impact on pricing and P&L

When you open a call spread, you are long one [implied volatility](/wiki/implied-volatility/) exposure (the bought call) and short another (the sold call). If overall IV rises before expiration, the long call gains more value than the short call loses (because the short strike is further out of the money). Conversely, if IV collapses, the long call loses more.

This assymetry is why call spreads are often recommended in high-IV environments: you sell more expensive premium on the short leg and buy cheaper premium on the long leg relative to historical volatility.

## Breakeven and assignment risk

The spread breaks even at the long strike plus the net debit. If you paid a net debit of 1.50 on a 100/105 spread, breakeven is 101.50. Below that at expiration, you lose money; above the long strike, you begin to profit; above the short strike, profit is capped.

Early assignment risk is real if the sold call is in the money and the stock is ex-dividend soon. If assigned on the short leg, you are obligated to deliver shares at the sold strike—but if you are short the shares and the long call isn't exercised, you can end up short stock and need to cover.

## Tax and holding-period considerations

Each leg of the spread has its own holding period and gain/loss character. If held longer than one year, both legs qualify for [long-term capital gain tax](/wiki/long-term-capital-gain-tax/) treatment separately. However, if the spread is closed before expiration (a common practice to lock in early profits), the tax lot treatment depends on whether you closed legs individually or as a unit.

Most traders close both legs simultaneously using a single "close spread" order through their broker, which simplifies tax reporting.

<div class="wiki-seealso">

### Closely related
- [Vertical spread](/wiki/vertical-spread/) — the family of spreads (call, put, and variations)
- [Bull call spread](/wiki/bull-call-spread/) — the bullish-bias variant of a call spread
- [Call option](/wiki/call-option/) — the long-leg instrument
- [Implied volatility](/wiki/implied-volatility/) — critical pricing input that shifts spread value

### Wider context
- [Debit spread](/wiki/debit-spread/) — spreads where you pay net on entry
- [Covered call](/wiki/covered-call/) — an alternative premium-collection strategy
- [Option premium](/wiki/option-premium/) — the cost you negotiate when opening a spread
- [Options Greeks](/wiki/options-greeks/) — delta, vega, theta that govern spread behavior

</div>
