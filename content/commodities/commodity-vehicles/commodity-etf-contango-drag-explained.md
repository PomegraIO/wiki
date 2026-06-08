---
title: "Commodity ETF Contango Drag Explained"
description: "How upward-sloping futures curves erode commodity ETF returns through roll costs, even when spot prices rise."
keywords:
  - commodity etf contango drag
  - contango explained
  - futures roll costs
  - commodity futures etf losses
image: "/svg/commodities.svg"
---

*A **commodity ETF contango drag** occurs when an ETF holds futures contracts on an upward-sloping price curve—meaning near-term contracts trade below distant ones. As those near-term contracts approach expiry, the fund must sell them and roll into higher-priced contracts, systematically crystallizing losses that prevent the fund from capturing the underlying spot price gains.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Contango Drag — key facts</div>

<img src="/svg/commodities.svg" alt="An abstract editorial mark for commodities." />

<div class="wiki-infobox-caption">Upward-sloping curves force commodity futures ETFs to lock in losses at each roll.</div>

|   |   |
|---|---|
| **What it is** | Loss from rolling futures up a rising curve |
| **Why it happens** | Storage costs, carry, and supply/demand shift to future periods |
| **Who pays** | ETF shareholders via NAV erosion |
| **Magnitude** | Can subtract 5–15% annually in steep contango |
| **Affected funds** | Roll-based commodity ETFs ([ETFs](/etf/), [futures-contract](/futures-contract/) structures) |
| **Physical holdings** | Usually avoid it (no roll required) |

</aside>

## How Futures Rolling Creates the Cost

A roll-based commodity ETF—say, a crude oil or copper fund—owns futures contracts that expire in days or weeks. Rather than take physical delivery (or settle in cash at expiry), the fund's manager sells the expiring contract and buys a farther-out contract. If the far contract is more expensive than the near one, that sale-to-purchase sequence locks in a loss.

Consider a concrete example. On a given day, crude oil's December futures trade at $75, and March futures trade at $78. The ETF holds December at $75. In mid-December, as December nears expiry, the fund sells that December contract and buys March at $78. The three-dollar difference—roughly 4%—is realized immediately as a drag on the fund's net asset value. If crude's actual spot price stayed flat or even rose, the ETF still lost ground to that structural loss.

## The Term Structure of Commodity Futures

Why are far contracts more expensive? In **contango**, a market condition where [forward-contracts](/forward-contract/) trade higher than near-term ones, several factors pile up: storage costs for physical metal or oil, financing charges, convenience yield (the benefit of having the commodity on hand), and insurance. These costs accrete over time, so a contract six months out embeds six months' worth of carrying expense, while a one-month contract embeds only one month's.

The steeper the contango—the larger the gap between near and far contracts—the larger each roll loss. In certain years, crude oil has traded with $8–12 per barrel spreads between nearby and three-month contracts, turning a simple buy-and-hold strategy into a paper mill for losses.

## Rolling Frequency and Cumulative Impact

Most commodity ETFs employ a rolling schedule: they might roll 20% of their holdings every few days over a two-week window, or use a staggered approach to minimize slippage and market impact. That continuous rolling means losses accrete repeatedly—not just once per year, but every month or every quarter, depending on the contract ladder.

Over a full year with a 3% annualized contango curve, a $10 billion fund rolls out losses of roughly $300 million before any changes in the commodity's actual market price. In steeper contango years, the drag can reach 10–15% annually, completely washing out spot-price appreciation.

## Real-World Erosion vs. Spot-Price Changes

The crucial insight is that **contango drag is independent of spot price movement**. If crude oil's spot price rises 20% in a year, but the market stays in steep contango, a roll-based crude oil ETF might show a 5% return (20% spot gain minus 15% roll losses). A physically-held fund, or a fund structured as a [closed-end-fund](/closed-end-fund/), would show the full 20% gain.

This is why many investors have reported holding commodity ETFs that underperform the commodity itself—a seemingly backwards outcome. It is not a market inefficiency; it is the cost of using leverage and roll-based [futures-contract](/futures-contract/) mechanics.

## Contango vs. Backwardation

When the market swings into **backwardation**—near-term contracts trading above far-term ones—the roll dynamic reverses. The fund sells the near contract at a premium and buys the far one at a discount, creating a gain. Backwardation boost can offset or exceed roll drag, and in certain commodities (like natural gas during supply squeezes), backwardation can deliver spectacular returns.

However, for decades, crude oil and most base metals have spent the bulk of their time in contango, making roll drag the structural reality for funds using [futures-contract](/futures-contract/) mechanics.

## Alternatives and Mitigation Strategies

Investors concerned about contango drag have a few options. A [physically-backed ETF](/etf/) in precious metals (like gold or silver) owns the metal directly, sidestepping roll costs entirely, though it faces storage and insurance expenses. Some funds employ a "laddered" or "smart rolling" algorithm designed to roll gradually or at moments of narrow spreads, shaving basis points off the cost.

Private [commodity-trading-advisor](/commodity-trading-advisor/) strategies and [hedge-fund](/hedge-fund/) approaches often time rolls or employ [algorithmic-trading](/algorithmic-trading/) to minimize execution costs. But for passive ETFs, contango drag is largely inescapable—it is baked into the structural cost of holding [futures-contract](/futures-contract/) exposure.

## See also

<div class="wiki-seealso">

### Closely related

- [Commodity Futures ETF vs Equity ETF: Key Differences](/commodity-futures-etf-vs-equity-etf/) — why commodity ETFs behave differently than stock ETFs
- [Futures Contract](/futures-contract/) — mechanics of expiry and settlement
- [Contango](/contango/) — definition of upward-sloping term structures
- [Backwardation](/backwardation/) — opposite condition and its effect on returns
- [ETF Premium/Discount](/etf-premium-discount/) — why ETF prices can diverge from NAV

### Wider context

- [Commodity Trading Advisor: How It Works](/commodity-trading-advisor-how-it-works/) — professional management of commodity exposure
- [Closed-End Fund](/closed-end-fund/) — alternative structure for commodity exposure
- [Commodity](/commodity-etf-contango-drag-explained/) — broad overview of commodity markets
- [Derivatives Hedging](/derivatives-hedging/) — using futures for protection

</div>