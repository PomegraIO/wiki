---
title: "Circuit Breaker Halt Levels Explained"
description: "Circuit breaker halt levels are automatic trading pauses triggered when the S&P 500 falls 7%, 13%, or 20% in a single day, halting equities and index futures for 15 minutes or closing the market."
keywords:
  - circuit breaker halt levels
  - circuit breaker explained
  - market circuit breakers
  - trading halt
  - s&p 500 decline threshold
  - market pause rules
  - automatic halt mechanism
---

*A **circuit breaker** is an automatic halt in U.S. equity trading triggered when the [S&P 500](/sp-500-index/) drops by a set percentage in a single trading session. The halt pauses most trading for 15 minutes, letting volatility cool before the market resumes—or closes for the day if the decline is severe enough. These rules have existed since the 1988 crash and are designed to prevent panic liquidation cascades.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Circuit Breaker Halt Levels — key facts</div>

<img src="/svg/markets.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Three threshold declines trigger automatic trading halts at 10:00 a.m., 13:00, or market close.</div>

|   |   |
|---|---|
| **Level 1 (7% decline)** | 15-minute halt, 10:00 a.m.–3:25 p.m. |
| **Level 2 (13% decline)** | 15-minute halt, 10:00 a.m.–3:25 p.m. |
| **Level 3 (20% decline)** | Market closes for the remainder of the day |
| **Basis** | S&P 500 index points from prior day close |
| **Halt applies to** | Equities, ETFs, [futures contracts](/futures-contract/) on broad indices |
| **Cooldown purpose** | Reduce panic, improve price discovery, clear order queues |

</aside>

## The three halt thresholds

Circuit breakers operate on a tiered system, with each threshold tied to an absolute S&P 500 point decline from the previous day's close.

**Level 1** activates when the index falls **7%** during a single trading day. If the S&P 500 closed at 5,000 and drops to 4,650 (a 350-point decline), the halt triggers. When Level 1 activates between 10:00 a.m. and 3:25 p.m., trading pauses for 15 minutes. Orders stop executing; the market hangs suspended. Traders receive the last execution price and can plan their next move. At 3:25 p.m., Level 1 halts are disabled—any further decline at that time won't trigger a pause, allowing the market to close normally.

**Level 2** triggers at **13%** decline—for a 5,000-point S&P 500, that's a 650-point drop to 4,350. Like Level 1, it halts trading for 15 minutes if it occurs before 3:25 p.m. However, if Level 2 activates at or after 3:25 p.m., the market closes immediately and doesn't reopen that day. This protects against an uncontrolled market free-fall in the final minutes.

**Level 3** activates at **20%** decline. A 5,000-point S&P at a 1,000-point drop (to 4,000) triggers this threshold. There is no 15-minute pause at Level 3. The market closes immediately, ending the trading day. The reasoning is clear: a 20% one-day decline is extreme, panic is likely already underway, and further trading would risk cascade failures in clearing and credit systems.

## How the percentages are calculated

The percentage decline is measured from the **previous day's closing price**, not from an intra-day peak. This prevents minor morning weakness from triggering false halts. If the S&P 500 closed yesterday at 5,000, opens today at 4,900 (down 2%), then rallies to 5,050 by noon, no circuit breaker fires—the market moved *up* from where the calculation resets daily.

The S&P 500 index value itself—not individual stocks—is the trigger. The exchange calculates this value in real time using the most recent quote for each of the 500 constituent stocks. During extreme volatility, the index calculation itself can face challenges (gaps in data, halted stocks), but modern systems are designed to handle this.

## What happens during the 15-minute halt

When a Level 1 or Level 2 breach occurs, the [New York Stock Exchange](/new-york-stock-exchange/) and [NASDAQ](/nasdaq/) halt trading in all equities and most [ETFs](/etf/). Simultaneously, [futures contracts](/futures-contract/) on broad indices (the [S&P 500](/sp-500-index/) e-mini, the Micro E-mini, Russell 2000) also halt. This prevents traders from circumventing the halt by trading the same economic exposure via index futures.

Traders cannot submit new orders, and existing orders are frozen. Selling pressure pauses. Importantly, this gives [market makers](/market-maker-trading/) and specialists a window to reassess valuations and prepare for the resumption. Prices often stabilize during the halt as the panic subsides.

After 15 minutes, trading resumes at the last traded prices. Some traders rush back in; others sit tight. Often, the resumption is calmer than the moment the halt was triggered. However, if the market continues to fall after resumption and hits Level 2, another halt is triggered.

## The 3:25 p.m. cutoff and market closure rules

The 3:25 p.m. rule exists because the regular market close is 4:00 p.m. A 15-minute halt triggered at 3:26 p.m. would extend into [after-hours trading](/after-hours-trading/). To avoid confusion and ensure a clean close, halts triggered at or after 3:25 p.m. do not pause trading; instead, if Level 2 is breached, the market closes outright.

Level 3 (20% decline) closes the market immediately, regardless of time. This is a nuclear option, deployed only in catastrophic scenarios. The last Level 3 halt occurred on October 19, 1987 ("Black Monday"), when the Dow fell 22% in a single day. Modern circuit breakers have prevented any Level 3 breach since their inception.

## Trading in halted and closed markets

When the primary market halts, some trading can continue via [over-the-counter](/over-the-counter-market/) dealers and [alternative trading systems](/alternative-trading-system/) (dark pools, ATS), but volume is thin and spreads widen sharply. Most retail investors cannot access OTC trading, so halts are effectively binding for them.

If the market closes due to Level 3, the next day opens normally (or with an opening delay if pre-market sentiment is dire). Trading does not resume at 4:00 p.m. the same day. Overnight, investors digest news, and markets in other regions (Asia, Europe) may have already reacted. By the next open, some of the volatility is priced in.

## Historical context and criticism

Circuit breakers were introduced after Black Monday in 1987, when the Dow fell 22% in a single day and clearing systems nearly failed under the transaction load. Regulators wanted a mechanical way to prevent panic cascades—a "circuit" that breaks when current flows too hot, shutting down the system before it overheats.

Some critics argue that halts merely postpone the inevitable and can create a "gap down" effect: after a 15-minute halt, bad news is fresh and prices fall again immediately upon resumption. Others defend them as necessary shock absorbers, preventing margin calls and credit stress from cascading into systemic failure. Empirical studies are mixed; halts do appear to reduce panic volatility but don't eliminate it.

## See also

<div class="wiki-seealso">

### Closely related

- [S&P 500 Index](/sp-500-index/) — The market indicator that triggers circuit breaker thresholds
- [Volatility](/historical-volatility/) — The intra-day price swings that circuit breakers are designed to cool
- [Market Maker Trading](/market-maker-trading/) — Who steps in during halts and resumptions to stabilize prices
- [Futures Contract](/futures-contract/) — Index futures that also halt when equities do
- [How Trade Matching Engines Work](/how-trade-matching-engines-work/) — The execution mechanisms halted during pauses

### Wider context

- [Stock Market](/stock-market/) — The broader ecosystem governed by circuit breaker rules
- [Securities and Exchange Commission](/securities-and-exchange-commission/) — Regulates circuit breaker thresholds and halt procedures
- Market Panic and Cascades — The systemic risk circuit breakers are designed to prevent
- [Black Monday](/black-monday-1987/) — The 1987 crash that prompted circuit breaker adoption

</div>
