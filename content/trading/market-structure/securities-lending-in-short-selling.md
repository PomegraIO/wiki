---
title: "Securities Lending in Short Selling"
description: "Securities lending in short selling provides the borrowed shares needed to sell short, enforced through locate requirements, borrow fees, and recall risk."
keywords:
  - securities lending short selling
  - how securities lending works
  - short borrow fees
  - locate requirement
  - stock borrow
  - short sale mechanics
image: /svg/trading.svg
---

*To execute a **short sale**, a trader must first borrow shares from someone who owns them—a process called **securities lending in short selling**. The lender (typically a broker, pension fund, or mutual fund) receives a fee; the borrower must pay dividends owed during the loan; and the lender retains the right to recall the shares at any time. This market is both essential to [short selling](/short-selling/) and a source of hidden costs and execution risk.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Securities Lending in Short Selling — key facts</div>

<img src="/svg/trading.svg" alt="An abstract editorial mark for trading." />

<div class="wiki-infobox-caption">Borrowing shares enables short selling; lending creates ongoing obligations and margin calls for the borrower.</div>

|   |   |
|---|---|
| **Lender** | Typically broker, fund, or custodian holding shares |
| **Borrower** | Short seller wanting to sell shares they don't own |
| **Locate requirement** | Broker must confirm borrow availability *before* short sale |
| **Borrow fee** | Annual rate, 0.1% to 50%+ depending on liquidity and scarcity |
| **Dividend obligation** | Borrower pays lender any dividends issued during loan |
| **Recall risk** | Lender can demand return of shares at short notice |
| **Collateral** | Borrower posts cash or securities equal to loan value |

</aside>

## Why shares must be borrowed

A short sale is a bet that a stock's price will fall. The mechanics are straightforward: sell first (hoping to buy back lower), then buy. But the law requires the seller to actually *own* the shares at the moment of sale—or obtain a binding commitment to deliver them. In modern markets, that commitment is fulfilled through borrowing.

Before the 2008 financial crisis, some traders executed "[naked shorts](/short-selling/)" (selling without arranging a borrow). The practice was officially banned in the US and tightened globally after the crisis. Today, [Regulation SHO](/short-selling/) and similar rules worldwide require the short seller's broker to confirm that shares are available to borrow—a "locate"—*before* the short order is executed. Violating this rule triggers forced buy-in or fines.

This borrow-first mandate created a securities lending market. Brokers and custodians hold millions of shares for clients; they lend those shares to short sellers, pocket a fee, and keep the interest (minus a small rebate to the account holder). The market is huge and largely invisible—triillions in daily borrow volume across US equities alone.

## How the borrow is arranged

When you place a short order at your broker, the broker's operations team immediately checks availability. Do they have shares in inventory (from other clients' long positions)? If yes, they match borrower and lender internally and take a spread on the fee. If no, they go to the wholesale borrow market—platforms like Markit, Equilend, or internal networks of prime brokers—to source shares.

Large mutual funds and pension funds are the largest sources of borrow supply. A fund with 10 million shares of Apple sits passively; those shares earn no fee. A prime broker (Goldman Sachs, Morgan Stanley, etc.) approaches the fund with an offer: "Lend us your Apple shares; we'll pay you 0.5% per year and return them anytime you ask." The fund agrees and signs a master securities lending agreement.

The prime broker now has the shares available. When a hedge fund or short seller needs to borrow, the prime broker lends from its pool and charges, say, 2%. The prime broker pockets the 1.5% difference, plus it gets to use the borrowed shares' cash collateral (which the borrower posts) for its own repo and investing—a hidden source of margin.

## Borrow fees and liquidity

Borrow fees are quoted as an annual percentage rate applied to the stock's market value. They vary wildly:

- **Liquid large-cap stocks** (Apple, Microsoft, Tesla): 0.05% to 0.3% annually—trivial.
- **Liquid mid-cap stocks**: 0.2% to 1.5%.
- **Illiquid small-cap or distressed stocks**: 5% to 50%+.
- **Stocks on hard-to-borrow lists** (due to high short interest or limited float): bid-ask spreads of 20% to 100% annualized.

The fee is not fixed. It's a market price, set by supply and demand. When many shorts want to borrow Apple and few lenders offer, the fee rises. Conversely, when a large holder decides to lend its position aggressively, fees collapse.

A short seller betting on a 20% price decline will pay 0.2% to borrow a liquid stock—negligible drag. But shorting a thinly-traded biotech stock might cost 10% per year. If the stock only falls 15% before the short is covered, the borrow fee has eaten most of the profit.

