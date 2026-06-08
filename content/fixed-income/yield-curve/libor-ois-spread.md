---
title: "LIBOR-OIS Spread"
description: "The difference between LIBOR (interbank lending rates) and OIS (overnight swap rates); a key gauge of banking-system stress and credit risk."
keywords:
  - libor
  - overnight indexed swap
  - credit spread
  - banking crisis
  - financial stress
---

*The **LIBOR-OIS spread** is the gap between the London Interbank Offered Rate and overnight indexed swap rates, both measured at the same tenor (typically 3-month or 1-month). It captures the credit risk and liquidity stress embedded in interbank lending, widening sharply during financial crises and narrowing in calm markets.*

<div class="wiki-hatnote">

For the broader concept of overnight swap rates, see [SOFR](/sofr/); for historical LIBOR mechanics, see [LIBOR](/libor/).

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">LIBOR-OIS Spread — Key facts</div>

<img src="/svg/fixed-income.svg" alt="An abstract editorial mark denoting fixed-income instruments and credit measurement." />

<div class="wiki-infobox-caption">A widening spread signals rising fear in the banking system; a narrow spread indicates confidence in interbank credit.</div>

|   |   |
|---|---|
| **What it is** | Difference between LIBOR and OIS rates at the same maturity |
| **Typical normal range** | 5–15 basis points in stable conditions |
| **Crisis levels** | 50–100+ basis points during acute stress |
| **Key driver** | Bank creditworthiness and willingness to lend |
| **Use case** | Barometer of financial stability and [credit risk](/credit-risk/) |
| **Also called** | TED spread (for 3-month LIBOR vs. Treasury bills) |

</aside>

## The spread's anatomy

[LIBOR](/libor/) is the average rate at which major banks lend unsecured funds to each other for short tenors—usually 1, 3, 6, or 12 months. A bank needing liquidity borrows at LIBOR; a bank with excess cash lends at LIBOR.

An overnight indexed swap (OIS) is a derivative contract in which two parties exchange fixed and floating cash flows based on overnight rates (now [SOFR](/sofr/) in the U.S., replacing the old federal funds rate). The OIS rate reflects the *expected average* of overnight rates over the contract's life, plus a small risk premium.

The spread between them—LIBOR minus OIS—captures credit risk. LIBOR is an unsecured loan rate; OIS is backed by overnight collateral and central-bank operations. When banks are confident in each other's creditworthiness, the spread is narrow (5–15 basis points). When doubt creeps in, it widens.

## What causes widening

The spread balloons when [counterparty risk](/counterparty-risk/) rises—when one or more major banks face suspected insolvency or severe [liquidity risk](/liquidity-risk/). During the 2008 financial crisis, the 3-month LIBOR-OIS spread hit 364 basis points in October, a historic peak. Banks stopped lending to each other unsecured; only the safest, most-collateralized funding (overnight) moved freely.

More recent episodes show similar mechanics. During the March 2020 COVID crash, the spread spiked to 70 basis points as credit concerns re-emerged. In 2023, bank failures in the U.S. (Silicon Valley Bank, Signature Bank) triggered fears of broader [systemic risk](/systemic-risk/), widening the spread again.

The spread also reacts to central-bank policy and balance-sheet moves. If the [Federal Reserve](/federal-reserve/) is perceived as tightening financial conditions or withdrawing liquidity, banks demand higher LIBOR premiums. Conversely, Fed [quantitative easing](/quantitative-easing/) or emergency lending programs (like the Federal Reserve's repo facilities) narrow the spread by reassuring banks they can access liquidity.

## The TED spread connection

The original "TED spread"—named in the 1980s—was the gap between 3-month T-bill yields and 3-month LIBOR. It served the same purpose: a gauge of financial stress. The 2008 peak of the TED spread (around 450 basis points) marked near-total loss of confidence in the banking system.

Since LIBOR's scheduled phase-out (ongoing since 2021, with most tenors ceasing publication by end-2023), the LIBOR-OIS spread has become less relevant as a real-time indicator. [SOFR](/sofr/) and other risk-free rates have replaced LIBOR in new contracts. Some traders now track analogous spreads—between corporate [overnight indexed swap](/sofr/) rates and risk-free OIS—but the conceptual framework remains the same.

## Using the spread strategically

Risk managers use the spread to size their banking [counterparty risk](/counterparty-risk/). A 10 basis-point spread might justify standard collateral posting. A 100 basis-point spread signals major concerns; firms may demand higher collateral or exit positions.

[Credit rating](/credit-rating/) analysts watch it for early signs of systemic stress. A sudden widening, even if no single bank has formally failed, often precedes credit downgrades or depositor runs.

Traders betting on financial stress—via [put options](/put-option/) on bank stocks or [credit spreads](/credit-spread/) on bank [bonds](/bond/)—often pair these trades with a long LIBOR-OIS position (expecting the spread to widen). A trader confident in system stability might short the spread, pocketing the compression as confidence returns.

## The shift to SOFR and beyond

As of 2023–2024, most LIBOR tenors have been discontinued in favor of [SOFR](/sofr/) and other risk-free rates. The LIBOR-OIS spread's relevance as a live market indicator has diminished. However, historical data remains important for academic study and risk-model backtesting. New analytics focus on spreads between credit-sensitive rates (like SOFR-based term rates offered by banks) and pure risk-free overnight indices.

## See also

<div class="wiki-seealso">

### Closely related

- [LIBOR](/libor/) — the interbank rate that LIBOR-OIS measures
- [SOFR](/sofr/) — the risk-free overnight rate replacing LIBOR
- [Credit spread](/credit-spread/) — broader concept of compensation for credit risk
- [Counterparty risk](/counterparty-risk/) — the risk one party will default on a contract
- [Liquidity risk](/liquidity-risk/) — difficulty converting assets to cash
- [Interest rate](/interest-rate/) — the foundation of all spread calculations

### Wider context

- [Credit risk](/credit-risk/) — the core concept driving the spread
- [Central bank](/central-bank/) — whose actions shape interbank lending conditions
- [Federal Reserve](/federal-reserve/) — the U.S. central bank whose policy dominates short-rate spreads
- Financial crisis — when spreads widen most dramatically
- [Systemic risk](/systemic-risk/) — the broader financial-stability concern the spread reflects

</div>
