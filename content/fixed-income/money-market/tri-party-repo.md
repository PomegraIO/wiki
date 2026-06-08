---
title: "Tri-Party Repo"
description: "A repurchase agreement structure where a third-party clearing bank manages collateral allocation and settlement between two counterparties."
keywords:
  - tri-party repurchase agreement
  - repo market mechanics
  - collateral management
  - clearing bank intermediary
image: /svg/fixed-income.svg
---

*A **tri-party repo** is a [repurchase agreement](/general-collateral-repo/) in which a clearing bank (usually the Federal Reserve or a private clearing agent) holds the collateral and manages its allocation, settlement, and margining between the cash lender and the securities seller—making the transaction simpler for both parties and reducing operational risk.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Tri-Party Repo — key facts</div>

<img src="/svg/fixed-income.svg" alt="An abstract editorial mark denoting fixed-income markets and debt instruments." />

<div class="wiki-infobox-caption">The clearing bank stands between two parties, holding collateral and managing the daily reshuffling of securities and cash that keeps the global short-term funding market running.</div>

|   |   |
|---|---|
| **What it is** | A short-term [secured loan](/debt-financing/) where a bank (the clearing agent) holds the securities and manages transfers of collateral and cash. |
| **Parties involved** | Cash lender (investor), securities seller (borrower), and clearing bank (intermediary). |
| **Also called** | Triparty repo, tri-party agreement; distinct from [bilateral repo](/general-collateral-repo/) (two parties only) and [general collateral repo](/general-collateral-repo/) (specific Treasury collateral). |
| **Primary collateral** | Government bonds, [mortgage-backed securities](/mortgage-backed-security/), corporate bonds; pooled or specified by the lender. |
| **Market role** | Accounts for roughly 50 percent of the U.S. repo market; essential for [overnight](/sofr/) and short-term dollar funding. |
| **Key agents** | Clearing banks: Federal Reserve (tri-party agent), Bank of New York Mellon, JPMorgan. |
| **Interest rate** | Typically below [LIBOR](/libor/); fixed or floating, determined at deal inception and marked daily. |
| **Duration** | Usually [overnight](/sofr/) to two weeks; some longer-term triparty trades exist but are less common. |

</aside>

## Why the third party matters

A standard [repurchase agreement](/general-collateral-repo/) is a simple two-party transaction: Alice holds a Treasury bond and needs cash; Bob lends her the cash and takes the bond as collateral; in one day (or one week), Alice pays Bob back plus interest, and Bob returns the bond. If Alice owns many bonds and is borrowing large amounts, she might prefer not to physically hand over each security. Instead, she wants a single arrangement where a middleman (the clearing bank) holds all her collateral in a central vault and automatically allocates bits of it to different lenders as needed. This is tri-party repo.

The clearing bank offers several services. First, it holds the collateral in its depository. Second, it verifies that the collateral meets the lender's requirements—no bonds that have defaulted, no illiquid securities, no excessive concentration in one issuer. Third, it calculates how much additional collateral Alice must deposit if her existing pledges decline in value ([margin call](/margin-call-forex/)). Fourth, it settles the cash loan and collateral swaps electronically, reducing paperwork and counterparty confusion. Without a clearing bank, Alice would have to negotiate separately with each lender about which bonds to pledge, what happens if prices move, and how to handle settlement—a nightmare at scale.

## How the daily reset works

A typical tri-party repo begins in the morning. Alice (a securities dealer or financial institution) contacts the clearing bank and says, "I want to borrow $1 billion cash for the day." The clearing bank identifies suitable collateral from Alice's vault—say, $1.05 billion in assorted Treasuries (the extra 5 percent is a [haircut](/cost-of-debt/), protecting the lender against price moves). At 9 a.m., the clearing bank transfers those bonds to a segregated account and electronically notifies the cash lender (Bob, a money-market [mutual fund](/mutual-fund/), a [hedge fund](/hedge-fund/), or another bank) that collateral has been pledged. Bob wires $1 billion to Alice.

By 5 p.m., the reverse happens. Alice must return $1 billion plus interest (say, $1,000,274 for an [overnight](/sofr/) loan at 2.74 percent annualised). The clearing bank verifies the funds and moves them to Bob's account; simultaneously, it releases the collateral back to Alice's vault. The bond transfer and cash transfer happen in lockstep—no one is exposed mid-day to counterparty failure.

