---
title: "Floor Broker vs Electronic Order Routing"
description: "Floor brokers execute large, complex orders on exchanges through human judgment and relationships. Electronic routing is faster and cheaper for standardized trades but lacks discretion for difficult orders."
keywords:
  - floor broker vs electronic order routing
  - floor broker execution
  - electronic order routing
  - block trading
  - order execution methods
  - market venues
image: "/svg/markets.svg"
---

*The choice between a **floor broker** and **electronic order routing** hinges on order size, complexity, and time sensitivity. A floor broker is a human on the exchange floor who uses judgment, market knowledge, and relationships to execute large or unusual orders while managing market impact. Electronic routing is automated, near-instantaneous, and ideal for standard-sized trades. Each persists because they solve different problems.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Floor Broker vs Electronic Routing</div>

<img src="/svg/markets.svg" alt="An abstract editorial mark for market venues." />

<div class="wiki-infobox-caption">Different tools for different order sizes and complexity.</div>

|   | Floor Broker | Electronic Routing |
|---|---|---|
| **Speed** | Seconds to minutes | Milliseconds |
| **Order size** | Large blocks (millions) | Small to mid-size (up to hundreds of thousands) |
| **Discretion** | High; human judgment | None; algorithmic/predefined |
| **Cost** | Higher per share, lower for large blocks | Lower commission, no ticket fee |
| **Complexity** | Handles unusual, multi-leg orders | Standard buy/sell only |
| **Confidentiality** | Can be preserved through negotiation | Exposed to electronic feeds |
| **Skill required** | High; relationships matter | Minimal; order sits in queue |

</aside>

## The Floor Broker: Human Judgment at Scale

A floor broker is a licensed trader physically present on an exchange floor (such as the New York Stock Exchange) or operating via direct telephone lines, tasked with executing orders on behalf of clients. The broker uses personal relationships with other traders, real-time market observation, and judgment to manage the execution of large or complex orders.

### When Floor Brokers Thrive

Floor brokers are essential for:

**Large block orders** (millions of shares): Releasing a million-share order into the electronic market at once would cause a price collapse, cascading losses for the client. A floor broker instead *works* the order—selling portions of it over time, in different venues, at different prices—to minimize market impact. The broker might place 50,000 shares here, wait for the bounce, sell 75,000 there, negotiate a private trade for another 200,000, repeatedly throughout the day. The goal is to get a better average execution price than hitting the electronic market with the full order.

**Complex, multi-leg orders**: An order to simultaneously buy 500K shares of Stock A, sell 300K of Stock B, and buy 200K of a call option on Stock C is difficult to split across electronic venues. A floor broker understands the dependencies, can negotiate terms with counterparties, and executes with judgment.

**Uncertain liquidity**: A trader wants to sell 250K shares of a thinly traded stock. The electronic market may not have enough bids to absorb the order without causing a severe price drop. A floor broker can canvas the market (phones, relationships), find willing buyers, and structure a trade.

**Sensitive corporate actions**: A major shareholder is divesting shares, and revealing the full order size could trigger panic selling. A floor broker can maintain confidentiality—the shares are sold quietly through multiple channels—whereas an electronic order is immediately visible to all market participants.

### The Cost of Floor Brokerage

Floor brokerage is expensive. A broker charges a commission (per share or per trade), typically ranging from $0.001 to $0.01 per share, plus a ticket charge of $10–$100 per trade, depending on size and complexity. For a 500K-share trade at $0.005 per share, the cost is $2,500 in commissions alone. This seems high compared to electronic routing, but for a block order, the floor broker's price improvement (better average execution) often more than offsets the fees.

Example: An institution wants to sell 500K shares of a stock trading at $50. An electronic market order might average $49.70 due to market impact (slippage). The institution nets $24.85M. A floor broker, working the order skillfully, might average $49.85, for a net of $24.925M—a $75K gain, easily offsetting a $2,500 brokerage fee.

## Electronic Order Routing: Speed and Transparency

Electronic order routing is the default for most modern trades. An investor submits a buy or sell order via a brokerage platform or trading system; the order is instantly routed to one or more exchanges (NYSE, Nasdaq, alternative trading systems) in milliseconds and is filled against available buyers or sellers.

### How It Works

