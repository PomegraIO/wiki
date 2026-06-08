---
title: "How Clearinghouses Interact with Securities Lending"
description: "Securities lending clearinghouse role: when repo or securities-lending transactions clear through a CCP, settlement and collateral flows differ from bilateral trades."
keywords:
  - securities lending clearinghouse role
  - clearinghouse securities lending
  - repo clearing
  - securities lending settlement
---

*A **securities-lending** transaction is normally bilateral between a lender and a borrower: the lender transfers securities, the borrower posts collateral, and each party trusts the other. But when a securities-lending or **repo** trade clears through a clearinghouse, the CCP becomes the counterparty to both sides, changing how collateral flows, settlement happens, and risk is managed.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Securities Lending & Clearinghouses — key facts</div>

<img src="/svg/institutions.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">CCP-cleared repo and securities lending shift settlement and collateral risk from bilateral relationships to the clearinghouse.</div>

|   |   |
|---|---|
| **Bilateral securities lending** | Lender and borrower deal directly; collateral held bilaterally |
| **CCP-cleared repo** | CCP steps in as counterparty; both sides post margin to CCP |
| **Settlement** | Bilateral: T+N; Cleared: typically T+0 (cash same-day) |
| **Collateral** | Bilateral: held by borrower; Cleared: held by CCP or custodian |
| **Counterparty risk** | Bilateral: exposed to borrower; Cleared: exposed only to CCP |
| **Cost** | Bilateral: cheaper, less processing; Cleared: higher fees, more robust |

</aside>

## Bilateral securities lending versus cleared repo

In a traditional **bilateral securities-lending** transaction:
- A lender (often an asset manager or pension fund) agrees to lend securities to a borrower (often a hedge fund or short seller).
- The borrower posts cash collateral (or, less often, other securities) as security.
- The borrower pays the lender a fee (the repo rate or borrow fee).
- The trade settles directly between the two parties, often through their custodians.
- The lender trusts the borrower to return the securities and maintains a bilateral relationship.

In a **CCP-cleared repo** transaction:
- A buyer (repo lender) and seller (repo borrower) agree on terms: securities, rate, term.
- They submit the trade to the CCP.
- The CCP confirms itself as the buyer to the seller and the seller to the buyer.
- Both sides post margin to the CCP (not to each other).
- The CCP holds or supervises the collateral (securities and cash).
- Settlement is T+0 or T+1, not T+N.
- If the borrower defaults, the CCP can immediately liquidate their collateral without negotiating with the lender.

This is a fundamental shift. Instead of managing bilateral risk with one counterparty, both lender and borrower are exposed only to the CCP's solvency.

## Settlement and timing differences

In bilateral lending, settlement happens on whatever schedule the parties negotiate, often T+1 or T+3. The lender's securities and the borrower's collateral move through custodians and correspondent banks, which adds operational delay.

In CCP-cleared repo, settlement is much faster. The CCP or its designated settlement bank processes trades on T+0 (same-day settlement during hours when the system is active) or T+1. The CCP maintains direct accounts at central securities depositories (CSDs) like the Depository Trust Company (DTC) in the US or Euroclear in Europe, so securities move immediately without custodian delays.

This speed matters. In a crisis (think March 2020), fast settlement means the CCP can immediately liquidate a defaulting borrower's collateral and return securities to the lender without a multi-day gap during which the lender is unsecured.

## Collateral management

In bilateral lending, the borrower's collateral sits in the borrower's account (or a triparty collateral account controlled by the borrower and lender). If the borrower goes bankrupt, the lender has to fight for the collateral in bankruptcy court.

In cleared repo, the CCP controls the collateral. Typically:
- The CCP's custodian holds the securities in the CCP's account at the central depository.
- Cash collateral is held in accounts at a settlement bank (usually a Federal Reserve member bank or similar).
- The CCP can liquidate securities or seize cash collateral within minutes if a member defaults.

This is much safer for the lender. The CCP's control and insolvency protections (backed by its default fund and, ultimately, by central-bank support) eliminate the operational and legal delays of bilateral collateral recovery.

