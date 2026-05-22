---
title: "Put-Call Ratio Volume"
description: "The ratio of trading volume in put options relative to call options, used as a market sentiment indicator."
keywords:
  - put-call ratio
  - trading volume
  - options sentiment
  - market fear gauge
---

*The **put-call ratio volume** is the ratio of the number of [put option](/wiki/put-option/) contracts traded (by volume) to the number of [call option](/wiki/call-option/) contracts traded during a given period. A high ratio (more puts traded than calls) suggests that traders are buying downside protection or betting on declining prices, signalling defensive or bearish sentiment; a low ratio indicates call dominance and bullish sentiment.*

<aside class="wiki-infobox">

| Item | Detail |
|---|---|
| **Numerator** | Volume of put contracts traded (shares controlled if exercised) |
| **Denominator** | Volume of call contracts traded |
| **Typical range** | 0.5 to 1.5 (broad market); 1.0 is neutral baseline |
| **High ratio** | >1.2–1.5 = Fear, hedging, bearish betting |
| **Low ratio** | <0.7–0.8 = Greed, confidence, bullish speculation |
| **Data source** | CBOE, exchange option volume reports, real-time feeds |
| **Time horizon** | Daily, weekly, or cumulative intra-session |

</aside>

## How put-call ratio volume works as a sentiment indicator

The put-call ratio volume reflects the **intensity of buying in puts versus calls**, not just the count of contracts. A trader buying 1,000 shares of downside protection via puts is voting for a decline; a trader selling 100 call spreads is also betting bearish, but with leverage. The volume-weighted ratio captures this flow.

When the ratio rises above 1.0 (more put volume than call volume), it signals that buyers are paying premiums to hedge against downside or to profit from crashes. Paradoxically, *extreme* put-call ratios often **contradict** the outlook they imply: a ratio spiking to 2.0+ ("panic buying") may indicate capitulation (sellers exhausted, price bottom imminent) rather than confirmation of further declines. Conversely, a ratio collapsing below 0.5 signals confidence bordering on [complacency](/wiki/overconfidence-bias/), suggesting that a pullback or short squeeze may be near.

Put-call ratio volume differs from put-call ratio **by open interest** (total outstanding contracts). Open interest reflects positioning held over time; volume reflects flow in the current session or day. A high volume ratio with low open-interest ratio suggests a single day's hedging spike (e.g., after an earnings miss) rather than sustained bearish betting.

## Interpretation and trading signals

**Moderate put-call ratio (0.8–1.2).** A ratio in this zone reflects balanced sentiment—neither extreme fear nor extreme greed. Traders across both sides are transacting, and the market is in equilibrium. No strong contrarian signal.

**High ratio (>1.5).** This often appears after sharp market drops (e.g., [flash crashes](/wiki/flash-crash-2010/), earnings gaps, geopolitical shocks). Retail investors buy protective puts; institutions hedge portfolios. Volume spikes in puts. The ratio spike is often contrarian: it signals capitulation (everyone is scared, so the risk-reward tilts bullish). Major market bottoms frequently coincide with or immediately follow put-call ratio volume spikes.

**Low ratio (<0.6).** This suggests aggressive call buying and put selling—greed and confidence. Investors are buying upside exposure and selling downside protection (taking on risk). Ironically, this can precede corrections: complacency breeds blindness to risks, and a small shock (earnings miss, Fed surprise) can trigger a sharp pullback that catches call buyers and put sellers off-guard.

**Divergence with price.** If prices rise sharply but put-call ratio volume remains elevated, it suggests that some large hedgers (e.g., fund managers protecting portfolios) are holding puts even as the market rallies. This divergence can signal underlying nervousness despite surface bullishness.

## Variations and related metrics

**Put-call ratio breadth**: Counts the number of put-to-call contracts, ignoring volume (shares controlled). Both versions exist; volume-weighted ratio is considered more sensitive to trader conviction.

**Index vs. single-stock.** The S&P 500 index put-call ratio is broader and less volatile than single-stock ratios; Apple's ratio can spike 2.0+ after earnings, while the SPX ratio rarely exceeds 1.5.

**Weighted by open interest.** Some analysts compute a ratio using total open interest (all outstanding contracts) rather than daily volume, capturing net positioning. This varies more slowly and is less reactive to single-day flows.

**VIX and implied volatility.** The [VIX](/wiki/fear-index/) (volatility index based on S&P 500 index option [implied volatility](/wiki/implied-volatility/)) is a related gauge of fear. It tends to spike when put-call ratio volume is high (because puts are more volatile than calls when IV rises). However, the VIX can stay elevated even as put-call volume normalizes, so the two metrics diverge at times.

## Practical use in trading and risk management

Institutional managers use put-call ratio volume as one of many sentiment gauges. A portfolio manager concerned about a correction might buy protective puts; if the ratio shows most other traders are also hedging, it reinforces the decision. Conversely, if the manager is bearish but the ratio is low (few puts bought), the manager might conclude that fear is underpriced and wait to buy puts at lower cost (if IV falls).

Retail traders often use the ratio as a contrarian indicator: buys when the ratio is extremely high (fear spike), sells when it's extremely low (greed). Backtests show mixed results; the ratio is useful as *one input* among many, not a standalone signal. Market structure also matters: during bull markets, put-call ratios tend to be lower because hedging is less urgent; the same ratio (0.8) might be neutral in a bull and bearish in a bear.

Hedging programs (stop-loss replacements, tail-risk hedges, portfolio insurance) all create puts and raise the volume ratio. Monitoring the ratio helps risk managers understand whether their hedges are crowded (expensive) or unique (cheap). Extreme ratios sometimes precede sharp repricing of volatility, affecting hedge costs.

## Limitations

Put-call volume can be distorted by single large trades (e.g., a hedge fund buying 100,000 puts to protect a $10 billion portfolio) and does not necessarily reflect "retail" vs. "institutional" sentiment. Options exchanges publish detailed data, but interpreting flows requires context: a bank might be selling calls to hedge equity issuance, not expressing bearish sentiment.

The ratio also conflates **hedging** (demand for put downside protection) with **speculation** (bullish bets via calls). A ratio spike can mean either more hedging or less speculation, and the trading implications differ.

<div class="wiki-seealso">

### Closely related
- [Put Option](/wiki/put-option/) — The downside instrument
- [Call Option](/wiki/call-option/) — The upside instrument
- [Put-Call Parity](/wiki/put-call-parity/) — Mathematical relationship between puts and calls
- [Implied Volatility](/wiki/implied-volatility/) — What puts and calls are pricing

### Wider context
- [Technical Analysis](/wiki/technical-analysis/) — Broader category of sentiment metrics
- [Fear Index (VIX)](/wiki/fear-index/) — Related volatility sentiment gauge
- [Market Sentiment](/wiki/sentiment-reversal/) — Broader investor psychology
- [Options Greeks](/wiki/options-greeks/) — Greeks affected by put-call shifts

</div>
