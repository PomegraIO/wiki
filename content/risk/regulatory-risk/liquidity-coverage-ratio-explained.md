---
title: "Liquidity Coverage Ratio Explained"
description: "The LCR measures whether a bank can survive a 30-day funding crisis. Learn what counts as a high-quality liquid asset and how regulators set the threshold."
keywords:
  - liquidity coverage ratio
  - LCR ratio
  - high-quality liquid assets
  - bank liquidity stress
  - 30-day liquidity crisis
  - regulatory liquidity requirement
---

*The **liquidity coverage ratio** (LCR) is a regulatory requirement that forces banks to hold enough cash and easily-sold securities to survive a severe 30-day funding crisis without borrowing or asset fire sales. It answers a simple question: if all your funding sources dried up tomorrow, could you pay withdrawals for a month? Regulators set a minimum LCR of 100%—meaning liquid assets must equal or exceed expected outflows over 30 days. This ratio prevents the liquidity trap that killed Lehman Brothers: a solvent bank with good assets but no cash when creditors panicked.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Liquidity Coverage Ratio — key facts</div>

<img src="/svg/risk.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">A bank's cash and liquid securities must exceed its 30-day funding outflows.</div>

|   |   |
|---|---|
| **Regulatory minimum** | 100% |
| **Current requirement** | Full phase-in as of 2019 |
| **Horizon** | 30-day crisis window |
| **Numerator** | High-quality liquid assets (HQLA) |
| **Denominator** | Net cash outflows (stressed scenario) |
| **Key regulators** | Federal Reserve, Basel Committee, EBA |
| **Consequence of failure** | Mandatory funding plan, dividend restriction |

</aside>

## The 30-day crisis window

The LCR rests on a specific regulatory assumption: a bank will face a "severe idiosyncratic and market-wide stress event" lasting at least 30 days. During this window, bad things happen in combination:

- Deposits flee faster than normal as customers lose confidence.
- [Counterparties](/counterparty-risk/) recall short-term lending, refusing to roll over [repurchase agreements](/repurchase-agreement/) or other short-term loans.
- The bank cannot easily access capital markets to raise new funds.
- Asset prices fall, making collateral less valuable.

The 30-day horizon was chosen because that is roughly the time it takes a solvent bank to arrange emergency funding from a central bank, sell assets, or arrange a rescue. Lehman Brothers collapsed in days because it had no liquid cash and no access to emergency loans. If Lehman had been forced to hold three weeks' worth of outflows in cash or Treasuries, it might have survived long enough for a deal.

The LCR does not prevent all runs. It prevents the *fastest* ones. A bank can still suffer a slow, months-long drain of deposits if fundamentals deteriorate. But 30 days buys time.

## Calculating the LCR: numerator (high-quality liquid assets)

The numerator of the LCR is the stock of **high-quality liquid assets** (HQLA) a bank holds. Not all assets count equally. Regulators categorize them into tiers:

**Level 1 assets (no haircut):**
- Cash and central-bank reserves.
- [Treasury bonds](/treasury-bond/) and [Treasury bills](/treasury-bill/) of any maturity.
- These are counted at full value because they are always saleable and creditworthy.

