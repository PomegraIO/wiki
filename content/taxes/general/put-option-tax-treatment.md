---
title: "Put Option Tax Treatment"
description: "How the IRS taxes purchased and written put options, from premium payments through exercise, expiration, and wash-sale interactions."
keywords:
  - put option tax treatment
  - put option capital gains
  - put option expiration tax
  - wash sale put option
  - put option premium tax
image: "/svg/taxes.svg"
---

*The IRS taxes purchased and written [put options](/put-option/) as either capital transactions or ordinary gains/losses, depending on whether the option is held to expiration, sold at a profit or loss, exercised, or closed. Premium paid and received are not immediately deductible; they become [cost basis](/cost-basis/) adjustments or holding-period rules that affect the final tax outcome.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Put Option Tax Treatment — key facts</div>

<img src="/svg/taxes.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Three outcomes—expiration, sale, or exercise—each trigger different tax rules.</div>

|   |   |
|---|---|
| **Option expires worthless** | Loss equals premium paid (purchased put); written put is zero gain; both [capital losses](/long-term-capital-gain-tax/) |
| **Option sold before expiration** | Gain or loss is sale price minus premium paid (long) or minus premium received (short); typically [short-term capital](/long-term-capital-gain-tax/) |
| **Option exercised** | Purchased put: loss or gain when underlying is sold; basis includes premium. Written put: cash received when assigned; cost basis of stock includes premium received |
| **Wash sale risk** | Selling a stock at loss, then buying a put (or call) within 30 days, can disallow the stock loss; put premium paid adjusts the new stock basis |
| **Holding period** | Options have separate holding periods from underlying stock; exercise does not "tack on" option holding period to stock |

</aside>

## The Basics: Premium and Cost Basis

When you buy a [put option](/put-option/), you pay a premium—the [option premium](/option-premium/). This is not an immediately deductible expense. Instead, it becomes part of your cost basis calculation.

**Purchased Put Example:**
You buy a put option on ABC stock for a premium of $200 ($2 per share × 100 shares). You hold the option until expiration, and it expires worthless. Your tax result is a $200 capital loss (short-term or long-term, depending on how long you held the option—typically short-term, since most options expire within one year).

If you sell the put option before expiration—for example, for $500—you have a $300 gain ($500 sales proceeds minus $200 cost basis). This is a [capital gain](/long-term-capital-gain-tax/), short-term or long-term depending on your holding period.

**Written Put Example:**
You write (sell) a put option and receive a premium of $300. You do not immediately report income on that $300. Instead, it sits on your books as a contingent liability. If the put expires worthless, you have a $300 capital gain (short-term). If you buy the put back (close the position) for $100, you have a $200 gain ($300 received minus $100 paid to close).

## Option Expiration

An option that expires worthless triggers an immediate and definitive tax outcome: a capital loss (for a purchased option) or capital gain (for a written option), both typically short-term.

**Purchased Put Expires Worthless:**
Loss = Premium paid.
Holding period = From purchase to expiration date (usually less than one year → short-term loss).

**Written Put Expires Worthless:**
Gain = Premium received.
Holding period = From sale to expiration date (usually less than one year → short-term gain).

This is straightforward because the option contract is fully settled and closed. The loss or gain is final.

## Option Sale or Closure Before Expiration

You can close a position before expiration by selling (if you own) or buying back (if you wrote) the option.

**Purchased Put Sold Early:**
Gain/Loss = Sale price − Premium paid.
If purchased for $200 and sold for $500, gain is $300.

The [holding period](/holding-period/) begins on the purchase date and ends on the sale date. If held less than one year, the gain is short-term. This is a pure [capital gain](/long-term-capital-gain-tax/) or loss.

**Written Put Bought Back Early:**
Gain/Loss = Premium received − Cost to close.
If sold for $300 and bought back for $100, gain is $200.

Again, holding period is from sale date to buy-back date. Short-term or long-term depends on duration.

## Option Exercise: The Complexity

Exercise is where [put option](/put-option/) tax treatment intersects with the underlying stock, creating basis and timing subtleties.

### Purchased Put Exercised

You own a put option on ABC stock. When you exercise it, you sell 100 shares of ABC at the [strike price](/strike-price/). The tax outcome depends on whether you already owned the shares (using a put as insurance or downside protection) or acquired them to satisfy the exercise.

**Scenario 1: You already owned the stock.**
You bought ABC stock for $10,000 (100 shares at $100 each). You bought a $95 put for $200 as insurance. ABC drops to $80, and you exercise the put, selling at $95. Your proceeds are $9,500 (100 × $95).

Gain/Loss on stock sale = $9,500 (proceeds) − $10,000 (stock basis) = -$500 loss.

The $200 put premium is *not* separately deducted. Instead, your total loss is -$700 if you treat the put premium as a sunk cost, *or* you can net the $200 loss from the put expiration against the stock loss. Tax law simplifies this: the put and stock sale are two separate transactions. You have a $500 loss on the stock sale and a $200 loss on the put (treated as a loss on the expired/exercised put). Typically they're claimed separately on [Schedule D](/schedule-d/).

**Scenario 2: You acquired stock to exercise the put.**
You buy 100 shares of ABC at $85 and immediately exercise your put (strike $95), selling those shares for $9,500. Your gain is $1,500 (proceeds $9,500 minus cost basis $8,000, or $85 × 100). The put premium of $200 is factored in as part of your total cost of executing this strategy. You'd claim the stock sale gain separately from any realized gain/loss on the put itself (if the put is closed).

