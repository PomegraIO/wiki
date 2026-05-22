---
title: "Margin Call (Forex)"
description: "Forced liquidation trigger when forex margin falls below the minimum required by the broker."
keywords:
  - margin call
  - forex leverage
  - margin requirement
  - liquidation
  - forex risk management
---

*A **margin call** in foreign exchange occurs when the equity in your trading account falls below the broker's minimum margin requirement. At that point, the broker is entitled to forcibly close (liquidate) your open positions to bring the account back into compliance. Margin calls are the enforcement mechanism that keeps [leveraged forex](/wiki/forex-leverage/) trading from blowing up entirely—but they also can turn small losses into total wipeouts.*

<div class="wiki-hatnote">
For the related concept in stock trading, see <a href="/wiki/margin-call-forex/">/wiki/margin-call-forex/</a>.
</div>

<aside class="wiki-infobox">

| Concept | Detail |
|---------|--------|
| **Margin Requirement** | 1% to 20% of position value (varies by broker, pair, regulation) |
| **Leverage** | 100:1 at 1% margin (50:1 at 2%, etc.) |
| **Trigger** | Equity falls below required margin |
| **Liquidation** | Broker closes positions (usually at market) |
| **Speed** | Immediate; no notice |
| **Slippage** | Often happens at unfavorable prices during crises |

</aside>

## How forex margin accounts work

When you open a [forex trading](/wiki/day-trading/) account, the broker requires you to deposit a margin amount—say, 1% or 2% of the total notional value of your intended trades. This margin is collateral, not the full purchase price. If you have $10,000 in your account and the broker requires 1% margin per position, you can control $1 million in notional forex exposure. This is leverage—you control 100 times your capital. As long as your open positions remain profitable (or losses stay small), you maintain equity above the minimum margin, and the broker is happy. But if losses accumulate, your equity (account balance minus losses) shrinks.

## The arithmetic of margin calls

Suppose you start with $10,000, buy 1 million units of EUR/USD at 1.10 (notional value $1.1 million), and the broker requires 1% margin. You are using $11,000 of margin—more than your account, which is impossible. Realistically, you would control less notional value. Let's say you control $100,000 notional (100:1 leverage); this requires $1,000 margin. Your account starts at $10,000; used margin is $1,000; free margin is $9,000. Now, if EUR/USD falls from 1.10 to 1.09, you are down $1,000 (100,000 × 0.01). Your account equity is now $9,000 ($10,000 loss). If the broker's margin requirement is 1%, you need $1,000 margin. You still have $8,000 free margin; no call yet.

But if EUR/USD falls to 1.08, you are down $2,000. Account equity is $8,000. Still above $1,000 margin requirement, though thinning. If EUR/USD falls to 1.00, you are down $10,000. Your account equity is $0. You have a [margin call](/wiki/margin-call-forex/). The broker liquidates your position at market (EUR/USD is 1.00) to recover the $1,000 margin. You are left with nothing. Leverage amplifies both gains and losses; a 10% move in the underlying wipes out 100% of your margin in this scenario.

## Broker-dependent margin levels

Different brokers set different margin requirements. Retail forex brokers (under US regulation) must offer at least 50:1 leverage (2% margin requirement) on major pairs, though some offer lower margins on exotic pairs. Institutional brokers may offer 100:1 or higher. Regulatory changes have tightened requirements in recent years. During the COVID-19 crash in March 2020, some brokers did not have capital to cover losses and failed. Survivors raised margin requirements mid-crisis to protect their own capital. This is a hidden risk: margin requirements can change, and tighter requirements can trigger cascading liquidations.

## Timing and slippage

A crucial risk during margin calls is [slippage](/wiki/slippage/): the difference between the price you expected and the price at which you are actually liquidated. During a calm market, selling your position at market is straightforward. But during a crisis or a [flash crash](/wiki/flash-crash-crypto/), when volatility spikes and [liquidity](/wiki/intraday-liquidity/) evaporates, the broker may liquidate at prices far worse than the current quote. In the March 2020 COVID crash, some forex pairs experienced extreme slippage. A trader holding a large position might get liquidated at a price 5% or 10% worse than the last trade, turning a manageable loss into a catastrophic one.

## Cascading margin calls in crisis

During systemic crises (Lehman bankruptcy, COVID crash, 2022 UK bond crash), margin calls can cascade. One large trader's forced liquidation moves prices, triggering margin calls for others. Those liquidations move prices further, triggering more calls. In extreme cases, the market can move so sharply that brokers cannot liquidate fast enough, leaving them with losses on unsettled positions. This is a [systemic risk](/wiki/systemic-risk/) mechanism: leveraged traders amplify volatility, which triggers more forced selling, which amplifies volatility further. The 2008 housing crisis and the 2020 COVID crash both had episodes of this dynamic, particularly in [commodity futures](/wiki/commodity-futures-rolling/) and [repo markets](/wiki/repurchase-agreement/).

## Stop-loss and risk management

Professional forex traders use [stop-loss orders](/wiki/stop-order/) to exit automatically at a predefined price, avoiding the tail risk of a margin call. A trader might buy EUR/USD at 1.10 and set a stop at 1.08, limiting losses to 2%. If EUR/USD hits 1.08, the position is sold automatically. This prevents the leverage from compounding losses. However, stop-losses are not guaranteed; during a gap or flash crash, the stop may not execute at the specified price. Moreover, a stop-loss that is too tight (1.09) may be triggered by normal intraday noise, closing a fundamentally sound position early.

## Margin requirements and position sizing

The only reliable hedge against margin calls is prudent [position sizing](/wiki/position-limit-regulations/). If you have $10,000, do not assume you can control $1 million notional. Account for the margin requirement, for potential slippage, and for the fact that rates can move sharply in minutes. A rule of thumb: risk no more than 1–2% of your account per trade. If you have $10,000 and you are willing to lose $100 on a trade, you can control about $10,000 notional (assuming a 1% price move trigger). This conservative sizing means you can survive multiple losses before a margin call.

## Regulatory changes post-2008

After the financial crisis, regulators tightened leverage limits in retail forex in many jurisdictions. The US [CFTC](/wiki/cftc-regulator/) imposed a 50:1 limit for major currency pairs (2% minimum margin). The EU went further: the ESMA imposed a 30:1 limit (3.3% margin) and even tighter limits for exotic pairs. These changes were motivated by investor protection—high leverage was seen as inducing excessive risk-taking. But they also reduced profitability for retail traders and shifted trading volume offshore to less-regulated jurisdictions.

<div class="wiki-seealso">

### Closely related
- [Forex leverage](/wiki/forex-leverage/) — use of borrowed capital to control larger positions
- [Forex margin](/wiki/forex-margin/) — collateral required to hold positions
- [Stop order](/wiki/stop-order/) — automated exit mechanism to avoid margin calls
- [Slippage](/wiki/slippage/) — actual execution price differs from expected price

### Wider context
- [Leverage ratio forex](/wiki/leverage-ratio-forex/) — measure of position size relative to capital
- [Counterparty risk](/wiki/counterparty-risk/) — broker's risk of inability to liquidate positions
- [Systemic risk](/wiki/systemic-risk/) — cascading margin calls during crises
- [Flash crash 2010](/wiki/flash-crash-2010/) — example of rapid liquidations and slippage

</div>