## Dividends and corporate actions

Here's a subtlety many new short sellers miss: when the company pays a dividend, the borrower (short seller) *pays* the lender the amount owed. If you short 1,000 shares of a stock paying a $0.50 quarterly dividend, you owe the lender $500 at ex-dividend date, regardless of the share price.

This turns the profit-loss calculation upside down. A long investor receives dividends; a short seller pays them. Over years of borrowing, dividends can exceed the short seller's original margin. Similarly, stock splits, mergers, and special payouts all flow through the borrow agreement.

## Recall risk and forced buy-in

The lender owns the shares and can recall them—demand the borrower return them—at any time. Retail brokers often have fine print allowing lenders to recall shares on short notice (sometimes 24 hours). Institutional borrowers negotiate longer recall periods (weeks or months) based on counterparty relationship and size.

Recall becomes painful in two scenarios. First: you're short a stock and it's soaring. Suddenly, the lender recalls. You're forced to buy back at the worst time, crystallizing losses. Second: shares become scarce. A company announces a buyback, insiders buy, or a merger closes—float shrinks. Short interest spikes, demand for borrows exceeds supply, and lenders recall to re-lend at higher fees. Shorts caught long are forced to cover, which can cause a "short squeeze," sending the stock price further up.

## The wholesale borrow market

Prime brokers and hedge funds operate on a wholesale level, where borrows are negotiated bilaterally and often bundled. A large short fund might arrange $100 million in borrows across 50 stocks with a single prime broker. Fees are negotiated as a blended rate.

This market is opaque. Borrow rates are not published in real time; they're revealed only to parties in the trade. Retail investors trading through a retail broker are shielded from this wholesale market but also get no visibility. Their broker simply says "shares available to short" or not.

Some brokers have begun disclosing borrow costs to retail customers (Interactive Brokers, for example, shows live borrow rates per stock). Others, like Robinhood, lend retail short shares to wholesale borrowers at rates the retail account holder never sees, and pocket the spread—similar to payment for order flow.

## Hard-to-borrow stocks and squeezes

Certain stocks become chronically hard-to-borrow. GameStop in 2021 is the canonical example: short interest exceeded 100% of the float (meaning more shares were shorted than existed, thanks to lending and rehypothecation), borrow rates spiked to 30%+ annualized, and eventually a viral retail buying surge forced shorts to cover en masse, sending the stock from $17 to $480+.

Hard-to-borrow lists are published by many brokers and reflect both high short interest and low lending supply. Stocks with significant activist investors, pending delisting, or litigation often have high borrow fees because lenders fear forced recalls.

## Collateral and financing

The borrower posts collateral—cash, Treasury bonds, or other securities—equal to the loan's market value (often with a "haircut," meaning 105% or 110% of value). That collateral sits with the lender or a third-party custodian. The lender can invest or re-lend the collateral, earning additional return.

If the borrowed stock rises, the collateral pool might no longer equal 100% of the loan's new value. The borrower must post additional margin. Conversely, if the stock falls, the borrower's collateral excess grows—"excess collateral."

This collateral machinery is what enables repo and leverage in finance. A short seller with $1 million in excess collateral can borrow more shares, or use it to fund other positions. Prime brokers optimize collateral across all client positions, squeezing out pennies of extra return.

## Regulations and compliance

Regulation SHO (US) and similar rules globally mandate:
- Locate before execution
- [Close-out of aged failures-to-deliver](/short-selling/) (borrower must return shares within 35 days or position is forced closed)
- Reporting of short positions (positions exceeding 0.5% of float in certain stocks are publicly disclosed)

Despite these rules, failures to deliver still occur, especially in smaller stocks where lending is fragmented. And the 35-day close-out rule is evaded through rolling borrowers (letting a borrow lapse and immediately rolling it into a new one).

## See also

<div class="wiki-seealso">

### Closely related

- [Short Selling](/short-selling/) — the broader mechanics and strategy
- [Short Squeeze](/short-selling/) — the endgame when borrows become scarce
- Stock Borrow Market — the institutional mechanics of lending
- [Margin Call](/margin-call-forex/) — consequences of collateral erosion
- [Regulation SHO](/short-selling/) — the US rule requiring locate

### Wider context

- [Derivatives Hedging](/derivatives-hedging/) — why hedgers use securities lending
- [Broker](/broker/) — intermediary arranging borrows
- [Hedge Fund](/hedge-fund/) — major borrower of securities
- [Custodian](/custodian/) — institution holding lender's shares
- [Credit Risk](/credit-risk/) — borrower default risk

</div>
