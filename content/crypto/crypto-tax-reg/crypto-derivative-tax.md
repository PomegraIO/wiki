---
title: "Crypto Derivative Tax"
description: "Tax treatment of futures, options, swaps, and other derivative contracts on cryptocurrency under U.S. and international law."
keywords:
  - crypto derivatives
  - section 1256 contracts
  - capital gains tax
  - wash sale rules
---

*The tax treatment of crypto derivatives—[futures](/wiki/currency-futures/), [options](/wiki/options-crypto/), and swaps on Bitcoin, Ethereum, and other cryptocurrencies—differs significantly from the tax on spot cryptocurrency holdings. Futures traded on regulated exchanges enjoy special treatment, while OTC derivatives face ordinary [capital gains tax](/wiki/capital-gains-tax/) rules.*

<aside class="wiki-infobox">

| Derivative Type | IRS Treatment | Tax Rate | Reporting |
|---|---|---|---|
| CME Bitcoin Futures | Section 1256 (60% long-term / 40% short-term) | 15%–37% blended | Form 6252 |
| OTC Options (calls, puts) | Capital gains or ordinary income | 0%–37% (same as spot crypto) | Schedule D |
| Crypto-Crypto Swaps | Unclear; likely ordinary income | 0%–37% | Case-by-case |
| Perpetual Futures (centralized exchange) | Ordinary income | 0%–37% | Schedule D (if reported) |
| Crash Derivatives (puts, short calls) | Same as underlying option type | Varies | Schedule D |

</aside>

## Section 1256 futures and the 60/40 blended rate

When the CME launched Bitcoin and Ethereum futures in December 2017 and February 2021 respectively, the IRS classified them as [Section 1256 contracts](/wiki/mark-to-market/)—a specific class of derivatives that receive preferential tax treatment. These are listed, regulated futures on a U.S. exchange.

The magic of Section 1256 is the "60/40" treatment: regardless of how long you hold the contract, 60% of gains are taxed as long-term capital gains and 40% as short-term capital gains. If you buy a Bitcoin futures contract on Monday and sell it on Tuesday for a $10,000 profit, the IRS treats $6,000 as a long-term gain (taxed at 15% or 20% depending on income) and $4,000 as a short-term gain (taxed at ordinary income rates of up to 37%). This results in an effective blended rate of around 24% federally for most traders, far better than the 37% you'd pay on short-term spot crypto gains.

Furthermore, Section 1256 contracts are [marked-to-market](/wiki/mark-to-market/) on December 31st each year. If you hold a contract that's up $50,000 at year-end, the IRS treats that as a realized gain in that calendar year, even if you don't sell. You owe tax on the gain and must file [Form 6252](/wiki/form-w-2g/) (or Form 8949 + Schedule D). This prevents year-end deferral games but forces disciplined year-end tax planning.

## OTC options and the ordinary capital gains treatment

Options contracts bought or sold on over-the-counter (OTC) markets—bilateral deals between you and a broker, not exchange-traded—do not qualify for Section 1256 status. If you buy a call option on Bitcoin and exercise it, or sell it for a gain, that gain is treated as ordinary [capital gains](/wiki/capital-gains-tax/). If you held the option less than a year, it's short-term capital gain (taxed at up to 37%). If longer, it's long-term (taxed at up to 20%).

