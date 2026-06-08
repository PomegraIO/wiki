---
title: "How Net Asset Value Is Calculated for a Fund"
description: "Steps through NAV calculation formula and explains which valuation inputs are hardest to verify in illiquid funds."
keywords:
  - net asset value calculation fund
  - nav formula
  - fund valuation methods
  - illiquid asset valuation
  - marked-to-model valuation
image: /svg/funds.svg
---

*A fund's **Net Asset Value (NAV)** is calculated as: (Total Assets − Total Liabilities) ÷ Shares Outstanding. But the complexity lies in the numerator. For liquid funds holding public equities and bonds, asset values are objective (close prices). For private equity, real estate, and illiquid credit funds, valuations are estimates built on comparable companies, discounted cash flows, and management judgment—making NAV as much art as arithmetic.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Fund Net Asset Value — key facts</div>

<img src="/svg/funds.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">The per-share worth of fund assets, before fees, adjusted for leverage and illiquidity.</div>

|   |   |
|---|---|
| **Formula** | (Total Assets − Liabilities) ÷ Shares Outstanding |
| **Liquid assets** | Marked to market (daily/weekly) at exchange prices |
| **Illiquid assets** | Marked to model using comparable companies, DCF, or industry benchmarks |
| **Frequency** | Daily (mutual funds), weekly/monthly (closed-end), quarterly (private equity) |
| **Who validates** | Fund auditor and valuation committee (for private funds) |
| **Biases to watch** | Stale valuations, optimistic assumptions, GP self-dealing in pricing |
| **Impact on fees** | [Management fees](/management-fee/) often calculated as % of NAV |

</aside>

## The Formula and Its Moving Parts

The NAV formula is deceptively simple:

$$\text{NAV per share} = \frac{\text{Total Fund Assets} - \text{Total Fund Liabilities}}{\text{Number of Shares Outstanding}}$$

For a $1 billion fund with $100 million in debt, $900 million in net assets, and 10 million shares outstanding, NAV per share is $90.

But each component requires judgment:

**Total Fund Assets:**
- **Liquid holdings**: Public equity holdings are marked to the last closing price; bonds to bid/ask spreads; cash to its face value. This is deterministic and auditable.
- **Illiquid holdings**: Private equity holdings, restricted stock, derivatives, and real estate require valuation estimates.

**Total Fund Liabilities:**
- Borrowed debt (clear, contracted amount)
- [Management fees](/management-fee/) accrued but not yet paid (known in advance)
- Carried interest accrued but not yet realized (estimated; disputed between GPs and LPs)
- Contingent liabilities (litigation, earnout obligations, clawback reserves)

**Shares Outstanding:**
- Clear denominator for open-end funds and ETFs (shares traded daily)
- For closed-end and private funds, can be complicated by share classes, preferred returns, waterfall preferences, and different entry dates

The real complexity is valuing illiquid assets.

## Valuing Liquid Assets: Mark-to-Market

For publicly traded stocks, bonds, and derivatives, valuation is mechanical. A mutual fund holds 100,000 shares of Apple. The NAV reflects that holding at yesterday's close (4 PM) or today's opening price, depending on fund rules. No debate.

The same applies to corporate bonds with active trading—NAV reflects the last reliable bid-ask midpoint. Money market funds holding Treasury bills use the bill discount rate. No model, no assumption required.

Liquid-asset funds publish NAV daily and can allow daily redemptions because the denominator is objective.

## Valuing Illiquid Assets: Mark-to-Model

Illiquid assets—a leveraged buyout company, a development-stage startup, a distressed debt position—have no quoted market price. The fund must estimate what the asset is worth.

**Comparable Company Multiples**

The most common approach. A private equity fund holds a regional automotive parts supplier. The GP surveys public comparable companies (similar industry, revenue scale, geography) and notes they trade at an average of 6.5× EBITDA. If the held company has $50 million EBITDA, it is valued at $325 million.

The challenge: which comparables? Public companies are larger and better-managed than a typical PE-held company, so using pure public multiples overstates value. GPs typically apply a "private company discount" (10–30%) to account for illiquidity and operational risk. The assumption is contractual and debated, but defensible.

**Discounted Cash Flow (DCF)**

The GP projects the company's free cash flows for 5–10 years, applies a [discount rate](/discount-rate/) reflecting risk, and sums the present value. This is economically pure but relies on three subjective inputs:

- **Revenue growth assumptions**: Will the company grow 5% or 15% annually? Often hotly disputed.
- **Terminal value**: What is the company worth in Year 10? Is it stable, or do you assume a recovery?
- **Discount rate (WACC)**: Reflects the required return given the company's risk. A 2% difference in WACC assumption swings the valuation by 20%+.

Most GPs use DCF as a secondary sanity check, not the primary valuation method, because small assumption changes create large value swings.

**Precedent Transaction Pricing**

If a similar company was recently acquired or refinanced, that price is treated as a market comparable. A regional hospital network was bought at 8× EBITDA last year. A fund holds a similar network and values it at 8×, adjusted for differences. This is conceptually tight but data is scarce (few truly comparable transactions).

**Cost Basis Holding Basis**

In early-stage venture or growth equity, the fund may value a holding at the most recent round price. If Series C closed at a $100 million post-money valuation, the fund carries the position at $100 million until the next financing round or exit.

The problem: venture rounds are often inflated by hot market conditions, and subsequent down rounds can force large write-downs. Cost-basis holding can hide deterioration.

**NAV at Cost**

