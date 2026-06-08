---
title: "Crypto FBAR and FATCA Reporting"
description: "Whether offshore crypto exchange accounts and foreign holdings trigger FinCEN FBAR and IRS FATCA foreign-asset disclosure requirements."
keywords:
  - fbar
  - fatca
  - foreign assets
  - reporting requirements
  - exchange accounts
  - FinCEN
image: "/svg/crypto.svg"
---

*US persons with offshore cryptocurrency holdings or foreign exchange accounts must often file two separate disclosures: the **FinCEN FBAR** (Report of Foreign Bank and Financial Accounts) and the **IRS FATCA** (Foreign Account Tax Compliance Act) Form 8938. Both require listing the maximum value of foreign accounts held during the year. The bar for filing is low—just USD 10,000 in aggregate foreign accounts triggers FBAR; lower thresholds apply to FATCA. Crypto exchanges, wallet providers, and even self-hosted wallets can qualify as "accounts" under both rules.*

Whether a specific crypto exchange account or wallet triggers filing depends on its location, custody structure, and the filer's residency status. The rules are strict: willful failure to file can result in penalties exceeding 50 per cent of account value, and the statute of limitations is ten years for FBAR violations.

## FBAR: the FinCEN reporting requirement

**FBAR** (FinCEN Form 114, "Report of Foreign Bank and Financial Accounts") is a **domestic requirement**—all US persons (citizens, permanent residents, residents for tax purposes) must file FBAR if they have control of foreign financial accounts totalling more than USD 10,000 at any point during the year.

"Control" is broad: the account owner (you), a signatory, a beneficial owner, or anyone with a power of attorney. A joint account held with a spouse counts as your account. A self-directed IRA in a foreign country counts. A crypto exchange account on a foreign exchange counts.

"Foreign financial account" includes:

- Bank accounts (checking, savings, money market) outside the US.
- Brokerage accounts, including crypto exchanges, held outside the US.
- Digital wallet accounts held with a non-US custodian.
- Cryptocurrency staking or interest-bearing accounts with foreign service providers.

**Self-hosted wallets** (a private key you hold in your own wallet, hardware wallet, or non-custodial software) are **not** FBAR-reportable because you do not have an account with a financial institution—you hold the asset directly. If you self-host Bitcoin or Ethereum in a wallet you control, no FBAR is required.

**Self-hosted wallets offshore are also exempt** because they are not accounts with foreign financial institutions. The exception: if you store private keys with a foreign custodian (a foreign vault, foreign safety deposit box, or foreign company holding keys for you), FBAR applies.

**US-based exchanges** (Coinbase, Kraken US, FTX US) do **not** trigger FBAR because the exchange is US-domiciled, even if you are a US person using it. The USD 10,000 threshold refers to accounts held at foreign institutions.

## FATCA: the IRS reporting requirement

**FATCA** (Form 8938, "Statement of Specified Foreign Financial Assets") is an IRS requirement for US persons reporting foreign financial assets above a threshold. The thresholds depend on filing status and residency:

- **Single or married filing separately, US resident**: USD 200,000 (end of year) or USD 300,000 (any day during the year).
- **Married filing jointly, US resident**: USD 400,000 (end of year) or USD 600,000 (during-year peak).
- **Non-resident aliens**: Lower thresholds; often USD 50,000 or less.

"Specified foreign financial assets" includes many asset types crypto does not quite fit into cleanly. The IRS has issued limited guidance on crypto. Most practitioners assume:

- Crypto held at a foreign exchange counts.
- Self-hosted crypto is debatable: some argue the fair market value of self-hosted crypto is a "specified foreign financial asset" if you are reporting it; others argue that because you do not have a custodial account, FATCA does not apply.
- Staking yields and interest-bearing accounts at foreign providers count.

If your foreign crypto holdings exceed the threshold, you file Form 8938 with your 1040. Unlike FBAR, Form 8938 requires listing the value *and* the type of asset (e.g., Bitcoin, Ethereum) but not necessarily the account number.

## Key differences: FBAR vs. FATCA

