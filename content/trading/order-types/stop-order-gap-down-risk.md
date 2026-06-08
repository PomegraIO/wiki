---
title: "Stop Order Gap-Down Risk"
description: "Why a stop order can execute far below the trigger price when a stock gaps down overnight, and how to measure and manage that slippage."
keywords:
  - stop order gap down risk
  - stop order slippage
  - gap down overnight
  - stop loss triggered below price
  - overnight gap risk
image: "/svg/trading.svg"
---

*A **stop order gap-down risk** occurs when a stock opens substantially below a trader's stop price, causing the order to execute at a much worse level than intended—sometimes 5–15% below the trigger. The problem arises because stop orders are not price guarantees; they become market orders once the stop price is touched, and a gap leaves no chance to execute at the stop level itself.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Stop Order Gap-Down Risk — key facts</div>

<img src="/svg/trading.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Stop orders become market orders during gaps, exposing traders to slippage far below the intended trigger.</div>

|   |   |
|---|---|
| **The risk** | Order executes at market open below the stop price by 5–15% or more |
| **When it happens** | Overnight earnings miss, geopolitical shock, or competitor announcement |
| **Why it happens** | Market order enters after gap; no intermediate prices to catch it |
| **Typical slippage** | 2–10% below stop price in single-stock; less in liquid ETFs |
| **Prevention** | Sell limit orders, widened stops, or tighter position sizing |
| **Measurement** | Historical gap frequency and magnitude for the stock class |

</aside>

## The mechanism: why stops become market orders

A stop order is a conditional directive to sell (or buy) once a stock hits a trigger price. The sequence is:
1. Trader sets stop at $100 on a $110 stock.
2. Stock trades down to $100 (the stop price is touched).
3. The stop **converts** to a [market order](/market-order/)—a live instruction to sell at any available price.
4. The market order executes at the best bid available *at that moment*.

If the stock trades down gradually—$110 to $105 to $100—the market order finds willing buyers near $100 and fills near the stop price. But if the stock gaps down overnight—$110 at close, $85 at open—the stop is triggered *before the market opens*. When trading resumes, the stock's first trade is $85. The market order queued overnight now executes against the $85 bid, not $100.

The trader wanted to cap losses at $100. Instead, the loss runs to $85—a 15% miss from the intended level.

## Why overnight gaps happen

**Earnings misses.** Company reports results after the close; revenue and profit fall short. The stock is halted from trading until the next morning. At the open, bad news has fully priced in, and the stock gaps down 10–20%.

**Acquisition or bankruptcy news.** A competitor acquires the company's largest customer overnight; the stock plunges 8% at the open.

**Macro shocks.** A central bank rate decision, a geopolitical crisis, or an FDA ruling hits outside market hours. Trading halts or resumes at a deeply gapped price.

**Liquidity dries up.** In thinly traded stocks or during fast market moves, ask prices may jump 5–10% from close to open, so even the first few trades execute far below yesterday's close.

These events are infrequent for large-cap stocks in normal markets but predictable *in aggregate*: any stock held long enough will eventually gap 5% or more.

## Quantifying slippage risk

To measure the expected gap size, traders review historical gap magnitude for the stock or asset class.

**Example: Single stock vs. index ETF.**
- A mid-cap tech stock that moves on earnings reports may have 1–3 gaps of 8%+ per year, and 8–12 gaps of 3%+ per year.
- An ETF tracking the S&P 500 rarely gaps more than 2% overnight (broader market shocks are rare), but it does gap 1–2% a few times per year.

If a trader runs a stop at $100 on a volatile stock, historical data might show a 5% gap happens once or twice annually. That implies a 1 in 250 chance of a gap that large on any given day. The expected loss, weighted by probability, might be:
- 98% of days: no gap, stop works fine.
- 2% of days: gap occurs, average loss is $5 (additional 5% slippage beyond the stop).
- Expected daily loss from gaps: 2% × $5 = $0.10 per $100 of capital, or 0.1% daily.

Over a year of holding the position, that sums to material exposure.

## How buyers and sellers use to manage the risk

**Sell limit orders instead of stops.** Rather than a stop order that converts to a market order, use a [sell limit order](/limit-order/)—an order to sell if the price falls to $100 or higher. If the stock gaps to $85, the limit order sits unfilled (the price never traded at $100). The trader keeps the position and losses continue, but avoids the spike of forced execution below $100. This trades the certainty of a gap loss for the risk of staying in a falling position.

**Widened stop prices.** Accept a 3–5% wider stop to reduce the chance of a gap triggering it. Set the stop at $97 instead of $100, cushioning against small overnight moves without requiring the trader to tolerate absurd slippage.

**Protective put options.** Buy a [put option](/put-option/) with a strike at or below the desired loss cap. If the stock gaps below the strike, the put holder has the right to sell at the strike price. Puts cost premium upfront but provide hard price floor. For a 1–3 month horizon, puts cost 1–3% of the stock's value, acceptable for traders who want gap protection.

**Reduce position size.** Trade a smaller position so that even a 5% gap loss stays within the trader's risk tolerance per position. Instead of a $100K position with a $100 stop (risking $5K on a 5% gap), run a $20K position (risking $1K on the same gap).

**Pre-market alerts or circuit breakers.** Some brokers allow traders to set alerts before the market opens; if a stock is indicated to open down 5%+, the trader can cancel the stop before the first trade prints. Not foolproof, but it catches obvious cases.

## Why stop orders remain popular despite the risk

Stop orders are simple, free, and align loss management with actual price movement in normal trading. They're the right tool for intraday trading where gaps are rare and stops are hit during normal hours. They also suit traders who want a hands-off mechanism—set a stop and walk away, trusting it will trigger if the thesis breaks.

The downside—gap risk—is a tail event that many traders underestimate. Many stock traders accept the gap as "part of the game" and use stops anyway, betting that gaps won't happen on their position.

## Market-wide gap behavior

**Large-cap indices** (S&P 500, Nasdaq 100) gap 2%+ overnight about 2–4 times per year; 5%+ gaps are rare (perhaps once per decade).

**Single-stock volatility** depends heavily on sector and market capitalization. Biotech stocks might gap 10%+ once or twice per quarter on clinical trial results. Blue-chip tech stocks gap 3–5% once or twice per year. Small-cap stocks gap more frequently; thinly traded micro-caps can gap 10%+ monthly.

**Forex and commodity gaps** vary widely. Major currency pairs (EUR/USD, USD/JPY) rarely gap more than 1% overnight because global forex trading runs 23 hours per day with overlapping sessions, but a shock during the single closed hour can produce a gap.

## See also

<div class="wiki-seealso">

### Closely related

- Stop Order — the mechanics of stop orders and their conversion to market orders
- [Market Order](/market-order/) — the type of order triggered after a stop is hit
- [Limit Order](/limit-order/) — alternative tool to cap losses without gap risk
- [Bid-Ask Spread](/bid-ask-spread/) — the spread that widens during gaps and affects execution price
- [Execution Risk](/execution-risk/) — broader category of slippage and order fill uncertainty
- [Protective Put](/protective-put/) — options-based hedge against gap downside

### Wider context

- [Volatility Smile](/volatility-smile/) — related concept about tail risk and extreme price moves
- [Value at Risk](/value-at-risk/) — framework for quantifying tail loss exposure including gaps
- [Support and Resistance](/support-and-resistance/) — price levels where stops cluster and gaps often break through
- [Market Cycle](/market-cycle/) — context for when gaps are more likely

</div>
