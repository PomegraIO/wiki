---
title: "Stock Lending Market"
description: "The market for borrowing securities to enable short selling, dividend stripping, and settlement convenience."
keywords:
  - stock lending
  - short sale
  - securities borrowing
  - locate requirement
---

*The **stock lending market** is the ecosystem in which investors borrow securities from [broker](/wiki/broker/) prime lenders (often from the brokers' customer margin accounts) to execute [short sales](/wiki/short-selling/), settle fails, or capture [arbitrage](/wiki/arbitrage-defi/) opportunities.*

Securities are borrowed in a formal financial transaction: the borrower receives the stock, posts [collateral](/wiki/counterparty-haircuts/) (usually cash equal to 102–105% of the security's market value), and pays the lender a [borrow fee](/wiki/stock-lending-market/) based on scarcity and term. The transaction is typically a securities lending agreement governed by [SIFMA](/wiki/settlement-cycles/) standards, with daily [mark-to-market](/wiki/mark-to-market/) of the collateral and immediate return rights. Unlike a [repo](/wiki/repurchase-agreement/), which is explicitly a collateralized loan of cash, a [stock lending](/wiki/stock-lending-market/) arrangement is a custody arrangement: the lender remains the beneficial owner, receives dividends and voting rights, and can recall the loaned shares at any time (triggering a forced buyback by the borrower).

<aside class="wiki-infobox">

| Feature | Detail |
|---|---|
| **Purpose** | Enable short sales; settle failed trades; arbitrage |
| **Collateral** | 102–105% cash or securities |
| **Borrow fee** | 0.01%–300%+ depending on scarcity |
| **Term** | Overnight to multi-month |
| **Participants** | Brokers, hedge funds, buy-side firms |
| **Settlement** | T+2 or T+1 (DTCC/DTC) |
| **Recall** | Lender can demand return at any time |
| **Dividend treatment** | Lender retains beneficial ownership rights |

</aside>

## The mechanics of a securities lending transaction

When a [short seller](/wiki/short-selling/) wants to sell a stock they do not own, [SEC Regulation SHO](/wiki/regulation-sho/) requires a [locate](/wiki/regulation-sho/) of a borrowable share. The short seller's [broker](/wiki/broker/) approaches internal stock lending desks (which maintain pools of shares lent to them by margin customers) or external lenders (other brokers, custodians, or prime brokers). The broker and lender agree on a [borrow fee](/wiki/stock-lending-market/) (the "short rebate"—a negative interest rate paid to the short seller; the lender keeps the positive rebate spread). The shares are transferred to the short seller's account at the [depository (DTC or Euroclear)](/wiki/depository-trust-company/), and the borrower posts cash [collateral](/wiki/counterparty-haircuts/) daily, [marked to market](/wiki/mark-to-market/) at settlement.

The borrowed stock is now freely tradable by the short seller. On any given day, the lender can recall it, triggering a forced buyback (the short seller must repurchase the shares immediately at market price). This recall right is how [dividend](/wiki/dividend/) events are handled: if the borrowed stock pays a dividend, the lender steps in, receives the cash dividend (economically they still own the shares), and the borrower must compensate the lender for the dividend (a "manufactured dividend" payment).

## Economics: borrow fees and the scarcity premium

Borrow fees in the stock lending market reflect three things: the risk-free [interest rate](/wiki/federal-funds-rate/) (if rates are high, cash [collateral](/wiki/counterparty-haircuts/) is expensive), the [term premium](/wiki/term-premium/) (longer loans cost more), and **scarcity**. A widely-held mega-cap stock like Apple has an abundant supply of shares available to borrow—the fee is often 0.01–0.05% annually, lower than cash rates. A thinly-traded micro-cap or a stock in high short demand (say, during a [short squeeze](/wiki/short-squeeze/)) can command fees of 50–300%+ per annum.

The borrow fee directly impacts the economics of a [short sale](/wiki/short-selling/). If a short seller profits from a 5% decline but pays 15% annualized fees over 6 months, that is a 7.5% drag—turning a 5% gain into a -2.5% loss. High borrow fees often signal [short-squeezable stocks](/wiki/short-squeeze/) and become a signal to short-biased traders (a hidden cost of entry that hedges away the thesis).

## Role in settlement and fails

The stock lending market also plays a critical role in resolving [settlement fails](/wiki/settlement-procedures/). When a seller fails to deliver shares to a buyer by [T+2](/wiki/settlement-cycles/), the buyer's broker can borrow shares at a borrow rate and lend them onward to the buyer's account, preventing a fail-to-receive and keeping the buyer whole. This is cheaper than [regulatory penalties](/wiki/fail-to-deliver-market-impact/) for unresolved fails.

## Relationship to dividend stripping and arbitrage

The stock lending market enables [dividend stripping](/wiki/dividend-stripping/)—a tax-motivated strategy where an investor buys a stock, borrows an offsetting short through stock lending, and arranges for the counterparty to hold the short through the [ex-dividend date](/wiki/ex-dividend-mechanics/). The lender captures the dividend; the short seller avoids it. This creates tax arbitrage (the lender often owns the shares in a tax-deferred account and pays the dividend a manufactured dividend to the short seller). Stock lending is essential to the mechanics.

## Regulation and transparency

The [SEC](/wiki/securities-and-exchange-commission/) does not regulate the borrow fee itself—it is determined by market supply and demand. However, [Regulation SHO](/wiki/regulation-sho/) requires the [locate](/wiki/regulation-sho/) of borrowable shares before a short sale, and [Rule 10b-21](/wiki/rule-10b-5/) restricts manipulative lending. The [DTCC](/wiki/depository-trust-company/) and [FINRA](/wiki/finra/) publish aggregate short interest data monthly, but not which exact shares are borrowed or at what fees.

In recent years, [meme-stock events](/wiki/gamestop-short-squeeze/) have highlighted the stock lending market's role in [short squeezes](/wiki/short-squeeze/). Retail traders noticed that heavily shorted stocks had high borrow fees and low available shares, signaling potential squeeze candidates. This visibility has somewhat democratized awareness of the market, though most lending remains opaque to retail participants.

<div class="wiki-seealso">

### Closely related
- [Short Selling](/wiki/short-selling/) — primary use of borrowed securities
- [Short Squeeze](/wiki/short-squeeze/) — when borrowing becomes scarce
- [Regulation SHO](/wiki/regulation-sho/) — SEC rules on borrowing and locates
- [Repurchase Agreement](/wiki/repurchase-agreement/) — similar cash-collateralized transaction

### Wider context
- [Settlement Cycles](/wiki/settlement-cycles/) — T+2 and fails to deliver
- [Depository Trust Company](/wiki/depository-trust-company/) — custodian of shares
- [Dividend Stripping](/wiki/dividend-stripping/) — tax-motivated use of borrowing
- [Counterparty Risk](/wiki/counterparty-risk/) — lender and borrower exposure

</div>
