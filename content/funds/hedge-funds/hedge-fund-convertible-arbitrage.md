---
title: "Convertible Bond Arbitrage"
description: "Profiting from pricing dislocations between convertible bonds and their underlying equities through delta-hedging."
keywords:
  - convertible bond arbitrage
  - delta hedging
  - bond equity mismatch
  - hedge fund strategies
  - option-adjusted value
image: /svg/funds.svg
---

*A **convertible bond arbitrage** hedge fund exploits pricing gaps between a company's convertible bonds and its ordinary equity. By simultaneously holding the bond and shorting the stock (or taking offsetting positions), the fund bets that the bond's option value and the underlying stock's price will eventually align, capturing the spread when they do.*

<div class="wiki-hatnote">

For the broader category, see [hedge fund](/hedge-fund/). For other spread-capturing strategies, see [merger arbitrage](/hedge-fund-merger-arbitrage/).

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Convertible Bond Arbitrage — key facts</div>

<img src="/svg/funds.svg" alt="An abstract editorial mark for financial strategy and fund operations." />

<div class="wiki-infobox-caption">Market inefficiency betting in credit and equity markets simultaneously.</div>

|   |   |
|---|---|
| **What it is** | Arbitrage between a convertible bond and its underlying stock, typically through delta-hedging |
| **Risk type** | Volatility, credit, financing, gamma |
| **Time horizon** | Days to months, depending on mismatch persistence |
| **Capital requirement** | Moderate to high (often leveraged) |
| **Typical return** | Low single digits, uncorrelated to stock direction |
| **Market condition** | Active in periods of high volatility and credit spreads |

</aside>

## How the Inefficiency Works

A convertible bond is a hybrid security: it pays a coupon like a bond but includes an embedded [call option](/option/) that lets the holder buy shares at a predetermined [strike price](/strike-price/). If the company's stock rises above that strike, the bond's value is anchored to what it would be worth as equity. If the stock falls, the bond's price is supported by its fixed income floor.

The arbitrage arises because the bond market and equity market price these components differently. The bond might trade at a price that implies the option is worth less than it actually is (or more), while the stock's trading volume and [volatility](/historical-volatility/) tell a different story. A convertible bond arbitrageur spots this gap and builds a portfolio to profit from it.

The classic trade is long the bond, short the stock. The fund purchases the convertible, then [short-sells](/short-selling/) the underlying equity in proportion to the option's [delta](/delta/)—the measure of how much the bond's price moves with the stock. This "delta hedge" aims to strip out directional risk and isolate the mispricing in the option's value.

## The Role of Delta-Hedging

Delta hedging is the spine of the strategy. As the stock price moves, the option's delta changes (an effect called [gamma](/gamma/)). A fund managing convertible arbitrage must continuously rebalance: selling more stock as the price falls (and delta decreases), buying it back as the price rises. This forced dynamic—sell low, buy high—means gamma works against the arbitrageur. That's why convertible bond arbitrage funds often run multiple positions to offset gamma losses in one trade with gains elsewhere, and why they rely on low financing costs and tight execution to survive.

## Why Mispricings Occur

Convertible bonds are illiquid relative to equities. A pension fund might buy a convertible for the yield and hold it without ever thinking about the option value embedded inside. Equity traders may be unaware of convertible supply or may focus only on the stock. Furthermore, the convertible's value depends on multiple variables—stock price, interest rates, [volatility](/historical-volatility/), credit [spread](/credit-spread/), and time to maturity—making it genuinely difficult to price fairly in real time.

Volatility changes are especially powerful. If implied volatility ([IV](/implied-volatility/)) rises, the embedded option becomes more valuable, but the stock market may price this in faster than the bond market does. Conversely, an earnings disappointment might trigger a stock crash that the convertible's credit component absorbs—the bond's price might not fall as far as the option value alone would suggest. These mismatches are the fund's hunting ground.

## The Risks

Convertible arbitrage is not risk-free, despite the name. **Gamma risk** is the most treacherous: rapid, large moves in the stock price force the fund to buy high and sell low, eroding returns. In a violent market rally or crash, the costs of rehedging can exceed the trapped profit.

**Financing risk** is equally important. Most convertible arbitrageurs leverage their positions—borrowing money to amplify returns. If [repo](/short-selling/) rates spike or lenders become risk-averse, the cost of maintaining the short stock position rises, crushing profitability. During the 2008 financial crisis, several convertible arbitrage funds collapsed when their lenders demanded immediate repayment.

**Credit risk** on the issuer matters too. If the company encounters trouble, the bond's floor collapses faster than the option value falls, and the arbitrage unwinds painfully. The short stock position may gain, but often not enough to offset the bond loss—especially if the company defaults.

**Liquidity risk** cuts both ways. The convertible bond itself may be hard to exit at a fair price, trapping the fund. Meanwhile, short-selling the stock might be expensive (if borrow supply is tight) or prohibited (if the lender recalls the shares). During stress periods, both legs of the position become illiquid simultaneously.

## When the Strategy Thrives

Convertible arbitrage is most profitable in environments with high stock [volatility](/historical-volatility/) and moderate credit stress. Volatility makes the embedded option expensive to hedge, increasing the mismatch. Moderate credit spreads mean the bond floor is reliable but not so tight that the bond trades almost on equity value alone (eliminating the mismatch).

The strategy struggled during periods of very low volatility (2017, parts of 2018) because option mispricings became tiny and hedging costs ate returns. It also suffered in episodes of sudden credit stress—2008, 2020, parts of 2022—when the bond's credit component and the stock's direction decoupled catastrophically.

## Skill and Competitive Dynamics

Running a successful convertible arbitrage operation requires deep expertise. Managers must monitor the option Greeks (delta, gamma, vega, rho) across dozens of positions, understand credit fundamentals, and execute large short positions in equity markets. They compete for edge by exploiting mispricings faster and more accurately than rivals, using quantitative models to identify attractive trades.

Over time, as more capital flowed into the strategy in the 2000s, mispricings became smaller and returns compressed. The convergence of hedge fund capital and electronic trading tightened spreads, making it harder to find trades that justify the leverage and operational complexity. Today, convertible arbitrage is a specialist segment, typically populated by funds with strong quantitative teams and access to cheap financing.

## See also

<div class="wiki-seealso">

### Closely related

- [Merger arbitrage](/hedge-fund-merger-arbitrage/) — capturing spreads between deal announcement and close
- [Statistical arbitrage](/hedge-fund-statistical-arbitrage/) — exploiting correlations among equity securities
- [Hedge fund](/hedge-fund/) — the broader category of private investment funds
- [Option premium](/option-premium/) — the value of an embedded or traded option
- [Delta](/delta/) — the option Greek measuring price sensitivity

### Wider context

- [Convertible bond](/convertible-bond/) — the hybrid security underlying the arbitrage
- [Call option](/call-option/) — the option component embedded in convertibles
- [Short selling](/short-selling/) — selling borrowed securities to profit from falling prices
- [Volatility smile](/volatility-smile/) — non-uniform implied volatility across strikes
- [Credit spread](/credit-spread/) — the premium required for corporate debt

</div>