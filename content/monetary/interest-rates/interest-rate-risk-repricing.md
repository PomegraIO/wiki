---
title: "Repricing Risk"
description: "The mismatch between assets and liabilities that reprice at different times, exposing financial institutions to net-interest-margin swings."
keywords:
  - repricing risk
  - net interest margin
  - asset-liability management
  - interest rate mismatch
  - rate reset schedule
  - gap analysis
image: "/svg/monetary.svg"
---

*A bank borrows short-term (deposits, funding markets) but lends long-term (mortgages, bonds). When [interest-rate](/interest-rate/) cycles turn, assets and liabilities don't reset in sync—a mismatch that either protects or cripples the net-interest-margin. **Repricing risk** is the exposure to this timing difference.*

<div class="wiki-hatnote">

For the broader category of yield and [interest-rate-risk](/interest-rate-risk/), see [Interest Rate Risk](/interest-rate-risk/). Repricing risk is a subset specific to mismatched asset and liability repricing schedules.

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Repricing Risk — key facts</div>

<img src="/svg/monetary.svg" alt="An abstract editorial mark for financial risk and time horizons." />

<div class="wiki-infobox-caption">Banks profit from the spread between deposit rates (low) and loan rates (high), but only if repricing happens in the right order.</div>

|   |   |
|---|---|
| **What it is** | The earnings exposure from assets and liabilities resetting at different times |
| **Also called** | Gap risk, maturity mismatch, repricing gap |
| **Primary risk to** | Banks, [mortgage-reit](/mortgage-reit/), financial institutions |
| **Measured by** | Gap analysis, repricing ladders |
| **Mitigated by** | [Interest-rate](/interest-rate/) swaps, floating-rate funding, matched-maturity lending |

</aside>

## The classic bank problem

A retail bank collects deposits on which it pays 2% annually. It lends out those deposits as 30-year fixed-rate mortgages at 6% annually. In year one, the spread is 4 percentage points—a profitable net-interest-margin. But the mortgage doesn't reprice; the deposit rate does.

Suppose the [Federal Reserve](/federal-reserve/) raises the policy [interest-rate](/interest-rate/) sharply, and deposit rates rise to 4%. The bank's mortgage still pays 6%, but it now costs 4% to fund it. The spread narrows to 2 percentage points. If rates rise further to 5%, the spread collapses to 1 percentage point. The bank's profits shrink, not because it made bad loans, but because the two sides of the balance sheet repriced at different times.

This is repricing risk. The bank's **assets** (mortgages) are locked in at 6%. Its **liabilities** (deposits) are floating. When rates rise, the cost of liabilities rises faster than the income from assets, squeezing margin. When rates fall, the cost of liabilities falls faster than asset income rises (because the mortgage rate can't drop below 6%), again squeezing margin, though in the opposite direction.

## Gap analysis and repricing ladders

Banks measure repricing risk through **gap analysis**: matching assets and liabilities into time buckets (zero to three months, three to six months, six to twelve months, one to two years, etc.). In each bucket, they calculate the net repricing exposure—how much more (or less) in assets reprices than liabilities.

A sample repricing ladder might look like:

- **0–3 months:** +$500M in assets, −$200M in liabilities = +$300M net gap (rate-sensitive assets exceed rate-sensitive liabilities)
- **3–6 months:** −$100M = net liability gap
- **6–12 months:** +$50M = net asset gap

If [interest-rate](/interest-rate/)s rise in the next three months, the bank earns an extra $300 million at the new higher rates, boosting the net-interest-margin—a positive outcome. But if rates fall, that same gap means $300 million of margin contraction.

Banks want their gap profiles matched to their view of the [interest-rate](/interest-rate/) environment and their risk tolerance. A bank expecting rates to rise can accept an **asset-sensitive gap** (more assets reprice than liabilities). A bank expecting rates to fall can accept a **liability-sensitive gap** (more liabilities reprice than assets). A bank neutral on rates aims for a **matched gap** across the repricing ladder.

## Repricing risk in a rising-rate environment

When the [Federal Reserve](/federal-reserve/) embarks on a rate-hiking cycle, liability-sensitive banks (more liabilities repricing than assets) suffer margin compression. Their deposit costs rise immediately; asset yields rise slowly (mortgages, long-term loans reprice only at maturity or refinance).

