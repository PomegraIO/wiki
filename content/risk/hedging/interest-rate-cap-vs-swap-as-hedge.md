---
title: "Interest Rate Cap vs Swap as a Hedge"
description: "Compare interest rate caps and swaps for hedging floating-rate debt: cost, flexibility, maximum payout, accounting, and when each hedge fits a borrower's risk profile."
keywords:
  - interest rate cap vs swap hedge floating rate debt
  - interest rate cap pricing
  - interest rate swap vs cap
  - floating rate borrowing hedge
  - interest rate risk management
image: /svg/risk.svg
---

*An **interest rate cap** sets a ceiling on floating-rate borrowing costs; everything above it is paid by the cap seller. A **swap** fixes the rate entirely. Caps preserve upside if rates fall; swaps eliminate guessing. Choosing between them depends on cost, [interest-rate](/interest-rate/) conviction, and how much certainty a borrower needs.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Cap vs Swap as a Hedge — key facts</div>

<img src="/svg/risk.svg" alt="An abstract editorial mark for risk management and hedging." />

<div class="wiki-infobox-caption">Both limit upside interest-rate risk; cap keeps downside exposure, swap eliminates it.</div>

|   |   |
|---|---|
| **Cap** | Borrower pays if rates rise above strike; benefits if rates fall |
| **Swap** | Borrower pays fixed rate; no benefit if rates fall |
| **Cap cost** | 0.20%–1.50% of notional upfront, depending on strike and term |
| **Swap cost** | Usually zero upfront; embedded in fixed rate vs. forward curve |
| **Best for cap** | Short horizons; strong conviction rates will stay flat or fall |
| **Best for swap** | Certainty needed; budgeting; longer terms |
| **Flexibility** | Cap can be unwound; swap unwind costs reflect current rates |

</aside>

## Floating-Rate Debt and Why It Must Be Hedged

A company borrows $100 million at SOFR (Secured Overnight Financing Rate) + 2%. SOFR fluctuates daily with the [federal-funds-rate](/federal-funds-rate/) and economic conditions. If SOFR rises from 4% to 6%, the borrower's interest cost jumps from 6% to 8% annually—$2 million per year on $100 million notional.

For a [balance-sheet](/balance-sheet/) with thin [interest-coverage-ratio](/interest-coverage-ratio/), that move could threaten [earnings-per-share](/earnings-per-share/) or covenant compliance. For a project finance deal with fixed revenues, it cuts into [net-operating-income](/net-operating-income/).

To manage this [interest-rate-risk](/interest-rate-risk/), borrowers hedge using either a **cap** or a **swap**—two fundamentally different tools.

## How a Cap Works

An **interest rate cap** is a [call-option](/call-option/) on interest rates. The borrower and a [counterparty](/counterparty-risk/) agree on a **strike rate**, say 5%. The borrower pays an **option premium** upfront (typically 0.20%–1.50% of notional). In exchange:

- If SOFR + spread rises above 5%, the cap seller reimburses the excess.
- If SOFR + spread stays at or below 5%, the borrower pays the full rate—the cap is out-of-the-money and worthless.

**Example:** Borrower has $100M debt at SOFR + 2%, strike cap at 5%.

- SOFR = 3%: Borrower pays 5% (3% + 2%). Cap is worthless. Cost: $5M annually.
- SOFR = 4%: Borrower pays 6% (4% + 2%). Cap is worthless. Cost: $6M annually.
- SOFR = 5%: Borrower would pay 7%, but cap pays excess. Borrower pays 5%. Cost: $5M annually. Cap seller pays $2M.
- SOFR = 7%: Borrower would pay 9%, but cap caps at 5%. Cost: $5M annually. Cap seller pays $4M.

The cap preserves the borrower's upside. If rates fall to 2%, the borrower pays only 4% (2% + 2% spread) and loses the premium paid for the cap. But that's the cost of optionality.

## How a Swap Works

