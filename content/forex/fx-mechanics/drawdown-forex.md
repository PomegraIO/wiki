---
title: "Drawdown (Forex)"
description: "The peak-to-trough decline in an account value, a risk metric used to measure the maximum loss from a previous high in forex trading and portfolio management."
keywords:
  - drawdown
  - peak-to-trough loss
  - risk metric
  - account equity
  - forex risk
---

*A **drawdown** in forex is the peak-to-trough decline in an [account](/wiki/cash-conversion-cycle/) value, measured from a previous high to the subsequent low. It quantifies the maximum loss a trader experiences from their account's highest point, a critical risk metric for evaluating strategy volatility and managing leverage.*

<aside class="wiki-infobox">

| Metric | Definition |
|--------|-----------|
| Measurement | Percentage decline from account peak to trough |
| Typical ranges | Retail trader: 20%–50%; Hedge fund: 10%–30%; Day trader: 10%–20% |
| Time horizon | Can span hours to years depending on strategy |
| Psychological impact | Major driver of trader abandonment |
| Leverage sensitivity | Higher leverage = wider drawdowns for same trades |
| Recovery requirement | A 50% loss requires 100% gain to recover |
| Margin trigger | Large drawdowns can trigger margin calls |

</aside>

## Measuring drawdown and its components

A drawdown begins when an account reaches a new peak (highest cumulative balance). As the account declines from that peak, the decline is measured continuously. The maximum decline from peak to the lowest subsequent valley is the maximum drawdown (MDD). The drawdown ends when a new peak is reached, establishing a new baseline for the next drawdown cycle.

Drawdown is expressed as a percentage: MDD = (Peak - Trough) / Peak × 100%. An account at \$100,000 (peak) that falls to \$60,000 (trough) has a 40% maximum drawdown. The trader must gain 66.7% on the \$60,000 to recover to the prior peak (\$60,000 × 1.667 = \$100,000). This asymmetry—large percentage gains are needed to recover from large drawdowns—is why managing drawdown is critical.

Running drawdown (or current drawdown) is the decline from the previous peak to the current value. A trader's account at \$100,000 (peak), currently \$75,000 (trough), has a 25% running drawdown. Peak-to-peak return measures the return between successive peaks, capturing complete cycles. These measurements provide different views of risk; peak-to-peak isolates trading performance between recovery periods, while maximum drawdown reveals the worst-case scenario.

## Psychological and operational impacts

Drawdowns are the primary driver of trader attrition. A 20% drawdown is abstract; a 50% drawdown is traumatic. Traders experiencing large drawdowns often abandon strategies, assuming they are flawed, not understanding that volatility is inherent to any trading system. This emotional response leads to "worst possible outcomes"—selling out of positions at the trough, locking in losses, and missing the recovery.

A 50% drawdown also triggers operational constraints. Forex brokers impose [margin requirements](/wiki/margin-trading-crypto/)—typically 1–5% depending on [leverage](/wiki/leverage-ratio-forex/)—meaning a trader must maintain a minimum account percentage above the sum of [margin](/wiki/margin-call-forex/) used by open positions. A trader using 20:1 leverage has a 5% margin requirement. A 50% account decline triggers margin calls; the broker liquidates positions at unfavorable prices to raise cash. A 10:1 leverage (10% margin requirement) offers more cushion.

## Drawdown profiles across trading styles

[Day traders](/wiki/day-trading/) with tight [stop losses](/wiki/stop-order/) often experience 10–20% maximum drawdowns. They exit losing trades quickly and lock in small gains, creating a choppy equity curve. A day trader might experience a 15% drawdown over a month, then recover to new highs within weeks. [Swing traders](/wiki/swing-trading/) holding positions 2–10 days often see 20–35% drawdowns; they give winners room to run, so occasional large losses create larger drawdowns. [Position traders](/wiki/position-trading/) holding weeks to months often experience 30–50% maximum drawdowns; they tolerate wider swings and compound losses during extended losing streaks.

[Carry trade](/wiki/carry-trade/) strategies (selling low-interest currencies, buying high-interest ones) have periods of drawdown, typically during [risk-off](/wiki/risk-on-risk-off/) events when the unwinding of leverage forces sudden position liquidation. The 2008 financial crisis saw AUD/JPY (a popular carry pair) drop 30% in a few weeks, creating catastrophic drawdowns for leveraged carry traders. The 2015 Swiss franc unpegging saw EUR/CHF crash 30% in minutes, wiping out traders with tight [stop-losses](/wiki/stop-limit-order/).

