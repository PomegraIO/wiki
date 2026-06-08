---
title: "Overcollateralization Test"
description: "Coverage ratio in CLOs and CDOs that, when breached, redirects cash from junior tranches to repay senior notes faster."
keywords:
  - structured credit
  - clo
  - cdo
  - cash diversion
  - senior tranche protection
image: "/svg/fixed-income.svg"
---

*The **overcollateralization test** (or OC test) is a numerical trigger in collateralised loan obligations and collateralised debt obligations that measures whether the aggregate value of a fund's collateral pool exceeds a threshold relative to its outstanding senior liabilities. If that ratio breaches below the required level, cash that would normally flow to junior noteholders is instead diverted to repay senior notes faster—a mechanical safeguard that protects senior investors when the portfolio begins to deteriorate.*

<div class="wiki-hatnote">

For the comparable measure on [interest income](/interest-rate/), see [Interest Coverage Test](/interest-coverage-test/).

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Overcollateralization Test — key facts</div>

<img src="/svg/fixed-income.svg" alt="An abstract editorial mark for fixed income and structured products." />

<div class="wiki-infobox-caption">A waterfall pivot triggered by asset-value erosion, not interest shortfalls.</div>

|   |   |
|---|---|
| **What it is** | Ratio of collateral value to senior liabilities |
| **Also called** | OC test, OC ratio, asset coverage test |
| **Typical trigger level** | 100–110% (varies by deal) |
| **Breach consequence** | Cash redirect: [equity distributions](/dividend/) stop; [senior bond](/corporate-bond/) repayment accelerates |
| **Covers** | [Par value](/par-value/) of loans held, market prices, and write-downs |
| **When tested** | Monthly or quarterly, after [valuation](/fair-value/) resets |
| **Who monitors** | [Trustee](/), [collateral manager](/collateral-manager/) |

</aside>

## Why structured deals need an asset-value floor

When a CLO issues four or five tranches of notes—senior, mezzanine, subordinated, equity—the waterfall assumes a steady stream of interest and principal from the underlying loan portfolio. Senior noteholders bear the least risk: they get paid first, in full, before anyone else touches the cash. Subordinated and [equity investors](/equity-financing/) accept the reverse deal: they get paid last and absorb losses first.

The OC test exists because loans default, ratings slip, and [credit spreads](/credit-spread/) widen. A CLO's collateral doesn't remain static; some borrowers weaken, a few blow up entirely, and the portfolio's total value can drift downward. The OC test asks a simple question every period: "Is the collateral pool still thick enough to cover all the senior debt?" If not, junior tranches lose their distributions, and all cash goes to shore up the seniors instead.

This is a purely mechanical, **balance-sheet** test. It ignores whether interest is being paid on time; that is the job of the [interest coverage test](/interest-coverage-test/). The OC test only cares about the fundamental solvency of the asset pile.

## The trigger threshold and its algebra

An OC test is usually expressed as a ratio. A typical formula:

$$\text{OC Ratio} = \frac{\text{Aggregate Par Value of Collateral}}{\text{Outstanding Principal of Senior Notes}}$$

If the deal's legal documents specify "OC test of 105%," then the collateral must always be worth at least 105 cents on the dollar of senior debt. Most deals set the bar between 100% and 110%; the exact level depends on expected default rates, recovery rates, and the [credit rating](/credit-rating/) of the senior class.

Because the test uses **par value** of the underlying loans (not market prices), it moves more slowly than a [mark-to-market](/fair-value/) trigger. A [leveraged buyout](/leveraged-buyout/) loan trading at 90 cents on the dollar still counts at par, as long as no default has occurred. Actual write-downs—principal recovery losses—move the needle. This design stabilises the test and avoids whipsaw from routine [volatility](/volatility-smile/).

## When breach means diversion

The moment the OC ratio falls below the threshold—say, to 104% in a 105% deal—the diversion kicks in immediately. The collateral has shrunk faster than senior debt has been paid down, and the deal has become undercollateralized.

Cash that would have flowed to equity holders (the **bottom tranche**) instead routes to paying off senior principal. Once OC is restored, distributions resume. This mechanic protects senior investors without requiring a vote or a restructuring; it is automatic and contractual.

If the breach persists and collateral continues to erode, the diversion can climb the waterfall: equity stops receiving cash first, then [subordinated noteholders](/junk-bond/) see their distributions curtailed or suspended. In a severe downturn, the entire [cash waterfall](//) may be redirected to pay down senior notes until the OC ratio recovers.

## How collateral managers live with it

For a [collateral manager](/collateral-manager/) running a CLO, the OC test is a constant constraint. If the portfolio begins to slip—defaults rise, ratings migrate downward—the manager faces an unpleasant choice: improve the portfolio (sell weakened credits, buy stronger ones) or accept a cash diversion that penalises the fund's [junior stakeholders](/preferred-stock/).

Many deals allow the collateral manager to make **selective sales and purchases** to keep the OC ratio above water. The manager can sell a performing loan at par and redeploy the proceeds into a higher-quality credit, nudging the ratio upward. This is not free—trades incur costs, and the manager's compensation is often tied to the overall fund performance—but it buys breathing room.

Some deals include a "cure provision": if OC dips below the trigger for a single month, but comes back above it the next month, the diversion may not activate (or activates only partially). Others allow the manager a brief [reinvestment period](/reinvestment-period/) to rebuild the portfolio before any diversion begins. These provisions soften the blow for junior holders while still anchoring the test as a hard-wired safety net.

## Why it matters in practice

The OC test is the CLO equivalent of a [debt-to-equity ratio](/debt-to-equity-ratio/) in a corporate bond indenture. Just as a corporation promises lenders a minimum equity cushion, a CLO promises senior noteholders a minimum collateral cushion. Breach triggers automatic cash flow changes that protect senior investors without requiring anyone to declare an official "default" or restructure the deal.

For equity investors, it is a bitter medicine: when a portfolio softens, equity cash dries up before anything else. For senior noteholders, it is a crucial safety mechanism. And for [collateral managers](/collateral-manager/), it is a **hard compliance floor**—ignore portfolio health and watch the OC test breach, and the fund's economics unravel.

The test is also a permanent reminder that [securitization](/securitization/) works only because subordination works. The junior tranches sit in harm's way so the senior tranches can sleep soundly. When the test breaches, junior investors feel the first chill.

## See also

<div class="wiki-seealso">

### Closely related

- [Interest Coverage Test](/interest-coverage-test/) — cash diversion triggered by shortfall in interest income, not asset value
- [Collateral Manager](/collateral-manager/) — portfolio guardian responsible for keeping the OC ratio above water
- [Reinvestment Period](/reinvestment-period/) — window when manager can rebuild the portfolio before OC breach mechanics activate
- [Securitization](/securitization/) — the broader mechanism that makes subordinated tranches and coverage tests possible
- [Subordinated Tranche](/junk-bond/) — junior noteholders absorb losses first and distributions last
- [Credit Rating](/credit-rating/) — OC thresholds are set based on expected credit losses in the portfolio
- [Cash Waterfall](//) — payment order through the tranches; OC test redirects flows up the priority stack

### Wider context

- Collateralised Loan Obligation — the primary home of OC tests in modern finance
- Collateralised Debt Obligation — similar structures and similar mechanics
- [Bond](/bond/) — the senior tranches that OC tests protect
- [Debt Financing](/debt-financing/) — why CLOs issue tranches and why they need safeguards
- Risk Management — structural protections in securitized deals

</div>
