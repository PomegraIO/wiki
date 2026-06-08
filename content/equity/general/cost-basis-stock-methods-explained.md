---
title: "Cost Basis Methods for Stock: FIFO, LIFO, and Specific Identification"
description: "Cost basis methods for stock determine which shares are treated as sold during a partial position liquidation. FIFO, LIFO, and specific identification each produce different tax outcomes."
keywords:
  - cost basis methods for stock
  - fifo lifo specific identification
  - tax-loss harvesting cost basis
  - average cost basis
image: "/svg/equity.svg"
---

*The **cost basis method** determines which of your shares are considered sold when you liquidate part of a stock position, directly shaping your realized gain or loss and, therefore, your tax bill.*

## Why the Same Stock Can Have Different Cost Basis

When an investor buys shares at different prices over time, partial sales create an accounting choice: which shares am I selling? Suppose you buy 100 shares of XYZ at $10 per share (cost basis $1,000), then 100 shares at $15 per share (cost basis $1,500), then sell 75 shares when the price is $20. Which shares are the 75 you sold—the cheaper first 100, the more expensive second 100, or some mix? The IRS allows multiple methods, and each produces a different capital gain.

The answer is not the same as your physical share certificates (which are fungible electronic entries anyway). It is a tax-filing choice that you must declare on [Schedule D](/schedule-d/) when you report the sale.

## FIFO: First-In, First-Out

**FIFO** assumes the oldest shares are sold first. Using the example above:

- Shares held longest: 100 at $10 cost = $1,000 total cost
- Shares held second: 100 at $15 cost = $1,500 total cost
- Sale: 75 shares at $20 each = $1,500 proceeds

Under FIFO, the 75 shares sold are the 75 oldest shares from the first batch, which cost $10 each ($750 total cost basis). Sale proceeds are $1,500, so realized gain = $1,500 − $750 = **$750 taxable gain**.

FIFO is the IRS default if you don't specify a method. It is also usually the worst tax outcome in a bull market, because you sell your cheapest shares first and book the largest gains. However, FIFO can be optimal in a bear market or sideways market if your oldest shares have declined below your newest ones.

## LIFO: Last-In, First-Out

**LIFO** assumes the most recent shares are sold first.

Using the same example:

- The 75 shares sold are from the second batch (most recent), which cost $15 each ($1,125 total cost basis).
- Sale proceeds are $1,500, so realized gain = $1,500 − $1,125 = **$375 taxable gain**.

LIFO defers the tax burden by selling higher-cost shares first, realizing smaller gains now. In a bull market, this is often superior to FIFO. However, LIFO is rarely permitted for US equities held by individual investors. The IRS restricts LIFO elections to certain inventory valuations for businesses and is generally unavailable on personal tax returns. Some tax software and brokers allow it for legacy reasons, but it is not the default election and may not be allowed at all on your specific shares—check with your broker.

## Specific Identification

**Specific Identification** (or "SpecID") lets you nominate *exactly which shares* you are selling. This is the most flexible method and the one preferred by sophisticated investors.

Using the example, you could specify: "Sell the 75 most expensive shares (the 75 from the $15 batch)," resulting in a $375 gain. Or, if you preferred, "Sell 50 shares from the $10 batch and 25 shares from the $15 batch," resulting in a gain of $50 × ($20 − $10) + 25 × ($20 − $15) = $500 + $125 = **$625 gain**.

To use specific identification, you must:

1. **Notify your broker in writing** (or via a clear electronic instruction) *before the sale* which lot(s) you are selling.
2. **Confirm the broker's execution** by cross-referencing the lot identification numbers to your trade confirmation.
3. **Keep records** and report the method on your tax return.

Many brokers now offer "tax-loss harvesting" that automatically implements specific identification by selecting the highest-cost shares for sale, minimizing gains. Others require explicit instructions.

## Average Cost Basis

**Average Cost** (either single-category or double-category) pools all shares into one or two buckets and treats each sold share as having the average cost of that bucket.

Example: You hold 200 shares total with a combined cost of $2,500, so average cost = $2,500 / 200 = $12.50 per share. If you sell 75 shares at $20, your gain = 75 × ($20 − $12.50) = 75 × $7.50 = **$562.50**.

Average cost is simple and is often the default at mutual-fund companies. However, it is less flexible than specific identification and is generally suboptimal for tax planning. Once you elect average cost on a mutual fund, you may not switch to another method without IRS permission—so the choice is somewhat binding.

## Comparing the Methods: Tax Impact

For the 75-share sale at $20, with a first batch at $10 and second at $15:

| Method | Cost Basis of Sale | Proceeds | Realized Gain | Ranking |
|---|---|---|---|---|
| FIFO | $750 | $1,500 | $750 | Worst (highest gain) |
| Average Cost | $937.50 | $1,500 | $562.50 | Middle |
| Specific ID (high cost) | $1,125 | $1,500 | $375 | Best (lowest gain) |

In a rising market, specific identification of the highest-cost shares is almost always superior. Specific ID is mandatory if you want to [tax-loss harvest](/tax-loss-harvesting/)—sell at a loss to offset other gains—because you need to select exactly which underwater shares to sell.

## Regulatory and Broker Constraints

**US equities (stocks)**: Specific identification is permitted and is the election of choice for tax-conscious investors.

**Mutual funds**: Specific identification is allowed, but many funds default to average cost. Switching methods mid-holding requires documentation and permission.

**Bonds**: Specific identification is permitted. FIFO is the default.

**ETFs**: Specific identification is permitted, though some brokers make it cumbersome.

**Cryptocurrency**: Tax treatment varies by jurisdiction and broker, but specific identification is generally the most defensible method.

Not all brokers implement specific identification clearly. Check your broker's documentation and confirm that any manual instructions are recorded in writing. If the broker cannot honor specific ID, you are often stuck with their default (usually FIFO or average cost), which may not be tax-optimal.

## Audit Trail and Documentation

The IRS requires clear documentation of the method used and which shares were sold. Keep:

- Confirmation of your lot-selection instruction to the broker (email, screenshot, or account statement note).
- Broker trade confirmations that cross-reference lot numbers or dates acquired.
- Your tax return line-item showing the method claimed.

Mismatches between your return and broker records invite IRS scrutiny. Many investors file inconsistently (claiming specific ID on the return but letting the broker default to FIFO), which can trigger an audit or a correction. File accurately.

## See also

<div class="wiki-seealso">

### Closely related

- [Tax-Loss Harvesting](/tax-loss-harvesting/) — Using cost-basis methods to realize losses
- [Long-Term Capital Gains Tax](/long-term-capital-gain-tax/) — How holding period and realized gains interact
- [Schedule D](/schedule-d/) — The tax form where cost basis method is reported
- [Share Buybacks](/share-buyback/) — Corporate repurchases and shareholder cost basis

### Wider context

- [Asset Allocation](/asset-allocation/) — How to structure a diversified portfolio
- [Capital Gains Tax](/long-term-capital-gain-tax/) — Overall capital gains taxation
- [Accounting Methods](/accrual-accounting/) — How businesses choose cost methods for inventory

</div>
