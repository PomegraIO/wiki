---
title: "Trade Compression"
description: "Automated netting mechanism that terminates offsetting OTC derivative contracts to reduce gross notional outstanding without changing net economic risk."
keywords:
  - trade compression
  - derivatives netting
  - bilateral netting
  - portfolio compression
  - notional reduction
image: "/svg/institutions.svg"
---

*Trade **compression** is the systematic termination and replacement of offsetting over-the-counter derivative positions to shrink the total notional amount outstanding between two counterparties without altering their net economic exposure. A bank that has bought 100 million euros of a five-year interest rate swap and sold 95 million euros of the same swap to the same counterparty carries 195 million in gross notional; compression would replace these with a single 5 million contract, reducing operational complexity and collateral requirements while preserving the net risk.*

<div class="wiki-hatnote">

For the clearing infrastructure compression sits atop, see Clearinghouses. For the broader OTC derivatives ecosystem, see [Over-the-counter market](/over-the-counter-market/).

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Trade Compression — key facts</div>

<img src="/svg/institutions.svg" alt="An abstract editorial mark for financial institutions and regulatory frameworks." />

<div class="wiki-infobox-caption">Netting that shrinks the notional value outstanding without changing net risk or cash flows.</div>

|   |   |
|---|---|
| **What it is** | Termination of offsetting swaps; replacement with a net position |
| **Scope** | Typically applied to interest rate swaps, credit default swaps, foreign exchange derivatives |
| **Mechanics** | Mutual agreement + auction-like matching engine to find compression chains |
| **Benefit** | Reduces collateral, operational cost, settlement complexity, system footprint |
| **Coverage** | Can reduce gross notional by 5–15% per compression session |
| **Frequency** | Typically quarterly or semi-annually; continuous in some platforms |
| **Service provider** | Specialist vendors (e.g., TriResolve, Enavate) and some clearinghouses |

</aside>

## Why compression matters

The OTC derivatives market, despite [clearing mandate](/clearing-mandate-emir-dodd-frank/) adoption, still carries a massive gross notional outstanding—measured in quadrillions of dollars. Much of this notional is redundant. A bank might have hundreds of swap positions with dozens of counterparties, many of them economically opposing each other. The bank's net interest rate risk from all these positions might be a few million dollars, yet the bank must manage, collateralise, and monitor each individual contract.

This duplication creates friction across the financial system. The bank must post initial margin on every contract, even if net risk is tiny. Operational teams must confirm, settle, reconcile, and report every single trade separately. A failure in one offsetting leg creates unexpected exposure in the other. Regulators see a bloated gross notional that masks the true systemic footprint.

Compression compresses this bloat. By identifying positions that net to zero or near-zero, and mutually agreeing to terminate them, two counterparties can shrink their bilateral exposure, cut collateral, and simplify operations—all while keeping their aggregate risk profile unchanged.

## How compression works

**Bilateral compression** is the simplest form. Two counterparties sit down (or their operations teams do, with increasing automation) and review every trade between them. If Bank A owes Bank B a 10 million notional swap and Bank B owes Bank A a 10 million notional swap with the same underlying terms and maturity, both agree to tear up both contracts. The net effect is zero, and both parties' balance sheets shrink by 20 million notional. Cash settlement—if the market value of the two contracts differs—is handled separately.

**Multilateral compression** is more powerful but operationally complex. A group of three or more banks identify a "compression chain": a cycle of offsetting exposures where Bank A has a position vs. Bank B, Bank B has an opposing position vs. Bank C, and Bank C has an opposing position vs. Bank A. By terminating all three trades and settling the net cash flows, all three banks reduce their total notional outstanding without changing their net exposure to any counterparty.

Matching such chains requires a specialised engine. Vendors like TriResolve run platforms where banks upload their derivative portfolios and let algorithms identify potential compressions. The vendor runs an auction-like process to find all possible compression chains, then invites banks to accept terminations. Once agreed, the vendor handles all the legal paperwork, calculation of cash settlement amounts, and coordination of the actual termination.

## The economic incentive

Banks have a strong incentive to compress. Each contract requires:

