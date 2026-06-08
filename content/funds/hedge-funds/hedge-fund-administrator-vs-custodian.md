---
title: "Hedge Fund Administrator vs Custodian: Key Differences"
description: "Explains the distinction between a hedge fund administrator (NAV, records) and custodian (asset safekeeping), and why both are essential."
keywords:
  - hedge fund administrator
  - hedge fund custodian
  - fund administration
  - asset safekeeping
  - NAV calculation
---

*A **hedge fund administrator** calculates the fund's net asset value (NAV), maintains investor records, and prepares regulatory reports; a **custodian** is an independent third party that takes physical possession of the fund's assets and protects them from theft, fraud, or misappropriation. Both roles are essential, but they are distinct and must be separate to prevent conflicts of interest.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Fund Administrator vs Custodian — key facts</div>

<img src="/svg/funds.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Two separate guardians: one counts the assets, one safeguards them.</div>

|   |   |
|---|---|
| **Administrator role** | NAV calculation, record-keeping, compliance, investor reporting |
| **Custodian role** | Asset holding, settlement, safekeeping, segregation |
| **Who appoints** | Fund manager (administrator); often mandated/required by regulators (custodian) |
| **Independence** | Administrator may be affiliated with the fund; custodian must be independent |
| **Conflict risk** | High for administrator (calculating own NAV); mitigated for custodian (segregated assets) |
| **Common custodians** | Major banks (BNY Mellon, State Street, Wilmington Trust, Citi) |
| **Regulatory mandate** | Custody segregation required by SEC, CFTC, and foreign regulators |

</aside>

## The administrator: calculating and recording

A fund administrator is the operational backbone of a hedge fund. Immediately after each trading day, the administrator collects trade data from the fund manager, brokers, and counterparties. It then calculates the **[net asset value](/net-asset-value/)** (NAV)—the total value of all positions, less fees and liabilities, divided by the number of fund shares.

This calculation is non-trivial. The administrator must:

- **Price all assets**, even illiquid ones. For public stocks and bonds, pricing is straightforward; for private equity stakes, distressed debt, or bespoke derivatives, the administrator works with the fund manager to apply agreed-upon valuation methods (cost basis, discounted cash flows, broker quotes, or independent appraiser reports).
- **Account for interest, dividends, and accruals.** If a position has accrued but not yet settled interest, it must be booked correctly.
- **Record all transactions.** Buys, sells, fees, dividends, deposits, and redemptions are logged in a centralized ledger.
- **Prepare investor statements.** Each investor receives a monthly or quarterly report showing their share count, NAV per share, gains/losses, and fees charged.
- **Maintain compliance records.** The administrator tracks regulatory filings, investor kyc (know-your-customer) documents, and audit trails.
- **Calculate and distribute fees.** Management fees and performance fees are computed from the NAV and collected or distributed to the fund manager.

The administrator is also the fund's interface with regulators. If the SEC or CFTC requests information, the administrator compiles and submits it. If an audit is required, the administrator cooperates with auditors.

## The custodian: safekeeping and segregation

A custodian is a bank or specialized financial institution that takes **physical or book-entry possession** of the fund's securities, cash, and other assets. The custodian's core duty is to keep those assets safe and separate from any other party's assets (including the custodian's own).

Specifically, the custodian:

- **Holds securities** in segregated accounts, legally registered in the fund's name or in the custodian's name "for the benefit of" the fund.
- **Settles trades**, ensuring cash flows in and out and securities are transferred correctly.
- **Earns income** (dividends, interest) into the fund's account, not the custodian's.
- **Verifies asset existence**, reconciling the custodian's records with the fund's holdings daily or weekly.
- **Resists claims** from creditors, the fund manager's personal lenders, or even the fund's own borrowers. Assets in custodial segregation cannot be seized or pledged without explicit authorization.
- **Maintains insurance** against loss, theft, or operational failure.

The custodian is a purely defensive institution. Its job is not to grow wealth or calculate returns; it is to ensure that no other party (not the fund manager, not a broker, not the custodian itself) can steal or lose the assets.

## Why both are necessary: separation of duties

If the fund manager were also the administrator and custodian, incentives would be misaligned. A corrupt manager could:

- Overstate valuations to boost reported NAV and performance fees.
- Understate holdings to hide theft.
- Create fictitious trades or deposits to mask losses.
- Pledge assets to lenders without disclosing the encumbrance.

History confirms this risk. The Madoff fraud (2008) succeeded partly because Madoff Securities was simultaneously the fund manager, administrator, and custodian. No independent party verified that the assets existed. Madoff's false statements on investor statements were never contradicted by a custodian.

Regulators now require that the custodian be independent—not an affiliate of the fund manager, and in some jurisdictions, not even the same corporate group. The SEC and CFTC mandate this for US-registered funds and advisers. Most major jurisdictions globally follow suit.

