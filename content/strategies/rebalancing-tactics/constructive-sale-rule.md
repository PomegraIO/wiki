---
title: "Constructive Sale Rule"
description: "Tax rule triggering gain recognition when substantially identical position is taken while holding original position"
keywords:
  - constructive sale
  - wash sale
  - tax loss harvesting
  - gain recognition
  - offsetting positions
---

*The **constructive sale rule** (Internal Revenue Code Section 1092) is a tax provision that forces an investor to recognize a gain on an appreciated security if, while still holding the original security, the investor enters into a substantially identical offsetting position. The rule is designed to prevent investors from having their cake and eating it too: holding appreciated stock for long-term capital gains treatment while synthetically selling it (via short sales, puts, calls, or futures) to lock in gains without triggering a taxable event.*

<aside class="wiki-infobox">

| Aspect | Details |
|---|---|
| **Trigger** | Substantially identical offsetting position taken while holding appreciated security |
| **Result** | Gain recognition on constructive sale date, even if original position remains open |
| **Holding period** | Resets for the new offsetting position |
| **Tax rate** | Long-term capital gains rate if 12+ months in original security |
| **Examples of offense** | Short sale, short call, long put, short futures, collar |
| **Timing** | Recognition occurs on date of constructive sale, not liquidation |
| **Exceptions** | Qualified covered calls (narrow exception); diversified securities |
| **Penalty** | Gain recognized; no loss can offset it from the transaction |

</aside>

## Why constructive sale rules exist: the hedging problem

Imagine you own 1,000 shares of Apple purchased five years ago at $50/share, now worth $150/share. You have a $100,000 gain. You want to lock in that gain (protect against downside) but defer the tax. In the early 1990s, investors found a way: short 1,000 shares of Apple at $150/share.

Now you are economically flat—long 1,000 at $150, short 1,000 at $150. Your gain is locked in, and you have zero downside exposure. But you have not sold the original shares, so you have not triggered a taxable event. The original shares can still sit for another few years, and when you close the short sale, you can claim long-term capital gains treatment on the $100,000 gain.

The IRS saw this and objected. Congress passed the constructive sale rule in 1997 (in the Taxpayer Relief Act) to close this loophole. The rule says: if you take a substantially identical offsetting position while holding the original appreciated security, you are deemed to have "constructively sold" the original security on the date you took the offset. You must recognize the gain immediately.

## How the rule works in practice

**Triggering transaction:** You own appreciated Microsoft stock and sell short an identical number of Microsoft shares (or equivalent via options/futures). The constructive sale rule is triggered on the date of the short sale, not on the date you close the short sale or liquidate the original long position.

**Gain recognition:** You immediately recognize long-term capital gain (if you held the original for 12+ months) equal to the difference between the cost basis and the fair market value on the constructive sale date. This is true even if you never actually liquidate the position.

**Holding period reset:** The holding period for the new offsetting position (the short sale) starts fresh on the constructive sale date. If you hold the short for another year and then cover it, you might qualify for long-term treatment on any gain on the short position itself (which would typically be a loss, because you shorted high).

**Example:** 
- Year 1: Buy 100 MSFT shares at $100/share, cost basis = $10,000
- Year 5: MSFT trades at $200/share. Unrealized gain = $10,000
- Day X (Year 5): Short 100 MSFT shares at $200/share
- **Constructive sale triggered:** You must recognize a $10,000 long-term capital gain on Day X, even if you never close the short sale

## What triggers constructive sale: substantially identical offsets

The rule applies to substantially identical offsets. Transactions that trigger the rule include:

- **Short sale** of the same security
- **Short call** on the security (short equity call option)
- **Long put** on the security purchased (protective put is an exception; see below)
- **Short sale of a call** combined with long put (a "collar" is usually constructive)
- **Futures contracts** that are substantially identical to the underlying security
- **Securities futures contracts** on the underlying
- **Forward contracts** to sell the same security

Transactions that do **not** trigger the rule:

- **Protective put** (long put on long stock, narrow exception for "qualified covered calls")
- **Protective put (qualified call)** — A covered call written on stock you own may be excluded from the rule if it is a "qualified covered call": the strike price is at or above the stock price, it expires within 12 months, and it does not have in-the-money components that are deemed to be offsetting

