---
title: "At What Contango Steepness Does Roll Cost Hurt ETF Returns"
description: "The relationship between annualised futures curve slope and drag on ETF returns from rolling contracts, with threshold calculations and examples."
keywords:
  - contango steepness roll cost etf
  - contango roll cost threshold
  - futures roll drag
  - etf commodity tracking
  - contango percentage threshold
  - commodity etf costs
image: "/svg/commodities.svg"
---

*When a [commodity ETF](/etf/) that holds futures must roll contracts into more expensive deferred months—the cost of steep **contango**—that drag erodes returns visibly. The threshold where roll costs become material depends on the [contango](/contango/) slope, the fund's turnover schedule, and the holding period.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Contango Steepness and ETF Roll Cost — key facts</div>

<img src="/svg/commodities.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">A commodity ETF's returns can be dragged significantly when the futures curve is steep and the fund rolls contracts frequently.</div>

|   |   |
|---|---|
| **Key metric** | Annualised curve slope as a percentage (e.g., 15%, 25%, 40%) |
| **Typical threshold** | ~10–15% annualised contango starts to noticeably reduce returns |
| **Material threshold** | >25% annualised contango can reduce annual returns by 5–15% or more |
| **Roll frequency** | Monthly rolls (common); some funds roll weekly, quarterly, or irregularly |
| **Cost formula** | Annual roll drag ≈ curve slope % × proportion of curve structure lost per roll |
| **Example impact** | A 30% annualised contango with monthly rolls ≈ 2–3% annual drag |
| **Extreme cases** | Energy contango >50% annualised; affects long-only commodity ETF returns severely |

</aside>

## Understanding Contango and the Roll Mechanic

**Contango** occurs when futures contracts further out in time trade at higher prices than near-term contracts. For storable commodities like crude oil or natural gas, contango is the norm: storage costs, carry costs, and financing are embedded in the premium of deferred contracts.

An ETF holding a December crude contract cannot hold that contract to infinity. As December approaches and trading volumes shift to the January contract, the December contract becomes illiquid. The ETF must sell December and buy January—transferring its exposure to a more liquid month.

If January is trading at a premium above December (contango), the ETF locks in that spread as a realized loss. Repeat this roll monthly for 12 months, and the cumulative drag can be substantial.

## The Contango Slope: A Quantifiable Measure

The slope of the commodity curve is usually expressed as a percentage per month or annualised percentage. 

**Example:**
- Near contract (Dec): \$80/barrel
- 1-month deferred (Jan): \$81/barrel
- Spread: \$1 = 1.25% monthly = ~15% annualised

Annualised slope = (1 − F₀ / Fₙ) × (12 / n) × 100, where F₀ is the near contract, Fₙ is n months out.

In this example, rolling from Dec to Jan locks in a 1.25% loss, or if done monthly throughout the year, roughly 15% cumulative drag. But not all of that 15% shows as ETF drag, because the ETF's exposure is not being "reset" from spot each time; it is transferring between positions on the curve.

## Calculating Roll Drag for an ETF

The actual drag depends on how much of the curve the ETF gives up per roll.

**Simple case (monthly rolling):**
If the curve is 15% annualised in contango and the ETF rolls monthly, it gives up approximately 15% ÷ 12 = 1.25% per roll. Over a year of monthly rolls, that is 12 × 1.25% ≈ 15% cumulative drag.

**Reality check:**
A 15% annualised ETF with zero underlying price movement would lose 15% in a year due to contango rolls alone. If the commodity price also rises 15%, the ETF breaks even (gross gain of 15% minus roll drag of 15%). This is why steep contango environments are notoriously unkind to long-only commodity ETFs.

**More nuanced calculation:**
The realized drag per roll = (Fₙ − F₀) / F₀, where Fₙ is the contract being bought and F₀ is the one being sold. If the roll happens every month and the slope is constant, annualised drag ≈ 12 × single-month spread / current price.

## Threshold: When Roll Cost Becomes Material

**Below ~10% annualised contango:** Roll costs are modest. An ETF with a 5% contango slope might suffer 0.4% annual drag—largely invisible against normal price volatility.

**10–20% annualised contango:** Roll costs become noticeable. A 15% slope produces roughly 1.25% per month, or 15% annualised drag. Against commodity price moves of ±5–10% annually, this is material.

**20–40% annualised contango:** Roll costs become dominant. A 30% slope creates 2.5% monthly drag, or 30% annualised. An ETF in this regime can lose 10–15% annually from rolls alone, independent of spot price direction.

**>40% annualised contango:** Extreme. Occurs in energy markets during supply shocks or financial stress. WTI crude oil has traded with 50%+ annualised contango; a long-only crude ETF in such conditions loses 30–40% annually from rolls, making the fund performance-drag despite stable or rising spot prices.

## Worked Example: Comparing Light and Heavy Contango

