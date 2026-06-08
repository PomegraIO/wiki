---
title: "Margin Call"
description: "A broker's demand that a leveraged investor deposit additional collateral or liquidate positions to cover accumulated losses and restore minimum margin requirements."
keywords:
  - margin-call
  - leverage
  - collateral-requirement
  - forced-liquidation
  - broker-enforcement
  - counterparty-risk
  - default-protection
image: /svg/risk.svg
---

*A **margin call** is a broker's demand that an investor immediately deposit additional cash or securities to meet minimum collateral requirements after losses on a [leveraged](/leverage-ratio-forex/) position. The investor must either post collateral within hours or days, or the broker will forcibly liquidate positions to cover the shortfall. Margin calls are the enforcement mechanism that prevents [counterparty-risk](/counterparty-risk/) from spiralling out of control.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Margin Call — key facts</div>

<img src="/svg/risk.svg" alt="An abstract editorial mark for risk and counterparty relationships." />

<div class="wiki-infobox-caption">The moment leverage turns from profit amplifier to trap.</div>

|   |   |
|---|---|
| **What it is** | Broker demand for additional collateral on a leveraged position |
| **Also called** | Margin requirement, maintenance call, collateral demand |
| **Triggered by** | Losses reducing account equity below maintenance level (typically 25–30%) |
| **Response time** | Hours to days (brokerage-dependent; very tight for [futures](/futures-contract/)) |
| **Consequences of non-payment** | Forced liquidation at market prices, potential account closure |
| **Applies to** | Margin accounts, [futures](/futures-contract/), [options](/option/), [short-selling](/short-selling/), [leveraged ETFs](/leveraged-etf/) |
| **Avoidable by** | Trading only with available cash (never borrowed funds) |

</aside>

## How margin works and when calls arise

[Leverage](/leverage-ratio-forex/) starts with a promise: an investor deposits $10,000 and the broker lends $20,000, giving $30,000 in buying power. The investor buys $30,000 of stock at, say, $100 per share (300 shares). The broker keeps the securities as collateral and charges interest on the loan.

If the stock rises to $105, the position is worth $31,500, profit is $1,500, and the loan is still $20,000. The investor is sitting pretty. But if the stock falls to $95, the position is worth $28,500, loss is $1,500, and the loan is still $20,000. Now the investor's equity has shrunk from $10,000 to $8,500.

Brokers enforce minimum [equity](/common-stock/) ratios. If the account must maintain 25% equity (a common rule), then on a $30,000 leveraged position, equity must be at least $7,500. At $95 stock price, equity is $8,500, so the investor is still above the minimum. But if the stock falls to $92.50, the position is worth $27,750, equity drops to $7,750 (the loan still $20,000). The investor is now exactly at the 25% minimum.

At $90 per share, the position is worth $27,000, equity is $7,000, and the investor has dipped *below* the 25% minimum (now only 25.9%). This triggers a margin call. The broker demands the investor deposit cash or post collateral to bring equity back to at least the maintenance level, typically within one business day.

## The forced-liquidation cascade

If the investor ignores or cannot meet the margin call, the broker acts unilaterally. It liquidates positions—often the most liquid ones first—to raise cash and reduce the loan. If the stock fell to $90, selling 100 of the 300 shares raises $9,000 in cash, which applies to the loan, leaving the investor with 200 shares worth $18,000, loan of $11,000, and equity of $7,000. Now equity is back to 25%.

This forced liquidation can be devastating. The broker doesn't care about the investor's conviction on the stock or long-term thesis. It cares only about protecting itself against further loss. Liquidations also happen at *market prices*, which might be unfavorable—if there's panic selling, the investor exits during peak fear and realizes the worst possible price.

In extreme cases, liquidations trigger a vicious cycle. A hedge fund gets a margin call and is forced to sell a large block of a stock. The block sale pushes the price down further. Other investors holding the same stock on margin now breach their maintenance levels and receive margin calls. They too are forced to sell. The price spirals downward in a self-reinforcing crash. This was a major driver of the 2008 financial crisis and again in March 2020 (Covid crash) and January 2021 (Gamestop squeeze).

## Margin requirements across asset classes

**Equities and equity funds.** Typical initial margin is 50–100% of position value (meaning 50–100% of the position must be funded with the investor's own cash; the broker lends the rest). Maintenance margin is often 25–30%, meaning the investor must have at least 25–30% equity at all times. If equity falls below this, a call is triggered.

**Options.** Margin requirements are complex and non-linear. Long call and put positions require 100% cash upfront (no margin). Short [call-options](/call-option/) and puts require collateral tied to [strike-price](/strike-price/) and [time-value](/time-value/). A short naked call against 100 shares of stock is very risky—if the stock soars, the short position faces unlimited loss—so brokers demand high margin (often 20–30% of the notional value of the underlying stock).

**Futures.** [Futures contracts](/futures-contract/) use daily settlement and are the most rigid margining system. An investor might control $100,000 of crude oil with only $5,000 initial margin. But the account is marked-to-market daily; every session-end, gains and losses are credited or debited. If a crude-oil position moves 2%, the margin account might swing by $2,000. Maintenance margin is very tight (often 50–75% of initial), and margin calls are issued within hours of breach. Futures have forced liquidation clauses in exchange rules; if an account doesn't meet a margin call by market open, the exchange automatically liquidates the position.

**[Leveraged ETFs](/leveraged-etf/).** These are designed to offer implicit leverage without explicit margin accounts. A 3x leveraged S&P 500 ETF aims to return triple the daily return of the S&P 500. The ETF uses [derivatives](/option/) and borrowing internally, so the investor never receives a margin call directly. But the leverage is still there—and decay and volatility drag can erode returns badly, especially in choppy markets. No margin call, but the investor can still lose heavily.

**[Short-selling](/short-selling/).** Shorting a stock requires margin: the investor borrows the stock, sells it, and must later repurchase it and return it. The broker holds the proceeds as collateral, but as the stock price rises (a short loss), the margin account shrinks. A margin call can be issued if the short loss exceeds 25–30% of the account equity. The risk is unlimited (a stock price can theoretically rise infinitely, so short losses are unbounded).

## Examples of margin call cascades

Consider a leverage-heavy fund in a market downturn. The fund has $1 billion in equity and $4 billion in borrowed funds, invested in $5 billion of [equities](/stock/). Markets fall 15%; the portfolio is now worth $4.25 billion. Loan is still $4 billion. Equity is now $250 million (down from $1 billion), or 5.6% of the portfolio. If the maintenance requirement is 10%, the fund is safe. But if it's 20%, the fund is in breach—it needs $1 billion in equity but has only $250 million. It must deposit $750 million in new capital or sell $750 million of assets.

If the fund can't deposit new capital (which most can't in a drawdown), it sells. Selling $750 million of equities pushes the fund's price impact into the market, depressing the market further. Other levered funds in the same positions see losses widen and face margin calls. A vicious liquidation spiral begins.

