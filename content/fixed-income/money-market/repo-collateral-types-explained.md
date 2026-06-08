---
title: "Repo Collateral: Treasuries, Agency Bonds, and MBS"
description: "Hierarchy of collateral used in repo markets—on-the-run Treasuries, agency bonds, and mortgage-backed securities—and how collateral quality affects repo rate and haircut."
keywords:
  - repo collateral types
  - collateral hierarchy repo
  - treasury repo haircut
  - agency mbs repo
  - repo market collateral
image: /svg/fixed-income.svg
---

*In a **repurchase agreement** (**repo**), one party sells securities to another with a promise to buy them back at a higher price, usually within days or weeks. The collateral—the securities sold—determines the [**repo rate**](/repurchase-agreement/) (the interest cost) and the **haircut** (the discount from market value). The safest collateral (on-the-run [U.S. Treasury bonds](/treasury-bond/)) commands the tightest repo rates and smallest haircuts, while riskier collateral (mortgage-backed securities, corporate bonds, equities) faces wider rates and deeper haircuts. Understanding collateral hierarchy is essential for money-market traders, [custodians](/custodian/), and [fund managers](/mutual-fund/) who rely on repo to finance holdings and manage [liquidity](/liquidity-risk/).*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Repo Collateral Hierarchy — key facts</div>

<img src="/svg/fixed-income.svg" alt="An abstract editorial mark for fixed income." />

<div class="wiki-infobox-caption">Collateral quality shapes the cost and availability of short-term financing in repo markets.</div>

|   |   |
|---|---|
| **On-the-run US Treasuries** | ~1–2% haircut; repo rate = Fed funds + 5–10 bps |
| **Off-the-run Treasuries** | ~1–3% haircut; repo rate = Fed funds + 20–30 bps |
| **Agency bonds** | ~2–5% haircut; repo rate = Fed funds + 30–50 bps |
| **MBS (mortgage-backed securities)** | ~3–7% haircut; repo rate = Fed funds + 50–100 bps |
| **Corporate bonds** | ~5–15% haircut; repo rate = Fed funds + 100–250 bps |
| **Equities** | ~10–30% haircut; repo rate = Fed funds + 200–400 bps |

</aside>

## The collateral hierarchy

The repo market enforces a strict pecking order based on perceived safety, [liquidity](/liquidity-risk/), and [counterparty risk](/counterparty-risk/). At the top sit U.S. Treasuries; at the bottom, equities and distressed debt.

**On-the-run US Treasuries**
These are the most recently auctioned Treasury bonds and bills in each maturity bucket (2-year, 5-year, 10-year, etc.). They are the most liquid, most actively traded U.S. government debt instruments. In the repo market, they receive the tightest haircuts (1–2%) and the lowest rates—often just a few basis points above the [federal funds rate](/federal-funds-rate/). If the Fed funds rate is 5.25%, an on-the-run 10-year Treasury might repo at 5.30–5.32%. The reason: the U.S. government will not default, and these securities trade in enormous volume, so their market value is not in question.

**Off-the-run Treasuries**
Older Treasury bonds that are no longer the most recently issued. A 10-year Treasury issued six months ago is "off-the-run" once the next quarterly auction delivers a newer version. Off-the-run bonds are still backed by the full faith and credit of the U.S. government, but they trade in lower volumes and are less immediately convertible to cash. They face slightly higher haircuts (1–3%) and higher repo rates (Fed funds + 20–30 bps). The differential is small but real.

**Agency bonds (Federal Home Loan Bank, Federal Farm Credit, etc.)**
Issued by government-sponsored enterprises (GSEs)—entities created or chartered by Congress to support specific lending (mortgages, farm credit, housing). Although not explicitly backed by the U.S. Treasury, they carry an implicit government guarantee: the market and Congress assume the government will not allow them to default. Agency bonds face haircuts of 2–5% and repo rates of Fed funds + 30–50 bps. The extra 20–40 bps versus Treasuries reflects the slightly elevated [counterparty risk](/counterparty-risk/).

**Mortgage-backed securities (MBS)**
Securities representing claims on pools of [residential mortgages](/residential-real-estate/). Issued or guaranteed by GSEs (Fannie Mae, Freddie Mac, Ginnie Mae), they are safer than corporate debt but riskier than Treasuries because they carry [prepayment risk](/prepayment-risk/) (borrowers may refinance early) and [extension risk](/duration/) (falling rates extend duration). MBS face haircuts of 3–7% and repo rates of Fed funds + 50–100 bps. The haircut variation depends on the [coupon](/coupon-rate/), age, and current price of the MBS; agency-guaranteed MBS are safer than non-agency (private-label) MBS.

**Corporate bonds and credit**
Bonds issued by non-government entities carry true [credit risk](/credit-risk/) and [default](/default-rate/) risk. Even [investment-grade corporate bonds](/corporate-bond/) face haircuts of 5–15% and repo rates of Fed funds + 100–250+ bps. The spread widens with credit quality: a [BBB-rated bond](/credit-rating/) might repo at Fed funds + 100 bps, while a [BB-rated or CCC-rated bond](/high-yield-bond-rating-distribution/) could exceed Fed funds + 300 bps or not repo at all.

**Equities**
Stocks can be rehypothecated (lent out) in repo markets, but they carry severe haircuts—10% to 30% or more, especially for volatile small-cap stocks—and high repo rates (Fed funds + 200–400+ bps). Most institutional investors avoid using equities as repo collateral due to the cost.