**Scenario 1: Light Contango (Agricultural)**
- Corn curve: Dec \$4.50, Jan \$4.54, Feb \$4.58
- Monthly spread: \$0.04 on a base of \$4.50 = 0.89% monthly
- Annualised: ~10.7%
- Annual roll drag for an ETF rolling monthly: approximately 10.7%
- If spot price is flat, a \$100 investment becomes \$89.30 after one year
- Impact: Visible but not catastrophic for longer-term holds

**Scenario 2: Heavy Contango (Energy)**
- WTI curve: Dec \$70, Jan \$73, Feb \$76
- Monthly spreads: Jan premium = \$3/$70 = 4.3%; Feb premium from Jan = \$3/$73 = 4.1%
- Annualised (approximate): 50%+
- Annual roll drag: Roughly 50% (exaggerated by rolling deeper into the curve each time)
- If spot price is flat, a \$100 investment becomes \$50 after one year (vastly simplified, but illustrative)
- Impact: Severe; positions held beyond a few rolls face significant leakage

In scenario 2, a trader holding a long crude ETF expecting stabilization would lose money from rolls even if the spot price rallies. The ETF is a poor vehicle for long-dated exposure in steeply contango markets.

## How Rolling Frequency Affects Drag

Some commodity ETFs roll contracts on fixed schedules (the first week of every month); others roll on an offset (staggering the roll over multiple days to minimize market impact); still others roll irregularly based on liquidity.

**Monthly rolling** (most common): Maximises roll frequency. With a 30% annualised contango, it produces about 2.5% monthly drag, accumulating to ~30% annually.

**Quarterly rolling:** Less frequent. Over three months, the ETF is exposed to the full depth of contango but only rolls four times yearly. A 30% annualised contango across three months might cost 7–8% in a single roll, but fewer total rolls can result in similar or slightly lower annual drag (around 28–30%) because the ETF may benefit from mean reversion or curve flattening during holding periods.

**Weekly rolling:** Seen in some short-term trading vehicles. Theoretically more efficient (smaller spreads between weekly contracts), but transaction costs and slippage can outweigh the benefit of tighter spreads.

## Contango, Curve Shape, and Holding Period

The true cost of contango is interactive with how long an investor holds the position.

An investor buying a commodity ETF in a 30% annualised contango environment does not necessarily lose 30%. If the commodity price appreciates 35%, the investor is ahead despite the roll drag. The problem is that an investor *expecting* flat or falling prices gets hit from both directions—price decline plus roll losses.

For tactical short-term bets, steep contango is a headwind. For strategic long-term allocation, the investor must believe the commodity will appreciate enough to overcome the drag, or choose a different vehicle (a long futures contract at a fixed date, a forward contract, or physical holding).

## Comparing Contango Regimes Across Commodities

**Natural gas:** Highly seasonal; can swing from severe backwardation (winter high demand) to steep contango (summer low demand). Annualised contango can reach 40–60% in summer.

**Crude oil:** Typically 10–25% annualised contango. Spikes to 50%+ during supply disruptions or financial crises. Normal baseline is modest but persistent.

**Precious metals (gold, silver):** Often 5–12% annualised contango due to gold lease rates and financing costs. Much flatter than energy.

**Agricultural:** Seasonal; peaks around harvest when storage is full, can flatten or reverse post-harvest. Corn and soybeans typically 5–20% annualised contango.

An ETF investor comparing performance across commodity ETFs must adjust for expected roll drag. A gold ETF in a 10% contango market and a crude ETF in a 35% contango market are not directly comparable on past returns without netting out the structural drag.

## Mitigation Strategies for ETF Investors

Investors aware of steep contango can make several choices:

- **Hold shorter-term:** Own the position for weeks, not years, to minimise cumulative roll cost.
- **Scale into position:** Reduce the impact of one large purchase by entering gradually; if contango flattens, later tranches roll cheaper.
- **Diversify away from pure long:** Use inverse (short) commodity ETFs or structured products to hedge against roll drag or express directional views without contango exposure.
- **Choose better timing:** Buy commodity ETFs after sharp sell-offs when contango is often flattened, not after prolonged rallies when contango re-steepens.
- **Consider alternatives:** Forwards, structured notes with embedded roll management, or managed futures funds that dynamically adjust exposure based on curve shape.

## See also

<div class="wiki-seealso">

### Closely related

- [Contango](/contango/) — Definition and causes of deferred contract premiums
- [Rolling hedge strategy explained](/rolling-hedge-strategy-explained/) — How to manage roll costs over time
- [Backwardation](/backwardation/) — When near contracts trade above deferred, reducing roll drag
- Commodity curves — Structure and dynamics of multi-month futures prices
- [Carry trade](/carry-trade/) — Exploiting the contango curve for profit
- [Futures contract](/futures-contract/) — Mechanics of standardised commodity contracts

### Wider context

- [ETF](/etf/) — How commodity ETFs track underlying futures
- [Expense ratio](/expense-ratio/) — Management fees; combined with roll costs, comprise true annual drag
- [Index provider](/index-provider/) — How commodity indices are constructed and rolled
- [Natural gas](/natural-gas/) — Highly seasonal commodity with extreme contango variance
- [Crude oil](/crude-oil/) — Storable commodity with persistent contango in normal markets

</div>
