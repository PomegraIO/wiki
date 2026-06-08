---
title: "How Market Indices Are Constructed: Price-Weighted vs Cap-Weighted"
description: "How stock market indices are constructed determines their behavior; price-weighted, market-cap-weighted, and equal-weight methods each produce different results."
keywords:
  - how stock market indices are constructed
  - price weighted index
  - market cap weighted index
  - equal weight index
  - index weighting methodology
  - stock index construction
image: /svg/markets.svg
---

*A stock market **index** is a mathematical tool designed to represent the movement of a group of stocks. The choice of **weighting methodology** — how much influence each stock has on the index's level — fundamentally changes which stocks drive the index and how it behaves. The three main methods are price-weighted, market-cap-weighted, and equal-weight, and each produces a different picture of the same market.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Market Index Construction — key facts</div>

<img src="/svg/markets.svg" alt="An abstract editorial mark for financial markets." />

<div class="wiki-infobox-caption">Index methodology is arbitrary; it affects which stocks matter most and how well the index represents "the market."</div>

|   |   |
|---|---|
| **Price-weighted** | Stocks with higher prices have more influence; biased toward higher-priced issues |
| **Market-cap-weighted** | Stocks weighted by total market value; most widely used; influences [passive-investing](/index-fund/) flows |
| **Equal-weight** | Each stock has equal influence regardless of size; requires frequent rebalancing |
| **Common indices** | Dow (price); S&P 500, NASDAQ (market-cap); Russell 2000 (market-cap) |
| **Impact on returns** | Same companies, different weighting = different index returns and correlations |

</aside>

## Why index methodology matters

An index is a mathematical construct, not a law of nature. The [S&P 500 Index](/sp-500-index/) includes 500 large-cap stocks, but the weighting of those stocks within the index is a choice made by the index administrator (in this case, S&P Dow Jones Indices). That choice cascades through the market: trillions of dollars in passive [index-fund](/index-fund/) and exchange-traded fund assets track the S&P 500, so the weighting methodology determines how much capital flows to each stock. If the weighting changes—even slightly—it can redirect billions of dollars in investment capital.

The three dominant methodologies are price-weighted (rarest), market-cap-weighted (most common), and equal-weight (specialized). Each produces a different returns pattern, risk profile, and distribution of capital.

## Price-weighted indices: the Dow Jones

The most famous price-weighted index is the [Dow Jones Industrial Average](/dow-jones-industrial-average/). In a price-weighted index, each stock's influence is proportional to its share price, not its market value. If Company A trades at $200 and Company B trades at $100, Company A has twice the weight in the index, regardless of whether Company A is a smaller company by market capitalization or a much larger one.

This methodology is intuitive if you think of an index as a simple average, but it is economically arbitrary. A company with a $200 stock price and 10 million shares outstanding has a $2 billion market capitalization. Another company with a $100 stock price and 100 million shares outstanding has a $10 billion market capitalization—five times larger. In a price-weighted index, the smaller company gets more influence just because its stock price is higher.

Price-weighted indices also create a peculiar rebalancing problem. If a stock undergoes a [stock-split](/stock-split/)—say, a 2-for-1 split that halves the price—the stock's weight in a price-weighted index is automatically cut in half, even though nothing about the company changed. To maintain its weight, the index must be adjusted by changing the divisor (the denominator used to calculate the index level). The Dow is famously adjusted for splits, mergers, and substitutions.

## Market-cap-weighted indices: the modern standard

Market-cap-weighted indices, by far the most common, weight each stock by its total market capitalization—share price times shares outstanding. The larger a company's market cap, the larger its weight in the index. The [S&P 500 Index](/sp-500-index/) is market-cap-weighted, as is the [NASDAQ](/nasdaq/) Composite. Most passive [exchange-traded-fund](/etf/) and index funds track market-cap-weighted indices.

Market-cap weighting has a powerful logic: it represents the proportional ownership value of the stocks in the index. If the S&P 500 has a total market capitalization of $40 trillion, and Apple has a $3 trillion market cap, then Apple is 7.5% of the index by value. If you own the index, you own Apple proportionally to its size in the market.

Market-cap weighting also minimizes rebalancing friction. As stock prices move, weights adjust automatically without forced buying or selling. If Apple's stock price rises and its market cap grows from $3 trillion to $3.5 trillion, its weight in the S&P 500 increases automatically; no rebalancing transaction is needed.

