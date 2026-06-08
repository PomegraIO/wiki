---
title: "Perpetual Futures"
description: "A perpetual futures contract with no expiry date that uses periodic funding payments to keep its price tethered to the underlying spot market."
keywords:
  - perpetual futures
  - cryptocurrency futures
  - funding rate
  - no expiry
  - spot-futures basis
image: /svg/derivatives.svg
---

*A **perpetual futures contract** is a derivative with no [expiration date](/expiration-contracts/)—it can theoretically be held forever. Instead of converging to a [spot price](/spot-exchange-rate/) at maturity like a standard [futures contract](/futures-contract/), a perpetual is anchored to the spot market via periodic **funding payments** passed between long and short holders. When the perpetual price drifts above spot, longs pay shorts; when it falls below spot, shorts pay longs. This mechanism keeps the perpetual trading near spot value indefinitely.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Perpetual Futures — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives." />

<div class="wiki-infobox-caption">No expiry, no delivery—just recurring payments to keep price in line with the spot market.</div>

|   |   |
|---|---|
| **What it is** | A [futures-like contract](/futures-contract/) with no maturity date, funded by periodic transfers between holders |
| **Also called** | Perpetuals; perpetual swaps; inverse perpetuals (for shorting) |
| **Where traded** | Cryptocurrency exchanges; some commodity and FX platforms |
| **Funding mechanism** | Every 8 hours (or daily), longs pay shorts if perpetual > spot, or vice versa |
| **Key advantage** | No rollover needed; one contract captures any time horizon |
| **Key risk** | Funding rates can spike in volatile markets; position can be [liquidated](/liquidation/) if collateral drops below [margin](/margin-call-forex/) requirements |

</aside>

## Why perpetuals exist

Standard [futures contracts](/futures-contract/) have an expiration date. A [futures strip](/futures-strip/) locks in prices across multiple expirations. But a trader holding a multi-year view of, say, [Bitcoin](/bitcoin/), must roll contracts forward repeatedly, paying the [contango](/contango/) cost each time, and managing the friction of expirations. A perpetual eliminates this friction: buy once and hold as long as you wish.

Perpetuals emerged in cryptocurrency trading because digital assets are volatile, fast-moving, and the spot market is fragmented across exchanges. Traders wanted leverage without rollover costs. Traditional markets have not widely adopted perpetuals (though some commodity and [forex](/currency-risk/) platforms now offer them) because standard [futures](/futures-contract/) are liquid and efficient, and institutional traders prefer the certainty of delivery dates.

## How funding rates anchor price to spot

The genius of perpetuals is the funding mechanism. Every 8 hours (on most crypto exchanges), the perpetual contract and the spot market are compared. If the perpetual price is above spot—buyers are enthusiastic and willing to pay a premium—the perpetual longs must pay the shorts a small percentage of position value. This is the **funding rate** (typically 0.01–0.05% per 8-hour period, depending on the premium).

Conversely, if the perpetual trades below spot, shorts pay longs. This constant rebalancing incentivises traders to arbitrage. If perps are expensive, arbitrageurs buy spot (cheap) and short perps (expensive), collecting funding while they converge. If perps are cheap, they go long perps and short spot, again profiting from convergence. These arbitrage trades pull the perpetual price back toward spot, usually within minutes.

The funding rate is known in advance (set by the exchange based on recent [basis](/bid-ask-spread/) observation), so traders can calculate the cost or benefit of holding their positions. A high positive funding rate means longs are paying; a negative rate means longs are receiving. Over months, accumulated funding payments can be substantial—worth planning for if you hold a large position.

## Perpetuals for leverage traders

Perpetuals are popular with [leveraged](/leverage-ratio-forex/) traders because they allow outsize bets. A trader might deposit $10,000 of collateral and control $100,000 of notional exposure (10:1 leverage, at exchanges that permit it). If the market moves 10% in their favour, they double their money. If it moves 10% against them, they wipe out—and the position faces [liquidation](/liquidation/).

