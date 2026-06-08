---
title: "Circuit Breakers in Global Stock Markets"
description: "How circuit breakers halt trading during sharp declines and how their design, thresholds, and durations vary across global exchanges."
keywords:
  - circuit breakers
  - how do circuit breakers work in global stock markets
  - trading halts
  - market circuit breakers
  - circuit breaker thresholds
  - exchange trading rules
image: "/svg/markets.svg"
---

*When a stock or index drops sharply in a short time, **circuit breakers** pause trading—a mechanical safeguard intended to prevent panic selling and give markets time to breathe—yet the triggers, halt durations, and scope differ significantly between the U.S., Asia, Europe, and emerging markets, reflecting each region's risk appetite and past crises.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Circuit Breakers — key facts</div>

<img src="/svg/markets.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Sharp declines trigger automatic pauses to prevent cascading panic and give traders time to assess.</div>

|   |   |
|---|---|
| **U.S. S&P 500 thresholds** | Level 1: 7%, Level 2: 13%, Level 3: 20% intraday decline; halts 15 min, 15 min, or close for day |
| **Scope** | Most commonly applied to broad indices (S&P 500) or individual stocks with unusual volume/volatility |
| **Individual stock halts** | Usually triggered by large single-stock moves (10–20%+) or extreme volatility surges |
| **Global variation** | Asia uses tighter thresholds (5–10%); Japan has a tiered system; India uses 10–20%; circuit breaker durations vary from 5–30 minutes |
| **Purpose** | Prevent [panic selling](/loss-aversion/), allow information to disseminate, cool order books |
| **Criticism** | May amplify volatility if triggers bunch trades at the restart; can strand investors trying to exit |

</aside>

## What circuit breakers do

A **circuit breaker** is a rule that automatically halts trading when an asset or market moves too sharply in too short a time. The pause is mechanical—not a human decision—triggered by a drop below a numerical threshold. During the halt, no trades are executed, but investors can submit orders that will execute when trading resumes.

The original intent, born from the [1987 Black Monday crash](/stock-market/) when the S&P 500 fell 20% in a single day, was to prevent a stampede. In a panic, [market makers](/market-maker-trading/) withdraw, spreads widen, and sellers overwhelm buyers, causing further drops. A brief trading halt gives [information to disseminate](/price-discovery/), investors to re-evaluate, and [market makers](/market-maker-trading/) to rebuild liquidity before resuming.

The theory is sound: if a stock falls 15% in one minute due to a false news flash that is immediately corrected, circuit breakers allow the correction to reach traders before they panic-sell at the bottom. In practice, circuit breakers work best for single-stock volatility (which is genuinely often false alarms) and less predictably for broad market declines (which reflect real uncertainty).

## The U.S. framework

The **U.S. equity market** has three circuit breaker levels for the S&P 500 index:

- **Level 1**: 7% decline from the previous day's close → 15-minute halt (any time of day)
- **Level 2**: 13% decline from the previous day's close → 15-minute halt (any time of day)
- **Level 3**: 20% decline from the previous day's close → trading halts for the rest of the day

These thresholds have been in place since 2012 and have been tested only a handful of times. On March 16, 2020 (during COVID), Level 1 triggered four times in a single session. On August 5, 2011, during the debt ceiling crisis, Level 1 triggered twice. Each time, the 15-minute pause allowed volatility to settle.

Individual **stock circuit breakers** are separate: under SEC Rule 10b-1, a stock trading more than 5 million shares per day can be halted if it moves 10% or more in a 5-minute window. A stock with low regular volume might trigger at a smaller percentage move. The halt lasts 5 minutes, after which trading resumes.

## Variation across global markets

**Asia's markets are tighter**. The Hong Kong Stock Exchange uses 5%, 10%, and 15% thresholds with 15-minute halts. The Tokyo Stock Exchange uses 5% and 10% thresholds. South Korea's KOSPI uses a 10% threshold. **India's NSE** uses 10%, 15%, and 20% thresholds. These lower thresholds reflect smaller markets that can be more vulnerable to volatility swings and regulatory preference for caution.

**European exchanges** are mixed. **Euronext** applies 5% and 10% thresholds for [Level 2 circuit breakers](/stock-market/) during the trading session. The **London Stock Exchange** uses similar bands. Halts are typically 5–15 minutes.

**Emerging markets** vary widely. **Brazil's B3** uses 10% thresholds. **Mexico's BMV** uses 5%, 10%, and 15% tiers. **Shanghai and Shenzhen** use 5% and 7% thresholds and apply them strictly—the 2015 devaluation spike triggered multiple halts. This reflects China's regulatory desire to control volatility tightly.

## How individual stock halts work

When a stock moves too fast, brokers and exchanges halt trading to investigate. A **stock halt** might be triggered by:

- An extreme price move (10–20%+) in a few minutes
- Unusual volume unmatched by a recent news event
- A news announcement (a company temporarily halts trading to allow news to disseminate fully)
- A regulatory inquiry or audit

The halt prevents further trading orders from being placed, though outstanding orders (limit orders, stop-losses) remain in the queue. Typically, a halt lasts 5–15 minutes. Brokers are required to notify the public of the halt reason and expected duration.