**Level 2A assets (15% haircut):**
- Government debt of highly-rated countries (not including the bank's home country).
- Bonds issued by major development banks ([World Bank](/federal-reserve/), [European Central Bank](/european-central-bank/)).
- Investment-grade [corporate bonds](/corporate-bond/) issued by banks' central banks.
- These are subtracted by 15%—so a $100 bond counts as $85—to reflect that they may take time to sell or prices may have fallen slightly.

**Level 2B assets (25–50% haircut):**
- Lower-rated government debt and corporate bonds (below investment-grade but not junk).
- Mortgage-backed securities and other [securitizations](/securitization/).
- Listed equities meeting strict criteria (highly liquid, low volatility).
- These carry steeper haircuts because they are less liquid or more volatile.

Regulators also cap how much of each tier a bank can use. A typical cap: no more than 40% of total HQLA can be Level 2B, and no more than 50% Level 2A. This forces banks to hold a core of the safest assets (cash and Treasuries) rather than trying to game the ratio with corporate bonds.

A bank computing its LCR subtracts haircuts and category caps from its asset stack, arriving at a total unencumbered HQLA available to cover outflows.

## Calculating the LCR: denominator (net cash outflows)

The denominator is trickier: it represents the bank's projected *net* cash outflows over the 30-day stress period.

**Outflows (cash the bank must pay out):**
- [Deposit](/accounts-payable/) withdrawals. Small deposits (under deposit-insurance caps) are assumed to flow out at a lower rate because they are insured; uninsured deposits flow out at a much higher rate. During a panic, uninsured depositors withdraw first. Typical assumptions: 5–10% of insured deposits leave; 25–75% of uninsured deposits leave.
- Debt maturing and not rolling over. [Bonds](/bond/) due in the next 30 days are assumed to mature, forcing repayment. Short-term [repurchase agreements](/repurchase-agreement/) and [LIBOR](/libor/)-based loans are assumed to be called.
- Collateral calls. If the bank has pledged securities as collateral and mark-to-market falls, it must post additional collateral.
- Customer drawdowns on committed credit lines.

**Inflows (cash the bank receives):**
- Principal and [coupon payments](/coupon-payment/) on securities maturing or paying interest.
- Customer loan repayments.
- Revenues from operations.

Only a fraction of inflows count toward the LCR—again, to be conservative. Typically, 50–100% of mature principal is counted; interest and loan repayments are capped at a percentage of total outflows.

**Net outflows** = total outflows minus (conservative estimate of) inflows. A bank with $100 billion in outflows and $40 billion in inflows has net outflows of $60 billion.

## The LCR formula and minimum requirement

The LCR is simply:

**LCR = HQLA / Net 30-day cash outflows**

A bank must maintain an LCR of at least 100%, meaning HQLA ≥ net outflows. An LCR of 100% means the bank can cover exactly one month of stress. An LCR of 150% means it can cover 1.5 months. Systemically important banks often hold LCRs of 120–150% voluntarily or at regulator request, because it signals confidence and avoids the optics of just barely meeting the minimum.

## Stress-test outflow assumptions

Regulators do not use the bank's historical deposit behavior to set outflow rates. They use a *stressed* scenario calibrated to crisis conditions observed in 2008 or other historical episodes. For example:

- Uninsured wholesale deposits: 75% runoff (i.e., 75% withdraw in 30 days). These are hot money that flees at first sign of trouble.
- Uninsured corporate deposits: 40–50% runoff.
- Secured funding (repurchase agreements): 25–50% runoff depending on collateral quality.
- Customer loan drawdowns: 10% of committed lines.

These are deliberately higher than peacetime behavior. A bank with 10% deposit runoff in normal times may face 50% runoff in a crisis. The LCR forces banks to plan for the crisis scenario, not the normal case.

## Why the 30-day horizon complements longer-term metrics

The LCR is a short-term buffer. It works in tandem with the [Net Stable Funding Ratio (NSFR)](/net-stable-funding-ratio-how-it-works/), which ensures banks can survive a one-year funding drought. The NSFR is stricter in some ways (it requires more long-term stable funding) but allows banks to substitute some less-liquid assets. The LCR is unforgiving: if you have not got the cash or near-cash, you fail. Together, they create a two-front defense: immediate liquidity (LCR) and structural funding stability (NSFR).

## Practical impact and gaming

Since the LCR became mandatory in 2015, banks have restructured their balance sheets. They now hold much larger reserves in central-bank accounts, Treasuries, and high-grade securities. The average LCR for large US banks is well above 100%—often 130–150%. This is expensive (cash earns little yield) but necessary.

Banks try to optimize within regulatory boundaries. They may structure deposits to lower runoff assumptions (e.g., tiering deposits by size or term), or they may hedge collateral risk to avoid margin calls. They also shop between jurisdictions; some countries allow higher haircuts on certain assets, making that jurisdiction's LCR easier to pass. But the spirit of the rule—hold enough liquid cash to survive a 30-day panic—has driven a real increase in bank liquidity worldwide.

## See also

<div class="wiki-seealso">

### Closely related

- [Net Stable Funding Ratio: How It Works](/net-stable-funding-ratio-how-it-works/) — longer-term (one-year) funding resilience requirement
- [Stress Testing: Regulatory Requirements Explained](/stress-testing-bank-regulatory-requirements/) — the broader framework testing capital and liquidity together
- [Systemic Risk Buffer Requirement](/systemic-risk-buffer-requirement/) — extra capital for systemically important banks
- [Counterparty Risk](/counterparty-risk/) — risk that the bank's creditors fail
- [Repurchase Agreement](/repurchase-agreement/) — short-term funding markets vulnerable to stress
- [Treasury Bill](/treasury-bill/) — the safest, most liquid asset banks hold

### Wider context

- [Federal Reserve](/federal-reserve/) — primary regulator and liquidity backstop
- [Deposit Insurance](/federal-deposit-insurance-corporation/) — insurance that affects deposit runoff assumptions
- [Securitization](/securitization/) — creates some assets counting toward HQLA
- Financial Crisis — why 30-day stress window was chosen
- [Basel III](/capital-adequacy/) — international framework including LCR requirements

</div>
