---
title: "Phi"
description: "The option's sensitivity to changes in the foreign risk-free interest rate, a key greek for FX options and dual-currency derivatives."
keywords:
  - phi greek
  - FX options
  - interest rate sensitivity
  - foreign rate risk
  - option greeks
image: "/svg/derivatives.svg"
---

*Phi measures how much an option's value changes when the foreign risk-free interest rate shifts by one basis point. It is the counterpart to rho (which captures sensitivity to the domestic rate) and is essential for pricing and hedging [options](/option/) on currency pairs, where two interest-rate regimes interact.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Phi — foreign rate sensitivity</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives and pricing mechanics." />

<div class="wiki-infobox-caption">The greek for dual-rate environments: how foreign interest changes reshape option value.</div>

|   |   |
|---|---|
| **What it is** | ∂V/∂r_f, the change in option value per basis point of foreign rate |
| **Units** | Option price per basis point of interest rate |
| **Also called** | Foreign rho, carry sensitivity |
| **Sign** | Call: negative; put: positive |
| **Key use** | FX option pricing; carry-trade hedging; interest-rate risk in currency forwards |
| **Relation to rho** | Rho tracks domestic rate; phi tracks foreign rate; both operate in same derivative |

</aside>

## The two-rate framework for currency derivatives

Pricing an option on a currency pair—say, a USD/EUR call—requires modeling two interest rates simultaneously. When a trader buys a US dollar call (sells euros), she earns the US risk-free rate on her dollar deposit but forgoes the euro rate she would have earned if she held euros instead. The difference between these rates—the interest-rate differential, or *carry*—affects both the forward price and the option's premium.

Phi isolates the impact of the foreign rate (the rate on the non-domestic currency in the pair). For a USD/EUR option, phi would measure sensitivity to changes in the euro risk-free rate. For a GBP/USD option, phi would capture British rate moves. This is distinct from rho, which measures domestic rate sensitivity.

## Pricing foreign-currency options: the carry effect

In the Garman-Kohlhlasen model for FX options—the standard framework extending [Black-Scholes](/black-scholes-model/) to currency pairs—the forward exchange rate incorporates the interest-rate differential:

F = S · e^{(r_d − r_f)T}

where S is the spot rate, r_d is the domestic risk-free rate, r_f is the foreign rate, and T is time to maturity. A higher foreign rate lowers the forward (euros appreciate less relative to the dollar), which lowers the value of a dollar call and raises the value of a dollar put—hence phi's sign.

Quantitatively, for a European call on a currency pair under Garman-Kohlhlasen:

φ = −e^{−r_f T} · K · T · N(d2)

The negative sign reflects the intuition: raising the foreign rate discounts the option's value (using a higher discount factor), and also shifts the forward exchange rate against the call holder. Puts have opposite sign: a higher foreign rate makes them more valuable.

## Phi versus rho: a complete picture

While rho measures sensitivity to domestic rates, phi captures foreign-rate moves. A trader managing FX options must monitor both.

Consider a multinational corporation hedging currency exposure on earnings expected in three months. If the firm has a USD liability and expects EUR revenue, it might buy a EUR/USD call (gaining upside if euros strengthen relative to dollars). The position will have:

- Negative rho (if USD rates rise, the option becomes less valuable—the forward shifts against the call).
- Positive phi (if EUR rates rise, the forward shifts even more against the call, making it even less valuable—no, wait: the sign must be reversed here).

Actually, the sign depends on the pair notation and which currency is the domestic reference. The key insight is that domestic and foreign rates push in opposite directions on the forward—one pushes spot appreciation, the other pushes spot depreciation—so rho and phi typically have opposite signs for the same option, helping to naturally offset interest-rate hedges.

## Practical importance in FX trading and hedging

Phi becomes mission-critical in several domains:

**Carry trades and interest-rate differentials**: Hedge funds and currency traders running carry strategies—borrowing in low-rate currencies and lending in high-rate currencies—use options to express carry views. Phi tells them how their option hedge will respond to moves in the rate differential. A trader expecting the EUR/USD rate differential to narrow might buy a straddle with negative combined phi: both the call and put lose value if euro rates rise, locking in gains if the carry narrows.

**Central bank policy hedging**: When central banks signal rate moves, FX option portfolios swing immediately via phi. A portfolio short phi (losing money if the foreign rate falls) will lose value if the foreign central bank cuts rates—a real risk for desks caught off-guard by policy announcements.

**Dual-currency bonds and structured notes**: These products embed optionality across currencies and rates. Phi is essential for pricing the coupon and principal exposure. A structured note with a "worst-of" coupon on USD and EUR will see its value shift not just with spot volatility but also with interest-rate differentials, channeled through phi.

**Cross-currency basis**: The difference between the FX swap rate and the spot-forward rate implied by the interest-rate differential is called the cross-currency basis. Phi hedges some of this basis risk, though a complete hedge also requires capturing duration and convexity across the two yield curves.

## Computing phi in practice

Phi is usually computed numerically by revaluing the option at foreign rates r_f and r_f + Δr, then dividing the price change by Δr. In most systems, it is reported as the price change per basis point (0.01%), so a phi of −0.005 means the option loses 0.5 cents for every basis point the foreign rate rises.

Traders often aggregate phi across their FX option book to measure net foreign-rate exposure. A large negative phi might prompt a hedge: shorting foreign government bonds, or entering a currency forward, or buying out-of-the-money puts where the foreign currency is the domestic reference—any position that gains value if the foreign rate rises.

## Phi's modest role in equity and bond options

Phi applies wherever a derivative is priced using two distinct discount rates or where the underlying asset generates a cash flow in a foreign currency. In plain vanilla equity options, interest rates are often less important than spot moves and volatility ([delta](/delta/) and [vega](/vega/) dominate), so phi is tertiary. But in commodity options, where storage costs or convenience yields are explicitly modeled, phi can be significant—especially if the commodity is priced in a foreign currency and hedged via currency forwards.

## See also

<div class="wiki-seealso">

### Closely related

- Rho — sensitivity to the domestic risk-free rate
- [Delta](/delta/) — spot-price sensitivity, typically larger than phi for equities
- [Vega](/vega/) — volatility sensitivity, often dominant in option pricing
- [Dual Delta](/dual-delta/) — strike-price sensitivity in the Black-Scholes framework
- [Dollar Delta](/dollar-delta/) — delta scaled to notional directional exposure
- [Forward Contract](/forward-contract/) — the rate-sensitive instrument underlying carry calculations

### Wider context

- [Option](/option/) — the fundamental derivative contract
- [Interest Rate](/interest-rate/) — the fundamental driver of phi exposure
- [Currency Risk](/currency-risk/) — the FX dimension that phi quantifies
- [Black-Scholes Model](/black-scholes-model/) — the theoretical foundation for all greeks

</div>