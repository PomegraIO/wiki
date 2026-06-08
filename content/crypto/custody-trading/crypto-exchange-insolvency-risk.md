---
title: "Exchange Insolvency Risk in Crypto"
description: "Understand what happens to your crypto if an exchange goes bankrupt, what legal protections apply, and how to reduce custody and counterparty risk."
keywords:
  - exchange insolvency risk crypto
  - what happens to crypto if exchange goes bankrupt
  - crypto exchange bankruptcy
  - counterparty risk
  - custodial risk crypto
image: /svg/crypto.svg
---

*When a cryptocurrency exchange becomes insolvent, customer funds are often lost because they are held as the exchange's property, not as segregated customer assets. Some jurisdictions offer limited legal remedies, but the harsh reality is that insurance and refunds are rare and customers are typically unsecured creditors.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Exchange Insolvency — key facts</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">A concentration of risk that depends on jurisdiction, insurance, and the exchange's actual asset reserves.</div>

|   |   |
|---|---|
| **Primary risk** | Exchange holds your funds; if insolvent, they're lost |
| **Legal status** | Most jurisdictions treat crypto deposits as unsecured claims on the exchange |
| **Insurance coverage** | Rare; most exchanges offer no FDIC-equivalent protection |
| **Bankruptcy timeline** | Years of litigation before any creditor recovery |
| **Recovery rate** | Often 0%; historical cases suggest 5–50% for privileged claimants |
| **Mitigation** | Self-custody, holding stablecoins off-exchange, or using segregated solutions |

</aside>

## Why exchange insolvency is different from bank failure

In traditional banking, deposits are protected by government insurance (FDIC in the U.S., equivalent schemes in other countries). When a bank fails, the government steps in, the insured deposits are made whole, and the insolvency is resolved within months.

Cryptocurrency exchanges operate in a near-total regulatory vacuum in most jurisdictions. There is no FDIC equivalent, no mandatory insurance, and no government backstop. When an exchange becomes insolvent, customer funds are treated as unsecured claims against the exchange's estate. In bankruptcy law, unsecured creditors are last in line, after employees, taxes, and secured creditors. Recovery rates are often zero.

Worse, the bankruptcy process itself is slow. Liquidation of crypto assets held by an insolvent exchange—if they can be located—may take years. During that time, the assets' value may fluctuate wildly. By the time bankruptcy is resolved, Bitcoin may have moved from $60,000 to $15,000, wiping out recovery.

## What happens during exchange bankruptcy

When an exchange announces insolvency or shuts down operations, customer funds are frozen. You cannot withdraw your coins or cash. The exchange may claim to be investigating, restoring service, or implementing a recovery plan, but in most cases, the funds are either stolen (via hack or mismanagement), intentionally misappropriated, or irretrievably lost.

Creditors—customers who had funds on the exchange—file claims in bankruptcy court. The court appoints a trustee or receiver, who attempts to locate and liquidate any remaining assets. The exchange's operational assets (servers, code, intellectual property) are auctioned. But rarely are the cryptocurrency holdings recovered in full.

The bankruptcy proceedings are governed by the laws of the jurisdiction where the exchange was incorporated. An exchange incorporated in Japan is subject to Japanese bankruptcy law. An exchange incorporated in the Cayman Islands or Malta is subject to those jurisdictions' laws. Customers worldwide may become claimants against that single bankruptcy proceeding, competing for limited recovery.

## Regulatory status and custody rules

In the U.S., the SEC treats many crypto assets as securities. Exchanges that trade securities must be registered as broker-dealers and are subject to SEC Rule 15c3-3, which requires them to segregate customer assets and maintain minimum net capital. In theory, this protects customers. In practice, enforcement is limited and many major exchanges trade unregistered assets (altcoins) with no SEC oversight.

Some jurisdictions (Malta, Singapore, Switzerland) have implemented licensing frameworks for crypto exchanges and require segregation of customer assets. But even in those jurisdictions, segregation requirements are often weak or poorly enforced.

Japan's Financial Instruments and Exchange Act (FIEA) requires exchanges to be licensed and maintain segregated customer assets. Yet Coincheck (a major Japanese exchange) suffered a hack in 2018 that lost user funds, and while the exchange was later acquired and customers were partially compensated, the legal process took years.

The reality: most exchanges are not legally required to segregate customer assets, and even where requirements exist, enforcement and proof of compliance are minimal.

## The FTX precedent

FTX's collapse in November 2022 offers a case study. FTX held approximately $8 billion in customer funds. The founder and CEO secretly transferred these funds to Alameda Research (a trading firm also owned by FTX's founder) to cover losses. When FTX couldn't cover withdrawals, it collapsed.

