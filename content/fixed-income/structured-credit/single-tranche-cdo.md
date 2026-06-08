---
title: "Single-Tranche CDO"
description: "A custom CDO structure where a dealer sells only one tranche to a client and delta-hedges the residual risk itself, avoiding public offering."
keywords:
  - structured credit
  - cdo tranche
  - bespoke cdos
  - credit derivative
  - delta hedging
image: /svg/fixed-income.svg
---

*A **single-tranche CDO** is a custom securitization in which a dealer creates a [collateralized debt obligation](/securitization/) on a loan or bond portfolio, sells a single [tranche](/tranche/) to a client, and hedges the remaining portfolio risk itself rather than offering the full capital structure to the public market. It is a privately negotiated alternative to multi-tranche CDOs, used when an investor wants a specific credit exposure without bearing the illiquidity of a full bond offering.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Single-Tranche CDO — key facts</div>

<img src="/svg/fixed-income.svg" alt="An abstract editorial mark for fixed income and structured instruments." />

<div class="wiki-infobox-caption">A dealer builds a CDO, sells one tranche, and hedges the rest on its own books.</div>

|   |   |
|---|---|
| **What it is** | A bespoke [securitization](/securitization/) in which the dealer sells only one [tranche](/tranche/) and retains/hedges others |
| **Typical structure** | Dealer buys a loan portfolio, issues client's chosen [tranche](/tranche/), hedges remaining tranches with [CDS](/credit-default-swap/) or cash bonds |
| **Pricing** | Customized to the client's risk appetite and the underlying pool's credit quality |
| **Key difference from multi-tranche CDO** | No public offering; no equity tranche sold to the market; dealer absorbs equity and mezzanine losses |
| **Dealer motivation** | Fee income, portfolio distribution, and ability to hedge risks on its own terms |
| **Client motivation** | Tailored [credit exposure](/credit-risk/) without buying an entire seasoned securitization |
| **Risk** | Underlying pool quality, [tranche](/tranche/) seniority, and dealer's hedging effectiveness |

</aside>

## The appeal of customization

Traditional [CDOs](/securitization/) are assembled from a pool of loans or bonds, divided into multiple [tranches](/tranche/), and offered to the market all at once—typically a senior piece, a mezzanine, a subordinated, and an equity [tranche](/tranche/). A single-tranche CDO inverts this process: the dealer and client negotiate directly. The client specifies the desired [tranche](/tranche/) (often mezzanine or subordinated), the underlying pool composition, and the expected [credit spread](/credit-spread/). The dealer then assembles the pool, issues only that [tranche](/tranche/) to the client, and **hedges all remaining [tranche](/tranche/) losses on its own balance sheet**.

This structure became popular in the mid-2000s, particularly in bank lending and European mortgages. An investor with a specific appetite for a certain credit [spread](/credit-spread/) and loss profile—say, senior mezzanine exposure to mid-market corporate loans—could acquire a note sized and priced to its exact needs without waiting for a public offering or accepting unfamiliar asset types. The dealer, in turn, obtained a client-driven asset and could manage hedging actively.

## The dealer's role: portfolio constructor and hedger

Once the [tranche](/tranche/) is sold to the client, the dealer owns or commits to hedging all subordinate [tranches](/tranche/). A dealer might keep the equity [tranche](/tranche/) (absorbing the first losses) but hedge the mezzanine and senior tranches through a [CDS](/credit-default-swap/) on the underlying collateral or by buying protective [puts](/put-option/) on the [tranche](/tranche/) itself.

The dealer's primary income comes from the client's coupon and from portfolio management fees. But it also benefits if the underlying portfolio performs better than the client anticipated—the dealer's equity and mezzanine [tranches](/tranche/) capture upside. Conversely, if the pool deteriorates, the dealer suffers. This creates a perverse incentive: dealers sometimes had loose standards for the underlying collateral because they knew they could hedge the senior risks and exit early.

The hedging can occur through [credit default swaps](/credit-default-swap/), [bond](/bond/) positions, or replication via other single-tranche CDOs issued to other clients. A dealer managing multiple single-tranche CDOs on overlapping pools gains diversification and can offset hedges across clients. Pricing and hedge ratios require sophisticated [valuation](/discounted-cash-flow-valuation/) models; errors in [correlation](/systemic-risk/) assumptions or pool performance led to enormous losses during the 2008 crisis.

## Why investors preferred them

From the client's perspective, a single-tranche CDO is more transparent than a multi-[tranche](/tranche/) offering. The investor negotiates the coupon, [spread](/credit-spread/), and subordination directly with the dealer. It avoids the friction of a primary market roadshow and the uncertainty of a fixed-price public sale. For some investors, especially hedge funds and specialized credit funds, the ability to customize the [tranche](/tranche/) to portfolio needs was highly attractive.

