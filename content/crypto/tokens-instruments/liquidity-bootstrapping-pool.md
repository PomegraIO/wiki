---
title: "Liquidity Bootstrapping Pool"
description: "How liquidity bootstrapping pools start token launches at high weights and gradually shift them, reducing front-running, price manipulation, and launch volatility."
keywords:
  - liquidity bootstrapping pool
  - lbp token launch
  - initial liquidity protocol
  - fair launch mechanism
  - weighted pool crypto
  - token price discovery
---

*A **liquidity bootstrapping pool (LBP)** is an automated market maker structure that begins with a new token at high weight (often 95%) against a stable asset at low weight (5%), then gradually reverses the ratio over hours or days. This forces early buyers to pay exponential prices for large purchases, preventing whales from capturing cheap tokens while the protocol achieves fair price discovery and raises capital.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">LBP Launch — key facts</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for the crypto topic." />

<div class="wiki-infobox-caption">LBPs replace traditional IDOs by turning the launch mechanism into a price-discovery engine.</div>

|   |   |
|---|---|
| **Starting weight** | New token: 95%, stablecoin: 5% (common) |
| **Ending weight** | New token: 50%, stablecoin: 50% (typical) |
| **Duration** | 24–72 hours (varies by project) |
| **Fee mechanism** | Protocol fee on swaps (0.5–2%), split between liquidity providers and project |
| **Price protection** | Traders pay more for larger sizes due to exponential AMM curve |
| **Capital raised** | Typically $1M–$50M per launch |
| **Risk to buyers** | Rapid price discovery; initial buyers may face losses if price crashes post-launch |

</aside>

## The problem LBPs solve

Traditional token sales—private rounds, ICOs, and IDOs—create artificial scarcity and information asymmetries. Insiders buy at low prices; public buyers either miss allocation or compete in chaotic auctions. The launch price is often arbitrary, set by deal terms rather than market activity. When a token hits exchanges, whales and arbitrageurs rush in, creating extreme volatility. Early momentum chasers suffer 50%+ losses within hours.

Liquidity bootstrapping pools invert this dynamic. Instead of a fixed launch price, the price emerges from continuous trading on an automated curve. Buyers face a hard economic constraint: buying a large amount early is extremely expensive, because the pool's math (the constant product formula, adjusted for weights) forces slippage to spike. This naturally spreads purchases across time and across buyers of different sizes.

## How the mechanism works

A typical LBP starts with the new token at 95% weight and a stablecoin (usually USDC or DAI) at 5% weight. If the pool has 100 tokens and $1 stablecoin initially, the price is roughly $100 per new token, but that is not the real starting price. The actual price is determined by the first trade. Because the pool is so imbalanced, buying even $10 worth of new tokens requires paying a premium; buying $1,000 is exponentially more expensive. This creates a barrier to whales dumping capital on day one.

As the LBP runs, the weight schedule automatically updates—every block or every hour, depending on configuration. The new token weight falls (95% → 80% → 65% → 50%) while the stablecoin weight rises (5% → 20% → 35% → 50%). The pool moves toward balance. As it does, the pricing pressure on large trades decreases. By the end of the 48-hour period, when weights are equal, the pool behaves like a standard 50-50 AMM. Price discovery has flattened out; normal [market-making](/market-maker-trading/) dynamics take over.

The mathematical curve ensures that a buyer's cost per token decreases over time *if they wait*. An early buyer pays premium prices. A patient buyer, arriving on day two when weights are near 75-25, pays less per token. This incentivizes rational actors to spread purchases rather than front-run. For the protocol, it means capital flows in gradually—some raised on day one at high prices, more on day two at lower prices, balancing fairness and fundraising.

## Fee structure and incentives

LBP protocols typically charge a swap fee—often 1% to 2% of each trade's output. A fraction of that (say, 0.5%) goes to liquidity providers (who are earning yield on their staked assets); the remainder goes to the project launching the token. Because trading volume can be high during a launch, the project can raise tens of millions without selling new tokens at a discount. For a 72-hour launch with $10M in total volume and a 1% fee, the project collects $100k in protocol fees.

Some projects sweeten the deal by offering LP rewards on top of fee splits. A user might earn both the AMM's 0.5% fee yield *and* extra governance token incentives for providing liquidity during the LBP. This encourages liquidity providers to front-load capital, ensuring deep liquidity from hour one.

## Price discovery vs. manipulation

The design's core advantage is reducing manipulation. A traditional IDO might have a fixed launch price of $5 per token; when secondary trading opens, coordinated buying pushes it to $20, a 300% pump. FOMO drives retail buyers into a crowded trap. The token then dumps back to $3 as insiders exit, leaving late buyers with 40% losses.

An LBP's gradual weight shift naturally cools this dynamic. Early traders who buy at premium prices get discouraged. Late traders benefit from better prices. The final price is a genuine market consensus, not a cartel outcome. Some tokens have launched via LBP and then *declined* from launch price—a healthy signal that the fair price was lower than anticipated, and that bagholders were not created by launch mechanics.

That said, LBPs are not manipulation-proof. A sufficiently well-capitalized actor could accumulate the stablecoin asset during the LBP and dump it post-launch, crashing price. Community sentiment, product hype, and subsequent revenue still drive long-term valuation. The LBP only controls for the launch phase.

## When LBPs are appropriate

LBPs work best for established teams launching new tokens. A protocol with a working product, live users, and transparent governance can raise capital fairly. The mechanism builds goodwill by distributing tokens across many buyers rather than concentrating them in VCs.

LBPs are less suitable for highly speculative projects with no product or cash flows. In that case, the fair-price-discovery claim rings hollow; the price is fair relative to existing trader sentiment, but sentiment is speculation rather than fundamentals. And because LBPs allow anyone to buy, they can attract retail into speculative traps.

Regulatory scrutiny is lighter for LBPs than for ICOs, since no legal terms or exemptions are required; it is just an on-chain mechanism. But the SEC and other regulators may still scrutinize whether the new token is an unregistered security.

## Comparison to alternatives

Unlike a traditional [ICO](/initial-coin-offering/) or pre-sale, an LBP has no allocation tiers, no minimum buy-ins, and no lock-ups. Anyone with a wallet can participate. Unlike a standard AMM launch (dropping onto Uniswap), an LBP controls the initial price path, reducing flash crashes and manipulation.

A [secondary offering](/secondary-offering/) (a project selling existing tokens to raise funds) is capital-efficient but dilutes holders and is not price-discovery-friendly. An LBP raises capital without the team dumping existing tokens at an arbitrary price.

Some teams combine an LBP with a treasury-backed [yield program](/yield-farming/), using the capital raised plus treasury reserves to offer high APY to early liquidity providers, further incentivizing participation.

## See also

<div class="wiki-seealso">

### Closely related

- Automated market maker — the underlying mechanism LBPs build on
- Constant product formula — the math powering LBP pricing curves
- Token launch strategies — broader context for how new tokens enter markets
- [Initial public offering](/initial-public-offering/) — traditional capital-raising parallel
- [Impermanent loss](/impermanent-loss/) — risk LP face in LBP liquidity positions

### Wider context

- Decentralized finance — LBPs operate within the DeFi ecosystem
- [Smart contract](/smart-contract/) — LBPs are implemented as smart contracts
- [Cryptocurrency exchange](/cryptocurrency-exchange/) — alternative for token launch and trading
- [Price discovery](/price-discovery/) — core mechanism LBPs rely on

</div>
