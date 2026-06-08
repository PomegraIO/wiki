---
title: "Volatility Targeting in Portfolio Strategy"
description: "How to scale position sizes to maintain constant realized volatility, and how this approach relates to risk parity and dynamic asset allocation."
keywords:
  - volatility targeting portfolio
  - volatility targeting strategy
  - volatility scaling
  - risk parity volatility
  - dynamic position sizing
  - portfolio volatility control
image: /svg/strategies.svg
---

*A **volatility targeting portfolio strategy** adjusts position sizes up when markets are calm (low volatility) and down when markets are turbulent (high volatility) to maintain a constant realized volatility target. This mechanical discipline can smooth returns, reduce drawdowns, and ease rebalancing without requiring market-timing skill.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Volatility Targeting — key facts</div>

<img src="/svg/strategies.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Scale your bets to smooth the portfolio's bumps, not forecast market direction.</div>

|   |   |
|---|---|
| **Target volatility** | Often 8–15% annualized (lower than 100% equities, higher than bonds alone) |
| **Measurement window** | 20–60 day rolling estimate of realized volatility |
| **Leverage ratio** | (Target vol / Current vol) applied to position sizing |
| **Rebalance frequency** | Daily, weekly, or monthly depending on cost tolerance |
| **Benefit** | Smoother returns, lower max drawdowns |
| **Cost** | Whipsaws if volatility oscillates (buy-high/sell-low effect) |
| **Relation to risk parity** | Risk parity is a special case: equal vol contribution across assets |

</aside>

## The core mechanism

Suppose you run a portfolio of U.S. equities and bonds. You set a volatility target of 10% annualized. Here's the process:

1. **Measure current volatility** using the last 30 days of daily returns. Say you find 12% volatility.
2. **Calculate the scaling factor**: 10% / 12% = 0.833.
3. **Scale all positions down** by 16.7% (multiply by 0.833). Your equity weight drops from 70% to 58%, bonds rise from 30% to 42%.

Next month, suppose volatility has calmed to 8%. The scaling factor becomes 10% / 8% = 1.25.

4. **Scale all positions up** by 25%. Equities rise to 72.5%, bonds to 37.5%.

The net effect: the portfolio's expected volatility stays anchored near 10%, regardless of whether markets are historically calm or turbulent. You've tied position size to market conditions without explicitly predicting where markets go.

## Why it works: the volatility paradox

