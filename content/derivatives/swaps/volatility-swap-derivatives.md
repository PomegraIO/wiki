---
title: "Volatility Swap"
description: "A forward contract where one party receives a fixed volatility strike and the other receives the realised volatility of an asset over the contract term."
keywords:
  - volatility swap
  - realised volatility
  - vol swap derivative
  - volatility trading
image: "/svg/derivatives.svg"
---

*A **volatility swap** is a [forward contract](/forward-contract/) in which one counterparty pays a fixed volatility strike, and the other pays the realised (historical) volatility of an underlying asset over the contract's term. Unlike a [straddle](/option/) or [variance swap](/forward-contract/), a volatility swap is linear in realised volatility, making it an elegant instrument for trading volatility as a standalone asset and for hedging [volatility risk](/market-risk/) without directional exposure to the underlying price.*

<div class="wiki-hatnote">

For volatility trading via options, see [Straddle](/option/); for variance (squared volatility), see [Variance Swap](/forward-contract/).

</div>

## Structure and settlement

A volatility swap is a one-for-one exchange. Party A pays a fixed volatility amount (the strike, typically quoted as an annualised percentage, such as 18%) multiplied by notional. Party B pays the realised volatility, also annualised and multiplied by the same notional.

Realised volatility is calculated as the annualised standard deviation of daily (or intra-daily) log returns of the underlying, observed over the swap's life. If the underlying is the S&P 500 and realised vol turns out to be 22%, then Party B (the realised-vol payer) owes Party A an amount equal to (22% − 18%) × notional. If realised vol is 16%, Party A owes Party B.

Unlike [option](/option/) payoff, there is no convexity or gamma. The payoff is linear in the difference between realised and fixed volatility. This linearity makes volatility swaps far more intuitive than variance swaps (which pay based on the square of volatility) and far cheaper to replicate using a [delta-neutral](/delta/) option portfolio.

## Why volatility swaps are cleaner than variance swaps

A variance swap pays proportional to the square of realised volatility, creating a convex payoff. This convexity arises naturally when you replicate a variance swap by selling a [straddle](/option/) and delta-hedging continuously; the hedging cost is proportional to realised squared volatility, not realised volatility itself.

Volatility swaps, by contrast, are harder to replicate via options alone, but they are linear and easier to reason about. If you believe volatility will be 25% but the market prices it at 20%, a vol swap lets you express that view directly, earning (25% − 20%) × notional at expiry. No non-linearity, no gamma surprises during the holding period.

The trade-off: volatility swaps are less liquid than variance swaps and option straddles. Fewer dealers make markets; the spreads are wider; and for exotic underlyings or very long tenors, pricing can be opaque.

## Pricing the volatility strike

The dealer's initial strike is set to the [implied volatility](/implied-volatility/) (IV) extracted from the option market on that same underlying, maturity, and moneyness. The intuition is simple: if an option market implies 18% volatility, a fair volatility strike is 18%. If realised vol is higher, the swap payer loses; if realised is lower, they profit.

However, dealers do not quote exactly at implied volatility. They adjust for:

1. **Term structure of volatility**: Longer-dated swaps (6 months, 1 year, 3 years) have different implied levels than short-dated. A dealer uses a volatility curve.

2. **Volatility risk premium**: Markets tend to price volatility swaps slightly higher than the unconditional expected realised volatility, as compensation for volatility being a risky asset and for the cost of hedging. The risk premium varies with market regime and can be 100–300 basis points.

3. **Dealer funding and repo**: The cost to hedge (often via options or variance swaps) includes financing. This cost is baked into the quote.

4. **Jump risk and tail risk**: If an underlying can jump sharply (such as earnings announcements for single stocks or central bank decisions for currencies), realised volatility can spike unexpectedly. Dealers demand additional premium for jump risk.

## How traders use volatility swaps

**Volatility speculators** are the primary users. If a trader believes the market is overpricing volatility (via option IV), the trader pays fixed vol (sells the swap) and pockets the difference if realised vol comes in lower. If the trader believes volatility is too cheap, they receive fixed vol (buy the swap) and profit if realised vol exceeds the strike.

**Volatility hedge funds** often run a book of volatility swaps across multiple underlyings and tenors, looking for mean-reversion opportunities. When IV spikes (as it does after market shocks), dealers often quote volatility swaps wide. Sophisticated traders step in, pay fixed vol, and wait for volatility to normalise, realising profits as spreads compress.

**Risk managers and asset allocators** use volatility swaps to hedge portfolio volatility without taking a directional bet on the underlying stock or index. A portfolio manager holding a large equity long position can buy a volatility swap on that index as portfolio insurance: if the market sells off sharply, realised volatility rises, and the swap payoff offsets the portfolio loss.

