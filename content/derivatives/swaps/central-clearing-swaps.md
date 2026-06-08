---
title: "Central Clearing of Swaps"
description: "The post-2008 regulatory framework requiring standardised OTC swaps to be novated to a central counterparty clearinghouse."
keywords:
  - central clearing
  - swap clearing
  - central counterparty
  - Dodd-Frank
  - OTC derivatives
  - systemic risk
image: "/svg/derivatives.svg"
---

*Central clearing of swaps is a post-crisis regulatory mandate requiring standardised [interest-rate swaps](/interest-rate-swap/) and other derivatives to be executed through a central counterparty (CCP) rather than bilaterally between two banks. The CCP interposes itself as buyer to every seller and seller to every buyer, absorbing [counterparty risk](/counterparty-risk/) and enforcing daily margin settlement, making the market safer but more expensive.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Central Clearing of Swaps — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives and structured products." />

<div class="wiki-infobox-caption">A regulatory fix to reduce systemic risk in the $600+ trillion derivatives market.</div>

|   |   |
|---|---|
| **What it is** | Mandate to route standardised swaps through a clearinghouse instead of bilaterally |
| **Trigger** | Dodd-Frank Act (2010) and international regulatory convergence |
| **Key actors** | Central counterparties, clearing members, swap dealers, regulators |
| **Primary swaps cleared** | [Interest-rate swaps](/interest-rate-swap/), credit default swaps, FX swaps |
| **Mechanism** | Bilateral swaps novated; CCP guarantees performance via margin and mutualized capital |
| **Effect** | Reduced [counterparty risk](/counterparty-risk/) but higher transaction costs and capital requirements |

</aside>

## The pre-crisis bilateral market

Before 2008, most [interest-rate swaps](/interest-rate-swap/) and other derivatives were negotiated bilaterally. Bank A would call Bank B and agree to swap floating for fixed on a notional $50 million. The two banks recorded the contract and began exchanging cashflows.

If Bank A worried about Bank B's creditworthiness, Bank A might demand collateral. But collateral management was inconsistent. Many bilateral swaps carried **no collateral** at all, leaving the profitable bank heavily exposed to counterparty default.

This created a hidden web of leverage. When Lehman Brothers collapsed in September 2008, the financial system discovered that countless institutions held massive uncleared swap positions with Lehman and with each other. No one knew who owed whom or by how much. The cascading defaults threatened the entire banking system.

The lesson was clear: bilateral [counterparty risk](/counterparty-risk/) in an opaque, unmargined market was systemic risk.

## The Dodd-Frank mandate

The Dodd-Frank Act (2010) required the US to move standardised derivatives—primarily [interest-rate swaps](/interest-rate-swap/), credit default swaps, and foreign-exchange swaps—to central clearing. Broadly similar rules followed in Europe (EMIR), Japan, and other jurisdictions.

The mandate applied to "standardised" swaps: those with common terms, liquid pricing, and active secondary markets. Bespoke or illiquid swaps remained bilateral, but those had to carry significantly higher capital charges to account for their risk.

The shift was not instantaneous. Regulatory timelines extended over years, and some categories of counterparties (e.g., pension funds, corporates) received partial exemptions. But the direction was irreversible: move to central clearing or pay a regulatory penalty.

## How central clearing works

A central counterparty (CCP) operates as a **novation intermediary**. When two banks agree on a swap, the CCP steps in: Bank A's swap with Bank B is torn up and replaced with Bank A–CCP and CCP–Bank B. The CCP is now the counterparty to both.

