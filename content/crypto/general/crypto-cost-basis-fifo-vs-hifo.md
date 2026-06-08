---
title: "FIFO vs HIFO for Crypto Cost Basis"
description: "Choosing FIFO or HIFO determines whether you match your oldest or highest-cost coins against sales, directly affecting your taxable gain or loss in the year of sale."
keywords:
  - fifo vs hifo
  - crypto cost basis
  - cryptocurrency tax
  - tax-loss harvesting
  - capital gains
image: "/svg/crypto.svg"
---

*When you sell cryptocurrency, the tax collector needs to know your **cost basis**—the price you paid. If you own multiple batches bought at different prices, the method you choose to identify which coins you sold changes your taxable gain or loss. **FIFO** (first-in, first-out) assumes you sell your oldest coins first; **HIFO** (highest-in, first-out) assumes you sell your highest-cost coins first. The difference can swing a six-figure profit into a loss.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Crypto Cost Basis Methods — key factors</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for cryptocurrency." />

<div class="wiki-infobox-caption">Cost basis method determines which batch's purchase price is matched against the sale price, changing your taxable gain or loss.</div>

|   |   |
|---|---|
| **FIFO (First-In-First-Out)** | Assumes oldest coins sold first; creates larger gains in rising markets, smaller gains in falling markets |
| **HIFO (Highest-In-First-Out)** | Assumes highest-cost coins sold first; reduces current-year gains by selling expensive coins |
| **Default (IRS assumption)** | FIFO, unless you elect otherwise in writing and follow consistently |
| **Tax impact example** | $1 BTC @ $10k (oldest) vs. $1 BTC @ $60k (newer): FIFO matches $10k cost to a $65k sale (55k gain); HIFO matches $60k cost (5k gain) |
| **Burden** | HIFO requires detailed record-keeping; IRS allows HIFO if specifically identified and documented |
| **Strategy potential** | HIFO enables tax-loss harvesting and gain deferral by choosing which coins to sell |

</aside>

## How cost basis methods work in crypto

When you buy cryptocurrency, your **cost basis** is the price you paid (in dollars, or whatever currency) plus any transaction fees. If you buy 1 Bitcoin at $50,000, your cost basis is $50,000.

If you buy a second Bitcoin at $60,000, you now own two coins with different cost bases.

When you sell 1 Bitcoin at $65,000, the tax outcome depends on which coin the IRS considers you to have sold:

- **If you sold the $50,000 coin (FIFO):** Taxable gain = $65,000 − $50,000 = **$15,000 gain**.
- **If you sold the $60,000 coin (HIFO):** Taxable gain = $65,000 − $60,000 = **$5,000 gain**.

This difference is not hypothetical. It flows directly to your capital gains tax bill for the year. Choose the wrong method, and you could owe thousands more than necessary.

## FIFO: the default assumption

**FIFO** (first-in, first-out) assumes you sold the coins you acquired first. This is the default method the IRS assumes you use, unless you explicitly elect otherwise.

**How it works:**

1. You buy 1 BTC on January 1 for $10,000 (cost basis: $10,000).
2. You buy 1 BTC on June 1 for $20,000 (cost basis: $20,000).
3. You sell 1 BTC on December 1 for $25,000.

Under FIFO, the IRS assumes you sold the January coin (the older one). Your taxable gain is $25,000 − $10,000 = **$15,000**.

**Pros:**
- Simple to administer; no detailed record-keeping required.
- IRS expects it; minimal audit risk if you follow consistently.

**Cons:**
- In a rising market, FIFO locks you into the largest gains because you're selling the cheapest coins. You owe more tax this year.
- If you're trying to manage gains strategically (e.g., staying below a [tax bracket](/tax-bracket-investor/) threshold), FIFO offers no flexibility.

**Market impact:** FIFO is harsher in bull markets. As Bitcoin rose from $10k to $60k over years, FIFO method users faced enormous deferred gains on early purchases. Selling even a small amount triggered recognition of old, cheap-purchase gains.

## HIFO: the strategic alternative

**HIFO** (highest-in, first-out) assumes you sold the coins you acquired at the highest cost. This allows you to minimize current-year gains by always selling your most expensive coins.

**How it works:**

1. You buy 1 BTC on January 1 for $10,000.
2. You buy 1 BTC on June 1 for $20,000.
3. You sell 1 BTC on December 1 for $25,000.

Under HIFO, you "identify" the June coin (the expensive one) as sold. Your taxable gain is $25,000 − $20,000 = **$5,000**.

**Pros:**
- Minimizes current-year taxable gains, deferring tax liability to future years.
- Enables intentional [tax-loss harvesting](/tax-loss-harvesting/): sell at a loss while rebuying the same coin after 30 days (wash-sale rule permitting).
- Aligns with economic reality in some cases: if you wanted to liquidate expensive positions, HIFO reflects that choice.

**Cons:**
- Requires explicit election and detailed documentation (Form 8949 and supplementary records for each lot).
- If you deviate or fail to document, the IRS defaults you to FIFO retroactively.
- Creates complexity if you later sell and need to show all your cost basis for each coin.
- Some advisors argue HIFO creates a "reporting burden" the IRS scrutinizes.

