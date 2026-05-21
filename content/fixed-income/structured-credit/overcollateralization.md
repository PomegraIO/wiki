---
title: "Overcollateralization"
description: "The practice of backing securitized bonds with a collateral pool whose value exceeds the bond's face amount, creating a cushion that absorbs potential losses before investors suffer."
---

*Overcollateralization (OC) is a form of financial insurance, built into the structure of a securitization. If $100 million in mortgages back $85 million in bonds, the 15% surplus—the excess collateral—absorbs losses. A borrower defaults, but the loss is cushioned by OC. It is the simplest and most direct form of structural protection in modern securitized credit.*

## How overcollateralization protects bondholders

In a straightforward securitization, the issuer would issue bonds equal to the collateral value, making it a 1:1 ratio. But if defaults occur—even small defaults—bondholders lose money. To prevent this, issuers maintain an OC ratio: if collateral is $100 million and bonds are $85 million, the OC ratio is 17.6% ($15M ÷ $85M).

Each month, as borrowers pay principal, the collateral pool shrinks. If the pool declines to $90 million while bonds are still $85 million, OC shrinks to 5.9%. If the pool declines further to $84 million, OC becomes zero and the next dollar of loss hits the equity or subordinate tranche.

Losses erode OC first. A pool with $100 million in collateral backing $80 million in bonds has 25% OC. If $5 million in mortgages default with 100% severity, collateral falls to $95 million, OC shrinks to 18.75%, and the equity (or the portion of collateral allocated to equity) absorbs the loss.

## Setting OC at issuance

The OC ratio is set at securitization issuance based on the originator's forecast of losses. An originator issuing a mortgage securitization might assume a 1% lifetime default rate, 60% loss severity (60% of defaulted mortgage principal is lost to the lender after foreclosure and sale), and calculate:

Expected lifetime loss = 1% × 60% = 0.6% of collateral.

To ensure rated tranches stay whole, the originator might set overall OC to 3%, ensuring that losses up to 3% hit equity or subordinate tranches. The senior tranche sits above 3% of OC.

Different asset classes have different loss assumptions. Auto loan securitizations might assume 2% default with 40% severity (a lower-severity asset because cars can be repossessed and resold quickly). Credit card securitizations might assume 4% default with 100% severity (cardholders walk away). OC is calibrated accordingly.

## Dynamic OC and triggers

In many securitizations, OC is not static. It changes with collateral quality. Some deals include "OC triggers": if OC falls below a threshold (say, 15%), the structure shifts to a "OC maintenance mode" where excess cash flow that would normally go to junior tranches instead goes toward maintaining OC.

For example:

- Normal case: Monthly excess cash (after paying all tranches) goes to the equity holder.
- OC trigger breached: Monthly excess cash is diverted to pay down senior bonds faster, or placed in a reserve account, until OC recovers.

These triggers align the originator's incentives with investor safety. If OC deteriorates, the originator's profits (which come from excess cash) shrink until OC is restored. This nudges originators to monitor collateral quality.

## Variation by asset class and seniority

OC ratios vary dramatically by asset class:

- **Mortgages**: 5–15% OC for senior tranches; 20–40% for the entire deal (including mezzanine and equity).
- **Auto loans**: 3–8% for senior; 15–25% overall.
- **Credit cards**: 10–20% for senior; 30–50% overall.
- **CLO loans**: 2–5% for senior; 15–25% overall.

Senior tranches require less OC cushion because they sit atop subordinate bonds. A senior tranche with 5% OC and a 10% mezzanine cushion below has 15% total protection.

## Turnover and OC tightening

As collateral amortizes (principal gets paid down) and the bonds are paid down, OC ratios shrink over time, all else equal. In a securitization with $100 million collateral and $80 million bonds (20% OC), if 10% of collateral prepays, collateral falls to $90 million. If bonds are paid down proportionally, bonds fall to $72 million, and OC becomes ($90M – $72M) / $72M = 25%.

But if collateral prepays faster than bonds amortize (common when rates fall and borrowers refinance), OC can actually rise. Conversely, if collateral prepays slowly while bond principal is paid, OC shrinks.

In rising-rate environments (where prepayment is slow), OC can deteriorate over time as bond principal repayment outpaces collateral paydown. This is a slow squeeze that eventually eats away investor cushions.

## OC as an earning asset

The collateral in an overcollateralized securitization generates returns. If $100 million in mortgages yield 4%, they generate $4 million in annual cash. Bonds pay out perhaps $3.4 million (interest on the bonds), leaving $600K in excess spread. This excess spread is the compensation to the originator (or to the equity holder if the equity has been sold).

But some originators and investors manage OC by periodically selling a portion of the excess collateral and using proceeds to pay down senior bonds or reinvest. This "OC management" allows more sophisticated investors to harvest yield from the OC while maintaining target OC ratios.

## The 2008 lesson: OC was insufficient

The subprime mortgage crisis revealed that OC alone is not a failsafe. Many deals were structured with 10–15% OC, which seemed adequate based on historical loss data. But when the crisis hit, default rates reached 10–15% with 50%+ severity, total losses of 5–7.5%, wiping out OC, tranches, and equity.

The lesson: OC must be calibrated to stressed, not historical, loss scenarios. Post-crisis securitizations use more conservative loss assumptions and higher OC ratios. A 2% default assumption with 60% severity might have been reasonable in 2005; a 6% default assumption with 70% severity is more prudent now.

Transparent deal disclosure (including loan-level data) allows modern investors to stress-test OC themselves. A sophisticated investor can calculate: what happens if defaults hit 5% instead of the issuer's 2% assumption? How much of my tranche survives?

## Combining OC with other protections

OC is one tool in a structured deal's toolkit. It works alongside:

- **Tranching**: Subordination provides additional cushions.
- **Reserve accounts**: Cash set aside to cover shortfalls.
- **Interest-rate hedges**: Swaps that protect against cash-flow disruption.
- **Trigger events**: Automatic actions that protect remaining OC.

A deal with 10% OC, 4 tranches with multiple subordination layers, a $2M reserve account, and tight OC triggers is far safer than a deal with 10% OC and no other protections.

<div class="wiki-seealso">
<h2>See also</h2>
<h3>Closely related</h3>
<ul>
<li><a href="/wiki/securitization/">Securitization</a> — the process that establishes OC ratios.</li>
<li><a href="/wiki/tranche/">Tranche</a> — subordination works in tandem with OC.</li>
<li><a href="/wiki/asset-backed-security/">Asset-Backed Security</a> — OC is a key feature of ABS structures.</li>
<li><a href="/wiki/collateralized-debt-obligation/">Collateralized Debt Obligation</a> — CDOs use OC extensively.</li>
<li><a href="/wiki/credit-rating/">Credit Rating</a> — rating agencies determine required OC to achieve ratings.</li>
</ul>
<h3>Wider context</h3>
<ul>
<li><a href="/wiki/structured-finance/">Structured Finance</a> — OC is a structural protection tool.</li>
<li><a href="/wiki/default-rate/">Default Rate</a> — OC is calibrated to expected defaults.</li>
<li><a href="/wiki/loss-severity/">Loss Severity</a> — OC depends on assumptions about severity.</li>
</ul>
</div>
