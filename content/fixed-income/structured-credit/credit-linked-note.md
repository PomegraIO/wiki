---
title: "Credit-Linked Note"
description: "A bond that embeds a credit default swap, passing default risk from a reference entity to note holders in exchange for higher yield."
keywords:
  - credit derivative
  - structured credit
  - default risk
  - cds embedded
  - credit-linked note cln
image: /svg/fixed-income.svg
---

*A **credit-linked note** is a funded debt instrument that combines a conventional bond with a [credit default swap](/credit-default-swap/), allowing an investor to take on the credit risk of a reference entity in return for an enhanced coupon. The investor receives regular payments and principal return—unless the reference entity defaults, triggering a loss.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Credit-Linked Note — key facts</div>

<img src="/svg/fixed-income.svg" alt="An abstract editorial mark for fixed income and structured instruments." />

<div class="wiki-infobox-caption">A bond that passes credit risk to the investor and rewards it with higher yield.</div>

|   |   |
|---|---|
| **What it is** | A funded debt instrument embedding a [credit default swap](/credit-default-swap/) on a reference entity |
| **Coupon structure** | Base coupon plus a spread or modified coupon tied to default probability |
| **Default trigger** | Credit event of the reference entity (bankruptcy, payment default, or restructuring) |
| **Payoff at maturity** | Full principal minus any [credit event](/credit-event-sovereign/) loss, or zero if a default occurs |
| **Typical issuer** | Banks and [securities](/securities-and-exchange-commission/) dealers |
| **Risk to investor** | Entire exposure to the reference entity; no diversification within the note |
| **Use case** | Speculators or hedge funds taking directional credit views without capital requirements |

</aside>

## The mechanics: bond + CDS wrapped in one wrapper

A credit-linked note is structurally simple. An investor buys a note from a dealer or bank, receiving coupons tied to a reference entity's credit risk. Behind the scenes, the issuer has entered a [credit default swap](/credit-default-swap/) on that same entity—one in which the note buyer implicitly provides default protection. If the reference entity suffers a [credit event](/credit-event-sovereign/) (default, bankruptcy, or major restructuring), the note's principal is adjusted downward or wiped entirely, compensating the issuer for the [CDS](/credit-default-swap/) payout obligation.

The appeal is transparency and simplicity. Rather than buying a distressed bond issued by the reference entity itself, an investor can take a pure view on that entity's creditworthiness through a single security. The note is funded—the dealer holds the note's proceeds and invests them, typically in ultra-safe [treasury securities](/treasury-bond/) or cash—so there is no counterparty risk between note buyer and dealer (the dealer simply transfers the credit risk via the embedded swap).

## Why investors accept the bet

CLN coupons are substantially higher than [risk-free rates](/interest-rate/). An investor might earn 5–7 percentage points more than a comparable [Treasury bond](/treasury-bond/), compensating for the risk that the reference entity defaults and the note's principal is lost. For credit traders or hedge funds seeking exposure to a specific name, CLNs offer a standardized, liquid way to short credit without short-selling the debt itself or posting collateral for a CDS.

Institutional investors—particularly those unable to enter [CDS](/credit-default-swap/) contracts directly—find CLNs convenient. A pension fund or insurance company can access credit derivatives through a conventional fixed-income vehicle on its balance sheet, sometimes more easily than through swap markets.

## The risk is concentrated

