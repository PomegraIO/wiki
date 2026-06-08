---
title: "Option Contract Multiplier: Why One Contract Controls 100 Shares"
description: "An option contract multiplier of 100 is the U.S. standard—one call or put contract grants the right to buy or sell 100 shares. Premiums are quoted per share but paid per contract."
keywords:
  - option contract multiplier 100 shares
  - option premium calculation
  - standardized option contracts
  - derivatives trading
  - option notional value
image: "/svg/derivatives.svg"
---

*In U.S. equity [options](/option/) markets, one standard [call option](/call-option/) or [put option](/put-option/) contract represents the right to buy or sell 100 shares of the underlying stock. This **100-share multiplier** is the standard, creating a gulf between the per-share premium quoted and the total dollar cost of buying or selling a contract.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Option Contract Multiplier — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">A $3 premium sounds cheap until you realize you're paying $300 per contract for 100 shares.</div>

|   |   |
|---|---|
| **Standard U.S. multiplier** | 100 shares per contract |
| **Premium quoting convention** | Quoted per share; multiply by 100 to get total contract cost |
| **Example** | $2.50 premium × 100 = $250 per contract |
| **Applies to** | All standardized equity options on U.S. exchanges |
| **Exceptions** | After stock splits, spin-offs, or special dividends; also non-standard derivatives |
| **Regulatory body** | Options Clearing Corporation (OCC) standardizes terms |
| **Leverage effect** | Multiplier amplifies both gains and losses in percentage terms |

</aside>

## The 100-share standard and its origins

The standard equity [option contract](/option-contract-multiplier/) multiplier of 100 shares emerged during the early decades of organized options trading in the U.S., before electronic markets. When the Chicago Board Options Exchange (CBOE) opened in 1973, founders chose 100 shares as a round lot because it matched the size of a typical institutional order block of the era. The number became convention, adopted by all U.S. exchanges and codified by the [Options Clearing Corporation](/options-clearing-corporation/) (OCC), which standardizes contract terms.

One hundred shares remains the standard even though trading practices have evolved. It persists because:

1. **Network effects:** All market participants—traders, brokers, clearers, regulators—use the same multiplier. Changing it would fragment liquidity.
2. **Historical continuity:** Legacy systems, trading floors' oral contracts, and entire pricing conventions depend on 100 being the unit.
3. **Adequate granularity:** For stock prices ranging from $10 to $500, a 100-share contract creates a notional exposure ($1,000 to $50,000) that is large enough to be interesting but small enough for retail participation.

The multiplier is not arbitrary; it is a deliberate design choice that has shaped the entire options market for fifty years.

## Converting premiums to total contract cost

Options premiums are quoted on a per-share basis, but the buyer or seller pays for a full contract (100 shares). This creates a common source of confusion.

If XYZ stock is trading at $50 and a call option with a $55 strike expires in 60 days, the market might quote the [call premium](/option-premium/) at $1.50. This means:

- **Per-share cost:** $1.50
- **Total contract cost:** $1.50 × 100 = **$150**

A trader buying one call pays $150 upfront (plus commissions and fees) to control the right to buy 100 shares at $55. Similarly, if a put option is quoted at $2.00 per share, one put contract costs $200.

This quoting convention persists even though it can mislead beginners. Every U.S. options exchange quotes prices on a per-share basis, but every contract settles on a per-contract basis (100 shares). Traders must always multiply by 100 when calculating actual dollar outlay or [counterparty](/counterparty-risk/) exposure.

## Leverage and the multiplier effect

The 100-share multiplier amplifies both gains and losses, creating [leverage](/leverage-ratio-forex/).

Suppose a trader buys one call on XYZ at $1.50 premium, strike $55. XYZ rallies to $60, and the call is now worth $5.00. The gain on the call is $3.50 per share, or $350 per contract—a 233% return on the $150 paid. Owning 100 shares of XYZ outright at $50 and selling at $60 yields a $1,000 gain (20% return). The call holder captured almost the same gain with a tenth of the capital committed, illustrating the leverage inherent in options.

Conversely, if XYZ falls to $48, the call expires worthless. The loss is the full $150 (100% of the premium paid). With the call's defined risk, the trader's maximum loss is known upfront. But the percentage loss can be sharp for small premium outlays.

This multiplier-driven leverage is why options are called [derivatives](/derivatives-hedging/)—their value is magnified relative to the capital committed, and small moves in the underlying create large moves in the option's price.

## Adjustments after corporate actions

The 100-share multiplier is fixed, but it can be temporarily disrupted by corporate actions:

