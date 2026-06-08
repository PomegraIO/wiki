---
title: "Forward Rate Agreement"
description: "An over-the-counter contract that locks in an interest rate for a future borrowing or lending period without exchanging principal."
keywords:
  - forward rate agreement
  - FRA
  - interest rate derivatives
  - OTC derivatives
  - interest rate hedging
  - LIBOR
  - borrowing costs
image: "/svg/derivatives.svg"
---

*A **forward rate agreement** (FRA) is a bespoke [over-the-counter](/over-the-counter-market/) contract between two parties that fixes an [interest rate](/interest-rate/) for a notional sum of money over a future period. No principal is exchanged; instead, the contract is settled in cash at the start of the borrowing period by comparing the agreed-upon rate to the market rate that prevails on that day. An FRA allows a company to hedge [interest rate risk](/interest-rate-risk/) months in advance without committing to an actual loan or deposit.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Forward Rate Agreement — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives." />

<div class="wiki-infobox-caption">A bespoke contract to lock in a future borrowing or lending rate without the overhead of actual debt.</div>

|   |   |
|---|---|
| **What it is** | An OTC derivative contract on an [interest rate](/interest-rate/) for a future period |
| **Principal exchanged** | None; only the interest differential is settled in cash |
| **Common underlyings** | [LIBOR](/libor/), [SOFR](/sofr/), or other short-term reference rates |
| **Typical term** | 1×4 (3-month rate, 1 month forward), 3×9 (6-month rate, 3 months forward) |
| **Counterparty** | Negotiated directly between borrower and lender or their banks; no exchange |
| **Settlement** | Cash payment at the start of the rate period, based on the rate differential |
| **Purpose** | Hedge [interest rate risk](/interest-rate-risk/) on future borrowing or lending without taking on actual debt |

</aside>

## The structure of an FRA

An FRA is defined by three dates and two rates. The **settlement date** is when the contract is settled in cash and the underlying borrowing or lending period begins. The **maturity date** is when that period ends. Between settlement and maturity lies the term of the borrowing (typically three or six months). The **agreed rate** is the fixed [interest rate](/interest-rate/) that both parties have contracted; the **reference rate** is the actual short-term market rate (usually [LIBOR](/libor/) or [SOFR](/sofr/)) that prevails on the settlement date.

A company that expects to borrow €10 million in three months for a six-month period can buy a 3×9 FRA. The "3×9" notation means the settlement date is three months away and the contract matures nine months away (six months of borrowing starting in three months). If the agreed rate is 3.50%, and when the settlement date arrives the actual [LIBOR](/libor/) fix is 3.75%, the FRA seller pays the buyer the difference (0.25%) on the notional €10 million, covering three months. The actual borrowing still occurs, but the cash received from the FRA offsets the higher market rate the company must pay on the real loan, effectively achieving its target rate.

## Why FRAs instead of futures or bonds?

FRAs occupy a middle ground between [interest rate futures](/interest-rate-futures/) and [bonds](/bond/). A [futures contract](/futures-contract/) is exchange-traded, standardized, and liquid—but only available in preset maturities and sizes. A [bond](/bond/) is the actual debt instrument itself—no optionality, capital must be raised, and there is no reversal without sales in the secondary market. An FRA is tailored to the exact size and timeline the borrower needs, negotiated over-the-counter with a bank, and settled in cash, meaning the borrower can then proceed with a real bank loan on the settlement date without complication.

FRAs are also popular for hedging because they impose no balance sheet recognition until the settlement date. A company does not record an FRA as a liability on day one (though [IFRS](/international-financial-reporting-standards/) requires disclosure). A [futures contract](/futures-contract/), by contrast, creates daily [mark-to-market](/mark-to-market/) adjustments and variation margin flows. For many treasurers, the simplicity and off-balance-sheet treatment of an FRA makes it the preferred tool.

## The cash settlement formula

