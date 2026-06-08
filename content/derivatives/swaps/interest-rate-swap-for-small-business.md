---
title: "Interest Rate Swaps for Small Business Borrowers"
description: "How small businesses use interest rate swaps to convert floating-rate loans to fixed rates, including minimum thresholds and termination costs."
keywords:
  - interest rate swap
  - small business loan
  - floating rate
  - fixed rate
  - interest rate hedge
image: "/svg/derivatives.svg"
---

*An **interest rate swap** for a small business converts a floating-rate loan into a fixed-rate obligation without refinancing. The business agrees to pay a fixed rate to a swap counterparty (typically a bank) while receiving floating-rate payments in return. This locks in borrowing costs upfront, protecting against [interest rate](/interest-rate/) increases—but introduces the risk that early termination will trigger a costly settlement payment.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Interest Rate Swaps for Small Business — Key Facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">A tool to hedge rate risk, but with hidden exit costs and bank-imposed thresholds.</div>

|   |   |
|---|---|
| **Primary use** | Convert floating-rate bank loan to fixed rate without refinancing |
| **Typical borrower** | Small to mid-sized business (revenue $10M–$500M+) with 3–7 year floating loan |
| **Notional minimum** | $5–25 million (varies by bank; larger minimums reduce bank costs) |
| **Upfront cost** | Usually zero; swap is negotiated as part of loan package |
| **Counterparty** | Typically the lead bank on the loan |
| **Accounting** | Requires [hedge accounting](/derivatives-hedging/) treatment under accounting standards (GAAP/IFRS) |
| **Early exit cost** | Substantial; based on mark-to-market value of swap; often $100K–$500K+ |
| **Typical maturity** | Matches loan maturity (3–7 years); can be shorter |

</aside>

## The Floating-Rate Problem

Most small business loans begin as floating-rate advances tied to a benchmark: the bank's prime rate, SOFR (Secured Overnight Financing Rate), or the bank's cost of funds plus a spread. If the company borrows $10 million at "prime plus 2.5%," the monthly interest payment fluctuates as prime rises and falls with [Federal Reserve](/federal-reserve/) policy.

This is efficient when rates are expected to stay flat or fall—the business benefits from lower payments. But when the [yield curve](/yield-curve/) suggests [interest rates](/interest-rate/) will climb, a small business faces a squeeze: rising rates compress margins, require larger cash reserves for debt service, and can blow up a fixed budget. A manufacturer with a 3% net margin cannot tolerate a 200-basis-point rate jump.

Rather than refinance into a fixed-rate loan (which is costly—appraisals, closing costs, a new origination fee—and may trigger rate-and-term restrictions), the business can enter an interest rate swap. The swap synthetically converts the loan to fixed rate without a formal refinancing.

## How the Swap Works: A Worked Example

A small business has a $15 million floating-rate loan at SOFR + 2.5%, with SOFR currently at 5.0%, giving an all-in rate of 7.5%.

The business enters a receive-floating, pay-fixed swap with the bank:
- **Notional:** $15 million (matches the loan)
- **Swap fixed rate:** 5.75% (negotiated with the bank)
- **Floating payment:** SOFR + 0% (the business receives SOFR from the swap; offset against SOFR on the loan)
- **Maturity:** 5 years (matches the loan)

**How the cash flows work:**

On the loan, the business pays SOFR + 2.5%. On the swap:
- The swap counterparty pays the business SOFR (the "floating" leg).
- The business pays the counterparty the fixed rate (5.75%).

**Net result:**

The SOFR payments offset: the business receives SOFR from the swap and pays SOFR to the lender, netting to zero. The business is left paying 5.75% (swap fixed) + 2.5% (loan spread) = **8.25% all-in, fixed.**

If SOFR rises to 6.5%, the business still pays 8.25%—no change. If SOFR falls to 3.5%, the business still pays 8.25%. The rate is locked in.

| Scenario | SOFR on Loan | Loan Rate | Swap Nets SOFR | Effective Fixed Rate |
|----------|--------------|-----------|-----------------|---------------------|
| SOFR = 5.0% | 7.5% | + Swap fixed 5.75% = | 8.25% |
| SOFR = 6.5% | 9.0% | - Swap SOFR + 5.75% = | 8.25% |
| SOFR = 3.5% | 6.0% | - Swap SOFR + 5.75% = | 8.25% |

## Minimum Notional Thresholds

Most banks will not enter a swap for a small notional—the administrative and hedging costs are not worth it. Typical minimums:

