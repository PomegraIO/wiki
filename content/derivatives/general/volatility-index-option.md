---
title: "Volatility Index Option"
description: "Derivatives contracts on the VIX measuring expected 30-day equity market volatility."
keywords:
  - vix options
  - volatility derivatives
  - index options
  - fear index
  - implied volatility
  - hedging
---

*A **Volatility Index Option** (or VIX option) is a derivative contract on the [VIX](/wiki/fear-index/), a measure of expected 30-day equity market volatility. Traders use VIX options to hedge portfolio risk, speculate on volatility spikes, or profit from changes in market fear expectations.*

<aside class="wiki-infobox">

| Element | Detail |
|--------|--------|
| **Underlying Index** | VIX (CBOE Volatility Index) |
| **Contract Multiplier** | 100 × VIX index level |
| **Expiration** | Monthlies + weeklies, typically 30 days |
| **Exercise** | European-style (exercise only at expiration) |
| **Strike Range** | 5–200+ points, wide intervals |
| **Pricing** | Based on volatility of volatility (meta-hedge) |
| **Exchange** | CBOE (Cboe Options Exchange) |
| **Cost** | Can be expensive due to underlying volatility |

</aside>

## The VIX as underlying

The [VIX](/wiki/fear-index/) is not a stock. It's an index calculated from [S&P 500](/wiki/sp-500-index/) option prices, measuring the implied volatility the market expects over the next 30 days. A VIX of 15 means the market expects relatively calm trading; a VIX of 40 signals panic and expected sharp moves.

Options *on* the VIX let traders bet on changes in this expectation. If you believe the market will calm down, you might buy a VIX call at a 20 strike, hoping the VIX falls below 20 and the option expires worthless (you profit). If you expect a crash, you buy a VIX call, banking on the VIX spiking to 35+.

## Why they're difficult to trade

VIX options are notoriously tricky:

- **Volatility of volatility:** The VIX itself is volatile. Predicting whether it will be 18 or 22 in 30 days is harder than predicting a stock price move.
- **Bid-ask spreads:** Lower trading volume than equity options means wider spreads and higher execution costs.
- **Contango decay:** [VIX futures](/wiki/volatility-index-futures/) roll into contango (later months cost more), meaning value decays over time if volatility doesn't spike. Holding a VIX call long-term bleeds value through contango.
- **Mean-reversion trap:** Extreme VIX levels (very high or very low) naturally revert. A VIX of 50 tends to settle back to 18, creating a headwind for long volatility positions.

## Hedging a portfolio with VIX calls

Portfolio managers often buy out-of-the-money VIX calls as insurance. Example:

- Manage a $10 million portfolio of stocks and bonds.
- Buy 10 contracts of VIX 25 calls (30-day expiration) for $2,000.
- If the market crashes and VIX spikes to 35, the calls are worth ~$100,000, offsetting losses in the stock portfolio.
- If the market stays calm and VIX ends at 12, the calls expire worthless and you lose the $2,000 premium.

This is classic portfolio insurance. It's expensive (the premium is a cost) but limits downside in a crisis. The question is whether the insurance cost is worth the peace of mind.

## Contango and the rolling problem

A structural challenge with VIX options is [contango](/wiki/contango/): longer-dated VIX futures typically trade higher than near-term futures, even though they all reference the same underlying index. This creates a drag on long volatility positions.

A trader who buys a 60-day VIX call at 20 and holds it rolling over 30 days (into the next month's contract) may experience decay as the newer contract is more expensive. Over time, this "roll yield" can erode returns, especially if realized volatility doesn't match implied.

## Spread strategies: long vs. short volatility

Rather than outright calls or puts, traders often use spreads:

- **Bull call spread:** Buy VIX 20 call, sell VIX 25 call. Bet on moderate volatility increase; defined risk and reward.
- **Bear call spread:** Sell VIX 15 call, buy VIX 20 call. Bet that VIX stays below 20; collect premium upfront.
- **Iron condor:** Sell OTM calls and puts, cap risk with long calls/puts further out. Profitable if VIX stays range-bound.

Spreads reduce the premium cost but also cap profit. They're favored by traders skeptical that the market will deliver the extreme moves that justify long-volatility premiums.

## Seasonal and sentiment patterns

VIX options exhibit seasonal patterns:

- **Pre-earnings:** Implied volatility in VIX options rises before major earnings seasons; decay is steeper.
- **Post-crisis:** After a market crash, volatility spikes, then mean-reverts quickly. VIX calls bought during the spike often expire worthless within 2–4 weeks as calm returns.
- **Fed uncertainty:** VIX options tend to be more active and volatile around Federal Reserve rate decisions.

Sophisticated traders study these patterns to time VIX option entry and exit.

## Comparison to VIX futures

[VIX futures](/wiki/volatility-index-futures/) are often compared to VIX options:

- **Futures:** Linear payoff; more liquid; simpler to trade; subject to margin calls.
- **Options:** Capped downside for long positions; premium cost upfront; more complex pricing; wider spreads.

Many hedge funds use a mix: VIX futures for tactical bets, VIX call spreads for defined-risk insurance.

## Tax and accounting considerations

VIX options settle in cash (not physically deliverable). Profits are realized when the position is closed or expired. Under Section 1256 treatment (in the US), VIX options are treated like [index options](/wiki/option/), subject to the 60/40 long-term capital gains rule: 60% of gains taxed as long-term, 40% as short-term, regardless of holding period. This is more favorable than ordinary short-term capital gains (37% top rate).

## Real-world case: 2020 volatility crash

In March 2020, the VIX spiked from 20 to 82 as equity markets crashed. VIX call owners profited handsomely. But by mid-April, the VIX had settled back to 30, and by summer, to 15. A trader who bought 90-day VIX 50 calls in March at $2,000 each might have been up $5,000–$10,000 within a week, but without exit discipline, would have watched the gains evaporate over the following month as the VIX mean-reverted. This illustrates the challenge: capturing the volatility spike without holding too long.

<div class="wiki-seealso">

### Closely related
- [VIX / Fear Index](/wiki/fear-index/) — The underlying measure
- [Volatility Index Futures](/wiki/volatility-index-futures/) — Futures on the same index
- [Option](/wiki/option/) — General derivatives mechanics
- [Implied Volatility](/wiki/implied-volatility/) — Pricing input for VIX options
- [Call Option](/wiki/call-option/) — Basic options contract

### Wider context
- [Portfolio Insurance](/wiki/portfolio-mental-accounting/) — Hedging framework
- [Derivatives](/wiki/derivatives-exchange-crypto/) — Broader class of contracts
- [Risk Management](/wiki/risk-parity-strategy/) — Use case for volatility hedging
- [Market Crashes](/wiki/flash-crash-2010/) — Scenarios where VIX spikes
- [Contango](/wiki/contango/) — Structural drag on volatility trading

</div>
