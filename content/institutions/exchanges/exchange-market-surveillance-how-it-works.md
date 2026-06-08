---
title: "How Exchange Market Surveillance Works"
description: "Stock exchanges use automated systems and human traders to detect wash trades, spoofing, and manipulation. Suspicious activity is escalated to the SEC and FINRA."
keywords:
  - how exchange market surveillance works
  - stock exchange surveillance system
  - detecting market manipulation
  - wash trading detection
  - exchange regulatory surveillance
---

*Stock exchanges monitor every trade and quote for signs of manipulation, layering, wash trades, and spoofing. **Exchange market surveillance** blends real-time automated alerts with forensic review by a dedicated compliance team, feeding suspicious patterns to federal regulators.*

## The two-layer surveillance model

Every major exchange—the NYSE, Nasdaq, CBOE, CME—operates a surveillance operation that never sleeps. The first layer is automated: algorithms scan every order, every quote, every fill in microseconds, looking for patterns that suggest wrongdoing. The second is human: surveillance teams review flagged trades, request data from brokers, and decide whether to escalate to the SEC or FINRA.

The automated layer catches most potential violations almost in real time. A trader layering buy orders at ascending prices, then canceling them as a stock rises, trips an algorithm within seconds. A wash trade where the same entity buys and sells the same block within milliseconds registers as an unusual order pair. The exchange's surveillance database stores these flags and patterns for further inspection.

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Exchange Surveillance — Process and Outcomes</div>

<img src="/svg/institutions.svg" alt="An abstract editorial mark for institutions and regulatory topics." />

<div class="wiki-infobox-caption">Detection triggers investigation, which may lead to broker referral and regulator action.</div>

|   |   |
|---|---|
| **Real-time detection layer** | Automated order-matching algorithms. |
| **Pattern flagging** | Spoofing, layering, wash trading, pump-and-dump. |
| **Broker contact window** | Usually within 24–72 hours for manual review. |
| **Data requested** | Trade blotter, broker communications, account history. |
| **Escalation threshold** | Pattern confidence + broker non-response or admission. |
| **Regulatory referral** | SEC for equity; CFTC for futures; FINRA for OTC. |
| **Public disclosure** | None usually. Enforcement action if violations confirmed. |

</aside>

## Automated detection: what the algorithms watch

The exchange's surveillance system monitors:

**Quote stuffing and layering.** An algorithm flags a trader who submits dozens of orders in rapid succession, each at slightly higher (or lower) prices, without the intention of having most of them filled. If the trader cancels 90% of orders within seconds, or if orders cancel en masse after a price movement, the system notes it.

**Wash trades.** The system detects when the same entity (or related entities) appears on both sides of a transaction—a buy order and sell order for the same quantity, same time, same price, often between linked accounts. True wash trades violate anti-manipulation rules because they create false trading volume without genuine change of ownership.

**Spoofing.** An algorithm identifies a pattern where a trader places a large order, waits as the price moves in their favor in response to that order signal, then cancels the large order before it fills. The order was never meant to execute; it was meant to move the market. Repeated instances of this pattern trigger an alert.

**Unusual price-volume relationships.** If a small stock suddenly trades 100x its average daily volume in a narrow price band without news, the system flags it as potential manipulation or information leakage.

**Cross-exchange arbitrage anomalies.** If a stock trades at $50.00 on the NYSE and $49.95 on Nasdaq for an unusual duration, or if an order moves prices across exchanges in a suspicious sequence, the system notes it.

**Halt triggers and reversals.** If a trade causes a sudden halt and is immediately unwound, or if a trade is preceded by a spike in options flow, the system preserves the data for review.

## The surveillance team's workflow

When an alert fires, it enters a queue for the exchange's surveillance team—typically a mix of former traders, analysts, and compliance specialists. The team does not automatically assume a violation. They contextualize the alert:

