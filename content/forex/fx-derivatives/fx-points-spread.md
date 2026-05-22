---
title: "FX Points Spread"
description: "Forward forex pricing using basis points for precision; difference between spot and forward rate."
keywords:
  - fx points
  - forward premium
  - currency forwards
  - forex pricing
  - basis points
---

*An **FX points spread** (or **forward points**) expresses the difference between a spot [currency](/wiki/currency-pair/) rate and a [forward exchange rate](/wiki/forward-exchange-rate/) in basis points (0.0001 of the quoted pair). Instead of quoting forwards directly, traders say "Buy EUR/USD spot at 1.0800, forward 1-month at +100 points," meaning the forward is 0.0100 pips higher.*

<aside class="wiki-infobox">

| Concept | Example |
|---|---|
| **Spot rate** | EUR/USD = 1.0800 |
| **Forward points (+100)** | 1-month forward = 1.0800 + 0.0100 = 1.0900 |
| **Basis points** | 100 points = 1 pip = 0.0001 in EUR/USD |
| **Positive points** | Forward premium (forward > spot) |
| **Negative points** | Forward discount (forward < spot) |
| **Time value** | Points reflect interest-rate differential and [basis risk](/wiki/basis-risk/) |
| **Use case** | Hedging imports/exports; [currency swaps](/wiki/cross-currency-swap/) |
| **Quotation** | Prices like "1.0800/06 + 100/110" (spot bid/ask, point spread) |

</aside>

## The forward premium/discount mechanism

Forward exchange rates are not arbitrary; they're derived from spot rates and interest-rate differentials. If the US interest rate is 5% and the eurozone rate is 2%, investors would demand to sell EUR and buy USD at spot, driving USD up. To prevent immediate arbitrage, the forward rate must offer a compensating change.

**Interest Rate Parity:**
Forward Rate = Spot Rate × (1 + r_domestic) / (1 + r_foreign)

If r_USD = 5% and r_EUR = 2%:
Forward = 1.0800 × (1.05 / 1.02) ≈ 1.0924

This forward is **92.4 points higher** (the USD is at a premium because US rates are higher, compensating for the interest-rate advantage of holding USD).

## Why use points instead of direct quotes?

Forex markets quote forwards in points rather than absolute rates because:

1. **Precision and liquidity** — basis points are the standard [tick size](/wiki/tick-size-regime/) for forwards. A dealer can quickly quote "+100 to +110 points" without specifying the full forward rate.

2. **Intuitive bid-ask spread** — showing "spot at 1.0800, forward +100/110" tells you the dealer's spread in points (10 pips), making comparison easy across maturities.

3. **Curve visibility** — by quoting points for different tenors (1-month, 3-month, 1-year), traders immediately see the shape of the forward curve. Steeply rising points signal a strong interest-rate premium; flat points signal rates are in equilibrium.

4. **Simplicity** — quoting the full forward rate (1.0900) is redundant; the points (+100) contain all the information, given a known spot.

## Types of forward curves

**Upward-sloping curve (premium):**
- 1-month: +50 points
- 3-month: +130 points
- 1-year: +450 points

Interpretation: The dollar is at a forward premium because US rates are higher than foreign rates. The larger the time horizon, the larger the premium (interest compounds).

**Downward-sloping curve (discount):**
- 1-month: −30 points
- 3-month: −85 points
- 1-year: −200 points

Interpretation: A foreign currency is at a premium (the domestic currency is at a discount) because foreign rates are higher.

**Flat curve:**
- All tenors: near zero points

Interpretation: Interest rates are similar, and there's no significant forward premium or discount.

## Practical use in hedging

A US importer owes EUR 1 million in 3 months. Current spot: 1.0800 EUR/USD.

**Option 1: Unhedged** — wait 3 months, convert at whatever spot rate exists then (risky if EUR rallies).

**Option 2: Forward contract** — lock in a 3-month forward at 1.0800 + 130 points = 1.0930.
- Cost: EUR 1M × 1.0930 = USD 1,093,000 (deterministic).
- If spot in 3 months is 1.1000, the importer is glad they locked in the lower forward (saved 7,000).
- If spot in 3 months is 1.0800, the importer paid a bit more (forward was expensive), but they had certainty.

