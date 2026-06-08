---
title: "Exchange Fee Schedule"
description: "The tiered fees that stock and options exchanges charge market participants for liquidity provision and consumption, directly shaping total trading costs."
keywords:
  - exchange fees
  - maker-taker fees
  - liquidity provision
  - trading costs
  - order routing
image: "/svg/trading.svg"
---

*An **exchange fee schedule** is the published structure of charges a trading venue imposes on market participants. Modern schedules split fees into maker rates (paid by firms providing liquidity by posting passive orders) and taker rates (paid by firms consuming liquidity by hitting existing orders), with tiered discounts for high-volume participants. These fees directly determine the net cost of every [market order](/market-order/) and shape competitive incentives across the market.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Exchange Fee Schedule — key facts</div>

<img src="/svg/trading.svg" alt="An abstract editorial mark for trading and costs." />

<div class="wiki-infobox-caption">The published rate card that determines what liquidity costs at each venue.</div>

|   |   |
|---|---|
| **What it is** | Tiered per-share fees charged by an exchange for liquidity provision and consumption |
| **Structure** | Maker rates (typically lower) and taker rates (higher), with volume-based discounts |
| **Charged on** | Equities and options, separately; sometimes futures and other assets |
| **Typical range** | $0.00005–$0.003 per share; options vary widely |
| **Published by** | [NYSE](/new-york-stock-exchange/), [NASDAQ](/nasdaq/), regional, and alternative exchanges |
| **Rebates** | [Makers](/market-maker-trading/) often receive credits (negative fees) during low-volume periods |

</aside>

## The maker-taker model

In 2001, the [NASDAQ](/nasdaq/) invented the maker-taker model: instead of charging all participants equally, it began paying firms that supplied liquidity (makers) and charging those that consumed it (takers). A [market maker](/market-maker-trading/) posting a passive limit order would receive a credit; a trader hitting that order with a market order would pay a fee. This reversed the old economics and sparked a revolution.

The [NYSE](/new-york-stock-exchange/) initially resisted but eventually adopted the model. The idea was elegant: rewards liquidity provision, penalizes liquidity consumption, and gives venues a lever to compete for order flow. By setting maker rebates higher than taker fees, a venue could attract the passive orders necessary to build depth and width of spreads.

Today, the maker-taker model dominates equity markets. Nearly every major venue publishes two separate rate schedules: one for makers, one for takers, with both typically declining as volume increases.

## Reading a schedule: the structure

A typical equity exchange schedule looks like this:

| Maker | Monthly Volume | Rebate |
|:---:|:---:|:---:|
| 0–1M shares | −$0.0004 per share |
| 1M–5M shares | −$0.0005 per share |
| 5M+ shares | −$0.0006 per share |

| Taker | Monthly Volume | Fee |
|:---:|:---:|:---:|
| 0–1M shares | +$0.003 per share |
| 1M–5M shares | +$0.0029 per share |
| 5M+ shares | +$0.0028 per share |

A [market maker](/market-maker-trading/) posting 10 million shares per month at the highest tier earns $0.0006 per share rebated. A retail taker executing 100,000 shares per month pays $0.003 per share. The spread between them creates an incentive for market makers to post and takers to consolidate volume at a single venue.

## Why tiers matter

Volume tiers create nonlinear cost structures. A firm executing exactly at a tier boundary—say, 999,999 shares in a month—pays a much higher rate than one hitting 1,000,001. This has real consequences. Large traders will deliberately batch orders to "just above" a tier boundary to unlock a discount; [market makers](/market-maker-trading/) will time their participation to capitalize on tier transitions; and brokers will advise clients on monthly volume optimization.

Some sophisticated traders have been known to deliberately "spill over" into a higher tier early in a month to lock in lower rates for the remainder of the month, sacrificing a few thousand dollars to gain momentum and avoid the cliff effect at month-end.

## Regional and alternative venues

The major U.S. equity [exchanges](/stock-exchange/)—[NYSE](/new-york-stock-exchange/), [NASDAQ](/nasdaq/), CBOE BZX, Cboe EDGX—all publish their own schedules. They compete aggressively on fees. In recent years, taker fees have compressed dramatically (some venues now charge $0.0001 per share for the highest-tier takers), while maker rebates have become negative, effectively subsidizing [market makers](/market-maker-trading/).

The rationale is straightforward: if you are a [market maker](/market-maker-trading/) choosing between two venues with identical spreads and depth, you will favor the one paying $0.0005 per share to the one paying $0.0003. Venues that want flow engage in a race to the bottom on taker fees and offer the highest maker rebates they can sustain.

Alternative trading systems ([ATS](/alternative-trading-system/), dark pools, and networks) offer their own schedules, often at a discount to public exchanges. An agency broker routing a large order might compare the net cost: public exchange taker fee, minus execution slippage versus expected price improvement and lower [ATS](/alternative-trading-system/) fees. The calculation is complex but highly consequential for institutional trading.

