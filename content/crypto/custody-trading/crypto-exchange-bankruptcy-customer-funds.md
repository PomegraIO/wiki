---
title: "What Happens to Customer Funds in a Crypto Exchange Bankruptcy"
description: "Learn what happens to customer cryptocurrency funds if an exchange goes bankrupt, including how bankruptcy law treats balances and recovery prospects."
keywords:
  - what happens to crypto funds if exchange goes bankrupt
  - crypto exchange bankruptcy
  - customer funds recovery
  - cryptocurrency custody risk
  - exchange default
image: "/svg/crypto.svg"
---

*When a centralized cryptocurrency exchange declares bankruptcy, the fate of customer funds hinges on two questions: Did the exchange hold the private keys (and thus true custody), or did it remain a custodian in name only? Is the exchange incorporated in a jurisdiction with clear bankruptcy law, or in a regulatory gray zone? The harsh answer from recent collapses—FTX, Genesis, Celsius—is that most customers rank as unsecured creditors, behind derivatives counterparties and insiders, with recovery prospects ranging from low to zero.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Crypto Exchange Bankruptcy — customer fund recovery</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for cryptocurrency." />

<div class="wiki-infobox-caption">Bankruptcy law treats crypto balances like unsecured claims, with low priority and uncertain payoff.</div>

|   |   |
|---|---|
| **Customer status** | Unsecured creditor (in most cases) |
| **Recovery timing** | Years of litigation; bankruptcy court discretion |
| **Recovery rate** | Wide range: 0–10% reported in major cases (varies by exchange) |
| **Priority order** | Secured lenders > employees > operators' insiders > customers |
| **Private key custody** | If exchange holds keys, funds are bankruptcy assets; if custodian holds, unclear |
| **Insurance** | No FDIC or SIPC equivalent for crypto |
| **Precedent cases** | FTX (filing 2022), Genesis (filing 2023), Celsius (filing 2022) |
| **Preventive custody** | Self-custody (cold wallet) eliminates bankruptcy risk entirely |

</aside>

## The custody problem: exchange as broker or custodian?

Most centralized exchanges operate as **brokers**, not custodians in the legal sense. When you deposit bitcoin to a trading account on an exchange, the exchange's legal terms state that it has discretion over those funds and can lend, hypothecate, or re-pledge them. You do not own the private keys; the exchange does. This is economically different from a bank holding your deposits, which by law must segregate and return customer funds on demand.

In traditional finance, this risk is mitigated by regulation and insurance. A brokerage holding customer securities is required by law (in the U.S., under Securities and Exchange Commission rules) to segregate customer assets and carry fidelity insurance. If the broker fails, the Securities Investor Protection Corporation (SIPC) guarantees up to $500,000 per customer account. Crypto exchanges have no parallel protection. Most jurisdictions do not require exchanges to segregate customer crypto or carry insurance. The exchange's private keys are co-mingled with operational capital, and when the exchange fails, customers discover they are unsecured creditors in a bankruptcy liquidation, not protected account holders.

## The bankruptcy process for centralized exchanges

When a major exchange declares bankruptcy (as FTX did in November 2022), it typically files for Chapter 11 in the U.S. (or equivalent insolvency procedures in other countries). Here is what unfolds:

**1. Filing and automatic stay**: The exchange files for protection and enters an automatic stay, freezing all customer withdrawals. Accounts are locked. Customers cannot access their balances, even to move them elsewhere.

**2. Asset discovery**: The bankruptcy trustee (court-appointed or debtor-in-possession) attempts to locate and inventory all assets. If the exchange kept private keys in cold storage or custody accounts, the trustee may gain access. If the keys are lost or held by co-founders who have disappeared (as in some cases), the assets are unrecoverable.

**3. Claim filing**: Customers submit proof of their balances—screenshots, email statements, blockchain records—to the court. The exchange contests or acknowledges each claim. Disputes can drag on for years.

**4. Creditor hierarchy**: U.S. bankruptcy code imposes a strict priority order:
   - **Secured claims** (liens, collateral): these are paid first.
   - **Administrative expenses and professional fees**: trustee, lawyers, accountants eat into the estate.
   - **Employee wages** (up to a cap).
   - **Customer deposits** (in traditional finance; not clearly defined for crypto).
   - **Unsecured creditors**: everyone else, including most customers.
   - **Equity holders and insiders**: last.

Crypto customers typically fall into the unsecured creditor category, behind secured lenders. FTX borrowed heavily from Alameda Research and other counterparties; those secured lenders had claims senior to customer deposits. Genesis Global Capital loaned crypto to 3AC and others; when those counterparties failed, Genesis' exposure was senior to customer withdrawals.

**5. Distribution**: If any assets remain after professional fees and secured creditors, they are distributed pro rata to unsecured creditors. The distribution is often less than 10% of claimed balances. It takes years.

## The FTX precedent

FTX filed for bankruptcy on 8 November 2022 with an estimated $8 billion shortfall in customer funds. Analysis later revealed that FTX founders Sam Bankman-Fried and Gary Wang had moved customer deposits into Alameda Research, a trading arm they owned, and Alameda had lost those funds in risky trading, loans to third parties, and payments to celebrities and political candidates.

