---
title: "Option Open Interest"
description: "The count of outstanding option contracts still held by traders, revealing market positioning and liquidity conditions."
keywords:
  - open interest options
  - contract positioning
  - option liquidity
  - outstanding contracts
image: "/svg/derivatives.svg"
---

*[Open interest](/option-open-interest/) is the total number of option contracts that remain unsettled—still owned and owed between counterparties. Unlike volume, which measures daily trading activity, open interest reveals the net position: how many contracts traders collectively hold at day's end. Higher open interest signals deeper liquidity and tighter [bid-ask spreads](/bid-ask-spread-options/); thin open interest warns of slippage on entry and exit.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Open Interest — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives markets." />

<div class="wiki-infobox-caption">The sum of live contracts awaiting settlement.</div>

|   |   |
|---|---|
| **What it is** | Total count of unsettled option contracts across all expiry dates and [strike prices](/strike-price/) |
| **Measured in** | Number of contracts (each representing 100 shares of the underlying) |
| **Updates** | Daily, after market close |
| **Key signal** | Liquidity depth; trader conviction; potential price support or resistance |
| **vs. [Volume](/option-volume/)** | Volume counts trades executed today; open interest counts contracts still live |
| **Also called** | Outstanding interest, position count |

</aside>

## Why open interest matters more than you might think

A seasoned trader glances at open interest before a trade. A novice checks only price and recent [volatility](/historical-volatility/). That's a costly gap. Open interest is a proxy for the ease—and cost—of getting in and out. When open interest in a particular strike and expiry is high (say, 50,000+ contracts), a small market order can fill near the mid-price. When it's thin (100 contracts or fewer), you'll hit significant slippage; the market maker quotes wider to cover the risk of holding an illiquid position.

Open interest also reveals where traders are clustering. A spike in open interest at an out-of-the-money call strike often signals bullish hedging or speculation: traders are loading up on the same bet. That consensus can be fragile. Conversely, open interest that shrinks as expiry approaches suggests confidence is waning—traders are taking profits or cutting losses rather than rolling forward.

## The mechanics: how open interest changes

Open interest is not a simple tally of all trades. Instead, it tracks the net number of open positions. When Alice buys a call from Bob, open interest rises by one contract (one pair of buyer-seller). When Alice later sells that call to Carol, open interest doesn't move—it's still one contract, just with Carol on the buy side and Bob now flat. Only when a position is closed (both sides agree to unwind) does open interest fall.

This quirk means that high trading [volume](/option-volume/) on a given day can coincide with flat or falling open interest. Imagine a strike with 10,000 open contracts. If traders churn 50,000 contracts in the session—everyone closing and rolling positions—the day's volume towers, but open interest ends unchanged. A savvy trader interprets volume and open interest together: volume reveals activity, open interest reveals conviction.

## Reading the signal: what levels tell you

Highly liquid option chains (like SPY or QQQ calls) routinely show open interest in the millions across each expiry. For a major index [ETF](/etf/), an active strike might hold 500,000+ contracts. For a mid-cap stock, significant open interest might be 10,000–50,000. For a micro-cap or newly listed [SPAC](/special-purpose-acquisition-company/), you may find strikes with just 50–200 contracts alive.

The threshold for tradability is subjective, but professionals often avoid strikes with fewer than 1,000 open contracts; at 5,000+, the spread typically tightens and you can size up without moving the market. In really liquid series, even 100,000+ contracts see tight pricing.

Seasonal patterns matter too. Near expiry (final week), traders roll to the next month or close entirely, often suppressing open interest in the expiring series. The month after next is often a graveyard of stale positions. The month after that—the most-liquid, best-for-trading cycle—tends to accrue open interest as new bets arrive. Professional traders learn to front-run this seasonal dance: when open interest shifts away from one expiry and toward another, volatility and spreads follow.

## Open interest and [price discovery](/price-discovery/)

Open interest indirectly shapes the [strike price](/strike-price/) itself. Imagine a stock hovering near $50. If calls at $55 have 500,000 open contracts while calls at $60 have 50, the $55 strike is a center of gravity—more traders are anchored there, and the [bid-ask spread](/bid-ask-spread-options/) is tighter. When price approaches, $55 tends to be stickier. The accumulated positions create friction, or sometimes springboard momentum, depending on whether those positions are underwater or in the money.

Exchange data and live option chains publish open interest for free or nominal cost. Serious traders watch it alongside [implied volatility](/implied-volatility/) and [the Greeks](/delta/) to detect shifts in market structure. A sudden spike in open interest at a far out-of-the-money strike often precedes a move—someone's buying insurance or speculating.

## Open interest ≠ liquidity, but they're close cousins

It's tempting to conflate open interest with liquidity. They're related but not identical. An option can have high open interest but low [volume](/option-volume/)—perhaps a position opened weeks ago and left untouched. Conversely, an illiquid option might see high volume on a single day (a large block trade, say) then revert to thin activity. For a trader placing a market order right now, today's [bid-ask spread](/bid-ask-spread-options/) and the [time of day](/option-volume/) matter more than yesterday's open interest.

Yet over time, open interest is the strongest proxy for structural liquidity. Strikes and expiries that accumulate open interest attract [market makers](/market-maker-trading/) and competing brokers; they narrow spreads and tighten execution. Deserted strikes, by contrast, carry bid-ask spreads of 10% or more.

## See also

<div class="wiki-seealso">

### Closely related

- [Option Volume](/option-volume/) — How daily trade counts differ from open interest; why both matter for timing
- [Bid-Ask Spread in Options](/bid-ask-spread-options/) — How open interest shapes the cost of entry and exit
- [Option Lot Size](/option-lot-size/) — Standard contract multipliers that scale your exposure
- [Strike Price](/strike-price/) — Why certain strikes accumulate more open interest than others
- [Implied Volatility](/implied-volatility/) — The volatility priced into open contracts at each strike
- [Delta](/delta/) — How open interest in calls vs. puts reveals directional bets

### Wider context

- [Option](/option/) — The foundational derivative contract
- [Futures Contract](/futures-contract/) — A related instrument with its own open interest conventions
- [Volatility Smile](/volatility-smile/) — How open interest clusters shape the implied volatility curve
- [Securities and Exchange Commission](/securities-and-exchange-commission/) — The regulator requiring open interest disclosure

</div>
