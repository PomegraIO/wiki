---
title: "Crypto Market Making"
description: "How firms quote continuous bid-ask spreads on crypto exchanges and manage inventory risk in volatile markets."
keywords:
  - market making
  - bid-ask spread
  - cryptocurrency
  - liquidity provision
  - inventory management
image: "/svg/crypto.svg"
---

*A **crypto market maker** is a firm that continuously quotes both buy and sell prices on digital-asset exchanges, profiting from the [bid-ask spread](/bid-ask-spread/) while taking on the risk that prices move sharply against their positions. Market makers anchor the liquidity that allows retail and institutional traders to execute large orders without moving the market dramatically.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Crypto Market Making — key facts</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for cryptocurrency and trading." />

<div class="wiki-infobox-caption">Professional liquidity providers embedded in crypto venues.</div>

|   |   |
|---|---|
| **What it is** | A firm quoting continuous bids and asks to earn the spread, while managing inventory exposure |
| **Key skill** | Rapid repricing in response to market moves and order flow imbalances |
| **Profit source** | Spread capture (buy low, sell high) and adverse-selection mitigation |
| **Main risk** | Inventory gets stranded if price gaps or volatility spikes; capital gets locked in bad positions |
| **Typical infrastructure** | Co-located servers, real-time market data feeds, automated repricing algorithms |
| **Related to** | [Market maker (stocks)](/market-maker-trading/), [Alternative trading systems](/alternative-trading-system/) |

</aside>

## Why crypto markets need market makers

Traditional stock exchanges have [market makers](/market-maker-trading/) embedded in their structure—the [New York Stock Exchange](/new-york-stock-exchange/) or [NASDAQ](/nasdaq/) have assigned specialists or dealer firms who compete to hold inventory. Crypto exchanges, especially decentralised venues and newer centralised platforms, often lack that automatic liquidity backbone. When a large buyer wants to sell a million dollars of Bitcoin or Ethereum, they either have to place limit orders and wait (passive) or cross the spread immediately with a market order (active, and expensive). Market makers fill that gap by standing ready: "I'll sell you Bitcoin at this price, and I'll buy from you at that price, right now."

This service is crucial. Without continuous quotes, the [bid-ask spread](/bid-ask-spread/) widens dramatically, raising the effective cost of trading. Volatile or illiquid altcoins can have spreads of 1–5% or more. Professional market makers narrow those spreads to 0.05–0.2%, making trading affordable and allowing price discovery to work properly.

## The mechanics of quoting and repricing

A crypto market maker monitors real-time prices across venues using algorithmic feeds and quotes both sides: a bid (what they'll pay to buy) and an ask (what they'll charge to sell). The width of the spread depends on [volatility](/historical-volatility/), order-flow intensity, and the firm's risk appetite. In calm periods with high volume, the spread can be razor-thin (0.01%). In panicky markets, market makers pull liquidity—they widen the spread or pause quotes entirely—because the risk of being picked off (having one side filled just before a sharp price move) becomes intolerable.

The game is to buy at the bid and sell at the ask frequently enough to compound the spread over thousands of trades per day. A market maker executing 10,000 trades per day at an average spread of 0.1% earns 10 basis points daily—trivial per trade but substantial in aggregate. The challenge is repricing fast enough to avoid adverse selection: if Bitcoin drops 2% in seconds, a market maker still holding a long position is out money. Sophisticated market makers use real-time feeds and millisecond-speed algorithms to reprice instantly when the mid-market price shifts.

## Inventory risk and hedging

Market makers carry inventory: they accumulate positions in crypto as trades flow through them unevenly. If more buyers show up than sellers, the market maker gets long Bitcoin. If the opposite happens, they get short. Holding large positions in volatile assets is risky. A market maker long 100 Bitcoin at $40,000 faces a potential $4 million loss if the price drops to $36,000 overnight.

To manage this, market makers hedge. They offset longs on one exchange by shorting on another (cross-exchange arbitrage). They use [futures contracts](/futures-contract/) to hedge spot holdings. They adjust their quote prices aggressively to discourage further buying if they're too long. Some operate multiple venues simultaneously, balancing inventory across a portfolio. The best market makers are almost always delta-neutral—meaning they don't want to take a bet on direction; they want to be indifferent to whether prices go up or down, earning money purely from flow and spreads.

## Capital requirements and competitive dynamics

Effective market making requires substantial working capital. A market maker quoting on a major venue like Binance or Coinbase typically holds hundreds of thousands or millions in crypto to back their quotes. They also need sophisticated risk management infrastructure, including real-time P&L tracking, automated position limits, and rapid-fire hedging systems. The barrier to entry is high enough that a small list of professional firms dominate most venues' top liquidity.

Competition among market makers is fierce and drives spreads tighter. If one market maker quotes a 0.2% spread on Ethereum and another quotes 0.1%, the tighter quoter will capture more volume. This arms race is relentless: firms invest heavily in latency reduction, better algorithms, and superior data to stay ahead. The winners in this space are often well-capitalised trading firms with deep expertise in derivatives and risk management—many migrated into crypto from traditional derivatives or FX markets, bringing institutional discipline to volatile, less-regulated markets.

## Market making under stress

When crypto markets crash—as they periodically do—market makers vanish. During sharp drawdowns or liquidity crises (e.g., March 2020 "Black Thursday," or the collapse of major exchanges like FTX), market makers pull their quotes to avoid catastrophic losses. Spreads widen to 1–3% or more, and large traders find their orders can't fill, or execute at terrible prices. This is a feature, not a bug: market makers are not obligated to provide liquidity at a loss. But it highlights the fragility of crypto liquidity in tail-risk scenarios.

Some [alternative trading systems](/alternative-trading-system/) and decentralised exchanges (DEXs) try to solve this by using automated [liquidity pools](/distributed-ledger/) and incentive schemes, but they introduce different trade-offs: less discretion, sometimes wider spreads, and novel risks. Traditional market makers remain the gold standard for tight, reliable liquidity.

## See also

<div class="wiki-seealso">

### Closely related

- [Market maker (stocks)](/market-maker-trading/) — How traditional exchanges maintain liquidity
- [Bid-ask spread](/bid-ask-spread/) — The cost you pay for immediacy
- [Futures contract](/futures-contract/) — A hedging tool market makers use to offset spot positions
- [Cryptocurrency exchange](/cryptocurrency-exchange/) — The venues where crypto market makers operate
- [Alternative trading system](/alternative-trading-system/) — Non-exchange venues where market making also happens
- [Inventory turnover](/inventory-turnover/) — A financial metric; related to how often a market maker cycles inventory

### Wider context

- [Algorithmic trading](/algorithmic-trading/) — High-speed, rule-driven trading broadly
- [Price discovery](/price-discovery/) — How market makers and traders collectively reveal true prices
- [Liquidity risk](/liquidity-risk/) — The danger of being unable to sell at a fair price
- [Volatility smile](/volatility-smile/) — Option pricing phenomenon; relevant to crypto options market makers

</div>
