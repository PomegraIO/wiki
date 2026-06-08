---
title: "Dollar Gamma"
description: "Gamma expressed in dollar terms, measuring the profit or loss from a one-percent move in the underlying's price."
keywords:
  - gamma
  - delta
  - greeks
  - options pricing
  - portfolio risk
  - derivatives
  - p&l sensitivity
image: /svg/derivatives.svg
---

*Dollar gamma is [gamma](/gamma/) converted into actual profit-and-loss impact, showing how many dollars an option position gains or loses when the underlying moves by one percent. It bridges the gap between the abstract rate of change and the concrete financial reality of hedging and speculation.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Dollar Gamma — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives and options pricing." />

<div class="wiki-infobox-caption">Gamma quantified in currency, not rate of change.</div>

|   |   |
|---|---|
| **What it is** | Gamma multiplied by the underlying price and the notional portfolio value, expressed in dollars per one-percent move |
| **Also called** | Gamma dollar value, gamma P&L, money gamma |
| **Unit** | Dollars (or local currency) per 1% underlying move |
| **When it matters most** | Portfolio hedging, risk management, intraday trading, volatility strategies |
| **Opposite risk** | [Theta](/theta/) — time decay erodes gamma's value daily |
| **Related concept** | [Delta](/delta/) — first derivative; gamma is the second |

</aside>

## The dollar translation problem

Raw [gamma](/gamma/) — typically expressed as a decimal between 0 and 1 — tells you that your delta will change by some fraction when the underlying moves. But traders care about money. A gamma of 0.05 means nothing to a risk manager unless you know how much that translates to actual profit or loss. Dollar gamma fills that gap. It answers the question every desk asks: *If the market moves 1%, how much does this position make or lose?*

The calculation is straightforward but critical. Dollar gamma equals gamma multiplied by the underlying price and the position size (notional delta), divided by 100. For a large [call option](/call-option/) position in a stock trading at $100, a gamma of 0.02 and a delta of 500 contracts might yield a dollar gamma of roughly $1,000 per 1% move. That means a 1% rally generates $1,000 in unrealized profit from the convexity alone.

## Why traders prefer this metric

Gamma in decimal form is a mathematician's number. Dollar gamma is a trader's number. When a portfolio holds thousands of positions across multiple underlyings and [strikes](/strike-price/), aggregating raw gamma tells you nothing actionable. You need a single currency figure that represents your true directional sensitivity. A long straddle with positive dollar gamma profits when volatility expands and the underlying moves sharply in either direction. A short gamma position — common in many [market maker](/market-maker-trading/) strategies — bleeds money on volatile days.

Portfolio managers use dollar gamma to set risk limits. A desk might impose a maximum dollar gamma of $50,000, meaning the portfolio should not be positioned to make or lose more than $50,000 from a 1% one-way move in any single underlying. This is enforceable, intuitive, and directly tied to the firm's risk appetite.

## The relationship to [theta](/theta/) and realized volatility

Dollar gamma is inseparable from [time decay](/time-decay-theta/). Long gamma positions — which profit from large underlying moves — typically have negative dollar theta, meaning they lose money every day the market stays flat. This is the essential [theta-gamma tradeoff](/theta-gamma-tradeoff/): you pay rent (theta) for the right to profit from volatility. A trader holding a long gamma position is essentially betting that the underlying will move by more than the daily theta decay; if the market stays calm, the position loses money day after day.

Conversely, a short gamma position (selling options) generates daily theta revenue but suffers immediately if volatility spikes. The dollar amount of that daily theta bleed, and the dollar gamma sensitivity to a shock move, determine whether the trade is profitable. Many volatility strategies rely on dollar gamma and dollar theta estimates to model profit scenarios.

## Scaling and leverage effects

Dollar gamma scales with the underlying price and portfolio size. A position with 10,000 shares of a $10 stock has a different gamma dollar value than the same position in a $1,000 stock. This is why traders sometimes prefer to think in basis points or as a percentage of portfolio value rather than raw dollars. A $50,000 dollar gamma might be trivial for a $100 million hedge fund but enormous for a $5 million operation.

Leveraged or [inverse](/inverse-etf/) strategies amplify dollar gamma. A 3x leveraged equity ETF has triple the dollar gamma of the underlying index fund, making it far more sensitive to large daily moves. During periods of market stress, this amplification can trigger cascading losses or gains that exceed expectations based solely on index movements.

## Practical risk management applications

Risk committees use dollar gamma to enforce position limits. An equity trading desk might allow $2 million of positive dollar gamma (betting on volatility expansion) but cap short dollar gamma at $1 million to avoid catastrophic losses on gap moves. Options [brokers](/broker/) use dollar gamma to estimate margin requirements: a position with high positive dollar gamma represents less immediate counterparty risk during a calm market but poses extreme tail risk in a crash.

Volatility [spreads](/spread/) — buying one [call option](/call-option/) and selling another at a different strike — generate specific dollar gamma profiles. A [bull call spread](/call-option/) has positive dollar gamma in a narrow price range and zero or negative gamma outside it. Understanding these profiles in dollar terms is essential for traders deciding which structures suit their directional and volatility views.

## Dollar gamma in stress scenarios

When markets move 5% or 10% in a single day, dollar gamma compounds rapidly. The [gamma P&L](/gamma/) becomes the dominant profit driver. A fund that misjudged its dollar gamma exposure can face sudden margin calls or capital losses that overwhelm the stated risk limits. During the 2020 volatility spike and the subsequent market rebounds, portfolios with large positive dollar gamma outperformed spectacularly, while short-gamma positions were decimated.

Conversely, market makers who maintain strictly balanced dollar gamma across strikes and underlyings protect themselves from directional shocks. By staying "gamma neutral" in dollar terms — not overly long or short convexity — they collect theta decay as their primary revenue without exposing themselves to catastrophic moves.

## See also

<div class="wiki-seealso">

### Closely related

- [Gamma](/gamma/) — the rate of change of delta, expressed in abstract terms
- [Theta-Gamma Tradeoff](/theta-gamma-tradeoff/) — the fundamental dynamic of long versus short option positions
- [Delta](/delta/) — first-order sensitivity to underlying moves
- [Theta](/theta/) — daily time decay, opposed to gamma profit
- [Vega](/vega/) — sensitivity to changes in implied volatility

### Wider context

- [Option](/option/) — the underlying instrument whose sensitivity is being measured
- Greeks — the full toolkit of derivative sensitivities
- [Volatility Smile](/volatility-smile/) — how gamma varies across strikes
- Risk Management — broader portfolio control
- Hedging — gamma's role in protecting positions

</div>
