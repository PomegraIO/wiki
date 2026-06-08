---
title: "Counterparty Risk vs Credit Risk"
description: "Counterparty risk arises from bilateral derivatives exposure and mark-to-market losses; credit risk is traditional one-directional loan default exposure."
keywords:
  - counterparty risk vs credit risk
  - bilateral derivatives exposure
  - mark-to-market counterparty exposure
  - credit risk loan default
  - derivative counterparty risk
image: /svg/risk.svg
---

*Counterparty risk and credit risk are often confused but address different failure modes. **Credit risk** is the classical lender's worry: a borrower stops paying back a loan. **Counterparty risk** is the derivatives trader's worry: the other side of a swap, forward, or options contract refuses to pay when the contract has swung in your favor, and the bank or trading house has lost money on the current market value of that exposure. The core distinction is directionality: credit risk is one-way (you are owed, they owe), while counterparty risk is potentially mutual (either party may be in the money at any moment).*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Counterparty Risk vs Credit Risk — key facts</div>

<img src="/svg/risk.svg" alt="An abstract editorial mark for risk." />

<div class="wiki-infobox-caption">One is bilateral and mark-to-market; the other is one-directional and contractual.</div>

|   |   |
|---|---|
| **Definition** | Credit: one-way loan default. Counterparty: bilateral mark-to-market exposure on derivatives. |
| **Maturity** | Credit risk: fixed loan term. Counterparty risk: evolves daily with market prices. |
| **Exposure size** | Credit: notional loan amount. Counterparty: current replacement value of the contract. |
| **Direction** | Credit: one-way (lender to borrower). Counterparty: swaps, which way (could be either party). |
| **Mitigation** | Credit: collateral, covenants, diversification. Counterparty: netting, collateral, CDS hedges. |
| **Historical event** | Credit: corporate bond defaults. Counterparty: Lehman Brothers derivatives losses (2008). |

</aside>

## Credit risk: the traditional loan perspective

Credit risk is the risk that a borrower defaults on a loan. A bank lends $100 million to a corporation at a stated interest rate. The bank expects to receive principal and interest on schedule. If the borrower becomes insolvent or refuses to pay, the bank suffers a loss.

The bank's exposure is **one-directional and fixed** (at origination). The amount at risk is the outstanding balance of the loan—initially $100 million, declining as repayment occurs. The bank can measure credit risk using bond spreads, credit ratings, or default probability models. Mitigation tools include securing the loan with collateral (mortgages, equipment, receivables), imposing covenants (minimum debt-to-equity ratios, liquidity thresholds), requiring guarantees, or diversifying across many borrowers.

Credit risk is embedded in bonds, mortgages, commercial loans, and structured credit products like [mortgage-backed securities](/mortgage-backed-security/).

## Counterparty risk: the derivatives danger

Counterparty risk arises on **bilateral contracts**—those where either party could owe the other, depending on market moves. The classic examples are:

- **Interest rate swaps**: Party A pays fixed, Party B pays floating. If rates fall, the fixed-rate payer (A) owes money. If rates rise, the floating-rate payer (B) owes money.
- **Currency forwards**: One party sells EUR, the other sells USD. Whichever currency strengthens determines who is in-the-money.
- **Options and derivatives**: The value changes daily with the underlying asset; who is "winning" flips as the market moves.

Counterparty risk is the risk that the party who is currently losing (out-of-the-money) refuses to settle when the contract matures, or that they default before settlement. Unlike a loan, there is no pre-set amount at risk; the exposure is the current **replacement value** of the contract.

Imagine a bank enters a $100 million notional interest rate swap with a pension fund. If rates fall and the bank owes the pension fund $2 million, the bank's counterparty risk on that contract is approximately $2 million—the amount the bank would have to pay a new counterparty to replace the economic benefit it would lose if the pension fund defaulted. If rates rise and the pension fund owes the bank, the bank's counterparty risk drops to near zero (the pension fund has incentive to pay) and the pension fund's counterparty risk rises.

## The mechanics of counterparty exposure

When a derivatives contract begins, it has little or no market value (absent an upfront fee). As time passes and markets move, the contract accrues value to one party and loss to the other. That accrued value is the **current exposure** (or replacement value).

A swap is usually settled at maturity or upon early termination. If the counterparty is healthy, they pay. If they default:

