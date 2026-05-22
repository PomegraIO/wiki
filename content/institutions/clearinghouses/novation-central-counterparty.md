---
title: "Novation by Central Counterparty"
description: "The legal and operational process by which a central clearing house substitutes itself as the counterparty to both sides of a bilateral transaction."
keywords:
  - novation
  - central counterparty
  - ccp
  - clearing
  - counterparty risk
  - trade guarantee
---

*A **novation by central counterparty (CCP)** occurs when a trade that was originally bilateral (between two financial institutions) is legally and operationally substituted so that the CCP becomes the buyer to every seller and the seller to every buyer. This novation transfers [counterparty risk](/wiki/counterparty-risk/) from bilateral exposure to the CCP, which stands between the parties and guarantees settlement.*

Novation is the legal foundation of modern clearing. When a swap dealer and a pension fund enter a trade, they no longer face each other on the trade; they each face the CCP. This single substitution—one contract becomes two—is what allows central clearing to reduce systemic risk by netting exposures and mutualizing default risk across all CCP members.

<aside class="wiki-infobox">

| Aspect | Detail |
|--------|--------|
| **Key mechanism** | Original contract is discharged; two new contracts arise (each counterparty with CCP) |
| **Legal timing** | Novation occurs at trade acceptance, often within seconds of execution |
| **Effect on risk** | Bilateral counterparty risk → CCP default risk (netted, mutualized) |
| **Examples** | [Interest-rate swaps](/wiki/interest-rate-swap/), [credit derivatives](/wiki/credit-derivative/), [futures](/wiki/futures-contract/) |
| **Not applicable** | Most bilateral loans, OTC equity derivatives, repo (when bilateral) |
| **Regulator** | [CFTC](/wiki/cftc-regulator/) (U.S.), [EMIR](/wiki/emir/) (EU) mandate clearing for standardized derivatives |

</aside>

## The Process

When a dealer executes a trade on an exchange or through a [swap execution facility](/wiki/swap-execution-facility/), the trade is transmitted to a CCP (e.g., [ICE Clear Credit](/wiki/ice-clear-credit/) for credit derivatives, CME Clearinghouse for interest-rate swaps). The CCP:

1. Receives trade details from both counterparties.
2. Validates that counterparties agree on terms (price, notional, settlement date).
3. **Novates** the bilateral trade: the original trade is extinguished, and two new trades (each between a counterparty and the CCP) are created.
4. Takes responsibility for guaranteeing both sides of settlement.
5. Begins daily [mark-to-market](/wiki/mark-to-market/) and [variation margin](/wiki/variation-margin/) collection.

From a legal standpoint, novation is a substitution of one contract for two. The original bilateral contract is discharged (typically by agreement), and two new contracts—each identical in economic terms but with the CCP as counterparty—come into effect. Both parties' legal rights and obligations are now to the CCP, not to each other.

## Counterparty Risk Reduction

The economic effect of novation is dramatic. Suppose Bank A and Bank B enter a $100M interest-rate swap. Before clearing, each is exposed to the other's credit risk. If Bank B defaults, Bank A may lose the present value of the swap (say, $5M).

After novation via a CCP, Bank A and Bank B are no longer exposed to each other. Instead:
- Bank A owes the CCP whatever it owes on its side of the swap.
- Bank B owes the CCP whatever it owes on its side of the swap.
- The CCP collects [variation margin](/wiki/variation-margin/) from the losing side daily, so mark-to-market losses are realized continuously, not deferred to maturity.

If Bank B defaults, the CCP absorbs the loss using Bank B's [initial margin](/wiki/initial-margin/) and other resources in its [default waterfall](/wiki/ccp-default-waterfall/), not Bank A's balance sheet. This is called "mutualization of risk"—all CCP members are protected, and the cost of any member's default is socialized among all participants.

## Netting and Collateral Efficiency

Novation enables **multilateral netting**. Suppose the CCP has 100 members, each with multiple positions. Without novation, each pair of members would need to post collateral on their bilateral exposures (potentially redundant). With novation, each member posts collateral only to the CCP, based on their net exposure across all trades. This dramatically reduces collateral demand.