The administrator, by contrast, is often chosen by the fund manager (though this is changing; some sophisticated LPs insist on administrator independence too). An administrator affiliated with the manager is still useful if the custodian is separate. The custodian's independence—the fact that it is a third-party bank—provides the critical check.

## Who chooses and appoints each?

**The administrator** is typically selected by the fund manager when establishing the fund. The manager wants an administrator familiar with its strategy and capable of handling complex valuations (e.g., a hedge fund investing in private debt will need an administrator experienced in illiquid credit instruments). Common administrators are Citco, GlobeOp (now part of SS&C), Intertrust, and Apex. Many large asset managers also build in-house administration teams.

**The custodian** is also chosen by the manager, but with less flexibility. Regulators often mandate that the custodian be a "qualified" institution—typically a bank or specialized custodian licensed to hold securities and insurance-protected. Major custodians like [BNY Mellon](/bank-of-america/), [State Street](/bank-of-america/), Wilmington Trust, and Citi dominate because they have global reach and custody-grade security. A small hedge fund cannot easily use an unbank custodian, even if the manager prefers it.

In some cases, investors negotiate custodian selection as a condition of investment. Large institutional investors (pension funds, endowments) often demand that custodian fees and terms be transparent and that the custodian be large and creditworthy.

## Operational mechanics: a typical fund day

A typical hedge fund's operational flow:

1. **Morning (fund manager's office).** Traders execute buys and sells; settlements are initiated.
2. **Late afternoon (administrator and custodian).** The manager sends trade confirmations to the administrator and custodian.
3. **Evening (custodian).** The custodian receives and processes settlements with counterparties. Securities are transferred into the fund's account; cash flows are settled.
4. **Evening (administrator).** The administrator receives custody confirmations, reconciles them against the manager's trade list, prices all positions (using custodian valuations for liquid assets, manager input for illiquid ones), calculates NAV.
5. **Next morning.** Investors receive the NAV via the administrator's system or portal. The fund's books are closed and auditable.

If the administrator's NAV differs materially from what custodian holdings support, reconciliation occurs. Discrepancies (missing cash, phantom holdings) are flagged and investigated. This daily cycle is the fund's heartbeat and the mechanism that detects fraud.

## Segregation and regulatory standards

Regulatory expectations around custodian segregation have tightened since 2008. The Financial Conduct Authority (FCA) in the UK and the SEC in the US now require that custodians segregate fund assets by individual fund (not pooling multiple funds' holdings). Some jurisdictions further require that client cash be held in segregated bank accounts, not co-mingled with the custodian's operational float.

These rules aim to protect investors if the custodian fails. If client assets are properly segregated, creditors cannot touch them. Without segregation, a custodian's bankruptcy can wipe out client holdings.

## Fees and incentive structures

Administrators typically charge a flat fee per fund or a percentage of AUM (assets under management). Their fees are disclosed to investors and often negotiated. An administrator managing a complex, illiquid portfolio (e.g., a private-equity fund) charges more than one managing a liquid equity fund.

Custodians also charge fees—typically a basis point or two of AUM plus transaction costs. Custodian fees are usually lower than administrator fees, but custodians are often more rigid on pricing because they are fewer and larger.

Both fees reduce investor returns. A fund with a $100 million NAV might pay $200K/year to the administrator and $50K/year to the custodian, totaling $250K annually (25 basis points). Added to the fund manager's fees, this becomes material for small funds or those with thin margins.

## The risk of administrator misalignment

Even with a separate custodian, conflicts of interest remain for the administrator. If the administrator is incentivized by the fund manager (e.g., the manager benefits from high NAV and thus high performance fees), the administrator might tolerate loose valuations of illiquid assets or delay mark-downs.

Best-practice funds now address this by:

- **Using independent valuations** for illiquid assets (third-party appraisers or specialist pricing services).
- **Requiring administrator independence** (the administrator is not affiliated with the manager).
- **Having investors audit the administrator** (large institutional investors conduct due diligence on the administrator's processes).
- **Using third-party compliance monitors** to review administrator calculations against custody holdings.

But custody alone is not enough to prevent fraud. The Madoff case and other failures have shown that a custodian can be fooled or complicit if it is not genuinely independent.

## See also

<div class="wiki-seealso">

### Closely related

- [Net asset value](/net-asset-value/) — The daily calculation the administrator performs and investors rely on
- [Custodian](/custodian/) — The independent third party that safeguards assets
- [Hedge fund](/hedge-fund/) — The fund type that requires both administrator and custodian
- [Due diligence](/due-diligence/) — The investor process of verifying administrator and custodian quality

### Wider context

- [Fund prospectus](/fund-prospectus/) — The document disclosing administrator and custodian identity and fees
- [Investment company act of 1940](/investment-company-act-of-1940/) — The regulatory framework mandating custodian independence
- [Operational risk](/operational-risk/) — The category of risk (fraud, error, theft) that separating these roles mitigates
- [Private equity fund](/private-equity-fund/) — A fund type with additional administrator complexity due to illiquid holdings

</div>