---
title: "Client Clearing"
description: "An arrangement in which end-users access CCP services indirectly through a clearing member, rather than joining the clearinghouse directly."
keywords:
  - client clearing
  - clearing member
  - central clearing
  - derivatives clearing
  - ccp access
image: "/svg/institutions.svg"
---

*In **client clearing**, an end-user—typically a hedge fund, pension fund, or institutional trader—does not join a central clearinghouse directly. Instead, it routes trades through a clearing member (often an investment bank), which holds the client's account at the CCP. The clearing member acts as an intermediary, funding margin requirements on behalf of its clients and managing their positions within the clearinghouse's risk framework.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Client Clearing — key facts</div>

<img src="/svg/institutions.svg" alt="An abstract editorial mark for institutions." />

<div class="wiki-infobox-caption">The indirect route that most end-users take to central clearing.</div>

|   |   |
|---|---|
| **What it is** | End-user access to a CCP through a clearing member intermediary |
| **Also called** | Indirect clearing, agency clearing |
| **Participants** | Client, clearing member, [central counterparty](/central-counterparty-clearing/) |
| **Main benefit** | Lower entry barriers; CCP doesn't contact each end-user |
| **Main cost** | Credit and concentration risk with the clearing member |
| **Initiated by** | Dodd-Frank and equivalent international regulations |

</aside>

## Why client clearing exists

Joining a central clearinghouse directly requires substantial capital, technology infrastructure, and regulatory approval. Most hedge funds and institutional traders cannot meet these thresholds. Client clearing solved this by allowing end-users to clear through an existing clearing member—typically a major bank—that already has a seat at the CCP.

The arrangement is efficient: the clearing member aggregates margin and risk management across many small clients, achieving economies of scale. The CCP avoids a explosion in the number of direct members it must supervise. Clients get access to central clearing without having to operate a clearing desk and front-to-back control systems themselves. Clearing members earn fees for the service and retain a profitable business line.

## The clearing member's role

A clearing member that offers client clearing maintains a house account at the [central counterparty](/central-counterparty-clearing/) and separate client subaccounts. Trades executed by a client are reported under that subaccount, and margin is collected and posted by the clearing member. The clearing member is obligated to fund margin calls and carry the client's default risk on its balance sheet.

From the CCP's perspective, the clearing member is the counterparty. If the clearing member defaults, the CCP must seize and liquidate all client positions in that clearing member's account, then return assets to each client. The speed and fairness of this [portability](/portability-client-positions/) process is critical: clients want assurance that they can be transferred intact to another clearing member rather than liquidated in a fire sale.

## Credit and concentration risk

The trade-off for clients is that they now face [counterparty risk](/counterparty-risk/) with their clearing member. If the clearing member becomes insolvent—or is perceived as likely to do so—clients lose immediate access to their positions and margin. Some clearing members maintain segregated, specially-secured client accounts (so-called "protected" accounts) to reduce this risk, but full elimination is impossible; if the clearing member defaults mid-position, even a protected account can be affected by margin calls or delays in transfer.

Clearing members also face concentration risk: a large client that loses money and fails to post additional margin forces the clearing member to decide whether to close the position, extend credit (increasing its own risk), or allow a default. If several large clients face trouble simultaneously, the clearing member's capital can be strained.

## How portability protects clients

To mitigate the risks of client clearing, regulators and clearinghouses introduced the principle of [portability of client positions](/portability-client-positions/). If a clearing member fails, the CCP does not liquidate every client position. Instead, it attempts to transfer the entire client account—trades intact, margin balances intact—to another clearing member within a prescribed window (often 24–48 hours). This preserves the client's economic exposure and avoids the need to realize losses in a fire sale.

Portability requires clearing members to maintain standardized account structures and documentation so that transfers can execute quickly. It also implies that the CCP must have a pre-established list of backup clearing members willing to accept transferred accounts during a stress event. If no clearing member volunteers, the CCP itself may be forced to wind down the client's positions at significant cost.

## Regulation and transparency

Under [Dodd-Frank](/dodd-frank-act/) and equivalent regulations in Europe and Asia, client clearing is mandatory for standardised derivatives: large financial firms must clear most interest-rate swaps, [credit](/credit-default-swap/) and equity derivatives through CCPs rather than bilaterally. This mandate dramatically increased the use of clearing members as intermediaries.

Regulators now impose extensive rules on clearing members. They must segregate client assets, publish margin methodologies, and stress-test their ability to fund client calls. Some jurisdictions allow clients to opt out of segregation and accept direct mingling of their funds with house funds—a riskier choice that can lower fees. The degree of transparency varies: some clearing members disclose client names to the CCP; others use omnibus accounts where the CCP sees only the clearing member's aggregate risk.

## The cost-access trade-off

For a small or medium-sized client, client clearing is often the only feasible way to access central clearing. Direct membership imposes fixed costs—infrastructure, regulatory capital, compliance staff—that only the largest institutions can absorb. Client clearing democratises access but adds a layer of fees: the clearing member typically charges a percentage of notional cleared volume or a flat per-contract fee.

Larger clients sometimes negotiate better terms by offering a clearing member stable, high-volume business. Some clearing members compete fiercely on client clearing fees in the hope of winning trading commissions and other revenue. Others have exited the business entirely, shrinking the number of clearing members available and potentially concentrating risk in the remaining few.

## See also

<div class="wiki-seealso">

### Closely related

- Clearing Member — the intermediary standing between client and CCP
- [Portability of Client Positions](/portability-client-positions/) — transfer mechanism if the clearing member fails
- [Central Counterparty Clearing](/central-counterparty-clearing/) — the CCP the clearing member connects to
- [Margin Period of Risk](/margin-period-of-risk/) — close-out window that affects clearing member margin calls
- [CCP Recovery and Resolution](/ccp-recovery-resolution/) — tools if the CCP itself is at risk

### Wider context

- [Counterparty Risk](/counterparty-risk/) — why clients face credit exposure to the clearing member
- [Dodd-Frank Act](/dodd-frank-act/) — mandate for clearing
- Derivatives — products commonly cleared through client accounts
- Segregation and Custody — protection of client assets

</div>
