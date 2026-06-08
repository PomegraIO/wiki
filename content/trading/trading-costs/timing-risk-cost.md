---
title: "Timing Risk Cost"
description: "The expected cost of price drift between the decision to trade and final execution of the full order."
keywords:
  - timing risk
  - trade execution
  - price drift
  - execution cost
  - slippage
image: "/svg/trading.svg"
---

*A **timing risk cost** is the price movement against a trader that occurs between the moment the decision to trade is made and the moment the full order is completed. Unlike [market-impact-model](/market-impact-model/) costs, which are self-inflicted by the order's own size, timing risk is driven by the market moving independently during the execution window.*

## The cost of not trading instantly

In an ideal world, a trader could execute a large order instantaneously at a single fair price. In reality, orders take time. An institutional trader deciding to sell $50 million of a stock can execute part of it immediately but must break the rest into smaller pieces to avoid shocking the market. This execution window—measured in seconds for high-frequency traders, hours for most equity traders, days for large block orders—exposes the trader to market risk. If the market moves against the position during execution, the trader realises a loss relative to the original decision price.

This loss is **timing risk cost**. It is the expected slippage attributable purely to adverse price movement, independent of the order's presence. A market maker might face timing risk when quoting prices; a portfolio manager faces it during rebalancing; a corporate executive faces it when selling shares; anyone deferring execution faces it.

Timing risk differs from [market-impact-model](/market-impact-model/) in mechanism: market impact is deterministic and tied to order size, while timing risk is stochastic and driven by random market price moves.

## Why timing risk exists

Three fundamental factors create timing risk:

### Volatility

The greater the asset's [volatility](/volatility-smile/), the wider the price swings in any given time window. A trader executing a volatile technology stock faces larger adverse moves than one executing a utility stock. Timing risk scales roughly with volatility and the square root of execution time.

### Urgency constraints

A trader with a fixed deadline (corporate mandate, fund outflow, rebalancing window) cannot choose execution timing freely. Forced sellers in a crisis must accept whatever price prevails; they have no choice to wait for better conditions. Traders with flexibility can defer execution to low-volatility periods, reducing timing risk.

### Information asymmetry

If other market participants suspect that a large order is coming, they may begin trading ahead of it, moving the price before the main order executes. A rumour that a large fund is liquidating might trigger pre-emptive selling. This is a form of timing risk driven by adverse selection.

## Quantifying timing risk

For a trader executing an order over a fixed time horizon T, the expected timing risk cost is approximately:

**Expected Timing Risk = (Volatility × √T / 2) × Position Size**

This square-root relationship with time reflects the diffusive nature of price movement under [Brownian motion](/market-risk/) assumptions. Doubling execution time does not double timing risk; it increases it by √2 (about 41%). This is the mathematical foundation for splitting large orders: if a trader can extend execution from 1 hour to 4 hours, timing risk only increases by a factor of 2, not 4.

In practice, the constant (the "1/2") varies based on market conditions, the likelihood of adverse moves, and the trader's execution strategy. A sophisticated algorithm that waits for size and buys only during upswings may reduce timing risk below the theoretical baseline; a naive market-order approach may exceed it.

## Timing risk versus market impact

The two costs often move in opposite directions. Consider splitting a large order:

| | **Timing Risk** | **Market Impact** |
|---|---|---|
| Execute quickly (single large order) | Small (short window) | Large (entire size at once) |
| Execute slowly (many small orders) | Large (longer exposure) | Small (diluted across many fills) |

An optimal execution strategy balances these: too-fast execution incurs punishing market impact; too-slow execution incurs punishing timing risk. An execution algorithm aims to find the sweet spot.

During high-volatility periods, timing risk rises steeply, and traders may prefer to execute quickly despite market impact. During calm periods, timing risk is negligible, and extending execution to minimise impact is rational. During a flash crash or liquidity crisis, both costs can spike simultaneously—the worst outcome.

## Real-world drivers of timing risk

### Intraday seasonality

Timing risk is typically lowest during high-volume windows (market open and close) because price discovery is most efficient and spreads are tightest. Mid-day periods often show higher volatility and wider spreads, increasing timing risk. A trader aware of these patterns can schedule execution to reduce timing risk.

### News and information events

Timing risk spikes around earnings releases, central bank decisions, economic data, or company-specific announcements. Traders facing a known data release must decide: execute before the event (facing standard timing risk) or wait until after (risking a large move in either direction). There is no risk-free choice.

### Market regime shifts

During stable market conditions, historical [volatility](/volatility-smile/) is a good predictor of near-term timing risk. During financial stress, volatility can spike unexpectedly, and historical models fail. Traders must use [value-at-risk](/value-at-risk/) or stress-testing frameworks to size timing risk exposure during potential crisis scenarios.

## Timing risk and execution algorithms

Most modern execution algorithms are designed to minimise total execution cost by dynamically balancing timing risk and market impact. An algorithm might:

- Accelerate execution if timing risk spikes (volatility jumps).
- Slow execution if market impact is unusually high (spreads widen, depth thins).
- Exploit intraday seasonality (execute more during high-volume hours).
- Respond to price momentum (buy more aggressively on rallies to reduce timing risk).

The best algorithms learn from real-time market microstructure and adapt the execution schedule in real time. Conversely, a naive trader executing a fixed schedule regardless of market conditions may incur timing risk far in excess of the theoretical minimum.

## Timing risk and investor decision-making

Timing risk affects buy-side investment decisions. A portfolio manager might decide that a stock is undervalued and want to buy. But if execution takes three days and the stock is volatile, there is a 50% chance that the manager will pay more than the original decision price, even if nothing fundamental has changed. This timing risk reduces the expected return of the idea. 

For trades with narrow expected profit margins, timing risk can flip a profitable idea into a loss. Institutional traders often use "soft order" signals—working an order passively for a few hours before escalating to aggressive execution—to dampen timing risk. Conversely, high-conviction traders may execute aggressively to avoid timing risk, accepting [market-impact-model](/market-impact-model/) costs.

## See also

<div class="wiki-seealso">

### Closely related

- [Market Impact Model](/market-impact-model/) — the cost of a trade's own size moving the execution price
- [Transaction Cost Analysis](/transaction-cost-analysis/) — post-trade measurement of total execution cost
- [Opportunity Cost of Trading](/opportunity-cost-of-trading/) — the cost of uninvested cash sitting idle
- [Volatility Smile](/volatility-smile/) — how volatility varies across strikes and time horizons
- [Value-at-Risk](/value-at-risk/) — quantifying the worst-case loss over a given horizon
- [Algorithmic Trading](/algorithmic-trading/) — automated algorithms designed to optimise execution cost
- [Liquidity Risk](/liquidity-risk/) — the risk that an order cannot be executed at fair value

### Wider context

- [Stock Market](/stock-market/) — the primary venue where timing risk manifests
- [Price Discovery](/price-discovery/) — how fair value is determined in real time
- [Market Order](/market-order/) — immediate execution, exposing the trader to timing risk
- [Bid-Ask Spread](/bid-ask-spread/) — the round-trip cost separate from timing and impact costs

</div>