Months of bankruptcy proceedings followed. The bankruptcy court appointed a trustee who struggled to locate assets. Some customer assets were eventually recovered (tens of billions in assets were found, though their value relative to customer claims was small). But the process revealed that FTX had no real segregation, no real insurance, and no governance preventing the founder from using customer funds as he wished.

Customers with significant balances in FTX at the time of collapse faced years without access to their funds and ultimately recovered only a fraction. The exchange had been valued at $32 billion (during fundraising) but was insolvent at the time of collapse. The bankruptcy could extend years.

## Insurance claims and recovery

Some exchanges claim to offer insurance or customer protection. Coinbase, for instance, holds the majority of user funds in offline storage with insurance coverage (though the specific policy terms limit coverage to certain asset types and amounts). But this insurance is provided by the exchange, not a government guarantor. If the exchange itself fails, the insurance may not cover the insolvency.

A small number of platforms use third-party custody solutions where assets are held by a separate, regulated custodian (a bank or specialized crypto custody firm). In this model, the exchange acts as a broker, and the custodian holds assets in segregated accounts. If the exchange fails, the custodian's assets are not affected. This is true custody separation and is a genuine risk reduction.

However, most retail-focused exchanges do not use true custody separation. They hold assets directly on their own balance sheet, meaning all counterparty risk falls on the exchange's solvency.

## Counterparty risk and mitigation

Leaving funds on an exchange creates counterparty risk: you depend on the exchange's honesty, competence, and solvency. That risk can be reduced in several ways.

**Self-custody**: Withdraw your crypto to a wallet you control (via a [seed phrase](/seed-phrase-security/) or hardware wallet). You now depend only on your own security, not the exchange's. This eliminates counterparty risk entirely but requires you to manage your own keys.

**Segregated custody**: Use an exchange or platform that employs a third-party custodian. Verify in the terms that assets are held by the custodian, not the exchange. Ask for proof of segregation (independent audit reports are sometimes published).

**Diversification**: Don't keep all assets on one exchange. Distribute across platforms to limit the damage if one fails. But this increases operational complexity.

**Stablecoin holdings**: If you hold dollars or stablecoins on an exchange, consider whether the stablecoin issuer is solvent. USDC and USDT are not covered by insurance; they're only as safe as the issuer's reserves. Tether (USDT) has faced audits and skepticism; USDC (from Coinbase-backed Circle) has published regular attestations. Holding either on an insolvent exchange means your dollars are frozen along with your crypto.

## Clawback risk

In a few cases, bankruptcy courts have ordered clawback—reversing transactions from the time before the bankruptcy was announced. Customers who withdrew funds days before the exchange collapsed were forced to return those funds to the bankruptcy estate to be distributed equally to all creditors. This happened with MtGox, where early winners who withdrew funds were forced to return them.

The implication: withdrawing funds from a failing exchange shortly before its collapse may not protect you if the withdrawal is later reversed by a court.

## No guaranteed recovery

The blunt truth is that there is no guarantee of recovery when a crypto exchange becomes insolvent. Unlike banks, exchanges have no deposit insurance. Unlike brokerages (in the U.S.), customer assets are not segregated or protected by SIPC. The customer is an unsecured creditor with minimal legal standing.

Recovery requires:
1. The bankruptcy court to locate and liquidate exchange assets.
2. Those assets to yield significant proceeds (not guaranteed; they may be fully stolen or impaired).
3. The recovery to occur while the asset price remains favorable (years of price depreciation can wipe out recovery value).
4. You to navigate the bankruptcy process (often requiring lawyers and sustained engagement).

Most customers who leave significant funds on an insolvent exchange never recover them.

## See also

<div class="wiki-seealso">

### Closely related

- [Counterparty Risk](/counterparty-risk/) — the core risk that an exchange insolvency embodies
- [Seed Phrase Security](/seed-phrase-security/) — how to avoid exchange risk entirely via self-custody
- [Cryptocurrency Exchange](/cryptocurrency-exchange/) — the platforms where insolvency risk arises
- [Distributed Ledger](/distributed-ledger/) — the technology that enables true self-custody
- [Custodian](/custodian/) — third-party custody as an alternative to exchange-held assets

### Wider context

- [Bitcoin](/bitcoin/) — the original asset and why self-custody became philosophically important
- [Ethereum](/ethereum/) — major asset often held on exchanges despite custody risks
- [Credit Risk](/credit-risk/) — the financial concept underlying exchange insolvency
- Bankruptcy — the legal process that applies when exchanges fail

</div>
