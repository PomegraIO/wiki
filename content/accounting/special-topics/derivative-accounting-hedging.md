---
title: "Derivative Accounting (Hedging)"
description: "Mark-to-market and hedge accounting treatment of derivatives, with special rules for hedge relationships."
keywords:
  - hedge accounting
  - mark-to-market
  - ast 815
  - effective portion
  - ineffective portion
  - cash flow hedge
---

*The **derivative accounting** treatment under **hedge accounting** allows firms to defer recognizing gains and losses on hedging instruments if the hedge effectively reduces a specific risk. Without this exception, derivatives would be marked to market every quarter with swings that disguise the underlying economic offset.*

<aside class="wiki-infobox">

| Attribute | Value |
|-----------|-------|
| **Standard** | ASC 815 (U.S. GAAP) |
| **Two hedge types** | Fair value hedge, Cash flow hedge |
| **Mark-to-market** | Full, unless formally designated |
| **Effectiveness test** | Typically 80–125% range |
| **Retest frequency** | Every rebalancing (monthly, quarterly) |
| **Ineffective portion** | Flows through income immediately |
| **Deferred gains/losses** | Reclassified when hedged item matures |

</aside>

## The mark-to-market problem

A company that buys a [currency forward](/fx-forward/) to lock in the cost of imports for next quarter faces a dilemma. The forward is a [derivative](/derivative-accounting-hedging/), and under strict U.S. GAAP rules, it must be valued at fair value at each quarter-end. If the dollar weakens, the forward gains value; if it strengthens, the forward loses value.

Without hedge accounting relief, a firm would swing the derivative's mark-to-market gain or loss into earnings, creating volatility that bears no relation to actual cash outflows. The company's foreign subsidiary might be operating normally and generating steady revenue, but the parent's consolidated earnings would jump $5 million one quarter and drop $3 million the next, purely from derivatives moves.

## How hedge accounting defers the volatility

**Hedge accounting** allows a firm to formally designate a derivative as a hedge of a specific asset, liability, or cash flow. If the hedge qualifies, gains and losses on the derivative are deferred into other comprehensive income (OCI), not run through net income immediately. This synchronizes the derivative's accounting with the underlying risk being hedged.

The firm must:
1. Document the hedge relationship *before* or *at inception* of the derivative.
2. Identify the specific risk being hedged (e.g., interest rate risk on a bond, foreign exchange risk on a forecast transaction).
3. Test the hedge's **effectiveness**—the derivative's price moves must offset at least 80% of the underlying risk's moves.

If the hedge qualifies, the accounting treatment depends on the type.

## Fair value hedge

In a **fair value hedge**, the company is hedging a recognized asset or liability. Example: a firm holds a fixed-rate bond and wants to hedge its [interest rate risk](/interest-rate-risk/). It enters a [pay-floating, receive-fixed interest rate swap](/interest-rate-swap/).

Under fair value hedge accounting:
- The derivative is marked to market each period.
- The hedged item is *also* marked to market for the specific risk being hedged (e.g., the bond's fair value is adjusted for changes in interest rates, not held at amortized cost).
- Gains on the derivative are offset by losses on the hedged item in earnings, net of any **ineffective portion**.

Because both are flowing through income, the net volatility is minimal if the hedge is effective. The derivative gain and the bond's fair-value loss roughly cancel, leaving only the ineffective portion (the portion of the derivative's move not offset by the underlying).

## Cash flow hedge

In a **cash flow hedge**, the company is hedging the variability of *future* cash flows from an unrecognized transaction. Example: a U.S. manufacturer forecasts a sale of goods to Europe three months from now and wants to hedge the foreign exchange risk.

The derivative is marked to market, but the gain or loss is deferred in other comprehensive income (OCI), a balance sheet holding area. When the forecasted transaction finally occurs (the sale is completed and the euro is converted to dollars), the deferred gain or loss is reclassified out of OCI and into earnings, where it offsets the actual transaction gain or loss.

The key difference: cash flow hedges decouple the derivative's accounting from the underlying transaction until that transaction occurs, preventing false earnings volatility in the interim.

## Effectiveness testing and ineffectiveness

To qualify for hedge accounting, the hedge must be **effective**—meaning at least 80% of the change in the derivative's fair value is offset by the change in the hedged item's fair value (or, for cash flow hedges, the forecasted transaction's value).

If a derivative qualifies but is only 90% effective, the 10% ineffective portion flows through earnings immediately. This keeps the company honest: if the hedge is slipping out of alignment, the ineffectiveness is visible in the P&L.

Firms must retest effectiveness, typically monthly or quarterly. If a hedge falls below 80% effectiveness, the firm must dedesignate it and mark-to-market the entire remaining derivative balance, reverting to the basic (volatile) accounting.

## Cross-currency swaps and natural hedges

Multinational firms often use [cross-currency swaps](/cross-currency-swap/) to manage long-term foreign exchange exposure on assets held overseas. A company with a subsidiary in Japan funded by yen debt will enter a swap to convert the yen interest and principal flows into dollars.

These swaps are nearly always effective hedges and often qualify for fair value or cash flow hedge treatment, smoothing the accounting and matching the economic offset.

## The controversy: asymmetry and complexity

Critics of hedge accounting note that it creates asymmetry. A derivative that qualifies for hedge accounting has smooth accounting; one that does not qualify shows wild volatility. Similarly, a $100 million [interest rate swap](/interest-rate-swap/) in a bank's trading book is marked to market with no deferral, while the same swap in a corporate treasury used to hedge debt gets special treatment.

The complexity also breeds errors. Firms must document hedges rigorously, retest quarterly, and reclassify OCI amounts at the right moment. A small mistake in documentation can invalidate hedge accounting retroactively, forcing a restatement.

Nevertheless, hedge accounting is essential for any company that actually uses derivatives to manage real business risks. Without it, earnings would be dominated by mark-to-market swings unrelated to operational performance.

---

<div class="wiki-seealso">

### Closely related

- [Interest Rate Swap](/interest-rate-swap/) — Common hedging instrument
- [Cross Currency Swap](/cross-currency-swap/) — Multinational hedging tool
- [Mark to Market](/mark-to-market/) — Fair value accounting treatment
- [Currency Hedging](/currency-hedging/) — Foreign exchange risk management
- [Fair Value](/fair-value/) — Fundamental accounting concept

### Wider context

- [ASC 606](/asc-606/) — Revenue recognition standard
- [Derivative Clearing Requirements](/derivative-clearing-requirements/) — Regulatory requirement for exchange-traded derivatives
- [Counterparty Risk](/counterparty-risk/) — Exposure when swap counterparty fails
- [Comprehensive Income](/comprehensive-income/) — OCI and earnings components
- [Interest Rate Risk](/interest-rate-risk/) — Primary hedge driver

</div>
