---
title: "Net Investment Hedge"
description: "Derivative strategy that hedges the translation risk on a parent company's equity stake in a foreign-currency subsidiary."
keywords:
  - net investment hedge
  - translation risk
  - foreign subsidiary
  - currency hedge
  - consolidated accounting
image: "/svg/risk.svg"
---

*A **net investment hedge** protects a parent company's equity stake in a foreign subsidiary from [currency risk](/currency-risk/). When a US firm buys a €100 million stake in a German company, it holds that investment in euros. If the euro weakens, the dollar value of the parent's equity investment shrinks, even if the subsidiary is thriving. A net investment hedge—typically a loan or [derivative](/forward-contract/) in the foreign currency—locks in the dollar value of that equity stake. It is the only [accounting hedge](/cash-flow-hedge/) where unrealised gains and losses bypass net income and sit instead in the consolidated [Other Comprehensive Income (OCI)](/interest-rate-risk/), mirroring the [translation adjustment](/currency-risk/) on the subsidiary's balance sheet itself.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Net Investment Hedge — key facts</div>

<img src="/svg/risk.svg" alt="An abstract editorial mark for financial risk and protection." />

<div class="wiki-infobox-caption">Protecting a parent company's equity value in a foreign-currency subsidiary from exchange-rate moves.</div>

|   |   |
|---|---|
| **What it is** | A foreign-currency liability (loan or derivative) that hedges the translation risk of a foreign subsidiary's net assets |
| **Typical use** | Multinational corporations with material stakes in foreign subsidiaries that report in foreign currencies |
| **Hedging instrument** | Foreign-currency loans, [forward contracts](/forward-contract/), [currency swaps](/interest-rate/), [put options](/put-option/) on foreign currency |
| **Scope** | Can hedge the entire net-asset value of a foreign subsidiary, or only a portion of it |
| **Accounting treatment** | Hedge gains/losses and subsidiary translation adjustments both flow to [OCI](/interest-rate-risk/); only realised amounts hit net income |
| **Effectiveness required** | 80–125% hedge effectiveness; ineffective portions may flow to net income |
| **Time horizon** | As long as the subsidiary is owned; hedge can be rolled or adjusted |

</aside>

## Why translation risk matters to parent companies

A US company acquires 100% of a German subsidiary for $100 million, funded by a $100 million equity investment. The subsidiary's net assets (assets minus liabilities) are €100 million, and the exchange rate is 1.00 USD/EUR. Fast forward two years: the subsidiary is profitable, its net assets have grown to €120 million, but the euro has weakened to 0.83 USD/EUR. In dollar terms:
- Subsidiary net assets: €120M × 0.83 = $99.6 million (down from $120M if the rate had held).
- The parent's consolidated equity stake has fallen $20.4M even though the subsidiary is stronger.

This is [translation risk](/currency-risk/)—the equity value of the parent's investment changes because of exchange-rate moves, not because the subsidiary performed poorly. Unlike [cash flow risk](/cash-flow-hedge/) (where the subsidiary's actual cash earnings are affected by rates), translation risk is a balance-sheet accounting effect. The subsidiary's profits may be unaffected; only the parent's consolidated financial statements suffer.

For small foreign stakes, translation risk is noise. But for multinational firms with large subsidiaries or many foreign operations, translation swings can dwarf earnings volatility. A net investment hedge lets the parent lock in the dollar value of its equity stake.

## The structure: borrowing or deriving in foreign currency

The most common net investment hedge is a **foreign-currency loan** made by the parent. The US parent borrows €100 million from a bank at a fixed euro rate. This loan is a liability in euros; it must be repaid in euros. Every quarter, when the subsidiary's assets are consolidated, the parent's euro liabilities are also revalued:
- If the euro weakens from 1.00 to 0.83, the subsidiary's equity (in dollars) falls by $20.4M.
- But the parent's euro-denominated loan liability also falls (fewer dollars needed to repay), creating a *gain* of $20.4M in the parent's accounting.
- Both effects flow to [OCI](/interest-rate-risk/) (consolidated translation adjustments); they offset, leaving net income unaffected.

The parent has effectively hedged the translation exposure by creating an equal-sized currency liability. It is simple, effective, and widely used.

**Derivative hedges** are also common. The parent might enter a [forward contract](/forward-contract/) to sell euros at a locked rate, or a [currency swap](/interest-rate/) where the parent pays euros and receives dollars. These achieve the same end: a euro-denominated exposure that offsets the euro translation risk on the subsidiary.

## Accounting: the OCI offset

This is where net investment hedges differ from [cash flow](/cash-flow-hedge/) and [fair value](/fair-value-hedge/) hedges. Under [GAAP](/generally-accepted-accounting-principles/) and [IFRS](/international-financial-reporting-standards/):

When a foreign subsidiary's assets and liabilities are consolidated, the change in their dollar value due to exchange-rate moves is recorded as a **translation adjustment** in [OCI](/interest-rate-risk/). If the euro weakens, the subsidiary's equity (in dollars) falls, and a negative adjustment lands in OCI.

