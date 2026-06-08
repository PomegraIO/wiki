---
title: "Prime Brokerage Margin Financing Explained"
description: "How prime brokers extend leverage to hedge funds through margin loans, rehypothecation, and securities lending arrangements."
keywords:
  - prime brokerage margin financing how it works
  - prime brokerage
  - hedge fund leverage
  - rehypothecation
  - securities lending
image: "/svg/institutions.svg"
---

*Understanding **prime brokerage margin financing** requires following three threads: the margin loan that lets a [hedge fund](/hedge-fund/) buy $2 of securities with $1 of capital, the rehypothecation of those securities to other clients or for the broker's own use, and the daily repricing and [margin call](/margin-call-forex/) machinery that keeps leverage from destroying both parties. Prime brokers bundle financing, lending, settlement, and risk analytics into a single relationship—one reason [hedge funds](/hedge-fund/) cannot operate without them.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Prime Brokerage Margin Financing — key facts</div>

<img src="/svg/institutions.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Leverage and securities lending are the core; collateral and daily repricing manage risk.</div>

|   |   |
|---|---|
| **Typical leverage ratio** | 2:1 to 4:1 for long books; higher for shorts |
| **Margin loan rate** | SOFR + 50–200 basis points, varies by fund credit |
| **Collateral haircut** | 5–15% on stocks, 1–5% on bonds, higher on illiquid assets |
| **Daily repricing** | Mark-to-market at close; margin calls issued within 24 hours |
| **Rehypothecation** | Securities re-loaned to other clients; enables broker profits |
| **Settlement** | Prime broker handles clearance for off-exchange trades |
| **Stock borrow fees** | 10–500+ bps annually on hard-to-borrow names |

</aside>

## The Core Relationship: Capital, Collateral, Leverage

A [hedge fund](/hedge-fund/) walks into Goldman Sachs or Morgan Stanley with, say, $100 million in capital. It wants to deploy $300 million—either in long positions (leverage = 3:1) or in a complex [short selling](/short-selling/) operation that requires even more counterparty exposure.

The prime broker allows this by extending a **margin loan**: the fund pledges its $100 million in capital (and any positions it holds) as collateral, and the broker lends cash or extends buying power. The fund can now buy $300 million of stock.

The key phrase: the broker *does not* lend from its own balance sheet alone. Instead, it:

1. Takes the fund's collateral (stocks, bonds, cash)
2. Applies a **haircut**—a discount reflecting risk
3. Lends against the remainder
4. **Rehypothecates** (re-lends) the collateral to other clients or uses it for its own trading

This machinery is what makes leverage cheap for the hedge fund. The broker funds itself at SOFR rates (currently 4–5% in mid-2020s terms) and lends to the fund at SOFR + 100–200 basis points. The fund pays 5–7%, well below traditional bank lending rates. The spread and the ability to rehypothecate make it profitable for the broker.

## Collateral, Haircuts, and Daily Mark-to-Market

The leverage ratio depends on collateral quality. If the hedge fund holds $100 million in S&P 500 stocks, the broker might apply a 5% haircut, meaning the broker deems the collateral worth $95 million. Against that, it will lend $150 million to $190 million, creating a leverage ratio of 1.5:1 to 1.9:1 before the fund's own capital amplifies risk further.

But collateral quality varies. Illiquid small-cap stocks might carry a 20% haircut. Emerging-market bonds, 30%. Cryptocurrency or structured products, 50% or more (or be ineligible entirely).

Every business day at close of market, the prime broker marks the fund's positions to market. If the S&P 500 fell 2%, those $100 million in stocks are now worth $98 million. With a 5% haircut, the broker now considers collateral worth $93.1 million. If the fund had already borrowed $150 million, the margin ratio is now in violation. The broker issues a **margin call**, demanding the fund post additional cash or securities by the next morning, or the broker begins unwinding positions.

This daily repricing is the safety valve. Without it, leverage can compound losses invisibly until the broker's own solvency is at risk.

## Rehypothecation: The Economic Engine

Rehypothecation is how the prime broker converts a margin loan into a profitable service. The mechanics:

1. The fund deposits $100 million in stocks as collateral
2. The broker lends the fund $150 million cash
3. The broker then **re-pledges those $100 million stocks** to another counterparty—perhaps a commodity trader, a foreign bank, or the broker's own trading desk—to finance *their* leverage

The broker earns the spread between the rate it pays the hedge fund and the rate it charges the second borrower. It also profits on the borrow fees collected from hard-to-borrow stocks (see below). Rehypothecation can happen multiple times in a chain, increasing systemic [counterparty risk](/counterparty-risk/).

