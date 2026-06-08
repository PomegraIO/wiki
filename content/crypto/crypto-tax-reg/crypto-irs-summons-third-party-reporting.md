---
title: "IRS John Doe Summons and Third-Party Crypto Reporting"
description: "The IRS uses John Doe summonses to obtain user data from crypto exchanges and custodians. Learn what information is shared and compliance implications."
keywords:
  - irs crypto third party reporting summons
  - john doe summons cryptocurrency
  - irs exchange subpoena crypto
  - third party crypto data reporting
---

*The IRS uses **John Doe summonses** to compel crypto exchanges, custody platforms, and blockchain analytic firms to turn over user transaction data in bulk. These legal demands can sweep millions of transaction records into IRS hands without targeting a specific person. Exchanges typically comply, and the agency then uses this data to identify and audit noncompliant taxpayers. Understanding this enforcement tool is critical for assessing long-term compliance risk.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">IRS Summons and Third-Party Reporting — key facts</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for cryptocurrency." />

<div class="wiki-infobox-caption">The IRS can compel exchanges to hand over broad user data; compliance depends on the exchange and jurisdiction.</div>

|   |   |
|---|---|
| **Tool** | John Doe summons (named summons to unnamed parties) |
| **Targets** | Exchanges, custodians, blockchain analytics firms |
| **Data sought** | Transaction history, user identity, IP addresses, account activity |
| **Scope** | Can cover years and millions of accounts |
| **Legal basis** | Internal Revenue Code § 7609; judicial review available |
| **Exchange compliance** | US platforms generally comply; offshore platforms resist or claim inability |

</aside>

## What is a John Doe summons?

A **John Doe summons** is a subpoena issued by the IRS to a third party (like Coinbase or Kraken) that does not name a specific taxpayer. Instead, it requests data on broadly defined groups of people—for example, "all accounts that conducted cryptocurrency transactions exceeding $10,000 between January 1, 2013 and December 31, 2022." The IRS then uses that data to cross-reference against tax returns and identify individuals who did not report income.

The summons is authorized under Internal Revenue Code § 7609. The IRS does not need a warrant or proof of wrongdoing to issue one; it simply asserts that the information is relevant to tax administration. The exchange can challenge the summons in court, arguing that it is too broad, unduly burdensome, or that the IRS lacks a legitimate purpose—but the bar for the agency to prevail is relatively low.

## Major summonses and what they revealed

The IRS has issued several high-profile summonses:

**Coinbase (2019):** The IRS demanded records on all US users who bought, sold, or held more than $20,000 in cryptocurrency in any year between 2013 and 2015. Coinbase fought the summons in court but ultimately lost. The exchange provided about 13,000 account records, including names, addresses, tax IDs, transaction histories, and account activity. The IRS has since used this data to identify unreported crypto gains and issue audit notices.

**Kraken (2022):** The IRS subpoenaed Kraken for records of US users with accounts during a multi-year period. Kraken initially challenged the summons but negotiated a narrower scope. The final agreement covered certain years and transaction types.

**Gemini, Bitstamp, Voyager, and others:** The IRS has issued summonses to numerous exchanges, with varying results. Some platforms settle on more limited data; others provide larger datasets.

## What information is typically demanded

A John Doe summons generally seeks:

- **User identity:** Full name, address, email, phone number, date of birth
- **Account information:** Account number, creation date, verification status
- **Transaction history:** Every buy, sell, deposit, withdrawal, and transfer with date, amount, price, and counterparty (e.g., USD deposit from Bank A, Bitcoin withdrawal to address 0x...)
- **Payment methods:** Bank account numbers, credit card information, PayPal accounts linked to the crypto account
- **IP addresses and device data:** Login IP addresses, user-agent strings, locations from which account was accessed
- **Tax reporting documents:** Any 1099 forms or statements the exchange already filed

The scope can be enormous. A single summons might request records covering 5+ years and thousands of accounts.

## How exchanges respond

**US-regulated platforms (Coinbase, Kraken, Gemini, etc.):** These are generally subject to US court jurisdiction and cannot refuse without risking fines or loss of banking services. Most have legal teams experienced in negotiating summons scope, but compliance is the default endpoint. They may challenge a summons as overbroad, but courts rarely invalidate them entirely. Exchanges typically comply within 6–12 months.

