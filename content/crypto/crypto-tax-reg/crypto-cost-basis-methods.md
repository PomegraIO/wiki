---
title: "Crypto Cost Basis Methods"
description: "Accounting rules that determine which units of cryptocurrency are deemed sold in each transaction, directly affecting tax liability."
keywords:
  - cost basis
  - FIFO
  - LIFO
  - specific identification
  - cryptocurrency tax
image: /svg/crypto.svg
---

*A **crypto cost basis method** is an accounting rule that specifies which units of a cryptocurrency are assumed to be sold or transferred when you dispose of a holding. The method you choose—whether FIFO (first-in, first-out), specific identification, or average cost—determines the gain or loss on every sale and, by extension, your annual tax bill. The IRS permits several methods, but selection is irreversible for a given asset in a given tax year.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Crypto Cost Basis Methods — key facts</div>

<img src="/svg/crypto.svg" alt="An abstract mark representing blockchain assets and valuation." />

<div class="wiki-infobox-caption">Choosing which coins you're selling changes your tax outcome; most traders default to the wrong method.</div>

|   |   |
|---|---|
| **What it is** | A rule that identifies which cryptocurrency units are disposed of in each transaction |
| **Main methods** | FIFO, LIFO, specific identification, average cost |
| **Default (US)** | FIFO, unless you elect and document another method |
| **Impact** | Directly determines [capital gains](/capital-gains-tax-investor/) and losses for the tax year |
| **Revocable** | Only for the first year; thereafter, method change requires IRS consent |
| **Relevant law** | [IRC Section 1012](/capital-gains-tax-investor/); IRS Rev. Proc. 2021-14 and 2023-17 |

</aside>

## FIFO: the default, and usually the worst choice

Under **FIFO** (first-in, first-out), the oldest units you own are always the first ones deemed sold. If you bought 1 bitcoin at $10,000 in 2019, then another at $50,000 in 2021, and now sell one at $60,000, FIFO says you sold the 2019 coin. Your gain is $50,000 (sold at $60,000 minus cost of $10,000), and you owe tax on that. The newer, dearer coin remains in your portfolio at cost basis $50,000.

FIFO is the IRS default; if you do not affirmatively elect a different method and document it contemporaneously, the IRS assumes you used FIFO. This is a trap for the unwary. In a bear market followed by a rally, FIFO can trigger enormous gains on your oldest, cheapest coins—the very units with the highest gains. A holder who accumulated crypto over years of price volatility can face a seven-figure tax bill on a modest portfolio because FIFO forces the realisation of all accumulated upside.

FIFO is optimal only in a market that has declined monotonically since you bought. That is rare in crypto.

## Specific identification: the tax-smart choice

**Specific identification** allows you to nominate, at the time of sale, exactly which units you are selling. You specify their lot numbers, purchase dates, and cost basis; the sale is matched against those specific coins. This gives you surgical control over your gain or loss.

Imagine the same scenario: you own two bitcoins at $10,000 and $50,000. You want to sell one at $60,000 but minimise tax. Under specific identification, you choose to sell the coin purchased at $50,000. Your gain is only $10,000 (sold at $60,000 minus cost of $50,000), and you owe tax on that instead of $50,000. The cheaper coin stays in your portfolio, available to harvest losses or defer gains.

Specific identification requires meticulous record-keeping. At the moment you sell, you must issue a written instruction to your exchange or wallet stating which lot you are selling. You must retain that documentation for the IRS. Many exchanges do not make this easy; some do not permit it at all. But if you can execute it, the tax efficiency is substantial—often the difference between a large tax bill and a modest one.

## LIFO, average cost, and other methods

**LIFO** (last-in, first-out) assumes the newest coins are sold first. In a rising market, LIFO defers the realisation of the longest-held, largest gains. But LIFO is disfavoured for individual investors in most contexts because [holding periods](/holding-period/) matter: coins held longer than one year generate [long-term capital gains](/long-term-capital-gain-tax/), taxed at preferential rates, while short-term sales are taxed as ordinary income. LIFO tends to force the sale of newer, short-term coins, wasting the long-term rate advantage. LIFO is more useful in corporate inventory accounting than in crypto tax planning.

