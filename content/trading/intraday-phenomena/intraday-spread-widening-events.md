---
title: "Intraday Bid-Ask Spread Widening Events"
description: "Why bid-ask spreads spike sharply during news releases, macro data prints, and trading halts; and how market-maker incentives drive the widening."
keywords:
  - intraday bid ask spread widening
  - spread widening events
  - news release spreads
  - macro data impact spreads
  - trading halt resumption
image: "/svg/trading.svg"
---

*During certain recurring moments each trading day, **intraday bid-ask spread widening** occurs sharply: when scheduled economic data arrives, when earnings are announced, when trading halts resume, or when geopolitical shocks hit. **Intraday bid-ask spread widening events** happen because market makers face sudden uncertainty about fair value and withdraw liquidity; retail traders and algorithms are hit by worse fills, while patient limit-order traders can profit by crossing wider spreads.*

## Why Spreads Widen Under Uncertainty

A [market maker](/market-maker-trading/) quotes a [bid-ask spread](/bid-ask-spread/) based on her estimate of fair value, her [inventory risk](/execution-risk/), and her profit target. When uncertainty about fair value surges, the spread must widen to protect the market maker from being picked off.

Suppose you are a dealer in a stock. You have been quoting:
- **Bid:** \$100.00 (you buy at this price)
- **Ask:** \$100.10 (you sell at this price)
- **Spread:** 0.10%

Your quotes assume the stock's true value is around \$100.05, and you're comfortable holding it at this price. Then, the Federal Reserve announces a surprise interest-rate cut. The market reprices: the stock's fair value is now \$102. You don't want to sell at \$100.10 anymore; you immediately yank your quotes. When you requote, the spread has widened:

- **New bid:** \$101.80
- **New ask:** \$102.20
- **New spread:** 0.39%

The dealer is now protecting herself against the risk that the next trade is an informed trade: a buyer or seller who knows something about the repricing that she doesn't. The wider spread is insurance.

## Scheduled Events: The Predictable Widening Calendar

Certain data releases and corporate announcements occur on known schedules, creating recurring widening events:

### Jobs Reports and CPI Data

In the U.S., the Bureau of Labor Statistics releases unemployment and non-farm payroll data on the first Friday of each month, pre-market. CPI data arrives mid-month. These are the largest macroeconomic surprises for equity and [bond](/bond/) markets.

In the minutes before these prints:
- **Spreads narrow sharply** as traders and market makers position for the announcement. Volume picks up; the "crowd" expects volatility and wants to be flat.
- **After the data release**, spreads *widen dramatically*. If the jobs report beats expectations (jobs > forecasted), equities spike up. Market makers don't know if the move is half-done or fully-priced; they widen spreads to 2–5 times normal width.
- **Volatility spikes:** [Historical volatility](/historical-volatility/) rises instantly; [implied volatility](/implied-volatility/) follows. Algorithms and dealers reprice risk models.

A stock with a typical 0.5-cent spread may see spreads of 2–3 cents for 2–5 minutes after the print. Retail traders executing market orders during this window take much worse fills.

### Earnings Announcements

Public companies report quarterly earnings on fixed dates. The typical pattern:

1. **Pre-announcement:** Spreads tighten as positioning finalizes.
2. **Announcement moment:** Spreads widen to 3–10 times normal, depending on the stock's volatility and the magnitude of surprise.
3. **Volatility spike:** If earnings are a major miss, the spread can stay wide for 10–20 minutes until price discovery settles.

A \$200 stock with a 1-cent normal spread may see 5–10 cent spreads immediately post-earnings. An earnings surprise larger than one standard deviation (beat by >20%, for instance) keeps spreads wide longer.

## Trading Halt Resumption and Volatility Halts

Exchanges halt trading when large price moves occur very quickly (a 10% swing in <5 minutes, for instance) or when companies issue material news. The halt lasts 5–15 minutes, giving the market time to digest. Upon resumption:

- **Spreads explode:** Order flow is unknown. The market maker has no idea whether the halt triggered a wave of sell orders or buy orders. Spreads widen to 5–50 times normal.
- **First trade is volatile:** Often, the first trade post-halt is a large block at a vastly different price from the halt price.
- **Price discovery:** Over the next 5–10 minutes, the spread gradually narrows as the market finds a new equilibrium.

A small-cap stock halted at \$50.00 might resume trading with an initial bid of \$48.00 and ask of \$52.00 — a 4% spread — before settling at \$49.50 with a 0.5-cent spread 10 minutes later.

## Geopolitical Shocks and "Flash" Events

When unexpected geopolitical news hits — a war announcement, a sudden government intervention, a major corporate scandal — spreads widen instantly in all related securities:

- **Flight to safety:** Safe-haven assets (U.S. Treasuries, Swiss francs, gold) see tighter spreads as demand surges; risky assets see wider spreads as sellers emerge.
- **Systematic repricing:** Market makers in equities face uncertainty not just about individual stocks but about the entire risk landscape. They widen spreads across the board.
- **Liquidity dries up:** Some market makers withdraw entirely, reducing competition and widening spreads further.

During the 2008 financial crisis, normal 0.5-cent equity spreads routinely hit 1–2 dollars. During the March 2020 COVID-19 crash, spreads in large-cap stocks hit 5–10 cents.

## Market Maker Incentives: Adverse Selection and Inventory Risk

