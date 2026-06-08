---
title: "Cost of Equity vs Required Return in the DDM"
description: "Cost of equity is a firm's cost to raise equity capital; required return is an investor's threshold to invest. In DDM, which one you use changes the valuation."
keywords:
  - cost of equity vs required return
  - dividend discount model
  - cost of capital
  - required rate of return
  - ddm valuation
  - equity valuation
image: /svg/valuation.svg
---

*In the [Dividend Discount Model](/dividend-discount-model/), the discount rate is a critical input—but is it the company's **cost of equity** (what the firm pays to raise capital) or the **investor's required return** (the minimum yield demanded to hold the stock)? They sound identical but rarely are, and the choice determines whether the stock looks cheap or expensive.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Cost of Equity vs Required Return — key distinctions</div>

<img src="/svg/valuation.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Two perspectives on the same hurdle, two different valuations.</div>

|   |   |
|---|---|
| **Cost of equity** | What the firm must earn to compensate all equity holders for risk; firm's cost of capital |
| **Required return** | What you (the investor) demand to accept the stock's risk; your personal hurdle rate |
| **Who decides?** | Cost of equity: determined by market pricing [beta](/beta/), spreads; Required return: your risk appetite |
| **Typical calculation** | Both use [CAPM](/capital-asset-pricing-model/): Required Return / Cost of Equity = Risk-Free Rate + Beta × Market Risk Premium |
| **Formula identity** | They use the same formula, but inputs reflect different perspectives |
| **DDM impact** | Higher discount rate = lower intrinsic value |
| **Reconciliation** | If cost of equity ≠ required return, the stock may be misvalued relative to your threshold |
| **Common mistake** | Using cost of equity (firm's perspective) when you mean your required return (investor's perspective) |

</aside>

## The subtle but critical distinction

Imagine a stock trading at $100. The company's management calculates a cost of equity of 8% using the [Capital Asset Pricing Model](/capital-asset-pricing-model/). This is what the firm believes it must earn on equity investments to keep investors satisfied.

But you, as an investor, demand a 12% return to hold the stock. You perceive its [beta](/beta/) as higher, or you demand a risk premium the market has not priced in, or you simply have other options offering 12%.

