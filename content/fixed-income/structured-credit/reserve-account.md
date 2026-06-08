---
title: "Reserve Account"
description: "Cash held within a securitization to cover periodic shortfalls and protect bondholders before assets are liquidated or subordinated tranches are impaired."
keywords:
  - reserve account
  - securitization
  - subordination
  - loss coverage
  - liquidity buffer
  - tranches
  - credit enhancement
image: "/svg/fixed-income.svg"
---

*A **reserve account** is cash locked inside a [securitization](/securitization/) vehicle, available to cover shortfalls when collateral payments fall short of bond obligations. It is a liquidity buffer: when losses occur or collections lag, the reserve is drawn down before senior bondholders are asked to take a haircut. Once drawn, the reserve must be replenished from deal cash flow — otherwise the vehicle is naked against the next shock.*

## The cash timing problem

In an ideal securitization, collateral payments arrive exactly when bonds mature, and losses never happen. Reality is messier. A [mortgage](/mortgage-backed-security/) pool might have:

- Seasonal payment patterns (some borrowers pay in clusters)
- Occasional delays (processor errors, weekend holdups)
- Unexpected defaults (a neighbourhood's unemployment spikes)
- Recovery lags (a foreclosed house takes six months to sell)

Without a reserve account, any gap between cash in and obligations out would force the servicer to advance funds out of pocket — and if they don't (or can't), bondholder payments are late. A late payment is a breach of the bond indenture, potentially triggering [defaults](/credit-risk/) on supposedly safe senior bonds.

The reserve account solves this: it holds surplus cash from the prior period, ready to fill gaps in the current period.

## How the reserve is funded and drawn

A reserve account is typically established at closing with an initial deposit — often 0.5% to 2% of the collateral pool value. This amount varies by asset class: higher for credit card receivables (which have lumpy, uncertain cash flows) and lower for plain-vanilla mortgages (which are predictable).

Throughout the life of the deal, the reserve is replenished from [excess spread](/credit-spread/) — the leftover interest income after paying bondholders and servicers. If a pool of mortgages earns 4.5% and the bonds are 2%, that 2.5% spread (minus servicing fees) becomes available to rebuild the reserve.

When collateral payments are light — say, a cohort of borrowers delays or defaults — the servicer draws from the reserve to make bondholders whole that month. The reserve shrinks. On the next strong collection month, excess spread flows back in to rebuild it.

If the reserve is fully drawn and stays empty, bondholder payments are at risk. This is why [rating agencies](/credit-rating/) stress-test reserve accounts: they model scenarios where draw-downs cluster and replenishment stalls.

## Reserve accounts and credit ratings

A large reserve account enhances the credit quality of a securitization, especially for senior tranches. Consider two identical mortgage pools: one with a 1% reserve and one with a 3% reserve. The pool with the fatter reserve can absorb larger or longer payment disruptions without shorting the senior bonds. Agencies will rate its senior tranche higher for the same collateral quality.

The reserve is not a [subordination](/subordination/) mechanism — it doesn't sacrifice one investor for another. Instead, it is a *timing buffer*. It protects all bondholders, senior and junior, from temporary cash shortfalls. But because senior bonds are paid first anyway, senior bondholders benefit the most from having a reserve; they are the last to be touched by either a reserve draw or [subordination](/subordination/).

## Drawing down vs. topping up

The sequence matters. When losses occur, there are competing claims on the reserve:

1. First, the reserve covers operational shortfalls (servicer advances, trustee fees, etc.).
2. Next, it covers interest shortfalls (if collections are too light to pay coupon).
3. Last, it absorbs principal shortfalls or losses.

In a healthy deal, the reserve rarely goes below its initial threshold. But in a stressed deal — think a [mortgage-backed security](/mortgage-backed-security/) during a recession — the reserve is drawn continuously and may never be replenished. Eventually, it is exhausted, and then [subordination](/subordination/) takes over: losses flow through [tranches](/tranche/) in waterfall order until senior bonds are hit.

