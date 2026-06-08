---
title: "Crypto Cost Basis Methods Explained"
description: "How FIFO, HIFO, and LIFO cost basis methods work for cryptocurrency sales and affect taxable gain calculations and tax liability."
keywords:
  - crypto cost basis methods
  - fifo hifo lifo cryptocurrency
  - crypto tax basis methods
  - cost basis accounting crypto
  - crypto taxable gain calculation
image: "/svg/crypto.svg"
---

*The way you calculate **crypto cost basis** when you sell determines your taxable gain or loss. FIFO, HIFO, and LIFO are three methods that pair different purchase prices with the sale, creating vastly different tax bills from the same activity. The IRS allows you to choose, but you must be consistent and document your method.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Crypto Cost Basis Methods — key facts</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for cryptocurrency." />

<div class="wiki-infobox-caption">Cost basis method choice is an active tax-planning decision that applies to each sale.</div>

|   |   |
|---|---|
| **Default method (IRS assumption)** | FIFO (first-in, first-out) |
| **Most tax-efficient for bull markets** | HIFO (highest-in, first-out) |
| **Most tax-efficient for bear markets** | LIFO (last-in, first-out) |
| **Requirement** | Must choose before or at time of sale; must document |
| **Frequency of choice** | Can specify method per sale (spec ID best practice) |
| **Tax impact** | Determines realized gain/loss and short- vs. long-term character |
| **IRS audit risk** | High if method isn't consistently applied or documented |

</aside>

## FIFO: The Default and Simplest Method

**FIFO** (first-in, first-out) assumes you sell the coins you bought first. It's the IRS default: if you don't document a different method, FIFO is what the IRS assumes happened.

Here's a concrete example:

- January 1: Buy 1 BTC at $30,000 (long-term holding).
- March 1: Buy 1 BTC at $40,000 (short-term holding).
- November 1: Sell 1 BTC at $50,000.

Under FIFO, you're deemed to sell the January coin. Your cost basis is $30,000, your sale price is $50,000, and your gain is $20,000. Crucially, because the January coin has been held longer than one year, it's a long-term capital gain (taxed at preferential rates in most cases).

FIFO is simple to track and requires no special software—anyone can sort their buy orders chronologically and pair them with sales in sequence. For that reason, it's embedded in many exchange and tax-reporting systems as the default.

But simplicity isn't the same as tax efficiency. In a bull market where prices generally climb, FIFO forces you to realize gains on your oldest, cheapest coins—maximizing your taxable gain and pushing you toward higher tax brackets. Many traders find this frustrating.

## HIFO: Targeting High-Basis Coins to Minimize Gain

**HIFO** (highest-in, first-out) reverses the logic: you sell the coins with the highest cost basis first, minimizing your realized gain.

Using the same example:

- January 1: Buy 1 BTC at $30,000.
- March 1: Buy 1 BTC at $40,000.
- November 1: Sell 1 BTC at $50,000.

Under HIFO, you'd sell the March coin (cost basis $40,000, gain $10,000 instead of $20,000). Your tax bill is lower.

HIFO shines in bull markets because high-basis coins often have the largest unrealized gains sitting in your wallet. By selling them first, you recognize smaller realized gains, deferring the recognition of massive gains to future years (or potentially avoiding them if you never sell).

The downside: HIFO is manual. Most exchanges and crypto tax software default to FIFO and won't automatically track HIFO. You have to identify which specific coins you're selling and document that choice. The IRS calls this "specific identification" (Spec ID). Without contemporaneous documentation—a record created at the time of sale showing which lot you chose to sell—the IRS may reject your HIFO claim in an audit.

## LIFO: Accounting Gain Deferral in Bear Markets

**LIFO** (last-in, first-out) assumes you sell the most recently purchased coins. It's less intuitive for most traders, but it has value in specific circumstances.

Same example:

- January 1: Buy 1 BTC at $30,000.
- March 1: Buy 1 BTC at $40,000.
- November 1: Sell 1 BTC at $50,000.

Under LIFO, you sell the March coin (cost basis $40,000), which is identical to HIFO in this case. The difference emerges when prices are falling.

Imagine instead you sell at $35,000:

- **FIFO**: Cost basis $30,000, gain $5,000.
- **HIFO**: Cost basis $40,000, loss of $5,000.
- **LIFO**: Cost basis $40,000, loss of $5,000.

In a bear market where recent purchases are underwater, LIFO lets you realize losses quickly (useful for [tax-loss harvesting](/tax-loss-harvesting/)), and it pairs your sale with the highest-basis (most recent) coins. Many long-term holders who bought during bull markets and are sitting on losses prefer LIFO to crystallize those losses and offset other gains.

LIFO also carries the same documentation burden as HIFO: you must use specific identification and keep records.

## Short-Term vs. Long-Term Holding and Cost Basis

The choice of cost basis method also interacts with holding period. Realized gains/losses are taxed differently depending on whether the coins have been held longer than one year.

In the FIFO example above, selling the January coin gave you a long-term gain (held >1 year). In a bull market, FIFO often pairs you with older, longer-held coins, which is good for tax character. But the realized gain is also larger.

With HIFO, you're selling the March coin (short-term holding in that example), which gives you a short-term gain—taxed as ordinary income, not capital gain rates. That's worse tax treatment, but the absolute dollar gain is smaller. The net tax bill depends on your marginal tax bracket and the size of each effect.

This trade-off is why thoughtful tax planning requires looking at the full picture: method, holding period, realized gain magnitude, and your personal tax bracket.

## Documentation and IRS Audit Risk

The IRS cares deeply about specificity. If you claim HIFO or LIFO, you must:

1. Choose the method before or at the time of sale (not retroactively).
2. Document which specific lot you sold (e.g., "1 BTC purchased March 1, 2024 at $40,000 cost").
3. Apply the method consistently across all your transactions.

Failing on any of these invites audit risk. An auditor will compare your claimed method against your exchange records and tax reporting. If you say you used HIFO but your documented lots don't match the highest-basis coins you owned, the IRS will recompute using FIFO and assess back taxes and penalties.

Because crypto transactions happen at high volume and across multiple exchanges, documentation is often scattered—emails to yourself, screenshots, exported CSVs from your exchange. The best practice is to use a specialized crypto tax software that tracks lots and allows you to tag specific coins sold. The software then produces the contemporaneous documentation you'll need if audited.

## Wash Sale Rules Don't (Yet) Apply

One key difference from stocks: the [wash-sale rule](/wash-sale/)—which prevents you from realizing a loss and immediately buying back the same security—does not officially apply to cryptocurrency as of 2024. This means you could use LIFO to harvest a loss in BTC, immediately buy BTC back, and the loss still counts.

The IRS has been unclear on this, and there's legislative movement to close the loophole, but for now, cryptocurrency wash sales are a gray area. Many tax professionals assume the rules will be extended eventually, so documenting a bona fide hold period between sale and repurchase is prudent risk management.

## Mixing Methods Across Transactions

You can use different cost basis methods for different sales—one sale FIFO, another HIFO. However, the burden of documentation grows. Most advisors recommend picking one method and sticking with it unless you have a very specific reason to deviate.

If your software or exchange doesn't support your preferred method, you're responsible for manually overriding the default and documenting your choice. Many traders who want HIFO end up doing FIFO because the friction of documentation is too high.

## See also

<div class="wiki-seealso">

### Closely related

- [Cryptocurrency Exchange](/cryptocurrency-exchange/) — where you buy and sell crypto
- [Cost Basis](/cost-basis/) — the principle applied to any investment
- [Form 8949](/form-8949/) — IRS form for reporting capital gains and losses
- [Schedule D](/schedule-d/) — tax form where gains/losses are reported
- [Long-term Capital Gain Tax](/long-term-capital-gain-tax/) — preferential rate for >1 year holdings

### Wider context

- [Tax-loss Harvesting](/tax-loss-harvesting/) — harvesting losses to offset gains
- [Tax Bracket](/tax-bracket-investor/) — how gains are taxed based on income
- [Bitcoin](/bitcoin/) — the original cryptocurrency and most-traded asset
- [Ethereum](/ethereum/) — the second-largest cryptocurrency
- [Securities and Exchange Commission](/securities-and-exchange-commission/) — US regulator (limited crypto authority currently)

</div>