The CCP does not take an economic position. If Bank A is entitled to receive 100 from Bank B, the CCP pays Bank A 100 (funded by Bank B's payment to the CCP). The CCP's profit is its fees, not trading risk.

To manage this role, the CCP requires **daily margin**. Each member posts initial margin (perhaps 5–15% of notional) to a segregated fund. Each day, as swap values change, the CCP marks positions to market and adjusts margin: winners collect variation margin; losers post additional margin.

This daily settlement eliminates the risk of an outstanding loss. If a member defaults, the CCP liquidates its positions immediately using the member's margin. Because margin is collected daily, the CCP's exposure is minimized.

## Mutualized capital and default cascades

If a member's margin is insufficient to cover its losses, the CCP has a **default fund**—typically a pool of capital contributed by all members, sized to cover the largest member's failure plus a stressed scenario.

In an extreme event, the CCP may tear up the defaulting member's positions, allocate losses across non-defaulters, or deploy the default fund. Because losses are shared, surviving members bear the cost, but in exchange they have clarity and containment. There is no domino effect of bilateral defaults cascading through the system.

This mutualization is the CCP's key innovation. It turns the problem of bilateral counterparty risk into a managed, transparent, predictable loss-allocation mechanism.

## The cost of clearing: capital and fees

Central clearing is not free. Members pay clearing fees (basis points on notional), initial margin, and operational overhead. For a large [interest-rate swap](/interest-rate-swap/) portfolio, clearing costs can add 10–50 basis points annually to a swap's expense.

More significantly, capital requirements increased. Under Basel III and subsequent regulations, cleared swaps carry risk weights (capital charges); uncleared swaps carry much higher weights. This creates a strong incentive to clear but also means cleared swaps consume balance-sheet capital.

For banks, this is manageable. For non-financial corporates accessing the swap market to hedge (e.g., a manufacturing company swapping fixed debt to floating), the capital charge and operational complexity make clearing more expensive and difficult.

## The exemption for end-users

Recognizing this, Dodd-Frank and subsequent rules exempted certain end-users from clearing requirements. A **non-financial corporation** hedging its own debt or commodity exposure could use bilateral swaps with its bank, avoiding the CCP.

This exemption, however, came with a condition: the bilateral swap required **collateral**. Most corporates now pledge collateral to their banks to back uncleared swaps, increasing their costs and operational burden.

Some corporates found clearing cheaper than collateral. Others, especially smaller firms, found both prohibitive and reduced their hedging.

## Systemic benefit and trade-offs

From a macro perspective, central clearing has worked. The opaque, unmargined $600 trillion derivatives market of 2008 now has meaningful price discovery and risk containment. The failures of Lehman and AIG did not trigger a derivatives-driven cascade because central clearing had been implemented.

But trade-offs exist. Central clearing concentrates systemic risk in a few large CCPs (in the US, the Chicago Mercantile Exchange and ICE Clear are dominant). If a CCP itself fails—a low-probability event but a tail risk—the consequences could be severe.

Regulators have placed stringent requirements on CCPs: stress testing, minimum capital, recovery and resolution plans. But a major CCP outage or failure remains a potential point of system fragility.

## Multilateral netting and efficiency

One under-appreciated benefit of clearing is **multilateral netting**. When thousands of swap contracts are cleared through one CCP, many offsetting positions cancel out. Instead of every bank owing every other bank, the CCP nets exposures and dramatically reduces the real capital tied up.

This netting effect means central clearing actually improves market efficiency by reducing balance-sheet usage, even as individual clearing costs rise.

## Residual bilateral markets

Despite the mandate, a substantial bilateral market remains. Pension funds, insurance companies, and other asset owners often enter non-standard swaps with minimal regulation. Private equity and hedge funds engage in bilateral contracts with looser collateral requirements.

These bilateral markets operate in the regulatory shadows, harder to monitor and without the CCP guarantee. Recent stress tests have shown that large pension-fund swaps could blow out during a financial crisis, replicating pre-2008 risks. Whether clearing will be extended to cover these remains politically contentious.

## Global fragmentation

Central clearing has not unified the world. Different jurisdictions (US, EU, Japan, Singapore) have different CCPs, margin methodologies, and exemptions. A swap cleared in Chicago's CME uses different risk models than one cleared in London's LCH.

This fragmentation creates arbitrage opportunities and complexity but also resilience: no single CCP failure brings down the entire system. However, it means cross-border swaps require careful routing, increasing costs.

## See also

<div class="wiki-seealso">

### Closely related

- [Interest-rate Swap](/interest-rate-swap/) — the primary derivative subject to clearing mandates
- [Counterparty Risk](/counterparty-risk/) — the core risk that clearing mitigates
- [Asset Swap](/asset-swap/) — cleared swaps are foundational to asset swap pricing
- [Liability Swap](/liability-swap/) — most standardised liability swaps are now cleared
- [Swap Curve](/swap-curve/) — central clearing improved transparency of swap pricing
- [Dodd-Frank Act](/dodd-frank-act/) — the US legislation mandating clearing

### Wider context

- Repo — another market transformed by post-crisis regulation
- [Systemic Risk](/systemic-risk/) — the regulatory concern driving clearing mandates
- [Hedge Fund](/hedge-fund/) — affected by clearing exemptions and capital requirements
- [Capital Adequacy](/capital-adequacy/) — Basel III rules governing capital for cleared and uncleared swaps

</div>
