---
title: "What Happens During a Market Halt"
description: "When a market halt is triggered, trading freezes, pending orders cancel, quotes are locked, and a reopening auction determines the next price—all within minutes."
keywords:
  - market halt definition
  - what happens during a market halt
  - stock trading halt mechanics
  - trading halt reopening auction
  - circuit breaker market halt
  - order cancellation trading halt
image: /svg/markets.svg
---

*When **a market halt occurs**, trading in one or more stocks—or in the entire market—stops abruptly. Orders freeze in place, asking and bidding quotes lock, and information systems issue alerts. Minutes later, if conditions permit, a reopening auction establishes a new price and trading resumes. The mechanism exists to prevent panic selling, buy time for information to disseminate, and let volatility cool.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Market Halt — key facts</div>

<img src="/svg/markets.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">A controlled pause in trading that resets expectations and prices.</div>

|   |   |
|---|---|
| **Triggers** | Volatility threshold (e.g., 10% move in 5 min), news halt, technical failure |
| **Duration** | 5 minutes (single-stock halt) to 15+ minutes (market-wide halt) |
| **Order fate** | Cancelled at halt; resubmitted in reopening auction |
| **Who can trigger** | Exchange (automatic), SEC (emergency), stock issuer (rare) |
| **Reopening method** | Auction matching buy and sell orders at one price |
| **Frequency** | Single-stock halts: daily; market-wide: rare (last major one: Aug 2015) |

</aside>

## The trigger: why a halt starts

Halts are initiated either automatically or by human decision:

**Volatility halt** (most common): If a stock moves more than a threshold percentage—typically 10%—within a short window (usually 5 minutes), the exchange's electronic system automatically halts it. The logic is straightforward: a sharp move may signal news that hasn't yet disseminated to all traders, or it may reflect a data error or fat-finger trade that hasn't been noticed.

**News halt**: A company issues material information (acquisition news, earnings surprise, insider trading probe, bankruptcy filing, executive death). To give all market participants a fair chance to absorb the news before trading resumes, the issuer or exchange halts trading, sometimes for 10–30 minutes or longer.

**Technical halt**: The exchange's systems fail, data feeds go down, or a circuit breaker is triggered at the market-wide level (see below).

