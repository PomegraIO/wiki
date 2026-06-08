---
title: "Bond Spread Over Treasury: What It Means"
description: "A bond spread is the yield premium above a risk-free Treasury benchmark. Learn how spreads are quoted, why they change, and what widening or tightening signals."
keywords:
  - bond spread over treasury
  - credit spread meaning
  - bond yield spread
  - treasury spread bonds
  - spread widening
---

*A **bond spread** is the difference between the [yield](/yield-to-maturity/) on a corporate, municipal, or other risky bond and the yield on a [Treasury bond](/treasury-bond/) of similar maturity. It represents the extra return investors demand to compensate for credit risk, liquidity risk, and other factors beyond the risk-free rate. Spreads widen when investors demand more compensation (signaling rising default fear), and tighten when fear recedes.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Bond Spread — key facts</div>

<img src="/svg/fixed-income.svg" alt="An abstract editorial mark for fixed income." />

<div class="wiki-infobox-caption">The extra yield an investor is paid for bearing credit and liquidity risk.</div>

|   |   |
|---|---|
| **Definition** | Corporate (or other) bond yield − Treasury yield |
| **Units** | Basis points (bps); 100 bps = 1% |
| **Benchmark** | Treasury of same maturity (e.g., 10-year corporate vs. 10-year Treasury) |
| **What it reflects** | Credit risk, liquidity risk, supply/demand, market stress |
| **Typical range (IG corps)** | 100–300 bps (varies by cycle and sector) |
| **Typical range (high-yield)** | 300–800 bps (much wider; higher default risk) |
| **Widening** | Signal of rising concern about default risk or overall market stress |
| **Tightening** | Signal of confidence, lower default risk, or improving economic conditions |

</aside>

## How bond spreads are quoted

A bond spread is expressed in **basis points** (bps)—hundredths of a percentage point. If a 10-year corporate bond yields 4.50% and the 10-year Treasury yields 3.75%, the spread is 75 basis points.

The choice of Treasury maturity matters. A corporate bond's spread is measured against the Treasury of the **same maturity**. A 5-year corporate bond is compared to the 5-year Treasury, not the 10-year. This ensures the risk-free rate used as a benchmark reflects the same time horizon as the bond being analyzed.

In practice, traders and bond managers refer to spreads conversationally: "XYZ Corp trades at plus-80," meaning 80 basis points above the Treasury curve. Financial terminals (Bloomberg, Refinitiv) display spreads in real time, updated as both bond and Treasury prices move.

## What a spread compensates for

The spread is not purely about default risk—though that is a major component. Several factors stack into it.

**Credit risk.** The primary driver. A company with weak earnings, high leverage, or deteriorating industry conditions has a wider spread because the probability of default is higher. If the company is investment-grade (rated BBB− or higher), the spread is modest (typically 50–200 bps for industrials). If the company is junk-rated (BB and below), the spread is wide (400 bps or more) because default is a real possibility.

**Liquidity risk.** A bond that trades infrequently commands a wider spread than an actively traded one. A mega-cap tech firm's bond might trade at 40 bps, while a smaller regional company's bond (with similar credit quality) might trade at 80 bps because fewer investors buy it and selling requires more concession.

**Sector and cyclical risk.** A cyclical sector (e.g., automotive, retail, commodities) tends to have wider spreads than a defensive one (e.g., utilities, healthcare) because earnings are more volatile. During an economic downturn, cyclical spreads widen sharply because investors worry about recession defaults.

**Market supply and demand.** If a large issuer floods the market with new bonds, spreads widen temporarily due to oversupply. Conversely, if a bond becomes scarce in the secondary market, its spread can tighten even if nothing about the issuer changed.

**Time to maturity.** Spreads are usually wider for longer-dated bonds (higher [duration](/duration/)) because there is more time for something to go wrong. A company's 2-year bond might spread 30 bps, while its 10-year bond spreads 70 bps.

**Embedded options.** A [callable bond](/callable-bond/) (one the issuer can redeem early) trades at a wider spread than a similar non-callable bond because the investor faces reinvestment risk if rates fall.

## Spread widening and tightening: what they signal

The daily movement of spreads is one of the most closely watched indicators in fixed income. Widening spreads signal alarm; tightening spreads signal confidence.

**Widening spreads.** When a company releases disappointing earnings, downgrades its guidance, or faces industry headwinds, its bond spreads widen. Investors demand more yield to compensate for elevated default risk. In a market stress scenario (e.g., a financial crisis, a credit event, or a sharp recession), spreads across the market widen simultaneously. The high-yield or junk-bond market is especially sensitive; spreads can widen 100–200 bps in a day if fear spikes.

A widening spread does not necessarily mean the bond price falls in absolute terms—it depends on whether rates move too. If the Treasury yield falls by 100 bps while the spread widens 50 bps, the corporate bond yield drops 50 bps overall, and the bond price rises. But spreads themselves track investor sentiment independently of rate moves.

