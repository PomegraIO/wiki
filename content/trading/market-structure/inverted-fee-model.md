---
title: "Inverted Fee Model"
description: "A trading venue that charges market makers for liquidity and rebates aggressive traders for aggressively taking it, the inverse of traditional exchange pricing."
keywords:
  - market structure
  - exchange fees
  - maker rebate
  - taker fee
  - order flow
  - aggressive trading
image: "/svg/trading.svg"
---

*Most stock and options exchanges charge a flat fee per share to traders who take liquidity (the taker), and rebate or subsidise those who supply liquidity (the maker). An **inverted fee model** flips this: the exchange charges makers for the privilege of posting bids and offers, and pays takers a rebate for hitting those orders. This unconventional pricing structure attracts high-frequency traders and institutional flow, concentrating aggressive order flow in one venue and creating a secondary ecosystem of trading venues and fintech intermediaries.*

## The traditional model and why it inverted

For decades, the standard exchange fee structure was straightforward: if you wanted to sell 1,000 shares, you paid a small fee per share (say, $0.001) to execute the trade. If you wanted to post a bid and hope someone else hit it, you usually paid nothing, or even received a rebate (perhaps $0.0005 per share). This rewarded "market makers"—traders who posted standing orders and provided liquidity—and charged "takers" who aggressively consumed it.

The logic was that markets need liquidity, and you had to reward the people providing it. A [market maker](/market-maker-trading/) takes the risk of holding inventory (hoping to sell at a profit) or being hit on both sides of their spread; the rebate was compensation for that service and risk.

By the early 2010s, however, several regulatory and technological shifts inverted this incentive in certain venues. [Regulation SHO](/regulation-sho/) and other post-2008 rules made short selling and inventory risk more expensive for market makers. At the same time, high-frequency trading firms became so fast and capital-efficient that they could supply liquidity profitably even without rebates. And retail brokers, flush with customer deposits, began internalizing order flow—matching customer buy orders against customer sell orders without sending them to an exchange—reducing the volume available to market makers on venues.

Facing declining activity, some upstart exchanges and alternative trading systems realised that they could compete by offering a radically different proposition: charge the market makers (the providers of liquidity), and pay the takers (the consumers of liquidity). This would invert the flow: if you were an aggressive trader or an institutional buyer, why pay traditional exchanges a taker fee when you could go to an inverted venue and *receive* a rebate?

## How the economics work

Suppose a traditional exchange charges a taker $0.001 per share to buy and offers makers a rebate of $0.0005 per share to sell. A high-frequency trader who wants to buy 10,000 shares pays $10 in fees. The venue nets $5 from the maker and $10 from the taker, for $15 total revenue per round.

Now suppose an inverted venue offers to *pay* the aggressive trader $0.001 per share to buy (a rebate) and *charge* the market maker $0.0015 per share to post bids. The aggressive trader receives $10 and the market maker pays $15. The venue nets $15 from the maker, minus the $10 paid to the taker, for $5 net revenue—but the venue has just stolen a customer from the traditional exchange by paying them to trade.

For this to work, the inverted venue must either:

1. Have very high volume, so that small net revenue per trade still totals to a healthy profit, or
2. Have a captive audience of market makers (e.g., an affiliated firm or a proprietary trading desk) that can afford to subsidise the model for strategic reasons.

In practice, inverted venues thrive when they capture order flow from a specific segment—high-frequency traders, retail brokers, or particular institutional desks—and can accumulate enough volume to operate profitably even on razor-thin or negative per-trade margins.

## The role of order flow and market concentration

The appeal of the inverted model is that it *attracts* flow. If you are a large asset manager considering where to route a block of shares, and one venue pays you to trade there while another charges you, you route to the paying venue, all else equal. This creates a virtuous cycle: as aggressive flow concentrates at the inverted venue, market makers follow (because that is where the volume is), which attracts even more aggressive traders.

The result is a kind of micro-ecosystem: the inverted venue captures the most aggressive or time-sensitive orders, while traditional exchanges become the venue of choice for patient, opportunistic traders. A single large order might be split: the aggressive part fills at an inverted venue and receives a rebate; the remaining patient part waits at a traditional venue for a slightly better price.

