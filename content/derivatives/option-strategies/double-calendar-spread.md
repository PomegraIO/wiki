---
title: "Double Calendar Spread"
description: "An options strategy that places calendar spreads at two different strike prices simultaneously to expand the range of profitable outcomes."
keywords:
  - calendar spread
  - option strategy
  - time decay
  - volatility trading
  - strike diversification
image: "/svg/derivatives.svg"
---

*A **double calendar spread** is an options strategy that simultaneously sells near-term options at one strike while buying longer-dated options at both that strike and a second strike, creating two overlapping calendar spreads. The tactic widens the profit zone by letting traders benefit from time decay across a broader range of underlying prices.*

## Why traders layer calendar spreads

A standard [calendar spread](/calendar-spread/) profits from the difference in [time decay](/time-decay-theta/) between a short-term option and a long-term option at the same strike. The trader sells the near-term contract, pockets the [premium](/option-premium/), and holds the long-term contract as a hedge. Profit is realised when the near-term option expires worthless while the longer-dated contract retains value.

The double calendar spread extends this idea. Instead of anchoring profit to a single [strike price](/strike-price/), the trader establishes calendar spreads at two strikes—often an [at-the-money](/at-the-money/) strike and either an [in-the-money](/in-the-money/) or [out-of-the-money](/out-of-the-money/) strike. This dual arrangement creates a wider profit tent. The trader benefits if the underlying settles near either strike when the short-term options expire, rather than only at the primary strike. It's a pragmatic choice when a single strike feels too narrow but buying more long-term contracts directly—a more expensive hedge—isn't warranted.

## Structure and mechanics

To set up a double calendar spread in calls:

- Sell two near-term call options at strike K₁ (e.g., ATM)
- Buy two longer-dated call options at strike K₁
- Sell two near-term call options at strike K₂ (e.g., a higher strike)
- Buy two longer-dated call options at strike K₂

The put variant mirrors this: sell near-term puts at two strikes, buy longer-dated puts at both. Each pair forms a complete calendar spread; together they bracket a range.

The net cost depends on the premiums exchanged. Since you're selling two near-term contracts and buying four longer-dated ones, [cash flow](/cash-flow-statement/) usually runs negative upfront—you're paying to widen the range. However, some traders engineer the strikes to approach breakeven or even a credit by choosing K₁ and K₂ where the longer-dated puts or calls fetch higher premiums than the near-term ones due to [volatility smile](/volatility-smile/) effects.

## Profit and risk zones

When the short-term options expire:

- **If the underlying is between K₁ and K₂**: Both short-term spreads potentially decay into profit. The trader still holds long-term contracts at both strikes, which can be closed for a gain or allowed to run.
- **Near K₁**: The calendar spread at K₁ harvests time decay efficiently; the K₂ spread may be out of the money, but the long-term K₂ contract still holds value.
- **Near K₂**: The K₂ calendar spread benefits; the K₁ spread may be deeper in the money, though the long hedge provides downside protection.
- **Far from both strikes**: Both calendar spreads face headwinds. The short-term options may expire worthless, but if the underlying moves sharply, [intrinsic value](/intrinsic-value/) losses in the long contracts can offset gains from the short leg.

Maximum loss is typically the debit paid upfront (for a debit-financed double calendar) minus any premium recovered when closing the long-term legs. Maximum profit is theoretically capped by the spread between the strikes and the premiums collected, though in practice the trader closes positions before expiration to manage risk.

## When to deploy it

A double calendar spread suits a trader who expects modest [volatility](/historical-volatility/) and relatively sideways price action over the near term but wants insulation against being wrong about direction. It's more capital-intensive than a single calendar spread yet less risky than a naked short position.

It also appeals in fragmented [implied volatility](/implied-volatility/) landscapes. If a certain strike is overpriced relative to others—common in earnings seasons or when [sector rotation](/sector-rotation/) creates local volatility hot spots—anchoring calendars at two strikes lets you diversify your bet against a single pricing anomaly.

## Managing the position

Since time decay works in your favour but [gamma](/gamma/) and directional moves against you, most traders roll the position before the short-term options expire. Rolling means selling new near-term contracts at one or both strikes and extending the long-term contracts further out. This harvests the time decay in stages and renews the profit opportunity.

If the underlying drifts significantly from both strikes, closing the long-term contracts and accepting the loss might be wiser than doubling down. The strategy's edge assumes price stickiness; when that assumption breaks, losses can compound across both strikes.

## Greeks and sensitivity

The [delta](/delta/) of a double calendar is neutral to slightly directional depending on your strike selection. A double calendar with K₁ at-the-money and K₂ [out-of-the-money](/out-of-the-money/) tilts bullish; flipping the strikes tilts bearish.

[Theta](/theta/) (time decay) is your friend when the underlying stays quiet. The strategy benefits from positive theta across both calendars.

[Vega](/vega/) is typically negative (short-term contracts have less vega exposure than long-term ones), so rising [volatility](/historical-volatility/) can hurt the position in its early life, though recovery is possible once the near-term legs shed enough premium.

## See also

<div class="wiki-seealso">

### Closely related

- [Calendar Spread](/calendar-spread/) — the foundational two-legged structure leveraged here
- [Covered Call](/covered-call/) — a simpler premium-collection strategy
- [Option Premium](/option-premium/) — what you sell and buy in these trades
- [Strike Price](/strike-price/) — the prices you anchor your calendar legs to
- [Time Decay](/time-decay-theta/) — the major force working in your favour
- [Implied Volatility](/implied-volatility/) — shapes what premiums you can collect
- [Sector Rotation](/sector-rotation/) — a market dynamic that can make certain strikes rich

### Wider context

- [Option](/option/) — the underlying building block
- Derivatives — the asset class
- [Volatility Smile](/volatility-smile/) — explains why premiums differ across strikes
- [Market Maker](/market-maker-trading/) — the institutions providing the liquidity you trade against

</div>
