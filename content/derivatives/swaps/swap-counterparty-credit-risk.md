---
title: "Counterparty Credit Risk in Swap Contracts"
description: "Understand how counterparty credit risk arises in OTC swaps, why it differs from bond credit risk, and how netting and collateral reduce default exposure."
keywords:
  - counterparty credit risk in swaps
  - swap default exposure
  - bilateral credit risk derivatives
  - swap credit collateral netting
  - OTC derivative counterparty risk
image: /svg/derivatives.svg
---

*In an **interest rate swap**, both parties face the risk that the other will default. Unlike a [bond](/bond/), where an investor simply loses principal if the issuer fails, swap credit risk is **bilateral** and **dynamic**: it depends on which party is in the money, grows and shrinks as rates move, and can be halved by a master agreement that nets payments.*

<div class="wiki-hatnote">

This entry focuses on default risk in swaps as bilateral over-the-counter instruments. For how a swap's value fluctuates mid-life (determining how much credit exposure exists), see [How an interest rate swap is valued after inception](/swap-valuation-mid-life/). For the calculation of swap payments, see [Fixed-for-floating swap payment mechanics](/fixed-for-floating-swap-mechanics/).

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Counterparty Credit Risk in Swaps — Key Facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives." />

<div class="wiki-infobox-caption">Swap credit risk is two-way, changes with interest rates, and can be hedged through collateral and netting.</div>

|   |   |
|---|---|
| **Nature** | Bilateral: either party can default; the other loses only if they're in the money. |
| **Exposure** | Equals the swap's positive mark-to-market to the creditor party. |
| **Timing** | Emerges after inception; at trade date, exposure is usually zero. |
| **Asymmetry** | For the same swap, the fixed-rate payer's exposure differs from the floating-rate payer's. |
| **Mitigation** | Netting agreements (ISDA Master Agreements) and collateral posting (CSA) reduce exposure. |
| **Systemic impact** | Default by a major swap dealer can propagate through the financial system. |

</aside>

## Why Swap Credit Risk Is Bilateral

When you buy a corporate bond, your credit exposure is one-way: if the issuer defaults, you lose money. You have no obligation to the bondholder in return.

In a swap, both parties are obligated to each other. The fixed-rate payer must pay coupons; the floating-rate payer must pay floating rates. If either party defaults, the other loses the present value of their net gains from the remaining cash flows.

**Example:** You're the fixed-rate payer in a five-year swap paying 3.50% fixed and receiving LIBOR. Interest rates rise sharply. Your floating-rate payments (LIBOR) are now worth more than your fixed payments, so you'd make money if you exited. Your counterparty has defaulted. You lose the value of your position—the present value of the remaining net interest you would have received. But you also have no obligation to pay the fixed coupons anymore, which is a benefit. Your net loss is the amount by which you were in the money.

Conversely, if rates had fallen and you were out of the money (owing value to your counterparty), their default would actually help you: you escape paying the underwater position.

## Default Exposure Equals Positive Mark-to-Market

Your **counterparty credit exposure** in a swap is the amount of money you'd lose if the counterparty defaults right now, assuming you can replace the swap at current market rates. This is precisely the swap's positive mark-to-market from your perspective.

