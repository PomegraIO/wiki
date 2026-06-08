---
title: "How Contango Erodes Commodity ETF Returns Over Time"
description: "The mechanical drag that contango imposes on commodity ETFs through futures rolling: explained with numerical examples and annualized cost."
keywords:
  - contango commodity etf returns
  - futures roll drag
  - commodity etf performance
  - contango cost basis
  - oil etf rolling cost
  - roll erosion
image: /svg/commodities.svg
---

*When a [commodity ETF](/etf/) holds [futures contracts](/futures-contract/) in a **contango** environment, the cost of rolling expiring contracts to longer-dated ones creates a mechanical drag on returns. This roll cost is independent of spot price movement: even if crude oil trades flat, a contango-driven ETF that must continuously roll forward can lose 3–5% annualized or more. The drag is largest in sustained contango and disappears—or reverses—in [backwardation](/backwardation/).*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Contango Roll Drag — key facts</div>

<img src="/svg/commodities.svg" alt="An abstract editorial mark for commodities." />

<div class="wiki-infobox-caption">Contango is a permanent tax on commodity ETFs; backwardation, a subsidy.</div>

|   |   |
|---|---|
| **Cause** | Futures curve upward slope; near contract cheaper than far |
| **ETF structure** | Must roll before expiration; always sells low, buys high |
| **Typical drag** | 1–5% annualized, depending on contango magnitude |
| **Peak drag example** | 2020 oil crash (June WTI at -$37); contango ~$4–6/barrel |
| **Duration** | Ongoing every roll period; compounds quarterly or monthly |
| **Backwardation benefit** | Near contract more expensive; roll becomes profitable |
| **Spot vs. futures** | Spot oil and futures oil can diverge sharply due to rolls |
| **Most affected** | Energy ETFs; less in metals; varies by supply regime |

</aside>

## The Mechanics: Why ETFs Must Roll

A [commodity ETF](/etf/) that tracks oil, natural gas, or copper typically holds [futures contracts](/futures-contract/) rather than the physical commodity. A futures contract matures on a specific date—say, the 20th of the month. On or before that date, the contract must be closed out, or the owner takes physical delivery. Most financial ETFs do not want oil barrels, so they close the expiring contract and buy a new one with a later maturity.

This process—closing the near contract and opening the far contract—is called **rolling**. An ETF does it once a month, once a quarter, or as dictated by the contract's [expiration date](/expiration-date/). A commodity ETF may roll continuously across all months of the year, maintaining perpetual exposure to "the commodity."

The problem: if the futures curve is in [contango](/contango/) (a normal, upward-sloping shape), the near contract is cheaper than the far contract. The ETF sells the cheap near contract and buys the expensive far contract, locking in a loss on each roll.

## Numerical Example: Oil Contango Drag

Suppose crude oil spot price is $50/barrel and the [futures curve](/contango/) is in contango:

| Contract | Price |
|---|---|
| Current month (Jan) | $50.00 |
| Next month (Feb) | $51.00 |
| Month after (Mar) | $52.00 |

The ETF holds January oil futures at $50. As January nears expiration, the fund closes that contract at $50 and buys February at $51. It has locked in a $1/barrel loss on the roll. If the spot price stays at $50 in February, the February contract will also decline toward spot, but the ETF must now roll again: sell February at approximately $51, buy March at $52. Another $1/barrel loss.

Over a year:
- Four quarterly rolls, each costing $1/barrel
- Total rolling cost: $4/barrel on a $50 spot price
- Annualized drag: $4 ÷ $50 = 8%

Even if spot oil never moves, the ETF's total return is minus 8% over the year, purely from rolling costs.

## Factors Affecting Drag Magnitude

**Steepness of the curve:** If the contango is shallow ($0.10/barrel between months), rolling costs only 0.4% annualized. If it is steep ($2–3/barrel between months, as it was in 2020 during the oil glut), the drag can exceed 5–10% annualized. The steeper the contango, the larger the drag.

**Roll frequency:** An ETF that rolls monthly incurs rolling costs monthly; one that rolls quarterly incurs them less often. Monthly rolling in steep contango is particularly painful.

**Volatility and front-month premium:** In some environments, the front month (nearest contract) trades at a premium because spot is tight and storage is expensive. In others, the front month is at a discount. The contango drag depends on where in the curve the ETF holds its position.

## The 2020 Oil Example

In April 2020, when US oil prices briefly crashed to –$37 per barrel, the near-term futures contracts were deeply underwater (negative prices are rare and reflect storage concerns). But forward contracts (months out) were positive: $5–$10/barrel. The contango was extreme: a $40+ spread between near and far.

