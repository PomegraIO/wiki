---
title: "Dark Pool"
description: "A dark pool is a private trading venue where investors can trade securities without displaying their orders to the public. Dark pools trade approximately 10-15% of US stock volume and are popular with institutions executing large orders, but they are controversial due to opacity and potential conflicts of interest."
keywords:
  - dark pool
  - private venue
  - hidden orders
  - institutional trading
  - off-exchange
  - transparency
image: "/svg/markets.svg"
---

*A **dark pool** is a private, non-transparent trading venue where institutions can trade securities without publicly displaying orders. Dark pools do not publish pre-trade quotes or post-trade data immediately; trades are reported with a delay or not at all until regulatory filing. Dark pools account for approximately 10–15% of US stock trading volume and are preferred by institutions executing large orders because they avoid the market impact of publicly announcing large buy or sell intentions.*

<div class="wiki-hatnote">

This entry is about private trading venues. For transparent venues, see [lit venue](/lit-venue-detail); for regulatory framework, see [alternative trading system](/alternative-trading-system).

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Dark Pool — key facts</div>

<img src="/svg/markets.svg" alt="A trading desk with dimmed lighting, symbolizing opacity of dark pools" />

<div class="wiki-infobox-caption">Dark pools trade orders privately, away from public view.</div>

|   |   |
|---|---|
| **Order visibility** | None; trades reported with delay or opacity |
| **Typical users** | Institutional investors, hedge funds, asset managers |
| **Market share** | ~10–15% of US equity volume |
| **Advantages** | Low market impact, privacy for large orders |
| **Disadvantages** | No price transparency, potential adverse selection |
| **Regulation** | SEC Rule 10b-2; [Reg NMS](/reg-nms-detail) |
| **Common operators** | Goldman Sachs, JPMorgan, Citadel, Instinet |

</aside>

## How dark pools work

A dark pool operator (typically a bank or broker-dealer) provides a private trading platform. Institutional clients submit orders specifying the stock, quantity, and price, but these orders are not visible to the broader market.

The operator's matching algorithm pairs buy and sell orders from different clients at midpoint prices (or negotiated prices) and executes the trades privately. The trades are reported to the [consolidated tape](/consolidated-tape) after execution (typically minutes to hours later), but the pre-trade demand and supply are never revealed.

**Example:** A pension fund wants to buy 10 million shares of Microsoft. Posting this order on the [NYSE](/stock-exchange) would announce its intention to the entire market, causing the price to rise as other traders front-run the large purchase. Instead, the pension fund's broker posts the order to a dark pool. A hedge fund with a sale order for 8 million shares matches with the pension fund's buy order. Both orders partially fill at a negotiated price. After the trade, it is reported to the tape, but the pension fund's intent to buy 2 million more shares remains hidden.

## Types of dark pools

**Broker dark pools.** Operated by investment banks and broker-dealers (Goldman Sachs, JPMorgan, Bank of America). These are the largest. They internalize client orders: they match buy and sell orders from different clients without routing to external venues.

**Institutional dark pools.** Operated by or for specific institutional investors (e.g., a large pension fund might operate its own internal dark pool).

**Independent dark pools.** Operated by independent companies not affiliated with major banks (e.g., Instinet, Level ATS, Posit).

## Advantages and disadvantages

**Advantages:**

- **Market impact minimization.** Large orders do not move prices against the buyer/seller. The pension fund buying 10M shares avoids the price spike.
- **Privacy.** Competitors and market observers don't learn of the institution's trading interest until after execution.
- **Cost savings.** Dark pools often offer lower fees than exchanges.
- **Execution certainty.** Large orders are more likely to fill.

**Disadvantages:**

- **No price transparency.** Buyers don't know if they're getting the best price available elsewhere. They're trading against peers, not the broader market.
- **Adverse selection.** If a counterparty is willing to trade at the dark pool price, why? Maybe they have better information or a desperation to exit.
- **Potential market impact anyway.** A pension fund selling a large position might split orders across multiple dark pools to hide intent, delaying the execution and extending the adverse market impact.
- **Regulatory concerns.** Dark pools lack the oversight of exchanges and are subject to less scrutiny.

## Pricing in dark pools

Dark pools typically execute at the midpoint of the [NBBO](/sip-securities-information-processor) (national best bid-ask):

- NYSE bid: $100.00, ask: $100.05
- NBBO midpoint: $100.025
- Dark pool trade: $100.025 (or negotiated price within the spread)

This "midpoint pricing" is designed to be fair; neither party gets the spread.

However, some dark pools allow "discretionary pricing" or "reference pricing" that trades closer to the bid or ask, benefiting the dark pool operator or one party.

## Regulatory framework

Dark pools are [alternative trading systems](/alternative-trading-system) regulated by the SEC under Rule 10b-2. Operators must:

- Register with the SEC.
- Adopt and enforce rules and procedures.
- Provide fair access to market participants.
- Report trades to the [consolidated tape](/consolidated-tape).
- File reports on order routing and execution quality.

However, dark pools are not required to publish pre-trade or real-time post-trade data, making them less transparent than [lit venues](/lit-venue-detail).

## Criticisms and controversies

**Information asymmetry.** Without pre-trade visibility, a dark pool operator or sophisticated participant might have information about large orders and trade ahead of them.

**Order filling behavior.** Some critics argue dark pools deliberately do not fill orders to induce traders to accept worse execution at the opening on an exchange.

**Market fragmentation.** The rise of dark pools has fragmented the market; it is harder to find the best prices when so much volume is hidden.

**Flash trading.** Some dark pools offered "flash orders" that showed orders to selected participants before execution, creating unfair advantages. The SEC largely prohibited flash orders.

## Size and prevalence

Dark pool trading has grown significantly since the early 2000s. By 2020, dark pools accounted for 10–15% of US equity volume, with the largest pools trading 1–3% of daily volume individually. The largest dark pools are affiliated with major banks.

In Europe, [MiFID II](/mifid-ii-trading) restrictions have reduced dark pool trading to less than 5% of volume, requiring more transparency.

## Market quality debate

Academic research is mixed on whether dark pools improve or worsen market quality:

- **Pro:** Dark pools reduce market impact for large orders and benefit institutions.
- **Con:** Dark pools reduce price transparency, potentially worsening market quality and creating information asymmetries.

Regulators continue to debate the appropriate balance.

## See also

<div class="wiki-seealso">

### Closely related

- [Lit venue](/lit-venue-detail) — transparent alternative to dark pools
- [Alternative trading system](/alternative-trading-system) — regulatory category
- [Consolidated tape](/consolidated-tape) — reports dark pool trades
- [Reg NMS](/reg-nms-detail) — regulatory framework
- [Stock exchange](/stock-exchange) — public alternative

### Wider context

- [Secondary market](/secondary-market) — component of
- [Liquidity](/secondary-market) — dark pools affect this
- [Price discovery](/stock-market) — hampered by dark pools
- [Transparency](/stock-market) — dark pools reduce this
- [Market fragmentation](/stock-market) — caused by dark pools

</div>
