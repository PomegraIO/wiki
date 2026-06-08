---
title: "How to Value a Startup Equity Offer"
description: "Value a startup equity offer by estimating ownership percentage, dilution risk, and potential exit scenarios. Learn the framework for private equity appraisal."
keywords:
  - how to value startup equity offer
  - startup equity valuation method
  - option pool dilution equity
  - private company ownership percentage
  - startup equity expected value
image: "/svg/equity.svg"
---

*When a startup offers equity alongside salary, the question is never rhetorical: what is it actually worth? **How to value a startup equity offer** requires a practical framework: establish your ownership percentage after dilution, estimate the company's likely [enterprise-value](/enterprise-value/) at exit, and weight outcomes by their probability. The result is an expected value in dollars—not certainty, but a rational basis for deciding whether to take the offer.*

<div class="wiki-hatnote">

This article assumes standard common stock or option grants to employees. It does not cover preferred stock valuations (used by investors) or specialized securities like SAFEs or convertible notes. For founders' equity, the logic applies but the negotiation context differs.

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Startup Equity Valuation — key facts</div>

<img src="/svg/equity.svg" alt="An abstract editorial mark for equity." />

<div class="wiki-infobox-caption">Expected value is ownership percentage times likely exit value, discounted for risk.</div>

|   |   |
|---|---|
| **Three inputs** | Current ownership percentage, probability of outcomes, exit value per outcome |
| **Dilution** | Assume 15–25% additional dilution for future rounds; obtain option pool size from the company |
| **Exit scenarios** | Acquisition ($20M–$500M+), IPO ($1B+), or failure (zero) |
| **Discount** | Reduce expected value by 40–70% for time value and risk |
| **Reality check** | Compare to salary foregone; if equity is >5 years of salary, scrutinize assumptions |

</aside>

## Step 1: Establish Your True Ownership Percentage

Your offer likely specifies a number of shares (e.g., "50,000 shares") and sometimes a vesting schedule (e.g., "4 years, 1-year cliff"). But raw share count is meaningless without context.

First, ask: **What is the total shares outstanding after this grant?** If the company won't say, that's a red flag. But assume a typical early-stage startup issued shares to founders, early investors, and employees. Total outstanding might be 10 million shares. Your 50,000 shares is therefore 0.5%.

But the company likely also has an **option pool**—a reserved block of shares (typically 10–20% of fully diluted shares) set aside for future employees. This pool dilutes existing shareholders proportionally. If the pool is 1 million shares (10% of 10 million), your true diluted ownership is roughly 50,000 / 11 million = 0.45%.

**Key question to ask**: 
- Total shares outstanding (including vested employee options)?
- Option pool size (shares reserved for future hires)?
- Any preferred stock issued to investors? (If yes, get the fully diluted cap table.)

Example: A Series A startup has 5 million common shares issued. An option pool of 1 million is reserved. You are offered 75,000 shares. Your current ownership is 75,000 / (5 million + 1 million fully diluted) = 1.25%.

## Step 2: Model Dilution From Future Fundraising

Startups rarely stop at Series A. If the company raises again—Series B, C, or D—each round dilutes existing shareholders. Later investors demand preferred stock, which can have liquidation preferences, but for your common stock valuation, the key is *what fraction of the company you own post-round*.

A rough rule of thumb: assume an additional 15–25% dilution over the next 5 years if the company is pre-Series A or Series A. (Series B+ companies with demonstrated traction often see less dilution in later rounds.)

If you own 1.25% now and the company raises Series B two years from now, issuing new stock that dilutes all existing shareholders by 20%, your ownership falls to 1.0%.

**Conservative approach**: Reduce your ownership percentage by 20% to account for future dilution.

Example: 1.25% × (1 – 0.20) = 1.0% post-dilution ownership.

## Step 3: Estimate Exit Outcomes and Values

Your equity is worth money only if the company exits profitably. There are three broad scenarios:

### Failure (Probability: 50–80%)

Most startups fail or exit at valuations below the last funding round. If the company burns cash and cannot raise more, it may wind down, sell assets, or merge at a loss. Common shareholders typically get nothing.

Probability depends on stage: early-stage (Seed–Series A) failure rates are 50–70%; later-stage (Series C+) are 20–30% because selection effects favor funded companies.

Value in failure: $0.

### Acquisition (Probability: 15–40%)

The most common successful exit. A larger company buys the startup. The acquirer negotiates a price (enterprise value), often expressed as a multiple of revenue or based on a strategic valuation.

Early-stage startups that exit via [acquisition](/acquisition/) typically see acquirers valued at $50M–$500M; some break $1B (e.g., a hot AI company). The acquirer often pays in cash, stock, or a combination. If they pay $200M for a company and common shareholders are last in line after preferred investors and debt, the common stock pool might capture 20–50% of that, depending on the cap table.

