---
title: "Carried Interest Calculation Explained with an Example"
description: "Numeric walkthrough of how private equity funds calculate carried interest after hurdle rate and high-water mark gatekeeping."
keywords:
  - carried interest calculation
  - how is carried interest calculated
  - hurdle rate carried interest
  - high water mark
  - private equity compensation
---

*Computing **carried interest** in a [private equity fund](/private-equity-fund/) is not a single multiplication. It's a multi-step gatekeeping process: only gains above the hurdle rate, and only once the high-water mark is re-achieved, trigger the incentive fee. Walking through a concrete example clarifies how the mechanics work in practice.*

## The basic framework

Carried interest (or "carry") is the manager's share of investment profits. In a typical private equity fund, the general partner (GP) earns a [management fee](/management-fee/) (say, 2% of assets annually) plus carried interest on profits above a hurdle rate.

The structure is:
- **Hurdle rate:** The minimum annual return (often 6–8%) that limited partners (LPs) must earn before the GP shares in profits.
- **High-water mark:** A safeguard preventing the GP from earning carry on the same dollar of profit twice if the fund has suffered a loss.
- **Carry percentage:** Typically 20% of profits above the hurdle, though this varies from 15% to 30%.

## Example: A three-year fund

Consider a $100 million private equity fund with:
- Hurdle rate: 8% annually
- Carry: 20% of profits above the hurdle
- High-water mark: Applies
- Management fee: 2% annually ($2M), deducted from capital

**Year 1: Deployment and modest return**

The GP deploys $95 million into portfolio companies (after deducting $2M in Year 1 management fees from the $100M capital). By year-end, the portfolio is valued at $103 million.

Net gain: $103M − $95M = $8M

Hurdle calculation:
- LP hurdle on their deployed capital: $95M × 8% = $7.6M
- Actual gain: $8M
- Profit above hurdle: $8M − $7.6M = $0.4M
- GP carry (20% of $0.4M): $0.08M (or $80,000)

The high-water mark is now set at $103M. The fund has paid out carry once.

**Year 2: Growth and larger carry**

The portfolio compounds; valuations rise to $115 million by year-end. A fresh $2M management fee is deducted.

Net gain from Year 1 ending value: $115M − $103M = $12M

Hurdle calculation (on the Year 1 ending NAV):
- LP hurdle on $103M: $103M × 8% = $8.24M
- Actual gain: $12M
- Profit above hurdle: $12M − $8.24M = $3.76M
- GP carry (20% of $3.76M): $0.752M

Total carry earned: $80,000 + $752,000 = $832,000 so far.

The high-water mark ticks up to $115M.

**Year 3: Market downturn and the high-water mark at work**

The portfolio suffers losses; NAV falls to $110M by year-end. Another $2M management fee is deducted. The GP still collects the management fee—it's a hard expense—but carry is at risk.

Hurdle calculation (on the Year 2 ending NAV):
- LP hurdle on $115M: $115M × 8% = $9.2M
- Actual change: $110M − $115M = −$5M (a loss)
- The hurdle has *not* been met. The portfolio is underwater relative to the required return.
- **Carry earned in Year 3: $0**

Critically, the high-water mark is not reset to $110M. It remains at $115M. The GP cannot earn carry on profits until the portfolio climbs back above $115M. This is the high-water mark in action: the GP doesn't get to "reset" and earn carry on the same ground twice.

**Year 4: Recovery**

Assume the portfolio recovers to $118M. The high-water mark was $115M.

Net gain: $118M − $115M = $3M

Hurdle calculation:
- LP hurdle on $115M: $115M × 8% = $9.2M
- Actual gain above the high-water mark: $3M

Here's the critical twist: the GP *also* owes the LP the full hurdle rate. Since the portfolio fell in Year 3 and didn't pay the hurdle then, Year 4 must "catch up" on that deferred hurdle.

The $3M gain is allocated first to the LP hurdle shortfall. Since the hurdle on $115M was $9.2M (not earned in Year 3), the Year 4 carry is again *zero*—the LP is recouping the deferred hurdle from the new gains.

Carry resumes only once the cumulative gain covers the full hurdle rate across all years. If the portfolio hits $125M (a $10M gain on the $115M HWM), the LP gets the full $9.2M hurdle, and the remaining $0.8M is profit above hurdle, entitling the GP to 20% × $0.8M = $0.16M in carry.

## High-water mark illustrated

The high-water mark is not a percentage target; it's a dollar level. Once reached, it acts as a floor for carry calculations. The GP is paid on *incremental* gains above that mark, after honoring the hurdle rate on any cumulative shortfalls.

This is why downturns are painful for GPs: they must earn their way back to the prior peak before carry flows resume. A fund that peaks at $120M, then falls to $100M, must climb back above $120M before carry is earned again—and the LP is owed the full hurdle rate on the entire period.

## Hurdle rate variations

Some funds use a **preferred return** instead, which is slightly different: LPs earn a cumulative threshold (e.g., 7% annually compounded) before carry is available. Once that preferred return is cleared cumulatively, all remaining profits are split (80% LP, 20% GP) until the end of the fund.

Other funds use a **catch-up provision**: once the hurdle is cleared, the GP is paid its 20% on *all* remaining profits, including the share that would have gone to LPs, until the GP has "caught up" to its pro rata share of the total gain. For example, if the GP was entitled to 20% of all profit, and LPs earned the hurdle first, the GP gets 100% of the next profits until the GP's total equals 20% of the total gain.

## Clawback provisions

A related safeguard: if the fund underperforms at exit, the GP may owe money back to the LP. If the fund was paid $2M in carry in Years 1–3, but the fund ends with only 1% returns to LPs (below the hurdle), the GP might clawback portions of earlier distributions. This protects LPs from being over-compensated during the fund.

## Practical implications

- **Fund timing:** A GP wants to recognize gains and reset the high-water mark in good years; carry is deferred or lost in bad years. Fund distributions and realizations are strategically timed.
- **LP alignment:** The hurdle rate and high-water mark align GP and LP interests—the GP doesn't profit until the LP has earned a baseline return and isn't rewarded for re-earning the same dollar.
- **Transparency:** LPs audit carry calculations carefully because they determine the value of the LP's stake. Disputes over hurdle calculations and high-water mark timing have led to legal battles.

## See also

<div class="wiki-seealso">

### Closely related

- [Private Equity Fund](/private-equity-fund/) — organizational structure and profit-sharing
- [Management Fee](/management-fee/) — annual fee distinct from carry
- [Hurdle Rate](/hurdle-rate/) — minimum return threshold in carry calculations
- [Performance Fee](/performance-fee/) — broader category of profit-sharing fees
- Limited Partnership — the legal structure of fund relationships

### Wider context

- [Leveraged Buyout](/leveraged-buyout/) — typical private equity strategy
- [Return on Invested Capital](/return-on-invested-capital/) — how fund returns are measured
- Fundraising — how PE managers secure LP capital
- General Partner — the active manager earning carry

</div>