1. **Gather broker metadata.** Who is the executing broker? What is the account holder's history? Are there unusual relationships (shared addresses, phone numbers, wire transfers between accounts)?
2. **Review news and corporate actions.** Did the company announce earnings, a merger, or a regulatory filing around the flagged trades? Is there a legitimate reason for the volume spike?
3. **Request the blotter.** The team contacts the broker and requests the trader's order blotter, communications, and intent documentation. Did the trader send an email saying "let's pump the stock" or "let's wash trade to inflate volume"? (Rarely explicit, but patterns matter.)
4. **Check for prior violations.** Does this trader or broker have a history of similar patterns?
5. **Evaluate intent.** This is the crux. Market manipulation requires *intent* to manipulate. Accidental or mistaken orders, failed hedges, or execution errors may generate false alerts. A trader might cancel orders out of changed market judgment, not market manipulation.

## Escalation to regulators

If the exchange's surveillance team concludes that a violation likely occurred, they file a report with the SEC (for equities) and may also notify FINRA and the broker's compliance department. The report includes:

- A summary of the suspicious pattern and dates
- Order timestamps, prices, and volumes
- The identities of traders and accounts involved
- Evidence of prior violations or coordination
- The exchange team's assessment of intent and materiality

The SEC then decides whether to investigate further, issue a subpoena, or refer the case to its Enforcement Division. FINRA may run its own parallel investigation and may impose sanctions on the broker or trader.

## Types of violations routinely detected

**Wash trades** are among the easiest to detect automatically. A trader executing identical buys and sells between their own accounts, with the same quantity and price, trips immediate alerts.

**Spoofing** is harder but identifiable by pattern. Submitting large orders that cancel before fill, consistently, in directions that benefit other positions, raises red flags. The SEC has successfully prosecuted spoofing cases against individual traders based on order-cancellation sequences.

**Pump-and-dump schemes** are detected when a coordinated group of accounts (often distributed across brokers) buy a low-liquidity stock, then sell it after an artificial price rise. The exchange's surveillance may not catch the pump itself (that happens organically), but the volume concentration and follow-up selling pattern can trigger review.

**Layering and disruptive trading** show up when a trader submits multiple orders in rapid sequence, moving price, then cancels them. Repeating this hundreds of times in a session signals the algorithm.

**Insider trading** leaves traces: an unusual order right before a major news event, combined with communications or timing, can raise suspicion. The exchange escalates; the SEC investigates using tools the exchange does not have.

## Limitations and false positives

The automated system generates many false alerts. A legitimate trader using algorithmic execution to minimize market impact may submit and cancel many orders. A hedge fund's complex multi-leg options strategy can look suspicious until contextualized. A broker's risk management system may cancel large orders automatically if market conditions shift.

The human surveillance team must filter these. This is why intent matters legally: a pattern alone is not a violation. The SEC and exchanges must show that the trader *intended* to manipulate, not merely made poor decisions or used unusual execution strategies.

## Cross-border and OTC limits

Exchange surveillance works well on lit, centralized venues. But a significant portion of trading happens over-the-counter, where order data is less transparent and surveillance is fragmented. The SEC has authority to police OTC manipulation, but detection is harder. Cryptocurrency exchanges, which operate with varying regulatory oversight, have even weaker surveillance.

For foreign exchanges, U.S. regulators have limited direct surveillance power. They rely on information-sharing agreements and the exchanges' own compliance teams. A trader based in the U.S. manipulating a foreign stock faces potential SEC action, but the foreign exchange may never know.

## See also

<div class="wiki-seealso">

### Closely related

- [Market Maker Trading](/market-maker-trading/) — How liquidity providers quote and execute.
- [Price Discovery](/price-discovery/) — The process by which markets establish fair value.
- [Short Selling](/short-selling/) — Naked short sales and fails-to-deliver are also under surveillance.
- [Securities and Exchange Commission](/securities-and-exchange-commission/) — The primary federal regulator of equity markets.
- [FINRA](/finra/) — The self-regulatory organization overseeing brokers and OTC trading.

### Wider context

- [Stock Exchange](/stock-exchange/) — The venue and operator of surveillance systems.
- [Over-the-Counter Market](/over-the-counter-market/) — Where surveillance is less transparent.
- [Alternative Trading System](/alternative-trading-system/) — Dark pools and ATS venues with lighter surveillance.
- Insider Trading — A manipulation form that exchanges escalate to the SEC.

</div>
