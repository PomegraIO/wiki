---
title: "Contango Drag on Futures-Based ETFs"
description: "Why commodity ETFs that roll futures contracts in a contango market suffer price erosion relative to the spot commodity, even when prices stay flat."
keywords:
  - contango drag futures etf
  - contango drag on leveraged etfs
  - futures roll cost contango
  - commodity etf underperformance
  - contango curve futures
image: /svg/derivatives.svg
---

*A **contango drag** is a silent erosion of returns that hits any [ETF](/etf/) based on rolling [futures contracts](/futures-contract/) when the market is in **[contango](/contango/)**. Because futures prices are higher in distant months, the fund must continuously sell near-term contracts (at lower prices) and buy far-term contracts (at higher prices). Over time, this mechanical pattern compounds losses even if the underlying commodity spot price does not move.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Contango Drag — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives." />

<div class="wiki-infobox-caption">A structural cost embedded in futures-rolling ETFs when the curve slopes upward.</div>

|   |   |
|---|---|
| **Root cause** | Futures curve upward sloping (contango); fund sells cheap, buys expensive at each roll |
| **Speed** | Depends on contango steepness; can cost 1–10%+ annually in steep contango |
| **Spot price impact** | Occurs *even if spot price is flat*; it is about the roll, not the underlying |
| **Affected products** | Commodity ETFs, [leveraged ETFs](/leveraged-etf/), inverse ETFs (different direction) |
| **Opposite scenario** | [Backwardation](/backwardation/) (inverted curve) creates a *roll gain* instead |
| **Example** | Oil futures in contango: December contract $70, June contract $73; rolling costs the fund the $3 spread × position size |
| **Related mechanics** | [Basis risk](/basis-risk/); [carry trade](/carry-trade/) (the inverse bet) |

</aside>

## The contango roll explained simply

Imagine an ETF that holds crude oil by buying December futures at $70/barrel. As expiration approaches (say, 10 days before settlement), the fund must close that position and roll into the next contract month. If June futures are trading at $73/barrel, the fund is forced to sell at $70 and buy at $73—locking in a $3/barrel loss right there.

Multiply that loss by the fund's position size (perhaps 10,000 barrels) and you get a $30,000 hit in one roll. If the fund does this monthly and the contango persists, those losses accumulate. After 12 rolls, the fund has bled $360,000 in roll losses, even though the spot price of oil could have risen, fallen, or stayed flat.

This is contango drag: a cost that is independent of the underlying commodity price movement. It is purely a feature of how the futures curve is shaped.

## Why contango exists

Contango is the normal state for most commodity futures markets. Future contracts cost more than near-term contracts because:

1. **Storage and insurance costs** — If you want to own physical oil in June instead of December, you must pay to store it for six months. That cost is built into the futures price.

2. **Financing** — A dealer holding physical inventory to hedge their short futures position must finance that inventory at some interest rate. That financing cost is priced into the curve.

3. **Convenience yield** — Sometimes near-term inventory is tight, and end-users are willing to pay a premium for immediate availability. But in normal times, this effect is minor compared to storage and financing.

The result: a [contango](/contango/) curve where June futures are typically more expensive than December futures. This is not a market anomaly; it is the market's way of pricing the cost of waiting and holding inventory.

## The erosion in four steps

**Step 1: Initial purchase**
The ETF buys 1,000 barrels of December futures at $70/barrel = $70,000 notional exposure.

**Step 2: Contango environment**
As December approaches, June futures are trading at $73. December futures are now trading at $72 (converging toward spot as settlement nears). The fund has an unrealized gain of $2,000 (1,000 × $2 per barrel). But the roll is coming.

**Step 3: The roll**
The ETF sells the December contract at $72/barrel and buys June at $73/barrel. It locks in a $1,000 loss relative to the initial $70 purchase (the difference between $72 sell and $73 buy, times 1,000 barrels). Now it owns June futures.

**Step 4: Repeat**
When June approaches, July is even higher (more contango). The fund repeats the roll, again selling into weakness and buying into strength.

Over a year of monthly rolls in a $3/barrel contango, the fund loses $36,000 in roll costs—a 5% annual drag—before even accounting for management fees or bid-ask spreads.

## How leverage amplifies the drag

[Leveraged ETFs](/leveraged-etf/) magnify both gains and losses, including contango drag. A 3x leveraged crude oil ETF does not hold 3,000 barrels; it holds derivatives and rebalances daily to maintain a 3x exposure. Each day's rebalancing is another roll opportunity, compounding the effect.

In a steep contango, a 3x leveraged oil ETF can lose 15%+ per year *even if the spot price is flat*, because the daily rebalancing forces it to buy high-cost far-dated futures constantly. This is why leveraged commodity ETFs are explicitly designed for *short-term* directional bets, not long-term holding. The drag is a mathematical certainty in contango.