Using the [valuation](/swap-valuation-mid-life/) framework:
- If your mark-to-market is +$2 million (you're in the money), your exposure is $2 million.
- If your mark-to-market is −$1 million (you owe value), your exposure is zero—the other party is the creditor.

The exposure changes every day as rates move. A five-year swap might have zero exposure at inception, $5 million exposure after six months if rates fall favorably, then $3 million a year later if rates rise again. This variability is called **replacement risk**: if your counterparty defaults while you're in the money, you must enter a new swap at unfavorable terms or at market rates, incurring a cost.

## How Netting Reduces Exposure

In the early days of the swap market, each deal was bilateral and standalone. If one counterparty defaulted, the other would receive payment for their in-the-money swap and owe nothing on their out-of-the-money swaps—an asymmetric outcome that shocked creditors.

The **ISDA Master Agreement** changed this. It allows one party to offset (net) all swaps with a defaulting counterparty. If you've entered five swaps worth +$3M, +$1M, −$2M, −$1M, and +$1M with the same counterparty, and they default, you owe them $0 billion. The ISDA Master Agreement lets you collect on the three profitable swaps and walk away from the two losing ones, reporting a net claim of $2 million ($3M + $1M + $1M − $2M − $1M).

This **bilateral netting** dramatically shrinks credit exposure. In a 2021 snapshot, major banks' gross swap exposures were in the hundreds of billions, but after netting, net exposure dropped by 80–90%.

## Collateral and Variation Margin

Since the 2008 financial crisis, bilateral swaps—especially between dealers—are governed by **Credit Support Annexes (CSAs)**, which require collateral posting. Under a typical CSA:

- Each day, both parties mark the swap portfolio to market.
- The party with negative mark-to-market (owing value) posts cash or qualifying securities equal to the mark (minus a threshold—typically zero for dealer-to-dealer).
- This collateral is held by the creditor and returned if the swap is exited or if the mark swings back.

This **variation margin** mechanism means that if a swap has a significant positive mark-to-market, the counterparty has already posted cash to cover it. If they default the next day, the creditor has already received collateral. Their economic loss is capped at the risk of rates moving enough to exceed the collateral in a single day—a tail risk, but much smaller than the full notional or even the full mark-to-market.

## Exposure Across Multiple Swaps

If you trade swaps with many counterparties, you face multiple bilateral exposures. Your total credit risk is the sum of all positive marks across all counterparties (or, more precisely, the sum across counterparty groups, each group covered by one ISDA Master Agreement).

Major derivatives dealers manage this by:
1. Trading only with creditworthy counterparties (investment-grade rated banks and large corporates).
2. Netting all trades under ISDA Master Agreements.
3. Requiring collateral via CSAs, typically daily.
4. Using central counterparty clearinghouses—which stands between the two parties and guarantees performance—for standardized swaps.

## The Dealer Default Scenario

The systemic risk became vivid in 2008. Lehman Brothers was a major swap dealer with billions in net credit exposure to other dealers and corporations. When Lehman failed, counterparties suddenly lost money on their in-the-money swaps and had to unwind or replace positions. Lehman's bankruptcy also raised the possibility that counterparties would be unable to recover collateral quickly, freezing liquidity across the market.

Regulatory reforms post-2008 mandated [capital adequacy](/capital-adequacy/) rules for credit exposure on swaps, stress-testing of dealer balance sheets, and the use of central counterparties for liquid swaps. These measures have reduced (but not eliminated) the risk of a dealer failure cascading through the financial system.

## Comparison with Bond Credit Risk

A bond's credit risk is **unilateral and static** (though spreads move). If you hold a $100M bond paying 4.5%, your loss upon default is the $100M principal plus accrued interest. A swap's credit risk is **bilateral and dynamic**. Even if the bond's issuer is solvent, your counterparty in a swap is always at risk of default, and your exposure can jump from $0 to $20M overnight if rates move sharply.

For this reason, swap counterparty risk is priced differently from bond risk. A corporate might have a 2% bond spread and a 50 basis point swap spread at the same maturity—the latter reflecting the shorter-dated and collateralized nature of typical swap exposures.

## See also

<div class="wiki-seealso">

### Closely related

- [How an interest rate swap is valued after inception](/swap-valuation-mid-life/) — The mark-to-market that drives credit exposure
- [Fixed-for-floating swap payment mechanics](/fixed-for-floating-swap-mechanics/) — What gets paid and when
- [Swap vs forward rate agreement](/swap-vs-forward-rate-agreement/) — How FRAs differ in credit structure
- [Credit risk](/credit-risk/) — General principles of default exposure

### Wider context

- [Interest rate swap](/interest-rate-swap/) — Overview of how swaps work
- [Derivatives hedging](/derivatives-hedging/) — Why parties enter swaps
- Central counterparty clearinghouse — How standardized swaps reduce credit risk
- [Capital adequacy](/capital-adequacy/) — Regulatory capital rules for derivative exposure
- [Systemic risk](/systemic-risk/) — Economy-wide implications of dealer defaults

</div>
