---
title: "Dark pool"
description: "A dark pool is a private trading venue where orders are hidden from the public order book. Prices are often based on the lit market, but buyers and sellers match anonymously. Institutions use dark pools to trade large blocks with minimal market impact."
keywords:
  - dark pool
  - private venue
  - hidden liquidity
  - institutional trading
image: "/svg/trading.svg"
---

*A **dark pool** is a private trading venue where orders are not displayed on the public order book. Buyers and sellers meet in the dark, match at mutually agreed prices (often the midpoint of the lit-market spread), and complete their trades away from public view. Dark pools handle about 10–15% of all U.S. stock trading and are most useful for institutions executing large blocks without moving the market.*

<div class="wiki-hatnote">

For public trading, see [lit venue](/lit-venue/). For hidden orders on a lit venue, see [hidden order](/hidden-order/) and [iceberg order](/iceberg-order/).

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Dark pool — key facts</div>

<img src="/svg/trading.svg" alt="A silhouette representing hidden trading activity" />

<div class="wiki-infobox-caption">Dark pools match buyers and sellers away from public view, minimizing price impact.</div>

|   |   |
|---|---|
| **What it is** | Private trading venue; orders not visible publicly |
| **Visibility** | None; orders are hidden until matched |
| **Price** | Often midpoint of lit-market spread; negotiable |
| **Best for** | Large blocks, minimizing market impact, institutions |
| **Downside** | Less price transparency, potential conflicts of interest |
| **Market share** | Roughly 10–15% of U.S. equity trading |

</aside>

## How dark pools work

You want to buy a large block of shares. Instead of placing a visible order on the NYSE (which would spook sellers and move the price against you), you go to a dark pool:

1. **Submit an order.** You tell the dark pool: "I want to buy 100,000 shares at the market (or with a price constraint)."
2. **Matching.** The dark pool's system searches its participants for a seller of 100,000 shares.
3. **Execution.** If a match is found, the trade executes. Price is typically the midpoint of the current lit-market spread, though it can be negotiated.
4. **Privacy.** The trade is not reported to the public order book in real time; it is reported to regulators (SEC) after the fact, with a time delay.

The beauty: no one on the lit market knew a 100,000-share buyer existed. Sellers were not spooked. The trade happened cleanly.

## Dark pool operators

Dark pools are run by:
- **Investment banks** (Goldman Sachs Sigma X, Morgan Stanley MS Pool, JPMorgan).
- **Brokers** (Fidelity, E*TRADE).
- **Exchanges** (NYSE Euronext, NASDAQ have dark venues).
- **Specialized ATS vendors** (Liquidnet, POSIT, etc.).

Each has its own matching rules, pricing logic, and participant base.

## Pricing in dark pools

**Midpoint pricing:** Most dark pools trade at the midpoint of the current lit-market bid-ask. If the NYSE shows bid $50.00, ask $50.04, a dark pool trade happens at $50.02.

**Negotiated pricing:** Some dark pools allow participants to negotiate prices directly, especially for very large blocks.

**Lit-market reference:** All dark pool prices reference the lit market (exchanges) to ensure prices are fair and tied to real public data.

## Advantages of dark pools

**Large blocks without impact.** A 100,000-share buyer can find a seller in a dark pool without the 100,000-share order visibly pushing the price up on the lit market.

**Privacy.** Neither side reveals the full size to the market; trades happen confidentially.

**Fair price.** Trading at the lit-market midpoint (the reference price) is often fair and transparent, even though the trade itself is opaque.

**Access to counterparties.** Institutions connected to a dark pool can find natural counterparties (buyers when you want to sell, sellers when you want to buy) without advertising.

## Disadvantages of dark pools

**Lack of price discovery.** Dark pools trade based on lit-market prices. They do not contribute to the discovery of truly new prices; they free-ride on lit-market transparency.