## Relationship to leverage and margin

Leverage amplifies both gains and drawdowns. A trader with 1:1 leverage (fully funded) experiences the same percentage drawdown as the underlying positions. A trader with 10:1 leverage experiences 10x the volatility and 10x the drawdown percentage from the same trading returns. A strategy returning 5% annually with a 20% maximum drawdown becomes a 50% maximum drawdown under 10:1 leverage.

The relationship between [leverage](/wiki/leverage-ratio-forex/) and drawdown is why professional traders limit leverage despite its attraction. A hedge fund with a 2% maximum drawdown target can use approximately 2:1–3:1 leverage; beyond that, drawdowns exceed target even with good trading. A retail trader with no stated drawdown target can use 20:1, 50:1, or higher, leading to frequent margin calls and ruin.

## Drawdown duration and recovery time

Some drawdowns are brief (hours to days); others linger (weeks to months). A trader with a losing streak might experience a 30% drawdown over 2 months, then recover over the next 3 months. The total time in drawdown is 5 months—a significant psychological toll. Longer drawdowns (6+ months) often lead traders to abandon strategies, missing the subsequent recovery.

Recovery time increases with drawdown size. A 10% drawdown requires a 11% gain to recover; a 50% drawdown requires a 100% gain. Even with consistent monthly returns, a 50% drawdown takes years to recover. An account returning 2% monthly gross is very profitable, but if it experiences a 50% drawdown, the recovery takes 18 months of 2% monthly gains. During that recovery period, trader confidence is low, and the temptation to overtrade or abandon the system is high.

## Risk management and drawdown limits

Professional asset managers often set drawdown limits to protect investors and comply with risk frameworks. A hedge fund might have a policy that if the fund drawdown exceeds 20%, it suspends trading until capital is restored. This forces discipline and prevents the compounding of losses. A retail trader might set a daily or monthly stop-loss, such as "if I lose 5% in a day, I stop trading."

[Value at risk](/wiki/value-at-risk/) (VaR) models and [conditional value at risk](/wiki/conditional-value-at-risk/) (CVaR) attempt to quantify potential drawdowns based on historical volatility and [correlation](/wiki/correlation-coefficient/). A trader with a 1% daily [volatility](/wiki/volatility-index-futures/) and 99% confidence might estimate a maximum one-day drawdown of 3%, but such estimates are backward-looking and often fail during regime changes or [flash crashes](/wiki/flash-crash-2010/). [Stress testing](/wiki/stress-testing/) and [scenario analysis](/wiki/scenario-analysis/) are more robust approaches, modeling losses under specific scenarios (China crisis, central-bank policy shock, geopolitical event).

## Monitoring and tracking drawdown

Most forex brokers provide account statements with peak equity and current drawdown; many trading platforms (MetaTrader, ThinkorSwim) calculate and display it in real time. A trader should track maximum drawdown alongside [win rate](/wiki/profit-margin-ratio/), average win size, and average loss size. The [Sharpe ratio](/wiki/sharpe-ratio/) (return per unit of volatility) and [Sortino ratio](/wiki/excess-spread/) (return per unit of downside volatility) are useful normalized risk-adjusted metrics.

Strategic review should occur after significant drawdowns. A trader experiencing a 40% drawdown should audit trades: Were there correlated positions that amplified losses? Was leverage too high? Was the stop-loss too wide? Did the strategy encounter a regime change (central-bank policy shift, geopolitical shock) that violated assumptions? Understanding the source of drawdown guides future improvements.

<div class="wiki-seealso">

### Closely related
- [Drawdown Analysis](/wiki/drawdown-analysis/) — Detailed drawdown measurement and interpretation
- [Value at Risk](/wiki/value-at-risk/) — Probabilistic risk estimation
- [Leverage (Forex)](/wiki/leverage-ratio-forex/) — Amplification effect on gains and losses
- [Margin Call (Forex)](/wiki/margin-call-forex/) — Liquidation trigger from drawdown

### Wider context
- [Risk Management](/wiki/liquidity-risk/) — Broader enterprise risk framework
- [Position Sizing](/wiki/position-limit-regulations/) — Controlling exposure per trade
- [Volatility](/wiki/volatility-smile/) — Source of account fluctuations
- [Forex Trading Basics](/wiki/forex-spread/) — Foundational forex mechanics

</div>
