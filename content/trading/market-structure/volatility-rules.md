---
title: "Volatility Rules"
description: "Trading restrictions and halts triggered when market prices or individual stocks experience unusually large, rapid movements."
---

*Volatility rules are designed to slow markets down during extreme price moves. When a stock jumps 10% in seconds, or when the entire market falls sharply, these rules can halt trading, cancel orders, or restrict trading to prevent panic selling. Like [circuit breakers](/wiki/circuit-breakers/), they give traders time to reconsider and [market makers](/wiki/market-makers/) time to adjust inventory.*

<div class="wiki-hatnote">
For systemwide halts on market declines, see <a href="/wiki/circuit-breakers/">/circuit-breakers/</a>. For halts on individual stocks due to news, see <a href="/wiki/trading-halts/">/trading-halts/</a>.
</div>

<aside class="wiki-infobox">
  <div class="wiki-infobox-title">Volatility rules — key facts</div>
  <table>
    <tr><th>Triggers</th><td>Large price movements, unusual volume, rapid execution</td></tr>
    <tr><th>Scope</th><td>Single stocks (volatility halts) or systemwide (circuit breakers)</td></tr>
    <tr><th>Response</th><td>Halt, order cancellation, trading pause, volatility auction</td></tr>
    <tr><th>Duration</th><td>5 minutes to 15 minutes, or end of day</td></tr>
    <tr><th>Goal</th><td>Prevent cascading forced sales; allow repricing</td></tr>
  </table>
</aside>

## Single-stock volatility halts

If a stock's price moves more than 10% in a five-minute window and there is no obvious news, the exchange may initiate a "volatility halt." The halt lasts 5 minutes (or longer if designated as a "Level 3" halt). The goal is to pause trading long enough for news to propagate and traders to understand what triggered the move.

A 10% move in five minutes is dramatic but can happen for legitimate reasons. A company might announce a merger, or a competitor might file for bankruptcy. The exchange confirms with the company that the news is real and material before resuming trading.

## Order quality filters

Before a volatility halt is formally declared, many exchanges trigger automated "order quality" filters. These filters are designed to catch obvious errors—trades that are clearly mispriced or outsized. A filter might auto-cancel an order to buy at a price 20% above the last traded price, assuming it's a typo.

These filters reduce the risk of a "flash crash"—a sudden spike or plunge in prices caused by errant orders, algorithms malfunctioning, or [market-making](/wiki/market-makers/) systems failing to keep up with velocity.

## Volatility auctions

Some exchanges use a "volatility auction" instead of a full halt. Instead of stopping trading, the exchange pauses for 30–60 seconds, aggregates all buy and sell interest at the current price, and finds a clearing price. The market reopens at that price, with reduced volatility because traders have had time to react.

The [volatility auction](/wiki/volatility-auction/) approach is becoming more common because it preserves some liquidity while still providing a repricing window.

## Post-halt price movement

When trading resumes after a volatility halt, the price often moves more sharply than it did before the halt. This is because the repricing has been delayed, and pent-up demand or supply floods the market. A stock that was halted while falling 10% might fall another 5% in the first minute after reopening as sell orders execute.

This can be jarring to investors, but it reflects the reality that the fundamental value has changed. The halt didn't prevent the repricing; it just postponed it.

## Circuit breakers vs. volatility halts

[Circuit breakers](/wiki/circuit-breakers/) are systemwide halts triggered by the level of the S&P 500 index. Volatility halts are single-stock halts triggered by individual stock price movements. The two work together: a [circuit breaker](/wiki/circuit-breakers/) halt pauses all stocks simultaneously, while volatility halts pause individual stocks based on their specific behavior.

## Criticisms

Critics argue that volatility rules are too blunt. A legitimate repricing (driven by new information) looks identical to a manipulative or error-driven move, at least in the first few seconds. By halting trading, the exchange prevents price discovery and can amplify volatility once trading resumes.

Supporters argue that the benefit of preventing a cascade of forced selling (from margin calls or [stop orders](/wiki/stop-order/)) outweighs the cost of a brief repricing delay.

## International volatility rules

European exchanges generally have similar volatility rules, though thresholds and halt durations vary. The Tokyo Stock Exchange has specific rules for large-cap and small-cap stocks, with smaller caps subject to more restrictive volatility halts.

Some exchanges distinguish between regular trading-hour volatility moves and opening or closing volatility, using different thresholds.

## Technological challenges

Modern electronic systems process trades at microsecond speeds, making it hard for volatility rules to react in time. A "flash crash" can move prices 5–10% in milliseconds, faster than a human observer can notice. Volatility-halt algorithms must run in real-time, triggering within milliseconds of the threshold breach.

The May 6, 2010 Flash Crash is the canonical case: the S&P 500 fell 9% and recovered within 36 minutes, primarily due to automated selling and buying by [algorithmic traders](/wiki/algorithmic-trading/). Afterward, the SEC and exchanges enhanced volatility-rule infrastructure to prevent recurrence.

## Future of volatility rules

There is ongoing debate about whether volatility rules should be stricter or lighter. Stricter rules (more halts, wider order-cancellation bands) would reduce extreme moves but might reduce legitimate trading. Lighter rules would preserve liquidity but risk another flash crash. The current system represents an uneasy equilibrium.

<div class="wiki-seealso">
<h2>See also</h2>
<h3>Closely related</h3>
<ul>
  <li><a href="/wiki/circuit-breakers/">Circuit breakers</a> — systemwide volatility protection.</li>
  <li><a href="/wiki/trading-halts/">Trading halts</a> — news-related halts on individual stocks.</li>
  <li><a href="/wiki/volatility-auction/">Volatility auction</a> — repricing mechanism during halts.</li>
</ul>
<h3>Wider context</h3>
<ul>
  <li><a href="/wiki/algorithmic-trading/">Algorithmic trading</a> — can trigger volatility moves.</li>
  <li><a href="/wiki/market-makers/">Market makers</a> — manage inventory during volatility.</li>
  <li><a href="/wiki/stock-exchange/">Stock exchange</a> — enforces volatility rules.</li>
</ul>
</div>
