---
title: "Two-Sided Quote Obligation for Market Makers"
description: "Explains two sided quote obligation market maker rules: continuous bid and ask posting, minimum size, spread limits, and regulatory enforcement."
keywords:
  - two sided quote obligation market maker
  - market maker regulation
  - bid-ask spread requirement
  - designated market maker
  - liquidity provision rules
  - quote obligations NYSE NASDAQ
---

*A **two-sided quote obligation** is a regulatory requirement that designated **market makers** must post continuous buy (bid) and sell (ask) quotes simultaneously on an exchange, within strict limits on spread and time-in-force. This obligation ensures liquidity and price efficiency by forcing market makers to take both sides of trades, not just profit from favorable moves.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Two-Sided Quote Obligation — mechanics and rules</div>

<img src="/svg/trading.svg" alt="An abstract editorial mark for market structure." />

<div class="wiki-infobox-caption">Exchanges impose continuous quote obligations to prevent liquidity evaporation during volatile conditions.</div>

|   |   |
|---|---|
| **What must be posted** | Simultaneous bid and ask quotes for a security |
| **Minimum size** | Usually 100 shares for stocks; varies by exchange and order type |
| **Maximum spread** | Often capped at 1–5% of price or a fixed penny amount (depends on volatility bands) |
| **Time-in-force** | Must remain continuously active during market hours; exceptions for technical failures |
| **Enforcement** | Fines, trading halts, or removal of market-maker designation |
| **Covered securities** | Typically stocks, some ETFs; OTC markets have looser rules |
| **Exemptions** | Periods of extreme volatility, illiquidity, or system failures |

</aside>

## Why Two-Sided Quotes Exist

Without a two-sided quote obligation, a market maker could post only a profitable bid (in a downtrend) or only an ask (in an uptrend), pocketing spread profits without assuming risk. Worse, during sharp rallies or crashes, market makers could vanish entirely, leaving retail traders and institutions stranded with no way to execute.

The two-sided requirement forces market makers to be true intermediaries: they must absorb shares when sellers hit their bid, and provide shares when buyers hit their ask, regardless of whether they think the price will move in their favor next. This is their compensation for the risks they take (inventory risk, adverse selection, opportunity cost).

Two-sided quotes also enhance price discovery. Because bids and asks are always present, the "true" midpoint price reflects constant negotiation between buyers and sellers, not just the one-directional quotes of an informed trader trying to position.

## How It Works in Practice

On the New York Stock Exchange (NYSE), market makers (called "specialists" or "designated market makers," DMMs) are obligated to post bids and asks on every stock they are assigned. The spread must not exceed certain thresholds, which vary by the stock's price and volatility.

For a \$50 stock trading normally, a DMM might post:
- Bid: \$49.98
- Ask: \$50.02
- Spread: \$0.04 (less than 1% of price)

If a large seller arrives and hits the bid, the DMM must absorb shares at \$49.98, even if they believe the stock could fall further. Conversely, if a buyer hits the ask, the DMM must provide shares at \$50.02.

On NASDAQ, market makers ("market participants") also post two-sided quotes, but the exchange uses a competing market-maker model rather than a single designated specialist. Multiple market makers post quotes for the same stock, creating competition. The best bid and ask across all market makers form the "national best bid and offer" (NBBO), which is the price retail traders see and brokers are required to route to.

## Minimum Size and Depth

The minimum quote size (the number of shares a market maker must be willing to buy or sell at their posted price) typically matches the round lot size for equities—100 shares. This is called "level 1" liquidity.

Larger traders often demand more liquidity. Exchanges and market makers may post multiple "levels":
- Level 1: 100 shares at the best bid/ask
- Level 2: 300 more shares at slightly worse prices
- Level 3+: large institutional order books

The obligation to post minimum size ensures that retail orders (100 shares or less) can fill at the quoted price, but large institutional trades may have to accept worse prices if they demand more shares than are available at the best level.

## Spread Limits and Volatility Bands

Spread limits vary by exchange, stock price, and market conditions. The SEC has published guidance that ties maximum spreads to volatility:

- **Normal conditions:** For a mid-cap stock, spreads might be capped at $0.01–$0.05.
- **Elevated volatility:** The cap may widen to $0.10–$0.25 to allow market makers to compensate for higher inventory risk.
- **Extreme volatility or liquidity crises:** Exchanges may temporarily suspend quote obligations to prevent market makers from withdrawing entirely.

During the COVID-19 crash in March 2020, some stocks saw bid-ask spreads widen to 5–10% as market makers pulled back. Regulators have since debated whether tighter spread obligations help or harm liquidity during stress.

## Time-in-Force and Continuous Obligation

Market makers must maintain their quotes continuously during regular trading hours (9:30 a.m. to 4:00 p.m. ET for US stocks). They cannot "cherry-pick" when to be a market maker, posting quotes only when conditions favor them.

However, there are narrow exceptions:
- **Technical failures:** If their trading system crashes, they are excused temporarily.
- **Extreme volatility:** An exchange may declare a "level 2" or "level 3" trading halt, suspending quote obligations.
- **Wide quotes during stress:** Regulators allow wider spreads when markets are stressed, acknowledging that market makers face real inventory risk.

A market maker who repeatedly fails to post or who withdraws quotes without justification faces fines, sanctions, or loss of their market-maker status and associated rebates.

## Economic Trade-Off for Market Makers

The two-sided obligation is a bargain. In exchange for bearing inventory risk and spread losses, market makers receive:

- **Rebates or priority**: Exchanges pay market makers small rebates per share for adding liquidity.
- **Information advantage**: They see flow early, allowing them to adjust quotes before price moves.
- **Profitability at scale**: Even a $0.01 spread on millions of shares generates significant revenue.

On high-volume stocks, market makers can be profitable despite the obligation. On low-volume or volatile stocks, the obligation can be costly, and fewer market makers volunteer to handle those stocks.

## Exceptions and Circuit Breakers

When a stock moves very sharply—typically 10% or more in a short period—the SEC's "circuit breaker" rules may halt trading. During a halt, quote obligations are suspended. This prevents market makers from being forced to trade at prices that reflect stale information.

Similarly, during an exchange-wide trading halt (if the S&P 500 falls 7%, 13%, or 20%), all quote obligations are suspended until trading resumes.

## Global Variation

The two-sided obligation is not universal. In the EU, MiFID II requires "liquidity providers" (similar to market makers) to post continuous quotes, but the rules are less prescriptive than US rules. OTC markets (like forex or corporate bonds) have much looser requirements, relying instead on tradition and reputation.

## See also

<div class="wiki-seealso">

### Closely related

- [Market Maker Trading](/market-maker-trading/) — the business model underlying two-sided quotes
- [Bid-Ask Spread](/bid-ask-spread/) — the cost of liquidity to traders
- [Stock Exchange](/stock-exchange/) — venue enforcing quote obligations
- [Price Discovery](/price-discovery/) — how two-sided quotes improve market efficiency
- [Limit Order](/limit-order/) — orders that interact with market maker quotes

### Wider context

- [Stock Market](/stock-market/) — the broader structure where two-sided quotes operate
- [Securities and Exchange Commission](/securities-and-exchange-commission/) — regulator enforcing rules
- [Liquidity Risk](/liquidity-risk/) — what happens when market makers are absent
- [Over the Counter Market](/over-the-counter-market/) — less-regulated alternative to exchanges

</div>