**Stock splits:** If XYZ executes a 2-for-1 stock split, each outstanding call contract still represents 100 shares. However, because the share price halves and the number of outstanding shares doubles, the OCC may adjust the [strike price](/strike-price/) and [multiplier](/option-contract-multiplier/) to preserve the contract's original economic intent. If the split is exact (e.g., 2-for-1), the strike is halved and the multiplier remains 100. If the split is unusual (e.g., 3-for-2), the OCC might leave the strike unchanged but adjust the multiplier to 150 shares per contract, keeping the notional value the same.

**Special dividends:** If a company pays an unusually large special dividend, the OCC may adjust the strike downward to reflect the cash departure. The multiplier typically remains 100.

**Spin-offs and mergers:** In a spin-off, all outstanding option contracts remain in effect on the original company, but the notional exposure to the spun-off entity is lost. The OCC generally does not adjust the multiplier; instead, the contract is treated as settled (with cash adjustment if necessary) or left to expire. Holders who want exposure to the new company must buy fresh contracts on the spun-off entity.

These adjustments are rare and technical, but they remind traders that the multiplier is not truly immutable—it is a convention that the OCC can modify to preserve economic intent when corporate structure changes.

## Non-standard multipliers and exceptions

U.S. equity options (those listed on exchanges like the CBOE, NYSE, or Nasdaq) standardize at 100. But exceptions exist:

**Index options:** Options on broad indices (like the [S&P 500](/sp-500-index/)) often use a multiplier of 100, but some use 250 or other values. For example, SPY (SPDR S&P 500 ETF) options use the standard 100, but micro-contract versions (with smaller notional values) use lower multipliers.

**Currency options:** Forex (foreign exchange) options on major pairs often use round-lot multipliers (e.g., 10,000 units of the base currency), which differ from equity conventions.

**Commodity futures options:** Options on [crude oil](/crude-oil/), [corn](/corn/), and other commodities use multipliers tied to the futures contract size. Crude oil options often represent 1,000 barrels per contract.

**Exotic and OTC options:** Over-the-counter (OTC) [derivatives](/derivatives-hedging/), negotiated privately between institutions, can have any multiplier. A custom [structured product](/structured-product/) might define a multiplier of 50 shares, 250 shares, or any other quantity.

The 100-share standard applies only to standardized, exchange-listed equity options. Anything traded over-the-counter or on non-U.S. exchanges may follow different conventions, making due diligence essential when trading non-standard instruments.

## Practical implications for traders and investors

Understanding the multiplier prevents costly errors:

1. **Position sizing:** A trader planning to spend $5,000 on call options cannot buy 5,000 ÷ 100 = 50 contracts if premiums average $1.00; they need $5,000 ÷ 100 = 50 contracts, confirming the math aligns with their capital.

2. **Margin requirements:** Brokers set [margin](/margin-call-forex/) requirements per contract, accounting for the 100-share multiplier. Buying 10 calls does not require margin equal to 1,000 shares of stock; instead, the broker uses an [options pricing model](/black-scholes-model/) to estimate worst-case loss and demands collateral accordingly.

3. **Assignment and delivery:** If a short call is assigned, the trader must deliver 100 shares. If the trader has only 50 shares, the short is naked (exposed to unlimited loss if the stock rallies further).

4. **Tax reporting:** For [capital gains](/capital-gains-tax-investor/) and loss-harvesting purposes, the gain or loss is calculated on the full notional amount (premium in minus premium out, multiplied by 100).

Traders who skip the multiplier step in their mental math often mis-estimate position size, commission costs, and risk.

## See also

<div class="wiki-seealso">

### Closely related

- [Call Option](/call-option/) — the basic contract whose multiplier this explains
- [Put Option](/put-option/) — equally governed by the 100-share multiplier
- [Option Premium](/option-premium/) — the quoted price per share that must be multiplied by 100
- [Strike Price](/strike-price/) — the fixed purchase/sale price, unaffected by the multiplier
- [Leverage](/leverage-ratio-forex/) — the amplification of gains and losses created by the multiplier

### Wider context

- [Derivatives](/derivatives-hedging/) — the broader world of contracts with embedded leverage
- [Black-Scholes Model](/black-scholes-model/) — the standard tool for pricing options, accounting for leverage
- [Volatility Smile](/volatility-smile/) — how option prices (and thus premiums) vary across strikes
- [Options Clearing Corporation](/options-clearing-corporation/) — the entity that standardizes contract terms and multipliers

</div>
