---
title: "Securities Lending in Secondary Markets"
description: "How securities lending works: who borrows shares, what collateral backs the loans, and the role of repo and third-party intermediaries in enabling short selling."
keywords:
  - securities lending how it works secondary market
  - short selling securities lending
  - stock lending collateral
  - securities borrowing derivatives
---

*Behind every [short sale](/short-selling/), a security is borrowed. **Securities lending in secondary markets** is the machinery that makes it possible: lenders (custodians, pension funds, brokers) rent out shares for a fee, borrowers post collateral, and a shadow market of trillions in daily loans runs parallel to official exchanges.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Securities Lending — key facts</div>

<img src="/svg/markets.svg" alt="An abstract editorial mark for market structure." />

<div class="wiki-infobox-caption">An invisible but essential market that enables short selling and provides revenue to long-term holders.</div>

|   |   |
|---|---|
| **Definition** | Temporary transfer of securities to a borrower for a fee, backed by collateral |
| **Primary use** | Enabling [short selling](/short-selling/), [arbitrage](/algorithmic-trading/), and [hedge fund](/hedge-fund/) strategies |
| **Collateral** | Cash, Treasury bonds, or letters of credit; typically 100–110% of security value |
| **Fees** | 0.1–10% annualized rebate on collateral, depending on security scarcity and demand |
| **Market size** | Trillions of dollars daily globally; largest in US, UK, and developed markets |
| **Intermediaries** | Prime brokers, custodians, [broker](/broker/)–dealers, and automated lending platforms |

</aside>

## The Basic Mechanics

A securities loan is a straightforward transaction: a lender transfers shares to a borrower, the borrower posts collateral (usually cash), and after a set period (often overnight, but can extend indefinitely), the borrower returns the same number of shares and the lender returns the collateral.

The borrower pays a fee, typically expressed as an annualized rebate on the collateral. If a borrower loans $10 million in cash collateral and the rebate is 2%, the borrower receives 2% annually ($200,000) from the lender—meaning the lender, after paying the rebate, nets only part of the cash lent. From the borrower's perspective, it is the cost of borrowing the security.

The collateral is critical. The lender keeps it as security against the risk that the borrower defaults or the share price moves against the lender's interests. Collateral is typically marked to market daily; if the borrower's collateral falls in value relative to the share price, the borrower must post additional collateral (a margin call).

This structure is nested within [repurchase agreement](/repurchase-agreement/) (repo) markets, where the mechanics are nearly identical but the underlying asset is typically a bond, not a stock. Securities lending is the equity-market parallel.

## Who Lends and Who Borrows

**Lenders** are typically holders of large, liquid securities who view lending as a source of incremental return. Major institutional lenders include:

- **Custodians and prime brokers** (like JPMorgan, Goldman Sachs, Bank of New York Mellon) who hold securities on behalf of clients and lend them out to generate fees
- **Pension funds and insurance companies** that hold large long-term positions and rent out lending rights without disrupting their investment thesis
- **Mutual funds and ETFs** with large, stable holdings; many now lease lending rights to generate revenue
- **Corporations** holding treasury stock

**Borrowers** are predominantly short-sellers, arbitrageurs, and hedgers:

- **Hedge funds** seeking to short stocks, betting on price declines
- **Long-short funds** that pair short positions (requiring borrowed stock) with long positions
- **Market makers** who borrow briefly to meet customer demand or maintain inventory
- **Arbitrageurs** exploiting mispricings between markets (e.g., a stock trading at different prices in two countries)
- **Dividend arbitrage traders** borrowing before ex-dividend dates to capture dividend-tax asymmetries

The asymmetry is important: without a lending market, short-selling would be cumbersome and rare. Lenders provide the infrastructure that makes short-selling liquid and accessible.

## Collateral and Risk Management

The collateral posted by borrowers serves two purposes: compensating the lender for opportunity cost and managing the lender's risk. A borrower cannot simply hand over their own cash; collateral is usually posted by the borrower's custodian or broker, held in a segregated account.

The collateral typically equals 100–110% of the market value of the securities borrowed. The extra 10% is a haircut—a buffer against the risk that the share price rises (making the collateral insufficient to recover the shares) or the borrower defaults.

Collateral is marked to market daily in real-time. If the borrowed stock rises 5% in a day, and the borrower's $105 million collateral now covers only a $105.25 million position, the borrower receives a margin call and must post an additional $250,000 or more. Failure to meet a margin call is typically grounds for the lender to close the position and return the shares, using the collateral to settle.

