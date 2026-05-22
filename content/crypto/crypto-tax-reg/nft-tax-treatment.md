---
title: "NFT Tax Treatment"
description: "How the IRS and foreign tax authorities classify and tax non-fungible tokens as either ordinary income or collectibles capital gains."
keywords:
  - nft taxation rules
  - capital gains collectibles
  - crypto tax compliance
  - digital asset basis
---

*The tax treatment of **non-fungible tokens** (NFTs) depends on their classification: the IRS typically taxes them as either [collectibles](/wiki/collectible/) under section 1231, triggering a preferential 28% [long-term capital gains](/wiki/long-term-capital-gain-tax/) rate, or as [ordinary income](/wiki/ordinary-dividend/) if held for sale in the [ordinary course](/wiki/wash-sale/) of business. How you acquire, hold, and dispose of an NFT fundamentally determines whether you owe 15%–20% or 28%–37% in [tax](/wiki/capital-gains-tax/).*

<div class="wiki-hatnote">
For general cryptocurrency taxation, see [Crypto Tax Implications](/wiki/crypto-derivative-tax/). For token vesting and reward taxation, see [Staking Rewards Tax](/wiki/staking-rewards-tax/).
</div>

<aside class="wiki-infobox">

| Aspect | Detail |
|---|---|
| **Classification** | Collectibles (28% rate) or ordinary income (37% rate) |
| **Cost basis tracking** | Purchase price, acquisition date, wallet address |
| **Wash-sale treatment** | 30-day wash-sale rule does *not* apply to crypto—yet |
| **Reporting form** | Schedule D (gains/losses), Form 8949 (sales detail) |
| **Character holding** | 1-year threshold for long-term treatment applies |
| **Fee deductibility** | Minting, platform, and gas fees typically increase cost basis |

</aside>

## NFT classification: art, utility, or ordinary income

An NFT is not a single tax category. The IRS distinguishes between **collectibles** (art, music, gaming assets) and **business inventory**. If you mint and sell NFTs regularly, you are likely a dealer, and each sale is [ordinary income](/wiki/ordinary-dividend/)—no [long-term capital gains](/wiki/long-term-capital-gain-tax/) benefit, no 1-year [holding period](/wiki/holding-period/) relief. If you are a collector who buys NFTs sporadically, holds them, and later sells at a gain, the gain is [long-term capital gains](/wiki/long-term-capital-gain-tax/) taxed at 28%.

This distinction mirrors [art market taxation](/wiki/capital-gains-tax/). A museum curator who acquires works for the institution's collection treats purchases as a business expense, but a private collector who buys art for enjoyment and appreciation is subject to [collectibles taxation](/wiki/collectible/). The same logic applies to NFTs: intent and frequency matter.

The IRS has not published definitive guidance on "utility NFTs" (tokens that grant access or voting rights), but the default assumption is that they fall under the [collectibles](/wiki/collectible/) umbrella unless they are clearly [business inventory](/wiki/inventory-turnover/). A gaming NFT that grants in-game benefits is treated as a collectible unless you are a professional game developer trading them as inventory.

## Cost basis and acquisition date tracking

Computing [cost basis](/wiki/cost-basis/) for NFTs is straightforward in concept but onerous in practice. You must record:

- The purchase price in fiat (USD, EUR, etc.) or, if you bought with [cryptocurrency](/wiki/bitcoin/), the [fair market value](/wiki/fair-value/) of that coin on the purchase date.
- [Minting fees](/wiki/nft-minting-mechanics/) (gas, platform fees) incurred at creation.
- Any [transaction fees](/wiki/currency-transaction-reporting/) on the exchange.
- The precise date of acquisition (usually the blockchain transaction timestamp, not the day you took possession).

[Acquisition date](/wiki/acquisition/) is critical because it determines when your [holding period](/wiki/holding-period/) begins. NFT markets operate 24/7 on blockchains, so the legal date is the on-chain timestamp, not the calendar date you initiated the purchase. A transaction at 11:59 PM UTC on June 30 and another at 12:01 AM UTC on July 1 are separate [tax years](/wiki/tax-bracket-investor/) for [wash-sale](/wiki/wash-sale/) calculations, even though they are minutes apart.

## Holding period and long-term treatment

Like [stocks](/wiki/common-stock/) and [bonds](/wiki/bond/), you must hold an NFT for more than one year (366 days from the [acquisition date](/wiki/acquisition/)) for [long-term capital gains](/wiki/long-term-capital-gain-tax/) treatment. One day short and the entire gain is [short-term](/wiki/short-term-capital-gain-tax/), taxed as [ordinary income](/wiki/ordinary-dividend/) at rates up to 37%.

