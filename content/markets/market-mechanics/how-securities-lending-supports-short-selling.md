---
title: "How Securities Lending Supports Short Selling"
description: "Explains how securities lending connects institutional lenders and borrowers, enabling short sellers to borrow shares and obligating them to return them later."
keywords:
  - how securities lending supports short selling
  - securities lending short selling mechanism
  - borrowing shares for short
  - lending interest rates
  - short seller stock recall
image: "/svg/markets.svg"
---

*A **short seller** cannot borrow shares from thin air. **Securities lending** is the mechanism that makes short selling possible: institutional investors (pension funds, insurance companies, asset managers) lend shares from their portfolios to borrowers—typically via a lending agent or prime broker—who deliver them to short sellers. The short seller sells the borrowed shares, betting on a price decline and promising to return them later. If no shares are available to borrow, short selling cannot occur.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Securities Lending and Short Selling — key facts</div>

<img src="/svg/markets.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">The lending chain connects lenders, borrowers, and short sellers; share availability constrains short interest.</div>

|   |   |
|---|---|
| **Lender** | Institutional investor (pension fund, mutual fund, asset manager) that owns shares and lends them for a fee |
| **Borrower** | Broker, prime broker, or lending agent that takes the lender's shares and delivers them to short sellers |
| **Short seller** | Trader or hedge fund that borrows shares, sells them, and later buys them back to return |
| **Lending fee** | Paid by borrower to lender; often 20 basis points to 5%+ annually, depending on share demand |
| **Short interest** | The total number of borrowed shares outstanding in the market; constrained by lending availability |
| **Recall risk** | Lender can demand return of shares; short seller must then buy back at the market price to return them |

</aside>

## The short-selling chain

Short selling requires three distinct roles:

1. **Lender (portfolio owner):** An institution holds shares for its own investment purposes. It does not need the shares immediately (they are long-term holdings) and is willing to lend them for income. The lender receives a fee—typically a percentage of the current market value of the lent shares.

2. **Borrower (facilitator):** A prime broker or lending agent takes possession of the lender's shares and acts as the middleman. The borrower collects the lending fee from the short seller and pays most of it (minus a cut) to the lender. The borrower also guarantees the return of equivalent shares if the lender demands recall.

3. **Short seller (trader):** The ultimate user borrows shares from the borrower's pool. The short seller immediately sells those shares into the market, betting that the price will fall. If the price falls, the short seller buys back the shares at the lower price, returns them to the borrower, and pockets the difference. The cost to the short seller includes the borrowing fee (lending fee paid to the borrower) plus the buy-back price.

## Why lending matters for short supply

### Share availability is finite

The total number of shares a short seller can borrow is limited by the number of shares available in the lending market at that moment. If a stock has 100 million shares outstanding but only 10 million shares are held by lenders willing to lend, then short sellers collectively can borrow at most 10 million shares. This hard constraint means short interest cannot exceed the available supply.

### Volatile lending fees signal demand

When many short sellers want to borrow the same stock but few shares are available, competition for lending drives the fee up. A stock with heavy short demand but scarce lendable shares may have lending fees of 10%, 50%, or even more annually. Conversely, a stock with abundant lendable shares and little short demand may have a lending fee of just 20 basis points (0.2%).

Lending fees act as a price signal: high fees indicate tight supply and strong short demand, which often correlates with potential short squeeze risk.

### Thin lending supply can freeze short selling

If lenders recall most of their shares or stop lending (for example, if they fear short-driven volatility), the available supply for borrowing shrinks. Short sellers already holding borrowed shares are safe until recall; new short sellers cannot borrow. In extreme cases, short selling a stock effectively stops because no shares are available to borrow, regardless of trader demand.

## The mechanics of borrowing and returning

### Borrowing

1. A short seller's broker requests a borrow from the prime broker's lending desk or a third-party lending agent.
2. The borrower confirms whether shares are available and what the lending fee is.
3. If the short seller agrees to the fee, the shares are transferred to the short seller's account and the short seller sells them immediately.
4. The short seller's account carries a short position (negative share count) and owes the shares.

### Holding and interest accrual

The short seller holds the short position and pays daily or monthly interest (the lending fee, usually quoted as an annual percentage). The longer the short is held, the more borrowing cost accumulates.

### Recall and return

