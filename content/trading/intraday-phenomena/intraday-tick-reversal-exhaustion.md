---
title: "Intraday Tick Exhaustion and Reversal"
description: "The NYSE TICK indicator shows the breadth of intraday buying or selling; extreme readings signal exhaustion and often precede intraday reversals."
keywords:
  - intraday tick exhaustion
  - tick reversal trading
  - NYSE TICK indicator
  - market breadth intraday
  - exhaustion reversal signal
  - intraday trading reversal
---

*The NYSE **TICK** is a real-time breadth indicator measuring the number of stocks on the New York Stock Exchange trading on an uptick minus those trading on a downtick in each moment. Extreme readings—strongly positive (say +1500 or higher) or deeply negative (−1500 or lower)—signal short-term buying or selling exhaustion and historically have preceded intraday reversals within hours.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Intraday Tick Exhaustion and Reversal — key facts</div>

<img src="/svg/trading.svg" alt="An abstract editorial mark for trading mechanics and intraday patterns." />

<div class="wiki-infobox-caption">Extreme TICK readings warn that buyers or sellers are overextended and reversals are near.</div>

|   |   |
|---|---|
| **Definition** | TICK = (stocks on uptick) − (stocks on downtick); real-time breadth snapshot |
| **Extreme positive** | +1200 to +2000; indicates widespread buying and potential overbought exhaustion |
| **Extreme negative** | −1200 to −2000; indicates widespread selling and potential oversold exhaustion |
| **Reversal signal** | Extreme TICK often precedes price reversals within minutes to hours |
| **Holding period** | Trades typically scalped within 5 minutes to 2 hours after the extreme |
| **Reliability** | Higher in low-volatility regimes; less reliable during major news or gap opens |
| **Data source** | Real-time from exchanges; published on Bloomberg, trading platforms, and financial dashboards |

</aside>

## What the TICK actually measures

Every stock trade on the NYSE is marked as either an uptick (at or above the last price) or a downtick (below the last price). At any given second, the TICK value is the running count of uptick stocks minus downtick stocks across all NYSE-listed issues—typically a few thousand stocks. A TICK of +800 means 800 more stocks are trading on upticks than downticks at that moment; a TICK of −800 means the reverse.

The TICK is a real-time [breadth](/support-and-resistance/) indicator. When the TICK is strongly positive, a broad majority of stocks are advancing—bullish breadth. When strongly negative, a broad majority are declining—bearish breadth. Casual observers mistakenly confuse TICK with an index price: the TICK does not directly move the S&P 500 or Nasdaq, but the breadth it captures often leads price moves.

## Extreme TICK and exhaustion

Exhaustion in a market trend occurs when buyers (or sellers) have pushed prices to a point where momentum runs out. Extreme TICK readings flag this state. A TICK reading above +1500 on the NYSE is rare and typically occurs during strong rallies late in the day or after a gap-up open. Such high readings suggest that a very broad swath of stocks have been bid up; retail and algorithmic buyers have been aggressive.

However, this broadness and aggression are themselves warnings. If nearly every stock is advancing, there are few buyers left to push higher. The buyers who remain are chasing the move—they've bought late in the exhaustion phase. Meanwhile, early buyers have taken profits, and sellers begin to emerge.

A TICK reading below −1500 signals the mirror image: nearly every stock is selling off, likely during panic selling in the first hour after a gap-down open or late in a decline. Sellers have been so aggressive that few stocks remain bid; the selling pressure has been exhausted because almost everyone who wanted to sell has already done so. Buyers then return, and the TICK bounces.

## How traders use extreme TICK for reversals

A common tactical approach among intraday traders:

1. **Watch for extreme TICK**: Set alerts for readings above +1400 or below −1400
2. **On extreme positive TICK**: scalp short (bet on a quick decline or cover longs for profit). The reasoning: the rally has sucked in late buyers; a minor reversal or consolidation is statistically likely within 5–30 minutes
3. **On extreme negative TICK**: scalp long or cover shorts. The reasoning: the sell-off has exhausted weak hands; a minor bounce is likely
4. **Hold period**: typically 5 minutes to 2 hours; if the TICK does not reverse and breadth remains extreme, the signal fails and the trader cuts the position

