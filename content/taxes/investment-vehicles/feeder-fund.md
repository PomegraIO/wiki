---
title: "Feeder Fund"
description: "An investment fund that deposits substantially all assets into a single master fund, used for legal, tax, or distribution flexibility."
keywords:
  - feeder fund
  - master feeder structure
  - investment fund
  - fund of funds
---

*A feeder fund is an investment vehicle that invests essentially all of its assets into a single master fund. The feeder collects capital from investors (often domestic or foreign investors with different tax or regulatory status), pools it, and forwards the capital to a master fund that executes the actual investment strategy. This structure is common in [hedge funds](/wiki/hedge-fund/), [private equity](/wiki/private-equity-fund/), and [managed futures](/wiki/hedge-fund-managed-futures/) strategies.*

<aside class="wiki-infobox">

| Component | Role |
|---|---|
| **Feeder Fund** | Collects capital from investors, minimal operations |
| **Master Fund** | Executes actual trades, holds portfolio, makes distributions |
| **Capital Flow** | Feeder → Master (one-way) |
| **Investor Base** | Often segmented (US domestic, foreign, pension plans) |
| **Fee Structure** | Feeder applies investor fees (management + [performance](/wiki/performance-fee/)), passes to master |
| **Tax Treatment** | [Pass-through](/wiki/pass-through-security/) (feeder is typically transparent or [flow-through](/wiki/pass-through-security/)) |
| **Regulatory Benefit** | Allows fund to comply with diverse regulations in single master fund |
| **Cost** | Modest layer of management fees at feeder level |

</aside>

## Why funds use master-feeder structures

The master-feeder structure solves a practical problem: investors with different regulatory, tax, or domicile status cannot always invest in the same fund. A hedge fund manager in the US wants to accept capital from:
- US domestic investors (who can invest in a US LLC)
- Foreign investors (who may prefer to invest through an offshore jurisdiction to avoid PFIC (passive foreign investment company) taxation)
- Pension plans (who have distinct regulatory requirements under ERISA)

Rather than operating three separate funds with three separate portfolios, the manager creates:
- One **master fund** (often an offshore LLC or Cayman Islands fund) holding the actual portfolio
- Multiple **feeders** (one domestic US LLC, one offshore fund, one ERISA-compliant fund) collecting capital from different investor classes

All feeders invest in the master, which simplifies operations: there is only one portfolio, one set of trades, one [prime broker](/wiki/prime-broker/), and one set of operational risks.

## Tax efficiency for foreign investors

The primary tax motivation for master-feeder structures is avoiding PFIC status.

Under US tax law, a "Passive Foreign Investment Company" is a foreign corporation earning >75% of income from passive sources ([dividends](/wiki/dividend/), [interest](/wiki/interest-coverage-ratio/), [capital gains](/wiki/capital-gains-tax/)). US shareholders in PFICs must either:
1. Mark-to-market gains annually (recognizing gains whether or not realized), or
2. Defer gains but pay [ordinary income tax](/wiki/marginal-tax-rate-investor/) rates (not [capital gains](/wiki/capital-gains-tax/) rates) when gains are eventually realized, plus interest penalties.

A foreign [hedge fund](/wiki/hedge-fund/) is almost always a PFIC. If it accepts US investors directly, those investors face harsh PFIC taxation.

Solution: use a master-feeder structure where:
- The **offshore master fund** accepts foreign investors (non-US persons) without PFIC concern.
- A **US domestic feeder** (typically an LLC) accepts US investors. Since the feeder is a US corporation, it is not a PFIC.

