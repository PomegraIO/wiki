---
title: "Hedging a Bond Portfolio With Interest Rate Swaps"
description: "How portfolio managers hedge bond portfolios with interest rate swaps to reduce duration risk and limit losses when rates rise."
keywords:
  - hedge bond portfolio with interest rate swaps
  - interest rate swap hedging
  - duration hedging
  - bond portfolio risk management
  - pay-fixed swap
  - mark-to-market losses
---

*A **hedge bond portfolio with interest rate swaps** is a risk-management strategy where a portfolio manager locks in a fixed payment rate on a notional amount of debt, offsetting the market-value decline that occurs when interest rates rise. The manager enters a pay-fixed, receive-floating swap—the opposite of the bond's economics—so gains on the swap offset losses on the held bonds.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Interest Rate Swap Hedging — key facts</div>

<img src="/svg/risk.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">A pay-fixed swap shortens effective duration and caps downside when rates are expected to rise.</div>

|   |   |
|---|---|
| **Core mechanism** | Manager pays fixed, receives floating; gains on swap offset bond mark-to-market losses |
| **Effective duration** | Reduced by the swap's [duration](/duration/) |
| **Notional amount** | Typically matches or slightly underhedges the bond portfolio value |
| **Cost** | [Management fee](/management-fee/), [counterparty risk](/counterparty-risk/) |
| **Breakeven** | Occurs when rates rise enough that swap gains equal bond losses |

</aside>

## Why bond managers hedge with swaps

A bond portfolio's market value falls when interest rates rise—the longer the [duration](/duration/), the sharper the decline. A portfolio manager might face redemptions in a rising-rate environment, be required by [risk-weighted-assets](/risk-weighted-assets/) constraints to reduce [interest-rate-risk](/interest-rate-risk/), or simply expect rates to climb and want to protect existing positions.

Rather than sell bonds outright (which might crystallize losses or force reinvestment at worse rates later), the manager can retain the bonds and hedge the duration exposure through a pay-fixed [interest-rate-swap](/interest-rate-swap/). The swap's fixed leg acts like a short position in a bond, while the floating-rate leg matches incoming coupon and principal flows. When rates rise, the bond loses value, but the manager's position as the fixed-rate payer gains: the floating rate it receives climbs, widening the economic advantage of being locked into a lower fixed rate.

## Mechanics of a pay-fixed swap

In a standard [interest-rate-swap](/interest-rate-swap/), two counterparties exchange interest-rate obligations on a notional principal. The manager agrees to pay a fixed rate (say 4.2%) on, for example, $10 million notional for five years. In return, it receives a floating rate (typically benchmarked to [SOFR](/sofr/) or another short-term reference rate, reset quarterly or semi-annually).

