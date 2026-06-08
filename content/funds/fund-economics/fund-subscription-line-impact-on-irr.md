---
title: "How Subscription Credit Lines Inflate Fund IRR"
description: "A subscription line of credit lets fund managers draw borrowed cash before capital calls are funded. This delays cash outflows, artificially inflating IRR even though it increases leverage and risk. Understand the mechanical advantage and its limits."
keywords:
  - subscription line of credit irr
  - subscription line impact on irr
  - fund leverage borrowed capital
  - internal rate of return
  - credit facility fund mechanics
image: /svg/funds.svg
---

*A **subscription line of credit** (or subscription facility) is a short-term loan a fund borrows against its committed but uncalled capital. Instead of waiting for limited partners to fund a capital call, the manager draws cash immediately, invests it, and repays the line when LP capital arrives days or weeks later. Because money invested early compounds longer before being repaid, the fund's reported internal rate of return climbs—even though the underlying investments haven't changed. This artificial IRR boost is pure mechanics: borrowed capital invested early, then debt service reducing final distributions.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Subscription Line of Credit Impact — Key Points</div>

<img src="/svg/funds.svg" alt="An abstract editorial mark for funds." />

<div class="wiki-infobox-caption">A short-term bridge loan that delays LP capital calls—and accelerates IRR math.</div>

|   |   |
|---|---|
| **Who borrows** | The fund manager on behalf of the fund |
| **Against what** | Limited partners' committed but not-yet-called capital |
| **Typical tenor** | 30–90 days (matches the capital call lifecycle) |
| **IRR effect** | Inflates IRR by 50–200 bps (sometimes more) |
| **Actual return change** | Zero; timing arbitrage, not performance improvement |
| **Cost to fund** | Spreads over SOFR, often 100–200 bps annually |
| **Who benefits** | Manager (higher reported IRR); LPs (net of fees, typically not) |

</aside>

## The Mechanics of the IRR Advantage

An IRR is the discount rate that makes all cash flows equal zero in present value. It reflects *when* money moves in and out, not just the total gain.

A simplified example: suppose a fund has called $100 million from LPs, invested it, and expects to distribute $120 million in one year. The IRR is 20%.

Now add a subscription line. The same fund hasn't called the full $100 million yet—say only $50 million is committed. The manager borrows $50 million on a subscription line at 2% (50 bps + 150 bps spread), invests the full $100 million immediately, and repays the $50 million line as soon as the LP capital call is funded (30–60 days later).

**Timeline with subscription line:**
- Day 1: Borrow $50 million, invest $100 million.
- Day 45: LP calls $50 million, repay the line, pay interest (~$0.4 million for 45 days).
- Year 1: Distribute $120 million.

The fund invested an extra $50 million for 45 days; this extra capital earned roughly $0.6 million gross (45/365 × 2.5% return on $50 million). Net interest cost was ~$0.4 million. The fund realized an extra ~$0.2 million gain, lifting the IRR from 20% to 20.15%.

This seems modest in isolation, but in large funds and longer windows, the compounding effect is material. A $5 billion fund with staggered capital calls over 18 months might boost IRR by 50–150 basis points simply by borrowing against committed capital.

## Why This Inflates IRR Without Improving Performance

The subscription line doesn't improve the *quality* of investments. It simply accelerates the timing of capital deployment. Here's why the IRR math inflates artificially:

