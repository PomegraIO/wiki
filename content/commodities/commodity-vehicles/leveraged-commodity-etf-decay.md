---
title: "Leveraged Commodity ETF Decay"
description: "The mathematical drag that erodes long-term returns in leveraged commodity ETFs due to daily rebalancing in volatile markets."
keywords:
  - leveraged etf decay
  - volatility decay
  - daily rebalancing
  - leveraged commodity etf
  - etf slippage
  - compounding loss
image: "/svg/commodities.svg"
---

*A leveraged commodity [ETF](/etf/) applies daily rebalancing to maintain a fixed [leverage](/debt-financing/) multiple (e.g., 2× or 3×). In volatile markets, this daily reset compounds losses through a phenomenon called **decay**—returns systematically trail the underlying commodity's theoretical leveraged performance. A 2× oil ETF does not deliver exactly twice the daily oil price move; it trails by an amount proportional to volatility, making it unsuitable for long-term holding.*

<div class="wiki-hatnote">

For the inverse effect in rising markets, see [inverse ETF](/inverse-etf/).

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Leveraged Commodity ETF Decay — key facts</div>

<img src="/svg/commodities.svg" alt="An abstract editorial mark for the commodities category." />

<div class="wiki-infobox-caption">A mathematical drag unique to daily-reset leverage in volatile derivatives markets.</div>

|   |   |
|---|---|
| **What it is** | Return slippage from daily rebalancing, not tracking error from [management fees](/management-fee/) alone |
| **Root cause** | Compounding losses from buying high and selling low on each rebalance |
| **Severity factor** | [Volatility](/historical-volatility/) — higher volatility = faster decay |
| **Typical drag** | 1–5% per month in high-volatility markets (crude oil, natural gas) |
| **Time horizon** | Insignificant intraday; severe over weeks to years |
| **Investor suitability** | Day traders and tactical traders only; not buy-and-hold |
| **Alternative for long-term** | Unleveraged [commodity ETF](/etf/), [futures](/futures-contract/), or [commodity pool](/commodity-pool-operator/) |

</aside>

## The daily rebalancing trap

Most leveraged [ETFs](/etf/) promise to deliver a fixed multiple of the underlying index return *on a daily basis*. A 2× crude oil ETF should deliver exactly 2% return when crude rises 1% in a single trading day. To maintain this leverage ratio, the fund's portfolio manager rebalances every day at close, adjusting the position size to keep leverage constant. This daily reset is the source of decay.

