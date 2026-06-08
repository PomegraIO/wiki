---
title: "Realized Spread"
description: "The spread revenue a market maker actually earns after accounting for adverse price movement between posting a quote and hedging the resulting trade."
keywords:
  - realized spread
  - market maker profit
  - bid-ask spread
  - adverse selection
  - trading economics
image: "/svg/trading.svg"
---

*The **realized spread** is the subset of [bid-ask spread](/bid-ask-spread/) revenue that a [market maker](/market-maker-trading/) keeps after short-term price movement washes out. Unlike the [effective spread](/effective-spread/) (which measures cost to a taker), realized spread measures what the [market maker](/market-maker-trading/) actually pockets—a crucial lens into market-making profitability and adverse selection risk.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Realized Spread — key facts</div>

<img src="/svg/trading.svg" alt="An abstract editorial mark for trading and costs." />

<div class="wiki-infobox-caption">The true profit a market maker earns, net of short-term inventory risk.</div>

|   |   |
|---|---|
| **What it is** | Quoted spread minus the loss from price movement after taking on inventory |
| **Who measures it** | Market makers, regulators, and researchers auditing market-making economics |
| **Core logic** | Posted spread revenue − adverse price movement = realized profit |
| **Also called** | Dealer profit, realized spread revenue, true spread |
| **Measured in** | Basis points (bps) or cents per share |
| **Why it matters** | Shows which trades lose money; reveals adverse selection costs |

</aside>

## The divergence between posted and realized

A [market maker](/market-maker-trading/) quotes a bid of 50.00 and an ask of 50.05—a 5-cent spread. When a buyer lifts the ask at 50.05, the market maker is short one unit. If the stock immediately ticks down to 50.02, the [market maker](/market-maker-trading/) can hedge by buying at 50.02, realizing a spread of only 50.05 − 50.02 = 3 cents. The realized spread is narrower than the quoted spread because adverse price movement eroded the profit.

