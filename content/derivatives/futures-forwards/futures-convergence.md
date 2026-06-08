---
title: "Futures Convergence"
description: "The process by which a futures contract's price approaches the spot price as the expiration date nears."
keywords:
  - futures pricing
  - spot price
  - expiration mechanics
  - arbitrage
  - basis
image: "/svg/derivatives.svg"
---

*Futures convergence is the economic law that a [futures contract](/futures-contract/)'s price must equal the [spot price](/spot-exchange-rate/) of the underlying asset on the day it expires. As expiration approaches, any gap between the two narrows as [arbitrageurs](/algorithmic-trading/) eliminate the opportunity for riskless profit. Understanding convergence is essential for hedgers, speculators, and [market makers](/market-maker-trading/) alike—it determines the final payoff and shapes strategies throughout the contract's life.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Futures Convergence — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">At expiration, the futures price must equal the spot price, or arbitrage eliminates the gap.</div>

|   |   |
|---|---|
| **What it is** | The mathematical requirement that futures prices converge to spot prices as expiration date arrives |
| **Also called** | Basis convergence, convergence to spot |
| **The mechanism** | Arbitrage: buying low and selling high across the two markets until prices align |
| **Time to convergence** | Complete at the final settlement date (e.g., third Friday for equity index futures) |
| **What can prevent it** | [Delivery constraints](/delivery-notice/), [credit events](/credit-event-sovereign/), or market disruption; rare |

</aside>

## Why prices must converge

Consider a simple scenario. A [stock](/stock/) trades at £100 today. A [futures contract](/futures-contract/) on that stock expires in three months and currently trades at £108. An [arbitrageur](/algorithmic-trading/) immediately buys the stock at £100, simultaneously selling the futures at £108, and locks in a £8 profit (less [financing costs](/cost-of-debt/)).

When the contract expires in three months, the futures must settle at whatever the actual stock price is—say, £105. The arbitrageur owns the stock at cost basis £100, sells it into the futures settlement at £105 (the convergence price), and pockets the £5 gain, plus the £8 profit from the initial spread. That £8 gain is riskless, which is precisely why it cannot persist.

If enough arbitrageurs perform this trade, buying physical stock and selling futures, the futures price will be bid down and the spot price may be bid up slightly. The spread collapses. By expiration day, the two prices must be identical—if they diverged, someone could repeat the arbitrage and capture a riskless profit again.

## The basis and its lifecycle

The **basis** is the difference between the futures price and the spot price:

```
Basis = Futures price – Spot price
```

Early in a contract's life, the basis can be large and positive (futures trading at a [premium](/etf-premium-discount/)) or occasionally negative (futures trading at a discount). But as expiration approaches, the basis must shrink toward zero.

In [commodity futures](/crude-oil/), the basis often reflects [storage costs](/interest-coverage-ratio/) and [interest rate](/interest-rate/) expense. A barrel of oil in the ground (spot) must be stored and financed if you want to hold it three months, so the futures contract trades at a higher price to compensate the holder for those costs. This is called [contango](/contango/).

In [equity index futures](/sp-500-index/), the basis reflects the [dividend yield](/dividend-yield/) and financing cost of holding the underlying [stocks](/stock/). Again, the futures typically trades at a premium, but this premium must erode to zero at expiration.

## The mechanics near expiration

In the final trading day before expiration, convergence is almost complete. The futures price will track the spot price almost tick-for-tick. If the spot opens at £104.50, the futures opens at £104.51 or £104.49, but the 1-cent difference is mere noise—trading costs and bid-ask [spreads](/bid-ask-spread/) prevent anyone from profiting on it.

On the actual settlement date, the exchange declares a final settlement price (often the [opening price](/price-discovery/), or sometimes a volume-weighted average price). Any remaining gap is eliminated by force—the [clearing house](/broker/) ensures that all long and short positions are square at that price.

For [physically settled contracts](/delivery-notice/) (like commodity futures), convergence is often tighter because holders can actually take delivery at spot prices. If a [corn](/corn/) futures contract trades above the local cash price by more than the cost of delivery, farmers will deliver and arbitrageurs vanish. The mechanism is biological and automatic.

For [cash-settled contracts](/expiration-contracts/) (like equity indices), convergence is guaranteed by the definition of the settlement price itself. There is no risk or friction—the exchange simply declares that the final price is the official spot price, and the game ends.

## Why convergence matters for hedging

A company that [hedges](/hedge-fund/) a purchase with a [futures contract](/futures-contract/) relies on convergence to ensure that the hedge price is honoured. If the futures price were to differ from the spot at expiration, the company would face an unexpected loss on the hedge.

This is usually not a risk—convergence is so reliable that textbooks treat it as a law of nature. But in stressed markets, [delivery constraints](/delivery-notice/) can emerge. During the 2020 oil price crash, some contracts faced so much uncertainty about whether physical delivery could occur that the basis remained distorted for days. This was rare and temporary, but it illustrates that convergence depends on market function.

More commonly, convergence risk is simply the risk that the spot price itself moves against you. If you shorted crude oil futures to hedge a purchase, convergence guarantees that your futures [settlement](/expiration-contracts/) price will match the spot. But the spot may have risen to £65/barrel by expiration, and you will pay that price. The convergence is mechanical; it does not protect you from the underlying price move.

## Convergence and the basis trade

Professional traders exploit convergence by taking [long positions](/bull-market/) in deferred contracts (expiring later) while selling near-term contracts short, betting that the [basis](/basis-risk/) will narrow as the near-term contract expires. This is called a **calendar spread** or **curve trade**. The trader profits if the basis compresses faster than expected, without betting on the direction of the spot price itself.

Convergence also ensures that calendar spreads eventually flatten—a near-term contract's premium over a deferred contract must shrink to zero as the near-term contract approaches expiration. This feature makes basis trading a lower-volatility alternative to directional speculation, especially appealing in stable commodity markets.

## Obstacles and exceptions

In nearly all liquid markets, convergence occurs without a hitch. But a few exceptions exist:

- **Physical delivery failure**: If delivery is impossible (e.g., a contract becomes undeliverable due to force majeure), the settlement may be forced to cash-only, and the settlement price might diverge from the true spot. This is vanishingly rare and usually stipulated in the contract terms.
- **Market suspension**: If an exchange halts trading in both the futures and the spot market, the final settlement price can be set administratively, sometimes with a lag. Convergence still occurs, but the mechanics are manual rather than automatic.
- **Illiquid spot markets**: In some commodities, the spot market is far less liquid than the futures market. The "true" spot price can be hard to define, and the settlement price may drift slightly. But the futures market is the authority, and convergence by definition occurs.

## See also

<div class="wiki-seealso">

### Closely related

- [Futures contract](/futures-contract/) — the instrument whose price converges to spot
- [Spot price](/spot-exchange-rate/) — the target price to which futures converge
- [Contango](/contango/) — when futures trade above spot; the basis that must narrow
- [Basis risk](/basis-risk/) — the broader problem of futures-spot misalignment
- [Delivery notice](/delivery-notice/) — the mechanism that enforces convergence in physical contracts
- [First notice day](/first-notice-day/) — when convergence enforcement becomes imminent

### Wider context

- [Arbitrage](/algorithmic-trading/) — the force that eliminates convergence gaps
- [Market maker](/market-maker-trading/) — traders who profit from providing tight pricing during convergence
- [Hedge fund](/hedge-fund/) — professional hedgers who depend on convergence reliability
- [Interest rate](/interest-rate/) — determines the cost of financing that shapes early-contract basis

</div>
