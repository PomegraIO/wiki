---
title: "Volatility Index Futures"
description: "Derivatives contracts based on measures of market volatility, especially the VIX—allowing traders and funds to hedge market risk, speculate on fear, and diversify portfolios."
---

*Equity markets have the S&P 500. Volatility has the VIX. The Volatility Index captures the market's near-term expectation of stock price swings. Traders and funds use VIX [futures](/wiki/futures-contract/) to bet on whether the market's own fear is overblown.*

## What the VIX measures

The VIX is an index of [implied volatility](/wiki/implied-volatility/) derived from [S&P 500](/wiki/sp-500-index/) index [options](/wiki/option/). It measures the market's expectation of 30-day stock market volatility, expressed as an annualized percentage.

A VIX of 15 means the market expects annual volatility of 15%—relatively calm. A VIX of 40 means annual volatility of 40%—turmoil. The VIX is sometimes called the "fear index" because it tends to spike when markets are stressed (March 2020 crisis, April 2020 crash, bad Fed days). It tends to be low when markets are complacent.

## VIX futures: the instrument

The CBOE publishes [futures contracts](/wiki/futures-contract/) on the VIX with monthly expirations, typically covering 9-10 months into the future. Each contract is notional: it does not physically deliver volatility (volatility is intangible). Instead, it settles in cash to the settlement value of the VIX on the contract's [expiration date](/wiki/expiration-contracts/).

A trader long one VIX December contract is betting that realized volatility over the next month will exceed what the option market is currently pricing into that December contract. If the VIX jumps to 50 on settlement day and the trader's VIX contract was struck at 20, the trader profits: $250 per VIX point (the notional multiplier), or $7,500 on the $5,000 move.

## Hedging equity exposure with VIX futures

The VIX tends to spike when equities fall. A portfolio manager holding a large equity position faces downside risk. Buying VIX [futures](/wiki/futures-contract/) provides a hedge: if markets crash and equities fall 20%, the VIX likely spikes to 40-50, and the long VIX futures position offsets equity losses.