| Aspect | FBAR | FATCA |
|--------|------|-------|
| **Filing agency** | FinCEN (Treasury) | IRS |
| **Threshold** | USD 10,000 aggregate (any day) | USD 200k–600k depending on status |
| **What triggers it** | Foreign financial accounts | Specified foreign financial assets |
| **Self-hosted crypto** | Generally exempt | Unclear; likely reported if claimed |
| **Form** | FinCEN Form 114 | Form 8938 (with 1040) |
| **Penalty for omission** | Up to 50 per cent (willful) | Up to 40 per cent (specified assets) |
| **Statute of limitations** | 10 years | 6 years (7 if substantial underreporting) |

## Crypto exchanges and which ones trigger filing

A crypto exchange account at a foreign exchange (Binance, Huobi, Kucoin if domiciled outside the US) triggers both FBAR and FATCA if you are a US person and the aggregate value exceeds the threshold. An exchange in a major crypto hub (Singapore, Malta, El Salvador) counts as a foreign account.

A **multi-sig or escrow wallet** held by a non-US custodian (e.g., a Swiss or Cayman Islands custody firm) counts as a foreign financial account.

A **yield account** at a foreign staking or lending platform (e.g., Celsius, BlockFi UK) counts if the provider is non-US and you have exceeded the threshold.

## The safe harbor and reasonable cause

The IRS and FinCEN rarely prosecute accidental omissions by filers with otherwise clean records. Reasonable cause—a good-faith effort to comply—can forgive a missed filing. However, willful violations (knowing failure to report) carry harsh penalties. If you discover you have missed prior years, you can file amended returns (Form 1040-X) and FBAR filings retroactively, ideally with a statement explaining the reason for the late filing.

The **Streamlined Filing Compliance Procedures** (SFCP) is a program that allows non-resident US citizens or bona fide non-residents who missed FBAR and FATCA filings to catch up without criminal prosecution. But you must file before the IRS contacts you.

## US expats and bona fide residents

A **bona fide resident** of a foreign country for an entire tax year can claim the **Foreign Earned Income Exclusion** (FEIE)—up to USD 120,000 (2023) of foreign *earned* income is excluded from US tax. Crypto gains are generally not earned income and so are not excludable. You still file FBAR and FATCA if thresholds are met.

An **expat** (US citizen working abroad) who is not a bona fide resident (e.g., on a work visa in a country where you spent less than half the year) must file FBAR and FATCA the same way as a US resident. The only exception is the Foreign Tax Credit (FTC)—if you paid taxes to a foreign country on crypto gains, you can credit those taxes against your US tax liability.

## Practical steps: documenting holdings

To file FBAR and FATCA correctly:

1. **Identify all foreign accounts** before 31 December each year. Document the maximum balance during the year (not year-end value).
2. **List each account separately**—name, institution, account type, highest balance, currency.
3. **For self-hosted crypto**, decide whether to report (if in a foreign jurisdiction, many practitioners recommend reporting to be safe).
4. **File FBAR by 31 December** of the year following the reporting year (e.g., 2023 accounts filed by 31 December 2024; deadline can be extended via FBAR extension form).
5. **File Form 8938 with your 1040**, due the same date as your tax return (15 April, or later if you request an extension).

Missing FBAR filing can trigger a penalty of up to 50 per cent of the highest balance in the account, applied to each unreported account. Missing Form 8938 can trigger a penalty of USD 10,000 per violation, with an additional USD 10,000 per day if not corrected after IRS notice (capped at USD 50,000 per year).

## See also

<div class="wiki-seealso">

### Closely related

- [Travel Rule for Crypto](/travel-rule-crypto/) — FATF mandate for VASPs to share originator and beneficiary data.
- [MICA Regulation](/mica-regulation/) — EU licensing and disclosure framework for crypto service providers.
- [Crypto Self-Employment Tax](/crypto-self-employment-tax/) — When mining or active trading triggers SE tax.
- Foreign Tax Credit — Offsetting foreign taxes paid against US tax on crypto gains.
- Penalties and Interest — IRS penalties for late or incorrect reporting.

### Wider context

- [Capital Gains Tax](/capital-gains-tax-investor/) — Tax on profit from selling crypto.
- Ordinary Income — Tax treatment of mining and staking rewards.
- Form 1040 — US individual income tax return.
- [Cryptocurrency Exchange](/cryptocurrency-exchange/) — Platforms where holdings often trigger FBAR/FATCA.
- [Bitcoin](/bitcoin/) — The most-held offshore crypto asset.

</div>
