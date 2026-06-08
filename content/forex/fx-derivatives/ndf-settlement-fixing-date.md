---
title: "NDF Settlement and Fixing Date: How Non-Deliverable Forwards Are Settled"
description: "On the fixing date of a non-deliverable forward, the reference rate is locked and the cash difference is paid. No currency is delivered—only the P&L."
keywords:
  - ndf fixing date
  - ndf settlement
  - non-deliverable forward cash settlement
  - ndf reference rate
  - how ndf works
image: /svg/forex.svg
---

*A **non-deliverable forward (NDF) settling** means that on the agreed fixing date, a reference rate is published, the cash difference between your contracted rate and that spot is calculated, and money changes hands. No foreign currency is ever delivered—only the profit or loss gets paid in the domestic currency.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">NDF Settlement and Fixing Date — Key Facts</div>

<img src="/svg/forex.svg" alt="An abstract editorial mark for forex derivatives." />

<div class="wiki-infobox-caption">NDFs lock in a rate today, settle in cash on a future fixing date using an official benchmark rate.</div>

|   |   |
|---|---|
| **Fixing date** | Pre-agreed date when the reference rate is locked (usually 2 business days before settlement) |
| **Settlement date** | When cash is paid (typically spot + 2 days, e.g., USD/INR in 2 calendar days) |
| **Reference rate** | Official published rate (RBI, central bank fixings, or Bloomberg poll) |
| **P&L calculated** | (Spot at fixing − Contracted NDF rate) × Notional × Settlement currency per unit |
| **Delivery risk** | Zero—only cash settles, making NDFs legal in countries restricting FX deliverables |
| **Typical maturity** | 1 month to 5 years (longer than [forward contracts](/forward-contract/) on convertible pairs) |

</aside>

## Why NDFs Exist and When You Use Them

Most currency pairs allow [deliverable forwards](/forward-contract/)—you lock in a rate, and at maturity you physically exchange the currencies. But many emerging-market currencies (Indian rupee, Brazilian real, Korean won, Chinese yuan) have restrictions or lack deep offshore delivery markets.

An **NDF** lets you hedge the rate without needing to deliver. You and your counterparty agree on a notional amount and a contracted rate. At maturity, neither of you exchanges the underlying currency; instead, you settle the P&L in a freely traded currency, usually US dollars.

A US exporter shipping goods to India can use a USD/INR NDF to lock in the rupee value of his payment. When the rupee payment arrives (say, 50 days later), he's guaranteed the pre-agreed exchange rate. The NDF settles separately in dollars, taking the difference between the actual spot and his contracted rate.

## The Fixing Date and Reference Rate

The **fixing date** is the day the reference rate is determined. It is *not* the same as the settlement date. There is a 2-business-day lag (sometimes 1 day in liquid pairs).

For a typical USD/INR NDF settling on, say, 15 June:
- **Fixing date**: 13 June (2 business days before settlement)
- **Settlement date**: 15 June (when cash moves)

On 13 June, the reference rate is locked. The most common reference is the official [Reserve Bank of India fixing](/spot-exchange-rate/) published at 12:30 pm IST. For other currencies, it might be:
- The central bank's daily mid-rate
- A benchmark from Thomson Reuters or Bloomberg
- A poll of dealer prices, published and certified

The contract specifies which reference applies. The reference is almost always a midpoint (no [bid-ask spread](/bid-ask-spread/)), so neither party has a profit incentive to move the rate—it's purely mechanical.

## How Cash Settlement Works

The P&L is calculated in the settlement currency, almost always US dollars:

**P&L = (Spot at fixing − NDF rate) × Notional × (settlement currency per unit of spot currency)**

