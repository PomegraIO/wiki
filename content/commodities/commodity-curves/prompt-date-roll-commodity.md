---
title: "Prompt Date and the Roll Window in Commodity Futures"
description: "What is the prompt date in commodity futures? Learn how roll windows work, why contracts expire, and how approaching expiry affects basis and spreads."
keywords:
  - prompt date commodity
  - roll window futures
  - commodity futures expiry
  - front-month contract
  - commodity curve roll
image: /svg/commodities.svg
---

*The **prompt date** (or first-nearby) is the nearest contract month not yet expired, and the **roll window** is the period when traders shift positions from one contract to the next before expiration. Understanding when and why rolls happen is essential to reading commodity markets, because basis risk and calendar spreads spike precisely as contracts enter their roll window.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Prompt Date & Roll Window — key facts</div>

<img src="/svg/commodities.svg" alt="An abstract editorial mark for commodities." />

<div class="wiki-infobox-caption">The prompt date is the nearest active contract, and rolling occurs in a defined window before expiry to avoid physical settlement.</div>

|   |   |
|---|---|
| **Prompt date** | Nearest contract month still open for trading |
| **Roll window** | Period (typically 5–20 days before expiry) when volume shifts to next month |
| **Typical expiry** | Contract-specific: crude oil ~3 weeks before delivery; natural gas ~3 business days |
| **Volume pattern** | Open interest migrates from front to back month during roll window |
| **Basis behaviour** | Often widens as front month approaches expiry and physical delivery looms |

</aside>

## What the prompt date is

The **prompt date** is the active commodity futures contract closest to settlement or delivery. If today is January 15 and March crude oil futures expire February 19, then March is the prompt month. The contract is listed and liquid because it represents the nearest market consensus on price and supply-demand balance.

Each commodity has its own prompt-month convention. Crude oil and gasoline expire approximately 21 calendar days before the month ends, at a date set by the exchange. Natural gas is tighter—typically 3 business days before month-end. Agricultural futures vary: corn, soybeans, and wheat have distinct delivery-period rules. Precious metals, energy products, and livestock all have their own exchange-mandated calendars.

The prompt date matures continuously. As time passes and the prompt month expires, the next contract (the deferred month, previously the second-nearby) becomes the new prompt. This creates a rolling sequence of "first nearby," "second nearby," and further-forward contracts.

## Why the roll window matters

A few weeks before expiry, trading volume begins to drift from the prompt month to the next contract. This is the **roll window**—the practical period when most active traders exit their prompt-month positions and re-establish them in the deferred month.

Rolling happens because:

1. **Physical delivery risk.** As contracts near expiry, they become subject to [delivery](/) obligations or cash settlement. Many traders, especially financial speculators, want no part of receiving truckloads of crude or soybean. They exit.

2. **Liquidity preservation.** Open interest (total outstanding contracts) in the expiring month shrinks as traders roll. The deferred month grows in volume and becomes the new focal point for price discovery. [Market makers](/market-maker-trading/) follow the volume.

3. **Basis convergence.** As expiry nears, the prompt month's price must converge toward cash (spot) price. A trader holding a forward position through roll will face widening or narrowing [basis](/basis/) depending on storage costs, convenience yield, and market conditions—mechanics that become acute as delivery looms.

Exchanges and clearinghouses set explicit last-trading dates to enforce orderly rolls. A trader who forgets to exit before the cutoff may find themselves forced into settlement or, worse, forced to deliver or accept delivery at unfavourable rates.

## How the roll window changes market behaviour

During the roll window, a few patterns emerge:

**Spread widening.** The calendar spread between prompt and deferred months often widens because traders are selling the front month while simultaneously buying the back month. If storage or convenience yield is limited, the spread can spike to reflect the urgency of the roll.

**Volatility concentration.** Price swings can intensify in the prompt month in the final trading days, as large positions are forced to exit and smaller players gamble on last-minute repricing.

**Contango vs backwardation shifts.** In a [contango](/contango/) market (where forward prices exceed spot), the prompt month may trade below the deferred month—making the roll cost-inefficient. In [backwardation](/backwardation/) (forward prices below spot), the prompt month trades at a premium; rolling forward requires eating that loss. Traders factor these roll costs into their entry and exit decisions.

**Basis behaviour.** The [cash-forward basis](/basis/) can widen sharply if physical supply tightens (increasing convenience yield) or excess inventory builds (reducing it). The prompt month is where this cash-forward premium is most pronounced because it faces imminent delivery.

## Practical timing of the roll

Different participants roll at different times, depending on their risk appetite and operational constraints:

- **Large index funds and systematic traders** often roll on calendrical schedules—for instance, always rolling 5 business days before expiry to minimize slippage.
- **Hedgers** may roll only when operationally necessary (e.g., a refinery locking in crude supply for the next month).
- **Speculators** may hold through roll, betting on price moves, then exit moments before expiry.

Volume data (open interest and settlement statistics) reveal the roll. You can often see the exact date when the majority of traders exited by spotting the sharp drop in prompt-month open interest and corresponding jump in the deferred-month open interest.

## Understanding forward curves through rolls

The forward curve is a sequence of prices for each month-ahead contract. Each roll event leaves a fingerprint on the curve. In [backwardated](/backwardation/) markets (spot premium), near-term contracts trade at higher prices; the moment the prompt expires, the next deferred contract becomes the new first nearby and trades at that premium. The curve is continually "rolling down" toward the prompt, reflecting the ticking clock.

## See also

<div class="wiki-seealso">

### Closely related

- [Contango and Backwardation](/contango/) — How forward prices can exceed or fall below spot price
- Commodity Forward Curve — The sequence of forward prices across contract months
- [Basis Risk](/basis-risk/) — Risk from widening or narrowing cash-forward gap
- Convenience Yield — Why holding physical commodity sometimes beats owning the forward
- [Calendar Spread](/spread/) — Trading the price difference between two contract months
- [Marked to Market](/commodity-curve-marking-to-market/) — Repricing a forward position daily using the curve

### Wider context

- [Futures Contract](/futures-contract/) — Legal definition of commodity futures exchange-traded contracts
- [Spot Rate](/spot-rate/) — Cash price for immediate delivery
- [Forward Contract](/forward-contract/) — Over-the-counter bilateral commodity agreements
- [Price Discovery](/price-discovery/) — How markets determine the fair value of assets

</div>
