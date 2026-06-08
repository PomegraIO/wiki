---
title: "Risk Parity"
description: "An allocation strategy that weights asset classes by their volatility so each contributes equally to portfolio risk, rather than equal dollar amounts."
keywords:
  - portfolio risk
  - asset allocation
  - portfolio construction
  - volatility weighting
  - diversification
image: "/svg/strategies.svg"
---

*A **risk parity** strategy allocates capital to asset classes in proportion to their inverse volatility, so that each asset class contributes equally to the portfolio's total [risk](/market-risk/), not equally in dollars. If [stocks](/stock/) are twice as volatile as [bonds](/bond/), a risk-parity portfolio holds half as much stock by value but the same amount of risk. The result is often a more balanced portfolio that does not hinge on stock performance.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Risk Parity — key facts</div>

<img src="/svg/strategies.svg" alt="An abstract editorial mark for investment strategies." />

<div class="wiki-infobox-caption">Balancing portfolio risk, not dollars.</div>

|   |   |
|---|---|
| **What it is** | Capital allocation such that each asset class contributes equally to total portfolio volatility or risk |
| **Also called** | Equal-risk-contribution, risk-balanced, balanced-risk portfolio |
| **Key insight** | Stocks are riskier than bonds; holding equal dollars in each concentrates risk in stocks; equal risk-contribution balances this |
| **Common mix** | 30–40 per cent stocks, 40–50 per cent bonds, 10–20 per cent alternatives (commodities, REITs), often with leverage |
| **Risk metric** | Portfolio standard deviation or [value-at-risk](/value-at-risk/) (VaR); ideally, each asset contributes 25 per cent to a four-asset portfolio |
| **Leverage** | Often used to boost returns to match equity levels, but introduces [counterparty risk](/counterparty-risk/) |
| **Best for** | Risk-averse investors seeking diversification without overweighting volatile equities |

</aside>

## The problem with traditional allocation

A traditional 60-40 portfolio holds 60 per cent stocks and 40 per cent bonds by value. But stocks are roughly twice as volatile as bonds. This means the portfolio's risk is dominated by the stock sleeve; stocks account for 90 per cent or more of portfolio volatility even though they are only 60 per cent of dollars. If equities crash, the portfolio crashes because the smaller bond position cannot offset the loss.

This concentration of risk in equities is rarely intentional. It is an artefact of [asset allocation](/asset-allocation/) by dollars rather than by risk. An investor who says "I want a balanced portfolio" intending to split the downside risk between stocks and bonds is actually betting most of the portfolio's fate on stocks. In a sustained bear market, that imbalance becomes obvious and painful.

Risk parity reverses the logic: allocate capital so that each asset class contributes equally to [volatility](/historical-volatility/). If stocks are twice as volatile as bonds, hold half as much stock. If you want stocks, bonds, commodities, and real estate to each contribute 25 per cent of portfolio risk, size each position inversely to its volatility.

## How to calculate and construct risk parity

The calculation is straightforward in concept but requires data on [volatility](/historical-volatility/) and correlations.

Start with the expected volatility (standard deviation) of each asset class. Historically, over rolling 10-year periods:

- Stocks: roughly 15–20 per cent per year.
- Bonds: roughly 5–8 per cent per year.
- Commodities: roughly 15–20 per cent per year.
- Real estate ([REITs](/real-estate-investment-trust/)): roughly 12–18 per cent per year.

To equalize risk contribution, allocate inversely to volatility. If stocks are 15 per cent vol and bonds are 6 per cent vol, the ratio is 6:15 or roughly 40:100, meaning 40 parts bonds to 100 parts stocks by capital. Adjusting for notional dollars:

- Stocks: 33 per cent of capital.
- Bonds: 50 per cent of capital.
- Commodities: 17 per cent of capital.

(These weights are illustrative; exact allocations vary by historical volatility at the time of implementation.)

With these weights, each of the three assets contributes roughly one-third of portfolio volatility. A portfolio shock that moves stocks down 10 per cent will move the stock position down 3.3 per cent; a move that lowers bond prices 2 per cent will move the bond position down 1 per cent; and so on. The portfolio becomes more balanced and less dependent on equity performance alone.

Most risk-parity implementations use [ETFs](/etf/) or [index funds](/index-fund/) for each asset class: a total stock market fund, a bond fund, a commodity ETF, and a real estate fund. Rebalancing happens annually or when allocations drift, just as in [asset allocation](/asset-allocation/).

## Leverage and the practical problem

A pure risk-parity portfolio weighted inversely to volatility often has lower expected returns than an all-stock portfolio, because it holds less of the highest-returning asset (equities). To maintain historical equity-like returns while reducing volatility, many risk-parity funds use [leverage](/leverage-ratio-forex/)—borrowing money to boost the notional size of the portfolio.

A typical leveraged risk-parity portfolio might hold:

- 40 per cent stocks, 50 per cent bonds, 10 per cent commodities (unleveraged, roughly 100 per cent of capital).
- Then borrow at low rates to amplify each position by 1.2x or 1.5x, so the notional portfolio is 120 to 150 per cent.

Leverage amplifies both gains and losses. In a falling market, losses are magnified. If the portfolio falls 10 per cent and you are 1.5x leveraged, you lose 15 per cent plus interest on the borrowed amount. In a stable or rising market, leverage boosts returns; in a sharp correction, it hurts.

