---
title: "CCP Recovery and Resolution"
description: "Regulatory mechanisms to stabilise or wind down a failing central clearinghouse, including loss allocation, margin haircutting, and forced bail-in of members."
keywords:
  - ccp recovery
  - ccp resolution
  - bail-in
  - variation margin haircutting
  - loss sharing
image: "/svg/institutions.svg"
---

*The **recovery and resolution** framework for a central clearinghouse is a regulatory toolkit designed to stabilise or orderly wind down a failing [CCP](/central-counterparty-clearing/). It includes contractual loss-sharing mechanisms (variation-margin haircutting, auction losses imposed on clearing members), equity clawbacks, and forced reduction of member positions. If recovery fails, resolution—formal insolvency or statutory takeover—transfers assets and liabilities to a backstop or liquidates the CCP under bankruptcy law. The goal is to contain contagion and protect the broader financial system.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">CCP Recovery and Resolution — key facts</div>

<img src="/svg/institutions.svg" alt="An abstract editorial mark for institutions." />

<div class="wiki-infobox-caption">The legal and financial toolkit for a failing clearinghouse.</div>

|   |   |
|---|---|
| **Recovery tools** | Variation-margin claw-back, default fund haircuts, position reduction |
| **Resolution tools** | Forced restructuring, bail-in, asset transfer, wind-down |
| **Trigger** | CCP unable to meet its margin or default-fund obligations |
| **Initiator** | CCP board; often subject to regulatory direction |
| **Primary objective** | Protect the financial system; preserve clearing services where possible |
| **Liability allocation** | Losses are imposed on clearing members and participants in a prescribed order |

</aside>

## Why CCPs need recovery frameworks

A central clearinghouse collects margin and default-fund contributions from all clearing members to absorb the loss of a member's default. Under normal circumstances, this buffer is adequate. But under stress—a 1-in-100-year market move, a correlated member failure, or a geopolitical shock—losses can exceed the pre-funded default fund. At that point, a CCP faces insolvency unless it can recover capital from its members or wind down operations.

Before 2008, most clearing infrastructure lacked explicit recovery and resolution plans. A CCP default was treated like any other bankruptcy—liquidation under state law, with clients' funds at risk. The financial crisis and subsequent reforms ([Dodd-Frank Act](/dodd-frank-act/), European EMIR rules, Australian RBA frameworks) mandated that major CCPs maintain published recovery and resolution frameworks that clearly specify how losses are allocated if the buffer is breached.

## Recovery: variation-margin haircutting

The primary recovery tool is **variation-margin haircutting**. When a CCP exhausts its own capital and default fund, it imposes a percentage loss on all clearing members' variation-margin cash balances. If a member holds €100 million in variation margin and the CCP declares a 10% haircut, the member loses €10 million. This directly converts client margin—money held by the CCP—into CCP capital.

Variation-margin haircutting is controversial because it is sudden and severe. Members can lose millions overnight, with no warning. Regulators justify it as a necessary instrument to prevent full failure: a 5–10% haircut, imposed immediately, can stabilise a CCP and allow it to continue operations. The alternative—CCP insolvency—would force liquidation of all positions and disrupt the entire clearing system.

Most CCP rulebooks specify a tiered approach: first, losses hit the CCP's own capital and equity. Then, a proportion of the default fund is exhausted. Only after those steps are depleted does variation-margin haircutting apply. The order reflects a hierarchy of pain: the CCP's owners lose first, then clearing members' risk contributions, then members' operational margin.

## Default-fund allocation

The default fund is a separate pool funded by each clearing member as a fixed contribution or a percentage of notional volumes. If a single member defaults, only its own portion of the default fund is used to cover the loss (plus any unfilled shortfall is allocated to others). In a multi-member failure or a systemic stress event, the CCP may deploy the entire default fund, and then pro-rata losses are imposed on all remaining members.

Some CCPs have introduced tiered default-fund structures: a first layer funded by all members in equal amounts, a second layer funded by larger members or those with high notional exposure, and a third layer underwritten by the CCP itself or a government backstop. This tiering limits the hit on small clearing members while still ensuring that large players bear proportional risk.