The "qualified covered call" exception is narrow and often misunderstood. Most covered calls written by individual investors do not meet the criteria and could trigger the constructive sale rule.

## The collar scenario: a common constructive sale trap

A **collar** is a popular hedging strategy: you own appreciated stock, you buy a put (downside protection) and sell a call (upside protection). This locks in a range of outcomes. However, the collar is typically treated as a constructive sale because the long put and short call together create a substantially offsetting position.

Example:
- Own 100 shares of Disney at $100/share; currently worth $150/share
- Buy a 140 put (pay $2 per share, or $200 total): protects against losses below $140
- Sell a 160 call (receive $3 per share, or $300 total): caps gains above $160

You now have limited upside (capped at $160) and limited downside (floored at $140). This is economically similar to owning a $140 call and being short a $160 call, which resembles a short sale. The IRS treats this as a constructive sale.

**Exception:** If the put strike and call strike are both out-of-the-money and the collar has sufficient spread (15%+ or other conditions), it may be treated as a qualified covered call and escape constructive sale treatment. The IRS has specific guidelines; many collars do not meet them.

## Diversified securities exception

There is a narrow exception for holders of "diversified securities"—investors owning a broad, diversified portfolio where no single position is large. If you own 100 different stocks and hedge your long position in one of them via a short sale, the constructive sale rule may not apply to that individual position because your overall portfolio is diversified. This exception is so narrow it is rarely used.

## Avoiding the rule: tax-loss harvesting strategies

Investors use two main strategies to harvest losses without triggering constructive sales:

**Scenario 1: Harvest loss, wait, then repurchase.** If you own XYZ stock at a loss, you can sell it to realize the loss. To repurchase XYZ without triggering a [wash sale](/wiki/wash-sale/), you wait 31 days. The constructive sale rule does not apply because you have no offsetting position during the 31-day window.

**Scenario 2: Hedge with a non-identical security.** If you own Apple, you can short a different tech stock (Microsoft) or buy a sector ETF short. This is not substantially identical, so no constructive sale is triggered. You achieve some downside protection without selling or synthetically selling the original position. The offset is imperfect, but it avoids the tax trigger.

**Scenario 3: Use options outside the rule.** A long put on the stock does not trigger the constructive sale rule per the "protective put" exception, provided the put is not part of a broader collar and the structure meets technical requirements. However, many protective puts in practice are part of a collar that does trigger the rule.

## Interaction with wash sale rule

The [wash sale rule](/wiki/wash-sale/) (IRC Section 1091) disallows loss deductions if you repurchase a substantially identical security within 30 days before or after a sale. The constructive sale rule is the inverse: it recognizes gains that you are trying to defer. The two rules work in tandem to prevent sophisticated hedging from displacing tax timing.

## Reporting and compliance

When a constructive sale occurs, the taxpayer must report the gain on Form 8949 (Sales of Capital Assets) and Schedule D (Capital Gains and Losses). The gain is recognized in the tax year in which the constructive sale occurs, even if the taxpayer never liquidates the original position or the offsetting position.

Failure to report a constructive sale correctly can result in understatement of income, penalties, and interest. The IRS has targeted aggressive hedging strategies, and many audits of high-income investors focus on potential constructive sales that were not reported.

<div class="wiki-seealso">

### Closely related
- [Wash Sale](/wiki/wash-sale/) — Loss disallowance on substantially identical repurchase
- [Capital Gains Tax](/wiki/capital-gains-tax-investor/) — Tax on investment gains
- [Tax Loss Harvesting](/wiki/tax-loss-harvesting/) — Strategy to deduct investment losses
- [Short Sale](/wiki/short-selling/) — Selling borrowed securities; common constructive sale trigger

### Wider context
- [Options Strategies](/wiki/option/) — Hedging tools including collars and puts
- [Hedge Fund](/wiki/hedge-fund/) — Institutions using hedges extensively
- [Derivative Tax](/wiki/crypto-derivative-tax/) — Tax treatment of derivative positions
- [Alternative Minimum Tax](/wiki/alternative-minimum-tax-investor/) — Related tax compliance issue

</div>