The US investors invest in the domestic feeder, which invests all capital in the offshore master. The feeder is transparent for tax purposes (each investor's share of master-fund income is [passed through](/wiki/pass-through-security/)) so the feeder itself pays no tax; the investors pay tax on the actual master-fund income at [capital gains](/wiki/capital-gains-tax/) rates. This is far more efficient than PFIC taxation.

## Operational benefits: single portfolio, multiple fund structures

From an operational standpoint, the master-feeder structure is elegant. The master fund:
- Makes all investment decisions
- Holds all securities
- Executes all trades
- Rebalances the portfolio
- Manages [prime broker](/wiki/prime-broker/) relationships
- Handles [capital calls](/wiki/capital-flows/) and distributions

The feeders:
- Market to investors
- Collect subscriptions
- Forward capital to the master
- Report to investors
- Handle compliance for their investor base

This division of labor reduces redundancy. Suppose the manager holds a 100-stock portfolio. If there were three separate funds, the portfolio would be replicated three times (100 stocks × 3 = 300 positions). With a master-feeder, there is one 100-stock portfolio, and all capital benefits from it.

The master fund's [expense ratio](/wiki/expense-ratio/) is "charged through" to the feeders. If the master expenses are 1%, and the feeder adds 0.5%, the investor pays 1.5% all-in. This is more efficient than running three entirely separate funds (each with its own [prime broker](/wiki/prime-broker/), back office, compliance) at 2% each.

## Regulatory and compliance benefits

Different investor classes have different rules:
- **Pension plans** (endowments, pension funds) must comply with ERISA regulations and often require "separately managed accounts" for accounting and governance.
- **Foreign institutional investors** may need to comply with their home-country regulations and often prefer offshore vehicles.
- **Retail / high-net-worth US investors** often prefer onshore structures to avoid foreign tax reporting (FBAR, FATCA).

A single master fund cannot easily satisfy all these constraints. A feeder structure allows the manager to offer compliant vehicles to each investor class while running a single investment strategy.

For example: A pension plan might invest in a US-domiciled feeder fund that is structured as a separate account; the feeder invests all capital in the master fund. The pension plan's accounting and ERISA compliance are satisfied at the feeder level, while the master fund handles the actual investing.

## Fee mechanics and double-fee structures

The feeder structure does introduce an extra layer of fees. The master fund typically charges an [all-in management fee and performance fee](/wiki/hedge-fund-performance-fee/). The feeder then may charge its own (usually smaller) fee.

Example: Master fund charges 1% management + 20% [performance fee](/wiki/performance-fee/). Feeder charges 0.25% management + 5% [performance fee](/wiki/performance-fee/). The investor pays:
- 1.25% management fee (1% master + 0.25% feeder)
- 20% to 25% [performance fee](/wiki/performance-fee/) (depending on how fees are structured)

This is sometimes called "double-fee" or "fee stacking." In the past, some feeder funds were criticized for excessive fees, but competition has normalized fee stacking to a modest premium (0.25-0.5% management, +5-10% on the [performance fee](/wiki/performance-fee/)).

Investors should be aware of fee layering when selecting feeder funds. If feeder fees are excessive (>1% + 10% performance), a [fund-of-funds](/wiki/fund-of-funds/) structure might offer better value.

## Master-feeder in [private equity](/wiki/private-equity-fund/) and [hedge funds](/wiki/hedge-fund/)

The master-feeder structure is ubiquitous in large [hedge funds](/wiki/hedge-fund/) and [private equity](/wiki/private-equity-fund/) firms:
- **Apollo Global Management**, **Blackstone**, and **KKR** operate master-feeder structures for their flagship funds.
- A [private equity](/wiki/private-equity-fund/) master fund closes acquisitions and holds portfolio companies; feeders raise capital from US [pension funds](/wiki/pension-obligation/), foreign [sovereign wealth funds](/wiki/sovereign-risk/), and ultra-high-net-worth individuals.
- [Hedge funds](/wiki/hedge-fund/) use master-feeders to segregate offshore and onshore capital, simplifying compliance and tax reporting.

## Risks and limitations

### Concentration risk

A feeder invests all assets in a single master fund. There is no diversification at the feeder level. If the master fund's manager is incompetent or fraudulent, the feeder's investors have zero recourse. The feeder structure provides no buffer.

(Contrast with a [fund-of-funds](/wiki/fund-of-funds/), which invests in multiple underlying funds and provides diversification.)

### Liquidity constraints

The master fund sets terms (lock-up periods, redemption frequency, etc.). If the master fund has a 1-year lock-up and only allows redemptions quarterly, the feeder's investors are bound by those terms regardless of the feeder's own terms. Feeder-level gates or side pockets can mitigate this, but they add complexity.

### Transparency

A feeder necessarily offers less transparency than a direct investment in the master. Investors see feeder-level reports, and the master fund may be offshore and less forthcoming with details. Some investors object to this opacity.

### Regulatory changes

If a regulator changes rules around feeders (e.g., PFIC rules reform, ERISA rules change), the master-feeder structure may become less advantageous, and the fund may need to restructure.

## Conclusion: a necessary complexity for large funds

Master-feeder structures are not ideal (extra fees, reduced transparency), but they are necessary for large, sophisticated funds serving multiple investor classes. A small hedge fund accepting only US accredited investors can operate as a single fund. A large manager raising capital from US pension plans, foreign institutions, and ultra-high-net-worth individuals across multiple jurisdictions needs a master-feeder structure to comply with tax, regulatory, and operational constraints.

<div class="wiki-seealso">

### Closely related
- [Fund of funds](/wiki/fund-of-funds/) — Alternative structure investing in multiple underlying funds
- [Hedge fund](/wiki/hedge-fund/) — Private investment fund using feeder structures
- [Private equity fund](/wiki/private-equity-fund/) — Uses master-feeder for diverse capital sources
- PFIC — Passive foreign investment company tax status

### Wider context
- Offshore fund — Fund domiciled outside investor's home jurisdiction
- ERISA — US pension and retirement plan rules
- [Pass-through security](/wiki/pass-through-security/) — Tax-transparent vehicles
- [Fund structure](/wiki/fund-family/) — Different vehicle types and organization

</div>
