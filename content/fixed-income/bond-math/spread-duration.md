---
title: "Spread Duration"
description: "The sensitivity of a bond's price to a one-basis-point change in its credit spread relative to a risk-free benchmark."
keywords:
  - credit spread
  - bond duration
  - price sensitivity
  - risk measurement
image: "/svg/fixed-income.svg"
---

*A **spread duration** (or **credit duration**) measures how much a [bond's](/bond/) price changes when its [credit spread](/credit-spread/)—the yield premium it offers over a [risk-free](/treasury-bond/) benchmark—shifts by one basis point. It is distinct from standard [duration](/duration/), which measures [interest-rate](/interest-rate/) sensitivity, and is essential for managing [credit risk](/credit-risk/) in fixed-income portfolios.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Spread Duration — key facts</div>

<img src="/svg/fixed-income.svg" alt="An abstract editorial mark for the fixed-income category." />

<div class="wiki-infobox-caption">A bond's price sensitivity to changes in credit spread, independent of interest-rate movements.</div>

|   |   |
|---|---|
| **What it is** | The percentage change in bond price per basis point of [credit spread](/credit-spread/) change |
| **Units** | Typically 1–15 years (similar to [duration](/duration/), but isolated to spread risk) |
| **What it isolates** | [Credit risk](/credit-risk/) and [counterparty risk](/counterparty-risk/) from [interest-rate risk](/interest-rate-risk/) |
| **Used by** | Credit investors, [hedge fund](/hedge-fund/) managers, [fixed income](/bond/) portfolio managers |
| **Related concepts** | [Duration](/duration/), [option-adjusted spread](/credit-spread/), [credit risk](/credit-risk/) |

</aside>

## Understanding spread duration

A [bond's](/bond/) [yield](/interest-rate/) consists of two components: the risk-free rate (typically the [Treasury](/treasury-bond/) yield) and a [credit spread](/credit-spread/)—the extra return demanded for [credit risk](/credit-risk/), [liquidity risk](/liquidity-risk/), or both. When the [Treasury](/treasury-bond/) rate moves, the [bond's](/bond/) price adjusts according to its [duration](/duration/). But when the [credit spread](/credit-spread/) widens or tightens independently (e.g., due to a [credit-rating](/credit-rating/) change or broader market sentiment about [credit risk](/credit-risk/)), the [bond's](/bond/) price adjusts according to its spread duration.

**Example:**
A [corporate bond](/corporate-bond/) with a spread duration of 5 will decline by approximately 5% in price if its [credit spread](/credit-spread/) widens by 100 basis points (1 percentage point)—even if [Treasury](/treasury-bond/) rates remain unchanged. Conversely, if the spread tightens by 100 basis points, the [bond](/bond/) price rises by approximately 5%.

This decoupling of [interest-rate risk](/interest-rate-risk/) and [credit risk](/credit-risk/) is powerful for portfolio managers who want to know what drives their returns. A [bond](/bond/) can underperform if [Treasury](/treasury-bond/) rates rise (captured by [duration](/duration/)) or if [credit spreads](/credit-spread/) widen (captured by spread duration). Each risk deserves its own metric.

## How spread duration differs from standard duration

**[Duration](/duration/)** measures the bond's price sensitivity to a parallel shift in the yield curve—that is, to changes in the risk-free rate. A [bond](/bond/) with a [duration](/duration/) of 7 will decline by approximately 7% if all [interest rates](/interest-rate/) rise by 100 basis points.

**Spread duration** isolates the bond's sensitivity to changes in its spread relative to [Treasuries](/treasury-bond/) or another benchmark, holding the risk-free rate constant. It reflects how much [credit risk](/credit-risk/) is embedded in the [bond's](/bond/) current yield.

The two are related but distinct. A [bond's](/bond/) total [duration](/duration/) captures both [interest-rate risk](/interest-rate-risk/) and [credit risk](/credit-risk/). If a [bond](/bond/) has a [duration](/duration/) of 6 and a spread duration of 4, then 4 units of that duration stem from [credit risk](/credit-risk/) and roughly 2 from [interest-rate risk](/interest-rate-risk/).

## Computing spread duration

Spread duration is computed similarly to standard [duration](/duration/). The analyst calculates the bond's price at the current spread, then at the spread plus one basis point (and sometimes minus one basis point), and measures the percentage change. The result is the spread duration.

For most [bonds](/bond/), spread duration is approximately the [modified duration](/duration/) of the [bond](/bond/) if we ignore the risk-free rate. More precisely:

**Spread Duration ≈ Modified Duration × (Spread / Yield)**

For a [high-yield bond](/high-yield-bond/) with a [yield](/interest-rate/) of 8% (200 basis points of spread over a 6% [Treasury](/treasury-bond/)), the spread duration is roughly 25% of the [modified duration](/duration/)—meaning [credit risk](/credit-risk/) accounts for a quarter of the [bond's](/bond/) price sensitivity, and interest-rate risk the rest.

This approximation breaks down for bonds near [maturity](/yield-to-maturity/) or with embedded [options](/option/), where convexity becomes important.

## Spread duration in portfolio management

Portfolio managers use spread duration to quantify [credit exposure](/credit-risk/). If a manager believes [credit spreads](/credit-spread/) will tighten (improving credit conditions), they may overweight bonds with high spread duration to capture the upside. If they fear a credit shock and spread widening, they may shift to shorter-spread-duration positions or quality-focused bonds.

A typical [high-yield bond](/high-yield-bond/) [fund](/mutual-fund/) might have a spread duration of 3–5 years, reflecting significant [credit exposure](/credit-risk/). An [investment-grade corporate bond](/investment-grade-bond/) [fund](/mutual-fund/) might have a spread duration of 1–3 years, indicating lower [credit risk](/credit-risk/). [Treasury](/treasury-bond/) bonds have zero spread duration (no [credit spread](/credit-spread/)).

[Relative value](/relative-valuation/) analysis often uses spread duration to compare [bonds](/bond/) fairly. A [bond](/bond/) offering 150 basis points of spread with a spread duration of 4 is cheaper (in expected return per unit of [credit exposure](/credit-risk/)) than a [bond](/bond/) offering 100 basis points with a spread duration of 5, all else equal.

## Spread duration and market dislocations

During periods of market stress ([credit events](/credit-event-sovereign/), financial crises), [credit spreads](/credit-spread/) can widen violently. The 2008 financial crisis saw [high-yield](/high-yield-bond/) spreads widen by 500–1,000 basis points in months. A [portfolio](/mutual-fund/) with a spread duration of 5 would have lost approximately 25–50% from spread widening alone, independent of any change in [Treasury](/treasury-bond/) rates. This is why spread duration is a crucial [risk management](/stress-testing/) metric.

Conversely, when [credit conditions](/credit-rating/) improve and spreads tighten, [bonds](/bond/) with high spread duration outperform. The rally in [investment-grade](/investment-grade-bond/) [spreads](/credit-spread/) in 2009–2010, after the financial crisis, delivered outsized returns to portfolios that carried spread duration through the downturn.

## Spread duration and curve positioning

Spread duration is often combined with [duration](/duration/) to create a two-dimensional risk picture. A portfolio might have:
- **[Duration](/duration/):** 5 years (interest-rate risk)
- **Spread duration:** 3 years (credit risk)

This tells investors exactly what they are long and short. If [Treasury](/treasury-bond/) rates rise but [spreads](/credit-spread/) tighten (a common scenario in economic slowdowns where the central bank cuts rates and credit conditions improve), the portfolio's [duration](/duration/) loss is offset by spread duration gain.

Managers can use spread duration targets to align the portfolio with market views. Believing spreads will remain stable or tighten, a manager might intentionally increase spread duration. Expecting volatility or stress, they might reduce it.

## Spread duration and credit indices

[Credit indices](/bond-etf/) (e.g., [investment-grade corporate bond](/corporate-bond/) indices, [high-yield](/high-yield-bond/) indices) publish weighted-average spread durations. These serve as benchmarks for assessing whether a particular [fund](/mutual-fund/) or portfolio has taken on more or less [credit exposure](/credit-risk/) than the index.

An [actively-managed fund](/actively-managed-fund/) with a spread duration of 3.5 versus an index spread duration of 3 is intentionally overweighting [credit risk](/credit-risk/) slightly, betting on spread tightening or positive [credit](/credit-rating/) surprises. A spread duration of 2.5 represents a more defensive [credit](/credit-rating/) positioning.

## Spread duration in exotic instruments

[Mortgage-backed securities](/mortgage-backed-security/) and [asset-backed securities](/securitization/) have embedded spread duration components. [Securitizations](/securitization/) backed by [corporate](/corporate-bond/) or [emerging-market](/sovereign-default/) loans carry both [prepayment](/refinancing-risk/) risk (analogous to [call risk](/callable-bond/)) and [credit risk](/credit-risk/). The spread duration of a [securitization](/securitization/) reflects the weighted-average [credit risk](/credit-risk/) of the underlying asset pool.

[Convertible bonds](/convertible-bond/) also have spread duration, though it may be less obvious. The [bond component](/bond/) of a [convertible](/convertible-bond/) carries [credit spread](/credit-spread/) risk separate from the [equity option](/stock/) component.

## Limitations

Spread duration assumes a parallel shift in the [credit spread curve](/credit-spread/)—that is, all maturities widen or tighten by the same amount. In reality, spread curves twist and curve. A widening in the 2-year [credit spread](/credit-spread/) may not match a 10-year spread widening. Spread duration also assumes the bond does not default and that [credit migration](/credit-rating/) (upgrading or downgrading) is continuous and smooth, not sudden.

For complex or illiquid [bonds](/bond/), spread duration estimates can be noisy or unreliable. [Market-makers](/market-maker-trading/) may reprice bonds without a movement in the broad [credit spread](/credit-spread/) index, so the spread duration estimated from index data may not apply to a specific security.

## See also

<div class="wiki-seealso">

### Closely related

- [Credit spread](/credit-spread/) — the yield premium of a [corporate bond](/corporate-bond/) over [risk-free](/treasury-bond/) debt
- [Duration](/duration/) — the sensitivity of a bond's price to interest-rate changes
- [Credit risk](/credit-risk/) — the risk that an issuer defaults or is downgraded
- [Option-adjusted spread](/credit-spread/) — a [spread](/credit-spread/) measure that accounts for [embedded options](/option/)
- [Counterparty risk](/counterparty-risk/) — the risk that a [bond](/bond/) issuer or counterparty fails

### Wider context

- [Corporate bond](/corporate-bond/) — a [bond](/bond/) issued by a business entity
- [High-yield bond](/high-yield-bond/) — a [bond](/bond/) with below-[investment-grade](/investment-grade-bond/) [credit rating](/credit-rating/)
- [Treasury bond](/treasury-bond/) — debt issued by a sovereign government, typically risk-free
- [Bond](/bond/) — a debt security with promised cash flows
- [Stress testing](/stress-testing/) — analysis of portfolio outcomes under adverse market scenarios

</div>
