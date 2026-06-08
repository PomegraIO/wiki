---
title: "FX Swap vs FX Forward: What Is the Difference?"
description: "FX swap vs FX forward: an FX swap exchanges currency twice (in opposite directions); a forward is a single settlement. Both lock in future exchange rates but serve different liquidity and term needs."
keywords:
  - fx swap vs fx forward difference
  - currency swap structure
  - forward contract exchange
  - fx derivatives mechanics
  - interest rate differential
  - currency exchange settlement
---

*An **FX swap** locks in a future exchange rate by exchanging currency twice in opposite directions, while an **FX forward** settles just once. Both eliminate exchange-rate risk, but the two-legged structure of a swap creates interest-rate economics and liquidity advantages that make it the preferred tool for short-term currency needs.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">FX Swap vs FX Forward — key facts</div>

<img src="/svg/forex.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Two instruments, one goal: lock in an exchange rate. The structure determines the cash flows and opportunity.</div>

|   |   |
|---|---|
| **FX Swap** | Two offsetting currency exchanges; near-leg and far-leg |
| **FX Forward** | Single exchange at a future date |
| **Typical maturity** | Swap: days to months; Forward: months to years |
| **Driver of rate** | Swap: spot + interest-rate differential; Forward: covered interest parity |
| **Most common user** | Swap: banks, corporates rolling short-term funding; Forward: exporters, importers hedging budgets |
| **Counterparty risk** | Forward: full notional at settlement; Swap: smaller at each leg, netted daily |

</aside>

## The Structure: One Leg Versus Two

An **FX swap** is fundamentally two forward contracts tied together. Party A buys currency today (the *near leg*, spot settlement) and simultaneously commits to sell that same currency at a future date (the *far leg*). The two exchange rates—near and far—are agreed upfront. Money flows twice, in opposite directions.

An **FX forward** is a single promise: exchange one currency for another on a specified future date at a pre-agreed rate. One date, one settlement.

This architectural difference cascades through cost, risk, and practical use. Because a swap involves an immediate cash leg, it absorbs funding costs and interest-rate differentials. A forward, which settles far in the future, prices in only the interest-rate gap between the two currencies over the entire holding period.

## Economics: Interest-Rate Parity and Funding

The reason a **FX swap vs FX forward difference** matters to traders and treasurers is that they price differently, even though both lock in a future rate.

An FX forward rate is derived from *covered interest parity*: the forward premium or discount adjusts for the interest-rate differential between the two currencies, so no arbitrage is possible. If the dollar earns 5% and the euro earns 2%, the euro will trade forward at a premium (you pay fewer euros for a dollar in the future).

An FX swap, by contrast, resets that calculus. The *swap points*—the difference between the near-leg rate and the far-leg rate—incorporate not only the interest-rate differential but also the cost of funding the near-leg purchase. For a bank, swapping dollars for euros today means holding euros and funding the dollars it just sold. The swap curve reflects the real borrowing costs in money markets, not theoretical interest rates. In times of stress or when one currency is scarce, swap points can deviate sharply from the forward rate implied by the interest-rate gap.

## Cash-Flow Timing: When You Need Money Now or Later

The two-leg structure of a swap makes it ideal when a firm needs foreign currency *right now*. An exporter receiving euros in 90 days but needing to pay suppliers today in euros can enter a swap: buy euros spot (getting them immediately), sell them 90 days forward. The exporter funds itself, de-risks the exchange rate, and schedules the offshore currency receipt to offset the forward leg—all in one trade.

A forward is better suited for a different scenario. A U.S. importer knows it will owe €1 million in six months and buys a forward to lock the dollar price. It has no need for euros today; it wants certainty on the cost of a future euro payment. A forward is simpler, cheaper (no immediate cash exchange), and sufficient.

## Maturity and Rollover: Why Banks Prefer Swaps

Most FX swaps are short-dated—one week, two weeks, one month. Banks use them daily to manage cash and funding. When a swap matures, a bank may *roll* it by closing the far leg and opening a new swap at that date, extending the maturity. Over six months, a series of rolled weekly swaps can effectively create a long-dated currency position without ever committing to a single forward contract.

