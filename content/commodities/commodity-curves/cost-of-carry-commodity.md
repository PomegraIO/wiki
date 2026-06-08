---
title: "Cost of Carry (Commodities)"
description: "The full financing, storage, and convenience-yield formula that determines why commodity futures trade above or below spot prices."
keywords:
  - commodity futures pricing
  - storage costs
  - convenience yield
  - carry trade
  - spot-forward relationship
  - contango
image: /svg/commodities.svg
---

*The **cost of carry** is the sum of all expenses required to hold a physical commodity from today until delivery at a futures contract's expiration date. It is the financial anchor that pins forward prices to spot prices, and the reason commodities trade in [contango](/contango/) or [backwardation](/backwardation/).*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Cost of Carry — key facts</div>

<img src="/svg/commodities.svg" alt="An abstract editorial mark for commodities and futures." />

<div class="wiki-infobox-caption">The bridge between spot and futures prices.</div>

|   |   |
|---|---|
| **What it is** | Total financing, storage, insurance, and yield costs of holding a commodity forward in time |
| **Also called** | Carry, carrying charges, cost of financing |
| **Core formula** | Forward price = Spot price + Financing cost + Storage cost − Convenience yield |
| **When it matters** | Arbitrage, [futures-contract](/futures-contract/) pricing, commodity fund rebalancing |
| **Key variables** | Interest rates, warehouse fees, spoilage risk, physical availability |
| **Inverse of** | [Implied lease rate](/implied-lease-rate/) (for metals) |

</aside>

## The complete carry formula

The reason a futures contract does not simply trade at the current spot price is that someone must finance, store, and insure the commodity while waiting for delivery. The **cost of carry** formula captures this perfectly:

**Forward Price = Spot Price + (r × T) + Storage Cost + Insurance Cost − Convenience Yield**

Each term is straightforward. The financing cost is typically the risk-free [interest rate](/interest-rate/) (or repo rate) multiplied by the time to expiration. Storage costs include warehouse fees, often quoted as a percentage of the commodity's value per month or year. Insurance protects against loss or damage. The convenience yield — the practical benefit of holding physical inventory — subtracts from the total, because a firm that owns the commodity now may avoid stockouts or manufacturing delays.

This relationship is not theoretical. Traders exploit deviations from it constantly. If the futures contract trades too far above the calculated carry value, a physical arbitrageur will buy spot, store it, and sell futures, pocketing the gap. If futures trade below full carry, the same trader reverses the trade. The market enforces the formula through these arbitrage acts.

## Why financing cost dominates

In most commodities, financing is the largest component of carry. An oil refiner or grain merchant who buys today and delivers three months hence must borrow—either explicitly or by forgoing interest on deployed capital. At 5% annual rates, a three-month carry cost is roughly 1.25% of spot price. For crude oil, agricultural commodities, and soft commodities, this quickly becomes material.

Consider oil. A trader might need to finance a one-million-barrel purchase at $80 per barrel—$80 million at 5% per annum is roughly $1 million in quarterly interest. If transport and storage add another $0.50 per barrel and convenience yield is negligible, the futures contract will trade roughly $1.5 to $2 per barrel above spot. That gap is entirely the cost of carry.

In times of tight [monetary policy](/monetary-policy/) and high [interest rates](/interest-rate/), carry costs balloon. Conversely, when central banks push rates to zero, the carry market flattens—and sometimes even inverts into [backwardation](/backwardation/), where near contracts trade higher than far ones.

## Storage and location premiums

Storage costs vary wildly by commodity. Crude oil in underground caverns costs a few cents per barrel per month. Grain in silos costs more; seasonal patterns in elevator availability create "storage premiums" that shift the entire [forward curve](/forward-curve/). Precious metals stored in a central bank vault cost fractions of a basis point, while non-standard [gold](/gold/) bars or platinum stored in commercial vaults may cost 20–50 basis points per annum.

The location of the stored commodity also matters. Oil stored in Rotterdam (the world's largest refining hub) has lower convenience yield—it is more useful there—than oil in a remote pipeline terminal. Forward curves reflect these geographic handoffs. [Crude oil](/crude-oil/) futures are cash-settled or deliverable in specific locations, and the carry cost adjusts to match delivery logistics.

For agricultural commodities, storage is often seasonal. Farmers harvest in autumn and sell into storage through spring. The cost of carry is highest during winter (when financing and heating costs peak) and lowest in late summer (when supply is lowest and convenience yield highest because inventory is scarce).

## Convenience yield—the hidden anchor

The convenience yield is not a cost; it is a benefit of holding the spot commodity instead of waiting for futures delivery. A manufacturer that needs raw material *now* values physical inventory differently than a trader with perfect patience. If a commodity is scarce or production disruptions are feared, convenience yield rises—the futures contract trades at a smaller premium to spot (or even inverts into backwardation).

This is why [contango](/contango/) and [backwardation](/backwardation/) patterns vary so much by commodity and market regime. During normal times, oil, metals, and grains trade in mild contango—costs exceed convenience yield. During supply shocks (Saudi Arabia suspends shipments, a mine floods), convenience yield spikes and markets flip to backwardation. The spot contract suddenly trades above all future contracts because the immediate availability of physical inventory is so valuable.

## Arbitrage enforcement and market efficiency

The beauty of cost of carry is that it is self-enforcing. If a trader can borrow at 4%, storage costs are $0.30 per barrel, and convenience yield is $0.10 per barrel, the forward price should trade exactly 4% annual financing plus $0.20 net of convenience yield above spot. If it does not, arbitrage money enters. A [hedge fund](/hedge-fund/) or bank will buy physical, fund it, store it, and sell futures, locking in the spread.

This process is not costless. Financing requires [credit rating](/credit-rating/) and repo access. Storage requires connections to warehouses and insurance brokers. But large institutions can execute carry trades for 10–30 basis points of friction. If the mispricing is wider, it closes fast.

Deviations from the carry formula reveal market stress. In 2020, oil briefly crashed below zero because storage near the [futures-contract](/futures-contract/) delivery point was full, and convenience yield collapsed below costs. Traders faced negative carry and paid to avoid physical delivery. The formula held even in chaos.

## Cost of carry in fund rebalancing

[Commodity ETFs](/etf/) and [mutual funds](/mutual-fund/) that hold futures instead of physical commodity must roll positions as contracts expire. A fund holding front-month oil futures selling at 95 and the next contract at 96 realizes the cost of carry each roll. Over many cycles, a fund's returns diverge from spot returns by exactly the cumulative carry costs. This is why [contango](/contango/) markets systematically hurt [ETF](/etf/) returns: investors in passive commodity baskets slowly bleed money to carry costs.

## See also

<div class="wiki-seealso">

### Closely related

- [Contango](/contango/) — the normal pattern where forward prices exceed spot prices
- [Backwardation](/backwardation/) — the inverted pattern where near contracts trade higher than far ones
- Convenience yield — the benefit of holding physical commodity versus waiting for futures delivery
- [Futures contract](/futures-contract/) — the derivative instrument to which carry costs are locked
- [Implied lease rate](/implied-lease-rate/) — the embedded borrowing cost for precious metals
- [Cost of equity](/cost-of-equity/) — the financing component applied to equity assets

### Wider context

- [Interest rate](/interest-rate/) — the rate that determines financing costs
- [Forward contract](/forward-contract/) — the fundamental instrument for locking in future prices
- Arbitrage — the activity that enforces the carry formula
- Commodity curves — the broader family of forward and futures prices
- [Hedge fund](/hedge-fund/) — the institution that actively exploits carry mispricings

</div>