## Position reduction and forced deleveraging

If variation-margin haircutting and default-fund depletion still leave losses unresolved, a CCP can invoke **forced position reduction**. Clearing members are compelled to cut the notional size of their exposures—a 10% reduction, for example—across all clients. This immediately lowers the CCP's aggregate risk and can unlock collateral. It is deeply disruptive: clients see their positions unwound without permission, and the market impact of simultaneous selling can trigger further losses.

A CCP may also demand that members transfer excess risk to other members or bid to exit positions at a loss. Alongside forced position reduction, some frameworks allow the CCP to suspend the ordinary margin model temporarily and impose higher charges, effectively forcing a capital injection from members or liquidation of positions to raise cash.

## Resolution: bail-in and restructuring

If recovery tools are exhausted and the CCP is still insolvent, it enters formal resolution. This can take several forms. In some jurisdictions, the CCP's bank regulator or financial stability authority issues a resolution order, triggering statutory bail-in: equity holders lose their investments, debt holders' claims are written down, and the CCP is either sold to a buyer or merged into another clearinghouse.

Under bail-in, contractual creditors (including clearing members' receivables from the CCP, if any) are partially or fully written down. The point is to raise capital from financial creditors rather than taxpayers. A CCP that cannot recover quickly enough is deemed unable to function, and its clearing operations are transferred to a healthy competitor or a state-sponsored continuation vehicle. Clients' positions are ideally preserved during this transfer through the [portability](/portability-client-positions/) mechanism.

## Resolution authority and discretion

Modern CCP frameworks (e.g., EMIR in Europe, Title II of Dodd-Frank in the US) assign resolution authority to a designated regulator or agency. In the US, the Federal Reserve and the CFTC can jointly place a systemically important CCP into orderly liquidation under the Financial Stability Board framework. In Europe, national resolution authorities may issue resolution orders that override the CCP's rulebook if necessary to preserve financial stability.

Resolution authorities are given broad discretion: they can force debt write-downs, override contractual priority, transfer assets to a buyer, or wind down the CCP entirely. This discretion is intentional—it prevents a CCP default from freezing the financial system—but it also introduces uncertainty. Clearing members and creditors cannot be entirely sure what their claims are worth in a resolution scenario, which can raise CCP funding costs and credit spreads.

## The limits of recovery and resolution

Even a well-designed recovery framework has limits. If a single catastrophic loss—a 20% market move in a major asset class, a correlated default among top clearing members—overwhelms the CCP's entire buffer and recovery toolkit, some losses must be absorbed by unsecured creditors or the government. The 2008 financial crisis underscored this: no amount of pre-funding can hedge against a true tail-risk event.

For this reason, regulators now pair recovery and resolution frameworks with other safeguards: stress-testing (so CCPs understand the losses they can face), diversified clearing-member bases (to prevent concentration risk), and macroprudential oversight (to prevent excessive leveraging across the system). A CCP recovery plan is a necessary but not sufficient hedge against systemic failure.

## See also

<div class="wiki-seealso">

### Closely related

- [Central Counterparty Clearing](/central-counterparty-clearing/) — the institution being recovered or resolved
- [Margin Period of Risk](/margin-period-of-risk/) — affects how quickly a CCP must act
- [Client Clearing](/client-clearing/) — clients protected by resolution frameworks
- [Portability of Client Positions](/portability-client-positions/) — mechanism to transfer positions during CCP stress
- [Default Fund](/default-fund/) — the CCP's loss buffer that recovery tools deplete

### Wider context

- [Counterparty Risk](/counterparty-risk/) — why CCP safety is systemic
- [Dodd-Frank Act](/dodd-frank-act/) — US mandate for CCP resolution frameworks
- [Systemic Risk](/systemic-risk/) — the reason recovery and resolution exist
- [Stress Testing](/stress-testing/) — validating CCP buffers before they are tested by reality

</div>
