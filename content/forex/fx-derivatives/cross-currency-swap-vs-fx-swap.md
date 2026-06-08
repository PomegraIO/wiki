---
title: "Cross-Currency Swap vs FX Swap: What Is the Difference?"
description: "Distinguish between cross-currency swaps and FX swaps by tenor, coupon exchange, balance-sheet treatment, and which institutions rely on each."
keywords:
  - cross currency swap vs fx swap
  - cross currency swap definition
  - fx swap definition
  - currency hedging instruments
  - interest rate swap cross-currency
image: /svg/forex.svg
---

*A **cross-currency swap** is a long-term agreement to exchange principal and periodic interest payments in two different currencies, often lasting years; an **FX swap** is a short-term forward contract that locks in an exchange rate for a future date, usually maturing in days or months. The difference lies in tenor, coupon flow, and accounting impact—and they solve different problems for banks, corporates, and sovereigns.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Cross-Currency Swap vs FX Swap — key facts</div>

<img src="/svg/forex.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Two instruments that both manage currency exposure but operate on different time horizons and coupon structures.</div>

|   |   |
|---|---|
| **Cross-Currency Swap** | Long-term (years); exchanges principal + periodic coupons |
| **FX Swap** | Short-term (days to months); exchanges principal at start and maturity only |
| **Primary use** | Corporate liability swaps; assets/liabilities in mismatched currencies |
| **Balance-sheet treatment** | Off-balance-sheet derivative | Off-balance-sheet derivative |
| **Coupon flow** | Yes; periodic (quarterly, annual) | No; only spot and forward legs |
| **Counterparty** | Banks, other corporates | Banks, primary dealers |

</aside>

## The two instruments at a glance

An **FX swap** is the simpler tool: Party A borrows USD at spot rates and lends EUR for 90 days, then reverses at a fixed future rate (the forward rate). No periodic interest flows occur—only two exchanges of principal, one at the start and one at maturity. Banks use FX swaps to finance short-term forex positions, manage daily liquidity needs, and lock in roll-over costs when sitting on currency mismatches.

A **cross-currency swap** is longer and more structured. Party A and Party B agree that A will pay coupons (say, 2% annually) on a EUR principal, while B pays coupons (say, 4% annually) on a USD principal. At maturity, they swap the principals back. The instrument can last three, five, ten years or longer—whatever the underlying business need is. A multinational with a EUR-denominated bond outstanding might enter a cross-currency swap to convert its coupons to USD, locking in the all-in cost of borrowing in its home currency.

## Tenor and the reason for the split

The split between these two exists because of how financial markets price time.

For short-term currency mismatches—say, a dealer that bought EUR 100 million and needs to hold it for a week—an FX swap is perfect. The dealer buys EUR at spot and sells it 7 days forward at a fixed rate. The [interest-rate-differential](/interest-rate/) between the currencies is baked into the forward premium or discount (see [covered-interest-rate-parity](/covered-interest-rate-parity/) equilibrium). No coupons change hands; just two leg exchanges.

For long-term asset or liability swaps, periodic coupon exchanges matter because:

1. **Mismatched bond currencies.** A German corporation borrows EUR but earns revenue in USD. It wants to pay in USD but the bond is in EUR. Refinancing the entire bond is expensive; a cross-currency swap flips the coupon currency and tenor without touching the bond itself.

2. **Different credit profiles.** A high-grade AAA-rated bank borrows at near-risk-free rates in the USD market but pays much higher spreads in EUR. It can borrow USD cheaply, then swap coupons with another entity, arbitraging the spread. This is profitable only over multi-year tenors where the spread difference compounds.

3. **Central bank reserves and structural hedges.** A sovereign central bank holds long-dated foreign-exchange reserves. It might enter a long-dated cross-currency swap to convert the yield (say, 2% in CHF) into domestic currency (say, 3% in CHF-equivalent), synthetic-yield management without selling the reserves outright.

FX swaps cannot handle these scenarios because they expire in days or weeks and carry no coupon stream. They are tools for roll-over, not transformation.

## Accounting and balance-sheet footprint

Both instruments are **off-balance-sheet derivatives**—neither party books the notional principal on the balance sheet itself. But the accounting for the periodic flows differs:

- **FX swap:** The interest differential is already embedded in the forward price. Accrual accounting recognizes the all-in financing cost upfront in the spread.
- **Cross-currency swap:** Periodic coupons create ongoing accruals. The swap is marked to market each period (under fair-value or hedge-accounting rules), so gains or losses on the remaining legs flow through either equity or income depending on the hedge classification ([asc-606](/asc-606/) for revenue, ifrs-9 for derivatives).

For a corporate using a cross-currency swap to hedge a long-dated foreign-denominated liability, the accounting is typically a **cash-flow hedge**. Changes in the swap's fair value due to interest-rate or spot-rate moves are recognized in other comprehensive income (OCI) until the swapped coupons are actually paid and the hedge is de-designated at maturity.

