---
title: "Strangle"
description: "A long call and long put, both out-of-the-money, that profits from large price moves while limiting loss to premium paid."
keywords:
  - strangle option strategy
  - out-of-the-money
  - volatility strategy
  - low-cost volatility
  - directional uncertainty
---

*A **strangle** is an [options](/wiki/option/) strategy that buys a call and a put on the same [underlying asset](/wiki/asset-allocation/), with both [options](/wiki/option/) out-of-the-money (OTM). The call is struck above the current price; the put is struck below. The strangle is cheaper than a [straddle](/wiki/straddle/) (which uses at-the-money strikes) and profits from large price moves in either direction while capping losses to the total premium paid.*

<aside class="wiki-infobox">

| Key Fact | Detail |
|----------|--------|
| **Long call** | Bought OTM; profits if price rises above strike + premium |
| **Long put** | Bought OTM; profits if price falls below strike − premium |
| **Cost** | Lower premium than straddle; appeals to lower-budget traders |
| **Profit zone** | Move above upper breakeven OR below lower breakeven |
| **Max loss** | Total premium paid (call + put) |
| **Max gain** | Theoretically unlimited on upside; capped on downside at strike price |
| **Ideal scenario** | Earnings announcement, merger risk, high [implied volatility](/wiki/implied-volatility/) before expansion |

</aside>

## Structure and mechanics

To construct a strangle, a trader:

1. **Buys a call option** with a strike price above the current spot price (say, spot at $100, call strike at $105).
2. **Buys a put option** with a strike price below the current spot price (say, put strike at $95).
3. **Both expire on the same date.** Most strangles use the same expiration to keep the strategy simple.

The cost is the sum of the call and put premiums. A $100 stock with a $105 call costing $2 and a $95 put costing $2 would have a total strangle cost of $4.

## Profit and loss zones

The strangle profits if the stock moves significantly in either direction:

**Upside profit.** If the stock rises above $105 + $4 = $109, the call is in-the-money and begins generating profit. The put expires worthless. The breakeven is the call strike plus the total premium paid.

**Downside profit.** If the stock falls below $95 − $4 = $91, the put is in-the-money and generates profit. The call expires worthless. The breakeven is the put strike minus the total premium paid.

**Maximum loss.** If the stock stays between the two strikes at expiration, both options expire worthless and the trader loses the full premium paid ($4 in this example).

**Typical returns.** The strangle is a bet on [implied volatility](/wiki/implied-volatility/) — if realized volatility (the actual price moves) exceeds implied volatility at entry, the strategy profits. If realized volatility is lower than implied, it loses.

## Why strangles are cheaper than straddles

A [straddle](/wiki/straddle/) uses the same call and put, but both at the current [at-the-money](/wiki/at-the-money/) strike (the $100 strike in our example). Because ATM options have more intrinsic exposure, their premiums are higher; an ATM straddle on a $100 stock might cost $8 total, versus $4 for the strangle. Traders who believe the move will be large but want to save on premium often choose strangles over straddles.

The trade-off is clear: a strangle requires a larger move to profit than a straddle (the stock must move above $109 or below $91, versus above $108 or below $92 for a $100-strike straddle). But if you expect high volatility and have a limited budget, the strangle is more capital-efficient.

## Typical use cases

**Earnings and announcements.** Before earnings, a company's stock often shows elevated [implied volatility](/wiki/implied-volatility/). A trader might buy a strangle, betting that the earnings announcement will move the stock significantly. If the stock gaps up or down after the announcement, the strangle profits.

**Merger or M&A speculation.** If a company is rumored to be acquisition target, market participants bid up implied volatility. A strangle can capture a large move if the deal is announced or denied.

**Macroeconomic events.** Before central bank decisions, jobs reports, or geopolitical announcements, markets often show elevated implied vol. Strangles can position for the inevitable large move.

