---
title: "Call Swaption"
description: "Option that grants the right, but not obligation, to enter into an interest rate swap as the fixed-rate payer."
keywords:
  - swaption
  - interest rate derivative
  - interest rate swap
  - fixed-rate payer
  - embedded optionality
---

*A **call swaption** (or payer swaption) is a financial contract that gives the holder the right—but not the obligation—to enter into a [swap](/wiki/interest-rate-swap/) at a future date as the **payer of fixed rates**. If market [interest rates](/wiki/interest-rate/) fall, the holder exercises the swaption and locks in the higher predetermined fixed rate, profiting from the rate decline. If rates rise, the holder lets the option expire and avoids locking in a low fixed rate.*

<aside class="wiki-infobox">

| Term | Detail |
|------|--------|
| **Holder right** | Enter swap as fixed-rate payer |
| **Expiration** | Option expires on the swap start date |
| **Underlying** | Interest rate swap (pay fixed, receive floating) |
| **Payoff if exercised** | Stream of fixed payments minus floating receipts |
| **Exercise incentive** | Exercise when current fixed swap rate < strike rate |
| **Typical user** | Corporations hedging funding costs, asset managers |

</aside>

## Structure: the option on a swap

A [swaption](/wiki/swaption/) is a compound derivative: an option on a [swap](/wiki/interest-rate-swap/). A basic [interest rate swap](/wiki/interest-rate-swap/) exchanges fixed cash flows for floating cash flows. A call swaption adds an optional layer: the holder can *choose* to enter into that swap at a predetermined fixed rate (the "strike") on a future date (the "expiration").

For example: on June 1, you buy a call swaption giving you the right to enter a 5-year [swap](/wiki/interest-rate-swap/) paying fixed at 3.5% and receiving floating (3-month LIBOR), with expiration March 31, 2025. On March 31, 2025, if the market fixed rate for 5-year swaps is 3.2%, you exercise—locking in a 3.5% fixed rate is attractive because you can receive floating at market terms (3.2%) and pocket the 0.3% spread. If market rates are 4.0%, you let the option expire and don't enter the swap.

## Why corporates use call swaptions to hedge refinancing risk

A company expects to refinance a bond or credit facility in 12 months but fears [interest rates](/wiki/interest-rate/) will rise, forcing it to pay higher [fixed rates](/wiki/fixed-rate-mortgage-personal/). Buying a call swaption hedges this risk: if rates rise, the swaption expires worthless (no big loss on the option premium paid), but the company refinances its debt at the new higher rate without additional obligation. If rates fall, the company can exercise the swaption to lock in a lower fixed rate, and benefit from the rate decline.

This is cheaper than entering a forward [swap](/wiki/interest-rate-swap/) now, which would lock in the current rate regardless of future movements.

## Payoff at expiration and exercise dynamics

A call swaption has no cash payoff at expiration—it either is exercised or expires. On the exercise date, the holder and counterparty *enter* the underlying [swap](/wiki/interest-rate-swap/) agreement, and future cash flows begin. The "value" of the swaption at expiration is the difference between the strike fixed rate and the market fixed rate for a swap starting on that date.

If market fixed rate < swaption strike, the option is in the money and will be exercised. If market fixed rate > swaption strike, the option is out of the money and will be abandoned.

## Comparison: call swaption vs. put swaption

A **call swaption** (payer swaption) lets you *enter* the swap as the fixed-rate payer. A **put swaption** (receiver swaption) lets you *enter* the swap as the fixed-rate *receiver*. A corporation expecting to receive floating cash flows (e.g., a bank's asset manager expecting declining rates) buys a put swaption to gain the option to receive fixed rates if rates collapse.

The two are mirror images: one bets on rates rising, the other on rates falling.

## Pricing and implied volatility inputs

[Swaption](/wiki/swaption/) prices depend on:
1. **Time to expiration**: longer options cost more (more time for the underlying [swap](/wiki/interest-rate-swap/) rate to move).
2. **Moneyness**: how far the strike is from the current market fixed rate.
3. **[Implied volatility](/wiki/implied-volatility/)**: the market's expectation of future [interest rate](/wiki/interest-rate/) swings. High volatility → higher option premium.
4. **The shape of the yield curve**: whether rates are expected to rise or fall.

Unlike equity [options](/wiki/option-premium/), swaption [implied volatility](/wiki/implied-volatility/) can differ across strikes and tenors, forming a volatility surface much like [FX volatility](/wiki/fx-volatility-smile-curve/).

## Swaptions in structured products and embedded optionality

[Callable bonds](/wiki/callable-bond/) (bonds where the issuer can force redemption early) are often replicable as a [straight bond](/wiki/bond/) minus a call swaption: the issuer buys a call swaption to lock in the right to refinance at a lower rate. Similarly, putable bonds can be replicated using put swaptions.

Many [convertible bonds](/wiki/convertible-bond/) and [structured products](/wiki/structured-finance/) embed swaption-like optionality to manage interest rate risk.

## Clearing and standardization

Standardized swaptions on major interest rates (USD, EUR, GBP, JPY swaps at common tenors like 5-year, 10-year) trade on regulated exchanges and clear through central counterparties, improving [liquidity](/wiki/liquidity-pool/). Off-the-run or exotic swaptions are traded over the counter (OTC) and carry [counterparty risk](/wiki/counterparty-credit-risk/). The 2008 crisis and subsequent regulatory reforms have pushed vanilla swaptions toward centralized clearing.

<div class="wiki-seealso">

### Closely related
- [Swaption](/wiki/swaption/) — the general class of options on swaps
- [Interest rate swap](/wiki/interest-rate-swap/) — the underlying instrument being optioned
- [Put swaption](/wiki/put-swaption/) — the complementary receiver swaption
- [Implied volatility](/wiki/implied-volatility/) — key pricing input for swaption premiums

### Wider context
- [Interest rate derivative](/wiki/interest-rate-option/) — family of rate-hedging derivatives
- [Callable bond](/wiki/callable-bond/) — bond with embedded swaption-like optionality
- [Convertible bond](/wiki/convertible-bond/) — often includes rate-option features
- [Derivative accounting](/wiki/derivative-accounting-hedging/) — hedging treatment of swaptions

</div>
