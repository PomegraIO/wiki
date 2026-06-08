---
title: "FX Straddle and Strangle"
description: "Volatility strategies that buy or sell both calls and puts to profit from large moves regardless of direction, or to harvest premium if the currency stays calm."
keywords:
  - fx straddle
  - fx strangle
  - volatility strategy
  - long straddle
  - short strangle forex
image: "/svg/forex.svg"
---

*An **FX straddle** is a volatility strategy that simultaneously buys (or sells) both a [call option](/call-option/) and a [put option](/put-option/) at the same [strike price](/strike-price/), allowing the trader to profit from a large currency move in *either* direction. A **strangle** is similar but uses calls and puts at *different* strike prices — typically an [out-of-the-money](/in-the-money/) call and an out-of-the-money put — reducing the premium cost and requiring a larger move to profit. Both are pure bets on [volatility](/currency-volatility/), divorced from direction.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">FX Straddle and Strangle — key facts</div>

<img src="/svg/forex.svg" alt="An editorial mark for foreign exchange instruments." />

<div class="wiki-infobox-caption">Volatility trades that profit from either big moves (longs) or stay profitable in calm markets (shorts).</div>

|   |   |
|---|---|
| **What it is** | Long: buy call + put at same (straddle) or different (strangle) strikes. Short: sell both, betting the move stays small. |
| **Also called** | Straddle, strangle, volatility long, volatility short, market-neutral volatility |
| **Straddle strike** | Typically at-the-money forward |
| **Strangle strikes** | 10-delta or 25-delta out-of-the-money in each direction |
| **Payoff** | Piecewise: two-legged payoff, unlimited profit above call strike or below put strike (long), capped profit in middle (short) |
| **Key metric** | [Implied volatility](/implied-volatility/) vs. realized volatility; [gamma](/gamma/) decay |
| **Time horizon** | Days to weeks for tactical trades; months for structural volatility bets |

</aside>

## Straddle: the at-the-money play

A long straddle on EUR/USD at 1.0900 means buying the 1.0900 call and buying the 1.0900 put. The trader pays the sum of both [option premiums](/option-premium/) — say, 1.2% of notional. Profit occurs if the currency moves far enough in *either* direction to overcome that cost.

If EUR/USD rallies to 1.1100, the call is deeply in-the-money and profits. The put expires worthless. Net gain is approximately the spot move minus the initial premium paid.

If EUR/USD crashes to 1.0700, the put profits and the call expires worthless. Again, the net is the spot move minus the premium.

If EUR/USD stays in the range [1.0812, 1.0988] (roughly 1.0900 ± 1.2%), both options expire worthless or out-of-the-money, and the trader loses the entire premium paid.

The breakevens are at strike price ± the total premium paid. A straddle is therefore a **long volatility** bet: the trader profits if [realized volatility](/currency-volatility/) — the actual historical moves over the life of the option — exceeds [implied volatility](/implied-volatility/) — the market's expectation priced into the options.

## Strangle: the cheaper alternative

A long strangle at 25-delta uses a 1.1050 call and a 1.0750 put, well away from the current spot of 1.0900. The total premium paid is smaller (each option is out-of-the-money and thus cheaper), but the currency must move further to profit.

If EUR/USD drifts to 1.0850, a strangle loses money; a straddle might break even or lose less. But if the currency explodes to 1.1200, the strangle's call generates the same profit as a straddle's call, and the strangle owner has paid less premium overall, so the net profit is higher.

Strangles suit traders who are confident a currency *will* move big but unsure of timing. Straddles suit traders with tighter confidence on timing but less certainty on size.

## The short side: harvesting premium in calm markets

A **short straddle** — selling both the call and put at-the-money — is a bet that the currency will *stay calm*. The trader pockets the premium from both legs. As long as the currency doesn't move more than the premium collected, the trader keeps the profit.

This is popular during periods of low geopolitical risk or when central banks have signaled a pause in tightening. The strategy suffers from **[gamma](/gamma/) risk**: if the currency suddenly makes a large move (a tail event), the losses accumulate rapidly. Selling premium on volatility is profitable in *normal* times but catastrophic in *abnormal* times.

A **short strangle** is milder: the trader sells out-of-the-money calls and puts, capturing less premium but facing less gamma risk. The breakeven loss levels are further out, giving more breathing room before losses pile up.

## The volatility arbitrage: implied vs. realized

The core edge in straddle and strangle trading is betting that **[implied volatility](/implied-volatility/) is mispriced relative to realized volatility**.

Suppose the market prices in 10% annualized [implied volatility](/implied-volatility/) for a 3-month EUR/USD straddle. The trader believes realized volatility will be 15%. The trader buys the straddle (long volatility). Over three months, if EUR/USD swings are indeed 15% annualized (large moves), the realized moves will exceed the break-even threshold, and the trade profits.

Conversely, if the trader believes realized volatility will be 5% and the market is asking 10% [implied volatility](/implied-volatility/), the trader sells the straddle, betting that calm will prevail and the market's expectations are too dire.

This trade is called a **volatility arbitrage** or **vol-realization trade**. Hedge funds run these constantly, using historical volatility models and tail-risk metrics to estimate what realized volatility *should* be, then comparing to market prices.

## Gamma decay and time value

Both long straddles and strangles suffer from time decay. As the option approaches expiration, the [time value](/time-value/) of both the call and put erodes, even if the currency hasn't moved. This is particularly acute near expiration (high [gamma](/gamma/) / [theta](/theta/) ratio). A trader holding a long straddle for a week before expiration may find that time decay has consumed all the profit, even if the move was larger than expected — if the move happened *too late*.

Conversely, short straddles and strangles *benefit* from time decay. The seller pockets the time value as it evaporates, which is why selling premium is attractive in calm, predictable environments.

## Straddle and strangle in earnings events and central-bank meetings

A corporate treasurer, uncertain whether a central bank will hike or hold rates, might buy a straddle on the currency before the announcement. Whatever the decision, the currency will likely move sharply, and the straddle owner profits.

This is common for:
- Central bank decisions (ECB, Federal Reserve, BoE rate calls)
- Non-farm payroll data releases
- Geopolitical elections or referendums
- Major economic surprises

A short strangle on the same event is a bet that the market is overpricing the expected move — that the surprise, if it comes, won't be as large as the option market expects.

## Multi-leg considerations: correlation and execution

In practice, buying and selling both legs simultaneously is difficult in liquid markets. A trader may get a quote on the straddle as a whole (broker bundles them), or may leg into the position over time, risking that prices move between the first and second leg execution. Costs add up in live trading, shrinking the edge.

For pairs with wider bid-ask spreads (emerging-market currency options, for instance), a straddle may be prohibitively expensive to establish.

## See also

<div class="wiki-seealso">

### Closely related

- [Call option](/call-option/) — the upside leg of a straddle or strangle
- [Put option](/put-option/) — the downside leg
- [Implied volatility](/implied-volatility/) — the option-market price that straddle traders are betting against
- [Gamma](/gamma/) — the acceleration cost if the currency moves unexpectedly
- [Theta](/theta/) — time decay, which favors short straddles and hurts long straddles

### Wider context

- [Currency volatility](/currency-volatility/) — the macro regime that makes straddles and strangles profitable or not
- [Hedge fund](/hedge-fund/) — institutions that systematically run vol-realization trades
- [Volatility smile](/volatility-smile/) — the shape of the option surface that prices individual strikes

</div>
