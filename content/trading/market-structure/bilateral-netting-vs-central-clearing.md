---
title: "Bilateral Netting vs Central Clearing"
description: "How bilateral netting offsets trades directly between counterparties, versus routing through a central counterparty, affecting counterparty risk, margins, and systemic stability."
keywords:
  - bilateral netting
  - central counterparty clearing
  - ccp clearing
  - counterparty risk
  - netting settlement
  - systemic risk
  - derivative clearing
image: "/svg/trading.svg"
---

*When two parties trade, they can settle by offsetting obligations—netting—either directly with each other (**bilateral netting**) or through a **central counterparty** (CCP) that interposes itself as buyer-to-all-sellers and seller-to-all-buyers. Bilateral netting reduces the cash owed between two firms; central clearing removes direct [counterparty risk](/counterparty-risk/) but concentrates it at the CCP. The choice between the two shapes capital efficiency, margin burden, and systemic stability.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Netting vs Clearing — key facts</div>

<img src="/svg/trading.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Netting simplifies; clearing isolates and concentrates risk.</div>

|   |   |
|---|---|
| **Bilateral netting** | Two parties offset trades; net settlement of cash or assets |
| **Central clearing** | CCP stands as intermediary; each trade novated to CCP |
| **Counterparty exposure** | Bilateral: direct to counterparty; CCP: indirect, to central party |
| **Margin posted** | Bilateral: lower, limited to net exposure; CCP: higher, per clearing member |
| **Settlement risk** | Bilateral: exists if counterparty fails; CCP: backstopped by default fund |
| **Regulatory driver** | Post-2008, CCPs mandated for standardized derivatives |
| **Cost trade-off** | Bilateral: cheaper for simple trades; CCP: expensive but risk-isolating |

</aside>

## Bilateral netting: direct offset

In bilateral netting, two counterparties track all outstanding trades between them and calculate a single net payment. If Bank A owes Bank B €10M on one trade but Bank B owes Bank A €7M on another, only a €3M net payment changes hands. No third party is involved; the settlement is a direct transaction.

The math is straightforward. If Party X has:
- Trade 1: owes $5M
- Trade 2: owed $3M
- Trade 3: owes $2M

Then net obligation = $5M + $2M − $3M = $4M. Only $4M settles; the rest is canceled via netting.

Bilateral netting works cleanly when the two parties have a master agreement (typically an ISDA agreement in derivatives markets) that allows netting across all trades and collateral accounts. The agreement specifies that upon default of one party, the other can close out all positions and settle on a net basis, rather than being forced to honor each trade individually—a protection that reduces recovery risk.

## Central clearing and novation

Central clearing interposes a **central counterparty** between the original traders. When Party X and Party Y trade, the trade is *novated*—the original contract is extinguished and replaced with two new contracts: Party X to CCP, and Party Y to CCP. The CCP becomes the buyer to every seller and the seller to every buyer.

The CCP then nets internally. If 100 buy orders and 95 sell orders for the same contract hit a CCP, the CCP holds a net long of 5 contracts (or distributes the offset among clearing members). From the perspective of the original traders, they face no direct counterparty risk to each other; instead, they face the CCP.

Central clearing requires three key features:

**1. Standardization.** Only standardized contracts (equities, listed options, most exchange-traded futures, and post-2008, standardized swaps) are eligible for central clearing. Custom derivatives remain bilateral.

**2. Membership and participation.** Not every trader is a CCP member. Banks and major dealers are clearing members; smaller firms must clear through a clearing member (broker). The broker is the CCP member and faces the CCP; the small firm faces the broker.

**3. Margin and default fund.** Clearing members post initial and variation margin daily. The CCP also maintains a default fund (mutualized loss-sharing pool) and, in some designs, a guarantee fund. If a clearing member defaults, the CCP uses these resources to absorb losses and keep other members whole.

## Counterparty risk comparison

Under bilateral netting, **counterparty risk is direct and bilateral**. If your counterparty fails, you lose the net amount owed to them and must replace the trade at current market prices. Your loss is:

**Loss = Max(0, Current Mark-to-Market − Amount Owed to You)**

If a counterparty owes you $10M on a position now worth $8M, you can recover $10M (if collateral is posted) but lose $2M on the underlying trade. You also lose all future upside on that position and must execute a replacement trade.

Under central clearing, **counterparty risk is concentrated at the CCP**. Your risk is:

**Loss = Risk of CCP default**

The CCP failure risk is far lower than any single bank's (CCPs are well-capitalized and government-supported), but it is non-zero. If the CCP fails despite its buffers, all clearing members lose proportionally. This is an existential risk for the financial system because all major derivatives flows would seize.

