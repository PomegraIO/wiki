---
title: "Specific Identification Method for Crypto Cost Basis"
description: "Crypto specific identification method lets you designate individual coin lots to minimize capital gains. Learn the IRS rules and recordkeeping you need."
keywords:
  - crypto specific identification cost basis
  - cryptocurrency cost basis method
  - crypto tax lot accounting
  - crypto capital gains minimization
  - irs crypto identification rules
image: /svg/crypto.svg
---

*The **specific identification method** for crypto lets you choose which coin lots to sell—rather than selling in the order you bought them—to minimize capital gains taxes. The IRS permits this method, but only if you keep clear records and formally designate lots at the time of sale.*

## How Specific Identification Works

When you buy Bitcoin or Ethereum over time at different prices, each purchase is a separate cost-basis lot. If you bought 0.5 BTC at $20,000 and 0.5 BTC at $40,000, you own two lots totaling 1 BTC.

When you sell, the IRS requires you to account for which lots left your wallet. Under specific identification, **you decide** which lots to sell—not the IRS, not your exchange.

Example:
- **Lot A**: 0.5 BTC bought at $20,000 (cost basis $10,000)
- **Lot B**: 0.5 BTC bought at $40,000 (cost basis $20,000)
- BTC is now $60,000

If you sell 1 BTC without identifying lots, the IRS assumes you use first-in-first-out ([FIFO](#fifo-vs-specific-identification-vs-lifo)) and sold Lot A first:
- Gain on Lot A: $30,000 − $10,000 = $20,000
- Gain on Lot B: $30,000 − $20,000 = $10,000
- **Total gain: $30,000**

If you use specific identification and designate Lot B (the higher-cost lot):
- Gain on Lot B only: $30,000 − $20,000 = $10,000
- **Total gain: $10,000**

By choosing the lot with the highest cost basis, you shrink your taxable gain by $20,000—potentially saving thousands in taxes depending on your [tax bracket](/tax-bracket-investor/).

## The IRS Rules for Specific Identification

The IRS allows specific identification under [IRC Section 1012](https://www.irs.gov/), but compliance is strict.

**At the time of the transaction**, you must identify which lots are being sold. This means:
- You specify the lot by its acquisition date and cost basis.
- You must have a contemporaneous record (a written notation at the time of sale, not a reconstruction months later).
- Your exchange or wallet app must support lot designation, or you must track it yourself and keep documentation.

If you do not identify lots at the time of sale, the IRS defaults to FIFO. Once you file your [Schedule D](/schedule-d/) claiming specific identification, that election is locked in for that transaction.

The burden of proof is on you. If the IRS audits your return, you must produce records showing:
- The date and price of each purchase (acquisition lot).
- The date and price of each sale.
- Which specific lots you sold and the method you used to identify them.

## Recordkeeping Requirements

Detailed records are non-negotiable. Keep:

1. **Purchase records** for every coin acquisition: date, quantity, price per coin, total cost, exchange or wallet name.
2. **Sale records** for every partial or full disposal: date, quantity sold, price per coin, total proceeds, and **the specific lots sold** by acquisition date.
3. **Lot designation documentation**: at minimum, a screenshot, email, or CSV export from your exchange showing which lots you designated at the time of sale. Many platforms (Kraken, Coinbase Pro) allow you to tag specific lots; export and archive those records.
4. **Wallet transfers**: if you move coins between wallets or exchanges, track the movement so you can trace cost basis from acquisition to sale.

The IRS increasingly scrutinizes crypto records because the space is still evolving. Exchanges are now beginning to report transactions on Form 8949 (Sales of Capital Assets). Mismatches between your return and your exchange's reporting will trigger correspondence; solid documentation is your only defense.

## Setting Up Specific Identification in Practice

Not all exchanges offer easy lot-level designation. Here's what to expect:

**Platforms with built-in support**: Kraken, Coinbase Pro, and some others let you tag purchases and then designate which lots to sell when you place a transaction. Before selling, confirm the platform is showing you the right lot.

**Platforms without built-in support**: If your exchange doesn't offer lot designation, **you must do it yourself**. Maintain a spreadsheet or CSV:

| Lot | Date | Qty | Price | Cost Basis | Sale Date | Qty Sold | Sale Price | Proceeds | Gain/(Loss) |
|-----|------|-----|-------|-----------|-----------|----------|-----------|----------|-------------|
| A   | 2020-01-10 | 0.5 | $9,000 | $4,500 | 2024-05-15 | 0.5 | $60,000 | $30,000 | $25,500 |
| B   | 2021-06-20 | 1.0 | $40,000 | $40,000 | — | — | — | — | — |

Print or screenshot your exchange's transaction history to prove you owned the coins and sold them on those dates. This manual documentation is admissible in an audit, though it's tedious.

## Specific Identification vs. FIFO vs. LIFO

Three methods are IRS-approved for crypto (and other assets):

**[FIFO](/fifo/)** (First-In-First-Out): You are deemed to sell the oldest lot first. Simple but usually results in the largest gains if prices have risen over time. Default method if you don't elect another.

**LIFO** (Last-In-First-Out): You are deemed to sell the newest lot first. More aggressive tax deferral, especially useful in bear markets. The IRS allows it, but you must elect it on your tax return consistently year to year.

**Specific Identification**: You choose the lot. Most tax-efficient if you want to minimize gains in a given year.

For most crypto holders in rising markets, specific identification is superior to FIFO. It lets you defer high-gain lots and realize low-gain or loss-making lots when you need to rebalance.

## Elections and Consistency

Once you elect a method on your tax return, you should stick with it. Switching from FIFO to specific identification mid-year, then back to FIFO, invites audit scrutiny. If you have a legitimate reason to change (e.g., you restructured your holdings), disclose the change in a written statement with your return.

## Common Pitfalls

**Forgetting to designate at the time of sale**: If you sell coins without specifying which lots, you cannot claim specific identification later. The IRS defaults to FIFO. Fix this by keeping a contemporaneous record (a note or email to yourself at the time of sale) and referencing it in your records.

**Mixing custodians**: If you own the same coin across multiple exchanges, track which lot is where. Selling from one exchange does not automatically link to a particular lot at another. Document which exchange held which lot.

**Not reconciling with exchange reports**: Exchanges are beginning to report crypto transactions to the IRS on Form 8949. If your records disagree with theirs, revise your records to match or be ready to explain the discrepancy.

**Wash-sale confusion**: The IRS has not formally clarified whether [wash-sale](/wash-sale/) rules (which disallow losses if you buy the same asset within 30 days) apply to crypto. Many advisors assume they will eventually. If you harvest a loss on BTC and buy it back shortly after, document your intent and keep records in case the rule is applied retroactively.

## See also

<div class="wiki-seealso">

### Closely related

- [Cost Basis](/cost-basis/) — general principles of determining what you paid for an asset
- [Schedule D](/schedule-d/) — IRS form for reporting capital gains and losses
- Long-Term Capital Gains Tax — preferential rates for holdings over one year
- [Wash Sale](/wash-sale/) — rules preventing loss harvesting followed by immediate repurchase
- [FIFO](/fifo/) — accounting method for cost basis when lots are not designated

### Wider context

- [Tax-Loss Harvesting](/tax-loss-harvesting/) — strategy for capturing losses to offset gains
- [Tax Bracket](/tax-bracket-investor/) — how marginal rates affect gain realization timing
- [Form 8949](/form-8949/) — the IRS form for reconciling capital gains with exchange reports
- [Cryptocurrency Exchange](/cryptocurrency-exchange/) — platforms where cost basis and lot designation begin

</div>
