---
title: "Tax-Lot Optimization in Portfolio Construction"
description: "How selecting specific tax lots—FIFO, LIFO, or highest-cost—affects after-tax returns and portfolio performance."
keywords:
  - tax lot optimization
  - tax lot selection
  - fifo lifo specific identification
  - after-tax returns
  - portfolio construction
  - tax-lot accounting
---

*A **tax lot** is a block of securities acquired at a single price on a single date; **tax-lot optimization** means choosing which lots to sell when you need to reduce a position, lowering the after-tax proceeds by selecting higher-cost or more favorably-taxed lots first. Since identical shares bought at different times have different cost bases, the lot you sell determines whether you realize a small gain or a large one—and thus whether you owe $5,000 or $50,000 in [capital gains tax](/long-term-capital-gain-tax/). Systematic lot selection during portfolio rebalancing, [dividend distributions](/dividend/), and [share buybacks](/share-buyback/) can add 0.5–2% annually to after-tax returns.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Tax Lots — The Mechanics</div>

<img src="/svg/strategies.svg" alt="An abstract editorial mark for portfolio strategy." />

<div class="wiki-infobox-caption">Choosing which block of shares to sell controls your realized gain and tax bill.</div>

|   |   |
|---|---|
| **Tax lot** | One batch of identical securities, bought on one date at one price |
| **FIFO (first-in, first-out)** | Sell oldest shares first; often triggers largest gains and highest taxes |
| **LIFO (last-in, first-out)** | Sell newest shares first; useful in rising markets to defer realized gains |
| **Highest-cost identification** | Sell highest-priced shares first; minimizes realized gain regardless of date |
| **Lowest-cost (wedding-day)** | Sell lowest-priced shares first; maximizes realized gain intentionally |
| **Tax impact on returns** | Proper selection can improve after-tax return by 0.5–2% per year over a decade |
| **Broker support** | Major custodians (Schwab, Fidelity, Vanguard) support specific-identification elections |

</aside>

## Why Lot Selection Matters

Suppose you bought Apple stock in three tranches:

- 100 shares on Jan 1, 2015 at $100/share (cost basis $10,000).
- 100 shares on Jan 1, 2018 at $150/share (cost basis $15,000).
- 100 shares on Jan 1, 2023 at $180/share (cost basis $18,000).

Today, Apple trades at $200/share. You want to raise $20,000 in cash by selling 100 shares.

**If your broker uses FIFO** (the default for most custodians unless you elect otherwise), you sell the oldest lot: the 2015 purchase. Your realized gain is $200 − $100 = $100 per share, or $10,000 total. At a 20% [long-term capital gains tax rate](/long-term-capital-gain-tax/), you owe $2,000 in federal tax, netting $18,000.

**If you elect highest-cost identification**, you sell the 2023 lot: cost $180/share, current price $200/share. Realized gain is only $20 per share, or $2,000 total. Federal tax is just $400, netting $19,600.

That is a $1,600 difference—an 8.9% tax savings—on a single sale of 100 shares. Over a career of rebalancing, dividend-reinvestment decisions, and strategic liquidations, the compounding effect is substantial.

## The Four Common Lot-Selection Methods

**FIFO (First-In, First-Out)** is the default for most US brokers and is the simplest to track: sell the oldest lot first. This method is straightforward for record-keeping but often the worst for taxes. In a rising market—which equities have been over most long-term horizons—FIFO forces you to realize the largest gains first because the oldest shares have climbed the most. It is tax-inefficient in most scenarios.

**LIFO (Last-In, First-Out)** sells the newest shares first. In a rising market, newer shares often have smaller unrealized gains than old shares, so LIFO can defer larger gains. However, LIFO has quirks: if newer shares were bought at higher prices than old ones, LIFO does not help. Also, LIFO creates a complex cost-basis tail; the oldest shares remain in your account, compounding in value and making eventual sale more painful. LIFO is best when the newest purchase was significantly cheaper than earlier buys, or when you anticipate a sharp market drop that will let you harvest losses on the old, expensive shares later.

**Highest-Cost Identification** (also called "specific identification") means selecting shares bought at the highest price, regardless of purchase date. This minimizes the gain on every sale and is often the most tax-efficient method over a long holding period. Because you are always selling the shares with the smallest unrealized gain, you defer the largest gains as long as possible. Compounding the deferred gains magnifies this advantage.

**Lowest-Cost (or "Average-Cost" or "Wedding-Day")** sells shares with the smallest [cost basis](/cost-basis/), triggering the largest realized gains. This is rarely optimal for tax purposes and is used only in specific scenarios, such as when you want to harvest large losses elsewhere in your portfolio to offset the gain, or when you face a near-term tax change that makes taking a gain now preferable to deferring it.

## How Tax-Lot Optimization Integrates into Portfolio Management

Smart portfolio construction uses lot selection at three key points:

**Rebalancing**: When [asset allocation](/asset-allocation/) drifts—equities rise and now represent 65% of your portfolio instead of the target 60%—you sell equity to reallocate. Choosing which stock to sell, and which lot within that stock, controls the tax impact. If one stock is up 200% and another 30%, you might sell the expensive stock (to realize a smaller gain) rather than the cheap one. If within a single stock you have a 300% gain and a 50% gain, you sell the 300% lot first, deferring the smaller one.

