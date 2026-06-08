---
title: "VIX Futures Roll Yield"
description: "The persistent negative return from rolling long VIX futures positions, caused by the typical upward slope of the volatility term structure."
keywords:
  - VIX futures
  - roll yield
  - contango
  - volatility term structure
  - volatility hedging
image: "/svg/derivatives.svg"
---

*A **VIX futures roll yield** is the loss incurred when a trader closes a long [VIX futures](/futures-contract/) contract near expiration and opens a new one at a later expiration date, because near-term [VIX futures](/futures-contract/) typically trade at lower prices than longer-dated contracts. This structural drag is called "roll yield," and it is a persistent cost of holding long [VIX futures](/futures-contract/) as a [volatility hedge](/historical-volatility/).*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">VIX Futures Roll Yield — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract mark representing the flow of time and volatility curves." />

<div class="wiki-infobox-caption">The price of stability: paying to stay hedged.</div>

|   |   |
|---|---|
| **What it is** | Negative [carry](/derivatives-hedging/) from rolling long [VIX futures](/futures-contract/) as contracts expire |
| **Also called** | Roll cost, roll drag, [contango](/contango/) decay, term-structure bleed |
| **Root cause** | [VIX futures term structure](/futures-contract/) is usually upward-sloping ([contango](/contango/)) |
| **Magnitude** | Often 1–5% per roll, or 4–20% annualized for monthly rolls |
| **Duration** | Most acute in low-[volatility](/historical-volatility/) regimes; reverses in crisis |
| **Trader response** | [Variance swaps](/derivatives-hedging/), [VIX ETPs](/etf/), or outright [volatility](/historical-volatility/) [options](/option/) |

</aside>

## The term structure of volatility

[VIX futures](/futures-contract/) expire on defined dates (typically the third Wednesday of each month). Unlike [stock](/stock/) [futures](/futures-contract/), which converge toward the spot price as expiration nears, [VIX futures](/futures-contract/) converge to the realised [volatility](/historical-volatility/) of the [S&P 500](/sp-500-index/) over the final settlement period. This is important: the [VIX](/option/) itself is an index of implied [volatility](/historical-volatility/) from near-term [options](/option/) on the [S&P 500](/sp-500-index/), not a tradeable asset.

The **volatility term structure** is the curve of [VIX futures](/futures-contract/) prices across expirations. In normal times—low [volatility](/historical-volatility/), no imminent crisis—this curve is upward-sloping, a condition called [contango](/contango/). A [VIX futures](/futures-contract/) contract expiring in one month might trade at 15, the two-month contract at 16, and the three-month contract at 17. This reflects the market's expectation that [volatility](/historical-volatility/) will remain low for months ahead.

The upward slope is not arbitrary. It arises from the fact that [volatility](/historical-volatility/) mean-reverts. When [volatility](/historical-volatility/) spikes (usually during [market stress](/bear-market/)), traders expect it to fall back to long-term averages. [Options](/option/) traders, pricing longer-dated [options](/option/), incorporate this mean reversion: they charge a lower [implied volatility](/implied-volatility/) premium for longer maturities. [VIX futures](/futures-contract/) prices reflect these [implied volatilities](/implied-volatility/) and thus slope upward in tranquil periods.

## The cost of rolling

A portfolio manager holds [VIX futures](/futures-contract/) as a [hedge](/derivatives-hedging/) against a [stock market](/stock-market/) crash. To maintain the [hedge](/derivatives-hedging/), the manager must roll: as the front-month contract approaches expiration, they sell it and buy the next-month contract. Here's where the roll yield bites.

Suppose the one-month [VIX futures](/futures-contract/) trade at 15.00 and the two-month contract at 16.00. The manager closes the 15.00 contract and opens the 16.00 contract. They have immediately lost 1.00 point, or roughly 6.7%, on the roll alone—before any [market](/stock-market/) moves. If this cycle repeats monthly, the annualized drag is approximately 80%, even if realised [volatility](/historical-volatility/) remains flat.

