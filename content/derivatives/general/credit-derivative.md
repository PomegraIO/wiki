---
title: "Credit Derivative"
description: "A contract that transfers credit risk from one party to another, allowing the holder to hedge or speculate on the likelihood of default by a borrower or issuer."
keywords:
  - credit risk
  - default risk transfer
  - credit default swap
  - credit derivatives
  - counterparty risk
  - bond hedging
---

*A bank holds a corporate [bond](/wiki/bond/) from a weakening company and worries about default. Instead of selling the bond (which might signal distress to the market), the bank can buy a **credit derivative**—a contract that pays off if the company defaults, offsetting the bank's loss. Credit derivatives are the machinery by which credit risk is isolated, priced, and transferred among investors. They exist in many forms, but the [credit default swap](/wiki/credit-default-swap/) (CDS) is the most famous.*

<div class="wiki-hatnote">Not to be confused with [interest rate derivatives](/wiki/interest-rate-swap/) (which hedge rate risk) or [equity derivatives](/wiki/option/) (which hedge stock price risk). Credit derivatives are specifically about default and credit events.</div>

<aside class="wiki-infobox">

| Feature | Detail |
|---------|--------|
| **Primary instrument** | Credit default swap (CDS) |
| **Risk transferred** | Default probability and recovery rate |
| **Typical payer** | Bond holder or lender seeking protection |
| **Typical receiver** | Investor willing to assume credit risk |
| **Premium (spread)** | Quoted in basis points per year (e.g., 150 bps) |
| **Notional size** | Global CDS market: ~$10 trillion |
| **Regulation** | Dodd-Frank requires central clearing for standardized CDS |

</aside>

## How a CDS works

The simplest credit derivative is the [credit default swap](/wiki/credit-default-swap/). Here is the mechanics:

1. **Setup:** A bank holds \$10 million in bonds from Company X. The bank buys protection by paying a periodic premium (say, 150 basis points, or \$150,000 per year) to a counterparty (the "protection seller").

2. **Normal case:** If Company X does not default, the bank pays the premium for the full term and receives no payout. The protection seller keeps the premium—a pure profit.

3. **Default case:** If Company X defaults before the contract ends, the protection seller pays the bank \$10 million (or the difference between the bond's par value and its recovery value in bankruptcy). The bank is made whole.

The protection buyer (the bank) has transferred credit risk to the protection seller. The bank's exposure to Company X's default is now hedged.

## Pricing credit derivatives

The CDS premium reflects the market's estimate of the probability of default. A CDS on a very safe company (e.g., Germany's sovereign debt) might trade at 5 basis points (0.05% per year). A CDS on a distressed company (near bankruptcy) might trade at 2,000 basis points (20% per year).

The spread depends on:
1. **Credit quality:** Higher default probability → higher spread.
2. **Maturity:** Longer-dated CDS typically carry higher spreads because there is more time for default to occur.
3. **Recovery rate:** Assets expected to be recovered in bankruptcy → lower spread. Full loss → higher spread.
4. **Liquidity:** Widely traded CDS have tighter spreads; illiquid CDS have wider spreads.

When a company's credit conditions worsen (earnings decline, leverage increases), the CDS spread widens—the protection becomes more expensive because the market reprices default probability upward.

## CDS as a trading instrument

While many CDS are used for hedging (protecting bond holders), many are used for speculation. A trader who believes a company's credit quality will improve can buy protection (pay the premium), betting that the spread will narrow and they can sell the protection at a profit.

Conversely, a trader who believes credit is strong can sell protection, collecting the premium.

This trading activity is both a feature and a risk. The feature: it provides liquidity and efficient price discovery. The risk: speculative leveraged bets can amplify credit market volatility. During the 2008 financial crisis, CDS spreads on major banks blew out to 500+ basis points as traders panicked and speculators doubled down on short bets.

## Other credit derivative structures

Beyond the vanilla CDS, credit derivatives include:

**Credit-linked notes (CLNs).** A bond with an embedded credit derivative. An investor buys a bond that pays a high coupon, but if a reference credit (a specified company) defaults, the bond's principal is reduced. The investor accepts credit risk in exchange for higher yield.