**Average cost** assumes you sell an average-priced unit from your holding. If you own two bitcoins at $10,000 and $50,000, the average cost is $30,000. Selling one at $60,000 yields a gain of $30,000 under average cost. Average cost simplifies record-keeping (you need not track individual lots) but offers no tax optimisation; you sacrifice the precision of specific identification without gaining the deferred-gain benefit of LIFO.

## How method affects tax outcomes

The choice can swing your tax liability by tens or hundreds of thousands of dollars on a single large sale. Consider a trader who bought $500,000 worth of Ethereum scattered across 2017–2021 at an average cost of $1,200 per coin, then sells 100 coins at $3,000 in 2023. Under FIFO, assuming the oldest coins cost $200 each, the gain is $280,000. Under specific identification, the trader nominates coins purchased at $2,800 each, generating a gain of only $20,000. Under average cost, the gain is roughly $180,000. The same sale, three different tax bills.

This explains why tax-aware traders closely watch [cost-basis tracking](/crypto-cost-basis-methods/) software. Many use specialised tools—or hire accountants—to ensure the right lots are matched to sales and that every redemption, transfer, [airdrop](/airdrop-tax-treatment/), and [mining](/crypto-mining-tax/) event is correctly logged. A single misclassified transaction can inflate your annual [capital gains tax](/capital-gains-tax-investor/) liability by multiples.

## Documentation and IRS rules

The IRS requires that if you elect a method other than FIFO, you must document the election in your tax return and maintain records of the specific lots, purchase dates, and cost basis for each sale. The documentation requirement is strict: without contemporaneous proof that you selected coin lot #47 (purchased 15 March 2020 at $8,945) when you made a sale, the IRS will reassign the sale to FIFO by default. This has caught many traders off guard.

If you file amended returns or change methods, you must get IRS consent (Form 3115) in most cases. Once you elect a method for an asset in a year, switching to another method in a future year is permitted only with IRS approval, and only rarely granted for capital assets. Choose once, and live with it—unless the situation changes dramatically.

## Exchanges and reporting

As of 2024, most major [cryptocurrency exchanges](/cryptocurrency-exchange/) (such as Coinbase or Kraken) default to FIFO if they report your transactions to the IRS on Form 8949. This is a friction point: traders who intend to use specific identification often must override the default manually, then document their choice carefully on their tax return. Some exchanges do not permit specific identification at all, forcing traders to carry out the tracking offline, in spreadsheets or specialist software.

## Strategy and planning

Tax-planning conversations in crypto often centre on which method to use before a large sale. The general principle is: use specific identification to match the highest-cost coins to the sale, minimising gain. This requires that you have accumulated coins at different prices (which most long-term holders have) and that your exchange or custodian permits specific identification. If the platform does not, keeping coins at multiple custodians and specifying which custodian you are selling from can achieve a similar effect.

Another tactic: stagger sales across years. A $1 million sale in one year might trigger a much larger [marginal tax rate](/marginal-tax-rate-investor/) than two $500,000 sales in consecutive years. The cost-basis method you choose for each sale can amplify or dampen this effect.

## See also

<div class="wiki-seealso">

### Closely related

- [Capital gains tax](/capital-gains-tax-investor/) — the federal income tax on gains from selling securities or crypto
- [Long-term capital gains](/long-term-capital-gain-tax/) — preferential tax rate on assets held longer than one year
- [Cost basis](/capital-gains-tax-investor/) — the tax value of an asset at purchase, the foundation of gain-loss calculations
- [Airdrop tax treatment](/airdrop-tax-treatment/) — how unsolicited tokens are valued at receipt and integrated into cost basis tracking
- [Crypto mining tax](/crypto-mining-tax/) — how coins mined or earned become taxable income, then are held at cost basis

### Wider context

- [Schedule D](/schedule-d/) — the IRS form on which capital gains and losses are reported
- [Form 8949](/form-8949/) — the detailed form listing individual asset sales that feed into Schedule D
- [Marginal tax rate](/marginal-tax-rate-investor/) — how the highest dollar of income is taxed, which determines effective tax on additional gains
- [Cryptocurrency exchange](/cryptocurrency-exchange/) — the venue where crypto is bought and sold, responsible for initial cost-basis tracking

</div>
