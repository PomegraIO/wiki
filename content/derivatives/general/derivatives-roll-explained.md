---
title: "Rolling a Derivatives Position Explained"
description: "What it means to roll a derivatives position forward: closing the near contract and opening a new one before expiration, with costs and timing implications."
keywords:
  - rolling derivatives position
  - futures roll forward
  - options position roll
  - contract expiration roll
  - roll cost basis
  - futures expiration management
image: /svg/derivatives.svg
---

*To **roll a derivatives position** is to close out an expiring [futures](/futures-contract/) or [options](/option/) contract and simultaneously open a new one with a later [expiration date](/expiration-date/), maintaining the trader's exposure without taking physical delivery or letting the position expire. Rolling is routine for institutional traders and hedgers who wish to maintain a long-term exposure but must replace contracts as they near maturity.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Rolling Explained — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives." />

<div class="wiki-infobox-caption">A roll shifts exposure from a near contract to a farther one, preserving the position while managing maturity.</div>

|   |   |
|---|---|
| **Definition** | Close expiring contract; open new contract with later expiration |
| **When it happens** | Weeks before expiration; rarely at maturity itself |
| **Who does it** | Hedgers, commodity ETFs, traders, [hedge funds](/hedge-fund/) |
| **Cost drivers** | [Contango](/contango/) or backwardation; bid-ask spread; slippage |
| **Timing** | Front-month contracts roll 1–3 weeks before expiration |
| **Common markets** | Oil, natural gas, gold, index futures, currency futures |
| **Impact on returns** | Negative in contango; positive in backwardation |

</aside>

## Why Positions Need to Roll

A [futures contract](/futures-contract/) obligates settlement at a specific [expiration date](/expiration-date/) (often the third Friday of the month, or a specific date). For a crude oil futures contract that expires in December, if you hold it through expiration, you must either:
- Take physical delivery of 1,000 barrels of crude oil (rarely what a trader wants)
- Close the position by the deadline (which forces you out)

A trader or hedger who wants to maintain an oil [hedge](/derivatives-hedging/) or a long oil exposure beyond December cannot just let the contract expire. Instead, two weeks or so before expiration—while there is still robust trading in the December contract—the trader sells (closes) the December contract and buys (opens) a new contract for January delivery, or February, or any month chosen. The trader now holds January futures instead of December, with the same size and the same directional exposure.

Similarly, an options trader holding an [out-of-the-money](/out-of-the-money/) [call option](/call-option/) expiring in one month may choose to close that call a few days or weeks before expiration and buy a new call with the same [strike price](/strike-price/) but later expiration. The [theta](/theta/) (time decay) of the original call is accelerating as expiration nears, so rolling to a later month resets the decay clock.

## The Mechanics of a Roll

Rolling is mechanically simple but operationally important. The trader:

1. **Sells (closes) the near contract** at the current bid/ask price
2. **Buys (opens) the far contract** simultaneously or within seconds
3. **Records the result** as a single roll transaction, or as two separate trades

The entire operation may take seconds. The trader is trying to close the near contract and open the far contract at or near the same time, to avoid the risk that prices move sharply between the two legs. Professional traders and algorithms often execute rolls as a single, pre-agreed package trade with a broker to minimize slippage.

For equity index futures, rolling is trivial: the March contract and the June contract trade on the same exchange, have tight bid-ask spreads, and are highly liquid. For illiquid or foreign contracts, rolling can take hours or days and incur wider spreads.

## Roll Cost and the Futures Curve

The cost of a roll depends on the shape of the [futures curve](/contango/)—the relationship between near and far contract prices. There are two scenarios:

**Contango (normal upward slope):** The far contract is more expensive than the near contract. When you roll, you sell the cheap (near) contract and buy the expensive (far) one. You pay the difference—a cost. If the near contract is at $100 and the far contract at $103, rolling costs you $3 per unit (3%). Over a year of quarterly rolls, this drag compounds. This is the reason commodity ETFs that hold oil or natural gas futures lose value during persistent contango, even if the spot price stays flat.

