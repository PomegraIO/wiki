---
title: "Rebalancing a Three-Fund Portfolio"
description: "Step-by-step walkthrough of calculating drift and trade sizes when rebalancing a three-fund portfolio of stocks, international stocks, and bonds."
keywords:
  - rebalancing three fund portfolio
  - three fund portfolio rebalancing
  - portfolio drift calculation
  - asset allocation rebalancing
  - fund rebalancing example
---

*Rebalancing a three-fund portfolio means bringing your domestic stock, international stock, and bond holdings back to their target allocation after prices have moved. The process is mechanical: calculate how far each piece has drifted from target, decide whether drift is large enough to rebalance, then compute exact trade sizes to restore balance.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Rebalancing Three Funds — key facts</div>

<img src="/svg/strategies.svg" alt="An abstract editorial mark for strategies." />

<div class="wiki-infobox-caption">Calculate drift, then trade to restore target weights.</div>

|   |   |
|---|---|
| **Target allocation** | E.g., 40% US stock, 20% international stock, 40% bonds. |
| **Current allocation** | Today's market values as a percentage of portfolio. |
| **Drift** | How far current weight has moved from target. |
| **Rebalancing threshold** | Typical: 5% absolute drift or annual calendar rebalance. |
| **Trade calculation** | Buy underweight, sell overweight—calculate dollar amounts. |
| **Tax and cost** | Commissions, bid-ask spread, and capital-gains taxes eat returns. |
| **Frequency trade-off** | More frequent rebalancing tightens allocation; costs rise. |

</aside>

## Setting Up the Scenario

Let's walk through a concrete example. Suppose you have a three-fund portfolio targeting:

- 40% US stock (via a total-market index fund)
- 20% international stock (via an international index fund)
- 40% bonds (via a bond index fund)

Your portfolio is worth $100,000 today. On day one, you allocate:

| Fund | Target % | Target $ | Actual $ (Day 1) |
|---|---|---|---|
| US stock | 40% | $40,000 | $40,000 |
| Int'l stock | 20% | $20,000 | $20,000 |
| Bonds | 40% | $40,000 | $40,000 |
| **Total** | **100%** | **$100,000** | **$100,000** |

Perfect alignment. Now six months pass.

## Calculating Current Allocation and Drift

The US stock market rises 12%, international markets fall 5%, and bonds rise 3%. Here's the impact:

| Fund | Actual $ (Day 180) | Current % | Target % | Drift |
|---|---|---|---|---|
| US stock | $40,000 × 1.12 = $44,800 | 44.8% | 40% | +4.8% |
| Int'l stock | $20,000 × 0.95 = $19,000 | 19.0% | 20% | −1.0% |
| Bonds | $40,000 × 1.03 = $41,200 | 41.2% | 40% | +1.2% |
| **Total** | **$105,000** | **100%** | **100%** | |

Your portfolio is now worth $105,000. US stock has grown to 44.8%—above its 40% target by 4.8 percentage points. International stock fell to 19.0%, below its 20% target by 1.0 point. Bonds are only slightly above at 41.2%.

The question: do you rebalance now?

## The Rebalancing Decision

Most individual investors rebalance when drift exceeds 5% in absolute terms, or on a fixed schedule (e.g., annually, quarterly). Here, US stock is drifted +4.8%—borderline. International stock is drifted only −1.0%. Some investors would wait for US stock to hit +5%; others rebalance quarterly or annually regardless.

For this example, assume you decide to rebalance—perhaps because your policy is to rebalance whenever any asset class drifts 5% or more, and you're close.

## Computing Trade Sizes

Your target allocation on a $105,000 portfolio is:

- US stock: $105,000 × 40% = $42,000
- Int'l stock: $105,000 × 20% = $21,000
- Bonds: $105,000 × 40% = $42,000

But you currently hold:

- US stock: $44,800
- Int'l stock: $19,000
- Bonds: $41,200

So you must:

