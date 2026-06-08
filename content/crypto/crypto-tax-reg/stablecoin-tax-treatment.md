---
title: "Stablecoin Tax Treatment: Are Stablecoin Trades Taxable?"
description: "Stablecoin swaps trigger capital gains only if the stablecoin's value differs from USD. Learn the tax treatment and rare edge cases where gains occur."
keywords:
  - stablecoin tax treatment
  - are stablecoin trades taxable
  - stablecoin swap capital gains
  - stablecoin tax implications
---

*Swapping crypto into a stablecoin (like USDC, USDT, or BUSD) is a **taxable disposition** in the eyes of the IRS—but the gain or loss is almost always zero. You are converting one asset into another, which triggers a [capital gains](/capital-gains-tax-investor/) calculation. Since stablecoins are pegged to the US dollar and trade at roughly $1, the realized gain equals the difference between your [cost basis](/cost-basis/) in the original crypto and $1 per stablecoin received. In most cases, this difference is negligible. Edge cases—where stablecoins trade at a premium or discount, or where the underlying collateral asset moves sharply—can create unexpected gains or losses.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Stablecoin Tax Treatment — key facts</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for cryptocurrency." />

<div class="wiki-infobox-caption">A stablecoin swap is a taxable event, but realized gains are typically zero or negligible.</div>

|   |   |
|---|---|
| **Taxable event?** | Yes — it is a disposition of the original asset |
| **Gain/loss calc** | Original asset cost basis vs. stablecoin received at $1 per coin |
| **Typical realized gain** | Near zero (stablecoin pegged to dollar) |
| **When gain occurs** | Stablecoin trades above/below $1, or sharp price moves in original asset |
| **Recordkeeping** | Document exchange rate and amount received (usually 1:1 USD) |
| **Holding period reset** | If you later sell stablecoin for fiat or volatile crypto, no gain |

</aside>

## Stablecoin swaps as taxable dispositions

The IRS treats a stablecoin swap the same way it treats any trade: you are exchanging one asset (volatile cryptocurrency) for another asset (a stablecoin). A taxable event occurs at the moment of exchange. The realized [capital gain or loss](/capital-gains-tax-investor/) is calculated as:

**Realized Gain = Amount Received (in USD terms) − Cost Basis of Original Asset**

For example:
- You bought 1 Bitcoin at $20,000 cost basis.
- You swap it for 45,000 USDC when Bitcoin is trading at $45,000.
- Realized gain = $45,000 − $20,000 = $25,000 (short-term or long-term, depending on holding period).

The gain is taxable even though you did not convert the stablecoin to US dollars. Possession of stablecoins is enough; the IRS does not require you to cash out to USD for the taxable event to occur.

## Why realized gains are usually zero

A stablecoin like USDC, USDT, or BUSD is designed to trade at exactly $1. If you receive 45,000 USDC for your Bitcoin, the fair market value of that USDC is $45,000—which matches the dollar value of the Bitcoin you gave up. So the gain or loss hinges entirely on your original cost basis, not on the stablecoin's value.

**Scenario 1 (long-term loss):**
- Cost basis: 1 BTC at $15,000 (bought 3+ years ago).
- Current BTC price: $45,000.
- You swap 1 BTC for 45,000 USDC.
- Realized gain: $45,000 − $15,000 = $30,000 long-term capital gain.

**Scenario 2 (break-even):**
- Cost basis: 1 BTC at $45,000 (bought recently).
- Current BTC price: $45,000.
- You swap 1 BTC for 45,000 USDC.
- Realized gain: $45,000 − $45,000 = $0.

**Scenario 3 (short-term loss realized):**
- Cost basis: 1 BTC at $50,000 (bought 1 month ago).
- Current BTC price: $45,000.
- You swap 1 BTC for 45,000 USDC.
- Realized loss: $45,000 − $50,000 = −$5,000 short-term capital loss.

In all three scenarios, the stablecoin's pegged value to the dollar is irrelevant to the gain calculation. The gain depends entirely on the comparison of the asset's original cost basis to its current market price (which the stablecoin receives you at fair market value).

## When stablecoin swaps create unexpected gains

Edge cases where the stablecoin swap does not result in a near-zero gain:

**Stablecoin trading above or below peg:**
If a stablecoin is depressed (e.g., USDC trading at $0.98 during a market panic or if the issuer faces solvency concerns), you may receive fewer dollars of value than the original asset's market price suggests. Conversely, if a stablecoin trades at a premium ($1.02), you receive more. The gain or loss is real and taxable.

