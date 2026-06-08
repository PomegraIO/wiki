---
title: "Netting Agreements in OTC Swaps"
description: "Netting agreements in swap contracts collapse multiple exposures into a single net payment obligation, reducing credit risk and systemic contagion in OTC derivatives."
keywords:
  - netting agreement in swap contracts
  - close-out netting OTC swaps
  - ISDA master agreement netting
  - bilateral netting derivatives
---

*A **netting agreement** in OTC swaps allows two counterparties to collapse their entire portfolio of swap exposures into a single net payment obligation, rather than settling each swap individually. Under an ISDA master agreement—the standard legal framework—if one party defaults, all outstanding swaps are closed out immediately and netted. This mechanism slashes [credit risk](/credit-risk/) and is a cornerstone of financial stability in over-the-counter derivatives markets.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Netting Agreements — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives." />

<div class="wiki-infobox-caption">Netting reduces credit exposure by offsetting multiple swap positions into one net amount.</div>

|   |   |
|---|---|
| **Definition** | Legal mechanism to collapse multiple swap exposures into a single net obligation |
| **Standard contract** | ISDA Master Agreement (governs most OTC swaps) |
| **Types** | Payment netting; close-out netting on default |
| **Credit impact** | Reduces effective credit exposure by 40–60% on average |
| **Enforceability** | Strong in most jurisdictions; weaker in some emerging markets |
| **Collateral role** | Works alongside [variation margin](/swap-collateral-variation-margin/) and initial margin requirements |
| **Systemic benefit** | Limits contagion when a dealer or counterparty fails |

</aside>

## What Netting Does

Two financial institutions rarely deal in a single swap. Over time, they may have entered dozens of swaps—some at gains, some at losses. Without netting, if the counterparty defaults, the non-defaulting party would have to settle each swap separately under local bankruptcy law, a process that can take months or years and expose the non-defaulting party to the full market risk of losing profitable swaps while still owing on losing ones.

Netting collapses this complexity. All outstanding swaps between the two parties are treated as a single economic relationship. If Party A is owed $50 million from swaps but owes Party B $30 million from others, the net obligation is $20 million from Party B to Party A. If the counterparty defaults, only that $20 million is at stake, not the $80 million in gross notional exposure.

This is the legal and economic foundation of the modern derivatives market. Without enforceable netting, the credit risk on trillions of dollars in outstanding swaps would be prohibitive.

## Payment Netting vs. Close-Out Netting

### Payment netting

At each settlement date, instead of two parties exchanging gross payments, they calculate the net payment obligation. In a fixed-for-floating [interest-rate swap](/interest-rate-swap/):

- Party A owes $4 million (fixed 4% on $100M notional).
- Party B owes $4.5 million (SOFR + 0.50% = 5.0% on $100M notional).
- **Net result**: Party B pays Party A $0.5 million.

Payment netting is routine and undisputed. All swap dealers practice it at every reset date.

### Close-out netting

Close-out netting applies if a counterparty defaults or a termination event occurs. Instead of settling each swap according to its individual terms, all swaps are valued at current market prices and netted into a single amount due from or to the defaulting party.

Example:
- Swap 1 (3Y interest-rate swap): Party A has a gain of $2 million.
- Swap 2 (5Y currency swap): Party A has a loss of $1.5 million.
- Swap 3 (equity swap): Party A has a loss of $0.8 million.
- **Net position**: Party A is owed $2 million − $1.5 million − $0.8 million = **−$0.3 million** (owes $300K).

If Party B defaults, Party A can immediately close out all three swaps, realize the net loss of $300K, and move on. Without netting, Party A would be forced to pay all losses on Swaps 2 and 3 to the bankruptcy estate and might recover only a fraction of the $2 million gain from Swap 1—if at all.

## The ISDA Master Agreement

The International Swaps and Derivatives Association (ISDA) Master Agreement is the legal document that makes netting enforceable. It is the standard contract under which institutional counterparties trade swaps. Key provisions:

- **Sets default and termination events**: Define what constitutes a credit event or trigger for close-out.
- **Establishes netting rights**: Explicitly allow close-out netting of all transactions under the agreement.
- **Specifies termination methodology**: How swaps are valued and offset.
- **Chooses governing law**: Most commonly New York or English law, jurisdictions with strong, predictable enforcement of netting rights.

