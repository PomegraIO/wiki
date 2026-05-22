---
title: "Circuit Breaker Halt"
description: "Automatic trading halts triggered by extreme price movements, designed to prevent panic selling and allow orderly price discovery."
keywords:
  - circuit breaker
  - trading halt
  - price limits
  - market circuit breaker
  - circuit-breaker-halt
---

*A **circuit breaker halt** is an automatic market-wide trading pause triggered when a major index (like the S&P 500) falls a certain percentage in a single day. Halts last 15 minutes, giving investors time to reassess and cooling panic selling. They are a direct response to the 1987 crash and designed to prevent free-fall.*

<aside class="wiki-infobox">

| Level | S&P 500 Decline | Duration | Status |
|-------|-----------------|----------|--------|
| **Level 1** | 7% | 15-min halt | Market-wide |
| **Level 2** | 13% | 15-min halt | Market-wide |
| **Level 3** | 20% | Close for day | End of session |
| **Timing** | 9:30am–3:55pm ET | Applies during trading hours | Current rule (2020) |

</aside>

## The 1987 crash and birth of circuit breakers

On October 19, 1987, the S&P 500 fell 20% in a single day—the largest one-day percentage drop in stock market history. [Panic selling](/wiki/capitulation-selling/) overwhelmed buyers, price discovery collapsed, and markets nearly spiraled. Margin calls forced more selling, creating a self-reinforcing loop. The crash prompted the SEC to overhaul market structure. The solution: circuit breaker halts would pause trading during extreme moves, break the selling momentum, and allow traders time to reassess.

The original circuit breakers (implemented in 1988) were tied to point drops (250 points on the Dow). Over time, these were replaced with percentage-based triggers (1997 reform) on the S&P 500, deemed more robust as indexes grow. The current rules (established in 2020 and periodically reviewed) use Level 1, 2, and 3 halts tied to 7%, 13%, and 20% declines.

## How a halt works: mechanics and timing

When the S&P 500 drops 7% before 3:25pm, the entire U.S. equities market (stocks, ETFs, options) halts for 15 minutes. No trades execute. After 15 minutes, trading resumes. If the market has stabilized or risen, trading continues normally. If the S&P 500 falls another 13% from opening (or 6% from the 7% trigger), a Level 2 halt occurs, again pausing 15 minutes.

If the market falls 20% from opening, the Level 3 halt closes the market for the day (unless the decline happens after 3:25pm, in which case trading closes normally at 3:30pm). This "circuit breaker" structure (three levels, ascending restrictions) is designed to give three opportunities for orderly closure before panic becomes unmanageable.

The 15-minute pause is deliberate. It is long enough to break momentum and allow traders to reassess, but short enough that it is not a market-closing signal (that would trigger panic selling into the halt). During the halt, traders can place orders and think; no one is forced to sell.

## International variations and copycat rules

Other major markets adopted circuit breakers. The UK (FTSE 100), Japan (Nikkei), and Korea (KOSPI) have similar rules. The mechanics vary: some use index-level triggers, others use sector triggers. The EU uses volatility auctions (when volatility spikes, trading pauses briefly instead of halting entirely, allowing electronic auctions to establish equilibrium prices before resumption).

Cryptocurrency markets, largely unregulated, have no circuit breaker halts, leading to extreme intraday swings. Bitcoin has fallen 20% in an hour with no pause, amplifying panic. Some [crypto exchanges](/wiki/cryptocurrency-exchange/) have voluntarily implemented circuit breaker-like mechanisms (trading pauses after 10% moves), but these are optional and vary by exchange.

## Empirical effectiveness: mixed findings

Circuit breakers succeed in their primary goal: preventing free-falls. Since 1988, a 20%-decline day has occurred only a handful of times (March 2020 COVID crash came close, with Level 1 and 2 halts triggering). When halts were tested, trading did resume and markets often stabilized without further collapse.

However, halts create distortions. During a halt, traders cannot execute, so order imbalances build up. When trading resumes, a flood of sell orders can execute at unfavorable prices, creating a gap down. Some researchers argue this "reopening shock" can worsen losses for traders stuck in positions. Others counter that 15 minutes is enough for news interpretation and new orders to form, largely offsetting this effect.

A key debate: do circuit breakers prevent real economic adjustment (price discovery), or do they simply delay it? If a company's economic value has genuinely fallen 20% (major event, sudden loss of assets), does a 15-minute pause help, or does it just defer the adjustment? Evidence suggests halts help during pure panic (when prices overshoot on fear alone), but do not prevent adjustment during fundamental shocks.

## Algorithmic trading and low-volatility periods

Modern circuit breakers face a new challenge: algorithmic and high-frequency trading. In low-volatility periods, algorithms trade on tiny price differences across venues. If a halt occurs, algorithms that were hedged (long on one exchange, short on another) are suddenly unhedged, and losses can mount during the pause. Some researchers have argued that circuit breakers should be more granular (halt individual securities instead of the entire market) in the age of fragmented markets and algorithmic trading.

The SEC has repeatedly reviewed circuit breaker rules and generally kept them intact, arguing that they continue to serve their purpose. The 2020 review (after the March 2020 volatility) proposed no major changes, suggesting confidence in the current framework.

## When halts cannot help: after-hours and international markets

Circuit breakers apply only to official trading hours (9:30am–4pm ET for U.S. equities). Trading in [after-hours markets](/wiki/after-hours-trading/) is not subject to halts and can experience extreme volatility (often lower volume, wider spreads). Major news (earnings misses, CEO departures, geopolitical shocks) that hits after close can gap down open the next day with halts not preventing the initial shock.

International investors face fragmentation. A stock trading on both NYSE and exchanges in Tokyo, London, and Frankfurt can experience circuit breaker halts in different markets at different times, creating temporary arbitrage opportunities but also confusion.

## Psychological effects and trader behavior

Some evidence suggests that circuit breaker halts reduce panic by giving traders a forced pause. The 15-minute timeout allows emotional traders to step back, reflect, and revise their strategies. Longer-term traders might use the halt to double-check their thesis. This psychological effect is hard to quantify but is valued by market structure advocates.

Others argue that in an age of instant information and automated algorithms, the 15-minute pause is outdated. Information is fully incorporated within seconds, and a 15-minute halt delays nothing. These critics argue the rules are security theater—they comfort politicians and the public but add little practical benefit.

## Future of circuit breakers

As markets evolve (decentralization, global 24/7 trading, DAO-based protocols), the circuit breaker model may be challenged. DeFi platforms (decentralized exchanges) cannot halt trading; they are smart contracts running 24/7. Some argue this is a feature (no artificial pauses), others argue it is a bug (no circuit breaker protection).

Regulators continue to monitor and adjust. The SEC's 2020 review kept the 7%-13%-20% structure in place, deeming it appropriate. But if volatility patterns shift (more frequent extreme moves), rules may be revisited.

<div class="wiki-seealso">

### Closely related
- [Circuit Breaker](/wiki/circuit-breaker/) — Automatic trading halt mechanism
- [Trading Halts](/wiki/trading-halts/) — Temporary pause in trading a security
- [Panic of 1987 (Black Monday)](/wiki/black-monday-1987/) — Historic crash prompting circuit breaker adoption

### Wider context
- [Flash Crash 2010](/wiki/flash-crash-2010/) — Extreme intraday decline that triggered circuit breakers
- [Market Impact Cost](/wiki/market-impact-cost/) — Cost of large trades moving prices
- [Algorithmic Trading](/wiki/algorithmic-trading/) — Automated trading in electronic markets

</div>
