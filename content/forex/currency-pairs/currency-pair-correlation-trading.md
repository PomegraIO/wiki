---
title: "Using Currency Pair Correlation in FX Trading"
description: "Currency pair correlation measures how two pairs move together or opposite, affecting position sizing, portfolio diversification, and hidden leverage in forex."
keywords:
  - currency pair correlation trading strategy
  - forex pair correlations
  - negative correlation pairs
  - portfolio risk currency pairs
  - correlated fx positions
  - diversification forex trading
---

*Currency pairs do not move in isolation. EUR/USD, GBP/USD, and AUD/USD often move together because they share the same quote currency (USD); conversely, EUR/GBP moves oppositely to EUR/USD and GBP/USD. **Currency pair correlation** quantifies how strongly two pairs move in sync or diverge. Understanding these relationships is critical for proper [position sizing](/position-sizing/), true [diversification](/diversification/), and avoiding hidden leverage in forex portfolios.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Currency pair correlation — key facts</div>

<img src="/svg/forex.svg" alt="An abstract editorial mark for foreign exchange trading." />

<div class="wiki-infobox-caption">Correlations range from +1 (perfect sync) to –1 (perfect opposition); most major pairs cluster at 0.7–0.95 correlation.</div>

|   |   |
|---|---|
| **Positive correlation** | EUR/USD and GBP/USD both rise/fall together (~+0.85–0.95) |
| **Negative correlation** | EUR/USD and EUR/GBP move opposite (~–0.80 to –0.90) |
| **Zero correlation** | Pair movements are independent (rare in forex; most pairs correlate 0.3–0.95) |
| **Measurement period** | Correlations shift; 20-day, 50-day, 252-day (one year) correlations differ materially |
| **Data source** | Daily close prices; intraday tick-by-tick correlations can diverge sharply |
| **Risk implication** | Two correlated pairs carry hidden leverage; sizing must account for correlation drift |
| **Diversification** | True diversification requires low or negative correlations; most majors are too similar |

</aside>

## Why currency pairs correlate

Correlation in forex stems from shared drivers and quote-currency effects.

**Shared quote currency:** When two pairs share the same quote currency, they often move together. EUR/USD and GBP/USD both rally when the US dollar weakens globally. This is not coincidence—the US economy, Fed policy, and dollar supply affect both pairs equally. A 100-basis-point Fed rate cut strengthens the euro and strengthens the pound in tandem, so both EUR/USD and GBP/USD rise.

**Shared base currency:** EUR/GBP, EUR/CHF, and EUR/JPY all have the euro as the base. When euro strength (or weakness) is driven by ECB policy or eurozone growth, all three pairs move together. An ECB rate hike strengthens the euro against all its counterparts, so EUR/GBP, EUR/CHF, and EUR/JPY rise in concert.

**Commodity sensitivity:** AUD/USD and NZD/USD are both commodity currencies—Australia and New Zealand export metals, dairy, and wool. When global commodity prices rally, both pairs often strengthen (AUD and NZD both appreciate). A copper-price crash depresses both pairs similarly.

**Risk sentiment:** During risk-off periods (equities falling, credit widening), investors flee emerging-market and high-yield currencies in favor of safe havens (JPY, CHF, USD). High-yielding pairs (AUD/JPY, NZD/JPY) often fall together because they share the same driver: risk appetite declining. Conversely, when risk appetite rebounds, all high-yielding pairs rally.

## Common correlation patterns

**Major dollar pairs (EUR/USD, GBP/USD, AUD/USD):** Typically +0.80 to +0.95 correlation over one year. They move closely because all three react similarly to Fed policy, US growth, and dollar flows.

**Cross pairs (EUR/GBP, GBP/JPY, AUD/CAD):** Often show lower or negative correlations relative to dollar pairs, because they isolate the relationship between non-dollar currencies. EUR/GBP, for example, is driven by ECB–Bank of England policy divergence, not Fed policy. It can move independently of EUR/USD.

**Safe-haven pairs (USD/JPY, USD/CHF):** Both strengthen in risk-off periods. They show positive correlation (~0.60–0.80) but weaker than dollar pairs, because JPY and CHF are influenced by their respective central banks' policies independent of the Fed.

**High-yielding carry pairs (AUD/JPY, NZD/JPY, CAD/JPY):** Show very high correlation (+0.85–0.95) because they are all driven by the same driver: risk appetite and carry-trade unwinding. When risk turns sour, all three collapse together.

## Measuring correlation and drift

Correlation is not static. It is calculated over a lookback window—commonly 20 days (one month), 50 days (two months), or 252 days (one trading year). Over different periods, correlations shift materially.

For example, EUR/USD and GBP/USD might correlate at +0.92 over a 252-day window, but over the last 20 days, if the Bank of England has raised rates while the ECB held steady, their correlation might drop to +0.75. A trader who assumes stable +0.92 correlation and sizes two positions aggressively could face unexpected volatility if the correlation suddenly drifts.

**Correlation breakdown:** During geopolitical shocks (wars, energy crises), safe-haven demand can overwhelm normal correlations. The March 2022 Russia–Ukraine invasion caused typically correlated dollar pairs to diverge sharply as investors fled to JPY and CHF, breaking the normal positive correlation.

## Position sizing and hidden leverage