Many panic-sellers submit orders right at the open of a halt-release, causing a volume spike that can briefly push the stock lower. Sophisticated traders know this and may delay their orders, causing a second smaller wave of activity after the initial shock.

## The debate: do circuit breakers work?

**Evidence is mixed**. Studies of the 2020 COVID crash show that Level 1 halts did allow markets to re-assess before falling further. The 15-minute pauses prevented even steeper declines and gave news to propagate. However, some data suggests that halts can also **bunch selling** at the restart—traders who wanted to exit at any price during the halt now try to exit simultaneously at the open, creating a fresh sell-off that might not have happened without the halt.

For **individual stocks**, the case is stronger. A stock that drops 15% in one minute due to a single large trade or fat-finger error (a typo that sends a huge order into the market) genuinely benefits from a halt. The halt allows brokers to correct the error, and it prevents other traders from compounding the damage by panic-selling into a disorderly market.

For **broad index declines** during genuine crises—a banking collapse, a geopolitical shock—circuit breakers have less impact. If the market is falling because something terrible is actually happening, a 15-minute pause only delays the decline; it doesn't prevent it. Investors may re-assess and decide the situation is even worse, accelerating the fall after the halt expires.

## Historical context and regulatory intent

Circuit breakers were mandatory after **Black Monday 1987**, when the S&P 500 fell 22% in one day and the market came close to completely seizing up. The crash prompted U.S. regulators and exchanges to design automatic speed bumps. The 2008 financial crisis and the 2020 COVID shock both saw circuit breakers activate multiple times and were credited with preventing even more severe declines.

However, the **2010 Flash Crash**—when the S&P 500 dropped 1,000 points in minutes due to a data glitch and [algorithmic trading](/algorithmic-trading/) interactions—occurred without any circuit breaker being triggered at the index level (individual stocks were halted, but the index was not). This prompted regulators to re-examine whether circuit breaker thresholds were too high or too slow to respond to new trading technologies.

The current thresholds (7%, 13%, 20% for the S&P 500) were set in part to ensure that normal [volatility](/volatility-smile/) and [market corrections](/bear-market/) don't trigger false pauses, while genuinely rare crises (drops exceeding 10–20%) do get a pause.

## Criticisms and edge cases

**Front-running the restart**: Sophisticated traders know that when trading resumes after a halt, there is often a volume spike and fresh selling. They may place limit orders just above the low hit during the halt, expecting to profit when the stock bounces 1–3% after the restart before falling again. This can create artificial bounciness.

**Stranded traders**: A retail investor trying to sell a stock during a halt has their order queued but cannot execute. If the stock gaps down significantly at the restart, the trader's limit order may be filled at an unexpectedly low price—or not filled at all if the stock resumes well below the limit.

**Asymmetric information**: During a halt, major news is usually disseminated to the market, but some traders (those with professional news feeds, proximity to exchanges) learn of it faster than others. When trading resumes, the faster traders have an advantage.

**Globalmarkets**: If a stock is dual-listed on two exchanges in different time zones, a halt on one exchange doesn't prevent trading on the other. An investor can avoid a halt on the home exchange by trading the [ADR](/adr/) or foreign listing. This undermines the halt's intended calm.

## The lasting principle

Circuit breakers are not a cure-all, but they're a useful tool for managing extreme volatility and preventing technical accidents from becoming financial crises. The thresholds across markets reflect each region's **risk tolerance**, **market structure**, and **past experiences**. A market that has experienced flash crashes and fat-finger errors (like the U.S.) uses broader thresholds and is more selective about halts. A market that is smaller and more vulnerable to sudden shocks (like some emerging markets) uses tighter thresholds. Neither approach is objectively "correct"; they're choices reflecting different priorities.

For traders, understanding circuit breakers is essential: they're another rule of the game that affects [price discovery](/price-discovery/), [execution costs](/bid-ask-spread/), and the timing of entry and exit.

## See also

<div class="wiki-seealso">

### Closely related

- [Price discovery](/price-discovery/) — how markets arrive at fair value despite disruptions
- [Volatility smile](/volatility-smile/) — market pricing of tail risk and sudden moves
- [Algorithmic trading](/algorithmic-trading/) — automated trading that can trigger cascade effects
- [Bid-ask spread](/bid-ask-spread/) — how market makers price liquidity risk
- [Market order](/market-order/) — the aggressive execution that can trigger moves
- [Bear market](/bear-market/) — prolonged decline vs. sharp intraday drop

### Wider context

- [Stock market](/stock-market/) — the ecosystem circuit breakers protect
- [Market maker trading](/market-maker-trading/) — who supplies liquidity during stress
- [New York Stock Exchange](/new-york-stock-exchange/) — where U.S. circuit breakers are enforced
- [Securities and exchange commission](/securities-and-exchange-commission/) — the regulator behind U.S. rules
- [Hong Kong Stock Exchange](/hong-kong-stock-exchange/) — major Asia venue with its own circuit breaker design
- [Hedge fund](/hedge-fund/) — sophisticated traders who navigate halts strategically

</div>
