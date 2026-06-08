---
title: "Exchange Circuit Breaker Rules Explained"
description: "How do exchange circuit breakers work: percentage-drop thresholds that halt trading temporarily during extreme volatility to prevent panic selling."
keywords:
  - how do exchange circuit breakers work
  - trading halt circuit breaker
  - market circuit breaker
  - circuit breaker rules
image: "/svg/institutions.svg"
---

*When a **stock market** drops sharply in a short span, exchanges impose automatic **circuit breaker** halts—temporary pauses in trading designed to let investors regain composure, prevent panic cascades, and allow fundamentals to reassert themselves. These rules exist because past crashes taught regulators that unlimited selling can become self-fulfilling.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Circuit Breaker Rules — Key Facts</div>

<img src="/svg/institutions.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Markets halt at percentage declines; pauses lengthen if drops accelerate; rules vary by country and apply to indices, sectors, and individual stocks.</div>

|   |   |
|---|---|
| **Level 1 halt** | 7% decline from prior close; 15-minute trading pause |
| **Level 2 halt** | 13% decline from prior close; 15-minute pause |
| **Level 3 halt** | 20% decline from prior close; market closes for remainder of day |
| **Who triggers** | [S&P 500](/sp-500-index/) index movements; also individual stock halts by [SEC](/securities-and-exchange-commission/) |
| **Typical duration** | 15 minutes for levels 1–2; permanent (day-end) for level 3 |
| **Regional variations** | EU, Asia, and other exchanges use similar but slightly different thresholds |
| **Time windows** | US rules apply only 9:30 a.m.–3:50 p.m. ET; after-hours halts rare |

</aside>

## Why Circuit Breakers Exist

The genesis of circuit breaker rules is the **1987 stock market crash**—Black Monday, October 19. The [S&P 500](/sp-500-index/) fell 22.6% in a single day, the largest one-day percentage decline in market history. Selling begat more selling; [margin calls](/margin-call-forex/) forced liquidation; liquidity evaporated. There was no pause, no "reset." The market simply crashed.

After 1987, regulators recognized that **speed and panic are feedback loops**. When prices fall fast enough to trigger the perception of a systemic crisis, investors sell reflexively, which drives prices down further, which triggers more panic. A brief pause—15 minutes—can break the cascade. In a quarter hour, news can be digested, advisors can be reached, and sellers can distinguish between panic-driven declines and actual fundamental deterioration.

Circuit breakers also serve an operational function: they give trading systems, clearing firms, and brokers a moment to process orders, sync balances, and prevent technical failures from amplifying market stress.

## US Circuit Breaker Thresholds and Mechanics

The US [Securities and Exchange Commission](/securities-and-exchange-commission/) and [FINRA](/finra/) enforce a three-tier system based on the [S&P 500](/sp-500-index/) index level:

**Level 1: 7% decline**
If the S&P 500 falls 7% or more from the prior trading day's close, trading halts for 15 minutes. This threshold is designed to catch significant but not yet catastrophic declines. A 7% drop in the S&P 500 is unusual enough to warrant a pause but not so extreme as to suggest system failure.

**Level 2: 13% decline**
If the index falls 13% from the previous close (and Level 1 has already been triggered), trading halts again for 15 minutes. This signals that the decline is persistent, not a brief spike.

**Level 3: 20% decline**
A 20% fall triggers a **market-wide close for the remainder of the day**. This is intended to prevent a total collapse. Once Level 3 is breached, trading does not resume that day; investors must wait for the next open.

These thresholds are calibrated in absolute percentage terms, not in points. A company worth USD 100 billion falling USD 7 billion in value triggers the halt; a market-cap-weighted index falling 7% from the prior close triggers the halt. The mechanism is mechanical: when the [NYSE](/stock-exchange/) or NASDAQ detects that the [S&P 500](/sp-500-index/) index price has moved 7%, 13%, or 20% downward, the halt initiates automatically, without human discretion.

**Time windows**: Halts apply only between 9:30 a.m. and 3:50 p.m. ET on regular trading days. If the market opens down 7% and the Level 1 threshold is breached in the first 15 minutes, trading halts. After 3:50 p.m., the S&P 500 can fall any percentage without triggering a halt; the market is closing soon anyway. Pre-market and [after-hours trading](/after-hours-trading/) also lack circuit breaker halts, though individual stock halts (below) can still occur.