Consider a simplified example: Day 1, crude oil rises 2%, and the 2× ETF rises 4%. The fund has now exceeded its 2× leverage ratio (because the fund's equity has grown), so it must reduce its position. Day 2, crude oil falls 2%, but the fund now holds fewer contracts. Its loss is only approximately 4%, while 2× crude would be 4% down. Over this two-day cycle—a flat move overall—the 2× ETF has lost value even though crude ended flat. This is decay in miniature.

## The mathematics of volatility drag

Decay is purely a mathematical artifact of compounding. The formula commonly cited is:

**Expected decay ≈ (Leverage)² × (Daily volatility)² × Number of periods**

For a 2× leveraged fund in an asset with 2% daily [volatility](/historical-volatility/), monthly decay is roughly 2² × (0.02)² × 21 trading days ≈ 3.4% per month. In a 3× leveraged natural gas fund during a crisis with 5% daily volatility, decay could approach 10–15% monthly. This is not management fees or bid-ask spreads; it is pure compounding loss.

The key insight: decay accelerates with volatility. In calm, trending markets (low volatility), decay is negligible and the leverage works as advertised. In choppy, sideways markets, decay kills returns. Commodity markets are notoriously choppy—subject to weather, geopolitics, and margin-call cascades—making them especially prone to decay.

## Why daily rebalancing is cheaper than static leverage

Fund sponsors choose daily rebalancing because it is mechanically simple and scales efficiently. Alternative approaches exist. A fund could hold a static position in leveraged [futures contracts](/futures-contract/) or [options](/option/), but those require active risk management, prime brokerage relationships, and margin monitoring—expensive infrastructure. Daily rebalancing via index futures or [swap contracts](/forward-contract/) is cheaper and more transparent, even if it guarantees decay in volatile conditions.

Regulatory arbitrage also plays a role: daily rebalancing allows the fund to avoid some restrictions on leverage ratios and [leverage](/debt-financing/) limits that static leverage structures face. The SEC permits daily-reset leverage as a sort of grandfathered exception, provided it is disclosed plainly.

## Empirical decay over time

A 3× crude oil ETF from 2014–2016 saw periods of spectacular decay. Crude fell from $100/barrel to $26/barrel, then recovered to $50, with violent intraday swings. An investor buying the 3× ETF in mid-2014 and holding through 2016 would have lost far more than 3× the crude fall, then gained far less than 3× the recovery. The [compounding](/compound-interest/) math worked against them both directions. Similarly, leveraged grain ETFs suffered decay during the 2022 agricultural volatility spike when wheat prices gyrated ±10% intraday. Empirical studies show decay rates of 1–3% monthly in commodity markets during normal periods, rising to 5–10% monthly during spikes.

## Decay vs. expense ratio and tracking error

Decay is distinct from [expense ratio](/expense-ratio/) and tracking error. A 0.5% annual [expense ratio](/expense-ratio/) is a flat cost, deducted proportionally over time. Tracking error arises from imperfect index replication—the fund's actual holdings lag the index slightly. Both are real drains, but they are deterministic. Decay, by contrast, is stochastic and volatile-dependent; the fund manager cannot control it. A fund with a 0.3% [expense ratio](/expense-ratio/) might incur 2% decay monthly, making the ratio noise by comparison.

## Why investors still buy them (and shouldn't hold long-term)

Leveraged commodity ETFs are liquid, inexpensive to access, and offer daily tradability. A trader expecting crude to rise 5% tomorrow can buy a 2× or 3× oil ETF without opening a futures account or understanding margin calls. For that one-day trade, decay is negligible. But retail investors often "accidentally" hold these funds for months or years, drawn by the leverage promise. This is where decay becomes catastrophic. A retiree who bought a 3× natural gas ETF in 2021 and held into 2022 watched it evaporate as volatility spiked and decay accelerated—a loss far worse than the underlying commodity's volatility alone would suggest.

Professionals exploit decay strategically. Hedge funds sometimes short leveraged ETFs, betting on decay, especially in sideways choppy markets. This is a statistical arbitrage; the decay is mathematically certain, just not the timing of decay's impact.

## Long-term alternatives

For investors seeking sustained commodity exposure, [commodity pool operators](/commodity-pool-operator/) hold positions longer (weeks to months) and rebalance less frequently, avoiding daily decay. Unleveraged [commodity ETFs](/etf/) and [commodity indices](/price-discovery/) remove leverage entirely, accepting lower returns but eliminating decay risk. Direct [futures](/futures-contract/) trading on exchange via a registered broker gives full control over rebalancing frequency and leverage timing—professionals manage this manually. [Energy master limited partnerships](/energy-master-limited-partnership/) and [natural resource equity funds](/natural-resources-equity-fund/) provide commodity exposure through operating cash flows and equity appreciation rather than derivatives, sidestepping volatility decay altogether.

## See also

<div class="wiki-seealso">

### Closely related

- [Leveraged ETF](/leveraged-etf/) — the broader mechanics of daily-reset leverage across asset classes
- [Volatility](/historical-volatility/) — the primary driver of decay severity
- [Inverse ETF](/inverse-etf/) — bear-market leverage with identical decay dynamics
- [Expense ratio](/expense-ratio/) — a separate, non-volatility cost structure
- [Compounding](/compound-interest/) — the mathematical principle underlying decay losses

### Wider context

- [Commodity pool operator](/commodity-pool-operator/) — alternative active vehicle with less frequent rebalancing
- [Futures contract](/futures-contract/) — underlying derivative used in leveraged ETF rebalancing
- [Options](/option/) — alternative for tactical leverage with different cost structure
- [Energy master limited partnership](/energy-master-limited-partnership/) — commodity exposure via operating cash flows, not leverage

</div>
