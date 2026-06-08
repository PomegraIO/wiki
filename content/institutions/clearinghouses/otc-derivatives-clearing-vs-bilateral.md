---
title: "OTC Derivatives Clearing vs Bilateral Settlement: Key Differences"
description: "Compare OTC derivatives clearing through central counterparties versus bilateral settlement. Understand risk, cost, and operational trade-offs."
keywords:
  - otc derivatives clearing vs bilateral
  - central counterparty clearing
  - bilateral settlement derivatives
  - counterparty risk management
  - cleared vs uncleared swaps
image: "/svg/institutions.svg"
---

*OTC derivatives clearing vs bilateral settlement represents a fundamental structural choice in how derivative contracts settle. Central clearing routes trades through a clearinghouse that stands between counterparties, while bilateral settlement keeps the contract between two parties with no intermediary. Each approach locks in different trade-offs: clearing reduces counterparty risk and enforces margin standards, but bilateral deals often cost less and offer more flexibility.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">OTC Clearing vs Bilateral — key facts</div>

<img src="/svg/institutions.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Clearing centralizes risk management and enforces uniform rules; bilateral deals preserve contract customization.</div>

|   |   |
|---|---|
| **Central party** | Clearinghouse (CCP) vs. direct counterparties |
| **Counterparty risk** | Eliminated (CCP risk replaces it) vs. two-sided |
| **Margin required** | Daily variation + initial, standardized | Variable by contract & credit |
| **Cost structure** | Clearing fees + higher initial margin | Potentially lower upfront, CSA-dependent |
| **Customization** | Standardized terms | Full flexibility |
| **Regulatory requirement** | Mandatory for many swaps (Dodd-Frank, EMIR) | Allowed only if exempted |

</aside>

## How central clearing works

When a derivative trade clears, the clearinghouse interposes itself. Party A no longer owes Party B; instead, Party A owes the clearinghouse and the clearinghouse owes Party B. This tripartite structure isolates each party's credit exposure to the CCP alone, not to each other.

The clearinghouse enforces daily settlement of variation margin—the daily mark-to-market gain or loss—and collects initial margin upfront. Both amounts are segregated in the CCP's own accounts. If one member defaults, the clearinghouse draws on that member's initial margin, then on a guarantee fund capitalized by surviving members, to meet obligations to the non-defaulting side.

Standardization is the price of centralization. Cleared contracts use vanilla terms: fixed-rate and floating-rate swaps on major currencies and indices, swaptions, futures, and simple options. A swap that deviates—say, a conditional coupon or a basket of three obscure emerging-market rates—cannot clear. The CCP's risk model works only if the population of contracts is narrow and liquid.

## The bilateral settlement alternative

Bilateral settlement leaves the contract between the two parties. They negotiate terms freely: any tenor, any underlying, any contingency. Margin is governed by a Credit Support Annex (CSA), a bilateral agreement that defines collateral posting rules. Initial margin can be zero if the parties trust each other; variation margin is typically exchanged daily.

Counterparty risk remains two-sided. If your counterparty fails, you lose the benefit of an in-the-money position and face replacement risk—you must hedge the economic exposure in the market at current prices. Conversely, if your counterparty is highly rated and you post collateral, bilateral settlement can feel cheaper: you post less initial margin against a trusted bank than you would to a clearinghouse.