**Dividend and Distribution Handling**: Many investors reinvest [dividends](/dividend/) automatically, creating dozens of small tax lots over time. When you need cash, you can choose to liquidate the most recent dividend reinvestment (small gain) rather than original shares (large gain). Over decades, this difference is material.

**Strategic Liquidations**: When you sell a concentrated position to fund a goal—down payment on a house, retirement drawdown, charitable giving—lot selection can cut the tax bill by 15–30%. For an executive exercising [stock options](/option/) or a founder exiting a liquidity event, lot optimization is non-negotiable. A $10 million sale that could net $7 million after taxes or $8.2 million with smart lot selection is a $1.2 million difference.

## Practical Record-Keeping and Broker Election

To use specific identification or any non-FIFO method, you must **elect it explicitly** with your broker at the time of sale. You cannot decide years later that a sale was LIFO; the election must be documented contemporaneously. Most custodians (Schwab, Fidelity, Vanguard) allow online election at the time of sell, or you can instruct in writing.

For your own records, maintain a **lot ledger**: a spreadsheet or document listing every purchase (date, quantity, price, commission) and every sale (date, quantity, elected lot, sale price, proceeds, realized gain/loss). This is essential for preparing [Schedule D](/schedule-d/) (Capital Gains and Losses) and defending your positions if audited. The IRS requires clear evidence that a specific lot was sold; if your records are ambiguous, the Service assumes FIFO, which usually works against you.

Tools like [Terraform Labs](https://www.terraform.io) (for crypto) and brokers' cost-basis reports help, but manual verification is wise. A single misallocated lot can cascade through years of tax filings.

## The Trade-Off: Complexity vs. Savings

Highest-cost identification is mathematically superior to FIFO in most scenarios, but it demands discipline. You must:

- Track dozens or hundreds of small lots carefully.
- Elect the specific lot at each sale.
- Ensure your tax preparer understands your method and reports it consistently.

For a $50,000 portfolio with one or two stock positions and annual rebalancing, the tax savings from lot optimization might be $200–500/year—meaningful, but not transformative. For a $5 million concentrated equity position with dozens of purchases over decades, the annual tax delta could be $20,000–100,000 by choosing the right lots.

Large investors and advisors often hire specialized tax software (like ARTAX, Tax-Lot Optimizer, or Morningstar) to automate lot tracking and optimization. These tools ingest your trades, run scenarios, and recommend which lots to sell to minimize a year's total tax liability while respecting your portfolio goals. For most individuals, a spreadsheet and discipline suffice.

## Behavioral Hazards: Mental Accounting and Lot Bias

Investors often fall prey to **mental accounting**, a cognitive bias where they treat a single stock's oldest lot (the original investment) as emotionally sacred or "foundational" to their wealth, even if it has become hugely profitable. They might sell a newer, cheaper lot to avoid "touching" the original, paying more tax in the process. Overcoming this requires discipline: a lot is a lot; it has no intrinsic value relative to others.

Similarly, some investors avoid selling at all when a position has a large unrealized gain, fearing the tax bill. But deferring the sale indefinitely is a form of "tying up" capital that could do better elsewhere. A strategic sale using highest-cost identification might reallocate that capital to a better opportunity, more than making up the tax paid.

## Wash Sales and Timing Considerations

One constraint: the [wash-sale rule](/wash-sale/). If you sell a security at a loss, you cannot buy the same or a substantially identical security within 30 days before or after the sale, or your loss is disallowed. This can complicate lot selection during market downturns. You might want to sell a low-cost, underwater lot to harvest the loss, but if you rebalance or reinvest the proceeds into the same stock within the wash-sale window, the IRS disallows the loss.

Planning around wash sales requires forward-looking discipline: harvest losses deliberately and either stay out of the position for 31 days or buy a different but similar asset (e.g., switch from an individual stock to an ETF of that sector, or use separate trading accounts if trading multiple related positions).

## Tax-Lot Optimization and Charitable Giving

One special case: donating appreciated securities to charity bypasses capital gains tax entirely. If you have a highly appreciated lowest-cost lot, donating it is often superior to selling and reinvesting the proceeds. The charity receives the full $200/share value, you claim a $200/share deduction, and you owe zero capital gains tax. This is a compelling alternative to lot optimization in some scenarios—not selling at all, but giving it away strategically.

## See also

<div class="wiki-seealso">

### Closely related

- [Cost Basis](/cost-basis/) — the foundation of capital gains calculation
- [Long-Term Capital Gains Tax](/long-term-capital-gain-tax/) — how holding periods affect tax rates
- [Schedule D](/schedule-d/) — IRS form for reporting capital gains and losses
- [Tax Loss Harvesting](/tax-loss-harvesting/) — selling losses to offset gains
- [Wash Sale](/wash-sale/) — the 30-day rule preventing loss-sale abuse
- Charitable Deduction — donating appreciated assets to avoid capital gains

### Wider context

- [Using a Charitable Remainder Trust to Defer Crypto Capital Gains](/crypto-charitable-remainder-trust-tax/) — advanced strategy for concentrated holdings
- [Asset Allocation](/asset-allocation/) — rebalancing decisions that trigger tax-lot optimization
- [Dividend](/dividend/) — reinvestment that creates new tax lots

</div>
