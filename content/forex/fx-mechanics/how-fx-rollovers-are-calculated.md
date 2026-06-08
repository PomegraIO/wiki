---
title: "How FX Rollovers Are Calculated on Open Positions"
description: "The arithmetic behind FX overnight rollover charges and credits, tied to interest-rate differentials and swap points between currency pairs."
keywords:
  - fx rollover calculation
  - currency swap points
  - interest rate differential
  - forex overnight fees
  - swap rollover
image: /svg/forex.svg
---

*The **FX rollover** is the overnight financing charge (or credit) applied to a foreign exchange position held past the settlement date. It flows directly from the interest-rate differential between the two currencies in a pair and is quoted in swap points that traders convert to a daily P&L impact.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">FX Rollover Calculation — key facts</div>

<img src="/svg/forex.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Overnight financing cost mirrors the interest gap between two currencies.</div>

|   |   |
|---|---|
| **Basis** | Interest-rate differential between the two currencies |
| **Unit** | Swap points (basis points in the fourth decimal place) |
| **Direction** | Positive (credit) when long the high-yielding currency |
| **Frequency** | Applied daily at market close; sometimes tripled on Fridays |
| **Settlement** | T+2 for spot forex (so rollover starts on the third day) |
| **Broker spread** | Broker marks up the true swap by 1–3 pips |

</aside>

## Why Rollovers Exist: Interest Parity

When you hold an open foreign exchange position overnight, you are in essence borrowing one currency and lending another. If you buy EUR/USD, you simultaneously borrow US dollars and lend euros. Since the [interest rates](/interest-rate/) on those two currencies are almost never equal, one side of the trade accrues interest and the other side incurs a cost.

A FX rollover compensates (or charges) for that interest differential. It is the daily funding cost of maintaining the position. The calculation rests on the [covered interest rate parity](/interest-rate/) principle: the forward exchange rate should reflect the spot rate plus the interest-rate difference. When positions roll over, the broker passes through this interest cost or benefit.

## The Core Formula

The rollover charge (or credit) per unit is straightforward in concept:

**Rollover (pips) = (Interest rate differential / 365) × Position size in base units**

In practice, it is quoted in **swap points**—basis points in the fourth decimal place (0.0001). A position rolling overnight at +5 swap points means you earn 5 pips per 100,000 units of the base currency.

**Worked example:**  
- Currency pair: EUR/USD  
- Spot price: 1.0800  
- EUR annual interest rate: 4.0%  
- USD annual interest rate: 5.5%  
- Interest-rate differential: –1.5% (unfavorable for the EUR buyer)  

The trader who buys EUR/USD borrows USD at 5.5% and lends EUR at 4.0%, netting a –1.5% annual cost. Over one day:

Rollover = –1.5% ÷ 365 = –0.00411% per day  

Per 100,000 EUR (one standard lot):  
Rollover cost = 100,000 × 1.0800 × (–0.00411%) ≈ –$4.44 USD per night

Brokers quote this as swap points. A –41 swap point position reflects the same cost (41 pips at the fourth decimal place).

## Swap Points and the Bid-Ask Spread

Brokers do not pass through the pure interest-rate differential. They widen the spread. A typical retail forex broker might quote:

- **Buy (long) EUR/USD:** +3 swap points  
- **Sell (short) EUR/USD:** –8 swap points  

The difference (11 points spread) is the broker's profit on funding. The true midpoint swap might be –2.5 points, but the broker quotes +3 for longs and –8 for shorts, pocketing 5–6 points per lot per night.

## Friday and Holiday Adjustments

Most brokers triple the rollover charge on Friday (or the last business day before a weekend or holiday) because the position will sit over two days (Saturday and Sunday, when no trading occurs, but interest still accrues). This is sometimes called a **weekend rollover** or **3-day rollover**.

Example: If a standard rollover is –5 points, a Friday rollover might be –15 points to account for the two-day gap. This avoids the arbitrage opportunity of holding a position through Friday at the same daily rate.

## Calculation by Broker: Points to Pips to Currency

Different brokers automate this differently, but the chain is always:

1. **Calculate the interest-rate differential** (e.g., –1.5% annually)  
2. **Annualize the overnight rate** (–1.5% ÷ 365 = –0.0041% per day)  
3. **Convert to swap points** (depends on the currency pair and the exchange rate)  
4. **Add the broker spread** (typically 2–5 pips wide)  
5. **Quote to the trader** (±N points per lot per night)  
6. **Convert to account currency** (multiply by the position size and the exchange rate to settle in the trader's base currency)

For a 1 lot (100,000 units) of EUR/USD at 1.0800, a swap point translates to approximately **1 USD** per lot per night. This makes the math transparent: if the swap is –5 points, the cost is roughly –$5 per lot per night.

## Why Rollovers Matter: Carry Trade Signals

The rollover cost (or benefit) is a standing source of P&L in long-term forex trades. Traders exploit **positive rollover** (a credit) by holding high-yielding currency pairs overnight. The classic [carry trade](/carry-trade/) buys a high-interest-rate currency (e.g., the Australian dollar or Brazilian real) financed by shorting a low-rate currency (e.g., the Japanese yen or US dollar), collecting the daily interest differential.

Conversely, traders avoid or short pairs with large negative rollover. If EUR/USD rollover is consistently –5 to –10 points per night, a long position hemorrhages money just from overnight funding. Over a year, that adds up: –7 points × 250 trading days × 100,000 units × ~$1 per point ≈ –$17,500 per standard lot.

## Central Bank Interest Rate Moves and Rollover Shifts

Rollovers shift whenever central banks change interest rates. If the Federal Reserve raises rates and the ECB keeps steady, the EUR/USD rollover swings in the USD's favor (more negative for EUR buyers). Savvy traders monitor Fed and ECB schedules, because large rate divergences can make or break the profitability of a carry position.

During financial crises or periods of rate cuts, rollovers can flip dramatically. In 2020, when the Fed cut rates to near zero, long USD positions stopped earning carry; short USD positions (longs in other currencies) became more attractive on rollover alone.

## See also

<div class="wiki-seealso">

### Closely related

- [Carry Trade](/carry-trade/) — strategy that profits from positive rollover
- [Interest Rate](/interest-rate/) — the fundamental driver of forex rollover
- [Spot Exchange Rate](/spot-exchange-rate/) — baseline for rollover calculations
- [Currency Risk](/currency-risk/) — risks in holding forex positions overnight
- [Forward Contract](/forward-contract/) — alternative mechanism for avoiding rollover

### Wider context

- [Central Bank](/central-bank/) — sets the interest rates that determine rollover differentials
- Forex — the market in which rollovers apply
- [Leverage Ratio (Forex)](/leverage-ratio-forex/) — how rollover costs scale with position size
- [Counterparty Risk](/counterparty-risk/) — broker operational risk in funding forex positions

</div>
