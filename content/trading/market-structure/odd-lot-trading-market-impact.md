---
title: "Odd-Lot Trading and Its Market Impact"
description: "How odd-lot orders (under 100 shares) are handled differently from round lots, and what the SEC's 2023 rule change means for price discovery."
keywords:
  - odd lot orders market structure
  - round lot trading
  - sec odd lot rule 2023
  - nbbo national best bid offer
  - price discovery
image: /svg/trading.svg
---

*An **odd lot** is a stock order for fewer than 100 shares, historically excluded from the National Best Bid Offer and priced less competitively than round lots; the SEC's 2023 rule change brought odd lots into the [market maker](/market-maker-trading/) pricing framework, improving transparency but complicating execution.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Odd-Lot Orders — key facts</div>

<img src="/svg/trading.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Sub-100-share orders now contribute to price discovery, not just fill at best-effort prices.</div>

|   |   |
|---|---|
| **Definition** | Orders for 1–99 shares (vs. round lot: 100+) |
| **Pre-2023 treatment** | Excluded from NBBO; quoted separately at wider spreads |
| **Current rule** | Odd lots contribute to best bid and ask; new tier structure |
| **Execution impact** | Retail orders may face segmented pricing based on lot type |
| **Cost to investors** | Historically higher spreads; now improving with transparency |
| **Market data** | Separate odd-lot reporting for tracking and analysis |

</aside>

## Why odd lots were historically separate

Until the SEC's 2023 overhaul, the U.S. stock market treated odd lots as a second-class order type. The [NBBO](/bid-ask-spread/)—the best [bid-ask spread](/bid-ask-spread/) visible to all traders—only included round lots (100 shares or multiples thereof). If an investor wanted to buy 50 shares, they couldn't see or access the best displayed price for a 100-share order; instead, brokers would fill them at separate, typically wider, odd-lot prices.

The historical rationale was operational. When markets were entirely manual, a floor broker managing 100-share orders couldn't economically track every odd lot hanging around. Consolidating odd lots into blocks reduced friction. Electronic markets made this irrelevant—a computer can track a single share—but the rule persisted because market participants had built systems and practices around it. Brokers kept odd-lot orders in separate books; [market makers](/market-maker-trading/) weren't required to quote them; price discovery remained bifurcated.

The result was a persistent micro-disadvantage for retail investors: odd-lot orders suffered wider spreads and slower fills, even for highly liquid stocks. A retail investor buying 75 shares of an actively traded company might pay a measurably worse price than someone buying 100.

## How the SEC's 2023 rule change reshaped odd-lot handling

In May 2023, the SEC adopted Regulation SHO amendments (Release 34-97109) requiring exchanges and brokers to include odd-lot orders in price discovery. The rule established a new tier of best bids and offers: odd-lot bids and offers that meet the same price as the displayed NBBO now appear in a new "OddLot Best Bid/Offer" field, aggregating all odd-lot interest at each price level.

The practical effect: odd-lot orders now contribute to [price discovery](/price-discovery/). If a market maker quotes $100 per share for a round lot but an odd lot seller offers $99.95, the lower price is visible—not hidden. This should theoretically compress spreads and reduce adverse selection against retail traders.

But the rule also created segmentation. Execution algorithms can now distinguish between round-lot and odd-lot fills, allowing brokers to route orders separately. A large round-lot order at the best displayed price takes priority; odd lots fill in a second tier. This is not necessarily harmful—it reflects genuine operational differences—but it does mean execution quality can diverge.

## Price discovery and market structure implications

The 2023 rule was designed to address a specific market microstructure problem: the exclusion of small orders from the reference price. When odd lots were invisible, [algorithmic trading](/algorithmic-trading/) systems and institutional [market makers](/market-maker-trading/) made decisions without seeing the full picture of supply and demand. A million-share institutional order would move the market, but a hundred small retail orders wouldn't show up in the price-setting mechanism until they were aggregated into round lots.

Including odd lots in the NBBO improved transparency. Now, if there's genuine demand for a stock at $50.01 from retail traders buying 1-99 shares, that's visible to algorithms and [market makers](/market-maker-trading/) and feeds into price discovery. In efficient markets, this should reduce the "bid-ask bounce"—the artificial spread created by uncertain demand.

However, improved visibility also increased [operational risk](/operational-risk/) for market makers. They now have to manage odd-lot inventory more carefully. Some are responding by widening odd-lot spreads to compensate for handling costs. The net benefit to retail depends on the specific stock, the broker's execution practices, and the liquidity environment.

## Execution quality and retail investor outcomes

For a retail investor, the SEC rule change is mostly positive but not uniformly. On highly liquid stocks (Apple, Tesla, S&P 500 components), the benefits are clear: spreads are tighter, fills are faster, and odd-lot prices track the round-lot NBBO more closely. The marginal cost of buying 50 versus 100 shares has shrunk.

On lower-liquidity stocks, the picture is murkier. A [market maker](/market-maker-trading/) might display a tight round-lot spread but widen the odd-lot tier to protect against adverse selection. An odd-lot buyer of a small-cap stock could still face a 5–10 cent spread while a round-lot buyer sees 1 cent.

Broker execution quality is critical. Some brokers proactively route odd-lot orders to exchanges that offer the best odd-lot prices; others still process them in-house or through less competitive venues. The rule doesn't mandate optimal routing for odd lots; it only requires that they're visible and included in price calculation.

## Market data and analytics considerations

The rule also changed how odd-lot data is reported. Exchanges now publish separate best-bid and best-offer data for odd lots, alongside standard NBBO. Traders analyzing market structure can see the depth of odd-lot interest; academics can study whether the rule actually improved retail execution (early evidence is mixed but improving).

For [market timing](/market-timing/) and [support-and-resistance](/support-and-resistance/) analysis, odd-lot orders can signal retail interest at specific price levels. If odd-lot bids cluster at $50.00 while round-lot bids are at $49.95, that might indicate retail support. Professional traders use this as a contrarian signal (odd lots often trade against the trend) or confirmation.

## When odd lots matter most

Odd-lot disadvantage is most acute for small account holders—typically those with fewer than six figures in investable assets. A $20,000 account might make 50-share purchases. The spread difference across hundreds of trades annually adds up.

Conversely, odd lots matter least in markets with extremely high liquidity. On the SPY ETF or major tech stocks, round-lot and odd-lot spreads have converged to a single penny. The rule's impact there is negligible.

Sector-specific trends also matter. Expensive stocks (Berkshire Hathaway, high-priced biotech) naturally attract more odd-lot trading; the rule's benefit is correspondingly larger.

## See also

<div class="wiki-seealso">

### Closely related

- [Bid-Ask Spread](/bid-ask-spread/) — how the spread is set and how order type affects cost
- [Market Maker Trading](/market-maker-trading/) — role of market makers in quote setting and liquidity provision
- [Price Discovery](/price-discovery/) — how market prices aggregate information
- [Limit Order](/limit-order/) — how orders are queued and executed relative to each other
- [National Best Bid Offer](/nbbo/) — the regulatory framework for displayed quotes

### Wider context

- Market Structure — exchanges, alternative trading systems, and order routing
- [Stock Market](/stock-market/) — overview of U.S. equity trading
- [Securities and Exchange Commission](/securities-and-exchange-commission/) — regulator and rule-setting authority
- [Algorithmic Trading](/algorithmic-trading/) — automated order routing and execution strategies

</div>