For newly acquired portfolio companies (within 1–2 years of purchase), a fund may carry the position at its entry price ([cost basis](/cost-basis/)) with minimal adjustment. As time passes and the company matures, the GP shifts to a multiple-based or DCF valuation. This transitional approach balances conservatism (no immediate mark-up on acquisition day) with realism (eventually adjusting toward expected exit values).

## The Valuation Committee and Auditor Role

Most private equity and closed-end funds have a **valuation committee**—usually including GP partners, a CFO, and sometimes independent committee members—that meets quarterly to review valuations of illiquid holdings.

The committee reviews:

- Comparables multiples used (are they still current? Have acquirers stopped buying at 6× EBITDA?)
- DCF assumptions (are revenue forecasts realistic in light of recent performance?)
- Changes in holding since last quarter (did operational improvements warrant an uplift? Have competitive threats emerged?)
- Actual exit comps from the fund's own realizations (if the GP sold a similar company at 5.5× EBITDA in Q2, is a Q3 unrealized holding at 6.2× defensible?)

The **external auditor** reviews valuation methodology quarterly or annually, examining:

- Consistency (did the GP value this company at 6× in Q1 and 5.8× in Q2 without explanation?)
- Supportability (are the comparables actually relevant? Can the auditor rerun the DCF and get similar results?)
- Related-party bias (if the company is being advised by a GP-affiliated consultant, did that inflate the valuation?)

A good auditor will flag overly optimistic assumptions or inconsistent application of methods. A passive auditor may wave through inflated valuations if the GP can cite a comparable transaction or analyst report.

## Stale Valuations and Valuation Bias

A subtle but pervasive problem is **valuation staleness**. A fund values a holding at quarter-end, then market conditions deteriorate (a competitor emerges, refinancing rates spike, a key customer is lost), but the holding is not revalued until next quarter. NAV appears artificially high for three months.

The opposite bias occurs when GPs strategically mark down holdings before a secondary sale or fund restructuring, making the opportunity appear cheaper to secondary buyers, then mark them up again afterward. This is fraud if systematic, but subtle mark-down-then-up sequences are hard to detect and police.

Another bias: **optimism from GPs with carry incentives**. A GP's carry is calculated on gains. If a holding can be valued at $100 million or $90 million, the GP has a financial incentive to choose $100 million. Many GPs manage this conflict by using external appraisers for large holdings, but appraisers are chosen and paid by the GP, creating a softer incentive misalignment.

## Worked Example: Private Equity Fund NAV

Consider a $500 million buyout fund (closed-end, 5 years into a 10-year life):

**Assets:**
- Cash and equivalents: $50 million (marked to market)
- Public stock holdings (from partial exits): $80 million (marked to market)
- Company A (acquired Year 2): $200 million (at 6.5× EBITDA, 2019 valuation approach)
- Company B (acquired Year 3): $150 million (DCF, terminal value assumption 4.0× EBITDA)
- Company C (acquired Year 4, still in build-out): $40 million (cost basis, one-year-old)
- Debt position (illiquid credit strategy): $35 million (marked to distressed credit spreads, derived from recent trades)
- **Total Assets: ~$555 million**

**Liabilities:**
- Debt on fund level: $80 million
- Accrued [management fees](/management-fee/) (not yet paid to GP): $8 million
- Estimated carried interest (to be paid if fund hits hurdle on next distributions): $20 million accrual
- **Total Liabilities: $108 million**

**Net Assets: $555 million − $108 million = $447 million**

**Shares Outstanding:** Assume 10,000 limited partner units (shares) outstanding.

**NAV per Share: $447 million ÷ 10,000 = $44,700**

Each LP's $100,000 investment (from original fundraising) is now worth about $110,000 at NAV (1.1× capital deployed), though this is pre-carry distribution and does not yet reflect the GP's stake in gains.

If you change the valuation assumption for Company A from 6.5× to 5.8× EBITDA, NAV per share drops to $42,800—a 4% shift from one assumption. This illustrates why fund valuations, despite their numerical precision, rest on judgment.

## Reconciling NAV and Distributions: Why They Don't Match

Investors sometimes ask: "My NAV is $100,000, but I only received $20,000 in distributions. Where's my money?"

The answer: NAV is the paper value of holdings, not the cash available to distribute. If the fund's private equity holdings are worth $100,000 on paper but the company has not been sold, there is no cash to distribute. Distributions come from exits (realized gains) or from debt proceeds (borrowed cash).

A more sophisticated investor knows that NAV per share, multiplied by their share count, is the LP's **pro rata claim** on fund assets—but that claim is subordinate to the GP's carry, debt holders' claims, and the illiquidity of the underlying assets.

## See also

<div class="wiki-seealso">

### Closely related

- [Management Fee](/management-fee/) — often calculated as % of NAV or AUM
- [Discounted Cash Flow Valuation](/discounted-cash-flow-valuation/) — a core NAV-building method for illiquid holdings
- [Cost Basis](/cost-basis/) — the entry value from which NAV assumptions deviate
- [Management Fee Offset in Private Equity](/management-fee-offset-private-equity/) — affects NAV by adjusting fee accruals
- Carry — NAV must account for estimated carry accruals

### Wider context

- [Private Equity Fund](/private-equity-fund/) — fund structure and NAV reporting cadence
- [Fund-Vintage-Year Performance Comparison](/fund-vintage-year-performance-comparison/) — NAV projections figure into vintage-adjusted returns
- [ETF Premium/Discount](/etf-premium-discount/) — how closed-end ETF prices diverge from NAV
- [Price-to-Book Ratio](/price-to-book-ratio/) — similar valuation concept for public equity
- [Fair Value](/fair-value/) — accounting standard governing NAV reporting in financial statements

</div>