Example:
- You bought a USD/INR NDF: locked in 83.50 rupees per dollar, notional $1 million.
- Fixing date arrives, and the RBI fixing is 82.50.
- The dollar appreciated (it's worth more rupees than you contracted for).
- P&L = (82.50 − 83.50) × 1,000,000 = −1,000,000 rupees.
- This loss is paid in dollars. At 82.50, 1 million rupees ÷ 82.50 = $12,121 paid by you to the counterparty.

If the fixing had been 84.50, you'd have won: (84.50 − 83.50) × 1,000,000 = 1,000,000 rupees profit, which at 84.50 = $11,834 paid to you.

The settlement happens in dollars (or sometimes euros for non-USD pairs), deposited into agreed settlement accounts. Many NDFs settle via [SWIFT](/), with T+2 clearing through standard forex settlement rails.

## The Role of the Fixing Date in Risk Management

The fixing date is the moment your hedge locks in. Any market move *before* the fixing affects your P&L. Any move *after* the fixing is irrelevant to the NDF.

This is crucial for corporates managing invoice timing:

- **Invoice arrives 15 June**: You receive 50 million rupees. The NDF fixing is that day, so you *immediately* know your dollar value. No guessing, no daily mark-to-market wobble.
- **Invoice arrives 10 June**: Your fixing isn't until 15 June. You have 5 days of unhedged rupee risk. The rupee could weaken (bad for you) and you lose money between invoice date and fixing date.

Many corporates align their NDF fixing date to their invoice date or settlement date, paying a slight premium for customization. Standard NDFs (1M, 3M, 6M, 1Y maturity) use calendar maturity dates (e.g., 15th of the month), cheaper and more liquid. Bespoke fixing dates are less frequent and cost more.

## Operational Flow: From Contract to Settlement

1. **Day 0 (trade date)**: Dealer and client agree on USD/INR NDF. Rate 83.50, notional $10M, 1-month maturity. Settlement 15 June, fixing 13 June.

2. **Day 1–12**: Market moves. NDF is [mark-to-market](/mark-to-market/) daily in accounting (both sides track the unrealized P&L), but no cash moves.

3. **13 June (fixing date)**: RBI publishes 82.80 at 12:30 pm IST. Both dealer and client compute the P&L: (82.80 − 83.50) × $10M = −$7M rupees, or roughly $84,600 (at 82.80 per dollar). The dealer sends a settlement instruction.

4. **13 June evening**: Confirmations exchanged. Both parties verify the fixing rate, notional, and calculated P&L. No disagreement on the fixing—it's published by a third party (RBI).

5. **15 June (settlement date)**: Cash settles. The party owing money deposits dollars (or the counterparty receives them).

6. **Post-settlement**: The NDF is closed. If you needed renewed hedging (say, for the next month), you'd enter a new NDF at a new negotiated rate.

## Comparing NDF Settlement to Deliverable Forwards

A **[deliverable forward](/forward-contract/)** uses similar mechanics for the fixing date, but the final outcome is different:

| **Aspect** | **NDF** | **Deliverable Forward** |
|---|---|---|
| **At fixing** | Rate is locked; P&L computed in cash | Rate is locked; currency exchange calculated |
| **Settlement** | Dollar/settlement currency P&L paid | Physical currencies exchanged |
| **Used when** | Currency is non-convertible or restricted | Currency is freely deliverable |
| **Duration** | Often longer (months to years) | Usually shorter (spot to 12 months) |
| **Liquidity** | Deep for major emerging-market pairs | Deep for G-10 currencies |

## Key Dates and Conventions

NDF contracts specify multiple dates clearly:

- **Trade date**: When you and the dealer agree (T+0).
- **Spot date** (or value date): Usually 2 business days from trade. Spot rate at trade date is the market rate on this day. Not used for NDF P&L, but used as the reference point for the NDF rate negotiation.
- **Fixing date**: Defined in the contract, often T+1M, T+3M, etc. This is when the benchmark is locked.
- **Settlement date**: Usually fixing date + 2 business days, or may be same-day depending on the currency.

Some pairs (e.g., USD/CNY) trade "deliverable NDFs" that *can* be physically settled if both parties agree, but cash settlement is the default. Others (USD/INR, USD/BRL) are purely cash-settled by convention and law.

## Practical Nuances

**Holiday adjustments**: If the fixing date falls on a holiday in the reference country, the fixing is usually moved back one business day. The contract specifies "modified following" or "preceding" convention.

**Dealer spread**: The quoted NDF rate includes the dealer's profit. On a USD/INR 1M, they might quote 83.40–83.60 (client can buy at 83.60 or sell at 83.40). The actual RBI fixing at maturity is irrelevant to your profit; your P&L locks in at the rate you contracted, 83.40 or 83.60.

**Volume and liquidity**: The most liquid NDFs are 1M, 3M, 6M, and 12M. Longer tenors or off-the-run fixing dates trade wider (larger spreads, higher cost).

**Margin and collateral**: Banks often require variation margin on NDFs if they move significantly in the customer's favor. A $10M NDF that's suddenly $500K underwater for the bank might trigger a margin call to reduce credit risk.

## See also

<div class="wiki-seealso">

### Closely related

- [Forward Contract](/forward-contract/) — Deliverable forwards, used when the currency can be exchanged physically
- [Spot Exchange Rate](/spot-exchange-rate/) — The reference rate at the fixing date determines the final settlement
- [Currency Risk](/currency-risk/) — Why businesses use NDFs to hedge emerging-market currency exposure
- [FX Option Expiry Cut Conventions](/fx-option-expiry-cut-conventions/) — Options also use fixing dates to lock in rates
- [Interest Rate Swap](/interest-rate-swap/) — Similar mechanics: fixing date locks a benchmark (LIBOR or SOFR)
- [Mark-to-Market](/mark-to-market/) — How NDFs are valued daily between trade and settlement

### Wider context

- [Derivatives Hedging](/derivatives-hedging/) — Broader view of hedging tools
- [Counterparty Risk](/counterparty-risk/) — Why margins and credit limits matter in NDF trading
- [Foreign Exchange Derivatives](/derivatives-hedging/) — Other FX hedging tools and strategies
- [Quanto FX Options Explained](/quanto-fx-option-explained/) — Exotic options that also use fixing dates to determine payoff

</div>