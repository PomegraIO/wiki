---
title: "How Crypto Options Are Taxed"
description: "Crypto options trigger tax events when purchased, exercised, or expired. Learn the difference between opening, closing, and exercise transactions and how to calculate gains and losses."
keywords:
  - crypto options tax
  - cryptocurrency options taxation
  - options exercises taxable event
  - crypto tax reporting
  - virtual currency options
---

*Taxing **crypto options** follows the same general framework as equity options in most jurisdictions, but with a critical caveat: crypto is treated as property (not securities in the U.S.), and each transaction—buy, sell, exercise, expiration—triggers a taxable gain or loss. Understanding when and how much tax is owed requires tracking basis, exercise prices, and the timing of asset sales.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Crypto options tax — key facts</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Options create taxable events at purchase, exercise, closure, and expiration.</div>

|   |   |
|---|---|
| **Taxable events** | Buying, selling, exercising, and letting expire (all recognized) |
| **Holding period** | Depends on the underlying crypto asset, not the option itself |
| **Cost basis** | Premium paid + exercise price when exercised |
| **Long-term vs short-term** | Determined by when you acquired the underlying crypto after exercise |
| **Expiration worthless** | Capital loss in the year of expiration |
| **Exercise treatment** | Immediate tax-deferred swaps (under current IRS guidance) |
| **Regulatory regime** | U.S. IRS treats options and underlying as separate property; UK, Canada vary |

</aside>

## Tax Events: When You Owe Tax on Crypto Options

A crypto option triggers tax obligations at four moments: **purchase, sale/closure, exercise, and expiration**. Each event may generate a capital gain or loss.

### Buying an Option

When you purchase a crypto option (call or put), you immediately owe tax on any capital gain or loss if the option itself increases or decreases in value. Most traders do not sell their options separately; instead, they hold to exercise or let expire. If you do sell an option position before exercise or expiration, the difference between the premium paid and the premium received is a **capital gain or loss**, taxed as short-term (if held less than one year) or long-term (if held more than one year).

Practically speaking, most retail traders do not separately track and report the sale of individual option positions, but if you are actively trading options on a platform that reports transactions, each sale is a taxable event.

### Exercising an Option

When you exercise a call option (buying the underlying crypto) or a put option (selling the underlying crypto), the transaction is typically treated as a **property exchange**, not as a separate sale of the option. Under current U.S. IRS guidance and most tax software interpretations:

- **For a call:** You convert the premium paid plus the strike price into a cost basis for the underlying crypto. If you exercise a call to buy 1 Bitcoin at a strike of $30,000 after paying a $2,000 premium, your cost basis in that Bitcoin is $32,000.
- **For a put:** You sell the underlying crypto at the strike price. If you exercise a put to sell 1 Bitcoin at a strike of $40,000, you realize any gain or loss relative to your prior cost basis in that Bitcoin, plus you recover the premium paid (which reduces the effective sale proceeds).

Exercising itself does **not** trigger an immediate tax bill on the option premium; instead, the premium becomes part of your basis in the underlying asset. Tax is deferred until you later sell the underlying crypto.

### Letting an Option Expire Worthless

If an option expires unexercised and worthless, the premium you paid is a **capital loss** in the year of expiration. If you paid $2,000 for a Bitcoin call option and it expires worthless, you can claim a $2,000 capital loss, reducing your overall capital gains or offsetting ordinary income (up to $3,000 per year under U.S. rules).

This is where tracking becomes critical: if you cannot document the purchase date and cost, the IRS may disallow the loss. Use your exchange statements or trading records to prove the premium paid and the expiration date.

### Closing a Position Before Expiration

If you sell an option before it expires, the difference between the premium paid and the premium received is a **capital gain or loss**, taxed in the year of the sale. For example:

- You buy a Bitcoin call for $2,000.
- Two weeks later, you sell the same call for $5,000 (because Bitcoin rallied and the option is now in-the-money).
- You report a $3,000 short-term capital gain on the sale of the option.

This is separate from any future gain or loss on the underlying Bitcoin, and it is taxable even if you never exercise the option.

## Holding Period: Option Duration vs. Underlying Duration

A crucial detail: **the holding period of the option does not transfer to the underlying asset**. Holding a call option for a year and then exercising it does not make the underlying crypto long-term.

When you exercise a call and acquire the underlying crypto, your holding period in that crypto starts on the **exercise date** (or the settlement date, depending on the exchange), not the purchase date of the option. If you exercise in January 2025 and sell the underlying crypto in February 2025, you have a short-term gain even though you held the option longer.

The premium paid for the option is added to your cost basis but does not affect the holding period of the underlying asset. This is a key difference from some other investment contexts and a common source of confusion.

## Cost Basis and Exercise Price: The Full Cost

Your cost basis in the underlying crypto acquired by exercising an option includes both the premium paid and the strike price.

**Example:**
- You buy a call option on Ethereum for 0.5 ETH strike at $2,000, paying a premium of $500.
- You exercise the call.
- Your cost basis in the 0.5 ETH is $2,000 (strike) + $500 (premium) = $2,500, or $5,000 per full ETH.