- The non-defaulting party loses the present value of all future payments it would have received.
- If the contract is in-the-money for the non-defaulting party, that loss can be substantial.

This is fundamentally different from a loan. A lender making a $100 million loan faces a $100 million credit risk immediately. A derivatives counterparty's risk grows or shrinks with market prices; it may be $0 today and $10 million tomorrow if rates move.

## Mark-to-market exposure and replacement cost

Banks measure counterparty risk as the sum of:
1. **Current market value** of the contract (amount owed today if fair value applies)
2. **Potential future exposure** (PFE): a statistical estimate of how much larger the exposure could grow over the remaining life

PFE is crucial because it captures the danger that a counterparty will default *after* losing money on the trade. For a long-dated interest rate swap, PFE can be 3–5 times the current exposure, because rates could move further against the counterparty, and the counterparty could fail before the swap matures.

## Netting and central counterparties

To reduce counterparty risk, derivatives traders use **netting**: if a bank has multiple trades with the same counterparty, it can offset trades in opposite directions. Instead of paying out $10 million on swap A and receiving $7 million on swap B, the bank nets to a single $3 million payment. This cuts counterparty exposure dramatically.

**Central counterparties (CCPs)** (like the Depository Trust & Clearing Corporation) stand between traders. Instead of owing each other directly, each trader owes the CCP. This eliminates bilateral counterparty risk (if one trader defaults, the CCP absorbs the loss and breaks even using collateral and insurance funds). Central clearing is now mandated for standardized derivatives in most jurisdictions, sharply reducing systemic counterparty risk.

## Collateral and credit support

Both credit risk and counterparty risk can be mitigated with collateral. A lender may require a mortgage (the borrower pledges the house). Derivatives counterparties may post **variation margin**—cash or securities that move daily with the contract's fair value. If a swap is worth +$5 million to one party and −$5 million to the other, the losing party posts $5 million of collateral. As the contract value changes, collateral is transferred.

This is very different from loan collateral, which sits in place for the life of the loan. Derivatives collateral is live and dynamic.

## Historical distinction: the Lehman Brothers case

In 2008, Lehman Brothers filed for bankruptcy. As a derivatives dealer, Lehman had thousands of outstanding swaps, options, and forwards. When Lehman defaulted:

- **Credit creditors** (bond holders and bank lenders): suffered as unsecured claims were paid cents on the dollar from an estate.
- **Counterparties**: faced a different problem. The contracts were immediately worthless if they were in-the-money (Lehman owed them money and wasn't paying). Many counterparties rushed to break Lehman contracts under default clauses, close out positions, and lock in their recoveries. The simultaneous liquidation of trillions of dollars of derivatives contracts created systemic stress.

This illustrated why counterparty risk was given regulatory and accounting prominence: it is volatile, potentially bilateral, and its failure mode (contagion across the derivative ecosystem) was distinct from traditional credit risk.

## Accounting and regulatory treatment

Under [IFRS 9](/international-financial-reporting-standards/) and [ASC 805](/asc-606/) standards, banks measure counterparty credit risk and impair derivatives assets if the counterparty's credit quality deteriorates. **Credit valuation adjustment (CVA)** accounts for the cost of this risk; banks set aside capital for it under [Basel III](/capital-adequacy/) rules (specifically, CVA risk capital).

Loan credit risk is more straightforward: [expected credit loss](/loss-aversion/) is estimated using historical default rates and recovery rates, and an [allowance for credit losses](/loss-aversion/) is reserved.

## See also

<div class="wiki-seealso">

### Closely related

- [Credit Risk](/credit-risk/) — the traditional one-directional borrower default risk
- [Derivatives Hedging](/derivatives-hedging/) — how counterparty risk is managed
- [Credit Spread](/credit-spread/) — the yield premium reflecting credit risk
- [Option](/option/) — derivatives contracts where counterparty risk accrues
- [Swap](/swap/) — the classic bilateral derivatives contract

### Wider context

- [Systemic Risk](/systemic-risk/) — how counterparty defaults can cascade across markets
- [Central Bank](/central-bank/) — role in managing systemic counterparty risk (swap lines, liquidity)
- [Capital Adequacy](/capital-adequacy/) — regulatory framework for holding capital against counterparty risk
- [Default Rate](/default-rate/) — historical probability of counterparty failure
- [Risk Weighted Assets](/risk-weighted-assets/) — how counterparty risk is weighted in capital calculations

</div>