However, market-cap weighting does have consequences. It means that large-cap stocks dominate the index returns. During periods when mega-cap technology stocks (Apple, Microsoft, Nvidia, Tesla) are soaring in price, a market-cap-weighted index of U.S. stocks (the S&P 500) will perform very well, even if the median stock is flat or down. Conversely, it means that smaller stocks have minimal influence on the index level, even if they are outperforming. An investor tracking a market-cap-weighted index is betting, implicitly, that the largest companies should be overweighted relative to smaller ones.

## Equal-weight indices: the rebalancing trade-off

In an equal-weight index, every stock has the same weight regardless of price or market capitalization. If an index contains 500 stocks, each is weighted at 0.2% (1/500). If an index contains 100 stocks, each is 1%.

Equal-weight indices are mechanically appealing: they give voice to smaller and mid-cap stocks that would otherwise be drowned out by mega-cap names. An equal-weight S&P 500 index would have small-cap (lowest market cap) stocks in the index with the same weight as Apple or Microsoft. Historically, this has led to outperformance during periods when small stocks outperform large ones, but underperformance when large-cap stocks lead.

The downside of equal-weighting is that it requires constant rebalancing. As stock prices move and some stocks appreciate faster than others, their weights drift away from the equal 0.2% target. To maintain equal weight, the index administrator must sell the winners and buy the losers, crystallizing the opposite bet from a market-cap-weighted index: it automatically overweights stocks that have fallen and underweights winners. This rebalancing creates transaction costs and tax inefficiency in ETFs tracking equal-weight indices. Academic research suggests that this rebalancing "drag" reduces after-cost returns over long periods.

## Comparing the three: a concrete example

Imagine three stocks: Company A ($300 price, 10M shares, $3B market cap), Company B ($100 price, 30M shares, $3B market cap), and Company C ($50 price, 40M shares, $2B market cap). Total market cap = $8B.

**Price-weighted:** A has weight 300/(300+100+50) = 60%; B has 20%; C has 10%. If A rises 10%, B flat, C down 5%, the index return = 0.60×10% + 0.20×0% + 0.10×(−5%) = +5.5%.

**Market-cap-weighted:** A has weight 3/8 = 37.5%; B has 37.5%; C has 25%. Same moves: 0.375×10% + 0.375×0% + 0.25×(−5%) = +2.5%.

**Equal-weight:** Each stock is 33.33%. Same moves: 0.333×10% + 0.333×0% + 0.333×(−5%) = +1.67%.

The same three stocks, same price moves, yet three different index returns because of weighting. Over decades, small differences in weighting compound into significant gaps in index performance.

## Impact on passive investing and capital flows

The index methodology determines the composition and weighting of passive investments. Trillions of dollars flow into index funds and ETFs that track indices like the S&P 500 (market-cap-weighted). This capital flows automatically to stocks in proportion to their weight in the index. A company entering or exiting the S&P 500 experiences sudden inflows or outflows of index-tracking capital. A large company whose market cap shrinks and falls out of the index experiences automatic selling by index funds.

This mechanical flow of capital means that index construction is not just a technical matter—it is an economic force. Index administrators (S&P Dow Jones Indices, MSCI, Russell Indices) make deliberate choices about methodology, constituent selection, and weighting that redirect billions in capital globally. These choices should be defensible, but they are inherently arbitrary.

## See also

<div class="wiki-seealso">

### Closely related

- [Index Fund](/index-fund/) — passive funds that track market indices and depend on index methodology
- [Exchange-Traded Fund](/etf/) — listed funds that replicate indices and amplify index weighting effects
- [Market Capitalization](/market-capitalization/) — the metric underlying most modern index weighting
- [S&P 500 Index](/sp-500-index/) — the most widely used market-cap-weighted index
- [Stock Split](/stock-split/) — an event that affects price-weighted index composition
- Passive Investing — the practice of holding indices that makes methodology consequential
- [Sector Rotation](/sector-rotation/) — how index tilts influence sector performance

### Wider context

- [Market Risk](/market-risk/) — how index composition affects systemic risk
- [Momentum Investing](/momentum-investing/) — how rebalancing in equal-weight indices creates mechanical contrarian effects
- [Price Discovery](/price-discovery/) — how heavily weighted stocks dominate price discovery in indices
- [Asset Allocation](/asset-allocation/) — how indices form the building blocks of diversified portfolios

</div>
