---
title: "Hedge Accounting Discontinuation Rules"
description: "IFRS 9 and ASC 815 conditions that require or allow companies to stop hedge accounting, and the income-statement consequences of dedesignation."
keywords:
  - when to discontinue hedge accounting
  - hedge accounting discontinuation
  - ifrs 9 hedge accounting
  - asc 815 dedesignation
  - hedge accounting income statement impact
image: "/svg/risk.svg"
---

*When to discontinue hedge accounting under **IFRS 9** and **ASC 815** depends on whether the hedge has become ineffective, the hedging relationship is no longer designated, or the hedging instrument is disposed of—each path triggering different income-statement consequences, from immediate mark-to-market on the derivative to reversal of accumulated other comprehensive income balances.*

<div class="wiki-hatnote">

This article addresses hedge accounting discontinuation under IFRS 9 (International) and ASC 815 (US GAAP). It does not cover general hedge effectiveness testing, fair-value vs. cash-flow hedge mechanics (though both apply), nor discontinued operations or segment exits.

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Hedge Accounting Discontinuation — Key Facts</div>

<img src="/svg/risk.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Rules for exiting hedge accounting and the accounting for residual derivative values.</div>

|   |   |
|---|---|
| **Triggering events** | Derivative expires or is sold; hedged item matures or is sold; hedge becomes ineffective; designation is revoked; critical terms change |
| **Fair-value hedge** | Accumulated fair-value adjustments on hedged item are amortized into earnings; derivative is marked-to-market in P&L |
| **Cash-flow hedge** | Accumulated OCI is reclassified to earnings when the forecasted transaction occurs; unused OCI remains until transaction settles |
| **Net-investment hedge** | Accumulated currency adjustments in OCI remain until the investment is disposed or the foreign subsidiary is sold |
| **Prospective vs. retroactive** | Discontinuation is prospective (stops hedge accounting going forward); prior-period accounting is not reversed |
| **Ineffectiveness designation** | If hedge was never effective, hedge accounting is prohibited retroactively (catch-up required) |
| **Income-statement volatility** | Fair-value hedge: minimal (derivative and item move together); cash-flow hedge: OCI release follows the hedged transaction; net-investment: minimal |

</aside>

## The Discontinuation Trigger

Hedge accounting is discontinued when:

1. **The hedging instrument expires or is settled.** A forward contract matures, an option lapses, or the derivative is sold.
2. **The hedged item is derecognized.** The bond is paid off, the loan is settled, the forecasted transaction is no longer probable.
3. **The hedging relationship is dedesignated.** Management revokes the hedge designation in writing, even though the derivative and item still exist.
4. **The hedge relationship fails effectiveness tests.** IFRS 9 requires "highly effective" (80–125% ratio) and ASC 815 requires the same; if effectiveness falls outside this band, hedge accounting is no longer permitted going forward.
5. **Critical terms have changed.** If the tenor, notional, currency, or index of the derivative no longer aligns with the hedged item, hedge accounting may be discontinued.

The key distinction: **prospective discontinuation**. When hedge accounting ends, prior-period entries are not reversed. The company stops treating new gains/losses as hedging entries; old accumulated balances are handled according to the hedge type.

## Discontinuation in Fair-Value Hedges

In a fair-value hedge, the company adjusts both the derivative *and* the hedged item for fair-value changes. When the hedge is discontinued:

**The hedged item's balance sheet value includes accumulated fair-value adjustments.** If you hedged a $100 million bond issuance at 4% fixed, the bond's carrying value went up or down with [interest rates](/interest-rate/). When you discontinue the hedge, that fair-value adjustment remains on the [balance sheet](/balance-sheet/) but is no longer updated.

The fair-value adjustment is **amortized into earnings** over the remaining life of the hedged item. If the bond has 5 years left and the adjustment is $2 million, the company books $400k in amortization each year until maturity, a synthetic reduction (or increase) to interest expense.

**The derivative is immediately fair-valued in earnings.** If the discontinued hedging derivative (say, an interest-rate swap) has a positive fair value, it becomes an asset on the balance sheet and is marked-to-market through P&L each period. If its value swings by $500k in the next quarter, that full amount hits earnings immediately.

