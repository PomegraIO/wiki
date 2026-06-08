---
title: "Crypto Exchange Fee Tiers Explained"
description: "Learn how centralized exchanges structure volume-based fee tiers to reward high-volume traders and how volume discounts cascade as trading activity increases."
keywords:
  - crypto exchange fee tiers
  - how crypto exchange fee tiers work
  - volume-based trading fees crypto
  - maker-taker fee structure
image: "/svg/crypto.svg"
---

*Most centralized **crypto exchange fee tiers** use a volume-based discount structure: as a trader's cumulative 30-day trading volume increases, their taker and maker [fees](/expense-ratio/) decrease in discrete steps. The system incentivizes high-volume traders—institutions and active proprietary traders—to consolidate activity on a single exchange. A trader moving from 0 to $1 million in monthly volume, for example, might drop from 0.1% taker fees to 0.05%, cutting trading friction in half.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Fee Tiers — key facts</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for crypto." />

<div class="wiki-infobox-caption">Volume tiers create progressively lower costs for heavy traders.</div>

|   |   |
|---|---|
| **Measurement period** | Usually 30-day rolling trading volume (cumulative buys and sells) |
| **Typical taker fee range** | 0.02% to 0.10%, highest for newcomers |
| **Typical maker fee range** | −0.01% to +0.05%, negative = rebate for liquidity |
| **Volume thresholds** | Usually 5–8 tiers; often starting at $10k–$100k per month |
| **Highest-tier makers** | Can earn rebates (negative fees) for adding liquidity |
| **Tier reset** | Resets every 30 days; past volume does not carry forward |

</aside>

## The Core Mechanic: Volume-Triggered Discounts

A [crypto exchange](/cryptocurrency-exchange/) fee tier is fundamentally a volume discount system. When you register an account, you begin at the lowest tier—the highest fee. Every buy and sell you execute counts toward your 30-day rolling trading volume. As your cumulative volume crosses preset thresholds, your fee rates automatically drop.

For example, a typical exchange might structure tiers like this:

| Volume (30-day) | Taker Fee | Maker Fee |
|---|---|---|
| $0–$50k | 0.10% | 0.02% |
| $50k–$500k | 0.08% | 0.01% |
| $500k–$5m | 0.06% | −0.01% |
| $5m+ | 0.04% | −0.02% |

A trader executing $100,000 in volume over a month falls into the second tier and pays 0.08% on buys as a taker. A trader pushing $6 million in volume lands in the top tier, paying only 0.04%—a 60% reduction compared to the newcomer.

The volume is almost always calculated as the sum of all buy and sell transactions, priced in USD or equivalent fiat. A purchase of 10 Bitcoin at $30,000 each and a sale of 10 Bitcoin at $31,000 each both count as trades; the volume is $600,000 for the calculation, even though the trader's net position change was zero.

## Why Exchanges Use Tier Systems

Tier systems serve the exchange's business interests directly. High-volume traders are valuable because they generate more fees in absolute terms and tend to be sticky—once they concentrate activity on one exchange, switching costs rise. By offering progressively lower fees, the exchange captures and retains this lucrative segment.

From the trader's perspective, the fee tier creates an incentive to consolidate volume on one exchange rather than splitting it across multiple platforms. A trader might normally split orders across three exchanges for [redundancy](/operational-risk/) or to avoid moving the price too much on a single venue. But if that trader knows they can reach a higher fee tier by moving all volume to one exchange, the savings may justify the consolidation.

Tier systems also price-discriminate based on real activity. A whale making 100 trades per day generates more operational load, more [custody](/custodian/) and settlement work, and more exposure to [counterparty risk](/counterparty-risk/) than a casual holder who trades once a month. Allowing fees to drop with volume rewards the trader while ensuring the exchange is compensated proportionally for the actual friction they incur.

## Maker vs. Taker: The Fee Asymmetry

Exchanges almost always charge lower fees—or even negative fees (rebates)—for market-making (limit orders that add liquidity) than for market-taking (orders that remove liquidity). This asymmetry is a deliberate design choice to attract liquidity providers.

A maker order sits on the order book and waits to be filled. By posting it, you improve the spread and allow other traders to trade more easily. The exchange wants more makers because they reduce volatility and tighten the [bid-ask spread](/bid-ask-spread/).

