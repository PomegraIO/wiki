---
title: "Myron Scholes"
description: "Canadian-American financial economist who derived the Black-Scholes model for pricing options, revolutionizing derivatives trading and finance theory."
keywords:
  - black-scholes model
  - options pricing
  - derivatives
  - long-term capital management
  - volatility
  - financial engineering
---

*Myron Scholes is a Canadian-American financial economist whose work on [options](/option/) pricing became the mathematical engine of the modern derivatives industry. Along with physicist Fisher Black (and completed after Black's death by Robert Merton), Scholes developed the [Black-Scholes model](/black-scholes-model/) — a formula that tells traders what an [option](/option/) should cost. His later role in the rise and catastrophic collapse of Long-Term Capital Management offers a sobering lesson in the gap between theoretical beauty and real-world risk.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Myron Scholes — key facts</div>

<img src="/svg/people.svg" alt="An abstract editorial mark representing an influential financial economist." />

<div class="wiki-infobox-caption">Author of the formula that transformed options from exotic bets into tradeable securities.</div>

|   |   |
|---|---|
| **Born** | 1941 |
| **Field** | Finance, Mathematical Economics |
| **Central contribution** | [Black-Scholes model](/black-scholes-model/) for options pricing |
| **Prize** | Nobel Prize in Economic Sciences (1997, shared with Merton) |
| **Key insight** | Option prices flow from [volatility](/historical-volatility/), time to expiration, and the underlying asset's dynamics — calculable via differential equations |

</aside>

## The options puzzle

Before the 1970s, [stock options](/option/) — rights to buy or sell shares at a fixed price by a certain date — were exotic instruments traded in a gray market by insiders and speculators. There was no agreed-upon method for pricing them. Traders used rough intuition: a more volatile stock demanded a higher [option premium](/option-premium/); more time before [expiration](/expiration-date/) was worth more. But how much more? No formula existed.

This ambiguity meant the [options market](/option/) remained small and suspect. How could you charge a fair price if you couldn't calculate one? How could institutional investors justify holding an instrument whose value was essentially a guess?

Scholes, working with Fisher Black (a physicist-turned-financier at MIT), tackled the problem using advanced mathematics. The insight was to treat an option as a hedge: instead of trying to guess the option's intrinsic value, ask how much you'd need to hold of the underlying stock to exactly offset the option's risk. If you can replicate the option's payoff through dynamic hedging, arbitrage forces the option price to equal the cost of that hedge.

## The Black-Scholes formula

The model's key assumption is that stock prices follow a [stochastic](/volatility-smile/) process with constant [volatility](/historical-volatility/). Given that, Scholes and Black derived a differential equation whose solution is the now-famous formula:

C = S₀ × N(d₁) − K × e^(−rT) × N(d₂)

where C is the call option price, S₀ is the current stock price, K is the [strike price](/strike-price/), r is the [interest rate](/interest-rate/), T is time to expiration, and N(d₁) and N(d₂) are cumulative normal probability functions.

What makes this formula revolutionary is what it requires as input: only the current stock price, the [strike price](/strike-price/), the time to expiration, the risk-free [interest rate](/interest-rate/), and the stock's [volatility](/historical-volatility/). It does not depend on the option trader's personal forecast of future stock price direction — an insight that puzzled many. The formula says: if you're patient and can rebalance your hedge continuously, direction doesn't matter. Only [volatility](/historical-volatility/) does.

The formula is also elegant in another way: it makes [options](/option/) tradeable as securities, not just gambling contracts. Before Black-Scholes, a [call option](/call-option/) was worth whatever a buyer and seller agreed on. After Black-Scholes, traders could plug in the [volatility](/historical-volatility/) estimate, calculate the fair price, and ask: is the market price higher or lower? If higher, sell; if lower, buy. This arbitrage logic unified the options market, made pricing transparent, and enabled options exchanges to operate at scale.

The model won Scholes and Merton the 1997 Nobel Prize. (Black had died before the prize was awarded, and Nobel prizes are not given posthumously.) Within a decade, Black-Scholes pricing was in every investment bank, every trading desk, every [hedge fund](/hedge-fund/). It became the lingua franca of derivatives trading.

## The model's assumptions and limits

The Black-Scholes formula rests on several critical assumptions:

- Stock prices follow a [log-normal distribution](/volatility-smile/) with constant [volatility](/historical-volatility/).
- There are no [transaction costs](/bid-ask-spread/) and no restrictions on [short selling](/short-selling/).
- The [interest rate](/interest-rate/) is constant.
- No [dividends](/dividend/) are paid.

In reality, each of these fails. Stock [volatility](/historical-volatility/) changes — sometimes wildly — creating a [volatility smile](/volatility-smile/): out-of-the-money options trade at higher implied volatilities than the formula predicts. [Dividends](/dividend/) are paid, [transaction costs](/bid-ask-spread/) exist, and rates change. More fundamentally, real markets occasionally experience sudden shocks — crashes, crises — that behave nothing like a smooth random walk. Options that protect against rare, catastrophic moves (like a [put option](/put-option/) on a stock index) trade at higher prices than Black-Scholes suggests, because the model fails to capture [tail risk](/tail-risk/).

Sophisticated traders and [quants](/quantitative-easing/) responded by building layers atop Black-Scholes: local volatility models, stochastic volatility models, jump-diffusion models. But Black-Scholes remained the baseline, the reference point to which all alternatives are compared.

## Long-Term Capital Management

Scholes' second act began in 1994 when he co-founded Long-Term Capital Management, a [hedge fund](/hedge-fund/) with a blue-chip team including Merton and numerous PhDs in finance and mathematics. LTCM's strategy was elegant: identify relative pricing misfits between bonds, [stocks](/stock/), currencies, and derivatives, hedge away directional risk, and profit from convergence trades. The math was sound, and for several years the returns were spectacular.

By 1998, LTCM had $4.8 billion in assets under management. Then Russia defaulted on its [sovereign debt](/sovereign-debt/), and the [credit spread](/credit-spread/) on risky bonds widened dramatically. Every relative-value trade that LTCM had constructed assumed spreads would stay narrow. They didn't. As prices moved against LTCM's positions, the fund faced margin calls and was forced to sell into a market that was already panicking. Within weeks, a fund that was supposed to be hedged against any conceivable scenario faced the prospect of insolvency.

The Federal Reserve coordinated a $3.6 billion private-sector rescue. Scholes and Merton, who had won the Nobel Prize mere months before the collapse, became symbols of a cautionary tale: even the cleverest math and the smartest people cannot foresee every market scenario. Models work until they don't — and the gap between "not working" and "catastrophic failure" can be measured in days.

## Legacy and reassessment

The Black-Scholes model remains taught in every finance MBA program and used by traders globally. Its core insight — that derivatives can be priced and hedged through dynamic replication — was genuine and has proven durable. Modern [options markets](/option/) operate on Black-Scholes logic, refined and extended but not fundamentally replaced.

The LTCM disaster, however, reshaped the conversation around quantitative finance. It showed that elegant mathematics applied to complex systems can create hidden leverage, correlation risk, and [tail risk](/tail-risk/) that numbers on a page don't capture. Risk models are useful guides, not gospel. Scholes himself has reflected thoughtfully on LTCM, noting that the fund's true error was not the math but operational risk: the market moved faster and further than the models' historical inputs suggested it could.

His work remains the foundation of derivatives finance, yet LTCM serves as a reminder that theories are maps, not territory.

## See also

<div class="wiki-seealso">

### Closely related

- [Black-Scholes model](/black-scholes-model/) — the formula for pricing options
- [Option](/option/) — the right but not obligation to buy or sell an asset at a fixed price
- [Call option](/call-option/) — the right to buy
- [Put option](/put-option/) — the right to sell
- [Volatility](/historical-volatility/) — the standard deviation of price movements
- [Strike price](/strike-price/) — the fixed price at which an option can be exercised
- [Option premium](/option-premium/) — the price paid for an option

### Wider context

- Derivatives — financial instruments whose value depends on underlying assets
- [Hedge fund](/hedge-fund/) — privately managed investment fund using sophisticated strategies
- Long-Term Capital Management — the hedge fund that collapsed in 1998
- [Risk modeling](/value-at-risk/) — quantitative methods for measuring portfolio risk
- [Quantitative trading](/algorithmic-trading/) — trading driven by mathematical models
- [Credit spread](/credit-spread/) — the yield difference between risky and safe bonds
- [Margin call](/margin-call-forex/) — demand for additional collateral when positions move against you

</div>
