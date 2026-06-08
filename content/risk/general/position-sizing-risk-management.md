---
title: "Position Sizing for Risk Management"
description: "Position sizing rules like Kelly criterion, fixed-fractional, and volatility-scaled sizing control per-trade risk exposure. Learn how to apply each method."
keywords:
  - position sizing risk management
  - Kelly criterion position sizing formula
  - fixed-fractional position sizing
  - volatility-scaled position size
  - risk per trade calculation
image: /svg/risk.svg
---

*A **position size** is the number of shares, contracts, or units you buy or short in a single trade. Position sizing for risk management is the practice of adjusting that size based on the trade's expected payoff, the inherent risk, or account volatility, so that no single trade can blow up your portfolio. Three main frameworks—Kelly criterion, fixed-fractional, and volatility-scaled—each balance growth against the risk of ruin.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Position sizing — key facts</div>

<img src="/svg/risk.svg" alt="An abstract editorial mark for risk management." />

<div class="wiki-infobox-caption">Controlling per-trade exposure to prevent catastrophic losses.</div>

|   |   |
|---|---|
| **Core idea** | Smaller position = smaller loss if you're wrong |
| **Kelly criterion** | Maximizes long-term wealth; math-driven; full Kelly is often too aggressive |
| **Fixed-fractional** | Risk a fixed percentage (e.g., 2%) of account per trade; simple, forgiving |
| **Volatility-scaled** | Size inversely to volatility; adapt to current market conditions |
| **Typical risk budget** | 1–3% of account per single trade for prudent traders |
| **Rough rule** | Position size = (Risk ÷ Stop loss distance) in dollars |
| **Account impact** | Larger position = larger drawdowns; smaller position = slower wealth growth |

</aside>

## Why position sizing matters

If you trade without a sizing rule, you're at the mercy of psychology and luck. A big winner pumps your ego and tempts you to oversize the next trade. A loss makes you timid. Over time, the inconsistency destroys returns.

Position sizing removes emotion: it defines exactly how much you risk on each setup, based on what you know (your expected win rate, the distance to your stop-loss, your account size). This discipline prevents any single bad trade from derailing your entire account.

Consider two traders, both with 60% win rates and the same trading logic:
- Trader A sizes carelessly, risking 5% on winners and 10% on losers. A few bad trades wipe her out.
- Trader B risks 2% per trade. He'll survive the same drawdown, recover, and compound over the long run.

The math of compounding heavily favors consistent, smaller risk over sporadic aggression.

## Fixed-fractional position sizing: the simplest rule

Fixed-fractional sizing says: "Risk a fixed percentage of my account on each trade."

**Formula:**
Position size = (Account size × Risk percentage) ÷ Stop-loss distance

**Example:**
- Account size: $100,000
- Risk percentage: 2% per trade
- Stop-loss distance: $5 per share (e.g., you buy at $50; stop at $45)

Position size = ($100,000 × 0.02) ÷ $5 = $2,000 ÷ $5 = **400 shares**

If the trade hits your stop-loss, you lose $2,000 (2% of the account). If it wins by the same distance, you gain $2,000.

**Advantages:**
- Transparent and easy to calculate
- As your account grows, position sizes grow (you can afford larger sizes)
- Removes the temptation to go "all in" on one bet

**Disadvantages:**
- Assumes constant volatility (a volatile stock deserves a smaller position than a stable one)
- Doesn't account for win rate (a high-probability trade and a 50-50 flip get the same risk)

**Common risk percentages:** Prudent traders use 1–3% per trade. Aggressive traders may use 5%. Day traders sometimes use smaller percentages (0.5–1%) because they take many trades. Swing traders and longer-term traders often use 2–3%.

## Kelly criterion: the mathematically optimal fraction

The **Kelly criterion** (or "Kelly formula") is derived from information theory and tells you the long-term wealth-maximizing bet size *if* you know your win rate and payoff ratio.

**Formula:**
f* = (b × p – q) ÷ b

Where:
- f* = the Kelly fraction (what percentage of your bankroll to bet)
- b = the odds you receive (payout / risk, in ratio form)
- p = your estimated win probability
- q = 1 – p (loss probability)

**Example:**
- You believe a trade has a 60% win rate (p = 0.60)
- If you win, you make 1.5× your risk (b = 1.5)
- q = 0.40

f* = (1.5 × 0.60 – 0.40) ÷ 1.5 = (0.90 – 0.40) ÷ 1.5 = 0.50 ÷ 1.5 = **0.333 or 33.3%**

**Interpretation:** Bet 33.3% of your bankroll on each trade to maximize long-run wealth.

**The problem with full Kelly:**
A 33% position size means a loss of 33% of your account on a single bad trade. Even though the math says it's optimal *in the long run*, the volatility is brutal. Most traders can't stomach it emotionally, and estimation errors (getting your win rate or payoff wrong) can wipe you out.