Some deals include "triggers" that accelerate the replenishment of reserves if they fall below a threshold. If the reserve drops below 1.5% of the pool, every available excess dollar flows to the reserve before any goes to junior investors. This is a protective mechanism: it ensures the reserve is not starved in a downturn.

## Reserve accounts in different structures

**Mortgage securitizations** typically carry small reserves (0.5–1%) because mortgages are seasoned, predictable, and have low monthly volatility.

**Credit card securitizations** carry much larger reserves (2–5%) because credit card receivables are high-velocity: monthly balances fluctuate wildly, charge-offs are lumpy, and payment patterns shift with economic sentiment.

**Corporate loan securitizations** (like [Collateralized Debt Obligations](/cash-flow-cdo/)) also carry substantial reserves (1–3%) to cover the possibility that several borrowers default in the same quarter.

The reserve size is a function of collateral stability: the more volatile the cash flows, the larger the reserve must be to credibly absorb timing mismatches.

## The cost of holding reserves

A reserve account is "dead money." It sits in a low-yielding account (often earning near-zero interest) and is not deployed to buy more collateral or pay down bonds faster. For the sponsor or originator, a large reserve reduces the present value of the deal.

Some deals try to minimize reserves by using servicer advances — the servicer lends to the deal short-term to cover shortfalls, then is repaid from the next month's cash. But this shifts the risk: now the trustee and servicer must be confident the servicer won't run out of liquidity and default on its advances.

Other deals use committed [lines of credit](/credit-risk/) in place of full cash reserves. A bank agrees to lend to the vehicle if cash is short. This is cheaper than hoarding cash, but it adds [counterparty risk](/counterparty-risk/): if the bank fails, the credit line may vanish.

In practice, most securitizations keep some blend: a modest reserve account plus a backstop credit line.

## Reserve accounts and priority

The reserve account sits outside the normal [tranche](/tranche/) waterfall. It is not senior debt or junior debt; it is a segregated pool. When drawn, it is typically replenished before any excess spread flows to junior tranches or equity. This gives the reserve an implicit priority: protecting the ability of the deal to pay all tranches on schedule is the first use of cash.

Some deals have tiered reserves: a primary reserve that covers interest and operating shortfalls, and a secondary reserve that covers principal losses. This reflects the priority: keeping interest paid is more critical to the deal's health than absorbing losses (which eventually hit equity anyway).

## The lesson for investors

For a bondholder, the existence and size of a reserve account is a material credit feature. A securitization with a robust, regularly replenished reserve is safer than one with a skimpy reserve that was drawn down and never topped up. When reading a securitization prospectus, the reserve account disclosure — initial size, replenishment mechanics, and draw triggers — is worth careful attention.

A reserve is not a substitute for solid collateral or adequate [subordination](/subordination/). But it is a crucial piece of the credit structure, often the difference between a tranche that survives a mild downturn and one that fails.

## See also

<div class="wiki-seealso">

### Closely related

- [Subordination](/subordination/) — the waterfall of tranche losses
- [Securitization](/securitization/) — bundling loans into tranched bonds
- [Cash Flow CDO](/cash-flow-cdo/) — securitization based on collateral coupon and principal
- [Market Value CDO](/market-value-cdo/) — securitization based on mark-to-market tests
- [Tranche](/tranche/) — a single class of a securitized bond
- [Excess Spread](/credit-spread/) — interest income left after fees and coupon
- [Mortgage-Backed Security](/mortgage-backed-security/) — common securitization of mortgages

### Wider context

- [Bond](/bond/) — fixed-income security
- [Credit Rating](/credit-rating/) — agency assessment of default risk
- [Credit Risk](/credit-risk/) — risk of borrower default
- Collateral — assets backing a loan or bond
- [Liquidity Risk](/liquidity-risk/) — risk of inability to raise or deploy cash

</div>