Later, if you sell that Ethereum at $3,000 per ETH, your gain is calculated as:
- Sale proceeds: 0.5 ETH × $3,000 = $1,500
- Cost basis: $2,500
- Capital loss: −$1,000

The option premium is not deductible separately; it is capitalized into the cost basis. This means you cannot double-count the tax: once the premium increases your cost basis, it does not create a separate loss if the underlying asset declines.

## Wash-Sale Rules and Crypto Options

The IRS wash-sale rule (which disallows losses if you re-acquire a substantially identical asset within 30 days) applies to crypto but with some ambiguity regarding options.

If you sell a Bitcoin at a loss and then buy a Bitcoin call option within 30 days, the IRS could argue that the option is a "substantially identical" position, disallowing your loss. Similarly, if you let a call option expire worthless (realizing a loss) and buy another call on the same asset within 30 days, a disallowance risk exists.

Practical traders often use options strategically to avoid wash-sale traps: selling a Bitcoin position at a loss and immediately buying a call (which is not Bitcoin but an option on Bitcoin) can create ambiguity. However, relying on this ambiguity is risky and audit-prone. Conservative approach: avoid re-entering an identical or substantially identical position within 30 days if you want to lock in a loss.

## Reporting Crypto Options on Tax Forms

In the U.S., crypto options are reported on **Form 8949 (Sales of Capital Assets)** alongside other [capital gains](/capital-gains-tax-investor/) and losses. The reporting depends on whether you are using specific lot identification (tracking which purchase/exercise relates to which sale) or averaging cost basis.

For options, most traders use specific lot identification because each option exercise creates a separate cost basis event. When you exercise a call and later sell the underlying crypto, you trace that sale back to the exercise date (not the option purchase date) to determine the holding period.

If you are reporting through tax software, you may need to manually enter options transactions because many platforms and integrations are incomplete. Keep detailed records:
- Option purchase date and premium paid.
- Exercise date, strike price, and quantity of underlying acquired.
- Sale date of underlying and sale price.

The cost basis (strike + premium) is then matched to the underlying asset, and the gain or loss is calculated from the sale price.

## Spreads and Multi-Leg Strategies

Traders often use spreads (e.g., buying a call and selling a call at a higher strike). Each leg is a separate transaction:

- Buying the long call: premium paid.
- Selling the short call: premium received.
- Each generates its own capital gain or loss when closed or when the strategy is exercised.

If both legs are closed at the same time (e.g., the spread is closed out for a net debit or credit), the net gain or loss is the difference between the premiums. However, if the legs are closed separately, each is tracked as an independent transaction.

This complexity is why professional traders often use specialized crypto tax software that breaks down multi-leg strategies into individual components and reports them correctly.

## Jurisdictional Differences

Taxation of crypto options varies globally:

- **United States**: Property treatment; each transaction taxable. Premium added to cost basis on exercise. Short-term and long-term treatment based on holding period of underlying.
- **United Kingdom**: Options are treated as disposals under capital gains tax. Exercise is a disposal of the option and a separate acquisition of the underlying.
- **Canada**: Similar to the U.S.; options are property. Exercise is a disposition of the option and purchase of the underlying, with cost basis adjustments.
- **Australia**: Capital gains tax applies; exercise of options is treated as a CGT event (acquiring the underlying asset at cost basis = strike + premium).
- **Singapore**: Capital gains are generally not taxed, so options exercises are not taxable events (though this depends on the trader's status and intent).

Check your local tax authority's guidance before relying on U.S. rules if you are domiciled elsewhere.

## Documentation and Audit Risk

The single largest risk for crypto options traders is poor record-keeping. Unlike equities, which trade on centralized exchanges with standardized reporting, crypto options are often traded on decentralized platforms, over-the-counter, or on less-regulated exchanges. Platforms may not issue tax documents automatically.

If you cannot document:
- The purchase date and cost of the option.
- The exercise date and strike price.
- The sale date and sale price of the underlying (if exercised and sold).

The IRS or your tax authority may disallow losses or assess penalties. Keep:
- Screenshots of option purchases and sales.
- Exchange confirmations and trade statements.
- A spreadsheet tracking option exercises and the subsequent sale of underlying assets.

For large or frequent traders, crypto-specific tax software (e.g., ZenLedger, CoinTracker, Koinly) can integrate with exchanges and build a transaction ledger automatically, reducing the risk of omissions.

## See also

<div class="wiki-seealso">

### Closely related

- [Capital gains tax](/capital-gains-tax-investor/) — Tax on profit from selling investments
- [Tax loss harvesting](/tax-loss-harvesting/) — Using losses to offset gains
- [Cost basis](/cost-basis/) — Purchase price determining gain/loss on sale
- [Option](/option/) — Right to buy or sell an asset at a fixed price
- [Cryptocurrency exchange](/cryptocurrency-exchange/) — Platforms where options are traded

### Wider context

- [Schedule D](/schedule-d/) — IRS form reporting capital gains and losses
- [Form 8949](/form-8949/) — IRS form detailing individual asset sales
- [Wash sale](/wash-sale/) — IRS rule disallowing losses on rapid repurchases
- [Holding period](/holding-period/) — Duration determining short-term vs. long-term tax rates
- [Tax bracket](/tax-bracket-investor/) — Marginal rate applied to investment gains

</div>