Over the course of the day, if the Treasury bonds pledged have lost value (say, [interest rates](/interest-rate/) rose and bond prices fell), the clearing bank's daily valuation will show that Alice's collateral no longer fully covers the $1 billion loan. Alice must deposit more collateral immediately. This is the [margin call](/margin-call-forex/). If Alice cannot post more bonds or cash, the clearing bank can liquidate some of her collateral and return the shortfall to Bob—automatically and without legal drama.

## The advantage over bilateral repo

A bilateral [repurchase agreement](/general-collateral-repo/) between two parties is simpler to negotiate but operationally cumbersome. Alice and Bob must agree on which specific bonds are acceptable, how often to revalue them, and what the [haircut](/cost-of-debt/) is. If Alice wants to borrow from Bob and Charlie simultaneously, she must make separate arrangements with each. If prices move sharply, Alice must renegotiate [margin](/margin-call-forex/) terms with each lender separately. If one lender demands more collateral at the worst moment, Alice is stuck.

Tri-party repo solves this by pooling collateral. Alice uploads her securities to the clearing bank's vault once. Any lender that trusts the clearing bank (and the clearing bank's collateral management process) can immediately tap this pool. Lenders do not argue about [haircuts](/cost-of-debt/)—the clearing bank applies standard, published haircuts (e.g., 2 percent for Treasury bonds, 5 percent for investment-grade corporates). Collateral allocation is automatic and impartial. Margin calls happen on a schedule (typically daily), not when one lender panics.

For borrowers like major dealers and banks, this is essential. Dealers rely on short-term repos to finance massive [inventory](/inventory-turnover/) positions—thousands of bonds worth billions of dollars. Without a clearing bank managing collateral, the operational complexity would be unmanageable. For lenders like [money-market funds](/mutual-fund/), tri-party repo is safer because the clearing bank's vaults and settlement systems are heavily regulated and tested. There is far less risk of a bond being "double pledged" (sold as collateral to two different lenders) or of settlement failure.

## Systemic importance and stress

Tri-party repo is the circulatory system of short-term global funding. On any given day, roughly $1–2 trillion is locked in tri-party transactions at the Federal Reserve's tri-party agents (mainly Bank of New York Mellon). This funding is essential: large banks use it to finance their bond inventory; dealers use it to fund [carry trades](/leverage-ratio-forex/); money-market [mutual funds](/mutual-fund/) earn [yields](/current-yield/) on their cash.

In normal times, tri-party repo is so routine that nobody notices it. Cash borrowers do not go out of business; lenders do not panic; collateral prices stay within expected ranges; [margin calls](/margin-call-forex/) are handled matter-of-factly. But in market stress, tri-party repo can become a transmission mechanism for contagion.

In March 2020, when the COVID-19 crisis hit and markets froze, the tri-party repo market experienced acute stress. Lenders (especially [mutual funds](/mutual-fund/)) tried to withdraw from overnight repo, fearing that securities dealers might fail. Dealers simultaneously faced wider [bid-ask spreads](/bid-ask-spread/), making their collateral harder to liquidate. The Federal Reserve had to step in and provide emergency liquidity through [quantitative easing](/quantitative-easing/) and expanded [reverse-repo](/general-collateral-repo/) facilities. Without these interventions, the tri-party repo market might have seized, and the entire financial system would have struggled to access short-term funding.

The 2008 crisis revealed tri-party weaknesses too. Bear Stearns and Lehman Brothers, both major tri-party borrowers, suddenly lost access to funding. Lenders—[hedge funds](/hedge-fund/), [money-market funds](/mutual-fund/), and banks—refused to roll over their repo loans. The clearing banks were forced to liquidate collateral at distressed prices, crystallising huge losses. Had the Federal Reserve not intervened with emergency lending and asset purchases, the tri-party system might have collapsed.

## The role of the Federal Reserve

The Federal Reserve is the largest tri-party clearing agent for the U.S. government bond market. Banks and large dealers maintain accounts at the Fed and pledge Treasuries, [mortgage-backed securities](/mortgage-backed-security/), and other eligible collateral. The Fed's triparty service is operated by the Banking Operations division and is heavily scrutinised for operational reliability. Every transaction is backed by the full faith and credit of the U.S. government (implicitly, if not explicitly).

