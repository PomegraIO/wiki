---
title: "Eurodollar Futures vs Fed Funds Futures"
description: "Compare Eurodollar and Fed Funds futures: reference rates, quotation methods, contract specifications, and how traders use each to hedge or speculate on short-term rates."
keywords:
  - eurodollar futures vs fed funds futures
  - eurodollar futures
  - fed funds futures
  - short-term interest rate futures
  - monetary policy trading
image: /svg/derivatives.svg
---

*The **Eurodollar futures vs Fed Funds futures** distinction matters because they reference different interest rates and serve different hedging needs. Eurodollar [futures](/futures-contract/) track offshore US dollar lending rates ([LIBOR](/libor/) or SOFR), while Fed Funds futures track the effective fed funds rate. Eurodollar is older and was once more liquid; Fed Funds is now the standard for US monetary-policy trading. Understanding which contract to use depends on whether you are hedging commercial paper, managing a bank's short-term funding, or betting on Fed decisions.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Eurodollar vs Fed Funds Futures — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives." />

<div class="wiki-infobox-caption">Two highways to the same destination, with different map conventions.</div>

|   |   |
|---|---|
| **Eurodollar futures** | Reference rate: 3-month SOFR or LIBOR legacy | Contract: $1 million notional | Price: 100 - (implied rate %) |
| **Fed Funds futures** | Reference rate: Effective Fed Funds Rate (EFFR) | Contract: $5 million notional | Price: 100 - (arithmetic mean rate %) |
| **Maturity** | Both traded out 3+ years | Monthly and quarterly contracts |
| **Quotation** | Both quoted as 100 minus rate; 1 basis point = $25 per Eurodollar, $12.50 per Fed Funds |
| **Typical use** | Eurodollar: corporate funding, banks | Fed Funds: Fed rate expectations, macro trading |
| **Primary exchange** | CME (Chicago Mercantile Exchange) |

</aside>

## The Rate Behind Each Contract

The fundamental difference lies in the **reference rate**. 

**Fed Funds futures** are based on the [effective federal funds rate](/federal-funds-rate/) (EFFR), the volume-weighted average rate at which banks lend reserve balances to each other overnight. This is the rate the [Federal Reserve](/federal-reserve/) targets with open-market operations. When the Fed says it is raising or cutting rates, it is moving the target range for the Fed Funds rate. Fed Funds futures allow traders to bet directly on Fed decisions and to hedge short-term funding costs tied to overnight rates.

**Eurodollar futures** (historically) referenced the London Interbank Offered Rate (LIBOR) for three-month US dollar deposits made offshore. LIBOR was the rate at which large banks could borrow unsecured from each other for three months. Since LIBOR's transition to [SOFR](/sofr/) (the Secured Overnight Financing Rate) in 2021, Eurodollar futures now reference three-month term SOFR, though the contract name persists. SOFR is also an overnight rate (like EFFR), but Eurodollar contracts quote the forward-looking three-month rate, not the overnight rate.

The relationship between them: EFFR (overnight) and three-month term SOFR are related but distinct. The three-month SOFR rate is typically higher than EFFR because lenders require compensation for duration risk and the uncertainty of future overnight rates over three months. The spread between the two — the **term premium** — varies with economic conditions and liquidity.

## Quotation and Pricing Mechanics

Both contracts are quoted identically in price format but reference different underlying rates.

**Price quotation:** Both are quoted as **100 minus the implied interest rate**. If three-month SOFR is 4.50%, a Eurodollar contract quotes at 100 - 4.50 = 95.50. If the effective Fed Funds rate is 5.00%, a Fed Funds contract quotes at 100 - 5.00 = 95.00.

**Tick size and value:** One basis point (0.01 on the price scale) in a Eurodollar contract is worth $25 per contract ($1 million notional × 0.0001 / 4 quarters). In a Fed Funds contract, one basis point is worth $12.50 per contract ($5 million notional × 0.0001 / 12 months). A trader buying Eurodollar contracts profits if rates fall (contract price rises); a trader buying Fed Funds contracts profits if rates fall.

**Daily settlement:** Both are [cash-settled](/cash-settlement/), meaning there is no physical delivery of an underlying deposit. Instead, positions are marked to market daily, and the final settlement price is the arithmetic mean of the daily effective Fed Funds rate (for Fed Funds contracts) or the daily three-month SOFR rate (for Eurodollar contracts) over the contract month, published by the CME.

## Contract Specifications and Maturities

**Fed Funds futures** are monthly contracts, with the contract month running from the first to the last day of a calendar month. A trader who wants to hedge or speculate on September's average Fed Funds rate buys a September contract. Contracts are listed out to 18–24 months into the future.

**Eurodollar futures** are quarterly contracts, with expirations in March, June, September, and December. They roll forward by quarter rather than month. Eurodollar contracts are listed out 3 or more years into the future, making them useful for long-dated hedges.

This difference in roll convention reflects their original use cases. Eurodollar futures grew out of the offshore banking market, where three-month deposits are the standard funding window; quarterly expirations align. Fed Funds futures (introduced later by the CME) use monthly expirations because the Fed's policy meetings occur roughly monthly and traders want to reference specific meeting windows.

## Liquidity and Trading Activity

Historically, **Eurodollar futures** were the dominant short-term interest-rate [futures contract](/futures-contract/) globally. They were the liquid hedge for offshore dollar borrowers, cross-currency traders, and macro funds building rate views. In the 1990s and 2000s, the Eurodollar complex (the stack of quarterly contracts from nearby to far-forward) was among the most actively traded derivatives instruments.

