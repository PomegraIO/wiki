---
title: "Carry Cost (Forex)"
description: "The interest rate differential between two currencies in a forex pair, determining the cost or benefit of holding the position overnight."
keywords:
  - carry cost
  - interest rate differential
  - forex overnight
  - rollover fee
---

*The **carry cost** in forex is the net interest paid or received when holding a currency pair overnight—it equals the [interest rate](/wiki/federal-funds-rate/) of the currency you are funding (the quoted currency) minus the interest rate of the currency you own (the base currency).*

In a simple [EUR/USD](/wiki/eur-gbp-euro-sterling/) position, suppose a trader is long 1,000,000 EUR (owns euros) and short 1,200,000 USD (borrowed dollars at 5.5% annually). The ECB's base rate is 4.0% and the Fed's is 5.5%. Each day the position is held overnight, the trader receives 4.0% / 365 on the EUR (roughly €1,096) and pays 5.5% / 365 on the USD (roughly $2,055), for a net carry cost of roughly $959 per day. Over a year, that is a $350,000 drag on the position—essentially paying to hold EUR/USD long. This is why carry trading is attractive when the interest differential favors the long currency—traders earn overnight interest while betting on appreciation.

<aside class="wiki-infobox">

| Component | Detail |
|---|---|
| **Calculation** | (Interest on base currency) – (interest on quote currency) |
| **Example** | Long EUR/USD: earn 4% on EUR, pay 5.5% on USD = -1.5% carry |
| **Frequency** | Daily (rolled at 5 PM NYC time, typically) |
| **Accrual** | Automatic; credited/debited to account balance |
| **Leverage impact** | Carry multiplied by [margin](/wiki/forex-margin/) employed |
| **Volatility risk** | Positive carry tempts over-leverage; can amplify losses |
| **Tax status** | Ordinary income (unless dealer status) |
| **Market factor** | Differentials driven by central bank rate policy |

</aside>

## Carry trade mechanics

A **carry trade** is a strategy that profits from the carry cost differential. A trader identifies two currencies with a large interest-rate gap—for instance, in the late 2000s, when the Fed was at 0% and the New Zealand OCR was 8%, shorting USD/NZD (borrowing dollars at 0%) and going long NZD (earning 8%) was a profitable carry trade, earning 8% per year *before* any appreciation of NZD.

The trade works as follows:
1. Borrow low-rate currency (e.g., JPY at 0.5%, [USD](/wiki/us-dollar/) at 5.5%).
2. Buy high-rate currency (e.g., AUD at 4.3%, BRL at 13%).
3. Hold overnight; receive the interest differential daily.
4. Unwind when the differential narrows or the exchange rate moves against you.

During low-volatility markets (when the [VIX](/wiki/fear-index/) is calm and [risk appetite](/wiki/risk-on-risk-off/) is high), carry trades are crowded—many hedge funds and prop traders pile into the same trade, amplifying returns and risk. When markets correct suddenly, carry positions unwind violently—borrowers must buy back the cheap currency fast, causing sharp moves.

## Overnight rollover in retail forex

For retail traders on [forex](/wiki/forex-margin/) brokers, overnight carry is called the "rollover" or "swap." If a trader goes long AUD/USD from 5 PM Friday to 5 PM Monday, they may be charged a triple rollover (weekend + two days) or collect triple interest, depending on which currency has the higher rate. Most brokers publish rolling rates daily on their platform.

High leverage magnifies carry costs. A trader using 50:1 leverage to hold 1 million dollars of AUD/USD exposure (with ~$20,000 margin) earns or pays the carry on the full $1M notional, not just the $20k. If carry is -1% (negative for the long position), the trader loses $10,000 per year, or $27 per day, on a $20k account—a 0.13% drag daily, compounding.

## Carry cost in derivatives

In [interest-rate swaps](/wiki/interest-rate-swap/), [currency swaps](/wiki/cross-currency-swap/), and [forwards](/wiki/forward-contract/), the carry cost is priced into the [forward rate](/wiki/forward-exchange-rate/). A 1-year [forward](/wiki/forward-contract/) EUR/USD price is lower than the spot EUR/USD price if USD interest rates are higher than EUR rates (because borrowing EUR to buy spot, then selling forward, locks in the interest-rate loss). The [forward premium](/wiki/forward-exchange-rate/) or discount encodes the carry.

For example, spot EUR/USD is 1.0900. Holding 1,000,000 EUR costs 1.5% annually in net financing (paying USD rates, earning EUR rates). After one year, the trader expects to be out of pocket 15,000 EUR in interest. To hedge, they agree to sell 1,000,000 EUR forward at a 1-year forward rate. That rate is roughly 1.0850 (lower than spot), reflecting the negative carry.

## Relationship to currency risk and hedging

Companies with international operations face currency exposure. An exporter selling in GBP but funding costs in USD faces carry cost drag: they receive GBP (lower rate, currently ~4.75% for the Bank of England) but must pay USD loans (5.5%). The net carry is -0.75% per year, or roughly £7,500 per million pounds. To hedge, the exporter can sell GBP forward at the discounted forward rate, locking in the loss but eliminating the currency risk.

Currency traders distinguish between **funded carry** (the actual interest cost of holding a position in leveraged forex accounts) and **economic carry** (the expected interest-income differential in the cash markets). Funded carry is typically higher due to [spreads](/wiki/bid-ask-spread-forex/) and broker markups; economic carry is what an unleveraged investor would capture by simply holding a higher-yielding currency.

## Policy and market implications

When central banks raise rates sharply (as the Federal Reserve did in 2022–2023), carry-trade dynamics shift. The USD became highly attractive to borrow at low cost and invest globally, flattening opportunities. Conversely, when the Fed cuts and other banks hold (as in 2024 expectations), differentials widen and carry trades re-attract capital.

Carry-trade unwinds are systemic risks. In August 2024, a carry-trade crash (yen strength, deleveraging of USD short positions) caused a mini-crash in [equity markets](/wiki/stock-market/) as leveraged traders unwound positions. The [Bank of Japan](/wiki/bank-of-japan/)'s rate hike tightened carry differentials, triggering margin calls and forced selling.

<div class="wiki-seealso">

### Closely related
- [Carry Trade](/wiki/carry-trade/) — strategy exploiting carry cost differentials
- [Interest Rate](/wiki/interest-rate/) — driver of carry cost
- [Currency Pair](/wiki/currency-pair/) — the two currencies involved
- [Forex Margin](/wiki/forex-margin/) — leverage that magnifies carry costs

### Wider context
- [Central Bank Policy](/wiki/central-bank-policy-tools/) — interest-rate setting
- [Forward Exchange Rate](/wiki/forward-exchange-rate/) — priced with carry embedded
- [Currency Hedging](/wiki/currency-hedging/) — technique to reduce carry costs
- [Interest Rate Parity](/wiki/interest-rate-parity/) — theoretical relationship between spot and forward rates

</div>
