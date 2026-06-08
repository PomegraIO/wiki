---
title: "Cross-Margining Between Clearinghouses: How Offsets Reduce Collateral"
description: "Cross-margining between clearinghouses allows firms to offset positions across multiple CCPs, reducing total collateral required and freeing up capital."
keywords:
  - cross-margining between clearinghouses
  - central counterparty
  - collateral offset
  - derivatives clearing
  - margin efficiency
  - ccp arrangement
---

*When a firm holds offsetting positions at different clearinghouses—say, a long equity futures contract at one CCP and a short at another—**cross-margining between clearinghouses** lets the firm post less total collateral by recognizing the hedge across venues. Instead of holding margin against each position in isolation, the firm gets credit for the offset, freeing trapped capital.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Cross-Margining — key facts</div>

<img src="/svg/institutions.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Offsetting positions held at different CCPs can be netted together under bilateral cross-margining agreements.</div>

|   |   |
|---|---|
| **Definition** | Recognition of hedges across multiple clearinghouses to reduce collateral posted in total |
| **Who benefits** | Broker-dealers, asset managers, and clearing members spanning multiple venues |
| **Primary driver** | Leverage constraint and capital efficiency in derivatives markets |
| **Mechanics** | Bilateral agreements between two CCPs, or umbrella frameworks (e.g., CSDX) |
| **Collateral freed** | 10–40% of margin, depending on correlation and hedge tightness |
| **Risk mitigation** | Requires pre-agreed protocols for default and forced liquidation |

</aside>

## The collateral trap without cross-margining

In a fragmented derivatives market, clearing members might execute strategies that naturally hedge each other—perhaps selling equity index futures at one venue while buying interest-rate swaps at another, or buying currency forwards at one CCP while selling at a rival. In isolation, each position looks like it requires margin collateral. But from the firm's economic perspective, the positions offset.

Without cross-margining, the firm must post margin against the full notional of both legs. A broker-dealer managing a $100 million hedge might face $15 million in total margin requirements across two clearinghouses, even though the economic risk is nearly neutral. That capital sits dormant, unable to deploy elsewhere, eroding returns on equity and limiting the size of the firm's operations.

This inefficiency emerged as a real problem after the 2008 financial crisis, when regulators mandated central clearing for standardized derivatives. Overnight, firms that once could net exposures bilaterally with counterparties now had to post collateral separately at each CCP. Capital constraints tightened. Clearing members began lobbying for a way to recognize cross-venue hedges.

## How cross-margining arrangements work

Cross-margining is a bilateral agreement between two central counterparties that allows them to recognize offsetting positions in their respective portfolios. When a firm is a clearing member at both venues, it can request that its positions be evaluated jointly rather than separately.

**The mechanics are straightforward:**

1. The firm notifies both CCPs of the offsetting relationship (or automates it via API).
2. Each CCP calculates the firm's margin requirement under its own haircuts and models (e.g., [value-at-risk](/value-at-risk/) or [sensitivity analysis](/sensitivity-analysis-valuation/)).
3. The CCPs then apply a joint stress test: they ask what collateral would be needed if both firms defaulted and both portfolios were liquidated simultaneously.
4. The result is typically 20–40% lower margin than the sum of standalone requirements.

The savings depend on the tightness of the hedge and the correlation of the underlying assets. A perfect hedge (long and short on identical contracts) yields close to a 100% offset. Imperfect hedges—e.g., S&P 500 futures hedged with Russell 2000 futures—yield smaller offsets proportional to their correlation.

## Frameworks and governance

Most cross-margining occurs through **bilateral agreements** between a pair of CCPs. These are negotiated individually and tend to be tighter and more restrictive. For example, CME and ICE Futures have allowed some limited cross-margining on FX and energy contracts, but with strict rules on which products qualify.

Broader frameworks have emerged. The **Cooperative Global Derivatives System (CSDX)** in Asia attempted a more systematic umbrella approach, letting members at participating Asian CCPs net positions in real time. However, such multilateral schemes have proven difficult to scale, because each CCP has its own risk models, default procedures, and collateral haircuts, and aligning them is technically and politically complex.

In Europe, the European Securities and Markets Authority (ESMA) has endorsed cross-margining as a capital-efficiency tool but requires detailed governance protocols, including stress-testing standards and default waterfall arrangements.

## Risk and the default waterfall

Cross-margining only works if all parties trust the mechanism in a crisis. The chief risk is **operational synchronization**: if one CCP fails or is breached before the cross-margin calculation is complete, the other CCP might be holding insufficient collateral against the firm's unilateral exposure.

To manage this, cross-margining agreements must specify a **default waterfall**:

- What happens if one CCP loses access to a firm's collateral?
- Which CCP has priority in liquidating the hedge?
- How are unsecured losses allocated?

These rules are negotiated upfront and stored in legal agreements. In practice, they have rarely been tested in real defaults, so some uncertainty persists.

Another risk is **basis risk**: the offset may be less perfect than assumed if market conditions move in unexpected ways. For instance, if equity volatility spikes and interest-rate volatility compresses, a long equity / short rate swap may no longer be a tight hedge. Margin will increase. The CCP must recalculate regularly and call for additional collateral if the offset degrades.

## Market adoption and limits

Cross-margining remains a niche practice, used primarily by the largest broker-dealers and hedge funds that:

- Span multiple CCPs (already common in interest-rate, FX, and equity derivatives).
- Have sufficient operational sophistication to maintain the agreements.
- Face acute capital constraints.

Smaller firms often find the negotiation and compliance cost prohibitive. Each bilateral agreement typically requires legal review, systems integration, and ongoing governance. A startup hedge fund would rarely justify the effort.

Adoption has been slower than some hoped because regulatory divergence persists. US CCPs operate under different collateral and default rules than European or Asian peers, complicating umbrella frameworks. Some regulators worry that cross-margining could mask true leverage if not monitored carefully.

That said, post-2008 interest in capital efficiency has kept the concept alive. As derivatives markets consolidate and fewer CCPs dominate each asset class, the pressure for cross-margining may grow.

## See also

<div class="wiki-seealso">

### Closely related

- Central counterparty — intermediary that novates trades and manages default risk
- [Collateral](/margin-call-forex/) — assets posted to secure derivative positions
- [Margin call](/margin-call-forex/) — demand for additional collateral when position value falls
- [Derivatives hedging](/derivatives-hedging/) — using derivatives to offset portfolio risk
- [Counterparty risk](/counterparty-risk/) — the risk that the other party to a trade defaults
- [Leverage ratio](/leverage-ratio-forex/) — measure of debt relative to capital, affected by collateral efficiency
- [Liquidity risk](/liquidity-risk/) — risk that assets cannot be quickly converted to cash

### Wider context

- [Stock market](/stock-market/) — primary venue for cash equities; some equity derivatives are cleared
- [Interest rate](/interest-rate/) — key driver of interest-rate derivative prices
- [Currency volatility](/currency-volatility/) — affects margin requirements in FX derivatives

</div>