When the settlement date arrives, no money changes hands on the principal. Instead, the bank calculates the cash flow:

```
Cash payment = Notional × (Reference rate − Agreed rate) × (Day count / 360)
```

If the reference rate is higher than the agreed rate, the FRA seller pays the buyer (protecting the borrower against rising rates). If the reference rate is lower, the buyer pays the seller (the borrower benefits from cheaper market rates and must pay the seller the difference—the cost of the insurance it bought). The payment is typically made upfront at settlement, not spread across the borrowing period.

The day count is usually Actual/360 (actual days divided by 360) for US dollar and EUR FRAs, though other conventions exist. A three-month FRA is therefore never exactly 90 days; it uses the actual number of days between settlement and maturity.

## Who uses FRAs and when

Large corporates, financial institutions, and investment managers use FRAs to manage [interest rate risk](/interest-rate-risk/) on anticipated borrowing or lending. A manufacturing company that plans to refinance a €50 million term loan in six months can lock in the rate now with an FRA. A pension fund expecting to invest large cash inflows in a bond fund can use an FRA to hedge the risk that rates will fall before the investment is made (locking in a lending rate protects against the cost of that move). A bank that has client loan commitments at rates not yet finalized uses FRAs to manage the mismatch.

FRAs are also used for [basis](/basis/) trades, where a trader simultaneously enters an FRA and buys or shorts [futures](/futures-contract/) to exploit the pricing difference between the OTC market and the exchange. Banks that are hedging client FRA positions use [interest rate futures](/interest-rate-futures/) as the offset, arbitraging small gaps in pricing.

## The counterparty risk

Because FRAs are OTC contracts, they carry [counterparty risk](/counterparty-risk/). If the reference rate moves sharply against the buyer's position and the FRA seller defaults, the buyer loses the economic benefit of the hedge. This risk is why most FRA trades today occur between large financial institutions with strong credit ratings or are subject to collateral agreements. Since the 2008 financial crisis, central clearing houses have moved some standardised interest rate swaps into the clearing system, but FRAs remain largely bilateral and require credit assessment between counterparties.

## After LIBOR transition

The global transition away from [LIBOR](/libor/) has reshaped FRA trading. Historically, FRAs were almost universally quoted on [LIBOR](/libor/) for multiple tenors and currencies. By regulation, most [LIBOR](/libor/) rates have been discontinued or are being phased out in favour of [SOFR](/sofr/) (Sterling Overnight Index Average, in the US) and equivalent risk-free rates in other currencies. New FRAs are increasingly quoted on the new rates, though the mechanics remain identical; the contract now references [SOFR](/sofr/) or another risk-free rate rather than [LIBOR](/libor/), and market participants have had to adjust pricing models to account for the spread between the old and new benchmarks.

## See also

<div class="wiki-seealso">

### Closely related

- [Interest rate futures](/interest-rate-futures/) — exchange-traded cousins that serve similar hedging purposes
- [Non-deliverable forward](/non-deliverable-forward/) — the currency equivalent of an FRA
- [LIBOR](/libor/) — the traditional reference rate for FRAs (now being phased out)
- [SOFR](/sofr/) — the replacement risk-free rate for many FRAs
- [Over-the-counter market](/over-the-counter-market/) — where FRAs are traded
- [Counterparty risk](/counterparty-risk/) — a key risk in bilateral FRA deals
- [Interest rate risk](/interest-rate-risk/) — what FRAs are used to manage
- Derivative — the broader category of instruments

### Wider context

- [Hedge fund](/hedge-fund/) — an investor type that uses FRAs extensively
- [Interest rate](/interest-rate/) — the underlying asset
- [Forward contract](/forward-contract/) — the broader class of OTC contracts
- [Monetary policy](/monetary-policy/) — which drives the interest rates FRAs are hedging
- [Basis](/basis/) — an important concept in FRA valuation and trading

</div>
