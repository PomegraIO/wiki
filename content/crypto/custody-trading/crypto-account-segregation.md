---
title: "Client Asset Segregation in Crypto Custody"
description: "How crypto custodians segregate customer assets from house funds. Why it matters in insolvency and what protections it provides."
keywords:
  - crypto client asset segregation
  - segregated crypto accounts
  - digital asset custody segregation
  - client funds isolation
image: "/svg/crypto.svg"
---

*In crypto custody, **client asset segregation** means a custodian keeps customer assets completely separate from its own operational funds—typically in distinct wallets, accounts, or legal entities. If the custodian fails or is hacked, proper segregation means client crypto remains untouched and should be recoverable, even if the custodian's house funds are depleted.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Client Asset Segregation — key facts</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">The foundational defense against commingling and custodian insolvency.</div>

|   |   |
|---|---|
| **Purpose** | Isolate customer crypto from custodian's own funds |
| **Typical methods** | Separate wallets, sub-accounts, or legal entities per client |
| **Benefit in insolvency** | Customer assets are not subject to custodian's creditors |
| **Regulatory parallel** | Similar to securities custody rules (Investment Company Act of 1940) |
| **Weakness** | Relies on custodian honesty and robust accounting controls |
| **Insurance complement** | [Custodian insurance](/crypto-custodian-insurance/) covers breaches of segregation |
| **Custody standard** | Gold-standard custodians publish segregation policies |

</aside>

## The Segregation Problem in Crypto

Unlike traditional securities or cash, which are held by custodians subject to decades of regulatory oversight, crypto is new. Early in the industry, some platforms (notably FTX and BlockFi before their collapse) *commingled* customer funds with house funds—mixing them in a single wallet or account. This created a catastrophic risk: if the platform had a shortfall (whether from fraud, mismanagement, or theft), customer funds were instantly at risk. When FTX imploded in 2022, customers discovered billions in missing assets because the company had lent out customer crypto to insiders and other entities.

Proper segregation prevents this by enforcing a hard separation: customer assets live in one place, custodian house funds in another. If the custodian goes insolvent, customer assets are untouched.

## How Segregation Works in Practice

