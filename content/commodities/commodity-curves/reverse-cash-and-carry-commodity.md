---
title: "Reverse Cash-and-Carry Arbitrage in Commodity Markets"
description: "How reverse cash-and-carry arbitrage works in commodity futures when backwardation creates profitable short-spot, long-futures trades."
keywords:
  - reverse cash and carry arbitrage
  - commodity backwardation
  - arbitrage futures markets
  - commodity curve trading
  - contango backwardation spread
image: "/svg/commodities.svg"
---

*A **reverse cash-and-carry arbitrage** is a short-spot, long-futures trade that exploits deep [backwardation](/backwardation/) in commodity markets. When a commodity's future contract trades significantly cheaper than the physical asset, traders can lock in risk-free profit by buying futures, shorting the spot commodity, and financing the position until delivery — a mirror image of the classical cash-and-carry play that enforces limits on how steep backwardation can become.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Reverse Cash-and-Carry — key facts</div>

<img src="/svg/commodities.svg" alt="An abstract editorial mark for commodities trading." />

<div class="wiki-infobox-caption">The trade that punishes excessive backwardation and keeps futures prices from collapsing below spot.</div>

|   |   |
|---|---|
| **Position** | Short spot commodity, long futures contract |
| **Market condition** | Deep backwardation (futures < spot price) |
| **Profit source** | Futures price increase toward spot at maturity |
| **Key costs** | Short-sale borrow cost, convenience yield foregone |
| **Time frame** | Until futures delivery date |
| **Risk profile** | Nearly riskless if arbitrageur controls delivery |

</aside>

## When backwardation invites the reverse carry trade

[Backwardation](/backwardation/) — when near-term futures trade above far-dated ones, or when futures trade below spot — occurs when supply is tight or immediate demand is high. Oil refineries scrambling for crude, power plants facing winter, or grain markets after poor harvests all show backwardation. The steeper the backwardation, the more attractive the reverse carry becomes.

The classical [cash-and-carry arbitrage](/backwardation/) works when [contango](/contango/) is too rich: buy spot, sell futures, finance the carry, pocket the spread. Reverse cash-and-carry does the opposite. It short-sells the physical commodity, buys futures, and holds until the futures converge to spot at delivery. The trader profits if the backwardation shrinks — which it almost always does as the contract approaches expiration.

Consider crude oil. If spot trades at $75 a barrel but the futures contract six months out trades at $70, a trader can short spot (borrow crude, sell it for $75), buy the six-month futures for $70, and finance the short position. When that contract expires, it converges to spot. If spot is $75 and the futures converge there, the trader locks in a $5-per-barrel spread, minus financing and borrow costs.

## The mechanics: financing and delivery

The reverse carry is not quite riskless, but it comes close for a well-capitalized trader. Here's the sequence:

1. **Borrow and sell the commodity.** The trader borrows the physical commodity — crude oil, copper, wheat, whatever — and sells it at today's spot price. This requires access to a lending market and willingness to pay borrow fees.

2. **Buy the futures contract.** Simultaneously, buy a futures contract that matures in the same period. This locks in a known future purchase price.

3. **Finance the short.** The trader must finance the short sale, keeping the cash proceeds in a money-market account or using the proceeds as margin. Financing cost is often the largest expense.

4. **Hold to delivery.** As the futures contract approaches maturity, it converges to spot. On delivery, the trader takes delivery of the commodity through the futures contract, returns it to the lender, and settles the trade. The spread between the short sale price and the delivery price is the gross profit; subtract borrow fees, financing costs, and commissions.

The key insight: if futures are too cheap relative to spot, reverse carries will proliferate until the gap closes. Smart traders with access to repo markets, borrowing desks, and physical inventory can execute this in minutes. The trade is capital-efficient and, for a truly integrated commodity firm, nearly mechanical.

## Why it matters: enforcing the backwardation floor

