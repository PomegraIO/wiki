---
title: "Value Date vs Settlement Date in Forex"
description: "Understand the difference between the value date when forex rates are set and the settlement date when cash actually changes hands."
keywords:
  - forex value date vs settlement date
  - spot settlement
  - t+2 settlement
  - value date definition
  - forex settlement cycles
image: "/svg/forex.svg"
---

*In foreign exchange trading, the **value date** is when the rate is locked in and the trade is priced, while the **settlement date** is when the actual currencies are delivered. Most forex pairs follow T+2 convention, meaning settlement occurs two business days after the trade is executed.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Value Date vs Settlement Date — key facts</div>

<img src="/svg/forex.svg" alt="An abstract editorial mark for forex." />

<div class="wiki-infobox-caption">Value date sets the price; settlement date delivers the cash.</div>

|   |   |
|---|---|
| **Value Date** | Day the exchange rate applies to the trade |
| **Settlement Date** | Day each currency leg actually changes hands |
| **Standard Convention** | T+2 (two business days after trade execution) |
| **Spot Transaction** | Trade date = T, Value date = T+2 |
| **Why It Matters** | Confirms which day's market rate you get and when you're at [counterparty risk](/counterparty-risk/) |

</aside>

## How Value Date and Settlement Date Differ

The **forex value date vs settlement date** distinction reflects two separate moments in any currency trade. On the trade date (T), two counterparties agree to exchange currencies at a particular rate. That rate is tied to a specific date — the value date — which determines the price. However, the actual transfer of money between bank accounts happens on the settlement date, which may come later.

Think of it this way: a corporate treasurer in London agrees to buy 5 million US dollars at 1.2850 GBP/USD at 10 a.m. on a Wednesday. That Wednesday is the trade date (T). The value date might be the following Friday (T+2 in standard spot forex). The rate 1.2850 applies because it's Friday's value date. But the actual pounds leave the company's British bank account and the dollars arrive in the US account on that same Friday — the settlement date.

In most cases for spot forex, the value date and settlement date are identical. The confusion arises because they exist as separate concepts: the value date is *when the rate applies*, and the settlement date is *when the exchange occurs*. For spot transactions, both happen on the same calendar day.

## The T+2 Standard and Business Days

The foreign exchange market adopted a T+2 (trade plus two business days) settlement convention as a global standard. This means when you execute a spot forex trade on a Monday, the value date and settlement date fall on Wednesday — two business days later, excluding weekends.

Business days matter: if you trade on a Friday, settlement is typically Tuesday (Monday is skipped as a non-business day in many markets). The two-day window gives [banks](/central-bank/) and custodians time to verify counterparty details, confirm account information, and route payments through correspondent banking networks.

For the trader, this T+2 lag introduces a critical window: during those two days, you are exposed to [counterparty risk](/counterparty-risk/). Your counterparty might fail to deliver the currency, or your own institution might default. This is why settlement risk, sometimes called Herstatt risk (named after a 1974 bank failure), remains a concern in high-volume currency trading.

## Forward Contracts and Non-Spot Value Dates

Spot transactions follow the T+2 standard, but currency [forwards](/forward-contract/) can have any value date the two parties agree on. A company might enter a forward contract today (trade date) with a value date six months hence. In that case, the rate is locked in today, but settlement doesn't occur until six months from now.

This flexibility is why forwards are crucial for [hedging](/derivatives-hedging/): a US exporter expecting a euro payment three months ahead can forward-contract to sell euros at a known rate, with settlement timed to match the expected receipt. The value date (three months from now) is the point on the calendar when the exchange rate applies, and that is also when euros and dollars change hands.

Other common non-spot value dates include:
- **Tomorrow Next (TN):** Settlement T+1, rarely used for spot trades but sometimes for rapid repositioning.
- **One Week, One Month, Two Months:** Standard conventions for forward contracts where traders specify settlement in round increments.

## Why Value Date Matters for Pricing

The value date is not arbitrary; it determines which interest-rate [differential](/carry-trade/) applies to the trade. Currency pairs incorporate a carry component that reflects the gap between the two countries' interest rates.

For example, if US rates are 5% and the euro rate is 3%, a forward EUR/USD trade will reflect that interest differential. The longer the time to value date, the larger the forward adjustment relative to the spot rate. The formula uses the interest-rate differential, the spot rate, and the time to maturity (from today until the value date). This is why a six-month forward EUR/USD price differs materially from the two-day spot rate: the value date is much further out, and more interest-rate drag accumulates.

Traders and treasurers must track the value date carefully because it pins down which rate your trade carries. A deal you make on Monday for a Friday value date is priced to Friday's fundamentals and interest expectations, not Monday's.

## Settlement Risk and Real-World Delays

Although T+2 is standard, settlement can be delayed by operational glitches, regulatory holds, or deliberate instructing by either party. During market stress, central banks have occasionally widened the settlement window to allow more time for processing.

A more insidious risk emerges if one counterparty sends its currency but the other defaults before delivering. This happened to banks in the 1974 Herstatt crisis: a German bank sent dollars to New York but failed before receiving the Deutsche marks it was owed. Modern systems like [CHIPS](/custodian/) and Fedwire in the US now use delivery-versus-payment (DVP) settlement, which reduces this risk by ensuring both legs settle simultaneously.

Real money traders and [institutional investors](/investment-grade-bond/) often segregate settlement risk in their systems: they know that until the value date arrives and both currencies have moved into their nostro accounts (foreign currency accounts held at correspondent banks), the trade is not finalized in the cash sense, even though the value date has been set.

## Corporate and Operational Implications

For corporate treasuries, the value date and settlement date matter operationally. A company that imports goods and must pay in a foreign currency needs to time the currency purchase so the settlement date aligns with when the supplier expects payment. Settling early ties up working capital; settling late risks breach of contract.

Similarly, a [multinational corporation](/accounts-receivable/) managing [cash flow](/cash-flow-statement/) across subsidiaries must coordinate value dates to optimize intra-company netting. If subsidiary A owes subsidiary B in one currency, and B owes A in another, netting happens at agreed value dates. Misalignment extends exposure windows.

Banks also use value date conventions in their [repo](/repurchase-agreement/) operations and for trading securities: not every asset trades on T+2, and mismatch between value dates can lock in financing costs or require temporary [liquidity](/liquidity-risk/) buffers.

## See also

<div class="wiki-seealso">

### Closely related

- [Spot rate](/spot-rate/) — the exchange rate for immediate (T+2) settlement
- [Forward contract](/forward-contract/) — custom settlement dates and rates for future currency exchanges
- [Counterparty risk](/counterparty-risk/) — why you are exposed between trade and settlement
- [Carry trade](/carry-trade/) — how interest-rate differentials drive forward pricing
- [Currency risk](/currency-risk/) — broader exposures in foreign exchange

### Wider context

- [Forex mechanics](/forex-cross-rate-calculation/) — how currency prices and conversions work
- [Settlement](/securitization/) — general principles of how trades clear
- [Bank of America](/bank-of-america/) — major currency settlement player
- [Central bank](/central-bank/) — manages settlement infrastructure and rules

</div>