**Separate wallets** are the simplest method. A custodian might maintain:
- Client Wallet A (holding customer assets only)
- Client Wallet B (separate customers or different asset classes)
- House Wallet (custodian's operational funds and collateral)

Each wallet is controlled by distinct private keys or multi-signature schemes. When a customer deposits Bitcoin, it goes directly to their designated client wallet. When they withdraw, the custodian initiates a transaction from that wallet.

**Sub-accounts** on a blockchain work similarly but are more granular. Some custodians assign each customer a unique Ethereum address, and all that customer's ether sits at that address. The custodian controls the private key to a master wallet that can move funds but doesn't commingle them.

**Legal entity segregation** is more robust for very large custodians. Fidelity Digital Assets, for example, holds customer crypto in accounts maintained by a separate legal entity. This adds a layer of protection: even if Fidelity the parent company were to fail, the custodian entity—and the assets within it—would be legally separate.

**Multi-signature** (requiring multiple keys to move funds) is often layered on top. A client wallet might require signatures from both a custodian key and an independent auditor key, ensuring no single party can unilaterally move the funds.

## Segregation vs. Commingling

The opposite of segregation is **commingling**—mixing customer and house funds. This happens when:

1. A custodian lumps all customer deposits into a single hot wallet (internet-connected, for liquidity).
2. The custodian then lends some of that crypto to internal trading desks or external counterparties.
3. If the loan defaults or the custodian goes insolvent, there's no clear accounting of who owns what.

In the FTX case, the company maintained a single commingled fund and transferred customer assets to Alameda Research (FTX's affiliated trading firm). When Alameda made bad bets and lost billions, customer funds were gone. Full segregation would have made this impossible: Alameda could never have accessed customer wallets.

BlockFi, which collapsed in 2022, also had severe segregation failures. It lent customer crypto to 3 Arrows Capital, a hedge fund that defaulted, and customers were caught in the bankruptcy.

## The Insolvency Scenario

Segregation is most critical in insolvency. If a custodian fails, its assets go into bankruptcy court. Creditors line up to claim them: loan holders, employees owed wages, vendors, and shareholders.

If customer assets are segregated, they are *not part of the bankruptcy estate*. The bankruptcy trustee cannot touch them. They remain the property of the customers and should be returned in full.

If assets are commingled, they're part of the estate. Even if customer assets outnumber the shortfall, the bankruptcy process is slow and uncertain. Customers might recover 50 cents on the dollar years later.

This is why securities custodians (governed by the [Investment Company Act of 1940](/investment-company-act-of-1940/)) are required to segregate client securities. Crypto custodians follow the same logic, though regulatory requirements are still evolving.

## Regulatory Gaps and Risk Limits

The catch: crypto custody is not yet fully regulated in most jurisdictions. The [SEC](/securities-and-exchange-commission/) and CFTC have proposed rules, but there is no uniform federal standard for crypto segregation yet.

This means a custodian's segregation policy is only as strong as:
1. Its internal controls (accounting, auditing, key management)
2. Its [insurance](/crypto-custodian-insurance/) (if it fails, insurance pays claims)
3. The jurisdiction's bankruptcy law (if the custodian goes under, does crypto get treated like traditional securities?)

A custodian without published segregation standards and regular audits is a red flag. Trustworthy custodians (Fidelity Digital Assets, Kingdom Trust, Coinbase Custody) maintain independent audits confirming that segregation is real and enforced.

## How to Verify Segregation

If you're considering storing crypto with a custodian, ask:

1. **Does the custodian publish a segregation policy?** Good custodians clearly explain how they isolate client funds.
2. **Is the segregation independently audited?** Ask for audit reports or SOC 2 certifications confirming that segregation controls are in place.
3. **Who controls the private keys?** Understand the custody arrangement. Is it multi-sig? Does a third party hold a key?
4. **What happens if the custodian goes bankrupt?** Understand the legal structure. Are client assets held in a separate legal entity?
5. **Does it have [insurance](/crypto-custodian-insurance/)?** Insurance is a backstop if segregation fails.

A custodian ticking all five boxes offers strong protection against loss through commingling or insolvency.

## Segregation as Layers of Defense

Proper segregation is not a single mechanism; it's layered defense:

- **Layer 1 (Operational)**: Separate wallets and accounts ensure day-to-day funds are isolated.
- **Layer 2 (Legal)**: Clear contracts and company structure make customer assets legally distinct.
- **Layer 3 (Audit)**: Independent audits confirm that segregation actually exists.
- **Layer 4 (Insurance)**: [Custodian insurance](/crypto-custodian-insurance/) covers breaches or losses despite proper segregation.

If one layer fails, the others remain.

## Modern Crypto Custodians and Standards

The best institutional crypto custodians have adopted robust segregation standards. Coinbase Custody segregates each client's assets into its own account. Kingdom Trust uses a decentralized self-custody model where clients own their private keys (no segregation needed; no custodian risk). Fidelity Digital Assets segregates customer crypto into a separate legal entity and publishes third-party attestations.

These standards exist because the industry learned from early failures. Commingling is now understood as a critical risk, and custodians competing for institutional business must demonstrate segregation to survive.

## See also

<div class="wiki-seealso">

### Closely related

- [Crypto Custodian Insurance](/crypto-custodian-insurance/) — the financial backstop when segregation fails
- [Slippage in Crypto Trading Explained](/crypto-slippage-explained/) — a different custody-related cost
- [Maker-Taker Fee Structure on Crypto Exchanges](/crypto-fee-structures-maker-taker/) — how exchanges operate
- [Counterparty Risk](/counterparty-risk/) — the broader risk that a custodian will fail
- [Operational Risk](/operational-risk/) — control failures and process breakdowns
- [Liquidation](/liquidation/) — what happens when a custodian goes insolvent

### Wider context

- [Bitcoin](/bitcoin/) — the primary asset held in custody
- [Ethereum](/ethereum/) — second-largest held asset
- [Blockchain Fundamentals](/blockchain-fundamentals/) — how crypto is technically stored
- [Investment Company Act of 1940](/investment-company-act-of-1940/) — the regulatory model for segregation
- [Federal Deposit Insurance Corporation](/federal-deposit-insurance-corporation/) — traditional banking parallel

</div>