Collateral can be posted as:

- **Cash**, the safest and most common form, earning interest (a rebate) paid to the borrower
- **Treasury bonds** or other high-grade securities, acceptable to most lenders but requiring a wider haircut
- **Letters of credit** from major banks, less common and typically used in large institutional loans

## The Cost of Borrowing: The Rebate Spread

The rebate rate—the interest the lender pays on collateral—is not fixed; it varies dynamically based on supply and demand.

For a common, heavily-traded stock, rebate rates are near the [federal funds rate](/federal-funds-rate/) or [SOFR](/sofr/) (the risk-free rate). Borrowing is cheap because many lenders are willing and many shares are available.

For a hard-to-borrow stock—one in short supply or high demand by short-sellers—rebate rates can soar. During 2020–2021, certain meme stocks and heavily-shorted names traded with rebate rates of 5%, 10%, or even 50% annualized. A borrower paying a 20% rebate is, in effect, paying a 20% annualized fee to hold a short position. This high cost often chokes off new short-selling demand.

The rebate spread—the difference between the rate the lender receives and the rate the borrower pays—is the intermediary's (broker's or custodian's) profit. A prime broker receives Treasury rebate rates (say, SOFR + 5 basis points) but passes only a SOFR – 10 basis points rebate to the lender, netting 15 basis points on every dollar of lending.

## Operational Structure and Intermediaries

Securities lending is not centralized. The NYSE does not run a clearinghouse for loans; instead, loans are brokered through a network of prime brokers, specialist lenders, and [automated matching](/algorithmic-trading/) platforms.

**Prime brokers** (Goldman Sachs, Morgan Stanley, JPMorgan) aggregate loanable inventory from their clients and from proprietary holdings, then match borrowers to that inventory. They manage collateral, handle daily settlements, and keep the transaction anonymous (the lender does not know the borrower and vice versa).

**Specialist securities-lending platforms** like Equilend and SL Lending have emerged to automate matching and reduce friction, allowing institutional lenders to manage their lending programs more efficiently.

**Custodians** (Bank of New York Mellon, State Street, Northern Trust) hold securities for fund managers and routinely lend them out; a large fund manager may receive millions in annual lending revenue from their custodian without active involvement.

All of this activity is over-the-counter (OTC)—off-exchange. There is no central order book; loans are negotiated bilaterally between brokers and entered into systems of record.

## Why Securities Lending Matters

From a market-structure perspective, securities lending enables important activities:

- **[Short selling](/short-selling/)** becomes viable and liquid, allowing investors to express bearish views without owning stock
- **Market efficiency** improves because short-sellers surface overvaluation and can drive prices toward fundamental value
- **Hedging** becomes practical; fund managers can hedge specific holdings without selling them
- **Revenue streams** are created for long-term holders, effectively reducing their cost of capital

But there is a darker side. Heavy short-selling in illiquid or speculative stocks (often enabled by securities lending) can amplify volatility and create risks of destabilizing short squeezes. The 2008 crisis exposed risks in securities lending too: when Lehman Brothers failed, counterparties lost track of lent securities and collateral simultaneously, creating legal chaos.

Regulation has since tightened. The SEC and international regulators now require greater transparency and collateral standards. But securities lending remains a largely hidden market running in parallel to visible exchange trading.

## See also

<div class="wiki-seealso">

### Closely related

- [Short selling](/short-selling/) — the core application of securities lending; betting on price declines
- [Repurchase agreement](/repurchase-agreement/) — the parallel lending market for bonds, using identical mechanics
- [Broker](/broker/) — the intermediary facilitating securities loans and managing collateral
- [Hedge fund](/hedge-fund/) — major borrowers of securities to implement leverage and short strategies
- [Prime broker](/broker/) — specialized brokers handling large institutional lending and borrowing

### Wider context

- [Stock market](/stock-market/) — the exchange and OTC infrastructure for trading and borrowing
- [Secondary market](/secondary-market/) — the market for existing securities post-IPO
- [Market maker trading](/market-maker-trading/) — how intermediaries profit from bid-ask spreads and inventory
- [Derivative](/derivatives-hedging/) — related tools for hedging and speculation that compete with short-selling
- [Counterparty risk](/counterparty-risk/) — the systemic hazard of lending between financial institutions

</div>
