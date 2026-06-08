---
title: "Prudential Treatment of Crypto Assets Under Basel Rules"
description: "How Basel Committee rules classify crypto assets into two groups and apply a 1,250% risk weight and exposure limits to bank holdings of unbacked tokens."
keywords:
  - crypto asset prudential treatment
  - basel committee rules
  - crypto risk weight
  - unbacked token
  - bank crypto exposure
  - basel capital requirements
image: /svg/risk.svg
---

*The **Basel Committee's prudential treatment of crypto assets** divides digital tokens into two regulatory groups—Group 1 ("stablecoins" meeting specific requirements) and Group 2 (all others)—and applies a punitive 1,250% risk weight to Group 2 holdings, making it extremely expensive for banks to hold volatile or unbacked tokens. The framework also imposes an exposure cap limiting aggregate crypto holdings to a small percentage of capital, reflecting concerns about [counterparty risk](/counterparty-risk/), [liquidity risk](/liquidity-risk/), and [operational risk](/operational-risk/).*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Basel Crypto Treatment — Key Facts</div>

<img src="/svg/risk.svg" alt="An abstract editorial mark for risk topics." />

<div class="wiki-infobox-caption">Basel rules make most crypto too expensive for banks to hold without massive capital buffers.</div>

|   |   |
|---|---|
| **Group 1 stablecoins** | Issuer creditworthiness, reserve backing, regulatory oversight |
| **Group 2 crypto** | Bitcoin, Ethereum, unbacked tokens, anything else |
| **Risk weight — Group 1** | 2% (similar to short-term [Treasury bonds](/treasury-bond/)) |
| **Risk weight — Group 2** | 1,250% (requires $12.50 of capital per $1 of holdings) |
| **Exposure cap** | Group 2 ≤ 1% of [Tier 1 capital](/tier-1-capital/); Group 1 ≤ 15% |
| **Purpose** | Prevent [systemic risk](/systemic-risk/) from volatile, lightly-regulated tokens |

</aside>

## The Basel Committee and Banking Prudence

The Basel Committee on Banking Supervision sets international standards for bank [capital adequacy](/capital-adequacy/), ensuring lenders maintain sufficient reserves to absorb losses. Basel III rules (finalized 2010–2019) codified how banks measure [risk](/risk-weighted-assets/) across different asset classes. Equities carry one risk weight; [corporate bonds](/corporate-bond/) carry another; [Treasury bonds](/treasury-bill/) carry the lowest.

Cryptocurrencies presented a novel challenge: no credit rating, no issuer backstop, extreme price volatility, nascent custody infrastructure, and no central bank lender-of-last-resort function. In early 2023, the Basel Committee issued guidance on crypto treatment, finalized in June 2023 and adopted by most major regulators globally.

The solution was to treat crypto as a high-risk asset class requiring far more capital than traditional securities.

## Group 1 versus Group 2: The Dividing Line