This is the **negative roll yield**. It is not a [volatility](/historical-volatility/) loss; it is a structural cost of maintaining long [volatility](/historical-volatility/) exposure through [VIX futures](/futures-contract/). A [hedge](/derivatives-hedging/) is valuable only if the underlying [asset](/asset-allocation/) (the [stock market](/stock-market/)) declines and [VIX futures](/futures-contract/) gain. But if the [market](/stock-market/) remains stable and [volatility](/historical-volatility/) does not spike, roll drag erodes the entire [hedge](/derivatives-hedging/) position over time.

## When does the term structure invert?

[Contango](/contango/) is the default state, but **backwardation**—an inverted, downward-sloping curve—occurs during [market](/stock-market/) stress. When [volatility](/historical-volatility/) spikes (e.g., a sudden crash or unexpected headline), the current [VIX](/option/) jumps, but traders expect it to mean-revert quickly. The front-month [VIX futures](/futures-contract/) trade at elevated levels (30, 40, 50), while longer-dated contracts are lower (25, 20, 15). Now the curve is inverted.

A manager rolling from front to back contracts in backwardation gains on the roll—they sell high (the front contract) and buy low (the back contract). Over several days of turbulence, this positive roll yield can offset [stock market](/stock-market/) losses. This is precisely when the [volatility hedge](/historical-volatility/) is needed; unfortunately, [backwardation](/contango/) is brief, and [contango](/contango/) resumes once panic subsides.

## The empirical magnitude

Studies of [VIX futures](/futures-contract/) returns show a stark pattern. Over long periods (decades), the roll drag from [contango](/contango/) is substantial. A trader holding a constant long [VIX futures](/futures-contract/) position and rolling monthly would have lost 4–8% per year to roll drag alone in a typical low-[volatility](/historical-volatility/) environment, even if [volatility](/historical-volatility/) itself did not decline. This is why most [VIX ETPs](/etf/)—[exchange-traded products](/etf/) tracking [VIX](/option/) [futures](/futures-contract/)—underperform the [VIX](/option/) itself by this roll drag over time.

The magnitude of roll yield is not constant. It depends on the **slope** of the term structure—how steep the [contango](/contango/) is. In very quiet markets (e.g., summer doldrums), the slope is gentle; monthly rolls cost 0.5–1.5%. In [risk-off](/bear-market/) environments when [volatility](/historical-volatility/) remains elevated but contained, [contango](/contango/) steepens; rolls cost 2–5% per month. The steepest roll drags occur in specific scenarios: after a major volatility spike that the market expects to fade, or when near-term [options](/option/) are expensive relative to longer-dated [options](/option/) due to upcoming events.

## Why [contango](/contango/) persists

The intuition is risk-averse: [market makers](/market-maker-trading/) and [options](/option/) traders do not want to be short [volatility](/historical-volatility/). They would rather quote a higher price for longer-dated [volatility](/historical-volatility/) to compensate for carrying that exposure longer. Additionally, hedge funds and [corporations](/corporate-income-tax/) that buy [volatility](/historical-volatility/) [hedges](/derivatives-hedging/) are willing to pay a premium to lock in longer-dated protection. This demand tilts the term structure upward.

From a [mean reversion](/implied-volatility/) perspective, the curve's shape reflects the market's belief that current [volatility](/historical-volatility/) will normalize. Traders are implicitly betting that near-term shocks will settle, allowing [volatility](/historical-volatility/) to fall. Longer-dated contracts thus offer a higher implied [volatility](/historical-volatility/) to compensate for the long wait.

## Alternatives to long [VIX futures](/futures-contract/)

Given the persistent roll drag, institutional investors have developed alternatives:

**[Variance swaps](/derivatives-hedging/)** are [swaps](/derivatives-hedging/) on realised [variance](/historical-volatility/) over a period. Unlike [VIX futures](/futures-contract/), they do not suffer from term-structure drag; the payoff is determined solely by realised [volatility](/historical-volatility/). However, [variance swaps](/derivatives-hedging/) are [over-the-counter](/over-the-counter-market/), illiquid, and carry [counterparty risk](/counterparty-risk/).

