---
title: "Herstatt Risk"
description: "Herstatt risk is the danger in foreign exchange transactions that one side will deliver currency while the other fails to deliver, named after Herstatt Bank which failed mid-settlement in 1974."
keywords:
  - Herstatt risk
  - FX settlement risk
  - foreign exchange risk
  - cross-currency risk
  - payment system failure
image: "/svg/risk.svg"
---

*Herstatt risk is a form of [settlement-risk](/settlement-risk) specific to foreign exchange transactions, where one counterparty delivers one currency while the other fails to deliver the counter-currency, named after Herstatt Bank's 1974 failure. It is a critical concern for international financial institutions and is mitigated through systems like CLS (Continuous Linked Settlement).*

<div class="wiki-hatnote">

This entry covers FX settlement failure specifically. For settlement risk more broadly, see [settlement-risk](/settlement-risk); for general FX exposure, see [currency-risk](/currency-risk).

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Herstatt Risk — key facts</div>

<img src="/svg/risk.svg" alt="A currency exchange frozen mid-transaction, one currency delivered, the other missing" />

<div class="wiki-infobox-caption">Herstatt risk materializes when one FX leg settles but the other fails.</div>

|   |   |
|---|---|
| **What it is** | Settlement failure in FX; one side pays, the other does not |
| **Named after** | Herstatt Bank, failed June 1974 mid-settlement |
| **Core problem** | Different settlement times across time zones |
| **Magnitude** | Can be billions per transaction; first mover faces full risk |
| **Occurs in** | OTC FX transactions; cross-border payments |
| **Mitigated by** | CLS settlement; netting; margin agreements |
| **Systemic impact** | Can cascade; historically a [systemic-risk](/systemic-risk) concern |

</aside>

## The Herstatt precedent: June 1974

Herstatt Bank was a German bank active in FX trading. In June 1974, financial difficulties led to its regulatory closure. At that moment, Herstatt had received deutsche marks from trading partners in FX transactions but had not yet paid out dollars (in New York, which operates on a later time zone).

When Herstatt failed, many counterparties lost dollars they had committed to receive. The bank had netted many billions in FX transactions, and its failure was one of the largest financial losses of the era.

Herstatt risk is named after this event: the danger that, in an FX transaction, you deliver your currency but the counterparty fails before delivering theirs, leaving you with a loss.

## Why FX is uniquely vulnerable to settlement risk

FX transactions are peculiarly exposed to settlement risk because:

1. **Time zones.** A bank in New York trading with a bank in Tokyo settles dollars in New York and yen in Tokyo. These settle on different schedules. The first bank delivers dollars and must wait for yen settlement in the Tokyo morning, a gap of 12+ hours.

2. **Different settlement systems.** Dollars settle through the US Federal Reserve; yen settle through the Bank of Japan. Each has its own rules, hours, and contingencies.

3. **Large transaction sizes.** FX transactions are often enormous — billions of dollars. A single failed settlement can wipe out capital.

4. **Interdependence.** Large banks are both counterparties and settlement agents, creating chains of dependency. A failure upstream can trigger failures downstream.

## The systemic risk

If a major FX dealer fails mid-settlement, the financial system can seize. In the days after Herstatt, other banks became fearful of FX settlement and reduced activity, tightening credit. The crisis prompted central banks to establish the Basel Committee on Banking Supervision to coordinate bank regulation.

During the 2008 financial crisis, Herstatt-like risk spiked. AIG, a major FX counterparty, nearly failed. US and international authorities recognized that AIG's failure would trigger cascading FX settlement failures and moved quickly to prevent it.

## Mitigating Herstatt risk: CLS settlement

The primary tool for reducing Herstatt risk is **Continuous Linked Settlement (CLS)**, operated by CLS Group, a settlement system for major currencies.

How CLS works:

- Banks that trade FX submit trade details to CLS.
- CLS acts as a central counterparty, guaranteeing settlement to both sides.
- At settlement, CLS nets all positions in each currency (a bank that owes $10M in one trade and is owed $12M in another owes net only $10M to CLS).
- CLS releases funds from both sides simultaneously in real time, eliminating the gap between payment and counter-payment.

This eliminates Herstatt risk because neither party is exposed to the other's failure between the two legs of the transaction.

CLS handles the majority of major currency FX settlements ($5+ trillion per day) and is a critical piece of financial stability infrastructure.

## Remaining Herstatt risk

Despite CLS, some Herstatt risk remains:

- **Non-CLS currencies.** Emerging market currencies often do not settle through CLS, leaving institutions exposed to Herstatt risk.

- **OTC derivatives in FX.** FX forwards, swaps, and options that are not centrally cleared still carry settlement risk.

- **Operational delays.** Even with CLS, operational failures or market disruptions can delay settlement.

For international firms and banks, Herstatt risk is actively managed through:
- Limiting exposure to single counterparties.
- Using CLS for major currencies.
- Holding collateral agreements and netting arrangements.
- Diversifying across settlement time zones.

## See also

<div class="wiki-seealso">

### Closely related

- [Settlement-risk](/settlement-risk) — broader concept; Herstatt is a type
- [Currency-risk](/currency-risk) — related but distinct; FX movement vs. settlement failure
- [Counterparty-risk](/counterparty-risk) — underlying risk in FX transactions
- [Central clearing](/central-bank) — CLS reduces Herstatt risk
- [Foreign exchange](/currency-risk) — the market where Herstatt risk occurs

### Broader context

- [Basel Committee](/capital-adequacy) — established after Herstatt to coordinate regulation
- [Systemic-risk](/systemic-risk) — Herstatt risk is a potential systemic threat
- [1974 financial crisis](/credit-risk) — Herstatt's failure was landmark
- [AIG](/credit-risk) — 2008 example of near-Herstatt scenario
- [Financial infrastructure](/stock-market) — CLS and settlement systems

</div>
