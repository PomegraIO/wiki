---
title: "Restricted Shares vs Free Float"
description: "Restricted shares vs free float clarifies which share categories are excluded from tradeable float, affecting index inclusion and liquidity."
keywords:
  - restricted shares
  - free float
  - share availability
  - index inclusion
  - insider holdings
  - lock-up period
---

*The **restricted shares vs free float** distinction separates shares that can be freely traded from those locked up by insiders, employees, or regulators. This matters because indexes and brokers use free float—not total shares outstanding—to measure a stock's true trading liquidity and determine inclusion eligibility.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Restricted Shares vs Free Float — key facts</div>

<img src="/svg/equity.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">The gap between outstanding shares and tradeable shares determines real market liquidity.</div>

|   |   |
|---|---|
| **Free Float** | % of shares available to trade; excludes insider, employee, and government holdings |
| **Restricted Shares** | Shares legally or contractually barred from open-market sale for a defined period |
| **Lock-up Window** | 180 days typical post-IPO; enforced by underwriter agreement, not law |
| **Index Weight** | Calculated on free-float market cap, not total market cap |
| **Why it Matters** | Lower float = wider bid-ask spreads, less liquidity, easier price moves |

</aside>

## What Counts as Restricted

Not all shares outstanding can hit the market on any given day. **Restricted shares** fall into a few categories.

**Insider holdings and lock-ups** are the most visible. When a company goes public, the underwriter imposes a contractual lock-up on founders, executives, and early investors—typically 180 days (six months). They literally cannot sell shares until that window closes. After lock-up expires, insiders *can* sell, but those shares still aren't part of free float as long as insiders hold them. If a founder owns 20% of a company post-IPO, that entire stake is "restricted" from the market-at-large because one person controls it and could dump it anytime.

**Employee stock options and RSUs** create similar friction. Vesting schedules lock up compensation for years. Unvested shares don't exist yet, so they're not in float; vested but unexercised options are contingent holdings. The moment an employee exercises or vests, the stock enters the available supply, but the *vesting schedule* itself constrains the timing.

**Government and strategic holdings** operate the same way. If a country owns 15% of a bank's shares post-privatization, or a corporate parent holds a significant stake in a subsidiary, those blocks are functionally off-market even if they're not legally restricted. Institutional holders with long lock-up agreements (via secondary offerings or direct placements) also reduce float.

## How Indexes and Market Data Calculate Free Float

**Free float** is a percentage. Stock exchanges and index providers (S&P, MSCI, FTSE) calculate it by taking total shares outstanding and subtracting restricted shares, then dividing:

```
Free Float % = (Shares Outstanding – Restricted Shares) / Shares Outstanding
```

A company with 100 million shares outstanding and 35 million held by insiders, employees (vesting), and the government has a free float of 65%. Only those 65 million shares represent genuinely available supply for the market.

This matters for index inclusion. The S&P 500, for example, has *explicit* free-float thresholds. A stock must have at least 10–15% free float (rules vary by index) to be eligible. A successful startup with one dominant founder/investor might have only 40% free float, making it ineligible for major indexes even if it meets size thresholds. Once enough insiders sell or vest schedules dilute their ownership, free float rises and the stock qualifies.

Market data vendors (Bloomberg, FactSet) publish free-float percentages for every major public stock. Most charting and analysis platforms use free-float market capitalization, not raw market cap, to weight portfolio positions and indexes.

## The Liquidity Consequence

Free float directly shapes trading friction. A stock with 50 million shares outstanding but 40 million in insider hands has only 10 million tradeable shares—a very thin float. Bid-ask spreads widen. An institutional investor wanting to accumulate a large position may struggle to find sellers without pushing the price up significantly. Conversely, unexpected insider selling into that thin float can trigger sharp price declines.

This is why small-cap and micro-cap stocks often show violent daily moves. Many have extremely low free floats (sometimes under 5 million shares). A single block trade can move the price 5% or more. In contrast, a mega-cap like Apple or Microsoft has billions in free float, so a single trade barely registers.

