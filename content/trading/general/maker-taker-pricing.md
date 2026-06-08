---
title: "Maker-Taker Pricing"
description: "An exchange fee model in which the trader who provides liquidity (the maker) receives a rebate and the trader who removes liquidity (the taker) pays a fee."
keywords:
  - maker-taker fees
  - liquidity provision
  - exchange pricing
  - rebate structure
  - trading costs
  - order types
image: "/svg/trading.svg"
---

*In a **maker-taker** fee model, the [stock exchange](/stock-exchange/) charges different fees to two sides of a trade: the trader who posts an order first (the "maker") receives a small rebate or pays a negative fee, whilst the trader who fills that order (the "taker") pays a fee to the exchange. This structure aims to incentivise the posting of [limit orders](/limit-order/) that provide [liquidity](/liquidity-risk/), tightening [spreads](/bid-ask-spread/) and deepening order books across the market.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Maker-Taker Pricing — key facts</div>

<img src="/svg/trading.svg" alt="An abstract editorial mark for trading mechanics." />

<div class="wiki-infobox-caption">The exchange rewards liquidity supply and charges for liquidity demand.</div>

|   |   |
|---|---|
| **What it is** | Two-tier fee structure: negative fee (rebate) for makers, positive fee for takers |
| **Typical costs** | Makers paid $0.001–$0.003 per share; takers charged $0.002–$0.005 per share |
| **Applies to** | All limit orders that are posted first and later executed against |
| **Originated** | Mid-2000s, adopted by most major [stock exchanges](/stock-exchange/) |
| **Effect** | Tightens spreads by making liquidity provision profitable; may distort order flow |
| **Alternative** | Uniform (flat) fee model used by some smaller exchanges |

</aside>

## The origins of maker-taker

Before the mid-2000s, most exchanges charged a single, uniform fee per trade. Everyone paid the same amount per share, regardless of whether they posted an order or hit one. But in the race to attract trading volume, exchanges began experimenting. What if they paid traders to post orders? The trader who sits at the [market maker](/market-maker-trading/)'s post, holding inventory and absorbing risk, could earn a rebate. The trader who comes in and immediately buys or sells would pay a fee.

The logic was elegant: offer a reward for providing liquidity, and traders will post tighter [bid-ask spreads](/bid-ask-spread/) and deeper order books. The market becomes cheaper and more efficient for everyone else. By the early 2010s, most major [stock exchanges](/stock-exchange/) had adopted the maker-taker model. It became the dominant fee structure globally.

## How maker-taker fees work in practice

Suppose the [NASDAQ](/nasdaq/) charges:
- Makers: rebate of $0.002 per share
- Takers: fee of $0.003 per share

A trader posts a [limit order](/limit-order/) to buy 1,000 shares of XYZ at $50. That trader is the maker. If that order sits on the book unexecuted, no fee is incurred. If another trader comes in with a [market order](/market-order/) and sells 1,000 shares directly into that buy order, both traders now have a transaction. The maker (the buyer who posted first) receives a $2 rebate (1,000 × $0.002). The taker (the seller who hit the order) pays a $3 fee (1,000 × $0.003).

The net cost to the taker is $3; the net gain to the maker is $2. The exchange retains the spread: $1 per 1,000 shares. The taker effectively pays $0.003 per share to cross the [bid-ask spread](/bid-ask-spread/); the maker is paid to wait.

## The effect on spreads and liquidity

Maker-taker pricing succeeds at its main goal: spreads tighten. Traders are willing to post [limit orders](/limit-order/) that sit on the book because they know they will earn a rebate if filled. A market maker can profitably post a $0.01 spread (one [tick](/tick-size/)) and still earn from the rebate on executions. In the old uniform-fee world, the spread might have been $0.02 or wider.

Tighter spreads benefit everyone who trades. A retail investor buying 100 shares now pays one tick instead of three. An institutional fund [executing](/vwap-execution/) a large order crosses less total spread over the course of many small fills. Overall market efficiency improves.

Order-book depth also increases under maker-taker. Because a posted order generates income, traders compete to post at the best available prices, filling the book with limit orders. This deep book of visible orders reassures traders that they can execute at reasonable prices without moving the market too far.

## Criticisms and unintended consequences

The maker-taker model has its critics. One complaint is that it incentivises high-frequency traders and algorithmic strategies that rapidly post and cancel orders. A trader can earn rebates by posting in anticipation of short-term price moves, then cancelling if the prediction fails. This creates order-book "flash" that never executes but clogs data feeds and confuses retail traders about the true depth of the market.

A second criticism is that maker-taker fees can distort order routing. Some traders with large order flow may negotiate discounted fees or special rebates from particular exchanges in exchange for routing orders there. This creates a two-tier market: sophisticated traders with negotiating power pay less, whilst ordinary traders pay the posted tariff. The regulatory benefit of the fee structure—incentivising liquidity—may be captured by a few insiders.

A third concern is that the taker fee incentivises the use of [dark pools](/alternative-trading-system/) and [alternative trading systems](/alternative-trading-system/), which do not charge these fees and do not post their orders on public exchanges. As order flow migrates off-exchange, the visible order book thins, and [spreads](/bid-ask-spread/) on the primary exchange may actually widen. The intended effect reverses.

Most controversial is the question of fairness. Is it right that the trader who provides liquidity is rewarded at the expense of the trader who removes it? Or is the taker simply paying for the privilege of instant execution? Depending on one's view, maker-taker fees are either an elegant incentive structure or a subsidy to market makers at the expense of the investing public.

## Variations and alternatives

Some exchanges charge a flat fee to both maker and taker. Others use a "maker-rebate" model where the maker gets paid and the taker is only charged a standard fee if the trade moves the spread. A few use a "tiered" rebate system: high-volume traders who post more orders receive larger rebates. The [New York Stock Exchange](/new-york-stock-exchange/) and [NASDAQ](/nasdaq/) both use variants of maker-taker pricing, with rebates scaled by monthly volume.

Some traders actively arbitrage the fee structure using [scalping](/scalping/) or "rebate trading"—posting orders purely to collect the rebate, with no intention to hold inventory. This is controversial and has attracted regulatory scrutiny.

## See also

<div class="wiki-seealso">

### Closely related

- [Bid-ask spread](/bid-ask-spread/) — the cost of crossing the market
- [Market maker](/market-maker-trading/) — trader who buys and sells for rebates and spreads
- [Limit order](/limit-order/) — posted order that earns rebates under maker-taker
- [Market order](/market-order/) — executed order that pays taker fees
- [Alternative trading system](/alternative-trading-system/) — off-exchange venue that may use different fee models
- [Tick size](/tick-size/) — minimum price increment that interacts with fee incentives
- [Order flow](/algorithmic-trading/) — direction and volume of buy and sell orders
- [High-frequency trading](/algorithmic-trading/) — rapid strategies exploiting fee structures

### Wider context

- [Stock exchange](/stock-exchange/) — venue where listed securities trade
- [Securities and Exchange Commission](/securities-and-exchange-commission/) — US regulator of exchange fee models
- [NASDAQ](/nasdaq/) — major US exchange using maker-taker pricing
- [New York Stock Exchange](/new-york-stock-exchange/) — primary US equities market with tiered maker-taker fees
- [Liquidity](/liquidity-risk/) — ability to buy and sell without moving the price

</div>
