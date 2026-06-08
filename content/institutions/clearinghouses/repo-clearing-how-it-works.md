---
title: "Repo Clearing: How Central Counterparties Clear Repurchase Agreements"
description: "Repo clearing how it works: central counterparties novate both legs of repurchase agreements, manage overnight rollover risk, and guarantee settlement in standardised terms."
keywords:
  - repo clearing how it works
  - central counterparty repo
  - overnight repo clearing mechanics
  - CCP novation repo
  - repurchase agreement settlement
image: "/svg/institutions.svg"
---

*Central counterparties (CCPs) clear **repurchase agreements** by inserting themselves as the counterparty to both sides of each repo transaction—a process called novation. This transforms an agreed bilateral trade into two standardised contracts against the CCP, eliminating counterparty credit risk but introducing operational complexity and overnight rollover mechanics unique to repo.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Repo Clearing — CCP novation</div>

<img src="/svg/institutions.svg" alt="An abstract editorial mark for financial institutions." />

<div class="wiki-infobox-caption">A CCP steps between both sides, guarantees both legs, and manages the uniquely short settlement cycle of repo.</div>

|   |   |
|---|---|
| **Novation** | CCP becomes counterparty to both seller and buyer |
| **Guarantee** | CCP backs all obligations; bilateral [counterparty risk](/counterparty-risk/) is eliminated |
| **Settlement** | Usually same-day or next-day; rarely longer |
| **Funding rate** | Overnight repo most common; rates reset daily |
| **Margin** | Initial and variation margin collected continuously |
| **Rollover risk** | Repo matures daily (or weekly/monthly); must be repriced and renewed |
| **Default management** | CCP liquidates collateral if member defaults |

</aside>

## The bilateral repo problem that clearing solves

Before central clearing became standard, two banks entered a repo—say, Bank A agrees to sell Treasury bonds to Bank B for $100 million, with the obligation to repurchase at a slightly higher price the next day. The contract is bilateral: if Bank B fails overnight and can't return the cash or securities, Bank A bears the loss. If Bank A fails before repurchasing, Bank B holds the bonds (now worth less due to credit fears) and faces a claim in the bankruptcy queue.

This [counterparty risk](/counterparty-risk/) was manageable when repo markets were small and mostly between strong banks. But as repo became the primary funding mechanism for dealers (trillions of dollars daily), the concentration of credit risk created systemic vulnerability. If one major dealer failed, repo counterparties faced cascade losses. The 2008 crisis exposed this starkly: when Lehman Brothers went insolvent, repo counterparties lost billions on unsecured positions and tied up collateral.

Central clearing was meant to solve this. A CCP—such as FICC (Fixed Income Clearing Corporation in the US) or LCH (in London)—interposes itself as the legal counterparty to every trade. The bilateral agreement is novated into two CCP contracts: one between Bank A and the CCP, one between Bank B and the CCP.

## How novation works

Novation is the legal substitution of the CCP for the original counterparty. The process is immediate and automatic (once both sides agree to clear):

1. Bank A and Bank B negotiate and agree on repo terms: 100 million Treasury bonds, 10 basis points interest, one day tenor.
2. Both submit the trade to the CCP.
3. The CCP becomes counterparty to both. Bank A now owes the CCP the cash and will buy back from the CCP; Bank B receives cash from the CCP and will deliver bonds to the CCP.
4. The original contract between Bank A and Bank B is cancelled and replaced by two CCP contracts.

From Bank A's perspective: "I sold bonds to the CCP for $100M and will buy them back for $100.001M tomorrow." From Bank B's perspective: "I bought bonds from the CCP for $100M and will sell them back tomorrow for $100.001M."

The CCP's job is to ensure both legs settle and both counterparties perform. If either fails, the CCP uses its guarantee fund and default-management procedures to make the other party whole.

## Why the CCP becomes creditworthy to both sides

The CCP is backed by:

**Default fund capital:** Member dealers (and sometimes the CCP itself) contribute capital to a guarantee fund. If a member defaults, this fund absorbs losses. For major CCPs like FICC, the default fund is many billions of dollars.

**Variation margin:** The CCP collects margin daily (or intra-day) from all members. If a repo dealer's position moves against them (e.g., bond prices rise, so the seller owes more in the repurchase), the dealer pays margin to the CCP. This keeps the CCP's exposure manageable.

**Mutualization:** All surviving members guarantee the default fund. If one member's $10 billion loss exceeds the fund, other members contribute. This creates strong incentives for members to police each other.

**Regulatory capital:** Central banks backstop major CCPs (the Federal Reserve can lend to FICC in extremis, though this is rare). Regulators treat CCP obligations as high-quality, allowing banks to hold them with low capital charges.

This structure makes the CCP creditworthy even if individual members fail—a key benefit to counterparties and to financial stability.

## Overnight rollover and term repo mechanics

Most cleared repo is overnight: it settles today, matures tomorrow, and the two counterparties reprice and renew the contract the next day. This creates a unique operational challenge: the repo must be continuously renewed.

