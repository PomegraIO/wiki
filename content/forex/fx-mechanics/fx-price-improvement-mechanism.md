---
title: "Price Improvement in Forex: How It Works"
description: "When and why a forex broker or ECN executes orders at better rates than quoted, and why it happens more during high-liquidity sessions."
keywords:
  - price improvement forex order execution
  - forex market order execution
  - ECN price improvement currency
  - bid-ask spread improvement forex
---

*When you place a market order for a currency pair, brokers and ECNs can sometimes execute you at a better [bid-ask spread](/bid-ask-spread/) than their published quote—a phenomenon called **price improvement in forex**. It happens most when the market is busiest and spreads are tightest, yet it is fragile and contingent on real liquidity matching.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Price Improvement in Forex — key facts</div>

<img src="/svg/forex.svg" alt="An abstract editorial mark for forex." />

<div class="wiki-infobox-caption">Better fills exist, but only when natural supply and demand align in real time.</div>

|   |   |
|---|---|
| **Definition** | Executing a trade at a rate inside the best-quoted [bid-ask spread](/bid-ask-spread/) |
| **Who provides it** | ECNs, [market makers](/market-maker-trading/), and some brokers with direct liquidity pools |
| **Likelihood** | Highest during overlap hours (London–New York, especially Asia–London) |
| **Mechanics** | Broker routes order to multiple liquidity sources and picks the best available fill |
| **For retail traders** | Common but small in pip terms (0.1–0.5 pips); does not offset slippage on large orders |
| **Regulation** | FCA rules require best execution; some brokers can legally decline the improvement |

</aside>

## The Quoted Spread vs. The Execution Price

In forex, the [bid-ask spread](/bid-ask-spread/) published by a broker or ECN is an offer to trade at those rates *right now*. If the EUR/USD bid-ask is quoted at 1.0850–1.0852, you can sell at 1.0850 or buy at 1.0852 instantly.

But the forex market is not a single exchange. Beneath any broker's quote are hundreds of [market makers](/market-maker-trading/) and liquidity providers, each quoting their own bid and ask. A broker's published spread is often the *worst* of the available prices—or a price aimed at a typical retail order size. Larger orders or orders placed at the right moment can access better prices from those deeper liquidity sources.

**Price improvement** occurs when an order gets filled at a rate better than the published spread. A buy order at the best ask of 1.0852 might execute at 1.0851 instead—a one-pip improvement. Or a sell at the quoted bid of 1.0850 executes at 1.0850.25, a quarter-pip better.

This is not magic—it is the result of real liquidity existing at those price levels. When a trader's order arrives, the broker routes it through an aggregator or ECN that connects to multiple liquidity providers. The broker picks the best available price at that instant.

## Why It Happens More During Peak Liquidity Hours

Price improvement depends entirely on the existence of liquidity at or better than the quoted spread.

During the **London–New York overlap** (roughly 12:00–16:00 UTC), the forex market is busiest. Spreads on major pairs (EUR/USD, GBP/USD, USD/JPY) can tighten to 0.5–1.5 pips. At the same time, thousands of market makers and banks are posting bids and asks, creating a deep order book at every price level. An order that arrives in this window has a good chance of finding a taker willing to trade at a price inside the published spread.

During **Asian trading hours** or late **US hours**, when liquidity is thinner, spreads widen (maybe 1–3 pips on major pairs) and fewer traders are at each price level. Price improvement becomes rarer because there is less depth to tap.

For **exotics and crosses** (less-traded pairs), price improvement is less common at any time of day. The liquidity sources are fewer and spreads are wider to start with. A broker might publish EUR/MXN at 19.50–19.65 (a 15-pip spread), and there may be little liquidity much better than that to tap.

## The Mechanics: Order Routing and Aggregation

When you send a market order to a retail broker or ECN, it does not stop at the single bid or ask you see. Instead:

1. The broker receives your order
2. It routes the order to an **aggregator** or **ECN** that connects to multiple liquidity providers (banks, [market makers](/market-maker-trading/), other ECNs)
3. Each liquidity provider has quoted their own bid and ask to the aggregator
4. The aggregator sorts offers by price and fills your order at the best available rate