**Volatility expansion.** When [implied volatility](/wiki/implied-volatility/) is expected to expand, the strangle becomes more valuable even if the stock price doesn't move, because the call and put premiums increase. This is a pure [vega](/wiki/vega-option-greeks/) bet — betting on rising volatility itself.

## Greeks and risk management

A long strangle is **long [vega](/wiki/vega-option-greeks/)** — it profits if implied volatility rises — and **long [gamma](/wiki/gamma-option-greeks/)** — it benefits from large moves. It is roughly neutral to [delta](/wiki/delta-option-greeks/) at inception (if the strikes are symmetric around the spot), so price movement in either direction can be profitable.

If the stock moves dramatically in one direction early, one leg becomes in-the-money while the other decays toward worthlessness. A trader can close out the profitable leg early and let the losing side expire, locking in a partial profit and capping loss.

**[Theta](/wiki/theta-option-greeks/) decay** is the main enemy of strangles. As expiration approaches, both out-of-the-money options decay in value. If the stock stays quiet, the strangle erodes day by day. This is why strangles are ideally held through an announcement or event that triggers a move; holding a strangle in a quiet, sideways market is a slow bleed of capital.

## Variants and adjustments

**Ratio strangle.** A trader might buy a call and sell more puts (or vice versa), creating an unbalanced risk profile that can reduce cost or target a specific market view.

**Butterfly spread variant.** Some traders combine strangles with other spreads to create more complex payoff structures with tighter risk bands.

**Rolling strangles.** An active trader might close one strangle at a profit and immediately open another for the next earnings or event, creating a continuous income from short-term volatility spikes.

**Wider or tighter strikes.** Adjusting how far out-of-the-money the strikes are changes the cost and the required move to profit. Very wide strangles (strikes far from spot) are cheaper but require bigger moves; tight strangles are closer to straddles in cost and required move.

## Comparison to other volatility strategies

**Straddle.** More expensive; profits from any large move regardless of direction. Lower breakeven range.

**Strangle.** Cheaper; still profits from large moves in either direction. Higher breakeven range.

**[Iron Condor](/wiki/iron-condor/).** Sells a strangle against a wider strangle, capping risk. Lower cost and more directional; suited to range-bound markets.

**[Butterfly Spread](/wiki/butterfly-spread/).** Tighter risk profile; profits only in a narrow range. Lower cost and risk but smaller profit potential.

## Tax and liquidation considerations

In the US, options profits are taxed as short-term [capital gains](/wiki/capital-gains-tax/) if held under one year (ordinary income rates) or long-term if over one year (preferential rates). Because strangles are typically held for days to weeks around events, most strangle profits are short-term gains.

Closing out a strangle before expiration in profit or to cap losses is straightforward: sell the in-the-money option to lock profit and let the out-of-the-money option expire. Brokers calculate the net P&L on the close.

## Market conditions for success

Strangles work best when:
- Implied volatility is elevated relative to expected realized volatility.
- An announcement or event is imminent (earnings, Fed decision, merger decision).
- You have confidence that the move will be large enough to overcome the premium paid.
- You can time the entry to capture the vol spike before the move.

Strangles suffer when:
- Implied volatility is low and the market is quiet (no catalyst).
- Realized volatility is much lower than implied at entry.
- You enter after the big move has already happened and vol is now collapsing.

<div class="wiki-seealso">

### Closely related
- [Straddle](/wiki/straddle/) — Similar strategy with at-the-money strikes; more expensive
- [Iron Condor](/wiki/iron-condor/) — Selling a strangle to cap risk
- [Implied Volatility](/wiki/implied-volatility/) — Option premium reflects expected move size
- [Options Greeks](/wiki/options-greeks/) — Vega, gamma, theta sensitivity

### Wider context
- [Out-of-the-Money](/wiki/out-of-the-money/) — Strike relationship to spot price
- [Call Option](/wiki/call-option/) — The upside hedge in the strategy
- [Put Option](/wiki/put-option/) — The downside hedge in the strategy
- [Butterfly Spread](/wiki/butterfly-spread/) — Alternative low-cost volatility strategy

</div>