Commodity ETFs holding oil were forced to roll into this contango, crystallizing massive losses in a single quarter. An ETF holding June contracts in mid-April had to close near-expiration contracts and buy July, August, and beyond. The July contract was trading at $10+/barrel; the June at negative or near zero. The roll cost was enormous—effectively a 50%+ loss on that quarter's rolling alone.

This episode showed that contango drag is not merely theoretical; it is a direct and visible hit to returns. ETF investors who bought oil in April 2020 thinking the spot price would bounce did not expect to lose 30–40% in rolling costs, yet many funds posted exactly that.

## Contango vs. Backwardation

In [backwardation](/backwardation/)—a downward-sloping curve—the near contract is expensive and the far contract is cheap. The ETF sells the expensive near contract and buys the cheap far contract, pocketing a gain on each roll.

Backwardation typically occurs when supply is tight or storage is expensive, and forward buyers are willing to pay a premium for deferred delivery. During the 2022 energy crisis in Europe (Russian gas supply disrupted), natural gas futures traded in steep backwardation, and gas ETFs benefited from rolling. An ETF could show positive returns purely from rolling, even if spot prices declined.

## Spot vs. Futures Divergence

Because of rolling costs, a commodity's spot price and its futures-tracking ETF can diverge significantly over time. If the spot price of oil rises 10% but the ETF is constantly rolling into a 5% contango drag, the ETF gains only 5%. Over years, this compounds: spot and futures can be 15–20% apart, purely because of rolling.

Sophisticated commodity traders and funds use [cost-of-carry](/cost-of-carry/) models to understand and exploit these discrepancies. Physical traders who can store the commodity may buy spot cheap and sell forwards dear, arbitraging the contango. ETF investors, without access to physical storage or arbitrage, simply accept the drag.

## Monthly vs. Quarterly Rolls

ETFs structured to roll monthly (e.g., by holding a rolling strip of one-month contracts) incur rolling costs more frequently than those rolling quarterly. But monthly rolls often catch better liquidity and tighter spreads, because the front month (just-expiring contract) has the highest trading volume. Quarterly rolling, less frequent, means one month lingers less-traded; the bid-ask spread is wider.

In practice, the frequency and timing of rolls matter, but the total annual drag is determined primarily by the average magnitude of contango and the roll frequency. A monthly roll into shallow contango might drag only 1.5% annually, while a quarterly roll into steep contango might exceed 6%.

## ETF Structures and Alternative Approaches

Some commodity ETFs try to minimize roll drag by:
- **Holding physical:** Actually buying and storing the commodity (rare and expensive for oil; more feasible for gold or silver). No rolling needed, but storage and insurance cost money.
- **Owning stocks or bonds of commodity producers:** An oil stock ETF tracks equities of oil companies, not oil futures, so no rolling. But the returns are not the same as spot oil; they are company performance, which includes dividends, debt, and management decisions.
- **Inverse or leveraged structures:** [Leveraged ETFs](/leveraged-etf/) magnify contango drag because they roll more frequently. An inverse or short ETF in contango can face severe drag; backwardation is its friend.

Most broad-based commodity ETFs accept the contango drag as a cost of doing business. The funds disclose roll costs and slippage in their prospectuses and annual reports, but they do not always highlight it in marketing.

## Long-Term Return Expectations

For an investor considering a long-term commodity ETF holding, contango drag is a permanent headwind. If you expect spot oil to rise 3% annually but the ETF drags 4% annually from contango, your total return is minus 1%. This is why many advisors recommend commodity ETFs only as a tactical position (betting on a near-term price move) or for very short-term exposures, not as a long-term buy-and-hold.

Conversely, if you expect a commodity to enter backwardation (supply tightening, storage becoming scarce), the rolling becomes a tailwind, and the ETF outperforms spot. This dynamic is important for longer-term strategic allocations.

## See also

<div class="wiki-seealso">

### Closely related

- [Contango](/contango/) — upward-sloping curve and its causes
- [Backwardation](/backwardation/) — downward-sloping curve and rolling gains
- [Futures contract](/futures-contract/) — the underlying derivative
- [Rolling a derivatives position](/derivatives-roll-explained/) — mechanics of the roll
- Commodity ETF — ETF structure and tracking methods
- [Expense ratio](/expense-ratio/) — additional layer of ETF costs
- [Basis risk](/basis-risk/) — futures-spot divergence
- [Cost of carry](/cost-of-carry/) — economic model of contango

### Wider context

- [ETF](/etf/) — broad category of tracked index funds
- [Leveraged ETF](/leveraged-etf/) — amplified contango drag
- [Natural gas](/natural-gas/) — volatile contango environment
- [Crude oil](/crude-oil/) — most common contango-affected commodity
- [Business cycle](/business-cycle/) — determines supply tightness and curve shape

</div>
