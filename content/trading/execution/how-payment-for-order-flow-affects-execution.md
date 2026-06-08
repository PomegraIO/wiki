---
title: "How Payment for Order Flow Affects Execution Quality"
description: "Payment for order flow mechanics and the debate over whether retail traders receive worse execution fills as a result."
keywords:
  - payment for order flow
  - pfof execution quality
  - retail execution fills
  - order flow sales
  - market maker incentives
image: /svg/trading.svg
---

*Retail brokers in the U.S. generate revenue partly by selling customer **payment for order flow** (PFOF)—that is, directing retail orders to [market maker](/market-maker-trading/)s and off-exchange trading venues that pay for the privilege. The mechanism raises a central question: does PFOF benefit retail traders through lower commissions, or does it harm them through worse [bid-ask-spread](/bid-ask-spread/) pricing and slower execution?*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Payment for Order Flow — key facts</div>

<img src="/svg/trading.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">PFOF is a structural feature of U.S. equity markets that trades retail execution quality for zero-commission trading.</div>

|   |   |
|---|---|
| **Who pays** | Market makers and off-exchange venues (wholesalers) |
| **Who receives** | Retail brokers (split with market makers' profit) |
| **Mechanism** | Orders routed to venues that pay per-share to access order flow |
| **Execution impact** | Contested; empirical evidence suggests mixed effects |
| **Regulatory status** | Legal under SEC rules; subject to ongoing oversight |

</aside>

## The PFOF mechanism

When a retail trader places an order to buy or sell stock, the broker does not automatically send it to a [stock-exchange](/stock-exchange/) like the [New York Stock Exchange](/new-york-stock-exchange/) or [Nasdaq](/nasdaq/). Instead, it can be routed to a **wholesaler**—a [market maker](/market-maker-trading/) such as Citadel Securities, Virtu Financial, or Two Sigma—that operates an [alternative-trading-system](/alternative-trading-system/) (ATS) or [over-the-counter-market](/over-the-counter-market/) venue. The wholesaler pays the broker a few cents per share (often $0.001 to $0.01) for the right to execute that order. The broker pockets the payment; the customer does not see it.

The economic rationale is mutually beneficial in theory. The broker gets paid per order without charging the customer a commission, enabling the advertised "zero-commission" model. The market maker profits by taking the other side of the retail order and managing the resulting position risk. If the market maker can aggregate retail orders, source liquidity elsewhere, and capture a small profit on the [bid-ask-spread](/bid-ask-spread/), the arrangement is profitable. The mechanism has also made it economically feasible for brokers to operate at scale without trading commissions.

## The execution quality debate

The critical tension is this: does a market maker that *pays* for order flow execute those orders at worse prices than it would execute its own institutional flow? The empirical evidence is genuinely mixed, and regulators and researchers have been investigating for years.

**Arguments that PFOF harms retail execution:**

Market makers have an incentive to widen [bid-ask-spread](/bid-ask-spread/)s on retail orders to capture additional profit, since they have already paid for the order flow. A retail buyer might receive a filled price 1 cent worse than the national best [bid-ask-spread](/bid-ask-spread/); the wholesaler keeps that 1 cent (or a portion of it) as profit. Over millions of shares, this compounds into billions of dollars of value transfer from retail traders to wholesalers annually.

Additionally, PFOF creates a structural conflict of interest: the broker has no incentive to route orders to venues that offer the best execution if another venue pays more. A broker's choice of wholesaler is influenced by PFOF payment size, not by whether that wholesaler's fills are demonstrably superior.

**Arguments that PFOF does not materially harm retail:**

Empirical studies, including work by academic researchers and market structure analysts, have found that spreads on heavily-PFOF-routed stocks are often *tighter* than spreads on exchange-listed securities, in part because wholesalers offer consistent liquidity. Market makers compete for order flow; if one wholesaler is known to provide poor fills, brokers can switch. Additionally, [price improvement](/price-discovery/)—fills better than the national best bid-ask—does occur and is reported to retail customers, though the extent is debated.

The SEC, which has examined PFOF practices repeatedly, has concluded that while conflicts of interest exist, the net effect is not clearly negative for all retail traders. Some benefit from tight spreads and fast execution; others are harmed by adverse selection on volatile orders.

## Regulatory and competitive context

The SEC classifies wholesalers as [broker](/broker/)s and imposes regulatory requirements on execution quality and disclosure. Brokers must route orders to venues that provide the best execution reasonably available under the circumstances. In practice, this is interpreted through a general obligation rather than a per-order audit.

A key rule is the **SEC's "best execution" standard**. Brokers are obligated to demonstrate that their PFOF arrangements do not systematically result in worse execution for their customers. The SEC, however, has not mandated that brokers maximize execution quality at the expense of PFOF revenue, creating the persistent tension.

In recent years, regulatory bodies including the SEC and state attorneys general have increased scrutiny. Some commissioners have called for banning PFOF outright, while others argue that competition among wholesalers and transparency disclosures are sufficient safeguards. The debate remains unresolved.

## Measuring execution impact empirically

Retail traders can partially assess their own execution quality using several metrics:

- **Fill price vs. national best**: Compare the price paid (or received) to the [bid-ask-spread](/bid-ask-spread/) at the time of submission. Better-than-spread fills (price improvement) reduce the cost of trading.
- **Spread width**: Tighter spreads mean lower implicit costs. For high-volume stocks, spreads are negligible; for lower-volume names, spreads are wider regardless of PFOF.
- **Execution speed**: Does the order fill immediately, or are there delays? Market makers that pay for flow are incentivized to fill quickly (to reduce their inventory risk), so speed is often good.
- **Adverse selection**: Do limit orders tend to get filled on adverse price moves (the order books up just before the fill, then moves against you)? This is harder to measure but can signal poor order flow quality.

Most brokers now disclose monthly execution statistics, broken down by order type and venue. Traders comparing brokers can examine these reports, though the data is dense and often obscures the net PFOF effect.

## The spread between retail and institutional execution

Institutional traders, who route orders through exchanges and [alternative-trading-system](/alternative-trading-system/) venues, typically receive price-discovery-based execution with minimal PFOF involvement. An institution trading 10,000 shares of a highly-liquid stock may pay a few basis points in total cost (commissions + spread). A retail trader trading 100 shares of the same stock, routed through a PFOF wholesaler, might pay 5–20 basis points in effective cost (implicit spread + wholesaler margin), even with zero commission listed.

The dollar amounts are small per trade ($5–$20 on a $5,000 order), but the pattern is consistent and economically meaningful over a lifetime of trading.

## Alternative execution models

Some brokers have opted to avoid PFOF, charging explicit commissions or monthly subscription fees instead. These include Interactive Brokers and some equity platforms. The trade-off is transparency: the customer pays a clear, auditable cost and receives orders routed to exchanges, where price discovery is competitive. Whether this yields better net execution is nuanced—exchange fees and other factors can offset the PFOF advantage.

Retail traders can also route orders directly to exchanges or alternative venues if their broker supports it, bypassing wholesalers altogether. This typically requires more sophisticated tooling and higher account minimums.

## See also

<div class="wiki-seealso">

### Closely related

- [Bid-ask spread](/bid-ask-spread/) — The core cost measure affected by PFOF routing
- [Market maker trading](/market-maker-trading/) — How wholesalers profit from PFOF orders
- [Price discovery](/price-discovery/) — Competition and pricing mechanisms affected by venue choice
- [Alternative trading system](/alternative-trading-system/) — Off-exchange venues that purchase PFOF
- [Broker](/broker/) — Entities receiving PFOF payments

### Wider context

- [Over-the-counter market](/over-the-counter-market/) — Wholesalers operate in OTC structures
- [Execution risk](/execution-risk/) — Broader notion of slippage and fill quality
- [Securities and Exchange Commission](/securities-and-exchange-commission/) — Regulator of PFOF practices
- [Market order](/market-order/) — Retail order type most vulnerable to PFOF adverse selection

</div>
