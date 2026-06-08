---
title: "Jump Risk"
description: "The discontinuous, price-gap hazard that standard diffusion models systematically underestimate, causing sudden large moves."
keywords:
  - jump risk
  - price gap
  - discontinuous movement
  - diffusion models
  - tail risk
  - valuation model risk
image: "/svg/risk.svg"
---

*A **jump risk** is the potential for a security's price to gap—to move sharply and discontinuously in a single trade or session—rather than drift smoothly, as traditional continuous-diffusion models assume. Jump risk represents the gap between real market behaviour and the mathematical models used to price derivatives and manage risk; underestimating jump risk is a common source of surprise losses and model failure.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Jump Risk — key facts</div>

<img src="/svg/risk.svg" alt="An abstract editorial mark for risk topics." />

<div class="wiki-infobox-caption">The flaw in models that assume smooth price movement; reality includes gaps.</div>

|   |   |
|---|---|
| **What it is** | Discontinuous price movement not captured by continuous-diffusion models |
| **Also called** | "Jump process risk", "Gap risk", "Discontinuity risk" |
| **Caused by** | Earnings shocks, regulatory news, market sentiment shifts, liquidity events |
| **Impact on models** | [Black-Scholes](/black-scholes-model/) and similar models underestimate tail losses |
| **Relevant to** | Options, bonds, equities; critical for tail-risk hedging and [VaR](/value-at-risk/) |
| **Modeling fix** | Jump-diffusion models (Poisson jumps, Lévy processes) |

</aside>

## The assumptions that create jump-risk blindness

The [Black-Scholes model](/black-scholes-model/) and most finance textbooks assume that security prices follow a **geometric Brownian motion**—a continuous, smooth random walk where prices can change by infinitesimally small amounts at each instant. Under this assumption, a stock cannot jump from \$100 to \$95 without passing through \$97.50, \$96.25, and so on. Prices are always continuous; volatility (the standard deviation of returns) follows the diffusion model's specification.

This assumption is convenient for mathematics. It allows closed-form solutions like the Black-Scholes formula and makes derivatives pricing tractable. But it is empirically false. Real stock prices and bond prices **jump**. An earnings surprise, a rating downgrade, a geopolitical shock, or a sudden shift in liquidity can cause a bid-ask gap where no trade occurs at intermediate prices. The next trade happens at a price several percentage points away.

Jump risk is the difference between what the model predicts can happen and what actually happens. When you price a [call option](/call-option/) using Black-Scholes, you are implicitly assuming the underlying stock will not jump 15% in a single session. But it can. The model then underprices the tail risk—the chance of an extreme loss—and the hedges built on the model fail.

## Where jumps come from in practice

Jumps are not rare events; they happen regularly. Earnings announcements, [credit rating](/credit-rating/) changes, regulatory decisions, [merger](/merger/) announcements, bankruptcy filings, and major litigation outcomes all trigger jumps. A company misses earnings badly, and the stock is down 12% at the open. A patent is upheld in court, and a stock jumps 8% on the news. A [credit spread](/credit-spread/) widens as a lender's health deteriorates, and bond prices fall by 2–3 points in a single session.

Jumps can also result from [liquidity](/liquidity-risk/) events. If a large position needs to be liquidated and the market depth is shallow, the seller may only fill orders at increasingly worse prices, creating a visible gap. [Volatility](/historical-volatility/) itself can jump: a market that seemed calm can suddenly become stressed (the "volatility jump"), and prices of assets exposed to volatility risk—like long-dated options—can shift sharply.

These jumps are often predictable in the abstract (we know earnings are coming), but their magnitude and sign are not. This is the signature of jump risk: the hazard that a known or unknown event will cause a gap, and the models used to price and hedge do not account for it.

## How models miss jump risk

Standard models miss jump risk in two ways. First, they assume volatility is constant, but volatility itself jumps. The [implied volatility](/implied-volatility/) of an option can spike 50% in a day if the underlying asset becomes more uncertain. Models using a single historical volatility number are caught flat-footed.

