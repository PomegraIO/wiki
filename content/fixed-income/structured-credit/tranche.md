---
title: "Tranche"
description: "A slice or layer of a securitized debt pool with a specific priority in receiving payments and absorbing losses, ranked from senior (safest) to equity (riskiest)."
---

*A tranche is a tier in the hierarchy of a securitized debt structure. In a mortgage-backed security with $100 million in collateral, investors might buy the senior tranche ($80 million), the mezzanine tranche ($12 million), and the equity tranche ($8 million). As losses accumulate, the equity tranche absorbs the first losses, the mezzanine gets hit second, and the senior investors sleep soundly—unless losses explode past their cushion. Tranching is the engineering mechanism that allows structured finance to exist.*

## The waterfall principle

Every securitization defines a "waterfall"—a priority order for distributing cash and absorbing losses. Imagine a mortgage pool generating $5 million per month in principal and interest, but with 0.2% of mortgages defaulting monthly (a $100,000 loss on average). Each month, that cash flows according to the waterfall:

1. Servicer fees: $20,000
2. Senior tranche principal and interest: $2,000,000
3. Mezzanine tranche interest: $500,000
4. Subordinated tranche interest: $200,000
5. Equity tranche: gets the remainder

As long as defaults stay low, all tranches get paid. When defaults spike, the equity absorbs losses first. If that is exhausted, the subordinated tranche loses money. Only when losses exceed the subordinated + mezzanine cushion does the senior tranche suffer.

This is the entire point of tranching: to create safe (senior), risky (equity), and intermediate securities from the same underlying collateral.

## Seniority and ratings

Seniority determines credit rating. A senior tranche backed by 30% equity cushion (i.e., the equity + mezzanine tranches below equal 30% of total collateral value) typically earns an AAA rating from rating agencies. A mezzanine tranche with a 10% cushion below it might earn BBB. An equity tranche is unrated.

This mapping is not deterministic—it depends on the default severity the rating agency assumes, the recovery rate on defaulted collateral, and the credit quality of the underlying pool. A prime mortgage pool with historically 0.5% annual default rates can support a larger senior tranche than a subprime pool with 5% default rates. The waterfall is structured to match the risk to the rating.

Rating agencies publish methodologies explaining the loss severity assumptions for each asset class. A mortgage bond analyst can calculate: for a given default rate, loss severity, and prepayment rate, which tranches remain whole and which take losses.

## The investor trade-off

Senior tranches pay lower yields (wider bids from investors competing to own safe assets) but have low risk of principal loss. The expected return is modest but reliable. Mezzanine tranches pay higher yields and carry meaningful principal risk. The equity tranche is the riskiest—it is paid last and absorbs the first losses—but offers the highest yield potential if credit performance is strong.

For institutional investors, this menu means they can choose their risk level. A conservative pension fund might buy senior tranches at 80 basis points over Treasuries. A hedge fund might buy equity tranches, betting that the originator's conservative underwriting will deliver excess returns.

The originator typically retains the equity tranche initially (skin in the game) but often sells it to specialized equity investors—firms that focus on analyzing credit risk and pricing senior and mezzanine tranches appropriately. These equity buyers are compensated for their analysis and loss-taking.

## Overcollateralization and the subordination ratio

Tranching does not happen in a vacuum. It is paired with "overcollateralization"—issuing bonds whose face value is less than the collateral value. If $100 million in collateral backs $80 million in bonds, the 20% spread is the OC. This padding absorbs losses before any bondholder loses a cent.

The subordination ratio (or "subordination level") specifies how much junior collateral sits below each tranche. For a senior tranche, the subordination ratio might be 30%, meaning 30% of collateral value sits in junior tranches. For a mezzanine tranche, subordination might be 8%.

These ratios are calibrated using models. An originator (or rating agency) assumes a default rate, severity, and prepayment rate for the collateral, then calculates: what subordination ratio will ensure this tranche has less than a 0.1% probability of loss (for AAA ratings) or 1% probability (for BBB ratings)? The deal is then structured to hit those targets.

## Triggers and dynamic tranches

Modern securitizations often include "triggers"—events that change how the waterfall distributes cash. A common trigger is: if the monthly default rate exceeds 0.5%, cash that normally goes to the equity tranche gets redirected to pay down the senior tranche faster, creating a larger buffer.

Another common trigger: if the average FICO score of remaining borrowers (as originations prepay) falls below a threshold, the senior tranche gets paid principal faster. These triggers are built to protect senior investors by shrinking their exposure when credit risk rises.

Triggers introduce complexity—outcomes depend on whether thresholds are crossed—but they align incentives. The originator cannot ignore deteriorating credit; the waterfall automatically shifts to protection mode.

## Synthetic tranches

In some structured deals, particularly collateralized debt obligations, a tranche's risk is synthetically transferred via a [credit default swap](/wiki/credit-default-swap/). Rather than issuing a mezzanine bond, the issuer might issue a senior bond and buy a CDS that protects against losses in the mezzanine layer. This "synthetic tranche" transfers mezzanine risk to the CDS counterparty (often a bank or insurance company) without issuing physical securities.

Synthetic tranches are more flexible (risk can be transferred in any size) but introduce [counterparty risk](/wiki/counterparty-risk/)—if the CDS seller fails, the protection vanishes.

## Information barriers and conflict

Because an originator may retain the equity (lower tranche), a conflict of interest arises. The originator benefits if the deal performs well (excess spread flows to equity). Senior investors benefit if defaults are low. But the originator also has an incentive to pass bad loans into the securitization—if defaults are low, the equity makes money; if they are high, investors take the loss.

Post-2008 regulation (Dodd-Frank) requires originators to retain 5% of the credit risk of each securitization, aligning incentives: an originator cannot completely divorce itself from the credit consequences. But the 5% rule is a floor, not a ceiling, and some deals have larger originator stakes.

## Tranches in different asset classes

Mortgage securitizations typically issue 3–5 tranches. [Auto loan ABS](/wiki/asset-backed-security/) might have 4–6. Corporate [collateralized loan obligations](/wiki/collateralized-loan-obligation/) might have 6–10, with granular subordination layers reflecting the wider range of borrower credit quality.

The tranche structure is customized to the asset class. Mortgages with historical stability can have more junior tranches (wider equity) than credit cards with volatile defaults.

<div class="wiki-seealso">
<h2>See also</h2>
<h3>Closely related</h3>
<ul>
<li><a href="/wiki/securitization/">Securitization</a> — the process by which tranches are created.</li>
<li><a href="/wiki/structured-finance/">Structured Finance</a> — the practice of creating tranches to reshape risk.</li>
<li><a href="/wiki/subordination/">Subordination</a> — the legal priority that defines tranches.</li>
<li>Waterfall — the payment priority rule that distributes cash to tranches.</li>
<li><a href="/wiki/credit-rating/">Credit Rating</a> — how rating agencies assign ratings to each tranche.</li>
</ul>
<h3>Wider context</h3>
<ul>
<li><a href="/wiki/asset-backed-security/">Asset-Backed Security</a> — the market where tranches are traded.</li>
<li><a href="/wiki/mortgage-backed-security/">Mortgage-Backed Security</a> — the most common type of tranched security.</li>
<li><a href="/wiki/collateralized-debt-obligation/">Collateralized Debt Obligation</a> — another tranche-heavy securitization structure.</li>
</ul>
</div>
