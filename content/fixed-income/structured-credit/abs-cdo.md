---
title: "ABS CDO"
description: "A collateralized debt obligation backed by tranches of asset-backed securities rather than direct loans, magnifying leverage and correlation exposure."
keywords:
  - structured credit
  - asset-backed securities
  - cdo securitization
  - mortgage leverage
  - correlation risk
image: /svg/fixed-income.svg
---

*An **ABS CDO** (or "CDO-squared") is a [securitization](/securitization/) backed by [tranches](/tranche/) of other asset-backed securities—typically [mortgage-backed securities](/mortgage-backed-security/) or consumer loan ABSs—rather than by direct loans or bonds. By layering [tranches](/tranche/) from multiple secondary securities, ABS CDOs compounded leverage and correlation risk, making them especially vulnerable to deterioration in the underlying asset pools.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">ABS CDO — key facts</div>

<img src="/svg/fixed-income.svg" alt="An abstract editorial mark for fixed income and structured instruments." />

<div class="wiki-infobox-caption">A CDO backed by tranches of mortgages and consumer ABSs; leverage and risk multiply.</div>

|   |   |
|---|---|
| **What it is** | A [CDO](/securitization/) whose collateral consists of [tranches](/tranche/) from [mortgage-backed securities](/mortgage-backed-security/) or other [ABSs](/securitization/) |
| **Collateral** | Typically mezzanine and senior [tranches](/tranche/) from residential mortgage pools, auto loans, credit card receivables |
| **Leverage chain** | Original borrowers → mortgage pool → MBS tranches → ABS CDO tranches |
| **Correlation assumption** | Depends on correlation among the underlying mortgage pools; highly concentrated |
| **Key risk** | Housing market deterioration or pool-level loss triggers cascade through multiple CDO layers |
| **Typical issuer** | Banks and securities dealers; minimal inventory before sale |
| **Market maturity** | Peaked 2006–2007; market nearly halted post-2008 |
| **See also** | [Single-Tranche CDO](/single-tranche-cdo/), [Credit-Linked Note](/credit-linked-note/) |

</aside>

## The leverage chain: borrower → pool → ABS → CDO

An ABS CDO exemplifies the multiplication of leverage inherent in structured finance. The chain begins with mortgages or consumer loans made by banks or mortgage brokers. These loans are then pooled into [mortgage-backed securities](/mortgage-backed-security/) (MBSs) or asset-backed securities (ABSs), which are themselves [tranched](/tranche/): a senior [tranche](/tranche/) (absorbing little loss), a mezzanine [tranche](/tranche/) (absorbing moderate loss), and a subordinated or equity [tranche](/tranche/) (absorbing first losses).

An ABS CDO then takes mezzanine and junior [tranches](/tranche/) from multiple MBS and ABS pools and uses them as collateral for a new, second-level [securitization](/securitization/). The CDO is also [tranched](/tranche/)—senior, mezzanine, and equity—creating a waterfall of losses. A decline in housing prices or consumer credit quality thus flows through multiple layers: borrowers default on the original loans, losses cascade through the MBS/ABS [tranches](/tranche/), triggering defaults on the ABS CDO's collateral, which then triggers losses on the CDO's own [tranches](/tranche/).

This structure magnified the housing bubble. During 2005–2007, as house prices rose and mortgage [credit spreads](/credit-spread/) compressed, the demand for AAA-rated securities seemed insatiable. Investment banks, desperate for collateral and fees, created ABS CDOs to supply it. A pool of subprime mortgages with 5–10% expected loss rates was sliced into [tranches](/tranche/); the junior pieces were pooled into an ABS CDO whose senior [tranche](/tranche/) received a AAA rating and sold at a tight [spread](/credit-spread/) over [Treasuries](/treasury-bond/). The originating loan originators, lenders, and ABS issuers had no skin in the game—all risk was passed to the CDO buyer.

## Correlation concentration and the false safety premise

The critical flaw was **correlation assumption**. An ABS CDO's senior [tranche](/tranche/) is safe if the losses from the underlying ABS [tranches](/tranche/) are independent—if a loss in one mortgage pool does not predict losses in another. Rating agencies and pricing models implicitly assumed this independence, based on historical data in which mortgage pools in different geographies and vintages did not all default simultaneously.

But this assumption was catastrophically wrong. During the 2008 housing collapse, default rates surged in all mortgage pools *at once*. Borrowers across the country became underwater on their homes simultaneously; subprime delinquencies became highly correlated. The ABS CDO model assumed that if pool A suffered losses, pool B would be relatively safer—so the CDO's junior tranches would absorb most of pool A's loss, leaving the senior tranche intact. In reality, when the housing market seized, pools A, B, and C all experienced synchronized defaults, and senior ABS CDO [tranches](/tranche/) themselves suffered large losses.

The rating agencies, which had assigned AAA ratings to senior ABS CDO tranches, failed to stress-test for this scenario. Models relied on realized [correlation](/systemic-risk/) from the past 30 years, when housing prices only rose. No model incorporated the possibility of a nationwide housing collapse, making the ratings worse than worthless—they were dangerously misleading.

## Double and triple leverage

