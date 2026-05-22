---
title: "Lock Limit Rules"
description: "Limits on daily price movements in commodity and futures markets; when prices gap-limit-up or gap-limit-down, trading halts."
keywords:
  - circuit-breaker
  - daily-limit
  - futures-halt
  - commodity-trading
  - price-control
---

*[Lock Limit Rules](/wiki/lock-limit-rules/) (or daily limit rules) cap the maximum price movement allowed in a single trading day for [commodity](/wiki/commodity-futures-trading-commission/) and [futures contracts](/wiki/futures-contract/). When a contract hits its daily limit, trading halts — a "lock-limit" — until the next session or until market sentiment shifts. The rule is intended to prevent panic-driven cascades but also constrains price discovery.*

<aside class="wiki-infobox">

| Item | Detail |
|------|--------|
| **Typical limit** | 10–20% of prior settlement price |
| **Varies by** | Commodity, contract month, exchange rules |
| **Triggered by** | A single trade at limit price or consecutive trades |
| **Effect** | Trading halts at limit-up or limit-down |
| **Holder risk** | Position locked; can't exit; forced to ride it out |
| **Exceptions** | Some exchanges allow "limit-only" orders outside normal hours |

</aside>

## How daily limits work

Each commodity futures contract has a **daily limit** — the maximum price movement above or below the prior day's settlement price. For example:

- **Corn futures:** Limit of $0.30/bushel (15% of a typical $2/bu price). If Dec corn closed at $4.00 and opens at $4.29, it has hit limit-up. No trades occur above $4.29.
- **S&P 500 E-mini futures:** Limit of 5% on the ES contract (though larger during volatility). If the ES closes at 4,000 and gaps to 4,200 (+5%), it locks limit-up.
- **Crude oil:** Historically had a $2.00/bbl limit; recently increased to $10/bbl (50% of typical price) due to [2020 crashes](/wiki/oil-crisis-1973/).

When a contract **locks limit-up** (hits the upper limit), no sales occur above that price. When it locks **limit-down** (hits the lower limit), no purchases occur below that price.

## Intended purpose: panic prevention

Daily limits exist to prevent panic-driven selling cascades. In a 1987-style [crash](/wiki/black-monday-1987/), if crude oil falls 20% in one hour, panicked holders rush to sell, causing further cascade. A daily limit of ±$3/bbl forces a pause: traders can't exit in one day, circuit-breaker psychology sets in, and the market has time to stabilize before the next day's opening.

Advocates argue limits reduce volatility and prevent market dislocations. Critics argue limits *trap* liquidity — a holder facing forced liquidation cannot exit; they're stuck holding a position they want to sell.

## Lock-limit episodes and contagion

A dramatic example occurred in crude oil in April 2020, when storage filled up due to demand collapse during lockdown. The May crude contract fell so sharply that it **locked limit-down** multiple times. Traders holding long positions couldn't sell; some took delivery of actual barrels (70,000 bbl tankers showed up at Cushing, OK, requiring emergency storage). The June contract then came under pressure as front-month traders rolled positions forward.

Similarly, soybean prices gap-limit-down when crop reports show supply surges; cattle prices limit-up during disease outbreaks.

## The trader's dilemma: liquidity vs. price discovery

A holder of 100 corn contracts (+3,000 bu) wants to exit before a bad harvest report. The market opens limit-down (can't sell). The holder is forced to hold through the gap, absorbing the loss. On the next day, the contract opens at the previous limit-down, possibly limit-down again. Over several days, the holder may unwind at terrible prices.

Conversely, price limits can mask true equilibrium. If crude "should" fall 25% on a massive supply shock, forcing a two-day halt while the market rebalances distorts the discovery process and imposes real costs on end-users (refineries can't hedge properly, futures prices deviate from physical markets).

## Variations in limit policy

Different exchanges and commodities use different approaches:

- **CBOT (Chicago Board of Trade):** Corn and soybeans have ±$0.30/bu limits, except on the last day (no limit to allow final settling).
- **CME (Chicago Mercantile Exchange):** Cattle (LC) and hog (LH) contracts have ±$0.04/lb limits.
- **Crude oil (NYMEX):** Historically $10/bbl; emergency rules can suspend during extreme volatility.
- **Stock index futures (ES, NQ):** Tier-1 limits at ±7%, tier-2 at ±13%, tier-3 can suspend for the day.

### Exception: no limit on last trading day

Most contracts remove daily limits on the final day (last notice day or cash settlement day) to allow markets to converge to the true spot price. This creates a "flash" of volatility on the final day but ensures the contract settles at fair value.

## Relationship to circuit breakers

Daily limits in futures differ from [circuit breakers](/wiki/circuit-breaker/) in equities:

- **Futures daily limits:** Exchange-enforced; automatic; apply to individual contracts.
- **Equity circuit breakers:** Whole-market halts triggered by S&P 500 falling 7%, 13%, or 20% intraday. Designed to slow panic, not to cap daily moves.

Equity circuit breakers are softer (15-minute halts) and market-wide; futures daily limits are hard (trading halts) and contract-specific.

## Policy debates: relax or tighten?

Post-2008 financial crisis and 2020 COVID crash, regulators debate whether daily limits are too tight (prevent efficient hedging) or too loose (allow cascades). Some argue:

- **Relax limits:** Modern trading is more liquid; forced pauses distort price discovery and create holding costs.
- **Tighten limits:** Volatility has increased; wider bands would reduce panic leverage and corner-market risk.

The CME periodically adjusts limits based on volatility. Crude oil limits expanded in 2020 in response to the May crash.

## Who benefits and who loses

**Beneficiaries of lock limits:**
- Farmers hedging crops (prevent panic-driven cascades destroying their [hedge](/wiki/hedging-with-futures/)).
- Market-makers with long-term mandates (prevents flash crashes that trigger margin calls).

**Losers from lock limits:**
- Short-term hedgers needing to exit immediately (locked in losses).
- End-users of commodities (refineries, flour mills) who can't hedge properly during limits.
- Spread traders ([carrying](/wiki/carry-trade/) calendar spreads) who face basis risk when front/back months move asymmetrically.

<div class="wiki-seealso">

### Closely related

- [Circuit Breaker](/wiki/circuit-breaker/) — equity market halt rules
- [Futures Contract](/wiki/futures-contract/) — underlying vehicle
- [Daily Limit](/wiki/lock-limit-rules/) — price cap per day
- [Hedging with Futures](/wiki/hedging-with-futures/) — hedger vulnerability to limits

### Wider context

- [Commodity Futures Trading Commission](/wiki/commodity-futures-trading-commission/) — regulator
- [Black Monday 1987](/wiki/black-monday-1987/) — crash that motivated circuit breakers
- [Flash Crash 2010](/wiki/flash-crash-2010/) — modern volatility episode
- [Market Surveillance](/wiki/market-surveillance/) — exchange oversight of trading

</div>