Inverse (short) ETFs have the opposite problem in backwardation: they benefit from rolling into a declining curve but lose in contango. A -1x inverse crude oil ETF in a steep contango gains from the rolls, because it is selling the expensive far-dated contracts and buying cheaper near-term ones. Paradoxically, an inverse ETF *loses* money when the underlying spot price falls *if the fall is accompanied by contango collapse*.

## A worked example: The 2020 oil crash and contango drag

In April 2020, WTI crude oil prices crashed to negative (briefly) and then recovered to the $30–40 range. During the recovery phase, the contango curve was extremely steep—June futures were trading $8–10 above spot. Oil ETFs that held continuous rolling positions suffered devastating losses in those months.

Here is a simplified scenario:

| Month | Spot | Near contract | Far contract | Roll action | Roll loss |
|---|---|---|---|---|---|
| April | $20 | $25 (May) | $30 (June) | Sell May @$25, buy June @$30 | $5 loss per barrel |
| May | $25 | $28 (June) | $32 (July) | Sell June @$28, buy July @$32 | $4 loss per barrel |
| June | $28 | $30 (July) | $34 (August) | Sell July @$30, buy August @$34 | $4 loss per barrel |

Over three months, with spot prices rising from $20 to $28 (a 40% gain), a simple ETF holding continuous rolling futures contracts lost ~13 percent per barrel in roll drag alone ($5 + $4 + $4 = $13 lost on a path from $20 to $28). An investor holding the spot price would be up 40%; an ETF holder was underwater or barely profitable, despite the huge rally.

This is not a prediction that contango always ruins returns; it is a reminder that contango drag is real and can exceed spot price gains in mean-reverting or range-bound markets.

## Backwardation as the mirror image

When the curve is inverted—near-term contracts are more expensive than far-term contracts (called [backwardation](/backwardation/))—the roll becomes a *gain*. The ETF sells expensive near-term contracts and buys cheaper far-dated ones. Over time, this backwardation roll gain offsets losses and amplifies gains.

This is exactly what happened in energy markets in late 2021 and early 2022, when supply constraints pushed spot prices high and the curve inverted. Oil ETFs benefited from both the rising spot prices *and* the favorable rolls, generating spectacular returns. But this is the exception; contango is the structural norm, and investors should assume it is working against them by default.

## Alternatives to rolling futures

Some investors avoid contango drag by:

1. **Holding physical commodities** — An ETF that actually stores gold bars or crude oil in tanks bypasses the roll entirely. Costs shift to storage and insurance (typically 0.5–1% per year), which is often lower than contango drag in steep curves.

2. **Synthetic replication** — Some ETFs use swaps or other over-the-counter derivatives to replicate commodity exposure without rolling futures. Swap dealers absorb (or profit from) the contango curve shape, and the ETF pays a fixed fee. This can reduce drag but adds [counterparty risk](/counterparty-risk/).

3. **Holding spot via equities** — Instead of commodity futures, buy stock in companies that produce the commodity (oil majors, mining companies). This sidesteps the futures curve entirely and adds equity risk.

4. **Short-term tactical holdings** — Accept that commodity futures ETFs are trading vehicles, not long-term investments. Use them for directional bets over days or weeks, then exit before roll costs compound.

## Duration and curve shape as the deciding factors

The impact of contango drag depends on two variables:

- **Holding period** — A day trader in and out in hours barely feels it. A one-year holder absorbs all 12 rolls and the full cost. A five-year holder in a consistently steep contango can see the drag exceed the underlying price move.

- **Curve shape** — A $0.50/barrel contango costs far less than a $3/barrel contango. In times of supply abundance and low storage scarcity, contango is flat and drag is minimal. In times of supply stress (oil production outages, agricultural crop failures), contango steepens and drag becomes a major headwind.

## See also

<div class="wiki-seealso">

### Closely related

- [Contango](/contango/) — the forward curve structure that drives the drag
- [Backwardation](/backwardation/) — inverted curve where rolling creates gains instead of losses
- [Futures contract](/futures-contract/) — the rolling vehicle that creates the mechanical cost
- [Basis risk](/basis-risk/) — the mismatch between spot and futures prices that contango exploits
- [Leveraged ETF](/leveraged-etf/) — products that amplify both contango drag and returns

### Wider context

- [ETF](/etf/) — index funds and specialized structures, including commodity-tracking variants
- [ETF premium discount](/etf-premium-discount/) — how commodity ETF prices diverge from Net Asset Value due to roll costs
- [Carry trade](/carry-trade/) — the opposite bet, where investors profit from contango by buying futures at the roll
- Commodity markets — the underlying markets where contango is priced

</div>