The ISDA Master Agreement also cross-defaults with other trading relationships. If you default on one swap agreement, other counterparties may be able to close out their positions immediately.

## Why Netting Reduces Systemic Risk

Consider a scenario without netting: When Lehman Brothers failed in September 2008, it had roughly $35 trillion in gross notional in outstanding derivatives. If counterparties had been forced to settle each derivative individually and had lost the ability to net, the bankruptcy process would have taken years, and losses would have cascaded through financial markets far more severely. Central clearing and netting helped contain that damage—though it was still enormous.

With netting:
- Counterparties' actual credit exposure is reduced by 40–60% on average.
- Systemic contagion is slower because losses are crystallized quickly, not suspended in bankruptcy limbo.
- Liquidity is conserved because entities do not post full gross notional as collateral.

Without netting, the effective cost of derivatives trading would be prohibitive, and markets would shrink dramatically.

## Netting and Collateral

Netting does not eliminate credit risk entirely—it reduces it. To manage residual risk, counterparties post [collateral](/swap/), both:

- **Initial margin**: Posted upfront to cover potential future exposure (PFE) over the time to close-out the position.
- **[Variation margin](/swap-collateral-variation-margin/)**: Posted daily (in cleared markets) or periodically (in bilateral OTC deals) to reflect mark-to-market changes.

Variation margin is netted too. If the portfolio has moved $10 million in Party A's favor, Party B posts $10 million. If it swings $5 million the other way, Party A pays $5 million. Only the net change flows, further reducing friction.

This combination—legal netting + daily margining—has allowed the OTC derivatives market to operate with minimal default losses relative to the scale of notional outstanding.

## Netting and Central Clearing

In 2009, post-financial crisis regulation mandated that certain standardized swaps be cleared through central counterparties (CCPs) like ICE Clear Credit or LCH SwapClear. Central clearing is netting on steroids:

- The CCP becomes the counterparty to every trade (novation).
- All exposures are netted across all participants.
- Initial and variation margin are pooled and used to cover losses in any default.
- The CCP's own capital and default fund back any shortfall.

Cleared swaps have far lower credit risk than bilateral OTC swaps, though the tradeoff is less customization and a small initial margin requirement.

## When Netting Fails

Netting is enforceable in most major jurisdictions (US, UK, EU, Japan, etc.), but enforcement can be weaker or ambiguous in some countries:

- **Emerging markets**: Some have not explicitly codified netting rights in law.
- **Bankruptcy law conflicts**: A foreign bankruptcy court may refuse to recognize netting rights, treating each derivative as a separate claim.
- **Regulatory changes**: Seizure or capital controls can override contractual netting.

For this reason, institutional counterparties typically require that swaps be governed by New York or English law and that either party can book trades in a subsidiary in a jurisdiction with strong netting rights.

## Netting and Regulatory Capital

Banks and dealers must hold [capital](/capital-adequacy/) against their credit exposures. The capital rule uses the net replacement value of the derivative (its mark-to-market) as the base, plus an add-on for potential future exposure. Netting reduces both the replacement value and the add-on, so it directly lowers capital requirements.

Regulators encourage netting because it aligns incentives: firms that net aggressively also tend to manage credit risk more actively and maintain tighter collateral agreements.

---

## See also

<div class="wiki-seealso">

### Closely related

- [Swap collateral and variation margin](/swap-collateral-variation-margin/) — how netting works with daily margin calls
- [Notional principal in swaps](/notional-principal-swap/) — the underlying amounts being netted
- [Counterparty risk](/counterparty-risk/) — the credit exposure that netting mitigates
- [Interest-rate swap](/interest-rate-swap/) — the swap type most commonly traded under ISDA
- [Central clearing](/swap/) — netting across all market participants, not just bilateral pairs

### Wider context

- [Systemic risk](/systemic-risk/) — how derivatives netting reduces contagion in financial markets
- [Bankruptcy and financial regulation](/dodd-frank-act/) — legal framework enabling netting enforcement
- [Credit risk](/credit-risk/) — the exposure reduced by netting mechanisms

</div>