The manager does not move the principal—only the interest payments. Every quarter or semi-annual period, the floating-rate reset occurs. If floating rates have risen, the manager receives more cash. If they have fallen, the manager pays the net difference. Across both legs, cash flows net: the manager effectively swaps its floating-rate inflows (from the bond's coupon or as rates rise) for a fixed payment.

This structure is the inverse of a [bond](/bond/)'s payoff: bonds gain when rates fall (higher present value of fixed coupons) and lose when rates rise. A pay-fixed swap loses when rates fall and gains when rates rise. The two positions hedge each other.

## Choosing the notional amount and duration

A portfolio manager must decide how much of the portfolio's duration to hedge. A full hedge means the swap's [duration](/duration/) exactly offsets the portfolio's duration, reducing net [interest-rate-risk](/interest-rate-risk/) to near zero. A partial hedge leaves some duration exposure, allowing the portfolio to benefit if rates fall while capping losses if rates rise.

The swap's duration depends on its maturity and the level of rates. A five-year pay-fixed swap will have a duration of roughly 4–4.5 years, assuming moderate [volatility](/historical-volatility/). If the portfolio duration is 6 years and the manager wants to reduce it to 2 years, it might enter a swap notional of 60–65% of the portfolio value. The resulting blended duration becomes shorter.

Selecting notional size also reflects [liquidity](/liquidation/) and [counterparty-risk](/counterparty-risk/) constraints. A very large swap notional relative to market depth can result in wider [bid-ask-spread](/bid-ask-spread/) pricing. Counterparty concentration—having too much exposure to a single [broker](/broker/) or dealer—can create [operational-risk](/operational-risk/) if that counterparty fails.

## Mark-to-market offset in a rising-rate scenario

Suppose a manager holds a $100 million portfolio of five-year corporates with an average coupon of 3% and [duration](/duration/) of 4.5 years. Interest rates rise by 0.5%. The portfolio's market value falls by approximately 0.5% × 4.5 = 2.25%, or $2.25 million.

The manager simultaneously entered a pay-fixed swap with a notional of $80 million at 4.2% fixed, receiving three-month [SOFR](/sofr/). After rates rise and the three-month SOFR reset moves higher, the manager receives more cash on the floating leg each period. The swap has increased in economic value—roughly 2.25% × (80% of portfolio) = $1.8 million in mark-to-market gain on the swap position.

The net loss on the hedged portfolio is therefore $2.25 million (bond loss) minus $1.8 million (swap gain) = $0.45 million, a 75% reduction in downside. The remaining exposure reflects the 20% unhedged portion and any slippage in the hedge due to [basis-risk](/basis-risk/) (the bond index and the swap curve may not move in lockstep).

## Duration reduction vs. outright sale

A critical advantage of swap hedging over selling bonds is flexibility. If the manager expects rates to rise, then fall later, a swap can be unwound or reversed. The portfolio remains intact, collecting coupons and maintaining reinvestment opportunities at higher rates. A sale, by contrast, forces the manager to buy back at an unfavorable time or hold cash (earning low returns) until rates peak.

Swap hedging also preserves [credit risk](/credit-risk/) exposure. The portfolio's corporate or municipal bonds still benefit if the issuer's [credit-spread](/credit-spread/) narrows (if it gets downgraded less than the market expects, or if the sector recovers). A pure sell-and-hold-cash strategy forgoes this alpha. The swap addresses only the [duration](/duration/) component of risk, leaving spread and credit selection intact.

## Costs and counterparty considerations

Swap hedging is not free. The manager pays a [management-fee](/management-fee/) to the swap dealer (typically a few basis points of notional, or embedded in the fixed rate quoted). The manager also assumes [counterparty-risk](/counterparty-risk/)—if the dealer fails, the manager cannot unwind the swap without delay and at potentially worse pricing. Large institutional managers often mitigate this by dealing with multiple dealers, using clearing mechanisms where available, and including [credit-event-sovereign](/credit-event-sovereign/) clauses to manage termination.

The effective cost of hedging is often viewed as the difference between the fixed rate on the swap and the yield available on new bonds with the same duration. If new bonds yield 5% and the swap fixed rate is 4.8%, the manager is paying an effective 0.2% premium to hedge. Over a five-year period, this compounds; on a $100 million portfolio, it might cost $100,000 per year in foregone yield.

## When to layer swaps or adjust hedge ratios

As rates move, the hedge ratio may no longer be optimal. If rates have already risen sharply, the portfolio's [duration](/duration/) may have contracted (because of higher discount rates on long coupons). The swap's notional amount might now be too large relative to remaining risk. The manager can reduce the notional by entering a receive-fixed swap (the opposite trade), unwinding part of the hedge. Conversely, if rates have fallen and the portfolio's duration has extended, adding more swap notional may be warranted.

Some managers layer hedges—entering multiple swaps at different rates to create a range of protection. A manager expecting rates to rise to 5% but not beyond might enter one pay-fixed swap at 4.5% for full protection, and another at 4.8% for partial protection if rates overshoot. This approach allows participation in some upside scenarios while capping downside.

## See also

<div class="wiki-seealso">

### Closely related

- [Interest-rate-swap](/interest-rate-swap/) — cash-flow mechanics and standard terminology
- [Duration](/duration/) — how to measure a bond portfolio's rate sensitivity
- [Interest-rate-risk](/interest-rate-risk/) — sources of loss in fixed-income portfolios
- [Counterparty-risk](/counterparty-risk/) — hazard of the swap dealer's failure to pay
- [Bond](/bond/) — fundamentals and coupon mechanics
- [Derivatives-hedging](/derivatives-hedging/) — broader uses of swaps, options, and forwards
- [Basis-risk](/basis-risk/) — imperfect correlation between the hedge and the underlying risk

### Wider context

- [Duration](/duration/) — impact on portfolio value when rates change
- Mark-to-market — accounting treatment and risk measurement
- [Federal-reserve](/federal-reserve/) — rate expectations and forward guidance
- [Monetary-policy](/monetary-policy/) — how central banks influence swap curves

</div>