**Result: Income-statement volatility.** After discontinuation, the derivative's mark-to-market is no longer offset by changes in the hedged item's fair value. The P&L becomes choppy.

### Example: Discontinued Fair-Value Hedge

A company issued a $100 million bond at 4% fixed. To hedge interest-rate risk, it entered a pay-fixed, receive-floating swap. For three years, interest rates fell, so the bond's fair value rose to $105 million (and was carried at that value due to fair-value hedge accounting). The swap, which the company sold, became a liability (fair value −$5 million due to the pay-fixed leg).

At year 3, the company unwinds the swap for $5 million cash (a loss), realizing that the $100M bond is no longer exposed to interest-rate swings (it has ~7 years left and the company accepts the lower coupon).

Upon discontinuation:
- The bond's carrying value of $105 million includes a $5 million fair-value adjustment.
- That $5 million adjustment is amortized over 7 years at ~$714k/year, reducing interest expense.
- The swap is derecognized; the $5 million loss is booked immediately in the P&L (or possibly reclassed if there was prior gain in OCI).
- Going forward, the bond's fair value is *not* recorded; only its amortized cost is carried.

## Discontinuation in Cash-Flow Hedges

Cash-flow hedges are trickier. The derivative is marked-to-market in other comprehensive income (OCI), not P&L, while the hedged item (e.g., a forecasted purchase) is carried at cost.

When a cash-flow hedge is discontinued, the company stops recording derivative gains/losses in OCI. **The accumulated OCI balance remains in equity.** When the forecasted transaction occurs (e.g., you buy the commodity you were hedging), the accumulated OCI is released to P&L and matches against the transaction's cost/revenue impact.

**The derivative itself continues to be marked-to-market.** But going forward, that mark-to-market enters P&L directly, not OCI, creating an asymmetry: the hedged item is still at cost, but the derivative is at fair value.

### Example: Discontinued Cash-Flow Hedge

A European exporter expects to receive €1 million in 6 months from a customer. To lock in the USD exchange rate, it enters a EUR/USD forward contract. Over 3 months, the euro strengthens; the forward gains $50k. That gain is recorded in OCI (not P&L) because the forecasted EUR receipt hasn't occurred yet.

At month 4, the company decides to discontinue the hedge. It no longer believes the euro will strengthen further, and it wants to exit the forward. Upon discontinuation:

- The accumulated $50k gain remains in OCI.
- The forward is no longer designated as a hedge.
- If the forward's value changes over the next 2 months (say it gains another $20k), that $20k is *now* recorded in P&L, not OCI.
- When the €1M is received (month 6), the original $50k accumulated OCI is released from equity to P&L, offsetting (or adding to) the month-6 translation gain/loss.

**The asymmetry can be jarring.** For 2 months, new forward gains enter P&L, but the hedged item (the €1M receivable) is still at cost. Then, when the transaction settles, the old OCI hits P&L all at once.

## Discontinuation in Net-Investment Hedges

A net-investment hedge uses a foreign-currency derivative (or a foreign-currency debt) to hedge the foreign-currency exposure of a subsidiary investment. When discontinued:

**Accumulated OCI remains in equity.** Unlike a cash-flow hedge, the accumulated balance is *never* reclassified to P&L unless the company divests the subsidiary or the foreign subsidiary is liquidated. It remains "in transit" indefinitely.

This creates a peculiarity: a company can have unrealized foreign-exchange gains locked in OCI for decades if it maintains the foreign subsidiary and never sells it.

## Mandatory Discontinuation Due to Ineffectiveness

Under IFRS 9 and ASC 815, if a hedge fails effectiveness tests (the ratio of hedge gain/loss to item gain/loss falls outside 80–125%), hedge accounting **must** cease immediately.

Critically, this is **retroactive** for IFRS 9: if the company discovers a month into a quarterly hedge that effectiveness is poor, it must restate prior periods, undoing hedge accounting entries. The derivative and item are separately fair-valued, and no more hedging offset applies.