**Conflicts of interest.** Some dark pool operators (banks, brokers) operate desks that trade the same securities. Regulators worry that operators might favor their own traders' orders over clients', or might price trades unfavorably.

**Execution quality.** Not all dark pools offer best execution. Some might price you worse than the lit market (just at the spread, not better).

**Opacity.** If a dark pool has a problem (bad matching, poor prices), you may not find out until after the fact.

## Regulation of dark pools

Dark pools are regulated under Reg SHO and other SEC rules, but with lighter oversight than exchanges:

- **Real-time transparency:** Not required; dark pools do not have to show quotes or order book in real time.
- **Post-trade reporting:** Dark pools must report trades to FINRA within time limits (usually same day, sometimes with delays for large trades).
- **Best execution:** Brokers routing clients' orders to dark pools must ensure they are getting "best execution" (comparable to lit-market prices).
- **Conflicts disclosure:** Dark pool operators must disclose their ownership and any conflicts of interest.

## Dark pools vs. lit venues

| Feature | Dark pool | Lit venue (exchange) |
|---|---|---|
| **Visibility** | None; orders hidden | Full; order book public |
| **Price discovery** | Piggybacks on lit market | Discovers prices |
| **Market impact** | Minimal for large orders | High for large orders |
| **Price quality** | Dependent on venue; often midpoint | Best bid-ask from all venues |
| **Regulation** | Less stringent | More stringent |
| **Use case** | Large blocks, institutions | Most retail; price-setting trades |

## Size and scope of dark pool trading

In the U.S. equity market, dark pools account for roughly 10–15% of trading by volume. Some observations:

- **Concentrated in large-cap stocks.** Dark pools trade mostly in stocks with tight public spreads (large-cap names).
- **Institutional-dominated.** The vast majority of dark pool traders are institutions (funds, banks); retail investors have limited direct access.
- **Growing but stable.** Dark pool volume has grown over the past decade but has stabilized at around 10–15% of total trading.

## How to access dark pools

**Institutional investors:** Brokers route orders to dark pools automatically (or on request) as part of their execution services.

**Retail investors:** Most brokers offer dark pool routing as an option, though with limitations:
- Some brokers charge extra fees for dark pool routing.
- Dark pools may reject retail orders if size is too small.
- Execution is not guaranteed; some dark pools have minimum order sizes.

Ask your broker whether they offer dark pool routing and under what conditions.

## Controversies and concerns

**Flash Boys:** The 2014 book "Flash Boys" highlighted high-frequency traders exploiting dark pools and lit venues. While HFT-specific concerns have evolved, dark pools remain scrutinized for:
- Potential conflicts of interest (operator-owned traders getting favorable treatment).
- Execution quality (some dark pools offer worse pricing than public venues).
- Information leakage (if a dark pool operator knows large client orders, they might tip off their trading desk).

Regulators have tightened rules, but concerns persist.

## See also

<div class="wiki-seealso">

### Closely related

- [Lit venue](/lit-venue/) — public exchanges where prices are discovered
- [Hidden order](/hidden-order/) — large orders hidden on lit venues
- [Iceberg order](/iceberg-order/) — visible tip, hidden size on lit venue
- ATS — alternative trading systems, a category including dark pools

### Execution and market structure

- [Best execution](/best-execution/) — brokers must ensure quality even in dark pools
- [NBBO](/nbbo/) — national best bid-offer; dark pools reference this
- Market impact — dark pools minimize this for large orders
- Block trading — common use case for dark pools

### Regulatory

- [Regulation SHO](/regulation-sho/) — governing short selling and dark pools
- SEC — regulates dark pools
- [FINRA](/finra/) — enforces rules for member brokers
- Trade reporting — dark pools must report to regulators

### Advanced topics

- [High-frequency trading](/high-frequency-trading/) — uses dark pools strategically
- [Algorithmic trading](/algorithmic-trading/) — breaks large orders across venues
- Information leakage — risk when using dark pools

</div>
