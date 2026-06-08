---
title: "Clearing Member vs Non-Clearing Member: How Market Access Works"
description: "How clearing members hold direct CCP access and assume risk, while non-clearing members access clearing indirectly through sponsors."
keywords:
  - clearing member vs non-clearing member
  - CCP clearing access
  - clearing membership
  - direct clearing
  - sponsored clearing
  - financial market infrastructure
image: "/svg/institutions.svg"
---

*A **clearing member** holds a direct relationship with a central counterparty (CCP) and assumes responsibility for its own trades and, typically, client trades it sponsors. A **non-clearing member** (or indirect participant) accesses clearing through a clearing member sponsor, delegating operational and credit management to that intermediary. The distinction determines capital requirements, operational costs, liability exposure, and market influence.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Clearing Member vs Non-Clearing Member — key facts</div>

<img src="/svg/institutions.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Membership tier defines access cost, operational burden, and risk responsibility in derivatives and securities clearing.</div>

|   |   |
|---|---|
| **Clearing Member** | Direct participant in CCP; holds a clearing account; assumes credit and operational risk for own and (optionally) client trades |
| **Non-Clearing Member** | Indirect participant; routes trades through a clearing member sponsor; does not hold a direct clearing account with the CCP |
| **Capital requirement** | CM: Must post initial margin and meet [**capital adequacy**](/capital-adequacy/) standards; NCM: sponsor handles margin on its behalf |
| **Operational burden** | CM: Manages settlement, collateral, reporting, and default procedures; NCM: delegates to sponsor |
| **Liability for default** | CM: Responsible for meeting obligations to the CCP; NCM: sponsor is liable to CCP; NCM is liable to its clients |
| **Cost of access** | CM: High upfront (membership fee, systems, compliance); NCM: lower fees, higher service charges to sponsor |
| **Typical participants** | CM: Large banks, major dealers, large hedge funds; NCM: smaller funds, regional brokers, corporate end-users |

</aside>

## The Structure of Central Counterparty Clearing

Central counterparties sit at the core of modern derivatives and post-trade securities infrastructure. When two parties trade a derivative or security, the CCP interpose itself: the buyer's counterparty becomes the CCP, and the seller's counterparty becomes the CCP. This eliminates bilateral credit risk between the original traders.

To participate in this process, a firm must be a member of the CCP—or route its trades through someone who is. This distinction—direct vs. indirect access—defines the clearing member and non-clearing member categories.

## Clearing Members: Direct Access and Responsibility

A **clearing member** is admitted to the CCP as a participant in its own right. It holds a clearing account with the CCP and can submit trades for clearing and settlement. A clearing member can clear:

1. **Its own proprietary trades** — positions the firm takes for its own account.
2. **Client trades** — positions it clears on behalf of customers, if it is registered as a sponsor.

When a clearing member submits a trade, it assumes the credit risk of that trade vis-à-vis the CCP. If the clearing member defaults, the CCP can liquidate that member's clearing account and auction its positions. Other clearing members are exposed to the defaulting member through [**default fund**](/default-fund/) contributions, which the CCP uses to cover shortfalls.

Clearing members must:
- Meet capital and liquidity standards set by the CCP and its regulator.
- Post [**initial margin**](/initial-margin/) on all positions.
- Contribute to the CCP's default fund (mutually shared default protection).
- Maintain operations, surveillance, and risk systems to manage their clearing accounts.
- Comply with the CCP's rulebook and regulatory filing requirements.

Membership is expensive and operationally demanding, but it confers several advantages: direct influence on CCP governance, lower per-trade clearing fees, direct access to CCP data and risk management tools, and the ability to clear for clients without a sponsor intermediary.

## Non-Clearing Members: Sponsored Access

A **non-clearing member** (also called an indirect participant or sponsored member) does not hold a direct account with the CCP. Instead, it routes all trades through a clearing member sponsor. The CCP has no direct relationship with the non-clearing member; only the sponsor does.

From the CCP's perspective, a non-clearing member's trades are just trades on the sponsor's clearing account. The CCP does not know (and often does not care) that the sponsor is acting on behalf of a client.

This structure creates a chain of liability:
1. The non-clearing member trades with its end-clients (e.g., taking their hedge fund or corporate customer orders).
2. The non-clearing member submits the trade to its sponsor clearing member.
3. The sponsor clears the trade with the CCP.
4. The sponsor is responsible to the CCP for the trade; the non-clearing member is responsible to the sponsor.

