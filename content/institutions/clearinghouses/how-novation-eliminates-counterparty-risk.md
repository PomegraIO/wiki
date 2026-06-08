---
title: "How Novation Eliminates Counterparty Risk in Cleared Markets"
description: "Novation is the legal substitution of a central counterparty (CCP) for the original counterparty in a derivatives trade, eliminating bilateral credit risk by making the CCP the buyer to every seller and seller to every buyer."
keywords:
  - how novation eliminates counterparty risk
  - novation central counterparty
  - ccp novation clearing
  - counterparty risk elimination
  - cleared derivatives novation
image: /svg/institutions.svg
---

*When you enter a derivatives trade — a futures contract, an interest rate swap, a credit default swap — in a cleared market, **how novation eliminates counterparty risk** is through a single legal moment: the original trade between two parties is terminated, and two new identical trades replace it, each with a **central counterparty (CCP)** as intermediary. The CCP becomes your counterparty and theirs, absorbing the credit risk that would otherwise bind you to each other. This substitution, called novation, is the core mechanism that converted derivatives trading from bilateral (and fragile) to centralized (and robust).*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Novation — Key Mechanics</div>

<img src="/svg/institutions.svg" alt="An abstract editorial mark for institutions." />

<div class="wiki-infobox-caption">A CCP steps between buyer and seller, becoming the sole counterparty to each at the moment of clearing.</div>

|   |   |
|---|---|
| **Before Novation** | Bilateral trade: Bank A owes Bank B $10M if rates move up |
| **Novation Moment** | CCP substitutes: Bank A pays CCP, CCP pays Bank A the same flows |
| **After Novation** | Two identical trades: Bank A vs CCP, CCP vs Bank B |
| **Credit Exposure** | Bank A risks the CCP's solvency, not Bank B's |
| **Risk Concentration** | CCP aggregates all member default risk; members post collateral |
| **Netting Benefit** | CCP nets exposures across all members, reducing capital required |
| **Legal Requirement** | Must occur automatically upon trade execution in centrally cleared markets |

</aside>

## The Three-Party Moment

Imagine a trader at Bank A negotiates a three-year interest rate swap with Bank B: Bank A will pay fixed 3% on $100 million, Bank B will pay floating SOFR. The contract details cash flows, credit triggers, and obligations. Before novation, Bank A and Bank B are counterparties; Bank A has credit exposure to Bank B (if rates fall, Bank B owes Bank A money and might fail to pay), and vice versa.

In a cleared market, the moment the trade executes, a central counterparty (often a dedicated entity like the Intercontinental Exchange Clearinghouse or the Depository Trust & Clearing Corporation) steps in. The original trade is terminated. In its place, two new, identical trades are created: Bank A vs CCP, and CCP vs Bank B. The CCP commits to honor all cash flows that Bank B agreed to pay Bank A, and Bank A commits to honor all flows that Bank A agreed to pay Bank B.

From Bank A's perspective, the trade is identical in economic terms — the cash flows are the same — but the counterparty has changed. Bank A no longer faces Bank B's credit risk; Bank A faces the CCP's credit risk. Bank B, conversely, no longer faces Bank A's credit risk; it faces the CCP. The credit exposure is no longer bilateral; it is now one-to-many (each member to the CCP) and aggregated.

## Why This Eliminates Risk

Bilateral credit risk is acute because it is bilateral. If Bank B fails before paying Bank A $10 million on a swap, Bank A loses $10 million and must hedge or unwind its position with a new counterparty, facing market losses if rates have moved unfavorably. The failure of Bank B directly harms Bank A.

Novation fragments that direct harm. The CCP, as the common counterparty, holds collateral (variation margin) from both banks. As the interest rate or value of the swap changes, the CCP adjusts margin calls daily — the losing party posts cash, the winning party receives it. The CCP guarantees the trade. If Bank B fails, Bank A does not lose the $10 million trade value because the CCP assumes the obligation. If Bank A fails, Bank B does not lose because the CCP steps in.

The CCP is not absorbing the credit risk out of goodness; it is absorbing it by design and extracting fees (clearing fees) to offset the risk. The CCP is typically a highly capitalized, well-regulated entity (sometimes government-backed), so its default probability is far lower than that of any single member bank. Aggregating all trades through the CCP also allows netting: if Bank A owes the CCP $5M on one trade and is owed $4M on another, the CCP nets the positions and only $1M is at risk. This netting reduces the total capital and collateral the system requires.