The points (+130) represent the cost of the forward hedge: the importer pays a higher rate upfront to lock in the exchange risk.

## Basis and swap points

In [currency swaps](/wiki/cross-currency-swap/), the swap points determine how much an investor effectively pays or receives to exchange one currency for another and back.

**Example: 1-year USD/EUR swap**
- Investor buys USD 1M cash at 1.0800 (sells EUR 1.08M)
- Simultaneously sells USD 1M forward at 1.0800 + 450 points = 1.0850 (buys EUR back later)
- Net: locks in a 450-point gain, representing the USD interest-rate advantage

The 450 swap points embed:
- Interest-rate differential (most of it)
- [Basis risk](/wiki/basis-risk/) (credit risk, funding costs)
- [Bid-ask spread](/wiki/bid-ask-spread/) (dealer margin)

## Factors affecting forward points

1. **Interest-rate differentials** — the primary driver. If the US Fed raises rates faster than the ECB, EUR/USD forward points steepen (USD premium increases).

2. **Central bank policy expectations** — forward guidance from [central banks](/wiki/central-bank/) affects expectations of future short rates, shifting the forward curve.

3. **Credit spreads and risk premium** — during crises (emerging-market currency attacks), forward points widen because investors demand extra compensation for [counterparty risk](/wiki/counterparty-credit-risk/).

4. **[Volatility](/wiki/implied-volatility/)** — options pricing on currency forwards increases [bid-ask spread](/wiki/bid-ask-spread/), which ripples to spot-forward spreads.

5. **Carry trade** — demand for forward contracts from carry traders (borrowing low-rate currencies to invest in high-rate ones) can shift points.

## Relationship to basis

The "basis" (cost of carry) in currency forwards includes:
- Interest-rate differential (the lion's share)
- Transaction costs (bid-ask spread, commissions)
- [Repo](/wiki/repurchase-agreement/) rate (cost of funding the spot position)
- Counterparty risk premium

For highly liquid pairs (EUR/USD, GBP/USD), interest-rate differential drives ~90% of forward points. For less liquid or emerging-market pairs, basis risk drives a larger share.

## Trading forward points

Traders play the forward curve:

**Curve steepening** — if interest-rate differentials are expected to widen, buy the near-term forward (lower points) and sell the far-term forward (higher points). As the curve steepens, the spread widens and the trader profits.

**Curve flattening** — if differentials narrow (e.g., both central banks cut rates equally), the curve flattens. Sell near-term, buy far-term.

**Volatility plays** — if [volatility](/wiki/implied-volatility/) is expected to spike, forward points may widen (as bid-ask spreads on swaps widen). Short the forward points (sell forwards) to profit from the spread widening.

## Quotation conventions and pitfalls

**Standard format:** "Spot 1.0800/06, 1M +100/110, 3M +130/145"
- Bid/ask spread on spot: 6 pips
- Bid/ask spread on 1-month points: 10 pips (dealer pays +100, receives +110)
- 1-month forward bid/ask: 1.0900/1.0910

**Pitfall: Negative points**
If points are negative (forward discount), the bid/ask can be quoted as "−20/−10" (dealer buys at −20, sells at −10). Traders must be careful not to confuse the sign and direction.

**Pitfall: Different quote bases**
Some dealers quote forward rates directly (1.0930) instead of points. Always clarify whether the quote is absolute or points-based.

<div class="wiki-seealso">

### Closely related
- [Forward exchange rate](/wiki/forward-exchange-rate/) — the absolute forward rate
- [Basis and bond trades](/wiki/basis-and-bond-trades/) — similar concept in fixed income
- [Carry trade](/wiki/carry-trade/) — strategy exploiting interest-rate differentials
- [Currency swap](/wiki/cross-currency-swap/) — uses forward points
- [Interest rate parity](/wiki/interest-rate-parity/) — theory behind forward points

### Wider context
- [Currency pair](/wiki/currency-pair/) — what forwards are quoted on
- [Forex leverage](/wiki/forex-leverage/) — how traders amplify forward moves
- [Currency hedging](/wiki/currency-hedging/) — primary use of forwards
- [Bid-ask spread (forex)](/wiki/bid-ask-spread-forex/) — spread mechanics in FX
- [Repo](/wiki/repurchase-agreement/) — funding tool affecting basis in forwards

</div>
