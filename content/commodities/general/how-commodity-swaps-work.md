---
title: "How Commodity Swaps Work"
description: "Mechanics of fixed-for-floating commodity price swaps used by producers and consumers to hedge price risk without physical delivery."
keywords:
  - commodity swaps
  - hedging commodity prices
  - fixed for floating
  - commodity derivatives
  - price risk management
  - producer hedging
---

*A **commodity swap** is an agreement between two parties to exchange commodity price risk over a fixed period. One side pays a fixed price; the other pays a floating price indexed to the market. Neither party physically exchanges goods—only cash differences change hands—making swaps an efficient way for producers and consumers to lock in predictable costs or revenues.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Commodity Swaps — key facts</div>

<img src="/svg/commodities.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Over-the-counter contracts that let producers and consumers hedge price risk through cash settlement.</div>

|   |   |
|---|---|
| **Type** | Over-the-counter [derivatives](/derivatives-hedging/) |
| **Parties** | Typically producer + financial institution, or consumer + bank |
| **Cash flow** | Only price differences settle; no physical commodity moves |
| **Fixed price** | Known at inception; often near-market spot or forward |
| **Floating price** | Reset daily or monthly, indexed to published spot prices |
| **Settlement** | Notional quantity × price difference, paid in cash |
| **Duration** | Months to years, structured to match production or consumption cycle |
| **Counterparty** | Usually a major bank acting as intermediary |

</aside>

## The Basic Mechanics

Imagine a copper mine produces 10,000 tonnes of copper per year. Copper prices fluctuate wildly—from $8,000 to $12,000 per tonne—making annual revenue unpredictable. The mine wants certainty. It contacts a bank and enters a commodity swap.

The mine agrees to pay the bank a fixed price—say, $9,500 per tonne on the notional 10,000 tonnes. In return, the bank pays the mine the floating price—the daily spot price of copper, averaged monthly or weekly. At settlement, only the difference moves. If copper trades at $10,200 on average, the bank pays the mine $10,200 − $9,500 = $700 per tonne. If copper falls to $8,800, the mine pays the bank $9,500 − $8,800 = $700 per tonne.

No physical copper changes hands. The mine continues to mine and sell copper to buyers at market rates. The swap is purely financial, settling the price difference on a notional amount of copper the mine produces anyway. This is the defining feature: swaps separate price risk from the actual physical business.

## Who Uses Commodity Swaps and Why

Commodity swaps attract three main user groups.

**Producers**—miners, farmers, oil drillers, timber harvesters—face the opposite problem a mine faces: they generate supply but want revenue certainty. A wheat farmer faces volatile grain prices. By locking the wheat price via a swap, they can budget input costs, plan investment, and secure bank loans with predictable cash flows. The bank on the other side typically hedges by taking the opposite position with traders, speculators, or other farmers in different geographies (who want to bet on price increases).

**Consumers**—refineries, manufacturers, utilities, agricultural processors—want to lock in input costs. An airline wants to hedge jet fuel prices. It enters a swap to pay a fixed fuel price, knowing its ticket revenue will absorb the fixed cost predictably. A plastics manufacturer locks in the price of [crude oil](/crude-oil/)—its primary feedstock—to control production margins.

**Financial institutions**—investment banks, hedge funds, commodity trading houses—act as intermediaries, taking both sides of swaps and managing the net [counterparty risk](/counterparty-risk/). Banks profit from the [bid-ask spread](/bid-ask-spread/): they quote a slightly higher fixed price to consumers and a slightly lower one to producers, capturing the difference. They also trade the underlying risk dynamically, buying and selling [futures contracts](/futures-contract/) and forward agreements to offset exposure.

## Fixed vs. Floating: How Prices Reset

The fixed leg is straightforward: both parties know it from day one, and it never changes. The floating leg is where mechanics matter.

Commodity prices are published by exchanges and price-reporting agencies. For [crude oil](/crude-oil/), typical benchmarks are WTI (West Texas Intermediate) and Brent; for natural gas, Henry Hub; for copper, the London Metal Exchange (LME) settlement price; for agricultural products, CBOT (Chicago Board of Trade) futures. A commodity swap will specify a pricing formula tied to one of these benchmarks.

A typical floating-price calculation might read: "The average daily spot price of WTI crude oil for the month of June, as quoted by the New York Mercantile Exchange, measured in USD per barrel." On the first business day of July, the June average is calculated, and the fixed and floating payments are compared.

Some swaps reset monthly; others weekly or even daily. More frequent resets mean tighter tracking of actual market conditions but more payment dates and administrative work. A producer might prefer monthly resets to simplify cash forecasting; a trader might prefer daily resets to minimize lag between market moves and settlement.

## Pricing the Fixed Leg

