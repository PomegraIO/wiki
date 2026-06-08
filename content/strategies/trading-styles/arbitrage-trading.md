---
title: "Arbitrage Trading"
description: "Buying and selling equivalent assets simultaneously across different markets to capture price differences with minimal risk."
keywords:
  - arbitrage trading
  - market inefficiency
  - statistical arbitrage
  - triangular arbitrage
  - risk-free profit
image: "/svg/strategies.svg"
---

*Arbitrage is the practice of buying an asset in one market and immediately selling it in another where the price is higher, locking in a riskless profit.* **Arbitrage trading** exploits temporary misalignments in the pricing of identical or equivalent securities across different venues. The profits, though often small per trade, accrue because the trader is genuinely removing risk by executing both legs simultaneously or near-simultaneously.

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Arbitrage Trading — key facts</div>

<img src="/svg/strategies.svg" alt="An abstract editorial mark for financial strategies." />

<div class="wiki-infobox-caption">Simultaneously buying low in one market and selling high in another, capturing the spread.</div>

|   |   |
|---|---|
| **What it is** | Buying and selling equivalent assets in different markets to lock in a price spread |
| **Core principle** | Markets are not perfectly efficient; temporary price gaps exist |
| **Risk profile** | Near-zero, if both legs execute as intended |
| **Time horizon** | Milliseconds to days, depending on the type |
| **Capital requirement** | Often modest; borrowed capital and leverage are common |
| **Execution speed** | Critical; delays allow the spread to close |

</aside>

## Why markets leave arbitrage opportunities on the table

Perfect markets would have identical assets trading at identical prices everywhere, instantly. Real markets do not. Transaction costs, information delays, regulatory barriers, currency conversion fees, and the friction of moving capital between venues mean that at any given moment, a Treasury bond might trade at a slightly different yield on the New York Stock Exchange than on an electronic communication network, or a stock trading in US dollars might price differently from its equivalent listing in euros on a European exchange.

Arbitrage traders search for these gaps. When they find one, they exploit it by buying the cheaper version and selling the expensive one—collapsing the spread back to zero (or to their cost of execution). By doing so, they also improve market efficiency: their buying pressure lifts the cheap asset, their selling pressure lowers the expensive one, and the two prices converge. This is why arbitrage, though often perceived as parasitic, actually serves a real economic function.

## Types of arbitrage

**Cash-and-carry arbitrage** is straightforward: buy an asset and simultaneously sell a forward contract (or futures contract) on the same asset. If the forward price exceeds the spot price by more than the cost of financing and storage, the trader locks in the difference. This is common in commodities and bonds.

**Statistical arbitrage** is more subtle. A trader identifies two stocks or assets that historically move together—say, two automakers or two semiconductor firms. When their price relationship deviates from the historical norm, the trader buys the relatively cheap one and shorts the relatively expensive one, betting that the relationship will revert. This is not truly riskless (the relationship might not revert), but the statistical edge can be significant over many trades.

**Triangular arbitrage** appears in foreign-exchange markets. If the euro–dollar rate, the sterling–euro rate, and the sterling–dollar rate are slightly misaligned, a trader can buy euros with dollars, convert euros to sterling, convert sterling back to dollars—and end up with more dollars than they started with. The margins are typically tiny but execution is fast.

**Merger arbitrage** (also called risk arbitrage or deal arbitrage) involves buying shares of a company being acquired in a takeover and potentially shorting shares of the acquirer, betting that the deal will close at the announced price. This carries genuine risk: deals can fall through or prices can be renegotiated. The spread reflects market uncertainty about deal completion.

## The challenge of execution

Arbitrage sounds mechanically simple on paper but turns on execution. A trader spots a 15-basis-point spread between a bond's price on NYSE and on an alternative trading venue. By the time the trading system sends the order, receives confirmation, and reports the result, the spread may have narrowed to 2 basis points—or reversed. Commissions, fees, and bid-ask spreads consume the profit.

This is why modern arbitrage is dominated by automated trading systems and high-frequency traders. Latency—the time delay between detecting a spread and executing both legs—is the enemy. Traders invest in direct exchange connections, co-location services (placing servers physically near exchange matching engines), and algorithmic code that can detect and act on opportunities in microseconds. The barrier to entry has shifted from capital to technology.

## Arbitrage and market structure

One consequence of intensive arbitrage activity is the compression of spreads. Where once an inefficiency might persist for minutes or hours, it now closes in milliseconds. For retail investors and traditional traders, this is both good and bad: spreads are tighter, improving execution, but the opportunities for casual arbitrage have largely vanished. An individual trader cannot manually spot and execute an arbitrage trade before automated systems have already arbitraged it away.

Large [hedge funds](/hedge-fund/) and proprietary trading desks do still pursue arbitrage, but often on a much larger scale: finding temporary mispricings in bonds, cross-listed equities, or derivatives, or waiting for discrete events (like corporate actions) that momentarily fragment prices.

## The role of [capital flows](/capital-flows/) and barriers

Arbitrage becomes harder when it crosses borders, asset classes, or regulatory jurisdictions. A company with a [primary listing](/primary-market/) in London and a secondary listing in New York will sometimes trade at different [price-to-earnings ratios](/price-to-earnings-ratio/) because of:

- Currency exposure: a trader arbitraging must account for the strength or weakness of sterling against the dollar, which can wipe out small price differences.
- Regulatory friction: each market may have different settlement rules, short-selling restrictions, or disclosure requirements.
- Tax treatment: the cost of executing an arbitrage may differ depending on the tax jurisdiction of the arbitrage trader.
- Liquidity: one listing may be far more liquid than the other, making it difficult to execute the equivalent trade simultaneously.

These frictions mean that arbitrage at scale requires not just capital and speed but also deep market knowledge and relationships with brokers and custodians across multiple venues.

## Arbitrage and systemic risk

Efficient arbitrage also plays a role in financial stability. By binding prices together across markets, arbitrage traders help prevent any one market from becoming drastically detached from reality. However, when arbitrage traders are forced to exit positions simultaneously (due to margin pressure or [counterparty risk](/counterparty-risk/)), the sudden unwinding can amplify price movements and exacerbate [volatility](/historical-volatility/). The 1998 crisis at Long-Term Capital Management is a sobering historical reminder: a massive multi-billion dollar arbitrage operation imploded when [funding markets](/debt-financing/) seized up and the firm could not exit positions.

## See also

<div class="wiki-seealso">

### Closely related

- [Statistical arbitrage](/factor-investing/) — exploiting persistent deviations between correlated assets
- [Merger arbitrage](/acquisition/) — buying the target and shorting the acquirer in announced deals
- [Algorithmic trading](/algorithmic-trading/) — using automated systems to detect and execute price-sensitive trades
- [Short selling](/short-selling/) — selling borrowed securities in the hope of buying them back cheaper
- [Market maker](/market-maker-trading/) — standing ready to buy and sell, profiting from bid-ask spreads
- [High-frequency trading](/alternative-trading-system/) — ultra-low-latency trading of price discrepancies

### Wider context

- [Pricing efficiency](/price-discovery/) — how markets converge on fair values
- [Bid-ask spread](/bid-ask-spread/) — the cost of immediacy in trading
- [Leverage and margin](/debt-financing/) — how traders amplify capital to exploit small spreads
- [Counterparty risk](/counterparty-risk/) — the hazard of simultaneous execution across venues
- [Derivatives](/futures-contract/) — forwards, futures, and options that enable complex hedging strategies

</div>