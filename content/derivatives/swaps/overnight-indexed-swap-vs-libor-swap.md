---
title: "Overnight Indexed Swap vs LIBOR Swap"
description: "Compare overnight indexed swaps and LIBOR swaps: how OIS reference rates embed credit risk differently, and why spreads diverge during market stress."
keywords:
  - overnight indexed swap vs libor swap
  - ois vs libor swap difference
  - overnight indexed swap credit risk
  - libor swap basis risk
  - swap reference rate comparison
image: /svg/derivatives.svg
---

*An **overnight indexed swap vs LIBOR swap** comparison reveals how these two interest rate derivatives embed risk differently. OIS references overnight funding rates with minimal credit risk built in, while LIBOR-based swaps carry embedded counterparty credit exposure—a distinction that becomes stark during financial stress, when the spread between them can widen dramatically.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">OIS vs LIBOR Swap — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives and swaps." />

<div class="wiki-infobox-caption">Two parallel interest rate hedging instruments that respond differently to credit cycles.</div>

|   |   |
|---|---|
| **Reference rate** | OIS = overnight federal funds; LIBOR = interbank 1M, 3M, 6M, 12M |
| **Credit risk** | OIS contains minimal counterparty exposure; LIBOR embeds bank credit risk |
| **Basis** | OIS-LIBOR spread typically 10–50 bps; widens to 100+ bps during crises |
| **Primary use** | OIS = core funding rate; LIBOR = commercial lending/derivatives |
| **Dealer motive** | Use basis widening to profit on credit stress bets |

</aside>

## What each swap references

**OIS** (overnight indexed swap) cashflows are tied to the geometric average of overnight federal funds rates over the accrual period. In the U.S., that is the [Federal Reserve](/federal-reserve/)-administered rate at which banks lend reserves to each other for one day. By definition, the overnight market is where the central bank operates; funding is collateralized and daily-marked; and the credit risk embedded in the overnight rate is minimal—it reflects only the risk that the Fed itself might fail (near-zero in practice).

**LIBOR** (London Interbank Offered Rate) is a panel-derived rate where large banks submit quotes for the cost to borrow unsecured cash from one another. A bank's LIBOR quote implies it would lend to other banks at that rate—which means LIBOR prices in the credit risk of the submitting banks. When a bank's funding stress rises, its LIBOR contribution may creep up. When system-wide credit fear strikes, LIBOR climbs and the [bid-ask spread](/bid-ask-spread/) widens.

## The OIS-LIBOR spread: what it measures

The **OIS-LIBOR basis**—the difference between a LIBOR swap and an equivalent OIS—is the market's measure of credit risk in the interbank system. In normal times, LIBOR sits only 10–50 basis points above OIS, reflecting modest compensation for bank credit exposure and the structural illiquidity of unsecured term lending.

During a [credit cycle](/credit-cycle/) downturn or panic, the basis explodes. In the 2008 financial crisis, the 3-month LIBOR-OIS spread reached 360 basis points; even after central banks deployed emergency lending facilities, it remained elevated for months. In March 2020, as the pandemic triggered equity market chaos, the spread spiked to 100+ basis points again—not a systemic banking collapse, but acute stress in short-term funding.

The spread widens because:
- Risk-averse banks pull back from unsecured lending, raising LIBOR quotes
- Banks and corporates fleeing to safety demand overnight repo (the funding mechanism underlying OIS), driving OIS lower
- Speculative traders and hedgers rebalance [derivatives-hedging](/derivatives-hedging/) portfolios, amplifying the move

## Cashflow mechanics and conventions

Both instruments are [interest rate swap](/swap/) variants. A typical 2-year contract might be:

- **OIS**: pay fixed 1.50%, receive floating SOFR (or Fed funds) daily-compounded
- **LIBOR swap**: pay fixed 1.65%, receive 3-month LIBOR quarterly

