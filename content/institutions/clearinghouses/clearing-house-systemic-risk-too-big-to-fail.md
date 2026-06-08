---
title: "Are Clearinghouses Too Big to Fail? Systemic Risk in CCPs"
description: "How concentrating counterparty risk in a central clearing party creates systemic risk, and why regulators treat CCPs as critical financial infrastructure."
keywords:
  - clearinghouse systemic risk
  - central clearing party CCP
  - counterparty risk concentration
  - too big to fail
  - financial system stability
image: "/svg/institutions.svg"
---

*Clearing houses, formally known as central counterparties (CCPs), sit between every buyer and seller in modern derivatives and securities markets, absorbing counterparty risk. By centralizing that risk in a single institution, they reduce bilateral default cascades — but create a new one: if the CCP fails, trillions of dollars in transactions hang in limbo. This paradox underpins the "too big to fail" argument for clearinghouses.*

<div class="wiki-hatnote">

This article addresses whether clearinghouses themselves pose systemic risk, distinct from the question of how clearinghouses function operationally. For mechanics, see the main clearinghouse entry.

</div>

## The Concentration Problem

Before central clearing, every derivatives dealer faced every other dealer as a counterparty. If Dealer A failed, Dealer B lost the value of all trades with A. If B's loss was large enough, B could fail, triggering losses for C, D, and E — a cascade of bankruptcies known as counterparty contagion.

Central clearing was designed to break this chain. Instead of A owing B directly, A owes the CCP, and the CCP owes B. The CCP's bankruptcy remoteness and daily margin practices (collecting collateral daily) reduce the risk that any single dealer default causes the CCP to fail. In theory, this is safer.

But now all dealers depend on one institution: the CCP. If the CCP loses money so large that its capital is exhausted, and if clearing members' contributions to a loss-sharing waterfall do not cover it, then the CCP faces insolvency. Because trillions of dollars in open contracts pass through a CCP, its failure is not a localized problem — it is a system-wide emergency. The CCP has become a single point of failure.

## How Clearing Risk Concentrates

A major CCP such as ICE Clear Credit may handle 99% of the US credit default swap market. A single institution holds the counterparty risk for billions of dollars of CDS. If a large bank defaults on its CDS obligations, the CCP absorbs that loss. If several large banks default simultaneously, or if one default triggers losses on other positions the CCP holds, the CCP's capital can erode fast.

The CCP's risk is not limited to immediate defaults. Many clearinghouses employ variation margin (daily cash settlement) on derivatives positions. In a severe market stress — say, a liquidity crisis or a 20% stock market drop — margin requirements spike. Clearing members must post trillions of dollars in additional collateral within hours. If any significant member cannot meet a margin call, the CCP is forced to liquidate that member's positions in turbulent markets, realizing losses.

The 2008 financial crisis illustrated this risk. Lehman Brothers was a major clearing member. When Lehman collapsed, CCPs faced the technical and operational challenge of liquidating Lehman's portfolio. Fortunately, no CCP itself failed — but the scenario made clear that a CCP failure was plausible under adverse conditions.

## The Systemic Risk Argument

Critics argue that concentrating derivatives and repo risk in a few large CCPs has created a new systemic vulnerability. A CCP default could freeze credit markets overnight. Dealers would not know their true counterparty exposure until the CCP's books were unwound, a process that could take months. In the interim, market participants would hoard cash and cut lending, amplifying financial instability.

A CCP failure could also trigger asset sales by other institutions. If the CCP is forced to liquidate a defaulting member's positions in illiquid derivatives markets, price movements could be violent. Other firms with similar exposures would mark-to-market losses and possibly fail as well. A single CCP failure, under this scenario, propagates into system-wide losses.

Additionally, if a major bank that is also a clearing member fails for reasons unrelated to the CCP (say, due to a geopolitical crisis), the CCP becomes collateral damage. The CCP suddenly faces large default losses, just as its ability to fund operations is questioned. This is the "pro-cyclicality" problem: systemic stress hits the CCP hardest when the broader system is already fragile.

