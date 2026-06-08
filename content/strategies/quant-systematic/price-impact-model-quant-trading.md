---
title: "Price Impact Models in Quantitative Trading"
description: "Understand how linear and square-root price impact models estimate slippage costs in large orders and reconcile backtest returns with real trading results."
keywords:
  - price impact model quant trading
  - market impact cost quantitative trading
  - square root impact model
  - linear price impact
  - slippage quantitative trading
  - execution cost modeling
image: /svg/strategies.svg
---

*A **price impact model** is a quantitative formula that estimates how a trader's large order moves prices and degrades realized returns relative to paper backtests. The two most common models—linear and square-root—capture the empirical reality that bigger orders face proportionally worse execution prices, and systematic traders use these models to adjust position sizing and entry/exit logic.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Price Impact Models in Quant Trading — Key Facts</div>

<img src="/svg/strategies.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Price impact models bridge the gap between backtested returns and actual execution by quantifying the cost of moving the market.</div>

|   |   |
|---|---|
| **Purpose** | Estimate the cost (slippage) of executing large orders relative to mid-market price |
| **Linear model** | Impact = constant × order size (simplest, assumes flat cost per share) |
| **Square-root model** | Impact ∝ √(order size) (empirically closer to reality; cost rises sublinearly) |
| **Key input** | Daily trading volume; models assume impact scales with order size relative to volume |
| **Typical impact** | 0.5–2 basis points per $1M order in liquid stocks; 10–100+ bps in illiquid names |
| **Application** | Adjust position sizing, set entry/exit limits, account for transaction costs in backtests |

</aside>

## Why Price Impact Matters in Quantitative Trading

When a systematic trader places a large order—say, $10 million to buy a stock—the market doesn't absorb it at a single price. As the [order](/market-order/) is filled, supply dries up at the best [bid-ask spread](/bid-ask-spread/), and the trader is forced to buy at progressively higher prices from deeper in the order book. This movement of the price is **price impact** or **market impact**, and it is a real, measurable cost that doesn't appear in simple backtests.

Retail backtests often assume unlimited [liquidity](/liquidity-risk/)—that a trader can buy or sell any size at the mid-market price with no spread or slippage. This is fantasy. In reality, the largest orders move prices by basis points or worse, especially in less liquid stocks. A strategy that backtests to 15% annual returns might deliver 8% after impact, because the strategy's own trading is its worst enemy: every entry moves the price against it, and every exit does the same.

Quantitative traders use **price impact models** to estimate this cost. A good model lets a trader know, before placing an order, whether the expected profit from a position is worth the cost of getting in. It also informs position sizing: if a trade has a 50-basis-point edge but will cost 75 basis points to execute, it should be skipped or downsized.

## The Linear Impact Model

The simplest price impact model is linear: assume that the impact cost is proportional to order size.

$$\text{Impact} = C \times \frac{Q}{V}$$

Where:
- $Q$ = the trader's order size (in dollars or shares)
- $V$ = typical daily volume (in dollars or shares, matched to $Q$)
- $C$ = a calibration constant (often 0.1–1, in basis points)

Example: suppose a stock has $100M in daily volume, and the constant $C = 0.25$ basis points. A trader wants to buy $5M of shares. The ratio $Q/V = 5 / 100 = 0.05 = 5\%$. The impact is $0.25 \times 0.05 = 0.0125$ basis points, or 1.25 basis points.

The linear model is intuitive: bigger trades cost more, and the cost is directly proportional. However, empirical research suggests reality is more forgiving. A doubling of order size doesn't exactly double the cost; instead, the cost curve is flatter. This is where the square-root model comes in.

## The Square-Root Impact Model

The **square-root model**, popularized by research from major algorithmic execution firms, posits that impact cost rises with the square root of relative order size.

$$\text{Impact} = C \times \sqrt{\frac{Q}{V}}$$

Using the same example: a $5M buy in a $100M daily volume stock. The ratio is $\sqrt{0.05} \approx 0.224$. If $C = 10$ basis points, the impact is $10 \times 0.224 = 2.24$ basis points.

The square-root model is empirically closer to how real markets behave. The intuition is that market impact has two components. The first is **temporary impact**: the direct cost of moving the order book. This is roughly proportional to order size. The second is **permanent impact**: the price move that reflects the information your order conveys about your intent or the market's new willingness to hold inventory. Permanent impact scales more slowly with order size, leading to a square-root aggregate relationship.

In liquid, high-turnover stocks (e.g., S&P 500 ETF or mega-cap tech), the square-root constant $C$ is smaller (often 2–5 bps). In less liquid stocks or less common times of day, $C$ can be 15–50 bps or more. Mid-cap and small-cap stocks can see 50–200 bps of impact for a large order.

## Calibrating the Model from Historical Data

