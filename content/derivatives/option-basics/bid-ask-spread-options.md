---
title: "Bid-Ask Spread in Options"
description: "The gap between buy and sell prices in options, often wider than equities due to lower volume and higher hedging costs."
keywords:
  - bid-ask spread options
  - option pricing liquidity
  - option trading costs
  - option slippage
image: "/svg/derivatives.svg"
---

*The [bid-ask spread](/bid-ask-spread-options/) in options is the gap between what a buyer will pay (bid) and what a seller will accept (ask). It's wider than in [stocks](/stock/)—often 5–20% of the option premium—because each contract is unique, [market makers](/market-maker-trading/) face higher hedging costs, and trading is thinner. A [call](/call-option/) on Apple might quote 2.10 bid / 2.20 ask; you'll pay 2.20 to buy or receive 2.10 to sell. That dime gap (and wider ones on illiquid strikes) is pure cost, and it compounds if you trade frequently.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Bid-Ask Spread in Options — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives markets." />

<div class="wiki-infobox-caption">The cost of immediacy in derivatives markets.</div>

|   |   |
|---|---|
| **What it is** | The difference between the highest price a buyer offers and the lowest price a seller will accept |
| **Measured in** | Dollars (or points, for index options); expressed as a percentage of premium or as absolute cents |
| **Typical width** | 5–20% of the premium for liquid strikes; 50%+ for illiquid or far out-of-the-money strikes |
| **vs. stocks** | Option spreads are typically 2–10x wider as a percentage of price |
| **Key drivers** | [Open interest](/option-open-interest/), [volatility](/historical-volatility/), time to expiry, distance from [strike](/strike-price/) |
| **Also called** | Bid-offer spread, the spread, option spread |

</aside>

## Why options spread wider than stocks

When you buy Apple stock, the bid-ask spread is often a penny or a nickel—negligible as a percentage of the $150+ share price. The market for Apple equity is vast: millions of shares trade daily. A [market maker](/market-maker-trading/) can buy 1,000 shares and resell them within seconds with near-zero risk.

Option spreads are different. Each call or put on each [strike](/strike-price/) and expiration is its own market. A call expiring in three months at $150 is not the same product as one expiring in four months or at $155. An Apple call $150 strike might have 500,000 open contracts; a $155 call might have 2,000. The deeper the [open interest](/option-open-interest/), the tighter the spread. The thinner the market, the wider the bid-ask, because the [market maker](/market-maker-trading/) is holding inventory at higher risk of loss.

Additionally, a market maker buying a call option is not neutral. She's long a leveraged asset; if the stock falls 5%, her call is worth 20% less. To hedge that risk, she must buy shares of the underlying stock (costly, with its own spread) or purchase a [put](/put-option/) (also costly). Those hedging costs—commissions, slippage, and price movement during the hedge—are baked into the option's bid-ask spread.

## How spreads vary by strike and expiry

The tightest spreads cluster near the [at-the-money](/at-the-money/) strike and the nearest [expiration](/expiration-date/). An Apple $150 call expiring in one week, with Apple trading at $151, might quote 1.80 bid / 1.85 ask—a five-cent spread (2.8%). That same call three weeks out might be 1.85 bid / 1.90 ask (2.7%). Move to $155, out-of-the-money, and it widens to 0.30 bid / 0.40 ask (25% spread). Bid the $160 call and you're in a desert: 0.05 bid / 0.15 ask (67% spread on a dime option).

Time to expiry also matters. As an option nears its final day, especially if it's near or out of the money, the spread can explode. The market maker faces acute hedging pressure—she can't hold a position overnight if expiry is tomorrow—and retail volume thins. A $150 call expiring in two days might trade at 0.10 bid / 0.30 ask even if it's at the money.

## The cost compounds over time