This mechanism is legal and standard, but it creates concentration: if Client A's collateral is rehypothecated to Client B's positions, and Client B faces a forced liquidation, the broker must unwind that chain—potentially hitting Client A's collateral hastily and unfavorably.

## Stock Borrow Fees and Hard-to-Borrow

Hedge funds frequently short stocks. To short a stock, they must borrow shares—and the prime broker facilitates that through its **securities lending desk**. The broker locates shares from other clients (or its own inventory) and lends them to the shortting fund.

The fee—a **borrow rate**—is negotiated annually, typically quoted as a basis-point (bps) annual rate:

- Heavily shorted, thinly floated stocks: 100–500+ bps per year
- Stocks with abundant supply: 10–25 bps
- Blue-chip stocks: 5–15 bps

On a 500-share position shorted at a 200 bps rate, a $100 stock costs the fund $100 per year in borrow fees alone. On a concentrated short of a hard-to-borrow stock, these fees add up.

The prime broker collects the borrow fee (minus a cut paid to the actual lender—perhaps a pension fund or asset manager) and factors it into the fund's economics. The fund must always ask: "Is my short thesis worth paying 200 bps annually to maintain?"

## Risk Management and Margin Calls

The prime broker manages risk through:

**Haircuts** on collateral, tightened when volatility rises. In March 2020, brokers sharply increased haircuts on equities, effectively forcing funds to reduce leverage overnight.

**Concentration limits** on individual positions. A broker might refuse to lend more than $50 million against a single stock to guard against a single name becoming distressed.

**Counterparty limits** to the fund itself. If the fund's recent returns are poor or its credit deteriorates, the broker will lower the leverage cap or demand higher haircuts.

**Daily repricing and** **margin calls** to ensure the fund maintains minimum equity. Calls are typically issued before market open, giving the fund hours to respond.

**Forced liquidation rights** if the fund cannot meet a margin call. The broker can begin selling the fund's positions without waiting for client permission (though agreements specify order and timing rules).

In extreme cases—the 2008 financial crisis being the archetypal example—brokers themselves face bank runs. Hedge funds attempt to withdraw capital, brokers attempt to liquidate collateral to return it, and the feedback loop becomes vicious. Lehman Brothers' prime brokerage franchise collapsed partly because clients lost confidence in the firm's solvency and pulled capital and collateral simultaneously.

## Operational Services Bundled In

Prime brokerage is not merely financing. It includes:

- **Trade execution**: The broker routes the fund's orders to exchanges and negotiates pricing
- **Settlement and clearance**: The broker handles the plumbing—moving cash, settling trades, managing fails
- **Financing**: Margin loans and securities lending (covered above)
- **Risk analytics**: Real-time P&L, Greeks on derivatives, liquidity analysis, concentration reports
- **Custody**: Holding the fund's securities in segregated accounts
- **Reporting and compliance**: Trade-by-trade reconciliation, tax lot tracking, regulatory filings

A large hedge fund might use multiple prime brokers to distribute risk—perhaps 40% of capital with Goldman, 30% with Morgan Stanley, 30% with JPMorgan. This hedges against any single broker becoming distressed or raising leverage caps suddenly.

## The Cost Structure

A fund pays the prime broker through:

1. **Margin loan spreads** (SOFR + 100–200 bps, depending on credit)
2. **Stock borrow fees** (10–500 bps on hard-to-borrow, negotiated annually)
3. **Financing spreads** on cash balances (broker pays less, lends more)
4. **Explicit service fees** on custody, reporting, or execution (flat fee or basis points on AUM)

For a fund managing $1 billion with 3:1 leverage and moderate borrow costs, total financing could run $10–15 million annually (1–1.5% of capital). For funds with higher leverage or concentrated short positions, costs can exceed 2%.

## See also

<div class="wiki-seealso">

### Closely related

- [Hedge Fund](/hedge-fund/) — investment vehicles that rely on prime brokerage for leverage
- [Margin Call](/margin-call-forex/) — daily repricing mechanism that enforces leverage limits
- [Short Selling](/short-selling/) — activity requiring stock borrowing through prime brokers
- [Counterparty Risk](/counterparty-risk/) — concentration danger in rehypothecation chains
- [Leverage Ratio](/leverage-ratio-forex/) — how brokers measure and constrain fund exposure
- [Broker](/broker/) — intermediary role in prime brokerage

### Wider context

- [Securities Lending](/derivatives-hedging/) — mechanics of lending stocks to shorters
- [Fedwire and Settlement](/secondary-market/) — behind-the-scenes clearance prime brokers manage
- [Liquidity Risk](/liquidity-risk/) — danger of cascading liquidations when leverage unwinds
- [Operational Risk](/operational-risk/) — failures in settlement or collateral management

</div>
