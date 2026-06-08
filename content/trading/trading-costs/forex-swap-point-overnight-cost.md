---
title: "Forex Swap Points and Overnight Carry Cost"
description: "How swap points on FX positions are calculated from interest rate differentials and charged as a carry cost."
keywords:
  - forex swap points overnight cost
  - FX overnight carry cost
  - swap points interest differential
  - forex carry trade costs
image: /svg/trading.svg
---

*A **forex swap point** is the interest cost or credit applied to spot FX positions held overnight. When you hold a foreign currency position beyond the settlement date, the interest rate differential between the two currencies determines whether you pay or receive a credit. Swap points accumulate daily and are a direct cost of carry for traders, particularly important for [carry-trade](/carry-trade/) strategies and long-term FX positions.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Forex Swap Points — key facts</div>

<img src="/svg/trading.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Daily cost or credit from holding FX overnight; determined by interest rates.</div>

|   |   |
|---|---|
| **Calculation** | Interest rate differential / 365 × notional position size |
| **Direction** | Debit if home rate > foreign rate; credit if foreign > home |
| **Charged** | Daily, at market open or on broker's timetable |
| **Impact on returns** | Reduces carry trade profit if rates unfavorable; boosts if favorable |
| **Alternative term** | "Overnight financing cost" or "roll-over cost" |

</aside>

## How swap points work

When you buy a foreign currency (say, EUR/USD), you own euros and owe dollars. The position rolls forward each night. To finance the long foreign position (which you've borrowed at the home currency rate) and earn interest on the domestic currency you've lent, the broker charges or credits you the difference between the two interest rates.

If the EUR (foreign) rate is 4% and the USD (home) rate is 5%, you pay a financing cost. The U.S. interest rate is higher, so holding euros costs you the 1% differential. The daily swap point is approximately:

**Swap point = (EUR rate − USD rate) / 365 × notional**

For €100,000 at a 1% differential:

Swap point = (0.04 − 0.05) / 365 × 100,000 = −€27.40

The negative sign indicates a debit (cost to you).

## Broker quotation conventions

Brokers quote swap points as two prices: the bid (rate they pay if you're short) and the ask (rate they charge if you're long). In major pairs, swap points are tight; in exotic pairs, they widen significantly. The bid-ask spread on swap points is analogous to the [bid-ask-spread](/bid-ask-spread/) on the spot rate itself.

A trader might see EUR/USD quoted with swap points of "−27 / −25", meaning holding long EUR costs about 27 pips daily, and holding short pays about 25 pips. The spread between bid and ask is 2 pips—the broker's margin for funding the trade.

## Relationship to interest rate differentials

Swap points reflect the interest rate differential between the two currencies. If the [federal-funds-rate](/federal-funds-rate/) rises in the U.S., the swap cost for holding foreign currencies increases immediately. Conversely, if a central bank cuts rates, holding that currency becomes cheaper (or more profitable).

The formula is a simplified version of the interest rate parity relationship: the difference between the spot and [forward-contract](/forward-contract/) FX rates should equal the interest rate differential. Swap points are the daily manifestation of this relationship. Over a full year, the accumulated daily swap points approximate the difference between spot and the 12-month forward rate.

## Carry-trade mechanics and swap costs

[Carry-trade](/carry-trade/) strategies exploit interest rate differentials. A trader borrows in a low-rate currency (e.g., Japanese yen at near-zero rates) and invests in a high-rate currency (e.g., Brazilian real at 10%+). The daily swap points are a large part of the carry trade's P&L.

If swap points are favorable (you receive a credit for holding the position), they subsidize your carry return. If unfavorable (you pay), they reduce your profit. The real return from a carry trade is:

Carry return = Interest differential − [currency-volatility](/currency-volatility/) losses ± spot move ± swap cost adjustments

Carry traders obsess over swap point schedules. Many brokers adjust swap points intra-day if their own funding costs shift, and swap point levels can widen dramatically in periods of [credit-risk](/credit-risk/) stress or liquidity crunch.

## Triple-paying weekends

Most brokers charge swap points for Fridays three times over (once at close Friday, once at close Saturday, once at close Sunday), since markets don't trade weekends but the carry of the position accrues. This "triple" treatment means holding a position over a weekend is more expensive. If you plan to close a position Friday, you'll avoid the weekend charge.

Alternatively, some brokers quote swaps for the full week on Fridays and don't separate out the weekend; the effect is the same—longer holding times cost more in absolute terms.

## Non-linear swap schedules and rollover periods

Swap points are not constant. Central bank policy, market expectations of future rate moves, and [credit-risk](/credit-risk/) premiums all shift swap points dynamically. A currency pair with a favorable swap point today might become unfavorable after a central bank announcement.

Also, swap points can differ sharply across rollover times. For some banks, the rollover is at 5 p.m. New York time (the standard FX settlement time, T+2 in most cases). For others, it's 12 a.m. London time. Traders must track their broker's rollover time to understand when costs are applied.

## Swap points on leveraged positions

Leverage magnifies swap costs. A retail trader holding 10:1 leverage on a €100,000 position (notional €1 million) sees swap charges 10 times larger. This is a major hidden cost for leveraged forex traders and a driver of losses in undercapitalized or over-leveraged accounts.

## Hedging and swap point adjustments

Corporate treasurers and investors use FX forwards or swaps to hedge currency exposure. The swap cost embedded in a [forward-contract](/forward-contract/) rate reflects the interest differential. If a U.S. company needs EUR in three months, the forward rate will be lower than the spot rate (if USD rates exceed EUR rates), locking in a "discount" on future EUR purchases. This discount is the cumulative carry cost.

## Relationship to term structure and [basis-risk](/basis-risk/)

The difference between spot and forward rates incorporates swap points. As a position approaches expiry, the forward converges to spot, and the remaining carry cost diminishes. Traders who manage large FX positions often think in terms of roll-over costs: the cost of rolling from today's forward to tomorrow's forward, month by month. Unexpected moves in swap points can create [basis-risk](/basis-risk/) for hedging programs.

## See also

<div class="wiki-seealso">

### Closely related

- [Carry trade](/carry-trade/) — strategy exploiting rate differentials
- [Forward contract](/forward-contract/) — locked-in future FX rate
- [Interest rate](/interest-rate/) — determines swap direction and magnitude
- [Currency volatility](/currency-volatility/) — risk offsetting carry return
- [Bid-ask spread](/bid-ask-spread/) — transaction cost alongside swap points

### Wider context

- [Federal funds rate](/federal-funds-rate/) — U.S. rate driver
- [Credit risk](/credit-risk/) — affects broker funding costs
- [Basis risk](/basis-risk/) — mismatch between hedge and underlying
- [Leverage ratio forex](/leverage-ratio-forex/) — magnifies carry costs and drawdowns

</div>