This happened sharply in 2022–2023. Many regional and mid-sized banks had built up cheap, sticky deposit bases during years of ultra-low rates. When the [Federal Reserve](/federal-reserve/) raised the policy rate from near zero to 5.25–5.50%, deposits repriced almost overnight to 4%+ to stem outflows, while mortgage portfolios—locked in at 2–3% from 2020–2021—remained largely unchanged. Repricing risk turned into margin compression and, for some institutions, insolvency. Silicon Valley Bank is the most visible example: it held $91 billion in available-for-sale securities earning 1.6% on average while new deposits demanded 4% or more.

## Asset-sensitive structures: a shelter in rising rates

Conversely, banks with asset-sensitive gaps—more assets repricing than liabilities—benefit as rates rise. If a bank holds $100 million in floating-rate commercial loans repricing every three months and funds them with fixed-rate bonds maturing in five years, it captures the benefit of higher rates on the asset side while the funding rate stays locked.

Mortgage [real-estate-investment-trust](/real-estate-investment-trust/) (REITs) also exhibit repricing risk. A mortgage REIT borrows short-term (using repurchase agreements, or repos) and buys long-dated mortgage-backed securities. In rising-rate environments, the REIT's funding costs (repriced daily in the repo market) spike while the securities' coupons reprice slowly, compressing [net-operating-income](/net-operating-income/). The structure is intentionally asset-sensitive—betting that the yield spread compensates for the repricing gap—but if rates rise faster than anticipated, the economics deteriorate.

## Dynamic hedging: swaps and derivatives

Modern banks don't passively accept repricing risk. They use [interest-rate](/interest-rate/) swaps to rebalance. A bank with a liability-sensitive gap (fearing margin compression) can pay fixed on a swap and receive floating, converting fixed-rate liabilities into synthetic floating-rate liabilities that reprice with assets.

Example: A bank borrows $50 million at a fixed rate of 4% (a five-year bond) but wants to convert this into floating-rate funding to match its repricing ladder. It enters a five-year [interest-rate](/interest-rate/) swap, paying 4.2% fixed and receiving SOFR (the overnight funding rate). The net result: the bank now effectively pays SOFR + spread, making the liability repricing-matched to its assets.

[Interest-rate](/interest-rate/) swaps, caps, floors, and other derivatives let banks fine-tune their repricing profiles without restructuring the balance sheet. This is expensive (dealers charge spreads and fees), but the cost is often worth it to avoid margin compression.

## Duration and repricing gap are different

It's easy to conflate repricing risk with [duration](/duration/) or [interest-rate-risk](/interest-rate-risk/). They're related but distinct.

**[Interest-rate-risk](/interest-rate-risk/)** is the risk that the market value of a security falls if [interest-rate](/interest-rate/)s rise. A bondholder holding a [bond](/bond/) to maturity doesn't care about mark-to-market losses; they only care if the borrower defaults. But a bank carrying held-for-sale securities on the balance sheet faces [interest-rate-risk](/interest-rate-risk/).

**Repricing risk** is the risk that net-interest-margin (the difference between what the bank earns and what it pays) shrinks due to timing mismatches. A bank with a [bond](/bond/) portfolio locked in at 2% faces [interest-rate-risk](/interest-rate-risk/) if rates rise (the securities' market value falls), but it faces repricing risk only if its funding costs are floating.

A bank can have low [interest-rate-risk](/interest-rate-risk/) (because it plans to hold securities to maturity) but high repricing risk (because funding reprices much faster than assets). Regulators watch both.

## See also

<div class="wiki-seealso">

### Closely related

- [Interest Rate Risk](/interest-rate-risk/) — the broader category of losses from adverse rate moves
- Net Interest Margin — the spread between what a bank earns and pays
- [Duration](/duration/) — how price sensitivity varies with maturity
- [Interest Rate Swap](/interest-rate-swap/) — the primary tool to manage repricing mismatches
- [Federal Reserve](/federal-reserve/) — whose rate hikes trigger repricing cycles

### Wider context

- [Mortgage Backed Security](/mortgage-backed-security/) — a common long-dated asset for banks
- [Basis Point Sensitivity](/basis-point-sensitivity/) — quantifying repricing exposure in dollar terms
- [Asset Allocation](/asset-allocation/) — how banks structure the balance sheet
- [Real Estate Investment Trust](/real-estate-investment-trust/) — another repricing-risk–sensitive instrument
- [Credit Risk](/credit-risk/) — a separate risk complement to repricing risk

</div>
