---
title: "Positive vs Negative Swap Rates on Currency Pairs"
description: "Why holding certain currency pairs overnight earns interest while others charge a fee; driven by the interest-rate differential between the two currencies."
keywords:
  - positive vs negative swap rate forex pair
  - currency swap rates overnight
  - interest rate differential forex
  - rollover interest forex
  - forex carry trade
  - currency pair funding cost
image: /svg/forex.svg
---

*A **positive swap rate** on a currency pair means you earn interest for holding the position overnight; a **negative swap rate** means you pay. The sign depends entirely on the interest-rate differential: if the currency you own pays higher interest than the currency you owe, you get paid. If the opposite is true, you pay.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Swap Rates — key facts</div>

<img src="/svg/forex.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">The cost (or credit) of holding a currency position overnight.</div>

|   |   |
|---|---|
| **Positive swap** | You earn interest by holding the pair |
| **Negative swap** | You pay interest to hold the pair |
| **Determines the sign** | Interest-rate differential between the two currencies |
| **Benchmark rates** | SOFR (USD), SONIA (GBP), EONIA (EUR), local central bank rates |
| **Timing** | Charged or credited at rollover (typically 5 PM US Eastern) |
| **Magnitude** | Typically 0.01%–0.5% annualized per night, varies by pair and broker |
| **Trading impact** | Largest on very-long-term trades; negligible on scalps; critical in carry trade strategies |
| **Direction** | EUR/USD often positive (if ECB rates > Fed rates); USD/JPY often negative (if BoJ rates < Fed rates) |

</aside>

## The mechanism: why one currency costs more than the other

When you open a forex position, you are simultaneously buying one currency and borrowing another. If you buy EUR/USD, you own euros and owe dollars. Overnight, your broker finances both sides of this trade, paying interest on the dollars you borrowed and receiving interest on the euros you own.

The difference between these two interest rates creates a **positive vs negative swap rate**. If the euro's interest rate exceeds the dollar's, you pocket the difference. If the dollar's rate exceeds the euro's, you pay the difference.

This mechanism is pure interest-rate [arbitrage](/interest-rate-swap/). Your broker pays the prevailing overnight rate (today typically [SOFR](/sofr/) for USD, [SONIA](/sofr/) for GBP, or ECB deposit rates for EUR) to borrow the base currency from a bank, and receives the same rate when lending out the quote currency. The spread between the two is passed through to you, sometimes with a small broker markup.

## Positive swap rates: you earn by holding

A **positive swap rate** occurs when the quote currency's interest rate exceeds the base currency's rate.

**Example: EUR/USD when ECB rates > Fed rates**

Suppose the ECB overnight deposit rate is 3.75% and the Fed's [SOFR](/sofr/) is 5.33%. You buy 1 million EUR/USD at 1.0900.

Your position:
- Own 1,090,000 USD (quote currency)
- Owe 1,000,000 EUR (base currency)

Overnight interest calculation:
- You earn on USD: 1,090,000 × (5.33% / 365) = ~$159
- You pay on EUR: 1,000,000 × (3.75% / 365) = ~$103
- Net credit: ~$56

You earn this credit every night you hold the position. Over a year, this would compound to roughly 0.56% of your position value (ignoring slippage and broker spreads). This is the essence of the [carry trade](/carry-trade/): borrow cheap in one currency, lend expensive in another, and pocket the spread.

## Negative swap rates: you pay to hold

A **negative swap rate** occurs when the base currency's interest rate exceeds the quote currency's rate.

**Example: USD/JPY when Fed rates > BoJ rates**

The Fed's SOFR is 5.33% and the Bank of Japan's deposit rate is -0.10%. You buy 1 million USD/JPY at 150.00.

Your position:
- Own 150,000,000 JPY (quote currency)
- Owe 1,000,000 USD (base currency)

Overnight interest calculation:
- You pay on USD: 1,000,000 × (5.33% / 365) = ~$146
- You earn on JPY: 150,000,000 × (-0.10% / 365) = ~-$41 (a cost, not a credit)
- Net debit: ~$187

You lose this amount every single night. Over a year, this is roughly -1.87% drag on the position, a significant headwind to any trade thesis.