## Regulatory Countermeasures

Regulators and CCP operators acknowledge this risk and have implemented multiple safeguards:

**Robust capital standards**: CCPs must hold capital that covers not just the default of the largest clearing member, but often the largest member plus a second-largest member (LSMC, or "Largest Severe Stress Loss Containing Member" standard). This is a stress-test approach: can the CCP absorb two simultaneous large defaults? The standard was tightened post-2008.

**Stress testing**: CCPs routinely model scenarios in which multiple large clearing members default, either in isolation or in combination with market stresses (volatility spikes, liquidity crunches). Margin models are recalibrated based on these tests.

**Tiered loss-sharing**: If a CCP's capital is exhausted by a default, clearing members contribute additional funds via a "mutuality" or "loss-sharing" fund. This shifts costs to the surviving members, creating incentives for members to monitor each other and ensure the CCP is well-managed.

**Resolution frameworks**: Regulators have developed "resolution" protocols for CCP distress. The Federal Reserve, SEC, and Treasury have plans to stabilize or resolve a failing CCP without allowing cascading market failure. These plans include temporary government lending (liquidity backstops) and mechanisms to transfer CCP functions to a healthy institution.

**Recovery and resolution planning**: Large CCPs must maintain detailed plans for how they would operate under stress or be unwound. This includes identifying which positions could be transferred to other CCPs, and which contracts could be auctioned to market participants.

## Is a CCP Too Big to Fail?

The label "too big to fail" typically applies to institutions whose failure would require government rescue. For CCPs, the argument is subtly different: a CCP may not be too big to fail in absolute terms, but it is too interconnected to fail without coordination between regulators, the central bank, and the private sector.

A CCP closure is not technically impossible. But because a CCP closure would immediately disrupt trillions of dollars in outstanding transactions, policymakers face enormous pressure to backstop the CCP or quickly transfer its business to a competitor. In this sense, CCPs operate under an implicit government guarantee. Clearing members know that if a CCP faces catastrophic loss, regulators will likely ensure the CCP survives, even if that means imposing losses on a subset of members or the broader financial system.

This creates a subtle moral hazard: clearing members may take on excess risk if they believe the CCP will be rescued in a crisis. Regulators try to offset this by imposing strict risk limits on clearing members, mandating margining practices, and threatening to exclude or penalize members that take excessive risk.

## Ongoing Tensions

The regulatory framework remains contested. Some argue that current safeguards are insufficient: stress-test assumptions may underestimate tail risks, and regulatory coordination between countries could break down in a true global crisis. Others argue that multiple competing CCPs would reduce systemic risk by decentralizing clearing, but this view is disputed — fragmented clearing may increase bilateral counterparty risk and reduce the netting benefits of centralized clearing.

Post-2008, regulators required most derivatives to be cleared, concentrating risk in CCPs by design. This was intended to reduce counterparty risk in the short term. It succeeded, but shifted the risk to a new focal point. Whether this is a net gain for stability remains an empirical and philosophical question.

## See also

<div class="wiki-seealso">

### Closely related

- [Central Bank](/central-bank/) — the lender of last resort that would backstop a CCP in crisis
- [Counterparty Risk](/counterparty-risk/) — the risk that a trading partner defaults; CCPs concentrate this
- [Systemic Risk](/systemic-risk/) — risks that threaten the financial system as a whole
- [Repo](/repurchase-agreement/) — short-term secured lending market also routed through CCPs
- [Derivative Hedging](/derivatives-hedging/) — the primary activity cleared through CCPs
- [Credit Default Swap](/credit-default-swap/) — derivatives heavily concentrated in a few CCPs
- Netting — the efficiency CCPs provide by offsetting obligations

### Wider context

- Financial Regulation — the rules governing systemic institutions
- [Capital Adequacy](/capital-adequacy/) — requirements ensuring institutions can absorb losses
- [Liquidity Risk](/liquidity-risk/) — the risk of not being able to meet obligations, acute for CCPs
- [Recession](/recession/) — stress events that test CCP resilience and trigger regulatory intervention

</div>
