---
title: "Option Contract Size Explained"
description: "The standard 100-share multiplier for equity options, how it affects cost and leverage, and when non-standard sizes arise."
keywords:
  - option contract size
  - how many shares option contract
  - 100 share multiplier
  - contract multiplier
  - equity options
---

*A standard equity **option contract** controls 100 shares of the underlying stock. When you buy or sell one contract, you are agreeing to a right or obligation on 100 shares. This 100-share multiplier is built into contract pricing and margin calculations, and it creates leverage—a relatively small cash outlay can control a large stock position.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Option Contract Size — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives." />

<div class="wiki-infobox-caption">One contract = 100 shares. Price quoted per share; total cost = price × 100.</div>

|   |   |
|---|---|
| **Standard equity option** | 100 shares per contract |
| **Index options** | 100 × index value (varies by index) |
| **Futures options** | Depends on the underlying futures contract |
| **Price quotation** | Per share; multiply by 100 for total contract cost |
| **Leverage** | Control large stock position with small premium payment |

</aside>

## The 100-Share Standard

By convention and regulatory definition, one equity [option](/option/) contract gives the holder the right (if a call or put buyer) or obligates the seller to deliver or purchase 100 shares at the [strike price](/strike-price/).

When you see an option quoted at $3.50, that price is per share. One contract costs $3.50 × 100 = $350 (plus commissions). If a contract is quoted at $0.15, the cost is $0.15 × 100 = $15.

This 100-share standard applies universally to U.S. equity options on major exchanges (NYSE, NASDAQ, etc.). It is standardized by the Options Clearing Corporation (OCC), which settles all option trades and enforces contract specifications.

The 100-share size is historical. When equity options were introduced in 1973, this multiplier was chosen for practical reasons: it created contracts large enough to be liquid but small enough to be accessible to individual investors. The standard has remained unchanged for over 50 years.

## How the Multiplier Affects Cost and Leverage

The 100-share multiplier creates significant leverage. Suppose Apple stock trades at $180 per share, and you want to gain exposure to a $18,000 stock position (100 shares).

**Buying stock directly:** You pay $18,000 upfront (plus commissions and potential margin costs).

**Buying a call option:** You pay $3 × 100 = $300 for a three-month call. If Apple rises to $190, the call is worth at least $10 (intrinsic value of $10 per share), or $1,000 total. You have tripled your money on a $300 investment, while directly owning stock would have given you a $1,000 gain on a $18,000 investment.

The trade-off: the option expires in three months, and you only profit if Apple moves above your strike plus the premium paid. The stock can be held indefinitely.

This leverage is why options appeal to traders seeking concentrated bets. It is also why options are risky: you can lose your entire premium if the trade moves against you.

## Impact on Margin and Account Buying Power

When you sell a call or put, you must post collateral (margin) to cover potential losses. The collateral requirement is calculated as a percentage of the contract's notional value (100 shares × underlying price).

For example, selling a naked call on Apple requires margin equal to roughly 20% of the stock's current value, or ~$3,600 per contract (100 shares × $180 × 20%). Some brokers use higher percentages (up to 30%) depending on volatility and account type.

The 100-share multiplier thus amplifies margin requirements. Selling five Apple calls ties up roughly $18,000 in margin—equivalent to buying 100 shares of stock outright in terms of account buying power. This leverage can quickly exhaust small accounts.

Covered calls (selling calls against shares you own) have much lower margin requirements because the underlying stock hedges the short call.

## Non-Standard Contract Sizes: Corporate Actions

When a company undergoes a **stock split**, **reverse split**, or **merger**, option contract sizes can become non-standard.

**Stock split:** If Apple splits 3-for-1, all existing option contracts adjust. A call originally on 100 shares becomes a call on 300 shares at 1/3 the original strike price. The total contract notional value is preserved, but the mechanics change. New contracts issued after the split use the standard 100-share multiplier based on the post-split price.

**Reverse split:** If a stock undergoes a 1-for-10 reverse split, option contracts shrink. A call originally on 100 shares becomes a call on 10 shares at 10× the original strike. Again, the notional exposure is preserved.

**Mergers:** If Company A acquires Company B, options on Company B stock may be adjusted to reflect the exchange ratio. If the deal is 0.5 shares of A per 1 share of B, then a call on B becomes a call for 50 shares of A (rather than 100).

These adjustments are handled by the OCC. Affected holders receive a notice explaining the new contract specifications. Most brokers' trading platforms automatically display the new size and adjust position displays accordingly.

## Index and Futures Options

**Index options** (like those on the S&P 500) typically have a multiplier of 100, but the contract size is calculated on the index value, not the number of shares.

An S&P 500 index option with a strike of 4,500 and a quoted price of $25 costs $25 × 100 = $2,500. The multiplier (100) is the same, but the underlying is an index level, not a share price.

**Futures options** (options on [futures contracts](/futures-contract/)) have varying multipliers depending on the futures contract itself. An option on a crude oil futures contract might control 1,000 barrels (the size of one crude futures contract), while an option on gold controls 100 troy ounces.

## Mini and Micro Contracts

Some exchanges offer **mini options** or **micro options** on popular stocks or indexes. These typically control 10 shares (mini) or 1 share (micro) per contract, making them more accessible to smaller accounts.

Mini options and micro options are less liquid than standard contracts and may have wider bid-ask spreads. Many retail brokers do not yet support them, limiting their availability.

## Implications for Position Sizing

The 100-share multiplier creates natural position sizes. If you want to own 100 shares' worth of call exposure, you buy one contract. If you want 500 shares' worth, you buy five contracts.

This discretization can be awkward. If you want exposure to exactly 75 shares, you cannot buy a fractional contract; you must buy one contract (100 shares) or zero. Some brokers allow fractional options trading (buying 0.75 contracts), but this is uncommon.

The fixed 100-share size also means that identical option prices on very different stocks have very different dollar values. A $2 option on a $10 stock costs $200 per contract; a $2 option on a $1,000 stock also costs $200 per contract. But the leverage and risk are vastly different.

## See also

<div class="wiki-seealso">

### Closely related

- [Option](/option/) — General overview of calls, puts, and mechanics
- [Strike Price](/strike-price/) — The agreed exercise price
- [Call Option](/call-option/) — Buying the right to purchase shares
- [Put Option](/put-option/) — Buying the right to sell shares
- [Expiration Date](/expiration-date/) — When contracts cease to exist
- [In-the-Money](/in-the-money/) — Options with intrinsic value

### Wider context

- [Leverage](/leverage-ratio-forex/) — Using borrowed capital or derivatives for amplified exposure
- [Futures Contract](/futures-contract/) — Similar to options; also standardized contract sizes
- [Bid-Ask Spread](/bid-ask-spread/) — Affects effective cost of trading options
- [Margin](/margin-call-forex/) — Collateral required for short option positions

</div>
