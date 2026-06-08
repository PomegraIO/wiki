---
title: "Bilateral vs Central Clearing: Cost Comparison"
description: "Bilateral clearing creates higher capital and margin costs than central counterparty clearing; dealers choose based on trade size, counterparty credit, and regulatory rules."
keywords:
  - bilateral clearing costs
  - central clearing
  - ccp clearing
  - derivatives clearing
  - counterparty risk
  - margin requirements
---

*In derivatives markets, a dealer can clear a trade **bilaterally** (posting margin directly to the [counterparty](/counterparty-risk/)) or through a **central counterparty (CCP)** (routing through an exchange-like clearinghouse). Bilateral clearing imposes higher margin, capital charges, and operational costs on the dealer; central clearing concentrates these costs at the CCP but spreads them across participants. The choice between the two is shaped by trade size, regulatory incentives, and credit relationships.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Bilateral vs Central Clearing — cost drivers</div>

<img src="/svg/trading.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Two paths for derivatives settlement; each carries distinct dealer costs.</div>

|   |   |
|---|---|
| **Bilateral margin** | Full variation margin + initial margin to counterparty |
| **CCP margin** | Shared pool; lower individual dealer requirement |
| **Capital charges** | ~2–10% of notional for bilateral; ~0.4–2% for CCP |
| **Operational burden** | High for bilateral (bilateral negotiation); low for CCP |
| **Counterparty credit** | Must be strong for bilateral; immaterial for CCP trades |
| **Regulatory incentive** | Dodd-Frank favors CCP for standardized derivatives |

</aside>

## Bilateral clearing: Direct counterparty settlement

In **bilateral clearing**, two dealers or a dealer and a client exchange derivative cash flows and post collateral directly to each other. There is no intermediary. If a dealer enters a 5-year interest rate swap with a corporate treasurer, the dealer must post variation margin (daily P&L adjustments) and initial margin (cushion against default) to the treasurer's account.

The dealer's cost structure is straightforward but heavy:

- **Variation margin**: The dealer must fund daily variation daily. On a large trade, a 100-basis-point market move can force the dealer to post millions in margin overnight. This ties up capital and incurs borrowing costs.
- **Initial margin**: The dealer must set aside capital upfront as a buffer. A 5-year interest rate swap might require 2–5% of notional as initial margin—on a $100 million swap, that is $2–5 million locked up.
- **Capital charge**: Under [Basel III](/capital-adequacy/) rules, bilateral derivatives attract a "counterparty credit risk" charge. The dealer must hold equity capital equal to 2–10% of the trade's potential future exposure, depending on the counterparty's credit rating and the trade's [duration](/duration/).

A dealer with a BBB-rated corporate counterparty carries more capital burden than a dealer with a AAA-rated bank counterparty. This asymmetry creates a direct price incentive: the dealer charges the weaker counterparty a wider spread to compensate for higher capital cost.

## Central clearing: Pooled risk through a CCP

In **central clearing**, the dealer routes the trade to a clearinghouse (e.g., the CME, ICE, or EUREX). The CCP becomes the buyer to the seller and the seller to the buyer—it interposes itself as the central counterparty and guarantees both sides will settle.

The dealer's cost structure shifts:

- **Variation margin**: The dealer posts variation margin to the CCP, not the counterparty. The CCP pools risk across all members and can offset long and short positions, reducing the total capital it must hold.
- **Initial margin**: The dealer posts initial margin to the CCP's margin pool. Because the CCP nets risk across members, its margin requirement for each member is typically 30–60% lower than bilateral margin for an equivalent trade.
- **Capital charge**: Under [Basel III](/capital-adequacy/), a trade cleared through a qualifying CCP incurs a much lower capital charge—typically 2–4% of the bilateral charge. A dealer might hold 0.4% equity capital for a CCP-cleared swap versus 4–10% for a bilateral equivalent.
- **CCP membership or clearing fee**: The dealer pays a clearing fee (typically a few basis points) and may maintain membership capital. These are small relative to the margin and capital savings.

