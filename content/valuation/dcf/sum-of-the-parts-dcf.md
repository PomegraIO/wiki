---
title: "Sum-of-the-Parts DCF"
description: "Valuing a diversified conglomerate by discounting each business segment at its own risk-appropriate WACC, then combining for a total."
keywords:
  - sum of the parts
  - segment valuation
  - conglomerate discount
  - dcf by segment
  - sotp valuation
image: "/svg/valuation.svg"
---

*A conglomerate is not one business—it's several operating at different risk levels and growth rates. **Sum-of-the-Parts** (SOTP) DCF values each segment independently with its own [discount rate](/discount-rate/), then adds them up. This approach often reveals whether the whole is worth more or less than its pieces.*

<div class="wiki-hatnote">

For the related phenomenon of market undervaluation, see [Conglomerate Discount](/conglomerate-discount/).

</div>

## When one WACC isn't enough

A standard DCF assumes all cash flows are discounted at a single company-wide WACC. This works fine for a focused firm: an airline's cash flows, whatever their term structure, carry airline-level risk.

But conglomerates—firms with two or more distinct operating segments—pose a problem. A financial-services holding with a stable bank, a volatile insurance unit, and a private-equity arm shouldn't use the same WACC for all three. The bank's cash flows justify a 6% discount rate; the PE arm's, 10%. Using a blended 8% understates the stable bank's value and overstates the risky fund's.

SOTP solves this by disaggregating. You build a separate DCF for each segment, assign it a segment-specific [cost of capital](/cost-of-equity/), discount its cash flows, and sum the resulting equity values. The result is often a more accurate enterprise value than a single monolithic model.

## The mechanics: segment-by-segment valuation

The process is straightforward but data-intensive.

First, extract (or estimate) each segment's [free cash flow](/free-cash-flow/). This requires reading the company's [10-K](/10-k/) and breaking down [operating income](/operating-margin/), capital expenditures, [working capital](/cash-conversion-cycle/) changes, and [taxes](/corporate-income-tax/) by segment. Many large firms disclose segment revenue and operating profit; calculating cash flows requires some inference.

Second, calculate a segment-specific WACC. This step is critical. You can't use the parent company's [debt-to-equity ratio](/debt-to-equity-ratio/) for each piece; instead, estimate what each segment's capital structure would be if it were standalone. A utility's segment WACC might be 5.5% (low leverage, stable cash); a growth software unit's, 8.5%.

Many analysts use [beta](/beta/) to calibrate the difference. A cyclical segment has higher [systematic risk](/market-risk/) and thus a higher cost of equity. A defensible, low-growth segment has lower beta and a lower required return.

Third, apply a terminal value assumption to each segment. Some segments (mature, low-growth) use a 2–3% perpetual growth rate; others (expansion-stage) might use 4–5%. Each segment's terminal value is then calculated and discounted separately.

Finally, sum the present values:

**Total Equity Value = PV(Segment A) + PV(Segment B) + ... − Net Debt**

## An illustrative case

Suppose a conglomerate has two divisions:

- **Division A (Insurance):** generates $100M free cash flow, $50M invested capital, faces 8% WACC.
- **Division B (Asset Management):** generates $50M free cash flow, $20M invested capital, faces 10% WACC.

Using a blended company WACC of 9%, you'd discount all cash as if they carry the same risk—wrong.

Under SOTP:

- Division A (8% WACC, 3% terminal growth): FCF discounted at 8%, terminal value calculated at 8%. Result: $1.25B equity value.
- Division B (10% WACC, 4% terminal growth): FCF discounted at 10%, terminal value calculated at 10%. Result: $550M equity value.
- **Total: $1.8B.**

If you'd used a 9% WACC for both, Division A would be undervalued (too-high discount rate suppresses its stable cash) and Division B might be overvalued (too-low discount rate inflates growth prospects). The SOTP method captures the actual risk profile of each.

## Estimating segment WACCs

The challenge in SOTP is assigning credible WACCs to divisions that aren't standalone entities and don't trade separately.

One approach: compare pure-play competitors. If the conglomerate's insurance arm resembles large independent insurers (which have WACC of 6–7%), use that. If the asset-management segment is closest to specialized fund managers (WACC of 8–9%), use that range.

A second approach: model the [leverage ratio](/leverage-ratio-forex/) and [cost of debt](/cost-of-debt/) each segment would carry if independent. A stable utility segment might support 40% leverage; a growth segment, 20%. Apply the parent's credit spread (or a typical spread for that segment type) to calculate cost of debt. Then solve for cost of equity using the WACC formula.

A third approach: sensitivity-test the valuation across a reasonable WACC range for each segment. If the total value is robust even when you shift segment WACCs by ±50 basis points, your answer is credible. If total value swings wildly, the SOTP answer is fragile and should be used with caution.

## When SOTP reveals a discount or premium

Comparing SOTP value to the company's market price often reveals market mispricing.

If SOTP value is 20% higher than market cap, the market is applying a [conglomerate discount](/conglomerate-discount/)—a penalty for holding disparate businesses. This can persist due to agency costs (managers of conglomerates often underinvest in high-return segments and overfund low-return ones) or because the market struggles to analyze multiple segments. A value investor might see a buy opportunity.

Conversely, if SOTP value is 10% *lower* than market cap, the market is pricing in future synergies, [spinoff](/spinoff/) value, or management improvements you haven't modeled. A spinoff—separating segments into standalone companies—sometimes creates value by unlocking segment-specific capital structures and investor focus.

## Pitfalls and limitations

SOTP's greatest weakness is that it requires estimates—segment cash flows, appropriate WACCs, terminal growth rates—for multiple divisions. Errors compound. A 0.5% WACC misestimate across four segments can swing total value by 5–10%.

It also ignores genuine synergies if the segments benefit from being together: shared overhead, cross-selling, consolidated bargaining power. If separating divisions would destroy economics, SOTP can overstate standalone values.

Finally, SOTP can be abused. Cherry-picking the highest plausible WACC for undervalued segments and the lowest for priced-in segments biases the total upward. A disciplined analysis uses comparable companies or market data to anchor WACC assumptions, not analyst preferences.

## When SOTP is essential

SOTP is most valuable for:

- **Holding companies** with distinct funds, subsidiaries, or divisions (Berkshire Hathaway, 3M, Alphabet).
- **Firms with announced spinoffs or divestitures**, where segment values must be isolated for deal modeling.
- **Analysts comparing conglomerate value to peer groups**, since pure-play comparables don't exist.
- **Private equity or strategic buyers** evaluating specific segments of a larger company.

It's less critical for focused firms or [ETFs](/etf/) holding pre-screened, homogeneous assets. But for any complex corporate structure with multiple operating environments, SOTP forces the hard questions: What is each piece worth? At what risk? And is the whole greater than the sum?

## See also

<div class="wiki-seealso">

### Closely related

- Discounted Cash Flow Valuation — the base methodology applied per segment
- [WACC](/cost-of-equity/) — segment-specific cost of capital is the core lever
- [Free Cash Flow](/free-cash-flow/) — what's being discounted in each segment
- [Return on Invested Capital in DCF](/return-on-invested-capital-dcf/) — segment ROIC reveals relative quality
- [Cost of Equity](/cost-of-equity/) — the equity risk component of segment WACC

### Wider context

- [Conglomerate Discount](/conglomerate-discount/) — the market penalty SOTP often benchmarks against
- [Acquisition](/acquisition/) — segment separation and valuation in M&A
- [Spinoff](/spinoff/) — the corporate action SOTP analysis often supports
- [Segment Reporting](/segment-reporting/) — the financial disclosures SOTP relies on

</div>
