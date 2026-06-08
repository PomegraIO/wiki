---
title: "Tick Size, Lot Size, and Pip Value Across Currency Pairs"
description: "Pip value varies across currency pairs and lot sizes. Learn how to calculate monetary pip worth for different quote currencies and position sizes."
keywords:
  - pip value lot size
  - currency pair lot size
  - forex pip calculation
  - micro lot mini lot standard lot
  - tick size currency pairs
  - quote currency pip value
---

*The **pip value**—the dollar (or other home-currency) profit or loss per pip move—is not the same across all currency pairs and lot sizes. A pip in EUR/USD is worth $10 on a standard lot but only $1 on a micro lot; a pip in USD/JPY is worth $10 on a standard lot but denominated differently because the yen is the quote currency, not the base. Understanding how to calculate pip value across different pairs and lot sizes is essential for position sizing, [risk management](/leverage-ratio-forex/), and knowing your true exposure.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Pip value — key facts</div>

<img src="/svg/forex.svg" alt="An abstract editorial mark for forex trading." />

<div class="wiki-infobox-caption">Pip value depends on lot size, base currency, quote currency, and the current exchange rate.</div>

|   |   |
|---|---|
| **Pip definition** | Fourth decimal place for most pairs (0.0001); second decimal for JPY pairs |
| **Standard lot** | 100,000 units of base currency |
| **Mini lot** | 10,000 units of base currency |
| **Micro lot** | 1,000 units of base currency |
| **Pip value (USD quote)** | (Pip × Lot size × Units per pip) ÷ Current rate |
| **Pip value (JPY quote)** | Calculated from second decimal; typically $10 per pip per standard lot |

</aside>

## Pip Definition and Decimal Places

A **pip** (percentage in point) is the smallest standardized price move in a currency pair. For most pairs—EUR/USD, GBP/USD, AUD/USD—a pip is **0.0001** (one ten-thousandth). So EUR/USD moving from 1.0950 to 1.0951 is a 1-pip move.

For pairs where the **Japanese yen is the quote currency** (USD/JPY, EUR/JPY, GBP/JPY), the pip is the **0.01 (second decimal place)**. So USD/JPY moving from 150.50 to 150.51 is a 1-pip move, not 0.0001 pips.

Some brokers also quote a **"pipette"** or **fractional pip** (fifth decimal or third decimal for yen pairs), allowing tighter [spreads](/bid-ask-spread/). But the full pip remains the standard unit for position sizing and risk calculation.

## Lot Sizes and Base Quantities

The forex market uses **standardized lot sizes**:

| Lot type | Units of base currency | Typical broker availability |
|----------|---|---|
| Standard lot | 100,000 | All major brokers |
| Mini lot | 10,000 | All major brokers |
| Micro lot | 1,000 | Most retail brokers; some institutional traders use it rarely |
| Nano lot | 100 | Some brokers; less common |

A "standard lot" of EUR/USD means 100,000 euros. A "mini lot" of GBP/USD means 10,000 British pounds. The lot size determines the absolute exposure in the base currency, and from there, the pip value follows.

## Calculating Pip Value: USD Quote Currencies

For pairs quoted in US dollars (EUR/USD, GBP/USD, AUD/USD, CAD/USD), the pip value formula is straightforward:

**Pip value = (Pip size × Lot size) ÷ Current exchange rate**

**Example 1: EUR/USD at 1.0950, 1 standard lot**

- Pip size: 0.0001
- Lot size: 100,000 euros
- Exchange rate: 1.0950 USD per euro
- Pip value = (0.0001 × 100,000) ÷ 1.0950 = 10 ÷ 1.0950 = **$9.13 per pip**

**Example 2: EUR/USD at 1.0950, 1 mini lot**

- Pip size: 0.0001
- Lot size: 10,000 euros
- Exchange rate: 1.0950 USD per euro
- Pip value = (0.0001 × 10,000) ÷ 1.0950 = 1 ÷ 1.0950 = **$0.91 per pip**

**Example 3: GBP/USD at 1.2800, 1 micro lot**

- Pip size: 0.0001
- Lot size: 1,000 pounds
- Exchange rate: 1.2800 USD per pound
- Pip value = (0.0001 × 1,000) ÷ 1.2800 = 0.1 ÷ 1.2800 = **$0.078 per pip** (roughly 7.8 cents)

Notice that as the lot size decreases (standard → mini → micro), the pip value scales proportionally. A 50-pip move on 1 standard lot EUR/USD (~$456) is equivalent to a 50-pip move on 10 micro lots EUR/USD, distributed across positions.

## Calculating Pip Value: JPY Quote Currencies

For pairs quoted in Japanese yen (USD/JPY, EUR/JPY, GBP/JPY), the pip size is **0.01**, and the calculation is slightly different because the quote currency is yen, not dollars:

**Pip value = (Pip size × Lot size) × Exchange rate factor**

However, a useful **shortcut** is that for yen pairs, a standard lot typically produces a **pip value of $10** (or close to it) regardless of the exact rate, because the math works out that way. This is a quirk of the yen's denomination.

**Example 1: USD/JPY at 150.00, 1 standard lot**

- Pip size: 0.01
- Lot size: 100,000 USD
- Quoted in yen, so: Pip value = (0.01 × 100,000) ÷ 100 = **$10 per pip** (approximately)

