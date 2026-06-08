---
title: "Factor ETF vs Direct Indexing: Implementation Tradeoffs"
keywords:
  - factor etf
  - direct indexing
  - smart-beta etf
  - tax-loss harvesting
  - factor investing
  - investment implementation
  - portfolio management costs
description: "Compare factor-based ETFs and direct-indexed factor portfolios on cost, tax efficiency, flexibility, and factor purity—and when each makes sense for investors."
image: /svg/strategies.svg
---

*A **factor ETF** bundles a systematic factor strategy (value, momentum, quality) into a fund that trades like any [exchange-traded fund](/etf/), while **direct indexing** builds a custom portfolio of individual stocks that follows the same factor rules. The choice hinges on cost, tax flexibility, and the precision of factor exposure: ETFs are cheap and liquid for broad audiences, but direct indexing lets sophisticated investors harvest losses daily and dial in exactly the factors they want.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Factor ETF vs Direct Indexing — Key Tradeoffs</div>

<img src="/svg/strategies.svg" alt="An abstract editorial mark for investment strategy." />

<div class="wiki-infobox-caption">Two paths to the same factor exposure, with vastly different costs and constraints.</div>

|   |   |
|---|---|
| **Cost (all-in)** | ETF: 0.15%–0.50% annually; Direct: 0.20%–0.75% (advisory + trading) |
| **Tax-loss harvesting** | ETF: Limited; Direct: Daily harvesting possible |
| **Factor purity** | ETF: Defined by fund rules; Direct: Unlimited customization |
| **Rebalancing frequency** | ETF: Quarterly/semi-annual; Direct: Daily or custom |
| **Liquidity** | ETF: Instant sell at market price; Direct: N/A (illiquid) |
| **Minimum account** | ETF: $1; Direct: Typically $250k–$1M+ |

</aside>

## What is a factor ETF

A **factor ETF** is an [exchange-traded fund](/etf/) that applies a systematic rule set to select and weight securities. Unlike a traditional [index fund](/index-fund/) that holds all stocks in a broad market cap-weighted index, a factor ETF tilts the portfolio toward stocks that score highly on a specific characteristic.

Examples:

- **Value factor**: Selects stocks trading below book value, low price-to-earnings, or high dividend yield
- **Momentum factor**: Selects stocks that have outperformed over a trailing period (e.g., past 12 months)
- **Quality factor**: Selects stocks with low debt, high profitability, low earnings volatility
- **Size factor**: Tilts toward small-cap stocks, which have historically had higher returns

The ETF publishes its rules (usually quarterly) and rebalances on a fixed schedule. You buy shares in the fund like any stock. The [expense ratio](/expense-ratio/) typically ranges from 0.15% to 0.50% per year.

Factor ETFs are sometimes called "smart beta" because they are more intelligent than pure market-cap weighting, but less active than a human stock picker. They are rules-based, transparent, and low-cost relative to [actively managed funds](/actively-managed-fund/).

## What is direct indexing

**Direct indexing** is a portfolio management service where an advisor builds a custom stock portfolio that tracks a factor rule or index but holds individual securities directly (not through a fund).

Instead of buying a factor ETF, the advisor:

1. Applies the factor rules to screen the universe of stocks (e.g., select the 500 stocks with the highest quality scores)
2. Constructs a portfolio of those individual stocks, sized according to the factor weight
3. Rebalances regularly, selling and buying individual stocks as needed
4. Harvests losses daily: whenever a stock falls below its cost basis, the advisor sells it to lock in a loss (for tax purposes) and immediately buys a similar stock to replace it, maintaining factor exposure

The investor receives a personalized, concentrated portfolio. Costs include an advisory fee (0.20%–0.75% annually) plus trading commissions, though commissions have fallen sharply in recent years.

Direct indexing has exploded since 2015, when robo-advisors and traditional wealth managers began offering it at scale. It is now particularly popular with high-net-worth investors and institutions.

## Cost analysis: the full picture

On the surface, factor ETFs look cheaper—0.15% to 0.50% versus 0.50% to 0.75% for direct indexing. But the real cost comparison must include taxes.

**Factor ETF costs:**
- Expense ratio: 0.25% (typical)
- Embedded capital gains: Minimal for equity-factor ETFs, since they are passively managed
- Tax-loss harvesting: None (you own a fund, not individual stocks)
- Trading costs: Minimal (you buy/sell shares in the fund)
- **Total estimated after-tax cost**: 0.25% annually

**Direct indexing costs:**
- Advisory fee: 0.50%
- Trading commissions: Negligible (near-zero at most brokers)
- Tax-loss harvesting benefit: 0.30% to 0.50% annually (the after-tax alpha generated)
- **Net cost after tax benefit**: 0.00% to 0.20% annually

The tax-loss harvesting benefit is the game-changer. By realizing losses daily, a direct-indexed portfolio defers tax liability and effectively reduces the investor's long-term cost. Studies suggest daily harvesting can generate 0.30% to 0.50% in annual after-tax alpha for taxable accounts.

But this edge only applies to taxable accounts. In tax-deferred accounts ([401k](/401k-plan/), [IRA](/traditional-ira/), [Roth IRA](/roth-ira/)), there is no tax-loss harvesting benefit, so direct indexing's cost advantage disappears.

