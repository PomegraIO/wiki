---
title: "Interest Rate Risk in the Banking Book (IRRBB)"
description: "How regulators measure interest rate risk in the banking book (IRRBB) under Basel standards, tracking bank sensitivity to rate shifts and economic value impact."
keywords:
  - interest rate risk in the banking book
  - irrbb basel framework
  - banking book interest rate exposure
  - regulatory rate risk measurement
  - net interest income sensitivity
---

*The **interest rate risk in the banking book** (IRRBB) is how regulators measure the danger that shifts in market rates will erode a bank's net interest income or wipe value off its balance sheet. Basel standards now require banks to disclose and manage this risk explicitly, using two metrics: one tracking how rate changes ripple through current and near-term earnings, the other capturing the full economic impact on shareholder equity.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">IRRBB — key facts</div>

<img src="/svg/risk.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Regulators measure banking book rate risk via earnings and economic-value exposure.</div>

|   |   |
|---|---|
| **What it is** | The sensitivity of a bank's net interest income and equity value to interest rate movements |
| **Measured by** | Change in net interest income (earnings approach) and change in economic value of equity (EVE approach) |
| **Basel standard** | BCBS 368 (2015); refined in BCBS 375 (2016) |
| **Key scenarios** | Parallel shifts, slope changes, curvature shifts in yield curve; also bank-specific rate shocks |
| **Supervisory outlier** | ~200 basis points for EVE, relative to capital |
| **Unlike trading book** | Not marked-to-market daily; not subject to [value-at-risk](/value-at-risk/) models; longer measurement horizon |

</aside>

## Why banks care about rate risk

A bank's core business is financial intermediation: borrowing short-term (deposits, wholesale funding) and lending long-term (mortgages, term loans). When [interest rates](/interest-rate/) are stable, the spread between the rate the bank pays and the rate it earns stays predictable. But rates move, and a bank that funds 30-year mortgages with short-term deposits faces a real problem if rates rise sharply: the bank pays higher rates on rolled-over deposits while earning the same fixed rate on its mortgages.

This mismatch lives in the banking book—the portfolio of loans, deposits, and securities a bank holds for the long term, as opposed to the trading book where it marks positions to market daily. Because banking-book positions are rarely traded, the risk sits hidden until earnings drop or asset values decay. **Interest rate risk in the banking book** is the name regulators give to this latent exposure.

## The two measurement lenses

Regulators ask banks to quantify IRRBB using two different lenses, each designed to catch a different kind of danger.

**The earnings approach** measures how a rate shock hits net interest income—the bank's annual profit from lending and borrowing spreads. If rates jump 200 basis points, some loans reprice upward while deposits must be offered at higher rates to retain customers. The net effect could be positive (more loans reprice than deposits) or negative (deposits reprice faster). A bank with a [duration](/duration/) mismatch can lose millions in a rising-rate scenario.

**The economic value of equity (EVE) approach** ignores near-term earnings and instead recalculates the present value of all future cash flows on banking-book assets and liabilities using the new rate curve. A rise in rates reduces the present value of fixed-rate assets and liabilities proportionally, but if the bank has more or longer-duration assets than liabilities, EVE shrinks—hitting tangible shareholders' equity. This approach reveals longer-term solvency risk that the earnings view might mask.

Both matter. A bank might maintain net interest income in the short term but lose enormous economic value in the long run.

## Basel supervisory standards

Under [Basel standards](/capital-asset-pricing-model/), the Basel Committee on Banking Supervision (BCBS) sets a supervisory outlier test. A bank is flagged as an outlier—and subject to tighter capital requirements and supervision—if its IRRBB exposure exceeds roughly:

- **Economic value of equity loss:** 200 basis points or more of the bank's [Tier 1 capital](/tier-1-capital/), under a 200 basis point parallel shift in rates

This threshold is intentionally conservative. Most banks in stable market conditions sit well below it. But in a crisis—a sharp, sudden rate shock like the 2022 Fed tightening cycle—banks that built up excess duration exposure in low-rate years can spike above the threshold.

## Rate scenarios and shocks

Regulators don't just test a single rate move. They run multiple scenarios to catch banks that are hedged for parallel shifts but exposed to curve bending or twists.

- **Parallel shift:** All rates move up or down by 200 bps or more (the supervisory standard shock).
- **Slope change:** Short rates move differently from long rates (e.g., short rates up 100 bps, long rates up 50 bps), which pressures banks with steep maturity mismatches.
- **Curvature:** The yield curve bends (the long end flattens while short and long ends steepen), which hits banks with concentrated duration exposure at specific tenors.
- **Bank-specific shocks:** [Spread risk](/basis-risk/) if deposits behave differently than modeled, or [basis risk](/basis-risk/) if floating-rate loans don't reprice exactly when the benchmark moves.

## Earnings vs. economic value trade-offs

A bank can reduce near-term earnings risk (through [interest-rate swaps](/interest-rate-swap/) and repricing management) yet still face large EVE risk if its balance sheet is heavily duration-mismatched. Conversely, a bank can accept short-term earnings volatility to earn a steep spread—betting that rates will stabilize before the cost of funds climbs too high.

This tension is why both metrics exist. Regulators want to prevent both a bank from quietly running down net interest income (a slow-motion death) and from blowing up overnight (a sudden EVE collapse). The earnings view catches the first; the EVE view catches the second.

## IRRBB and capital requirements

Under BCBS 375 and refined in later guidance, banks flagged as IRRBB outliers may face add-on [capital requirements](/capital-adequacy/) or restrictions on dividend payouts and executive compensation. The idea is to force a buffer: if you're running outsize rate risk, you must hold more equity capital to absorb the loss.

This is especially relevant for smaller regional banks, which often have outsized IRRBB exposure due to less sophisticated hedging and a higher proportion of fixed-rate mortgages funded by stable deposits. The 2023 U.S. regional bank stress illustrated the real-world stakes: banks that had loaded up on cheap long-term bonds and deposits during 2020–2021 faced massive unrealized losses when the Fed raised rates rapidly.

## See also

<div class="wiki-seealso">

### Closely related

- [Interest rate](/interest-rate/) — the percentage cost of borrowing or return on lending
- [Duration](/duration/) — how sensitive a bond or loan's value is to rate changes
- [Interest-rate risk](/interest-rate-risk/) — general concept of losses from rate movements
- [Basis risk](/basis-risk/) — when a hedge doesn't move perfectly in line with the position being hedged
- [Net interest income](/net-operating-income/) — the bank's core profit from lending and borrowing spread
- [Tier 1 capital](/tier-1-capital/) — the highest-quality regulatory capital buffers
- [Capital adequacy](/capital-adequacy/) — regulators' requirements for bank capital ratios

### Wider context

- [Federal Reserve](/federal-reserve/) — the central bank that sets U.S. interest rate policy
- [Credit cycle](/credit-cycle/) — the boom-and-bust pattern of lending and rates
- [Market risk](/market-risk/) — broader category of losses from market price changes
- [Basel standards](/capital-asset-pricing-model/) — the international regulatory framework for bank capital

</div>