Retail traders sometimes exploit low-float situations intentionally, betting that limited supply will amplify any buying enthusiasm. Market regulators keep an eye on these names because pump-and-dump schemes thrive in low-liquidity stocks.

## Lock-Up Expiration and "Lock-Up Pop"

When an IPO lock-up expires, insiders can finally sell. Investors often anticipate a flood of insider selling, causing the stock to decline just before or immediately after expiration. This is called a "lock-up overhang."

However, the opposite sometimes happens: **lock-up pop**. If the stock has performed well and insiders believe in the company, they may hold shares post-expiration. The market interprets insider confidence as bullish, and the stock rises. The dynamic depends entirely on company fundamentals, market sentiment, and insider communication.

Sophisticated investors track lock-up calendars closely. A large insider stake at expiration signals a huge potential influx of supply that could depress price. Conversely, if insiders *don't* sell at expiration, it's a strong bullish signal.

## Restricted vs Unrestricted: Legal Clarity

In securities law, **restricted securities** are those not registered with the SEC and not freely tradeable. They come from private placements, founder grants, or employee compensation packages. Selling restricted securities without registration violates securities laws unless an exemption (Rule 144, Form 4 filings by officers) applies.

**Unrestricted securities** are registered and freely tradeable. Nearly all publicly traded shares are unrestricted once they leave insider accounts. The term "restricted" in everyday usage refers to contractual or practical constraints (lock-ups, vesting), not legal registration status.

This distinction matters most around IPOs and secondary offerings where Form S-3 or Form S-1 filings spell out exactly which shares are restricted and for how long.

## Free Float and Index Rebalancing

Index managers recalculate free float quarterly or annually, adjusting index weights accordingly. If a company's free float drops (because insiders buy back shares or a large block gets locked up contractually), its index weight shrinks even if total market cap stays flat. This forces index funds to rebalance, selling shares of the company and rotating into others.

Conversely, free float can expand if a founder finally sells a large stake, adding supply to the market and increasing the stock's index weight. The mechanical buying and selling tied to free-float changes sometimes creates predictable trading patterns that sophisticated traders exploit.

## Why Investors Care

A low free-float stock is harder to build a large position in without moving the price. Institutional investors running indexing or factor strategies need liquidity; low-float names are often excluded from their universes regardless of fundamental quality. 

For active traders and short-sellers, low float is a feature, not a bug. Shorting a stock is harder when float is tight (fewer shares to borrow); going long is easier when enthusiasm can move prices higher on limited supply.

The free-float metric also signals concentration risk. If 80% of a company is owned by insiders or the government, the business is less *liquid* even if it's fundamentally sound. A sudden shift in insider sentiment or regulatory action could create forced selling and sharp declines.

## See also

<div class="wiki-seealso">

### Closely related

- [Stock](/stock/) — equity shares and their characteristics
- [Share Buyback](/share-buyback/) — when a company repurchases its own stock, reducing free float
- [Initial Public Offering](/initial-public-offering/) — the IPO process and post-IPO lock-ups
- [Market Capitalization](/market-capitalization/) — how free-float market cap differs from total cap
- [Insider Holdings and Restricted Stock Units](/restricted-shares-vs-free-float/) — vesting schedules and lock-up mechanics
- [Index Fund](/index-fund/) — how free-float rules determine fund holdings
- [Liquidity Risk](/liquidity-risk/) — trading friction in low-float securities

### Wider context

- [Stock Exchange](/stock-exchange/) — where shares trade and liquidity is priced
- [Bid-Ask Spread](/bid-ask-spread/) — the cost of trading illiquid securities
- [Price Discovery](/price-discovery/) — how supply and demand set share prices
- [Securities and Exchange Commission](/securities-and-exchange-commission/) — regulatory rules on restricted securities

</div>