**Group 1: Qualifying Stablecoins**
A stablecoin meets Group 1 status if it meets ALL of these criteria:
- The issuer has a [credit rating](/credit-rating/) from a recognized agency (Moody's, S&P, Fitch) rated A- or higher, OR the issuer is a [central bank](/central-bank/) or multilateral development bank
- The stablecoin is fully backed by reserves (100% on a daily basis)
- Reserves are held in central bank deposits or low-risk government bonds
- The issuer has transparent, audited reserve disclosures
- The stablecoin is legally redeemable on a 1:1 basis

Examples: USDC (issued by Coinbase, backed by US Treasury and bank deposits), EURC (Euro-backed), tokens issued by central banks. As of mid-2024, very few private stablecoins meet Group 1 criteria.

**Group 2: Everything Else**
All other crypto assets fall into Group 2: Bitcoin, Ethereum, existing stablecoins that do not meet the strict criteria (including USDT, which lacks a sufficiently high credit rating on the issuer itself), any emerging token, and any stablecoin that is not backed 1:1 or not held in sufficiently safe reserves.

## The 1,250% Risk Weight: Capital Explosion

A 1,250% risk weight is nearly a non-starter for bank holdings of Group 2 crypto. To understand the economics, recall that [risk-weighted assets](/risk-weighted-assets/) determine the denominator of a bank's capital ratio.

A bank with $100 billion in assets and a 10.5% minimum [Tier 1 capital](/tier-1-capital/) ratio must hold $10.5 billion in capital. If the bank holds $1 million in Bitcoin:

- Under the 1,250% rule, that $1 million counts as $12.5 million in risk-weighted assets
- To maintain a 10.5% ratio, the bank must hold an additional $1.3125 million in capital
- That means $1 million in Bitcoin requires $1.31 million in capital—a $310,000 capital charge for one dollar of Bitcoin held

In practice, this makes proprietary trading in crypto for a bank's own account prohibitively expensive. A bank could hold crypto only if it expected extraordinary appreciation to justify the capital drag.

Contrast this with a US Treasury bond. A one-year Treasury carries a 0% risk weight, meaning no additional capital is required. A corporate bond rated BB carries roughly 100%, so a $1 million position requires about $105,000 in capital. The 1,250% weight on Group 2 crypto is an order of magnitude stricter.

## The Exposure Cap: Hard Limits

Beyond the risk weight, Basel imposes absolute exposure limits:

- **Group 1 stablecoins:** Up to 15% of Tier 1 capital
- **Group 2 crypto:** Up to 1% of Tier 1 capital

For a mid-sized bank with $10 billion in Tier 1 capital, this means:
- Group 1 stablecoins: $1.5 billion maximum
- Group 2 crypto: $100 million maximum

These caps are hard floors. A bank cannot hold more than these amounts regardless of capital ratios. The cap serves as a structural limit on systemic exposure.

## Implications for Crypto Trading and Banking

**Trading desk operations:** Most large banks have crypto trading desks. These are not restricted outright, but holdings of volatile crypto must be reconciled with the exposure cap. If a bank is at 0.9% of Tier 1 capital in Group 2 holdings, it cannot add more without reducing other positions.

**Stablecoin versus Bitcoin:** The rules create a stark incentive to use only Group 1 stablecoins (or fiat currency) for settlement and liquidity purposes, rather than Bitcoin or Ethereum, which are Group 2. Institutions may prefer stablecoins for internal money movement and USD peg preservation.

**Custody and settlement:** Banks offering [custody](/custodian/) services for crypto clients face questions about whether holding client assets counts toward the exposure cap. Regulators have suggested that if a bank is a true custodian and does not take ownership risk, the asset might not count toward the bank's own limits. However, this remains an area of regulatory clarification.

**Merchant acquiring:** Banks that settle payments in crypto (e.g., accepting Bitcoin for merchant acquiring) may accumulate positions. If exposure grows beyond the cap, they must sell or rehedge immediately.

## Why Such Strict Rules?

The prudential concern is multi-faceted:

**Volatility:** Bitcoin and Ethereum have experienced 50%+ drawdowns in months. A bank holding such assets faces rapid mark-to-market losses that erode capital.

**Counterparty risk:** Cryptocurrency exchanges and stablecoin issuers have no deposit insurance and minimal [capital adequacy](/capital-adequacy/) rules. If FTX or another major custodian fails, banks holding assets there suffer immediate loss.

**Liquidity risk:** While Bitcoin and Ethereum are liquid in normal times, in a stress event (market crash, regulatory shock, exchange failure), bid-ask spreads widen and selling large positions may be impossible without accepting steep discounts.

**Operational risk:** Crypto custody involves private keys, smart contracts, and custody infrastructure with no legacy of proven resilience. The risk of theft, hacking, or technical failure is material.

**Regulatory and reputational risk:** Regulators in many countries view crypto with skepticism. Banks with large crypto exposures face political pressure and potential regulatory action.

## Global Adoption and Variation

Most major regulators have adopted or are adopting Basel's framework. The US [Federal Reserve](/federal-reserve/), Office of the Comptroller of the Currency, and FDIC have issued guidance aligned with Basel. The European Union, UK, Singapore, and others have issued parallel rules. A few jurisdictions (El Salvador, some Caribbean jurisdictions) have encouraged crypto adoption, but they lack the systemic banking safeguards that Basel implements.

The upshot is that for a globally active bank, the de facto standard is the 1,250% rule and the 1% exposure cap. Deviance is costly and invites regulatory friction.

## See also

<div class="wiki-seealso">

### Closely related

- Basel Committee Rules — the international body setting prudential standards for banks
- [Capital Adequacy](/capital-adequacy/) — the framework for measuring bank capital sufficiency
- [Risk-Weighted Assets](/risk-weighted-assets/) — the mechanism by which Basel translates holdings into capital requirements
- [Tier 1 Capital](/tier-1-capital/) — the highest-quality bank capital against which exposure caps are measured

### Wider context

- [Cryptocurrency Exchange](/cryptocurrency-exchange/) — where Group 1 and Group 2 assets trade
- [Counterparty Risk](/counterparty-risk/) — a key concern driving the high risk weight on unbacked tokens
- [Liquidity Risk](/liquidity-risk/) — the danger of forced selling in stressed markets
- [Federal Reserve](/federal-reserve/) — US authority enforcing Basel prudential rules domestically

</div>