**Reality check**: 
- Ask founders if there has been any interest from acquirers.
- Research comparable acquisitions in the sector (Crunchbase, PitchBook, or recent news).
- A Series B software company with $5M revenue might exit at a 5–10× revenue multiple, or $25M–$50M.
- A deep-tech company with no revenue yet would exit on a strategic rationale, often $100M–$1B+ if the tech is strong.

Probability and value depend on product-market fit, team reputation, market size, and traction. No formula exists; judgment is required.

Example: You estimate a 30% chance of acquisition at an $150M enterprise value. If common shareholders recover 30% after preferred investors, your share is 1% × $150M × 30% = $450,000.

### IPO (Probability: 5–15%)

A minority of startups go public via [initial-public-offering](/initial-public-offering/). At IPO, the company typically has >$100M in revenue or clear path to profitability, and a valuation in the billions.

Your ownership percentage translates directly to public market value. If you own 1% and the IPO values the company at $5 billion, your stake is worth $50 million. But this is pre-lock-up: you may not be able to sell immediately, and secondary sales are typically staggered.

Probability of IPO is low for most startups but non-zero if the company has strong growth and clear unit economics.

Example: You estimate a 10% chance of IPO at $2 billion valuation. Your 1% stake is worth $20 million.

## Step 4: Calculate Expected Value

Multiply probability by outcome for each scenario:

```
Expected Value = (P_failure × $0) + (P_acq × Value_acq) + (P_ipo × Value_ipo)
```

Example calculation:

- Failure (60% probability): $0
- Acquisition at $150M (30% probability): 1.0% ownership × $150M × 0.30 recovery for common = $450,000
- IPO at $2B (10% probability): 1.0% ownership × $2B = $20 million

Expected Value = (0.60 × $0) + (0.30 × $450,000) + (0.10 × $20M) = $135,000 + $2,000,000 = **$2,135,000**

## Step 5: Discount for Time and Risk

The expected value above is nominal and assumes the exit happens immediately. In reality, startups take 5–10 years to exit (if they do). You must discount for:

1. **Time value of money**: $1 million in 7 years is worth ~$500,000 today (at 10% discount rate).
2. **Execution risk**: Even with favorable scenarios, the company might miss targets, lose key people, or face unforeseen competition. Subjective risk: apply a 20–30% haircut.

A practical approach: apply a 40–70% haircut to the expected value depending on stage and risk profile.

Early-stage (Seed–Series A): 60–70% haircut.
Series B–C: 40–50% haircut.

Example: Your $2.135M expected value becomes $2.135M × 0.40 = ~$854,000 after a 60% discount for risk and time.

This is a rough heuristic. If you want precision, use a [discounted-cash-flow-valuation](/discounted-cash-flow-valuation/) approach: model cash flow to exit, apply a [discount-rate](/discount-rate/) of 40–60% (reflecting startup risk), and solve for net present value.

## Comparing to Salary and Vesting

Once you have a discounted expected value, compare it to the salary you're being offered—and the salary you'd make elsewhere.

If the startup offers $100K salary + equity worth $854K (discounted expected value), and you'd make $150K at a big tech company with no equity, the trade-off is: give up $50K annual salary for a chance at $854K in equity.

Over 4 years (typical vesting), that's $200K foregone salary. If your equity fully vests and the company exits at the modeled value, you come out ahead. But if the company fails or takes 10 years to exit, you lose.

**Reality check**: If the equity offer is worth more than 3–5× your annual salary (discounted), the valuation assumptions are likely optimistic. Scrutinize the business plan and comparable exit values.

## Common Pitfalls

- **Ignoring the option pool**: If the pool is large, your dilution is severe. Always ask.
- **Assuming full recovery for common shareholders**: Preferred investors have liquidation preferences. If the company exits below its last funding round's valuation, preferred shareholders may capture all proceeds, and common gets nothing.
- **Overestimating exit probability**: Founder optimism is infectious. Research the market and compare to base rates (how often does a startup at this stage exit successfully?).
- **Discounting too little**: Startup risk is real. A 30–40% haircut is minimum.
- **Forgetting clawback and acceleration clauses**: Some grants clawback if you leave early, or accelerate upon acquisition. Read your option agreement.

## See also

<div class="wiki-seealso">

### Closely related

- [Enterprise Value](/enterprise-value/) — valuation metric used at startup exits
- [Initial Public Offering](/initial-public-offering/) — successful exit path for startups
- [Acquisition](/acquisition/) — most common exit for early-stage companies
- [Discounted Cash Flow Valuation](/discounted-cash-flow-valuation/) — rigorous framework for valuing future cash flows
- [Equity Financing](/equity-financing/) — how startups raise capital and issue shares
- [Carried Interest Compensation](/carried-interest-compensation/) — how investment returns are shared

### Wider context

- [Common Stock](/common-stock/) — ownership and voting in private companies
- [Private Equity Fund](/private-equity-fund/) — institutional investors in startups
- [Liquidation](/liquidation/) — what happens when exits are below funding round valuations
- [Market Risk](/market-risk/) — risk of holding concentrated private positions
- [Cost of Equity](/cost-of-equity/) — required return for illiquid equity investments

</div>
