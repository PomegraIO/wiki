---
title: "Put Swaption"
description: "Option granting the right to enter into a swap where the holder receives fixed and pays floating interest rates."
keywords:
  - put swaption
  - interest rate option
  - swap option
  - receive-fixed swap
---

*A **put swaption** is an option on an [interest rate swap](/wiki/interest-rate-swap/). Specifically, it grants the right (but not the obligation) to *enter into* a swap where you receive a fixed rate and pay floating. The holder of a put swaption benefits if [interest rates](/wiki/interest-rate/) rise — the fixed rate becomes more valuable, and the holder can lock in the fixed side at an attractive rate or exercise to capture gains. The counterparty to the swaption (the seller) is short the put, facing the risk of the holder exercising when rates have moved unfavorably.*

<aside class="wiki-infobox">

| Factor | Detail |
|--------|--------|
| **Underlying** | Interest rate swap contract |
| **Strike/Fixed Rate** | Pre-agreed rate set at swaption inception |
| **Exercise Right** | Receive fixed, pay floating (put perspective) |
| **Payoff** | Intrinsic value: max(market fixed rate − strike, 0) × notional |
| **Expiration** | Swaption expires; if exercised, swap begins |
| **Counterparty** | Typically a bank or derivatives dealer |
| **Pricing Model** | Black-76, Bachelier, or Monte Carlo methods |
| **Use Case** | Borrowers hedging future fixed-rate debt needs; savers protecting against rate declines |

</aside>

## How a put swaption works

Suppose you are a corporation that may need to borrow $100 million in fixed-rate debt six months from now, but you are unsure of future [interest rates](/wiki/interest-rate-parity/). You buy a put swaption: the right to enter a 5-year [swap](/wiki/swap/) at a fixed rate of 4% (the strike). You pay a premium upfront.

**If rates fall to 3%:** The swaption is out-of-the-money. You do not exercise. You borrow at 3% on the market and ignore the swaption. You have lost the premium you paid, but you got the fixed rate you wanted.

**If rates rise to 5%:** The swaption is in-the-money. You exercise the swaption, locking in the 4% fixed rate instead of borrowing at 5%. The swaption has a value of (5% − 4%) × $100M × 5 years (discounted) = substantial. The premium you paid is recouped and exceeded.

The key insight: the swaption is *insurance*. You pay a premium to cap your borrowing cost (or protect your investment income if you are a saver).

## Notation: "payer swaption" vs. "receiver swaption"