The fixed price is not arbitrary. It reflects the bank's view of forward prices, [basis risk](/basis-risk/), credit spreads, and operating costs.

At inception, the bank looks at the forward curve—market expectations for future spot prices. For [crude oil](/crude-oil/), the forward market might show $95 expected in three months and $92 in six months. If a producer wants a one-year swap, the bank quotes a fixed price near the average of expected futures prices, adjusted for convenience yield (the benefit of holding physical inventory) and storage costs.

The bank also charges for [counterparty risk](/counterparty-risk/): the possibility that the producer defaults. If the producer is creditworthy, the spread is small (perhaps $0.10 per barrel). If risky, larger. The bank also embeds its own funding cost; if they must borrow at 4% to finance the hedge, part of that cost flows into the quoted fixed price.

Finally, the fixed price incorporates bid-ask spreads. A producer calling for a quote receives a fixed price slightly higher than the bank's true fair value. A consumer calling receives a slightly lower quote. The bank captures the difference—sometimes $0.20 to $0.50 per unit, depending on market conditions and volatility.

## Basis Risk and Why Swaps Don't Perfectly Hedge

A producer's physical output and the swap's notional quantity rarely align perfectly. The mine might produce 10,000 tonnes of refined copper per year, but the swap references 9,800 tonnes at a specific grade. Or the producer's output fluctuates seasonally, but the swap divides payment evenly across months.

This mismatch is [basis risk](/basis-risk/): the exposure that the physical price diverges from the swap's floating reference. If the swap references LME copper prices but the producer sells on the Shanghai Futures Exchange, local market conditions may cause deviations. If the producer holds inventory, storage costs and financing rates affect the realized price versus the forward price.

Smart hedgers recognize this. A producer might swap 80% of expected output, leaving 20% exposed to market upside but also limiting basis risk. Alternatively, they structure the swap with embedded optionality—a cap or collar—so that if prices move sharply, the hedge adapts.

## Settlement Mechanics: Cash vs. Physical

Most commodity swaps are cash-settled. At each reset date, the difference between fixed and floating prices is multiplied by notional quantity and paid in cash. If WTI averages $98 for June and the fixed price is $95, the consumer pays the producer $3 per barrel on, say, 50,000 barrels = $150,000 cash. The two parties never touch physical barrels.

Some swaps, especially in metals, include optional physical settlement. If the fixed price falls far below spot, the party owing cash may instead deliver physical commodity at the fixed price. This introduces operational complexity—Who stores? Who transports? How is quality verified?—but it prevents extreme cash drains. A producer hedging copper at $9,500 when spot jumps to $15,000 would owe $5,500 per tonne on 10,000 tonnes = $55 million. Physical settlement rights let them negotiate a delivery instead, though that's unusual.

## Risks and Limitations

Commodity swaps shift price risk but introduce [counterparty risk](/counterparty-risk/). If the bank fails mid-contract, the producer or consumer loses the hedge and must scramble to re-enter the market at potentially worse prices. This is why central clearing and [credit rating](/credit-rating/) matter; regulated swaps are now often cleared through exchanges to mitigate default risk.

[Liquidity risk](/liquidity-risk/) also matters. A producer locked in a five-year swap but facing unexpected production shutdown cannot easily exit without negotiating with the bank, which will quote a generous exit price capturing any in-the-money position.

Accounting risk is real too. [GAAP](/generally-accepted-accounting-principles/) and [IFRS](/international-financial-reporting-standards/) rules determine whether a swap qualifies as a "hedge" under accounting standards. If it doesn't, mark-to-market losses flow through earnings volatility, which investors dislike even though the physical exposure is hedged. This dynamic has led some companies to avoid swaps in favor of [futures](/futures-contract/) or [options](/option/), which have clearer accounting treatment.

## See also

<div class="wiki-seealso">

### Closely related

- [Derivatives: hedging](/derivatives-hedging/) — The broader category of risk-transfer instruments
- [Futures contract](/futures-contract/) — Exchange-traded alternative to commodity swaps
- [Forward contract](/forward-contract/) — Over-the-counter price-lock similar to a swap but settled once
- [Basis and basis risk](/basis-risk/) — The divergence between hedging instrument and physical position
- [Counterparty risk](/counterparty-risk/) — Credit risk in over-the-counter derivatives
- Commodity market — The physical and financial markets for commodities
- [Carry trade](/carry-trade/) — Leveraged bets that exploit forward curve shapes

### Wider context

- [Crude oil](/crude-oil/) — Major commodity and common hedging target
- [Natural gas](/natural-gas/) — Volatile commodity widely hedged via swaps
- [Volatility smile](/volatility-smile/) — Advanced pricing consideration for commodity options and swaps

</div>
