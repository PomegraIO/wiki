---
title: "Naked Option"
description: "An option position with no hedging position in the underlying, leaving the seller exposed to theoretically unlimited loss."
keywords:
  - naked call
  - naked put
  - uncovered option
  - short option risk
image: "/svg/derivatives.svg"
---

*A **naked option** is a sold [option](/option/) contract where the seller holds no offsetting position in the underlying asset. A naked [call option](/call-option/) seller does not own the shares; a naked [put option](/put-option/) seller has no cash set aside to buy them. The seller's loss is capped only by the market price of the underlying, making naked selling riskier than covered strategies.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Naked Option — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for financial derivatives." />

<div class="wiki-infobox-caption">Selling without a hedge means loss exposure extends as far as the market moves.</div>

|   |   |
|---|---|
| **What it is** | A sold option with no underlying position to offset gains or losses |
| **Also called** | Uncovered option, unhedged short option |
| **Max loss on naked call** | Theoretically unlimited as the stock price rises |
| **Max loss on naked put** | Limited to the strike price (stock falls to zero) |
| **Premium received** | Higher than covered option selling because of the extra risk |
| **Regulatory status** | Restricted to experienced traders and certain account types |

</aside>

## Naked calls: unlimited loss potential

When you sell a [call option](/call-option/) on a [stock](/stock/) you do not own, you pocket the [premium](/option-premium/)—the full income upfront. But if the stock rallies sharply above your [strike price](/strike-price/), you face a problem. The [call option](/call-option/) holder exercises (or the option expires [in-the-money](/in-the-money/)), forcing you to deliver shares at your [strike price](/strike-price/).

You must buy those shares in the open market at current prices. If the stock has rallied from $100 to $150, and you sold $100 calls, you now must buy at $150 and deliver at $100, losing $50 per share (minus the [premium](/option-premium/) you collected). Scale that loss across 100 shares (standard [option contract](/option/) size), and a $50 loss per share becomes $5,000.

The horrifying part: if the stock rallies to $500, your loss per share is now $400, multiplied by 100 equals $40,000. If you sold five contracts, that is $200,000 gone. The stock could theoretically rally to $1,000, $10,000, or beyond (though practically, regulatory margin rules will [liquidate](/liquidation/) your position long before such extremes).

A [covered call](/covered-call/) writer owns the shares, so their loss is capped: if they sold $100 calls and the stock rallies to $150, they deliver at $100 and miss the $50 upside, but they do not buy shares at a loss. The naked [call option](/call-option/) seller has no such protection. For a trader or institution, selling naked calls is like selling earthquake insurance on a fault line—the premium feels good until the disaster happens.

## Naked puts: large but capped loss

Selling a naked [put option](/put-option/) is less catastrophic but still exposing. When you sell a [put option](/put-option/), you are agreeing to buy the underlying [stock](/stock/) at the [strike price](/strike-price/) if the buyer exercises. If you have no cash set aside and no shares to finance the purchase, you are naked.

If you sold a $100 [put option](/put-option/) and the stock falls to $50, you must buy at $100. Your loss is $50 per share, or $5,000 per contract. That is painful, but it is not infinite. The stock cannot fall below zero, so your maximum loss is capped at $100 per share (if the stock becomes worthless), or $10,000 per contract.

This cap makes naked puts less dangerous than naked calls in one sense, but only in one. A trader who sells five $100 puts still faces a maximum loss of $50,000 if the stock goes to zero. For many retail traders, that wipes out their entire account.

## Why traders sell naked options anyway

The [premium](/option-premium/) for naked options is higher than for covered strategies because buyers demand compensation for the extra risk they are taking on (you, the seller, have no cushion to absorb small losses gracefully). A [covered call](/covered-call/) writer might collect 1% to 2% premium per month; a naked [call option](/call-option/) seller might collect 3% to 5%, creating the illusion of "free money."

Some institutions and experienced traders run naked [option](/option/) strategies deliberately, using portfolio-level hedges and risk limits to manage exposure. A market-making firm selling millions of dollars of [naked options](/naked-option/) every day is not gambling; they are arbing tiny [bid-ask spreads](/bid-ask-spread/) and closing [deltas](/delta/) through rapid trading. The premium adds up, losses are small and frequent, and the business model works.

For retail traders, naked selling is almost always a mistake. The probability of profit is high in the short term (most options expire worthless), creating a false sense of safety. But when the market moves sharply—which it does, periodically—naked positions can vaporise a year's worth of gains in one afternoon.

## Regulatory restrictions

Most brokers restrict naked [option](/option/) selling to experienced traders and require special account approval. Brokers must verify that you understand the risks, have sufficient [capital](/capital-flows/), and can withstand [margin calls](/margin-call-forex/). Many brokers prohibit naked [call option](/call-option/) selling entirely for retail accounts and allow only naked [put option](/put-option/) selling if the trader is well-capitalized.

These restrictions exist because regulators have seen naked [option](/option/) sellers blow up spectacularly, and the fallout can destabilise markets if large positions unwind in a panic.

## The margin game

Naked [option](/option/) selling ties up significant margin (borrowed buying power). When you sell a naked [call option](/call-option/) 10% [out-of-the-money](/out-of-the-money/), your broker sets aside margin equal to a fraction of the notional value—often 15% to 20%. If the stock rallies and your [call option](/call-option/) moves further [in-the-money](/in-the-money/), margin requirement explodes. A [margin call](/margin-call-forex/) follows, forcing you to deposit cash or liquidate other positions.

Many traders blow up by overleveraging naked [option](/option/) positions. They sell ten contracts assuming smooth sailing, but after a 5% market move, they get margin calls they cannot meet. The broker liquidates the position at the worst price, locking in a catastrophic loss.

## Alternatives: covered strategies and spreads

Instead of selling naked [options](/option/), professional traders use [covered call](/covered-call/) (owning the underlying), cash-secured [put options](/put-option/) (holding cash equal to the strike price), and [spreads](/option/) (selling one [option](/option/) and buying another to cap loss). These strategies reduce the [premium](/option-premium/) collected but eliminate infinite loss exposure. For most investors, the trade-off is worth it.

## See also

<div class="wiki-seealso">

### Closely related

- [Covered Call](/covered-call/) — selling calls against shares you own to limit risk
- [Option Assignment Risk](/option-assignment-risk/) — the forced settlement that exposes naked sellers
- [Margin Call](/margin-call-forex/) — the demand for additional capital when a position deteriorates
- [Delta](/delta/) — how much an option price moves relative to the underlying; matters for hedging
- [Out-of-the-Money](/out-of-the-money/) — an option with no intrinsic value, safer for sellers but still risky if naked
- [Call Option](/call-option/) — the right to buy; naked calls have unlimited loss
- [Put Option](/put-option/) — the right to sell; naked puts have capped but large loss

### Wider context

- [Option](/option/) — contracts granting the right to buy or sell at a fixed price
- [Leverage Ratio](/leverage-ratio-forex/) — how much borrowed capital you are using, a factor in blowups
- [Broker](/broker/) — enforces margin rules and liquidates naked positions when margin is insufficient

</div>