A taker order hits the book immediately, paying the ask or hitting the bid. Takers remove liquidity and create friction. Exchanges charge them more (or full price) to discourage excess taker volume and to offset the rebate paid to makers.

A top-tier maker might earn −0.02%, meaning the exchange pays *them* 0.02% of the trade value for providing liquidity. Simultaneously, that same trader pays 0.04% as a taker. This 6:1 ratio encourages limit orders and discourages market orders, which tightens spreads and benefits all traders.

## How Traders Climb Tiers

A trader aiming to reach a higher fee tier has several levers:

**Consolidation**: Move all trading activity from multiple exchanges onto a single one. If you spread $2 million in volume across four exchanges ($500k each), you might qualify for mid-tier fees on all of them. By concentrating the $2 million on one exchange, you reach a higher tier with lower fees overall.

**Timing**: Since most tiers reset monthly, some traders time large positions or liquidations to hit targets within a calendar month. A trader intending to rebalance a $100,000 portfolio might wait until late in the month so the rebalancing trades push them into the next tier starting tomorrow.

**Wash trading (prohibited)**: Some traders are tempted to artificially inflate volume by buying and selling the same coins repeatedly to reach a higher tier. Reputable exchanges actively detect and penalize this, freezing accounts or clawing back rebates. The practice is banned and usually results in account suspension.

**Staking or holdings**: Some exchanges tier traders based on a mix of volume *and* holdings—for instance, holding a large balance of the exchange's native token might grant fee discounts. This blurs the pure volume-based system but serves the exchange's goal of building a locked-in user base.

## Volume Resets and Month-to-Month Dynamics

Fee tiers almost always reset monthly. If you achieved top-tier status in January with $10 million in volume, you drop back to your earned tier level on February 1, which might be mid-tier if you don't maintain that volume pace.

This reset dynamic has unintended consequences. A trader in late December might rush to hit a certain tier for January, knowing it will give them lower fees for the whole month. Similarly, some traders might strategically avoid certain activities early in the month if they expect lower volume and prefer to consolidate activity later when they are closer to a tier threshold.

For busy traders and institutions running systematic strategies, this can lead to non-uniform daily trading patterns—essentially a "volume scheduling" problem. Some desks use algorithms to model whether an order should be split across days and venues based on the current tier position and expected resets.

## Comparing Tier Structures Across Exchanges

Fee tiers vary considerably across platforms. Major centralized exchanges typically offer 5–10 tiers, with volume thresholds ranging from $10,000 to $10 million+ in 30-day volume.

Binance, the world's largest by volume, has a steep tier structure that rewards very-high-volume traders and BNB token holders. Coinbase's tier system is shallower and more favorable to smaller traders. Kraken offers multiple fee schedules for different asset classes. Decentralized exchanges generally do not use tiers—they charge uniform percentage fees or rely entirely on liquidity pools with no explicit tiering.

Institutions often negotiate custom fee schedules directly with exchanges, especially for very high volumes. These bespoke arrangements bypass the published tier system entirely, which is why the tier structure matters most for retail and small-to-medium traders.

## The Hidden Cost: Concentration Risk

Tier structures create an incentive to concentrate trading on a single exchange. While this lowers fees, it creates operational and custodial risk. If that exchange experiences downtime, a security breach, or regulatory action, the concentrated trader faces immediate disruption.

Sophisticated traders often weigh the fee savings against diversification costs. Splitting volume across two or three exchanges might cost an extra 0.01–0.02% in fees, but it insures against a single point of failure. For smaller traders, the tier discount usually dominates this calculation. For larger traders and institutions, redundancy becomes critical and the fee savings less material in percentage terms.

## See also

<div class="wiki-seealso">

### Closely related

- [Cryptocurrency Exchange](/cryptocurrency-exchange/) — platforms where digital assets trade and how they operate
- [Bid-Ask Spread](/bid-ask-spread/) — the cost of immediate trading versus patient limit orders
- [Maker-Taker Model](/market-maker-trading/) — how exchanges incentivize liquidity provision with asymmetric fees
- Trading Costs — transaction expenses that eat returns and justify consolidation strategies

### Wider context

- [Counterparty Risk](/counterparty-risk/) — why traders must balance fee savings against exchange risk
- [Custody](/custodian/) — how digital assets are held securely during trading
- Order Routing — how traders decide which exchange to use for each order
- Liquidity — why exchanges tier fees to encourage active market-making

</div>