An ABS CDO investor bought risk that was already embedded in a secondary security. If an investor had purchased an MBS mezzanine [tranche](/tranche/) directly, they would absorb losses starting after the mortgage pool's equity [tranche](/tranche/] lost its capital. An ABS CDO investor in a comparable [tranche](/tranche/) of the CDO bore risk after both the original ABS equity [tranche](/tranche/) AND the ABS CDO's equity [tranche](/tranche/) were wiped out—but because correlation meant multiple ABS tranches defaulted together, the CDO's own junior pieces evaporated quickly, leaving the "senior" CDO tranches exposed.

This double leverage made ABS CDOs a magnified bet on housing. Dealers, conscious of this, often hedged senior ABS CDO tranches through [credit default swaps](/credit-default-swap/) on the underlying pools, assuming this would protect them. But during the crisis, [CDS](/credit-default-swap/) spreads widened so sharply that the hedging was insufficient, and counterparties themselves became stressed, unable to pay out [CDS](/credit-default-swap/) claims.

## Valuation and sales model

Dealers priced ABS CDOs using models that estimated the probability distribution of losses in the underlying ABS pools. They calibrated these models to historical [credit spreads](/credit-spread/) on the MBS and ABS tranches, then solved for the [spread](/credit-spread/) that compensated the CDO's tranches for their expected losses. The models output a probability that the CDO's senior [tranche](/tranche/) would suffer any loss at all; if that probability was very low (say, 0.01%), the senior [tranche](/tranche/) was assigned a AAA rating.

The model outputs were then typically backed by confidence intervals or stress tests—calculations showing loss rates under higher [correlation](/systemic-risk/) or higher default assumptions. However, the stress tests were often far too narrow. A dealer might assume correlation increased from 20% to 40%, recompute the loss distribution, and find the senior [tranche](/tranche/) still AAA-rated. In reality, during the crisis, correlation spiked to 80%+ and loss rates were catastrophic, rendering the senior tranches nearly worthless.

## Cascade of losses post-2008

When housing prices started to decline in 2006 and mortgage delinquencies spiked in 2007, ABS CDO investors and dealers realized their mistake. The underlying mortgage pools were performing far worse than historical norms suggested they should. The ABS [tranches](/tranche/) backed by subprime mortgages, which had been rated A or BBB, experienced losses. Those losses flowed through to the ABS CDOs. Senior ABS CDO [tranches](/tranche/), previously thought to be nearly risk-free, were suddenly seen as junk.

By 2008, most ABS CDOs were marked far below par, and the secondary market for them virtually halted. Dealers holding inventory suffered enormous losses. Investors who had bought senior ABS CDO [tranches](/tranche/) as AAA-safe assets received ratings downgrades and realized losses of 50–100%. The reputational damage to rating agencies was severe; their models were revealed to be inadequate, and their conflicts of interest—agencies were paid by issuers—were exposed.

## The broader lesson: leverage and [correlation](/systemic-risk/)

ABS CDOs encapsulate a core lesson from the financial crisis: **leverage compounded without corresponding risk reduction is fragile**. Each layer of [securitization](/securitization/) promised to isolate and distribute risk, but it actually concentrated it through correlation. The illusion of diversification—that senior CDO [tranches](/tranche/) were safe because losses would be absorbed by junior pieces—collapsed when the underlying assets all deteriorated together.

Post-crisis, ABS CDO issuance fell to near zero. Regulatory [capital-adequacy](/capital-adequacy/) rules imposed punitive charges on dealer holdings of structured credit. Investors became skeptical of model-driven ratings and demanded much tighter [spreads](/credit-spread/) (higher compensation) for any complex securitization. The secondary market became hostile: buyers knew that dealers holding ABS CDO inventory were in distress and used that leverage to demand fire-sale pricing.

Today, ABS CDOs are rare. Most securitization of mortgages is done at the primary level (government-backed [MBSs](/mortgage-backed-security/) or plain commercial MBSs), and secondary-level [securitization](/securitization/) is confined to niche structures with clear, transparent collateral pools and robust [credit enhancement](/credit-risk/). The appetite for double-tranched complexity has not returned.

## See also

<div class="wiki-seealso">

### Closely related

- [Securitization](/securitization/) — the general mechanism by which ABS CDOs are created
- [Mortgage-Backed Security](/mortgage-backed-security/) — the primary collateral for ABS CDOs
- [Tranche](/tranche/) — the risk layers within ABS CDOs and their underlying ABSs
- [Single-Tranche CDO](/single-tranche-cdo/) — custom CDO structure often used for ABS collateral
- [Credit-Linked Note](/credit-linked-note/) — alternative funded structure for credit exposure
- [Nth-to-Default Swap](/nth-to-default-swap/) — multi-name derivative often used in CDO payoff waterfalls
- [Credit Default Swap](/credit-default-swap/) — used to hedge ABS CDO tranches post-issuance

### Wider context

- [Asset-Backed Security](/securitization/) — the family of [securitizations](/securitization/) that feed into ABS CDOs
- [Credit Spread](/credit-spread/) — yield compensation for ABS CDO tranche risk
- [Credit Risk](/credit-risk/) — the fundamental risk ABS CDOs concentrate
- [Correlation](/systemic-risk/) — the critical assumption (and flaw) in ABS CDO pricing
- [Liquidity Risk](/liquidity-risk/) — why ABS CDOs became illiquid in the 2008 crisis
- [Financial Crisis of 2008](/great-depression/) — when ABS CDO losses catalyzed systemic stress

</div>