- **$5–10 million** for borrowers with multi-million-dollar loan portfolios or strong banking relationships
- **$15–25 million** for smaller borrowers or one-off swaps
- **$50 million+** for a truly commoditized rate (the bank can lay off the hedge easily, reducing its cost)

A business with a $2 million floating loan will have difficulty finding a bank willing to swap it. The bank would have to hedge the rate exposure, and the hedging costs (or potential hedging losses) exceed the margin the bank can earn on the swap.

Businesses seeking swaps on smaller notionals should:
1. Combine multiple loans into a single swap (if the lending bank manages all loans)
2. Approach larger, more sophisticated banks (regional and national banks are more willing than community banks)
3. Consider refinancing instead if the notional is too small

## The Hidden Termination Cost

The most dangerous aspect of a small business interest rate swap is the early exit cost. If the business wants or needs to terminate the swap before maturity, the termination cost is the swap's current mark-to-market value.

Here's the risk: If rates fall after the swap is entered, the fixed rate the business locked in (say, 5.75%) becomes expensive relative to market rates (now 4.0%). The swap has a negative value to the business—the counterparty owes the business nothing; instead, the business owes the counterparty the present value of the unfavorable rate differential.

**Concrete example:**

A business entered a $15 million, 5-year swap at 5.75% fixed. After two years, rates have fallen, and a comparable 3-year swap (the remaining term) now trades at 4.0% fixed. The business's 5.75% obligation is now 175 basis points above market. To exit, the business must pay the counterparty the present value of that 175 bps × $15 million over 3 years, perhaps $400,000–$600,000.

This termination fee is a real cost that surprises many small business owners. It surfaces when:
- The business is acquired and the buyer refinances
- The business grows and refinances early
- The business faces distress and wants to free up cash
- The business wants to refinance at a lower rate because market rates have declined

A clause in many loan agreements allows the lender to unwind a swap if the borrower prepays the loan—but the business still pays the termination fee (it doesn't disappear). Some lenders bundle the swap termination fee into the loan prepayment penalty, obscuring the true cost.

## Accounting and Reporting

Under [GAAP](/generally-accepted-accounting-principles/) and [IFRS](/international-financial-reporting-standards/), a swap qualifies for hedge accounting if properly documented and if the business designates it as a hedge of the underlying loan. With hedge accounting, the swap's mark-to-market gains and losses are recorded in other comprehensive income (OCI), not flowing directly to earnings. This smooths income statement volatility.

Without hedge accounting, the swap's mark-to-market value flows directly to earnings each quarter—creating earnings volatility unrelated to the business's operations. For small businesses, hedge accounting documentation can be a burden, and some simply accept the earnings volatility.

The swap must also be recorded on the balance sheet as an asset or liability (depending on whether it's in-the-money or out-of-the-money). This is a non-cash item but can affect balance sheet ratios—particularly if the swap is significantly out-of-the-money and the business needs to show strong balance sheet metrics to lenders or investors.

## When Swaps Make Sense

A small business interest rate swap is most valuable when:
- The business has a 3–7 year floating-rate loan and wants to lock in a rate
- The notional is $15 million or larger (to meet bank minimums)
- The business does not expect to need to refinance or pay down the loan early
- The business's earnings are sensitive to interest rate changes (thin margins)
- The business is willing to bear the termination cost if circumstances change

Conversely, swaps are less useful if:
- The loan is small ($5 million or less) and no bank will price a competitive swap
- Early payoff is likely (especially if driven by acquisition or distressed sale)
- The interest rate environment is highly uncertain, and the business wants optionality

In those cases, refinancing into fixed-rate debt or accepting floating-rate risk may be cheaper in total economic cost.

## See also

<div class="wiki-seealso">

### Closely related

- [Interest rate swap](/interest-rate-swap-for-small-business/) — note: avoid self-link
- [Swap](/swap/) — the general mechanics of interest-rate and currency swaps
- [Interest rate risk](/interest-rate-risk/) — the underlying risk the swap hedges
- [Derivatives hedging](/derivatives-hedging/) — how companies use derivatives to manage risk
- [Interest rate](/interest-rate/) — the underlying benchmark of the swap

### Wider context

- [Federal Reserve](/federal-reserve/) — sets policy that drives the benchmark rates
- [Yield curve](/yield-curve/) — shows market expectations of future rates
- [Credit spread](/credit-spread/) — the bank's margin above the benchmark rate
- [Cost of debt](/cost-of-debt/) — the overall borrowing cost the swap affects
- [Fixed-rate mortgage](/fixed-rate-mortgage-personal/) — a simpler alternative for long-term borrowing certainty

</div>
