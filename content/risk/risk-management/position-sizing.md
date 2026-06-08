---
title: "Position Sizing"
description: "The practice of determining how much capital to allocate to a single trade relative to total portfolio capital."
keywords:
  - position sizing
  - trade size
  - portfolio allocation
  - risk management
  - capital allocation
  - portfolio construction
image: "/svg/risk.svg"
---

*[Position sizing](/position-sizing/) is the decision of how many shares, contracts, or dollars to commit to a single trade—a calculation that often matters more than which trade you choose. It sits at the intersection of [risk control](/risk-budgeting/), mathematical optimization, and emotional restraint.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Position Sizing — key facts</div>

<img src="/svg/risk.svg" alt="An abstract editorial mark for risk management and capital allocation." />

<div class="wiki-infobox-caption">The difference between a good idea that survives and a good idea that bankrupts you.</div>

|   |   |
|---|---|
| **What it is** | Allocating a specific percentage of portfolio capital to a single position |
| **Also called** | Trade sizing, capital allocation, exposure management |
| **Key input** | Account size, risk tolerance, estimated probability of loss |
| **Common rules** | 1–2% of portfolio per trade; larger % for higher conviction/tighter stops |
| **Trade-off** | Larger positions mean larger gains but also larger losses |
| **Outcome if ignored** | Overexposure to single bets can wipe out the portfolio in one loss |

</aside>

## Why size matters more than being right

Two traders, both brilliant stock-pickers, make identical trades: both buy the same stock at the same price and both eventually profit. But one allocates 20% of their portfolio to the position while the other allocates 2%. The outcomes diverge not because of insight but because of size. A 50% drop hits the large position catastrophically; the small position is a manageable drawdown.

This is not pedantic math—it's the difference between surviving losses and being wiped out. A trader can be right 60% of the time, make profitable trades on average, and still blow up the account if a single oversized loser hits before the wins compound. This is why position sizing is often called the most important skill in trading, even more so than stock selection. You cannot out-pick your position-sizing errors.

The logic is stark: if you risk more than you can afford to lose on any single trade, you don't need to be wrong very often to lose everything. A portfolio with fifty 2% positions can weather five consecutive losses without fatal damage. A portfolio with five 20% positions is destroyed by one.

## The fixed-percentage rule and its simplicity

The most common discipline is the fixed-percentage rule: allocate a fixed percentage of your portfolio to each new trade, typically 1–2%. You start with £100,000. A 1% rule means each position gets £1,000. A 2% rule means £2,000. This divorces position size from your emotional conviction about the trade.

This has obvious appeal. It is mechanical, fair to each trade, and forces you to pass on ideas that don't fit your account size. If your best idea is a penny stock with a £50,000 position size, a 1% rule tells you it's too large—you'd need £5 million under management for that to comply. This is the system's virtue: it says no to your best, most emotionally compelling ideas when those ideas violate your risk budget.

The drawback is that the fixed percentage is arbitrary. Why 1% and not 0.5%? Why 2% and not 3%? The answer lies partly in statistics. If you make many independent bets, each risking 1–2%, your portfolio volatility stabilizes at a managed level. But if your trades are correlated—they all tank in the same market downturn—even 1% per trade can stack into ruin. The fixed-percentage rule assumes independence, which is often fiction.

## The stakes-based approach: matching size to confidence

A more sophisticated method ties position size to conviction. A trade you're 95% confident in might warrant 2–3% of your portfolio. A marginal idea gets 0.5%. This reflects the intuitive notion that higher-probability bets deserve bigger bets.

But conviction is notoriously unreliable. Traders feel most confident right before they're catastrophically wrong. Overconfidence is a documented bias in both professionals and amateurs. Letting conviction determine size means your largest positions are often your most dangerous ones. Paradoxically, it can amplify losses exactly when you need to play small.

Many disciplined traders sidestep the confidence trap by setting size based on the [stop-loss order](/stop-loss-orders/) and total acceptable loss per trade. You decide in advance: "I will not lose more than 1% of my portfolio on any single trade." If you buy a stock at £100 with a stop at £95, your loss per share is £5. To stay within 1%, you can buy 200 shares (£5 × 200 = £1,000 loss, 1% of a £100,000 account). This inverts the logic: instead of picking a size and accepting whatever loss it produces, you pick an acceptable loss and let it determine size.

## The [Kelly Criterion](/kelly-criterion/) and aggressive optimization

The [Kelly Criterion](/kelly-criterion/) offers a mathematical answer: it calculates the exact fraction of your bankroll to bet given your edge and the odds you face. Oversimplified, it says: bet more when the edge is large and the odds are favorable, bet less (or not at all) when the edge is thin.

For a trader with an estimated 55% win rate, 2:1 payoff ratio (you win twice as much as you lose), the Kelly Criterion recommends a certain percentage per trade. For someone with a 52% win rate and 1:1 odds, it recommends much less. This is mathematically elegant: it maximizes long-run compound returns given your actual win rate and payoff structure.

But Kelly has teeth. It implies large positions (sometimes 10–25% or more per trade) for high-edge opportunities. In practice, this produces gut-wrenching drawdowns. Most professionals use fractional Kelly—half Kelly, quarter Kelly—to reduce volatility and sleep at night. A trader might apply 0.25 × Kelly to size, which is much more conservative but still adapts to edge.

Kelly also requires that you know your true win rate and payoff ratio, which is harder than it sounds. Overestimate your edge, and Kelly tells you to oversize. Underestimate, and you're playing too small. Many traders find the formula philosophically elegant but practically treacherous.

## Sector, correlation, and hidden leverage

Position sizing is also about portfolio construction, not just individual trades. If you own 10 technology stocks, each sized at 2%, you've effectively created a 20% technology position. If the sector crashes, that 20% loss is not mitigated by your disciplined 2% rule on each trade.

Institutional portfolios manage this through [sector limits](/sector-rotation/) and correlation overlays: a position in Apple might be sized smaller if you already own Microsoft, because the correlation between them is high. This is especially true in [hedge fund](/hedge-fund/) portfolios, where the manager is often trying to isolate specific risk factors.

For retail traders, the simpler rule is awareness. If you own three 2% positions in highly correlated assets, you effectively own a 6% position in that risk factor. You size the next trade accordingly.

## See also

<div class="wiki-seealso">

### Closely related

- [Kelly Criterion](/kelly-criterion/) — mathematical optimization of position size given your win rate and payoff
- [Stop-Loss Order](/stop-loss-orders/) — the exit price that determines your maximum loss per trade
- [Risk Budgeting](/risk-budgeting/) — setting total portfolio risk limits that constrain individual position sizes
- [Diversification](/diversification/) — spreading capital across uncorrelated assets to reduce single-position impact
- [Asset Allocation](/asset-allocation/) — the strategic division of capital across classes, informing position-level decisions

### Wider context

- [Leverage Ratio](/leverage-ratio-forex/) — taking borrowed money to size positions beyond available capital
- [Margin Call](/margin-call-forex/) — the forced liquidation when leveraged positions move against you
- [Volatility](/historical-volatility/) — the price swings that make position size critical to survival
- [Hedge Fund](/hedge-fund/) — institutional application of position sizing within diversified strategies

</div>