**Single-stock traders** use them for hedging idiosyncratic volatility. A private equity firm holding a portfolio company might buy a volatility swap on the portfolio company's equity (if private equity shares can be traded); realised vol spikes if the company faces operational distress, and the swap hedges that uncertainty.

## Calculation and measurement challenges

Computing realised volatility is straightforward in principle but fraught with implementation details. Daily returns are calculated as log price changes, then annualised by multiplying by the square root of the number of trading days (usually 252 for equities). But every swap contract must specify:

- **Observation frequency**: Daily, hourly, every 5 minutes? This affects estimated vol; intra-daily sampling picks up more short-term noise.
- **Opening vs. closing prices**: Some use closing-to-closing returns; others use opening-to-closing or intra-day OHLC (open, high, low, close) ranges. Different methods give different realised vols.
- **Handling gaps and holidays**: If a market is closed, are those days counted? Are overnight gaps ignored?
- **Adjustment for dividends and splits**: Are price returns adjusted for dividends? Most modern swaps adjust for splits only, not dividend adjustments.

Dealers and indices (such as the [CBOE VIX](/implied-volatility/), which measures implied vol on the S&P 500) standardise these choices, but bilateral swaps require explicit negotiation. A difference in methodology can shift realised vol by 50–100 basis points.

## Volatility swaps versus variance swaps

Variance swaps pay on (realised vol)², not realised vol. This makes variance swaps more sensitive to extreme moves (a 50% daily move contributes (50%)² = 2,500 to the payoff, not just 50). Variance swaps replicate more naturally using options (because a delta-hedged short straddle earns the realised variance), so they are more liquid and easier to price.

But variance swaps are confusing: a 20% increase in realised volatility (from 15% to 18%) translates to a roughly 32% increase in variance (from 225 to 324), which is not intuitive.

A volatility swap's payoff is linear, intuitive, and practical for traders who think directly about volatility as an asset. The downside is that dealers hedge volatility swaps using variance swaps or straddles, not perfectly, so the economics are less efficient.

## Risks and failure modes

**Model risk**: Realised volatility depends heavily on the calculation method and observation frequency. A dealer quoting a strike might use one method (5-minute sampling), while the swap settles using a different method (daily closes), creating basis risk.

**Jump risk**: A single large move can dramatically increase realised volatility for a given period. An earnings surprise, a geopolitical shock, or a central bank decision can widen realised vol by 300+ basis points in a day. This is priced into the risk premium, but large jumps still surprise both counterparties.

**Counterparty credit risk**: If a dealer fails, the swap receiver (betting on high vol) may not recover the owed amount from the estate. [Counterparty risk](/counterparty-risk/) is elevated for long-dated swaps.

**Correlation between volatility and price**: Volatility swaps are supposed to be pure-volatility bets, but realised volatility is correlated with price movements (higher moves often lead to higher recorded volatility). This introduces hidden directional exposure that is not fully isolated by a simple volatility hedge.

## Variants and exotic structures

A **monthly reset volatility swap** pays and resets volatility monthly, creating a series of one-month volatility forwards. This allows traders to express views on volatility term structure.

A **corridor volatility swap** only counts days where the underlying stays within a band; realised volatility outside the corridor is ignored. This is used for hedging directional price moves while keeping volatility exposure.

A **leveraged volatility swap** multiplies the volatility exposure by a factor (e.g., 2× or 3×), amplifying gains and losses.

## See also

<div class="wiki-seealso">

### Closely related

- [Implied Volatility](/implied-volatility/) — Market expectations of future volatility, extracted from option prices.
- [Quanto Swap](/quanto-swap/) — A swap that swaps a foreign index while hedging currency exposure.
- [Dividend Swap](/dividend-swap/) — A swap exchanging fixed and realised dividend payments.
- [In-Arrears Swap](/in-arrears-swap/) — A swap where the floating rate is set at the end of each period.
- [Option Premium](/option-premium/) — The price paid for the right to buy or sell an asset.
- [Delta](/delta/) — The sensitivity of an option or portfolio to changes in the underlying price.

### Wider context

- [Forward Contract](/forward-contract/) — A bespoke agreement to exchange an asset at a future date and price.
- Derivative — An instrument whose value is derived from an underlying asset.
- [Market Risk](/market-risk/) — The exposure to losses from unfavourable price or rate moves.
- [Over-the-Counter Market](/over-the-counter-market/) — Decentralised market for bilateral derivatives.
- [Counterparty Risk](/counterparty-risk/) — The risk that the other party to a contract defaults.

</div>