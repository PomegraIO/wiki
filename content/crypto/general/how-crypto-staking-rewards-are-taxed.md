---
title: "How Crypto Staking Rewards Are Taxed"
description: "How crypto staking rewards are taxed: treated as ordinary income when received, at fair market value. Cost basis is the FMV on receipt date."
keywords:
  - how crypto staking rewards are taxed
  - staking income tax treatment
  - crypto ordinary income
  - staking tax cost basis
  - proof of stake taxation
image: "/svg/crypto.svg"
---

*When you receive **crypto staking rewards**, the IRS treats them as ordinary income at the moment of receipt—not when you sell the tokens. Your cost basis is the fair market value of the reward tokens on the exact date you received them, and that date-of-receipt valuation is critical for calculating [capital gains](/long-term-capital-gain-tax/) or losses when you eventually sell.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Crypto Staking Rewards — taxation snapshot</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Reward income is ordinary; capital gain is later.</div>

|   |   |
|---|---|
| **Income recognition** | Date of receipt, at fair market value (FMV) |
| **Income type** | Ordinary income; taxed at your full [marginal rate](/marginal-tax-rate-investor/) |
| **Cost basis** | FMV on the exact date you received the reward |
| **Future gain/loss** | Sale price minus cost basis = capital gain or loss |
| **Holding period** | Starts on the receipt date; >1 year = long-term capital gain |
| **Reporting** | Schedule 1 (Form 1040); may need Form 8949 or Schedule D at sale |

</aside>

## Staking Rewards as Ordinary Income

The IRS treats **proof-of-stake** rewards (tokens you earn by locking up [cryptocurrency](/cryptocurrency-exchange/) on a [blockchain](/blockchain-fundamentals/)) as income. The moment the tokens are credited to your wallet—not when you convert them to dollars, not when you transfer them—you have taxable income.

This is distinct from selling tokens at a profit. Selling triggers a [capital gain](/long-term-capital-gain-tax/), which may be taxed at a preferential long-term rate if you held the tokens more than one year. Staking rewards, by contrast, are **ordinary income**, taxed at your full [marginal rate](/marginal-tax-rate-investor/), which is typically higher.

### Why the Timing Matters

Imagine you stake 10 ethereum (ETH) and receive 0.5 ETH as a reward on June 1, 2025, when ETH trades at $2,000. You have $1,000 of ordinary taxable income on June 1, even though you haven't sold anything.

- **Ordinary income recognized:** June 1, 2025: $1,000  
- **Your cost basis in the reward:** $2,000 (the FMV on June 1)  
- **Scenario A:** You sell the 0.5 ETH on July 1, 2025, at $2,100.  
  - Capital gain: $2,100 − $2,000 = $100 (short-term capital gain, taxed as ordinary income).  
  - Total tax: $1,000 ordinary (staking) + $100 ordinary (short-term gain).  
- **Scenario B:** You hold until January 2026 and sell at $2,500.  
  - Capital gain: $2,500 − $2,000 = $500 (long-term capital gain, lower rate).  
  - Total tax: $1,000 ordinary + $500 long-term capital gain.

The **date of receipt** is the hinge pin: it determines the cost basis, and combined with the sale date, it determines whether capital gain is long-term or short-term.

## Determining Fair Market Value on Receipt

The hardest part of staking-reward taxation is pinpointing the FMV on the exact date you received the reward—not the average price that week, not the round price, but the FMV on that specific day.

### Using Exchange Prices

If your staking platform credits rewards in the morning, use the **opening or mid-point price** on that exchange for that token on that date. Most taxpayers use major exchange prices:

- **Coinbase, Kraken, Gemini closing price** on the reward date.  
- **CoinMarketCap or CoinGecko median price** (averaged across major exchanges).  
- **IRS accepted approach:** Any reasonable, documented source that reflects the market price on that date.

Keep a screenshot or CSV export showing the date, token, quantity, and price. If audited, you'll need to defend that valuation.

### Multiple Rewards, Same Day

If you stake multiple tokens or receive rewards in tranches throughout the day, you can either:

1. **Use the same closing price** for all rewards received that day (simpler).  
2. **Prorate by time-of-receipt** if your platform shows timestamps (more granular, but tedious).

Most accountants recommend the closing-price approach for simplicity, as long as you document it.

### Missing Price Data

If the token is illiquid or was not traded on the date you received the reward:

- Use the **most recent prior trade date's price**.  
- Or use the **first subsequent trade date's price**.  
- Document your choice and reasoning; the IRS will scrutinize this.

For newly launched tokens or low-volume altcoins, getting a defensible valuation is harder. This is a known audit risk.

## Cost Basis Tracking

Once you establish the cost basis of the reward tokens (FMV on receipt), you need to track that basis separately for each reward, because each reward has a different cost basis and a different date of receipt.

### Example: Multi-Reward Scenario

