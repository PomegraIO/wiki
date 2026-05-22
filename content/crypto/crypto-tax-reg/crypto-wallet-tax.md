---
title: "Crypto Wallet Tax"
description: "Tax treatment of gains and losses from cryptocurrency holdings in digital wallets, including reporting requirements and timing of taxable events."
keywords:
  - crypto wallet tax
  - cryptocurrency tax
  - capital gains crypto
  - wallet transactions
  - tax reporting crypto
---

*Crypto wallet tax refers to the [tax treatment](/wiki/capital-gains-tax/) of gains and losses from holding and transacting [cryptocurrency](/wiki/bitcoin/) in digital wallets, including when gains are recognized, how losses are deducted, and reporting obligations.*

<aside class="wiki-infobox">

| Event | Tax Status | Reportable |
|-------|-----------|-----------|
| **Buying crypto with fiat** | No taxable event | No |
| **Selling crypto for fiat** | Taxable gain/loss | Yes, on Form 8949 |
| **Swapping crypto for crypto** | Taxable gain/loss | Yes |
| **Receiving crypto (staking, airdrop)** | Ordinary income at FMV | Yes, on Schedule C or Form 1099 |
| **Mining crypto** | Ordinary income at FMV | Yes |
| **Transferring between own wallets** | No taxable event | No |
| **Donating to charity** | No gain recognized; [charitable deduction](/wiki/charitable-contribution-deduction/) | Yes, if > $500 |

</aside>

## When is crypto a taxable event?

The **IRS treats cryptocurrency as property, not currency.** This is critical: every time you exchange crypto for something else of value—fiat money, another crypto, goods—a taxable event occurs. You must recognize any [gain or loss](/wiki/capital-gains-tax/) on the transaction.

**Buying crypto with dollars:** Not taxable. You trade $10,000 for 0.5 BTC; there is no gain or loss—you have simply swapped equal values.

**Selling crypto for dollars:** Taxable. You sell 0.5 BTC bought for $10,000 at $25,000. Taxable gain: $15,000. Whether it is [short-term capital gain](/wiki/short-term-capital-gain-tax/) (held < 1 year; taxed at ordinary income rates, up to 37% federally) or [long-term capital gain](/wiki/long-term-capital-gain-tax/) (held ≥ 1 year; taxed at 0%, 15%, or 20% depending on income) depends on the holding period.

**Swapping crypto for crypto:** Taxable under current IRS guidance. You swap 1 ETH for 10 USDC when ETH is worth $2,000 and USDC is worth $1. Taxable gain: if you bought ETH for $1,500, your gain is $500 (the FMV at time of swap). This applies to all trades on [decentralized exchanges](/wiki/decentralized-exchange-mechanics/) and centralized venues.

**Receiving crypto as income (staking, mining, airdrops):** Taxable at ordinary income rates. You earn 0.5 ETH from [staking](/wiki/staking/) rewards worth $1,000 when received. Taxable income: $1,000. Your [cost basis](/wiki/cost-basis/) in that ETH is $1,000. If you later sell it for $1,500, you realize a $500 long-term gain (if held 1+ year).

## Cost basis and wash sales

Your **[cost basis](/wiki/cost-basis/)** in crypto is what you paid for it. If you bought 1 BTC for $30,000 and later buy another for $40,000, your average cost basis is $35,000 per BTC. When you sell 1 BTC, you must specify which lot you are selling (specific identification) to optimize [capital gains tax](/wiki/capital-gains-tax/). FIFO (first in, first out) is the default if you do not specify.

The [wash-sale rule](/wiki/wash-sale/) in the US tax code has historically applied to stocks and bonds but not crypto. However, the IRS has signaled intent to extend it to crypto. If enacted, you could not realize a loss on crypto by selling at a loss and repurchasing the same crypto within 30 days; the loss would be disallowed and added to the basis of the new purchase. Many tax professionals already treat crypto as subject to the wash-sale rule.

## Reporting requirements

**Form 8949** (Sales of Capital Assets) is where you report each crypto transaction. Long gains/losses go to Schedule D, which is filed with your [1040](/wiki/estate-tax/). Brokers and exchanges issue [Form 1099-B](/wiki/1099-b/) (Proceeds from Broker Transactions) for certain crypto trades; however, crypto exchanges often do not report to the IRS. This does not mean the IRS cannot find out—the IRS is increasingly cross-referencing bank deposits (especially large ones) with missing 1099 reports.

