---
title: "How to Report Crypto on IRS Form 8949"
description: "Step-by-step guide to completing IRS Form 8949 for cryptocurrency disposals, handling multiple exchanges, missing cost basis, and Schedule D summary."
keywords:
  - how to report crypto on form 8949
  - form 8949 cryptocurrency
  - crypto capital gains reporting
  - schedule d crypto reporting
  - crypto tax reporting form
image: /svg/crypto.svg
---

*Filing taxes on cryptocurrency sales requires **how to report crypto on Form 8949**, the IRS form for reporting the sale or exchange of capital assets. For most investors with a handful of trades, Form 8949 is straightforward: list the date acquired, the date sold, the proceeds, the cost basis, and the gain or loss. But high-volume traders, multi-exchange holdings, and missing cost basis records create headaches—and the form's design can penalize poor recordkeeping.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Form 8949 for Crypto — key facts</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for cryptocurrency topics." />

<div class="wiki-infobox-caption">Form 8949 aggregates all capital gains and losses; each transaction gets its own line.</div>

|   |   |
|---|---|
| **Form name** | Sales of Capital Assets (Form 8949) |
| **Supporting schedule** | [Schedule D](/schedule-d/) summarizes totals from all Form 8949 forms |
| **Filing requirement** | Required for any crypto sale or exchange (including swaps) |
| **Required columns** | Date acquired, date sold, proceeds, cost basis, gain/loss |
| **Multiple exchanges** | One Form 8949 per exchange OR combine all on a single form |
| **Missing basis issue** | Line item marked "Code B" (basis not reported to IRS); tax consequences apply |
| **Holding period** | Long-term (>1 year) and short-term (≤1 year) listed separately |

</aside>

## The role of Form 8949 in your tax return

Form 8949 is the detailed schedule that documents every sale or exchange of a capital asset you made during the tax year. For each transaction, you report:

- **Description of property:** "Bitcoin," "5 Ethereum," "100 USDC"
- **Date acquired:** When you first bought the coin
- **Date sold:** When you disposed of it (sale, swap, gift, fork, airdrop)
- **Proceeds:** How much you received (in USD, or FMV if received in another coin)
- **Cost or basis:** Your original cost or adjusted basis
- **Gain or (loss):** Proceeds minus basis

The Form 8949 lines aggregate into totals, which then flow to [Schedule D](/schedule-d/). Schedule D sorts gains and losses into long-term (assets held over one year) and short-term (one year or less), and then to the rest of your tax return for final tax calculation.