IRR weighs early cash outflows more heavily. Borrowing delays the timing of LP capital calls (moving them backward in time from the fund's perspective). This makes the fund's net cash outflow appear smaller early on. Since IRR penalizes early outflows, a smaller early outflow raises the discount rate that zeros the NPV.

**In concrete terms:** If a fund realizes a $10 million profit on a $100 million investment, the IRR return is fixed at 10%. But if you delay the outflow of $50 million from day 1 to day 45, you've reduced the fund's early cash consumption. The same $10 million profit now credits against a smaller average outstanding balance, mathematically boosting the IRR.

The subscription line's interest cost offsets part of this advantage, but rarely all of it. In rising markets, the extra cash deployed via the line often earns more than the 2–3% cost.

## How Large Is the Distortion?

The IRR boost depends on three factors: the **proportion of capital borrowed**, the **tenor of the loan**, and the **expected return on invested capital**.

A rule of thumb: a subscription line covering 30% of fund commitments, drawn for 60 days, with a 2% annual cost and 10% annual investment return, typically adds 30–80 bps to IRR.

Larger distortions occur when:
- The loan covers most of the fund's capital (60–80%).
- The tenor is long (90+ days).
- The investment return is high (15%+) relative to the loan cost (2–3%).

In a $5 billion leveraged buyout fund with staggered capital calls and a 12-month deployment period, subscription lines have been known to boost IRR by 100–200 bps. Institutional investors have grown wise to this and often adjust for the effect when comparing fund IRRs.

## The Cost Structure

Subscription lines are not free. A fund typically pays:

- **Pricing**: SOFR (or sometimes LIBOR) plus 100–200 basis points, depending on credit quality and market conditions.
- **Commitment fee**: 25–50 bps on the undrawn portion (if structured as a revolving line).
- **Administrative fees**: Several thousand dollars per drawdown.

For a fund borrowing $100 million at SOFR + 150 bps for an average of 50 days:
- Interest cost: ~100 mm × (2.5% + 1.5%) × (50/365) = ~$0.55 million.

The line is attractive because the cost (55 bps annualized on a single drawdown) is far below the typical fund return (8–15%), so the arbitrage is real, even if modest.

## Lender Perspective and Risk

Banks and specialty finance firms offer subscription lines because they are low-risk. The debt is backed by committed capital from institutional LPs (endowments, pension funds, insurance companies); these are among the safest obligors in credit markets.

During the 2008 financial crisis and again in 2020 (COVID shock), some subscription lines were reduced or cancelled, illustrating that the "safety" is conditional on continued LP funding. If a recession triggers LP defaults on their commitments, the subscription line could default too. This tail risk is usually priced into the spread.

Banks also retain the right to call the line if the fund underperforms or LPs defect, adding another layer of structural protection.

## Why LPs May Not Benefit (or Lose)

Limited partners who committed capital are charged management fees regardless of when their capital is actually called. A subscription line accelerates deployment but does not reduce fees.

**Scenario:** An LP commits $10 million. The fund borrows $10 million on a subscription line at 2%, invests it, and waits 60 days for the LP's capital call. During those 60 days, the borrowed capital earns, say, 0.5% ($50,000). The subscription line costs ~$33,000. The LP gets the net $17,000 benefit, but they *also* pay their pro-rata share of management fees on the full $10 million, even though their actual capital was only deployed for 60 days of the fund's life.

In many cases, the fee drag outweighs the IRR benefit, and LPs end up slightly worse off. This is one reason institutional investors scrutinize subscription line usage carefully—it can mask mediocre underlying returns.

## Regulatory and Disclosure Issues

The SEC and leading proxy advisors (e.g., the Institutional Limited Partners Association, ILPA) have flagged subscription line inflation as a transparency issue. Some fund managers now disclose "IRR net of subscription line costs" or "IRR absent subscription line assumptions," but this is not yet standard practice.

Sophisticated LPs often request a "vintage-adjusted IRR" calculation from their managers, which removes the timing arbitrage and shows true investment performance. Subscriptions lines, in this view, are cosmetics, not substance.

## See also

<div class="wiki-seealso">

### Closely related

- Internal rate of return — the metric that subscription lines mechanically boost
- [Capital call](/capital-call/) — when LPs deploy their committed capital
- [Management fee](/management-fee/) — charged on committed capital, not just deployed capital
- [Leveraged buyout](/leveraged-buyout/) — the most common user of subscription lines
- [Private equity fund](/private-equity-fund/) — fund structure and LP relationships
- [Debt financing](/debt-financing/) — borrowing mechanics and cost of capital

### Wider context

- [Return on invested capital](/return-on-invested-capital/) — the true measure of investment quality
- [Interest rate](/interest-rate/) — SOFR and LIBOR pricing
- [Counterparty risk](/counterparty-risk/) — lender risk in a credit squeeze
- [Due diligence](/due-diligence/) — why LPs should examine subscription line mechanics

</div>