**Fed Funds futures** were introduced by the CME in 1988 but remained less liquid until the financial crisis (2007–2009). As the Fed's policy moves became the focus of market trading (especially after zero rates and quantitative easing), and as Fed communication increased, Fed Funds futures liquidity surged. In the post-2020 period, Fed Funds futures are now more liquid than Eurodollar futures, especially in the near-term (first 1–2 years).

The shift reflects macro and market structure changes: hedgers increasingly care about Federal Reserve policy decisions (which move EFFR), while the Eurodollar market — tied to offshore LIBOR and later SOFR term rates — serves a smaller constituency (international banks, corporate treasuries managing offshore funding).

## Hedging and Trading Use Cases

**Eurodollar futures** are still used by:
- Banks managing three-month funding costs (matching assets and liabilities)
- Corporate treasury departments hedging commercial paper programs (which often roll on 3-month terms)
- Cross-currency traders hedging basis risk between USD and other currencies over a 3-month horizon
- Mortgage originators hedging the duration of their pipelines

A bank expecting to issue a three-month certificate of deposit (CD) in three months buys Eurodollar futures today. If three-month SOFR rises, the bank's borrowing cost will rise when it issues the CD, but the futures gain offsets the loss. This is a classic **basis hedge**.

**Fed Funds futures** are used by:
- Macro traders and hedge funds betting on Federal Reserve policy (rate hikes, cuts, or holds)
- Banks and treasuries managing overnight funding costs and reserve balances
- Investors forming expectations about the Fed's reaction function to inflation, employment, or growth
- Systematic strategies that dynamically adjust exposure to near-term monetary policy

A trader who believes the Fed will cut rates by 50 basis points over the next six months buys Fed Funds futures at each contract month. If the Fed cuts as expected, the average fed funds rate will fall, the futures price will rise, and the trader profits.

## The LIBOR-to-SOFR Transition and Eurodollar Contracts

The transition from LIBOR to SOFR (completed in 2021–2023) created complexity. Eurodollar futures contracts ceased referencing LIBOR and now reference **three-month term SOFR**. However, many old Eurodollar contracts maturing before the transition deadline were cash-settled using LIBOR, and the basis between LIBOR and SOFR created persistent trading dynamics.

The CME also launched **SOFR futures**, which reference overnight SOFR rather than three-month term SOFR. These compete directly with Fed Funds futures for hedging overnight rate exposure, though they have not yet captured as much liquidity. The Federal Reserve has signaled a preference for SOFR over LIBOR and for overnight rate derivatives over term-rate derivatives, as overnight rates are more directly observed and less prone to manipulation.

For a treasurer or trader today, the relevant question is: **Do I want exposure to overnight or three-month rates?** If overnight, use Fed Funds futures (or overnight SOFR futures). If three-month, use Eurodollar futures (which now reference term SOFR). This question determines the contract choice more than Eurodollar vs. Fed Funds historical dominance.

## Relative Performance and Basis

Because both contracts reference US short-term rates (one overnight, one three-month), they are closely correlated. However, they do not move perfectly in lockstep. The **basis** — the difference in rates between them — reflects term premium, credit and liquidity spreads, and expectations about the path of overnight rates over three months.

In normal times, three-month SOFR is 10–30 basis points above EFFR. In a liquidity crisis, the spread can widen dramatically (SOFR surges relative to EFFR) or compress (the spread narrows). A trader can exploit basis movements by going long one contract and short the other, a spread trade that generates returns if the basis normalizes or widens.

This basis relationship also means that **hedging mismatches** are possible. A bank with a 3-month liability (a CD that matures in 90 days) might hedge using Fed Funds futures if Eurodollar liquidity is poor, but the hedge is imperfect because the rates diverge. This is a form of [basis risk](/basis-risk/).

## Regulatory and Market Structure Changes

The [Dodd-Frank Act](/dodd-frank-act/) (2010) and subsequent regulations increased capital and margin requirements for derivatives trading and encouraged central clearing through futures exchanges rather than bilateral OTC markets. This benefited **exchange-traded futures** like Eurodollar and Fed Funds, which became cheaper and more standardized compared to bespoke [interest-rate swaps](/interest-rate-swap/).

The Federal Reserve's communication and policy clarity also increased the relevance of Fed Funds futures. When the Fed is precise about its policy path (forward guidance), traders use Fed Funds futures to price in expected Fed moves. This has made Fed Funds futures the primary vehicle for monetary policy trading, especially in the immediate aftermath of Fed announcements.

## See also

<div class="wiki-seealso">

### Closely related

- [Futures Contract](/futures-contract/) — mechanics and terminology of futures exchanges
- [Federal Funds Rate](/federal-funds-rate/) — the rate targeted by the Federal Reserve
- [SOFR](/sofr/) — the benchmark overnight rate replacing LIBOR
- [LIBOR](/libor/) — the historic three-month offshore lending rate (now retired)
- [Interest Rate Swap](/interest-rate-swap/) — OTC alternative for hedging longer-term rate exposure

### Wider context

- [Federal Reserve](/federal-reserve/) — the monetary authority; Fed decisions move both contracts
- [Carry Trade](/carry-trade/) — trading strategy exploiting interest-rate differentials
- [Basis Risk](/basis-risk/) — risk from imperfect correlation in hedges
- [Monetary Policy](/monetary-policy/) — the Fed's actions and forward guidance
- Central Counterparty — the clearinghouse that settles exchange-traded futures

</div>