**Form 1099-MISC** or [**Form 1099-NEC**](/wiki/form-1099-nec/) is used to report staking rewards, mining income, and airdrops of crypto. If you stake 10 ETH and earn 0.5 ETH per year worth $1,000, the staking platform or validator operator should issue a 1099 for that $1,000 income.

**Foreign accounts:** If you hold crypto in a foreign exchange or wallet and the FMV exceeds $10,000 at any point during the year, you must file **FBAR** (Foreign Bank Account Report) and **FATCA** (Foreign Account Tax Compliance Act) forms with FinCEN. Penalties for not filing are severe.

## State and local taxes

Most states treat crypto [capital gains](/wiki/capital-gains-tax/) the same as federal. A few states (California, New York) have additional taxes. New York introduced "crypto tax" proposals (not yet law) that would tax unrealized gains annually, similar to wealth taxes. If enacted, this would make crypto even less attractive for NY residents.

## International tax treatment

The US is one of the most aggressive on crypto taxation. Other countries vary:
- **UK:** Treated as capital gains; [capital gains tax](/wiki/capital-gains-tax/) rates apply (same as the US effectively).
- **Germany:** Held < 1 year → fully taxable at ordinary rates; held > 1 year → tax-free (zero rate). This incentivizes long-term holding.
- **Singapore:** Crypto is largely untaxed if held as a personal investment; taxed only if trading is "habitual" (deemed trading business).
- **El Salvador:** Zero tax on [bitcoin](/wiki/bitcoin/).
- **Portugal:** Tax-exempt for crypto investors.

US citizens abroad are still taxed on worldwide crypto gains; they cannot escape US tax by moving overseas.

## [Wash sale](/wiki/wash-sale/) rules and loss harvesting

**Tax-loss harvesting** in crypto means realizing losses to offset gains elsewhere. If you bought 1 BTC at $50,000 and it fell to $30,000, selling it realizes a $20,000 loss that offsets $20,000 of other gains. Then you rebuy (or buy a similar crypto like Ethereum) to maintain exposure.

The classic wash-sale rule does not (yet) apply to crypto, so you can sell BTC for a loss and immediately rebuy. Some tax professionals caution that the IRS may retroactively extend the rule, so be defensive.

## Staking, airdrops, and forks

**Staking rewards** are taxable as ordinary income when you receive them, even if you immediately stake them (no sale). Many platforms do not issue 1099s, but the IRS expects reporting. Keep records of all staking rewards.

**Airdrops** (free tokens distributed to wallet holders) are taxable at FMV on the date received. A 1000-coin airdrop worth $1 each is $1,000 income.

**Cryptocurrency forks** (like Bitcoin Cash splitting from Bitcoin) are treated as a taxable event by the IRS: you receive a new asset with a zero basis. If you later sell it, all gains are taxable. Some tax advisors argue that forks should not be taxable until you dispose of the new coin, but the IRS disagrees.

## Contested areas and pending guidance

**Like-kind exchange treatment (Section 1031):** Before 2018, some investors argued that crypto-to-crypto swaps qualified for like-kind exchange deferral (defer gains if you swap one property for a similar one). The Tax Cuts and Jobs Act of 2017 eliminated this for crypto, making all swaps taxable effective 2018. This is now settled.

**Decentralized finance (DeFi) and yield farming:** The IRS has not provided clear guidance on complex DeFi transactions (liquidity pools, [impermanent loss](/wiki/impermanent-loss/), governance token distributions). Practitioners are conservative, treating each pool deposit/withdrawal as a taxable event and each yield distribution as income. This can result in dozens or hundreds of transactions to report.

**Environmental/ESG exemptions:** There is no special tax exemption for "green" or "sustainable" crypto, though some propose one.

<div class="wiki-seealso">

### Closely related
- [Capital gains tax](/wiki/capital-gains-tax/) — Tax on profits from selling appreciated assets
- [Wash sale](/wiki/wash-sale/) — IRS rule disallowing losses on quick repurchases
- [Cost basis](/wiki/cost-basis/) — Original purchase price and cost basis tracking
- [Form 8949](/wiki/form-8949/) — IRS form for reporting capital gains and losses

### Wider context
- [Bitcoin](/wiki/bitcoin/) — First and largest cryptocurrency
- [Staking](/wiki/staking/) — Earning crypto rewards for validating transactions
- [DeFi tax implications](/wiki/defi-tax-implications/) — Tax treatment of decentralized finance
- [Yield farming](/wiki/yield-farming/) — Earning rewards by providing liquidity

</div>
