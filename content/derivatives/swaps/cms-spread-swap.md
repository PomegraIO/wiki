---
title: "CMS Spread Swap"
description: "A swap exchanging the difference between two constant-maturity swap rates for a fixed or floating payment, used to trade the relative value of different swap tenors."
keywords:
  - cms spread swap
  - constant maturity swap spread
  - basis swap variant
  - swap curve positioning
  - tenor spread
  - derivative strategy
image: "/svg/derivatives.svg"
---

*A **CMS spread swap** is a [derivative](/option/) contract in which one party exchanges the spread (difference) between two [constant-maturity swap (CMS)](/interest-rate/) rates of different tenors for a fixed or floating payment. Traders use CMS spread swaps to take directional views on the shape of the [yield curve](/yield-curve/) and the relative [volatility](/historical-volatility/) of different [swap](/interest-rate/) maturities.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">CMS Spread Swap — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for financial derivatives." />

<div class="wiki-infobox-caption">A synthetic exposure to the spread between two different-maturity [swap rates](/interest-rate/).</div>

|   |   |
|---|---|
| **What it is** | A [swap](/interest-rate/) contract exchanging a spread between two CMS rates for a fixed or floating leg |
| **Also called** | CMS spread; constant-maturity spread swap; tenor spread swap |
| **Underlying spreads** | Typically 10y−2y, 30y−10y, or 10y−5y CMS spreads |
| **Counterparties** | Investors, banks, and speculators trading [yield curve](/yield-curve/) positioning |
| **Settlement** | Periodic [reset](/interest-rate/) to market CMS rates; net payment to counterparty |
| **Key risk** | [Spread risk](/bid-ask-spread/); CMS rate [volatility](/historical-volatility/); basis mismatch |

</aside>

## How a CMS spread swap works

A [constant-maturity swap (CMS)](/interest-rate/) rate is a synthetic rate derived from the [swap market](/stock-exchange/), representing the [fixed rate](/interest-rate/) on a [swap](/interest-rate/) of a specified maturity (e.g., 10-year, 30-year). It is reset periodically (often quarterly or semi-annually) based on observed swap prices in the market.

A CMS spread swap pays or receives the difference between two such CMS rates. A common example is a 10-year minus 2-year CMS spread swap:

- Party A pays the difference (10y CMS − 2y CMS) times notional
- Party B pays a fixed rate (or floating reference) times the same notional
- Settlement occurs each reset period

If the 10-year CMS is 4.50% and the 2-year CMS is 3.00%, Party A pays 1.50% (or 150 basis points) on the notional. If rates invert or compress, Party A's payment shrinks.

The two CMS rates are observed at the same reset date, eliminating the timing basis between them. However, the spread between tenors changes with [yield curve](/yield-curve/) shape, [volatility](/historical-volatility/), and relative supply/demand across maturities.

## Why traders use CMS spread swaps

**[Yield curve](/yield-curve/) positioning**: A trader expecting the [curve](/yield-curve/) to steepen (longer maturities rising faster than shorter ones) may receive the 10-minus-2 spread, profiting if it widens. A trader expecting flattening may pay the spread.

**Speculative positioning**: CMS spread swaps allow synthetic exposure to [curve](/yield-curve/) trades without owning or shorting actual bonds or swaps. They are leveraged, enabling larger notional positions with less capital.

**Relative-value trading**: Banks and hedge funds trade CMS spreads against other indicators of curve shape (e.g., bond [yield curve](/yield-curve/) spreads) to exploit mispricings.

**Hedging**: Asset managers with long duration (e.g., pension funds with long-dated [liabilities](/accounts-payable/)) may sell the long-minus-short CMS spread to hedge against steepening [curves](/yield-curve/), which would reduce the relative value of their long-duration assets.

**[Volatility](/historical-volatility/) expression**: The payoff of a CMS spread swap is sensitive not only to the level of the spread but to the [correlation](/concentration-risk/) between the two rates. High [correlation](/concentration-risk/) means spreads are stable; low [correlation](/concentration-risk/) means spreads are volatile.

## Mechanics and pricing

A CMS spread swap can be structured as:

1. **Receiver**: Receives the CMS spread, pays fixed
   - Profits if the longer CMS outpaces the shorter CMS
   
2. **Payer**: Pays the CMS spread, receives fixed
   - Profits if the spread contracts or reverses

3. **Floating vs. floating**: One leg is CMS spread; the other is a different floating reference (e.g., [SOFR](/sofr/)) at a fixed spread

