---
title: "Fence Strategy"
description: "An options strategy combining long underlying, long at-the-money put, and short out-of-the-money call to define a bounded profit range while limiting losses."
keywords:
  - option strategy
  - collar
  - protective put
  - covered call
  - hedging
image: "/svg/derivatives.svg"
---

*A **fence strategy** is a three-legged options approach that owns the underlying stock, buys an [at-the-money](/at-the-money/) or slightly [out-of-the-money](/out-of-the-money/) [put](/put-option/) for downside protection, and sells an [out-of-the-money](/out-of-the-money/) [call](/call-option/) to fund the put. It creates a defined "fence"—a payoff zone bounded by the put and call strikes—appealing to holders who want certainty over maximum loss and maximum gain.*

## The hedged shareholder's dilemma

A shareholder holds stock for its long-term value but worries about near-term downside. Buying a protective put eliminates loss below the put's [strike price](/strike-price/)—but it's expensive, costing [theta](/time-decay-theta/) daily and requiring capital upfront.

A fence strategy solves this by funding the put through a short call. You sell upside above a chosen strike in exchange for the downside insurance. The result is a bounded return profile: you keep profits up to the call strike, lose nothing below the put strike, and accept a zero profit if the underlying trades between the strikes at expiration.

For risk-averse shareholders—especially those near retirement, managing concentrated positions, or navigating uncertain periods—the fence offers peace of mind. Losses are capped. Gains are capped. The surprise (if any) is limited.

## Structure and mechanics

To establish a fence on 100 shares currently trading at $100:

- **Own**: 100 shares at $100 (cost: $10,000)
- **Buy**: One [put option](/put-option/) at $95 strike (pay premium, e.g., $2 per share = $200)
- **Sell**: One [call option](/call-option/) at $105 strike (collect premium, e.g., $2 per share = $200)

Net cost of the hedge: $0 (if premiums match). At expiration:

- **Stock at $110**: You keep profits to $105 (the call strike). Your payoff = $105 + $0 = $105. Call is [in-the-money](/in-the-money/) and assigned; you sell the shares.
- **Stock at $100**: Both options expire worthless. Your payoff = $100. No gain, no loss on the hedge (but you've used capital and time).
- **Stock at $90**: Put is [in-the-money](/in-the-money/). You're protected; your payoff = $95 (the put strike). You lose $5 per share from your purchase price, but this is your maximum loss.
- **Stock at $80**: Put still delivers $95. Maximum loss is capped at $5 per share.

The "fence" is the range between $95 and $105—inside which you keep the underlying's actual movement, minus any net premium paid.

## Why it's called a fence

The term evokes boundaries. Above the call strike, you have a ceiling (your gains are capped). Below the put strike, you have a floor (your losses are capped). Between them is your actual hedge payoff. In a narrow market, you break even on the hedge itself, retaining your shares and capital for the next period.

Some call it a "[collar](/collar/)" when the put is at-the-money and the call is out-of-the-money, which is the fence structure. The terms are often used interchangeably, though "fence" sometimes connotes a deliberate strategy to define a tight range, while "collar" may be broader.

## When to use it

**Concentrated holdings**: You own a large block of a company stock (perhaps from [restricted stock](/founder-shares/) or an acquisition). You want to diversify gradually but preserve upside near-term. A fence lets you sleep at night.

**Pre-event uncertainty**: Before an earnings release, regulatory decision, or [credit event](/credit-event-sovereign/), volatility may spike. A fence caps your risk until clarity emerges.

**Liquidity planning**: You plan to sell within 6–12 months. A fence defines a target exit band, reducing paralysis from daily price swings.

**Dividend capture with protection**: You own a [dividend](/dividend/)-paying stock and want to stay through the [ex-dividend](/dividend/) date. A fence insures you against a sharp drop post-dividend while letting you keep gains to a ceiling.

**Retirement portfolios**: Retirees or near-retirees often favour fences. The capped loss is psychologically and financially valuable; the capped gain is a small price for certainty.

## Cost efficiency

The fence is cheapest when:

- [Implied volatility](/implied-volatility/) is high (premiums on both put and call are fat; the put becomes less expensive relative to the call).
- The strike separation is wide (a $95–$105 fence is cheaper than a $98–$102 fence, as the call premium is higher and the put premium is lower).
- The holding period is short (theta works faster; fewer days of decay to price in).

Ideally, the call premium covers or exceeds the put premium, making the hedge "free" or "net credit." In low-volatility regimes, you may pay a net debit to establish the fence.

## Variations

**Asymmetric fence**: Buy a put further [out-of-the-money](/out-of-the-money/) (e.g., $90) and sell a call closer (e.g., $103). This lowers the put cost but widens your loss zone; conversely, it raises upside cap. Risk-tolerant investors use this.

**Rolling fence**: At expiration, close both legs and open new ones at different strikes. This lets you harvest defined returns and reset the fence for changing market conditions.

**Fence with longer-dated call**: Buy a near-term put (to hedge a near-term event) and sell a far-dated call (to fund it and benefit from time decay over a longer period). This decouples your hedging horizon from your upside cap.

## Greeks and payoff characteristics

**Delta**: Net delta is approximately +1.0 (you own 100 shares). The bought put has negative delta (costs you upside potential near the strike), and the short call has negative delta. The long stock dominates.

**Gamma**: Near zero to slightly positive. Gamma is greatest near the put strike (downside); the call strike (upside) has negative gamma. Large moves can still cause losses in the "tails," though those tails are now fenced.

**Theta**: Slightly positive (call decay) minus slightly negative (put decay). If put and call have similar vega and decay speeds, theta is near breakeven. Some fences collect theta; others cost it.

**Vega**: Near zero, since you're long put and short call. If [implied volatility](/implied-volatility/) rises, both legs gain or lose in offsetting ways.

## Managing into expiration

As expiration approaches:

- If the stock is well inside the fence (e.g., between $95 and $105), you can roll both legs outward, resetting your hedge and capturing any remaining premium value.
- If the stock has rallied above the call strike, decide: accept assignment (sell the shares at $105) or buy back the call (closing the position) and ride upside with just the put as a residual hedge.
- If the stock has fallen below the put strike, you're protected at $95. At expiration, take the $95 payoff or buy back the put and reassess your conviction.

Early assignment is possible on both legs. The put seller has incentive to exercise if it's deep in the money; the call buyer has incentive to exercise if it's deep in the money and the stock is about to pay a dividend.

## See also

<div class="wiki-seealso">

### Closely related

- [Collar](/collar/) — the foundational variant
- [Protective Put](/protective-put/) — the downside leg in isolation
- [Covered Call](/covered-call/) — the upside leg in isolation
- [Put Option](/put-option/) — buys downside protection
- [Call Option](/call-option/) — funds the hedge
- [Strike Price](/strike-price/) — defines your fence boundaries
- [At-the-Money](/at-the-money/) — typical put-strike location

### Wider context

- Option Strategy — the broader category
- Derivatives — the asset class
- [Implied Volatility](/implied-volatility/) — drives premium costs
- [Delta](/delta/) — governs the position's directional exposure
- [Theta](/theta/) — time decay you harvest or pay

</div>
