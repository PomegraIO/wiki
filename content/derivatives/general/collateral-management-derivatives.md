---
title: "Collateral Management in Derivatives"
description: "The practices of posting, substituting, and managing initial and variation margin to secure bilateral and cleared derivatives exposures."
keywords:
  - variation margin
  - initial margin
  - collateral posting
  - mark-to-market
  - rehypothecation
  - credit support
image: "/svg/derivatives.svg"
---

*Derivatives expose both parties to credit risk—if one defaults, the other loses the mark-to-market value of the trade. **Collateral management** is the practice of the losing party posting cash or securities (margin) to back its exposure, reducing the winner's credit risk. Post-2008, this has become mandatory, daily, and highly standardized, turning derivatives collateral into a multi-trillion-dollar operational machine.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Collateral Management in Derivatives — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives and risk." />

<div class="wiki-infobox-caption">Margin is collateral that flows daily as exposures change.</div>

|   |   |
|---|---|
| **Two forms** | **Initial margin**: up-front, fixed per trade. **Variation margin**: daily adjustment for gains/losses |
| **Calculation** | Initial margin uses standard models (SIMM). Variation margin equals mark-to-market change |
| **Posting frequency** | Variation margin daily; initial margin at trade inception and after large moves |
| **Collateral types** | Cash, government bonds, investment-grade corporate bonds, sometimes equities |
| **Haircuts** | 0–10% on cash and bonds; higher for illiquid or volatile assets |
| **Rehypothecation** | Common among dealers; allows leverage but adds counterparty risk |

</aside>

## Why collateral is essential: credit exposure in derivatives

A derivatives trade creates asymmetric credit risk. Suppose Bank A and Bank B enter a five-year interest-rate swap: A receives a fixed 3% rate, B receives floating SOFR. On day one, the swap is at par—no one owes the other anything (assuming SOFR equals 3%). But SOFR rises to 4% by month two. The swap is now worth money to A: A will receive fixed 3% while floating has risen to 4%, a gain of roughly 1% × 5 years = 5% of notional. If the swap is on $100 million notional, A's gain is worth $5 million, making B's loss also $5 million.

Without collateral, B could simply default and walk away, leaving A with a $5 million loss and an unsecured claim in B's bankruptcy. To prevent this, B posts collateral—typically $5 million in cash or government securities—held by a custodian or transfer agent in a segregated account. If B later defaults, A can seize the collateral to cover its loss.

This is the essence of collateral in derivatives: it transforms credit risk into collateral risk, which is more manageable because the winner can liquidate the collateral quickly.

## Initial margin: the up-front buffer

**Initial margin** (IM) is collateral posted at trade initiation to cover potential losses due to adverse price moves over the time it takes to exit the trade (typically 2–5 business days). It is calculated as a percentile of the loss distribution, meaning it is designed to cover the worst-case move that occurs with 99% probability.

The calculation is complex and depends on the derivative type and its volatility. For interest-rate swaps, initial margin is typically 1–3% of notional (a $100 million swap requires $1–3 million). For longer-dated or more exotic contracts, it can exceed 5–10%. Currency forwards and commodity futures often require higher IM.

**SIMM (Standard Initial Margin Model)**, endorsed by the Basel Committee and IOSCO, is the agreed global standard. It breaks down the derivative into risk factors (interest rates, FX rates, credit spreads, etc.), measures the [volatility](/historical-volatility/) of each, and calculates the loss if market moves by a given percentile in adverse directions. The result is a single IM number per trade.

Initial margin does not move (in principle) unless market conditions change dramatically or the counterparty's credit rating falls. If Bank A posts $1 million IM for a swap that stays at par, A holds that $1 million throughout the trade's life. At maturity or early termination, it is returned.

## Variation margin: the daily accounting

**Variation margin** (VM) is the real-time collateral adjustment. Every day, the mark-to-market value of the derivatives portfolio between two counterparties is recalculated. If the portfolio moved against you (you lost money), you post additional collateral equal to the loss. If it moved in your favour (you gained money), you receive collateral back.

Most institutional derivatives now settle VM daily. If Bank A's portfolio with Bank B gains $2 million in a day, B posts $2 million to A the next morning. The day after, if A loses $500,000, A posts $500,000 back to B. This daily settlement mimics the idea of mark-to-market accounting: each party books its current gain or loss and backs it with collateral, so no one carries large unsecured exposures overnight.

For cleared derivatives (those going through a central counterparty), VM is mandatory and settled in cash only. For bilateral (non-cleared) derivatives, VM settlement is now also required by regulation but happens through more varied mechanisms: wire transfers, triparty repo arrangements, or central securities depositories.

## Collateral eligibility and haircuts

Not all assets are equally good as collateral. Cash is best: it is immediately liquid and cannot fall in value. Government securities (Treasury bills, bonds) are nearly as good. Investment-grade corporate bonds are acceptable but riskier. Equities, commodities, and illiquid or low-grade bonds are rarely accepted.