Pricing depends on:

- **Swap curve shape**: The steeper the curve, the wider the spread between long and short CMS rates
- **[Volatility](/historical-volatility/)**: Higher [volatility](/historical-volatility/) in [interest rates](/interest-rate/) increases spread variability and the option value embedded in the payoff
- **[Correlation](/concentration-risk/)**: Positive [correlation](/concentration-risk/) between the two rates tightens spreads; negative [correlation](/concentration-risk/) widens them
- **Time to [maturity](/expiration-date/)**: Longer-dated CMS spreads have more [convexity](/bond/) and uncertainty

Dealers use Monte Carlo simulation and [yield curve](/yield-curve/) models (such as Heath–Jarrow–Morton or Libor Market Model) to price CMS spreads, accounting for the [volatility](/historical-volatility/) smile and path-dependent behaviour of [interest rates](/interest-rate/).

## Comparison with related structures

A CMS spread swap is distinct from a plain-vanilla [basis swap](/interest-rate/), which exchanges two different floating rates (e.g., [SOFR](/sofr/) vs. SONIA). A CMS spread swap uses CMS rates (derived from fixed swap coupons) rather than liquid floating indices.

It differs from a [callable](/callable-swap/), [puttable](/puttable-swap/), or [extendable swap](/extendable-swap/) in that it does not embed a [swaption](/option/) but instead creates synthetic exposure to [curve](/yield-curve/) positioning via spread payoffs.

A CMS spread swap can also be viewed as a synthetic package of fixed/floating swaps combined to isolate the slope of the [yield curve](/yield-curve/).

## Risks and considerations

**[Spread risk](/bid-ask-spread/)**: The spread between two CMS rates can widen or compress unexpectedly due to [curve](/yield-curve/) reshaping, [volatility](/historical-volatility/) shocks, or changes in relative supply/demand across tenors. A receiver of the spread faces mark-to-market losses if spreads compress.

**[Volatility](/historical-volatility/) risk**: Higher [interest rate](/interest-rate/) [volatility](/historical-volatility/) increases the [convexity](/bond/) of CMS rates and can skew payoffs, especially for longer-maturity spreads. Realized [volatility](/historical-volatility/) may differ from implied [volatility](/historical-volatility/) at entry.

**[Curve](/yield-curve/) inversion risk**: If the [curve](/yield-curve/) inverts (short rates exceed long rates), a receiver of the long-minus-short spread faces losses. In severe inversions, the spread can turn sharply negative.

**[Counterparty risk](/counterparty-risk/)**: CMS spreads are [interest rate](/interest-rate/) [derivatives](/option/), so [credit exposure](/credit-risk/) builds as [rates](/interest-rate/) move and the contract becomes in-the-money. The counterparty must remain solvent for the full [maturity](/expiration-date/) of the trade.

**Basis and [correlation](/concentration-risk/) risk**: If the two CMS rates' [correlation](/concentration-risk/) changes unexpectedly (e.g., due to shocks in different sectors of the [yield curve](/yield-curve/)), the spread behaviour becomes unpredictable. The trader may find the spread moving against expectations despite correct [curve](/yield-curve/) positioning.

**Model risk**: Pricing relies on [volatility](/historical-volatility/) surfaces, [correlation](/concentration-risk/) matrices, and [yield curve](/yield-curve/) models. Errors in model calibration lead to mispricings and losses.

## See also

<div class="wiki-seealso">

### Closely related

- [Interest Rate Swap](/interest-rate/) — the underlying vanilla [swap](/interest-rate/) structure
- [Callable Swap](/callable-swap/) — [swap](/interest-rate/) with embedded early exit right
- [Puttable Swap](/puttable-swap/) — [swap](/interest-rate/) with embedded exit right for the floating payer
- [Extendable Swap](/extendable-swap/) — [swap](/interest-rate/) with right to extend maturity
- [Swaption](/option/) — explicit option on a [swap](/interest-rate/)
- [Basis Swap](/interest-rate/) — exchange between two floating rate indices

### Wider context

- [Swap](/interest-rate/) — general derivative exchanging cash flows
- [Yield Curve](/yield-curve/) — relationship between [interest rate](/interest-rate/) and maturity
- [Interest Rate](/interest-rate/) — the underlying market variable
- [Derivatives](/option/) — financial contracts deriving value from underlyings
- [Volatility](/historical-volatility/) — measure of price and rate uncertainty
- [Counterparty Risk](/counterparty-risk/) — risk that the counterparty defaults or fails to settle

</div>
