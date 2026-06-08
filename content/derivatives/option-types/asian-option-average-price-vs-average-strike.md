---
title: "Average-Price vs Average-Strike Asian Options"
description: "Average-price and average-strike Asian options reduce volatility impact differently. Average-price options average the asset's price over time; average-strike options fix the strike as the mean price. Learn when each lowers hedging costs."
keywords:
  - asian option average price
  - asian option average strike
  - average price vs average strike
  - path-dependent option
  - volatility reduction derivative
image: /svg/derivatives.svg
---

*An **average-price Asian option** pays out based on the gap between a fixed strike and the mean asset price observed over a window; an **average-strike Asian option** flips this—the strike itself becomes the average price, and the payout is the final spot price minus that mean strike. Both lower volatility-driven premiums compared to vanilla options, but they transfer risk in opposite directions and suit different hedging needs.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Average-Price vs Average-Strike — Key Differences</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives." />

<div class="wiki-infobox-caption">Two structurally opposite ways to tame the tail risk of individual price spikes.</div>

|   |   |
|---|---|
| **What averages** | Average-Price: the asset price over time; Average-Strike: the strike level |
| **Strike at issue** | Average-Price: fixed upfront; Average-Strike: observed, then locked |
| **Cost vs vanilla** | Both cheaper; strike averaging typically costs less |
| **Who benefits** | Average-Price: buyers hedging final price exposure; Average-Strike: sellers reducing entry cost |
| **Typical use** | Average-Price: commodity, FX hedges; Average-Strike: structured products, long accumulation |

</aside>

## Mechanics of Average-Price Asian Options

In an **average-price** call, you specify a strike (say $100) upfront. At expiry, the exchange calculates the arithmetic mean of the asset's price sampled daily (or at other intervals) over the observation window. Your profit is the max of zero or (average price – strike). A $100 strike with a final average of $105 pays $5 per share.

This structure smooths out single-day shocks. If the stock spikes to $120 on day 50 then crashes to $95 by maturity, the average might still be $102, leaving you with a modest payoff. A vanilla call at $100 would deliver $20 at the spike peak—capturing that tail—but the average call clips it.

Average-price options are cheaper than vanilla calls because the averaging dampens extreme price outcomes. You lose upside from being tied to the mean, not the final spot. This trade-off appeals to hedgers buying protection: the cost is lower, and the protection is smooth rather than binary.

## Mechanics of Average-Strike Asian Options

An **average-strike** call works in reverse. There's no pre-set strike. Instead, the exchange logs the price path over the observation window, calculates the arithmetic mean, and that mean *becomes your strike*. At expiry, you receive the max of zero or (final spot price – average strike).

If the asset averages $100 over the window but finishes at $110, you collect $10 per share. The appeal: your effective entry point is the average of everything that happened, not a single moment. You capture the final price move (from $100 to $110), but your cost basis is the patient mean, not the worst price during the window.

Average-strike calls cost even less than average-price calls because the strike itself is drawn from the actual price path. A buyer effectively gets downside protection built into the lower strike; a seller knows the strike won't be set at a peak—it's the *observed reality* of the mean price.

## Cost and Volatility Implications

Both average-price and average-strike options are cheaper than vanilla counterparts because averaging reduces the surface area for extreme payoffs. Volatility, in option pricing terms, measures the severity of price moves; averaging shrinks the effective volatility.

**Average-price options** typically trade at 70–80% of vanilla call premiums in moderately volatile assets. The savings come from clipping upside: if the stock doubles in a day then sinks back, you don't capture that spike.

**Average-strike options** are even cheaper—often 50–70% of vanilla. The reason: the strike itself moves with the price path. In a rising market, the average strike climbs too, so your breakeven point rises as well. In a sideways or declining market, the average strike is lower than a pre-set $100, but the final spot price is also lower, leaving a narrower or zero payoff.

The cost advantage is largest when the asset exhibits large, episodic swings. A commodity with seasonal price jumps will see bigger premiums for vanilla calls than Asian calls, because the spikes are partly averaged away.

## When to Use Average-Price Asian Options

Average-price Asian options suit **hedgers with continuous exposure** to price risk over a known window. A food company buying quarterly soybean hedges might use average-price puts: if soy spikes mid-quarter, the put protects the average, not the spike alone. The lower premium and smooth payoff align with the company's steady input costs.

A multinational firm hedging currency over a payment quarter also benefits. Rather than hedging the final day's spot rate, it hedges the quarter's average rate, recognizing that its revenue (in foreign currency) and costs accumulate over time.

Average-price calls suit buyers betting on a sustained uptrend. The cheaper premium lets you buy more protection per dollar, even though you forfeit the tail upside.

## When to Use Average-Strike Asian Options

Average-strike Asian options appeal to **accumulators and systematic buyers**. A pension fund dollar-cost averaging into equities over a year wants to lock in the average entry price, not the worst day's price or a pre-set strike that proves too conservative.

Structured products and notes often embed average-strike calls to offer a lower knock-in level or a cheaper embedded call. A "10-year accumulated return note" might use an average-strike call to reduce issuance cost while still delivering participation in the final price move.

They also suit **short sellers and issuers** reducing hedging costs. An issuer writing structured notes with embedded calls wants cheap call optionality; an average-strike call, with its moving strike, costs less to issue than a vanilla call.

## Sampling Frequency and Observation Windows

Both variants hinge on the sampling schedule. Daily sampling (the most common) creates a full-window average. Weekly or monthly sampling is coarser and cheaper, because fewer data points reduce the average's precision and increase the probability of higher final payoffs.

The observation window matters too. A 1-month average-price call is more sensitive to intra-month shocks than a 3-month window. Long windows smooth more aggressively, justifying even lower premiums.

Exchanges and dealers specify these terms upfront; they are not negotiable once the contract is struck.

## Correlations with the Underlying Market

Average-price options decay in value if the market drifts sideways or down—the averaging acts like a drag on realized profits. Average-strike options are more sensitive to the final price level; if the asset rallies sharply in the final week after a sleepy first three months, the average-strike call captures that rally with a strike set by the prior calm period.

In calm, uptrending markets, average-strike calls outperform average-price calls on a payout basis. In choppy, mean-reverting markets, the averaging dampens outliers for both, but average-price options feel less value if the spike happens early and the asset mean-reverts down.

## Settlement and Operational Considerations

Most Asian options settle in cash on a single maturity date, with the exchange computing the average for you. Some OTC variants offer customizable sampling—daily close, intraday high-low average, volume-weighted, etc.—but exchange-traded versions stick to standardized schedules.

Illiquidity is real. Average-strike and average-price options trade much smaller volumes than vanilla calls and puts; this widens bid-ask spreads and makes it harder to exit early.

## See also

<div class="wiki-seealso">

### Closely related

- [Option](/option/) — the foundational mechanics of calls, puts, and intrinsic value
- [Call option](/call-option/) — long calls and their payoff profiles
- [Derivatives hedging](/derivatives-hedging/) — why corporations hedge and how Asian options fit in
- [Volatility smile](/volatility-smile/) — how options markets price different strikes
- [Strike price](/strike-price/) — setting and adjusting the breakeven level
- [Path-dependent option](/option/) — the broader category of options where history matters

### Wider context

- [Option premium](/option-premium/) — what you pay for optionality
- [Over-the-counter market](/over-the-counter-market/) — where most Asian options are traded
- [Commodity hedging](/derivatives-hedging/) — agricultural and energy use cases
- [Structured product](/structured-product/) — products that embed average-price and average-strike options

</div>