To use a price impact model, a trader must calibrate it: estimate the constant $C$ from real trading data or from market microstructure research. One approach is to regress historical price changes against order flow.

For each trade, measure the price movement over the next few seconds or minutes and correlate it with the trade size relative to daily volume. Repeat over hundreds of trades and fit a linear or square-root curve to the data. The slope of that curve is your estimate of $C$.

Alternatively, a trader can use industry benchmarks. Major brokers and execution venues (e.g., [Nasdaq](/nasdaq/), [NYSE](/new-york-stock-exchange/)) publish market impact studies that estimate impact constants for various asset classes and liquidity conditions. A trader can use these as starting points and refine them with proprietary data.

## Permanent vs. Temporary Impact

Understanding the two types of market impact is crucial for realistic execution planning.

**Temporary impact** is the friction cost: the immediate spread the trader pays to move through the order book. If you want to buy 100,000 shares and the offer price is $50.10, you might need to buy 30,000 at $50.10, 40,000 at $50.20, and 30,000 at $50.30 to clear your full order. The average fill price is $50.21, a temporary impact of 11 cents. This impact is largely recoverable: if you exit a few minutes later, the price may revert, and you might get a better price on the way out.

**Permanent impact** is the information effect: your order revealed something about supply, demand, or your intent, and the market reprices permanently. If you buy a large block of shares, other traders may infer that something is afoot—a takeover, a hedge fund accumulation, etc. They mark prices higher in expectation. This impact doesn't decay; it sticks.

A trader might accept temporary impact (it's the cost of doing business), but permanent impact is the real cost. The square-root model conflates the two, which is why it's a heuristic. Sophisticated execution algorithms try to minimize permanent impact by disguising intent: they slice orders into smaller pieces, trade at non-round times, and avoid announcing large positions.

## Incorporating Impact Into Backtest Assumptions

Many quantitative traders backtest their strategies without any price impact assumption, or with a crude flat-fee model (e.g., "assume 1 basis point per round trip"). The result is a backtest that dramatically overstates real-world returns.

A better practice: estimate the impact cost for each trade using the trader's actual order sizes and the stock's typical daily volume. If a strategy involves buying an average of $2M of mid-cap stocks with $50M daily volume, the square-root model (with a calibrated $C$) might estimate 5–10 bps per entry. Apply the same to exits. Add commissions and bid-ask spreads, and the total round-trip cost might be 20–30 bps.

Example: a strategy backtests to 15% annual return with 100 trades per year. Without impact, the gross PnL is 15%. Assuming 25 bps per round trip and 100 trades, the impact cost is 0.25 bps × 2 × 100 = 5% of gross notional traded per year. If the strategy is turning over at 50% per year (a moderate turnover), the impact drag is roughly 2.5% of notional AUM, or 1.25% on a $100M fund. The realistic return drops to 13.75%.

## Limitations and Caveats

Price impact models are simplified. They assume that:
1. The stock's daily volume is stable (not true during crises or earnings).
2. Your order is "medium-sized" relative to the stock (very large orders might face nonlinear impacts; tiny orders might face essentially zero impact).
3. Execution is passive and doesn't use exotic algorithms to minimize slippage (smart order routing, VWAP algorithms, etc. can reduce impact).
4. Market conditions are "normal" (high volatility or regime changes can break the model).

Real market impact is also affected by the time of day (morning and close often see lower impact than midday), the stock's volatility, and broader market conditions. On a day when the [VIX](/volatility-smile/) spikes, impact constants can double or triple.

Additionally, impact models assume liquidity is available. During a [liquidity crisis](/liquidity-risk/) (e.g., March 2020), even large-cap stocks may have minimal liquidity, and a trader's order might move prices far more than the model predicts. Prudent traders stress-test their models under adverse scenarios.

## See also

<div class="wiki-seealso">

### Closely related

- [Market Maker (Trading)](/market-maker-trading/) — Who provides the liquidity that price impact models rely on
- [Bid-Ask Spread](/bid-ask-spread/) — The direct cost of entry and exit, separate from but related to price impact
- [Execution Risk](/execution-risk/) — Broader context of slippage and execution costs in trading
- [Algorithmic Trading](/algorithmic-trading/) — Systematic trading strategies that use price impact models to optimize order execution
- [Liquidity Risk](/liquidity-risk/) — How lack of available liquidity exacerbates price impact

### Wider context

- [Order](/market-order/) — The mechanism by which traders express intent and move markets
- [Quantitative Easing](/quantitative-easing/) — Large-scale institutional buying that also faces acute market impact
- [Market Cycle](/market-cycle/) — How market conditions and volatility change the empirical values of price impact constants
- [Value Investing](/value-investing/) — An alternative style that emphasizes stocks with low trading volume and high expected impact

</div>