Because of this, risk-parity strategies using leverage are sensitive to [counterparty risk](/counterparty-risk/) (if the lender calls the loan) and to funding costs (interest on borrowed money). During the 2008 financial crisis, leveraged risk-parity funds suffered sharp drawdowns because [credit](/credit-risk/) tightened, borrowing costs spiked, and forced selling exacerbated losses. Unleveraged risk-parity portfolios (no borrowed money) suffered less but returned less in the years after because they had lower equity exposure.

## Risk parity vs. traditional asset allocation

The key difference is philosophical and practical:

| Aspect | Traditional 60-40 | Risk Parity |
|--------|------------------|------------|
| Allocation basis | Dollar amounts | Risk contribution |
| Typical stock weight | 60 per cent | 30–40 per cent |
| Typical bond weight | 40 per cent | 40–50 per cent |
| Portfolio volatility | Mostly from stocks | Balanced across assets |
| Expected return | Higher (more equities) | Lower (less equities) |
| Drawdown in bear market | Steep (stocks dominate) | Shallower (diversified) |
| Implementation | Simple, no leverage needed | May require leverage to boost returns |

Risk parity is not "better" than traditional allocation; it reflects a different trade-off. A traditional portfolio has higher expected returns but is underdiversified on a risk basis. A risk-parity portfolio is more balanced but may have lower returns and, if leveraged, introduces borrowing risks.

## Who should use risk parity

Risk parity appeals to several investor types:

- **Risk-averse long-term savers** who dislike the concentration of volatility in equities and prefer a portfolio where bond performance matters as much as stock performance.
- **Retirees drawing income** who want to reduce the odds of a severe portfolio drawdown early in retirement, which can threaten long-term sustainability.
- **Institutional investors** (pension funds, endowments) who have borrowed money or plan to access the portfolio on a regular schedule and therefore prefer lower [volatility](/historical-volatility/).
- **Investors in low-rate environments** where bonds offer modest returns and adding leverage to stocks seems expensive, making diversified risk parity more attractive than owning mostly bonds for safety.

Risk parity is less suitable for:

- Young savers with a 30+ year horizon who can afford high equity exposure and benefit from the higher expected return.
- Investors uncomfortable with leverage or unable to monitor [margin](/margin-call-forex/) calls.
- Investors in high tax brackets, because the frequent rebalancing and [dividend](/dividend/) income (especially from bonds and commodities) generate [short-term capital gains](/capital-gains-tax-investor/) and ordinary income, both taxed at high rates.

## Empirical performance

Historically, risk-parity portfolios have offered lower volatility than 60-40 portfolios but not dramatically lower. A 60-40 portfolio (stocks and bonds only) has had roughly 10 per cent annualized volatility; a risk-parity portfolio with stocks, bonds, and commodities, unlevered, has had roughly 8–9 per cent. The return is also lower, because less equity exposure means slower long-term growth.

When leveraged to bring returns closer to equities, risk-parity portfolios have shown middling results: lower volatility than all-stock portfolios, but returns in some periods similar to or below a 60-40 traditional portfolio. This is partly because leverage is not free and partly because rebalancing into volatile assets after they have crashed—a rule of risk parity—can drag on returns.

Risk parity has also underperformed in the recent era of low interest rates and persistent equity outperformance, when stocks have beaten bonds dramatically. Historically, bonds and equities have been more negatively correlated (bonds rise when stocks fall), which would make risk parity shine; but in an environment where rising rates hurt bonds and boost equity earnings, that correlation has shifted, and risk-parity portfolios have lagged.

## Implementation and costs

Risk parity can be implemented directly by an investor using low-cost [ETFs](/etf/): a stock fund, a bond fund, a commodity ETF, and a real-estate fund, weighted by inverse volatility and rebalanced annually. Costs are low if you use index funds.

Alternatively, risk-parity mutual funds and hedge funds exist that do the calculation and rebalancing for you, but they charge fees (often 0.5 to 1.5 per cent per year), which erodes returns. Some funds also use leverage internally; you should understand the leverage ratio and [counterparty risk](/counterparty-risk/) before investing.

For a do-it-yourself investor, the simplest approach is to hold a 35-35-30 mix of a US stock fund, a bond fund, and a diversified commodity or multi-asset fund, and rebalance annually. This approximates risk parity without complex volatility calculations.

## See also

<div class="wiki-seealso">

### Closely related

- [Asset allocation](/asset-allocation/) — the foundational decision of how much to invest in each asset class
- [Buy-and-hold investing](/buy-and-hold/) — a simpler alternative focused on long-term diversification without risk-based weighting
- [Diversification](/diversification/) — spreading money across uncorrelated assets to reduce risk
- [Volatility](/historical-volatility/) — the measure of price swings that risk parity seeks to equalize
- Rebalancing — the ongoing adjustment of portfolio weights to maintain target allocations
- [Leverage](/leverage-ratio-forex/) — borrowing to amplify returns, used in some risk-parity funds

### Wider context

- Portfolio construction — the discipline of building portfolios with specific risk or return goals
- [Value-at-risk](/value-at-risk/) — a statistical measure of potential losses, relevant to risk-parity design
- Correlation — how assets move together; risk parity assumes diversification benefits from low correlations
- Hedging — protecting portfolios from downside, which risk parity addresses through diversification
- [Counterparty risk](/counterparty-risk/) — the risk that a lending counterparty fails, relevant if risk parity uses leverage
- Institutional investing — the domain where risk parity originated, among pension funds and endowments

</div>