**Fractional Kelly:**
To reduce volatility, traders use a fraction of Kelly: half-Kelly (f* ÷ 2) or quarter-Kelly (f* ÷ 4).

In the example above:
- Full Kelly: 33.3%
- Half-Kelly: 16.7%
- Quarter-Kelly: 8.3%

Half-Kelly is a popular middle ground: it gives up some long-run wealth growth but cuts drawdowns roughly in half.

## Volatility-scaled position sizing: adaptive risk

Volatility-scaled sizing adjusts position size based on current market or instrument volatility. In calm markets, you can size up; in turbulent markets, you size down.

**Formula:**
Position size = Base position ÷ (Current volatility ÷ Average volatility)

Or more simply:
Position size = Inverse of volatility (higher volatility → smaller position)

**Example:**
- You normally risk $2,000 per trade (fixed fractional with a standard volatility baseline)
- Current [implied volatility](/implied-volatility/) for the underlying: 40
- Your average volatility: 25

Position size = $2,000 ÷ (40 ÷ 25) = $2,000 ÷ 1.6 = **$1,250**

You shrink the position because the stock is more volatile now.

**Advantages:**
- Accounts for changing market conditions
- Reduces exposure when risk is highest
- Smoother equity curves (fewer blow-ups in choppy markets)

**Disadvantages:**
- Requires real-time volatility estimates (historical volatility, implied volatility, ATR—each has pros and cons)
- More complex to implement
- Over-optimized if you constantly tweak the volatility input

**Use cases:**
- Swing traders adapting to market regime changes
- Options traders using implied volatility to size trades
- Systematic traders building volatility filters into their algorithms

## Combining approaches: a practical framework

Many traders use a hybrid:

1. **Start with fixed-fractional:** Risk 2% per trade (a simple baseline)
2. **Adjust for win rate:** If you have backtested historical data showing 55% win rate, use a mild Kelly adjustment to find a slightly larger base position
3. **Adjust for volatility:** If the instrument or market is in a high-volatility regime, apply a volatility scaler to reduce the base position

**Example workflow:**
- Account: $200,000
- Base risk: 2% = $4,000 per trade
- Historical win rate: 55%, average payoff ratio: 1.2
- Kelly suggests ~11.7% per trade; using half-Kelly, that's 5.85% → scale up base position to $11,700
- Today's market volatility (VIX): 20; your baseline VIX: 15
- Apply volatility scaler: $11,700 ÷ (20 ÷ 15) = $8,775

Final position size is roughly $8,775 of risk, down from $11,700 because volatility is elevated.

## Risk of ruin and position sizing

All position sizing rules aim to avoid **ruin**—a drawdown so large you can't recover (or don't have the capital to continue). The relationship between position size and ruin risk is exponential: doubling your per-trade risk more than doubles your ruin probability.

A trader risking 5% per trade with a 50% win rate faces meaningful ruin risk (roughly 40% chance over 100 trades). The same trader risking 2% faces under 2% ruin risk.

This is why many successful traders say "position sizing is 90% of the game": it's the lever that separates traders who survive to compound from those who blow up early.

## Common pitfalls

**Bluffing on win rate:** Traders often overestimate their true edge. A trader who is 55% right still faces a drawdown risk if they're 5%-per-trade aggressive. Be conservative on your edge estimate.

**Ignoring correlation:** If you hold multiple positions in correlated assets (all tech stocks, for example), the portfolio risk is higher than the sum of individual risks. Position size needs to account for the diversification (or lack thereof).

**Adjusting mid-trade:** Once you're in a trade, changing your position size based on current price is a form of revenge trading or loss aversion. Stick to your plan.

**Sizing up after wins:** Momentum from a big win often tempts traders to overshoot their sizing rule. The worst trades often follow the best ones. Discipline means sticking to your formula.

## See also

<div class="wiki-seealso">

### Closely related

- Risk management — position sizing as one pillar
- [Kelly criterion](/kelly-criterion/) — the mathematical framework
- [Value at risk](/value-at-risk/) — another way to quantify per-trade and portfolio risk
- Stop-loss — the distance that defines position size math
- Drawdown — the peak-to-trough loss from position sizing errors
- [Volatility](/historical-volatility/) — input to volatility-scaled sizing
- [Implied volatility](/implied-volatility/) — dynamic volatility measure for options traders

### Wider context

- [Risk-weighted assets](/risk-weighted-assets/) — institutional sizing concepts
- [Portfolio diversification](/diversification/) — reduces concentration risk alongside position sizing
- [Margin call](/margin-call-forex/) — the hard boundary when positions are over-sized
- Leverage — the amplifier of position sizing mistakes
- Backtesting — how to validate win rate and payoff assumptions

</div>