## Individual Stock Circuit Breakers

Beyond the index-level halts, the [SEC](/securities-and-exchange-commission/) also requires **individual stock circuit breakers**. If a single stock moves 10% or more in a 5-minute window, trading in that stock halts for 5 minutes.

This protects against runaway selling in a single stock due to technical glitches, false rumors, or momentary panic. A company with a major news event might see a 10%+ move; the 5-minute pause lets the news disseminate and lets brokers catch up.

## International Circuit Breaker Rules

Circuit breaker rules vary by country and exchange, but all major markets now have them.

**European Union**: The [London Stock Exchange](/london-stock-exchange/) and other EU exchanges follow similar halt thresholds (typically 5–10% declines trigger 15-minute pauses). The EU harmonized some rules after 2008 to ensure consistency across member states.

**Japan**: The Tokyo Stock Exchange halts the entire market if the Nikkei 225 index falls 7% in the morning session, and again at 13% and 20% (similar to the US). Additionally, daily trading limits exist: the index can decline at most 5% before system limits prevent further price moves downward.

**Hong Kong**: The Hong Kong Exchanges implement halts at 5%, 10%, and 15% index declines, with 15-minute pauses at the first two thresholds and a longer halt or close at the third.

**Singapore** and other regional exchanges have comparable thresholds, typically in the 5–10% range for initial halts.

## How a Circuit Breaker Halts Trading

When a halt is triggered:

1. The exchange's trading system receives the price movement alert (automated).
2. All trading in the affected security or index ceases immediately.
3. [Brokers](/broker/) cannot accept new orders during the halt.
4. Orders already placed are typically canceled or suspended (rules vary by exchange).
5. After 15 minutes (or the specified duration), trading resumes. The opening price post-halt may differ sharply from the pre-halt price, but there is no further delay.

Some exchanges allow a "reopening auction"—a brief window where buy and sell orders accumulate, then execute at a single price, preventing another immediate cliff. Others simply resume normal [limit-order](/limit-order/) and [market-order](/market-order/) processing.

## Real-World Example: February 2018

On February 5, 2018, the [S&P 500](/sp-500-index/) fell 3.8% in a single session. On February 6, the market opened lower and, within the first 30 minutes, triggered a Level 1 (7%) halt. Trading paused for 15 minutes. When it resumed, the selling had moderated; the market closed down roughly 4% but not in freefall.

Without that halt, some analysts argued, the selling could have cascaded further. The pause gave investors and [brokers](/broker/) time to absorb the news and reassess. Whether circuit breakers truly prevent catastrophe or merely delay the inevitable is debated, but they remain standard practice.

## Criticisms and Debate

**Possible delays without prevention**: Some argue that circuit breakers merely postpone a crash, not prevent it. If sentiment has genuinely shifted, the 15-minute halt does not change the underlying [fundamentals](/earnings-per-share/); it merely delays the repricing. When trading resumes, selling often accelerates.

**Artificial scarcity of information**: Critics contend that halts can trap traders with stale information during the pause—news breaks while the market is closed, and the halt prevents rapid repricing.

**[Volatility](/currency-volatility/) amplification**: Some research suggests that the certainty of a halt can itself induce panic—traders know that if they sell now, others will follow, so they rush to sell before the halt. The halt becomes a self-fulfilling prophecy.

Regulators counter that the rules, on balance, have prevented cascading failure and that the pauses, even if brief, matter. The debate continues, but the rules remain in place globally.

## See also

<div class="wiki-seealso">

### Closely related

- [Stock Exchange](/stock-exchange/) — how exchanges operate
- [S&P 500 Index](/sp-500-index/) — the index that triggers US circuit breaker halts
- [Market Order](/market-order/) — orders that execute at market price during halts
- [Securities and Exchange Commission](/securities-and-exchange-commission/) — the US regulator imposing circuit breaker rules
- [Volatility Smile](/volatility-smile/) — pricing anomalies during extreme moves

### Wider context

- [Bear Market](/bear-market/) — prolonged declines that may trigger halts
- [Stock Market Crash](/stock-market/) — historic crashes that prompted circuit breaker rules
- [Algorithmic Trading](/algorithmic-trading/) — automated strategies sensitive to halts
- [Margin Call Forex](/margin-call-forex/) — forced selling that can cascade during crises

</div>