Forwards, by contrast, are typically booked for longer periods—three months, six months, a year, even several years. Some corporations even lock in multi-year forwards to eliminate all exchange-rate uncertainty on committed contracts.

The ease of rolling swaps, plus the ability to adjust the notional or terms week to week, makes them operationally flexible for dealers. Forwards are more of a "set and forget" hedge.

## Settlement and Counterparty Risk

A forward exposes the buyer and seller to full principal risk at settlement. If you committed to buy €100 million at 1.10 USD/EUR and the contract matures on that date, you must pay $110 million. Counterparty risk—the risk that the other side fails to settle—sits on the full notional until the exchange occurs.

In a swap, each leg settles separately, and daily mark-to-market and collateral management in modern markets (CSA agreements) mean counterparty exposure is continuously managed. The first leg settles at spot, the second at the far date. Many participants in FX swaps also *net* exposures across thousands of trades, reducing settlement risk further.

This is why systemically important dealers and central banks can handle enormous FX swap volumes: the risk infrastructure is robust.

## Regulatory Treatment and Balance-Sheet Impact

Forwards and swaps are treated differently under accounting rules and bank capital requirements. A forward is typically an off-balance-sheet derivative, marked to market through profit and loss. A swap, because it involves an immediate cash exchange at spot rates, can sometimes be treated as a spot transaction (the near leg) plus a forward derivative (the far leg), or as a single derivative depending on the accounting framework.

For banks, this distinction affects capital calculations and balance-sheet ratios. A firm financing itself with short-term swaps versus long-term forwards will show different leverage and liquidity metrics, influencing how regulators and rating agencies assess financial health.

## Practical Example: A Two-Week Funding Need

Imagine a bank in Tokyo has a €50 million funding gap for 14 days. It can enter an FX swap: buy €50 million at spot (1.08 USD/EUR) today, immediately exchange it for $54 million, and commit to sell €50 million back in 14 days at 1.0795 USD/EUR (a lower rate reflecting the interest-rate differential and funding cost). The bank gets dollars today, avoids the exchange-rate risk, and schedules a euro payment in two weeks. The cost is the 105-pip difference—about $52,500 on $54 million.

Had the bank instead bought a 14-day forward, it would incur only the forward premium (approximately the same 105 pips), but it would receive no money until settlement. For an immediate liquidity need, the forward does not solve the problem.

## Conventions and Market Practice

In major forex markets, swap markets are deeper and more liquid than forwards, especially at shorter tenors. The overnight (O/N) swap and one-week swap are benchmarks that central banks monitor for funding stress. The [spread](/bid-ask-spread/) on a dollar/euro swap at one week might be 0.5 pips; a one-week forward might be 1.5 pips wider.

Traders watch the *FX swap curve*—the term structure of swap points from overnight to two years—as a proxy for funding conditions and interest-rate expectations. During crises, swap curves dislocate, signaling a breakdown in arbitrage or a funding squeeze in one currency.

## See also

<div class="wiki-seealso">

### Closely related

- [Forward Contract](/forward-contract/) — the single-settlement derivative used to lock in future prices
- [Interest Rate Swap](/swap/) — a cash-flow exchange structure that adjusts interest payments, not currencies
- [Covered Interest Parity](/bid-ask-spread/) — the no-arbitrage relationship that ties forward rates to interest differentials
- [Spot Exchange Rate](/spot-rate/) — the immediate rate in an FX swap's near leg
- [Currency Risk](/currency-risk/) — why both swaps and forwards exist as hedges

### Wider context

- [Derivatives Hedging](/derivatives-hedging/) — the broader toolkit for managing price and rate risks
- [Counterparty Risk](/counterparty-risk/) — the settlement and credit exposure both instruments create
- [Central Bank](/central-bank/) — a key participant in FX swap markets, especially during stress
- [Liquidity Risk](/liquidity-risk/) — why short-term swaps are preferred in funding markets

</div>