The CSA is a private document. Terms vary: some agreements include credit thresholds (you don't post margin until losses hit a negotiated level), multipliers (you post 1.5x accrued losses), or haircuts (you post more collateral for volatile assets). A bank might offer favorable terms to a large, investment-grade client and harsher terms to a smaller counterparty.

## When clearing is mandatory

Post-financial crisis regulation in the US and EU made central clearing the default for standard derivatives. The [Dodd-Frank Act](/dodd-frank-act/) required most interest-rate and currency swaps to clear through a registered swap clearinghouse. The European Market Infrastructure Regulation (EMIR) imposed the same rule in the EU.

Exemptions exist. A swap is exempt if it is not "standardized" (the clearinghouse's price-discovery model can't accommodate it), if the counterparties are not financial entities (e.g., a manufacturer hedging commodity exposure), or if one party has an aggregate notional of swaps below a regulatory threshold. Many end-users and corporates still operate outside the cleared world.

A bank or hedge fund cannot opt for bilateral settlement on a standardized swap; they must clear. But they can bilaterally trade non-standardized products, commodity swaps, equity swaps, or credit derivatives that no clearinghouse accepts.

## Capital and margin burden

Cleared swaps require variation margin and initial margin, both calculated daily by the CCP. Initial margin is typically pegged to a value-at-risk (VaR) model—1–2 standard deviations of daily P&L over a 10-day holding period. For a $100 million notional interest-rate swap, initial margin might run $500k to $2 million per side.

Bilateral swaps use a CSA that reflects the credit quality of both parties. Two investment-grade banks might agree on a $100k threshold: neither posts collateral until the mark-to-market loss exceeds $100k. A bank and a speculative-grade hedge fund might post full variation margin with a 20% haircut on non-cash collateral. A bank and an unrated subsidiary might exchange collateral daily from day one.

The difference matters for [cost-of-debt](/cost-of-debt/) modeling. Clearing adds a direct cost (clearing fees, often 0.5–2 basis points per annum on notional) and an indirect cost (higher initial margin tied up, carrying an implicit funding cost). Bilateral settlement may shift costs to the riskier party—they post more or post sooner—but can avoid the clearing fee.

## Operational and liquidity layers

Cleared swaps trade on designated swap execution facilities (SEFs) and report to swap data repositories (SDRs). Prices are transparent; the largest swap trades appear in real-time market data feeds. A bank or trader looking to unwind a $50 million interest-rate swap can check a data feed, call a dealer, and often trade within minutes.

Bilateral swaps are opaque. You negotiate directly, and the trade typically does not appear in public data until SDR reporting (which is not real-time). If you want to exit a bespoke bilateral swap early, you negotiate a termination with the original counterparty or find a trilateral arrangement where a third party assumes the original dealer's side. This takes days to weeks.

Liquidity, in turn, props up market efficiency. A clearinghouse publishes daily settlement prices and collateral levels, creating transparency that tightens bid-ask spreads. For vanilla swaps, the clearing market is deep and liquid. For bilateral swaps—especially non-standard ones—you face thicker spreads and execution risk.

## Counterparty risk vs. systemic risk

From a single firm's perspective, clearing eliminates counterparty risk: the CCP replaces it. But from a system-wide view, clearing concentrates risk in a few large CCPs. If a major CCP's guarantee fund is breached—if losses exceed all segregated collateral and the fund—surviving members might face a loss allocation, or the CCP might fail entirely.

This is why CCPs are heavily regulated. They must meet strict [capital-adequacy](/capital-adequacy/) standards, conduct stress tests on members' default scenarios, and regularly validate their margin models. A bilateral swap creates no systemic risk if it is small; but a $10 trillion portfolio of bilateral swaps across the banking system creates concentration risk: one large counterparty failure cascades.

After the 2008 crisis, the shift to clearing was meant to contain counterparty contagion. It succeeded in reducing opacity and enforcing margin discipline. It also relocated risk to a new critical node—the clearinghouse.

## Hybrid and novation considerations

Some firms manage both. They clear standardized swaps for efficiency and regulatory compliance. They use bilateral settlement for customized or illiquid products where clearing is impossible or for small trades where clearing fees outweigh the risk reduction.

A swap can also change custody. A bilateral swap can be novated into a cleared swap if both parties agree and the swap is standardized. Conversely, a cleared swap cannot be bilateralized; it stays cleared for its life.

Banks also offer cleared swaps with collateral funding agreements: they clear on behalf of clients and charge a fee for collateral management. This layers clearing with bilateral negotiation on margin terms.

## See also

<div class="wiki-seealso">

### Closely related

- Clearinghouse (Derivatives) — structure and role of a central counterparty
- [Counterparty Risk](/counterparty-risk/) — how default exposure arises in bilateral contracts
- [Swap](/swap/) — definitions and mechanics of interest-rate and currency swaps
- Credit Support Annex (CSA) — bilateral margin agreements (if available)
- [Dodd-Frank Act](/dodd-frank-act/) — US clearing mandate and regulatory context
- [Systemic Risk](/systemic-risk/) — how concentrated CCP risk translates to financial stability

### Wider context

- [Derivatives Hedging](/derivatives-hedging/) — broader use of swaps in risk management
- [Market Maker (Trading)](/market-maker-trading/) — dealers' role in cleared and bilateral markets
- [Over-the-Counter Market](/over-the-counter-market/) — OTC derivatives ecosystem
- [Margin Call (Forex)](/margin-call-forex/) — daily settlement and margin mechanics

</div>
