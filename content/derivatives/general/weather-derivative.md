---
title: "Weather Derivative"
description: "A contract whose payoff depends on meteorological outcomes such as temperature, rainfall, or snow rather than asset prices."
keywords:
  - weather contract
  - temperature derivative
  - rainfall derivative
  - weather swap
  - parametric insurance
image: "/svg/derivatives.svg"
---

*A **weather derivative** is a derivative contract whose payoff is determined by a meteorological measurement—temperature, rainfall, wind speed, or snowfall—rather than the price of a financial asset or commodity. Weather derivatives allow businesses with exposure to climate fluctuations to hedge that risk or to speculate on seasonal weather patterns.*

<div class="wiki-hatnote">

For weather insurance products, see [auto-insurance](/auto-insurance/). Weather derivatives are financial hedges, not traditional insurance policies.

</div>

## Why weather matters economically

Many businesses depend critically on weather. Ski resorts and snowplough contractors thrive on cold winters; warm winters erode their earnings. Farmers' yields hinge on rainfall timing and temperatures during the growing season. Energy utilities face demand shocks from temperature swings: heat waves spike air-conditioning load; cold snaps spike heating demand. An unusually mild winter can devastate a heating-oil supplier's annual profit.

For decades, these weather-dependent businesses had no tradable hedge. You cannot short the weather itself. A ski resort owner facing a warm winter could diversify into other businesses or store equipment to minimize losses, but had no financial instrument to offset the risk. Weather derivatives solved this by creating synthetic contracts where the payoff reflects meteorological data.

## Structure and settlement

A weather derivative is typically a [forward contract](/forward-contract/) or [swap](/interest-rate/), structured around a temperature index. The simplest form is a **heating degree-days (HDD) contract** or a **cooling degree-days (CDD) contract**.

**Heating degree-days** measure how cold a season was. If the average daily temperature is 65°F, and the base (reference) is 65°F, then zero HDD for that day. If the average is 50°F, that is 15 HDD. Over a winter, cumulative HDDs can be thousands. An HDD contract specifies a payoff formula: if actual cumulative HDDs fall below a threshold, the contract holder receives a cash payment proportional to the shortfall. This compensates a heating-oil seller for a warm winter—fewer people buy heating oil.

**Cooling degree-days** work symmetrically. If cumulative CDDs in summer fall below a strike level (milder-than-normal summer), an air-conditioning provider is compensated. If actual CDDs exceed the strike, the contract holder pays out.

Other indices include **rainfall derivatives** (indexed to total rainfall in a region over a season), **wind derivatives** (indexed to average wind speed or wind-power density), and **snow depth derivatives** (indexed to seasonal snow accumulation). Each is settled against official meteorological data published by government agencies—the National Weather Service in the US, the Met Office in the UK.

## Payoff mechanics and leverage

A typical structure: an HDD [swap](/interest-rate/) with a [notional value](/notional-value/) of $10,000 per HDD. Actual winter HDDs average 2,000. The contract specifies a strike of 2,100 HDDs. If actual is 1,900, the contract holder receives (2,100 − 1,900) × $10,000 = $2 million. If actual is 2,200, the contract holder pays (2,200 − 2,100) × $10,000 = $1 million.

Like other derivatives, weather contracts embed leverage. A heating company might control $10 million of climate risk exposure (notional) with an upfront margin deposit of $200,000. Temperature swings that would cause a few percentage change in annual revenue can generate large absolute dollar P&Ls on the derivative position if the notional is high.

**Collars** are common risk-control tools. A heating oil supplier, unwilling to lose more than $500,000 in a warm winter, might buy a CDD contract (receiving payoff if it's warm) while selling an HDD contract above a threshold (limiting profit if it's cold). The net cost is zero or near-zero after netting premiums.

## Who trades weather derivatives

**End-users** are the primary hedgers: utilities, ski resorts, agricultural concerns, and food-processing companies. A power utility expecting higher summer demand due to hot weather can sell CDD [futures](/futures-contract/) locking in revenue. A dairy farmer worrying about drought can buy rainfall derivatives covering his region, receiving cash if rainfall falls short of normal.

**Weather risk specialists** (some banks, specialized hedge funds) trade weather derivatives purely as a financial bet, taking positions on seasonal temperature or rainfall forecasts. They provide [liquidity](/liquidity-risk/) and [price discovery](/price-discovery/), allowing hedgers to lay off risk at market prices.

**Reinsurers** occasionally trade weather derivatives to manage their natural-disaster exposure. A reinsurer exposed to hurricane risk across the Atlantic basin might buy hurricane-intensity derivatives that trigger if storms exceed defined thresholds.

## Market structure and limitations

The weather derivatives market is small relative to [interest rate swaps](/interest-rate/) or [commodity futures](/crude-oil/), but is significant in specific sectors. The Chicago Mercantile Exchange (CME) lists HDD and CDD [futures contracts](/futures-contract/) on major US cities (Chicago, New York, Dallas, Los Angeles). Volumes are steady but not liquid; bid-ask spreads can be wide.