If you are buying 1 million EUR/USD, the aggregator might fill 300,000 at 1.0851, another 400,000 at 1.0851.50, and the remaining 300,000 at 1.0852—blending a slightly better average than the published 1.0852 ask.

This is standard practice at ECNs like [Currenex](/market-maker-trading/) or EBS. Retail brokers using ECN models (such as True ECN brokers) do the same. Pure [market-maker](/market-maker-trading/) brokers, who trade *against* you rather than for you, have less incentive to improve prices—they profit from the spread, so a tighter fill cuts their edge.

## Regulatory and Practical Limits

In regulated markets (US, UK, EU), brokers must provide **best execution** on average. They cannot deliberately skip a better price. In the US, Regulation SHO and FINRA rules require brokers to execute at the best available price or display the improvement to the customer. In the EU, MiFID II imposes similar best-execution rules.

**But** best execution does not mean every trade is improved. It means that *on average*, over time, the broker must not systematically disadvantage clients. A single order might not be improved, yet the client still receives the best fill available at that instant—which is acceptable.

Some retail brokers, especially those outside strict regulatory jurisdictions, may decline to pass through available improvements if it conflicts with their own [market-making](/market-maker-trading/) desk. This is why checking a broker's best-execution policy and trading conditions is essential.

## Price Improvement vs. Slippage

Price improvement and [slippage](/bid-ask-spread/) often get confused.

**Price improvement** is when you get a *better* fill than quoted. **Slippage** is when you get a *worse* fill than quoted.

On a fast-moving market, slippage is common. A EUR/USD pair quoted at 1.0850–1.0852 might slip to 1.0849–1.0851 between the moment you click "buy" and the instant it executes—you miss the 1.0852 ask and instead pay 1.0851. That is slippage, and it costs you.

Price improvement and slippage can both occur on the same order—the broker routes your order, but by the time it hits the liquidity pool, prices have moved. You might have received 1.0851 instead of 1.0852 (improvement), but the true market mid has shifted to 1.0851–1.0853 (slippage).

For retail traders, slippage on large orders or during low-liquidity periods usually outweighs any benefit from small pips of improvement.

## Practical Implications for Traders

Price improvement is real but small—usually 0.1 to 0.5 pips on major pairs. Over a year of active trading, it might reduce your total trading costs by a few basis points.

The best conditions for price improvement are:

- **Major currency pairs** (EUR/USD, GBP/USD, USD/JPY, AUD/USD) with established liquidity pools
- **Peak trading hours** (London open, London–New York overlap)
- **Small to medium order sizes** (up to a few million units); very large orders may move the market
- **ECN or STP brokers** with genuine multi-source liquidity routing; avoid pure [market makers](/market-maker-trading/) if improvement matters to you
- **Limit orders** placed away from the spread also benefit; they wait for better prices to form

Price improvement is most useful as a tie-breaker when choosing a broker. If two brokers offer similar spreads and conditions, pick the one with documented commitment to best execution and price improvement.

## See also

<div class="wiki-seealso">

### Closely related

- [Bid-Ask Spread](/bid-ask-spread/) — the gap between buy and sell prices that improvement narrows
- [Market Maker Trading](/market-maker-trading/) — the firms and mechanisms providing liquidity
- [Market Order](/market-order/) — immediate execution at market rates, where improvement occurs
- [Limit Order](/limit-order/) — orders placed away from the spread that improve over time
- [ECN](/alternative-trading-system/) — electronic systems connecting traders directly to multiple sources
- [Slippage](/bid-ask-spread/) — the opposite of improvement; getting a worse price than quoted

### Wider context

- [Currency Risk](/currency-risk/) — what drives price movement in forex
- [Carry Trade](/carry-trade/) — strategy that benefits from tight spreads and low costs
- Forex — the broader forex market structure
- [Leverage Ratio (Forex)](/leverage-ratio-forex/) — large positions make slippage and improvement more material
- [Spot Exchange Rate](/spot-exchange-rate/) — the "spot" rates where improvement applies

</div>
