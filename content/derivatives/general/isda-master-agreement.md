---
title: "ISDA Master Agreement"
description: "The standard legal contract that governs bilateral over-the-counter derivatives transactions, setting default remedies, netting, and credit terms."
keywords:
  - derivatives trading
  - OTC market
  - legal framework
  - counterparty risk
  - netting
  - close-out
image: "/svg/derivatives.svg"
---

*The **ISDA Master Agreement** is the de facto global legal standard that binds two counterparties in over-the-counter derivatives trades. Published by the International Swaps and Derivatives Association, it spells out default remedies, [netting](/netting-agreement/) mechanics, credit terms, and dispute resolution, allowing trillions of dollars in swaps, forwards, and options to trade across the world under a uniform framework.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">ISDA Master Agreement — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives and risk." />

<div class="wiki-infobox-caption">The backbone of bilateral OTC derivatives trading.</div>

|   |   |
|---|---|
| **What it is** | A standardized legal contract template that governs bilateral OTC derivatives transactions |
| **Published by** | International Swaps and Derivatives Association (ISDA) |
| **First issued** | 1987; updated 2002, 2020 |
| **Covers** | Swaps, forwards, options, swaptions, and other custom derivatives |
| **Key features** | Close-out [netting](/netting-agreement/), default remedies, collateral terms, credit support |
| **Status** | Recognized and enforced by courts in 75+ jurisdictions |

</aside>

## The standard that unified a fragmented market

Before the ISDA Master Agreement existed, banks trading over-the-counter derivatives each wrote their own bilateral contracts. Terms varied wildly: one bank's definition of "default" differed from another's; netting mechanics were unclear; dispute resolution was undefined. The result was legal and settlement chaos. When a counterparty failed to perform, banks faced months of litigation to determine who owed what.

In 1987, ISDA published the first Master Agreement to address this gap. The idea was radical: a single, uniform template that all market participants would use. Banks negotiated the schedule—the terms specific to their relationship—and left the boilerplate identical. By the early 1990s, the Master Agreement had become so pervasive that a bilateral OTC swap without an ISDA Master Agreement was a rarity. Today, it is the universal standard for institutional derivatives.

## Structure: boilerplate plus schedule

An ISDA Master Agreement consists of two documents: the (lengthy) standard form and the user's guide; and the **Schedule**, a shorter document where the two counterparties negotiate specific terms.

The **Agreement** itself contains 26 sections addressing:
- Obligations and payment dates for each trade (Confirmation)
- Events of default (missed payments, insolvency, breach, etc.)
- Close-out netting mechanics (how to value positions upon default)
- Dispute resolution and governing law
- Representations and warranties
- Credit support (collateral posting)
- Termination rights and remedies

The **Schedule** is where counterparties customize their relationship: they specify which law governs the agreement (New York and English law are most common), how collateral will be posted, what events trigger early termination, whether they will use a particular [credit support](/collateral-management-derivatives/) annex, and other operational details.

This separation—standard terms paired with negotiated schedules—is what makes ISDA so efficient. Two banks can sign an ISDA Master Agreement in hours once the Schedule is settled, rather than drafting a custom contract from scratch.

## Close-out netting: the core protection

The single most important feature of the ISDA Master Agreement is its close-out [netting](/netting-agreement/) clause. Upon an Event of Default, the non-defaulting party can immediately:
- Terminate all outstanding transactions with the defaulting party
- Value each transaction at its mark-to-market cost (typically the cost to replace it with a new counterparty)
- Net all gains and losses into a single payment obligation
- Set-off any amounts owed by the defaulting party against amounts owed to it

Without this clause, an insolvent counterparty's bankruptcy trustee could "cherry-pick," paying obligations on profitable trades while refusing to pay on unprofitable ones. Netting prevents this abuse, protecting both parties and reducing systemic risk.

Courts have consistently upheld ISDA netting in bankruptcy, though the US Bankruptcy Code and foreign insolvency laws required specific amendments to make this guarantee rock-solid. The [Dodd-Frank Act](/dodd-frank-act/) and European insolvency directives now explicitly protect netting agreements, cementing their legal standing.

## Credit support annexes and margin mechanics

An ISDA Master Agreement by itself does not require collateral posting. But nearly all institutional trades supplement the Master Agreement with a **Credit Support Annex (CSA)**, a detailed addendum that specifies:
- How much [collateral](/collateral-management-derivatives/) each party must post initially
- How often they adjust (daily, bi-weekly)
- What forms of collateral are acceptable (cash, government securities, corporate bonds)
- Haircuts applied to each collateral type
- How collateral is held and rehypothecated

