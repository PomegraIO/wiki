---
title: "Spread Cost: High-Frequency Traders vs Retail Investors"
description: "Explore the asymmetry in spread cost between HFT firms that capture the spread and retail investors who pay it, and how this shapes the true cost of trading."
keywords:
  - spread cost high frequency
  - HFT liquidity provision
  - retail bid-ask spread
  - market-maker profitability
  - execution costs
  - tick spreads
image: "/svg/trading.svg"
---

*The **spread cost** is fundamentally asymmetrical: high-frequency traders and market makers *capture* the spread as profit on each transaction, while retail and institutional investors *pay* it. This divide explains why order flow is so valuable to HFT firms and why the true cost of trading differs dramatically between a professional and a retail shop.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Spread Cost — HFT vs Retail</div>

<img src="/svg/trading.svg" alt="An abstract editorial mark for trading." />

<div class="wiki-infobox-caption">The same spread width means profit to the market-maker and a cost to the order-taker.</div>

|   |   |
|---|---|
| **Who captures the spread** | Market makers and HFT firms providing two-sided prices |
| **Who pays the spread** | Retail traders, institutional investors, and others taking liquidity |
| **Typical retail spread (liquid stocks)** | 1–5 cents per share, or 0.1–0.5 basis points; wider for illiquid securities |
| **Cost per round-trip trade** | 2 × spread (buy at ask, sell at bid); can add 0.2–1% to transaction cost |
| **HFT advantage** | Technology and rebates allow profitable spreads of 0.5–2 cents, paid by retail |
| **Impact on retail profitability** | A losing trader's costs are 5–10× higher than a professional's |

</aside>

## The Mechanics: Who Stands on Each Side

When a retail investor places a [market order](/market-order/) to buy 100 shares, they hit the [bid-ask spread](/bid-ask-spread/). The **ask price** they pay is typically higher than the **bid price** at which they could immediately sell the same shares. The difference—the spread—is pocketed by whoever was willing to sell at that ask.

For heavily traded stocks like Apple or SPY, the spread might be $0.01 per share. But the structure of who profits differs starkly:

- A **[market maker](/market-maker-trading/)** or HFT firm quotes both a bid and an ask, captures the spread on each transaction, and then manages the [inventory risk](/operational-risk/) of holding the shares. Over hundreds or thousands of trades per day, small spreads across high volume generate steady profit.

- A **retail investor** submitting a market order takes the worst price immediately, paying the full spread in one direction. If they then want to exit—say, an hour later—they face the spread again in the opposite direction (selling at the bid instead of the ask). For a round-trip trade, they pay the spread twice.

## The Mathematics of Asymmetrical Costs

Suppose a stock trades with a $0.02 spread. A market maker captures that $0.02 profit per share. A retail trader:

- **Buying 100 shares at the ask**: pays $0.02 × 100 = $2 more than the midpoint.
- **Selling the same 100 shares at the bid**: receives $0.02 × 100 = $2 less than the midpoint.
- **Round-trip cost**: $4 on a transaction of, say, $50,000—or 8 basis points (0.08%).

For a stock trading $500 with a $0.05 spread, the round-trip cost jumps to 20 basis points. For illiquid microcap stocks with spreads of $0.50 or wider, round-trip costs can exceed 1% or 2%.

By contrast, a market maker capturing the spread 1,000 times per day at $0.02 per share on 100-share lots profits $2,000 daily before inventory risk and technology costs. The retail trader faces that cost head-on.

## Why HFT Firms Win the Spread Game

High-frequency trading firms profit from the spread through several reinforcing advantages:

### 1. **Scale and Speed**
HFT firms operate thousands of [limit order](/limit-order/) updates across hundreds of securities, millisecond by millisecond. A single basis point on a million shares moves $100. At their speed, they can turn over inventory fast enough to harvest the spread repeatedly without holding unhedged directional risk for long.

### 2. **Technology and Venue Access**
Co-location (servers housed in exchange data centers), proprietary order routing, and access to dark pools allow HFTs to see order flow fractionally ahead of the broader market. This information advantage lets them tighten spreads when they have inventory they want to shed, and widen them when they want to accumulate—effectively frontrunning retail order flow.

