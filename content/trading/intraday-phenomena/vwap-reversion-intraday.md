---
title: "VWAP Reversion Intraday"
description: "Covers how prices frequently revert toward the daily VWAP after large deviations and why institutional algorithms reinforce this tendency."
keywords:
  - vwap reversion intraday
  - volume weighted average price
  - vwap trading strategy
  - mean reversion vwap
  - intraday price reversion
image: /svg/trading.svg
---

*The **VWAP reversion intraday** pattern reflects a tendency for stock prices to drift back toward their volume-weighted average price (VWAP) after sharp intraday moves—a tendency reinforced by algorithms that use VWAP as a benchmark for large execution, limiting order flow, and algorithmic trading that exploits deviations.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">VWAP Reversion — key facts</div>

<img src="/svg/trading.svg" alt="An abstract editorial mark for trading." />

<div class="wiki-infobox-caption">VWAP is a benchmark price, not a law; large deviations persist but tend to close over the trading session.</div>

|   |   |
|---|---|
| **VWAP definition** | Cumulative trade value ÷ cumulative share volume, reset daily |
| **Reversion timing** | Hours to full session close, not minutes |
| **Strength** | Stronger in liquid, heavily-traded assets; weaker in thin, speculative stocks |
| **Root cause** | Algorithmic execution benchmarking + order flow imbalances that reverse |
| **How to trade it** | Enter on large deviations; exit on reversion; size for bid-ask cost |
| **Risk** | Deviation can widen further; reversion is not guaranteed intraday |

</aside>

## What VWAP Is and Why It Matters

The **volume-weighted average price (VWAP)** is calculated as:

VWAP = Σ (Price × Volume) / Σ Volume

It accumulates throughout the trading session: the opening price and first trade of the day carry zero weight (VWAP is undefined until the first trade). By mid-morning, VWAP reflects trades from the open through mid-morning. By close, VWAP is the true volume-weighted average of the entire session's trading.

VWAP is critical infrastructure for institutional traders. A portfolio manager with a large order to buy 500,000 shares tries to execute near VWAP to demonstrate to clients that the order was filled at a "fair" price relative to the session average, not on a spike or dip. Many buy-side trading desks are evaluated on their ability to trade at or better than VWAP (called "VWAP target" or "VWAP-neutral" execution).

## Why Prices Revert to VWAP

The reversion pattern emerges from multiple feedback loops:

**Algorithmic benchmarking:** Sell-side broker algorithms that execute on behalf of large buyers are programmed to complete trades near VWAP. When a stock price rallies sharply above VWAP mid-session, it signals a shortage of sellers at reasonable prices. The algorithm pauses and waits for the price to retreat closer to VWAP before resuming. This creates a natural gravitational pull: as the algorithm withdraws buying interest, prices cool and drift back down.

**Order flow imbalance and reversal:** Large orders create transient imbalances. A wave of buy orders from a mega-fund pushes price up, but the selling that arrives to meet those buyers is not permanent price demand—it is simply the supply that was lurking at higher levels. Once that buy order wave completes, order flow rebalances and the price drift reverses.

**Profit-taking after deviations:** Intraday traders who bought into the rally take profits as the stock approaches local highs. This mechanical selling is not informed by fundamental news; it is pure technician behavior. As these traders exit, price gravitates back toward VWAP.

**Algorithmic mean reversion:** Some high-frequency and quantitative trading firms explicitly trade the VWAP reversion. They detect when price has deviated 2–3% above VWAP and lean into selling, accelerating the reversion. This, in turn, strengthens the gravitational pull.

## VWAP Reversion is Statistical, Not Mechanical

However, **VWAP reversion is not a law**. It is a statistical bias, stronger in some assets and sessions than others.

VWAP reversion is strongest in highly liquid, heavily-traded assets: mega-cap stocks like Apple, Microsoft, or the [S&P 500](/sp-500-index/) ETFs experience pronounced reversion because the sheer volume of algorithmic trading benchmarked to VWAP is enormous. A single $50 million order that deviates price 0.5% will face algorithmic selling and a flood of counter-flow.

Reversion is weaker in lower-volume stocks, micro-caps, or volatile small-caps. A stock rallying 5% on earnings surprise or an acquisition rumor may drift further away from VWAP because fundamental information, not just algorithmic order imbalances, is driving price. Deviations from VWAP driven by information can persist or widen further.

Similarly, reversion takes time—hours or a full session, not minutes. A stock that surges 2% in the first 30 minutes may take until late afternoon to revert. During that interim period, price can widen further if new information arrives.

## Practical Trading Implications

Traders exploit VWAP reversion by:

1. **Identifying large deviations early in the session:** Watching for price moves 1–2% away from VWAP within the first 1–2 hours, without supporting news.

2. **Entering against the deviation:** Shorting a stock that has rallied sharply above VWAP, or buying a stock that has plummeted below VWAP.

3. **Setting profit targets near VWAP:** A trader short above VWAP targets a close at or below VWAP; a trader long below VWAP targets a close at or above VWAP.

4. **Sizing for transaction costs:** The bid-ask spread and slippage must be smaller than the expected reversion. In a 1% deviation, the trader expects roughly 0.8–1% of price recovery; if spread and slippage consume 0.3%, the net edge is 0.5–0.7%, which may be insufficient to cover commissions and risk.

5. **Avoiding the afternoon trap:** Reversion often stalls in the final hour, especially before major news or Fed announcements. Traders close winners early and avoid holding into the close.

## Limitations and Risks

**Deviations can widen:** In choppy or volatile sessions, a stock oversold below VWAP may fall further before reverting. A leveraged trade short an oversold stock risks margin calls or forced liquidation.

**Information creates lasting deviations:** Earnings surprises, [credit events](/credit-event-sovereign/), or major technical breaks shift VWAP itself—reversion targets the (moving) VWAP, not a fixed level. A stock that gapped up on a merger announcement may trade well above the prior VWAP for the entire session; the "reversion" is to a new VWAP, not the old one.

**Liquidity evaporates in thin conditions:** During halt periods, news releases, or flash crashes, VWAP reversion trading is a losing proposition. Bid-ask spreads widen to 2–3%, and the expected reversion cannot pay for execution.

**Crowding weakens the trade:** If too many traders attempt VWAP reversion simultaneously, the feedback loop changes. What was a reliable reversion dynamic becomes a crowded, choppy battle as traders step on each other trying to exit the trade.

## See also

<div class="wiki-seealso">

### Closely related

- [Moving Average](/moving-average/) — related intraday price benchmarks
- [Support and Resistance](/support-and-resistance/) — related technical patterns
- [Market Order](/market-order/) — order type that affects VWAP
- [Limit Order](/limit-order/) — order type used to exploit VWAP deviations
- [Bid-Ask Spread](/bid-ask-spread/) — transaction cost that reduces VWAP reversion profit

### Wider context

- [Algorithmic Trading](/algorithmic-trading/) — drives VWAP benchmarking and reversion
- [Price Discovery](/price-discovery/) — how VWAP reflects true intraday pricing
- [Market Maker Trading](/market-maker-trading/) — institutions that create and exploit VWAP patterns
- Intraday Phenomena — broader patterns in same-day trading

</div>
