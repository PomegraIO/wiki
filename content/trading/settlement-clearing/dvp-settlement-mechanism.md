---
title: "Delivery Versus Payment: How DVP Settlement Works"
description: "How delivery versus payment settlement ensures that securities transfer and cash payment occur simultaneously, eliminating principal risk."
keywords:
  - delivery versus payment settlement
  - dvp mechanism
  - securities settlement
  - principal risk elimination
  - simultaneous settlement
  - settlement systems
  - institutional trading
image: /svg/trading.svg
---

*In a **delivery versus payment** (DVP) settlement, the securities transfer and the cash payment are linked so that each occurs if and only if the other occurs, eliminating principal risk—the danger that one counterparty delivers the securities but never receives payment (or vice versa). DVP is the industry standard for institutional securities trading and is enforced through central counterparties and real-time settlement systems.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Delivery Versus Payment — key facts</div>

<img src="/svg/trading.svg" alt="An abstract editorial mark for trading and markets." />

<div class="wiki-infobox-caption">DVP locks securities and cash movements together to eliminate counterparty loss on settlement day.</div>

|   |   |
|---|---|
| **Core principle** | Securities move only when cash moves; neither party is at risk of losing both |
| **Where it happens** | Central securities depositories and custodians; enforced by settlement infrastructure |
| **Timing** | Typically T+1 or T+2 (one to two business days after trade date); increasingly T+0 |
| **Principal risk** | DVP reduces it to near zero by making settlement atomic |
| **Pre-requisite** | Both buyer must have cash ready and seller must have securities available |
| **Who enforces it** | Central bank, central counterparty, settlement operator (e.g., DTC, Euroclear, Clearstream) |
| **Failure mode** | If either side defaults, settlement fails; netting can reduce aggregate obligations |

</aside>

## The Problem DVP Solves

Before DVP became standard, securities settlement was fraught with counterparty risk. A buyer would wire cash to a seller, trusting that the seller would deliver the securities afterwards. Or a seller would deliver securities first, trusting the buyer to pay. Either way, one party was exposed for a window of time—sometimes hours, sometimes days—during which the counterparty could fail to deliver its side of the trade, leaving the other with a loss.

This risk, called **principal risk** or **settlement risk**, was not academic. When large securities trades failed, the resulting losses cascaded: a bank that did not receive expected cash could fail to meet its own payment obligations, triggering a domino effect across the financial system. Regulatory bodies and exchanges recognized that without simultaneous settlement, systemic risk was unacceptable.

## How DVP Works Mechanically

DVP works through a real-time connection between the cash settlement system (often the central bank) and the securities settlement system (usually a central securities depository or CSD). When a trade is ready to settle:

1. **The seller's securities account** is frozen or instructed to transfer the agreed-upon quantity of securities.
2. **The buyer's cash account** is frozen or instructed to transfer the agreed-upon cash amount.
3. **The settlement system** checks that both accounts have sufficient resources (the seller has the securities; the buyer has the cash).
4. **If both checks pass, the system executes both transfers simultaneously** in a single transaction. Securities move to the buyer; cash moves to the seller.
5. **If either check fails, neither transfer occurs** and the settlement fails, alerting both parties to resolve the issue.

The crucial element is **atomicity**: the two transfers are one indivisible event. Either both happen or neither does. There is no window in which one party has the cash but not the securities, or vice versa.

## DVP Models: Gross Versus Netting

There are three main DVP models, differing in how trades are aggregated before settlement:

**Model 1 (Gross DVP):** Each trade settles individually and immediately (or at the end of day). If Trader A buys 100 shares from Trader B, that trade settles on its own, with cash and securities moving as a single transaction. This is the simplest model and the most common in real-time systems today, but it requires both parties to have full resources ready for every trade.

**Model 2 (Bilateral netting):** Before settlement, the two parties (or a pair of banks) calculate their net positions. If Bank A owes Bank B 100 shares and Bank B owes Bank A 50 shares, they settle the net: Bank A delivers 50 shares and Bank B delivers the corresponding cash. This cuts down settlement traffic.