**[Volatility options](/option/)** (e.g., [call options](/call-option/) on the [VIX](/option/)) directly express the bet on [volatility](/historical-volatility/) spike without the roll cost of [futures](/futures-contract/). However, [options](/option/) on [volatility](/historical-volatility/) are expensive; their [time decay](/time-decay-theta/) [theta](/delta/) is also negative, so they bleed value as time passes (unless [volatility](/historical-volatility/) rises).

**[Put options](/put-option/) on [equity indices](/sp-500-index/)** (the [S&P 500](/sp-500-index/)) are a traditional [hedge](/derivatives-hedging/) that avoids [VIX](/option/) altogether. A [portfolio manager](/mutual-fund/) buys [puts](/put-option/) on the [index](/sp-500-index/); if the [market](/stock-market/) crashes, the [puts](/put-option/) gain. [Put options](/put-option/) have positive [carry](/derivatives-hedging/) if bought out-of-the-money (you pay less [premium](/option-premium/)), though they also [time-decay](/time-decay-theta/). The [cost-benefit](/option-premium/) trade-off differs from [VIX futures](/futures-contract/).

**[Inverse ETFs](/inverse-etf/)** (e.g., -1x or -3x [leveraged](/leverage-ratio-forex/) [S&P 500](/sp-500-index/) trackers) provide direct [downside](/bear-market/) hedge but also carry daily rebalancing costs and are unsuitable for long-term holding.

## The practical lesson

Roll yield is not a reason to avoid [volatility](/historical-volatility/) [hedging](/derivatives-hedging/); rather, it is a cost to budget for. A [pension fund](/401k-plan/) that buys [VIX futures](/futures-contract/) as disaster insurance is essentially paying an annual insurance premium equal to the roll drag. If the [market](/stock-market/) crashes and the [hedge](/derivatives-hedging/) gains outweigh the roll cost, the trade succeeds. If the [market](/stock-market/) stays calm, the fund has paid for peace of mind—and that cost is real.

The term structure of [VIX futures](/futures-contract/) is not static; it changes daily as market expectations shift. A savvy [hedger](/derivatives-hedging/) monitors the slope, rolling when [contango](/contango/) is steep (roll cost is high) and refraining when [contango](/contango/) is flat or even inverted. Others accept the drag as an immutable cost of [hedging](/derivatives-hedging/), much as a homeowner pays [insurance](/auto-insurance/) premiums regardless of the weather.

## See also

<div class="wiki-seealso">

### Closely related

- [VIX](/option/) — the underlying [volatility](/historical-volatility/) index that [VIX futures](/futures-contract/) track
- [Futures Contract](/futures-contract/) — the mechanism through which [VIX](/option/) is traded
- [Contango](/contango/) — the upward-sloping term structure that drives roll drag
- [Volatility](/historical-volatility/) — the core concept [VIX futures](/futures-contract/) capture
- [Derivatives Hedging](/derivatives-hedging/) — why investors use [VIX futures](/futures-contract/) despite roll drag
- [Implied Volatility](/implied-volatility/) — reflected in [VIX futures](/futures-contract/) prices

### Wider context

- [Time Decay (Theta)](/time-decay-theta/) — related concept; [options](/option/) bleed value over time
- [Put Option](/put-option/) — alternative to [VIX futures](/futures-contract/) for [downside](/bear-market/) [hedge](/derivatives-hedging/)
- [Variance](/historical-volatility/) — related measure often used in [swaps](/derivatives-hedging/) as [hedge](/derivatives-hedging/) alternative
- [Mean Reversion](/implied-volatility/) — the economic force behind [contango](/contango/) in [volatility](/historical-volatility/) term structures
- [Bid-Ask Spread](/bid-ask-spread/) — additional transaction cost beyond roll yield
- [ETF](/etf/) — passive trackers of [VIX futures](/futures-contract/) are heavily impacted by roll drag

</div>
