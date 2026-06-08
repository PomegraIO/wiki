---
title: "Exchange Trading Halt vs Circuit Breaker"
description: "Understand the difference between trading halts on individual stocks and market-wide circuit breakers triggered by index declines."
keywords:
  - difference between trading halt and circuit breaker
  - stock trading halt
  - market circuit breaker
  - trading halt rules
  - halt vs circuit breaker
image: /svg/institutions.svg
---

*An **exchange trading halt** is a pause on trading a single stock, typically triggered by news, an SEC investigation, or a pending announcement, while a **circuit breaker** is an automatic market-wide trading pause triggered when the S&P 500 or other index drops by a set percentage. Halts are localized and discretionary; circuit breakers are systemic and mechanical.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Trading Halt vs Circuit Breaker — key facts</div>

<img src="/svg/institutions.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Two distinct mechanisms for pausing trading to prevent cascade failures.</div>

|   |   |
|---|---|
| **Scope** | Halt: single stock; Circuit breaker: entire market |
| **Trigger** | Halt: news, pending announcement, SEC action; Breaker: index percentage drop |
| **Decision maker** | Halt: exchange rules and SEC; Breaker: automatic algorithm |
| **Duration** | Halt: typically 15 minutes to several hours; Breaker: 15 minutes per level |
| **Market-wide effect** | Halt: none; Breaker: all trading pauses |
| **Frequency** | Halt: hundreds per year; Breaker: rare (only severe declines) |
| **Lifting** | Halt: exchange staff decision; Breaker: automatic after time elapses |

</aside>

## Trading halt: single stock, temporary pause

A **trading halt** suspends all trading in a single security on all exchanges. It is designed to prevent trades when material information is about to be released—or has been released but not fully digested by the market.

### When halts happen

**Pending announcement.** A company is about to issue a significant announcement (merger, earnings surprise, management change, acquisition). The exchange halts the stock to prevent insiders from trading ahead of the news. Once the announcement is public and a reasonable time has passed, trading resumes.

**News pending clarification.** News breaks—rumor of a takeover, a major product failure, financial irregularities—but the company has not confirmed or denied it. The exchange may halt trading until the company issues an official statement.

**SEC or regulatory action.** The SEC is investigating the company for fraud or disclosure violations. A halt may be imposed while the agency gathers facts or the company is given time to respond.

**Trading volatility from an apparent error.** A stock trades at an extreme price far from recent levels, suggesting a data error, error in order entry, or system malfunction. The exchange halts to investigate.

**Compliance issues.** The company has filed late or is otherwise non-compliant with listing standards. A halt precedes potential delisting.

### How long it lasts

Most halts are temporary, lasting **15 minutes to a few hours**. The typical news-related halt runs 15 minutes while the company prepares a statement. Once a press release is issued, the stock is eligible to resume.

Some halts are longer. An SEC investigation halt might last days or weeks. A delisting halt can be permanent.

### Who controls it

The primary market where the stock trades (e.g., [NYSE](/new-york-stock-exchange/) or [Nasdaq](/nasdaq/)) has the authority to halt. The SEC can also request or order a halt. In practice, the exchange's rules specify the circumstances (pending news, volatility, etc.), and exchange staff execute the halt.

## Circuit breaker: market-wide, automatic, percentage-based

A **circuit breaker** is an automatic trading pause that applies to the entire market when a broad index drops by a specified percentage in a single trading day. It is designed to halt panic selling and give traders a moment to reassess.

### How it's triggered

The primary mechanism uses the **S&P 500** as the gauge. There are three levels:

- **Level 1 (7% decline)**: 15-minute trading halt
- **Level 2 (13% decline)**: 15-minute trading halt
- **Level 3 (20% decline)**: Trading halted for the rest of the day