Simultaneously, if the parent has a euro-denominated loan or derivative, its value (in dollars) changes in the opposite direction. That gain also lands in OCI.

If the two are perfectly correlated (as they should be if the hedge is effective), they offset in OCI, leaving net income unchanged. This is elegant: the parent's earnings are not distorted by translation noise, and the balance sheet reflects a stable equity stake despite currency moves.

Contrast this with a [fair value](/fair-value-hedge/) or [cash flow](/cash-flow-hedge/) hedge, where ineffectiveness flows to net income and can cause earnings volatility.

## Real-world example: the US pharmaceutical company

A US pharmaceutical firm owns a Swiss subsidiary (acquired for $500M in equity) that manufactures and sells drugs across Europe. The subsidiary's balance sheet is in Swiss francs (CHF). Over the past year:
- Subsidiary's net assets (assets minus liabilities) grew from CHF 500M to CHF 520M (4% growth, good news).
- The CHF exchange rate moved from 1.10 USD/CHF to 0.95 USD/CHF (franc weakened 14%).
- Dollar value of the subsidiary's net assets: was $550M (500M × 1.10), now $494M (520M × 0.95).

In consolidated financials without a hedge:
- Equity value fell from $550M to $494M (−$56M), mostly due to currency.
- Earnings grew (subsidiary was profitable), but the balance sheet suffered.
- Shareholders see: net income up, equity down—confusing.

Now assume the parent company hedged by borrowing CHF 500M at the time of acquisition:
- Parent has a CHF 500M liability, revalued each quarter.
- When the franc weakens, the dollar amount of the liability falls: from $550M (500M × 1.10) to $475M (500M × 0.95).
- The CHF loan now "costs" $75M less to repay, a gain of $75M.
- The subsidiary's equity in dollars fell $56M (translation loss).
- Net effect in OCI: $75M gain (on the CHF liability) − $56M loss (on the subsidiary) = $19M net gain.
- Actually, the math is slightly different because the subsidiary grew from CHF 500M to CHF 520M, and the hedge only covers CHF 500M. The unhedged CHF 20M growth has translation risk.

The result: the parent's consolidated balance sheet shows a more stable equity position because the currency exposure is intentionally matched on both the asset side (foreign subsidiary) and the liability side (foreign-currency loan).

## When to hedge net investments

Net investment hedges are most valuable when:
- The subsidiary is large relative to total equity (material exposure).
- The foreign currency is volatile or expected to depreciate.
- The parent's regulators or accounting environment penalise large translation swings.
- The subsidiary is permanent (a long-term holding, not a short-term investment).

A multinational with dozens of small foreign distributors might not hedge each one individually; the net translation effect is small. But a firm that has made a major acquisition overseas—a US tech giant opening a €5 billion R&D centre in Germany—will almost always hedge to stabilize consolidated equity.

Central banks and sovereign wealth funds also use net investment hedges to protect foreign-currency reserves and foreign direct investments.

## The cost and limit

A net investment hedge is not free. The parent must borrow in foreign currency (at some cost and possibly at a premium) or pay [option premiums](/option-premium/) on [puts](/put-option/). The benefit is reduced balance-sheet volatility and clearer earnings. Whether the trade-off is worth it depends on the size of the exposure and the parent's appetite for translation swings.

Also, a net investment hedge protects *equity value*, not cash flows. If the subsidiary's actual earnings (in foreign currency) decline, the hedge does not help. The hedge only insulates the parent from the accounting effects of currency moves on a stable or growing underlying business.

## See also

<div class="wiki-seealso">

### Closely related

- [Cash Flow Hedge](/cash-flow-hedge/) — hedging uncertain future cash flows; contrast with net investment hedges on existing equity
- [Fair Value Hedge](/fair-value-hedge/) — hedging the market value of recognised assets or liabilities
- [Macro Hedging](/macro-hedging/) — portfolio-level currency protection versus single-subsidiary hedges
- [Currency Risk](/currency-risk/) — the translation and transaction exposure that net investment hedges address
- [Foreign Exchange Forward](/forward-contract/) — a derivative often used in net investment hedges
- [Currency Swap](/interest-rate/) — another hedging instrument for foreign-currency liabilities
- [Other Comprehensive Income (OCI)](/interest-rate-risk/) — accounting category where translation adjustments and hedge gains/losses sit

### Wider context

- [Generally Accepted Accounting Principles (GAAP)](/generally-accepted-accounting-principles/) — US standard defining net investment hedge accounting rules
- [International Financial Reporting Standards (IFRS)](/international-financial-reporting-standards/) — global standard with similar framework
- Consolidated Financial Statements — how parent and subsidiary results are merged for reporting
- [Translation Adjustment](/currency-risk/) — the balance-sheet effect of exchange-rate moves on foreign-subsidiary assets
- [Counterparty Risk](/counterparty-risk/) — risk that a bank providing a currency derivative defaults

</div>
