---
title: "Differential Swap"
description: "A swap in which the counterparties exchange floating-rate payments based on two different currency-area indices, but both legs settle in a single domestic currency."
keywords:
  - differential swap
  - quanto swap
  - cross-currency basis swap
  - multi-currency swap
  - basis differential swap
image: "/svg/derivatives.svg"
---

*A **differential swap** (or "diff swap") exchanges floating interest rates from two separate currency zones without introducing actual currency risk. One leg accrues at a rate from, say, the euro zone (EUR), and the other at a rate from the [US dollar](/us-dollar/) zone (USD), but both payments settle in dollars. The structure isolates interest-rate differential risk from [currency-risk](/currency-risk/), making it ideal for borrowers and investors who want exposure to one but not the other.*

<div class="wiki-hatnote">

For hedging currency exposure itself, see [currency-risk](/currency-risk/).

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Differential Swap — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract mark representing derivatives and structured contracts." />

<div class="wiki-infobox-caption">A swap isolating rate differentials across currency zones without incurring currency exposure.</div>

|   |   |
|---|---|
| **What it is** | Exchange of two floating rates from different currencies, both paid in one currency |
| **Also called** | Quanto swap, basis differential swap |
| **Reference rates** | [SOFR](/sofr/), EUR EONIA, GBP SONIA, others |
| **Settlement currency** | Single domestic currency (usually USD or EUR) |
| **Primary users** | Multinational corporates, asset managers, central banks |
| **Key risk** | Basis risk: divergence between rate and FX markets |

</aside>

## Why the structure exists

Imagine a US-domiciled investment firm wants to take a view on whether [interest rates](/interest-rate/) in the euro area will outpace US rates, without betting on the euro itself appreciating or depreciating. A traditional [interest-rate swap](/interest-rate-swap/) within the US market gives only USD exposure; buying euro bonds exposes the firm to currency moves. A differential swap lets the firm express the rate view in isolation.

Similarly, a multinational corporation might have liabilities in euros but cash generation in dollars. If euro rates are unusually high relative to US rates, the firm might swap into a differential to benefit from that spread without the hedging complexity of cross-currency funding.

Central banks and sovereign wealth funds use them to express macro views on [interest-rate](/interest-rate/) divergence—a key driver of [capital-flows](/capital-flows/) and [exchange rates](/spot-exchange-rate/). If a fund believes the [Federal Reserve](/federal-reserve/) will stay lower for longer than the [European Central Bank](/central-bank/), a differential swap is a clean way to play that thesis without currency speculation.

## Mechanics and settlement

A differential swap typically has two floating legs:

**Leg A (e.g., USD):** pays [SOFR](/sofr/) reset quarterly on a notional of $100 million.

**Leg B (e.g., EUR):** pays [EONIA](/sofr/) (or [EURIBOR](/interest-rate/)) reset quarterly on an equivalent notional (also $100 million, or converted at inception spot), *but paid in USD*.

The EUR leg's payment is computed as: [EONIA](/sofr/) × notional, then that amount is paid in dollars. There is no currency conversion at the payment date; the conversion happened at inception, locking in the basis. If EONIA rises 50 basis points above SOFR, the EUR leg owner receives 50 bps more (in dollar terms) than the USD leg owner, every reset.

This is where the "differential" name comes from: you are betting on the difference between two rates, not on the rates themselves or the currency.

Some differential swaps include a spread on one or both legs. For instance, Leg B might pay EONIA + 25 bps. This compensates one side for taking on [basis-risk](/credit-spread/) (the risk that the two rates diverge unexpectedly) or reflects credit terms negotiated between counterparties.

## The basis risk at the heart of it

The core risk in a differential swap is basis risk: the two rates you swapped don't move together. [SOFR](/sofr/) is a true overnight rate; the euro equivalent is slightly different in methodology and market depth. If one market seizes (as happened in 2008 and again during the COVID shock), the rates can spike independently. A corporate holding a differential might suddenly see EONIA rocket while SOFR stays flat—a huge loss if the rate spread assumption breaks.

This is why differential swaps trade at a visible spread. The fixed side of the swap (or a higher floating rate on one leg) compensates for basis risk. During stable periods, the spread is tight; during stress, it blows out. A firm caught on the wrong side of a 100+ basis-point blowout faces significant mark-to-market losses.

## Pricing and valuation

Pricing a differential swap means valuing two separate floating legs in two different currency zones, then anchoring both to a single currency. This requires models of:

1. **Rate dynamics in each zone** — [implied-volatility](/implied-volatility/) of [SOFR](/sofr/) versus EONIA, [yield-curve](/yield-curve/) slope in each zone.
2. **Basis correlation** — how tightly the two rates co-move. High correlation means lower spread; low correlation (or expected divergence) means wider spread.
3. **Counterparty credit** — the probability that your swap counterparty survives to maturity and pays.

The valuation is done in a single currency (usually the domestic currency of the payer of the fixed rate or the larger economy). Cash flows in the foreign rate are discounted using the foreign zone's curve, then converted to domestic at the initial spot rate.

[Duration](/duration/) is the primary risk metric. A differential swap on long tenors (10+ years) has high duration; the present value of the basis spread is magnified. [Convexity](/interest-rate-risk/) matters too if rates in either zone are likely to move sharply.

## Who uses them and why

**Multinational corporates** use differential swaps to hedge cross-currency funding mismatches without full [currency-risk](/currency-risk/) exposure. A US company with euro debt and dollar revenues can swap into a differential to lower effective borrowing cost if euro rates are wide.

**Asset managers** and hedge funds use them to express macro views on [interest-rate](/interest-rate/) differentials as a signal of [capital-flows](/capital-flows/) or central bank policy divergence. If a macro fund believes US rates will outpace eurozone rates (without betting on dollar strength), a differential is a clean position.

**Banks and dealers** use them to hedge funding arbitrage. If a bank borrows in euros (say, at EONIA + 50) and lends in dollars (at SOFR + 75), the natural hedge is a differential swap that locks in the 25 bps spread.

**Central banks** and [sovereign debt](/sovereign-debt/) managers occasionally use differentials to manage the international policy transmission mechanisms or to hedge foreign-exchange reserves in a way that isolates rate moves from currency moves.

## Real-world complications

**Basis blowouts:** During financial stress, SOFR and EONIA can diverge sharply. The 2008 crisis and the March 2020 COVID shock both saw unexpected spikes in basis risk. Holders of differential swaps suffered large losses.

**Liquidity:** Differential swaps are less liquid than vanilla [interest-rate swaps](/interest-rate-swap/). Mid-market spreads can be wide, and large positions are hard to exit without moving the market. A corporate might enter a differential easily but find it costly or impossible to unwind.

**Accounting:** Under [generally-accepted-accounting-principles](/generally-accepted-accounting-principles/), differential swaps may require complex [fair-value](/fair-value/) accounting, with gains or losses flowing through P&L or other comprehensive income depending on the hedge relationship.

**Documentation:** ISDA (International Swaps and Derivatives Association) standard documentation for differential swaps is less standardized than for plain vanilla interest-rate swaps. Bespoke terms around rate observation, settlement, and basis triggers need careful legal review.

## Relationship to other swap structures

A [range-accrual-swap](/range-accrual-swap/) is interest-rate only and single-currency; a differential swap is multi-rate but single-currency. A [step-up-swap](/step-up-swap/) has a predetermined coupon schedule; a differential has two floating legs. A plain [interest-rate swap](/interest-rate-swap/) exchanges a fixed rate for floating in one currency.

Differential swaps sit at the intersection of [interest-rate swap](/interest-rate-swap/) and [currency-risk](/currency-risk/) hedging. Unlike a full cross-currency [interest-rate swap](/interest-rate-swap/) (which includes currency principal exchange), a differential keeps both legs in one currency.

## See also

<div class="wiki-seealso">

### Closely related

- [Interest-Rate Swap](/interest-rate-swap/) — the single-currency parent structure
- [Currency Risk](/currency-risk/) — the exposure differential swaps do NOT take on
- [SOFR](/sofr/) — the benchmark US overnight rate
- [Basis Risk](/credit-spread/) — the core risk in differential swaps
- [Range-Accrual-Swap](/range-accrual-swap/) — another conditional swap variant
- [Step-Up-Swap](/step-up-swap/) — a structured coupon schedule variant

### Wider context

- [Implied Volatility](/implied-volatility/) — input for differential swap pricing
- [Duration](/duration/) — the primary interest-rate sensitivity metric
- [Capital Flows](/capital-flows/) — macro driver often expressed via differential swaps
- [Fair Value](/fair-value/) — accounting treatment of differential positions
- [Counterparty Risk](/counterparty-risk/) — credit risk in bilateral swap agreements
- [Federal Reserve](/federal-reserve/) — US monetary policy anchor for SOFR
- [Central Bank](/central-bank/) — issuer of rate regimes underlying the swaps

</div>