Now you run a [Dividend Discount Model](/dividend-discount-model/) valuation. If you use 8% (the company's cost of equity), the model says the stock is worth $125. If you use 12% (your required return), the model says it's worth only $75. Which is correct? Both—they're asking different questions.

**Cost of equity** answers: "What value is this stock worth if every investor in it earns the firm's target return?" It's the fair value from the company's capital-allocation perspective.

**Required return** answers: "What value would this stock need to offer for me to buy it?" It's the fair value from your investment perspective.

## Calculating cost of equity

Most practitioners calculate cost of equity using the Capital Asset Pricing Model:

**Cost of Equity = Risk-Free Rate + Beta × (Market Risk Premium)**

Suppose:
- Risk-free rate: 4% (long-term Treasury yield)
- Beta for the stock: 1.2 (stock moves 20% more than the market)
- Market risk premium: 5% (long-term expected excess return on stocks over bonds)

Cost of Equity = 4% + 1.2 × 5% = **10%**

This 10% is what the company's management considers the minimum return needed to compensate shareholders for equity risk. It is **market-wide, impersonal, and firm-specific only via beta**. If the stock's beta is 1.2, its cost of equity is roughly 10% regardless of who owns it.

## Calculating required return

Your required return is similar in form but personal in content:

**Required Return = Risk-Free Rate + Your Perceived Beta × (Your Perceived Market Risk Premium)**

You might calculate:
- Risk-free rate: 4% (you agree with the market here)
- Your perceived beta: 1.5 (you think the stock is riskier than consensus beta suggests—maybe management is weak, or the competitive position is weaker than headlines imply)
- Your perceived market risk premium: 6% (you are more pessimistic about long-term stock returns than the historical average; you demand a higher hurdle)

Your Required Return = 4% + 1.5 × 6% = **13%**

Now the same stock has two "correct" discount rates: 10% (cost of equity, market consensus) and 13% (your required return, personal view). This is not a mistake; it is the essence of investment disagreement.

## Applying each to the DDM

The Dividend Discount Model (constant growth version) is:

**Stock Value = Next Year's Dividend ÷ (Discount Rate − Growth Rate)**

Assume a stock pays an annual dividend of $2 per share and grows it at 3% per year.

**Using cost of equity (10%):**
Stock Value = $2 ÷ (0.10 − 0.03) = $2 ÷ 0.07 = **$28.57 per share**

This is the "fair value" based on market consensus about risk and return. If the stock trades at $30, it's slightly expensive; at $25, slightly cheap, by consensus.

**Using your required return (13%):**
Stock Value = $2 ÷ (0.13 − 0.03) = $2 ÷ 0.10 = **$20 per share**

By your standard, the stock is overpriced at $30—you'd need to see it at $20 or below to pull the trigger.

## Which one should you use?

If you are **a company manager** making capital-allocation decisions (building factories, buying competitors), use **cost of equity**. You need to know: "Will this project earn enough to compensate shareholders at the market rate?" If cost of equity is 10% and your project earns 8%, kill it.

If you are **an individual investor or portfolio manager** making buy/sell decisions, use **your required return**. You need to know: "Does this stock offer a return that exceeds my hurdle rate and my alternatives?" If your required return is 12% and the stock's earnings yield (dividend/price) implies only 8%, you pass.

The confusion arises because both use the same formula. The internet, textbooks, and software often treat them synonymously. But they diverge whenever:

1. **You disagree with market beta.** You think the stock is riskier than its historical beta suggests (perhaps due to upcoming execution risk or competitive threats).
2. **You demand a different market risk premium.** You are more or less optimistic than consensus about long-term stock returns.
3. **You include idiosyncratic premiums.** You demand extra return because the stock is illiquid, you have concentrated exposure, or you know something unpopular about its sector.

## Real-world divergence: Why it matters

Consider a dividend-paying utility stock with a cost of equity of 7% (low beta, stable). The market prices it at $50, implying a dividend yield of 4% and expected total return (dividend plus growth) of, say, 6.5%. This is below the cost of equity, which might seem like a bargain—the market is pricing in a return below what shareholders should demand.

But here's the catch: the stock is perceived as safe and stable. **Many investors accept 6.5% for that safety.** Their required return is lower than the cost of equity because they value stability. They are comfortable with the lower return for the lower volatility and income predictability.

Conversely, a small-cap biotech stock with a cost of equity of 18% might trade at valuations implying a 15% expected return (dividend unlikely; purely from capital appreciation and growth reinvestment). Investors with high risk tolerance—say, required return of 12%—see the stock as a bargain. It exceeds their hurdle. Investors with a 20% required return see it as too expensive. Both perspectives are internally consistent.

## Reconciling the two when valuing a stock

**Step 1: Calculate the stock's current "implied required return."**
- Observe its price, expected dividend, and expected growth rate.
- Solve for the discount rate: Implied Return = (Next Dividend ÷ Price) + Growth Rate.

**Step 2: Compare to the cost of equity.**
- If implied return > cost of equity, the stock is priced below fair value by consensus.
- If implied return < cost of equity, the stock is priced above fair value by consensus.

**Step 3: Compare to your required return.**
- If implied return > your required return, the stock meets or exceeds your hurdle.
- If implied return < your required return, the stock falls short of your threshold.

**Example:**
- Stock price: $40
- Dividend: $2
- Growth: 3%
- Implied required return = ($2 ÷ $40) + 3% = 5% + 3% = **8%**
- Cost of equity (market consensus): 10%
- Your required return: 12%

By this analysis:
- The stock is **expensive vs. the market** (8% implied < 10% cost of equity).
- The stock is **very expensive vs. your hurdle** (8% implied < 12% required return).
- You would pass, even though some investors might see it as cheap.

## Pitfalls in practice

**Pitfall 1: Using cost of equity when evaluating the stock for your portfolio.** If you calculate a 10% cost of equity but demand a 14% return for stocks with that risk profile, using 10% as your discount rate will overvalue the stock. You'll buy positions you should pass on.

**Pitfall 2: Conflating risk-free rate and beta into a single "risk premium."** The two components of required return are distinct. A 2% rise in the risk-free rate (e.g., from 4% to 6%) affects all stocks equally; it doesn't change risk. A rise in beta affects only that stock. Conflating them distorts comparisons.

**Pitfall 3: Ignoring that required return changes with circumstances.** Your required return is not fixed. In a downturn, when you become more risk-averse, your required return rises. In a bull market, it may fall. The same stock can be overpriced in one regime and underpriced in another.

**Pitfall 4: Assuming cost of equity is stationary.** Over time, beta changes (as the business matures or becomes riskier), and the market risk premium fluctuates. A stock's cost of equity is not timeless.

## See also

<div class="wiki-seealso">

### Closely related

- [Dividend Discount Model](/dividend-discount-model/) — the valuation framework that depends on discount rate choice
- [Capital Asset Pricing Model](/capital-asset-pricing-model/) — the standard way to calculate cost of equity or required return
- [Beta](/beta/) — the systematic risk measure that drives both calculations
- [Cost of capital](/cost-of-equity/) — the firm's overall hurdle for investment projects
- Required rate of return — your personal investment threshold

### Wider context

- [Cost of equity vs cost of debt](/cost-of-equity/) — how a firm's overall cost of capital is built
- Valuation — the broader framework these discount rates serve
- Risk and return — the economic principle underlying both concepts
- [Discounted cash flow](/discounted-cash-flow-valuation/) — broader than dividends; same discount-rate logic
- [Market risk premium](/market-risk-premium/) — the expected excess return on stocks; a key input to both calculations

</div>
