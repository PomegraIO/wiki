---
title: "Spot Value Date"
description: "The standard settlement date for FX spot trades, two business days after execution, which accommodates clearing and payment infrastructure across currencies."
keywords:
  - spot value date
  - FX settlement
  - forex mechanics
  - T+2 settlement
  - settlement risk
image: "/svg/forex.svg"
---

*The **spot value date** in forex is the date on which both parties to an FX spot trade actually exchange the principal currencies. It falls two business days after the trade is struck—written as T+2 in market convention. This two-day window allows payment and custody systems across different countries to coordinate the delivery.*

<div class="wiki-hatnote">

For the one-day rollover convention that bridges tomorrow and spot, see [Tom-Next in FX](/tom-next-forex/).

</div>

## Why two days?

The foreign exchange market is vast but operationally complex. When a trader in London agrees to sell euros for dollars, the actual cash—physical or electronic—must move between bank accounts in Frankfurt (for euros) and New York (for dollars). Those two financial centres operate on different local business days, use different payment systems, and require time for compliance checks.

The two-day settlement window emerged as a compromise that gives both legs of the trade time to clear. The first day allows each side to instruct its bank to prepare the payment. The second day allows the banks themselves to confirm receipt and custody. If the trade settled T+0 (same-day), the operational risk would be enormous: one party might deliver currency only to find the counterparty had failed.

This T+2 convention is so entrenched that it applies to almost all FX spot trades, regardless of currency pair. A trade of USD/GBP, USD/JPY, or EUR/AUD all settle two business days forward.

## Spot date in different calendars

One twist: the two business days are counted in *both* currency zones. A EUR/USD trade executed on Monday (London and New York both open) settles on Wednesday. But if the trade is struck on Thursday and Friday is a holiday in New York (but not London), then:

- Thursday to Friday: one business day has passed.
- Friday to Monday: Monday is the first business day *after* the holiday, so it counts as the second day.

Spot date becomes Wednesday.

Banks and settlement systems account for [holidays](/sovereign-default/) in multiple time zones. In December, when Christmas falls on a weekend but is observed on different days in different regions, spot date calculations get tricky. Most market participants use published holiday calendars (published by SFEMC, the Securities Industry and Financial Markets Association) to keep everyone aligned.

## The spot market versus spot rate

"Spot" in forex refers to two related but distinct things. The **spot rate** is simply the price of the currency pair quoted today, as opposed to forward or futures rates. The **spot market** is the market for immediate (or near-immediate) delivery, where trades are struck and settled at that spot rate.

The spot value date (T+2) is the settlement point that defines the boundary between the spot market and the [forward](/forward-contract/) markets. A trade for delivery beyond T+2 is technically a forward, not a spot trade, and trades at a different price (usually reflecting interest-rate differentials between the currencies).

## Operational workflow

From the trader's desk to settlement:

1. **Trade execution** (T+0): Buyer and seller agree on a rate, amount, and currencies. Confirmation is generated.

2. **Instruction period** (T+0 to T+1): Each counterparty instructs its bank to arrange payment. Compliance checks occur: beneficial ownership, sanctions screening, counterparty credit limits.

3. **Novation and netting** (T+1): Large financial institutions may offset or net their positions with the same counterparty, to reduce the number of actual cash transfers. Clearing houses (in some cases) may step in as intermediary.

4. **Delivery** (T+2): The actual funds are transferred. A's bank debits A's account and credits B's bank. B's bank debits B's account and credits A's account (in the other currency, simultaneously).

In reality, most of this happens electronically. The [SWIFT](/over-the-counter-market/) network and domestic payment systems (like Fedwire in the US) handle the choreography, often with minimal human intervention.

## Why spot date matters for trading

Spot value date is not merely technical; it influences pricing and [counterparty risk](/counterparty-risk/):

- **Carry cost**: If you buy euros and have to wait two days to receive them, you've implicitly financed that purchase for two days. A dealer will charge you a small amount, embedded in the spot price, for that financing cost. A trader who can settle faster (via [Tom-Next](/tom-next-forex/) or [same-day settlement](/spot-value-date/), if available) might pay a different price.

- **Default risk**: Between T+0 (the trade) and T+2 (settlement), both counterparties are exposed to the other's credit. If the counterparty fails on T+1, the first party has already promised to deliver currency but may not receive any in return. This settlement risk is one reason why major banks use clearing houses and central counterparties in large spot trades.

- **Pricing across maturities**: The relationship between the spot rate and forward rates is anchored by the interest-rate differentials over the T+2 period. If EUR rates rise faster than USD rates between now and the spot date, the euro will trade at a premium in the forward market.

## Exceptions and alternatives

In most cases, spot settlement is T+2. But exceptions exist:

- **Major pairs (USD/EUR, USD/GBP, USD/JPY)**: Standard T+2 settlement.

- **Emerging market currencies**: Some may settle T+1 or T+3 due to local payment system limitations.

- **CNY (offshore, CNH)**: Often T+2 but sometimes with different holiday calendars.

- **Crypto-collateralised settlements**: Some newer platforms settle FX forwards and swaps instantly or on custom schedules.

- **Expedited settlement**: For very large or strategically important trades, counterparties may negotiate same-day delivery at a premium.

## Central clearing and spot settlement

The rise of central clearing houses (LCH, CME, EUREX) in FX markets has changed settlement dynamics. When both parties clear through the same house, that house becomes the counterparty to both sides and guarantees settlement. This reduces [bilateral counterparty risk](/counterparty-risk/) but introduces clearing-house risk. Most major spot FX trades now go through a clearing house, shortening effective settlement risk even though the calendar date is still T+2.

## Conventions in practice

Professional traders and settlement specialists know that spot value date is a mechanical rule, but it has teeth. Missing a spot date (failing to deliver when promised) incurs a **fail charge**: a daily penalty that accrues until the trade is settled. Repeated failures can breach a bank's credit agreement.

For this reason, treasury and operations teams carefully track spot dates, even in liquid currency pairs. A small trade in a major currency pair is almost never a settlement problem; a large trade in an exotic pair on a day near a holiday can be.

## See also

<div class="wiki-seealso">

### Closely related

- [Tom-Next in FX](/tom-next-forex/) — the one-day rollover convention bridging tomorrow and spot
- [Forward contract](/forward-contract/) — FX transactions with settlement beyond spot date
- [Counterparty risk](/counterparty-risk/) — credit risk between two parties over the settlement window
- [Interest rate](/interest-rate/) — the driver of price differentials between spot and forward
- [Over-the-counter market](/over-the-counter-market/) — decentralised market where most FX spot trades occur

### Wider context

- [Currency risk](/currency-risk/) — exposure to moves in exchange rates
- [Settlement](/counterparty-risk/) — operational and credit risks between trade and settlement
- Forex — foundational mechanics of foreign exchange markets

</div>