1. An order enters the [broker's](/broker/) system.
2. The order is routed to the best available market (the exchange or venue with the best price and liquidity).
3. The order sits in the central limit order book until a matching order arrives.
4. The trade executes automatically at the posted price.
5. The fill is confirmed back to the trader in milliseconds.

No human intervention, no negotiation, no delay.

### Cost Structure

Electronic commissions are minimal: $0–$5 per trade for retail investors, or a flat fee ($0–$1) per 100 shares for institutional traders. There's no ticket charge and no per-share commission (unless trading micro-cap penny stocks, which carry higher fees). For standard-sized orders, electronic routing is far cheaper than floor brokerage.

### Limitations of Electronic Routing

The speed and automation come with tradeoffs:

**Limited order size**: Electronic markets work well for orders up to a few hundred thousand shares, depending on liquidity. Submitting a multi-million-share order electronically exposes the full size to the market immediately, triggering front-running, market-making adjustments, and slippage. The average execution price suffers.

**No discretion**: An electronic order cannot be modified mid-execution based on market conditions. The system fills at available prices with no judgment. If slippage occurs, the trader bears the loss.

**Transparency**: The order is visible to market participants via [price discovery](/price-discovery/) mechanisms. This can trigger unwanted price movement if the order size is perceived as a sign of institutional demand or distress selling.

**Non-standard orders**: An electronic system handles buy/sell in round or fractional shares only. Orders requiring custom conditions (e.g., "sell only if the 50-day moving average is above the price") are not natively supported; they must be split manually or routed to a specialized venue.

## Execution Algorithms: A Middle Ground

Modern trading has spawned algorithmic execution—a hybrid. An institution's algorithm receives a large order and breaks it into smaller electronic orders, timed and sized to minimize market impact.

Example: A $50M institutional order to sell 500K shares is given to an execution algorithm. The algorithm:
- Estimates intra-day volume patterns.
- Breaks the order into 50 smaller orders of 10K shares each.
- Releases orders at intervals throughout the day, adjusting pace based on real-time volume.
- Targets a lower price impact than a single block trade.

The advantage: it's cheaper than a floor broker (algorithm cost is typically $500–$2,000) and faster than manual floor brokerage. The disadvantage: it's still mechanical; a skilled floor broker with real-time intuition might achieve better results in unpredictable markets.

## When Each Makes Sense: A Decision Matrix

| Scenario | Preferred | Reason |
|----------|-----------|--------|
| Buy 100 shares of Apple | Electronic | Speed, minimal cost, ample liquidity |
| Sell 1M shares of a liquid stock | Floor broker or algorithm | Block size; minimize market impact |
| Buy 50K shares of a thinly traded stock | Floor broker | Uncertain liquidity; broker finds buyers |
| Execute a complex 3-leg order | Floor broker | Requires judgment and coordination |
| Urgent position need to liquidate by day's end | Electronic or algorithm | Speed is critical; accept slippage |
| Sensitive divestiture (avoid tipping off market) | Floor broker | Confidentiality, relationships protect information |

## Regulatory and Structural Context

The rise of electronic markets has marginalized floor brokers. In 1990, most large trades went through the floor of the NYSE or regional exchanges. Today, the NYSE floor is largely ceremonial; most trading is electronic. However:

- **Hybrid venues**: Some exchanges maintain hybrid systems where electronic orders coexist with floor brokers; the two systems interact.
- **Alternative Trading Systems (ATS)**: These electronic venues operate off-exchange and handle large blocks via special mechanisms, retaining some floor-broker-like functionality (e.g., a broker can negotiate a price privately before executing).
- **Block trading desks**: Large brokerage firms maintain dedicated teams (often remote, but functionally equivalent to floor brokers) who negotiate block trades off-exchange or via ATS, using judgment and relationships.

## Cost-Benefit Analysis: Slippage vs. Fees

The core tradeoff is transparent: does the price improvement from floor brokerage outweigh the fees?

**Slippage** is the difference between the order price and the actual average execution price due to market impact.

Example:
- **Electronic order**: 500K shares, market price $50.00, electronic order results in average fill of $49.70 (30¢ slippage). Total loss: $150,000. Brokerage fee: $5. Net cost: $150,005.
- **Floor broker**: Same 500K shares, floor broker achieves average fill of $49.88 (12¢ slippage). Total loss: $60,000. Brokerage fee: $2,500. Net cost: $62,500.

The floor broker saves $87,500 on this single trade. Over a portfolio of large institutional orders, the cumulative advantage is material.

For small orders (under 50K shares), the math flips. Slippage is minimal; the 30¢ loss is modest. The floor broker fee ($500–$1,000) is not justified. Electronic execution is cheaper overall.

## Future Trajectory

Electronic markets continue to improve:
- **Smart order routing**: Brokers' systems automatically split orders across multiple venues to minimize impact.
- **Execution algorithms** that learn patterns and optimize timing.
- **Increased transparency** in execution prices and timing, reducing the need for a broker's subjective judgment.

Floor brokers and block trading desks are now a niche service, relevant primarily for:
- Billion-dollar institutional orders.
- Highly illiquid securities (penny stocks, distressed debt, private equity stakes being sold).
- Confidential or sensitive transactions where discretion is critical.

For the vast majority of modern traders—retail and small institutional—electronic routing is the only practical choice.

## See also

<div class="wiki-seealso">

### Closely related

- [Broker](/broker/) — the intermediary role and regulatory framework
- [Alternative trading system](/alternative-trading-system/) — electronic venues for large and complex orders
- [Market maker trading](/market-maker-trading/) — how counterparties provide liquidity
- [Price discovery](/price-discovery/) — how market information is revealed through trading
- [Bid-ask spread](/bid-ask-spread/) — the cost of immediate execution
- [Execution risk](/execution-risk/) — the risk of adverse price movement while working a large order

### Wider context

- [Stock exchange](/stock-exchange/) — primary venue where floor brokers and electronic routing coexist
- [Over-the-counter market](/over-the-counter-market/) — an alternative to exchange trading for large blocks
- [Secondary market](/secondary-market/) — the broader ecosystem where floor brokers and electronic routing both operate
- [Stock](/stock/) — the most common asset class for floor and electronic execution

</div>