The 2008 financial crisis escalated partly this way: as mortgage defaults spiked and [mortgage-backed-securities](/mortgage-backed-security/) fell sharply, leveraged bank portfolios fell into margin breach. Banks sold bonds, [equities](/stock/), and real estate to raise collateral. The selling intensified losses. Spreads widened. More funds breached. More selling. The cascade didn't stop until central banks injected emergency liquidity.

## Margin call timing and notification

Brokers vary in how quickly they demand collateral. For equities and most instruments, a margin call typically gives the investor one business day to respond. Some brokers give intraday calls if a loss is severe enough. For [futures](/futures-contract/), the call comes by the next market open or within hours in extreme cases.

The broker notifies the investor via email, phone, or trading platform. Retail investors sometimes miss notifications (especially overnight or on weekends), and the broker may liquidate without warning if the call is not met by the deadline. This has led to famous stories of investors waking up to find their positions liquidated at terrible prices.

## Risk management and avoiding calls

The straightforward way to avoid margin calls is to trade only with available capital and never use leverage. But for professional investors and [hedge funds](/hedge-fund/), leverage is often essential to returns, so the goal is instead to manage leverage carefully and maintain comfortable margin buffers.

Risk managers use [value-at-risk](/value-at-risk/) and [stress-testing](/stress-testing-portfolios/) to estimate the maximum daily loss a portfolio might face. If daily loss could be 5%, a fund with 20% equity might breach its 25% maintenance level. Managers then reduce leverage or hedge (via [protective-puts](/protective-put/) or [index-puts](/put-option/)) to avoid that scenario.

Intraday margin management is also important. A trader in a [leveraged-etf](/leveraged-etf/) or using [options](/option/) margin might carry a position overnight that is safe at market close but faces risk if markets gap at open. Good risk discipline involves mental or actual stops and re-hedging before high-risk windows.

Some investors intentionally carry high leverage to amplify returns in normal times but accept the risk of margin calls and forced liquidation in crises. This is a calculated bet that returns will exceed the leverage cost. This works in bull markets; it blows up in crashes. The 1998 Long-Term Capital Management fund was a famous example of leverage that worked brilliantly until it didn't.

## Counterparty risk and systemic implications

From the broker's perspective, margin calls are protection against [counterparty-risk](/counterparty-risk/). If a client's account is worth $1 billion but is borrowed $3 billion, the broker is exposed: if the client defaults and the portfolio falls another 20%, the broker loses $200 million. Margin requirements keep this exposure within tolerance.

But if all leveraged investors receive margin calls simultaneously (as happened in 2008 and March 2020), forced liquidations can destabilize markets. Regulators now monitor leverage concentrations and stress-test large institutions for margin-call scenarios. Central banks stand ready to provide emergency liquidity to prevent a cascade.

The 2008 crisis also exposed a subtlety: many margin calls came from derivatives [counterparties](/counterparty-risk/) (particularly on CDS and repo contracts) rather than equity brokers. A financial institution might be fine on its equity margin but suddenly face a $10 billion collateral demand from a derivatives dealer as [credit-spreads](/credit-spread/) widened. This is one reason [systemic-risk](/systemic-risk/) regulators now focus on central clearing and standardized margin rules.

## See also

<div class="wiki-seealso">

### Closely related

- [Leverage Ratio (Forex)](/leverage-ratio-forex/) — leverage as a risk measure
- [Counterparty Risk](/counterparty-risk/) — broker default and collateral loss
- [Value-at-Risk](/value-at-risk/) — estimating tail losses that trigger margin calls
- [Short-Selling](/short-selling/) — margin calls on short positions
- [Futures Contract](/futures-contract/) — daily settlement and tight margin enforcement
- [Protective Put](/protective-put/) — hedging margin-call risk

### Wider context

- [Stress Testing](/stress-testing-portfolios/) — banks stress-test margin requirements
- [Systemic Risk](/systemic-risk/) — margin cascades as financial contagion
- [Leveraged ETF](/leveraged-etf/) — embedded leverage without explicit margin calls
- [Volatility Smile](/volatility-smile/) — options margin and convex risk
- [Tail Risk](/tail-risk/) — gap-opens and margin enforcement in crises

</div>