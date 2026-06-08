---
title: "Limit Up-Limit Down Rule"
description: "The US equity circuit breaker that pauses trading when a stock's price moves too far (typically 5–10%) within five minutes, preventing crash-like volatility."
keywords:
  - limit up limit down
  - circuit breaker
  - trading halt
  - volatility rule
  - price bands
  - flash crash
image: "/svg/regulation.svg"
---

*On 6 May 2010, the stock market crashed nearly 1,000 points in minutes—the "Flash Crash"—and recovered almost as quickly. Prices for individual equities swung wildly, some trading at pennies. To prevent such extreme intraday volatility, the SEC introduced the **Limit Up-Limit Down Rule**, a "circuit breaker" that halts trading in a stock when its price moves too far (typically 5–10% depending on the stock's price level) within five minutes. The rule is a hard stop: when a stock hits its limit, no trades can occur at any price beyond the limit band until the band resets or trading resumes. It is one of the few automated, mechanical constraints on the US equity market.*

<div class="wiki-hatnote">

For the related rule that protects order routing, see [Reg NMS Order Protection Rule](/reg-nms-order-protection/). For broader volatility management, see [circuit breaker](/), [volatility](/), and [stress testing](/stress-testing/).

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Limit Up-Limit Down Rule — key facts</div>

<img src="/svg/regulation.svg" alt="An abstract editorial mark for regulation and governance." />

<div class="wiki-infobox-caption">Automated price bands that pause trading during extreme intraday moves.</div>

|   |   |
|---|---|
| **What it is** | A rule that halts trading in a stock when its price moves 5–10% (depending on price tier) in five minutes |
| **Enacted** | 2012 (pilot), 2013 (permanent) following the 2010 Flash Crash |
| **Regulator** | [Securities and Exchange Commission (SEC)](/securities-and-exchange-commission/) in coordination with exchanges |
| **Price tiers** | Tier 1 stocks ($3+): 5% band; Tier 2 stocks (<$3): 10% band |
| **Halt duration** | 5 minutes; after which the band "refreshes" and trading resumes if price is within the new band |
| **Applies to** | US equities listed on [NYSE](/new-york-stock-exchange/) and [Nasdaq](/nasdaq/), and [ETFs](/etf/) |
| **Complementary rule** | [Reg NMS Order Protection Rule](/reg-nms-order-protection/) |

</aside>

## Why the Flash Crash exposed a gap in market safeguards

Before 2010, the US stock market had a market-wide circuit breaker: if the [S&P 500](/sp-500-index/) fell 20% in one day, trading paused. But there was no circuit breaker for individual stocks. On the afternoon of 6 May 2010, a large algorithmic sell order in [index futures](/sp-500-index/) triggered a cascade of selling. Liquidity evaporated, prices for individual stocks plummeted, and some equities traded at absurdly low prices—one stock briefly at $0.01—before recovering. The market rebounded nearly as fast as it crashed, but not before billions in value seemed to vanish and reappear.

The incident revealed a critical flaw in market design: modern [algorithmic trading](/algorithmic-trading/) and [electronic communication networks](/alternative-trading-system/) could move prices so fast that no human trader could react, and no existing safeguard could kick in. The circuit breaker for the overall market was too coarse—it protected the index but not individual investors in specific stocks. Some traders lost money when their orders filled at crisis prices; others profited from the dislocation.

The SEC concluded that individual stocks needed their own circuit breakers. The goal was not to prevent trading or to set "fair" price limits, but to force a pause—to give markets, traders, and systems time to absorb shocks and for new information to propagate before trading resumed.

## How the rule operates: bands that refresh

When a stock's price moves 5% (or 10% for low-priced stocks) within a five-minute window, trading is halted. No transaction can execute at any price beyond the limit band—if the limit-up level is $51.00, no sell order can be executed at $51.00 or higher; if the limit-down level is $49.00, no buy order can execute at $49.00 or lower. This is strict: a trader cannot bid for shares at $50.50 if the stock is limit-down at $49.00. The order is rejected or queued.

The halt lasts five minutes. During that time, market participants, algorithms, and news systems can catch up. Orders may arrive reflecting new information or revised risk assessments. After five minutes, trading resumes. If the stock's price is still within the original band (e.g., it opened the day at $50, moved to limit-down at $47.50, and is trading at $48 when the five-minute halt ends), the band resets based on the reference price at the moment trading resumes.

The reference price used to calculate the band is updated every five minutes, so the bands are continuously "refreshing". This prevents the rule from freezing a stock at an artificially low or high price. If a stock gaps down 10% and halts, but new information justifies an even lower price, the bands will widen or shift after five minutes to allow price discovery to continue.

## Price tiers and proportional protection

Stocks are divided into two tiers for LULD purposes. **Tier 1** stocks—those priced at $3 or higher and meeting certain [market capitalization](/market-capitalization/) and trading volume thresholds—have a 5% price band. These are the most liquid stocks: the [S&P 500](/sp-500-index/) constituents, large-cap [ETFs](/etf/), and other highly traded equities. A Tier 1 stock at $100 would have limit-up at $105 and limit-down at $95.

**Tier 2** stocks—lower-priced equities, penny stocks, and less liquid issues—have a 10% band. A Tier 2 stock at $3 has limit-up at $3.30 and limit-down at $2.70. The wider band reflects the fact that lower-priced stocks are more prone to wider percentage swings and have less continuous trading; a tighter band could cause excessive halts. The threshold between tiers is $3 per share.

## Effectiveness and unintended consequences

Since the rule's implementation, dramatic "crash-like" single-stock moves within minutes have become rare. The rule clearly dampens extreme intraday volatility and provides breathing room. However, it also has costs and quirks.

One criticism is that the rule may sometimes delay price discovery. If a stock receives very bad news and should trade much lower, the circuit breaker imposes a five-minute pause that locks in stale prices. Some traders and market makers argue this allows uninformed traders to exit at better prices than they should get, and slows the market's ability to respond to shocks. The SEC defends the pause as essential for order matching systems to process the flood of new information.

Another effect is the "LULD tail risk" for traders using [algorithmic](/algorithmic-trading/) and [high-frequency trading](/), strategies. Algorithms must be programmed to handle trading halts; an algorithm that expects continuous trading may malfunction if a stock halts unexpectedly. Some traders have exploited this by triggering limit moves in low-liquidity stocks, causing a halt and then profiting from the resulting repricing or algos scrambling to cancel orders.

The rule has also evolved. In 2016, the SEC expanded LULD to cover nearly all US equities and [ETFs](/etf/), tightening the earlier thresholds. This broadened protection but also increased the frequency of halts, particularly for volatile or illiquid stocks.

## Limits of a mechanical circuit breaker

Importantly, the Limit Up-Limit Down rule does not address systemic flash crashes. It protects individual stocks but is only one layer of circuit breakers. The market-wide circuit breaker (triggered when the [S&P 500](/sp-500-index/) falls 20%) remains in place. [Volatility](/), [leverage](/), and correlated selling by many traders can still cause broad market declines that halts of individual stocks cannot prevent.

Nor does the rule solve the underlying cause of flash crashes: [liquidity risk](/liquidity-risk/), the failure of [market makers](/market-maker-trading/) to provide bids and offers during stress, and the concentration of risk in correlated strategies. A circuit breaker pauses trading but does not force [liquidity](/); when trading resumes, if risk is still concentrated and supplies of willing buyers or sellers are thin, prices can still move dramatically.

The rule is also mechanical and inflexible. It does not distinguish between "good" volatility (e.g., a firm beating earnings, causing a large move) and "bad" volatility (e.g., a data error or cascading margin calls). Any move beyond the threshold triggers a halt. This has the virtue of consistency but the drawback of bluntness.

## See also

<div class="wiki-seealso">

### Closely related

- [Circuit breaker](/), — automated trading halts at the market-wide level
- [Volatility](/), — the price variation the rule constrains
- [Algorithmic trading](/algorithmic-trading/) — trading strategies affected by halts and LULD mechanics
- [Liquidity risk](/liquidity-risk/) — the underlying danger that LULD aims to prevent
- [Market maker](/market-maker-trading/) — liquidity providers affected by halt mechanics

### Wider context

- [Securities and Exchange Commission (SEC)](/securities-and-exchange-commission/) — the regulator that enforces LULD
- [Flash Crash](/), — the 2010 event that motivated the rule
- [Reg NMS Order Protection Rule](/reg-nms-order-protection/) — complementary order-routing rule
- [Stock market](/stock-market/) — the venue where LULD applies
- [Stress testing](/stress-testing/) — how regulators assess resilience to flash-crash-like events

</div>