**Model 3 (Multilateral netting):** A central entity (usually a clearinghouse or CCP) nets all trades across all participants. Each participant then settles its net position with the clearinghouse, not bilaterally with each counterparty. This is the most efficient model and the primary mechanism used in modern equity and derivatives markets, because it allows the clearinghouse to guarantee settlement even if one participant defaults (the clearinghouse steps in as counterparty to both sides).

When [netting in clearing](/netting-in-clearing-how-it-reduces-settlement-obligations/) is used, DVP still applies: the netting reduces the volume of securities and cash that must move, but when settlement occurs, it is still simultaneous and atomic.

## T+1, T+2, and Settlement Horizons

For decades, equity settlement operated on a T+2 basis: trades settled two business days after execution. The delay served practical purposes—it gave institutions time to confirm trade details, verify accounts, and physically transport securities and funds.

As technology improved, the industry moved to faster settlement windows. In 2024, U.S. equities moved to T+1 (settlement the next business day), reducing counterparty risk windows and freeing up capital more quickly. Some markets and asset classes now operate on T+0 (same-day settlement) or even near-real-time settlement.

The faster the settlement, the less principal risk and the less capital tied up in settlement pipelines. However, faster settlement requires more robust and reliable infrastructure and greater operational discipline from market participants.

## The Role of Central Counterparties

In modern markets, a **central counterparty** (CCP) is often interposed between buyers and sellers. The CCP becomes the buyer to every seller and the seller to every buyer. This means:

- The seller does not have to trust the buyer; it trusts the CCP.
- The buyer does not have to trust the seller; it trusts the CCP.
- If one party defaults, the CCP steps in and settles with the other party using default funds or its own capital.

The CCP enforces DVP: it will not allow a seller's securities to leave its custody unless it simultaneously releases cash to the seller from the buyer's account. This central orchestration is why modern markets are far safer from settlement risk than bilateral over-the-counter trades.

## Failures and Shortfalls

Despite DVP protections, settlements do sometimes fail. This happens when:

- A seller does not deliver securities on time (a [settlement fail](/settlement-fails-causes-and-consequences/)).
- A buyer does not have sufficient cash (unusual in a CCP model because the CCP pre-funds or has credit lines).
- Systems fail or undergo maintenance.
- Regulatory or legal constraints prevent settlement.

When a failure occurs, the trade does not settle and both parties must negotiate a resolution. Depending on market rules, a failed trade might be forced to settle a few days later, or it might be canceled entirely.

## DVP and Different Asset Classes

DVP is standard for equities and most fixed-income securities traded on public exchanges. For over-the-counter derivatives and repurchase agreements, DVP principles apply, but infrastructure varies. Modern derivatives settlement through a CCP (such as LCH or CME) incorporates DVP. Bilateral repo trades may have less immediate DVP protection, which is why central banks and regulators have pushed for central clearing of repo markets.

In cryptocurrency and blockchain markets, DVP through traditional central counterparties does not apply. Some blockchain platforms attempt to implement DVP-like mechanisms through smart contracts or atomic swaps, but these operate under different assumptions and may not eliminate all principal risk.

## See also

<div class="wiki-seealso">

### Closely related

- [Settlement fails: causes and consequences](/settlement-fails-causes-and-consequences/) — Why trades sometimes fail to settle and the costs that result
- [Netting in clearing: how it reduces settlement obligations](/netting-in-clearing-how-it-reduces-settlement-obligations/) — How aggregating offsetting trades cuts settlement volume
- Clearinghouse and central counterparty — The infrastructure that enforces simultaneous settlement
- [Settlement risk and counterparty risk](/counterparty-risk/) — The broader category of risk DVP addresses
- [Custody and depositories](/custodian/) — The infrastructure that holds securities for settlement

### Wider context

- Stock settlement and T+1 — How the recent move to next-day settlement works
- Securities market infrastructure — The systems behind modern trading
- [Securities and exchange commission](/securities-and-exchange-commission/) — The U.S. regulator overseeing settlement standards
- [Broker](/broker/) — Institutions that facilitate DVP on behalf of clients
- [Repurchase agreement](/repurchase-agreement/) — A short-term financing instrument where DVP is critical

</div>