**First-to-default baskets.** A credit derivative on a basket of credits. It pays off if the *first* company in the basket defaults. The premium is cheaper than buying individual CDS on each company.

**Index CDS.** A single contract that represents the default risk of 125 or 225 major companies (like the CDX indices). A trader can get broad-based credit exposure in one transaction.

**Credit spread options.** An option on the CDS spread itself. A trader buys the right to buy (or sell) protection at a specified spread, betting that the spread will move favorably.

## The 2008 crisis and regulatory reform

Credit derivatives were a central player in the 2008 financial crisis. Credit default swaps on mortgage bonds and financial institutions exploded in value as credit deteriorated. Lehman Brothers, AIG, and others faced massive losses.

The problem: CDS contracts were not centrally cleared, so if one counterparty failed, the other counterparty was left exposed. AIG, which had sold massive amounts of CDS protection to banks, went insolvent and required a government bailout. The banking system was fragile because counterparty risk was not transparent.

After 2008, the [Dodd-Frank Act](/wiki/dodd-frank-act/) mandated that standardized CDS be centrally cleared through a clearinghouse (like the OCC or LCH.Clearnet). This reduced counterparty risk: instead of Bank A owing Bank B money on a failed CDS, both owe the clearinghouse, which is backed by capital buffers and daily margin settlement.

This reform made the market safer but also more regulated and expensive—dealers now hold capital against CDS positions and pass costs to clients.

## CDS and corporate bonds

A corporate bond and CDS on the same company should be tightly linked. If a bond yields 5% and CDS protection costs 200 basis points, the "credit spread" (yield minus risk-free rate) should roughly equal the CDS spread. If the bond yields too high relative to CDS, there is an arbitrage: buy the bond, buy protection, and earn the spread.

However, dislocations occur. During stress periods (March 2020, Russia invasion of Ukraine in Feb 2022), bond and CDS markets decoupled—credit spreads widened more than CDS spreads, or vice versa—as liquidity dried up and forced selling hit bonds harder than derivatives.

## Systemic risks

Because CDS are widely traded and leveraged, concentrations can build. During the 2008 crisis, most CDS protection on AIG was sold to a small number of major banks. When AIG failed, those banks faced coordinated losses, threatening the system.

Regulators now monitor "counterparty concentration risk"—the exposure of the largest firms to any single protection seller. Similarly, they track which credits have the most CDS protection outstanding, flagging potential systemic risk if that credit fails suddenly.

## Credit derivatives and bond market dynamics

The existence of credit derivatives can change bond market behavior. A bondholder who can easily buy CDS protection is more likely to hold a credit-risky bond—the hedge reduces risk. This can keep credit spreads compressed (narrower, suggesting less risk) even as fundamentals deteriorate, because holders are hedged.

Conversely, when hedging is expensive or unavailable, bondholders are more cautious, and spreads widen. The 2023 regional banking crisis saw credit spreads widen sharply partly because protection was expensive and hedging capacity was limited.

<div class="wiki-seealso">

### Closely related
- [Credit Default Swap](/wiki/credit-default-swap/) — The primary credit derivative
- [Credit Risk](/wiki/credit-risk/) — The underlying risk being transferred
- [Credit Spread](/wiki/credit-spread/) — Bond yield premium reflecting default risk
- [Default Rate](/wiki/default-rate/) — Empirical frequency of defaults

### Wider context
- [Bond](/wiki/bond/) — The underlying instrument often hedged with credit derivatives
- [Counterparty Risk](/wiki/counterparty-risk/) — Risk that protection seller fails
- [Central Counterparty Clearing](/wiki/central-counterparty-clearing/) — Infrastructure managing CDS risk
- [Dodd-Frank Act](/wiki/dodd-frank-act/) — Regulation following 2008 crisis
- [Derivatives](/wiki/derivatives-exchange-crypto/) — Broader category of derivative instruments
- [Financial Crisis](/wiki/lehman-brothers-collapse/) — Credit derivatives were central to 2008

</div>