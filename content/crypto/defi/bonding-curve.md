---
title: "Bonding Curve"
description: "A mathematical function that continuously prices token issuance and redemption based on total supply, replacing order-book matching with automated pricing."
keywords:
  - bonding curve
  - automated pricing
  - token issuance
  - continuous token model
  - mathematical pricing
  - amm pricing
image: "/svg/crypto.svg"
---

*A **bonding curve** is a deterministic mathematical function that relates a token's price to its circulating supply. Instead of relying on an order book or discrete trading events, bonding curves allow anyone to buy newly issued tokens directly from the protocol at a price determined by the curve, and sell tokens back to the protocol at a redemption price. The curve's shape determines the price elasticity: linear curves have constant per-token price, quadratic curves see price accelerate with supply growth, and more exotic curves create different incentive structures for early adopters.*

<div class="wiki-hatnote">

For the general AMM framework, see [Market maker trading](/market-maker-trading/). For liquidity-bootstrap mechanisms, see [Liquidity mining](/liquidity-mining/).

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Bonding Curve — key facts</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for automated token pricing and continuous issuance." />

<div class="wiki-infobox-caption">Bonding curves replace discrete trades with a continuous price function, eliminating order-book friction.</div>

|   |   |
|---|---|
| **What it is** | Mathematical supply-to-price function for continuous token buying and selling |
| **Common shapes** | Linear, quadratic (power law), exponential, or sigmoid (S-curve) |
| **Pricing mechanism** | Buyers pay increasing price as supply rises; sellers receive decreasing price as they exit |
| **No counterparty** | Traders buy from and sell to the protocol's smart contract, not other traders |
| **Use cases** | Token launches, DeFi protocol governance tokens, bonding in decentralized autonomous orgs |
| **Advantage** | Automatic price discovery, no slippage from thin order books, early-buyer incentive |
| **Disadvantage** | Early buyers hold all the risk if adoption stalls; illiquidity relative to order-book DEXs |
| **Governance integration** | Often paired with [liquidity mining](/liquidity-mining/) or [revenue model](/defi-revenue-model/) fee switches |

</aside>

## The continuous pricing problem

Traditional order books work well at scale: millions of users, competing bids and asks, tight spreads. But in early-stage projects—a new DEX, a startup DAO, or a niche token—there often aren't enough traders to fill an order book. Buyers see empty bids, sellers see empty asks, and the market freezes.

A bonding curve solves this by eliminating the need for counterparties. The protocol itself is the market maker: it always quotes a price and executes trades immediately. The price is determined solely by the formula and the total supply—no human or algorithm needs to input prices.

## How bonding curves work mathematically

The simplest example is a **linear bonding curve**: 

Price per token = initial price + (supply multiplier × current supply)

If you want to buy 1 token when supply is 100 and the curve is price = 1 + 0.01 × supply, you'd pay 1 + 1 = 2 USD. The next buyer faces price = 1 + 0.01 × 101 ≈ 2.01 USD. This creates a natural disincentive to large purchases (slippage accumulates) and incentivises early adoption: the first buyer gets the cheapest entry.

**Quadratic curves** raise the supply term to a power, accelerating price growth:

Price per token = supply^2

This curve is steeper: early buyers hold an asymmetrically large advantage because price growth compounds. Such curves reward earliest participants heavily—useful for bootstrap phases—but can feel exploitative to later entrants.

Other curves include exponential (price = e^supply), sigmoid (S-shaped, slow at first then fast), and piecewise functions that change shape as supply milestones are hit.

## Redemption and arbitrage mechanics

Most bonding curves allow sellers to redeem tokens back to the protocol. A seller typically receives a price slightly below the current buy price, creating a bid-ask spread. If the buy price is supply + 1, the sell price might be 0.95 × (supply + 1), giving the protocol a 5% haircut.

This spread is often the protocol's revenue; alternatively, it goes to a treasury or is burned (reducing supply and backing the price).

Arbitrage limits curve abuse: if the buy price on the curve diverges significantly from external market price (e.g., an exchange trading the same token), traders will buy cheap on the curve and sell on the exchange, pulling price back into alignment. Sophisticated bonding curves integrate external price feeds or oracles to avoid becoming stale.

## Adoption in DAOs and protocol launches