Over-the-counter (OTC) contracts are more common, especially for rainfall and wind indices. A farming co-op might negotiate a bespoke rainfall contract with a bank, tailored to the specific region and crop-critical months. Because these are OTC and non-standardised, liquidity is poor and [counterparty risk](/counterparty-risk/) is higher.

## Basis risk and model assumptions

The payoff is indexed to official meteorological measurements, but a specific business's weather exposure may not align perfectly. An ice-skating rink in Manhattan is exposed to temperature, but the amount of footfall loss per degree varies with marketing, competing entertainment, and regional holidays. Even if HDD contracts pay off accurately, the correlation between HDDs and actual business loss is imperfect. This **basis risk** cannot be fully hedged.

Furthermore, weather is measured at a central weather station (e.g., LaGuardia Airport for NYC). But the rink's local weather may differ slightly; a frost warning for LaGuardia might not materialize on the rink's outdoor rink. Basis risk can be substantial in regional or hyper-local weather bets.

## Parametric vs. indemnity hedges

Weather derivatives are **parametric** contracts: they pay off based on a defined meteorological index, regardless of actual business loss. You don't need to prove you lost money; if HDDs fall below the strike, you receive the payout.

Traditional [insurance](/auto-insurance/), by contrast, is **indemnity-based**: the insurer compensates you for your actual loss, but you must document the damage. Indemnity insurance is slower to settle (claims adjusters assess damage) and requires proof of loss.

Parametric weather derivatives settle instantly when the measurement is published. If the National Weather Service records 1,800 HDDs on the last day of March (end of the winter observation period), the contract settles that day. This speed is appealing to hedgers, but it means basis risk is the hedger's problem, not the derivative issuer's.

## Applications in agriculture and energy

**Agricultural derivatives** on rainfall help farmers in regions with high rainfall variability. A smallholder farmer in India or sub-Saharan Africa might buy a rainfall contract: if monsoon rains are below normal, the contract pays out, offsetting lost yield. This is cheaper and faster than traditional crop [insurance](/auto-insurance/).

**Energy derivatives** on temperature are used by utilities and energy traders. A natural gas utility in a cold-climate region buys HDD futures, locking in a minimum floor on revenue. A renewable-energy company (solar or wind) might buy temperature or wind derivatives to hedge production shortfalls caused by unusual weather.

## Pricing and assumptions

Weather contracts are priced using historical climatology and [Monte Carlo simulation](/discounted-cash-flow-valuation/). A bank estimating the fair price of an HDD contract runs a large sample of simulated winter temperatures based on 30–50 years of historical data, calculates the payoff distribution, and discounts expected payoffs at a risk-free rate. The model assumes weather patterns are stationary and independent of pricing activity—assumptions that hold reasonably well for weather, since no financial market can meaningfully alter the climate.

Climate change is altering weather distributions, making historical data less predictive. Banks have begun incorporating climate models and forward-looking trend adjustments into pricing. If a region's average winter is warming by 2°F per decade, the fair price of an HDD contract shifts lower (fewer HDDs expected in the future).

## Regulation and accounting

Weather derivatives are treated as financial derivatives under accounting standards. An end-user that buys a weather contract must designate it as a hedge (cash-flow hedge, typically) and mark it to fair value. The gain or loss flows through [other comprehensive income](/income-statement/) (OCI) until the underlying risk materializes.

Regulators view weather derivatives as leveraged financial instruments. Banks trading them must hold [capital](/capital-adequacy/) against counterparty risk and market risk. Some jurisdictions limit retail investors' access to weather derivatives, requiring an institutional accreditation or sophisticated-investor classification.

## See also

<div class="wiki-seealso">

### Closely related

- [Forward Contract](/forward-contract/) — the simplest weather derivative structure
- [Futures Contract](/futures-contract/) — CME HDD/CDD contracts are standardised weather futures
- Derivative — the broader family that weather derivatives belong to
- [Counterparty Risk](/counterparty-risk/) — especially relevant for OTC weather contracts
- [Notional Value](/notional-value/) — the amount per HDDs or rainfall index that scales the payout

### Wider context

- [Price Discovery](/price-discovery/) — weather markets establish consensus on seasonal weather patterns
- [Hedge Fund](/hedge-fund/) — specialized funds trade weather derivatives for profit
- [Interest Rate Swap](/interest-rate/) — the structural template weather contracts follow
- [Commodity](/crude-oil/) — natural gas and electricity prices correlate with temperature, creating related hedges
- [Risk Management](/enterprise-value/) — weather derivatives are a risk-transfer tool used by utilities and agriculture
- [Basis Risk](/currency-risk/) — the mismatch between a specific business's loss and the index payoff

</div>