## Why haircuts matter

A haircut is a discount applied to the market value of collateral to protect the lender (repo buyer) if the borrower defaults and the collateral must be liquidated. Here is a concrete example:

**Scenario: Financing a Treasury portfolio**
- You own $100 million in on-the-run 10-year Treasuries (market value).
- You repo them out at a 2% haircut.
- You receive $98 million in cash from the repo buyer.
- In return, you pay the repo buyer the agreed repo rate (say, 5.30% annually).
- After one week, you repay the $98 million + interest (~$10,000) and recover your Treasury collateral.

The 2% haircut means the lender can sell $98 million of your $100 million Treasuries if you fail to repay, recover the $98 million, and still own $2 million in profits as a cushion. If Treasury prices fall 1%, the lender loses only 1% on the collateral sold—well within the cushion.

Compare that to repo financing with MBS:

**Scenario: Financing an MBS portfolio**
- You own $100 million in [MBS](/mortgage-backed-security/) (market value).
- You repo them out at a 5% haircut.
- You receive $95 million in cash.
- You pay the repo buyer 5.75% annually (Fed funds + 50 bps).
- After one week, you repay the $95 million + interest (~$10,400) and recover your MBS collateral.

If MBS prices fall 3% (a not-uncommon weekly move), the lender's $95 million in recovered collateral is worth only $92.15 million—a $2.85 million loss. The 5% haircut cushion ($5 million) absorbs this, but with less margin of safety than Treasury repo.

## How collateral quality affects the repo rate

The repo rate is not fixed by the Fed (except in rare crises when the Fed operates a [standing repo facility](/repurchase-agreement/)). Instead, it emerges from supply and demand: borrowers who want cheap financing and lenders who want to earn yield negotiate bilaterally or through brokers.

Collateral quality shapes these negotiations in two directions:

**Borrower's side:** If you have pristine collateral (on-the-run Treasuries), lenders will lend you cash cheaply because their risk is minimal. If you have distressed corporate debt, lenders will demand a higher rate or refuse to lend at all.

**Lender's side:** If you lend cash secured by Treasuries, you earn a thin rate (barely above the Fed funds rate) but your principal is almost completely safe. If you lend against corporate bonds or equities, you can demand a much higher rate to compensate for the risk.

During periods of market stress—such as the 2008 financial crisis or the March 2020 COVID-19 panic—collateral hierarchy tightens dramatically. Repo rates for safe collateral (Treasuries, agencies) might fall as [flight-to-quality](/intraday-correlation-breakdown/) intensifies; simultaneously, rates on riskier collateral spike or access dries up entirely. In March 2020, corporate bond repo rates exceeded 4–5% above the Fed funds rate, and many corporate issuers could not finance through repo at any price.

## Collateral transformation and re-use

Most repurchase agreements include a **right to rehypothecate**—the lender (repo buyer) can use your collateral as collateral in another repo transaction or sale. This multiplies the effective supply of scarce collateral and reduces financing costs for borrowers with access to high-quality collateral.

A trader at a [hedge fund](/hedge-fund/) might finance their positions by entering a tri-party repo arrangement with a [custodian](/custodian/). The custodian holds the collateral and lends cash overnight, then rehypothecates the collateral to a bank. The bank uses those Treasuries in another repo to borrow from a [money-market fund](/money-market-fund/). The same Treasury has now become the collateral for three transactions—which increases the supply of available financing (beneficial) but also creates [systemic risk](/systemic-risk/) if the chain breaks (one party defaults, and liquidity dries up).

## Collateral scarcity and special repo

In certain markets, specific securities become so scarce and valuable that their repo rates turn **special**—they fall below the general (collateral-neutral) repo rate. For example, if on-the-run 10-year Treasury supply is tight and demand to finance is high, that specific maturity might repo at Fed funds − 50 bps (a reverse carry), while off-the-run 10-years repo at Fed funds + 10 bps. This signals the market's urgency to borrow or lend that specific collateral.

Understanding which securities trade special is crucial for [portfolio managers](/mutual-fund/) seeking to optimize short-term financing costs and for traders seeking to exploit collateral [arbitrage](/algorithmic-trading/) opportunities.

## See also

<div class="wiki-seealso">

### Closely related

- [Repurchase agreement](/repurchase-agreement/) — the mechanics of repo transactions and market structure.
- [Counterparty risk](/counterparty-risk/) — why haircuts are needed and collateral safety matters.
- [Custodian](/custodian/) — the intermediary that holds repo collateral and manages tri-party agreements.
- [Treasury bond](/treasury-bond/) — the safest and most commonly used repo collateral.
- [Mortgage-backed security](/mortgage-backed-security/) — agency MBS as repo collateral.
- [Federal funds rate](/federal-funds-rate/) — the benchmark against which repo rates are quoted.

### Wider context

- [Money market fund](/money-market-fund/) — a major supplier of cash in repo markets.
- [Hedge fund](/hedge-fund/) — a heavy user of repo to finance positions.
- [Liquidity risk](/liquidity-risk/) — collateral scarcity can impair repo market function.
- [Systemic risk](/systemic-risk/) — interconnected repo markets and rehypothecation chains.
- [Flight to quality](/intraday-correlation-breakdown/) — how collateral hierarchy tightens in crises.

</div>