Bonding curves gained prominence in decentralized autonomous organisations (DAOs) and early-stage DeFi protocols. Projects like Bancor (2017) and later Curved used bonding curves to issue governance tokens continuously, replacing discrete ICO or airdrop events with ongoing token sales.

The appeal: early backers who believed in the vision could buy tokens directly, and their entry price reflected their timing risk. No centralized allocation, no pre-sale valuation games. As the project gained adoption and supply grew, later buyers paid higher prices but benefited from a mature protocol and community.

However, early adopters often dump tokens after the hype period, and bonding curves don't prevent this—price collapses are painful and automatic, punishing believers who held.

## Why bonding curves haven't become default for DEXs

Despite their elegance, bonding curves didn't displace order-book DEXs at scale. Several reasons:

1. **Slippage at size**: On a bonding curve, a 1 million USD trade on a 10 million USD supply experiences significant slippage. Order books with enough depth distribute that trade across many price levels, reducing slippage.

2. **Liquidity pools vs. curves**: [Automated market makers](/market-maker-trading/) (AMMs) like Uniswap discovered that pooling liquidity from many LPs generated much deeper markets than single bonding curves. Liquidity providers earn fees, incentivising them to add capital.

3. **Coordination problems**: Order books and AMMs benefit from network effects—all traders flock to the deepest venue. A bonding curve is isolated; to trade token X via bonding curve, you must transact with that token's specific protocol.

4. **Miner extractable value (MEV)**: Bonding curves with static formulas are predictable, allowing traders to front-run large purchases if the transaction takes time to settle.

## Bonding curves in DeFi today

Modern DeFi rarely uses pure bonding curves for trading. But they appear in niche roles:

- **Token launches**: Some protocols still use bonding curves for the initial issuance phase, then transition to AMMs or order books as volume scales.
- **Bonded staking**: Protocols like Cosmos chains use curves to price staking rewards—the more you stake, the lower the per-unit APY, discouraging concentration.
- **Fractional reserve tokens**: Some stablecoin designs use bonding curves to price treasury-backed redemptions.
- **Creator tokens and social finance**: Platforms like Rally or Mirror use bonding curves to price creator or synthetic-asset tokens, leveraging the curve's price-incentive properties.

## The rise of dynamic bonding curves

Recent innovations include **dynamic bonding curves** that adjust shape based on market conditions. If volume spikes, the curve flattens (reducing slippage); if volume drains, it steepens (protecting the treasury). These require oracle input and are more complex, but they balance accessibility and incentives better than static curves.

Some protocols combine bonding curves with fee mechanisms: buyers pay a tax (10–20%), and sellers receive a redemption rate slightly below fair value. The gap is allocated to insurance, treasury, or burned, creating a self-sustaining ecosystem.

## The future role of bonding curves

Bonding curves peaked in hype around 2018–2019, fell out of fashion as AMMs proved superior for trading volume, and are now a specialist tool: useful for specific use cases (DAO governance issuance, bonded staking, fractional protocols) but not a replacement for order books or AMMs in general trading.

Their strongest remaining property is pedagogical and philosophical: they make price discovery automatic and transparent, with no central gatekeeper deciding valuation. For communities that value that principle, bonding curves remain an elegant, if inefficient, mechanism.

## See also

<div class="wiki-seealso">

### Closely related

- [Market maker trading](/market-maker-trading/) — the order-book and AMM mechanics that compete with bonding curves
- [Liquidity mining](/liquidity-mining/) — often paired with bonding curves to bootstrap token value
- [DeFi Revenue Model](/defi-revenue-model/) — how bonding curve spreads fund protocol development
- [Perpetual Protocol (DeFi)](/perpetual-protocol-defi/) — uses AMM-style pricing rather than bonding curves
- Decentralized Finance — the ecosystem in which bonding curves function
- [Cryptocurrency exchange](/cryptocurrency-exchange/) — the trading venues that bonding curves serve

### Wider context

- [Distributed ledger](/distributed-ledger/) — blockchain infrastructure executing bonding-curve transactions
- [Smart contracts](/blockchain-fundamentals/) — the code layer implementing curve mathematics
- [Price discovery](/price-discovery/) — the economic mechanism underlying bonding-curve pricing
- [Governance tokens](/dividend/) — commonly issued via bonding curves in DAOs

</div>