## Tax-loss harvesting and wash-sale rules

The tax-loss harvesting story is more subtle than marketing suggests. When a stock in a direct-indexed portfolio falls, the advisor sells it at a loss and immediately buys a "substantially identical" replacement. The realized loss offsets capital gains or ordinary income (up to $3,000 per year; excess carries forward).

But the IRS has a **wash-sale rule**: if you sell a security at a loss and repurchase the same or substantially identical security within 30 days, the loss is disallowed. To comply, direct-indexing advisors must buy stocks that are *similar* but not identical—a different stock in the same sector or factor.

This creates a subtle issue: the replacement stock may not have the exact same factor exposure. If the advisor sells a high-quality, low-volatility stock at a loss and buys another quality stock, the factor tilt is preserved. But if forced into a distant substitute, the portfolio's factor purity degrades.

High-quality direct-indexing platforms manage this by maintaining a database of factor-alike replacements and rotating through them as needed. Low-cost or automated platforms may accept slippage.

Additionally, for factor ETFs, wash-sale rules apply when you harvest losses on ETF holdings directly (if you sell a factor ETF at a loss, you cannot immediately buy another factor ETF that targets the same factor and call it a wash-sale escape). So direct indexing's harvesting advantage is partly offset by the complexity of finding appropriate substitutes.

## Factor purity and customization

A factor ETF is defined by its published rules. If the S&P 500 Value ETF uses a specific metric to identify value (e.g., price-to-book), you get exactly that. There is no wiggle room.

A direct-indexed portfolio can be customized in ways a fund cannot:

- **Blend factors**: Combine value, momentum, and quality in a bespoke weight
- **Exclude securities**: Remove companies you find objectionable or that conflict with your values
- **Regional/sector tilt**: Overweight certain geographies or industries while maintaining factor exposure
- **Concentration**: Hold fewer stocks (higher conviction) or the full universe
- **Thematic overlay**: Layer in ESG screens, growth themes, or sector rotations on top of factor rules

For instance, an investor could ask for a "quality + low volatility" portfolio that explicitly excludes fossil-fuel companies and tech stocks with high debt. A factor ETF cannot do this (or can only approximate it through separate holdings).

This customization is valuable for investors with strong convictions or constraints. But it also increases implementation risk: a bespoke portfolio is less liquid, harder to monitor, and depends on the advisor's skill in maintaining factor exposure while layering in the customization.

## Liquidity and rebalancing

A factor ETF trades on an exchange, so you can sell your shares at market price instantly during market hours. You can move to a different investment, withdraw cash, or rebalance your overall [asset allocation](/asset-allocation/) with no friction.

A direct-indexed portfolio is illiquid. If you need to withdraw cash or move to a different strategy, the advisor must sell individual stocks—a process that takes days to settle and triggers [capital gains tax](/capital-gains-tax-investor/). You cannot exit as easily.

However, rebalancing *within* the portfolio (say, trimming value exposure to buy momentum exposure) is easier with direct indexing: the advisor can make any adjustment daily without worrying about fund creations/redemptions or trading frictions. Factor ETFs rebalance on a fixed schedule, which can create drag if factor valuations shift between rebalancing dates.

## Minimum account sizes and accessibility

Factor ETFs are designed for everyone: minimum investment is often just the price of one share ($50–$200). You can start with $1,000 and dollar-cost average into the position.

Direct indexing typically requires a minimum account size—often $250,000 to $1 million. This is partly due to economies of scale in advisory and trading, and partly because the advisor needs enough assets to build a concentrated stock portfolio and still achieve diversification. A $100,000 direct-indexed portfolio might hold only 30–50 stocks, which is more volatile than a 500-stock factor ETF.

Some robo-advisors have lowered minimums to $10,000–$50,000, but at the low end, the tax-harvesting benefit often does not justify the higher fees.

## When to choose factor ETFs

- You have limited assets ($250k or less)
- You want simple, transparent, liquid exposure
- You are investing in a tax-deferred account ([IRA](/traditional-ira/), [401k](/401k-plan/))
- You need to rebalance your factor exposures frequently
- You value standardized rules and want to compare performance to a benchmark

## When to choose direct indexing

- You have $500k+ in a taxable account
- You want to customize factor weights or exclude certain securities
- You have high tax brackets and want to maximize tax-loss harvesting
- You value daily rebalancing and can monitor or trust your advisor to do so
- You prefer a personalized portfolio to a fund-based approach

## See also

<div class="wiki-seealso">

### Closely related

- [Factor Investing](/factor-investing/) — The theory and evidence behind factor strategies
- [Index Fund](/index-fund/) — Passive, market-cap-weighted portfolios
- [Actively Managed Fund](/actively-managed-fund/) — Discretionary stock picking and factor tilts
- [ETF](/etf/) — How exchange-traded funds work and when they are efficient
- [Tax-Loss Harvesting](/tax-loss-harvesting/) — Using losses to offset gains and income

### Wider context

- [Asset Allocation](/asset-allocation/) — Dividing portfolios across asset classes and factors
- [Capital Gains Tax: Investor](/capital-gains-tax-investor/) — How realized and unrealized gains are taxed
- [401k Plan](/401k-plan/) — Employer-sponsored retirement accounts
- [Expense Ratio](/expense-ratio/) — The annual fee funds charge

</div>