**Offshore platforms (Binance, OKX, FTX, etc.):** These platforms operate outside the US and may claim they cannot comply with US subpoenas. However, if the platform maintains any US operations (banking relationships, IP ranges, subsidiary entities), the IRS may obtain court orders to seize assets or block bank transfers. Binance has faced such pressure. Many offshore platforms eventually provide at least partial compliance to avoid being shut out of the US financial system.

**Decentralized exchanges and non-custodial wallets:** The IRS cannot summon a decentralized protocol (like Uniswap) because there is no legal entity to summon. However, if a DEX front-end is hosted by a US company, or if a staking or lending protocol is operated by a US entity, the IRS can target that operator.

## Timeline and audit risk

The process typically unfolds over years:

1. IRS issues summons (year 0).
2. Exchange challenges or negotiates for 3–6 months (optional).
3. Exchange produces data (year 1–2).
4. IRS matches data against tax returns and identifies discrepancies (year 2–3).
5. IRS sends letter 3115 (exam opening notice) or 3911 (notice of deficiency) to affected taxpayers (year 3–4).

If you did not report a gain, did not report income, or filed a return with incorrect figures, an IRS notice can lead to:
- Proposed assessment of back taxes
- Failure-to-file and accuracy-related penalties (20–75%)
- Interest on unpaid tax (currently ~8% annually)
- Possible criminal referral if fraud is suspected (willful evasion carries up to 5 years in prison)

The statute of limitations is generally 3 years from filing, but extends to 6 years if income is substantially underreported (>25% understatement), and to unlimited if return is fraudulent or not filed.

## How the IRS uses the data

Once the IRS receives summons data, it loads it into its systems and cross-references it against filed tax returns. Matching algorithms flag taxpayers where:

- Exchange records show significant transactions, but the return reports no crypto income.
- A taxpayer reported a capital gain on Form 8949 or Schedule D, but exchange records show larger transactions.
- A taxpayer claimed zero income in a year where exchange data shows thousands of dollars in activity.

The agency then selects accounts for examination. The IRS prioritizes high-dollar transactions and cases where there is clear evidence of intent to hide income (e.g., accounts opened in false names or through VPNs).

## Privacy and legal challenges

Taxpayers have challenged John Doe summonses as violating privacy rights under the Fourth Amendment. Courts have generally rejected these arguments, finding that summonses are a valid investigative tool under the tax code. However, the IRS must still meet statutory requirements:

- The information must be relevant to tax liability.
- The IRS must not have adequate alternative sources.
- There must be a legitimate purpose (not arbitrary or harassing).

Exchanges can challenge summonses on these grounds. In the Coinbase case, the exchange argued the summons was too broad; the court agreed but narrowed rather than invalidated it. Most challenges result in negotiated limits (e.g., "provide data only on accounts with >$20,000 in annual volume").

## Compliance steps for affected taxpayers

If you received an IRS notice related to crypto:

1. **Do not ignore it.** The IRS will eventually assess tax, penalties, and interest if you do not respond.
2. **Gather exchange records.** Download all transaction history from every exchange you used, including historical exports if available.
3. **Calculate corrected returns.** Use [cost basis](/cost-basis/) methods (FIFO, LIFO, or specific identification) consistently.
4. **File an amended return (Form 1040-X)** if you were undercompliant. Filing amended returns before the IRS issues a formal assessment can reduce penalties.
5. **Consult a CPA or tax attorney.** Crypto tax disputes are technical; professional guidance reduces audit risk and potential penalties.

## Foreign financial accounts and FBAR

If your crypto exchange account is held offshore (e.g., a Kraken account while you lived abroad), and the account exceeded $10,000 at any point, you may be required to file an FBAR (Form FinCEN 114) disclosure. Failure to file carries civil penalties up to $100,000+ per year of violation. The IRS increasingly enforces FBAR compliance and cross-checks it against exchange data.

## See also

<div class="wiki-seealso">

### Closely related

- [Securities and Exchange Commission](/securities-and-exchange-commission/) — Regulatory body overseeing financial markets and exchanges
- [Capital Gains Tax (Investor)](/capital-gains-tax-investor/) — How capital gains are calculated and taxed
- [Cost Basis](/cost-basis/) — Determining the starting value for tax purposes

### Wider context

- [Is Moving Crypto Between Your Own Wallets Taxable?](/crypto-moving-between-wallets-taxable/) — Non-taxable transfers vs. dispositions
- [NFT Royalty Income Tax](/nft-royalty-income-tax/) — Ordinary income treatment for creator royalties
- [Stablecoin Tax Treatment](/stablecoin-tax-treatment/) — Capital gains implications of stablecoin swaps

</div>