- **Sell** US stock: $44,800 − $42,000 = **sell $2,800**
- **Buy** Int'l stock: $21,000 − $19,000 = **buy $2,000**
- **Buy** Bonds: $42,000 − $41,200 = **buy $800**

Check: $2,800 out = $2,000 + $800 in. ✓

If you're buying and selling funds through a brokerage, you'd place an order to sell $2,800 of the US stock fund, then use that cash (plus any additional cash on hand) to buy $2,000 of the international fund and $800 of the bond fund.

## Practical Considerations: Commissions and Spreads

In the real world, you'll face frictions:

- **Trading commissions**: Many brokers offer commission-free mutual fund trades, but some funds or platforms charge flat fees (e.g., $20–$50 per trade).
- **Bid-ask spreads**: ETFs have spreads (typically 0.01%–0.05% for popular broad-market funds), meaning you'll pay slightly more to buy and receive slightly less to sell.
- **Timing**: If you execute the sell and buy at different times, market moves between orders can change the final allocation.

For a $105,000 portfolio rebalancing $2,800, a $50 trading fee is 0.18% of the traded value—material enough to justify only larger drifts. This is why many investors rebalance only annually or on a calendar schedule rather than continuously.

## Tax Consequences (Taxable Accounts)

In a tax-advantaged account (401(k), IRA), rebalancing is tax-free. In a taxable brokerage account, selling an appreciated fund triggers capital gains taxes if you've held it more than one year (long-term rate, usually lower) or less (short-term, taxed as ordinary income).

In the example, you're selling US stock that appreciated from $40,000 to $44,800—a $4,800 gain. If the realized gain is $2,800 (proportional to your sale), and your long-term capital-gains rate is 15%, you'd owe $420 in taxes. For that, your rebalancing has become much less attractive.

Many investors in taxable accounts use a threshold of 7–10% drift before rebalancing to justify the tax cost. Others rebalance only in December using tax-loss harvesting opportunities to offset gains.

## Variations: Threshold vs. Calendar Rebalancing

**Threshold-based rebalancing** (also called "bands" or "corridor" rebalancing) requires action only when drift exceeds a preset limit (e.g., 5%). This minimizes unnecessary trading but can let drift widen in long trends.

**Calendar rebalancing** locks in a date—annual, quarterly, or monthly—and rebalances on that date regardless of drift. It's simpler psychologically and easier to automate but may force you to trade when drift is minimal, incurring unnecessary costs.

A hybrid approach: rebalance annually if drift is less than 5%, but rebalance sooner if any asset class drifts more than 7%. This balances cost control with drift management.

## The Three-Fund Advantage

The appeal of the three-fund portfolio—total US market, total international market, bonds—is simplicity and low cost. Rebalancing is straightforward because you're moving money between just three liquid, commission-free funds at most brokers. A 20-fund portfolio would be a bookkeeping nightmare.

The mathematical benefit of rebalancing (forcing you to "buy low, sell high") compounds over decades, though in modest amounts. Rebalancing adds 0.1–0.3% per year of additional return on average—less than the cost of active management, but real. The main benefit is behavioral: rebalancing enforces discipline and keeps risk in check as allocations drift.

## See also

<div class="wiki-seealso">

### Closely related

- [Asset Allocation](/asset-allocation/) — theory of diversifying across stock, bonds, and alternatives
- [Index Fund](/index-fund/) — low-cost, passively managed funds used in three-fund portfolios
- [Diversification](/diversification/) — why spreading capital across uncorrelated assets reduces volatility
- [Expense Ratio](/expense-ratio/) — fund costs that compound to reduce long-term returns
- [Tax-Loss Harvesting](/tax-loss-harvesting/) — offsetting gains by selling losers in taxable accounts

### Wider context

- [Stock Market](/stock-market/) — how equities are traded and priced
- [Bond](/bond/) — fixed-income securities and their role in portfolio balance
- [Market Timing](/market-timing/) — why trying to time rebalancing often backfires
- Behavioral Biases — psychological traps in portfolio management

</div>
