---
title: "Basis Order"
description: "An order to buy or sell a basket of stocks at a fixed spread relative to an index or futures contract."
keywords:
  - basis order
  - stock basket
  - index arbitrage
  - spread order
  - program trading
image: "/svg/trading.svg"
---

*A **basis order** is an instruction to trade a portfolio of stocks at a fixed spread above or below an index or futures benchmark, rather than at explicit market prices. Instead of naming individual share prices, the trader quotes a single spread and lets that gap float relative to the benchmark, absorbing the index movement as a given and pricing only the difference.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Basis Order — key facts</div>

<img src="/svg/trading.svg" alt="An abstract editorial mark for trading and order mechanics." />

<div class="wiki-infobox-caption">A single-spread instruction lets a basket move with its benchmark.</div>

|   |   |
|---|---|
| **What it is** | An order to trade a stock basket at a fixed spread (premium or discount) to a benchmark |
| **Benchmark** | Usually an [index](/sp-500-index/), [futures contract](/futures-contract/), or ETF price |
| **Primary use** | Index arbitrage, hedging, efficient portfolio rebalancing |
| **Execution** | Broker fills all legs simultaneously or via algorithm, capturing the spread |
| **Pricing** | Single basis-point spread, not individual fills per stock |

</aside>

## Why a spread, not a price

In traditional equity markets, you name a price per share. A basis order abandons that. Instead, you offer a spread—say, "I will buy this 50-stock basket at 3 basis points over the S&P 500." The actual purchase price of each stock moves with the index in real time. If the index rises 1%, your price per share rises 1% plus or minus the 3 basis-point fee. This approach matters most when you are trading large portfolios that closely track a benchmark and care mainly about the friction between you and the index, not the absolute level.

The logic is simple: if your goal is to own the index, why argue over every stock price separately? Let the benchmark do the heavy lifting. You and the broker agree only on the spread between your execution and the benchmark's closing price or real-time level.

## Index arbitrage and the rise of basis orders

Basis orders became standard in index arbitrage, where traders exploit tiny mispricings between a stock basket and its [futures contract](/futures-contract/). When the S&P 500 futures trade richer than the underlying stocks by a few basis points, an arbitrageur buys the basket and sells futures at the spread. Both sides must transact almost simultaneously; a basis order lets them do so without waiting for individual-stock fills.

Program trading in the 1980s and beyond relied heavily on basis-order mechanics. A large portfolio rebalance—say, a [mutual fund](/mutual-fund/) shifting $100 million into an index—could be submitted as a single basis order rather than 500 separate limit orders. The [market maker](/market-maker-trading/) or algorithmic broker would slice the basket, respect the spread constraint, and complete the full position within minutes.

## The broker's job

When you submit a basis order, the broker assumes significant execution risk. They must fill all (or most) of the basket at or better than the quoted spread, meaning they handle slippage on every individual stock. If the market moves against them while they're working the order, they absorb the loss. This is why basis orders typically come with a size threshold: brokers will not accept tiny basis orders because the risk-reward is unfavourable. A $200 million basis order to buy an index tracking basket is profitable; a $500,000 basis order is administratively wasteful.

The execution path varies. Some brokers use [algorithmic trading](/algorithmic-trading/) to slice the order into smaller tranches across time. Others farm portions to multiple trading desks. Large institutional traders often negotiate "not held" arrangements, where the broker is free to execute on their own schedule and discretion as long as they hit the spread by day-end or within a defined window.

## Spread as the only negotiation

The beauty and constraint of basis orders is their simplicity: there is only one number to haggle over. A bid-ask spread for a large basket can be wide (10–20 basis points or more), but once you and your broker agree on 5 basis points, the agreement is locked. Neither of you argues over Intel versus Chevron; you argue only over the cost of the entire transaction as a spread. This has made basis orders the default for index-related strategies where [price discovery](/price-discovery/) is not your primary concern.

Some institutional clients push back on basis orders, preferring to see every stock's individual execution price for transparency. This is legitimate but slower and more expensive. A basis order trades simplicity and speed for a single agreed friction number.

## Variations: different benchmarks, different uses

Not all basis orders are against the S&P 500. A portfolio manager might submit a basis order against a factor index (a [factor-investing](/factor-investing/) basket) or a custom benchmark. A real-estate manager might baseline against Russell 2000 futures. The structure stays the same: one spread, one benchmark, one execution commitment.

Basis orders also appear in [securities](/securitization/) operations when underwriters syndicate a new issue. A dealer might offer to buy a large tranche at a fixed basis to a comparable seasoned security, letting the underwriting desk hedge by short-selling that comparable on the same spread.

## See also

<div class="wiki-seealso">

### Closely related

- [Algorithmic TWAP Order](/algorithmic-twap-order/) — time-based slicing alternative to basis-order execution
- [Futures Contract](/futures-contract/) — the benchmark against which basis orders are often priced
- Program Trading — the historical driver of basis-order adoption
- Index Arbitrage — prime use case for basis orders
- [Market Maker Trading](/market-maker-trading/) — the broker role in executing basis orders

### Wider context

- [Algorithm Trading](/algorithmic-trading/) — execution methods underlying basis orders
- [S&P 500 Index](/sp-500-index/) — common basis-order benchmark
- [Exchange Traded Fund](/etf/) — baskets often traded via basis orders
- [Spread](/bid-ask-spread/) — the single negotiated number in a basis order
- [Price Discovery](/price-discovery/) — deliberately sidestepped by basis orders

</div>