Conversely, if the stock ticks up to 50.08 after the sale, the [market maker](/market-maker-trading/) can buy at 50.08 and still come out ahead with a spread of 50.05 − 50.02 (the hedge price she paid for the offsetting buy)—but the realized spread has now benefited from favorable price movement. Most trades, however, show some adverse movement, especially the ones initiated by sophisticated traders who often trade when information favors the [market maker's](/market-maker-trading/) counterparty.

## Adverse selection and who trades with whom

Realized spread reveals a harsh truth: [market makers](/market-maker-trading/) lose money on informed trades. When a professional trader spots a pricing inefficiency and hits a [market maker's](/market-maker-trading/) bid, or when a sharp fund lifts an ask before news reaches the rest of the market, the [market maker](/market-maker-trading/) is on the wrong side. The quoted spread is not enough to compensate for the loss that follows when the [market maker](/market-maker-trading/) hedges into a market that has moved against her.

This is called adverse selection or adverse selection risk—the risk that you are trading with someone who knows more than you do. [Market makers](/market-maker-trading/) price this risk into their spreads, but they cannot eliminate it entirely. By measuring realized spread, researchers can quantify how much [adverse selection](/bid-ask-spread/) costs the [market maker](/market-maker-trading/) on each trade or on trades from specific counterparties.

## How realized spread is calculated

The standard calculation uses the quote midpoint:

**Realized Spread = (Posted Spread / 2) − [Midpoint at Hedge Time − Midpoint at Trade Time] / 2**

Equivalently, if the [market maker](/market-maker-trading/) buys at the ask and then sells to a counterparty at the bid (a round-trip), the realized spread is the net of the quoted spreads on both legs minus the loss incurred by the adverse price movement between them.

In practice, researchers use a simpler backward-looking definition: the [effective spread](/effective-spread/) paid by the counterparty minus the [effective spread](/effective-spread/) the [market maker](/market-maker-trading/) faces on her hedge. If the hedge is one tick worse than expected, realized spread shrinks.

## The scale of adverse selection losses

In highly liquid stocks, realized spread is often 40–70% of the quoted spread. In thinly traded issues or at the open and close, realized spread can fall to 10% of quoted spread or even turn negative (meaning the [market maker](/market-maker-trading/) loses money even before operating costs). This is one reason spreads widen during low-liquidity periods—[market makers](/market-maker-trading/) demand more room to cover [adverse selection](/bid-ask-spread/) risk.

On very liquid, information-insensitive stocks like large-cap index components, realized spread is higher—sometimes 60–80% of quoted spread—because most trades are noise or portfolio rebalancing, not information-driven. [Market makers](/market-maker-trading/) face less adverse selection and can keep more of their spread revenue.

## Technology and prediction

Modern [market makers](/market-maker-trading/) use machine learning and real-time feeds to anticipate adverse selection. They observe order flow, market depth, and volatility to predict which trades are information-driven and which are incidental. A [market maker](/market-maker-trading/) who detects an incoming algorithmic order splitting a large position into small pieces will quote wider to protect against adverse selection. One who sees a retail order from a discretionary trader's account might quote tighter, knowing the trade is unlikely to front-run her hedge.

This cat-and-mouse game between [market makers](/market-maker-trading/) and traders has dramatically tightened quoted spreads over the past two decades, but realized spreads have compressed far less. The gap between quoted and realized spread has become one of the most valuable assets a [market maker](/market-maker-trading/) can engineer.

## Regulatory and research applications

The [Securities and Exchange Commission](/securities-and-exchange-commission/) and academic researchers use realized spread data to audit [market maker](/market-maker-trading/) behavior and market quality. A [market maker](/market-maker-trading/) whose realized spreads are consistently near zero (losing on most trades) is probably not managing information asymmetry well and may exit the market. One whose realized spreads are reliably high (say, 50 basis points on every trade) is either taking less [adverse selection](/bid-ask-spread/) risk or operating in a less efficient market.

Realized spread also serves as a benchmark for algorithmic trading systems. An algo that can execute a large order at an [effective spread](/effective-spread/) of 8 basis points is a bargain if normal realized spreads for similar trades are 20 basis points.

## The link to quote setting

[Market makers](/market-maker-trading/) that track their own realized spreads can refine their quoting algorithms dynamically. If realized spread is unusually low on a given security, the [market maker](/market-maker-trading/) can widen her quotes (increasing the posted spread) without losing much volume, since takers will still find it competitive compared to other venues. If realized spread is high, the [market maker](/market-maker-trading/) can tighten quotes to capture more volume, confident that the [adverse selection](/bid-ask-spread/) margin is still healthy.

## Realized versus effective spread

The two metrics are inverses of a two-sided transaction. [Effective spread](/effective-spread/) is the cost borne by the taker; realized spread is the net revenue kept by the [market maker](/market-maker-trading/). Together, they reveal the total economics of a trade: the spread quoted, minus the [adverse selection](/bid-ask-spread/) loss to the [market maker](/market-maker-trading/), equals what the taker overpaid. The remainder is the [market maker's](/market-maker-trading/) true economic profit from the trade.

---

## See also

<div class="wiki-seealso">

### Closely related

- [Effective spread](/effective-spread/) — the cost paid by the taker, mirror of realized spread
- [Bid-ask spread](/bid-ask-spread/) — the quoted spread, before adverse price movement
- [Market maker trading](/market-maker-trading/) — the role and strategies of market makers
- [Adverse selection](/bid-ask-spread/) — the cost of trading with informed counterparties
- [Exchange fee schedule](/exchange-fee-schedule/) — how venues set taker and maker fees

### Wider context

- [Price discovery](/price-discovery/) — how spreads reflect pricing efficiency
- [Liquidity risk](/liquidity-risk/) — why realized spread widens in illiquid markets
- [Stock market](/stock-market/) — the ecosystem where market makers operate
- [Market order](/market-order/) — how realized spread is born from taker-initiated trades

</div>