Here's the intuition. In a crash (high volatility regime), your bets shrink. You're defensively positioned not because you think the crash will last (you don't predict the future), but because current volatility is high. You take less risk when risk is highest—pure mechanical discipline.

Conversely, in a bull market with low volatility, you lever up your positions. You take more risk when risk is lowest. This sounds backward, but it has a subtle edge: you buy dips cheaply and sell rallies dearly in the natural course of rebalancing, capturing the mean-reversion tendency that's baked into financial markets.

Over long periods, this trades some upside (you're never fully levered in the biggest rallies) for smoother, more consistent returns. A 10% volatility target compounds more reliably than a 20% volatility portfolio that oscillates between boom and bust.

## Relationship to risk parity

**Risk parity** is a specific case of volatility targeting. In risk parity, you assign equal contribution to portfolio volatility to each asset class or factor, regardless of their expected returns. A simple example:

- Stocks have realized volatility of 15%.
- Bonds have realized volatility of 5%.
- Gold has realized volatility of 12%.

To give each equal vol contribution to a 10% target portfolio:
- Stocks: 10% / 3 ≈ 3.33% vol contribution → position size = (3.33% / 15%) = 22.2%
- Bonds: 3.33% vol contribution → position size = (3.33% / 5%) = 66.6%
- Gold: 3.33% vol contribution → position size = (3.33% / 12%) = 27.8%

The bond allocation balloons because bonds are calm. Stocks are sized down because they're naturally volatile. This creates a diversified portfolio that doesn't hinge on any one asset's forecast return—pure risk discipline.

Volatility targeting is a broader church: you don't require equal vol contribution. You just maintain your target total volatility by adjusting position sizes proportionally.

## Implementation: the mechanics

### Measurement window
Use a 20–60 day rolling estimate of realized volatility. Longer windows (60 days) smooth out noise; shorter windows (20 days) react faster to regime shifts. The choice is a trade-off between responsiveness and stability. Most practitioners use 20–30 days.

### Scaling frequency
Rebalance to your volatility target daily, weekly, or monthly. Daily rebalancing is theoretically optimal but incurs transaction costs and taxes. Weekly or monthly strikes a balance for most investors. Institutional funds with low frictions often do it daily.

### Leverage constraint
If you're using leverage (borrowed money), there's a hard ceiling. A 15% volatility target applied to a 70/30 stock/bond portfolio requires leverage if real volatility is below 10%. Most retail investors can't use leverage; they cap the scaling factor at 1.0 (no selling below the initial target weights).

### Rebalancing bands
To avoid whipsaws from tiny volatility swings, use bands: only rebalance when current volatility drifts outside a range (e.g., target ± 1 percentage point). This cuts unnecessary trading costs.

## Advantages

1. **Smoother returns**: A 10% volatility target produces steadier, less emotionally draining drawdowns than a standard 60/40 portfolio that swings 12–18%.
2. **Consistent risk budgeting**: You know the portfolio's expected volatility at all times. Risk is predictable.
3. **Behavioral discipline**: The mechanical rule removes emotion. You buy dips and sell rallies automatically through rebalancing, the opposite of panic selling.
4. **Portfolio insurance without hedges**: You achieve some of the risk-reduction benefits of put options through position sizing alone, avoiding the cost and drag of explicit hedges.

## Disadvantages

1. **Whipsaw risk**: If volatility oscillates sharply (spike, then collapse), you'll sell low (when vol spikes) then buy high (when it collapses). This is a form of market timing against yourself.
2. **Compounded drawdown in regime shifts**: If you're scaling down into a prolonged crash, you miss the eventual recovery. A volatility-targeted portfolio that dropped to 50% equities in 2008 would have underperformed a static 60/40 in the 2009 rebound.
3. **Upside cap**: You never run the full leverage that would maximize returns in a low-volatility bull market.
4. **Cost sensitivity**: Transaction costs, bid-ask spreads, and taxes can eat the small edge from mean reversion, especially for retail investors with modest accounts.

## When volatility targeting makes sense

- **Institutional investors with low frictions**: Hedge funds and pension funds with minimal transaction costs can exploit the mean-reversion edge.
- **Portfolios with high-volatility components**: A portfolio of tech stocks and gold, naturally volatile, benefits from size discipline.
- **Risk-averse mandates**: Insurance companies, endowments with low-volatility targets, and conservative portfolios benefit from smoothed returns.
- **Long-term holding periods**: The whipsaw cost is smaller relative to decades of compounding; you capture the behavioral edge.

Volatility targeting is less compelling for:

- **Retail investors with low account sizes**: Transaction costs dominate.
- **Tax-sensitive investors**: Frequent rebalancing triggers capital gains.
- **Strong conviction views**: If you truly believe bonds will outperform in the next year, a mechanical volatility rule works against your thesis.

## See also

<div class="wiki-seealso">

### Closely related

- Volatility — what volatility is and how to measure it
- [Risk parity](/risk-parity/) — equal risk contribution across asset classes
- [Asset allocation](/asset-allocation/) — how to size portfolio weights
- Rebalancing — periodic adjustment of portfolio weights
- [Beta](/beta/) — systematic market risk and its role in sizing
- Hedging — alternatives to volatility targeting for risk control
- [Dynamic asset allocation](/dynamic-asset-allocation/) — broader category of rule-based portfolio adjustment

### Wider context

- [Momentum investing](/momentum-investing/) — trend-following strategy (opposite of volatility targeting's mean reversion)
- Mean reversion — statistical tendency that makes volatility targeting work
- Drawdown — measure of portfolio decline volatility targeting aims to reduce
- [Sharpe ratio](/sharpe-ratio/) — risk-adjusted return metric often optimized by volatility targeting
- Transaction costs — friction that limits volatility targeting's edge for retail

</div>
