---
title: "SOFR Swap"
description: "A SOFR swap is an interest-rate swap using SOFR (Secured Overnight Financing Rate) as the floating leg, replacing the deprecated LIBOR standard."
keywords:
  - sofr
  - sofr swap
  - interest rate swap
  - overnight rate
  - derivatives
image: "/svg/derivatives.svg"
---

*A **SOFR swap** is an [interest-rate-swap](/interest-rate-swap/) where one party pays fixed and receives SOFR (Secured Overnight Financing Rate), a transaction-based overnight borrowing rate. SOFR replaced LIBOR (London Interbank Offered Rate) globally as the benchmark interest rate for derivatives. SOFR swaps are now the standard interest-rate [swap](/swap/) instrument and are more transparent, less subject to manipulation, and better anchored in actual market transactions than LIBOR.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">SOFR Swap — key facts</div>

<img src="/svg/derivatives.svg" alt="SOFR rate vs. historical LIBOR" />

<div class="wiki-infobox-caption">SOFR replaced LIBOR as the benchmark rate.</div>

|   |   |
|---|---|
| **Floating rate** | SOFR (overnight secured rate) |
| **Fixed leg** | Agreed percentage (e.g., 4.5% annual) |
| **Accrual** | Overnight rates compounded; reset quarterly |
| **Pricing basis** | Spread over overnight indexed swap (OIS) |
| **Transition date** | LIBOR cessation: June 2023 (USD) |
| **Existing contracts** | Mostly transitioned; some legacy LIBOR remain |
| **Liquidity** | High; standard market instrument |
| **Duration** | 1–30 years |
| **Primary use** | Interest-rate risk management, asset-liability |
| **Clearing** | Standardized; central clearing required |

</aside>

## SOFR: replacement for LIBOR

LIBOR was the global standard for decades but was plagued by manipulation scandals (2012 Barclays, others). Regulators mandated transition to more transparent, transaction-based rates.

**SOFR** (Secured Overnight Financing Rate) is calculated daily based on actual repo transactions secured by US Treasury collateral. It is harder to manipulate and reflects genuine market borrowing costs.

Similar rates exist globally:
- **€STR** (Euro Short-Term Rate) in the eurozone
- **SONIA** (Sterling Overnight Index Average) in the UK

## SOFR mechanics

SOFR is an overnight rate: the rate you pay to borrow cash for one day, secured by Treasury collateral. It is published daily by the Federal Reserve.

In a SOFR swap, the floating leg compounds overnight rates over a period (e.g., a quarter):

Floating Payment = Notional × (Product of daily SOFR − 1)

This compounding creates a quarterly interest amount that varies with realized SOFR path.

## Comparison to LIBOR

| Aspect | LIBOR | SOFR |
|--------|-------|------|
| **Basis** | Survey of interbank borrowing | Actual repo transactions |
| **Manipulation risk** | High; survey-based | Low; transaction-based |
| **Transparency** | Low; quoted rates | High; Fed publishes |
| **Term rates** | 1M, 3M, 6M, 12M | Only overnight; forward rates derived |
| **Status** | Ceased June 2023 | Active, standard |

## Transition logistics

The June 2023 LIBOR cessation required the global derivatives industry to transition trillions in notional swaps:

1. **Legacy contracts:** Mostly converted to SOFR with specified spreads to match economics.
2. **New contracts:** Issued in SOFR from 2021–2023 onward.
3. **Basis risk:** Transition introduced temporary mispricing as old and new contracts had different bases.

## Spread adjustments

A SOFR swap typically trades at a fixed spread above the overnight indexed swap (OIS) rate. The spread reflects credit risk, supply-demand, and market factors.

A 4.5% SOFR swap fixed rate might be quoted as "SOFR + 150 bps" (1.5% spread above the OIS curve).

## Overnight indexed swaps (OIS)

Closely related to SOFR swaps are **OIS contracts**, which swap fixed for overnight rates (in SOFR's case, fixed for SOFR). OIS are the baseline for SOFR pricing; SOFR swaps trade at spreads to OIS.

## Market implications

**Lower effective rates:** SOFR is an overnight rate (always lower than term LIBOR). Swaps referencing SOFR often have lower all-in costs.

**Convenience for central banks:** SOFR is the Fed's preferred rate for policy guidance and market operations.

**Liquidity:** SOFR swap markets are very liquid; standardized contracts trade in size.

## See also

<div class="wiki-seealso">

### Closely related

- [Interest rate swap](/interest-rate-swap/) — traditional structure
- [Swap](/swap/) — general contract
- [LIBOR](/interest-rate/) — historical standard (deprecated)
- [Overnight indexed swap](/sofr-swap/) — closely related
- [SONIA](/interest-rate/) — UK equivalent

### Rates and benchmarks

- [SOFR](/interest-rate/) — the floating rate index
- [Overnight rate](/interest-rate/) — SOFR is overnight
- [Fed funds rate](/federal-reserve/) — related policy rate
- [Yield curve](/yield-curve/) — SOFR curve determines pricing

### Transition and risk

- [Basis risk](/basis/) — SOFR vs. LIBOR temporary basis
- [Contract conversion](/interest-rate-swap/) — transition logistics
- [Spread adjustment](/interest-rate/) — to match LIBOR economics
- [Forward SOFR](/interest-rate) — rates for future periods

### Deeper context

- [Derivative](/option/) — the family of instruments
- [Interest rate](/interest-rate/) — market being hedged
- [Benchmark rate](/federal-reserve/) — SOFR is standard
- [Fixed income](/bond/) — SOFR essential market

</div>
