---
title: "Freight Rate Swap"
description: "A derivative that locks in shipping costs by exchanging floating freight rates for fixed payments, used to hedge bulk cargo expense volatility."
keywords:
  - shipping derivative
  - freight rate hedge
  - commodity shipping
  - bulk carrier costs
  - maritime derivative
  - hedging tools
image: "/svg/derivatives.svg"
---

*A **freight rate swap** is a derivative contract that exchanges floating shipping rates against a benchmark index for a fixed payment, allowing importers, exporters, and shipping companies to hedge the cost of moving bulk cargo. Most active in maritime transport—particularly for containers, dry bulk, and tankers—these swaps decouple physical shipping decisions from the financial exposure of rate volatility.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Freight Rate Swap — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives." />

<div class="wiki-infobox-caption">A financial contract managing shipping cost uncertainty through index-based rate exchange.</div>

|   |   |
|---|---|
| **What it is** | [Swap](/swap/) on freight benchmarks—usually cash-settled against published indices |
| **Settle mechanism** | Cash settlement; rarely physical delivery of shipping services |
| **Key indices** | Baltic Dry Index (BDI), Shanghai Containerized Freight Index (SCFI), time-charter equivalents |
| **Counterparties** | Exporters, importers, shipping lines, logistics firms, commodity traders, hedge funds |
| **Duration** | 3 months to 3 years; shorter than bond or equity swaps |
| **Price driver** | Cargo supply and demand, vessel availability, fuel costs, global trade flows |

</aside>

## How the swap locks in a shipping rate

A freight swap works like any [swap](/swap/): one party (the fixed payer) commits to pay a set rate per ton or per voyage, while the other (the floating payer) pays whatever a published freight index reports at each settlement date. Neither party ships anything themselves. A container operator expecting to import goods six months hence might pay the fixed rate today, fixing its logistics budget regardless of whether Baltic rates jump 40% or fall. The counterparty—perhaps a shipping line confident rates will rise—takes the floating side, pocketing the difference if rates exceed the strike.

The benchmark is everything. The Baltic Dry Index tracks large dry-bulk freight costs (iron ore, coal, grain). The SCFI reflects containerized box rates on major Asia–Europe and China–US routes. Time-charter equivalents (TCEs) translate a vessel's rental cost into an implied daily freight rate. Published in real time by exchanges and specialist firms, these indices settle disputes and eliminate ambiguity: there's no "what was the market rate?"—it's printed. This transparency is why swaps can exist without a physical shipping transaction.

## Who uses them and why

Exporters of steel, grain, or raw materials face a squeeze: they know a buyer will pay a lump sum for goods delivered in three months, but freight costs are unpredictable. Locking in a swap rate means that margin becomes certain. Importers buying bulk commodities similarly hedge transport cost as a fixed line item. Shipping lines, which own vessels, use swaps for the opposite reason: they may commit to a charterer at a negotiated rate but want to lock in their own operating costs, or they speculate on rate direction.

Trading firms and hedge funds trade freight swaps for pure price discovery and return. A prop trader might believe the SCFI is mispriced relative to the underlying supply of container capacity and short it via a swap, betting rates will fall. The swap market offers leverage and liquidity that physical shipping cannot. Some agricultural or metals firms use swaps as a crude substitute for an insurance contract—you cannot insure against freight costs per se, but a [forward-contract](/forward-contract/) or swap approximates that protection.

## Settlement and basis risk

Freight swaps are typically cash-settled monthly or quarterly. Neither party expects to hand over a ship or sign a bill of lading. The index fixes on a specified date (often the last business day of the month), and the difference between that index and the swap strike is multiplied by the notional quantity—say, 10,000 tons—and paid by the losing side. This simplicity keeps transactions fast and legal risk low: there is no ambiguity about whether a load was "properly shipped."

Basis risk, however, remains. The SCFI may not exactly reflect what your shipper offers you on your specific route; regional indices can diverge. A firm shipping from Hamburg to Shanghai might reference a different rate than the published index implies. Furthermore, spot rates (for immediate shipment) can differ from the forward rates embedded in a swap, especially if the freight curve is in steep contango or backwardation. A hedger must match the swap tenor and commodity type carefully or end up paying to hedge something that never materializes.

## The curve and the cost of leverage

The freight forward curve—the implied rates for future time periods—can slope upward (contango, suggesting rising demand or tightening capacity) or downward (backwardation, often reflecting oversupply). A company locking in a swap today at 125% of the current spot rate is betting the market will not be cheaper; that premium compensates the counterparty for the time and carrying cost implied in the forward market.

Swaps carry credit risk: each party must believe the other will settle at maturity. For large counterparties, this may be small; for a smaller operator, it can be significant. Many swaps are cleared through central counterparties, eliminating direct counterparty exposure but adding a small fee. Margin requirements (both initial and variation margin) mean that a sudden adverse move in rates forces cash collateral posting—a hidden cost for firms in tight liquidity positions.

## Why swaps instead of futures or forwards

Freight futures exist on some exchanges (the Baltic Exchange publishes them for BDI components), but swap contracts often offer longer tenors and better liquidity for customized cargo types and routes. A [futures-contract](/futures-contract/) is standardized and lives on an exchange; a swap is bespoke. If you need a 18-month hedge on a specific lane with a custom notional, swaps beat futures. Forwards are also available but concentrate counterparty credit risk with a single bank. A swap, especially if cleared, spreads that risk.

The downside: swaps are less liquid than standardized futures during market stress, and the bid–ask spread is wider. For small or infrequent hedgers, the cost of entering a swap can outweigh the benefit. Large, frequent shippers and vessel operators lean on swaps for their flexibility; occasional importers may instead accept the freight risk or use simpler [forward-contract](/forward-contract/) structures.

## See also

<div class="wiki-seealso">

### Closely related

- [Swap](/swap/) — the foundational exchange of fixed for floating cash flows
- [Forward-contract](/forward-contract/) — a non-standardized commitment to a future price
- [Futures-contract](/futures-contract/) — standardized exchange-traded contracts allowing long-term hedging
- [Weather-swap](/weather-swap/) — a swap tied to temperature or precipitation indices, similar structure to freight swaps
- Commodity hedging — the broader use of derivatives to lock in input costs
- [Counterparty-risk](/counterparty-risk/) — the credit exposure both parties assume in an over-the-counter swap

### Wider context

- Derivatives market overview — the ecosystem and regulation of swaps and forwards
- Baltic Dry Index — the leading benchmark for dry-bulk shipping rates
- Supply chain risk — the operational disruptions that freight swaps help to financialize

</div>
