---
title: "Covered Call Tax Treatment"
description: "How writing covered calls affects holding periods, qualified dividend status, and capital gains taxation when options expire, close, or are exercised."
keywords:
  - covered call tax treatment
  - covered call capital gains
  - qualified covered call
  - holding period option writing
  - covered call exercises
---

*The **covered call tax treatment** is a complex intersection of holding-period rules, premium taxation, and the qualified covered call exception. When you sell a call option against 100 shares you own, the premium you receive is income; if the call is exercised, your gain is taxed based on the holding period of the underlying shares — but that holding period can be suspended or reset by the option position itself.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Covered Call Taxation — key rules</div>

<img src="/svg/taxes.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Option premiums, holding periods, and exercise outcomes drive covered call tax liability.</div>

|   |   |
|---|---|
| **Premium received** | Ordinary income in year received (if opening call); reduces cost basis if closing call |
| **Holding period effect** | Suspended if call is [in-the-money](/in-the-money/); restarts when call closes or expires |
| **Qualified covered call** | Exception: holding period NOT suspended if call is out-of-the-money and certain conditions met |
| **Exercise taxation** | Gain = sale price − cost basis; rate depends on holding period at time of exercise |
| **Ordinary income outcome** | Possible if holding period broken; [long-term capital gain](/long-term-capital-gain-tax/) if 1+ year held before exercise |
| **Loss realization** | Short-call losses can offset long-call gains; wash-sale rules apply if re-bought within 30 days |

</aside>

## The Premium as Income

The moment you sell a [covered call](/covered-call/), you receive cash — the [option premium](/option-premium/). That premium is yours to keep, regardless of whether the call is exercised.

**In the opening transaction** (when you sell the call), the premium is ordinary income for tax purposes. If you sell a 3-month call on 100 shares of stock you own and collect $200 in premium, that $200 is taxable income in the year you sell the call, reported on [Schedule D](/schedule-d/) (if the call expires or is exercised in the same year) or deferred if the position remains open across year-ends.

**In a closing transaction** (when you buy the call back to exit the position), the premium paid reduces your basis in the call position. If you sold the call for $200 and buy it back for $150, you realize a $50 gain on the call position itself. If you buy it back for $250, you realize a $50 loss.

## Holding Period Suspension: The Core Rule

Here's where the tax code intervenes. Section 1092 imposes a harsh rule for [in-the-money](/in-the-money/) covered calls: **the holding period of the underlying stock is suspended** while you hold an [in-the-money](/in-the-money/) covered call.

