---
title: "What a Smart Contract Audit Covers — and What It Does Not"
description: "Smart contract audit scope: what vulnerability classes are caught, what remains undetected, and how audit status should factor into risk assessment."
keywords:
  - smart contract audit scope
  - what smart contract audit covers
  - smart contract security review
  - audit limitations risks
  - code vulnerability detection
---

*A **smart contract audit** is a security review, not a guarantee of safety. Professional auditors examine code for common vulnerability classes—reentrancy, integer overflow, access-control flaws, logic errors—but cannot detect economic exploits, game-theoretic attacks, or risks that emerge only when the contract interacts with live market conditions. An audit passing gives confidence in code quality, not immunity from loss.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Smart Contract Audit Scope — key facts</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for cryptocurrency and blockchain." />

<div class="wiki-infobox-caption">An audit reveals code flaws—not market behavior or economic design.</div>

|   |   |
|---|---|
| **Typical audit scope** | Code review for known vulnerability classes; static and dynamic analysis |
| **Usually catches** | Reentrancy, overflow/underflow, improper access control, logic bugs |
| **Usually misses** | Price-oracle manipulation, liquidation cascades, incentive misalignment, front-running |
| **Audit timeline** | 1–4 weeks for medium-sized contracts; costs $5,000–$50,000+ |
| **Auditor firms** | Trail of Bits, OpenZeppelin, Certora, ConsenSys, others |
| **Audit types** | Code review, formal verification (mathematical proof), or hybrid |
| **Post-audit risk** | Audits are point-in-time snapshots; upgrades invalidate findings |

</aside>

## What Auditors Look For

A professional **smart contract audit** examines code against a checklist of known vulnerabilities. The best audits use multiple techniques: manual code review (a human reads every line), static analysis (tools scan for patterns), and dynamic testing (simulations run the code against test scenarios).

**Reentrancy** is a classic target. A contract that sends funds before updating balances can be exploited by a malicious recipient that calls the original contract again, draining more funds. Good auditors will flag functions that transfer value and verify state changes happen first.

**Integer overflow and underflow** were common in early smart contracts. A counter that counts from 0 to 255 and wraps back to 0 if incremented again. Modern Solidity versions protect against this by default, but auditors still check for cases where developers disabled safety mechanisms.

**Access control** flaws mean anyone can call sensitive functions. An auditor verifies that only the owner can withdraw, only administrators can change parameters, only authorized callers can trigger state changes. Missing checks are high-severity findings.

**Logic errors** are harder to spot but critical. A contract meant to limit user withdrawals might have an off-by-one error in a loop, allowing more withdrawals than intended. Auditors write test cases that probe edge cases: what happens at the minimum or maximum value? What if amounts are zero? What if called in rapid succession?

These techniques are proven and effective. An audit passing gives real confidence that common programming mistakes were caught.

## What Auditors Typically Miss

The audit's scope is code-level security—"is the code doing what it claims?" What audits rarely catch is whether the code's economic design is sound—"is the system safe when incentives are real?"

**Price-oracle manipulation** is a leading blind spot. If a lending protocol uses an off-chain price feed to set collateral value, an attacker might temporarily move the price on a decentralized exchange, triggering liquidations or withdrawals at unfair rates. The contract code—the price-checking logic—may be correct. But the system's dependence on manipulable data is a design flaw, not a code bug. Most audits mention it as a risk; few can eliminate it.

**Liquidation cascades** occur when one liquidation triggers another in a tightly coupled market. A contract may be coded correctly to liquidate a borrower if collateral falls below a threshold, but if many borrowers are underwater simultaneously, mass liquidations can crash prices further, orphaning more collateral. No code mistake occurs; the system's leverage and correlation are the problem.

**Incentive misalignment** and **game-theoretic attacks** are often invisible to code-level review. A governance contract may have no bugs—voting works, execution works, funds transfer correctly—but the voting rules might allow a whale to extract value by proposing harmful upgrades and hoping low participation lets them pass. The code is sound; the system's incentive structure is weak.

