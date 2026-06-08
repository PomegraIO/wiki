---
title: "Intermediate-Term Momentum Window"
description: "The 12-minus-1 month lookback period that captures the strongest return predictability in cross-sectional momentum strategies."
keywords:
  - momentum investing
  - 12-minus-1 month window
  - cross-sectional momentum
  - time decay momentum
  - price reversal
image: "/svg/strategies.svg"
---

*The **12-minus-1 month momentum window** is a specific time period—the prior 12 months of returns excluding the most recent month—that empirical research has shown delivers the strongest return predictability for [momentum investing](/momentum-crash-risk/) strategies. This lookback period balances the signal of genuine price trends against the short-term microstructure noise and reversals that contaminate shorter intervals.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">12-Minus-1 Month Window — key facts</div>

<img src="/svg/strategies.svg" alt="An abstract editorial mark for investment strategy." />

<div class="wiki-infobox-caption">The Jegadeesh–Titman standard that defined momentum investing practice.</div>

|   |   |
|---|---|
| **What it is** | A lookback period spanning the 12 months prior to each measurement date, excluding the most recent calendar month |
| **Also called** | JT window, canonical momentum window, 12-1 lookback |
| **Returns captured** | Month 2 through month 12 (inclusive) prior returns; month 1 excluded |
| **Key finding** | This window showed 1–2% monthly returns in seminal studies (1990s onward) |
| **Why month 1 excluded** | Recent price movement often reverses; excluding it improves signal-to-noise |
| **Holding period** | Typically 3–12 months; momentum effect persists across horizons |
| **Alternatives tested** | 6-month, 18-month, 24-month windows; 12-1 proved most robust |

</aside>

## Why a 12-month lookback caught academics' attention

When Jegadeesh and Titman published their foundational momentum study in 1993, they tested multiple lookback windows to isolate which time frame best predicted future returns. A 3-month window was too noisy; a 5-year window conflated momentum with value. The 12-month period emerged as an empirical sweet spot. Over decades of subsequent research, it remained the industry standard—not because of theory alone, but because data repeatedly confirmed it worked.

The 12-month span is long enough to reveal true price trends (filtering out random daily noise) yet short enough to avoid mean reversion, where very old price history begins to predict *opposite* future returns. This creates a [term structure](/yield-to-maturity/) of momentum returns: weak predictability at one month, rising sharply from three months onward, peaking around 12 months, then gradually declining for lookback windows of 24 months or longer.

## Why month 1 is excluded

The most recent month must be dropped because price reversals are strongest right after large moves. If you bought yesterday's biggest winners, you often underperformed—a phenomenon called **short-term reversal**. This reversal is believed to reflect order-flow toxicity and microstructure effects: large price moves can trigger selling from [margin calls](/margin-call-forex/), stop-losses, and portfolio rebalancing, which temporarily pushes prices in the "wrong" direction before they recover.

By excluding the most recent month and using months 2–12, momentum strategies capture the true intermediate-term price trend while sidestepping this reversal noise. The evidence is striking: a 12-month window *with* the most recent month included performs noticeably worse than 12-1. This exclusion is not optional; it is mechanical and critical to the strategy's profitability.

## The empirical dominance of 12-1

Studies across multiple asset classes and time periods have validated the 12-1 window. In equities, it generates excess returns that persist even after controlling for risk factors. In commodities and [currency pairs](/canadian-dollar/), similar structures appear—though commodity momentum sometimes peaks at 6 or 10 months instead. This variation by asset class suggests the 12-1 rule is not universal law but rather a strong empirical regularity driven by market microstructure and behavioral frictions specific to stocks.

The persistence of 12-1 dominance is partly puzzling to efficient market theorists. If the pattern were widely known and highly profitable, more capital would exploit it, driving returns toward zero. Yet the strategy has remained profitable in out-of-sample periods even after publication. Hypotheses include: (1) [leverage constraints](/leverage-ratio-forex/) and capital limits prevent full arbitrage; (2) momentum strategies suffer periodic crashes (see [momentum crash risk](/momentum-crash-risk/)), scaring away some capital; (3) the predictability is real but marginal after [management fees](/management-fee/) and transaction costs, so the strategy remains profitable only for low-cost, disciplined practitioners.

## Holding periods: independent of lookback

Once a portfolio is formed using 12-1 ranks, the subsequent holding period is separate from the lookback window. Early studies held positions for one month; later research tested holding periods of 3, 6, 12, and 24 months. A fascinating finding: the momentum premium persists across all holding periods, though it is strongest in the first 3–6 months post-purchase. Practitioners often hold for 3–12 months to balance the magnitude of the return signal against transaction costs and the risk of [momentum crash](/momentum-crash-risk/) reversals.

This separation between lookback and holding period is crucial. A common mistake is conflating them: a "12-month momentum strategy" could mean 12-month lookback with 1-month holding, or 3-month lookback with 12-month holding. The 12-1 momentum effect is specifically about the *lookback*, not the holding period.

## Extensions and variations in practice

Once the 12-1 window was canonized, researchers began testing modifications. Some studies added a **2-3 month skip** between the end of the lookback window and the start of the holding period, to further dampen short-term reversals. Others explored **rank-weighted** momentum (linear score based on the 12-1 returns) rather than simple binary long–short splits. And some practitioners now blend 12-1 with other signals—[earnings surprises](/earnings-quality/), [revenue acceleration](/revenue-growth-investing/), or [factor](/factor-investing/) tilts—to reduce [crash risk](/momentum-crash-risk/).

The core 12-1 window remains the baseline, however. Asset managers launching momentum funds or smart-beta momentum ETFs typically cite it as their foundation, even if they apply refinements. It represents the clearest empirical anchor in an otherwise slippery realm of price-based forecasting.

## See also

<div class="wiki-seealso">

### Closely related

- [Momentum Crash Risk](/momentum-crash-risk/) — how momentum strategies suffer reversals in market recoveries
- [Factor Investing](/factor-investing/) — momentum as a tradeable risk premium
- [Revenue Growth Investing](/revenue-growth-investing/) — alternative signal combining growth and value
- [Market Timing](/market-timing/) — related attempts to predict returns using historical patterns
- [Time Decay (Theta)](/time-decay-theta/) — how time value erodes in option and momentum contexts
- [Sector Rotation](/sector-rotation/) — cyclical selection within or across momentum frameworks
- [Algorithmic Trading](/algorithmic-trading/) — execution of momentum strategies at scale

### Wider context

- [Price Discovery](/price-discovery/) — how prices incorporate information and momentum information
- Behavioral Finance — explains momentum through overreaction and anchoring
- Risk Management — portfolio construction including momentum hedge or tilt
- [Value Investing](/value-investing/) — contrasts with momentum; sometimes called "opposing" returns
- [Volatility Smile](/volatility-smile/) — how option markets price momentum and crash risk

</div>