Example: You buy 100 shares of XYZ on January 1 at $50, then sell a [covered call](/covered-call/) on February 1 with a $45 [strike price](/strike-price/) (it's [in-the-money](/in-the-money/) because the stock is at $48). The holding period clock stops. If you hold the shares for a full year, but the call is still open and [in-the-money](/in-the-money/) at year-end, the *tax-year holding period is not complete*. The clock only restarts when the call closes (expires worthless, is exercised, or you buy it back).

This rule can turn a [long-term capital gain](/long-term-capital-gain-tax/) into a [short-term capital gain](/long-term-capital-gain-tax/) (taxed at ordinary rates) if you're not careful.

### Why the suspension?

The IRS views an [in-the-money](/in-the-money/) covered call as economically equivalent to selling the shares. If you own XYZ at $50 and sell a $45 call, you've capped your upside. You've effectively locked in a sale near the strike. The IRS doesn't want you to:

1. Hold shares briefly, then sell an [in-the-money](/in-the-money/) call to generate an instant [long-term capital gain](/long-term-capital-gain-tax/) appearance while you wait out the clock.
2. Engineer [short-term capital gains](/long-term-capital-gain-tax/) into [long-term capital gains](/long-term-capital-gain-tax/) by layering options.

## The Qualified Covered Call Exception

The one escape hatch is the **qualified covered call** exception, introduced in the American Jobs Creation Act of 2004. If you meet all these conditions, the holding period is *not* suspended:

1. The call is **not** [in-the-money](/in-the-money/) when you sell it (i.e., the [strike price](/strike-price/) is at or above the current stock price).
2. The call is **not** deep in the money — it has genuine upside optionality for you.
3. The call expires within 12 months of sale.
4. The shares themselves have been held continuously (no closing and re-opening the shares during the call life).

If these conditions are met, the call's holding period is *not* suspended. You can sell an [out-of-the-money](/in-the-money/) call on June 1, hold the shares through June 1 of the next year, and achieve [long-term capital gain](/long-term-capital-gain-tax/) status even though the call is still open.

**Critical caveat**: "not in the money" is determined at the time of sale. If XYZ is $50 and you sell a $50 strike call, it qualifies. If XYZ then rises to $55 while the call is open, the call is *now* in the money — but the exception already applied, and the holding period remains unsuspended, assuming you don't take action to violate the conditions.

## Taxation When the Call Expires Worthless

If the stock stays below the [strike price](/strike-price/), the call expires worthless. You pocket the premium, the shares remain yours, and the holding period resumes from where it left off (or continues uninterrupted, depending on whether the exception applied).

The premium is ordinary income. The shares are taxed when you eventually sell them.

## Taxation When the Call Is Exercised

If the call finishes [in-the-money](/in-the-money/) on expiration and is exercised (or you are assigned early), you must sell 100 shares at the [strike price](/strike-price/).

Your [capital gain](/capital-gains-tax-investor/) or loss is:

**Gain/Loss = Strike Price × 100 − Cost Basis**

If you bought at $50 and sold a $55 call that is exercised, you get $5,500 in proceeds (excluding the premium already collected). Your basis is whatever you paid for the shares. Gain is taxed at [long-term](/long-term-capital-gain-tax/) or [short-term](/long-term-capital-gain-tax/) rates depending on your holding period.

**Holding period matters**: If the call was [in-the-money](/in-the-money/) and suspended your holding period, you may have a [short-term capital gain](/long-term-capital-gain-tax/) even if you held the shares for years.

**The premium adjusts the calculation**: The premium you received earlier is separately taxable income (in the year you sold the call). The sale price of the shares is the strike price. The call premium is *not* added to the strike price to calculate gain; it's already been reported as ordinary income.

Example:
- Buy 100 shares at $50 on January 1, Year 1.
- Sell a [covered call](/covered-call/) on January 15, Year 1, strike $55, collect $200 premium. Call is out-of-the-money.
- Premium is ordinary income in Year 1.
- Call is exercised in March, Year 1 (stock at $56).
- Proceeds: $5,500. Cost basis: $5,000. Gain: $500.
- Holding period: ~2.5 months — less than 1 year.
- Tax: $500 at [short-term capital gains](/long-term-capital-gain-tax/) rates (ordinary rates) + $200 premium as ordinary income = $700 ordinary income total.

If you'd held the shares for over a year *before* selling the call (and sold a qualified covered call), the $500 gain would be [long-term capital gain](/long-term-capital-gain-tax/).

## Buying Back the Call: Closed Positions

If you buy back (close) the [covered call](/covered-call/) before expiration, you realize a gain or loss on the call position itself. This is a standalone [capital gain](/capital-gains-tax-investor/) or loss, reported separately on [Schedule D](/schedule-d/).

- Sold the call for $200, buy it back for $150: $50 short-term [capital gain](/capital-gains-tax-investor/).
- Sold the call for $200, buy it back for $250: $50 [capital loss](/capital-gains-tax-investor/).

The shares' holding period resumes (if it was suspended).

## Dividends and Qualified Dividend Income

A [covered call](/covered-call/) does not typically disqualify [dividends](/dividend/) paid on the underlying shares from [qualified dividend](/qualified-dividend/) treatment (assuming the shares themselves satisfy the holding period requirement). However, if you sell a call with a very short maturity or roll calls continuously, the IRS may challenge whether you truly "own" the stock for economic purposes.

If you sell a call that covers an ex-dividend date and the call is exercised just after, you've locked in the sale before collecting the dividend. The ex-dividend holder of record gets the dividend, but you're the one selling the shares. Timing matters.

## Wash-Sale Rules and Covered Calls

If your [covered call](/covered-call/) expires worthless and you immediately sell the underlying shares at a loss, the wash-sale rule applies: you cannot deduct the loss if you repurchase the same or substantially identical stock within 30 days before or after the loss sale.

Similarly, if you close the call at a loss and buy back the underlying shares within 30 days, the loss on the call position may be disallowed as a wash sale (though case law is murkier here — the call and the stock are not identical).

## Form 8949 and Schedule D Reporting

Covered call gains and losses are reported on [Form 8949](/form-8949/) (Sales of Capital Assets) and [Schedule D](/schedule-d/). Each lot of shares is a separate transaction. The holding period, cost basis, and sale date must be accurate.

If the call is exercised, the transaction date is the assignment date. If the call expires worthless, the holding period may reset mid-year, complicating multi-year tracking.

## See also

<div class="wiki-seealso">

### Closely related

- [Covered Call](/covered-call/) — the option strategy creating these tax situations
- [Long-Term Capital Gain Tax](/long-term-capital-gain-tax/) — preferential rate at stake with holding periods
- [Schedule D](/schedule-d/) — form for reporting [capital gains](/capital-gains-tax-investor/) and losses
- [Option Premium](/option-premium/) — the income received when selling calls
- [In-the-Money](/in-the-money/) — the key condition triggering holding-period suspension

### Wider context

- [Capital Gains Tax (Investor)](/capital-gains-tax-investor/) — overview of gain and loss taxation
- [Wash Sale](/wash-sale/) — rule preventing loss deductions on rapid repurchases
- [Form 8949](/form-8949/) — detailed reporting vehicle for option transactions
- [Qualified Dividend](/qualified-dividend/) — treatment of dividend income (largely unaffected by calls)
- [Tax Loss Harvesting](/tax-loss-harvesting/) — strategy for managing call-related losses

</div>