Two distinct incentives drive spread widening:

### 1. Adverse Selection (Bad-News Avoidance)

When new information arrives, the market maker faces a classic problem: is the next trade an informed trade (someone who knows something) or a random trade (liquidity-driven)?

If bad news arrives and spreads don't widen, informed sellers will hit the bid, buying the market maker's inventory at stale prices. The market maker loses money. By widening the spread, she makes it expensive for informed traders to cross, protecting herself.

The wider the expected quality of incoming order flow, the wider the spread must be to compensate for adverse selection risk.

### 2. Inventory Risk (Repricing Risk)

When fair value becomes uncertain, holding inventory becomes risky. A market maker long 10,000 shares at \$100.05 faces potential loss if the stock reprices to \$98 in the next hour. To offset this risk, she widens spreads, either to avoid taking more inventory or to extract higher profits from each trade to compensate for holding risk.

Over time, as volatility subsides and information is digested, spreads narrow again as dealers feel safer about their inventory positions.

## Timing the Widening: Predictable Patterns

Certain intraday widening events are forecastable, allowing savvy traders to avoid the worst fills:

| Event | Time (ET) | Typical Spread Widening | Duration |
|-------|-----------|------------------------|----|
| **Jobs report (1st Fri)** | 8:30 AM | 3–8x normal | 5–30 min |
| **CPI data (mid-month)** | 8:30 AM | 2–5x normal | 5–15 min |
| **Fed funds decision (8x/year)** | 2:00 PM | 2–6x normal | 10–20 min |
| **Earnings announcement** | 4:00–4:30 PM (after-hours) | 5–15x normal | 10–40 min |
| **Trading halt resumption** | Variable | 5–50x normal | 5–10 min |
| **Market open (9:30 AM)** | 9:30–9:45 AM | 2–3x normal | 15 min |
| **Market close (4:00 PM)** | 3:55–4:00 PM | 1.5–2x normal | 5 min |

A retail trader checking the schedule knows that buying at 8:35 AM on jobs report Friday will incur worse spreads than buying at 8:45 AM. Delaying execution by 15–20 minutes is often cheaper than paying the event-driven spread premium.

## Volatility-Driven Widening and Self-Reinforcement

Spread widening can be self-reinforcing:

1. **Spreads widen** (due to information uncertainty).
2. **Retail traders get worse fills**, inducing some to cancel orders or switch brokers.
3. **Liquidity evaporates**, spreading further.
4. **Algorithms that use bid-ask as a signal** interpret wider spreads as higher risk and withdraw liquidity-providing orders.
5. **Spreads widen more.**

This feedback loop is why spreads in some stocks can remain elevated for 20–30 minutes after a shock, even after new information is widely known. Dealers and algorithms are waiting for competitors to step in and quote tighter; when they don't, patience wears out and spreads reset.

## Comparison: Spread Width by Event Type

| Event type | Triggers widening? | Speed of normalization | Typical relative spread | Notes |
|------------|-------------------|------------------------|---|---|
| **Scheduled macro data** | Yes, sharp | 5–30 min | 3–8x | High predictability |
| **Earnings surprise** | Yes, if large | 10–40 min | 5–15x | Depends on surprise magnitude |
| **Trading halt** | Yes, very sharp | 5–15 min | 10–50x | Most dramatic event |
| **Geopolitical shock** | Yes, sustained | 30 min–2 hours | 2–10x | Spreads stay wide if news is evolving |
| **Illiquid small-cap news** | Yes | 1–8 hours | 0.5–5% | Can be permanent re-widening if demand shifts |
| **Analyst downgrade** | Modest | 5–20 min | 1.5–3x | Depends on degree of surprise |

## Strategies to Avoid Widening Cost

Traders seeking to minimize spread costs during widening events use several tactics:

- **Use limit orders:** Quote a willing price and wait for a cross. Avoids the market-order penalty.
- **Delay execution:** If you can wait 20–30 minutes, do so. Spreads normalize quickly once the uncertainty passes.
- **Split orders:** Spread your buy/sell over several minutes or hours to reduce the market impact and opportunity for market makers to widen further.
- **Trade less-affected sectors:** During equity shocks, spreads in bonds and commodity ETFs may remain tighter than equities.
- **Monitor the volatility calendar:** Know upcoming data releases and avoid aggressive execution immediately before/after.

## See also

<div class="wiki-seealso">

### Closely related

- [Bid-Ask Spread](/bid-ask-spread/) — the core spread that widens during these events
- [Market Maker](/market-maker-trading/) — the dealer whose inventory and repricing decisions drive the widening
- [Implied Volatility](/implied-volatility/) — often spikes in concert with spread widening
- [Historical Volatility](/historical-volatility/) — the realized volatility that justified the widening
- [Liquidity Risk](/liquidity-risk/) — why spreads widen: liquidity evaporates under uncertainty
- [Limit Order](/limit-order/) — the patient order type that can exploit widened spreads

### Wider context

- [Consumer Price Index](/consumer-price-index/) — a key economic data release that triggers widening
- [Federal Funds Rate](/federal-funds-rate/) — central bank decisions that drive macro-event widening
- Trading Cost — the broader category; widening events are a major intraday cost driver
- [Market Order](/market-order/) — most vulnerable to widening; executed at worst available prices
- [Execution Risk](/execution-risk/) — the uncertainty about execution price and size, evident during widening

</div>
