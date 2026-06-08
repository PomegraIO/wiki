---
title: "Default Fund"
description: "Mutualised pool of member contributions a central counterparty draws to cover losses from a defaulting member."
keywords:
  - default fund
  - central counterparty
  - clearinghouse
  - member contributions
  - CCP
  - counterparty risk
  - mutualization
image: "/svg/institutions.svg"
---

*A default fund is a mutualized reserve that a [central counterparty](/central-bank/) (CCP) or [clearinghouse](/central-bank/) holds in common. When a member defaults and its posted [collateral](/market-risk/) is exhausted, the CCP draws on the default fund to cover the loss—spreading the cost across all surviving members. Default funds transform bilateral [counterparty risk](/counterparty-risk/) into systemic risk mutualized by the collective.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Default Fund — key facts</div>

<img src="/svg/institutions.svg" alt="An abstract editorial mark for financial institutions." />

<div class="wiki-infobox-caption">Mutualized member contributions absorb losses when clearing members fail.</div>

|   |   |
|---|---|
| **What it is** | Reserve pool funded by clearinghouse members; absorbs default losses after collateral exhaustion |
| **Also called** | Guarantee fund, clearing fund, or loss-mutualisation account |
| **Trigger** | Member default; exhaustion of member's [margin](/bid-ask-spread/) and security |
| **Funding** | Proportional or risk-based contributions from all clearing members |
| **Governance** | [CCP](/central-bank/) manages; loss allocation rules vary by clearinghouse |
| **Related concepts** | [Counterparty risk](/counterparty-risk/), [margin call](/bid-ask-spread/), [central counterparty](/central-bank/), member default |
| **Scope** | Universal in equity, derivatives, and fixed-income clearinghouses; mandatory for members |

</aside>

## The architecture of mutualisation

A [clearinghouse](/central-bank/) sits between buyers and sellers. Instead of Party A owing Party B directly, Party A owes the clearinghouse and the clearinghouse owes Party B. This interposition eliminates bilateral [counterparty risk](/counterparty-risk/)—you no longer worry whether your counterparty will perform; you worry only whether the clearinghouse will.

But clearinghouses must manage their own risk. They require members to post [collateral](/market-risk/)—called margin—proportional to their open positions. If a member defaults (fails to settle, breaches credit standards, or becomes insolvent), the clearinghouse liquidates the member's collateral to cover its obligations to other members.

In a typical default, collateral suffices. The member posted $10 million in margin; they owe $10 million; the clearinghouse recovers fully. No problem. But severe market stress can make this assumption fail. Suppose volatility explodes and the member's positions are deeply underwater. They owe $15 million, but collateral covers only $10 million. A $5 million hole remains. This is where the default fund steps in.

## How loss allocation works

The default fund is capitalized by contributions from all clearinghouse members, typically proportional to their trading volume or [notional exposure](/market-capitalization/). A large bank clearing $100 billion in daily trades contributes more than a small dealer clearing $1 billion. This linkage ensures that the riskiest participants—those moving the most volume—fund the greatest share of protection.

When a default occurs and collateral is depleted, the CCP draws on the default fund to cover the shortfall. The draw is typically allocated across surviving members according to a pre-agreed formula. Many clearinghouses use a tiered approach: the CCP's own capital covers the first tranche, then the defaulting member's default fund contribution is exhausted, then surviving members' contributions are used pro rata.

The allocation is not painless. If a large member defaults during a crisis, the draw can be substantial and rapid. A clearinghouse with a default fund of $5 billion facing a $20 billion loss will exhaust its own capital and the defaulter's contribution, then impose calls on surviving members. Each surviving member faces a loss proportional to its exposure. The mutualization is real: you bear the cost of another member's failure.

## Risk implications

Mutualisation has two effects: it reduces the expected loss to each individual member (the risk is shared) but it creates a new source of risk—the possibility of a sudden, unexpected draw from the default fund. From the perspective of a single clearing member, this is a form of [tail risk](/tail-risk/). In normal times, the default fund sits idle. In crises, it bleeds cash.

This creates a perverse incentive: members benefit if others fail, because the default fund is finite and will be exhausted in order. If Bank A's contribution is high and Bank B's is low, Bank A bears more loss when the fund is depleted. Some clearinghouses address this by allowing the default fund to be replenished after a draw, requiring surviving members to fund the shortfall. This avoids permanent reduction in the common safety cushion but compounds the crisis impact on members.

## Size and adequacy

