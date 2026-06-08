---
title: "Rebalancing a Portfolio Using Only Index Funds"
description: "Rebalancing with index funds simplifies execution but creates overlapping exposures and complications in tracking true drift from targets."
keywords:
  - rebalancing index funds
  - rebalancing portfolio index funds only
  - portfolio rebalancing
  - index fund overlap
  - asset allocation drift
  - buy-and-hold versus rebalancing
image: "/svg/strategies.svg"
---

*Rebalancing a portfolio using only index funds appeals to many investors: low fees, tax efficiency, and transparency. But using broad index funds for rebalancing introduces a hidden complexity—overlapping exposures that make it harder to know when your portfolio has actually drifted from target, and which fund to buy or sell to restore balance.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Rebalancing With Index Funds — key facts</div>

<img src="/svg/strategies.svg" alt="An abstract editorial mark for strategies." />

<div class="wiki-infobox-caption">Simple tools with subtle structural trade-offs.</div>

|   |   |
|---|---|
| **Primary advantage** | Low cost and tax efficiency compared to active funds |
| **Core challenge** | Broad index funds overlap; drift calculations become ambiguous |
| **Drift calculation** | Must account for overlapping holdings, not just fund weights |
| **Typical rebalancing triggers** | Annual, quarterly, or when allocation drifts 5%+ from target |
| **Tax consideration** | In taxable accounts, tax drag from rebalancing may exceed fee savings |
| **Overlap solution** | Use narrower funds (core/satellite) or accept that drift is measured at portfolio level, not per fund |

</aside>

## Why index funds are attractive for rebalancing

Index funds are the default choice for many rebalancing programs. A [total stock market index fund](/index-fund/) (like a U.S. total-market fund) holds thousands of stocks, eliminating single-company risk. An [international developed-markets index](/index-fund/) does the same for non-U.S. equities. A [bond index fund](/bond-etf/) covers the bond market. [Expense ratios](/expense-ratio/) are low—often 0.03% to 0.10% annually—and turnover is minimal, keeping [capital gains](/capital-gains-tax-investor/) distributions small.

This simplicity is powerful. An investor with $500,000 can build a diversified, globally allocated portfolio with three or four index funds and very little paperwork. Rebalancing becomes mechanical: if U.S. stocks outperform and drift from a 60% target to 62%, the investor sells a small portion of the U.S. stock fund and buys more bonds. No stock-picking, no manager selection, no research required.

For many investors, this is the right approach. Low cost and [diversification](/diversification/) trump most other considerations, and the simplicity reduces behavioral errors.

## The overlap problem

The hidden friction emerges when you think carefully about what you own. Suppose your target [asset allocation](/asset-allocation/) is:

- 50% U.S. stocks
- 30% International developed-market stocks
- 20% Bonds

You buy a U.S. total-market index fund, an international index fund, and a bond index fund. But what you are really holding is:

- A bundle of large-cap U.S. stocks (1,500+ companies)
- A bundle of mid-cap and small-cap U.S. stocks (2,000+ companies)
- A bundle of European, Japanese, Australian, and other developed-market stocks (2,000+ companies)
- A bundle of government and corporate bonds (thousands of securities)

All of these are impeccable diversification. The problem arises when you ask: *where is the market risk in this portfolio?* The answer is ambiguous. The U.S. index fund contains different industries and regions than the international fund, but both are equities and move together in market downturns. During a financial crisis, "U.S. 50%, International 30%" as asset classes might both fall 40%, but the granular overlap means the true diversification benefit is less than the nominal 50/30 suggests.

More practically: if you rebalance based on fund weights alone, you may be solving a problem that does not exist. Suppose the U.S. stock fund rises to 52% of portfolio value while international falls to 28% (a 2% drift). If you sell 2% of U.S. and buy 2% of international, you are rebalancing your funds. But you may not be rebalancing your underlying equity exposure, because both funds hold equities, and your total equity weight (80%) is still intact. You have merely shifted within a larger asset class.

## Calculating true drift with overlapping funds

The precise way to handle this is to map each fund to its underlying asset classes, then calculate your true exposure. A framework might look like:

| Fund | Your Weight | Underlying Components | Effective Equity | Effective Bonds |
|------|-------------|----------------------|-----------------|------------|
| U.S. Total | 50% | U.S. equities | 50% | 0% |
| Intl Dev | 30% | Non-U.S. equities | 30% | 0% |
| Bond | 20% | Bonds + cash equivalents | 0% | 20% |
| **Portfolio total** | | | **80% equities** | **20% bonds** |

This is fine if that matches your intended exposure. But if your actual strategic allocation is "65% equities, 35% bonds," you are over-exposed to equities and should rebalance by adding bond funds, not by shuffling between U.S. and international stock funds.

## Three rebalancing approaches