## Options fee schedules

Options [exchanges](/stock-exchange/) publish separate fee schedules, typically more complex than equities. Fees vary not only by maker-taker and volume tier but also by contract type (index vs. single-stock), opening vs. closing, and sometimes by strategy (naked short puts attract higher fees due to [risk](/counterparty-risk/)).

A typical options maker might earn $0.15–$0.30 per contract; a taker might pay $0.40–$0.75. Volume tiers can compress these by 20–30%. For a trader executing 10,000 options contracts per month, the difference between two venues can amount to $1,000–$2,000 in monthly fee impact.

## Rebates and incentive programs

Beyond standard tiers, many venues offer rebates and incentives to attract specific types of flow. A venue might offer an "opening volume incentive"—extra rebates to market makers who post within the first 15 minutes after the open, when spreads are usually tight and depth is needed most. Another might offer "liquidity provider" programs that grant extra discounts to firms maintaining a certain percentage of their flow on that venue.

Some venues also offer "intermarket sweep" credits: if a firm routes an order to a venue knowing it will be partially filled there and partially swept to pick off better prices at other venues, the sweeping venue may grant a credit for having its quote protected, even though the order was partially filled.

These incentive programs create complex cross-venue optimization problems for large traders and brokers.

## The cost cascade into spreads

Exchange fee schedules directly shape [bid-ask spreads](/bid-ask-spread/). If an exchange charges takers $0.005 per share and the nearest competitor charges $0.001, [market makers](/market-maker-trading/) will naturally post wider on the expensive exchange to offset the higher fee burden on their counterparties. A [market maker](/market-maker-trading/) will widen the ask from 50.05 to 50.055 on the expensive exchange, hoping to be less likely to be hit by a taker paying the high fee.

Conversely, venues with low or negative taker fees and high maker rebates attract [market maker](/market-maker-trading/) competition, and spreads compress. This is why retail traders often get better fills on venues with aggressive maker rebates—the rebate subsidizes tight spreads.

## Regulatory scrutiny

The [Securities and Exchange Commission](/securities-and-exchange-commission/) has begun scrutinizing maker-taker fees, asking whether they create undue incentives for [market makers](/market-maker-trading/) to post stale quotes or engage in other behavior that harms retail traders. Some proposals would ban maker rebates or cap their size. Others would require venues to offer uniform pricing (everyone pays or earns the same) to reduce gaming.

The economic debate is live: supporters of maker-taker fees argue they have tightened spreads and improved liquidity; critics contend that the rebates distort incentives and create conflicts of interest in order routing, since brokers may be incentivized to route orders to high-rebate venues rather than best-execution venues.

## Internalization and the spread compression paradox

As rebates have grown more generous and taker fees have compressed, major brokers have increasingly internalized order flow—matching buy and sell orders internally rather than routing to an exchange. An internalized order typically pays neither maker nor taker fees (the [broker](/broker/) captures both sides). This has driven spreads tighter for retail traders but has also siphoned volume away from public venues.

The public exchanges, now receiving less flow, have responded by increasing rebates further or lowering taker fees, setting off another round of compression. Spreads are historically tight, but it is unclear whether the fee schedule subsidies that enabled this are economically sustainable long-term.

## Planning trade execution around fee schedules

Sophisticated traders and brokers explicitly optimize order routing around exchange fee schedules. An algorithmic order execution system will calculate the net cost of executing a given order on each available venue:

**Net Cost = Expected Spread + Taker Fee − Maker Rebate (if applicable) + Market Impact**

The optimal route is the one with the lowest net cost. High-volume participants tier across venues and can negotiate volume discounts with brokers. A $50 billion fund executing $1 billion per month might negotiate a "rebate pass-through" arrangement where the [broker](/broker/) agrees to pass through 100% of the exchange rebates earned on that fund's flow.

---

## See also

<div class="wiki-seealso">

### Closely related

- [Market maker trading](/market-maker-trading/) — firms earning rebates on maker fees
- [Effective spread](/effective-spread/) — the cost to a taker, inclusive of exchange fees
- [Realized spread](/realized-spread/) — market maker revenue after exchange fees and adverse movement
- [Brokerage commission structure](/brokerage-commission-structure/) — broker fees layered on top of exchange fees
- [Alternative trading system](/alternative-trading-system/) — non-exchange venues with their own fee schedules

### Wider context

- [Stock exchange](/stock-exchange/) — the venues publishing fee schedules
- [Stock market](/stock-market/) — the ecosystem of trading and fees
- [Price discovery](/price-discovery/) — how fees affect the efficiency of markets
- [Securities and Exchange Commission](/securities-and-exchange-commission/) — regulator of exchange fee practices
- [Liquidity risk](/liquidity-risk/) — why liquidity provision costs more during stress

</div>