Pre-2008, [counterparty risk](/wiki/counterparty-risk/) was largely unnetted. Bank A might owe Bank C $5M on one swap and owe Bank C $5M on another, but bank-to-bank netting agreements were not universal. Post-2008, the [Dodd-Frank Act](/wiki/dodd-frank-act/) and [EMIR](/wiki/emir/) mandated central clearing for standardized derivatives, making novation and netting systemic.

## The CCP Guarantee

When a CCP novates a trade, it explicitly or implicitly guarantees settlement. This means:
- If Bank A owes the CCP $1M on the settlement date, the CCP demands payment.
- If Bank A cannot pay, the CCP has legal priority to seize Bank A's collateral and use it to cover the loss.
- If Bank A's collateral is insufficient, the CCP invokes its [default waterfall](/wiki/ccp-default-waterfall/): it taps its insurance fund, then draws on a guarantee fund (contributions from all members), then potentially calls for additional member contributions.

This guarantee is the CCP's franchise: market participants will use the CCP only if they trust it to stand behind failed members. Recent crises (e.g., the 2008 near-collapse of [Lehman Brothers](/wiki/lehman-brothers-collapse/)) stressed how critical CCP viability is to systemic stability.

## Novation vs. Other Settlement Models

Not all derivatives are centrally cleared:
- **Bilateral repo** — no novation; the two parties remain exposed to each other. Post-2008, the industry moved toward CCP-cleared repo, but significant bilateral repo markets persist.
- **OTC equity derivatives** — largely not cleared; counterparty risk remains bilateral. Some [credit derivatives](/wiki/credit-derivative/) (credit-default swaps) are cleared; others are not.
- **Bespoke derivatives** — customized swaps between sophisticated counterparties often remain bilateral, because their non-standard nature precludes centralized clearing.

The regulatory trend post-2008 has been to **expand clearing mandates** — pushing more standardized derivatives through CCPs to reduce systemic risk. The trade-off is reduced counterparty risk vs. higher collateral costs (members must post initial and variation margin daily) and CCP operational risk (if the CCP fails, systemic consequences are severe).

## Mechanics of Default

When a CCP member defaults, novation creates a powerful tool for managing the failure:
1. The CCP marks all defaulting member's positions to market.
2. It calculates the member's net liability (or asset, if the member is a creditor).
3. The CCP immediately reassigns the defaulting member's positions to other members (who are compensated from the CCP's guarantee fund).
4. The CCP hedges any exposures it inherits temporarily, then auctions the positions to other members.

This process typically takes hours to days, not months. By contrast, a bilateral default (e.g., the [Lehman bankruptcy](/wiki/lehman-brothers-collapse/)) can entangle counterparties in legal disputes for years.

## Practical Implications for Traders

From a trader's perspective, novation is transparent: they execute a trade, it is novated to the CCP, and they receive a confirmation from the CCP showing themselves as counterparty. They are aware that the CCP stands between them, and they pay for this protection (implicitly, through higher transaction costs and collateral requirements).

Modern derivatives markets cannot function without novation and central clearing. Regulatory requirements (U.S. [Dodd-Frank](/wiki/dodd-frank-act/), EU [EMIR](/wiki/emir/)) now mandate clearing for standardized swaps, making novation the default for trillions of dollars in derivatives notional each day.

<div class="wiki-seealso">

### Closely related
- [Central counterparty clearing](/wiki/central-counterparty-clearing/) — the CCP's role in the broader clearing ecosystem
- [Counterparty risk](/wiki/counterparty-risk/) — the bilateral risk novation eliminates
- [CCP default waterfall](/wiki/ccp-default-waterfall/) — how CCPs manage member failures
- [Variation margin](/wiki/variation-margin/) — the daily cash flow resulting from novation
- [Interest-rate swap](/wiki/interest-rate-swap/) — a commonly cleared derivative

### Wider context
- [Dodd-Frank Act](/wiki/dodd-frank-act/) — U.S. law mandating clearing
- [EMIR](/wiki/emir/) — EU regulation on derivatives clearing
- [Swap execution facility](/wiki/swap-execution-facility/) — venue for novated trades
- [Lehman Brothers collapse](/wiki/lehman-brothers-collapse/) — motivated central clearing reforms
- [Collateral management](/wiki/counterparty-haircuts/) — operational consequence of novation

</div>
