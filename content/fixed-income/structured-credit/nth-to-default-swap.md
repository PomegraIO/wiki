---
title: "Nth-to-Default Swap"
description: "A credit derivative that pays out when the n-th entity in a reference basket defaults, concentrating default risk in a way that depends on correlation."
keywords:
  - credit derivative
  - default risk
  - correlation risk
  - multi-name cds
  - structured credit
image: /svg/fixed-income.svg
---

*An **nth-to-default swap** is a [credit derivative](/credit-default-swap/) on a basket of reference entities in which the protection buyer collects a payoff only when the n-th default occurs in that basket. If n = 1, the swap pays on the first default; if n = 3, it pays only after three entities have defaulted. The seller of protection bears concentrated default risk, while the pricing depends heavily on the correlation among the reference entities' credit events.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Nth-to-Default Swap — key facts</div>

<img src="/svg/fixed-income.svg" alt="An abstract editorial mark for fixed income and structured instruments." />

<div class="wiki-infobox-caption">A derivative paying out on the n-th default; risk concentration rises sharply with n.</div>

|   |   |
|---|---|
| **What it is** | A [credit derivative](/credit-default-swap/) on multiple names; pays when the n-th default occurs |
| **Typical baskets** | 5 to 125 reference entities (corporates, sovereigns, loans) |
| **Value of n** | 1 (first-to-default), 2, 3, up to basket size |
| **Protection buyer** | Receives payoff (usually the basket's notional) upon the n-th credit event |
| **Protection seller** | Bears the risk of the n-th default; compensated via a coupon or upfront fee |
| **Coupon** | Higher for lower n (first-to-default more likely than 10th-to-default); depends heavily on correlation |
| **Key driver** | [Correlation](/systemic-risk/) between reference entities; higher correlation means each entity's default is less independent |
| **Use** | Speculation on multi-name credit risk, hedge on loan/bond portfolios, [securitization](/securitization/) payoff structure |

</aside>

## The mechanics: n defaults and you collect

A first-to-default swap is the simplest variant. An investor buys protection on a basket of, say, 10 investment-grade corporations. The swap seller receives a coupon (typically a few basis points per annum). As soon as any one of the 10 entities defaults, the protection buyer receives a fixed payoff—often the notional of the swap, minus any [recovery value](/credit-default-swap/) on the defaulted name's debt.

An nth-to-default swap generalizes this. The payoff is triggered not on the first default but only on the n-th default. In a 10-name basket with n = 3, the swap pays out only after three of the entities have defaulted. The time between each default can be months or years, during which the seller continues paying the coupon.

Structurally, this is a credit derivative with an embedded default counter. Most nth-to-default swaps are traded in the [over-the-counter market](/over-the-counter-market/), negotiated bilaterally between dealer and client. The basket composition, seniority of the reference debt (senior unsecured vs. subordinated), and recovery assumptions are all negotiated. Pricing is done using models of default timing and [correlation](/systemic-risk/).

## Why correlation is everything

A key difference from single-name [credit default swaps](/credit-default-swap/) is sensitivity to [correlation](/systemic-risk/). If the 10 entities in the basket are perfectly uncorrelated—each defaulting independently—then the probability that three will default by a given date is purely a function of each entity's individual [credit rating](/credit-rating/) and [spread](/credit-spread/). 

But in reality, defaults cluster. During a recession, many corporates suffer simultaneously. During a credit crisis, even unrelated firms become stressed as financing dries up. Higher correlation means that if one entity defaults, others are more likely to follow soon after. This reduces the expected time to the n-th default and increases the likelihood of hitting n defaults, raising the value of protection.

A protection seller in a 3rd-to-default swap pricing example might assume low correlation and quote a tight coupon (cheap protection), reasoning that it's unlikely three independent defaults will occur in a short horizon. But if correlation spikes—as it does in stress periods—the dealer's actual loss frequency will be far higher than modeled, resulting in losses.

This dynamic plagued dealers during the 2008 crisis. Many nth-to-default swaps were priced assuming historical [correlation](/systemic-risk/), which was much lower than realized correlation when the financial system became stressed. Dealers who sold protection on CRE (commercial real estate) and mortgage baskets found themselves paying out repeatedly; the n-th default sometimes came far sooner than the pricing models predicted.

## First-to-default as a credit hedge

First-to-default swaps (n = 1) have a practical use in loan syndication. A bank originating a commercial loan to a borrower often syndicated the risk to other investors. To protect itself, the originating bank might buy a first-to-default swap on a basket of borrowers in the same industry or region. If any one borrower defaults, the swap pays out, offsetting the originating bank's loss on that loan. This is cheaper than buying single-name [CDS](/credit-default-swap/) on all borrowers because the protection is triggered by the first default, not every default.

In a 10-name basket of mid-market companies, the probability that at least one will default in a 5-year period is quite high (maybe 20–30%, depending on [credit quality](/credit-rating/)). So a first-to-default swap on such a basket is relatively expensive to buy—a few hundred basis points per annum or an upfront fee. The protection seller is bearing a concentrated bet that at least one name will blow up.

## Higher n: fewer defaults required, but still correlated

As n increases, the swap becomes cheaper to buy (lower coupon), because the payoff is less likely. A 5th-to-default swap on the same 10-name basket is much cheaper than the 1st-to-default because five independent defaults is a low-probability event. However, **correlation inversely helps the seller**: if the basket is correlated and one default occurs, the probability of the 2nd, 3rd, 4th, and 5th following in quick succession rises sharply, compressing the time to payoff.

Dealers pricing nth-to-default swaps must account for default timing—how long between defaults—not just whether they occur. Models calibrated to [CDS](/credit-default-swap/) spreads on individual names provide starting point, but multi-name correlation is estimated separately, often from historical default data or equity [correlation](/systemic-risk/) proxies. In the 2000s, dealers were notoriously overconfident in their correlation calibrations, leading to severe underpricing.

## Use in structured credit

Nth-to-default swaps embed naturally in [securitizations](/securitization/). An [ABS CDO](/abs-cdo/) or [single-tranche CDO](/single-tranche-cdo/) often uses nth-to-default logic: the equity [tranche](/tranche/) absorbs the first m defaults (or first m percent of losses), the mezzanine absorbs the next k defaults, and the senior [tranche](/tranche/) is protected by all junior losses. The payoff structure is a series of overlapping nth-to-default instruments.

Dealers also used nth-to-default swaps to create synthetic [CDOs](/securitization/). Rather than buying actual loans or bonds, a dealer would assemble a basket of reference names and issue tranches backed by a waterfall of nth-to-default payoffs. This allowed rapid CDO creation without the operational complexity of warehousing and funding physical collateral.

## Valuation and risk

Pricing nth-to-default swaps requires a multi-name credit model. Standard approaches include:

- **Gaussian copula models**: Assume each name's default is driven by a latent factor plus idiosyncratic noise; correlated defaults emerge through the latent factor.
- **Jump-diffusion models**: Default times are modeled as random jump arrivals, with [correlation](/systemic-risk/) reflecting the intensity of the jumps.
- **Historical simulation**: Calibrate default frequencies and timing from past credit cycles.

The challenge is parameter uncertainty. [Correlation](/systemic-risk/) is not directly observable (equity correlations are a proxy but often unstable); recovery rates vary by seniority and industry; the probability of default depends on forward [credit spreads](/credit-spread/), which are volatile.

Dealers often use stress testing to bound losses. They might compute the expected loss under a baseline scenario, then recalculate assuming correlations are 25% or 50% higher. In 2007–2008, many dealers found that their stress bounds were grossly insufficient; realized losses far exceeded the high-correlation scenarios.

## Market context and usage

Nth-to-default swaps trade primarily in the [OTC market](/over-the-counter-market/), with dealers acting as market makers. The market is most active during periods of tight [credit spreads](/credit-spread/) and low [volatility](/historical-volatility/), when investors are hungry for yield and willing to buy protection on higher-n swaps.

During crises or high-stress regimes, liquidity dries up. A dealer trying to exit a large long nth-to-default position in stressed markets may find few willing buyers and must accept steep discounts. The illiquidity of multi-name [credit derivatives](/credit-default-swap/) was a major source of losses during the 2008 crisis—dealers holding large books of nth-to-default swaps and other structured credit products found them difficult to value or exit.

Post-crisis, the market has been modest. Regulatory [capital-adequacy](/capital-adequacy/) charges on structured credit discourage dealer risk-taking, and clients remain wary of the [correlation](/systemic-risk/) model risk. Nth-to-default swaps remain useful for genuine hedging (e.g., a syndicate bank protecting a loan portfolio), but speculative issuance is a fraction of pre-2008 levels.

## See also

<div class="wiki-seealso">

### Closely related

- [Credit Default Swap](/credit-default-swap/) — single-name credit derivative; n-th-to-default extends it to multiple names
- [Credit-Linked Note](/credit-linked-note/) — funded instrument that may embed n-th-to-default logic
- [Single-Tranche CDO](/single-tranche-cdo/) — structure often using n-th-to-default payoff logic
- [ABS CDO](/abs-cdo/) — securitization that relies on multi-name correlation and default waterfalls
- [Securitization](/securitization/) — the broader structure into which n-th-to-default swaps embed
- [Credit Spread](/credit-spread/) — the yield premium on reference entities; critical to swap pricing
- [Correlation](/systemic-risk/) — drives n-th-to-default pricing and risk

### Wider context

- [Credit Risk](/credit-risk/) — the fundamental risk all credit derivatives transfer
- [Systemic Risk](/systemic-risk/) — how correlated defaults in a crisis can trigger widespread losses
- [Over-the-Counter Market](/over-the-counter-market/) — where n-th-to-default swaps trade
- [Liquidity Risk](/liquidity-risk/) — primary challenge in exiting n-th-to-default positions
- [Financial Crisis of 2008](/great-depression/) — when n-th-to-default models failed catastrophically

</div>
