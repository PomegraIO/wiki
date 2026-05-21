---
title: "Market maker"
description: "A market maker is a firm that buys and sells securities continuously, standing ready to trade at their quoted bid and ask prices. They profit from the spread and provide liquidity, which makes them essential to smooth market functioning."
keywords:
  - market maker
  - liquidity provider
  - bid-ask spread
  - trading
image: "/svg/trading.svg"
---

*A **market maker** is a trading firm or individual that continuously quotes both a **bid** (buy price) and an **ask** (sell price) for a security. When you place a [market order](/market-order), a market maker is usually the counterparty — they sell you shares if you are buying, or buy your shares if you are selling. They profit from the bid-ask spread (the gap between their buy and sell prices) and lose when the price moves against them. Market makers are essential: they provide liquidity and enable trading to happen.*

<div class="wiki-hatnote">

For the role of market makers in exchanges, see [lit venue](/lit-venue). For orders that rest in the book waiting for market makers, see [limit order](/limit-order).

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Market maker — key facts</div>

<img src="/svg/trading.svg" alt="A trader surrounded by bid and ask quotes" />

<div class="wiki-infobox-caption">Market makers continuously quote bid and ask, profiting from the spread.</div>

|   |   |
|---|---|
| **What they do** | Quote buy (bid) and sell (ask) prices continuously |
| **Profit source** | The spread (ask − bid) and inventory management |
| **Loss source** | Price moving against their inventory; adverse selection |
| **Essential to** | Liquidity, tight spreads, continuous trading |
| **Regulation** | Heavily regulated; designated market makers on exchanges |

</aside>

## How market makers profit

Market makers make money in two ways:

**Spread profit:** They quote a bid and ask with a gap. Buy at $50.00, sell at $50.01. Every time they buy and sell, they pocket the $0.01. Over millions of shares, the spread is substantial.

**Inventory management:** If they accumulate too much inventory (hold too many shares), they adjust their quotes lower to sell off the excess. If they run low, they adjust higher to buy more. They trade the difference: buy low, sell high.

**Risk/loss:** If the price moves sharply against their inventory (they bought at $50.00, but the stock falls to $49.50), they take a loss.

## Market makers vs. traders

| Role | Buys and sells | Goal | Time horizon | Risk tolerance |
|---|---|---|---|---|
| **Market maker** | Continuously | Profit from spread and inventory | Seconds to minutes | High (holds inventory) |
| **Trader** | Opportunistically | Profit from price moves | Minutes to months | Varies |

Market makers are always in the game; traders enter and exit based on opportunity.

## Types of market makers

**Exchange-designated market makers:** On the NYSE, there is a designated market maker (DMM) for each stock. They have special obligations (must quote during stressed times) and special privileges (fee discounts).

**Electronic market makers:** Most [options](/option) and futures venues have market makers who trade via algorithms on computers, continuously updating quotes.

**Retail traders:** Some retail traders use market-maker accounts (if their broker allows) to quote prices and earn the spread.

**High-frequency traders:** Modern HFTs are essentially market makers, quoting continuously and profiting on the spread.

## Spreads and market quality

The spread a market maker quotes reflects:
- **Demand for liquidity:** High demand → wide spreads (market maker compensates for risk).
- **Volatility:** More volatile → wider spreads (market maker protects against losses).
- **Competition:** Many market makers → tight spreads (they compete on price).
- **Liquidity:** More available shares at each price → tighter spreads.

In a liquid stock (Apple, Microsoft), spreads might be 1 cent. In a thinly traded stock, spreads might be 5–10 cents or more.

## Market makers and adverse selection

Market makers face a risk called **adverse selection**: informed traders take their orders against you when they know the price is moving.

**Example:** You are a market maker quoting Apple at bid $150.00, ask $150.01. A trader who knows bad news is coming (insider, or someone who read the pre-earnings whisper) comes and sells you 100,000 shares at $150.00. Seconds later, Apple crashes to $149.00, and you are stuck holding 100,000 shares worth $100,000 less.

To protect against adverse selection, market makers:
- **Widen spreads** in volatile times or around earnings.
- **Reduce size** (only quote small quantities).
- **Use algorithms** to detect informed order flow and adjust prices.

## Market maker obligations and regulations

On major exchanges, market makers have obligations:

**NYSE:** The Designated Market Maker must:
- Quote during trading hours.
- Be present (physically or electronically) for the opening and closing auctions.
- Provide liquidity in stressed markets.

In return, they get fee breaks and rebates.

**SEC and FINRA:** Market makers are regulated to prevent:
- Manipulation (artificially moving prices).
- Fraud (misquoting prices intentionally).
- Insufficient capital (they must have enough cash to cover positions).

## High-frequency trading and market making

Modern [high-frequency traders](/high-frequency-trading) operate as electronic market makers: they quote continuously on thousands of stocks, execute thousands of trades per second, and rely on speed and scale to profit from the spread.

Concerns about HFT-based market making:
- **Flash crashes:** Rapid unwinding of positions can move markets sharply.
- **Information asymmetry:** HFTs may have latency advantages that give them faster information.
- **Fairness:** Regulations like trade-through rules exist partly to ensure HFTs do not prevent retail traders from getting best prices.

## Market makers and retail traders

For retail traders, market makers are usually helpful:
- **Tight spreads:** Their competition keeps spreads small.
- **Instant execution:** Your [market order](/market-order) fills against a market maker in milliseconds.
- **Continuous trading:** You can trade anytime during market hours, even in low-volume securities, because market makers stand ready.

However, retail traders should be aware:
- **Conflicts of interest:** Some brokers that execute retail orders through their own market-making desk may have incentives to pay poor prices. Regulations (like best execution rules) limit this, but it is a known risk.
- **Payment for order flow:** Some brokers sell their retail order flow to market makers (usually for a small rebate), which can create conflicts.

## When market makers fail

In crashes and market stress, market makers may:
- **Pull liquidity:** Stop quoting or quote very wide spreads.
- **Go insolvent:** If losses exceed capital, they fail.
- **Cause cascades:** If a major market maker fails, it can reduce liquidity for other traders.

The **2008 financial crisis** and the **2020 COVID crash** both had moments when market makers temporarily pulled back, causing liquidity to evaporate and spreads to widen dramatically.

## See also

<div class="wiki-seealso">

### Closely related

- Bid-ask spread — profit source for market makers
- Liquidity — market makers provide this
- [Market order](/market-order) — executes against market makers
- Order book — where market makers post quotes

### Market structure

- [Lit venue](/lit-venue) — exchanges rely on market makers
- [High-frequency trading](/high-frequency-trading) — modern market makers
- [Dark pool](/dark-pool) — market makers also operate here
- Designated market maker — special role on NYSE

### Execution and costs

- [Best execution](/best-execution) — brokers must route for best prices vs. market makers
- [Payment for order flow](/payment-for-order-flow) — brokers sell retail flow to market makers
- Slippage — cost when market makers quote wide

### Risk and regulation

- Adverse selection — risk market makers face
- Flash crash — when market makers pull liquidity
- Market manipulation — regulated against

</div>