Private clearing agents—Bank of New York Mellon and JPMorgan Chase—operate tri-party systems for less-regulated collateral (corporate bonds, equities, non-U.S. government securities). They face rigorous oversight from banking regulators and must maintain large capital cushions to absorb losses if a borrower defaults. During the 2008 crisis, these private agents came under pressure when collateral values fell and borrowers could not meet margin calls. Regulators pushed for stronger risk controls and more conservative haircuts; the system has become more resilient since then, though stress events continue to test it.

## Tri-party vs. general collateral repo

Tri-party repo and [general collateral repo](/general-collateral-repo/) are distinct. In [general collateral repo](/general-collateral-repo/), the lender specifies that the collateral must be U.S. Treasuries (any eligible Treasury, not a specific bond), and the [interest rate](/interest-rate/) is typically the GC rate—a benchmark that reflects the cost of dollar funding against any Treasury. In tri-party repo, the collateral can be anything the lender is willing to accept (Treasuries, mortgage-backed securities, corporate bonds, even equities, depending on the agreement), and the [interest rate](/interest-rate/) is negotiated between the borrower and lender (or set by the clearing bank as an administered rate).

GC repo is simpler and more liquid; it trades actively on electronic platforms and is the reference rate for [repurchase agreement](/general-collateral-repo/) markets. Tri-party repo is bespoke and relationship-driven; borrowers and lenders negotiate terms, and the clearing bank executes. As a result, GC repo rates are transparent and easy to track; tri-party rates are more opaque.

## Modern pressures and evolution

Tri-party repo has faced pressure from regulation and competition. Post-2008 reforms required clearing banks to reduce their intraday exposure to borrowers (if a borrower defaults, the clearing bank should not be left holding the bag). The Federal Reserve mandated twice-daily margining and wider haircuts for riskier collateral. These rules made tri-party repo more expensive and complex.

Simultaneously, the rise of electronic trading platforms for bilateral repo and the introduction of [central clearing](/tri-party-repo/) for standardised contracts has fragmented the tri-party market. Some borrowers now prefer to negotiate bilateral repo directly; others use [exchange-traded](/etf/) repo futures to hedge [interest rate](/interest-rate/) risk.

Yet tri-party repo remains indispensable. No other system can match the operational efficiency and risk management of a clearing bank holding collateral centrally and managing daily resets across multiple lenders and borrowers. As long as modern finance relies on short-term secured lending, tri-party repo will be at the heart of it.

## See also

<div class="wiki-seealso">

### Closely related

- [General collateral repo](/general-collateral-repo/) — benchmark short-term funding rate against any Treasury; simpler and more liquid than tri-party
- [Eurodollar deposit](/eurodollar-deposit/) — competing short-term funding mechanism; offshore dollar deposits rather than collateralized loans
- [SOFR](/sofr/) — secured overnight financing rate based on actual tri-party and bilateral repo transactions; the modern benchmark replacing LIBOR
- [Margin call](/margin-call-forex/) — the daily revaluation and collateral adjustment that defines tri-party repo mechanics
- [Haircut](/cost-of-debt/) — the lender's discount on collateral value to protect against price moves
- [Mortgage-backed security](/mortgage-backed-security/) — commonly used as tri-party collateral, especially in stress periods when [Treasury](/treasury-bond/) collateral is scarce
- [Counterparty risk](/counterparty-risk/) — managed by the clearing bank's pooling and daily settlement

### Wider context

- [Federal Reserve](/federal-reserve/) — the primary tri-party clearing agent and emergency liquidity provider in crises
- [Monetary policy](/monetary-policy/) — Fed actions that ripple through repo rates and [short-term funding](/treasury-bill/) availability
- [Money-market fund](/mutual-fund/) — major tri-party lenders seeking yields on cash
- [Hedge fund](/hedge-fund/) — both lenders and borrowers in tri-party repo
- [Financial crisis of 2008](/mortgage-backed-security/) — when tri-party repo markets froze and the Fed intervened massively
- [Liquidity risk](/liquidity-risk/) — the danger that tri-party repo funding evaporates in stress
- [Systemic risk](/systemic-risk/) — tri-party repo's role as a critical infrastructure for modern finance

</div>
