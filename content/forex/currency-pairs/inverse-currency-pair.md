---
title: "Inverse Currency Pair"
description: "The reciprocal of a direct currency quote; the arithmetic relationship between USD/EUR and EUR/USD, and how traders select between direct and inverse quotes."
keywords:
  - inverse currency pair
  - currency quote direction
  - indirect quote
  - forex notation
  - bid-ask spread
image: "/svg/forex.svg"
---

*An **inverse currency pair** is the reciprocal of a direct quote: if the direct pair is USD/EUR, the inverse is EUR/USD. The relationship between them is purely mathematical—if USD/EUR trades at 0.92, then EUR/USD trades at 1/0.92 ≈ 1.087—yet the choice between direct and inverse affects how traders interpret moves, manage spreads, and execute orders. Most major pairs are quoted both ways, with market convention and liquidity determining which is "primary."*

## The reciprocal relationship

Currency pairs are always quoted as base/quote. In USD/EUR, the US dollar is the base and the euro is the quote. A price of 0.92 means one dollar buys 0.92 euros. In the inverse, EUR/USD, the euro is the base and the dollar is the quote. A price of 1.087 means one euro buys 1.087 dollars. Mathematically, these are identical positions: if you exchange one dollar for 0.92 euros, you are simultaneously exchanging 1 euro for 1.087 dollars (ignoring bid-ask spreads and transaction costs).

The conversion is straightforward: **Inverse Price = 1 / Direct Price**. If EUR/USD is at 1.10, then USD/EUR is at 1/1.10 ≈ 0.909. If GBP/USD moves from 1.25 to 1.26, then USD/GBP moves from 0.80 to 1/1.26 ≈ 0.794—a move that, in percentage terms, is identical but opposite in sign when viewed from the inverse's perspective.

## Why both quotes exist

Market convention determines which pair is primary (most liquid and widely quoted) and which is secondary. For the dollar against most developed currencies, the dollar-first convention prevails: EUR/USD, GBP/USD, and USD/JPY are the primary quotes. But for certain pairs, the convention flips. USD/CAD and USD/CHF are quoted dollar-first because of historical market practice, yet traders often reference the inverse (CAD/USD, CHF/USD) when discussing relative strength.

This dual quotation survives because different market participants find different quotes natural. A US corporate treasurer managing euro exposure thinks in euros-per-dollar (EUR/USD) and wants to know how many euros she gets for a dollar. A European asset manager managing US exposure thinks in dollars-per-euro (USD/EUR) and wants to know how many dollars he gets for a euro. Both are trading the same cross rate; they simply frame it inversely.

Interbank dealers quote both, and their pricing engines convert seamlessly between them. A dealer quoting "1.0850 / 1.0855" on EUR/USD is simultaneously quoting "0.9215 / 0.9220" on USD/EUR (applying the reciprocal formula to both sides of the spread). Traders can choose whichever framing is most convenient and liquid.

## Bid-ask spread and inverse quotes

An important subtlety arises when converting bid-ask spreads between direct and inverse quotes. If EUR/USD is quoted 1.0850 / 1.0855 (a 5-pip spread), the inverse USD/EUR spread is not also 5 pips. To invert the bid and ask prices, a trader must reverse their order: the ask price inverts to the new bid, and the bid price inverts to the new ask.

1 / 1.0855 (original ask) ≈ 0.92119 (new bid on inverse)
1 / 1.0850 (original bid) ≈ 0.92174 (new ask on inverse)

The new spread is now 0.92174 - 0.92119 = 0.00055, which in pips on a currency denominated to four decimals is 5.5 pips. The spread has widened slightly because the bid-ask spread, when inverted on a price far from 1.0, is no longer symmetric. This is why traders sometimes choose the inverse of a less-liquid pair if doing so narrows the effective spread they face.

## Choosing between direct and inverse in trading

Traders choose the direct or inverse quote based on three factors: **liquidity**, **spread**, and **intuition**. 

Most major currency pairs have a clear liquidity hierarchy. EUR/USD is far more liquid than USD/EUR; GBP/USD is far more liquid than USD/GBP. A trader wanting to exchange large size will route through the more liquid quote to minimise market impact. This usually means the primary quote, but not always.

For less-liquid pairs, the inverse may actually be tighter. If a hedge fund wants to buy Norwegian krone against the dollar, it might find that EUR/NOK is more liquid than USD/NOK, and therefore more efficient to express the trade via the EUR pair rather than the dollar pair. Similarly, some emerging market currencies are more liquid when quoted against a major developed currency (like the euro) than against the dollar directly.

Intuition is subtler. A trader who manages a portfolio with a structural long position in euros thinks in EUR/USD—higher is good, higher is a weaker dollar. The same trader, if managing a different portfolio or time horizon, might think in USD/EUR—higher is bad, higher is a stronger dollar. The quote chosen becomes a mental frame that can affect decision-making. A trader in a high-beta market can be influenced by whether they see the move as "a big jump in the price" or "a barely perceptible shift in the decimal places."

## Cross rates and synthetic pricing

Inverse quotes also matter when constructing synthetic cross rates. If a trader wants to exchange Norwegian krone for Canadian dollars, neither currency is the dollar, so there is no primary "NOK/CAD" market. Instead, a trader constructs the cross by combining two dollar pairs:

NOK/CAD = (NOK/USD) × (USD/CAD)

To invert this, a trader would use:
CAD/NOK = (CAD/USD) × (USD/NOK)

The choice of which inverse to use depends on which legs of the synthetic are most liquid. This is not merely academic: in periods of volatility, the synthetic price can diverge from real underlying demand, creating arbitrage opportunities for traders who can execute the entire package quickly.

## Inverse moves and leverage

In leverage trading (margin), the choice of direct versus inverse pair can affect how margin requirements are calculated by different platforms. A trader using 10:1 leverage to buy 1 standard lot of EUR/USD controls €100,000 of exposure. The same trader using 10:1 leverage to buy 1 standard lot of USD/EUR (the inverse) still controls €100,000 of exposure, but the notional dollar value is different (approximately $108,700). Some platforms calculate margin based on the base currency, others on the quote currency; the choice of pair can shift the effective leverage the trader receives. This is why traders must be careful when switching between direct and inverse pairs on the same underlying exposure.

## See also

<div class="wiki-seealso">

### Closely related

- [Currency pair](/us-dollar/) — the fundamental definition and notation of FX quotes
- [Spot exchange rate](/spot-exchange-rate/) — the real-time price underpinning both direct and inverse quotes
- [Bid-ask spread](/bid-ask-spread/) — how spreads change when converting between direct and inverse pairs
- [Over-the-counter market](/over-the-counter-market/) — the structure allowing both direct and inverse quotation

### Wider context

- [Market maker trading](/market-maker-trading/) — how dealers quote both directions of a pair
- [Cross rate](/us-dollar/) — synthetic pricing of non-dollar pairs
- [Leverage ratio (forex)](/leverage-ratio-forex/) — how pair selection affects margin and notional exposure
- [Foreign exchange microstructure](/over-the-counter-market/) — pricing conventions in FX markets

</div>
