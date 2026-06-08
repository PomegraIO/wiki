---
title: "Crypto Mining Income: Tax Treatment Explained"
description: "Mined cryptocurrency is taxed as ordinary income at fair-market value on the receipt date; miners can deduct equipment, electricity, and labor costs."
keywords:
  - crypto mining income tax treatment
  - mining cryptocurrency taxable income
  - miner deductions expenses
  - fair market value mining
  - self-employed miner taxes
---

*When a miner receives newly minted cryptocurrency for validating transactions or solving a hash puzzle, the IRS treats that receipt as **ordinary income** equal to the fair-market value of the coin on the day it is received. This is taxable immediately—not when the coin is later sold. Miners can deduct operating expenses, equipment, and depreciation, but the gross income is locked in at receipt.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Crypto Mining Income — tax essentials</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Mining is taxed as business income; fair-market value at receipt is ordinary income, subject to self-employment tax.</div>

|   |   |
|---|---|
| **Income recognition** | Ordinary income = FMV on receipt date |
| **Self-employment tax** | 15.3% (Social Security + Medicare), if net profit > $400 |
| **Cost basis** | FMV at receipt (for later capital gains/loss calc) |
| **Deductible expenses** | Electricity, hardware, labor, depreciation, rent |
| **Depreciation method** | [Section 179](/section-179-deduction/) (if eligible) or MACRS (5–7 yr) |
| **Form filing** | Schedule C (self-employed) or Schedule F (business) |
| **Record-keeping** | Mandatory; FMV evidence (exchange prices, appraisals) |

</aside>

## Income recognition at receipt

The IRS has been clear on mining income since at least 2014 guidance: when a miner successfully mines a coin, that coin's fair-market value at the time of receipt is **ordinary income** to the miner. This is not a capital gain (which would apply only when the coin is later sold); it is taxable business income, as if the miner had earned salary.

The "receipt date" is the date the miner receives the coin in their wallet—the block confirmation date, not the date it is sold or moved. If Bitcoin is worth $60,000 on Tuesday and the miner receives 0.01 BTC, the miner reports $600 of ordinary income on Tuesday, regardless of whether they sell the Bitcoin on Tuesday or hold it for five years.

This creates an important asymmetry: the miner pays income tax on a hypothetical sale price on day one, but the actual sale may happen later at a different price. If the price falls to $50,000 by the time the miner sells, they will have overpaid tax (but cannot recoup it as a loss on the original income). If the price rises to $80,000, they benefit from the appreciation (taxed only at capital gains rates).

## Determining fair-market value at receipt

Fair-market value is defined as the price at which a property would change hands between a willing buyer and a willing seller, neither being under a compulsion to buy or sell. For publicly traded cryptocurrencies like Bitcoin and Ethereum, the FMV is typically the exchange price on a major exchange (Coinbase, Kraken, etc.) on the day of receipt.

The miner should document this price using:
- Screenshots of the exchange price on the receipt date.
- Historical price data from CoinMarketCap, CoinGecko, or similar sources.
- Tax software that imports historical price data (e.g., TurboTax, Koinly).

If the cryptocurrency is not widely traded or is illiquid, the miner may need a professional appraisal—though this is rare for major coins.

Any significant divergence between the price the miner uses and what auditors can verify as the exchange price will trigger scrutiny. Conservative miners use the daily closing price or a volume-weighted average price (VWAP) for the day of receipt.

## Self-employment tax obligations

Mining income is classified as self-employment income. If a miner's net profit (revenue minus deductible expenses) exceeds $400 in a year, the miner owes self-employment tax—a combined 15.3% for Social Security and Medicare. This is in addition to ordinary income tax.

A small solo miner with $5,000 of annual mining income and $3,000 of electricity costs would have $2,000 of net self-employment income, owing 15.3% × $2,000 = $306 in self-employment tax alone (before ordinary income tax).

For larger mining operations, the self-employment tax can be substantial. Mining operations structured as corporations or partnerships may be treated differently, but most solo hobbyists and small operators file as self-employed on Schedule C (Form 1040).

## Deductible expenses

Once mining income is recognized, miners can deduct ordinary and necessary business expenses:

**Electricity**: The most significant expense for most miners. The miner can deduct the full cost of electricity used for mining operations. If the miner's home electric bill includes non-mining usage, only the mining portion is deductible—requiring either a separate meter or a reasonable allocation.

**Hardware and equipment**: GPUs, ASIC miners, cooling systems, and related hardware are deductible. Most hardware is depreciated over 5–7 years using [Section 179](/section-179-deduction/) or MACRS (Modified Accelerated Cost Recovery System), rather than expensed immediately. However, under [Section 179](/section-179-deduction/), a miner can elect to immediately deduct up to $1.16 million of equipment in 2023, subject to phase-out limits.

