---
title: "Excess Return DCF Model"
description: "A reformulation of DCF valuation that separates invested capital from the present value of excess returns to isolate value creation."
keywords:
  - excess return
  - dcf model
  - invested capital
  - residual income
  - valuation framework
image: "/svg/valuation.svg"
---

*The standard DCF discounts all [free cash flows](/free-cash-flow/). The **Excess Return** variant isolates the equation differently: value equals today's invested capital plus the present value of future returns earned *above* the [cost of capital](/cost-of-equity/). This mental separation clarifies where value actually comes from.*

## The standard DCF versus the excess return approach

In a traditional DCF model, you forecast cash flows, discount them at WACC, and subtract debt to arrive at equity value. The algebra works. But the Excess Return (or Residual Income) model asks a sharper question: how much value does the firm create beyond simply returning its investors' money?

The formula is:

**Equity Value = Invested Capital + PV of Future Excess Returns**

where Excess Return = (ROIC − WACC) × Invested Capital.

Put plainly: if I put a dollar into a business, I expect it to earn my cost of capital back. Anything *above* that is surplus. The Excess Return model makes that surplus visible in every forecast year.

## Why separate these two components?

The separation serves three purposes.

First, it forces a disciplined assumption about [return on invested capital](/return-on-invested-capital-dcf/). You can't fudge the forecast—if ROIC is 12% and WACC is 8%, the spread is 4%, applied to your projected invested capital. No hiding a weak ROIC behind optimistic cash flow growth.

Second, it clarifies the terminal assumption. In many DCF models, terminal value is a black box—often 60–80% of total value. In Excess Return, you're explicitly assuming: "ROIC converges to WACC, so excess returns fade to zero." This is the economic truth, and seeing it written out prevents lazy perpetual-growth assumptions.

Third, it separates the "base" value (what you paid in) from the "created" value (what you earned). A company with high invested capital but mediocre ROIC might have high absolute value simply because it's large, but it's destroying returns relative to its cost of capital. The excess return component catches this.

## Building the excess return forecast

The mechanics are simple but require discipline.

For each forecast year, calculate:

**Excess Return = (ROIC − WACC) × Invested Capital**

Then discount these excess returns at WACC back to present value. Add the result to today's invested capital.

The key assumption is ROIC. In years 1–5, you might forecast it declining from 14% toward the long-run steady state (often 10–11%, the economy-wide average for mature firms). WACC stays constant at, say, 8%. So year 1 excess return is (14% − 8%) = 6% spread; year 5 is (11% − 8%) = 3% spread. After year 5, assume ROIC = WACC, so excess returns disappear, and terminal value is zero.

Why this conservative move? Because competition erodes above-normal returns. Firms earning 14% ROIC attract rivals; some of that spread eventually compresses. By assuming convergence to WACC in the terminal period, you're saying "I don't believe in perpetual competitive advantage" unless your company has genuinely defensible moats.

## Invested capital: the foundation

Invested Capital isn't just accounting equity. It's:

**Invested Capital = Shareholders' Equity + Net Debt**

Or equivalently:

**Invested Capital = [Total Assets](/balance-sheet/) − [Current Liabilities](/accounts-payable/)**

This is the total capital *employed* in the business. In the excess return model, you forecast its growth alongside ROIC. If invested capital grows 5% per year and ROIC is steady at 12%, you're reinvesting earnings to fund that growth. The model captures the compounding explicitly.

## Terminal value revisited

Here's where Excess Return shines. In a traditional DCF, terminal value is:

**TV = Year 5 FCF × (1 + g) / (WACC − g)**

where *g* is a perpetual growth rate. That number is sensitive to small changes in *g*—and *g* is often guessed.

In an Excess Return model, terminal value is much simpler:

**TV = Invested Capital in Year 5 × (ROIC − WACC) / WACC**

But if you assume ROIC converges to WACC in the terminal period, this becomes **zero**. Value beyond the explicit forecast period comes *only* from the excess returns already captured in years 1–5.

This is more realistic. It says: I'm going to value the firm on excess returns I can articulate. Once those excess returns fade (because of competition, maturity, or saturation), there's no terminal surplus. The firm then earns its cost of capital and no more.

## Comparing it to alternatives

A traditional DCF and an Excess Return model, built on the same ROIC, growth, and discount-rate assumptions, should arrive at the same answer. The math is equivalent—just rearranged. But the mental clarity differs.

If you're comparing two companies, Excess Return makes the comparison sharper. Company A: $50M invested capital, 15% ROIC, 8% WACC. Company B: $200M invested capital, 10% ROIC, 8% WACC. Company A's excess return rate is 7%; Company B's is 2%. If invested capital is similar, Company A is the value creator.

The formula also aligns naturally with [valuation](/relative-valuation/) concepts like [price-to-book](/price-to-book-ratio/). A P/B of 2.5× means the market is willing to pay $2.50 for every dollar of invested capital, implying it expects future excess returns to be worth $1.50 in present value. Excess Return models often forecast whether that premium is justified.

## When to use it

Excess Return shines for mature companies with stable, predictable [return on invested capital](/return-on-invested-capital-dcf/). Banks, insurance, utilities, and consumer staples are natural fits—their ROIC is usually stable, capital requirements are clear, and competitive advantage is long-lived or well-defined.

It's less useful for early-stage, high-growth firms where ROIC is volatile and future capital needs are uncertain. In those cases, you fall back to traditional FCF discounting, which is more flexible.

For any large [acquisition](/acquisition/) or [merger](/merger/) analysis, the Excess Return lens is invaluable: it forces you to articulate exactly what ROIC uplift you're paying for, and over how long a period that premium persists.

## See also

<div class="wiki-seealso">

### Closely related

- Discounted Cash Flow Valuation — the standard framework from which Excess Return is derived
- [Return on Invested Capital in DCF](/return-on-invested-capital-dcf/) — the ROIC assumption that drives excess returns
- [WACC](/cost-of-equity/) — the cost of capital that excess returns are measured against
- [Free Cash Flow](/free-cash-flow/) — the traditional cash-based alternative input to DCF
- [Price-to-Book Ratio](/price-to-book-ratio/) — market value relative to invested capital

### Wider context

- Valuation — the broader discipline
- Competitive Advantage — the source of sustainable excess returns
- Terminal Value — the anchor assumption in excess return models
- [Cost of Equity](/cost-of-equity/) — the equity portion of WACC

</div>