**Approach 1: Rebalance fund weights only.**
Rebalance so that each fund stays within its target range (e.g., U.S. ±5%, Intl ±5%, Bonds ±5%). This is simplest but ignores the underlying asset class structure. You may be nominally rebalanced at the fund level while over or under-exposed to equities overall.

**Approach 2: Rebalance underlying asset classes.**
Define your true targets at the asset class level (60% equities, 40% bonds), then allocate fund weights to hit those targets. Rebalance only if your true equity or bond exposure drifts from target. This is more precise but requires you to mentally map funds to asset classes and recalculate quarterly. 

**Approach 3: Use narrower funds to reduce overlap.**
Instead of one U.S. total-market fund, split into a U.S. large-cap fund and a U.S. small-cap fund. Instead of one international fund, use separate developed-markets and emerging-markets funds. This segmentation makes drift clearer because each fund has a distinct economic role. The trade-off is slightly higher fees and more transaction costs during rebalancing.

## Tax implications of rebalancing with index funds

In taxable accounts, rebalancing incurs [capital gains tax](/capital-gains-tax-investor/). If the U.S. stock fund has appreciated significantly and you sell 2% of it to buy bonds, you realize long-term capital gains and owe tax. Even though the fund's turnover is low, the rebalancing creates a tax bill.

Index funds are tax-efficient compared to [actively managed funds](/active-etf/) because they do not churn their holdings. But rebalancing is a separate decision from fund turnover. The tax drag from rebalancing can sometimes exceed the fee savings of using low-cost index funds—especially if you rebalance frequently (quarterly) rather than annually or on a threshold basis (only when drift exceeds 5%).

In retirement accounts (where gains are not taxed), rebalancing is tax-free, so the cost is only the [bid-ask spread](/bid-ask-spread/) and any commissions (which are minimal with most brokers today).

## A practical example

Consider a $100,000 portfolio with a target of 60% U.S. stock, 20% international, 20% bonds. You invest:

- $60,000 in U.S. total market index (VTI or VTSAX)
- $20,000 in international developed index (VXUS or VTIAX)
- $20,000 in bond index (BND or VBTLX)

Over three years, U.S. stocks outperform. The portfolio grows to $130,000, with:

- $78,000 U.S. stock (60% of old value; now 60% of $130,000 = 78,000 fits)
- $26,000 international (20% of old; now ~20% of $130,000 = 26,000)
- $26,000 bonds (20% of old; now 20% of $130,000 = 26,000)

Wait—that is a perfect scenario. In reality, suppose instead:

- $82,000 U.S. stock (appreciated more; now 63% of portfolio)
- $22,000 international (appreciated less; now 17%)
- $26,000 bonds (unchanged; now 20%)

Your U.S. weight drifted to 63%, international to 17%. You are now over-exposed to U.S. and under-exposed to international equity. If your target is strictly 60/20/20, you sell $2,600 of U.S. and buy $2,600 of international.

But should you? That depends on whether your true goal was "60% U.S, 20% international" or "80% equities total, split between U.S. and international at some ratio." If the former, rebalance. If the latter, ask whether a 3% drift in the equity/bond split matters. If international and U.S. are both equities and you are comfortable with 82% total equities (vs. 80% target), you may not need to rebalance at all.

## When to rebalance and by how much

A threshold-based rule (rebalance only if any allocation drifts more than 5%) is common and sensible. It reduces transaction costs and the tax drag in taxable accounts while maintaining rough discipline. Annual rebalancing is a middle ground between constant adjustment and complete drift.

Aggressive rebalancers (those who believe in buying the dip and selling the run-up) rebalance quarterly or more often. Passive investors often do it annually on a set date (e.g., January 1) regardless of drift. The academic research suggests that for long-term investors, the differences are small—the main driver of returns is [asset allocation](/asset-allocation/), not the rebalancing frequency.

## The case for slightly more complexity

For investors with large portfolios or strong views about managing risk, a modest increase in complexity can pay off. Using a separate small-cap fund, a separate emerging-markets fund, and a longer-duration bond fund makes drift measurement clearer and rebalancing more precise. The cost is slightly higher fees (though still well under active management) and a bit more mental accounting.

For most investors, especially those just starting out, three broad index funds and annual rebalancing strikes the right balance: simplicity, low cost, and reasonable discipline.

## See also

<div class="wiki-seealso">

### Closely related

- [Asset allocation](/asset-allocation/) — the strategic split of a portfolio across asset classes
- [Diversification](/diversification/) — how to spread risk across many holdings
- [Expense ratio](/expense-ratio/) — the ongoing cost of funds
- [Index fund](/index-fund/) — how and why passive funds track benchmarks
- [Capital gains tax](/capital-gains-tax-investor/) — tax implications of selling appreciated assets

### Wider context

- [Buy-and-hold](/buy-and-hold/) — the alternative to regular rebalancing
- Behavioral finance — why rebalancing helps control emotional decisions
- [Portfolio performance measurement](/return-on-invested-capital/) — assessing whether rebalancing improves results

</div>