The CSA is where the real operational detail lives. Most bilateral trades now require daily [variation margin](/variation-margin/) settlements calculated from the ISDA-driven mark-to-market value. If Bank A's exposure to Bank B grows $5 million, B posts an additional $5 million in collateral the next day.

## Events of default and remedies

The ISDA Master Agreement defines a detailed list of events that allow the non-defaulting party to terminate and close out:

- **Payment default**: missed cash flows or margin calls for more than 3 business days (or contractually specified period)
- **Material breach**: failure to perform any material obligation, not cured within 30 days
- **Cross-default**: default on another obligation exceeding a threshold (e.g., $10 million)
- **Bankruptcy**: insolvency proceedings, receivership, or similar
- **Credit support default**: failure to post required collateral
- **Rating downgrade** (sometimes): falling below investment grade
- **Specified entity**: change in control or dissolution of key subsidiaries

Upon default, the non-defaulting party has the right—but not the obligation—to close out all trades. It can do so immediately, without waiting for bankruptcy proceedings, maximizing its ability to recover.

## Versions: 1992 and 2002

ISDA issued two major versions of the Master Agreement:

**1992 Agreement**: The original widely adopted version. Still in heavy use despite age; courts have issued thousands of rulings on its clauses, reducing legal uncertainty.

**2002 Agreement**: A modernized version addressing issues that arose in the late 1990s, including better multi-currency provisions, clearer netting mechanics, and refined default definitions. Most new bilateral trades now use 2002.

**2020 Addendum**: A light update adding provisions for physical settlement of derivatives and minor clarifications, without replacing the 2002 agreement.

Most banks maintain both versions for legacy deals. New counterparties negotiate 2002 or 2002-with-2020-addendum terms.

## Exceptions and limitations

Despite its prevalence, the ISDA Master Agreement is not universal. Some jurisdictions enforce it less reliably; Japan, for example, has a weaker legal tradition of recognizing netting, creating issues for global banks. Some corporate counterparties (pension funds, insurance companies) resist full ISDA terms due to their own credit policies. And the ISDA framework applies only to bilateral OTC derivatives; central clearing houses use their own rules and bylaws.

The Master Agreement also does not eliminate all disputes. Counterparties sometimes disagree on mark-to-market values at the moment of close-out, leading to litigation. And while netting collapses exposures, it does not prevent loss: if Bank A is $100 million in-the-money with a defaulting Bank B, A still loses the amount by which B's collateral is insufficient.

## Role in post-2008 regulation

The financial crisis exposed weaknesses in bilateral OTC derivatives that the ISDA Master Agreement alone could not fix. Regulators introduced mandatory clearing for standardized derivatives (swaps on liquid indices), moving those trades to central counterparties (CCPs). Multilateral netting through a CCP is more robust than bilateral netting under ISDA, reducing systemic risk.

However, for non-standard derivatives—bespoke swaps, exotic options, long-dated forwards—bilateral ISDA Master Agreements remain the standard. Regulators and the industry have not found a better alternative. The result is a two-tier market: standardized derivatives cleared through CCPs and custom derivatives traded bilaterally under ISDA.

## See also

<div class="wiki-seealso">

### Closely related

- [Netting Agreement](/netting-agreement/) — the close-out netting mechanism embedded in ISDA Master Agreements
- [Collateral Management in Derivatives](/collateral-management-derivatives/) — how ISDA agreements and Credit Support Annexes govern margin
- [Derivatives Market Regulation](/derivatives-market-regulation/) — how Dodd-Frank and EMIR reshaped the legal framework around ISDA
- [Counterparty Risk](/counterparty-risk/) — the credit risk that ISDA addresses through netting and collateral
- Central Counterparty — the alternative to bilateral ISDA for standardized derivatives
- [Credit Default Swap](/credit-default-swap/) — a derivative governed by ISDA Master Agreement

### Wider context

- [Forward Contract](/forward-contract/) — bilateral derivatives covered by ISDA agreements
- [Interest-Rate Risk](/interest-rate-risk/) — the exposure managed by swaps under ISDA
- [Over-the-Counter Market](/over-the-counter-market/) — where ISDA agreements are the legal backbone
- [Securities and Exchange Commission](/securities-and-exchange-commission/) — a regulator overseeing derivative brokers bound by ISDA

</div>
