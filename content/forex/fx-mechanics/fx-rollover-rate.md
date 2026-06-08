---
title: "FX Rollover Rate"
description: "The overnight interest charge or credit applied when an open FX spot position is held past its standard T+2 settlement date."
keywords:
  - fx rollover
  - swap rate forex
  - overnight financing forex
  - position holding cost
image: /svg/forex.svg
---

*An **FX rollover rate** (also called a swap rate or financing charge) is the interest expense or credit applied to a [spot FX](/spot-exchange-rate/) position when it is kept open beyond its standard settlement date. If you buy a currency and want to hold it for another day, you must either allow it to settle (and pay for the cash you've borrowed) or roll it forward and pay interest on the notional amount at the overnight rate differential between the two currencies.*

<div class="wiki-hatnote">

For the mechanics of FX trading itself, see [spot exchange rate](/spot-exchange-rate/). For immediate settlement, see [same-day settlement in FX](/same-day-settlement-forex/).

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">FX Rollover Rate — key facts</div>

<img src="/svg/forex.svg" alt="A symbolic representation of forex settlement mechanics." />

<div class="wiki-infobox-caption">The cost of carrying an FX position overnight; driven by the interest rate gap between two currencies.</div>

|   |   |
|---|---|
| **What it is** | Daily financing cost or credit when a spot FX position rolls past T+2 settlement |
| **Also called** | Swap rate, carry charge, overnight financing, interest carry |
| **Magnitude** | Typically 0.01–0.1% per day, or basis points on the notional position |
| **Determined by** | Difference in overnight [interest rates](/interest-rate/) between the two currencies |
| **Paid to/by** | Counterparty (your FX dealer); deducted or credited daily |
| **Direction** | Positive if you're long the higher-rate currency; negative if you're short it |

</aside>

## Why rollovers exist: the mechanics of settlement

When you buy EUR/USD at 1.10, you are agreeing to pay 1.1 million dollars and receive 1 euro in 2 business days (the settlement date). At that settlement date, you have to deliver the dollars and take receipt of the euros. If you want to keep the position open—to stay long euros—you must ask your dealer to roll it forward: instead of settling the original deal, you unwind it (sell euros, buy back dollars) at the settlement date, and simultaneously enter a new deal for 2 days further out.

Rolling forward effectively creates a new FX swap: you're selling the currency for near-term value and buying it back for far-term value (or vice versa). The price difference between these legs is the rollover cost. That price difference reflects the interest rate differential between the two currencies.

If the euro earns 4% per year and the dollar earns 2%, the cost to borrow dollars and lend euros for one night is roughly (4% − 2%) ÷ 365 ≈ 0.005% per day. On a position size of 1 million euros, that's roughly €50 per night. Conversely, if you're short euros and long dollars, you *earn* that 50 euros each night, because you're earning the dollar rate and paying the euro rate.

## Positive and negative carry

A trader is said to earn "positive carry" when the [interest rate](/interest-rate/) of the currency they are long exceeds the interest rate of the currency they are short. Buy high-yielding currencies (Turkish lira, Brazilian real, South African rand, Mexican peso) and hold them against low-yielding currencies (USD, EUR, JPY), and you collect interest every night. For years, the USD/JPY pair was a classic "carry trade" because the dollar paid 2–5% while the yen paid near zero.

Negative carry is the reverse. Go long USD/JPY, and you pay interest every night because you're long the low-yielding yen against the dollar. Negative carry eats into your profit if you're wrong on the direction, which is why many FX traders prefer to avoid negative carry unless they have a strong directional view.

Central bank decisions change carry regimes overnight. When the Federal Reserve raised rates from 0% to 5% (2022–2023), USD carry suddenly became valuable again; the US/Japan pair swung from negative to positive carry, and the yen weakened sharply as carry traders rotated into dollar longs.

## How dealers quote rollover rates

Your FX dealer doesn't tell you the rollover as an interest percentage; they embed it into the spot price for the next settlement date. If the spot rate for EUR/USD is 1.1000 and the 3-day (next settlement) rate is 1.0998, the difference of 0.0002 is the rollover cost. Multiply by the notional (1 million euros = 1.1 million dollars), and you get the daily carry in dollar terms.

Dealers often quote rollover rates in basis points per day or as an annualised rate. A dealer might say "EUR/USD is trading 25 basis points positive carry" meaning you earn roughly 0.25% per year, or 0.0007% per day, for being long euros.

This is not a fixed rate. Rollover rates change daily because overnight [interest rates](/interest-rate/) change, and they can swing sharply during central bank meetings or financial stress. On the eve of a major [interest-rate](/interest-rate/) decision, rollover rates can widen (dealers demand a larger spread for uncertainty), sometimes making it expensive to hold a position.

## Retail forex and rollover charges

Retail FX brokers often quote and charge rollover rates differently than institutional dealers. A retail trader rolling a position might see a larger fee because the broker is passing through dealer costs and adding a markup. Some brokers offer "rollover-free" accounts that avoid overnight interest charges by, in effect, refusing to let you carry positions beyond 5 p.m. New York time. Instead of rolling, the position is closed and you can re-enter the next day.

For institutional traders, rollover rates are negotiable and are embedded in the spot quote. For retail traders, they are usually a disclosed fee per unit or per lot.

## Rollover rates and volatility

During periods of financial stress—bank failures, central bank emergency action, [credit events](/credit-risk/)—overnight [interest-rate](/interest-rate/) differentials can spike. In 2020, when the Fed emergency-lowered rates to zero and Swiss banks raised their rates, rollover on USD/CHF swung wildly. A trader holding large positions could face unexpectedly large overnight charges.

This is one reason institutional traders monitor rollover rates as carefully as spot rates. A position that is profitable on the currency move but suffers large daily rollover costs can become uneconomical to hold, especially if the bet takes time to play out.

## Weekend and holiday rollover

Rollover is usually charged only on business days. But because the settlement date for an FX trade is 2 business days forward, a position held on Friday until Monday actually rolls 3 calendar days (Friday, Saturday, Sunday) but only 1 business day (Friday to Monday). Dealers charge 3 days' worth of rollover to account for the weekend. Similarly, positions rolling through holidays (US Thanksgiving, Christmas, bank holidays in other countries) may incur 2 or 3 days' rollover in a single night.

Some dealers offer "mini" rollover on Friday afternoon that charges only 1 day's interest, but this varies by institution.

## The relationship to forward exchange rates

The FX rollover rate is intimately tied to the [forward exchange rate](/forward-contract/). If you buy EUR/USD spot at 1.1000 and want to lock in a price 3 months forward, the dealer quotes you a forward rate that reflects both the spot price and the cumulative rollover cost over those 3 months. Higher euro interest rates push the forward euro price *down* (making it cheaper to buy euros 3 months out) because the daily carry is already built into the price.

This relationship is so fundamental that arbitrage traders constantly check whether the forward rates implied by carry match the actual quoted forwards. If they don't, there's a profit opportunity.

## See also

<div class="wiki-seealso">

### Closely related

- [Spot exchange rate](/spot-exchange-rate/) — the price for delivery in 2 business days; the base for rollover calculations
- [Interest rate](/interest-rate/) — the overnight rate differential that drives the rollover charge
- [Forward contract](/forward-contract/) — locking in a price further out; incorporates cumulative rollover
- [Carry trade](/carry-trade/) — strategy of holding high-yielding currencies against low-yielding ones
- Settlement date — the T+2 date when trades would normally clear

### Wider context

- [Currency risk](/currency-risk/) — underlying exposure being managed
- [Central bank](/central-bank/) — sets interest rates that drive carry differentials
- [Monetary policy](/monetary-policy/) — interest rate decisions that reshape carry regimes
- [Bid-ask spread](/bid-ask-spread/) — dealer margin; can widen during stress
- [Counterparty risk](/counterparty-risk/) — credit risk borne between deal and settlement

</div>
