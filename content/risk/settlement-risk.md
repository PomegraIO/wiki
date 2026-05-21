---
title: "Settlement Risk"
description: "Settlement risk is the danger that one side of a financial transaction will be settled (payment delivered) while the other side is not, leaving one party with a loss."
keywords:
  - settlement risk
  - Herstatt risk
  - FX risk
  - delivery risk
  - transaction risk
image: "/svg/risk.svg"
---

*Settlement risk — also called **delivery risk** or **Herstatt risk** — is the probability that one counterparty will deliver payment or securities in a transaction while the other fails to deliver, leaving the first party with a loss. It is most acute in foreign exchange transactions where settlement occurs across time zones.*

<div class="wiki-hatnote">

This entry covers the risk during the gap between trade and settlement. For the specific case of FX settlement failure, see [herstatt-risk](/herstatt-risk); for the broader risk that any counterparty fails, see [counterparty-risk](/counterparty-risk).

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Settlement Risk — key facts</div>

<img src="/svg/risk.svg" alt="A payment instruction frozen mid-delivery between two banks" />

<div class="wiki-infobox-caption">Settlement risk peaks in the gap between trade and final clearing.</div>

|   |   |
|---|---|
| **What it is** | Risk that one side settles but the other does not |
| **Also called** | Herstatt risk, delivery risk |
| **Most acute in** | Foreign exchange; cross-border transactions |
| **Timing** | Between trade execution and final settlement |
| **Root cause** | Time zones; different settlement systems; counterparty failure |
| **Magnitude** | Can be full transaction value or the difference if partially executed |
| **Mitigated by** | Same-day settlement; DVP (Delivery versus Payment); real-time gross settlement |

</aside>

## How settlement risk arises

When you buy a [stock](/stock), the trade occurs instantly (electronically), but settlement happens two business days later (in the US). On trade day, you own the [stock](/stock) and your broker holds cash. The seller owns the cash and their broker holds the [stock](/stock). Over the next two days, the stock and cash are transferred to their final destinations.

During those two days, settlement risk exists. If the buyer's broker fails before delivering cash, the seller loses the [stock](/stock). If the seller's broker fails before delivering the [stock](/stock), the buyer loses the cash.

This is settlement risk: the risk during the gap between trade and final settlement.

## Settlement risk in foreign exchange

Settlement risk is most acute in foreign exchange (FX) transactions. An international company in New York trades dollars for yen with a bank in Tokyo. The NY company sends dollars to Tokyo; the Tokyo bank sends yen to New York.

But dollars settle in the US and yen settle in Japan — on different time zones. The NY company sends dollars first (during US business hours). The Tokyo bank receives them and should send yen back. But if the Tokyo bank fails before sending yen, the NY company has given away dollars and received nothing.

This is the core of Herstatt risk (named after Herstatt Bank, which failed in 1974 while owing billions in FX settlements). The first mover in an FX transaction faces the risk that the second mover does not complete the deal.

## Settlement fail cascades

Settlement failures can cascade. If Bank A does not deliver securities to Bank B, Bank B cannot deliver to Bank C, and so on. The failure propagates through the financial system, creating [systemic-risk](/systemic-risk).

During the 2008 financial crisis, settlement failures increased sharply as counterparties became distrustful. Some institutions stopped delivering securities, fearing non-delivery by others. Central banks had to intervene to restore confidence in settlement systems.

## Mitigating settlement risk

The financial system has developed several solutions:

- **Delivery versus Payment (DVP).** Securities and cash are delivered simultaneously, so neither party is exposed to the other's failure between trade and settlement. If one side fails, the other gets nothing, preventing the one-sided loss.

- **Real-time gross settlement (RTGS).** Transactions settle immediately, in real time, rather than batching at the end of the day. This reduces the window for failure.

- **Central counterparties (CCPs).** In exchange-traded and centrally cleared markets, the CCP interposes itself, guaranteeing settlement to both sides. If one side fails, the CCP absorbs the loss.

- **T+0 settlement.** Newer systems settle trades on the same day (T = trade date). The faster settlement reduces risk accumulation.

- **Collateral and margin.** In derivative markets, daily margin requirements mean losers must post collateral, reducing accumulated exposure.

For FX transactions, no perfect solution exists because of time zones. But systems like CLS (Continuous Linked Settlement) reduce risk by netting and simultaneous settlement in real time.

## Settlement risk for individual investors

For retail investors, settlement risk is largely abstracted away by brokers and clearing systems. When you buy a [stock](/stock), your broker and the seller's broker handle settlement using DVP, and the risk is minimal.

However, for very large trades, OTC derivatives, or international transactions, settlement risk can be material. Large institutional investors insist on DVP terms, netting agreements, and collateral arrangements to minimize settlement risk.

## See also

<div class="wiki-seealso">

### Closely related

- [Herstatt-risk](/herstatt-risk) — settlement risk in FX specifically
- [Counterparty-risk](/counterparty-risk) — underlying risk during settlement
- [Systemic-risk](/systemic-risk) — settlement failures can cascade
- [Derivative](/option) — subject to settlement risk in OTC markets
- [Foreign exchange](/currency-risk) — most prone to settlement risk

### Broader context

- [Central clearing](/central-bank) — reduces settlement risk
- [Delivery versus payment](/settlement-risk) — mitigates settlement risk
- [Stock exchange](/stock-market) — executes trades; brokers handle settlement
- [Banking system](/stock-market) — interconnected through settlement systems
- [2008 financial crisis](/credit-risk) — settlement failures worsened crisis

</div>