At any time, the lender can demand recall of the shares. This can happen for various reasons: the lender wants to sell its position, a major news event changes the lender's view, or the lender's asset manager decides to reallocate capital. When recall occurs:

1. The borrower notifies the short seller that shares must be returned by a specified date (often T+3, three trading days).
2. The short seller must buy back the borrowed shares at the current market price.
3. The repurchased shares are returned to the borrower, who returns them to the lender.
4. The short seller's borrowing obligation is closed.

If the stock has risen sharply since the short was initiated, a recall forces the short seller to buy back at a loss. If the stock has fallen, the short seller buys back at a gain and returns the shares with profit in hand.

## Determinants of lending fee and availability

### Short demand

The more traders and funds want to short a stock, the higher the demand for borrowed shares and the higher the lending fee.

### Long inventory

Institutions that hold large positions in a stock are sources of lendable shares. If an asset manager or pension fund holds 5 million shares of a company, it can lend some of those shares (while keeping the rest in its portfolio).

### Market sentiment

In bull markets, institutions are less willing to lend (they expect shares to appreciate) and more willing to hold. In bear markets or during uncertainty, lenders may actively seek borrowing fees as additional income. This shifts lending supply.

### Earnings announcements and catalysts

Before major events, lenders often recall shares to avoid the volatility risk of the shares being lent while unknown news hits. Conversely, after an event passes, lenders may be more relaxed about recall.

### Regulatory and governance constraints

Some institutions (certain pension funds, for example) have governance policies that limit or prohibit securities lending. These institutions are not lenders, further constraining supply.

## Short interest as a constraint

[Short interest](/short-selling/) is the total number of shares currently borrowed and sold short. It can never exceed the number of shares available to borrow. This creates a natural ceiling:

- If 10 million shares are available to borrow, short interest can be at most 10 million shares.
- If lenders recall half their shares, available supply drops to 5 million, and short interest must fall (as recalls force short sellers to buy back and return shares).

In most liquid stocks, short interest is a small fraction of total shares outstanding and the lending market is ample. In illiquid or controversial stocks, lending supply can be scarce and short interest can approach the available supply, creating squeeze risk.

## Prime brokers and lending agents

### Prime brokers (for hedge funds and prop traders)

Prime brokers offer short selling and securities lending as a bundle. A hedge fund opens a prime brokerage account and can immediately access the prime broker's lending pool. The prime broker uses its own inventory (shares it owns), customer inventory (shares from other customers), or third-party lenders to fulfill borrows. The prime broker charges the short seller a lending fee and remits the bulk of it to lenders or keeps a margin.

### Lending agents (for passive institutions)

Asset managers and pension funds that do not actively trade often use a lending agent. The lending agent manages their shares, lends them to borrowers (short sellers, hedge funds, et cetera), and remits the lending fees back to the asset manager. This is a hands-off way for a long-term holder to earn additional income.

## The practical impact on short selling costs

A trader shorting a stock must account for three costs:

1. **Borrowing fee (lending fee):** The annual fee paid to borrow the shares, calculated daily or monthly.
2. **Dividend payments:** If the stock pays a dividend while the trader holds a short position, the trader must pay the dividend to the lender (as if the lender still owned the shares).
3. **Buy-back price:** The price at which the trader buys back the shares to return them.

In most stocks, the borrowing fee is small (0.2%–1% annually). In heavily shorted, hard-to-borrow stocks, the fee can be 10%+ annually, effectively penalizing the short seller and limiting how long the position can remain profitable.

## See also

<div class="wiki-seealso">

### Closely related

- [Short Selling](/short-selling/) — the practice of selling borrowed shares with the expectation of buying them back at a lower price
- [Custodian](/custodian/) — intermediary that holds and settles securities for institutional clients
- [Broker](/broker/) — intermediary that executes trades and facilitates borrowing
- [Short Squeeze](/short-squeeze/) — price surge when short sellers are forced to buy back as shares become unavailable or expensive to borrow
- [Counterparty Risk](/counterparty-risk/) — risk that a lender or borrower fails to deliver or return shares

### Wider context

- [Over-the-Counter Market](/over-the-counter-market/) — where securities lending and derivatives trades often occur
- [Market Maker](/market-maker-trading/) — traders that provide liquidity and often use securities lending
- [Leverage](/leverage-ratio-forex/) — how short sellers and hedge funds use borrowed securities to amplify bets

</div>
