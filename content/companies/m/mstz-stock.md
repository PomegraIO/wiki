---
title: "T-Rex 2X Inverse MSTR Daily Target ETF (MSTZ)"
description: "MSTZ aims to deliver twice the inverse (opposite) of MicroStrategy's daily price movement. It is a leveraged short vehicle for tactical trading; not suited for buy-and-hold investing."
keywords:
  - inverse ETF
  - leveraged short
  - MicroStrategy
  - daily rebalancing
  - volatility decay
  - tactical hedge
handwritten: true
---

*The **T-Rex 2X Inverse MSTR Daily Target ETF** (MSTZ) is a leveraged short fund designed to move in the opposite direction of MicroStrategy's stock price — specifically, to deliver roughly double the inverse daily return. It is a tactical instrument for traders who expect MicroStrategy to fall in the short term, not a long-term holding.*

---

## The mechanism: betting against MicroStrategy, with leverage

MSTZ does not own MicroStrategy shares. Instead, it uses derivatives — primarily [futures contracts](/futures-contract/) and swaps — to establish a short exposure with 2x leverage. On a day when MicroStrategy's stock falls 1%, the fund aims to deliver roughly a 2% gain. On a day when MicroStrategy rises 1%, the fund should lose roughly 2%. The "daily target" in the name signals the critical constraint: the fund rebalances every single trading day to reset its [leverage ratio](/leverage-ratio-forex/). This is not a set-and-forget instrument.

The mechanics are technical. The fund manager uses index futures on the MicroStrategy stock (or direct short positions in the stock via [prime brokerage](/prime-brokerage-venue/)) to construct the negative beta. The 2x multiplier is achieved by borrowing capital and deploying it alongside the fund's equity, much like a margin account. The borrowed money carries an implicit cost — the [repo rate](/repo-rate/) or swap financing cost — which is the fund's primary hidden friction.

---

## Why volatility decay kills leveraged inverses

Here is the brutal math. Suppose MicroStrategy swings sharply: up 2% one day, down 2% the next, ending where it started (flat over two days). A regular investor is flat. MSTZ aims for the inverse with leverage: down 4% on day one, up 4% on day two.

But here is what actually happens. If MSTZ is worth $100 on day zero:
- **Day one** (MSTR down 2%): MSTZ should gain 4%, reaching $104.
- **Day two** (MSTR up 2%): MSTZ should lose 4%, falling from $104 to $99.84.

The fund ends at $99.84, not $100. The underlying stock is flat; the fund has lost money. This is **volatility decay** — the tax that leverage pays to volatility, regardless of direction. The bigger and wilder the swings, the faster the decay happens.

For a volatile stock like MicroStrategy — daily moves of 3%, 5%, or larger are common — holding MSTZ for more than a few weeks is almost certain to result in losses even if MicroStrategy's price eventually moves sharply in MSTZ's favor. The document is silent on the historical impact, but it is a mathematical certainty for any leveraged inverse fund on a volatile underlying.

---

## Who uses MSTZ, and when?

MSTZ is a tool for a specific, limited purpose: a trader who expects MicroStrategy to fall sharply over a horizon of days, not weeks. A macro event — disappointing earnings, a scandal, a sudden shift in sector sentiment — might prompt a short-term seller to use MSTZ as a hedge or a short bet. The 2x leverage amplifies the payout on a sharp downward move.

It is emphatically not a "set it and forget it" investment. The combination of daily rebalancing, volatility decay, and the fund's structural deterioration in range-bound or choppy markets makes it unsuitable for anyone without a specific, short-dated thesis about MicroStrategy's direction.

Some institutional investors use leveraged [inverse ETFs](/inverse-etf/) tactically as portfolio hedges — buying MSTZ briefly when they expect a market shock — then selling after a few days or weeks. This is the intended use case. A retail investor holding MSTZ for months or years is almost guaranteed to suffer compounding losses even if they are right about the direction.

---

## The costs: expense ratio, and the true invisible drag

MSTZ carries an [expense ratio](/expense-ratio/) and a borrowing cost (the swap or repo financing embedded in the fund's returns). These are real but modest on a per-month basis. The true cost is volatility decay, which is invisible because it is not labeled as such — it simply erodes the fund's value day by day whenever the underlying stock moves, regardless of direction. The larger the daily swings, the faster the erosion.

The prospectus discloses this clearly: the fund is designed for short-term trading, and long-term returns are expected to significantly trail the inverse of MicroStrategy's long-term return.

---

## Tracking error and rebalancing mechanics

The fund's stated objective is to deliver 2x the inverse daily return. In practice, the fund typically tracks this target within a small margin of error on any single day — usually within 1–2% of the theoretical outcome — but tracking error can widen in unusual market conditions, especially if MicroStrategy gaps open or closes on news, or if derivatives markets become dislocated. The prospectus outlines the specific tracking-error band and the conditions under which it might widen.

Every evening, the fund rebalances: it adjusts its short position to reset the 2x leverage. This rebalancing is mechanical and daily, not discretionary. It is the engine of volatility decay: the fund is perpetually buying near local highs (to re-establish its short position after an up day) and selling near local lows (to reduce its short position after a down day).

---

## How to research MSTZ responsibly

Read the prospectus first. It is lengthy and technical, but it clearly states the fund's objectives, the rebalancing methodology, the risks, and the historical total return versus the inverse of MicroStrategy's return — which will show you the real drag volatility decay has caused.

Check the historical total return over various horizons: one week, one month, three months. Compare MSTZ's performance over each period to what you would expect from the inverse of MicroStrategy's price over the same period (roughly minus 2x MicroStrategy's return). The gap is volatility decay.

Use MSTZ only as a tactical position sized for the risk of rapid loss. Understand that leverage is not a free amplifier; it is a contract with volatility decay. No amount of skill or conviction about MicroStrategy's downward direction will overcome that structural headwind if you hold the fund for months. It is a tool for the next few days or weeks, not a multi-month or multi-year position.