- **Collateral:** Initial and variation margin, as mandated by clearing rules. Compression reduces this drag directly.
- **Operational labour:** Confirmation, reconciliation, month-end reporting, regulatory reporting. Compression shrinks the headcount needed.
- **System footprint:** Derivative processing platforms, valuation systems, and risk engines. Compression reduces system load and IT infrastructure cost.
- **Capital:** Under regulations like Basel III and FRTB (Fundamental Review of the Trading Book), some derivative positions carry capital charges. Fewer contracts = lower capital requirement.

A single compression cycle can reduce gross notional outstanding by 5–15%, depending on the set of banks participating and the overlap of their portfolios. Large banks undertake multilateral compressions quarterly. Some platforms now offer continuous compression, where new trades are immediately checked against existing positions and opposite flows are netted intraday.

## Systemic implications

From a regulatory and systemic risk perspective, compression is beneficial but incomplete. Regulators pushed for compression partly to curb the gross notional outstanding, which had become a political lightning rod post-2008 (the industry argued that notional was a misleading risk metric; critics countered that it signaled the scale of interconnection). Compression has become almost reflexive—banks that do not regularly compress face peer pressure and investor questions.

However, compression does not eliminate risk; it merely hides it. Two banks with offsetting swaps do carry net-zero risk between them, but each still owes collateral to a clearinghouse, and if one bank fails, the remaining banks in the cycle face complexity and settlement uncertainty. Compression also tempts banks to think of notional reduction as an end in itself, sometimes masking that they are taking on concentrated risk in a smaller set of remaining positions.

Compression also does not prevent future duplication. A compression cycle today may become obsolete in six months as banks execute new trades and create new offsetting positions. This is why continuous or high-frequency compression—offered by some platforms—attempts to prevent the duplication from ever occurring.

## Challenges and barriers

**Operational burden:** Setting up compression requires standardisation of data. If Bank A and Bank B use incompatible systems or different conventions for recording swap terms (day-count rules, holiday calendars, notional rounding), matching positions becomes difficult.

**Credit exposure:** During the compression process itself, there is a window where deals have been verbally agreed but not yet legally terminated. If a counterparty defaults or changes its mind during this window, complications arise. Vendors now use escrow-like mechanisms to mitigate this.

**Regulatory constraints:** Some banks cannot compress because of regulatory or accounting rules. A bank holding a derivative for a specific regulatory purpose may not be able to terminate it simply to reduce notional.

**Cost and infrastructure:** Multilateral compression is effective only at scale. A small regional bank might find compression uneconomical; an institution must process sufficient notional to justify the vendor fee and internal coordination cost.

## Compression and clearing mandates

The [clearing mandate](/clearing-mandate-emir-dodd-frank/) and compression are complementary but separate tools. Clearing concentrates risk at a clearinghouse and reduces bilateral counterparty risk. Compression reduces gross notional outstanding and operational burden. A cleared derivative can still be compressed. In fact, compressed trades are typically re-cleared after compression, creating a fresh set of contracts between the clearing member and the CCP with reduced notional.

Some regulators have suggested that compression should happen automatically before clearing—the idea being that the CCP should not have to carry a bloated notional base filled with economic offsets. A few initiatives, like "post-trade compression" mandates in some EU rules, are moving in this direction.

## See also

<div class="wiki-seealso">

### Closely related

- Clearinghouses — institutions that benefit from smaller cleared notional
- [Clearing mandate](/clearing-mandate-emir-dodd-frank/) — regulation that drives compression alongside clearing
- [Straight-through processing](/straight-through-processing/) — automation that makes compression easier
- [Failed settlement](/failed-settlement/) — operational risk compression helps mitigate
- [Over-the-counter market](/over-the-counter-market/) — the bilateral derivatives market compression operates on

### Wider context

- [Counterparty risk](/counterparty-risk/) — the interconnection compression reduces
- [Systemic risk](/systemic-risk/) — the gross notional that compression aims to contain
- [Dodd-Frank Act](/dodd-frank-act/) — regulation emphasising compression post-2008
- [Interest rate swap](/interest-rate-swap/) — the most commonly compressed derivative product

</div>