### 3. **Liquidity Rebates**
Exchanges pay [liquidity rebates](/market-maker-trading/) (typically 0.1–0.3 basis points) to firms that post limit orders that get executed. Retail traders pay, and market makers get paid. Over millions of transactions, these rebates alone can cover a significant portion of operating costs.

### 4. **Adverse Selection**
Market makers know that large [market order](/market-order/) flow often signals information or large institutional trading. They widen spreads before likely directional moves and tighten them when they're confident in two-sided order flow. Retail traders, on the other hand, are often hit with adverse selection—their entry points are frequently near local peaks, their exits near local troughs.

## The Retail Penalty

The cumulative effect on a retail trader's profitability is stark. Assume a retail trader with a 52% win rate on individual trades (only barely better than random), holding each position for an hour, and facing a 10 basis point round-trip spread cost:

- **Expected profit on edge** (52% win rate): roughly 0.2% per trade.
- **Spread cost**: 1% (10 bp round-trip).
- **Net outcome**: a ~0.8% loss per trade.

The spread alone erases profitability for all but the most edge-driven traders. By contrast, a [market maker](/market-maker-trading/) with the same 52% win rate harvests the spread first (the spread *is* their profit) and then depends on avoiding adverse selection and inventory loss—a much softer hurdle.

## Commissions, Rebates, and the Full Picture

Modern retail brokers (Robinhood, Fidelity, Interactive Brokers) have eliminated per-trade commissions, which was a major step forward for retail traders. But the spread cost remains. Some retail brokers offer small rebates or price improvement in certain circumstances, but these rarely offset the average spread paid by retail order flow.

Institutional investors (pensions, hedge funds, asset managers) negotiate [execution quality](/price-discovery/) with brokers and can use smart execution algorithms to minimize market impact. They still pay spreads, but their negotiating power and size give them better average prices than a retail account making 100-share market orders.

## The Persistence of the Spread in Modern Markets

Despite automation and tighter regulation (like Regulation SHO and quote requirements), spreads remain economically significant. For liquid stocks on major exchanges, the one-cent spread persists because:

1. **Tick size rules** limit how close market makers can place orders.
2. **Inventory risk** must be compensated; even passive market making incurs risk.
3. **Technology costs** are real; maintaining systems for thousands of symbols requires capital.
4. **Competition among market makers** drives spreads lower, but not to zero, because at zero they'd operate at a loss.

## Order Types and Spread Avoidance

Retail traders can reduce spread costs by using [limit order](/limit-order/) instead of market orders. Placing a limit order to buy at the bid (or sell at the ask) lets you capture the spread's opposite side—but success depends on price moving toward you, which is not guaranteed. Large traders can also use VWAP or TWAP algorithms to split orders across time, reducing market impact. But for small retail orders and short time horizons, the market order and its spread cost are often unavoidable.

## Connection to Market Structure

The spread is the most visible reminder that financial markets have a structural incentive system. Market makers are essential to liquidity, but they profit by standing between buyers and sellers. Regulators have pushed for tighter spreads through tick-size reviews and minimum quoting requirements. But the fundamental asymmetry—that liquidity providers profit and liquidity takers pay—is intrinsic to how markets function.

## See also

<div class="wiki-seealso">

### Closely related

- [Bid-Ask-Spread](/bid-ask-spread/) — Definition and measurement of the spread itself
- [Market-Order](/market-order/) — How retail traders pay the spread in full
- [Limit-Order](/limit-order/) — Alternative execution method that can reduce spread cost
- [Market-Maker-Trading](/market-maker-trading/) — How professionals capture the spread
- [Price-Discovery](/price-discovery/) — How spreads reflect market information and risk
- [Alternative-Trading-System](/alternative-trading-system/) — Dark pools and non-standard venues where spreads differ

### Wider context

- [Execution-Risk](/execution-risk/) — Broader trading costs beyond the spread
- [Algorithmic-Trading](/algorithmic-trading/) — Tools professionals use to minimize spread cost
- [Fragmented-Market](/fragmented-market/) — How multiple venues affect spread opportunities
- [Finra](/finra/) — Regulator overseeing market-maker conduct and fairness

</div>
