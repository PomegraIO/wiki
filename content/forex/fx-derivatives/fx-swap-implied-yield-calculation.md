---
title: "FX Swap Implied Yield Calculation"
description: "The forward points in an FX swap encode an implied yield spread, derived from the interest-rate differential between two currencies."
keywords:
  - fx swap implied yield calculation
  - forward premium calculation
  - interest rate parity forex
  - fx swap points
  - swap yield spread
image: /svg/forex.svg
---

*An **FX swap** bundles a spot currency trade with a reverse forward contract, locking in an exchange rate for repayment. The difference between the spot rate and the forward rate—called the forward points—is not arbitrary. It encodes the **implied yield**, which reflects the interest-rate gap between the two currencies. Calculating that implied yield shows how the swap's economics relate to each currency's short-term money-market rates.*

<div class="wiki-hatnote">

This entry covers the mathematics of implied yield in FX swaps and its relationship to interest rates. It assumes familiarity with [forward contracts](/forward-contract/) and [interest rates](/interest-rate/).

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">FX Swap Implied Yield — Key Facts</div>

<img src="/svg/forex.svg" alt="An abstract editorial mark for currency and forex." />

<div class="wiki-infobox-caption">The swap's forward points reveal the interest-rate differential between currencies in annualized form.</div>

|   |   |
|---|---|
| **Forward points** | The difference between forward and spot rates, expressed in pips or basis points |
| **Implied yield formula** | (Forward rate − Spot rate) / Spot rate × (360 / days) × 100 = annual % |
| **Underlying driver** | Interest-rate differential (domestic minus foreign [interest rate](/interest-rate/)) |
| **Time convention** | 360-day year in FX markets (not 365) |
| **Covered interest parity** | The no-arbitrage principle linking spot, forward, and interest rates |
| **Common terms** | Spot (today), forward (1 month, 3 months, 6 months, 1 year) |

</aside>

## Why forward points exist

When two currencies have different [interest rates](/interest-rate/), an investor would have an arbitrage opportunity if both currencies traded at the same exchange rate today and in the future. Suppose the U.S. dollar earns 5% annually and the euro earns 1% annually. An arbitrage trader could borrow euros at 1%, convert to dollars at the spot rate, invest dollars at 5%, and pocket the 4% spread—unless the dollar is expected to weaken in the forward market.

The forward exchange rate adjusts to eliminate that free profit. The dollar strengthens in the forward market (costs more euros to buy), offsetting the interest-rate advantage. This adjustment appears as **forward points**—the number of pips the forward rate differs from the spot rate.

## The covered interest parity formula

The no-arbitrage relationship is **covered interest parity**:

$$\frac{F}{S} = \frac{1 + r_d \times \frac{t}{360}}{1 + r_f \times \frac{t}{360}}$$

Where:
- **F** = Forward rate
- **S** = Spot rate
- **r_d** = Domestic interest rate (annual)
- **r_f** = Foreign interest rate (annual)
- **t** = Days to maturity
- **360** = Days in a year (FX market convention)

Rearranging to isolate the forward premium:

$$\frac{F - S}{S} = \frac{r_d - r_f}{1 + r_f \times \frac{t}{360}} \times \frac{t}{360}$$

For short time periods and small interest-rate differences, this simplifies to:

$$\text{Implied yield (annual)} = \frac{F - S}{S} \times \frac{360}{t} \times 100\%$$

## A worked example

Suppose today (spot date):
- Spot USD/EUR rate: 1.1000 (1 dollar = 1.10 euros)
- 3-month forward rate: 1.0950 (dollars strengthen, cost fewer euros)
- Days to maturity: 90

The forward points are: 1.0950 − 1.1000 = −0.0050 (negative, meaning the dollar is at a forward **premium**—it is worth more in the forward market, so fewer euros are needed to buy a dollar).

