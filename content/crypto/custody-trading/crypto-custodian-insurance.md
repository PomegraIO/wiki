---
title: "Crypto Custodian Insurance"
description: "What crypto custodian insurance coverage protects—and what it doesn't. Learn how policies handle hacks, theft, and operational losses."
keywords:
  - crypto custodian insurance coverage
  - digital asset custody insurance
  - institutional crypto insurance
  - crypto wallet insurance
image: "/svg/crypto.svg"
---

*A **crypto custodian insurance** policy protects a digital asset custodian—and often its clients—against losses from hacking, internal fraud, and operational errors, but only within strict limits. Understanding which types of loss are covered, and which are excluded, is essential for anyone relying on a custodian to hold crypto.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Crypto Custodian Insurance — key facts</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Insurance protection for institutional digital asset custody comes with narrow carve-outs.</div>

|   |   |
|---|---|
| **Typical coverage** | Hot-wallet hacks, employee theft, transaction errors |
| **Common exclusions** | Counterparty default, protocol exploits, fraud by custodian itself |
| **Policy limit** | Usually $100M to $1B+ per incident for large custodians |
| **Covered parties** | Custodian, and often its clients (depends on endorsement) |
| **Industry standard** | Fidelity, Coinbase Custody, Kingdom Trust, others; Lloyd's syndicates |
| **Claim process** | Formal notice, investigation, usually 30–90 days |

</aside>

## Why Crypto Custody Needs Insurance

Crypto custody is fundamentally different from traditional securities custody. A custodian holds the private keys or has authority over wallets containing billions of dollars in assets. If those keys are compromised—whether by outside hackers or rogue employees—the loss is permanent and irreversible. Unlike a stolen stock certificate, which can be voided and reissued, stolen crypto cannot be recovered through normal legal channels.

