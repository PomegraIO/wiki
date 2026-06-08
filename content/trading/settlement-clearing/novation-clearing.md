---
title: "Novation in Clearing"
description: "The legal substitution by which a central counterparty replaces the original trading counterparty, creating two new contracts from one."
keywords:
  - novation clearing
  - bilateral novation
  - CCP counterparty substitution
  - trade novation
  - derivative clearing
image: "/svg/trading.svg"
---

*Novation in clearing is the legal mechanism by which a bilateral trade is transformed into two separate cleared contracts, each with a clearing house as an intermediary counterparty. One bilateral contract between Trader A and Trader B becomes two: A owes the CCP, and the CCP owes B. The original counterparties no longer face each other; they face the CCP.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Novation in Clearing — key facts</div>

<img src="/svg/trading.svg" alt="An abstract editorial mark for trading, settlement, and market operations." />

<div class="wiki-infobox-caption">The legal sleight of hand that makes bilateral trades disappear and creates cleared ones.</div>

|   |   |
|---|---|
| **What it is** | Legal substitution of a CCP as counterparty, terminating the original bilateral contract |
| **Effect** | One bilateral contract → two cleared contracts (Party A–CCP, CCP–Party B) |
| **Legal basis** | Novation agreement signed by both parties and the CCP |
| **Timing** | Can occur at trade execution (mandatory clearing) or post-execution ([back-loading](/back-loading/)) |
| **Key requirement** | Mutual consent of original counterparties and the CCP |
| **Economics** | Remain unchanged; only the counterparty structure changes |

</aside>

## The concept

A novation is a fundamental agreement: the original contract is discharged, and a new one (or two) takes its place. In the clearing context, both parties consent to **substitute the CCP** for each other. The bilateral contract ceases to exist. In its place are two new contracts, each enforceable only between one original party and the CCP.

Before novation:
- Trader A owes $10 million to Trader B (interest rate swap, for example)
- Trader B owes $10 million to Trader A (on the opposite leg)
- Credit risk flows directly between them

After novation:
- Trader A owes $10 million to the CCP
- The CCP owes $10 million to Trader B
- Both A and B now face the CCP, not each other

The cash amounts are identical. The maturity and terms are identical. The only change is *who is obligated to whom*. Yet this change is profound: it removes bilateral credit risk and concentrates it in the CCP.

## Legal requirements

Novation is not automatic. Three conditions must be met:

1. **Consent of the original parties.** Both Trader A and B must agree to terminate their bilateral contract. This is usually straightforward—the CCP requires it as a condition of clearing—but it is legally essential. If A refuses novation, the trade cannot be cleared.

2. **Agreement by the CCP.** The clearing house must accept the role of counterparty to both trades. It does this by signing a novation agreement or by rules of participation that each member accepts.

3. **Discharge of the original contract.** The bilateral contract must be explicitly terminated. Some agreements are novated by written instruction; others by a formalized novation agreement. The exact mechanism varies by CCP and trade type.

Once these are complete, novation is effective. The bilateral contract is dead; the cleared contracts are born.

## Mandatory versus voluntary novation

**Mandatory clearing** (imposed by regulators for standardised derivatives) means all new trades in that asset class must be novated to a CCP immediately upon execution. The CCP is built into the trade workflow. Both parties know at the moment of trading that novation will occur.

**Voluntary clearing** (or post-execution clearing) allows parties to trade bilaterally and later choose to clear. Many non-standardised derivatives, bespoke swaps, and longer-dated contracts are traded bilaterally and may remain bilateral for years. Back-loading regimes allowed voluntary submission of old bilateral trades to CCPs.

The mechanics differ slightly. Mandatory clearing often has novation occur in real-time or within hours. Voluntary back-loading can occur days or weeks after the original trade, after both parties have time to audit the trade details and confirm agreement.

## Novation and settlement finality

