---
title: "Euroclear"
description: "A European post-trade settlement and central securities depository system that clears and settles bond, stock, and derivative transactions across European markets."
keywords:
  - euroclear
  - settlement
  - clearinghouse
  - securities depository
---

*Euroclear is Europe's largest post-trade infrastructure operator, providing [settlement](/wiki/settlement-cycles/), [custody](/wiki/custodian/), and central depository services for securities traded on European exchanges and beyond. It is the settlement counterparty for trillions of euros in transactions daily, including bonds, equities, repos, and [derivatives](/wiki/derivative-accounting-hedging/). Euroclear acts as a central counterparty, assuming credit risk between buyer and seller, and reducing settlement risk.*

<aside class="wiki-infobox">

| Key Fact | Detail |
|---|---|
| **Headquarters** | Brussels, Belgium |
| **Founded** | 1968 (as a depository); evolved into current form in 2000 |
| **Daily settlement value** | ~€500–700 billion |
| **Coverage** | Pan-European equities, bonds, repos, derivatives |
| **Settlement model** | Delivery-versus-payment (DVP) |
| **Regulatory oversight** | ECB (European Central Bank) and national regulators |
| **Competitors** | Clearstream (DTCC subsidiary), national depositories (Intergovernmental) |

</aside>

## The role of a central depository

Before modern clearinghouses, when a buyer purchased 10,000 shares of a stock, the seller had to physically deliver the share certificates, and the buyer had to physically deliver cash. This took weeks and created massive operational risk—certificates could be lost, cash might not arrive, or one party might renege. The central depository solved this by holding all securities in "immobilized" (centralized) form.

Euroclear holds securities on behalf of participating institutions (banks, brokers, investors). When a buyer purchases shares on the Euroclear system, they don't receive a physical certificate; instead, Euroclear transfers book-entry ownership from the seller's account to the buyer's account. Cash and securities move simultaneously (delivery-versus-payment), eliminating the "Herstatt risk" (settlement risk) that plagued earlier systems.

## How Euroclear settles a trade

1. **T (trade date)**: A buy-side firm (a pension fund) instructs its custodian bank to purchase 5 million euros of a German government [bond](/wiki/bond/). The custodian executes the trade on the Eurex exchange.

2. **T+0 to T+1 (settlement window, typically next business day)**: The custodian sends settlement instructions to Euroclear, confirming the amount, price, counterparty, and settlement date. Euroclear matches the instruction with the seller's instruction (the sell-side institution's instruction).

3. **Settlement (T+1 or T+2 depending on asset)**: Euroclear verifies that:
   - The buyer has sufficient cash (or credit line) available.
   - The seller has sufficient securities available.
   - Both parties' settlement accounts are in good standing.

   If all checks pass, Euroclear executes a DVP trade: it transfers the bond from the seller's Euroclear account to the buyer's account and simultaneously transfers cash from the buyer's settlement bank to the seller's.

4. **T+2 to T+3**: Final confirmation. Cash is delivered to the seller's settlement bank; the bond is fully transferred.

Throughout this process, Euroclear bears the credit risk. If the buyer's settlement bank fails to deliver cash, Euroclear's guarantee fund covers the bond seller. If the seller fails to deliver the bond, Euroclear has access to emergency borrowing and securities. This protection is why Euroclear is considered systemically important to European financial markets.

## Custody and asset servicing

Beyond settlement, Euroclear provides **custody services**—safekeeping of securities on behalf of institutions. A US pension fund holding European securities might not want to store certificates in Brussels; instead, it instructs its global custodian (e.g., JPMorgan) to maintain custody at Euroclear. Euroclear:

- Holds the securities in immobilized form.
- Collects dividends and [coupon payments](/wiki/coupon-payment/).
- Manages corporate actions (splits, mergers, spin-offs).
- Provides daily statements and reporting.

Custody fees typically run 1–3 basis points annually of assets under custody, generating significant revenue.