Unlike the classical cash-and-carry, which is only attractive when contango is absurdly deep, reverse carries become profitable at much smaller backwardation spreads. A 1–2% backwardation over a three-month horizon might make a reverse carry viable if financing costs are low and the trader can borrow the commodity cheaply.

This creates a **lower bound on how cheap futures can become relative to spot**. If futures drop too far below spot, reverse carry traders step in, buy futures (pushing the price up), and short spot (adding supply pressure). The combined effect narrows the backwardation. Market efficiency isn't perfect — storage costs, convenience yield, and transaction costs mean some backwardation is structural — but the reverse carry is the mechanism that prevents it from spiraling into absurdity.

In crisis moments — when storage is clogged and spot demand is acute — backwardation can still spike. During the March 2020 oil crash, front-month crude futures traded briefly below zero while spot (though depressed) remained above it, because storage capacity vanished and physical delivery became impossible. But once physical constraints ease, reverse carries flood in and flatten the curve.

## Convenience yield and structural limits

The reverse carry also reveals why some backwardation is "sticky." **Convenience yield** — the benefit of holding physical inventory rather than futures — makes shorting the commodity cheaper than it appears on paper. A refinery that holds crude benefits from being able to respond to unexpected supply disruptions. A power plant stockpiling coal gains scheduling flexibility. These benefits don't appear on a balance sheet but reduce the effective cost of holding spot.

When convenience yield is high — signaling supply stress — the gap between spot and futures can remain substantial even after reverse carries push prices. The arbitrage isn't truly riskless because the arbitrageur forgoes that convenience yield. A trader with no operational need for the commodity cannot fully replicate the profit opportunity a refinery or utility enjoys.

For major commodities — crude, metals, grains — convenience yield is typically modest during normal supply. But in supply shocks, it widens dramatically and can justify deeper backwardation than mechanical arbitrage alone would predict.

## Limits and frictions

Not all traders can execute reverse carries effectively. Physical commodity access is restricted; borrowing markets are not equally efficient for all assets; and delivery logistics vary. Agricultural commodities are harder to short than crude (you can't easily borrow wheat). Precious metals are easier, because there's a deep lease market and refiners/mints actively participate in arbitrage.

Small traders or speculators cannot execute reverse carries; the [bid-ask spreads](/bid-ask-spread/), borrowing costs, and deposit requirements are prohibitive. This means backwardation can persist for retail traders even while institutional players find it profitable to arbitrage. The market may seem "broken" to a day trader unaware that a Goldman Sachs desk six floors up is collecting the spread in microseconds.

Reverse carries also require credit and balance-sheet capacity. A trader must post margin to short spot and buy futures. During liquidity crises, repo spreads blow out and financing becomes expensive. The profitable trade becomes unprofitable or unexecutable.

## The takeaway

Reverse cash-and-carry arbitrage is the flip side of the classical carry trade. It emerges when [backwardation](/backwardation/) becomes too steep and forces prices to adjust. The trade polices the [commodity curve](/backwardation/), preventing futures from drifting too far below spot. Understanding when and why it becomes profitable is essential for predicting curve shape and spotting supply-demand imbalances in physical markets.

## See also

<div class="wiki-seealso">

### Closely related

- [Backwardation](/backwardation/) — the market condition that makes reverse carries profitable
- [Contango](/contango/) — the opposite curve shape and the classical carry trade
- [Futures contract](/futures-contract/) — the exchange-traded instrument used in the arbitrage
- [Commodity curve](/backwardation/) — the term structure of commodity prices over time
- [Basis risk](/basis-risk/) — the risk that spot-futures convergence is imperfect

### Wider context

- [Arbitrage](/backwardation/) — the mechanics of risk-free profit in markets
- [Convenience yield](/backwardation/) — the economic benefit of holding physical inventory
- [Cash conversion cycle](/cash-conversion-cycle/) — how traders finance inventory
- [Derivatives hedging](/derivatives-hedging/) — risk management using futures

</div>
