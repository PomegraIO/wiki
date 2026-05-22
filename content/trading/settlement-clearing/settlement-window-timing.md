---
title: "Settlement Window Timing"
description: "How T+2, T+1, and same-day settlement impact liquidity, risk, and trading mechanics."
keywords:
  - settlement timing
  - t plus two
  - t plus one
  - settlement cycles
  - clearing mechanics
---

*The **settlement window** is the time interval between trade execution and final transfer of securities and cash. The US moved from [T+3](/wiki/settlement-cycles/) to [T+2](/wiki/settlement-t2/) in 2017; T+1 (next day settlement) is now standard in some markets. Shorter windows reduce counterparty risk but increase operational burden and opportunity cost.*

<aside class="wiki-infobox">

| Timing | Region | Status | Key Impact |
|---|---|---|---|
| **T+2** | US, EU | Current standard (as of 2017) | 2-day window for risk mitigation |
| **T+1** | Some retail, futures | Emerging | Faster capital release; higher ops cost |
| **Same-day (T+0)** | Crypto, some swaps | Niche | Minimal counterparty risk; tech-heavy |
| **T+3 (legacy)** | Phased out US 2017 | Historical | High operational flexibility; high risk |
| **[Herstatt risk](/wiki/herstatt-risk/)** | Cross-border FX | Always present | Time-zone gap causes settlement exposure |
| **Fails** | All markets | Non-zero | Failed settlements create breaks; reset mechanics |

</aside>

## Why settlement takes time

Trade execution (buyer and seller agree on price) happens instantly, but settlement (actual movement of securities and cash) lags because:

1. **Confirmation delays** — each side must verify the counterparty's identity and trade details (amount, price, delivery instructions).
2. **Custodial logistics** — securities are held by [custodians](/wiki/custodian/) or [central depositories](/wiki/depository-trust-company/); the depository must:
   - Confirm the seller has the securities (no double-selling)
   - Transfer them to the buyer's account
   - Debit the buyer's cash and credit the seller's
3. **[Clearinghouse](/wiki/central-counterparty-clearing/) netting** — the [clearinghouse](/wiki/clearing-firm/) (e.g., [DTCC](/wiki/dtcc/) for US equities) nets obligations across all traders to reduce the volume of transfers.
4. **Regulatory checks** — anti-money laundering ([AML](/wiki/anti-money-laundering/)) screening, sanctions checks, and position limit verification.

## T+2 and T+1: the timeline difference

### T+2 (Trade date + 2 business days)

An equity trade on Monday settles on Wednesday. Seller delivers securities Wednesday morning; buyer wires cash. This was the standard in the US until 2017 and remains so in most markets.

**Advantages of T+2:**
- Wide window for confirmation and error correction
- [Clearinghouses](/wiki/clearing-firm/) can batch and net more aggressively, reducing settlement risk
- Operational teams have breathing room
- Common across global markets (harmonization reduces friction)

**Disadvantages:**
- Seller is at [counterparty risk](/wiki/counterparty-risk/) for 2 days (what if buyer defaults?)
- Buyer's capital is locked up for 2 days (opportunity cost)
- Fails (undelivered trades) take longer to resolve
- In a [flash crash](/wiki/flash-crash-2010/) or panic, two days of unresolved trades can amplify contagion

### T+1 (Trade date + 1 business day)

Trade Monday, settle Tuesday. This is standard for US Treasury securities and some broker-dealer operations. It's increasingly common in retail venues as technology improves.

**Advantages:**
- Capital cycle accelerates (seller gets cash next day, not day-after-next)
- Reduced [counterparty risk](/wiki/counterparty-credit-risk/) exposure
- Fewer fails in a market crisis (less time for things to break)
- Aligns with retail expectations ("I sold today, where's my money?")

**Disadvantages:**
- Tighter operational window; less time for confirmation and fixes
- Higher [settlement risk](/wiki/settlement-risk/) in the compressed timeframe (operational failures can cascade)
- Requires more robust technology (no room for manual workarounds)
- Cross-border trades become even harder to coordinate

### T+0 (Same-day, or instant settlement)

Trade and settle in the same market session. This is standard in [cryptocurrency](/wiki/bitcoin/) (blockchain settlement is often 10 seconds), [repo](/wiki/repurchase-agreement/) transactions, and some [FX swap](/wiki/fx-swap/) markets.

