---
title: "Circuit Breaker and Trading Halt"
description: "Automatic market-wide or single-stock pauses triggered by extreme intraday price moves to prevent panic selling and allow information processing."
keywords:
  - circuit breaker
  - trading halt
  - market pause
  - price decline limit
  - sec trading halts
  - intraday trading suspension
image: "/svg/trading.svg"
---

*A **circuit breaker** is an automatic market-wide or individual stock trading pause triggered when prices fall (or occasionally rise) by a preset percentage within a single trading day. A **trading halt** is a temporary suspension of trading in a specific security, often imposed by an exchange or regulator when material news arrives or when conditions are disorderly. Both mechanisms exist to interrupt panic and give market participants time to absorb information.*

<div class="wiki-hatnote">

For the circuit-level pause rules that govern US equities, see [price-time priority](/price-time-priority/); for the resolution of impossible pricing across venues, see [locked-and-crossed-markets](/locked-and-crossed-markets/).

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Circuit Breaker and Trading Halt — key facts</div>

<img src="/svg/trading.svg" alt="An abstract editorial mark for trading mechanics and market regulation." />

<div class="wiki-infobox-caption">Automatic pauses that lock markets when volatility spikes or information asymmetries threaten orderly price discovery.</div>

|   |   |
|---|---|
| **What it is** | Regulatory pause rule triggered by percentage price drops (or rises) or by exchange/SEC decision |
| **Purpose** | Interrupt panic, allow information distribution, restore [market-maker-trading](/market-maker-trading/) confidence |
| **Circuit breaker scope** | US equities: market-wide 7%, 13%, 20% declines; individual stocks: 10% in 5 minutes |
| **Trading halt scope** | Single security, typically 8 hours or until news is fully disclosed |
| **Authority** | [SEC](/securities-and-exchange-commission/), exchanges ([NYSE](/new-york-stock-exchange/), [NASDAQ](/nasdaq/)) |
| **Cooldown effect** | Mandatory reboot of [price discovery](/price-discovery/), reset of bid–ask dynamics |

</aside>

## The 1987 crash and the genesis of circuit breakers

On 19 October 1987—"Black Monday"—the [S&P 500](/sp-500-index/) fell roughly 20% in a single day. Panic selling, [margin calls](/margin-call-forex/), and computerised [algorithmic trading](/algorithmic-trading/) feedback loops collided to create a cascade of selling that seemed unstoppable. By day's end, the market had shed more value than many nations' GDP. The [SEC](/securities-and-exchange-commission/) and the exchanges that followed concluded that a completely unfettered market could eat itself alive in hours and that some form of automatic brake was essential.

Circuit breakers were born not as market interference, but as market preservation. The logic is straightforward: when prices move so fast and so far that rational [price discovery](/price-discovery/) becomes impossible—when [bid-ask spreads](/bid-ask-spread/) explode, [liquidity](/liquidity-risk/) dries up, and [counterparty risk](/counterparty-risk/) becomes unknowable—a pause button allows time for information to distribute, for fear to cool, and for normal trading mechanics to reboot.

## Market-wide circuit breakers in US equities

The [SEC](/securities-and-exchange-commission/) maintains three tiers of market-wide halts for US equities (they apply to most securities traded on [NYSE](/new-york-stock-exchange/), [NASDAQ](/nasdaq/), and other exchanges):

**Level 1 (7% decline).** If the [S&P 500](/sp-500-index/) falls 7% from the previous day's close before 3:25 p.m., all trading halts for 15 minutes. The market then resumes. If it resumes but hits the 13% threshold, trading halts again.

**Level 2 (13% decline).** A 13% drop triggers a second 15-minute halt. After resumption, only a 20% decline triggers Level 3.

**Level 3 (20% decline).** A 20% drop before 3:25 p.m. closes the market for the remainder of the trading day. After 3:25 p.m., no circuit breaker applies; the day is allowed to close wherever it falls.

These rules are mechanical, not discretionary. No [SEC](/securities-and-exchange-commission/) official votes on whether to pause; the math decides. That predictability matters: investors know the rules, and traders can plan around them. It also prevents political or emotional judgment from creeping into the decision to halt.

## Single-stock trading halts

Not every anomaly needs a market-wide pause. If a single stock plummets 10% or more in 5 minutes—or if news breaks that creates information asymmetry—the exchange may halt that one security. A trading halt is normally triggered by:

- An impending material news announcement (earnings, regulatory action, merger rumour, insider action).
- Disorderly trading conditions (a fat-finger trade sending the stock down 50% by accident).
- Pending [broker](/broker/) or exchange action (investigation, delinquency).

[SEC](/securities-and-exchange-commission/) Rule 15c2-1 grants exchanges broad discretion to halt trading in a single security for up to 8 hours while management prepares an announcement or while conditions stabilize. The halted period allows the [price-time priority](/price-time-priority/) queue to clear and resets the mood. When trading resumes, the opening [call auction](/stock-exchange/) (on NASDAQ and NYSE) collects fresh supply and demand at the new equilibrium price.

Notably, trading halts fall unevenly on different categories of investors. Those watching the news grasp the reason for the halt; those passive or trading abroad may not. This information gap is precisely why exchanges impose the halt—not to punish, but to enforce synchronization before [price discovery](/price-discovery/) resumes.

## The mechanics of a market reboot

When a [circuit breaker](/circuit-breaker-trading-halt/) or halt concludes, the market does not simply resume tick-by-tick from where it stopped. Instead:

1. **Order cancellations process.** Any [limit orders](/limit-order/) placed before the halt may be cancelled (at [broker](/broker/) discretion, depending on the instrument and the duration of the halt).
2. **New orders accumulate.** During the halt, buyers and sellers have placed fresh orders in the dark, waiting for the restart.
3. **Opening auction.** On NASDAQ and NYSE, trading opens with an [call auction](/stock-exchange/)—a repricing event where all accumulated orders meet at a single price where the most shares can trade. This repricing is often far from the pre-halt level, reflecting new information and fresh sentiment.
4. **Continuous trading resumes.** Once the opening price is set, [market makers](/market-maker-trading/) and traders begin fresh two-sided [price discovery](/price-discovery/).

This reset is psychologically important. Momentum loses its grip. [Volatility](/historical-volatility/) recalibrates. [Algorithms](/algorithmic-trading/) that fired during the descent now face a new dataset.

## Debate over circuit breaker effectiveness

The case *for* circuit breakers is well-worn: they prevent cascades, they force information distribution, they have coincided with fewer panic sell-offs since 1987. The [1987 crash](/great-depression/) itself became a reference point—a day so extreme that it justified any amount of regulation.

The case *against* is subtler. Critics argue that circuit breakers may postpone panic rather than prevent it, creating a false sense of calm. If the bad news does not dissipate during the halt, selling resumes just as violently after the halt as it would have before. Some studies suggest that halts can prolong disorderly price action. And circuit breakers on single stocks create perverse incentives: a trader facing a halt might not bother selling because the halt will do it for them anyway. This can reduce the price-correcting volume that would otherwise occur.

Most economists favour circuit breakers at the market-wide level (they appear to work) but remain divided on single-stock halts. Most exchanges and regulators default to the preservationist camp: when in doubt, halt.

## See also

<div class="wiki-seealso">

### Closely related

- [Trade-Through Protection](/trade-through-protection/) — The rule that orders must be routed to the best available price across venues.
- [Price-Time Priority](/price-time-priority/) — The queue logic that determines which orders execute first during continuous trading.
- [Locked and Crossed Markets](/locked-and-crossed-markets/) — The impossible pricing state that circuit breakers and regulation help prevent.
- [Bid-Ask Spread](/bid-ask-spread/) — The cost of immediate execution, which widens dramatically during panic.
- [Algorithmic Trading](/algorithmic-trading/) — Automated strategies that can amplify moves and trigger halts.
- [Market Maker Trading](/market-maker-trading/) — The professionals who provide liquidity and pause during uncertainty.
- [Counterparty Risk](/counterparty-risk/) — The unknown danger that circuit breakers address by creating information breaks.

### Wider context

- [Stock Exchange](/stock-exchange/) — The venue operator that enforces trading rules and halts.
- [SEC](/securities-and-exchange-commission/) — The regulator that sets circuit breaker thresholds.
- [Price Discovery](/price-discovery/) — The continuous process of finding equilibrium that halts temporarily interrupt.
- [Black Monday](/great-depression/) — The 1987 crash that spawned circuit breaker rules.
- [Margin Call](/margin-call-forex/) — The forced liquidation that circuit breakers prevent from cascading.

</div>