### Written Put Exercised (Assignment)

You wrote a put option and were assigned (meaning the buyer exercised, forcing you to buy the stock at the strike price).

You sell a put at a $95 strike for a premium of $300. ABC stock falls, and you are assigned 100 shares at $95. You must pay $9,500 to buy the shares.

Tax treatment:
- The $300 premium received *does not* trigger immediate [income tax](/corporate-income-tax/).
- Your [cost basis](/cost-basis/) in the 100 shares is $9,500 (the amount you pay) *minus* the $300 premium received. So basis = $9,200 per your records (or $92 per share).
- The holding period for the shares *starts on the assignment date*, not earlier. It does not include the time you held the short put.

When you later sell those shares, your gain/loss is calculated using the adjusted basis of $9,200 (reflecting the premium).

Example continuation:
You hold the 100 shares (basis $9,200) for 14 months, then sell at $100. Your gain is $800 ($10,000 proceeds − $9,200 basis). Since you held the shares more than 12 months, this is a long-term capital gain.

## Long-Term vs. Short-Term Gains on Options

Options themselves typically generate short-term gains or losses because:
1. Most listed options expire within one year.
2. Even if you hold an option longer than a year before selling or expiration, the IRS generally classifies option gains/losses as short-term, except in specialized cases (deep-in-the-money calls or puts used as securities substitutes under Section 1092).

When an option is exercised and results in a stock holding, the *option gain/loss* is separate from the *stock gain/loss*. The stock holding period begins on the exercise/assignment date, not the option purchase or sale date.

## Wash Sale Rules and Put Options

The [wash sale](/wash-sale/) rule (IRC Section 1091) can trap option traders: if you sell stock at a loss and buy (or acquire) substantially identical stock within 30 days before or after the sale, the loss is disallowed, and the disallowed amount adds to the cost basis of the new stock.

**Wash Sale with Put Options:**

*Scenario A: Sell stock at loss, then buy a protective put.*
You sell ABC stock at a $2,000 loss. Within 14 days, you buy a call option on ABC (or even a put on the same stock). Does the put trigger the wash sale rule?

Generally, *no*—the purchase of a put option alone is not a purchase of "substantially identical stock." However, if you subsequently *exercise* that put by acquiring stock, the wash sale rule could apply to the stock purchase in relation to the earlier sale.

*Scenario B: Sell a put (write it), then sell the underlying stock at loss.*
You write a put on XYZ stock and collect a premium. The put is exercised (or about to expire), forcing you to buy 100 shares of XYZ. Meanwhile, you own XYZ shares you bought earlier. You sell those shares at a loss. 

If the timing is within 30 days, the wash sale rule could apply: the shares you're acquiring via the assigned put (or the shares themselves) could be treated as a "purchase" of substantially identical stock, disallowing the loss on your sale.

The IRS has issued guidance that if you own or acquire substantially identical stock (or are obligated to acquire it, via a short put position) within 30 days of a loss sale, the wash sale rule applies. The cost basis of the "newly acquired" shares increases by the disallowed loss.

**Workaround:**
To avoid a wash sale when selling stock at a loss, wait 31 days before buying a protective put, or consider a put on a different stock (not substantially identical).

## Special Rules: Section 1092 (Straddles and Mixed Positions)

IRC Section 1092 imposes additional rules on "straddles"—simultaneous positions in calls and puts (or multiple calls, multiple puts) on the same underlying, designed to lock in a gain while deferring losses. 

Under Section 1092, if you hold a straddle and one side is at a loss while the other is at a gain, you may be required to defer the loss until the position is fully closed. Moreover, any loss realized must be characterized as [short-term capital](/long-term-capital-gain-tax/) loss, regardless of how long you held the position.

Example: You hold both a long call and a long put on XYZ, purchased on the same day. You sell the put at a gain but close the call at a loss in the same year. You cannot net the call loss against the put gain using straddle rules; instead, the call loss becomes short-term, and the gain on the put may also be restricted.

Section 1092 is complex and applies mainly to sophisticated hedging strategies, but traders using multiple option legs should be aware that ordinary capital-gain treatment may not apply.

## Practical Tax Reporting

Options are reported on [Schedule D](/schedule-d/) (Capital Gains and Losses). Each transaction—purchase, sale, expiration, exercise—is listed separately with:
- Date acquired
- Date sold (or expiration date)
- Cost basis (premium paid)
- Proceeds (premium received or sales price)
- Gain or loss
- Holding period (short or long)

Many brokers supply a cost-basis statement that simplifies this. However, if you execute hundreds of option trades, reconciliation and proper categorization become critical.

## See also

<div class="wiki-seealso">

### Closely related

- [Put Option](/put-option/) — structure, mechanics, and hedging uses
- [Option Premium](/option-premium/) — definition and how it affects cost basis
- [Cost Basis](/cost-basis/) — how basis is calculated and adjusted for option transactions
- [Capital Gains Tax](/long-term-capital-gain-tax/) — rates and treatment of short-term vs. long-term gains
- [Wash Sale](/wash-sale/) — interaction with option strategies and loss deferral

### Wider context

- [Schedule D](/schedule-d/) — tax form for reporting capital gains and losses
- [Covered Call](/covered-call/) — related option strategy with its own tax nuances
- [Tax Bracket](/tax-bracket-investor/) — how gains are taxed at your marginal rate
- [Option](/option/) — broader overview of calls, puts, and derivatives taxation

</div>
