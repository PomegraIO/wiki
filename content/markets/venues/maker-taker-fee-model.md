---
title: "Maker-Taker Fee Model"
description: "Exchange fee structures that charge less for orders that add liquidity (makers) and more for those that remove it (takers); incentivizes or discourages participation."
keywords:
  - maker-taker fees
  - exchange fees
  - liquidity rebates
  - market microstructure
  - trading costs
---

*A **maker-taker fee model** is an exchange fee structure in which traders who provide liquidity (makers) receive a rebate or pay lower fees, while traders who remove liquidity (takers) pay higher fees. The structure inverts the traditional model where market makers received rebates and everyone else paid; now, any trader adding an order to the book can earn a rebate. The model is designed to incentivize [liquidity provision](/wiki/liquidity-provider/) and narrow [spreads](/wiki/bid-ask-spread/), though critics argue it has created perverse incentives and fragmented markets.*

<aside class="wiki-infobox">

| Aspect | Detail |
|--------|--------|
| **Maker rebate** | −$0.001 to −$0.003 per share (negative = rebate paid to order placer) |
| **Taker fee** | +$0.002 to +$0.004 per share (positive = fee paid by order placer) |
| **Net exchange revenue** | Maker rebate + Taker fee; often net positive |
| **Historical shift** | Emerged in early 2000s; majority of U.S. equities exchanges now use it |
| **Market impact** | Encouraged algorithmic market-making; increased order flow competition |
| **Unintended effects** | Layering, quote stuffing, predatory order placement strategies |
| **Regulatory scrutiny** | SEC limits rebate size; some proposals to ban entirely |

</aside>

## The structure: maker and taker defined

A **maker** is a trader whose order sits on the [order book](/wiki/order-book-depth/) and is filled later by another trader's incoming order. Example:

- Trader A bids $100.00 for 100 shares of XYZ
- Order sits on the book waiting
- Trader B sells 100 shares at $100.00 → Trader A's bid is filled
- **Trader A is the maker** (provided liquidity)
- **Trader B is the taker** (removed liquidity)

A **taker** is a trader whose order is filled immediately against an existing order on the book. Takers execute market orders or limit orders that cross the spread.

## Fee schedule example

A typical U.S. equity exchange (e.g., NASDAQ, NYSE Arca):

| Maker rebate | −$0.002/share |
| Taker fee | +$0.003/share |

A trader buying 10,000 shares:
- **As a maker** (placing a bid that sits, then gets filled): Receives $0.002 × 10,000 = $20 rebate
- **As a taker** (sending a market buy order): Pays $0.003 × 10,000 = $30 fee

Net spread: The maker gets paid; the taker pays. The exchange nets +$0.001/share on the round-trip.

Pricing is often volume-tiered: high-volume traders get better rebates or lower fees (e.g., −$0.004 rebate for 500M+ monthly shares traded).

## The rationale: liquidity encouragement

Before the maker-taker model (in the 1990s), stock exchanges charged a single flat fee to all traders, and market makers (specialized firms) received separate rebates to encourage them to maintain continuous bid-ask quotes.

The maker-taker model generalized this: *any* trader can be a liquidity provider and earn a rebate. This incentivized:

- **High-frequency trading firms**: To place orders rapidly and earn rebates by providing microsecond-duration liquidity
- **Passive investors**: Large traders could earn rebates by using limit orders instead of market orders
- **Wider use of limit order books**: Orders stayed on the book longer, creating depth

The claim was that narrower spreads and deeper order books would benefit all traders. And indeed, [bid-ask spreads](/wiki/bid-ask-spread/) compressed significantly in the 2000s–2010s; large-cap stocks that once traded with $0.10 spreads now trade with $0.01 spreads.

## Criticism: Perverse incentives

Critics argue the model created problems:

### Layering and quote stuffing

Market makers place hundreds of orders (many meant to be canceled) to earn rebates, then cancel them when adverse orders appear. The goal is to:
1. Earn rebate on orders placed
2. Cancel orders if they'd lose money
3. Net profit from rebates despite not facilitating actual trades

This "layering" or "[quote stuffing](/wiki/quote-stuffing/)" overloads the system with spurious orders, increasing latency and creating execution confusion.

### Predatory order placement

High-frequency traders use maker-taker rebates to subsidize predatory strategies:
- Place orders to "probe" the order book
- Cancel orders immediately if they'd cross with aggressive order flow
- Earn rebates anyway
- Use the information gathered to front-run slower traders

### Market fragmentation

Maker-taker models incentivized the creation of new exchanges (NYSE Arca, CBOE BZX, NASDAQ PSX) to compete on rebates. Liquidity fragmented across dozens of venues, raising search costs for traders and increasing latency.

