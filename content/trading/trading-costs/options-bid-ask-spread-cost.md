---
title: "Options Bid-Ask Spread Cost"
description: "How options bid-ask spreads translate into immediate mark-to-market losses, and what drives spread width across contracts."
keywords:
  - options bid ask spread cost
  - option spread width
  - options trading costs
  - bid-ask spread options contracts
image: "/svg/trading.svg"
---

*The **options bid-ask spread cost** is the immediate loss you sustain by buying an option at the ask price and facing the bid price if you exit right away. That gap—expressed in dollars per share or percentage of the contract's value—determines the true entry cost of opening an option position beyond the premium itself, and it varies dramatically with contract liquidity, underlying volatility, and how far the option lies from the money.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Options Bid-Ask Spread Cost — key facts</div>

<img src="/svg/trading.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Bid-ask spreads on options compound the true cost of entry and exit, with width driven by liquidity and moneyness.</div>

|   |   |
|---|---|
| **Definition** | The difference between the ask price (what you pay to buy) and the bid price (what you receive when you sell), expressed per contract |
| **Typical cost** | 1–3 cents per contract for liquid options; 5–50+ cents for illiquid strikes and expirations |
| **Percentage impact** | 0.5–5% of the option's premium for near-the-money contracts; can exceed 20% for far OTM or short-dated options |
| **Who bears it** | Retail traders taking on risk; market makers profit by capturing the spread |
| **Factors widening spreads** | Lower underlying volume, longer time to expiration, further distance from at-the-money, concentrated market making |

</aside>

## How the spread translates to a cost

When you buy an option, you pay the ask price—the lowest price anyone is willing to sell at. If you immediately sell the same contract, you receive the bid price—the highest price anyone is currently willing to pay. The difference is your spread cost.

Imagine a call option bid at $2.30 and ask at $2.40. If you buy at $2.40 and sell at $2.30 moments later—before volatility or the underlying price shifts—you've lost a dime per share, or $10 per contract (assuming a 100-share standard contract). That's a 4.2% loss on a $2.35 midpoint premium, pure friction.

For illiquid options, spreads can blow much wider. A far out-of-the-money option on a thinly traded underlying might have a 50-cent spread on a $1.00 mid price—a 50% haircut on entry. The cost compounds at exit: you pay the ask to enter and receive the bid to exit, so a round trip costs two spreads' worth.

## What determines spread width

**Underlying volume and volatility** matter most. A call option on the [S&P 500 Index](/sp-500-index/) trades in mammoth size with tight spreads (often 1–2 cents) because the underlying has huge daily volume. A call on a penny stock or a micro-cap ETF might have 30-cent spreads because market makers face wider [counterparty risk](/counterparty-risk/) and fewer offsetting trades.

**Distance from at-the-money** (moneyness) drives spreads wider as you move away from the strike closest to the current spot price. Near-the-money options are most liquid because they attract hedgers and speculators. Far out-of-the-money options, used as cheap lottery tickets, have thin order books and wide spreads because they're harder to hedge and riskier to hold. In-the-money options, especially deep ITM, also suffer wider spreads because volume thins as the option behaves more like the stock itself.

**Time to expiration** is another critical factor. Near-term options (days to weeks) attract high-frequency traders and hedgers rolling positions, so spreads tighten. Options expiring in months have fewer active traders and wider spreads. Quarterly expirations attract institutional hedging and can be tighter than monthly or weekly contracts.

**Market maker concentration** and [market-making](/market-maker-trading/) technology affect spreads across the board. When a single firm dominates an option's market, spreads tend to widen—they have less pressure to compete. Fragmented markets with multiple competing market makers tighten spreads because each competes for flow.

## The cost as a percentage of premium

For a 6-month at-the-money call option, a 5-cent spread on a $3.00 premium is 1.7%—a real but manageable cost. But for a short-dated far-OTM call at $0.20, a 5-cent spread is 25% of the premium—enough to turn a moderately profitable edge into a break-even or losing trade.

This is why retail traders often pay more in spread costs (percentage-wise) than institutional traders. Institutions typically trade large blocks of near-the-money, liquid options on benchmark underlyings, compressing spreads to 1–3 cents. Retail traders chase speculative far-OTM contracts and less-liquid underlying names, paying 10–50 cents per contract and seeing those costs eat into returns.

## Spread cost and [bid-ask-spread](/bid-ask-spread/) behavior across product types

**Single options** (calls and puts) have the widest spreads because each strike-expiration pair is a separate instrument. A given strike might trade infrequently.

**Spreads** (vertical call spreads, straddles, butterflies) are custom combinations that may not trade as single units. Some market makers will quote spreads; others won't, forcing you to leg in and out. Legging in creates [execution risk](/execution-risk/) and multiple spread costs.

**Index options** (like those on the [S&P 500](/sp-500-index/)) typically have tight spreads because underlying index trading is continuous and enormous.

**Equity options** vary wildly—mega-caps (Apple, Tesla) have spreads in the 1–2 cent range; small-cap optionable stocks might see 20–50 cent spreads even on liquid strikes.

## Relationship to [volatility](/implied-volatility/) and [delta](/delta/)

Spreads widen when [implied volatility](/implied-volatility/) is elevated. High volatility increases [counterparty risk](/counterparty-risk/) for market makers holding inventory, so they post wider two-sided quotes to compensate. During earnings season or market dislocations, spreads can double or triple.

Spreads also narrow for deep [in-the-money](/in-the-money/) options because [delta](/delta/) approaches 1—they behave like the stock itself, and market makers can easily hedge by trading the underlying. Conversely, far out-of-the-money options have near-zero delta and no straightforward hedge, so spreads widen.

## Practical implications for traders

The spread cost is often invisible in a single trade, but over dozens of round-trip positions it compounds into significant friction. A retail trader who:

- Buys 10 out-of-the-money calls at 10 cents above mid-price
- Sells them at 10 cents below mid-price  
- Repeats this 20 times per year

…is losing 0.40 cents per contract on 200 round trips, or $800 per 100-contract position, before considering [slippage](/bid-ask-spread/) from price movement between entry and exit.

Strategies to minimize spread cost include trading only high-volume options on liquid underlyings, preferring near-the-money and intermediate-dated contracts, using limit orders to improve entry prices, and avoiding the temptation to "chase" the ask—patience and entry at the mid or better can save tens of dollars per contract.

## See also

<div class="wiki-seealso">

### Closely related

- [Bid-Ask Spread](/bid-ask-spread/) — the fundamental cost of market immediacy across all instruments
- [Market Maker Trading](/market-maker-trading/) — how market makers profit from spreads and manage inventory risk
- [Delta](/delta/) — option sensitivity that correlates with spread width
- [Implied Volatility](/implied-volatility/) — volatility's effect on spread width and option pricing
- [Execution Risk](/execution-risk/) — slippage and adverse fill timing in options strategies
- [In the Money](/in-the-money/) — moneyness and its relationship to spread width and option behavior

### Wider context

- [Option](/option/) — foundational mechanics and terminology
- [Call Option](/call-option/) — the most commonly traded option type
- [Covered Call](/covered-call/) — strategy sensitive to spread costs on both legs
- [Option Premium](/option-premium/) — what you pay and how spreads interact with it
- [Derivatives Hedging](/derivatives-hedging/) — institutional hedging where spread costs matter at scale

</div>
