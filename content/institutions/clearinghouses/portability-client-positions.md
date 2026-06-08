---
title: "Portability of Client Positions"
description: "A CCP's mechanism to transfer a defaulting clearing member's client positions intact to a surviving firm, preserving trades rather than forcing liquidation."
keywords:
  - portability
  - client positions
  - clearing default
  - central clearing
  - ccp auction
image: "/svg/institutions.svg"
---

*The **portability of client positions** is a regulatory mechanism that allows a central clearinghouse to transfer the open trades and margin balances of a defaulted clearing member's clients to a surviving clearing member, preserving the economic substance of each client's portfolio rather than forcing immediate sale. Portability operates as an orderly alternative to liquidation, protecting clients from the catastrophic losses and market disruption that fire-sale closeouts can inflict.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Portability — key facts</div>

<img src="/svg/institutions.svg" alt="An abstract editorial mark for institutions." />

<div class="wiki-infobox-caption">The safety net that transfers client positions when a clearing member fails.</div>

|   |   |
|---|---|
| **What it is** | Transfer of a failed member's client accounts to another clearing member |
| **Timeline** | Typically 24 to 48 hours post-default |
| **Who benefits** | Clients; avoids fire-sale losses |
| **Who absorbs loss** | The defaulted member's creditors; surviving member assumes position risk only |
| **Prerequisite** | Clearing members must accept transferred clients in a stress auction |
| **Failure mode** | If no buyer emerges, CCP may be forced to liquidate |

</aside>

## The problem: fire-sale losses

When a clearing member defaults—because of insolvency, a major client loss, or a sudden market shock—the CCP must act quickly to prevent contagion. Historically, the only option was to liquidate every position in that member's account as fast as possible. For clients, this is catastrophic. A large position sold into a thin, panicked market can realise losses far worse than the underlying market move. If multiple members fail, overlapping liquidations can trigger a downward spiral in asset prices.

Portability inverts this outcome. Rather than selling the positions outright, the CCP attempts to transfer the entire client account—all open trades, margin balances, and account documentation—to another clearing member within 24 to 48 hours. The surviving clearing member accepts the client relationship and the economic exposure, but not the defaulted member's unsecured debts. Clients remain continuously cleared without interruption.

## How portability works

When a clearing member default is detected, the CCP immediately segregates that member's client accounts from its house account. The CCP then notifies other clearing members that client accounts are available for transfer and invites them to bid. This auction is typically anonymous to protect client confidentiality, or conducted on an omnibus basis where the acquiring clearing member sees only the net risk profile and margin, not client names.

A surviving clearing member that wins a client account (or accepts an assignment) agrees to take on the economic position: it assumes the market risk, becomes the CCP counterparty, and takes over day-to-day margin management. The transfer includes the client's margin balance at the CCP. What it does not include is the defaulted clearing member's unsecured debt—credit lines, staff salaries, rent—which are resolved in the member's bankruptcy, not through client accounts.

The client relationship itself may or may not transfer. Some clearing members offer "take over" agreements where the surviving member assumes the exact client relationship; others require clients to establish new accounts. In either case, the critical step—the trade transfer—happens under CCP auspices within the regulatory window, not through time-consuming bilateral negotiations.

## Backup auctioneer and forced acceptance

In most developed clearing systems, [Dodd-Frank](/dodd-frank-act/) and equivalent regulations require that clearing members maintain a plan to accept a proportion of client portability transfers in a stress scenario. Some jurisdictions (notably the United Kingdom) have imposed explicit acceptance obligations: a clearing member cannot remain a member unless it commits to absorb a fraction of any large member's client base in the event of default.

If a voluntary auction fails to attract buyers, or if the volume of client positions exceeds what willing members will accept, the CCP may then force assignments on existing members according to a pre-agreed formula. This is controversial: a healthy clearing member may face a sudden injection of risky client positions and margin calls, straining its own capital. Yet regulators view forced acceptance as preferable to the alternative—a CCP unable to transfer positions and forced to unwind them in a market panic.

## Margin, collateral, and auction mechanics

The transfer of client positions and margin balances is complex. At the moment of default, the CCP values all positions at current market prices (mark-to-market) and calculates net margin owed by or to each client. If a client is in profit—the CCP owes it money—that cash or collateral transfers to the acquiring clearing member. If a client owes margin, the acquiring member inherits the receivable and the right to collect it (or liquidate the position if the client fails to meet a call).

The CCP may also offer a "sweetening fee" to entice a clearing member to accept a large or particularly risky client book. This fee comes from the defaulted member's collateral or a loss-sharing pool, allowing the CCP to subsidise the transfer and reduce the chance of failed portability. Some regulations allow the CCP to impose a loss haircut on all clearing members if portability costs exceed the defaulted member's collateral—a measure known as [variation margin](/variation-margin/) claw-back or haircutting.

## Risk to the surviving clearing member

A clearing member that accepts a client transfer inherits the market risk of those positions immediately. If the market moves against the client's portfolio after the transfer, the surviving member faces margin calls and potential loss if the client cannot or will not post additional margin. The acquiring member has recourse only to the client, not to the original defaulted clearing member's estate.

For this reason, surviving clearing members typically conduct rigorous due diligence during an auction: they assess the quality of the client book, the volatility of the positions, and the creditworthiness of individual clients. If the client base is poor quality or the positions are particularly risky, bids will be low or absent. A CCP that finds itself unable to place clients in a voluntary auction faces an acute dilemma and may have to invoke forced acceptance or even liquidate—a regulatory and market failure.

## Portability in a systemic crisis

The ultimate test of portability is a true systemic default: a clearinghouse member so large that no surviving member can absorb its entire client base. Iceland's CCP closure in 2008, triggered by the collapse of local financial institutions, exemplified this scenario. When the demand for transfer capacity exceeds supply, portability fails. Clients must wait for either a forced assignment or a managed wind-down of positions.

Modern regulations attempt to prevent this by diversifying the clearing member base and stress-testing the volume of clients each member can absorb. Still, in a sufficiently severe crisis—a flash crash, a geopolitical event, a deflationary shock—even a robust portability framework can be overwhelmed. This is why regulators now pair portability with additional tools: [CCP recovery and resolution](/ccp-recovery-resolution/) mechanisms that can force loss-sharing and bail-in if portability alone is insufficient.

## See also

<div class="wiki-seealso">

### Closely related

- [Client Clearing](/client-clearing/) — the arrangement that portability protects
- Clearing Member — the entity that defaults and whose clients are transferred
- [Central Counterparty Clearing](/central-counterparty-clearing/) — the CCP orchestrating the transfer
- [Margin Period of Risk](/margin-period-of-risk/) — the close-out window during which portability must complete
- [CCP Recovery and Resolution](/ccp-recovery-resolution/) — tools if portability is insufficient

### Wider context

- [Counterparty Risk](/counterparty-risk/) — why clients need protection against clearing member default
- [Dodd-Frank Act](/dodd-frank-act/) — regulatory mandate for clearing and portability
- [Variation Margin](/variation-margin/) — margin adjustments during transfer
- [Market Risk](/market-risk/) — the inherited exposure when a client account transfers

</div>