## How swap rates change with interest-rate differentials

The **positive vs negative swap rate** flips whenever the interest-rate differential shifts. This happens when central banks change policy.

Consider GBP/USD over the past decade:

- **2010–2021:** The Fed kept rates near zero; the BoE gradually raised rates. GBP/USD was often positive, rewarding carry traders.
- **2022–2023:** The Fed hiked aggressively to 5.33%; the BoE lagged, raising to 5.25%. GBP/USD swaps remained modestly positive.
- **2024+:** If the Fed cuts to 4% but the BoE stays at 5%, GBP/USD swaps would turn negative.

Traders monitoring these differentials can sometimes identify pairs about to flip. A trader holding a negative-swap position might close it just before the central bank raises rates and the swap turns positive. Conversely, buying before a positive swap becomes even more positive is a classic carry trade setup.

## Why swap rates matter across holding periods

**For scalpers and day traders:** Swap rates are irrelevant. You open and close positions within hours, so overnight financing costs never apply. A scalper earning 10 pips on EUR/USD over 5 minutes does not care if the swap is +50 or -50 pips per night.

**For swing traders (days to weeks):** Swap costs accumulate but remain modest. A trader holding USD/JPY for 5 days and paying -$187 per night pays ~$935 total, or roughly 0.1% on a $1 million position. This is material but manageable if the trade moves 50 pips in your favor.

**For position traders and carry traders (weeks to years):** Swap rates are critical. A carry trade holding a positive-swap pair like AUD/JPY (Australia's higher rates, Japan's near-zero rates) for six months earns thousands of dollars purely from overnight financing. Conversely, a position trader forced to hold a negative-swap pair absorbs significant carrying costs.

## The broker's role in swap rates

Your broker sets the swap rate you actually pay. Most brokers use central bank overnight rates as the benchmark but add a small spread (0.1%–0.5% depending on the pair and broker quality). Some brokers also apply different swap rates to long versus short positions: shorting a pair with a positive swap might charge you the positive rate (you pay to be short) or sometimes a higher negative rate.

A few exotic brokers offer "swap-free" accounts, particularly for Islamic trading (where interest is forbidden under Sharia law). These brokers simply bundle the carry cost into the [spread](/bid-ask-spread/) or charge a flat fee. The cost does not disappear; it is just hidden.

## Swap rates and [volatility](/currency-volatility/)

Swap rates are mechanically tied to central bank policy, not to market volatility or fear. A currency pair can be extremely volatile yet still carry a positive swap if the interest-rate differential is wide.

However, during crashes or panic, interest rates themselves can swing sharply, flipping swap rates overnight. During the 2020 COVID crash, many central banks cut rates to near-zero in days, turning previously positive swaps deeply negative.

## Trading strategies around swaps

**The carry trade** is the most famous: buy high-yielding currencies, short low-yielding currencies, earn the spread. This works beautifully in calm markets but blows up during [volatility](/currency-volatility/) spikes when correlations shift.

**Swap optimization:** Traders sometimes choose between similar pairs based on swap rates. If you want exposure to emerging-market equities, you might choose to hold ZAR (South African rand, often positive vs USD) rather than INR (Indian rupee, often negative vs USD) simply to reduce overnight costs.

**Hedge financing:** Some traders use negative-swap pairs as a hedge, intentionally accepting the carry cost because the pair moves in the right direction when they need it. This is explicit hedge financing.

## See also

<div class="wiki-seealso">

### Closely related

- [Interest-Rate Swap](/interest-rate-swap/) — the broader concept of swapping interest-rate streams
- [Carry Trade](/carry-trade/) — the strategy that profits directly from positive swap rates
- [SOFR](/sofr/) — the benchmark rate that determines USD swap costs
- [Basis Risk](/basis-risk/) — the risk that your hedge and position diverge in value
- [Currency Risk](/currency-risk/) — the primary risk in forex positions, separate from carry cost

### Wider context

- [Forex Trading](/stock-market/) — the market where these pairs trade
- [Spread](/bid-ask-spread/) — how brokers profit and where swap costs can hide
- [Central Bank](/central-bank/) — whose policy directly sets the interest-rate differential

</div>
