---
title: "Pip Value (Forex)"
description: "Minimum price movement in currency pairs converted to dollar impact per standard lot traded."
keywords:
  - pip value
  - forex
  - currency pair
  - price movement
  - standard lot
  - basis point
---

*A **pip** (percentage in point) is the smallest price increment in a currency pair — typically 0.0001 for major pairs like EUR/USD. The **pip value** translates this tiny move into actual profit or loss in dollars, varying by pair, lot size, and which side of the quote is moving.*

<aside class="wiki-infobox">

| Factor | Typical Value |
|--------|---|
| **Pip Size (Major Pairs)** | 0.0001 (1/10,000) |
| **Pip Size (JPY Pairs)** | 0.01 (1/100) |
| **Standard Lot Size** | 100,000 units of base currency |
| **Mini Lot** | 10,000 units |
| **Micro Lot** | 1,000 units |
| **Pip Value (1 Standard Lot, EUR/USD)** | $10 per pip move |
| **Formula** | Pip value = Lot size × Pip size ÷ Current exchange rate |

</aside>

## Why pips matter to forex traders

In forex markets, prices move in fractions. EUR/USD at 1.1050 means 1 euro buys 1.1050 US dollars. A move to 1.1051 is a 1-pip gain. For a retail trader holding 1 [standard lot](/wiki/standard-lot/) (100,000 euros), that single pip is worth $10 of profit or loss. A 100-pip move — from 1.1050 to 1.1150 — is a $1,000 P&L swing.

Pip value scales with lot size. A [micro lot](/wiki/micro-lot/) (1,000 units) on the same 1-pip move yields $0.10; a [mini lot](/wiki/mini-lot/) (10,000 units) yields $1.00. This granularity lets traders size positions by risk: "I can afford a 50-pip stop-loss on 2 mini lots" (lose $100 max).

## The formula and why it varies by pair

Pip value is not constant across currency pairs because the exchange rate is the denominator:

```
Pip value = Lot size × Pip size ÷ Current exchange rate
```

**Example 1: EUR/USD at 1.1050, 1 standard lot (100,000 EUR)**
```
Pip value = 100,000 × 0.0001 ÷ 1.1050 = $9.05 per pip
```

**Example 2: GBP/USD at 1.2700, 1 standard lot (100,000 GBP)**
```
Pip value = 100,000 × 0.0001 ÷ 1.2700 = $7.87 per pip
```

The difference stems from exchange rate. GBP/USD is stronger (higher rate), so each pound-pip is worth fewer dollars. This is why [cross pairs](/wiki/cross-currency-swap/) (not USD-based) require careful position sizing — the pip value relative to your account can be opaque.

## Special case: Yen pairs

Japanese yen pairs (USD/JPY, EUR/JPY) are quoted to 2 decimal places, not 4. USD/JPY at 110.50 means 1 US dollar = 110.50 yen. A move to 110.51 is 1 pip. The formula still holds:

```
Pip value (USD/JPY, 1 standard lot) = 100,000 × 0.01 ÷ 110.50 = $9.05 per pip
```

Note the pip size is 0.01 (not 0.0001) because yen quotes use only 2 decimals. Traders new to yen pairs often confuse pip size with other majors and mis-size positions — a common error.

## Fractional pips (pipettes)

Modern forex brokers quote prices to 5 decimals (or 3 for JPY pairs), introducing sub-pip moves called "pipettes" or "fractional pips." EUR/USD might be quoted 1.10505, splitting the 0.0001 pip into 10 parts. For practical trading, a pipette = 0.1 pips.

This matters for high-frequency and scalping strategies where [bid-ask spreads](/wiki/bid-ask-spread-forex/) are narrow (1–2 pips). A 0.5-pip spread on a 10-pip move is significant; on a 10,000-pip multi-week trend, irrelevant.

## Leverage amplifies pip impact

[Forex leverage](/wiki/forex-leverage/) — borrowing from your broker to control larger positions — multiplies pip value exposure. A trader with $1,000 and 50:1 leverage controls 50,000 EUR at current rates. A 50-pip loss wipes the account. This is why risk management is the first lesson in forex: position size and stop-loss placement must account for pip value and leverage together.

## How to use pip value for position sizing

A disciplined risk framework:

1. Decide max loss per trade (e.g., $50).
2. Identify your stop-loss distance in pips (e.g., 50 pips).
3. Solve for lot size: $50 ÷ (50 pips × pip value) = max lot size.

For EUR/USD at $9.05 per pip:
```
Lot size = $50 ÷ (50 × 9.05) = $50 ÷ $452.50 = 0.11 standard lots ≈ 11,000 EUR (1.1 mini lots)
```

This ensures the stop-loss triggers a $50 loss, no worse. Professional traders apply this logic to every trade; retail traders who skip it are vulnerable to [margin calls](/wiki/forex-leverage/).

## Pip value across order types

[Market orders](/wiki/market-order-execution/), [limit orders](/wiki/limit-order/), and [stop-loss](/wiki/stop-order/) orders all incur slippage and [spread](/wiki/bid-ask-spread-forex/) costs on entry. The pip value of the spread (difference between bid and ask) is real P&L leakage. On a tight 1-pip spread, 1 standard lot of EUR/USD loses ~$10 on entry. A 3-pip spread costs $30.

This is why [high-frequency traders](/wiki/high-frequency-trading/) and [scalpers](/wiki/scalping/) obsess over [execution quality](/wiki/execution-quality-analysis/) and broker selection — basis points in spread can be larger than actual edge in some strategies.

<div class="wiki-seealso">

### Closely related
- [Bid-Ask Spread (Forex)](/wiki/bid-ask-spread-forex/) — Entry cost in pips
- [Forex Leverage](/wiki/forex-leverage/) — Amplifies pip-value impact on account
- [Currency Pair](/wiki/currency-pair/) — Base and quote units determining pip value
- [Standard Lot](/wiki/standard-lot/) — 100,000 units; foundation of pip-value calculation
- [Mini Lot](/wiki/mini-lot/) — 10,000 units; smaller position size
- [Micro Lot](/wiki/micro-lot/) — 1,000 units; smallest standard size

### Wider context
- [Foreign Exchange Market](/wiki/forex-leverage/) — Global FX trading landscape
- [Price Discovery](/wiki/price-discovery/) — How pips aggregate into meaningful trends
- [Carry Trade](/wiki/carry-trade/) — Strategy sensitive to pip moves over time
- [Currency Hedging](/wiki/currency-hedging/) — Risk management relative to pip exposures
- [Position Sizing](/wiki/concentration-limits/) — Risk discipline applied to pip values

</div>
