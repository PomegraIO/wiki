---
title: "Securities Settlement Bridges: Euroclear and Clearstream"
description: "How Euroclear and Clearstream bilateral settlement bridges enable cross-system delivery of Eurobonds and international securities without asset movement."
keywords:
  - securities settlement bridge
  - euroclear clearstream
  - icsd bridge
  - eurobond settlement
  - cross-system settlement
image: /svg/trading.svg
---

*A **securities settlement bridge** allows two central securities depositories to deliver the same bond or share across their systems during settlement without moving the underlying asset. The Euroclear–Clearstream bridge, linking the world's two largest international central securities depositories (ICSDs), is the industry standard for Eurobond and cross-border securities trades.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Securities Settlement Bridge — key facts</div>

<img src="/svg/trading.svg" alt="An abstract editorial mark for trading infrastructure." />

<div class="wiki-infobox-caption">Two ICSDs settle the same trade on both sides without moving physical assets between them.</div>

|   |   |
|---|---|
| **What it solves** | Reduces settlement friction between the two largest Eurobond clearers |
| **Key participants** | Euroclear, Clearstream (both ICSDs) |
| **Asset types** | Eurobonds, international equities, debt securities |
| **Settlement method** | Bilateral instruction matching; assets stay in originating ICSD |
| **Risk reduced** | Counterparty risk, delivery failure, settlement delay |

</aside>

## How the bridge works

Before the settlement bridge, a trader instructing Euroclear to deliver Eurobonds to a Clearstream participant faced a problem: the bonds lived in Euroclear's vault. The Clearstream participant would receive a claim on Euroclear, not the bonds themselves, unless Euroclear physically (or digitally) moved the securities between systems. That added friction, cost, and operational complexity.

The bridge flips this. When a Euroclear holder sells to a Clearstream participant, settlement happens *simultaneously* on both sides. The seller's Euroclear account is debited, the buyer's Clearstream account is credited, and the bond stays put in Euroclear's ledger. A corresponding reciprocal instruction flows to Clearstream's settlement engine. At the moment of settlement, both parties see the transaction complete: the seller has given up the bond (visible as a debit in Euroclear), and the buyer has received it (visible as a credit in Clearstream). The bridge participants, not the individual traders, hold the counterparty risk—and that risk is mutually managed via collateral and novation agreements.

The critical piece is the instruction matching. Both ICSDs have standing technical agreements that tell their settlement systems, "When you see instruction X from participant A in system A matching instruction Y from participant B in system B, settle both sides simultaneously." This bilateral coordination happens tens of thousands of times each day across Eurobond markets.

## Why Euroclear and Clearstream are bridged

These two institutions control roughly 90 percent of all Eurobond settlement. A trader in London, Tokyo, or New York will typically use one ICSD account as their primary depot. But their counterparties may use the other. Without a bridge, every cross-ICSD trade would require asset movement, which is slow and expensive.

The bridge also reflects market history. Euroclear and Clearstream (originally Cedel) have been the dominant continental-European ICSDs for decades. When the Eurobond market exploded in the 1980s and 1990s, both systems became entrenched. Forcing participants to choose one ICSD exclusively would have fragmented the market and raised funding costs for issuers. The bridge is a market compromise: live in your preferred system but trade seamlessly with the other.

## Settlement mechanics under the bridge

Here's a concrete flow:

1. **Trade execution**: A Euroclear member sells €10 million of a German Bund (a Eurobond) to a Clearstream member. Both sides confirm the trade.
2. **Settlement instruction**: The seller sends Euroclear an instruction: "Deliver this bond; debit my account; expect payment."
3. **Bridge instruction**: Euroclear's settlement system automatically generates a bridge instruction to Clearstream: "Clearstream participant B should receive the same bond as a credit; this is a delivery against payment."
4. **Bilateral match**: Clearstream's system receives the seller's payment instruction and matches it against the instruction generated from Euroclear's side.
5. **Simultaneous settlement**: Both legs settle at the same moment: seller's Euroclear account is debited, buyer's Clearstream account is credited. The bond remains in Euroclear's vault; Clearstream holds a claim or entitlement to it.
6. **Finality**: Both parties see funds/securities finality in their respective systems.

This is faster and safer than physical or inter-system asset transfer because neither ICSD has to verify ownership across the boundary; the technical agreement is pre-established and covers tens of millions of possible trades.

## Liquidity benefits

The bridge creates a single deep liquidity pool for Eurobonds across both systems. A trader using Clearstream who wants to buy a bond can find sellers in Euroclear; the bridge ensures delivery without extra steps. This reduces [bid-ask-spread](/bid-ask-spread/) and trading costs. Conversely, it also means that the two systems are so tightly coupled that any operational failure in one cascades into the other—a reason why both ICSDs maintain redundant settlement engines and extensive backup infrastructure.

## Risk management on the bridge

Both ICSDs charge fees (typically basis points per settlement) to manage the bridge. They also maintain bilateral collateral agreements to cover potential losses if one ICSD fails to deliver. In practice, the risk is very low because both institutions are heavily regulated by the European Central Bank and are lenders of last resort—meaning their member central banks back them in a crisis. Still, the bridge participants (large banks and buy-side firms) hold legal claims and counterparty limits against both ICSDs.

## Limitations and alternatives

The bridge works only for assets that both ICSDs hold. New issuances, thematic securities, or niche bonds may settle in only one depot. In those cases, traders must either move accounts or accept settlement via [over-the-counter-market](/over-the-counter-market/) settlement agents. Blockchain-based settlement networks and new entrants promise to eventually bypass the bridge entirely by holding all securities in a common ledger, but as of now, the Euroclear–Clearstream bridge remains the market standard for international bond trading.

## See also

<div class="wiki-seealso">

### Closely related

- [Central bank](/central-bank/) — Euroclear and Clearstream are ECB-regulated utilities
- [Primary market](/primary-market/) — Where Eurobonds are first issued into ICSDs
- [Over-the-counter-market](/over-the-counter-market/) — Direct settlement alternative to bridge-based settlement
- [Counterparty risk](/counterparty-risk/) — Why bilateral ICSD risk management matters
- [Collateral](/capital-adequacy/) — Bridge participants post collateral to manage ICSD exposure
- [Custodian](/custodian/) — ICSDs act as custodians for global assets

### Wider context

- [Bond](/bond/) — Eurobonds are the primary asset type on the bridge
- [Mortgage-backed-security](/mortgage-backed-security/) — Another major asset settled via bridge systems
- [Securities-and-exchange-commission](/securities-and-exchange-commission/) — Regulates U.S. settlement infrastructure; ICSDs follow similar principles
- [Broker](/broker/) — Primary users of the Euroclear–Clearstream bridge

</div>