Terminology varies by perspective. A **payer swaption** (from the perspective of the party that pays fixed if exercised) is a call on the floating side — the holder profits if rates rise. A **receiver swaption** (from the holder's perspective) is a put on the floating side — the holder profits if rates fall.

In this article, we use the **put swaption** term, which means: holder has the right to *receive* fixed and *pay* floating. This is equivalent to a receiver swaption. If you are a borrower worried about rising rates, you want a put swaption (receive-fixed protection).

## Pricing and Greeks

Swaption value depends on:

- **Current swap rate:** If the market's current fixed rate on the underlying swap is 4.5% and your strike is 4%, the swaption has intrinsic value of roughly 0.5% × notional × swap duration.
- **Implied volatility:** Higher volatility makes the swaption more valuable (more upside potential). Swaption dealers quote prices in terms of [implied volatility](/wiki/implied-volatility/) rather than dollar amounts.
- **Time to expiration:** Longer time to exercise increases value (more time for rates to move in your favor).
- **Yield curve shape:** Steepness affects the value of the underlying swap and thus the swaption.

[Greeks](/wiki/options-greeks/) include [delta](/wiki/delta-option-greeks/) (sensitivity to swap rate changes), [vega](/wiki/vega-option-greeks/) (sensitivity to volatility), and [theta](/wiki/theta-option-greeks/) (time decay). Swaptions decay over time if rates remain stable; they gain value if realized volatility increases.

## Comparison to a call swaption

A **call swaption** (or payer swaption) grants the right to *pay* fixed and *receive* floating. This is a hedge for investors who own fixed-income assets and are worried about declining rates — if rates fall, bonds rally, but if they own a call swaption, they can enter a swap to receive floating and benefit from the swap hedge as rates fall. Call and put swaptions are economically opposite and trade at different prices depending on rate expectations and volatility.

## Swaptions as volatility plays

Traders view swaptions as bets on [volatility](/wiki/volatility-smile/). A trader expecting [interest rate](/wiki/interest-rate-option/) volatility to increase (larger moves ahead) buys swaptions (calls or puts, depending on rate direction expectation). A trader expecting calm might sell swaptions to collect premium.

A common strategy is a **straddle** of swaptions: buy both a payer and receiver swaption at the same strike, betting on large moves in either direction. If rates move sharply, one leg will be deep in-the-money and offset the loss on the other, netting a profit. If rates stay flat, both legs expire worthless.

## Corporate use: interest rate risk management

A company with floating-rate debt can use a put swaption to hedge future refinancing risk. At the time the swaption expires, if the company needs to roll over its debt, it can exercise and lock in a fixed rate via the swap. If rates have fallen, the company simply borrows at the lower market rate and lets the swaption expire unexercised.

A company with a fixed-rate debt maturity coming due can use a call swaption as a reverse hedge: if rates have fallen, the company can exercise and enter a receive-fixed swap, turning its new fixed-rate borrowing into a floater, capturing the benefit of lower rates.

## Dealer perspective: managing swaption risk

Banks that sell swaptions are short volatility and long the underlying swap. To hedge, they trade the underlying [swap](/wiki/swap/), [treasury bonds](/wiki/treasury-bond/), and [interest rate futures](/wiki/currency-futures/) to maintain a neutral [delta](/wiki/delta-option-greeks/). A rise in implied volatility increases the bank's loss on the swaption book, so dealers actively manage [vega](/wiki/vega-option-greeks/) exposure.

## Relationship to bond options and caps/floors

A swaption is complementary to [bond options](/wiki/bond-callability/) (options on bond prices). A bond call is a fixed-income instrument's embedded option; a swaption is a standalone derivative. [Interest rate caps](/wiki/interest-rate-option/) and [floors](/wiki/interest-rate-option/) are also related: a cap is a series of call options on floating rates; a floor is a series of puts. A swaption gives you the right to enter the underlying swap; a cap gives you the right to benefit from each individual coupon being above a strike.

## Settlement and exercise mechanics

When a swaption is exercised, it typically settles via **physical settlement**: the holder and counterparty enter into the swap at the pre-agreed fixed rate. Cash exchanges begin immediately according to the swap's terms. Alternatively, some swaptions allow **cash settlement**: the difference between the strike fixed rate and the market fixed rate is paid in a lump sum.

Physical settlement is more common for corporate hedges; cash settlement is more common for trading-oriented positions.

## Regulatory and credit considerations

Swaptions are [derivatives](/wiki/derivative-accounting-hedging/) subject to [clearing](/wiki/central-counterparty-clearing/) requirements and [margin](/wiki/initial-margin/) rules under [Dodd-Frank](/wiki/dodd-frank-act/). A corporation buying a swaption from a bank posts initial [collateral](/wiki/collateral-ratio/) and may face [variation margin](/wiki/variation-margin/) calls if rates move sharply.

<div class="wiki-seealso">

### Closely related
- [Interest Rate Swap](/wiki/interest-rate-swap/) — underlying instrument
- [Swaption](/wiki/swaption/) — general swaption entry
- [Call Swaption](/wiki/call-swaption/) — alternative direction (pay fixed)
- [Option Greeks](/wiki/options-greeks/) — sensitivity measures
- [Interest Rate Option](/wiki/interest-rate-option/) — broader category

### Wider context
- [Derivatives](/wiki/derivative-accounting-hedging/) — risk transfer instruments
- [Central Counterparty Clearing](/wiki/central-counterparty-clearing/) — settlement infrastructure
- [Interest Rate Risk](/wiki/interest-rate-risk/) — the risk being hedged
- [Implied Volatility](/wiki/implied-volatility/) — pricing input
- [Hedging](/wiki/currency-hedging/) — risk management strategy

</div>
