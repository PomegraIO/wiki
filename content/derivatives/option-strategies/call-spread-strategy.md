---
title: "Call Spread Strategy"
description: "Limited-risk options strategy combining a long call with a short call at a higher strike, capping both profit and loss."
keywords:
  - call spread
  - bull call spread
  - debit spread
  - vertical spread
  - limited-risk option strategy
---

*A call spread strategy is a [vertical spread](/wiki/vertical-spread/) option position that combines buying a [call option](/wiki/call-option/) at a lower strike price and selling a call at a higher strike, capping both risk and reward.*

<aside class="wiki-infobox">

| Aspect | Detail |
|--------|--------|
| **Structure** | Long call (lower strike) + Short call (higher strike) |
| **Initial Cost** | Net debit (long call more expensive than short) |
| **Max Profit** | Width of strikes minus debit paid |
| **Max Loss** | Initial debit paid |
| **Breakeven** | Long strike + debit paid |
| **Best Case** | Stock rises above short call strike |
| **Worst Case** | Stock falls below long call strike |

</aside>

## Mechanics and payoff

When you buy a $100 call and sell a $105 call for $2 net debit, you own the right to buy at $100 and have obligated yourself to sell at $105. If the stock is $107 at expiration:
- Long call at $100 is worth $7 (intrinsic value $107 − $100)
- Short call at $105 is worth $2 and you lose $2 (obligated to sell at $105 when worth $107)
- Net gain: $7 − $2 − $2 (initial debit) = $3

The width between strikes ($105 − $100 = $5) is your **max profit**: the difference between what you can sell (at the short strike) and what you can buy (at the long strike). Subtract your debit paid, and you have the net max profit. You profit dollar-for-dollar as the stock rises until the short strike, then gains cap out.

## Why traders use call spreads

**Cost reduction.** Buying a naked [call option](/wiki/call-option/) can be expensive; the [option premium](/wiki/option-premium/) decays with time and rises with [volatility](/wiki/historical-volatility/). By selling a [call](/wiki/call-option/) higher up, you offset the cost of the [call](/wiki/call-option/) you buy, making the position cheaper to enter. For income-conscious traders, this is the whole point: reduce the cost of directional bullish exposure.

**Defined risk.** Your max loss equals the debit paid, not unlimited. A [naked call](/wiki/naked-short-selling-ban/) has theoretically unlimited loss; a call spread caps it at, say, $2 per share. This makes position sizing predictable and forces discipline on [portfolio risk](/wiki/portfolio-mental-accounting/).

**Theta decay benefit.** As time passes and the stock does not move much, both calls lose value (due to [theta](/wiki/time-decay-theta/)). The long call decays, but so does the short call—and you benefit from the short call's decay since you are short it. The spread experiences "neutral [theta](/wiki/time-decay-theta/)" decay that is often less punishing than owning a naked call.

## Variations: bull call spread vs. bear call spread

A **[bull call spread](/wiki/bull-call-spread/)** (described above) bets the stock will rise. You profit if it goes above your [breakeven](/wiki/resistance-zone-ceiling/).

A **[bear call spread](/wiki/bear-call-spread/)** is the inverse: sell a lower-strike call and buy a higher-strike call. You profit if the stock stays below the short strike, losing money if it rises. Max profit is the credit received; max loss is the width of strikes minus the credit.

A bull call spread is a **debit spread** (you pay net to enter). A bear call spread is a **credit spread** (you collect net upfront). The choice depends on your market outlook and how much [premium](/wiki/option-premium/) is available at each strike.

## Greeks and hedging dynamics

A call spread's **[delta](/wiki/delta-option-greeks/)** (sensitivity to stock price) is the difference between the long call's delta and the short call's delta. At-the-money calls have ~0.50 delta; out-of-the-money calls have lower delta. A $100 long call ($100 strike) has ~0.50 delta; a $105 short call has ~0.40 delta. Net delta: ~0.10—you are slightly bullish but heavily [delta](/wiki/delta-option-greeks/)-neutral. This makes call spreads useful for trading [implied volatility](/wiki/implied-volatility/) rather than outright direction.

**[Vega](/wiki/vega-option-greeks/)** (sensitivity to [volatility](/wiki/implied-volatility/)) is also the difference: long vega on the long call, short vega on the short call. If the two strikes are not far apart, vega nearly cancels. A call spread profits from the short call's [volatility](/wiki/implied-volatility/) decay more than it loses on the long call—a useful feature if you believe [implied volatility](/wiki/implied-volatility/) will fall.

**[Theta](/wiki/time-decay-theta/)** is typically positive for call spreads, especially those centered near the current stock price. Time works in your favor; you earn money each day the stock does not move sharply.

## When to use vs. naked calls

A trader comparing a naked $100 call ($5 premium) vs. a $100–$105 call spread ($2 debit):
- Naked call: costs $5, max loss infinite, max profit unlimited. Best if you think the stock soars.
- Call spread: costs $2, max loss $2, max profit $3. Better if you want defined risk and cost savings.

The spread is ideal for traders with limited capital, those uncomfortable with naked call risk, or those trading a mildly bullish outlook. The naked call is for traders convinced of a sharp move and wanting unlimited upside.

## Assignment risk and early exercise

If you sell a call, the buyer can exercise it before expiration. If your short call is in-the-money, the buyer might exercise and you are obligated to sell the stock. If you also own the stock, this is covered—no problem. If you don't, you face a forced short position. Many traders close call spreads before expiration to avoid assignment drama.

<div class="wiki-seealso">

### Closely related
- [Vertical spread](/wiki/vertical-spread/) — General spread using two options of the same type at different strikes
- [Bull call spread](/wiki/bull-call-spread/) — Bullish variant of call spread
- [Bear call spread](/wiki/bear-call-spread/) — Bearish variant of call spread
- [Call option](/wiki/call-option/) — Right to buy at a fixed price

### Wider context
- [Options Greeks](/wiki/options-greeks/) — Delta, gamma, theta, vega, rho sensitivities
- [Implied volatility](/wiki/implied-volatility/) — Expected price fluctuations priced into options
- [Time decay](/wiki/time-decay-theta/) — Erosion of option value as expiration approaches
- [Debit spread](/wiki/debit-spread/) — Spread entered at net cost (you pay to enter)

</div>