The trade-off: bilateral netting feels safer if your counterparty is strong (e.g., trading with JP Morgan), but it scales your risk with theirs. Central clearing feels centralized, but the CCP is designed to be systemically immune.

## Margin and capital efficiency

Bilateral netting is capital-efficient for large, repeat traders because margin is posted only on net exposures. If two banks trade $100M notional swaps with each other daily, netting might leave them with a $2M net exposure, requiring modest initial margin.

Central clearing requires margin on *gross* exposures and is often higher. The CCP posts margin at standardized levels; it does not recognize the netting between trades that a bilateral counterparty might. Clearing members post initial margin per contract, plus variation margin daily, plus contribute to the default fund. For a clearing member with many trades, margin drag is substantial.

However, this higher margin reflects a real benefit: **risk isolation**. If a clearing member fails, the CCP can liquidate that member's portfolio without triggering cascading defaults across the network. Under bilateral netting, one bank's failure can trigger defaults at multiple counterparties, as seen in the 2008 crisis (Lehman Brothers' bilateral exposures tangled the entire system).

## Regulatory mandate and standardized derivatives

The 2008 financial crisis revealed that bilateral derivatives markets were opaque and systemically dangerous. Dodd-Frank in the US, EMIR in Europe, and similar rules globally mandated central clearing for standardized derivatives. Today:

- **Equity derivatives**: mostly centrally cleared
- **Listed options and futures**: all centrally cleared by design
- **Interest rate swaps**: mandated central clearing in most jurisdictions
- **Credit default swaps**: mostly centrally cleared
- **Foreign exchange forwards**: bilateral netting still common (small notional, short tenor)
- **Bespoke/custom derivatives**: bilateral only; no CCP will clear them

The shift to mandatory clearing reflects a judgment that the systemic risk reduction (isolating failures, preventing cascade) outweighs the capital cost (higher margins). Regulators also require clearing members to clear at multiple CCPs to avoid single-point-of-failure risk, raising costs further.

## Netting across counterparties and collateral arrangements

In bilateral markets, counterparties sometimes agree to **netting across multiple counterparties**, using a triparty collateral agent. For example, Bank A posts collateral with a custodian; Bank B and Bank C both hold claims against that collateral. Upon Bank A's default, Bank B and Bank C share the collateral proportionally. This reduces each counterparty's capital requirement below the bilateral-netting level but introduces operational complexity.

Central clearing automates this via a CCP's default waterfall: initial margin, variation margin, CCP's own capital, default fund, and finally (in extreme scenarios) member haircuts. The waterfall is specified in advance, reducing ambiguity.

## Systemic implications and too-big-to-fail

Central clearing concentrates systemic risk at the CCP. If a major CCP (CME Globex, Eurex, LCH) fails, the entire financial system stops. Regulators have made the implicit guarantee explicit: no major CCP will be allowed to fail. This creates moral hazard—clearing members and their clients know the CCP is government-backed, reducing their incentive to monitor it.

Bilateral netting preserves decentralization but at the cost of interconnectedness. Complex webs of bilateral exposures mean one failure can spread rapidly. The 2008 crisis showed that bilateral netting alone could not contain systemic risk.

Most modern markets use a hybrid: **mandatory central clearing for standardized, liquid contracts**; bilateral netting and collateral arrangements for bespoke, bilateral derivatives. This minimizes systemic concentration while reducing counterparty risk on most flows.

## Implementation and settlement mechanics

**Bilateral netting** requires:
- Legal master agreement (ISDA or equivalent)
- Daily mark-to-market and collateral adjustment
- Close-out protocols and dispute resolution
- Counterparty credit line management

**Central clearing** requires:
- Clearing member registration and capital requirements
- Real-time trade reporting to CCP
- Daily initial and variation margin settlement
- Default procedures and member behavior rules

Operationally, central clearing is more rigid and standardized; bilateral is more flexible but requires active counterparty relationship management.

## See also

<div class="wiki-seealso">

### Closely related

- [Counterparty Risk](/counterparty-risk/) — the risk bilateral netting aims to manage
- Netting Settlement — the mechanism underlying bilateral offsets
- Collateral — posted to secure both bilateral and cleared exposures
- [Swap](/swap/) — the most common instrument affected by clearing rules
- [Dodd-Frank Act](/dodd-frank-act/) — mandated central clearing in the US
- [Credit Default Swap](/credit-default-swap/) — now mostly centrally cleared

### Wider context

- [Systemic Risk](/systemic-risk/) — the financial stability concern driving clearing rules
- Market Infrastructure — CCPs as critical financial infrastructure
- [Repurchase Agreement](/repurchase-agreement/) — another major cleared market
- [Over-the-Counter Market](/over-the-counter-market/) — bilateral derivatives' home

</div>