Investors also believed—often incorrectly—that single-tranche CDOs offered better risk control. Because the dealer was retaining junior [tranches](/tranche/), investors reasoned, the dealer had skin in the game and would manage the pool conservatively. In practice, dealers often hedged their junior exposure quickly, reducing that incentive.

## The structural flaw: correlation risk

A critical vulnerability in single-tranche CDOs (and all CDO structures) is dependence on default correlation assumptions. A [tranche's](/tranche/) [credit spread](/credit-spread/) is priced assuming that the underlying loans and bonds default independently (or with a historically calibrated correlation). If correlation spikes—as it did in 2008 when financial stress became systemic—junior tranches experience sudden, synchronized losses, and the mezzanine and senior [tranches](/tranche/) take far larger losses than modeled.

Many single-tranche CDOs were structured on pools where the underlying obligors were correlated (e.g., all regional banks, or all mortgage lenders). A dealer might have believed that hedging the senior [tranches](/tranche/) through CDS was sufficient protection; but if that [CDS](/credit-default-swap/) counterparty itself became stressed or insolvent, the hedge evaporated and the dealer's losses exploded.

Dealers' hedging models also often underestimated [liquidity risk](/liquidity-risk/). In a stress scenario, the [bond](/bond/) market dries up, [CDS](/credit-default-swap/) spreads widen sharply, and the dealer cannot exit or rebalance its hedge without absorbing huge losses. The structured credit market seized up in 2008, turning many single-tranche CDOs and their hedge positions into underwater, illiquid positions.

## Relation to other structured vehicles

Single-tranche CDOs sit between plain [credit-linked notes](/credit-linked-note/) and multi-[tranche](/tranche/) CDOs. A [credit-linked note](/credit-linked-note/) is usually single-name—the investor takes on the credit risk of one reference entity. A single-tranche CDO pools many assets but sells one [tranche](/tranche/) of the resulting securitization. A multi-[tranche](/tranche/) CDO distributes the full capital structure to multiple investors, with each [tranche](/tranche/) having a different seniority and coupon.

[ABS CDOs](/abs-cdo/), another structure, often took the single-[tranche](/tranche/) form in the 2000s—dealers issued one client-facing [tranche](/tranche/) backed by pools of [mortgage-backed securities](/mortgage-backed-security/) or asset-backed securities, compounding leverage and correlation risk.

## Market context and decline

Single-tranche CDOs flourished from 2005 to 2007, particularly in structured credit on mortgages and loans. The market peaked as leverage reached extreme levels and [credit spreads](/credit-spread/) compressed to historic lows. Dealers could issue very cheap mezzanine [tranches](/tranche/) to clients, hedge them partially, and retain equity exposure that seemed to have upside.

When the housing market declined and credit markets froze in 2007–2008, the market collapsed. Dealers found themselves unable to hedge, and the equity [tranches](/tranche/) they retained became worthless. Many single-tranche CDOs on mortgage pools suffered total losses; dealers and their clients both took catastrophic hits.

Post-crisis, single-tranche CDO issuance fell to a small fraction of pre-2008 levels. Regulatory [capital-adequacy](/capital-adequacy/) rules imposed heavier charges on structured credit positions, discouraging dealer risk-taking. Clients also became skeptical of dealer hedging effectiveness. The market never fully recovered; today, single-tranche CDOs remain niche, used primarily for specialized loan and infrastructure portfolios by dealers with strong track records.

## See also

<div class="wiki-seealso">

### Closely related

- [Securitization](/securitization/) — the general process of pooling and tranching assets
- [Tranche](/tranche/) — the layers of a CDO; investors buy a specific tranche
- [Credit-Linked Note](/credit-linked-note/) — another custom credit instrument sold by dealers
- [Nth-to-Default Swap](/nth-to-default-swap/) — alternative structure for multi-name credit exposure
- [ABS CDO](/abs-cdo/) — CDOs backed by asset-backed securities; often single-tranche
- [Credit Default Swap](/credit-default-swap/) — used by dealers to hedge CDO tranches
- [Collateralized Debt Obligation](/securitization/) — the broader CDO family

### Wider context

- [Credit Risk](/credit-risk/) — the fundamental risk structured credit transfers
- [Correlation](/systemic-risk/) — assumption about default correlation; critical to CDO valuation
- [Credit Spread](/credit-spread/) — the excess yield compensating for tranche risk
- [Liquidity Risk](/liquidity-risk/) — hedging liquidity, key vulnerability during crises
- [Financial Crisis of 2008](/great-depression/) — when single-tranche CDOs suffered enormous losses

</div>