An **interest rate swap** is a [swap](/swap/): the borrower and counterparty exchange cash flows. The borrower agrees to pay a **fixed rate**, say 5.50%, to the counterparty. The counterparty pays the borrower SOFR + 2% (the borrower's floating rate on the loan).

There is no upfront premium; instead, the fixed rate is set so that the two legs have equal present-value at inception.

**Example:** Borrower has $100M debt at SOFR + 2%, swaps into 5.50% fixed.

- SOFR = 3%: Borrower pays 5% on loan, receives 5% from swap. Net: 5.50% fixed. Cost: $5.5M annually.
- SOFR = 4%: Borrower pays 6% on loan, receives 6% from swap. Net: 5.50% fixed. Cost: $5.5M annually.
- SOFR = 7%: Borrower pays 9% on loan, receives 9% from swap. Net: 5.50% fixed. Cost: $5.5M annually.

The borrower is completely insulated from rate moves. The downside is zero recovery if rates fall; the borrower still pays 5.50% while floating rates would have been only 4%.

## Cost Structures and Break-Evens

**Upfront costs:**

A cap has an explicit **option premium** paid upfront, usually 0.20%–1.50% of the loan amount. A 1% premium on $100M is $1M cash out the door.

A swap has no upfront cash, but the fixed rate is typically 25–100 basis points *above* the [forward-guidance](/forward-guidance/) curve, embedding the dealer's profit. Over the loan life, this is usually equivalent to an upfront premium but spread over time.

**Effective cost under different rate scenarios:**

- **Rates stay flat:** The cap preserves cash; the swap is a cost (fixed rate higher than floating would have been).
- **Rates fall 200 bps:** The cap costs the premium + lost savings on the loan; the swap costs the premium spread.
- **Rates rise 200 bps:** The cap limits the rise; the swap is indifferent.

The "break-even" rate—the level at which the cap and swap cost the same—depends on the strike, the premium, the fixed rate, and the [holding-period](/holding-period/).

## Accounting and Financial Reporting

Historically, caps and swaps received different [asc-606](/asc-606/) treatment under hedge accounting rules, affecting [earnings-per-share](/earnings-per-share/) and [balance-sheet](/balance-sheet/) volatility.

Under current [generally-accepted-accounting-principles](/generally-accepted-accounting-principles/), both *can* qualify for **cash-flow hedge** accounting if properly documented. This means the gain or loss on the hedge is deferred in [accumulated-depreciation](/accumulated-depreciation/) (Other Comprehensive Income) rather than flowing through [income-statement](/income-statement/) earnings immediately.

However, **execution and timing matter.** A cap that requires periodic settlements (if rates spike) might require accrual accounting, adding earnings volatility. A swap's back-to-back nature (borrower pays floating, counterparty pays fixed) makes it easier to document as a clean hedge.

Tax treatment can also differ. Consult tax and accounting advisors on jurisdiction-specific implications.

## Scenarios Favoring a Cap

**Short time horizon (1–2 years):** If the loan or project is short-lived, the upfront premium is a small percentage of total interest cost. The optionality (capped upside, preserved downside) is valuable for visibility.

**Conviction that rates will fall or stay flat:** If management believes the [federal-reserve](/federal-reserve/) will cut rates within a few years, a cap lets the borrower benefit from that outcome. The premium is insurance, not a permanent cost.

**Volatility preference:** Some CFOs prefer the "known maximum cost" of a cap (fixed ceiling) to the black-and-white certainty of a swap. A cap feels more like disaster insurance.

**Partial hedge:** A borrower can buy a cap on part of the debt (say, 50%) and leave the rest floating. This blends optionality with downside protection at lower cost than capping everything.

## Scenarios Favoring a Swap

**Long duration (5+ years):** For a 10-year term-loan, the upfront premium on a cap (1%+) is meaningful. A swap, which has no upfront cost, is more economical over a long horizon.

**Certainty and budgeting:** If the company must forecast [interest-coverage-ratio](/interest-coverage-ratio/) for bond indentures, [credit-rating](/credit-rating/) agencies, or shareholder commitments, a fixed swap rate is easier to plan around than a capped variable.

**Accounting simplicity:** Swaps are easier to qualify for hedge accounting and often receive less scrutiny from auditors.

**Conviction is low:** If management is uncertain whether rates will rise or fall, and simply wants to eliminate [interest-rate-risk](/interest-rate-risk/) to focus on business risk, a swap forces a clear decision and removes the asymmetry.

## Combination Strategies

Some borrowers use **collar** structures: they buy a cap (protecting against rate rises) and sell a cap at a lower strike (reducing the net upfront cost but capping the benefit if rates fall sharply).

Others **ladder** hedges: swap half the debt, cap a quarter, and leave a quarter floating. This diversifies the bet and reduces the cost of any single hedge.

## Counterparty Risk and Collateral

Both caps and swaps create [counterparty-risk](/counterparty-risk/). If SOFR spikes and a cap is deep in-the-money, the cap seller owes the borrower money. If the cap seller defaults (or faces [credit-rating](/credit-rating/) downgrade), the borrower loses the hedge precisely when it's most needed.

Swaps also carry collateral requirements. If [interest-rate](/interest-rate/) moves favor the borrower (SOFR falls), the borrower may have to post collateral with the counterparty under a Credit Support Annex.

Large corporates typically mitigate this by dealing with [bank-of-america](/bank-of-america/), [jpmorgan-chase](/jpmorgan-chase/), [goldman-sachs](/goldman-sachs/), or [morgan-stanley](/morgan-stanley/)—counterparties with investment-grade ratings and deep derivative markets.

## Market Conditions and Timing

The **price** of a cap (option premium) varies with market [implied-volatility](/implied-volatility/). When rate volatility is expected to be high, caps are expensive. When volatility is low, they are cheap.

A borrower floating-rate debt during a low-volatility regime should lock in a cheap cap. One who delays in a high-volatility market will pay more.

Similarly, the fixed rate on a swap reflects the forward curve. If the market expects rates to rise, the fixed swap rate is high. If rates are expected to fall or flatten, the fixed rate is lower.

Timing the hedge is part of the cost-benefit analysis, though it requires judgment or conviction about [interest-rate](/interest-rate/) direction.

## See also

<div class="wiki-seealso">

### Closely related

- [Interest Rate Risk](/interest-rate-risk/) — Exposure to changes in borrowing or lending rates
- [Forward Contract](/forward-contract/) — Agreement to lock in future exchange or interest rates
- [Call Option](/call-option/) — Right but not obligation to buy or exercise at a strike
- [Swap](/swap/) — Exchange of cash flows in different currencies or at different rates
- [Interest Rate Swap](/interest-rate-swap/) — Exchange of fixed and floating rate payments

### Wider context

- [Federal Reserve](/federal-reserve/) — Central bank setting the federal funds rate
- [Counterparty Risk](/counterparty-risk/) — Risk of default by the other party to a contract
- [Credit Rating](/credit-rating/) — Assessment of default risk
- [Basis Risk](/basis-risk/) — Risk that a hedge does not perfectly offset the underlying exposure
- [Debt Financing](/debt-financing/) — Use of borrowed money to fund operations or investment

</div>