## Margin and variation margin

In bilateral lending, the collateral is posted once at the outset and adjusted periodically (if at all) as the securities' value changes. Many bilateral loans are under-margined or un-margined for operational convenience.

In CCP-cleared repo, both the lender (buyer) and borrower (seller) post **initial margin** when the trade is cleared, and then post **variation margin** daily. If the securities' value rises, the borrower posts additional margin to the CCP. If it falls, the lender posts margin to the CCP. This real-time repricing prevents the CCP from accumulating unhedged losses.

The result is a much tighter risk boundary, but also higher operational and financial cost to participants.

## Term and renewal

Bilateral securities lending is often open-ended. A borrower can keep the securities indefinitely by rolling the collateral. Interest accrues; fees are paid; and the relationship persists until one side wants out.

CCP-cleared repo typically has a fixed term: overnight, 1-week, 1-month, etc. At maturity, the trade settles and the borrower must roll into a new trade if they want to keep the securities. This frequent repricing gives the CCP (and the lender) the chance to reprice risk regularly.

## Which transactions clear?

Not all securities lending clears. **Bilateral repo** (especially among major banks and hedge funds) often remains uncleared. Regulatory capital and liquidity requirements now encourage clearing of standardized repo, but bilateral repos still happen when credit relationships are tight or when counterparties want bespoke terms.

**Exchange-traded repo** (repo traded on platforms like NYSE Euronext) is always cleared. Most **GC repo** (general collateral repo, using a broad basket of treasuries as collateral) is now cleared in major markets.

**Securities lending** (lending of equities, bonds, or other securities not necessarily for short sale) remains largely bilateral, though some large lenders push for clearing to reduce operational risk.

## Regulatory drivers

Post-2008, regulators have mandated or strongly encouraged clearing of standardized derivatives and repo. The [Dodd-Frank Act](/dodd-frank-act/) in the US and EMIR in the EU both require standardized swaps to clear. Repo clearing has expanded, though not as aggressively.

The rationale: cleared trades reduce counterparty risk and improve transparency. Uncleared trades require higher [capital-adequacy](/capital-adequacy/) charges to banks, making clearing cheaper in many cases.

## Cost and accessibility

CCP-cleared repo is safer and more efficient, but also more expensive. Members must pay [clearing fees](/), margin requirements are higher, and participants must meet CCP membership or banking requirements.

Bilateral securities lending is cheaper and more accessible to smaller players (specialty finance firms, smaller hedge funds) who cannot access clearing. It trades off lower cost against higher operational risk.

## Fails and recovery in clearing

If a counterparty fails to deliver securities in a bilateral loan, the lender must pursue a claim in bankruptcy. Resolution may take months or years.

If a counterparty fails to deliver in a CCP-cleared trade, the CCP immediately buys in the securities (at market) and charges the failing party for the difference. This happens within hours, not months. The risk of loss is transferred to the CCP and its default fund, not left hanging in bankruptcy.

This reliability is why institutional asset managers increasingly require that securities-lending and repo activity be CCP-cleared, even if it raises costs.

## See also

<div class="wiki-seealso">

### Closely related

- Central Counterparty — the entity clearing securities lending trades
- [CCP Stress Testing Explained](/ccp-stress-testing-explained/) — how CCPs size reserves for cleared repo stress
- [Segregated vs Omnibus Client Accounts at a Clearinghouse](/segregated-vs-omnibus-account-clearing/) — how account structure affects repo margin
- Margin — the collateral mechanism in cleared repo
- [Repurchase Agreement](/repurchase-agreement/) — the bilateral or cleared repo transaction itself

### Wider context

- [Counterparty Risk](/counterparty-risk/) — the bilateral risk that clearing eliminates
- Custody — the infrastructure holding cleared collateral
- Settlement — the mechanics of trade completion
- [Liquidity Risk](/liquidity-risk/) — the risk CCPs manage in repo markets

</div>
