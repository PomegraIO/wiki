---
title: "Paasche Price Index"
description: "A price index weighted by current-period quantities that systematically understates inflation but requires real-time consumption data."
keywords:
  - paasche-index
  - current-weighted-index
  - price-index-bias
  - substitution-adjustment
  - inflation-measurement
image: /svg/macro.svg
---

*A **Paasche Price Index** measures the cost of current consumption patterns at current prices relative to what those same patterns would have cost in a base period. By reweighting according to what people actually buy now, it avoids the substitution bias of the [Laspeyres Price Index](/laspeyres-price-index/)—but introduces the opposite error: systematically understating the true inflation in living costs.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Paasche Price Index — key facts</div>

<img src="/svg/macro.svg" alt="An abstract editorial mark for macroeconomic data." />

<div class="wiki-infobox-caption">The inverse answer: real-time weights, inverse bias, and a data lag that keeps it from official use.</div>

|   |   |
|---|---|
| **What it is** | Index number = (cost of current-period basket at current prices) ÷ (same basket at base prices) × 100 |
| **Named after** | Hermann Paasche, 19th-century statistician |
| **Key bias** | Downward (overstates real living standards by comparing to a basket the old consumer never faced) |
| **Data requirement** | Current-period consumption quantities, not available until survey lags |
| **Alternative** | [Laspeyres Price Index](/laspeyres-price-index/), Fisher index, chained indices |

</aside>

## The inverse of Laspeyres

Where the [Laspeyres Price Index](/laspeyres-price-index/) locks the basket to the past, the Paasche index locks it to the present. Instead of asking "How much would a 2000 consumer need to spend to buy 2000 quantities today?", Paasche asks "How much would a 2024 consumer have spent in 2000 to buy 2024 quantities?"

The result is a mirror-image distortion. A Paasche index, by construction, is always lower than Laspeyres. If prices have risen unevenly—if beef is up 200% but chicken is flat—a Laspeyres index counts the beef rise heavily (since the 2000 consumer bought a lot of beef). Paasche counts it lightly (since the 2024 consumer bought much less beef, having substituted to chicken).

## Why the downward bias matters

This downward bias is not harmless. By always selecting the cheapest alternatives as the comparison point, Paasche overstates how well off people are. It tells a story in which inflation is smaller than it truly was, because it forces the old base period to accommodate new shopping patterns that did not exist then.

A concrete example: suppose housing costs triple and food costs stay flat. Paasche takes 2024 consumption patterns (which include less housing because people bought fewer homes) and asks what it would have cost to buy that reduced-housing bundle in 2000. The answer understates the shock to living costs, because it does not ask what happened to the households who did try to maintain their 2000 housing standard.

This is why economists say Paasche has a **substitution bias in the opposite direction**. Laspeyres overestimates inflation by assuming no substitution. Paasche underestimates it by assuming perfect, instantaneous substitution. The truth lies between.

## The data-lag problem

If Paasche is such a natural correction to Laspeyres, why do most statistical agencies not use it? The answer is practical: Paasche requires knowing current consumption quantities. You cannot calculate a Paasche index until you survey households and learn what they actually bought. That survey data typically lags the reference month by weeks or months.

The [Laspeyres Price Index](/laspeyres-price-index/), by contrast, needs only current prices, which are collected much faster. A central bank can publish Laspeyres inflation within days; Paasche inflation often cannot be published with confidence until it is already old news.

In modern practice, some statistical agencies publish Paasche indices retroactively—months or years after the fact—as part of detailed inflation analysis. But for the real-time inflation signal that guides [monetary policy](/monetary-policy/), Laspeyres dominates.

## The Fisher index as compromise

Aware that Laspeyres and Paasche bracket the truth—one too high, one too low—the statistician Irving Fisher proposed taking their geometric mean, known as the **Fisher index** or "ideal" index. Fisher is not biased in the same direction as either Laspeyres or Paasche; it splits the difference.

Some statistical agencies, including the U.S. [Consumer Price Index](/consumer-price-index/), now publish chained indices that function somewhat like Fisher indices by rebasing and reweighting periodically. This reduces but does not eliminate the upward bias of pure Laspeyres methodology.

## Paasche in practice

In academic research and detailed inflation studies, Paasche indices are useful as a reality check. If an official Laspeyres-based [Consumer Price Index](/consumer-price-index/) reads 4% inflation and a retroactive Paasche index reads 3.2%, the gap suggests substitution effects are significant. This is valuable information for understanding whether people are truly worse off or whether they have painlessly adjusted to new prices.

During the 2021–2023 inflation surge, some researchers constructed Paasche indices using real-time spending data from credit-card processors and online retailers. These "nowcast" Paasches showed lower inflation than the official indices, hinting that households had already begun substituting away from the most expensive goods—a message the backward-looking Laspeyres index missed.

## See also

<div class="wiki-seealso">

### Closely related

- [Laspeyres Price Index](/laspeyres-price-index/) — the official standard, upward biased, and the reason Paasche exists
- [Consumer Price Index](/consumer-price-index/) — inflation measure using Laspeyres logic with periodic reweighting
- [Hedonic Pricing](/hedonic-pricing/) — a quality-adjustment technique orthogonal to the Laspeyres-Paasche tradeoff
- [Inflation](/inflation/) — the concept both indices try to measure, imperfectly
- [Core Inflation](/core-inflation/) — inflation excluding volatile items, also subject to index-number choice bias

### Wider context

- [Monetary Policy](/monetary-policy/) — policy that relies on inflation indices despite their known biases
- [Deflation](/deflation/) — downward price movements, also measured via index-number formulas
- Substitution Bias — the fundamental tension that Laspeyres and Paasche represent

</div>