The distinction between exchange-traded and OTC is critical. An [options contract](/wiki/option-premium/) on the CME Bitcoin Futures contract might qualify for Section 1256; an options contract on a centralized crypto exchange (where you're trading with the exchange, not a listed instrument) almost certainly does not. The IRS has not issued clear guidance on crypto options that are exchange-traded but not on a U.S.-regulated exchange.

A practical issue: many OTC derivatives are not settled in a taxable event for tax reporting purposes. If you hold a [perpetual futures](/wiki/futures-contract/) position on a centralized exchange (Bybit, OKX, Binance) with no closure or settlement, have you realized a taxable gain? The tax code isn't definitive. Most tax advisors treat unrealized gains as potentially taxable if the position is marked-to-market by the platform, but enforcement is patchy because these exchanges are largely outside U.S. regulatory perimeter.

## Wash sale rules and their limits

The [wash sale rule](/wiki/wash-sale/) prevents you from selling an asset at a loss and immediately repurchasing a substantially identical asset to harvest the loss for tax purposes. Does the wash sale rule apply to crypto derivatives? The IRS has not issued final guidance.

Arguments both ways: (1) Bitcoin futures are substantially identical to spot Bitcoin, so selling futures at a loss and buying spot Bitcoin (or vice versa) might trigger the wash sale rule, disallowing the loss; (2) futures and spot are different assets—one is a derivative contract, the other is a commodity—so wash sale does not apply.

Conservative tax advisors assume wash sale applies and recommend waiting 30 days before repurchasing after a derivative loss. Aggressive traders assume it doesn't and harvest losses freely. The IRS has not clarified the matter, leaving a compliance gray zone. If challenged, a trader without a documented tax position would face a difficult audit.

## Staking rewards and option settlement

If you receive a [crypto derivative](/wiki/crypto-derivative-tax/) as a settlement—for example, you sell a call option that expires in-the-money and are assigned 1 Bitcoin—what is your basis? You inherited the Bitcoin at the strike price (the exercise price of the option) plus any premium you paid for the option you sold. Your holding period for that Bitcoin starts at the settlement date, not at the origination date of the option.

Crypto-to-crypto derivatives, like a swap of Ethereum for Bitcoin, are trickier. A swap is a bilateral exchange of cryptocurrencies at an agreed ratio. The IRS arguably treats each leg as a separate transaction: you've disposed of Ethereum (a taxable event) and received Bitcoin (a new asset). The gain or loss on Ethereum is the difference between its fair market value at swap execution and your basis. The Bitcoin's basis is its fair market value at execution, with a holding period starting that day.

Many crypto traders execute swaps without tax tracking, assuming the wash sale rule (or tax deferral) applies. It does not. Each swap is likely two taxable transactions, and swaps between crypto and crypto are never tax-deferred.

## Perpetual futures and daily settlement ambiguity

On centralized crypto exchanges, perpetual futures are synthetic instruments that behave like futures but are settled daily through funding rates (the exchange pays you or charges you to keep the contract open). The IRS classification is unclear: are they Section 1256 contracts? Ordinary capital gains? Or are gains/losses on each funding payment separately taxable?

A reasonable reading is that perpetual futures are *not* Section 1256 contracts because they're not listed on a U.S. regulated exchange (the CME, CBOT, or NYMEX). They'd be taxed as ordinary capital gains. If you hold a perpetual futures position for a month and the price moves 10% in your favor, that gain is taxable income when you close the position. If the exchange has automatic liquidation (e.g., if your margin falls below a threshold), is that a forced realization? Probably yes, though some exchanges offer margin preservation mechanisms that muffle the event.

## Cost basis tracking and the lack of infrastructure

Unlike stock brokers, most crypto exchanges and OTC derivatives brokers do not provide tax reporting forms. The IRS requires Form 1099-B for brokered transactions, but crypto exchanges largely avoid issuing them. A trader using Bybit, Deribit, or OKX perpetual futures has almost no official tax documentation. They must build their own cost-basis ledger from exchange statements and self-report.

This creates enforcement risk. The IRS increasingly flags traders with large crypto trading volumes but minimal reported income. Conversely, a trader who files a meticulous Schedule D with every trade documented is less likely to face scrutiny than one who reports nothing.

## International and non-U.S. exchange considerations

A U.S. citizen trading crypto derivatives on foreign exchanges (not the CME) has a complex tax situation. The derivatives may be foreign property or foreign-sourced income, triggering [FATCA](/wiki/aml-compliance/) and [FinCEN](/wiki/fincen-reporting/) reporting. A large position might trigger reporting on Form 8938 (foreign financial assets) if aggregate foreign financial assets exceed $600,000.

Furthermore, the gain or loss on a foreign exchange trade is still U.S.-taxable income (the U.S. taxes worldwide income). But the lack of an official 1099-B means DIY documentation is essential. Many traders miss this requirement, creating a tail risk of penalty assessments.

<div class="wiki-seealso">

### Closely related
- [Capital Gains Tax](/wiki/capital-gains-tax/) — tax on profits from asset sales
- [Wash Sale](/wiki/wash-sale/) — rule against harvesting losses and immediately repurchasing
- [Cryptocurrency Exchange](/wiki/cryptocurrency-exchange/) — platform for buying/selling crypto
- [Mark-to-Market](/wiki/mark-to-market/) — valuing assets at current market price for tax purposes

### Wider context
- [Crypto Wallet Tax](/wiki/crypto-wallet-tax/) — tax implications of holding cryptocurrency off-exchange
- [Crypto Margin Trading Tax](/wiki/crypto-margin-trading-tax/) — tax treatment of leveraged crypto trades
- [Bitcoin](/wiki/bitcoin/) — the primary cryptocurrency subject to derivative trading
- [Staking Rewards Tax](/wiki/staking-rewards-tax/) — tax on cryptocurrency earned via validation

</div>