Second, standard models cannot produce the observed distribution of real returns. Real return distributions have **fat tails**—more extreme events than a normal distribution predicts. A normal distribution says a 5-standard-deviation move should occur once every 7,000 years; in reality, financial markets experience such moves every few years. Jump-diffusion models can better fit the empirical distribution because they allow for sudden, large moves.

The most famous model failure tied to jump risk was the 1987 stock market crash, when the S&P 500 fell nearly 23% in a single day. Option traders and risk managers using Black-Scholes were catastrophically unprepared. The model said such a move was essentially impossible (billions of standard deviations away); the market did it anyway. Similarly, the 2008 financial crisis and the March 2020 COVID shock both involved market jumps that vaporized fortunes in portfolios hedged using models that assumed continuous prices.

## Jump-diffusion and Lévy process models

To better capture reality, financial mathematicians developed **jump-diffusion models**, which allow the price to follow a smooth diffusion path interspersed with random jumps. At any moment, the price can either drift gradually (Brownian motion) or jump (a Poisson process). The frequency and size of jumps are parameters fitted to historical data.

More sophisticated alternatives use **Lévy processes**, which generalize both diffusion and jump components and allow for self-similar, scale-free behavior—long tails without assuming a specific jump size. These models fit market data much better but are harder to calibrate and have no closed-form solutions; practitioners must use numerical methods.

The trade-off is familiar: realism versus tractability. Black-Scholes is simple and widely used, but it is wrong about jump risk. More realistic models are harder to implement, require more data, and can fit the training data so closely that they overfit and predict poorly out of sample. A bank using a sophisticated model that fits the last five years perfectly may still be blindsided by a new regime.

## Hedging against jump risk

If you believe jump risk is real and material, how do you hedge it? Straightforward [put options](/put-option/) help, but only if the market prices them fairly—which it often does not, because most models underestimate jump risk. A put that costs 2% of your portfolio to buy might seem expensive if the model says a crash is a billion-to-one shot. But if crashes happen every few years, the put is cheap.

Some investors use [value at risk](/value-at-risk/) (VaR) to measure jump risk, but standard VaR also assumes continuous distributions and underestimates tail risk. Conditional VaR (or expected shortfall) is better, as it measures the expected loss beyond the VaR threshold, capturing some tail information. But even conditional VaR can miss jump events if they are more frequent or severe than the historical sample suggests.

Practical hedging often relies on diversification, maturity management, and stress testing. Holding assets from many uncorrelated sources reduces the chance that a single event wipes out the portfolio. Keeping short duration (low interest rate risk) reduces exposure to sharp [yield](/yield-curve/) moves. And regularly asking "what if interest rates spike 100 basis points overnight, or the stock market falls 20%?" helps identify exposures that models miss.

## See also

<div class="wiki-seealso">

### Closely related

- [Event Risk](/event-risk/) — Discrete loss from specific corporate or market shocks
- [Tail Risk](/tail-risk/) — Extreme loss potential; jump risk is a major source
- [Volatility](/historical-volatility/) — Jump risk includes volatility jumps and spike risk
- [Black-Scholes Model](/black-scholes-model/) — Model that assumes continuous prices and underestimates jumps
- [Put Option](/put-option/) — Hedging tool for tail risk including jump risk

### Wider context

- [Value at Risk](/value-at-risk/) — Risk metric that models often underestimate for jumps
- [Implied Volatility](/implied-volatility/) — Changes sharply during jumps
- [Idiosyncratic Risk](/idiosyncratic-risk/) — Company-specific shocks often cause jumps
- [Credit Spread](/credit-spread/) — Widens suddenly during credit events
- [Liquidity Risk](/liquidity-risk/) — Sudden illiquidity can force price gaps
- [Beta](/beta/) — Assumes continuous correlation; breaks during jumps

</div>