**Labor**: If the miner pays others to oversee mining operations, optimize settings, or manage hardware, those wages are deductible and subject to payroll tax withholding.

**Facility costs**: Rent or mortgage interest (if the mining operation occupies part of a home or rented space), property taxes, and utilities are partially deductible based on the proportion of space used for mining.

**Repairs and maintenance**: Replacing failed fans, servicing hardware, and other upkeep.

**Software and subscriptions**: Mining pool fees, monitoring software, tax software, and accounting services.

**Internet and connectivity**: The portion of broadband used for mining operations.

Miners cannot deduct capital losses on mining hardware that declines in value, but they can claim depreciation deductions over time.

## Depreciation and Section 179

Most mining hardware depreciates over 5–7 years. A miner who purchases a $10,000 ASIC miner can claim annual depreciation deductions, reducing taxable income.

Under [Section 179](/section-179-deduction/), a miner can elect to immediately deduct the full cost of qualifying equipment in the year of purchase, up to an annual limit (currently $1.16 million). This accelerates deductions and can be valuable for miners with high mining income.

The choice between [Section 179](/section-179-deduction/) and MACRS depreciation depends on the miner's tax situation. High-income miners may prefer to spread deductions over time to keep taxable income lower in any single year. Lower-income miners may prefer the immediate deduction.

## Pool mining and mining rewards

Mining pools operate by collecting rewards from many miners and distributing them proportionally. The tax treatment is the same: a pool miner reports the FMV of received coins as ordinary income, even if the coins are held by the pool or exchanged for fiat currency on the miner's behalf. The pool should issue tax documentation (often a custom report) showing the miner's share of income.

Similarly, staking rewards (in [proof-of-stake](/proof-of-stake/) networks) are treated identically: the FMV of received coins at receipt is ordinary income.

## Record-keeping and audit risk

The IRS expects miners to keep detailed records: dates and amounts of each mining reward, FMV documentation for each receipt date, and a complete list of expenses with supporting invoices and receipts. Without this documentation, the miner cannot defend a reported FMV if audited.

Miners using major pools and exchanges have an advantage: the pools and exchanges maintain transaction records that can corroborate reported income. Solo miners face a heavier burden of documentation.

Audit risk increases for miners with large operations or inconsistent reporting. The IRS has historically focused on miners who fail to report mining income entirely, but inconsistent FMV valuations or inflated expense deductions also draw attention.

## Interaction with capital gains tax

After mining income is recognized and a cost basis is established (at the FMV on receipt), any subsequent sale of the coin is treated as a capital gain or loss.

Example:
- A miner receives 1 BTC worth $60,000 on Jan 1 (ordinary income: $60,000; cost basis: $60,000).
- The miner sells the BTC on Mar 1 for $65,000.
- The gain is $5,000, taxed at [long-term capital gains](/long-term-capital-gain-tax/) rates if the holding period is more than one year, or short-term rates if less.

The miner does not re-pay ordinary income tax on the $65,000 sale price; only on the incremental $5,000 gain.

## State and local taxes

In addition to federal income and self-employment taxes, miners may owe state income tax, local business taxes, or property taxes on mining hardware. Tax treatment varies by state; some states follow federal FMV treatment, others have specific crypto guidance, and some have not yet weighed in. Miners in high-tax jurisdictions (California, New York, Vermont) should consult a tax professional.

## Mining as a hobby vs. business

If a miner mines only occasionally and with equipment primarily for personal use, the IRS might classify it as a hobby rather than a business. Hobby income is still taxable ordinary income, but hobby losses cannot be deducted to offset other income. Most miners with significant electricity use and dedicated hardware are treated as running a business, not a hobby. Documentation and intent (profit motive, time spent, reinvestment of income) support a business classification.

## See also

<div class="wiki-seealso">

### Closely related

- [Proof of work](/proof-of-work/) — the consensus mechanism behind Bitcoin and mining
- [Section 179 deduction](/section-179-deduction/) — the tax deduction for business property purchases
- [Long-term capital gain tax](/long-term-capital-gain-tax/) — taxation of the gain when a mined coin is sold
- [Cost basis](/cost-basis/) — how the FMV at receipt establishes the cost basis for future gains/losses
- Cryptocurrency — the asset class being mined and taxed
- [Proof of stake](/proof-of-stake/) — the alternative consensus mechanism (staking income is taxed identically)

### Wider context

- Ordinary income — the tax classification of mining rewards
- Self-employment tax — the 15.3% tax owed on net self-employment income
- [Depreciation](/depreciation/) — the deduction for equipment over time
- [Cryptocurrency exchange](/cryptocurrency-exchange/) — where price data is sourced for FMV determination
- Business deduction — the general principle governing expense deductibility

</div>