The reason a LIBOR swap fixed rate is higher reflects the credit premium and term-lending illiquidity. When pricing a [rate hedging](/derivatives-hedging/) program, a borrower choosing which swap to reference depends on:
- **Operational matching**: if the underlying debt is LIBOR-indexed, a LIBOR swap is the natural hedge
- **Cost**: in benign credit conditions, LIBOR swaps may appear cheaper (tighter spread); in stress, the opposite
- **Counterparty appetite**: during crises, dealers may widen LIBOR swap pricing or reduce [market-maker-trading](/market-maker-trading/) sizes

## Why basis risk matters in a portfolio

A sophisticated borrower or [hedge fund](/hedge-fund/) that holds both OIS and LIBOR swaps faces **basis risk**—the risk that the spread between them moves unexpectedly. For example:

- A borrower hedges a LIBOR-indexed loan with a LIBOR swap (natural hedge)
- But to lower borrowing costs, she pays fixed OIS, receives floating LIBOR, and takes the short basis position
- If LIBOR rallies hard because her bank gets downgraded, the LIBOR swap loss exceeds the loan's floating-rate benefit—basis widens against her

Dealers manage this basis position as a [trading strategy](/algorithmic-trading/). In 2022–2024, dealers bid aggressively on OIS and offered LIBOR swaps, betting that the spread would compress toward historical norms once credit fears subsided. This is a view on the [credit-spread](/credit-spread/) dynamic, not on rate direction.

## Transition and regulatory shifts

Notably, LIBOR has been phased out. As of end-2023 in the U.S. and 2024 in other jurisdictions, new LIBOR contracts are no longer issued. The market has migrated to [SOFR](/sofr/) (Secured Overnight Financing Rate)—a transaction-based overnight rate like federal funds, but backed by Treasury repo. SOFR-based swaps increasingly serve the role LIBOR swaps played.

However, legacy LIBOR swaps remain in portfolios and trade actively in the secondary market. Understanding the OIS-LIBOR comparison is still essential for:
- Traders managing legacy positions
- Risk managers valuing historical [credit-default-swap](/credit-default-swap/) relationships
- Analysts tracking interbank credit stress as an early-warning signal

## Practical implications for traders and risk managers

The OIS-LIBOR basis is watched as a real-time gauge of financial stress. Central banks and regulators monitor it closely; a widening basis signals:
- Bank [counterparty-risk](/counterparty-risk/) concerns
- Tightening liquidity in term funding markets
- Potential contagion risk across derivative exposures

Traders exploit these moves through **curve trades**—simultaneously going long OIS and short LIBOR (or vice versa)—to capture basis compression or expansion without taking outright rate risk. For example, in early 2023, regional bank stress in the U.S. temporarily widened the OIS-LIBOR basis, and relative-value traders who shorted the basis made substantial P&L.

Because the spread is tightly watched and liquid, it moves efficiently; excess profits are hard to capture persistently. But the basis remains an asymmetric bet: when credit conditions weaken, the basis almost always widens. When they improve, the tightening can be slower and less dramatic.

## See also

<div class="wiki-seealso">

### Closely related

- [SOFR](/sofr/) — the transaction-based overnight rate replacing LIBOR
- [Interest Rate Swap](/swap/) — mechanics and conventions for fixed-for-floating exchanges
- [Credit Spread](/credit-spread/) — the LIBOR-OIS basis as a measure of interbank credit risk
- [Swap](/swap/) — foundational swap structure and terminology
- [Derivatives Hedging](/derivatives-hedging/) — how swaps are used to manage rate risk
- [Federal Reserve](/federal-reserve/) — the central bank behind overnight rate administration
- [Counterparty Risk](/counterparty-risk/) — credit exposure in derivatives transactions

### Wider context

- [Interest Rate Risk](/interest-rate-risk/) — why fixed-rate hedging matters
- [Credit Cycle](/credit-cycle/) — the broader pattern of credit expansion and stress
- [Market Cycle](/market-cycle/) — how swaps and spreads respond to economic cycles
- [Financial Stress Testing](/stress-testing/) — how regulators monitor basis widening

</div>
