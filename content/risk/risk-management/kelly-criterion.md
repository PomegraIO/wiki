---
title: "Kelly Criterion"
description: "A mathematical formula that calculates the optimal fraction of a bankroll to bet on each wager to maximise long-run capital growth."
keywords:
  - Kelly Criterion
  - optimal betting
  - position sizing
  - bankroll management
  - capital growth
  - bet sizing formula
image: "/svg/risk.svg"
---

*The **Kelly Criterion** is a formula that tells you what fraction of your bankroll to stake on each bet, given your win probability and payoff ratio. It is the mathematically optimal bet size for maximising long-run wealth, but it is almost never applied in full—because the optimal amount of risk would make you bankrupt first.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Kelly Criterion — key facts</div>

<img src="/svg/risk.svg" alt="An abstract editorial mark for risk management and capital optimization." />

<div class="wiki-infobox-caption">The formula your edge deserves, but rarely the risk your stomach can bear.</div>

|   |   |
|---|---|
| **What it is** | A formula computing optimal bet fraction = (edge × payoff − 1) / (payoff) |
| **Also called** | Kelly formula, Kelly strategy |
| **Key inputs** | Win probability, loss probability, payoff ratio (win size / loss size) |
| **Typical output** | 10–25% per bet for professional traders; impractically high |
| **In practice** | Usually applied at 0.25–0.5 (quarter Kelly, half Kelly) for tractable drawdowns |
| **First published** | 1956, John Kelly; applied to sports betting and trading since |

</aside>

## The formula and its elegance

The Kelly Criterion is deceptively simple. If you have a bet with probability *p* of winning and probability *q* = 1 − *p* of losing, and the payoff odds are *b*-to-1 (you win *b* dollars for every 1 you lose), the fraction of your bankroll to bet is:

f* = (bp − q) / b = (p(b+1) − 1) / b

For example: you have a coin flip that wins £2 for every £1 staked (2-to-1 odds), and you know it's slightly biased, hitting heads 55% of the time. The Kelly fraction is:

f* = (2 × 0.55 − 0.45) / 2 = 0.65 / 2 = 0.325, or 32.5%

Kelly says bet 32.5% of your bankroll. If you start with £1,000, stake £325. Win, and you have £1,650. Lose, and you have £675. Repeat this forever (with your bankroll recalculated each round), and Kelly's formula guarantees that you grow your wealth faster than any other constant betting fraction.

This is not luck—it is mathematics. The growth rate is proportional to log-wealth, and Kelly maximises the expected value of log-wealth. No other strategy will, on average, turn a long sequence of biased bets into greater final wealth.

## Why it's theoretically perfect and practically insane

The beauty of Kelly is also its curse. The formula tells you to bet large when your edge is large. For a 55% win-rate trade with symmetric payoffs (you win as much as you lose), Kelly recommends betting roughly 10% per position. For a professional trader with a 60% win rate and 2:1 payoff (you win twice as much as you lose), Kelly can recommend 25–30% per trade.

This is catastrophic for the human psyche. If you follow full Kelly, a typical losing streak of five trades in a row means you've lost 35–40% of your bankroll. The next trade you place is 35–40% smaller than the original. The math is still optimal, but the volatility is unbearable. Most traders who try full Kelly do not stay the course; they quit in despair during the inevitable drawdowns.

More practically, any misestimation of your true win rate gets amplified under Kelly. Believe you have a 60% win rate when you actually have 50%, and Kelly tells you to size far too aggressively. By the time you realize the error, the losses are severe. The formula assumes perfect knowledge of your edge, which no trader possesses.

## Fractional Kelly in the real world

Because of this, nearly every professional trader who references Kelly applies a fraction of it—commonly 0.25 Kelly (quarter Kelly) or 0.5 Kelly (half Kelly). If full Kelly says bet 20%, you bet 5% (quarter) or 10% (half) instead. This reduces your long-term growth rate, but it also reduces drawdown volatility. You still benefit from the formula's edge-awareness—betting bigger when the edge is larger—while avoiding the stomach-wrenching swings of full Kelly.

Quarter Kelly is conservative enough to sleep through a losing streak, yet aggressive enough to compound wealth meaningfully if your edge is real. Many successful traders gravitate to this middle ground: the formula guides you, but you don't let it destroy you.

The choice of fractional Kelly is arbitrary—there is no mathematical argument for 0.25 over 0.2 or 0.3. It is a matter of risk preference. A risk-averse trader might use 0.1 Kelly (tenth Kelly). A trader who has tested their edge extensively and trusts their win-rate estimate might venture toward 0.5 Kelly. But full Kelly is nearly universal in practice, a theoretical ideal that is respected but not followed.

## The hidden assumption: independent bets

Kelly assumes that each bet is independent of the previous ones—that your win rate and payoff ratio do not change based on what happened before. In reality, markets are correlated. A trader's edge in normal markets might evaporate in a crash. A strategy that works in trending markets fails in choppy ones. A [short-volatility](/implied-volatility/) position that is mathematically optimal in calm times becomes catastrophic if volatility spikes.

This is the Kelly Criterion's fundamental fragility: it is a formula for a world of stable, repeatable bets. Real trading is a world of regime changes, correlations, and fat tails. When the underlying distribution changes—when an edge turns into a trap—Kelly's formula continues recommending the old, now-wrong bet size.

For this reason, many traders use Kelly as a general guide, not a precise rulebook. If Kelly says 10%, you might bet 5% and adjust dynamically based on recent performance and market regime. You treat the formula with respect but not obedience.

## See also

<div class="wiki-seealso">

### Closely related

- [Position Sizing](/position-sizing/) — the broader discipline of sizing trades, which Kelly optimizes mathematically
- [Risk Budgeting](/risk-budgeting/) — setting portfolio-wide risk limits that constrain Kelly-sized positions
- [Stop-Loss Order](/stop-loss-orders/) — the exit point that determines payoff ratio for a Kelly calculation
- [Value at Risk](/value-at-risk/) — measuring portfolio drawdown risk, which fractional Kelly mitigates
- [Diversification](/diversification/) — spreading bets to reduce correlation, which Kelly assumes is absent

### Wider context

- Probability — the estimated win rate underlying Kelly's formula
- [Overconfidence Bias](/overconfidence-bias/) — the tendency to overestimate edges, leading to Kelly oversizing
- [Leverage Ratio](/leverage-ratio-forex/) — Kelly with borrowed money amplifies both gains and losses
- Expected Value — the expected return Kelly formula seeks to maximise

</div>
