---
title: "Basis Risk in Currency Hedging"
description: "How basis risk in currency hedging creates residual exposure when hedges use related but non-identical currency pairs."
keywords:
  - basis risk currency hedging
  - currency hedging
  - forex basis risk
  - hedging imperfection
  - currency exposure
  - cross-rate hedging
  - residual risk
image: /svg/forex.svg
---

*A company that exports to Europe faces **basis risk in currency hedging** when it hedges EUR exposure using a correlated but not perfectly matched currency pair—perhaps CHF or another euro-linked currency instead of EUR itself. The hedge reduces but does not eliminate the true currency loss, leaving the company exposed to the gap (the "basis") between the hedging instrument and the actual underlying currency. This article explains why that gap exists, how to quantify it, and when it becomes material.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Basis Risk — key facts</div>

<img src="/svg/forex.svg" alt="An abstract editorial mark for forex mechanics." />

<div class="wiki-infobox-caption">The residual loss when your hedge doesn't perfectly match your exposure.</div>

|   |   |
|---|---|
| **Definition** | Difference between the price movement of the item you want to hedge and the price movement of the hedge instrument |
| **Common cause** | Hedging with a related (but not identical) currency pair due to illiquidity or cost |
| **Measurement** | Historical [correlation](/currency-pair-correlation-explained/) and standard deviation of the basis over time |
| **Magnitude** | Ranges from near-zero (major pairs) to 5–15% (emerging-market or cross-rate proxies) |
| **Hedging vehicle** | [Forward contracts](/forward-contract/), [futures](/futures-contract/), or [currency swaps](/swap/) |
| **When it rises** | Market stress, widening [spreads](/bid-ask-spread/), or structural divergence between the pair and its proxy |
| **Mitigation** | Use the exact currency pair as the hedge; diversify across multiple hedges; accept and budget for residual risk |

</aside>

## The Hedging Mismatch Problem

Suppose a US exporter sells goods to a Swiss customer and will receive 10 million Swiss francs (CHF) in 90 days. The exporter wants to lock in the USD value of that receivable and reduce [currency risk](/currency-risk/). The textbook solution is to sell CHF forward—that is, to enter a [forward contract](/forward-contract/) committing to exchange CHF for USD at a fixed rate in 90 days.

But what if the forward market in CHF/USD is illiquid, the bid-ask [spread](/bid-ask-spread/) is wide, or the exporter's bank charges a steep premium? The exporter might instead hedge using EUR, which is more liquid and cheaper to trade. If the exporter sells EUR forward (or buys USD/EUR futures) as a proxy for CHF exposure, the hedge is imperfect. When the settlement date arrives:

- The CHF receivable converts to USD at the *actual* CHF/USD spot rate.
- The EUR hedge settles at the *actual* EUR/USD rate.
- If those two rates moved in different directions (or by different magnitudes), the hedge protected only part of the loss.

That unprotected portion is the basis risk.

## The Basis Defined

The **basis** in currency hedging is the difference between:

**Basis = (Spot rate of actual currency on settlement date) − (Spot rate of hedging currency on settlement date)**

Adjusted for the forward rates locked in during the hedge.

More concretely: if a hedger locks in a forward rate of 1.08 USD/EUR and a forward rate of 0.95 USD/CHF, but the *actual* spot rates at settlement are 1.06 USD/EUR and 0.93 USD/CHF, the basis is the unexpected divergence between how those two pairs moved.

Suppose the exporter sold €10 million forward at 1.08 (receiving $10.8 million) as a proxy for CHF 10 million. The actual CHF/USD spot is 0.93, so the CHF receivable is worth only $9.3 million. Without any hedge, the loss would be $1.5 million. But the EUR forward locked in $10.8 million. The hedger has gained $10.8 million on the euro position but lost $1.5 million on the unhedged CHF exposure—a net gain of $300,000.

However, if CHF and EUR had moved *together* (as they often do, being European currencies), the EUR hedge would have absorbed most of the loss. The fact that CHF fell against the dollar *differently* than EUR means the hedge was imperfect.

## Why Basis Risk Matters Most for Distant Proxy Pairs

**Perfect hedge:** When an exporter hedges USD/CHF exposure using a USD/CHF forward, basis risk is zero. The underlying and the hedge instrument are identical.

**Partial proxy:** A US company with GBP exposure might hedge part of it using EUR forwards (both are advanced economies in Europe, both liquid). CHF and EUR tend to move together, but not perfectly. The [correlation](/currency-pair-correlation-explained/) between EUR/USD and CHF/USD is typically 0.80–0.95, meaning they move in similar directions but with meaningful divergence.

**Poor proxy:** A company with exposure to the Indian rupee might use the Hong Kong dollar as a proxy (both emerging markets in Asia). The correlation might be 0.50–0.70, leaving substantial basis risk. Alternatively, a smaller company might hedge a developing-market currency using a major pair (say, using EUR as a proxy for Turkish lira). The correlation could be even lower, and basis risk is severe.