A critical drawback: the note carries full exposure to the reference entity. If the reference entity is a bank and it fails, the note holder loses principal entirely, often alongside the issuer (which may have held the entity's bonds as collateral). The 2008 financial crisis exposed this danger sharply; many CLNs on lehman brothers and Bear Stearns evaporated when those firms collapsed.

The investor also assumes [counterparty risk](/counterparty-risk/) on the dealer—if the dealer defaults before the credit event, the note's legal status in bankruptcy can be unclear. A [treasury bond](/treasury-bond/) has no such risk; a CLN's creditworthiness depends partly on the issuer.

CLNs are also relatively illiquid compared to single-name bonds or [CDS](/credit-default-swap/) contracts. If an investor wishes to exit mid-term, it must find a willing buyer at prevailing credit spreads—and fewer investors track CLNs than plain CDS. This liquidity cost can widen the effective loss on exit.

## Structure variations

A basic CLN pays a fixed coupon and returns principal at maturity unless a credit event occurs. Some variants are more complex. A "barrier" CLN might be triggered only if the reference entity's [credit spread](/credit-spread/) breaches a certain level, or if the entity's [credit rating](/credit-rating/) drops below a threshold. A "multi-name" CLN embeds protection on multiple entities, similar to an [nth-to-default swap](/nth-to-default-swap/) or [single-tranche CDO](/single-tranche-cdo/).

The dealer's exposure structure varies too. In a "structural CLN," the dealer holds the actual debt of the reference entity and replicates the CLN's cash flows through the bond's interest and principal. In a "synthetic CLN," the dealer is neutral on the credit and simply warehouses the default risk—funding itself by borrowing or taking repo [financing](/debt-financing/). Most modern CLNs are synthetic, giving the dealer pure duration and spread management.

## Why dealers issue CLNs

From the issuer's perspective, a CLN is a funding and risk management tool. A bank may have a large directional credit view on an entity (say, it thinks a company's [credit rating](/credit-rating/) is too low) and needs to hedge or monetize that view without posting heavy [capital-adequacy](/capital-adequacy/) charges. A CLN lets the bank transfer the risk to an investor while raising funding at a tight spread.

In the 2000s pre-crisis era, CLNs proliferated—particularly those referencing mortgages and [mortgage-backed securities](/mortgage-backed-security/), which later became a mechanism for distributing [structured credit](/securitization/) exposure through a seemingly safer wrapper. Many of the worst losses in the crisis came from CLNs on mortgage pools and [ABS CDOs](/abs-cdo/).

## Market context

CLNs are issued primarily in dollars and euros by major global banks and dealers. The market is concentrated: a handful of issuers dominate. Primary issuance typically occurs when credit spreads are tight and investor appetite for risk is high; it slows dramatically during stress periods.

Pricing a CLN requires solving for the [spread](/credit-spread/) that compensates for the expected loss on default. Dealers use [valuation](/discounted-cash-flow-valuation/) models calibrated to [CDS](/credit-default-swap/) spreads and the credit quality of the reference entity. If a reference entity's CDS spread widens sharply, the CLN's implied value falls—yet the note owner cannot easily sell it at that mark without accepting a steep loss.

The secondary market for CLNs is thin. Most note holders are buy-and-hold investors, and dealers sometimes actively trade them, but the market liquidity is a fraction of that for plain CDS or corporate bonds. Pricing disparities between CLNs and equivalent CDS positions can persist for long periods, a sign of the structural illiquidity.

## See also

<div class="wiki-seealso">

### Closely related

- [Credit Default Swap](/credit-default-swap/) — the derivative underlying a CLN
- [Single-Tranche CDO](/single-tranche-cdo/) — another custom credit-linked structure used by dealers
- [Nth-to-Default Swap](/nth-to-default-swap/) — multi-name credit derivatives often embedded in CLNs
- [ABS CDO](/abs-cdo/) — structured credit products that sometimes took the CLN form during the 2000s
- [Securitization](/securitization/) — the broader family of structured finance instruments
- [Credit Spread](/credit-spread/) — the excess yield compensating CLN buyers for default risk
- [Credit Rating](/credit-rating/) — the reference entity's creditworthiness, central to CLN valuation
- [Counterparty Risk](/counterparty-risk/) — the risk the CLN issuer defaults before a credit event

### Wider context

- [Bond](/bond/) — the fixed-income instrument structure underlying a CLN
- [Corporate Bond](/corporate-bond/) — plain debt issued by a reference entity, an alternative to CLN exposure
- [Credit Risk](/credit-risk/) — the fundamental risk CLNs transfer to investors
- [Structured Finance](/securitization/) — the ecosystem in which CLNs trade
- [Financial Crisis of 2008](/great-depression/) — when many CLNs embedded in mortgage pools suffered catastrophic losses

</div>
