---
title: "Guaranteed Settlement"
description: "Central counterparty commitment to complete transactions even if a clearing member defaults, insulating buyers and sellers."
keywords:
  - central counterparty
  - CCP guarantee
  - settlement finality
  - credit risk mitigation
---

*The **guaranteed settlement** promise is a central commitment made by a [central-counterparty-clearing](/wiki/central-counterparty-clearing/) (CCP) organization: when a trading member defaults, the CCP steps in as buyer to every seller and seller to every buyer, ensuring that all transactions settle in full regardless of counterparty failure.*

<aside class="wiki-infobox">

| Aspect | Detail |
|--------|--------|
| **Legal mechanism** | Novation or legally binding CCP insertion between parties |
| **Backstop source** | Default waterfall: member margin, CCP capital, mutualized loss fund |
| **Critical for** | Derivatives clearing, repo, central bond clearing |
| **Pre-Dodd-Frank** | CCP guarantees were less comprehensive; bilateral [counterparty-credit-risk](/wiki/counterparty-credit-risk/) was higher |
| **Post-2008 mandate** | G20 required standardized derivatives clear through CCPs |
| **Stress events** | Lehman Brothers 2008, MF Global 2011, CME's handling of both |

</aside>

## How the guarantee works in practice

When a trader enters a derivatives contract on a [centralized-exchange](/wiki/centralized-exchange/) or via a clearing service, the CCP inserts itself between the buyer and seller through a process called **novation**. Instead of the buyer owing the seller, the buyer owes the CCP and the CCP owes the seller. The buyer and seller have zero direct credit exposure to each other; all risk flows through the CCP.

The value of this setup becomes clear when a clearing member fails. If Bank A defaults on a $100 million obligation to Bank B, Bank B does not take a $100 million loss. Instead, the CCP immediately steps into the role of counterparty, declaring: "You were owed $100 million from Bank A; you now have a $100 million claim on the CCP." The CCP then liquidates Bank A's positions, margin collateral, and any other resources to satisfy that claim. This transformation turns a binary default risk—either Bank B gets paid or loses everything—into a prioritized [liquidation](/wiki/liquidation/) process where the CCP's capital and guarantee absorb losses in order.

## The default waterfall: multilayered protection

The CCP does not rely solely on its own capital. Instead, a **default waterfall** ranks sources of loss absorption:

1. **Defaulting member's margin**: The CCP immediately liquidates the failed member's posted collateral (initial and [variation-margin](/wiki/variation-margin/)).
2. **CCP capital**: The CCP's own equity absorbs losses that margin cannot cover.
3. **Loss-mutualization fund**: Non-defaulting members contribute pro rata to a guarantee fund, which absorbs the next tranche.
4. **Additional member assessments**: If the fund is depleted, surviving members may be charged additional assessments (rare but possible under CCP bylaws).
5. **Member-forced wind-down or guarantee suspension**: In extreme cases (not observed in modern CCPs), the CCP may segregate the failed member's positions and force a slower liquidation to preserve the broader system.

This waterfall ensures that the CCP's guarantee is backed by real capital and that non-defaulting members have skin in the game, creating discipline.

## Settlement finality and irreversibility

A critical feature of the CCP guarantee is **settlement finality**: once a trade is novated and settled, it is irrevocable. A buyer of a bond cannot unwind the settlement even if the issuer immediately defaults. This irreversibility is the cornerstone of financial stability; without it, settlement uncertainty would freeze markets.

In the U.S., the [depository-trust-company](/wiki/depository-trust-company/) (for equities and bonds) and [options-clearing-corporation](/wiki/options-clearing-corporation/) (for derivatives) provide this finality. Internationally, exchanges like [euronext](/wiki/euronext/) and [london-stock-exchange](/wiki/london-stock-exchange/) operate with CCPs ([euroclear](/wiki/euroclear/) and [clearnet](/wiki/lch-clearnet/)) that guarantee settlement to the last second.