## Measuring Basis Risk Quantitatively

A hedger can estimate basis risk using historical data:

1. Gather daily (or hourly) spot rates for the true currency pair and the proxy pair over a recent period (e.g., the past 2–3 years).
2. Calculate the **correlation** between percentage changes in the two pairs. A correlation near 1.0 means they move together; 0.5 means weak co-movement.
3. Calculate the **basis** as the difference in returns: (return of true pair) − (return of proxy pair).
4. Calculate the **standard deviation** of the basis. This is the volatility of basis risk.

**Example:**

Suppose EUR/USD and CHF/USD have a correlation of 0.90, meaning they move together 90% of the time. But on days when they diverge, EUR might move 0.5% while CHF moves 0.3%, leaving a 0.2% basis divergence. If historical standard deviation of the basis is 0.15% per day, a 90-day hedge might experience a cumulative basis shift of 0.15% × √90 ≈ 1.4% (by the square-root-of-time rule).

On a CHF 10 million exposure, a 1.4% basis movement means the hedge leaves you exposed to roughly 140,000 CHF of unhedged risk—a meaningful gap.

## Basis Risk and Market Stress

Basis risk typically grows during times of market stress:

- **Liquidity evaporates:** In a crisis, bid-ask [spreads](/bid-ask-spread/) widen across all pairs, but they widen *unevenly*. A major pair (EUR/USD) might widen to 5 pips, while a cross-rate (CHF/GBP) widens to 20 pips. Proxies become less reliable as their spreads balloon faster than the true currency.
- **Correlations break:** During geopolitical stress or sector-specific shocks, currencies that normally move together can decouple. A bank run in Switzerland might weaken CHF more than EUR, destroying a EUR-hedged CHF position.
- **Safe-haven flows:** If a market shock sends capital fleeing to USD and CHF (the classic safe-haven currencies), their movements might diverge sharply from EUR or GBP.

During the 2008 financial crisis or the 2020 COVID crash, basis risk widened dramatically for many emerging-market currency hedges, catching many hedgers off guard.

## When to Accept Basis Risk

Not all basis risk is avoidable. A company might tolerate basis risk when:

- **Exact hedging is too expensive:** The bid-ask spread on the true currency pair is so wide that the cost of a perfect hedge exceeds the benefit. Trading a small amount of a developing-market currency might cost 1–2% in spread and intermediary fees, making a proxy hedge preferable.
- **Liquidity is absent:** Some currencies (e.g., frontier-market FX) lack deep forward markets. A perfect hedge simply is not available, so a proxy is the only option.
- **The residual is small:** If the company's total exposure is small, or if the basis risk is expected to be minimal (high correlation, narrow spread differential), the company might decide the unhedged sliver is acceptable.
- **Partial hedging is the strategy:** Some companies hedge only 50–75% of currency exposure, accepting that a portion remains exposed. Basis risk is another layer of that accepted exposure.

## Managing and Monitoring Basis Risk

Practitioners can reduce or manage basis risk in several ways:

1. **Use the exact currency pair:** If USD/CHF forwards are available, use them. No basis risk.
2. **Diversify the hedge:** Instead of using only EUR to hedge CHF, use a portfolio of proxies (EUR, GBP, etc.). If they have different correlations, the diversified hedge may more closely track the true exposure.
3. **Layer in a [currency swap](/swap/):** A multi-legged swap can be customized to hedge the true exposure more closely than a simple forward.
4. **Monitor and rebalance:** Periodically mark the basis to market and adjust the hedge if the basis has drifted significantly.
5. **Stress test:** Run scenarios to see how the hedge performs if the two currencies decouple sharply.

## See also

<div class="wiki-seealso">

### Closely related

- [Currency pair correlation explained](/currency-pair-correlation-explained/) — How correlated pairs move together (or diverge)
- [Forward contract](/forward-contract/) — The primary tool for locking in a currency rate
- [Currency risk](/currency-risk/) — The exposure that basis risk applies to
- [Bid-ask spread](/bid-ask-spread/) — Why proxy hedges are often chosen (wider spreads on true pairs)
- [Triangular arbitrage forex](/triangular-arbitrage-forex/) — How misalignments between currency pairs are exploited

### Wider context

- [Swap](/swap/) — A more sophisticated hedging tool that can reduce basis risk
- [Derivatives hedging](/derivatives-hedging/) — Broader principles of hedging with derivatives
- [Operational risk](/operational-risk/) — Risk that hedges fail to execute as planned
- [Value-at-risk](/value-at-risk/) — Quantifying risk, including basis risk in a portfolio
- [Market risk](/market-risk/) — The broader category of risks from market price movements

</div>