This is the perpetual's dark side. In a crash, when prices fall rapidly, a leveraged long position loses value fast. If collateral drops below the [maintenance margin](/margin-call-forex/) threshold, the exchange liquidates the position automatically, often at unfavourable prices. In extreme volatility (flash crashes, exchange outages), liquidation cascades can trigger outsized losses. The trader's entire collateral is forfeited.

Liquidations create a feedback loop. When many leveraged traders are liquidated simultaneously, their positions are force-sold, pushing the market down further and triggering more liquidations. This is a genuine systemic risk in cryptocurrency perpetual markets, where leverage is high and regulatory oversight lighter.

## Why perpetuals carry higher risk than spot or forwards

Holding a perpetual is riskier than holding the underlying spot asset for several reasons. First, there is the liquidation risk just described: leverage amplifies gains and losses. Second, there is **funding rate risk**. If you are long and rates turn sharply positive (longs paying shorts), you bleed cash every 8 hours. In a prolonged bullish rally where funding rates stay high, long-term holders accrue large payment liabilities.

Third, there is **basis risk**. Although perpetuals are designed to track spot, in illiquid or extreme markets, the perpetual price can decouple. If an exchange goes offline or faces a [liquidity crisis](/liquidity-risk/), the perpetual may trade at a steep premium or discount to the true spot price, and traders are trapped. The 2022 crypto market stress saw perpetual exchanges face insolvencies and lost customer funds; perpetuals proved less robust than advertised.

Finally, there is **operational risk**. Exchanges hold collateral and manage liquidations. A hacked or mismanaged exchange can seize funds or trigger erroneous liquidations. Decentralized perpetual protocols (smart-contract-based, avoiding a central counterparty) reduce counterparty risk but introduce smart-contract risk and reduced liquidity.

## Perpetuals as a discovery mechanism

From an economist's perspective, perpetuals are fascinating because they reveal spot-futures [basis](/bid-ask-spread/) continuously. The funding rate is a real-time measure of how much the market is willing to pay for leverage or short exposure. High positive funding (longs paying shorts) signals bullish sentiment; negative funding signals bearish sentiment. Traders use funding rates as a contrarian indicator. Extremely high positive funding sometimes precedes a correction; extremely negative funding sometimes precedes a rally.

## Perpetuals in traditional markets

Commodity and currency perpetuals are less common but do exist. A few exchanges offer gold or oil perpetuals with similar mechanics. However, the traditional [futures](/futures-contract/) market is already so liquid and efficient (and rollover costs so manageable via [futures strips](/futures-strip/)) that perpetuals have not gained traction. The main value of perpetuals is in markets where spot is highly fragmented (crypto) or where leverage is a primary draw.

In traditional finance, the closest equivalent is a [total return swap](/equity-financing/), a bespoke over-the-counter agreement where one party pays the other the return on an asset in exchange for a fixed rate. Swaps are perpetual-like in that they can run for years without rollover, but they are privately negotiated and subject to [counterparty risk](/counterparty-risk/).

## See also

<div class="wiki-seealso">

### Closely related

- [Futures Contract](/futures-contract/) — the standard contract with an expiry, which perpetuals are designed to replace
- [Spot Exchange Rate](/spot-exchange-rate/) — the underlying market price that perpetuals track via funding rates
- [Leverage Ratio](/leverage-ratio-forex/) — why perpetuals attract leveraged traders
- [Liquidation](/liquidation/) — the risk event unique to margined perpetual positions
- [Basis Risk](/bid-ask-spread/) — the gap between perpetual and spot that funding rates manage
- [Forward Contract](/forward-contract/) — an over-the-counter alternative for locking in future prices

### Wider context

- [Bitcoin](/bitcoin/) — where perpetuals are most heavily traded
- [Cryptocurrency Exchange](/cryptocurrency-exchange/) — the platforms offering perpetual contracts
- [Counterparty Risk](/counterparty-risk/) — a risk heightened by centralised perpetual exchanges
- [Volatility Smile](/volatility-smile/) — a related concept in options markets about basis and implied volatility

</div>