## Wash-sale rule and tax-loss harvesting

The **wash-sale rule** (Section 1091) disallows a loss if you repurchase the same asset within 30 days before or after the sale.

Under HIFO, tax-loss harvesting becomes more precise:

**Scenario:**

1. You bought 1 BTC at $30,000.
2. BTC is now at $20,000; you want to harvest a $10,000 loss.
3. You sell 1 BTC at $20,000, triggering the $10,000 loss.
4. You immediately repurchase 1 BTC at $20,000.

Under FIFO, you'd be forced to sell your oldest coin (maybe purchased at $5,000, a $15,000 gain)—not a loss. Under HIFO, you deliberately identify and sell a high-cost coin at a loss, harvesting the loss without wash-sale violation (as long as you wait 30 days before repurchasing).

This precision made HIFO popular among serious crypto tax strategists. However, the IRS has never formally endorsed HIFO for crypto; it is permitted for other assets (stocks), but crypto's treatment is ambiguous. Conservative advisors recommend explicit written election and meticulous documentation.

## Specific identification vs. automatic methods

The IRS recognizes three methods for identifying which securities you sold:

1. **Specific Identification** – You explicitly choose which lot you sold (e.g., "I am selling the June purchase at $20,000 cost basis").
2. **FIFO** – Oldest lot is sold first (default).
3. **Average Cost** – You average all purchases and apply that average to all sales.

HIFO is a subset of specific identification. It works only if you make an affirmative, documented election. If you do not, the IRS treats you as using FIFO.

## Documentation and record-keeping

To use HIFO (or any method other than FIFO), you must:

1. **Elect it in writing** before or at the time of the sale (or at tax filing, if done timely).
2. **Maintain a detailed record** of:
   - Each purchase: date, quantity, cost basis (in USD), exchange used.
   - Each sale: date, quantity, proceeds, method used (HIFO).
   - Lot identification: specify which purchase lot was matched to which sale.
3. **Report consistently**: Once you choose HIFO, use it for all crypto sales unless the IRS grants permission to change.

A spreadsheet suffices, but many use specialized crypto tax software (CoinTracker, Koinly, etc.) that automatically tracks cost basis. These tools allow you to select FIFO or HIFO at sale time, then export a report for [Schedule D](/schedule-d/).

## Real-world example: a volatile year

**Setup:**

- You hold 3 Bitcoin:
  - Lot A: 1 BTC purchased at $20,000 (from 2017).
  - Lot B: 1 BTC purchased at $45,000 (early 2021).
  - Lot C: 1 BTC purchased at $60,000 (late 2021).

- BTC falls to $30,000 by November. You sell 1 BTC to raise cash.

**FIFO outcome:**
- You sell Lot A (oldest, $20,000 cost).
- Gain = $30,000 − $20,000 = $10,000.
- Remaining basis: $105,000 for 2 BTC.

**HIFO outcome:**
- You specifically identify and sell Lot C ($60,000 cost).
- Gain = $30,000 − $60,000 = **−$30,000 (loss)**.
- You harvest a $30,000 capital loss, offsetting other gains or up to $3,000 of ordinary income (with remainder carried forward).
- Remaining basis: $65,000 for 2 BTC.

**Tax impact:** Using HIFO instead of FIFO shifts your tax position by $40,000 in gain/loss—potentially a $10,000+ tax swing at a 25% combined rate.

## Caveats and IRS ambiguity

The IRS has **not formally clarified** whether HIFO is permitted for cryptocurrency specifically. The regulations reference FIFO and average-cost explicitly; HIFO is permitted for stocks and mutual funds via specific identification, but crypto occupies a grey zone.

Most tax professionals recommend using HIFO only if:
- You file a formal election and documentation.
- Your software explicitly supports it (avoiding manual tracking error).
- You work with a qualified tax advisor who is willing to defend the method.

Conservative taxpayers default to FIFO to avoid audit risk. Aggressive tax planners use HIFO and document meticiously. The IRS may clarify crypto treatment in future guidance; until then, defensibility rests on documentation and professional judgment.

## See also

<div class="wiki-seealso">

### Closely related

- [Cost Basis](/cost-basis/) — The foundational concept for any capital gains calculation
- Long-Term Capital Gains Tax — Tax rates depend on holding period and cost basis method
- [Tax-Loss Harvesting](/tax-loss-harvesting/) — Strategy enabled by HIFO for selecting which coins to sell
- [Schedule D](/schedule-d/) — Tax form where capital gains and losses are reported
- [Form 8949](/form-8949/) — Detailed line-by-line reporting of sales and basis

### Wider context

- [Cryptocurrency](/cryptocurrency-exchange/) — The asset class where cost basis method matters most
- [Capital Gains Tax](/capital-gains-tax-investor/) — Broader tax treatment of gains
- [Tax Bracket](/tax-bracket-investor/) — Threshold that can be managed via cost basis elections

</div>