Here's the flow for an overnight repo that rolls:

**Day 1 morning:** Bank A and Bank B agree on a 1-day repo at 5.10%. Trade is submitted to the CCP, novated, and settles same-day or next-morning.

**Day 2 morning:** The overnight repo matures. Bank B is obligated to return the bonds; Bank A must return the cash. But both parties typically agree to "roll" the repo—enter a new 1-day agreement at the new market rate (which might be 5.08%, 5.15%, or whatever the overnight rate is that morning).

**Rolling mechanics:** The CCP handles this as a continuation. The securities and cash pass from one counterparty to the other. Margin is recalculated at the new rate. No interruption.

The risk in rolling: overnight rates can spike. A dealer rolling repo might be forced to accept 6.50% instead of 5.10%. This is [refinancing risk](/refinancing-risk/). Large dealers manage it by rolling smaller pieces daily or using term repo (7-day, 28-day, etc.) to lock in rates for longer periods.

## Variation margin and daily repricing

Every day, the CCP reprices each repo contract based on the current market value of the collateral and the interest accrual. Suppose Bank A sold $100M of Treasury bonds to Bank B at 5.10% overnight. The next morning, bond prices rise, making the collateral worth $100.2M. Bank A now owes more in the repurchase (more collateral, same cash payment is a loss). The CCP collects variation margin from Bank A and pays it to Bank B, equalizing the position.

This happens continuously. Variation margin flows daily, sometimes intra-day, keeping the CCP's net exposure minimal. In a volatile market, a dealer can owe or receive millions in variation margin in a single day.

Dealers must manage margin reserves carefully. Running out of margin (failing to pay when due) triggers an event of default, and the CCP can close out the position and liquidate collateral. This is rare for major dealers but happened to smaller firms and repo counterparties in 2020 when volatility spiked during the pandemic.

## Collateral management in cleared repo

The CCP specifies which securities are eligible for each repo, often with "haircuts." A $100M package of US Treasuries might be valued at $99.5M (0.5% haircut); a $100M package of lower-grade corporate bonds might be valued at $97M (3% haircut). The haircut is the CCP's buffer against price moves.

The CCP also manages collateral chains. When Bank A delivers bonds to the CCP (as part of the repo), the CCP holds those bonds in trust and can re-use them. The CCP may simultaneously lend those bonds to Bank C in a different repo. This re-use of collateral is critical to the repo system's efficiency—securities flow through many transactions, not sitting idle.

But re-use creates operational risk: if the CCP fails to segregate collateral correctly, or if multiple claims arise against the same bonds, settlement breaks. Regulatory oversight of collateral management has become stricter post-2008, with emphasis on bankruptcy remoteness (collateral is protected from the CCP's creditors) and tri-party repo infrastructure.

## Default and management procedures

If a clearing member defaults (stops posting margin or misses settlement), the CCP enters default management:

1. **Immediately closes out the defaulter's positions:** The CCP auctions the repo contracts and collateral to other members or the market. This must happen fast—within hours—because repo is short-term and the market is tight.

2. **Uses the default fund:** If auction losses exceed the defaulter's skin in the game (capital contribution), the CCP draws from its guarantee fund. Remaining members absorb losses proportionally.

3. **Protects the non-defaulting side:** The CCP steps in as counterparty, ensuring the non-defaulting member receives what was owed (or funds equivalent to the loss).

This happened rarely but notably in 2001 when Enron defaulted; its energy derivatives cleared at another CCP, and the CCP's guarantee fund covered losses. CCPs have since improved their ability to quickly auction positions and execute default procedures.

## Why some repo stays bilateral (non-cleared)

Despite central clearing's benefits, significant repo volumes remain bilateral:

- **Customization:** Bilateral repo allows for tailored terms, collateral, and rates. Cleared repo is more standardised.
- **Small dealers and non-banks:** Some borrowers don't have CCP membership or pre-arranged credit lines. They do bilateral repo with large dealers who absorb counterparty risk (and charge a premium).
- **Repo funding arrangements:** Some dealers run internal repo networks with subsidiary companies or clients, accepting bilateral exposure to manage liquidity.

Regulators have pushed for more central clearing but stop short of mandating it for all repo, recognizing the value of flexibility for certain participants.

## See also

<div class="wiki-seealso">

### Closely related

- [Repurchase agreement](/repurchase-agreement/) — the fundamental contract
- [Counterparty risk](/counterparty-risk/) — what central clearing eliminates
- Central counterparty — the institution behind clearing
- [Variation margin](/variation-margin/) — daily repricing in cleared contracts
- [Refinancing risk](/refinancing-risk/) — the exposure in rolling overnight repo

### Wider context

- Repo market — the broader system and infrastructure
- Collateral management — managing securities in clearing
- [Tri-party repo](/tri-party-repo/) — a specific clearing structure
- Default procedures — how CCPs handle member failure
- [Systemic risk](/systemic-risk/) — how clearing reduces contagion

</div>