This is economically similar to buying [put options](/wiki/put-option/) on equities, but cheaper in many environments. Put options are expensive in low-volatility regimes (the VIX is in the teens), charging you upfront premium. VIX futures allow you to enter a long position without paying explicit premium, though you accept [contango](/wiki/contango/) costs (as we'll see below).

## The VIX term structure: contango and constraints

VIX [futures](/wiki/futures-contract/) almost always trade in [contango](/wiki/contango/): far-month contracts trade at higher VIX levels than near-month contracts. If the spot VIX is 20, the March VIX futures might trade at 22, and the June at 24. This reflects the market's expectation of mean reversion: near-term volatility will be elevated (the spot VIX is high), but longer-term volatility will be lower and more stable.

This [contango](/wiki/contango/) creates costs for hedgers:

- A portfolio manager buys December VIX at 24 to hedge equity downside.
- If the VIX falls to 16 in December and then rallies to 25, the manager's hedging economics are mixed: the equity position suffered from the 16 level, but the VIX futures had time decay from 24 to 16.
- When the manager rolls the hedge into new VIX contracts, they must buy at the new contango levels, further reducing hedge efficiency.

The [contango](/wiki/contango/) in VIX futures is not arbitrary; it reflects the fact that the option market is constantly pricing out near-term uncertainty. A spike in the spot VIX is usually temporary; the market's pricing of longer-term uncertainty is more stable.

## VIX futures for speculation

Traders also use VIX [futures](/wiki/futures-contract/) to bet on volatility moves directly, independent of stock prices. Some scenarios:

- **Earnings season:** Traders might buy front-month VIX futures weeks before earnings, betting that realized volatility will spike above the option market's pricing. If earnings beats are wide, individual stocks whipsaw, and realized volatility exceeds implied, the bet pays.
- **Interest rate expectations:** Fed decision days create volatility spikes. A trader might buy VIX futures ahead of a Fed announcement, betting the surprise will boost volatility above current pricing.
- **Regime shifts:** A trader believing the market is about to shift from calm to turbulent (e.g., geopolitical shock, economic shock) can buy back-month VIX futures, betting the pricing will shift upward over time.

These bets are pure volatility plays, orthogonal to stock price direction. A trader can be right about volatility direction and wrong about stock prices, or vice versa.

## VIX futures curve mechanics

The VIX futures curve is traded actively. Traders execute calendar spreads:

- **Buy near, sell far:** Betting the [contango](/wiki/contango/) will flatten, or that near-term volatility spikes.
- **Buy far, sell near:** Betting [contango](/wiki/contango/) will steepen, or that the spot VIX will crash while longer-term expectations persist.

The spreads are cheaper to trade (lower margin, tighter bid-ask) than outright VIX futures, because they isolate curve risk, not directional volatility risk. They are useful for traders who have a view on curve shape but not absolute volatility levels.

## Structural challenges and limitations

VIX [futures](/wiki/futures-contract/) have quirks:

**Mean reversion and mean eversion:** The VIX has a long-term average around 15-18. Over long periods, it tends to revert to this mean. A trader long VIX futures betting on sustained high volatility faces powerful mean reversion headwinds. Most volatility spikes are temporary.

**Liquidity and [basis](/wiki/basis/) risk:** VIX futures liquidity is concentrated in front months. Back-month VIX contracts are thin. A hedger needing to hedge 6+ months out faces liquidity challenges and wide [bid-ask spreads](/wiki/etf-bid-ask-spread/).

**Spot VIX jumps:** The spot VIX can gap sharply overnight (e.g., overnight geopolitical shock before markets open), but VIX futures have defined [expiration dates](/wiki/expiration-contracts/) with no gapping. This creates [basis](/wiki/basis/) risk: the spot VIX may jump to 50, but VIX futures have already settled or are illiquid.

**Convexity of realized vs. implied:** VIX futures settle to implied volatility, but hedgers care about realized volatility. A sharp, quick market crash (low realized volatility) might not raise the VIX much. A slow, grinding decline (high realized volatility) might raise it more. A hedger using VIX futures may find the hedge is uncorrelated with their actual losses.

## VIX ETFs and leveraged products

Retail investors often access VIX via [ETFs](/wiki/etf/) and [inverse ETFs](/wiki/inverse-etf/) that hold VIX [futures](/wiki/futures-contract/) internally. Most VIX ETFs hold near-month contracts and roll them as expiration approaches, exposing investors to [contango](/wiki/contango/) decay. This is why VIX ETFs often underperform the spot VIX index over long periods: they are paying the structural [contango](/wiki/contango/) cost.

[Inverse VIX ETFs](/wiki/inverse-etf/) bet against volatility spikes, profiting when the VIX falls. They face similar [contango](/wiki/contango/) drag in opposite form: when VIX rises and then reverts, the ETF profits on the revert but loses on the upward spike. Over long periods with mean reversion, these products can deliver positive returns, but they are designed for tactical use, not buy-and-hold.

<div class="wiki-seealso">
<h2>See also</h2>
<h3>Closely related</h3>
<ul>
<li><a href="/wiki/implied-volatility/">Implied volatility</a> — the market's expectation of future price swings, which the VIX measures.</li>
<li><a href="/wiki/futures-contract/">Futures contract</a> — the vehicle enabling VIX derivatives trading.</li>
<li><a href="/wiki/put-option/">Put option</a> — an alternative way to hedge equity downside, often compared to VIX futures.</li>
<li><a href="/wiki/contango/">Contango</a> — the persistent upward-sloping VIX curve, creating costs for long VIX holders.</li>
<li><a href="/wiki/basis/">Basis</a> — the gap between spot VIX and VIX futures, which can widen during stress.</li>
<li><a href="/wiki/inverse-etf/">Inverse ETF</a> — retail products betting against volatility or broader market declines.</li>
</ul>
<h3>Wider context</h3>
<ul>
<li><a href="/wiki/option/">Option</a> — overview of how options market pricing drives the VIX.</li>
<li><a href="/wiki/derivatives/">Derivatives</a> — the broader category of risk-transfer instruments.</li>
</ul>
</div>