## Who uses each, and when

**FX swaps** are the backbone of global interbank funding. A New York bank that needs EUR overnight will borrow USD at the Fed funds rate, then FX-swap the USD for EUR at the 1-day forward rate, borrowing EUR synthetically at the EUR-implied rate. The [federal-reserve](/federal-reserve/) and other central banks use FX swaps to inject emergency liquidity in foreign currencies during stress. Large [hedge-fund](/hedge-fund/) desks use them to finance short-term forex positions cheaply.

**Cross-currency swaps** are the tool of multinational corporates and sovereigns. A Japanese exporter with USD revenue but JPY debt uses a cross-currency swap to convert JPY coupons into USD, matching its cash flow. A [sovereign-debt](/sovereign-debt/) manager might use a cross-currency swap to optimize the currency mix of reserves and reduce funding costs. Japanese insurance companies—famous for their high savings rates and demand for yield—have used cross-currency swaps to buy, say, Australian bonds and swap the coupons back into JPY, locking in the yield differential.

## The economics: forward rate vs. coupon differential

Both instruments price in the interest-rate differential between currencies (and credit risk, if applicable).

In an FX swap, the forward rate is set such that the all-in return from borrowing one currency and lending the other is zero (covered-interest-rate parity). If USD rates are 5% and EUR rates are 3%, the forward EUR/USD rate is set to make a US investor indifferent between lending USD at 5% and lending EUR (after converting at the forward) at 3%.

In a cross-currency swap, the fixed coupons are set similarly: the net present value of both legs, in their respective currencies, must equal zero at initiation. But the swap coupons stay fixed for the life of the swap. If a corporate locks in a cross-currency swap at a 2% EUR coupon rate and a 4% USD coupon rate, it has locked in those rates for five years—even if market rates diverge. The initial swap rate reflects the forward curve, the credit-spread curve, and the term structure of volatility.

## Valuation and rehedging

An FX swap's valuation is simple: the difference between the original forward rate and today's forward rate, times the notional, discounted. A bank that bought EUR three months forward at 1.09 USD/EUR and today's 3-month forward rate has fallen to 1.08 will have a [mark-to-market](/mark-to-market/) gain.

A cross-currency swap's valuation is more complex. You value each leg separately as if it were a bond in its currency, discount using that currency's yield curve, then convert one leg to the other's currency at today's spot rate. A widening in the EUR credit-spread curve, a steep drop in EUR rates, or a plunge in the EUR/USD spot rate can all swing a swap's value sharply, requiring the swap to be marked to market and potentially requiring additional collateral from one party.

## Structural similarities and the swapnote yield

Despite their differences, FX swaps and cross-currency swaps share the same conceptual risk factors: spot [currency-volatility](/currency-volatility/), interest-rate volatility, credit spread, and counterparty default. Both are priced off the forward curve and credit curves. A dealer quoting both instruments uses the same inputs—spot rate, interest rates in both currencies, credit spread, funding cost—and prices them consistently to avoid arbitrage.

Some practitioners speak of the **cross-currency swap basis**—the spread above the risk-free coupon that is required to make a cross-currency swap attractive. If the basis widens, it can mean the market expects interest-rate divergence or increased funding stress in one currency, and it affects the pricing of both instruments.

## Key takeaway

Choose **FX swaps** when you have a short-term currency mismatch (days to months) and want to borrow one currency synthetically at a locked-in all-in cost. Choose **cross-currency swaps** when you have a long-dated asset or liability in a foreign currency that you want to convert into your home currency while keeping the bond structure intact. The swap lets you change the currency of cash flows without refinancing, is often cheaper than a new bond issuance, and is transparent on your balance sheet as a derivative rather than as a new liability.

## See also

<div class="wiki-seealso">

### Closely related

- [Interest-rate swap](/interest-rate-swap/) — the domestic-currency analogue; fixes a variable rate or swaps fixed for floating
- [Currency risk](/currency-risk/) — the underlying exposure that FX swaps and cross-currency swaps are designed to hedge
- [Interest-rate risk](/interest-rate-risk/) — affects the valuation of cross-currency swaps, especially on longer tenors
- [Covered interest-rate parity](/covered-interest-rate-parity/) — the no-arbitrage principle that prices FX swaps
- [Swap](/swap/) — general framework for all swap instruments

### Wider context

- [Derivatives hedging](/derivatives-hedging/) — why and how institutions hedge using derivatives
- [Federal Reserve](/federal-reserve/) — central bank that lends dollars via FX swaps in stress
- [Counterparty risk](/counterparty-risk/) — both instruments carry default risk to the other party
- [Securitization](/securitization/) — corporate issuers often combine bond issuance with a cross-currency swap

</div>