If you hold an NFT for 366+ days and sell at a gain, the gain is [long-term capital gains](/wiki/long-term-capital-gain-tax/) taxed at 28% (the "art/collectibles" rate) if the IRS classifies it as a collectible. Most NFTs fall into this bucket. If your NFT somehow escapes collectibles classification—perhaps because it is a utility token with genuine economic substance—you receive the standard [long-term capital gains](/wiki/long-term-capital-gain-tax/) rate of 15% or 20%, depending on [income](/wiki/income-statement/).

## Wash-sale rule and the gray area

The [wash-sale rule](/wiki/wash-sale/) typically forbids you from deducting a loss if you repurchase a "substantially identical" asset within 30 days before or after the [sale](/wiki/short-selling/). For decades, [cryptocurrency](/wiki/bitcoin/) was exempt—the IRS had no guidance—but [regulations](/wiki/regulation-best-interest/) increasingly treat [crypto](/wiki/bitcoin/) losses as subject to [wash-sale](/wiki/wash-sale/) restrictions. The safest approach is to assume a 30-day window applies to NFTs. If you sell an NFT at a loss in July, avoid repurchasing that exact NFT (or a "substantially identical" one, like the same asset on another blockchain) until August 1 or later.

"Substantially identical" is harder to define for NFTs than for stock—no two NFTs are identical by definition. However, two mints from the same series by the same artist might be considered substantially identical; a fungible-token variant of the same asset might be considered substantially identical. The IRS has not clarified, so conservative practitioners assume repurchasing *any* derivative of the same asset within 30 days triggers [wash-sale rules](/wiki/wash-sale/).

## Minting, trading, and staking taxation

**Minting**: When you mint an NFT (create and issue a new token), you have immediate [ordinary income](/wiki/ordinary-dividend/) equal to the NFT's fair market value on the mint date, less [minting fees](/wiki/nft-minting-mechanics/) and gas costs. Your [cost basis](/wiki/cost-basis/) is that fair market value (your income), so you start with a zero gain. If the NFT immediately sells for a profit, the gain is short-term [capital gains](/wiki/capital-gains-tax/).

**Trading**: Each buy and sell is a separate [taxable event](/wiki/tax-gain-harvesting/). Swapping an NFT for another NFT (rather than selling it for cash) is still a [taxable exchange](/wiki/1031-exchange/). You recognize a gain or loss on the NFT given up, using its [cost basis](/wiki/cost-basis/) and [fair market value](/wiki/fair-value/) at the time of trade.

**Staking and yield**: If an NFT generates yield (dividends, staking rewards, rental income), that income is [ordinary income](/wiki/ordinary-dividend/) in the year earned. The basis step-up does *not* apply to future yield—you pay [tax](/wiki/capital-gains-tax/) on 100% of the reward amount.

## Reporting and IRS compliance

You report NFT transactions on **Schedule D** (capital gains and losses) and **Form 8949** (proceeds and basis detail). Each [sale](/wiki/short-selling/) requires:

- Description of the NFT (name, token ID, or serial number).
- Date acquired (on-chain timestamp).
- Date sold.
- [Cost basis](/wiki/cost-basis/).
- [Fair market value](/wiki/fair-value/) on [sale](/wiki/short-selling/) date (in USD at the time of the transaction).
- Gain or loss.

The IRS is increasingly monitoring [cryptocurrency](/wiki/bitcoin/) and NFT transactions via exchange data-matching programs. If you report losses that dwarf your documented income, expect scrutiny. Large [exchanges](/wiki/cryptocurrency-exchange/) are required to report [customer](/wiki/customer-due-diligence/) information to the IRS, and [broker](/wiki/broker/) reporting of [cryptocurrency](/wiki/bitcoin/) sales is mandatory.

## International treatment

Non-US residents and foreign taxpayers face similar frameworks in most jurisdictions. The UK, EU, and Canada treat NFTs as [capital assets](/wiki/asset-allocation/) or collectibles under local [taxation](/wiki/capital-gains-tax/) codes. Australia's ATO explicitly classifies NFTs as CGT assets. Each jurisdiction has its own [holding period](/wiki/holding-period/) threshold (e.g., Australia's is 12 months; the UK has no statutory [holding period](/wiki/holding-period/)) and rates, so consult local tax counsel.

<div class="wiki-seealso">

### Closely related
- [Crypto Tax Implications](/wiki/crypto-derivative-tax/) — General tax treatment of cryptocurrency gains, losses, and staking
- [Capital Gains Tax](/wiki/capital-gains-tax/) — How [asset sales](/wiki/short-selling/) are taxed at preferential long-term rates
- [Wash-Sale Rule](/wiki/wash-sale/) — The 30-day repurchase restriction that may now apply to NFT losses

### Wider context
- [Collectibles Tax Rate](/wiki/collectible/) — The preferential 28% rate applied to art, precious metals, and certain digital assets
- [Cost Basis](/wiki/cost-basis/) — Tracking purchase price and fees to calculate taxable gains
- [Long-term Capital Gains Tax](/wiki/long-term-capital-gain-tax/) — Preferential rates for assets held over one year

</div>