The adequacy of a default fund is measured against historical and stress scenarios. How large should it be? No consensus exists. A fund that covers all but the two largest members' defaults is a common rule. Another is coverage of the 99th percentile loss under stress scenarios. Yet no amount of pre-positioning guarantees sufficiency if markets move in unprecedented ways.

The 2008 financial crisis tested several clearinghouses' default funds. Most proved adequate because no major member defaulted at the clearinghouse level. However, Lehman Brothers' default at the LCH.Clearnet fixed-income clearinghouse in 2008 revealed how thin the margin of safety can be. The clearinghouse's capital and default fund together bore an estimated $2 billion loss—substantial but manageable. Had the default been larger, or had multiple members defaulted in cascade, the fund would have been depleted and emergency measures (member bailins or clearinghouse recapitalization) would have been necessary.

Post-2008 regulatory standards (including Dodd-Frank in the US and EMIR in Europe) require higher default funds and more frequent stress testing. Nevertheless, adequacy remains a moving target in markets that regularly produce tail events previously thought impossible.

## Behavioral and systemic effects

Default funds introduce moral hazard. A member taking excessive risk knows it is mutually insured against tail losses (up to the fund's limit). This incentivises riskier behaviour than would occur if members bore 100% of their own default loss. Regulators attempt to counter this through margin requirements (higher margin for riskier positions) and member-clearing requirements (a member's own capital must exceed its default fund contribution), but the incentive persists.

Default funds also amplify systemic risk in crises. Suppose many members face losses simultaneously (a financial panic). Each member's ability to meet calls on the default fund deteriorates as their own profitability declines. The clearinghouse, facing calls from non-defaulting members to cover defaults from troubled members, becomes pressured itself. In severe crises, clearinghouses may become unable to satisfy loss absorption, forcing government or central bank intervention.

This dynamic was visible in 2020 when extreme [volatility](/volatility-smile/) in equity markets caused clearinghouses to call for large intra-day margin increases. Some members struggled to meet these calls, creating liquidity stress throughout the system. The default fund, in this scenario, is not a solution but a slow mechanism; what matters is moment-to-moment ability to absorb shocks through collateral and liquidity.

## Governance and transparency

Clearinghouses typically publish default fund rules in their rulebooks, disclosing how contributions are calculated and how loss allocation works. However, the actual size of the default fund, the composition of its assets, and stress-testing methodologies are often less transparent. This reflects both proprietary interest (clearinghouses compete and do not wish to reveal reserves) and practical difficulty (funds are complex, hold heterogeneous collateral, and are difficult to value rapidly).

Post-crisis regulatory standards push for greater transparency. Regulators and participating members increasingly demand clarity on fund adequacy. Some clearinghouses now publish aggregate stress test results. Nevertheless, a veil of confidentiality remains, particularly around the details of how loss would be allocated in a member default. This lack of transparency can itself breed systemic risk if market participants doubt the sufficiency of protection.

## International variation

Default fund structures vary across clearinghouses. The London Clearing House (equity and derivatives), CME Clearing (futures and derivatives), Eurex (European equities and derivatives), and others all employ default funds, but the proportions of capital, contribution formulas, and recovery procedures differ. Some clearinghouses maintain larger default funds relative to activity; others rely more heavily on strict [margin](/bid-ask-spread/) discipline.

Asian and emerging-market clearinghouses often use similar structures, though government backing is sometimes explicit (state sponsors may guarantee a portion of the default fund). This is both a advantage (greater loss-absorption capacity) and a complication (moral hazard magnifies because the implicit government put is widely understood).

## See also

<div class="wiki-seealso">

### Closely related

- [Counterparty risk](/counterparty-risk/) — Risk that the other party to a transaction fails to perform; default funds mutualize this
- [Central counterparty](/central-bank/) — Institution that interposes itself between trading parties, using default funds to manage its risk
- [Margin](/bid-ask-spread/) — Collateral posted to clearinghouses; exhausted before default fund is drawn
- [Collateral](/market-risk/) — Assets posted as security; the first loss buffer in a member default
- [Credit risk](/credit-risk/) — Member failure is a credit event for the clearinghouse and surviving members

### Wider context

- [Securities and Exchange Commission](/securities-and-exchange-commission/) — US regulator of clearinghouses and default fund adequacy
- [Dodd-Frank Act](/dodd-frank-act/) — Post-2008 law mandating clearinghouse standards and default fund minimums
- [Systemic risk](/tail-risk/) — Default funds address bilateral risk but can amplify systemic stress in crises
- [Liquidity risk](/liquidity-risk/) — During crises, calls on default funds can trigger liquidity crunches
- [Mutual insurance](/counterparty-risk/) — Conceptual basis for default fund mutualization across clearing members

</div>