**Front-running** and **MEV** (maximal extractable value) risks are largely outside audit scope. A contract that executes swaps in the correct order might be exploited by a miner or sequencer who reorders transactions to profit from price slippage. The contract code is not vulnerable; the blockchain's transaction ordering is the problem.

## Audit Types and Their Limits

**Code review** audits rely on human expertise. A senior engineer reads the contract, runs local tests, and identifies patterns they recognize as risky. This is thorough and flexible but slow and depends on the auditor's experience. They may miss rare vulnerabilities or assume something is intentional when it is actually a bug.

**Formal verification** mathematically proves that a contract satisfies a specification—e.g., "balances never go negative," "only the owner can withdraw." This catches entire classes of bugs at once. But writing a correct specification is hard; if the spec misses a security property, formal verification certifies a flawed contract. Formal methods work best for well-defined financial contracts and are rarely used on complex DeFi protocols.

**Hybrid approaches** combine code review and automated analysis. The auditor runs static-analysis tools (like Slither or Mythril) to flag suspicious patterns, then manually investigates. This scales better than pure review but still misses design-level risks.

## How Audit Status Should Factor Into Risk

An audit is not a seal of absolute safety. It is a data point—a signal that the developers hired professionals to scrutinize the code and that common mistakes were addressed. But it does not account for:

- **Novel vulnerabilities**: Unknown attack classes are not caught by definition.
- **Systemic risk**: The contract may be safe in isolation but dangerous in the broader ecosystem.
- **Upgradeable contracts**: If the contract can be upgraded by a governance process or multisig, a past audit becomes stale immediately. New code is unaudited.
- **Dependencies**: The contract relies on other contracts (oracles, routers, lending protocols). Bugs in dependencies can cascade.

When evaluating a DeFi protocol, treat audit passing as table stakes, not proof of safety. Ask:

1. Is the audit recent (within the last year)?
2. Did the auditor actually run tests, or just review code?
3. Did the auditor review recent upgrades?
4. Are there known open issues or mitigations the team is tracking?
5. What is the governance model? Can the team upgrade without warning?
6. How much liquidity and user funds are at stake? Is the protocol systemic?

A small, audited contract with $1 million TVL and conservative governance is low-risk. A complex, audited mega-protocol with billions at stake and governance issues is high-risk, audit or not.

## The Cost of Relying Solely on Audit Status

Audits are valuable but incomplete. Users and investors who assume "audited = safe" often discover—too late—that an audited contract can still fail spectacularly. The [Ronin bridge exploit](/blockchain-fundamentals/) was not a code bug; it was a social engineering attack on key management. The [Wormhole hack](/blockchain-fundamentals/) involved a contract that had been reviewed multiple times but had a subtle logic error no reviewer caught.

An audit raises the bar for attack difficulty but does not make systems risk-free. The relationship is:

Risk = (probability of code bug × impact) + (probability of design flaw × impact) + (probability of operational failure × impact)

Audits address the first term. The second and third terms—which often dominate—remain untouched.

## See also

<div class="wiki-seealso">

### Closely related

- [Smart Contract](/smart-contract/) — code deployed to blockchains; the object being audited
- [Blockchain Fundamentals](/blockchain-fundamentals/) — how smart contracts fit into the broader system
- [Cryptocurrency Exchange](/cryptocurrency-exchange/) — where smart contract tokens trade; source of price-oracle risks
- [Distributed Ledger](/distributed-ledger/) — the infrastructure that executes smart contracts

### Wider context

- [Counterparty Risk](/counterparty-risk/) — the risk that another participant fails to perform
- [Execution Risk](/execution-risk/) — operational risks in deploying and maintaining systems
- [Systemic Risk](/systemic-risk/) — how contract failures can cascade across markets
- [Proof of Work](/proof-of-work/) — consensus mechanism; affects MEV and transaction ordering
- [Proof of Stake](/proof-of-stake/) — consensus mechanism; affects validator incentives and governance

</div>