A single round-trip trade on a liquid strike might cost 1–2% of your premium in spread. Acceptable. But if you're a day trader or swing trader—entering and exiting the same strike multiple times per week—spreads erode your edge. Buy at ask, sell at bid, and you're giving up 5–10% per round-trip on moderately liquid options, 15–50% on thin ones. Scale that over dozens of trades, and spread is your largest expense.

Professional traders manage this by:
- Trading only the deepest [open interest](/option-open-interest/) strikes (usually the 1–2 closest to the money in the nearest expiry)
- Using limit orders and waiting for favorable prices (not pressing with market orders)
- Trading in size to negotiate better prices or finding institutional counterparties
- Avoiding expiring contracts and far out-of-the-money bets where spreads blow up

Retail traders often underestimate spread costs because brokers quote "mid-market" prices on charts, not real bid-ask levels. You see 2.15 on your platform and assume you can buy at 2.15; in reality, the ask is 2.20 and you pay 2.20.

## The role of [implied volatility](/implied-volatility/) and [Greeks](/delta/)

A market maker doesn't quote spreads in isolation. She adjusts them based on [implied volatility](/implied-volatility/) and time decay. When IV is high—during earnings or market stress—spreads widen because the market maker's hedging cost rises (she needs a larger buffer to stay safe). When IV collapses, spreads compress.

[Delta](/delta/), [gamma](/gamma/), and other [Greeks](/delta/) also influence spreads. An option with high gamma (short-dated, near the money) requires more frequent rehedging, so the market maker widens the spread to compensate for the effort and risk. An option with low gamma (long-dated, far from the money) is cheaper to hedge, so spreads tighten.

## Spread hunting and market maker behavior

Savvy traders exploit spread widening. When a stock is about to report earnings, options traders know IV will spike and spreads will widen. Some will close positions in advance (selling at tighter spreads before the announcement). Some will wait and trade after the move (buying dips when everyone is panicked). Some will sell [straddles](/straddle/) or other multi-leg positions designed to profit from spread compression once volatility mean-reverts.

Market makers compete for order flow. If one market maker's bid-ask on a strike is 2.10–2.20 and another's is 2.05–2.25, traders will hit the tighter bid (2.10) to sell and lift the tighter ask (2.20) to buy. Competition between market makers keeps spreads honest, at least in liquid series. In illiquid options, there may be only one market maker or a handful, and spreads can blow out to absurd levels.

## Spread width as a liquidity signal

Traders use spread width as a proxy for [open interest](/option-open-interest/) and trading activity. A 1–2% spread signals a liquid, well-patronized strike. A 5–10% spread suggests moderate liquidity; the strike exists but isn't a hub of activity. A 20%+ spread is a red flag: this strike is either extremely far out of the money, expiring very soon, or simply ignored by the market. Trading it is like wading through mud—you'll move the price against yourself.

Before entering a trade, professional traders check spreads. A fantastic setup on paper—a 50-delta short-term call with a high [implied volatility](/implied-volatility/) skew—is worthless if the [bid-ask spread](/bid-ask-spread-options/) is 30% and you can't leg out without huge slippage.

## See also

<div class="wiki-seealso">

### Closely related

- [Option Open Interest](/option-open-interest/) — How contract volume depth affects spread width
- [Option Volume](/option-volume/) — Daily activity and its impact on liquidity costs
- [Option Lot Size](/option-lot-size/) — Standard contract multipliers that scale your exposure and spread costs
- [Implied Volatility](/implied-volatility/) — How IV changes influence bid-ask spreads
- [Delta](/delta/) — The Greeks that shape market maker hedging costs
- [Market Maker Trading](/market-maker-trading/) — How market makers set spreads and manage inventory

### Wider context

- [Option](/option/) — The foundational derivative contract
- [Bid-Ask Spread](/bid-ask-spread/) — The same concept in equities; narrower due to higher volume
- [Over-the-Counter Market](/over-the-counter-market/) — Where many options trade with wider spreads
- [Strike Price](/strike-price/) — Why strikes near the money have tighter spreads

</div>
