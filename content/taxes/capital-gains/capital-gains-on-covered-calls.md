---
title: "Capital Gains on Covered Calls"
description: "How premium from covered calls is taxed, how exercise or expiration determines capital gain character, and holding-period traps for covered call writers."
keywords:
  - capital gains on covered calls
  - covered call taxation
  - option premium tax
  - short-term capital gains
  - holding period
  - investment income
---

*The tax treatment of **capital gains on covered calls** is surprisingly nuanced: the premium you receive is not immediately taxed as income, but the way the position unwinds—exercise, expiration, or assignment—determines whether your gain is short-term or long-term, and can even reset your holding period for the underlying stock.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Covered Call Taxation — key facts</div>

<img src="/svg/taxes.svg" alt="An abstract editorial mark for tax topics." />

<div class="wiki-infobox-caption">Premium is not ordinary income; exercise and assignment control the ultimate gain character.</div>

|   |   |
|---|---|
| **Premium received** | Not immediately taxable as income; part of your proceeds when position closes |
| **If stock assigned** | Your sale proceeds = strike price + premium; gain is short-term or long-term based on your holding period of the stock |
| **If call expires worthless** | Premium is short-term capital gain; you keep the stock and its original holding period |
| **If you close the call early** | Depends on profit or loss on the option itself; complicated by wash-sale rules |
| **Holding period reset** | Assigning a covered call does NOT reset your stock holding period (common misconception) |
| **Documentation** | Report on Form 8949 and Schedule D |

</aside>

## How premium is initially treated

When you write a [covered-call](/covered-call/), the premium you receive is not wages, dividends, or ordinary income. It is part of the proceeds of your eventual transaction—either the sale of the stock via assignment, or income from expiration.

This is a critical distinction. Many writers mistakenly believe the premium is taxable immediately as short-term income. It is not. The premium sits, unrecognized, until the position is closed.

Think of it this way: you own 100 shares of a stock and sell a call option. You receive $200 in premium. That $200 does not show up on your 1099 or as ordinary income in April. Instead, it is part of the calculation of your capital gain when the position ends.

## Assignment and long-term capital gains

The most common outcome is assignment. Your shares are called away at the strike price, and the transaction closes. Your proceeds equal the strike price plus the premium you collected.

Your capital gain or loss is calculated as:

**Gain = (Strike Price + Premium + Any Other Income) − Original Purchase Price**

The character of that gain—whether it is short-term or long-term—depends on how long you held the stock, not how long the option was outstanding.

Suppose you bought 100 shares of XYZ at $50 a share, held it for 14 months, then sold a 30-day call for a $200 premium, strike $60. If assigned, your total proceeds are ($60 × 100) + $200 = $6,200. Your gain is $1,200. Because you held the stock for more than a year, this is a [long-term-capital-gain-tax](/long-term-capital-gain-tax/), taxed at favorable rates (0%, 15%, or 20%, depending on income).

If you had bought those shares only 6 months prior to assignment, the same $1,200 gain would be short-term capital gains, taxed as ordinary income at rates up to 37%.

The timing of the call is irrelevant to this calculation. A 30-day call or a 6-month call makes no difference. Your holding period is measured from purchase to assignment.

## Expiration and the short-term gain

If the [covered-call](/covered-call/) expires worthless (stock price stays below strike at expiration), you keep the stock. The premium, $200, becomes a short-term capital gain. You realize that profit immediately and must report it, but the stock remains yours with its original holding period intact.

In the example above, if XYZ stock falls to $55 at call expiration, the call expires, you pocket the $200 premium as a short-term gain, and you still own the stock with its 14-month holding period. You have converted part of your upside into a short-term gain while retaining long-term upside potential.

This is a deliberate trade-off. By capping your upside, you generate immediate short-term income. If you later sell the stock at a profit, that additional gain might be long-term, offsetting the short-term premium gain in your overall tax picture.

## Early exit and wash-sale complications

Suppose you sell the [covered-call](/covered-call/) for a profit before expiration. If the call is trading for $50 and you bought it back for $50 less, you have a $50 gain on the option. That is treated as a short-term capital gain, regardless of how long you held the call.

But things get complicated if you close the call at a loss. If you bought the call back for more than you sold it for, you have a short-term capital loss. That loss can offset other gains, but it also triggers [wash-sale](/wash-sale/) risk if you repurchase a call on the same or similar stock within 30 days.

Similarly, if you sell your stock early—before the call is assigned—you are realizing your capital gain on the stock. That gain's character depends on your holding period. The premium is factored in as additional proceeds.

## The holding-period reset myth

A common misconception is that assignment of a covered call resets your holding period on the stock. This is false. Once your shares are called away, you no longer own them, and there is nothing to reset. Your holding period for *that* position ended at assignment.

However, if you immediately buy 100 shares of the same stock post-assignment, that is a brand-new position with a brand-new holding period clock. Some investors confuse this with a holding-period reset.

If you want to continue a long-term holding period without interruption, you must not write calls that are likely to be assigned, or you must accept that assignment ends the position.

## Tax-loss harvesting and covered calls

Some investors use covered-calls to harvest tax losses. You own a losing position, sell a call to collect premium, and hope the call expires so you can claim the loss while capturing some income from the call.

But be careful: if the stock drops and the call expires, you have a capital loss on the stock (deductible against gains) and a short-term capital gain from the expired call. The net may be favorable, but you must track both legs separately on Form 8949.

Additionally, if you buy back the stock within 30 days of realizing the loss, the wash-sale rule disallows the loss. Writing a call does not prevent wash-sale; the purchase of replacement shares does.

## Reporting and documentation

When a covered call is assigned, your broker reports the transaction as a stock sale on Form 1099-B. The proceeds include both the strike price and the premium. You must then determine your [cost-basis](/cost-basis/) in the stock—typically purchase price per share—and calculate the gain.

Use [Form 8949](/form-8949/) to list each covered-call assignment and any expiration or closing transactions. Transfer the totals to [Schedule D](/schedule-d/) and then to Form 1040.

If your covered call is assigned and you immediately buy back the same stock, be extremely careful not to trigger a wash sale if there is an unrealized loss from your original purchase date to the assignment date. The IRS has issued guidance allowing covered-call assignment to avoid wash-sale complications in some cases, but documentation is essential.

## See also

<div class="wiki-seealso">

### Closely related

- [Covered Call](/covered-call/) — The strategy and mechanics
- [Long-Term Capital Gain Tax](/long-term-capital-gain-tax/) — Preferential tax rates on long-term gains
- [Cost Basis](/cost-basis/) — How to calculate gain or loss on sale
- [Form 8949](/form-8949/) — IRS form for reporting capital gains and losses
- [Schedule D](/schedule-d/) — Summary of capital gains and losses
- [Wash Sale](/wash-sale/) — Restriction on deducting losses if you buy similar security within 30 days
- [Tax Lot](/tax-lot/) — Tracking cost basis for specific share lots

### Wider context

- [Option Premium](/option-premium/) — What you receive for selling an option
- [Strike Price](/strike-price/) — The contractual price at which covered calls are exercised
- [Capital Gains Tax Investor](/capital-gains-tax-investor/) — Overview of capital gains taxation
- [Tax-Loss Harvesting](/tax-loss-harvesting/) — Using losses to offset gains

</div>