## The Moment of Novation

Novation happens instantly upon trade execution in a cleared market — the trader typically does not see it occurring. The CCP's systems receive the trade confirmation, validate both sides' details, and immediately record two new positions. The original bilateral contract is terminated with no further obligation; the new trades with the CCP are the binding obligations. This happens in milliseconds.

For this to work, both parties must have pre-arranged clearing membership or access to the CCP. A bank opens a clearing account with the CCP, signs the master clearing agreement (which includes the novation language), and deposits initial margin. When a trade clears, the novation is automatic.

Not all derivatives are centrally cleared. Over-the-counter (OTC) trades in exotic options, bespoke credit derivatives, or customized combinations often cannot be standardized enough for a CCP, so they remain bilateral. In those cases, Bank A and Bank B remain counterparties and face each other's credit risk directly, though they may use collateral agreements or central clearing for [credit default swap](/credit-default-swap/) to hedge some of the exposure.

## Collateral and Default Waterfall

After novation, the CCP's protection of each member relies on collateral. Bank A and Bank B each post initial margin (a deposit based on the notional value and expected volatility of their trades) and daily variation margin (updates based on mark-to-market gains and losses). If Bank B becomes insolvent, the CCP can liquidate Bank B's collateral, and if it is insufficient, the CCP dips into its own capital buffer. If that fails, losses cascade to the surviving members through a default waterfall — a pre-arranged mechanism in which non-defaulting members contribute additional funds or absorb losses.

This design ensures that even if a large member defaults, the CCP's obligation to non-defaulting members is honored. The system is much more resilient than bilateral networks of credit exposure, where a single large failure can trigger cascading defaults (as happened in 2008 when Lehman Brothers' bilateral counterparties all suffered simultaneous losses).

## What Novation Requires

For novation to work, three conditions must hold:

1. **Standardization**: The trade must be standardizable — fixed contract terms (expiry, notional, underlying) so that CCPs can offset and net positions across members.

2. **Regulatory framework**: Jurisdictions must recognize novation as valid and legally binding. US law, UK law, and EU law all have legal opinions confirming that novation upon clearing is enforceable even in bankruptcy.

3. **Member creditworthiness**: The CCP requires members to meet capital and operational standards. A bank cannot clear trades with a CCP unless it is solvent and sufficiently capitalized.

These constraints mean not all derivatives markets clear. Complex, bespoke trades stay bilateral and are managed through bilateral collateral.

## Evolution and Scope

Before the 2008 financial crisis, most derivatives did not clear. Lehman Brothers' bilateral counterparties (hundreds of banks, insurance companies, pension funds) found themselves directly exposed to Lehman's default, with no CCP buffer. The shock to the system led to regulations (Dodd-Frank in the US, EMIR in the EU) mandating central clearing for all standardized derivatives: interest rate swaps, credit default swaps, and foreign exchange forwards.

Today, the vast majority of new interest-rate swap and credit default swap volume clears through CCPs. Futures have cleared since the 1920s, so novation in futures markets is ancient practice. The post-2008 regulatory push greatly expanded the scope of novation and reduced the stock of bilateral derivatives credit risk in the financial system.

## See also

<div class="wiki-seealso">

### Closely related

- [Counterparty risk](/counterparty-risk/) — How bilateral credit exposure arises and how novation eliminates it
- [Central bank](/central-bank/) — Role in regulating and backstopping clearinghouses
- [Credit default swap](/credit-default-swap/) — A common derivative that clears through CCPs and benefits from novation
- [Collateral](/repurchase-agreement/) — Margin and capital reserved to cover novation risk
- [Dodd-Frank Act](/dodd-frank-act/) — Legislation mandating central clearing for most derivatives

### Wider context

- [Swap](/swap/) — General mechanism of derivative contracts that undergo novation
- [Futures contract](/futures-contract/) — The oldest centrally cleared instrument; novation embedded by design
- [Systemic risk](/systemic-risk/) — How central clearing reduces contagion from a single default
- [Securities and Exchange Commission](/securities-and-exchange-commission/) — Regulator overseeing clearinghouses and novation compliance
- [Market risk](/market-risk/) — Credit risk as one component of total derivatives exposure

</div>