**Tightening spreads.** As economic data improve, defaults slow, or central banks cut rates and reduce systemic risk, spreads narrow. Investors are willing to hold riskier assets at lower extra yields because fear is receding. After a recession ends and earnings stabilize, high-yield spreads often tighten 200–400 bps as investors rush back into credit.

## Spread monitoring in practice

Fixed income portfolios are managed on a spread basis as much as an absolute yield basis. A portfolio manager tracking corporate bonds does not just watch their individual prices; she watches:

- **OAS (Option-Adjusted Spread).** This adjusts the simple yield spread for embedded options (call features, prepayment options, etc.), giving a cleaner measure of credit compensation. Most bond indices and risk systems use OAS rather than simple spreads.

- **Sector spreads.** Different sectors—utilities, industrials, energy, financials, consumer—have different average spreads reflecting their cyclicality and leverage profiles. A manager might find value by overweighting a sector whose spread has widened excessively relative to historical averages.

- **Spread-to-history.** If a company's spread is at a 5-year high, it might signal either a genuine deterioration in creditworthiness or an overreaction that presents a buying opportunity. Comparing current spreads to historical ranges is a core analytical practice.

- **CCC-B-BB laddering.** High-yield managers often build positions across ratings tranches (lowest-rated to higher-rated) and compare spreads within the junk universe to find relative value.

## Spreads in context: risk-free rate is not the only variable

It is important to distinguish between spread changes and yield changes. A bond's yield moves for two reasons: (1) the risk-free rate (Treasury yield) changes, and (2) the spread changes. Understanding which is driving the price is crucial for bond investing.

Suppose a corporate bond yielded 4.00% (with Treasury at 3.00%, spread 100 bps) last month. This month, it yields 4.10%. Why?

- **Scenario A:** Treasury rose to 3.20%, spread unchanged at 100 bps. Corporate yield is now 4.20%. (The stated 4.10% would imply the spread compressed; something is inconsistent here. But the principle holds: if Treasury rises and spread is stable, the corporate yield rises.)

- **Scenario B:** Treasury fell to 2.75%, but spread widened to 135 bps. Corporate yield is now 4.10%. The tighter risk-free rate offset the wider spread.

Traders and portfolio managers run split analysis: "How much of the move is macro (rate-driven) versus credit (spread-driven)?" A portfolio that is rate-hedged might still suffer losses if spreads widen, and vice versa.

## Spread metrics for portfolio construction

Several spread-based metrics guide bond portfolio decisions.

**[Credit spread](/credit-spread/).** The simple yield differential, the most common metric for individual bonds.

**[Duration-weighted spread.** In a portfolio, spreads are averaged with duration weighting so that longer-dated bonds (which move more) get higher weight in the portfolio's aggregate spread.

**Spread duration.** How much portfolio value changes if spreads move 1 basis point (separate from rate duration). A portfolio with high spread duration is more sensitive to credit conditions.

A typical corporate bond portfolio might have a spread duration of 3–5 years, meaning if spreads widen 50 bps, the portfolio loses about 1.5%–2.5% in value (all else equal).

## Historical perspective: normal vs. stressed spreads

Spreads are not constant. They compress in bull markets and expand in crises.

**Normal times.** Investment-grade corporate spreads typically range 75–150 bps; high-yield, 300–600 bps. These are tighter in low-volatility periods and wider in slow-growth periods.

**Crisis.** In 2008–2009, IG spreads blew out to 600+ bps; HY spreads exceeded 2,000 bps. In March 2020 (COVID shock), similar spikes occurred. These represent panic and forced selling, not fundamental valuation. Over weeks or months, spreads normalized as central banks intervened and the immediate crisis passed.

**Recovery.** After a crisis, spreads gradually tighten as default rates fall and growth returns. This tightening is often one of the first profit opportunities for credit investors—buying when spreads are abnormally wide.

## See also

<div class="wiki-seealso">

### Closely related

- [Credit spread](/credit-spread/) — the technical definition underlying bond spreads
- [Yield to maturity](/yield-to-maturity/) — the absolute yield component of spread analysis
- [Duration](/duration/) — how bond prices respond to spread and rate moves
- [Option-adjusted spread](/credit-spread/) — an refinement that accounts for embedded options
- [Corporate bond](/corporate-bond/) — the main security type priced on spreads
- [Treasury bond](/treasury-bond/) — the risk-free benchmark

### Wider context

- [Credit risk](/credit-risk/) — the fundamental risk reflected in spreads
- [Bond](/bond/) — the broader asset class context
- [Yield curve](/yield-curve/) — how spreads vary by maturity
- [Junk bond](/junk-bond/) — the highest-spread segment of the market

</div>