**SEC emergency halt**: In extreme cases (e.g., order routing error, market disruption, credible fraud), the [SEC](/#) can halt trading in a security for up to ten business days.

Once triggered, the exchange announces the halt via electronic alert to all market participants and the financial press.

## What happens to your orders

The moment a halt is announced, all pending orders on the order book are **cancelled**. This is the single most important consequence for traders. If you entered a limit order to sell at $95 before the halt, that order vanishes. You cannot execute it during the halt. You cannot modify it. It's gone.

Cancelled orders are not automatically resubmitted when trading resumes. Some [brokers](/#) offer features to resubmit orders at reopening, but this is optional and broker-specific—never automatic.

If you have an open buy or sell order and a halt is called, check your broker's alert or terminal immediately to confirm the cancellation and decide whether to resubmit in the reopening auction.

## The halt window: everything freezes

During the halt, trading is completely suspended. The ticker stops. No market orders execute. No new [bid-ask spread](/bid-ask-spread/) updates; the last quoted price is frozen.

Block trades, after-hours trading, and alternative trading venues (dark pools, electronic communication networks) may continue operating, but the primary exchange is silent.

Information flows, however. News keeps breaking. Research firms and brokers release comments. Social media explodes. By the time the halt ends, market sentiment may have shifted dramatically from the moment of the halt call.

Traders use this time to reassess. Some want to sell, some to buy, some to get out entirely.

## The reopening auction

After 5–15 minutes (depending on the reason for the halt), the exchange moves to the **reopening auction**—a structured process to establish the next price and resume trading fairly.

Here's the sequence:

1. **Auction entry window**: The exchange announces that traders may submit new orders for a brief period (typically 30–90 seconds). These orders are only valid for the reopening auction; they don't rest on the book during the halt.

2. **Matching**: The exchange's matching engine collects all submitted bids and asks. It then calculates a single price—the **opening price**—at which the maximum volume of shares can trade. This price might be far from the pre-halt price; that's the point. It reflects what the market is actually willing to do *right now*.

3. **Publication**: The exchange announces the reopening price and the volume transacted at that price (e.g., "Reopening at $91.50, 2.3M shares traded").

4. **Trading resumes**: Orders resume routing normally. New trades execute at the reopening price or at whatever price the next buyer and seller agree on.

Some exchanges offer price collars around the pre-halt price (e.g., the reopening price cannot be more than 5% away from the last traded price). This prevents a vacuum of information from causing a wild gap, which protects passive holders but may delay reopening if supply and demand are too far apart.

## Market-wide halts: circuit breakers

When the entire market—not just one stock—crashes in minutes, [circuit breakers](/#) halt all trading temporarily:

- **Level 1** (S&P 500 down 7% from previous close): 15-minute halt.
- **Level 2** (down 13%): 15-minute halt.
- **Level 3** (down 20%): Halt for the remainder of the trading day.

These thresholds have triggered only a handful of times in modern history. The most memorable is **August 24, 2015**, when the S&P 500 fell 3.9% in the opening minutes, triggering a Level 1 halt on the [NYSE](/#). The market reopened 15 minutes later, and the session recovered most of the loss by close.

Circuit breakers exist to prevent a self-reinforcing panic: a big drop causes forced selling (stop losses, margin calls), which causes another drop, which triggers more selling. The halt gives human traders and risk managers time to regroup.

## Who benefits, who loses

**Winners**: 
- Traders with stale limit orders that become irrelevant after news; they're automatically cancelled, preventing an unintended execution.
- Long-term holders; the pause prevents panic-driven washouts.
- The market itself; it avoids the spiral of electronic trading robots amplifying a move into a crash.

**Losers**:
- Traders trying to exit; if you want to sell a crashing stock and a halt is called, you can't, and information might deteriorate further during the halt.
- Option holders; the halt freezes options prices, potentially locking in losses.
- Arbitrageurs; the halt can break the synchronization between a stock and its ETF or options, creating mispricings.

## Why halts are controversial

Some argue halts are outdated. Modern markets move in milliseconds; a 5-minute halt is an eternity, and the reopening auction may not reflect the true fair price if information is still asymmetric.

Others argue halts are essential. Without them, [algorithmic trading](/algorithmic-trading/) and [momentum](/momentum-investing/) strategies could turn a 10% correction into a 40% crash in seconds, with no human oversight.

Most markets have settled on a middle ground: automatic halts for single stocks, circuit breakers for broad sell-offs, and limits on how frequently halts can be triggered (to prevent repeated halt-and-reopen cycles that exhaust traders).

## See also

<div class="wiki-seealso">

### Closely related

- [Circuit breaker](/circuit-breaker/) — the market-wide halt mechanism triggered at 7%, 13%, 20% drops
- Reopening auction — the orderly process to establish a fair price and resume trading
- Order cancellation — what happens to pending orders when a halt is called
- Trading halts news — why companies request halts for material announcements
- [Bid-ask spread](/bid-ask-spread/) — frozen during a halt; updates when trading resumes
- Volatility — the trigger for most single-stock halts
- [Algorithmic trading](/algorithmic-trading/) — the force that halts aim to slow during crashes

### Wider context

- [Stock exchange](/stock-exchange/) — where halts are managed
- [Market maker](/market-maker-trading/) — the participants most affected by halts
- [Liquidity](/liquidity-risk/) — reduced during a halt; restored at reopening
- [Price discovery](/price-discovery/) — the process interrupted by halts and resumed at reopening
- [Bear market](/bear-market/) — the condition in which halts are most frequent

</div>