The trades are usually small and quick—scalps, not swing trades. A trader might buy 100 shares of QQQ (Nasdaq-100 ETF) when TICK hits −1600, hold for 15 minutes as the market bounces, then sell for a small profit.

## Example: a real intraday scenario

Imagine the S&P 500 gaps down 1% at the open (bad news overnight). The TICK crashes to −1800 as panicked sellers hit bids. Traders with this alert immediately start covering shorts or buying index futures, reasoning that the sell-off is extreme and a bounce is imminent. Within 10 minutes, covering and bottom-fishing drives the TICK up to −500, then positive, and the S&P 500 rallies 0.3% off the lows. Traders who went long at the −1800 TICK reading banked a quick 0.3% gain on leverage, capturing the exhaustion rebound.

Conversely, on a strong up day, the market rallies 1.5% in the first two hours. The TICK reaches +1700 as nearly every stock is being bought. Intraday traders short the indexes or sell long positions into the strength, anticipating that the broad buying has exhausted and a pullback is near. The market indeed pulls back 0.2–0.3%, and those shorts profit.

## Limitations and when the signal fails

The TICK exhaustion signal is not a mechanical trade. It fails when:

- **Major news or economic releases**: If a strong earnings report or jobs number hits while TICK is extreme, the move can continue further, and the exhaustion signal is invalidated. The catalyst overrides breadth signals.

- **Algorithmic trading dominance**: Modern high-frequency trading and momentum algos can chase extremes and push them further, creating "exhaustion fails" where the move extends further than expected.

- **Illiquidity regimes**: On slow, low-volume days, extreme TICK readings are less reliable. A TICK of +1200 on a normal trading day is extreme; on a light volume day, it may be routine.

- **Directional trends**: In very strong directional days (e.g., the first day of a large earnings season rally), extreme TICK can hold or grow more extreme, and reversals are weak or nonexistent.

- **Close to economic calendar**: Options expiration, Fed announcements, or other scheduled events can generate extreme TICK readings that persist longer than normal.

The TICK is a tool, not a guarantee. Successful traders combine it with other signals—volume, [support and resistance](/support-and-resistance/) levels, order flow imbalances, and technical patterns—before executing a reversal trade.

## TICK vs. other breadth indicators

The TICK measures moment-to-moment breadth (uptick vs. downtick count). Related but distinct breadth indicators include:

- **Advance/Decline line**: cumulative count of advancing vs. declining stocks; slower to respond than TICK
- **Market breadth percent**: percentage of stocks above their 50-day moving average; longer-term exhaustion measure
- **Put/call ratio**: options sentiment; complements TICK
- **VORTEX and other volume-breadth hybrids**: combine breadth with volume for multi-timeframe exhaustion signals

TICK is the most responsive real-time breadth signal and is favored by short-term traders. Longer-term investors rely on advance/decline and breadth percent for swing or position trade timing.

## See also

<div class="wiki-seealso">

### Closely related

- [Support and Resistance](/support-and-resistance/) — price levels that, combined with TICK extremes, confirm reversals
- [Market Maker Trading](/market-maker-trading/) — how dealers adjust to TICK extremes and breadth signals
- [Market Timing](/market-timing/) — using intraday indicators like TICK to time short-term entries and exits
- [Algorithmic Trading](/algorithmic-trading/) — how algos respond to TICK and breadth extremes
- [Stock Market](/stock-market/) — the underlying trading environment and structural mechanics

### Wider context

- [Momentum Investing](/momentum-investing/) — longer-term trend-following that also uses breadth confirmation
- [Volatility Smile](/volatility-smile/) — options pricing shifts during TICK extremes and volatility expansion
- [Bid-Ask Spread](/bid-ask-spread/) — widens during TICK extremes due to order book stress
- [Technical Analysis](/support-and-resistance/) — broader framework for using price and breadth patterns

</div>