This is where correlation matters most. Suppose you hold 1 standard lot of EUR/USD and 1 standard lot of GBP/USD. You believe you are balanced—two independent positions offsetting each other's risk. But if EUR/USD and GBP/USD correlate at +0.90, you are not balanced at all. They move in near-perfect lockstep. Your actual leverage is much higher than you realize.

Imagine EUR/USD loses 1% and you profit $1,000. If GBP/USD loses 0.95% (0.90 correlation), you lose $950 on the short. Net loss: $950. Your two "independent" positions actually behaved nearly identically, creating hidden leverage.

**Proper sizing:** If you hold a long EUR/USD and want to hedge with a short GBP/USD, you must size the short larger to account for correlation. If correlation is +0.90, you need roughly 1 lot EUR/USD long and 1.1 lots GBP/USD short to achieve true hedging. If correlation drops to +0.50, you need 2 lots GBP/USD short to offset the EUR/USD long completely.

The general rule:

**Short sizing = (Lot size × Long correlation) ÷ (1 – desired hedge ratio)**

For a short GBP/USD hedge against 1 lot EUR/USD at +0.90 correlation, if you want 90% hedge: Short = (1 × 0.90) ÷ (1 – 0.90) = 9 lots. That seems extreme, but it reflects the reality: if you want to hedge a highly correlated pair, you need to oversized the opposite position dramatically.

This is why traders often avoid hedging with highly correlated pairs. Instead, they use cross pairs or non-correlated pairs, or they turn to [futures contracts](/futures-contract/), options, or [swaps](/swap/) for cleaner hedging.

## Correlation drift and mean reversion

Correlations also mean-revert. A pair that correlates at +0.50 for months might spike to +0.85 during a shock, then gradually drift back to +0.50 over weeks. Traders watching correlation breakdowns can anticipate mean reversion: when EUR/USD and GBP/USD suddenly drop from +0.90 to +0.60 correlation, history suggests they will gravitate back to +0.90 over time, creating a relative-value trade.

This is the basis of **correlation arbitrage:** betting that two pairs' correlation will revert to historical levels. If your model predicts +0.80 correlation and realized correlation is +0.55, you might long the GBP/USD relative to EUR/USD (buy GBP/USD, short EUR/USD), betting they will re-correlate.

## Negative correlations: natural hedges

Negative correlations offer true diversification. EUR/USD and USD/JPY often show negative or weak positive correlation (~–0.10 to +0.40) because eurozone and Japan economic cycles differ. Strong euro often coincides with weak yen (Japan in deflation, low rates), creating a natural hedge.

**Example:** You hold a long EUR/USD and a short USD/JPY. If the euro weakens (EUR/USD drops 1%), the yen typically strengthens (USD/JPY drops 1–2%). Your two positions partly offset each other, reducing portfolio volatility. This is genuine diversification.

Traders seeking true diversification avoid loading up on major dollar pairs, which are too similar. Instead, they pair:

- EUR/USD with USD/JPY (negative correlation)
- GBP/USD with AUD/USD (often +0.60–0.75, moderate; offers some diversification)
- AUD/JPY with USD/JPY (both safe-haven driven, but via different routes; moderate correlation)
- Commodity pairs (AUD/USD, CAD/USD) with safe-haven pairs (USD/JPY)—inverse exposure to risk appetite

## Correlation and carry trades

Carry traders must be aware of correlation clustering. If you hold five high-yielding pairs (AUD/JPY, NZD/JPY, GBP/JPY, AUD/NZD, GBP/NZD), they likely correlate at +0.85–0.95. A single risk-off event (flight to safety) wipes out all five simultaneously. Genuine carry-trade diversification requires mixing high-yielding pairs with short-correlation pairs, or with unrelated pairs to create uncorrelated return streams.

## Practical trading implications

- **Hedging:** To hedge a long EUR/USD, use a short currency pair with correlation near zero (like EUR/JPY or GBP/JPY), not another dollar pair.
- **Position sizing:** Account for correlation when calculating true portfolio risk. A portfolio of 10 "diversified" major-dollar-pair positions is concentrated, not diversified.
- **Trend trading:** If you trade EUR/USD and GBP/USD because both are trending up, recognize they trend together. You have one directional bet, not two independent ideas.
- **Correlation breakdown:** When correlations suddenly break (drop from +0.90 to +0.50), watch for mean reversion. Historical extremes rarely persist.
- **Time frame sensitivity:** Intraday correlations (15-minute, hourly) can differ sharply from daily correlations. Scalpers need tick-level data; swing traders rely on daily closes.

## See also

<div class="wiki-seealso">

### Closely related

- [Currency pair](/currency-pair/) — structure and quote conventions
- [Carry trade](/carry-trade/) — leveraging interest rate differentials
- [Position sizing](/position-sizing/) — proper lot selection and risk management
- [Diversification](/diversification/) — reducing portfolio risk
- Leverage — amplification and hidden leverage risks
- [Currency pair rollover and swap rates](/currency-pair-rollover-swap-rates/) — overnight carry costs on correlated pairs

### Wider context

- Risk management — portfolio volatility and drawdown
- [Hedge fund](/hedge-fund/) — correlation arbitrage strategies
- Forex market — structure and trading mechanics
- [Beta](/beta/) — systematic market risk and co-movement

</div>
