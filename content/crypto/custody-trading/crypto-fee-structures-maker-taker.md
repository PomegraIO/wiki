---
title: "Maker-Taker Fee Structure on Crypto Exchanges"
description: "Why crypto exchanges charge different fees for limit orders (makers) vs. market orders (takers). How fee structure drives trading behavior."
keywords:
  - maker taker fee crypto exchange
  - crypto exchange fee structure
  - maker fee taker fee difference
  - limit order vs market order fees
image: "/svg/crypto.svg"
---

*Crypto exchanges use a **maker-taker fee structure** to reward traders who post [limit orders](/limit-order/) (makers, who add liquidity) with lower or even negative fees, while charging higher fees to traders who immediately buy or sell using [market orders](/market-order/) (takers, who remove liquidity). This incentive structure is designed to keep the order book thick and competitive—and it directly shapes how traders execute.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Maker-Taker Fees — key facts</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Exchanges reward patient traders and charge impatient ones.</div>

|   |   |
|---|---|
| **Maker fee (typical)** | 0.01%–0.10% of order size |
| **Taker fee (typical)** | 0.05%–0.25% of order size |
| **Fee rebate (maker)** | Some exchanges pay rebates on maker orders (negative fee) |
| **Purpose** | Attract liquidity providers; keep order book deep |
| **Applies to** | Both spot trading and [derivatives](/option/) on most platforms |
| **Major exchanges** | Coinbase, Binance, Kraken, FTX (defunct), Deribit |
| **Tier incentive** | Fees often lower for high-volume traders (tiered structure) |

</aside>

## Why the Fee Difference Exists

At its core, the maker-taker fee structure solves a market design problem. A healthy exchange needs a deep, liquid [order book](/bid-ask-spread/)—many [limit orders](/limit-order/) sitting at various prices, ready to be filled. Without that depth, trades encounter high [slippage](/crypto-slippage-explained/), and traders migrate to competing exchanges.

**Makers** are traders who post limit orders—"I will sell 1 BTC at $67,500." They're patient; they're willing to wait for the market to come to them. In doing so, they provide liquidity for other traders. If no one posted limit orders, every trade would have to negotiate bilaterally, and nothing would trade.

**Takers** are traders who submit market orders—"I will buy 1 BTC at the current best asking price, whatever it is." They get immediate execution but take away the liquidity that makers provided.

Exchanges charge makers lower (or *negative*) fees and charge takers higher fees to encourage the behavior the market needs: patient limit orders, not constant market orders. It's a subsidy to liquidity provision.

## Typical Fee Levels

On most major exchanges:

- **Maker fee**: 0.01%–0.10% per trade (Coinbase Pro, Kraken, Binance Spot)
- **Taker fee**: 0.05%–0.25% per trade (Binance averages 0.10%, Coinbase Pro averages 0.50%)

For a 1 BTC order at $67,000:

| Scenario | Fee | Cost |
|---|---|---|
| Post limit order (maker), not filled for 1 hour, then filled | 0.05% | $33.50 |
| Submit market order (taker), filled immediately | 0.10% | $67.00 |

The taker pays roughly double. Over 100 trades, that compounds.

## Rebates and Negative Maker Fees

Some exchanges go further and pay **rebates**—negative fees—to makers. Deribit (a major crypto [derivatives](/option/) exchange) offers rebates of 0.01%–0.05% on maker orders, meaning the exchange *pays* you a small amount to post a limit order. This aggressively incentivizes liquidity provision.

How do exchanges afford to pay rebates? The spread between the taker fee (0.10%–0.25%) and the maker rebate (−0.05%) is wide enough that the exchange still profits, and they capture more trading volume, which nets more taker fees overall.

## How Fee Structure Shapes Trading Behavior

The maker-taker fee differential is not neutral. It actively changes how professional traders execute.

A market maker or high-frequency trading firm will often:

1. Post limit orders slightly better than the current best bid/ask, knowing they pay a lower (or negative) fee.
2. If the limit order is about to expire without filling, quickly send market orders to unwind the position, accepting the taker fee cost.
3. Use algorithms to optimize the trade-off between waiting (to get the maker fee benefit) and executing immediately (to avoid [inventory risk](/operational-risk/)).

A retail trader who only uses market orders is systematically overpaying compared to a professional using limits. If a retail trader averages 0.20% per trade in taker fees and a professional averages 0.05% (through mixed maker/taker execution), the professional saves ~15 basis points per round trip—roughly $1,000 on a $1M order.

## Tiered Fee Schedules

Most exchanges offer tiered fees based on 30-day trading volume. A trader with $100M volume in a month qualifies for "VIP" tier with maker fees of 0.00% and taker fees of 0.05%, while a $1M-volume trader might pay 0.05% maker and 0.10% taker.

This creates a scaling advantage: larger traders pay lower fees, which lowers their cost of capital and makes them more competitive. Startups and smaller operations have to outthink size with skill (better algorithms, better execution timing) to compete.

## Maker-Taker Fees on Crypto Derivatives

Crypto [derivatives](/option/) exchanges (perpetual futures, options) also use maker-taker fees, often with even steeper rebates. On Deribit, maker orders get paid 0.01%–0.02%, while takers pay 0.05%–0.10%. The rebate incentivizes market makers to quote tight bid-ask spreads on derivatives, where liquidity is even more critical.

## The Economics for Exchanges

From the exchange's perspective, maker-taker fees are a lever to control which trades happen on their platform. By offering attractive maker rebates, an exchange attracts professional market makers, who bring deep liquidity, which attracts retail traders seeking tight [spreads](/bid-ask-spread/), which grows the exchange's user base and total fee revenue.

Exchanges also use fee structures competitively. When Coinbase and Binance compete for spot trading volume, they often adjust their maker-taker spread. A 1% swing in taker fees can shift millions in volume.

## Comparison to Fixed Percentage Fees

Some smaller exchanges or platforms use a flat percentage fee regardless of whether you're a maker or taker (e.g., 0.15% per trade). This is simpler but less effective at incentivizing liquidity. Traders are indifferent between posting limits and sending market orders, so the order book thins. Retail-focused exchanges or platforms without professional market makers sometimes accept this trade-off.

## See also

<div class="wiki-seealso">

### Closely related

- [Slippage in Crypto Trading Explained](/crypto-slippage-explained/) — the hidden cost beyond fees
- [Bid-Ask Spread](/bid-ask-spread/) — what maker-taker incentives aim to keep tight
- [Limit Order](/limit-order/) — how makers trade
- [Market Order](/market-order/) — how takers trade
- [Cryptocurrency Exchange](/cryptocurrency-exchange/) — where these fees apply
- [High-Frequency Trading](/algorithmic-trading/) — professionals exploiting fee structures

### Wider context

- [Algorithmic Trading](/algorithmic-trading/) — trading strategies that minimize fees
- [Bitcoin](/bitcoin/) — most-traded crypto pair (BTC/USD)
- [Ethereum](/ethereum/) — second-largest, high-volume trading
- [Futures Contract](/futures-contract/) — crypto derivatives with similar fee structures
- [Price Discovery](/price-discovery/) — why thick order books matter

</div>
