---
title: "Dividend Yield Plus Growth Model"
description: "An estimate of required equity return as the sum of the current dividend yield and the long-run expected dividend growth rate."
keywords:
  - dividend yield
  - required return
  - equity return
  - cost of capital
  - dividend growth
image: "/svg/valuation.svg"
---

*The **Dividend Yield Plus Growth Model** is a simple two-input formula that estimates the [cost of equity](/cost-of-equity/) (or required return on a stock) by adding the current [dividend yield](/dividend-yield/) to the expected long-run growth rate of dividends. It is one of the oldest and most widely cited shorthand in equity finance.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Dividend Yield Plus Growth Model — key facts</div>

<img src="/svg/valuation.svg" alt="An abstract editorial mark for valuation methods." />

<div class="wiki-infobox-caption">A two-variable approximation of required return; simple but limited.</div>

|   |   |
|---|---|
| **What it is** | Required return = Dividend yield + Expected dividend growth |
| **Formula** | r = (D₁ / P₀) + g |
| **Speed** | Fastest of all return estimates—two observable or stated inputs |
| **Key use** | Benchmarking cost of equity; setting hurdle rates for mature firms |
| **Limitation** | Assumes dividends will grow at constant rate forever |
| **Applies to** | Stable, mature firms with consistent dividend policy |

</aside>

## The simple model

The Dividend Yield Plus Growth Model rests on a rearrangement of the [dividend discount model](/dividend-discount-model/) formula. The basic DDM says:

**P₀ = D₁ / (r − g)**

Where P₀ is today's stock price, D₁ is next year's expected dividend, r is the required return, and g is the perpetual growth rate. Rearranging to solve for r gives:

**r = (D₁ / P₀) + g**

The first term, D₁ / P₀, is the forward [dividend yield](/dividend-yield/)—the cash dividend per share expected next year divided by the price today. The second term, g, is the expected growth rate of dividends in perpetuity. Their sum is the required return.

## Why it makes sense

The logic is intuitive. An investor buys a stock expecting two sources of return: cash income (the dividend) and capital appreciation (price growth, which is tied to dividend growth in this model). If a stock yields 3% in dividends and dividends grow at 5% annually, the investor expects a 3% + 5% = 8% return.

In equilibrium, this required return should match the risk of the stock. A defensive utility with stable cash flows should have a lower required return than a cyclical industrial firm. The model captures this through the yield and growth terms: a utility might yield 4% with 3% growth (7% required return); a cyclical firm might yield 1% with 8% growth (9% required return).

## The yield component

The dividend yield is observable: today's dividend divided by today's stock price. If a firm pays an annual dividend of £2 and the stock trades at £50, the yield is 4%. This part of the formula is mechanical and uncontroversial.

In practice, analysts often use the *next* expected dividend (forward yield) if they believe the company will increase its payout imminently. A firm that just raised its dividend might have a 3% trailing yield but a 3.5% forward yield.

## The growth component

This is where judgment enters. The model assumes dividends will grow at rate g forever. Where does g come from?

**Historical average**: analysts often use the long-term historical dividend growth rate. A firm that has grown dividends at 4% over 20 years might be assumed to continue at 4%.

**Long-run GDP growth**: some use the expected long-run nominal GDP growth rate (inflation + real growth) as a proxy for a firm's perpetual growth. If nominal GDP grows at 3–4%, a mature firm probably cannot grow faster indefinitely.

**Analyst forecast**: some rely on consensus sell-side estimates of 5-year or 10-year dividend growth, accepting that beyond that horizon, the rate will settle toward some stable level.

**Management guidance**: firms sometimes provide explicit dividend-growth targets (e.g., "grow dividends 5–7% annually").

The choice matters. If g = 3%, then r = 4% yield + 3% = 7%. If g = 5%, then r = 9%. A 2-percentage-point assumption difference swings the required return by 2 points.

## Practical application

Portfolio managers and corporate finance teams use this model to:

- **Set hurdle rates**: a firm evaluating a capital project will set its required return based on its [cost of equity](/cost-of-equity/). If the yield-plus-growth model says 8%, any project must clear an 8% return bar.
- **Screen valuations**: if a stock's implied return (yield + expected growth) looks low relative to its risk, it may be overpriced. Conversely, a high implied return might signal undervaluation.
- **Benchmark against alternatives**: an investor comparing a stock to a bond can ask, "Does 8% equity return compensate me for the risk versus a 5% bond yield?"

## Limitations and departures from reality

The model's simplicity is both strength and weakness.

**Constant growth assumption**: Real firms rarely grow dividends at a constant rate forever. Most experience a high-growth phase, transition, and maturity. The H-Model and multistage models handle this; the dividend yield plus growth model cannot.

**Growth and risk are linked**: The model treats g as independent of r. In reality, faster-growing firms are often riskier. If g rises (say, a firm enters a riskier, higher-growth business), r should also rise. The simple model ignores this coupling.

**Non-dividend-paying firms**: Firms that do not pay dividends (or reinvest all earnings) don't fit this model directly. Analysts adapt it by using implied dividends or switching to other methods, but the adjustment is ad-hoc.

**Circular reasoning**: If you observe a stock price and use the model to back out r, you're not really *estimating* required return—you're assuming the market price is correct and extracting the implied rate. This is valid for [implied cost of equity](/implied-cost-of-equity-ddm/) calculations but not independent of the market.

**Growth is hard to forecast**: 10-, 20-, or 30-year dividend growth rates are guesses. Economic conditions change, competitive landscapes shift, and firms alter capital allocation policy. Committing to a single g value invites overconfidence.

## When it works best

The model is most reliable for:

- Large, established firms with decades of stable dividend history.
- Industries with predictable, low growth (utilities, mature consumer staples).
- Sectors where long-run growth converges toward GDP growth (e.g., food, beverages, basic goods).

It is least reliable for:

- High-growth firms (tech, biotech) where dividend policy is irregular or nonexistent.
- Turnaround or cyclical businesses with volatile dividend history.
- Young firms in uncertain competitive positions.

## Comparison to alternatives

The [Capital Asset Pricing Model](/capital-asset-pricing-model/) (CAPM) estimates cost of equity using [beta](/beta/) and market risk premium: r = rₓ + β(rₘ − rₓ). CAPM is theoretically grounded but requires estimating beta. The dividend yield plus growth model is more direct—just yield and growth—but theoretically weaker.

The [H-Model](/h-model-dividend-valuation/) and [Stochastic Dividend Discount Model](/stochastic-dividend-discount-model/) offer more realism at the cost of more parameters. For a quick sanity check or a teaching example, dividend yield plus growth is hard to beat.

## See also

<div class="wiki-seealso">

### Closely related

- [Dividend Discount Model](/dividend-discount-model/) — the foundational valuation formula from which this return estimate derives
- [H-Model](/h-model-dividend-valuation/) — a richer dividend valuation with two growth phases
- [Implied Cost of Equity (DDM-Derived)](/implied-cost-of-equity-ddm/) — backing out required return from observed price
- [Cost of Equity](/cost-of-equity/) — the broader concept of return required on equity investment
- [Dividend Yield](/dividend-yield/) — the income component of stock returns
- [Capital Asset Pricing Model](/capital-asset-pricing-model/) — an alternative method for estimating cost of equity

### Wider context

- [Stock](/stock/) — the security whose return is being estimated
- [Dividend](/dividend/) — the cash payment to shareholders
- Required Return — the minimum acceptable return on investment
- [Market Risk Premium](/market-risk-premium/) — the excess return investors demand for bearing market risk
- Long-Term Capital Gain Tax — tax treatment of investment returns

</div>