## Post-Dodd-Frank mandates and global standardization

The [dodd-frank-act](/wiki/dodd-frank-act/) and subsequent international agreements (via the Financial Stability Board and G20 mandate on derivatives) required that most standardized derivatives clear through regulated CCPs rather than via bilateral [counterparty-risk](/wiki/counterparty-risk/) relationships. This shift reduced systemic risk by concentrating defaults into controlled environments.

The [cftc-regulator](/wiki/cftc-regulator/) and [sec-enforcement](/wiki/sec-enforcement/) now designate certain derivatives exchanges and clearinghouses as systemically important, subjecting them to [stress-testing](/wiki/stress-testing/) and capital requirements. The idea is that CCP guarantees are only as good as the CCP's solvency; regulators therefore impose minimum capital ratios, margin adequacy standards, and [reverse-stress-test](/wiki/reverse-stress-test/) scenarios to ensure the guarantee holds even in extreme crises.

## Real-world tests: Lehman and MF Global

The Lehman Brothers bankruptcy (September 2008) was the first major stress test of modern CCP guarantees. The [options-clearing-corporation](/wiki/options-clearing-corporation/) and [cme-group](/wiki/cme-group/) cleared Lehman's positions without triggering losses to non-defaulting members or the CCPs' own capital. The waterfall system absorbed Lehman's margin ($6+ billion of collateral), and the failed firm's positions were transferred to solvent dealers. This success validated the CCP guarantee model.

MF Global (November 2011), a smaller but more operationally complex failure, again held: futures cleared through CME settled cleanly; equity options cleared through OCC settled cleanly. Client funds were eventually recovered due to segregation rules and CCP guarantees. These two episodes established historical evidence that CCP guarantees work under real stress.

## Limitations and remaining risks

Despite the guarantee, a few risks remain:

**Procyclical margin**: CCPs raise margin (both initial and variation) when volatility spikes. During a crisis, when a member is thinly capitalized, a sudden [margin-call](/wiki/margin-call-forex/) can trigger a forced liquidation or default. The guarantee protects other members but does not prevent the cascade.

**Liquidity risk during liquidation**: If a failed member's positions are so large that liquidating them moves prices unfavorably, the CCP may realize bigger losses than pre-default market valuations suggested. [Lch-clearnet](/wiki/lch-clearnet/) and [ice-clear-credit](/wiki/ice-clear-credit/) have provisions for this, but it remains a tail risk.

**Contagion**: A CCP guarantee only applies within that CCP. If a major bank fails and was clearing through multiple CCPs, losses could cascade across clearing venues, exposing interconnectedness risks that the guarantee cannot eliminate.

Despite these caveats, the CCP guarantee has been the single most effective post-2008 financial reform, reducing [systemic-risk](/wiki/systemic-risk/) and enabling [settlement-cycles](/wiki/settlement-cycles/) to compress from T+3 to T+2 and eventually T+1.

<div class="wiki-seealso">

### Closely related
- [Central counterparty clearing](/wiki/central-counterparty-clearing/) — Operational mechanism enabling CCP guarantees
- [Counterparty credit risk](/wiki/counterparty-credit-risk/) — Risk the CCP guarantee mitigates
- [CCP default waterfall](/wiki/ccp-default-waterfall/) — Layered loss absorption mechanism
- [Novation](/wiki/novation-central-counterparty/) — Legal process of CCP insertion
- [Settlement finality](/wiki/final-settlement/) — Irreversibility of settled transactions

### Wider context
- [Dodd-Frank Act](/wiki/dodd-frank-act/) — Legislation mandating CCP clearing
- [Clearing firm](/wiki/clearing-firm/) — Organization that manages settlements
- [Lehman Brothers collapse](/wiki/lehman-brothers-collapse/) — Event validating CCP guarantees
- [Options Clearing Corporation](/wiki/options-clearing-corporation/) — Major U.S. CCP
- [CME Group](/wiki/cme-group/) — Major derivatives CCP

</div>