The implied yield (from the dollar's perspective relative to the euro) is:

$$\text{Implied yield} = \frac{1.0950 - 1.1000}{1.1000} \times \frac{360}{90} \times 100 = \frac{-0.0050}{1.1000} \times 4 \times 100 = -1.82\%$$

The negative value tells us that the dollar is trading at a **premium** in the forward market, reflecting the fact that the dollar's [interest rate](/interest-rate/) is higher than the euro's. An investor giving up euros now (at a lower rate) and getting paid back in a higher-rate dollar environment expects to lose on the currency conversion to offset the interest advantage.

## Practical interpretation

The annualized implied yield of −1.82% in the example corresponds roughly to the interest-rate spread between dollar and euro short-term rates. If the 3-month dollar [SOFR](/sofr/) is 5.5% and the 3-month euro rate ([EURIBOR](/european-central-bank/)) is 3.7%, the spread is 1.8%—matching the implied yield. (The exact match depends on the simplified vs. precise formula used.)

This relationship allows traders to:

1. **Detect arbitrage:** If the implied yield deviates significantly from the actual interest-rate differential, a [carry trade](/carry-trade/) (borrowing low, investing high, and locking in the forward) becomes attractive.
2. **Price swaps:** Market makers use the covered-interest-parity formula to quote [FX swap](/carry-trade/) rates. A wider bid-ask spread reflects less liquidity or higher [counterparty risk](/counterparty-risk/).
3. **Hedge currency risk:** A firm expecting to receive euros in 90 days can lock in a dollar amount by selling euros forward at the forward rate, knowing the economic cost is the implied yield—not a mystery.

## Spot versus forward interest rates

The [interest rates](/interest-rate/) used in the formula are typically **spot (current) money-market rates** for the tenor in question. A 3-month FX swap uses 3-month [SOFR](/sofr/) (or [LIBOR](/libor/) historically) for dollars and the 3-month euro rate for euros.

In some markets, particularly emerging-market currencies, the interest-rate differential can be much wider (5–10% annually), leading to large forward premiums or discounts. A high-yield currency typically trades at a **forward discount** (weakens into the future), while a low-yield currency trades at a **forward premium** (strengthens into the future).

## The role of [SOFR](/sofr/) and currency basis

Since 2020, U.S. money-market trading has transitioned from [LIBOR](/libor/) to [SOFR](/sofr/). This shift affected FX swap pricing, because the gap between SOFR and other currencies' reference rates (like EURIBOR) is not identical to the old LIBOR gap. The difference is called **currency basis** and is a real cost for cross-currency [swaps](/swap/).

For example, even if the 3-month SOFR is 5.3% and the 3-month EURIBOR is 3.6%, a euro-borrowing bank must pay a basis (often −20 to −50 basis points) on top of EURIBOR to borrow dollars synthetically via FX swaps. This basis widens during periods of dollar scarcity or [stress-testing](/stress-testing/) scenarios.

## Non-linear effects and conventions

For longer tenors (1 year or more) or high [interest rates](/interest-rate/), the simplified linear formula diverges from the precise formula. Always use the full covered-interest-parity formula:

$$\frac{F}{S} = \frac{1 + r_d \times \frac{t}{360}}{1 + r_f \times \frac{t}{360}}$$

Also, FX swap quotes use a **360-day convention** (not 365), which is a longstanding market standard. Some currencies or markets may deviate; always confirm the convention with the [broker](/broker/).

## See also

<div class="wiki-seealso">

### Closely related

- [Forward contract](/forward-contract/) — the core instrument whose pricing the formula explains
- [Interest rate](/interest-rate/) — the primary driver of forward points and implied yield
- [SOFR](/sofr/) — the modern U.S. money-market reference rate replacing LIBOR in FX pricing
- [LIBOR](/libor/) — the legacy rate that governed FX swap pricing for decades
- [Carry trade](/carry-trade/) — the strategy of borrowing in a low-yield currency and investing in high-yield, locked in by FX swaps
- [Counterparty risk](/counterparty-risk/) — the credit risk that a swap counterparty defaults on its obligations
- [Swap](/swap/) — the broader class of interest-rate and currency derivatives

### Wider context

- [Currency risk](/currency-risk/) — the exposure that FX swaps hedge or create
- [Currency volatility](/currency-volatility/) — the price fluctuation in spot markets, separate from the forward basis
- [Spot exchange rate](/spot-exchange-rate/) — the starting point for the forward calculation
- [Futures contract](/futures-contract/) — an alternative mechanism for locking in exchange rates, with different economics
- [Derivative hedging](/derivatives-hedging/) — the broader practice of managing financial risk

</div>