| Date received | Quantity | FMV per token | Total cost basis | Date sold | Sale price | Gain/(loss) |
|---------------|----------|---------------|-----------------|-----------|-----------|-----------|
| June 1, 2025 | 0.5 ETH | $2,000 | $1,000 | July 15, 2025 | $2,100 | $100 ST |
| June 15, 2025 | 0.4 ETH | $1,950 | $780 | Dec 1, 2025 | $2,500 | $420 LT |
| July 1, 2025 | 0.6 ETH | $1,800 | $1,080 | Still holding | — | — |

Each reward is a separate [tax lot](/tax-lot/). If you claim a loss on one reward and a gain on another, they can offset—but you must track each lot separately and report the aggregate on [Schedule D](/schedule-d/) (Form 1040).

## FIFO, LIFO, and Specific ID

When you sell staking reward tokens (or any crypto), you must specify which cost-basis method you're using:

- **FIFO** (first-in-first-out): The first tokens you received are the first you sell. Simple but often unfavorable if your early rewards had low cost basis.  
- **LIFO** (last-in-first-out): The most recent rewards are sold first. Can reduce gains if recent tokens have higher basis.  
- **Specific identification** ([specific-identification-basis](/specific-identification-basis/)): You pick which specific reward lots to sell, based on cost basis and holding period. Most flexible but requires detailed record-keeping.

Choose your method upfront and apply it consistently. Once you've filed a return using FIFO, switching to LIFO requires filing an amended return and [Form 3115](/corporate-income-tax/).

Most crypto taxpayers use specific ID because it minimizes tax, but you must document the specific lot sold in each transaction.

## Validator Rewards vs. Exchange Staking

**Self-staking on a [blockchain](/blockchain-fundamentals/):** You control the private keys; you receive rewards directly. Income recognition is on the date the reward hits the blockchain, visible in the ledger.

**Exchange staking (Coinbase, Kraken, etc.):** The exchange stakes on your behalf. Income recognition is typically on the date the exchange credits your account—which may lag the actual blockchain confirmation by hours or a day. Use the date the exchange shows in your account; that's your defensible position.

**Lending platforms (Celsius, BlockFi, etc.):** Rewards from staking platforms that also offer lending. The same rule applies: ordinary income on the date of credit.

Document the exact date and amount in each case using your exchange statement as evidence.

## Delegated Staking and Consensus Mechanisms

Different blockchains have different reward-distribution timelines:

| Blockchain | Timing | Example |
|-----------|--------|---------|
| Ethereum (proof of stake) | Rewards deposited to your wallet immediately or batched daily | Income recognized on deposit date |
| Solana | Rewards batched into epochs (roughly daily) | Income recognized when epoch settles |
| Cardano | Rewards distributed monthly | Income recognized on distribution date |
| Cosmos (delegated staking) | Rewards accrued but only claimable when you manually withdraw | Income recognized on withdrawal date? (IRS unclear) |

For delegated staking where rewards accrue but are not automatically claimed, the IRS position is evolving. **Conservative approach:** Recognize income when you claim/withdraw the rewards. **Aggressive approach:** Recognize income when rewards accrue. Most advisors recommend the conservative view until the IRS clarifies.

## Audit Risk and Documentation

The IRS is ramping up scrutiny on cryptocurrency taxation. Common audit triggers for staking:

- **No reported staking income** despite owning staked crypto.  
- **Discrepancies between exchange reports and your tax return.**  
- **Aggressive cost-basis valuations** (e.g., claiming a reward was worth $0.10 when it traded at $1.00).  
- **FIFO vs. specific-ID inconsistencies** across multiple years.

**Protect yourself by:**

1. **Reporting all staking income** on Schedule 1, Form 1040.  
2. **Keeping monthly or quarterly summaries** from your exchange showing staking rewards.  
3. **Recording the date, quantity, and FMV** for every reward.  
4. **Using a cost-basis tracking tool** (CoinTracker, Koinly, etc.) to generate [Schedule D](/schedule-d/) reports.  
5. **Filing an amended return** immediately if you discover unreported staking income; this shows good faith.

## See also

<div class="wiki-seealso">

### Closely related

- [Capital gains tax](/long-term-capital-gain-tax/) — lower rates on long-term gains after holding >1 year
- [Cryptocurrency exchange](/cryptocurrency-exchange/) — platforms where you stake and receive rewards
- [Blockchain fundamentals](/blockchain-fundamentals/) — proof-of-stake mechanics
- [Cost basis](/cost-basis/) — establishing the starting value of an asset for future gain/loss calculation

### Wider context

- [Marginal tax rate](/marginal-tax-rate-investor/) — how ordinary staking income is taxed at your top bracket
- [Schedule D](/schedule-d/) — form for reporting capital gains and losses on the sale of staked tokens
- [Tax-loss harvesting](/tax-loss-harvesting/) — offsetting crypto losses against gains
- [Ordinary income](/corporate-income-tax/) — how staking rewards are classified and taxed

</div>