More precisely:
- 1 pip move = 0.01 yen per dollar = 1 yen per 100 dollars
- 100,000 dollars × 1 yen per 100 dollars = 1,000 yen profit per pip
- At 150 yen per dollar, 1,000 yen = 1,000 ÷ 150 = $6.67 per pip

But the convention is to quote yen pip values in the local currency (yen), then convert later. So traders often say "a standard lot of USD/JPY is worth 1,000 yen per pip," and then convert at the current rate if needed.

**Example 2: EUR/JPY at 130.00, 1 mini lot**

- Base: EUR, denominated 10,000
- Quote: JPY (0.01 pip size)
- Pip value = 10,000 × 0.01 = **100 yen per pip** = roughly $0.77 per pip (at 130 yen/euro)

## Impact of Lot Size on Risk and Reward

The relation between lot size and pip value is **linear**. Doubling the lot size doubles your pip value—and doubles your risk per pip.

**Example: Risk calculation for a 50-pip stop-loss**

- 1 standard lot EUR/USD at $9 per pip: 50 pips × $9 = **$450 loss**
- 1 mini lot EUR/USD at $0.90 per pip: 50 pips × $0.90 = **$45 loss**
- 1 micro lot EUR/USD at $0.09 per pip: 50 pips × $0.09 = **$4.50 loss**

This is why position sizing is critical. A trader with a $5,000 account can afford many micro lots but only a few mini lots and no standard lots if they want to keep [risk to 2% per trade](/position-sizing/).

## Cross Pairs and Less Common Quotes

When a pair is **quoted in a currency other than USD** (e.g., EUR/GBP, where the quote is pounds, not dollars), the pip value depends on the current rate and your home currency. The conversion adds a step:

**Pip value (in home currency) = [Pip value in quote currency] × [Spot rate of quote currency to home currency]**

**Example: EUR/GBP at 0.8500, 1 standard lot, trader's home currency is USD**

- Pip size: 0.0001
- Lot size: 100,000 EUR
- Pip value in GBP = (0.0001 × 100,000) ÷ 0.8500 = 11.76 GBP per pip
- Current GBP/USD rate: 1.2700
- Pip value in USD = 11.76 GBP × 1.2700 = **$14.93 per pip**

Most brokers **automatically calculate and display pip value** in your home currency, so you do not need to do this manually. But understanding the math helps you size positions correctly across diverse pairs.

## Practical Position-Sizing Examples

**Scenario 1: Trader with $10,000, 1% risk per trade, 50-pip stop**

- 1% risk = $100
- EUR/USD at 1.0950: $9.13 per pip
- Pips available for loss: $100 ÷ $9.13 = 10.96 pips—need to widen stop to match intention
- OR: Reduce position to 1 mini lot: $0.91 per pip, 50-pip stop = $45.50 loss = 0.45% risk ✓

**Scenario 2: Trader with $50,000, 2% risk per trade, 100-pip stop on GBP/JPY**

- 2% risk = $1,000
- GBP/JPY at ~190.00: 1,000 yen per pip per standard lot ≈ $5.26 per pip
- For 100-pip stop: $1,000 ÷ $526 = 1.9 standard lots available
- Trade 1–2 standard lots depending on comfort ✓

## Microlot Scalping and Tight Stops

Retail traders using microlots and tight 10–20 pip stops can trade with very small dollar risk:

- 1 micro lot EUR/USD ($0.09 per pip) with 20-pip stop = $1.80 loss if stopped out
- A trader can execute 50 such trades a day and keep total daily risk below $100

This makes microlots attractive for scalping and learning, where position size flexibility matters more than absolute pip count.

## Broker Variations and Custom Lot Sizes

Some brokers allow **custom lot sizes** (e.g., 25,000 units or 500 units), and some offer fractional lots. This flexibility is useful:

- A trader might want exactly $10 per pip risk and can select a position size that delivers it, rather than being forced into standard/mini/micro buckets.
- API traders building algorithmic systems often use custom sizing to match their exact risk models.

Always check your broker's lot-size rules and pip-value calculations, as small differences compound over large portfolios.

## See also

<div class="wiki-seealso">

### Closely related

- [Leverage and Margin in Forex](/leverage-ratio-forex/) — How lot size and leverage interact for margin requirements
- [Bid-Ask Spread](/bid-ask-spread/) — How spread cost varies with lot size and liquidity
- [EUR/JPY: The Euro–Yen Cross Rate](/eur-jpy-euro-yen-cross/) — Example pair with yen quote currency
- [GBP/JPY: Sterling–Yen Volatility Characteristics](/gbp-jpy-sterling-yen-volatility/) — Another yen-quoted pair for pip value context
- [Position Sizing and Risk Management](/leverage-ratio-forex/) — Matching lot size to account and stop-loss
- [Weekend Gap Risk in Currency Pairs](/currency-pair-gap-risk-weekend/) — Why position sizing matters for overnight risk

### Wider context

- [Forex Market Structure](/stock-exchange/) — How FX quotes and conventions are standardized
- [Options and Optionality](/option/) — Alternative risk/reward profiles to lot-based sizing
- [Currency Volatility](/currency-volatility/) — Relating lot size to expected moves
- [Performance Metrics and Sharpe Ratio](/sharpe-ratio/) — Measuring returns relative to position-size and risk

</div>