If you have 100 crypto transactions in a year, you will have 100 line items on Form 8949 (or multiple Form 8949 forms if the IRS's space runs out). The IRS's modern e-file system handles many pages, so volume alone is not a problem. Poor record-keeping is.

## Long-term versus short-term capital gains

Form 8949 requires you to segregate transactions by holding period. Transactions where you held the asset for more than one year are **long-term capital gains**. Transactions where you held the asset for one year or less are **short-term capital gains**.

Long-term gains receive preferential tax rates: 0%, 15%, or 20% depending on income level. Short-term gains are taxed as ordinary income at your marginal rate (up to 37% for top earners).

**Holding period calculation:** If you bought Bitcoin on June 15, 2022, and sold it on June 16, 2023, it is a long-term gain (held over one year). If you sold on June 15, 2023, it is a short-term gain (held exactly one year, not "over" one year). The IRS counts using the acquisition date; if the sale date is one year or more after the acquisition date, it is long-term.

When filling out Form 8949, the first few lines ask about long-term transactions. Later sections ask about short-term. Do not mix them on the same part.

## Completing Form 8949: a step-by-step example

**Step 1: Gather your records.**

For each transaction, you need:
- Purchase date and amount in USD or foreign currency equivalent
- Coin or token type and quantity bought
- Sale date
- Proceeds in USD
- Any fees or commissions (which reduce proceeds or increase basis)

Example: On Coinbase, you bought 2 Bitcoin for $60,000 total ($30,000 per coin) on January 15, 2023. On July 1, 2023, you sold it for $70,000 (after Coinbase's $500 fee, your net proceeds are $69,500).

**Step 2: Determine the holding period.**

You held the Bitcoin from January 15 to July 1—less than one year. This is a **short-term gain**. It goes on the short-term section of Form 8949.

**Step 3: Fill out the line item.**

| Field | Entry |
|-------|-------|
| Description | 2 Bitcoin |
| Date Acquired | 01/15/2023 |
| Date Sold | 07/01/2023 |
| Proceeds | 69,500 |
| Cost or Basis | 60,000 |
| Gain or (Loss) | 9,500 |

**Step 4: Check reporting status.**

In the "Code" column, you mark whether the transaction was reported to the IRS on a Form 1099-B or similar. If you traded on Coinbase, they may have sent you a 1099-B. Check the IRS notice or Coinbase's records. If reported, mark "A." If not reported to the IRS, mark "B." This does not change your tax; it flags to the IRS whether they already have data on the transaction.

## Handling multiple exchanges and large transaction volumes

If you traded on five different exchanges in one year—Coinbase, Kraken, FTX (if still operating), etc.—you have two options:

1. **One Form 8949 per exchange:** File separate Form 8949 sheets labeled "Coinbase transactions," "Kraken transactions," etc. This is cleaner and easier to audit.
2. **Combine all on a single Form 8949:** List all transactions from all exchanges in one document. The IRS does not require separation by exchange.

Most tax software handles this automatically. If you are filing by hand, separating by exchange is slightly better for clarity, but combining is acceptable.

For high-volume traders (100+ transactions), using tax software that integrates with exchanges and generates Form 8949 automatically is essential. Manual transcription invites errors.

## Missing cost basis and "Code B" reporting

The IRS distinguishes between:

- **Code A transactions:** The broker reported cost basis to the IRS on Form 1099-B, so the IRS has the data already.
- **Code B transactions:** The broker did not report cost basis, or the cost basis was not available to the broker.

Code B does not mean you owe more tax—you still owe tax on the full gain. But it signals to the IRS that the information is "unverified by a third party," and it can increase audit risk if the IRS later determines the cost basis was incorrect.

Common scenarios for Code B in crypto:

- You sold crypto from a wallet where you had lost track of the purchase date or price.
- You bought crypto on an exchange that no longer exists (Mt. Gox, before it closed).
- You received crypto from mining, staking, or an airdrop, and you used the FMV on receipt as your basis, but no broker has this data.
- You bought on a foreign exchange that did not issue a 1099-B.

If you have Code B transactions, the IRS may request supporting documentation. Keep:
- Emails or account statements from the exchange showing the purchase.
- Screenshots or PDF exports of historical pricing from that date.
- A written narrative explaining how you determined the cost basis (e.g., "I mined this Bitcoin in 2017; I used the closing price from Coinbase on that date as my basis").

## Swaps and exchanges—treating them as disposals

If you swapped Bitcoin for Ethereum on Uniswap or another DEX, that is a **taxable exchange**—not a simple transfer. Form 8949 requires you to report two transactions: the disposal of Bitcoin (gain/loss) and the receipt of Ethereum (which becomes a new asset with a cost basis equal to the FMV of Bitcoin at the moment of swap, not the FMV of Ethereum received—unless those are the same, which is rare).

Example: You swapped 1 Bitcoin (cost basis $40,000, FMV $65,000) for 100 Ethereum (FMV $65,000) on August 1, 2023. Your Form 8949 entry is:

| Description | 1 Bitcoin |
|---|---|
| Date Acquired | (the date you originally bought it) |
| Date Sold | 08/01/2023 |
| Proceeds | 65,000 (FMV of Ethereum at swap time) |
| Cost Basis | 40,000 |
| Gain | 25,000 |

You also receive 100 Ethereum with a cost basis of $65,000 (the FMV at receipt) and a new acquisition date of 08/01/2023. If you later sell that Ethereum, the holding period starts from August 1, 2023.

## Forks, airdrops, and other "free" transactions

If you received cryptocurrency from a fork (Bitcoin fork to Bitcoin Cash) or an airdrop, the IRS treats the receipt as income—ordinary income at the FMV on the date received.

**Airdrop example:** On October 1, 2023, you received 10 tokens from a DeFi protocol airdrop. The tokens are worth $500 at receipt. You report $500 as ordinary income on your 2023 return (Schedule 1, "Other Income").

Later, if you sell those 10 tokens on December 1, 2023, for $600, you file Form 8949 with:

| Description | 10 airdropped tokens |
|---|---|
| Date Acquired | 10/01/2023 |
| Date Sold | 12/01/2023 |
| Proceeds | 600 |
| Cost Basis | 500 (FMV on receipt) |
| Gain | 100 |

The $100 gain is short-term (held under one year). The initial $500 income is ordinary income, taxed at regular rates. The $100 gain is capital gain, potentially short-term or long-term depending on whether you later hold the tokens over a year.

## Reconciling Form 8949 with broker statements

Tax software like TurboTax, TaxAct, and professional tools can import transactions from major exchanges (Coinbase, Kraken, Gemini, etc.) and auto-fill Form 8949. This is faster and more accurate than hand-entry.

But reconciliation is critical. Check that:

- All transactions from each exchange are imported.
- No duplicate transactions appear (e.g., both the exchange export and a manually entered transaction for the same trade).
- Holding periods are correct (the software may misclassify if you edited the transaction date).
- Proceeds and cost basis match the exchange's records.

Print a copy of the imported data and your broker statement side-by-side and compare line by line. Errors here are the most common source of audit risk.

## Schedule D and the summary totals

Once Form 8949 is complete, the totals roll up to Schedule D. Schedule D shows:

- **Part 1:** Long-term gains and losses
- **Part 2:** Short-term gains and losses

The net total from each part flows to the main tax return for final calculation. If your long-term gains exceed long-term losses, the net is taxed at the favorable long-term capital gains rate. If short-term losses exceed short-term gains, those losses can offset [ordinary income](/income-statement/) (up to $3,000 per year; excess carryover to future years).

Ensure that Form 8949 totals match the Schedule D line items exactly. A discrepancy here will trigger an IRS notice.

## Common Form 8949 mistakes to avoid

**Confusing proceeds with gain.** Proceeds are what you sold *for*. Gain is proceeds minus cost basis. Do not enter gain in the proceeds column.

**Wrong holding period.** Check the acquisition date. If you bought January 15 and sold January 16 of the next year, that is long-term (>1 year). If you sold January 15 of the next year, that is short-term (≤1 year).

**Omitting exchange fees.** If Coinbase charged a $50 fee to sell Bitcoin, your proceeds are sale price minus $50. If the fee was charged when you bought, add it to cost basis.

**Reporting in non-USD amounts.** All entries must be in USD. If you sold Bitcoin for EUR 100,000, convert to USD using the spot exchange rate on the sale date.

**Listing the same transaction twice.** Some traders re-enter transactions manually after importing them, resulting in duplicates. Check for this before filing.

## See also

<div class="wiki-seealso">

### Closely related

- [Schedule D](/schedule-d/) — the form that summarizes Form 8949 gains and losses
- [Cost Basis](/cost-basis/) — how to determine the cost of your crypto for tax reporting
- [Capital Gains Tax](/long-term-capital-gain-tax/) — how gains are taxed at different holding periods
- Form 1099-B — broker reports of cryptocurrency sales
- [Tax Lot](/tax-lot/) — tracking individual purchases to minimize taxes on selective sales

### Wider context

- [Cryptocurrency Exchange](/cryptocurrency-exchange/) — how exchanges facilitate taxable transactions
- [Fair Value](/fair-value/) — how to determine asset value for tax reporting
- [Holding Period](/holding-period/) — how the IRS counts time to determine long-term vs. short-term status
- [Wash Sale](/wash-sale/) — rules on offsetting losses with repurchases (limited for crypto)

</div>
