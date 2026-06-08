---
title: "Pip Value When Your Account Currency Differs From the Pair"
description: "How to calculate the monetary value of a pip when your account is in a different currency than the trading pair."
keywords:
  - pip value calculation different account currency
  - forex pip value conversion
  - account base currency pip
  - trading currency pairs
  - forex position sizing
image: /svg/forex.svg
---

*A [pip](/pip/) represents the smallest price movement in a forex pair, but its monetary value depends on which currency your account is denominated in. If you trade EUR/USD with a JPY account, you must convert the pip value to yen—a straightforward calculation that many traders misunderstand or skip, leading to position sizing errors.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Pip Value Across Currencies — key facts</div>

<img src="/svg/forex.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Position size depends on knowing your pip value in your home currency.</div>

|   |   |
|---|---|
| **Standard pip size** | 0.0001 for most pairs; 0.01 for JPY pairs |
| **Base formula** | (Pip size × Contract size) ÷ Current exchange rate |
| **Contracts sizes** | Typically 100,000 units (1 standard lot) |
| **When conversion matters** | Account currency ≠ pair quote currency |
| **Common mistake** | Using pip value in quote currency instead of home currency |
| **Impact on risk** | Underestimating position risk if conversion ignored |

</aside>

## The Standard Case: GBP/USD with USD Account

When your [account](/accounts-receivable/) is funded in the quote currency of the pair, pip calculation is simple. Trade GBP/USD with a USD account: each 0.0001 move in the pound's value against the dollar represents a fixed dollar profit or loss per contract. A standard lot (100,000 units) moves USD 10 per pip. This is straightforward because the account and quote currency are the same.

But most forex traders do not have accounts in every currency they trade. A UK trader with a GBP account trading EUR/USD must convert the pip value into pounds. A Japanese trader with a JPY account trading any major pair must convert to yen. Failure to do this creates hidden leverage: a trader might position as if the pip is worth USD 10, but their actual home-currency exposure is much larger or smaller depending on the [exchange rate](/spot-exchange-rate/).

## Converting Pip Value to Your Home Currency

The formula is straightforward. Calculate the pip value in the pair's quote currency, then multiply by the current exchange rate between the quote currency and your account currency.

**Example 1: EUR/USD with GBP Account**

You trade EUR/USD on a standard 100,000-unit lot. The pair is at 1.0950.

- Pip value in USD (quote currency): (0.0001 × 100,000) ÷ 1.0950 = 9.13 USD per pip
- EUR/GBP exchange rate: suppose 0.8450 GBP per 1 USD
- Pip value in GBP: 9.13 USD × 0.8450 = 7.72 GBP per pip

So each 0.0001 move costs or gains you approximately 7.72 GBP. If you place a [stop-loss](/support-and-resistance/) 50 pips away, your max loss is 50 × 7.72 = 386 GBP. Sizing your position depends entirely on this home-currency calculation.

**Example 2: USD/JPY with GBP Account**

USD/JPY trades at 150.50. You hold a GBP account.

- Pip value in JPY: (0.01 × 100,000) ÷ 150.50 = 6.64 JPY per pip (note: JPY pairs use 0.01 as the pip)
- GBP/JPY exchange rate: suppose 190.00 JPY per 1 GBP
- Pip value in GBP: 6.64 JPY ÷ 190.00 = 0.035 GBP per pip

This pair is far less valuable per pip when measured in pounds. You would need to take much larger positions to achieve the same pound-sterling risk as an EUR/USD trade.

## Why the Conversion Matters

Failure to convert pip value creates systematic mispricing of risk. Many traders calculate position size using an imaginary pip value, resulting in positions that are either under-leveraged or dangerously over-leveraged.

Consider a trader with a JPY account who assumes every major pair has a pip value of 10 USD. This is true for some pairs in USD accounts, but in JPY it is wildly wrong. The trader might intend to risk only 1% of the account per trade, but if their pip calculation is off by a factor of two, they are actually risking 2% per trade without realizing it. Over dozens of trades, this compounds into catastrophic drawdown.

Brokers differ in how they quote pip values. Some show the value in your account currency (converted already); others show it in the pair's quote currency, leaving conversion to you. Always verify which convention your broker uses and do the math yourself.

## The Role of [Leverage Ratio](/leverage-ratio-forex/) and Margin

Leverage does not change the pip value calculation, but it changes how much capital you must post to control a position. If you have a 1:100 leverage account and want to control one standard EUR/USD lot, you post 1,000 EUR in margin. The pip value remains the same—approximately 10 USD per pip with a USD account—but you are controlling it with less capital.

Converting pip value becomes even more critical when leverage is high. A 1:500 account with poor position sizing can blow up a trader's entire account in a single bad trade, because the pip value in home currency determines the absolute loss per move, regardless of how much margin was posted.

## Practical Approach

Most modern forex platforms handle the conversion automatically in their position risk displays. Before opening a trade, check the platform's "Position Details" or "Trade Setup" panel: it should show your pip value (or per-pip [loss](/equity-financing/)) in your account currency. If it does not, calculate it yourself using the formula above.

For traders handling positions across multiple pairs and account currencies, a simple spreadsheet or calculator that fetches current exchange rates is invaluable. Many trading platforms offer this as a built-in tool; if yours does not, several free forex calculators online do the conversion.

## See also

<div class="wiki-seealso">

### Closely related

- [Pip](/pip/) — The definition and structure of forex price movements
- [Spot exchange rate](/spot-exchange-rate/) — Current rates used for pip value conversion
- Currency pair — Notation and mechanics of forex trading
- [Leverage ratio forex](/leverage-ratio-forex/) — How margin and leverage magnify pip value exposure
- [Margin call forex](/margin-call-forex/) — Risk thresholds that depend on accurate pip calculations

### Wider context

- Forex — The foreign exchange market
- [Currency risk](/currency-risk/) — Exposure to exchange rate moves
- [Currency volatility](/currency-volatility/) — How pip moves vary across pairs
- [Interest rate swap](/interest-rate-swap/) — Related cross-currency instruments

</div>
