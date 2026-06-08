---
title: "Odd-Lot Trading Mechanics"
description: "How orders for fewer than 100 shares are executed separately from round lots and their treatment in NBBO and market data."
keywords:
  - odd lot
  - round lot
  - 100 shares
  - NBBO
  - execution priority
  - fractional shares
image: "/svg/markets.svg"
---

*An **odd lot** is an order for fewer than 100 shares of a stock; a **round lot** is exactly 100 shares or a multiple thereof. Most US equity exchanges historically treated odd-lot orders separately from round-lot orders, executing them at different prices or times, and excluded them from the official [bid-ask spread](/bid-ask-spread/) and [market maker](/market-maker-trading/) quotations. This distinction has blurred in recent years but remains embedded in market microstructure and regulation.*

<div class="wiki-hatnote">

For fractional-share purchasing by retail investors, see [Fractional-Share Trading](/fractional-share-trading-mechanics/). This article covers how exchanges handle odd-lot orders within the standard quotation and execution framework.

</div>

## The historical round-lot convention

For most of equity market history, 100 shares was the standard trading unit. Brokers, market makers, and exchanges built all their systems around round lots. When a dealer quoted "100 shares at $50 bid, $50.05 offer," they meant 100-share parcels. Odd-lot orders—say, 37 shares—fell outside this quotation and were routed to a separate odd-lot dealer or executed at a wider spread or delayed execution.

This convention arose from practical constraints: in the days of open outcry and paper certificates, bundling trades into neat round lots made back-office settlement far simpler. By the time electronic trading arrived, the round-lot rule had become codified in [Securities and Exchange Commission (SEC)](/securities-and-exchange-commission/) regulations and exchange rulebooks.

The core consequence: odd-lot orders were **not** part of the national best bid or offer ([NBBO](/bid-ask-spread/)). If Nasdaq quoted 100 shares at $50 bid and the New York Stock Exchange quoted odd lots at $49.95, the NBBO remained $50 (the best round-lot bid), and odd-lot traders at $49.95 were not protected by trade-through rules that normally prevent execution at inferior prices.

## Execution mechanics and price determination

When an odd-lot buy order arrives, an exchange faces a few choices. Under traditional rules, it may:

1. **Execute against existing odd-lot inventory** at the current best odd-lot ask.
2. **Fill at the next round-lot print**, often at a slight markdown or markup relative to the round-lot price.
3. **Queue the order** for batch execution at a future round-lot price.
4. **Route to an odd-lot specialist** (increasingly rare) who quotes tighter spreads but takes on inventory risk.

In modern markets, most odd-lot orders on major exchanges like [Nasdaq](/nasdaq/) and NYSE are executed within seconds, often at the previous round-lot trade price or slightly better. However, the exact mechanism varies by exchange and order type.

Critically, odd-lot orders **do not** update the official NBBO—the quote that appears on every broker platform and that [market makers](/market-maker-trading/) must respect. This creates a two-tier execution environment: round-lot traders see tighter spreads and better price priority; odd-lot traders accept wider spreads and may be price-improvemented (executed at a better price) only if the exchange chooses to do so.

## Why odd lots matter today

For most institutional traders, odd-lot mechanics are irrelevant; they trade round lots. But the rise of retail investing and fractional-share ETFs has changed the picture. Millions of retail investors now hold odd-lot positions (35 shares, 72 shares) from regular investments or [dividend reinvestment](/dividend-distribution/). When they sell, their orders go into odd-lot channels.

More significantly, **index rebalancing and ETF creation/redemption** routinely generate odd lots. An ETF that tracks 500 stocks with an Assets Under Management (AUM) of, say, $5 billion, must hold each constituent stock; if the portfolio is equally weighted, each stock is worth $10 million. Dividing by stock price often yields a fractional number of shares. These odd-lot holdings must be managed at the edges of the portfolio.

Some [market makers](/market-maker-trading/) and [algorithmic trading](/algorithmic-trading/) firms now specialize in odd-lot aggregation, buying tiny positions from retail sellers and bundling them into round lots for institutional resale—profiting from the bid-ask spread differential.

## NBBO and trade-through protection

The key regulatory point: because odd-lot orders are not part of the NBBO, a broker is **not obligated to offer a customer a better price than an NBBO quote, even if an odd-lot market quote would be superior**. 

For example, if the round-lot NBBO is 50.00 bid / 50.05 offer, and an odd-lot bid of 50.10 exists somewhere, a broker selling an odd-lot order is not required to route to the 50.10 bid. The customer does not benefit from odd-lot price improvement unless the broker voluntarily chooses to hunt for it.

This creates what critics call a "tiering" problem: retail odd-lot traders are excluded from the best-execution protections that round-lot traders enjoy.

## Modern regulatory shifts

The SEC and exchanges have been gradually chipping away at odd-lot isolation. Some exchanges now include odd-lot orders in the NBBO under certain conditions, and some brokers (especially discount and zero-commission brokers) now aggregate odd-lot orders and execute them at round-lot prices or better. A trader selling 75 shares might now see an offer to round up to 100 and receive the round-lot price, profiting from the spread elimination.

However, the old round-lot/odd-lot divide remains embedded in market data feeds, exchange rulebooks, and the quoting practices of some [market makers](/market-maker-trading/). A trader working with a sophisticated broker may see odd lots integrated seamlessly; a trader at a smaller or older platform might encounter wide odd-lot spreads or delayed execution.

## See also

<div class="wiki-seealso">

### Closely related

- [Bid-Ask Spread](/bid-ask-spread/) — How odd-lot orders affect quoted spreads
- [Market-Maker Trading](/market-maker-trading/) — How dealers handle odd-lot flow
- [Auction Imbalance Mechanism](/auction-imbalance-mechanism/) — How odd lots are treated in opening and closing auctions
- [Spoofing and Layering Mechanics](/spoofing-and-layering-mechanics/) — Manipulation of odd-lot quotes
- [Limit Order](/limit-order/) — Limit orders for odd-lot parcels
- Trade-Through — Odd-lot orders and best-execution rules

### Wider context

- [Stock Exchange](/stock-exchange/) — Exchange rules governing odd-lot handling
- [Nasdaq](/nasdaq/) — Primary market for odd-lot trading
- [New York Stock Exchange](/new-york-stock-exchange/) — Listings and odd-lot mechanics
- [Securities and Exchange Commission](/securities-and-exchange-commission/) — Regulator of odd-lot rules

</div>
