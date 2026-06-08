---
title: "Volatility Targeting"
description: "A dynamic position-sizing technique that adjusts portfolio leverage to maintain constant realized volatility over time."
keywords:
  - volatility targeting
  - risk management
  - leverage adjustment
  - portfolio scaling
  - dynamic hedging
image: "/svg/strategies.svg"
---

*A **volatility targeting** strategy scales position sizes up or down to keep a portfolio's realized risk—measured as price swings—constant throughout changing market conditions. When markets turn turbulent and volatility rises, the fund shrinks its holdings; when calm returns, it re-leverages. The goal is steady, predictable risk regardless of external market chaos.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Volatility Targeting — key facts</div>

<img src="/svg/strategies.svg" alt="An abstract editorial mark for trading strategies." />

<div class="wiki-infobox-caption">Adjust size dynamically so the portfolio always shakes the same amount.</div>

|   |   |
|---|---|
| **What it is** | A rules-based approach that increases leverage during low-volatility periods and reduces it during high-volatility periods |
| **Goal** | Maintain a constant level of realized volatility (portfolio standard deviation) |
| **Typical target volatility** | 10–12% annualized; chosen before implementation |
| **Mechanism** | Calculate recent realized volatility; adjust notional exposure to hit the target |
| **Key benefit** | More predictable drawdowns and smoother equity curves; better risk control than fixed leverage |
| **Main drawback** | Can amplify losses if volatility spikes suddenly before positions are scaled down |
| **Common pairing** | Often combined with [trend-following](/trend-following-strategy/) or [algorithmic trading](/algorithmic-trading/) systems |

</aside>

## The volatility-targeting principle

Fixed-leverage portfolios live or die by market conditions. A fund running 2× leverage in a 10% volatility regime experiences 20% portfolio swings; if volatility doubles to 20%, those swings double again to 40%. An investor expecting steady risk instead gets whipsaw. Volatility targeting inverts this problem: the fund commits to maintaining, say, 12% annualized volatility regardless of how turbulent the underlying market becomes. When market volatility climbs, the fund cuts its leverage and shrinks positions. When volatility drops, it levers back up.

The mechanics are straightforward. The fund calculates rolling realized volatility—typically the standard deviation of daily or weekly returns over the past 20–60 trading days. It then compares this to the target level. If realized volatility is 20% but the target is 12%, the fund scales down position sizes so that the same market moves produce proportionally smaller portfolio returns. Mathematically, the scaling factor is the target divided by actual volatility: if actual is 20% and target is 12%, multiply all positions by 12/20 = 0.6. Conversely, if realized volatility falls to 8%, scale up by 12/8 = 1.5.

## Why volatility targeting appeals to investors

Investors care about drawdowns and recovery time more than they care about absolute returns. A strategy that averages 8% per year with 8% volatility and shallow 5% drawdowns is often preferred to one delivering 15% per year with 20% volatility and 40% peak-to-trough declines. Volatility targeting delivers the first profile: by maintaining constant realized risk, it produces smoother equity curves and more predictable drawdowns. This matters to pension funds and insurance companies that must communicate performance to boards and regulators; a steady 12% volatility fund is easier to explain and defend than a fund whose volatility range spans 5% to 35%.

The approach also equalizes capital utility. In low-volatility regimes like 2017, a fixed-leverage fund earns large returns on its invested capital. But much of that leverage is unnecessary—the market isn't moving enough to require it. A volatility-targeting fund uses excess capital to reduce fees or redeploy to new strategies, ensuring that every dollar of capital is bearing proportional risk.

## Practical construction

Most volatility-targeting implementations use exponential weighting to calculate recent volatility—recent days count more heavily than old ones. This ensures the fund reacts quickly to market regime shifts. Some funds recalculate and rebalance daily; others weekly or monthly. More frequent rebalancing tracks volatility swings more precisely but incurs higher transaction costs. The optimal frequency depends on the portfolio's size and the costs of trading its holdings.

The target volatility itself is a strategic choice set before launch. A fund targeting 10% volatility will feel significantly calmer than one targeting 20%. Institutions often choose targets aligned with their risk appetite: conservative funds target 8–10%, balanced funds target 12–15%, and aggressive allocations might target 20% or more. The target is typically held constant, though sophisticated managers occasionally adjust it based on macroeconomic regime or forward-looking market assessment.

## The convexity problem and volatility spikes

Volatility targeting has a well-known Achilles heel: sudden, sharp volatility spikes. If the market gaps down 10% in a single day, realized volatility explodes immediately. The fund must cut leverage fast to comply with its target. But if the market has already moved 10%, selling into that decline locks in losses. This is a form of negative convexity: the strategy is short volatility in a mathematical sense.

The February 2018 volatility event exposed this clearly. Funds employing volatility targeting faced a cruel choice: wait for volatility measures to normalize (and experience much larger than normal drawdowns), or cut positions quickly (and sell at the worst time). Many did both, trimming positions at the peak of panic. Systemically, if many funds are volatility targeting, they all try to cut at once, amplifying volatility further and creating feedback loops.

Managers mitigate this risk in several ways: using volatility forecasts rather than just realized volatility (to anticipate spikes); implementing gradual rather than instantaneous position adjustments; or accepting temporary target violations during crisis periods. None is perfect. The underlying tension—that volatility targeting is mechanically adversarial to large, sudden moves—remains.

## Volatility targeting with trend following

Volatility targeting and [trend-following strategies](/trend-following-strategy/) are often married. Trend following generates directional returns; volatility targeting controls the magnitude. A 12%-volatility trend-following fund might enter a strong uptrend during low-volatility markets with heavy leverage, capturing outsized gains. As volatility rises (perhaps due to profit-taking or macro uncertainty), the fund scales back, protecting against a correction. This pairing has proven effective for managed futures funds and systematic hedge funds because it combines signal quality with risk control.

## Alternatives and trade-offs

Not all systematic managers volatility target. Some prefer fixed leverage for simplicity and to avoid frequent rebalancing costs. Others use [value-at-risk](/value-at-risk/) or expected shortfall (tail risk) targets instead, focusing on downside extremes rather than average volatility. A few employ dynamic hedging or option strategies to cap risk. Volatility targeting remains popular, though, because it is transparent, computationally simple, and—outside of crisis moments—produces the promised behavior.

For long-term investors, the key trade-off is accepting whipsaws during volatility shocks in exchange for steadier risk and easier risk communication at other times. For systematic investors and hedge funds with frequent rebalancing and risk-sensitive mandates, volatility targeting is nearly standard. Understanding its mechanics and failure modes is essential for anyone investing in or running systematic strategies.

## See also

<div class="wiki-seealso">

### Closely related

- Volatility — the measure being targeted and managed
- [Trend-following strategy](/trend-following-strategy/) — often paired with volatility targeting
- [Algorithmic trading](/algorithmic-trading/) — the operational execution method
- Risk management — the broader discipline encompassing volatility targeting
- [Value-at-risk](/value-at-risk/) — an alternative risk metric and targeting approach

### Wider context

- [Leverage ratio](/leverage-ratio-forex/) — positions are scaled by adjusting leverage
- [Hedge fund](/hedge-fund/) — the investor type most likely to use volatility targeting
- [Factor investing](/factor-investing/) — volatility targeting often applied to factor strategies
- [Diversification](/diversification/) — volatility targeting helps maintain portfolio balance
- [Market volatility](/historical-volatility/) — the underlying phenomenon being managed

</div>