**Advantages:**
- Zero counterparty risk (each side gets what they expect immediately)
- Maximum capital efficiency
- No fails possible (trade either completes or reverts)

**Disadvantages:**
- Requires nearly-instant confirmation (often impossible for retail traders)
- Minimal time for error correction or dispute resolution
- Technology must be perfect; a systems glitch = instant losses
- Incompatible with global settlement (time-zone gaps make real T+0 impossible across regions)

## The 2017 US shift from T+3 to T+2

In 2015–2017, the SEC and [DTCC](/wiki/dtcc/) worked to shorten US equity settlement from T+3 to T+2. The goal: reduce systemic risk and align with EU/UK standards (which had moved to T+2 in 2014).

**Drivers:**
- Lehman Brothers' 2008 collapse exposed how multi-day settlement lags made contagion worse
- Regulatory push for global consistency
- Technology was mature enough to handle tighter windows

**Impact:**
- Operational costs rose (more confirmation automation needed)
- Retail investors saw minimal difference (most don't monitor settlement)
- Institutions had to upgrade systems
- Fails slightly increased initially (operational bugs) but normalized after 6–12 months

## Settlement fails and their resolution

A **fail** occurs when either party doesn't deliver (securities not received or cash not wired) on the settlement date. In T+2 systems:

1. Trade settles Monday; if no deliver by close of business Wednesday, it's officially failed.
2. Fail persists until one party makes good. During the fail, the buyer often has to pay a [fail-to-deliver fee](/wiki/fail-to-deliver-market-impact/) (daily penalty on the seller).
3. In extreme cases (coordinated short squeezes or system failures), fails can cascade and require exchange/clearinghouse intervention.

T+1 windows leave less room for market participants to manually hunt down missing securities or resolve disputes, which can trigger more fails during operational stress.

## Herstatt risk and cross-border settlement

**[Herstatt risk](/wiki/herstatt-risk/)** is the danger that one party in a cross-border trade delivers its leg (e.g., EUR payment) but the other party's leg (USD delivery) doesn't arrive because of a time-zone gap or operational failure in a different zone.

For example, a German bank (Herstatt Bank) paid out DM but didn't receive USD in 1974, triggering a famous settlement default. Modern [FX settlement](/wiki/settlement-procedures/) uses established [settlement windows](/wiki/settlement-cycles/) (e.g., T+2 for [currency pairs](/wiki/currency-pair/)), but Herstatt risk persists because no amount of timing will eliminate the time-zone asynchrony between Frankfurt and New York.

## Leverage and margin implications

Shorter settlement windows reduce margin requirements. If a [day trader](/wiki/day-trading/) buys stock Monday and sells Tuesday, they can settle-to-settlement without holding overnight [margin](/wiki/margin-trading-crypto/). With T+3, they had to finance an extra day. Some day traders and [proprietary traders](/wiki/principal-trading/) budget cash based on settlement lag; T+1 frees up capital and reduces [opportunity cost](/wiki/time-value/).

## Future: toward T+1 or T+0

Market pressure is building for faster settlement:
- **Retail investing growth** — younger investors expect instant settlement (influenced by crypto)
- **Repo market efficiency** — repurchase agreements often settle same-day or next-day
- **Regulatory push** — global initiatives (SEC, ECB, PBoC) are discussing coordinated T+1 shifts

Full T+0 in mainstream equities is unlikely because of time-zone complexity and the need for confirmation windows. But T+1 may become the new standard within 5–10 years as technology matures.

<div class="wiki-seealso">

### Closely related
- [Settlement cycles](/wiki/settlement-cycles/) — the complete settlement process
- [Settlement T+2](/wiki/settlement-t2/) — current US standard (detailed)
- [Central counterparty clearing](/wiki/central-counterparty-clearing/) — how clearinghouses manage settlement
- [Herstatt risk](/wiki/herstatt-risk/) — cross-border settlement hazard
- [Fail-to-deliver market impact](/wiki/fail-to-deliver-market-impact/) — consequences of failed settlements

### Wider context
- [Counterparty risk](/wiki/counterparty-risk/) — why settlement windows matter
- [DTCC](/wiki/dtcc/) — US securities clearinghouse
- [Custodian](/wiki/custodian/) — settlement infrastructure
- [Depository trust company](/wiki/depository-trust-company/) — depository for securities
- [Repo (repurchase agreement)](/wiki/repurchase-agreement/) — alternative settlement structure

</div>