Each collateral type is assigned a **haircut**—a discount reflecting its illiquidity and volatility:
- **Cash**: 0% haircut (1 dollar of cash = 1 dollar of margin)
- **US Treasury bonds**: 0–1% haircut
- **Investment-grade corporate bonds**: 2–5% haircut
- **High-yield bonds**: 5–10% haircut (if accepted at all)
- **Equities**: 10–20% haircut (rarely accepted)

A 5% haircut means you must post $105 in corporate bonds to cover $100 of margin requirement. The haircut cushions the collateral receiver against the risk that the collateral asset will fall in value before it can be sold in a default.

## Rehypothecation: leverage and risk

Banks routinely rehypothecate collateral they receive—that is, they use it as collateral in other transactions to raise cash or enter new trades. This amplifies leverage throughout the financial system. If Bank A receives $100 million in cash as collateral from Bank B, A can post that $100 million to its prime broker, borrow against it, enter new trades, and multiply its balance sheet. This is normal practice and profitable, but it also means that if Bank B defaults and A cannot recover its collateral, A's rehypothecation chains can break, triggering losses up and down the line.

Regulators permit rehypothecation but require it to be disclosed and limited. Non-financial end-users (pension funds, corporations) typically do not allow rehypothecation, while banks accept and use it. The 2008 crisis revealed that some institutions' rehypothecation was poorly tracked, leading to disputes over who owned the collateral. Regulations now require better segregation and disclosure.

## Who holds the collateral: custodians and triparty

Collateral is not held by either party (that would be a conflict of interest) but by a neutral third party, typically a **custodian** or **triparty agent**:

- **Custodian arrangement**: A major bank or specialized firm holds the collateral in a segregated account. The account is legally the winner's but operationally controlled by the custodian. If the loser defaults, the winner instructs the custodian to liquidate and transfer proceeds.

- **Triparty arrangement**: A custodian bank (typically BNY Mellon or State Street) manages collateral for both parties and conducts daily settlements automatically. The triparty agent also conducts daily "unwind" and "rewind" steps (liquidating and rebooking collateral) to ensure the loser always posts eligible collateral.

Triparty arrangements are more efficient and standardized, especially for bilateral swaps among major dealers. Custodian arrangements are older and more bespoke, often used in bilateral trades between smaller counterparties.

## Collateral management post-2008

Before 2008, collateral requirements were minimal and bilateral. A major bank might trade derivatives with another bank and post only 1–2% margin. The 2008 crisis exposed the danger: when credit spreads widened and mark-to-market losses mounted, collateral demands spiked, forcing dealers to liquidate other assets rapidly, amplifying panic.

Regulation now mandates:
- **Initial margin** for all non-cleared swaps (phased in 2016–2020); standardized via SIMM
- **Daily variation margin** for both cleared and non-cleared swaps
- **Daily segregation** (collateral is always in a third-party account, not the dealer's)
- **Haircuts and eligible collateral** lists defined by regulators

These changes have reduced dealer leverage and increased the cost of derivatives trading (dealers pay funding costs on margin balances, which they pass to clients). But they have also made the system more resilient: a dealer's failure today would not trigger a cascade of collateral calls and forced asset sales, as happened in 2008.

## Operational challenges: collateral mobility and friction

Despite standardization, collateral management remains operationally complex. A dealer may have thousands of bilateral counterparties, each posting collateral in different forms and custodians, with slightly different posting schedules. The dealer must track which collateral is eligible, apply haircuts, manage substitutions (swapping out illiquid collateral for more liquid types), and settle daily VM moves.

The COVID-19 pandemic in March 2020 exposed friction: a sudden market spike triggered collateral calls across the system, and some custodian systems were overwhelmed by the volume. Dealers had to borrow heavily, and the Federal Reserve had to step in with repo facilities to supply liquidity. The result has been renewed focus on collateral mobility—the ability to quickly move collateral between accounts and counterparties without operational delays.

New technologies, including distributed ledger and tokenization, are being explored to simplify collateral settlement, though adoption remains slow.

## See also

<div class="wiki-seealso">

### Closely related

- [Netting Agreement](/netting-agreement/) — reduces the collateral requirement by offsetting exposures
- [ISDA Master Agreement](/isda-master-agreement/) — defines credit support terms alongside netting
- [Derivatives Market Regulation](/derivatives-market-regulation/) — mandates initial and variation margin
- Central Counterparty — manages collateral for cleared derivatives automatically
- [Counterparty Risk](/counterparty-risk/) — the credit risk that collateral mitigates
- [Mark-to-Market](/fair-value/) — the daily valuation used to calculate variation margin

### Wider context

- [Interest-Rate Swap](/interest-rate-swap/) — the most common derivatives requiring margin
- [Credit Default Swap](/credit-default-swap/) — another swap requiring substantial collateral
- [Forward Contract](/forward-contract/) — a bilateral derivative often requiring margin
- [Systemic Risk](/systemic-risk/) — the market danger that collateral practices help reduce

</div>
