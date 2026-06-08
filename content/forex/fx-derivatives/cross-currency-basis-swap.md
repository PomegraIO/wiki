---
title: "Cross-Currency Basis Swap"
description: "Floating-for-floating swaps that exchange interest payments in two currencies, where the basis reflects the cost of synthetic currency conversion."
keywords:
  - cross-currency swap
  - basis swap forex
  - currency basis
  - synthetic financing
  - fx swap spread
image: "/svg/forex.svg"
---

*A **cross-currency basis swap** is a floating-for-floating interest rate swap that exchanges cash flows denominated in two different currencies, allowing two parties to synthetically borrow or lend in a foreign currency without spot exchange. The "basis" — the spread added to the floating rate of the weaker-demand currency — moves away from zero when banks find it cheaper to fund one currency than another, creating profitable arbitrage for currency traders and genuine funding pressures for multinational corporations.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Cross-Currency Basis Swap — key facts</div>

<img src="/svg/forex.svg" alt="An editorial mark for foreign exchange instruments." />

<div class="wiki-infobox-caption">A synthetic borrowing tool that reveals hidden funding costs across currencies.</div>

|   |   |
|---|---|
| **What it is** | A swap exchanging [floating-rate](/interest-rate/) payments in one currency for floating-rate payments in another, plus a spread |
| **Also called** | Basis swap, cross-currency floating-for-floating swap, FX basis swap |
| **Typical maturity** | 2–10 years |
| **Drivers of basis** | [Interest-rate](/interest-rate/) differentials, [currency-risk](/currency-risk/) premia, balance-sheet constraints, cross-border capital flows |
| **Key participant** | Banks, multinational corporations, [hedge funds](/hedge-fund/) |
| **Spot exchange** | Usually no upfront spot leg; principal notional typically exchanged at maturity |

</aside>

## How the swap works in practice

Two parties exchange periodic floating-rate payments in different currencies. A US company might pay 3-month USD [SOFR](/sofr/) plus 20 basis points in exchange for receiving 3-month EUR EURIBOR. At maturity, they exchange back the notional in both currencies at a prearranged forward rate, locking in the synthetic funding cost.

The basis — the spread paid on top of the foreign currency rate — is where economics lives. When positive, it means borrowing synthetically in the foreign currency costs *more* than it appears from raw [interest-rate](/interest-rate/) spreads alone. When negative, synthetic funding is unusually cheap. This spread does not come from nowhere: it reflects the actual cost and difficulty for banks to fund themselves in that currency, capital requirements, and the shadow cost of removing assets from one balance sheet to another.

Unlike a standard currency swap, which pairs a fixed rate in one currency against a fixed rate in another, a cross-currency basis swap floats both legs. This makes it ideal for corporations or investors who already face floating-rate liabilities in one currency and want to transform them into floating-rate liabilities in another, or for arbitrage traders spotting pricing gaps between the swap market and spot-and-forward markets.

## Why the basis deviates from theoretical zero

In textbook efficient markets, the basis should be zero — the forward discount on a currency should exactly compensate for the interest-rate differential between the two currencies. But this assumes costless capital flows and unlimited balance-sheet capacity. Reality is messier.

During the 2008 financial crisis, the USD basis blew out to historic lows (negative 100+ basis points). Banks had lost access to dollar funding markets and would pay dearly to get dollars via swaps rather than earn it naturally from interest-rate spreads. The crisis revealed that the basis is a real *price* for scarcity and risk. More recently, post-2020 quantitative easing inflated central-bank balance sheets unevenly across currencies, pushing basis around — the EUR basis sometimes tighter, sometimes looser, as ECB policy diverged from Federal Reserve tightening.

Modern factors keeping the basis away from zero include:

**Capital regulation.** A bank taking a large position must hold capital against it. If the capital charge for holding euros is higher than dollars, that asymmetry pushes the basis negative (euros trade at a synthetic discount). [Tier-1 capital](/tier-1-capital/) rules and leverage ratios create real constraints.

**Balance-sheet scarcity.** A bank's total assets and liabilities are finite. In a slow-growth environment with cheap funding in one currency, banks are reluctant to swap out of that currency if they can earn better returns. The basis falls to entice them.

**Cross-border flows.** When large inflows hit one currency (say, during a commodity boom in AUD), banks accumulate the currency and swap it away synthetically at the best basis they can offer — pushing the basis tighter in the commodity currency.

## How traders and corporates use it

**Synthetic financing.** A German automaker borrows USD in its home market but needs euros to fund operations. Rather than constantly buying euros in the spot market, it enters a cross-currency basis swap, paying USD SOFR + X and receiving EUR EURIBOR. The cost is transparent and locked in. If the basis widens later, it doesn't matter — the lock is in place.

**Arbitrage.** A trader notices that the cost to synthetically get dollars via a EUR swap (implied by the swap spread and interest-rate differential) is cheaper than the actual forward price of dollars. The trader sells dollars forward, receives euros forward, and *receives* the swap leg in euros while *paying* the swap leg in dollars, pocketing the difference. This is the classic carry trade variant — pure relative-value.

**Hedging currency-specific liabilities.** A pension fund holds yen assets but faces EUR liabilities. A cross-currency swap, paired with a forward contract, can synthetically "relocate" cash flows from one currency to another without moving principal across borders, useful in jurisdictions with capital controls.

## The basis as a market signal

The cross-currency basis is watched closely by central banks and international policymakers. Extreme basis levels (especially large negative bases in the dollar) signal that the global financial system is under stress or that capital is fleeing to safety. During normal times, the basis is relatively tight — a few tens of basis points. A blowout suggests funding fractures.

[Securities-and-exchange-commission](/securities-and-exchange-commission/) regulation has required greater transparency in swap markets, making basis data more accessible to researchers. This has helped economists confirm that basis movements do precede real economic shocks, rather than lagging behind them — they are information-efficient.

## Pricing and no-arbitrage bounds

The basis cannot drift arbitrarily far from the interest-rate differential without triggering immediate arbitrage. If the synthetic cost to borrow in euros (paying USD + spread, receiving EUR rate) is much cheaper than actually borrowing euros directly, a corporation will simply borrow euros in the bond market instead of using the swap. This closes the gap. The mathematical bound is roughly: the basis should equal the forward-implied interest-rate differential *minus* the actual quoted interest-rate differential. When the basis strays far, it signals mispricing or real friction — constraints on who can execute the arbitrage.

## See also

<div class="wiki-seealso">

### Closely related

- [Forward contract](/forward-contract/) — the spot-and-forward machinery underlying synthetic currency conversion
- [Interest-rate](/interest-rate/) — the floating-rate benchmarks (SOFR, EURIBOR) anchoring swap legs
- [Currency risk](/currency-risk/) — the underlying exposure that basis swaps help isolate or transfer
- [SOFR](/sofr/) — the USD floating-rate reference index in modern cross-currency swaps
- [Leverage ratio (forex)](/leverage-ratio-forex/) — bank constraints that influence basis pricing

### Wider context

- [Stock market](/stock-market/) — capital flows into and out of equities move basis
- [Central bank](/central-bank/) — quantitative easing and policy divergence reshape currency funding costs
- [Capital flows](/capital-flows/) — the ultimate driver of basis extremes

</div>