ASC 815 is slightly more lenient: failure to document or test effectiveness prospectively triggers dedesignation, but restatement is not always required if the hedge was actually effective economically.

## Disposal of the Hedged Item

If the company sells the hedged item before the derivative expires:

**Fair-value hedge:** The accumulated fair-value adjustment is derecognized along with the item. The gain or loss on the item (including the fair-value adjustment) is realized in P&L. The derivative, if still outstanding, is marked-to-market and treated as an unhedged derivative.

**Cash-flow hedge:** If the forecasted transaction no longer exists (you sold the asset before you received the revenue), the hedge is no longer protecting a future cash flow. Hedge accounting must cease. Accumulated OCI is reclassified to P&L when... this is ambiguous. If the underlying transaction never occurs, OCI remains pending indefinitely in many interpretations, though ASC 815 permits release to P&L if the forecasted transaction becomes unlikely.

## Management Dedesignation (Voluntary Discontinuation)

A company can *elect* to discontinue hedge accounting even if the derivative and item remain and the hedge is effective. Common reasons:

- **Rebalancing the balance sheet.** The company wants to take a fair-value adjustment onto the item and live with it.
- **Avoiding OCI volatility.** A company with volatile OCI may want to move to mark-to-market P&L accounting to reduce balance-sheet fluctuations.
- **Tax planning.** Discontinuing a hedge can affect the tax character of gains/losses.

Upon voluntary dedesignation:
- The derivative is immediately fair-valued in P&L (if not already).
- Accumulated OCI/adjustments follow the rules above for the hedge type.
- The company documents the dedesignation in writing and applies the rules prospectively.

## Income-Statement Consequences Summary

| Hedge Type | Discontinuation Impact | P&L Volatility | OCI/Equity Impact |
|------------|------------------------|----------------|-------------------|
| **Fair-value** | Derivative mark-to-market; fair-value adjustment amortized | High (derivative swings) | FV adjustment slowly amortizes; OCI released if any |
| **Cash-flow** | Derivative mark-to-market in P&L; accumulated OCI remains | Medium (new derivative moves hit P&L) | Accumulated OCI released when transaction settles |
| **Net-investment** | Derivative mark-to-market in P&L; accumulated OCI in equity | Medium (currency moves) | Accumulated OCI remains until subsidiary sold |

## Audit and Disclosure

When a company discontinues hedge accounting, it must disclose:
- The reason for discontinuation.
- The impact on earnings and OCI in the period of discontinuation.
- Remaining derivative fair values and intended accounting treatment.

Auditors scrutinize discontinuations carefully. A pattern of discontinuations (especially before year-end) can suggest earnings management. A hedge that becomes suddenly "ineffective" just because the company wants to unwind it raises red flags.

## See also

<div class="wiki-seealso">

### Closely related

- [Derivatives hedging](/derivatives-hedging/) — The strategic use of derivatives to hedge risk
- [Fair value](/fair-value/) — The basis for marking hedging derivatives and items
- [Interest-rate swap](/interest-rate-swap/) — A common hedging instrument subject to discontinuation
- Other comprehensive income — The equity account holding accumulated OCI from hedges
- [Coupon rate](/coupon-rate/) — Fixed coupons that are hedged in fair-value hedges
- [Currency risk](/currency-risk/) — Often hedged in net-investment and cash-flow hedges
- [Interest-rate risk](/interest-rate-risk/) — The primary target of interest-rate hedges

### Wider context

- [Balance sheet](/balance-sheet/) — Where fair-value adjustments to hedged items are recorded
- [Income statement](/income-statement/) — Where derivatives are marked and hedges are offset
- [Debt financing](/debt-financing/) — The source of many fair-value hedges
- Financial reporting — The regulatory framework (IFRS 9, ASC 815) governing hedge accounting
- [Revenue recognition](/revenue-recognition/) — ASC 606 can interact with cash-flow hedges of revenue
- [Accounting standards](/asc-606/) — The standards that govern hedge accounting rules

</div>