### Rebate arms race

Exchanges competing for order flow increased rebates over time. In the late 2010s, some venues offered −$0.004 or higher rebates, subsidizing high-frequency trading while ordinary investors subsidized these subsidies through higher taker fees.

## Impact on different trader types

**High-frequency traders**: Benefit enormously. Rebates can account for 20–40% of HFT profits. Without them, many strategies would be unprofitable.

**Large institutional investors**: Mixed. They earn rebates on large limit orders but pay taker fees on market orders. Savvy institutional traders use tactics (iceberg orders, VWAP algorithms) to minimize taker fees.

**Retail traders**: Disadvantaged. Retail traders typically use market orders (taker side), paying the full fee. They rarely earn rebates.

**Passive index funds**: Slightly disadvantaged. When rebalancing or faced with inflows, index funds often use market orders (taker), incurring fees.

## Regulatory scrutiny

The SEC has expressed concerns:

- **Rebate caps**: The SEC has capped maker rebates at $0.003/share in some rulings, limiting exchange ability to subsidize high-frequency traders indefinitely.

- **Anti-fraud concerns**: The SEC has brought cases against exchanges for disclosing inadequate information about rebate structures, arguing that non-transparent rebate practices constitute fraud.

- **Fragmentation**: Critics argue the fragmentation caused by maker-taker competition reduces market quality despite narrower spreads.

- **Industry proposals**: Some regulatory proposals would ban maker-taker fees entirely and return to transparent, single-price auction models.

## Alternatives to maker-taker

### Single pricing model
All traders pay the same fee, regardless of maker/taker status. Market makers are separately subsidized (or not). This is simpler and less manipulable but may result in wider spreads (less liquidity subsidy).

### Rebate-free model
Exchanges charge no fees and earn revenue from listing fees, market data subscriptions, or other sources. A few private exchanges (dark pools) use this; it's not common for lit exchanges.

### Tiered/progressive model
Fees are based on volume but not maker/taker status. Higher-volume traders get better pricing. This encourages participation but doesn't subsidize market makers or HFT.

## Empirical outcomes

Academic research finds:

- **Spreads narrowed**: From $0.10+ in the 1990s to sub-$0.01 in the 2010s for large-cap stocks. Much of this is attributable to maker-taker competition and HFT entry.

- **Depth increased**: Order book depth (liquidity at multiple price levels) increased in the 2000s–2010s, partly due to maker-taker subsidies of patient orders.

- **Volatility and crashes**: Some studies link maker-taker incentives to increased market fragility and flash crashes. The 2010 flash crash occurred during a period of high-frequency trading driven by rebate incentives.

- **Welfare effects mixed**: Lower spreads benefit all traders (takers and makers), but rebate arms races increased fixed costs for exchanges and required higher taker fees to compensate.

## Global perspectives

- **U.S.**: Predominantly maker-taker for equities and options; most futures markets use single pricing
- **Europe**: Mixed; some European exchanges have caps on rebates; MiFID II regulations limit rebate disclosure requirements
- **Asia**: Slower adoption; some Asian exchanges use single pricing or offer maker-taker optionally
- **Futures/derivatives**: Most rely on single pricing to exchanges but allow clearing houses to charge member fees based on volume

## Practical impact for traders

For traders, understanding the maker-taker structure is critical:

1. **Use limit orders when possible**: Earn rebates instead of paying taker fees; saves 0.4–0.5% on large trades
2. **Choose venues carefully**: Rebate structures vary; some venues offer better rebates than others for your size/asset class
3. **Use smart order routing**: Algorithms route orders to venues offering best execution considering rebates
4. **Negotiate volume**: Large traders negotiate rebate tiers directly with exchanges

A large mutual fund paying $50K in annual taker fees could save $10K–$20K by optimizing order routing and using limit orders more aggressively.

<div class="wiki-seealso">

### Closely related
- [Bid-ask spread](/wiki/bid-ask-spread/) — the cost of immediacy; compressed by maker-taker competition
- [Liquidity provision](/wiki/liquidity-provider/) — the supply of orders willing to trade
- [High-frequency trading](/wiki/high-frequency-trading/) — strategy relying heavily on maker-taker rebates
- [Market maker obligations](/wiki/market-maker-obligations/) — traditional role now generalized via rebates

### Wider context
- [Exchange competition](/wiki/centralized-exchange/) — multiple venues fragmenting liquidity
- [Market microstructure](/wiki/market-order-execution/) — how markets process orders at the granular level
- [Order routing](/wiki/smart-order-router/) — algorithms directing orders to best venues
- [Flash crash](/wiki/flash-crash-2010/) — 2010 intraday crash partly attributed to HFT strategies enabled by rebates

</div>