**Backwardation (downward slope):** The far contract is cheaper than the near contract. When you roll, you sell at a higher price and buy at a lower price. You pocket the difference—a gain. Backwardation typically reflects tight supply or high convenience value of holding spot (physical) inventory, and traders profit from rolling in this environment.

## Timing the Roll

Professional traders do not wait until expiration is imminent. For energy futures, which have highest volume in the front (nearest) contract, rolling typically begins 2–3 weeks before expiration. The front contract is most liquid, so the bid-ask spread is tightest, and executing the roll is easiest. If a trader waits until the final week before expiration, the front contract may have dried up (traders have already rolled), and the bid-ask spread widens, increasing the cost.

For commodity indices that systematically roll (like the S&P GSCI or similar benchmarks), the roll is methodical: the index committee publishes the exact date and time when rolling will occur, and it typically spans several days to avoid market impact. Market participants often front-run the index roll, trading ahead of the announced date.

## Roll Costs in Commodity ETFs

A [commodity ETF](/etf/) that owns [futures contracts](/futures-contract/) must roll continuously. If the fund holds December oil futures and buys January, it incurs the contango cost. Over a year, if the contango averages 1% per quarter (4% annualised), the fund's return lags the spot oil price by roughly that 4%. This is called **roll drag** or **roll erosion**, and it is a permanent tax on commodity ETF returns relative to the actual commodity [price discovery](/price-discovery/).

During extended backwardation, the opposite happens: rolling generates positive returns, and a commodity ETF may outperform the spot price.

## Rolling Options

Options rolls are similar in principle but have additional subtleties. An options trader holding [short call options](/call-option/) (covered calls or naked shorts) expiring in one month may roll up, out, or both:

- **Roll out:** Sell the current month's call at the higher time value, buy the same strike for a later month (paying less time value). Net debit or credit depends on [gamma](/gamma/) and [volatility](/implied-volatility/).
- **Roll up and out:** Sell a lower strike for the current month, buy a higher strike for a later month. This might be done to reduce the probability of assignment or to collect additional premium.

Because options have [vega](/vega/) (exposure to implied volatility), gamma, and theta all moving together, rolling is more of an art than a mechanical operation. Traders use these rolls to manage the Greeks and adjust the risk/reward of the position without closing it entirely.

## Rolling in Backwardation

In backwardation, rolling is profitable or at least neutral. A hedger in crude oil during periods of supply stress (like a war, refinery outage, or temporary supply shock) may find that rolling forward is cheap or even positive—the near contract is worth more than the far contract. In this environment, maintaining the hedge is rewarded.

Conversely, in strong contango (like mid-2020, when oil storage was full and future supply was expected to normalize), rolling was punitive. A hedger who wanted to maintain an oil short would pay a steep price, quarter after quarter.

## Roll Slippage and Execution Risk

Even in liquid markets, rolling incurs transaction costs:
- **Bid-ask spread:** The trader buys at the ask (higher) and sells at the bid (lower).
- **Slippage:** Prices may move while the order is being executed, especially for large rolls.
- **Market impact:** A very large roll can move prices enough to cost the trader money.

Institutional traders often negotiate with their brokers for better pricing on rolls, especially for recurring hedges, and use algorithms to break large rolls into smaller pieces to minimize market impact.

## See also

<div class="wiki-seealso">

### Closely related

- [Futures contract](/futures-contract/) — what is being rolled
- [Options](/option/) — alternative derivative structure
- [Expiration date](/expiration-date/) — trigger for rolling decisions
- [Contango](/contango/) — curve shape that imposes roll cost
- [Backwardation](/backwardation/) — curve shape that rewards rolling
- [Commodity ETF returns](/contango-impact-on-etf-returns/) — practical example of roll drag
- [Strike price](/strike-price/) — fixed reference point in options rolls
- [Theta](/theta/) — time decay that motivates options rolls

### Wider context

- [Derivatives hedging](/derivatives-hedging/) — why traders maintain long-term positions
- [Price discovery](/price-discovery/) — how rolls affect forward prices
- [Hedge fund](/hedge-fund/) — major users of rolling strategies
- [Business cycle](/business-cycle/) — determines contango/backwardation regimes

</div>
