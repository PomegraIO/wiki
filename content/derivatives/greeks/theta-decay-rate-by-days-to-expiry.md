---
title: "Theta Decay Rate by Days to Expiry"
description: "Theta decay accelerates as expiration approaches; time decay is non-linear. Learn how the last 30 days of an option's life drain value fastest."
keywords:
  - theta decay rate days to expiry
  - theta acceleration near expiration
  - time decay options
  - theta decay non-linear
image: "/svg/derivatives.svg"
---

*The time value of an option does not drain at a constant rate. **Theta decay** — the daily loss to time — is slow for the first two months, then sharpens dramatically in the final month, and becomes ferocious in the last week. This non-linear schedule reshapes the economics of option strategies and defines why expiration proximity matters so much to traders.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Theta Decay — accelerating with expiration</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives." />

<div class="wiki-infobox-caption">Time decay is slowest early and fastest at the end.</div>

|   |   |
|---|---|
| **What it is** | Daily loss in option value due to the passage of time (all else equal) |
| **Acceleration point** | Visible at 30 days; acute at 7 days; extreme on expiration day |
| **Impact on buyers** | Negative; you bleed money every day the stock doesn't move |
| **Impact on sellers** | Positive; you collect premium as time evaporates |
| **Peak magnitude** | Last 7–10 days, when theta can exceed [gamma](/gamma-risk-near-expiration/) risk |
| **Typical schedule** | 10% decay in first 90 days, 50% decay in final 30 days |

</aside>

## The mathematics of non-linear decay

An option's time value follows no straight line. Imagine a 90-day at-the-money call trading at $3.00. Fifty days later, with 40 days left, that same call might trade at $2.10 — a loss of $0.90 or 30% of original value. But twenty-five days further out (15 days to expiration), the call trades at $0.80, a loss of $1.30 or 62% of original value.

The pattern is clear: the second month bleeds 30% of value, but the final two weeks drain another 62%. Theta does not halve with each passing day; it compounds. Mathematically, theta accelerates because the denominator in the option's time value decreases: an option with one week left has far fewer days of "volatility benefit" remaining than one with four weeks left.

In formal terms, if **T** is time to expiration and **σ** is volatility, the [time value](/time-value/) of an option depends on **σ × √T**. As **T** shrinks, the square root function flattens; the decay per day increases. With ten days left, one day lost is 10% of the remaining time window. With forty days left, one day is only 2.5% of the window. The percentage drain multiplies the impact of each passing day.

## The shift at 30 days to expiration

Professional traders treat the 30-day mark as a critical threshold. Before 30 days, theta is manageable — an option buyer can afford to wait and hope for a move in the underlying. After 30 days, decay accelerates visibly. A trade that was profitable on day 45 becomes breakeven or worse by day 30 unless the underlying has moved in your favor.

This scheduling is baked into options market pricing. Option [premiums](/option-premium/) are highest relative to realized volatility when there are 60–90 days left; they become expensive for buyers precisely because they have low theta. By day 30, buyers have already paid for much of the remaining time decay in the form of the premium itself; the seller's edge starts compounding.

Sell-side options traders often focus on the 21–30 day window as the "sweet spot" for profitability — long enough to collect meaningful theta, short enough that the absolute decay per day is substantial, but before gamma risk becomes acute.

## Buyers versus sellers: the race against time

For an **option buyer**, theta is a constant headwind. You pay a premium upfront and bleed that premium every day the underlying does not move. In the first month, that bleed is tolerable — you have time for a move to occur. In the final month, theta turns vicious. An at-the-money call with one week left loses roughly half its remaining value just from time decay, even if the stock price never changes.

This is why option buyers must be right about direction *and* move *soon*. A buyer who expects a 5% move eventually but is not sure *when* will lose money if the move occurs after expiration — or will suffer ruinous decay if the move is slow to unfold.

For an **option seller**, theta is your ally. You pocket the premium upfront and watch it vanish as days pass — that vanishing premium becomes your profit. All else equal, the passage of time is working in your favor. But the tradeoff is [gamma risk](/gamma-risk-near-expiration/): as theta accelerates near expiration, gamma does too, forcing costly rehedging.

The seller's economic reality is harsh: late in the option's life, you have collected most of your profit from theta, but now must protect against [gamma](/gamma-risk-near-expiration/) bleed on shrinking premium. A seller who wants to close a position with one week left may find that market conditions have deteriorated and no one wants to buy the residual risk.

## The final week: theta meets gamma

In the last seven days, theta becomes the dominant P&L driver for short option positions. A short at-the-money call might lose $0.30 from [gamma](/gamma-risk-near-expiration/) if the stock makes a 5% move, but gain $0.45 from theta decay. For a net-short-gamma trader, theta is the majority of profit — if the trade is profitable at all.

But those final days are also when [gamma](/gamma-risk-near-expiration/) becomes most acute. A short position in the final week is short both gamma (forced to rehedge at bad prices) and long theta (collecting rapid decay). The gamma losses compound faster than theta can offset them if realized volatility is high.

This is why option sellers often close positions early — a week or two before expiration — to lock in theta profits before gamma consumes them. Waiting for expiration day itself is aggressive and suitable only for traders with large positions and sophisticated hedging infrastructure.

## Calendar spread mechanics: selling near-term theta

The **calendar spread** — buying a longer-dated option and selling a shorter-dated one at the same strike — is a pure play on theta acceleration. When you sell a 30-day option and buy a 60-day option, you are short the sharper decay (30-day theta) and long the slower decay (60-day theta). As the short-term option expires and the long-term option rolls forward, your position benefits from the theta differential.

The profit exists specifically because theta accelerates non-linearly. Early in the position, the short leg decays only slightly faster than the long leg; the profit is modest. But in the final 10–15 days of the short option, theta spike narrows the price gap, and your spread widens. The strategy profits most when implied volatility is stable and realized volatility is low — pure theta harvest, undisturbed by gamma.

## Theta and dividend-paying stocks

For stocks paying dividends, theta on call options is reduced by the present value of the dividend. The [call buyer](/call-option/) loses the dividend, a cost baked into the option's price. Conversely, put buyers benefit slightly from dividend reduction (lower expected stock price), so theta on puts is less negative near ex-dividend dates. Near expiration, dividend effects become immaterial because time to the dividend payment is nearly zero.

## See also

<div class="wiki-seealso">

### Closely related

- [Theta](/theta/) — time decay parameter
- [Time Decay Rate by Days to Expiry](/theta-decay-rate-by-days-to-expiry/) — this article
- [Gamma Risk Near Expiration](/gamma-risk-near-expiration/) — gamma accelerates alongside theta
- [Option Premium](/option-premium/) — what you pay (or collect) for time value
- [Implied Volatility](/implied-volatility/) — drives the magnitude of theta

### Wider context

- [Options](/option/) — the instrument itself
- [Time Value](/time-value/) — the premium above intrinsic value
- [Delta](/delta/) — rate of change of option price
- [Derivatives Hedging](/derivatives-hedging/) — managing time decay risk

</div>