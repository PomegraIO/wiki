---
title: "FX Rollover and Swap Points Explained"
description: "How swap points in forex rollover are calculated from interest-rate differentials and whether they cost or credit a trader."
keywords:
  - swap points forex rollover
  - what are swap points
  - forex overnight rollover
  - interest rate differential currency
  - fx rollover cost
image: "/svg/forex.svg"
---

*In spot foreign exchange, holding a currency position overnight incurs a **swap point** — a credit or debit determined by the gap between the interest rates of the two currencies in the pair. Swap points are not negotiable fees; they flow mechanically from the interest-rate differential, and they can swing from a cost to income depending on which currency you hold and which direction rates move.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">FX Rollover and Swap Points — Key Facts</div>

<img src="/svg/forex.svg" alt="An abstract editorial mark for forex and currency trading." />

<div class="wiki-infobox-caption">Overnight holding costs or credits in forex stem directly from interest-rate spreads between two economies.</div>

|   |   |
|---|---|
| **What it is** | Fee or credit applied to an open spot FX position held past 5pm ET (or local rollover time) |
| **Basis** | Interest-rate differential between the two currencies |
| **Calculation** | (rate of higher-yielding currency minus lower-yielding currency) × position size ÷ 365 |
| **Who pays** | Trader holding the lower-yielding currency; trader holding the higher-yielding currency receives it |
| **When it applies** | Daily at rollover; weekends and holidays typically charge 3× the standard rate |
| **Can it be avoided** | Partly — by closing positions before rollover or using forwards instead of spot FX |

</aside>

## Why Interest Rates Matter in Overnight Trades

When you buy a currency pair in the spot market, you are implicitly borrowing one currency and lending another. If you buy USD/JPY at 1.10, you are buying US dollars (and paying with Japanese yen). To finance this purchase overnight, you must borrow yen; the counterparty lending you those yen expects compensation based on what the Bank of Japan pays on yen deposits. Similarly, the dollars you now hold are earning the interest rate set by the Federal Reserve.

The swap point is the net interest you owe or receive for this overnight financing. It is not a broker fee—it is the mechanical result of the interest-rate gap between the two economies. The higher the spread between the two rates, the larger the swap point, and the larger the daily cost or credit to your position.

## How Swap Points Are Calculated

The formula is straightforward:

**Swap Points = (Rate of Long Currency - Rate of Short Currency) × Position Size ÷ 365**

Suppose you hold one standard lot (100,000 units) of EUR/USD, which means you are long the euro and short the dollar. The ECB's deposit rate is 4.0% and the Federal Reserve's rate is 5.5%. The daily cost to you is:

(4.0% - 5.5%) × 100,000 ÷ 365 = -$41 per day

You owe $41 each night you hold the position. The negative number means a debit.

If instead you sold EUR/USD (short the euro, long the dollar), you would receive $41 per day. The sign flips because you now benefit from the rate gap.

These rates are not official central-bank overnight rates but the [interest rates](/interest-rate/) that banks charge each other and that brokers use to model the cost of their own financing. Different brokers use slightly different interbank rates, so swap points vary modestly between platforms.

## When Swap Points Reverse—and Cost the Most

On Fridays and before holidays, rollover typically charges three times the standard swap. A position held from Friday 5pm ET to Monday 5pm ET (or from the day before a holiday) carries three business days of swap in a single charge. This reflects the higher cost to the broker of financing your position over a weekend or long weekend.

Additionally, swap points fluctuate as central banks move their [policy rates](/federal-funds-rate/). If the Federal Reserve cuts rates and the ECB holds steady, the swap on EUR/USD reverses: instead of paying to hold euros, you now earn. Traders sometimes enter positions specifically to capture this drift—a low-risk carry trade—though the gains are small unless the rate gap is wide and the position is large.

## Positive vs. Negative Swaps—and the Carry Trade

A **positive swap** occurs when the currency you are long has a higher yield than the currency you are short. A trader holding AUD/JPY (Australian dollar paired with Japanese yen) typically receives a positive swap because the Reserve Bank of Australia's rates are usually well above the Bank of Japan's. Day after day, simply holding the position earns interest—a reason some retail traders favor this pair even if the exchange rate stays flat.

A **negative swap** is the opposite. Holding USD/JPY (buying dollars, shorting yen) from the US side is negative because Japan's rates are so low. You pay every night to hold it. Some high-volume traders accept this cost because they expect the USD to strengthen; the daily swap is a small tax on their directional bet.

This interest-rate differential is the foundation of the [carry trade](/carry-trade/), in which traders borrow in a low-rate currency and lend in a high-rate currency, pocketing the spread. However, the carry trade is not risk-free: if the low-rate currency suddenly appreciates, losses on the exchange rate can dwarf cumulative interest earnings.

## Hedging and Avoiding Swap Costs

Traders who want to hold a directional position but avoid negative swaps can use currency [forwards](/forward-contract/) instead of spot trading. A forward locks in an exchange rate for settlement several days, weeks, or months ahead. The forward rate already incorporates the interest-rate differential, so there is no daily swap charge—but the forward is less liquid and typically wider bid-ask spreads than spot.

Alternatively, traders can hold one-day or multi-day options, which have [theta decay](/time-decay-theta/) but no explicit swap. Or they can close the position before rollover time and re-enter it the next morning, though this incurs bid-ask costs and slippage that often exceed the swap savings.

## Market Conventions and Rollover Times

In most retail forex markets, rollover occurs at 5pm US Eastern Time. In some institutions and markets, particularly in Asia, rollover happens at the local close. Weekends and major holidays (Christmas, New Year) shift the rollover schedule, and some brokers charge double or triple swaps on these dates.

Large banks and professional traders often use [repurchase agreements](/repurchase-agreement/) (repos) instead of spot trading to manage overnight exposures. A repo explicitly buys and sells a currency pair at two different rates and dates, making the financing cost transparent and avoiding the daily swap mechanics that retail traders encounter.

## See also

<div class="wiki-seealso">

### Closely related

- [Carry Trade](/carry-trade/) — How traders profit from interest-rate differentials between currencies
- [Interest Rate](/interest-rate/) — The foundation of swap point calculations
- [Forward Contract](/forward-contract/) — An alternative to spot trading that avoids daily swap charges
- [Federal Funds Rate](/federal-funds-rate/) — US overnight borrowing rate that affects USD swap points
- [Currency Risk](/currency-risk/) — Broader framework for understanding FX exposures over time

### Wider context

- [Forex Broker](/broker/) — How intermediaries charge and execute spot FX trades
- [Spot Rate](/spot-rate/) — The immediate exchange rate for physical settlement
- [Repo Agreement](/repurchase-agreement/) — How banks finance short-term currency positions
- [Interest Rate Risk](/interest-rate-risk/) — Impact of rate moves on broader financial positions

</div>
