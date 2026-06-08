---
title: "Swap Novation Explained"
description: "Novation is the replacement of one party to a swap contract with a new counterparty, requiring consent of the original party and transferring all rights and obligations."
keywords:
  - swap novation
  - novation in swaps
  - swap counterparty change
  - derivatives novation
  - swap transfer
image: /svg/derivatives.svg
---

*A **swap novation** is a legal process that replaces one party to an existing [swap](/swap/) contract with a new counterparty, with the knowledge and consent of the party remaining in the swap. Instead of the original parties unwinding the position and entering a new contract, novation transfers all economic rights and obligations to the new counterparty while preserving the terms and life of the underlying agreement. It is the standard mechanism for clearing swaps through central counterparties and for restructuring dealer positions during distress or consolidation.*

<div class="wiki-hatnote">

Novation is distinct from assignment (which can often occur without consent) and from close-out netting (which terminates both sides). It requires explicit agreement and replaces one party entirely.

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Swap Novation Explained — Key Facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives and risk management." />

<div class="wiki-infobox-caption">Novation transfers swap obligations to a new counterparty; it requires consent and is the backbone of swap clearing.</div>

|   |   |
|---|---|
| **Definition** | Legal replacement of one swap party with a new counterparty |
| **Requires** | Explicit consent of the remaining party; economic terms unchanged |
| **Common drivers** | Clearing through a central counterparty, dealer consolidation, [counterparty risk](/counterparty-risk/) mitigation |
| **Legal mechanism** | Discharge of original contract + simultaneous creation of new contract with new party |
| **Fees involved** | Trivial administrative costs; original spread/terms stay intact |
| **Use in clearing** | Central clearinghouse novates dealer–client swap to clearinghouse–dealer + clearinghouse–client |
| **Difference from assignment** | Assignment can occur unilaterally in some contracts; novation requires explicit consent |

</aside>

## What Novation Does

When a swap is novated, three things happen simultaneously:

1. **Original contract is discharged**: The original agreement between parties A and B is legally terminated.
2. **New contract is created**: A new swap contract, with identical economic terms, is created between the remaining original party and the new counterparty (let's call it party C).
3. **Consent is required**: Party B or the remaining party must agree to the novation; it cannot happen unilaterally.

The result: the remaining party (A) now owes and is owed cash flows by C instead of B, with no change to the swap's [coupon rate](/coupon-rate/), [notional amount](/strike-price/), or [maturity](/expiration-date/). The economics are identical; only the credit risk counterparty changes.

## Why Novation Matters: Clearing and Central Counterparties

The most significant use of novation is in **swap clearing**. When a swap is cleared through a central counterparty (CCP), novation happens in a specific sequence:

1. **Original swap**: Bank A and Bank B enter into a $100 million interest-rate [swap](/swap/).
2. **At clearing**: The CCP interposes itself. The original swap between A and B is novated into *two* swaps: A–CCP and CCP–B.
3. **Result**: The CCP becomes the [counterparty](/counterparty-risk/) to both, but the underlying economic flows remain unchanged.

This setup isolates A from B's credit risk. If B defaults, A still receives its swap payments from the CCP (which is backed by collateral and guaranty funds). The CCP then manages the B side of its portfolio, potentially closing out B's position or transferring it to a solvent counterparty.

Before mandatory clearing (post-2008), bilateral swaps carried [counterparty risk](/counterparty-risk/)—if the dealer went under, the client lost both the swap's economic value and any margin posted. Novation to a CCP eliminated that risk, which is why clearing became a regulatory requirement for standardized swaps.

## Novation in Dealer Consolidation and Distress

Outside clearing, novation is used when:

**Dealers merge**: If Goldman Sachs and another institution consolidate, the combined entity may novate existing swaps to simplify the balance sheet. Instead of running the same swap twice (once for each dealer), they combine into a single contract with the client.

**A dealer is distressed**: If a bank enters [credit default swap](/credit-default-swap/) protection or regulatory capital stress, it may ask clients to agree to novate their swaps to a stronger counterparty. The client consents because it reduces [counterparty risk](/counterparty-risk/).

**A dealer exits a market**: A bank closing a swap desk may novate existing client positions to a peer bank that is acquiring the book. The client retains the same economic exposure but now owes payments to a different dealer.

In all cases, novation preserves the original swap's terms and avoids the need for both parties to unwind, find new counterparties, and re-price.

## Novation Mechanics and Documentation

Swap novations are documented in **Novation Agreements**, which state:

- Identity of the exiting and incoming parties
- Which swap is being novated (reference contract details)
- Effective date of novation
- Confirmation that economic terms are unchanged
- Consent of all parties

The legal effect is a **three-party transaction that results in a two-party contract**. Party A signs with Party C, the original agreement with B is discharged, and B is released from all future obligations (and has no further claims).

**Fees** are minimal—mostly administrative processing. The [spread](/bid-ask-spread/) or fixed rate on the swap does not change. The incoming counterparty (C) steps into the exact economic position that B held, at no price adjustment.

## Novation vs. Assignment

**Assignment** is sometimes confused with novation. In an assignment, one party transfers its contractual rights to a third party, but the original party may retain some contingent obligations. Assignment often *does not* require the consent of the non-assigning party (depending on contract language).

**Novation** requires explicit consent and fully releases the exiting party from all obligations and future claims. It is a cleaner, more protective mechanism and is the standard in derivatives markets.

In swap markets, novation is preferred because the remaining party (A) does not want to be exposed to credit risk from the exiting party (B) if B later defaults on obligations to C. Novation ensures a clean break.

## Novation in Restructuring and [Credit Events](/credit-event-sovereign/)

During [debt restructuring](/debt-restructuring/), novation can be used to transfer swaps as part of a package deal. A company buying a division from a bankrupt firm may novate the division's hedging swaps to itself, assuming the counterparties consent. This simplifies unwinding and allows the acquiring party to step seamlessly into the hedge without repricing or gap risk.

In [credit default swap](/credit-default-swap/) markets, novation is also used to transfer protection between investors—one protection-buyer may novate its position to another investor if market conditions change or if capital needs force an exit.

## See also

<div class="wiki-seealso">

### Closely related

- [Swap](/swap/) — the underlying contract transferred in novation
- [Counterparty Risk](/counterparty-risk/) — why novation to stronger counterparties is valuable
- [Credit Default Swap](/credit-default-swap/) — derivative often novated in distress scenarios
- [Interest Rate Swap](/swap/) — the most commonly novated swap type
- [Central Counterparty](/central-bank/) — the party that interposes itself in cleared swaps
- [Debt Restructuring](/debt-restructuring/) — where novation appears in distress situations

### Wider context

- [Derivatives Hedging](/derivatives-hedging/) — broader context for swap use
- [Clearinghouse](/stock-exchange/) — infrastructure where novations occur at scale
- [Credit Risk](/credit-risk/) — what novation to a CCP mitigates
- [Dodd-Frank Act](/dodd-frank-act/) — regulation requiring clearing of standardized swaps
- [Over-the-Counter Market](/over-the-counter-market/) — where bilateral swaps are novated

</div>
