---
title: "IEX (Investors Exchange)"
description: "A stock exchange founded to reduce high-frequency trading advantages through a 350-microsecond speed bump."
keywords:
  - iex exchange
  - high-frequency trading
  - speed bump
  - market structure
  - lit exchange
image: /svg/institutions.svg
---

*The **IEX (Investors Exchange)** is a US stock exchange launched in 2013 as a deliberate challenge to high-frequency trading dominance. Its defining feature is a 350-microsecond "speed bump" — a engineered delay that prevents traders collocated at the exchange from gaining unfair advantage over distant market participants.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">IEX — key facts</div>

<img src="/svg/institutions.svg" alt="An abstract editorial mark for financial institutions." />

<div class="wiki-infobox-caption">A US stock exchange designed to level the playing field between fast and slow traders.</div>

|   |   |
|---|---|
| **Founded** | 2013 |
| **Regulator** | SEC (registered national securities exchange as of 2016) |
| **Primary business** | Equities trading via [lit order book](/lit-order-book/) |
| **Signature feature** | 350-microsecond speed bump |
| **Listing numbers** | ~1,600 US-listed stocks (as of mid-2020s) |
| **Ownership** | Public company (IPO 2019) |

</aside>

## Why IEX was built to slow things down

By the early 2010s, high-frequency trading had become invisible infrastructure in US equity markets. Firms with servers milliseconds closer to exchanges could exploit microscopic price discrepancies before other traders could react. The arbitrage was legal but increasingly criticized as extracting wealth from ordinary investors without improving price discovery.

IEX's founders, led by Brad Katsuyama, witnessed this problem firsthand while executing large institutional trades. They discovered that traders bidding for blocks on one venue would flee if they spotted the same trader's signals minutes later on another — suggesting that aggressive high-frequency algorithms were "front-running" institutional orders by watching activity across fragmented markets. The answer was not to fight latency at its source but to control it deliberately. By imposing a 350-microsecond delay on all order flow — using fibre optic loops under the exchange floor — IEX ensured that speed could never be a source of unfair advantage. A trader 1,000 miles away received the same latency to IEX's matching engine as a collocated firm with a server next door.

## How the speed bump works in practice

The 350-microsecond delay is not punitive; it is structural. When an order arrives at IEX, it enters a queue, travels through approximately 38 miles of fibre optic cable in a deliberate coil, and emerges 350 microseconds later ready to be matched. High-frequency traders collocated at the exchange are delayed by the same amount. No one is privileged. The delay is longer than a human's reaction time but short enough that ordinary institutional traders do not perceive slippage.

This neutrality extends to order priority. IEX enforces strict [price-to-book-ratio](/price-to-book-ratio/) and [time-priority rules](/time-value/): the best bid and offer always win, ties go to the earliest order. No secret order types, no speed-tiered fee structures that favour certain participants. Transparency of the [lit order book](/lit-order-book/) is absolute — all bids and offers are visible, and every trade is reported.

## Why institutional traders adopted IEX

IEX's appeal was powerful to asset managers and pension funds tired of subsidizing latency races. By 2015, a handful of major institutions — including some of the world's largest passive index funds — began routing a significant share of their order flow through IEX. The volume was still small relative to [New York Stock Exchange](/new-york-stock-exchange/) or [NASDAQ](/nasdaq/), but it was growing. IEX offered proof that an exchange could prosper without race-to-the-bottom fee wars or arms races in latency technology.

The SEC approved IEX's registration as a national securities exchange in June 2016, validating the model. Competitors dismissed the speed bump as gimmick; in reality, it was a statement of intent: this exchange existed to serve the investor, not the fastest algorithm.

## The limits of fair structure

Yet IEX's existence alone has not solved high-frequency trading concerns. Most US equity volume still flows through exchanges like [NYSE](/new-york-stock-exchange/) and NASDAQ, where latency advantages persist and dark pools and over-the-counter trades (executed off-exchange) are rife. IEX captured perhaps 2–3% of US equity volume, respectable for an entrant but not transformative.

The speed bump itself, while clever, does not prevent a sophisticated trader from gaming other venues. A firm can still exploit price differences across multiple exchanges by using [algorithmic trading](/algorithmic-trading/) strategies that are only slightly slower than human perception. Nor does IEX's structure solve information asymmetry; a large institutional [block trade](/block-trade/) on IEX is visible to all, which can expose the trader's intentions to market opportunists.

Additionally, IEX's public company status — it went public in 2019 — has exposed tensions between its mission to protect investors and its duty to maximize shareholder returns. Pressure to grow volume and earnings could eventually compromise the principles that made it distinctive.

## IEX's influence on market design thinking

Regardless of IEX's market share, its existence has shifted how the industry thinks about market structure. The speed bump forced serious conversation: Is faster always better? Does an exchange exist to serve traders or investors? Can intentional friction improve price discovery? These questions were not new, but IEX made them concrete.

Some newer venues have adopted similar ideas. [NYSE Arca](/nyse-arca/) and other exchanges have added [periodic auction venues](/periodic-auction-venue/) — discrete matching windows that deliberately batch orders and reduce the advantage of speed. IEX's founding also contributed pressure toward the industry's eventual adoption of [Regulation SHO](/regulation-a/) amendments and other reforms.

## See also

<div class="wiki-seealso">

### Closely related

- [Lit order book](/lit-order-book/) — how IEX's transparent central-limit order book works
- [Algorithmic trading](/algorithmic-trading/) — the high-frequency strategies IEX was designed to constrain
- [NYSE Arca](/nyse-arca/) — a larger electronic equities venue with different design choices
- [Over-the-counter market](/over-the-counter-market/) — where much trading still happens outside lit exchanges
- [Market maker (trading)](/market-maker-trading/) — the role of liquidity provision that IEX restructured
- Latency arbitrage — the problem IEX set out to solve
- [Alternative trading system](/alternative-trading-system/) — regulatory category for non-exchange venues

### Wider context

- [Stock exchange](/stock-exchange/) — general structure and role of equity venues
- [Securities and Exchange Commission](/securities-and-exchange-commission/) — the regulator that approved IEX
- [Systemic risk](/systemic-risk/) — market structure's role in financial stability
- [Bid-ask spread](/bid-ask-spread/) — execution quality that IEX aims to preserve

</div>