## Repo and collateral management

Euroclear also operates a major **repo (repurchase agreement) settlement platform**. A bank borrows cash and pledges a [bond](/wiki/bond/) as collateral. The bank must deliver the bond to the repo counterparty (or Euroclear, if it's a tri-party repo), receive cash, and later repurchase the bond at a slightly higher price to repay the loan and interest.

Euroclear's tri-party repo service is critical for short-term funding in Europe. A bank needing overnight cash pledges collateral to Euroclear, which finds a counterparty (another bank with excess liquidity). Euroclear verifies the collateral's value, ensures it meets haircut requirements, and manages the daily mark-to-market and collateral substitution. On tri-party deals, neither party needs to manage the collateral directly—Euroclear does it.

## Interoperability and links to other systems

Euroclear does not operate in isolation. It maintains links with:

- **National Central Depositories** (NCDs): Each EU member state has a national securities register (e.g., Spain's IBERCLEAR, Italy's Monte Titoli). Euroclear connects to these, allowing cross-border settlement.

- **Other international depositories**: Euroclear has links to Clearstream (the DTCC's European arm), the Federal Reserve's settlement systems, and other global CSDs (Central Securities Depositories).

- **Target2-Securities (T2S)**: A shared settlement platform led by the ECB, designed to integrate all European settlement systems. As of 2025, most European CSDs have migrated to T2S, though Euroclear remains a major node.

## Ownership and governance

Euroclear is owned by users (financial institutions) and currently traded as **Euroclear Group N.V.** on Euronext Brussels. Its governance structure balances shareholder returns with its role as market infrastructure. The board includes representatives from major users, ensuring that decisions reflect the needs of the financial system.

The ECB and other central banks regulate Euroclear under the CSDR (Central Securities Depository Regulation), enforcing standards for:

- Operational resilience (uptime, cybersecurity, business continuity).
- [Counterparty risk](/wiki/counterparty-credit-risk/) management (guarantee funds, haircut policies).
- Transparency and fair access.

## Market impact and systemic importance

Euroclear is systemically critical: if it fails or is shut down, European capital markets would seize up. Governments and central banks treat it as such. During the 2008 financial crisis, when credit markets froze, Euroclear's guarantee fund was critical in maintaining settlement finality and preventing cascading defaults.

In 2022, when Russia invaded Ukraine and Western sanctions froze Russian financial assets, Euroclear became a battleground: Russian entities tried to access securities held in Euroclear, while sanctions blocked settlement. Euroclear had to navigate political pressure, legal obligations, and operational constraints—illustrating its role as both market infrastructure and political actor.

## Fees and economics

Euroclear generates revenue from:

- **Settlement fees**: €0.10–1.00 per trade depending on asset type and size.
- **Custody fees**: 1–3 basis points annually of assets held.
- **Repo fees**: 0.5–2 basis points annually of borrowing.
- **Cash service fees**: Spreads on [cash](/wiki/cash-basis-accounting/) transfers and credit lines.

With ~€30 trillion in assets under custody and billions of daily transactions, Euroclear is a highly profitable utility.

<div class="wiki-seealso">

### Closely related
- [Settlement Cycles](/wiki/settlement-cycles/) — The T+1/T+2 timing Euroclear manages
- [Delivery-Versus-Payment](/wiki/cash-settlement/) — The DVP principle Euroclear uses
- [Central Counterparty Clearing](/wiki/central-counterparty-clearing/) — The guarantee function
- [Custodian](/wiki/custodian/) — The role Euroclear plays for investors

### Wider context
- Clearstream — A competitor in European settlement
- [Herstatt Risk](/wiki/herstatt-risk/) — The settlement risk Euroclear eliminates
- [European Central Bank](/wiki/european-central-bank/) — The regulator
- [Repo](/wiki/repurchase-agreement/) — A major use case for Euroclear infrastructure

</div>