## Capital and Margin Flow Under Sponsorship

When a non-clearing member clears a client trade through a sponsor, margin and capital flow indirectly:

- The **CCP requires initial margin** on the position, which it holds against the sponsor.
- The **sponsor may require additional collateral** from the non-clearing member to cover its intermediation risk and funding costs. Sponsors typically charge haircuts (additional margin buffers) on top of CCP requirements.
- **Variation margin** (daily gains/losses) flows from the CCP to the sponsor, then from the sponsor to the non-clearing member, minus any sponsor fee or haircut.

If the non-clearing member defaults and cannot return collateral to the sponsor, the sponsor absorbs the loss (until it exhausts its own capital). The CCP is protected because the sponsor remains obligated to the CCP.

## Cost-Benefit Trade-Offs

**Cost to become a clearing member:**
- Membership application and admission fee: $50,000–$1 million+, depending on the CCP.
- Upfront capital commitment and ongoing default fund contributions: hundreds of thousands to millions of dollars.
- Technology and operations infrastructure: $1–5 million+ annually.
- Compliance and regulatory filing: ongoing legal and operational cost.

**Benefit:**
- Lower clearing fees per trade (often 50%–70% cheaper than non-clearing member rates after sponsor markup).
- Direct CCP access for clients; ability to compete on execution quality.
- Governance influence (voting on CCP decisions, rule changes, fee schedules).

**Cost to become a non-clearing member (or remaining one):**
- Clearing service fee to sponsor (often 0.5–5 basis points per trade), plus sponsor margin haircuts.
- No governance rights or direct CCP access.
- Operational dependence on sponsor for clearing and risk management.

**Benefit:**
- Much lower capital and infrastructure burden.
- Faster market access without building clearing systems.
- Flexibility to switch sponsors if service degrades.

## Sponsorship Relationships and Operational Risk

A non-clearing member's performance and risk depend significantly on its sponsor. If the sponsor:
- **Raises clearing fees:** the non-clearing member's margins compress.
- **Imposes larger haircuts:** capital requirements increase.
- **Becomes operationally disrupted:** so does the non-clearing member (e.g., no ability to submit new trades if the sponsor's systems fail).
- **Defaults or exits the clearing business:** the non-clearing member must find a new sponsor, potentially at unfavorable terms or after a forced liquidation.

The global financial crisis illustrated this risk: several hedge funds had trades stuck in limbo when their sponsor clearing members failed or became insolvent. Non-clearing members with no alternative sponsor could not exit positions without broker-dealer intermediation, incurring additional costs.

Post-crisis regulations (in particular, Dodd-Frank and EMIR) introduced rules on sponsor protections: non-clearing members' collateral must be segregated from the sponsor's own assets, and sponsors must provide backup access arrangements. These protections reduce but do not eliminate sponsor risk.

## Regulatory and Strategic Drivers of Membership Choice

A firm's decision to become a clearing member depends on:

1. **Scale and trading volume:** If a firm clears many trades, the fixed cost of membership amortizes, making direct membership economical.
2. **Client business:** A broker-dealer or prime brokerage firm typically becomes a clearing member to offer clearing services to hedge funds and clients.
3. **Regulatory capital efficiency:** Clearing members may benefit from lower regulatory capital charges (depending on their CCP's recognition) if they have very large derivatives positions.
4. **Market power:** Clearing members have voting rights and influence on CCP rule changes, important for systemically significant firms.
5. **Operational maturity:** A firm must have sufficient operational infrastructure and risk expertise to manage clearing accounts; smaller firms often lack this and remain non-clearing members.

## See also

<div class="wiki-seealso">

### Closely related

- [Central counterparty clearing](/central-counterparty-clearing/) — How CCPs function and why they matter in post-trade infrastructure
- [Authorized participant](/authorized-participant/) — Analogous distinction in exchange-traded funds
- [Initial margin and variation margin](/initial-margin/) — How margin flows between members and CCPs
- [Default fund](/default-fund/) — Mutually shared default protection mechanism that clearing members contribute to
- [Counterparty risk](/counterparty-risk/) — The credit risk that clearing addresses

### Wider context

- [Securities and Exchange Commission](/securities-and-exchange-commission/) — Regulates clearing membership and CCP operations
- [Capital adequacy](/capital-adequacy/) — Standards clearing members must meet
- [Dodd-Frank Act](/dodd-frank-act/) — Post-crisis legislation that reshaped clearing membership requirements

</div>