As of mid-2024, FTX's bankruptcy estate recovered some assets and received a substantial cash offer from potential buyers. Early estimates suggested customers might recover 10–20% of their claims, far below the 100% return of traditional bank deposits. The recovery process is ongoing, and the timeline is measured in years. Additionally, Bankman-Fried faced criminal charges for wire fraud and conspiracy, adding uncertainty about whether any restitution would reach customer claimants.

The FTX collapse illustrates a critical vulnerability: centralized exchanges that claim to be custodians often lack meaningful oversight. Audits are sparse or non-existent. Private keys are held by operators with few checks. When founder incentives flip toward risk-taking or fraud, customer funds are defenseless.

## Genesis and Celsius: the lending-default cascade

Genesis Global Capital filed for bankruptcy in January 2023 after its parent (DCG) incurred massive losses in the 3AC collapse and Genesis made unsecured loans to Alameda. Celsius Network, a "crypto bank" offering high-yield deposits, filed in July 2022 after realizing its loans to 3AC were nearly worthless and it had lent out 80% of customer funds without adequate collateral.

In both cases, customers who thought they were earning yield on deposits discovered they were de facto venture capital investors in a failed lending operation. When the loans defaulted, there were no assets to return. Customers ranked as unsecured creditors and faced years of litigation over what remained.

The lesson: high-yield promises on crypto deposits are red flags. If an exchange or "bank" guarantees 10% annual returns on deposits, it is making aggressive bets with your funds. When those bets fail, you become a creditor in bankruptcy, not a protected depositor.

## The jurisdiction gamble

The bankruptcy treatment of crypto is clearer in the U.S. than in many other countries. U.S. bankruptcy law is transparent and predictable, even if the outcome is unfavorable. In contrast, exchanges incorporated in the Bahamas (FTX), Singapore (some regional exchanges), or other lightly regulated jurisdictions face murky legal frameworks. A Bahamian exchange's failure might not trigger formal bankruptcy; it could simply disappear, and customers have no legal recourse at all.

This jurisdictional arbitrage was one reason FTX chose the Bahamas. Regulators there were more permissive, and if the exchange failed, customers had few remedies. (In reality, FTX filed for U.S. bankruptcy once it became clear the game was up, but the initial jurisdiction choice was deliberate.)

For customers, the implication is stark: an exchange incorporated in a common-law jurisdiction with transparent insolvency law is safer than one in a regulatory black hole, even if neither offers deposit insurance.

## The private key question

A critical but often overlooked detail: **who holds the private keys?** If the exchange is merely the operator of a web interface but uses a licensed custodian (such as Fidelity Digital Assets or Kingdom Trust) to hold the actual private keys, then those funds are segregated. The custodian's failure would not affect customer funds. Conversely, if the exchange holds the keys, they are bankruptcy assets—and if the keys are lost or co-mingled with operational funds, customers' recovery is hindered.

Most centralized exchanges hold their own keys (or hold them with third-party custodians but still maintain access). This gives the exchange maximum operational flexibility but maximum risk to customers. A few platforms, such as some staking services, use third-party custody to reduce this risk, but this is uncommon in trading exchanges.

## Self-custody as the definitive hedge

The ultimate protection is **self-custody**—holding private keys in a personal wallet (hardware wallet, cold storage, or multisig arrangement). If you hold your own keys, you are not a customer of any exchange. You are not exposed to the exchange's credit risk, operational risk, or founder fraud. Your funds can only be lost if you lose or compromise the keys yourself. This is why experienced crypto investors keep the majority of holdings in self-custody and use exchanges only for active trading or yield-seeking (which inherently carries counterparty risk).

For most users, however, self-custody is burdensome. It requires technical competence, secure key backup, and discipline. Many users opt for the convenience of exchange custody despite the risk—and when the exchange fails, they discover that convenience was not worth it.

## The legal and regulatory trajectory

As of 2025, several jurisdictions are tightening crypto exchange regulation. The EU's Markets in Crypto Regulation (MiCR) and the U.S. SEC's proposed rules would impose custody segregation and insurance requirements similar to traditional brokerages. The UK's Financial Conduct Authority has banned unregulated derivatives trading on crypto exchanges. These moves are meant to reduce the bankruptcy risk to customers by forcing exchanges to behave more like traditional custodians.

However, enforcement is uneven. Many exchanges remain unregulated or lightly regulated in their home jurisdictions, and they resist custody and insurance rules as costly. Until regulation is global and uniform, the risk asymmetry persists: exchanges in developed markets face pressure to segregate and insure; exchanges in light-touch jurisdictions do not.

## See also

<div class="wiki-seealso">

### Closely related

- [Cryptocurrency exchange](/cryptocurrency-exchange/) — the platform structure and operational role
- [Custodian](/custodian/) — third-party holding of financial assets; the crypto parallel is nascent
- [Counterparty risk](/counterparty-risk/) — the credit exposure you carry when depositing funds with an exchange
- Private key — cryptographic control of crypto assets; self-custody requires holding these
- Secured creditor — the bankruptcy priority above unsecured customers

### Wider context

- Bankruptcy — the legal process and creditor hierarchy
- Cryptocurrency regulation — evolving custody and insurance standards
- [Systemic risk](/systemic-risk/) — interconnectedness of crypto lending markets
- [Credit risk](/credit-risk/) — the broader framework for assessing counterparty default

</div>
