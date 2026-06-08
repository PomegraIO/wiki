---
title: "Tailing the Hedge"
description: "Reducing futures contract count to account for daily mark-to-market cash flows when hedging future obligations."
keywords:
  - futures hedging
  - daily settlement
  - contract adjustment
  - basis risk
  - cash flow timing
image: "/svg/derivatives.svg"
---

*A **tailed hedge** is a futures position that is slightly smaller than the underlying exposure it protects, adjusted downward to compensate for daily mark-to-market cash flows earned during the holding period. Because futures contracts settle daily while forward contracts settle at maturity, a futures hedge accumulates interest on cash gained or lost each day—money that reduces the net size of the position needed to achieve the same final payoff.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Tailing the Hedge — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Futures hedges require smaller notional positions than forwards because daily settlement generates its own return.</div>

|   |   |
|---|---|
| **What it is** | A reduction in the number of [futures contracts](/futures-contract/) held to hedge an exposure, accounting for reinvested daily settlement gains or losses |
| **Also called** | Hedge tailing, dynamic hedging adjustment |
| **When it matters** | Any [futures contract](/futures-contract/) hedge held for weeks or months; essential when rates are high |
| **Core math** | Number of futures contracts = (Exposure × Discount factor) / Contract size |
| **Alternative** | Holding the full notional hedge and accepting the compounding effect |

</aside>

## Why daily settlement creates this problem

When you enter a [futures contract](/futures-contract/), the exchange demands settlement of daily price moves. If the futures price rises, you receive cash immediately; if it falls, you pay. This daily cash flow is fundamentally different from a [forward contract](/forward-contract/), which settles all gains or losses in one lump sum at maturity.

A company hedging a future purchase with futures will receive cash each day the price falls in its favour. That cash earns [interest](/interest-rate/)—whether reinvested at [LIBOR](/libor/), the risk-free rate, or the company's own cost of capital. Over weeks or months, this interest accumulates to a material amount.

The result: you need *fewer* futures contracts to achieve the same economic hedge as a forward would provide.

## The arithmetic of tailing

Suppose you plan to buy 1 million barrels of crude oil in 90 days. A [crude oil futures contract](/crude-oil/) controls 1,000 barrels. Naively, you might short 1,000 contracts as a perfect [hedge](/hedge-fund/).

But your daily gains will earn interest. If the interest rate is 5 per cent per annum—roughly 1.25 per cent over 90 days—then the present value of your position 90 days from now is worth about 1.25 per cent less than its face value *today*. To achieve the same protection, you should buy only 987 or 988 contracts instead, and let the daily interest accumulation make up the difference.

More formally:

```
Number of futures = (Notional exposure × Discount factor) / Contract size
```

where the discount factor reflects the interest rate and time to maturity. As rates rise or time extends, the tail becomes larger and you short progressively fewer contracts.

## When to tail and when to ignore it

For overnight hedges or short-dated positions, tailing is negligible. If you're hedging three weeks of [inventory turnover](/inventory-turnover/), the interest effect is pounds, not thousands.

But institutional [asset managers](/return-on-assets/), [pension funds](/401k-plan/), and corporate [treasury departments](/cash-flow-statement/) routinely tail. A monthly or quarterly hedge that accounts for tailing can reduce [operational costs](/operational-risk/) by 1–2 per cent of the hedged amount. In a portfolio of billions, that is material.

Tailing also matters in [dynamic hedging](/volatility-smile/) strategies where positions are rebalanced frequently. Each rebalancing implicitly generates cash that must be reinvested, and failing to account for it introduces a subtle drift in the [hedge ratio](/basis-risk/).

## The cost and benefit trade-off

Tailing is *defensive*—it prevents you from over-hedging and accidentally creating a short bias. A tailed hedge protects against the scenario where daily cash gains compound so substantially that your effective short position grows larger than intended, leaving you exposed to prices moving in the unfavourable direction.

The drawback is administrative friction. Calculating the exact discount factor requires knowing your funding rate precisely, and recalculating it as rates shift means continuously adjusting contract counts. Some firms accept a small amount of over-hedging (holding full notional futures) to avoid this overhead.

For [leveraged](/leverage-ratio-forex/) or [prime brokerage](/hedge-fund/) setups, where every basis point of return is tracked, tailing is standard. For smaller hedges or volatile rate environments where recalculation becomes expensive, a simpler approach—holding the full notional and accepting the rounding—is common.

## Relationship to other hedging mechanics

Tailing sits between two extremes. On one end is a perfect [forward contract](/forward-contract/), which requires zero adjustment because there is no daily settlement. On the other is a naive [futures contract](/futures-contract/) hedge of exactly the same notional size, which slightly over-hedges because of reinvested cash.

The concept also connects to [repo](/hedge-fund/) financing. If you're financing a hedge via a repo loan, your borrowing cost *is* your funding rate, and tailing accounts for this automatically. In a falling-rate environment, your daily cash gains compound at a higher rate, so tailing requires an even smaller hedge.

## See also

<div class="wiki-seealso">

### Closely related

- [Futures contract](/futures-contract/) — the daily-settlement mechanism that makes tailing necessary
- [Basis risk](/basis-risk/) — the broader problem of imperfect hedging that tailing refines
- [Forward contract](/forward-contract/) — the alternative with single settlement and no tail effect
- [Futures convergence](/futures-convergence/) — how the futures price aligns with spot at expiration
- [Delivery notice](/delivery-notice/) — the mechanics of actually taking or making delivery

### Wider context

- [Hedge fund](/hedge-fund/) — institutions that routinely use tailed hedges at scale
- [Interest rate](/interest-rate/) — the discount factor that determines tail size
- [Crude oil](/crude-oil/) — a common underlying for long-dated commodity hedges
- [Cash conversion cycle](/cash-conversion-cycle/) — the operational periods over which tailing compounds

</div>