This fragmentation of order flow is economically efficient in some ways (traders get paid for urgency, patient capital is rewarded for patience) but problematic in others. Regulators worry that fragmentation can reduce [price discovery](/price-discovery/) and liquidity at traditional venues, and that it incentivizes brokers to route orders to whichever venue generates the highest rebates for the broker, rather than the best price for the client.

## Who uses inverted venues and why

The primary users are [high-frequency trading](/algorithmic-trading/) firms. They are fast enough to arbitrage small price differences across venues and to profit from rebates even when they lose money on the spread. A [high-frequency trader](/algorithmic-trading/) might pay a traditional exchange $0.001 per share to buy, then immediately sell to an inverted venue for a $0.001 rebate, pocketing the difference (or profiting from a fractional-cent move in between). Their speed allows them to turn inventory quickly, so they do not need the rebate to compensate for holding risk.

Large asset managers and institutional traders also use inverted venues, especially when they have time-sensitive orders they want to execute immediately. A pension fund that needs to buy a large block of stock quickly will sometimes route to an inverted venue (or an [alternative trading system](/alternative-trading-system/)) to get the benefit of the rebate.

Retail brokers, particularly those that earn revenue from selling order flow to [market makers](/market-maker-trading/), may or may not route to inverted venues. If the venue pays high rebates, the broker will route there and keep a cut for itself. If the rebate is low and the venue is less liquid, the broker might prefer a traditional exchange where its customers' orders are more likely to fill at tight spreads.

## Regulatory scrutiny and structural concerns

Regulators have expressed concern about the inverted-fee model's effect on market structure. The [SEC](/securities-and-exchange-commission/) has argued that paying rebates to takers incentivizes aggressive orders that may not be economically justified, leading to inefficient trading and higher costs for patient investors. Some regulators have proposed caps on rebates or even bans on inverted-fee models in certain asset classes.

Conversely, other economists argue that inverted fees are simply a more transparent way of expressing the true cost of liquidity. Instead of hiding the cost in the bid-ask spread (where market makers compensate themselves implicitly), inverted venues make it explicit: makers pay a fee, takers receive a rebate. If anything, this transparency should promote efficiency, since all parties see the true cost.

The debate is ongoing. The UK's Financial Conduct Authority has been cautious about inverted fees, while US regulators have generally tolerated them, viewing them as a form of competition between trading venues.

## The evolution of inverted models

Over the past decade, the pure inverted model has evolved. Some venues now offer hybrid structures: a low taker fee and no maker rebate, sitting between the traditional and inverted models. Others offer rebates only to certain types of participants (e.g., retail, institutional, or algorithmic traders) or during certain times of day, trying to finely tune the flow they attract.

The rise of retail trading platforms has also complicated the picture. Brokers like Robinhood internalize much retail order flow and route it to [market makers](/market-maker-trading/) or wholesalers in exchange for payment, rather than sending it to an exchange. This is a kind of inverted subsidy: the retail trader pays zero commission to trade, and the broker is paid by the [market maker](/market-maker-trading/) who fills the order. The line between an inverted exchange and an internalization platform has blurred.

## See also

<div class="wiki-seealso">

### Closely related

- [Market maker](/market-maker-trading/) — the liquidity providers charged under inverted models
- [Alternative trading system](/alternative-trading-system/) — the regulatory category inverted venues often occupy
- [Bid-ask spread](/bid-ask-spread/) — the cost inverted rebates aim to reduce
- [Algorithmic trading](/algorithmic-trading/) — the primary beneficiary of inverted fee structures
- [Price discovery](/price-discovery/) — potentially disrupted by fragmented order flow
- Order flow — the asset being bought and sold through fee structures

### Wider context

- [Stock exchange](/stock-exchange/) — the traditional venues competing with inverted models
- [Securities and exchange commission](/securities-and-exchange-commission/) — the regulator scrutinizing these structures
- Market structure — the broader ecosystem of trading venues and pricing
- [High-frequency trading](/algorithmic-trading/) — the dominant user of inverted venues

</div>