## Worked cost comparison

Consider a $100 million 5-year interest rate swap between a dealer and a corporate client (BBB-rated):

**Bilateral clearing:**
- Initial margin posted: 3% × $100M = $3 million
- Annual margin funding cost (at 4% rate): $120,000
- Capital charge: 6% × $100M = $6 million
- Annual capital cost (at 10% ROE): $600,000
- Annual cost: ~$720,000

**CCP clearing (same $100M swap):**
- Initial margin posted: 1.5% × $100M = $1.5 million
- Annual margin funding cost (at 4%): $60,000
- Capital charge: 0.8% × $100M = $800,000
- Annual capital cost (at 10% ROE): $80,000
- CCP clearing fee: 0.005% × $100M = $5,000
- Annual cost: ~$145,000

The dealer saves ~$575,000 per year by clearing through a CCP. On large books of derivatives, this compounds into tens of millions in annual savings for major dealers.

## Who bears the cost?

The client does not see these costs directly, but feels them in pricing. A dealer that faces lower capital charges on CCP-cleared trades will quote tighter spreads for CCP-eligible products. A dealer that must absorb heavy bilateral capital charges will widen spreads or decline bilateral trades altogether.

In practice, dealers actively route standardized derivatives (e.g., plain-vanilla swaps, futures) to CCPs, where margin and capital are cheapest. Non-standard, bespoke derivatives—which CCPs cannot handle—remain bilateral, and clients pay wider spreads to compensate the dealer for elevated capital costs.

## Regulatory drivers of central clearing

The [Dodd-Frank Act](/dodd-frank-act/) (2010) and equivalent global rules mandate that standardized derivatives be cleared through a registered CCP. The intent was to reduce systemic risk by concentrating counterparty exposure and netting across the market. A happy side effect for dealers is the dramatic reduction in capital costs.

This regulatory push explains why the industry moved sharply toward CCP clearing in the 2010s. It was not purely voluntary; it was economically efficient *and* legally required. Non-CCP-clearable derivatives (e.g., exotic options, long-dated bespoke swaps) remain bilateral, and dealers price these products to recover the higher capital burden.

## Trade size and the bilateral-CCP boundary

Bilateral clearing is economically rational for very large, unique trades where:
- The counterparty has strong credit (AA or AAA), minimizing capital charge.
- The trade is non-standard (e.g., a structured option or long-dated forward) that CCPs do not offer.
- The notional is so large that CCP margin pools cannot accommodate it without stress.

For a $500 million exotic structured swap with a multinational corporation, a dealer may accept bilateral clearing because the CCP route is unavailable or prohibitively expensive. For a $10 million plain-vanilla swap with a hedge fund, the dealer routes to a CCP to cut costs.

## Operational burden

Beyond margin and capital, bilateral clearing carries operational friction. The dealer and counterparty must negotiate bilateral credit agreements, agree on collateral types and haircuts, and manage daily margin reconciliation. A dealer might have 200 bilateral counterparties, each with different agreements. CCP clearing standardizes these processes, reducing back-office headcount and risk.

## See also

<div class="wiki-seealso">

### Closely related

- [Counterparty risk](/counterparty-risk/) — default risk in bilateral trades
- [Repurchase agreement](/repurchase-agreement/) — another collateralized instrument subject to similar capital rules
- [Capital adequacy](/capital-adequacy/) — how regulators mandate equity reserves
- [Swap](/swap/) — the canonical derivative cleared through both bilateral and CCP channels

### Wider context

- [Dodd-Frank Act](/dodd-frank-act/) — regulatory push toward CCP clearing
- [Derivatives hedging](/derivatives-hedging/) — how companies use swaps and forwards
- [Risk-weighted assets](/risk-weighted-assets/) — the denominator in capital ratio calculations
- [Operational risk](/operational-risk/) — costs of managing bilateral agreements

</div>