Insurance emerged to bridge this gap. Institutional custodians (such as [Fidelity](https://www.fidelity.com), Coinbase Custody, Kingdom Trust, and others) carry policies specifically designed for digital asset loss. These policies are underwritten by traditional insurance syndicates, often through Lloyd's of London, which bring decades of risk assessment to a young asset class.

For a large institution or fund holding significant crypto, custody insurance is table stakes. It reassures depositors that if the unthinkable happens, their assets are protected—at least up to the policy limits.

## What's Covered: Hacking and Theft

**Hacking losses** are the core coverage area. If a sophisticated attacker breaches the custodian's hot wallet (the internet-connected reserves used for liquidity) and drains funds, the insurance policy typically covers the loss. This includes both the initial intrusion and the subsequent theft of assets.

**Employee theft and fraud** is similarly covered. If a custodian employee steals private keys or uses them to move client assets, the insurance pays out. This has real teeth: several early crypto custody incidents involved employees attempting to move funds, and insurers paid claims.

**Operational errors** are also insurable events. If a custodian accidentally sends assets to the wrong address, or double-disburses funds due to a system glitch, that loss is generally covered under the "errors and omissions" portion of the policy.

**Key loss and destruction** (if the custodian's backups and redundancy fail and private keys are irrecoverably lost) may be covered, though terms vary widely. Some policies explicitly exclude this; others cover it only if it results from a defined peril like fire or flood.

## What's Usually *Not* Covered

Insurance coverage has firm boundaries, and understanding them is critical.

**Market losses** are never covered. If the price of Bitcoin drops 50% while held in custody, insurance doesn't compensate for it. The custodian is responsible for safekeeping, not performance.

**Counterparty risk** sits in a gray zone. If the custodian uses a third-party hot-wallet provider or clearing house, and that provider fails, the original custodian's insurance may not cover the loss—especially if the custodian failed to conduct due diligence on that counterparty. This is why many large custodians maintain wholly owned hot-wallet infrastructure.

**Protocol exploits and smart-contract losses** are typically not covered. If a custodian incorrectly implements a [blockchain-fundamentals](/blockchain-fundamentals/) protocol or stores assets in a buggy smart contract, and an attacker exploits it, that's a business risk, not an insured peril. Insurance applies to theft and loss, not to operational misuse of the chain itself.

**Fraud by the custodian itself** is excluded. If the custodian lies about holdings or misappropriates assets in a way that falls outside "employee theft," insurance won't cover it—and the client has no recourse except through litigation and potential bankruptcy of the custodian.

**Regulatory seizure and legal disputes** are not covered. If a government freezes assets, or a court orders the custodian to surrender funds in a lawsuit, the loss falls on the client, not the insurer.

**Insider trading or market abuse losses** are excluded. If a custodian's employee trades on inside information or manipulates markets, and the client is sued, the custodian's fidelity insurance does not apply.

## Coverage Limits and Endorsements

Policies typically cap coverage at a specific amount per incident—often $100M to $1B for well-capitalized custodians, though that ceiling varies. A large fund with $5B in assets may need an umbrella or excess policy to cover losses beyond the base policy's limit.

**Endorsements matter.** Some policies cover only the custodian itself (the direct victim of loss), while others extend protection to the clients of the custodian through an "clients as named insureds" or similar rider. This is crucial: if client assets are stolen but the custodian's coverage excludes clients, the client has to sue the custodian—and if the custodian is insolvent, they recover nothing from insurance.

## The Investigation and Claim Process

When a loss occurs, the insured custodian must notify the insurer within a defined window—usually 30 days. The insurer then investigates the loss to confirm it falls within coverage. This can take 6–12 weeks for complex incidents.

For a hack, the investigation typically involves:
- Forensic analysis of the breach chain
- Verification that the custodian did not negligently fail in security duty (insurers will deny claims if gross negligence is found)
- Confirmation of the loss amount and timing

Disagreements over causation are common. If a hack succeeded because the custodian skipped a security update, the insurer may deny the claim as resulting from negligence rather than an unforeseeable attack.

## How Insurance Relates to Asset Segregation

Custodian insurance is distinct from [crypto-account-segregation](/crypto-account-segregation/). Asset segregation means the custodian holds client assets separately from its own house funds—usually in a distinct wallet or through a legal structure. Insurance is the financial backstop *if* segregation fails or is breached.

A custodian with both strong segregation *and* robust insurance is the gold standard. Segregation prevents the loss in the first place; insurance pays if segregation is compromised.

## Practical Limits of Coverage

Insurance cannot cover all risks in crypto custody. It works well for discrete, sudden events (a hack on a specific date) but poorly for slow erosion of value, commingling, or fraud that occurs over months. It also depends entirely on the custodian's diligence in maintaining records and proving causation.

For clients, this means vetting not just whether a custodian *has* insurance, but reading the policy schedule, understanding the exclusions, and confirming that coverage extends to them as named insureds. A custodian with a $500M policy cap is a poor choice for a $2B fund.

## See also

<div class="wiki-seealso">

### Closely related

- [Client Asset Segregation in Crypto Custody](/crypto-account-segregation/) — how custodians isolate customer crypto from house funds
- [Slippage in Crypto Trading Explained](/crypto-slippage-explained/) — understanding price impact when trading
- [Maker-Taker Fee Structure on Crypto Exchanges](/crypto-fee-structures-maker-taker/) — why liquidity providers pay differently
- [Counterparty Risk](/counterparty-risk/) — risk of the other party in a transaction failing
- [Operational Risk](/operational-risk/) — losses from failed processes or systems
- [Cybersecurity and Digital Asset Management](/blockchain-fundamentals/) — foundations of secure custody

### Wider context

- [Bitcoin](/bitcoin/) — the largest cryptocurrency by market cap
- [Ethereum](/ethereum/) — the leading smart-contract platform
- [Hedge Fund](/hedge-fund/) — institutions that may hold crypto
- [Credit Risk](/credit-risk/) — general principles of counterparty reliability
- [Liquidation](/liquidation/) — what happens when a custodian or fund fails

</div>
