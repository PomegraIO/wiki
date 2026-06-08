---
title: "Call Backspread"
description: "An option strategy that sells fewer near-the-money calls and buys a greater number of out-of-the-money calls to profit from explosive upside moves."
keywords:
  - call option
  - option spread
  - ratio spread
  - directional trading
  - volatility trading
image: "/svg/derivatives.svg"
---

*A **call backspread** (also called a call ratio spread) sells a smaller number of [at-the-money](/strike-price/) or slightly out-of-the-money calls, then buys a larger number of farther out-of-the-money calls at a higher strike. The position reverses the typical "ratio" relationship, creating a net debit that profits most aggressively when the underlying rallies hard through the long call strike.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Call Backspread — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives." />

<div class="wiki-infobox-caption">A bullish, asymmetrical structure that turns limited upside risk into outsized gains above a breakeven.</div>

|   |   |
|---|---|
| **What it is** | Sell n calls at strike A; buy 2n calls at strike B (B > A) |
| **Also called** | Call ratio spread, call backspread |
| **Max profit** | Theoretically unlimited (above the long call strike) |
| **Max loss** | Limited to initial debit if stock stays below short strike |
| **Ideal market** | Strong bullish conviction; expect a breakout move |
| **Key risk** | Capped gains between strikes; unlimited loss if rally stalls near short strike |
| **Legs** | Two (short call, long call) |

</aside>

## The asymmetrical structure

A simple call backspread works like this: sell 1 call at strike $100, then buy 2 calls at strike $105. The two long calls are cheaper than the one short call you sold, so you typically collect a net credit. This credit is your maximum profit if the stock stays below $100 at expiration.

The magic happens if the underlying rallies above $105. Your 2 long calls are now in the money by more than your 1 short call, so profits accelerate. At $110, for instance, you're long one call worth $5 (the excess of buys over sells), minus any extrinsic value in the original trade. The asymmetry—selling fewer than you buy—inverts the typical spread risk/reward.

The name "backspread" refers to this reversal. A standard [call spread](/call-option/) (buy lower, sell higher) caps upside; a backspread flips the quantity relationship to unleash upside while sacrificing the middle ground.

## When the credit matters

The initial cash flow is often a credit, not a debit. You sell 1 contract at a higher [option premium](/option-premium/), then buy 2 at a lower premium; if the math favours you, you pocket the difference. This credit cushions small moves downward.

But the credit comes at a cost: if the stock rallies modestly into the space between your two strikes (between $100 and $105 in the example), both legs lose money. Your short call gains value rapidly, and your long calls gain value more slowly because the extrinsic value is still meaningful. The worst outcome often occurs around the short strike, where you've surrendered the credit and haven't yet captured the explosive upside.

Some traders deliberately structure the backspread as a debit, buying farther-out calls than necessary, to reduce or eliminate the worst-case loss. That trade-off sacrifices the credit for a cleaner risk profile.

## The role of implied volatility

High [implied volatility](/implied-volatility/) helps backspreads because the sold call is worth more relative to the bought calls. When IV is elevated, you can sell the short call for more premium and still afford the long calls, making the structure cheaper or more profitable.

Conversely, a sharp drop in volatility—especially post-earnings—can whipsaw the trade. Your sold call may lose value faster than your bought calls, eroding the credit or forcing a realized loss if you close early.

The strategy is most attractive when you expect both a directional move and a volatility event. Earnings announcements are classic setups: IV rises going into earnings, you sell the short call at a fat premium, then the stock gaps on the announcement. If it gaps up past your long calls, you win big; if it gaps down, you lose the credit but your long calls limit the damage.

## Risk and reward asymmetry

The call backspread is inherently bullish with a limited downside. Below the short strike, you've already pocketed the credit and simply watch the position decay. Your loss is capped at the initial debit (if you structured it that way) or at zero (if you collected a credit).

But between the short and long strikes, the position is a loser. And above the long strike, every dollar the stock rises nets you roughly one dollar of profit (minus the cost of the spread). This is the appeal: you're essentially levered upside with defined downside.

The catch is that the stock rarely rockets straight through both strikes. It often stalls or reverses in the squeeze zone, forcing you to either close at a loss or hold through uncertainty. Many backspread trades are managed before expiration—closed early if the directional bet turns sour, or rolled if the stock hits a local top.

## Common variations and sizing

Traders use 1x2 (sell 1, buy 2), 1x3, or even 1x4 backspreads depending on conviction and capital. A 1x4 gives you more leverage and a bigger profit cap but concentrates risk more sharply around the short strike.

Some traders run a "broken wing" backspread by buying a third call far out of the money to cap the theoretical unlimited loss if the stock soars. This reduces upside profit but turns the trade into a defined-risk position.

## When to deploy a call backspread

Use a call backspread when you have high conviction in an upside move and expect a catalyst—earnings, FDA approval, acquisition news, or a technical breakout. The strategy is especially attractive if you believe the market is underpricing the upside risk, which often shows up as a relatively low [implied volatility](/implied-volatility/) relative to historical moves.

It is least suitable for guesswork or low-conviction trades. The compressed payoff zone between strikes makes timing critical. If you're wrong about direction, you pay the cost. If you're right about direction but the stock moves sideways, you bleed time and volatility.

Backspreads also demand active management and discipline. Holding to expiration with an unfavourable stock price is usually a mistake.

## See also

<div class="wiki-seealso">

### Closely related

- [Put Backspread](/put-backspread/) — the downside equivalent for bearish directional moves
- [Double Diagonal Spread](/double-diagonal-spread/) — sells time on both sides while managing directional risk
- [Reverse Calendar Spread](/reverse-calendar-spread/) — exploits short-term volatility while capping long-term exposure
- [Option Premium](/option-premium/) — the value collected and risked in backspread trades
- [Implied Volatility](/implied-volatility/) — the key leverage point for entering and exiting backspreads profitably
- [Strike Price](/strike-price/) — the critical lever for structuring backspread ratios

### Wider context

- [Option](/option/) — the foundational contract for all spreads
- [Delta](/delta/) — directional sensitivity that determines upside profit capture
- [Volatility Smile](/volatility-smile/) — the IV pattern that can make backspreads cheap or expensive
- [Protective Put](/protective-put/) — an alternative way to hedge upside risk

</div>