Example:
- You swap 1 ETH (valued at $2,000) for 2,000 USDC when USDC is trading at $0.99.
- You receive $1,980 of economic value in stablecoins.
- If your cost basis in ETH was $1,500, your realized gain is $480 (not $500).

**Wrapped or bridged stablecoins:**
If you swap into a stablecoin on a different blockchain (e.g., USDC on Polygon instead of Ethereum), and the wrapped version trades at a different price, the valuation differs. A wrapped or bridge-specific stablecoin might trade at $0.995 or higher/lower, creating a realized gain or loss.

**Collateral-backed stablecoins:**
Some stablecoins (e.g., DAI, supported by collateralized debt positions) do not maintain a strict $1 peg and can trade above or below $1. Swapping into DAI at $0.98 creates an immediate realized loss compared to trading into USDC at $1.00.

## Stablecoin to USD conversion (not a taxable event)

Converting a stablecoin to US dollars on an exchange or bank is **not a taxable event**. You are simply converting currency, not trading one asset for another. This is similar to exchanging dollars for euros and back—no capital gain.

Example:
- You hold 10,000 USDC.
- You cash out to your bank account (receive $10,000 USD).
- No taxable gain or loss.

This clarity is important: many taxpayers worry that cashing out stablecoins triggers tax. It does not. The tax was triggered when you swapped volatile crypto for the stablecoin.

## Recordkeeping and exchange-rate documentation

Even though realized gains on stablecoin swaps are usually near-zero, the IRS requires you to document:

- **Date of swap:** The exact date you initiated the trade.
- **Amount swapped:** How much of the original asset you exchanged.
- **Price and valuation:** The price of the original asset at the moment of trade (in USD).
- **Stablecoin received:** How many stablecoins you received.
- **Exchange rate (if not $1):** The actual rate of the stablecoin if it traded off-peg.

If you swap on an exchange (Coinbase, Kraken, etc.), the exchange record is your documentation. If you use a DEX (Uniswap, SushiSwap), you can extract the transaction data from the blockchain and the DEX's frontend, but you should also record the USD value of the original asset and the stablecoin at the moment of trade.

## Holding period and subsequent sales

If you hold stablecoins for more than one year and then sell them for another cryptocurrency or cash out, the holding period does not reset. The IRS looks back to the original purchase date of the asset you swapped into the stablecoin.

Example:
- You buy Bitcoin on January 1, 2023.
- You swap it for USDC on July 1, 2024 (realized gain: $5,000, short-term).
- You hold the USDC until January 1, 2025 (8 months later).
- You swap USDC for Ethereum (not a taxable event; stablecoin-to-crypto swaps are still dispositions but the gain is near-zero).
- You hold Ethereum and sell it on March 1, 2025.
- The holding period for the original Bitcoin is still measured from January 1, 2023—over 2 years, so the gain is long-term.

The stablecoin holding period does not reset long-term status. The asset's original acquisition date is what matters for long-term vs. short-term [capital gains](/capital-gains-tax-investor/).

## Stablecoin interest or yield (ordinary income)

If you earn interest on stablecoins through a lending protocol, yield farm, or staking reward, that income is **ordinary income**, not a capital gain. It is reportable even if you do not convert it to USD.

Example:
- You hold 10,000 USDC in a protocol that pays 5% annual yield.
- You earn 500 USDC per year.
- That 500 USDC is ordinary income, taxable at your marginal rate.

This is separate from the capital gain/loss on the stablecoin swap itself.

## Stablecoin as a hedge (does not change tax treatment)

Some traders use stablecoins as a temporary holding position to avoid volatility (selling an appreciating asset into a stablecoin, then buying back into volatile crypto later). The IRS does not care about intent or strategy; the stablecoin swap is still a taxable event with a calculated gain or loss.

If you are trying to harvest losses or time gains, stablecoin swaps are an important part of your documentation. Every swap—even a brief one—is a taxable disposal and must be reported.

## See also

<div class="wiki-seealso">

### Closely related

- [Capital Gains Tax (Investor)](/capital-gains-tax-investor/) — How capital gains are calculated and taxed
- [Cost Basis](/cost-basis/) — Determining the purchase price for tax purposes
- [Holding Period](/capital-gains-tax-investor/) — How long-term vs. short-term classification works

### Wider context

- [Is Moving Crypto Between Your Own Wallets Taxable?](/crypto-moving-between-wallets-taxable/) — Non-taxable transfers vs. taxable swaps
- [NFT Royalty Income Tax](/nft-royalty-income-tax/) — Ordinary income treatment for creator royalties
- [Crypto IRS Summons and Third-Party Reporting](/crypto-irs-summons-third-party-reporting/) — How the IRS obtains exchange data

</div>