If the market opens down 7% from the previous close by 3:25 p.m. ET, Level 1 triggers, all trading pauses for 15 minutes, and then resumes. If it declines another 6 percentage points (reaching 13% total) before 3:25 p.m., Level 2 triggers again with another 15-minute halt. A 20% drop triggers Level 3, and the market closes for the day.

Percentages are calculated from the **prior day's close**, not intraday swings. A recovery during the day does not reset the circuit breaker threshold.

### Why market-wide?

Circuit breakers exist because cascade panic selling can overwhelm normal market functions. In October 1987 (Black Monday), the S&P 500 fell 22% in a single day. Later research showed that as prices collapsed, sellers swamped buyers, trading systems became congested, and the decline fed on itself. Circuit breakers are meant to interrupt this feedback loop, giving traders and systems a moment to stabilize.

### Automatic and mechanical

Unlike a trading halt, which requires human judgment, a circuit breaker is triggered automatically by algorithm. The [SEC](/securities-and-exchange-commission/) and [NYSE](/new-york-stock-exchange/) monitor the index in real time. When the threshold is breached, trading stops immediately. There is no discretion; the rule applies.

### Duration and resumption

Each Level 1 or Level 2 halt lasts exactly 15 minutes. After 15 minutes, trading resumes automatically if the halt was triggered before 3:25 p.m. ET. If Level 1 or Level 2 is triggered at or after 3:25 p.m., trading is halted until the following day.

Level 3 (20% decline) halts for the remainder of the day, and the market reopens the next morning.

## Key contrasts

| Aspect | Trading Halt | Circuit Breaker |
|--------|--------------|-----------------|
| **Applied to** | One stock | Entire market |
| **Trigger** | News, investigation, volatility anomaly | Index percentage drop |
| **Decision** | Human judgment (exchange/SEC) | Automatic algorithm |
| **Frequency** | Hundreds per year | Rare (severe decline only) |
| **Duration** | Variable (15 min to days/permanent) | Fixed (15 min or remainder of day) |
| **Purpose** | Ensure fair information flow | Prevent cascade panic |

## Historical context and updates

Circuit breakers were introduced in 1988, after the 1987 crash. The percentages and mechanisms have been refined over time. The current Level 1–3 structure was established in 2013. The S&P 500 touched a circuit breaker halt only a handful of times since, most notably in March 2020 during the COVID-19 sell-off.

Trading halts have existed far longer and remain routine. The SEC's authority to halt extends even beyond exchange rules: it can impose a one-sided halt on a stock while investigation is ongoing.

## Impact on traders

A trading halt on a single stock is typically neutral to the broader market; other stocks trade normally. A circuit breaker, by contrast, stops all trading and can create a dramatic shift in sentiment and positioning when it lifts.

For [algorithmic trading](/algorithmic-trading/) and high-frequency trading firms, circuit breakers are well-understood and factored into risk models. For retail traders, a halt can mean being unable to sell or buy for minutes to hours, while a circuit breaker is a rare, dramatic event that resets the entire market narrative.

## See also

<div class="wiki-seealso">

### Closely related

- [Stock exchange](/stock-exchange/) — venues where trading is conducted and halted
- [Market order](/market-order/) — orders vulnerable to halts and breakers
- [Limit order](/limit-order/) — orders that may or may not execute depending on price when trading resumes
- [Securities and Exchange Commission](/securities-and-exchange-commission/) — the regulator overseeing halts and breakers
- [NYSE](/new-york-stock-exchange/) — the primary exchange where circuit breaker thresholds are monitored
- [Nasdaq](/nasdaq/) — an alternative exchange also subject to circuit breaker rules

### Wider context

- [Market cycle](/market-cycle/) — boom and bust patterns that circuit breakers are designed to interrupt
- [Systemic risk](/systemic-risk/) — risks that one failure cascades through the entire market
- [Algorithmic trading](/algorithmic-trading/) — automated strategies affected by halts and breakers
- Black Monday — the 1987 crash that prompted circuit breaker invention

</div>