Novation and [settlement finality](/settlement-finality/) are closely linked but distinct. Novation is the legal substitution of the CCP as counterparty. Settlement finality is the moment the cleared contract becomes irrevocable and immune from clawback.

A trade can be novated to a CCP without immediate finality. For example:
- 9 a.m.: Bilateral trade is novated to CCP
- 4 p.m. (end of business): Finality is declared across all of the day's trades

During the intervening hours, the novated trade is binding, but it is not yet final; the CCP could, in theory, unwind it if a member defaulted and the trade was in default. Once finality is declared, even default cannot unwind it.

Most modern CCPs grant finality almost instantaneously—often within minutes of novation—to minimise residual risk.

## Novation and credit risk

Before novation, Trader A faces bilateral [credit risk](/credit-risk/) to Trader B. If B defaults, A's claim is against B's bankruptcy estate, competing with all of B's creditors.

After novation, A faces credit risk only to the CCP. If B defaults, A is unaffected (as long as the CCP survives). If the CCP defaults, A is protected by the [CCP Default Waterfall](/default-waterfall-ccp/)—a pool of resources the CCP has set aside or accrued from all members.

This is the core benefit of novation: it transforms concentrated bilateral risk (two counterparties face each other) into pooled, mutualized risk (all parties face a CCP, which is far larger and more capitalised than any single trader).

## Operational mechanics

When a trade is novated, several steps occur:

1. **Trade matching.** Both parties confirm the trade details: notional, terms, underlying, settlement date, etc.

2. **Novation instruction.** Both parties (or their clearing brokers) instruct the CCP to novate the trade. This is typically done electronically, through the CCP's participant portal.

3. **CCP acceptance.** The CCP confirms it has received the instruction, validates the trade against its eligibility rules, and confirms the novation.

4. **Legal execution.** The novation agreement is executed (or is deemed executed by the instruction itself, depending on participant rules).

5. **Risk system updates.** The CCP adds the novated contract to its margin and default-management systems. The original counterparties' systems are updated to reflect the new cleared status.

6. **Collateral.** The CCP typically demands [initial margin](/initial-margin/) on the newly cleared contract. This is calculated using the CCP's risk models and may differ from the collateral the parties held bilaterally.

For exchange-traded contracts (futures, standardized options), novation happens automatically at execution; no additional instruction is needed. The clearing house is a default participant in all such trades.

## Novation and central counterparty risk

Novation creates a new form of systemic risk: CCP concentration risk. If all derivatives in a market are novated to a single CCP, and that CCP becomes insolvent, the entire market is affected. Regulators have worked to mitigate this by:

- Requiring CCPs to be well-capitalised and meet capital and liquidity standards
- Establishing recovery and resolution plans for CCPs
- Creating [default waterfalls](/default-waterfall-ccp/) that give members and the wider market time to respond
- Sometimes mandating multiple CCPs for the same asset class, so traders can distribute risk

Despite these safeguards, a CCP failure would be severe. This is why CCPs are now viewed as systemically important institutions in most jurisdictions.

## See also

<div class="wiki-seealso">

### Closely related

- [Settlement Finality](/settlement-finality/) — the moment novated trades become irrevocable
- [Back-Loading](/back-loading/) — submission of pre-mandate bilateral trades for novation to a CCP
- [CCP Default Waterfall](/default-waterfall-ccp/) — how a CCP protects members after novation if a participant defaults
- Clearinghouses — the institutions that stand as counterparty after novation
- [Counterparty Risk](/counterparty-risk/) — the bilateral risk novation seeks to eliminate

### Wider context

- [Dodd-Frank Act](/dodd-frank-act/) — US legislation mandating novation for standardised derivatives
- Derivatives — the instruments most commonly novated
- [Over-the-Counter Market](/over-the-counter-market/) — the bilateral markets that feed trades into CCPs via novation
- [Securities and Exchange Commission](/securities-and-exchange-commission/) — US regulator overseeing clearing mandates

</div>
