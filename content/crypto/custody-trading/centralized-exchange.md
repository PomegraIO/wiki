---
title: "Centralised Exchange"
description: "A centralised exchange (CEX) is a cryptocurrency trading platform operated by a company that holds user funds in custody. Users deposit fiat or cryptocurrency, and the exchange executes trades between them."
keywords:
  - centralised exchange
  - cex
  - order book
  - custody
  - trading platform
  - binance
  - coinbase
image: "/svg/crypto.svg"
---

*A **centralised exchange** (**CEX**) is a cryptocurrency trading platform operated by a company that manages user accounts and holds cryptocurrency in custody. Users deposit funds and trade through the exchange's order book. CEX platforms prioritise speed, liquidity, and ease of use but introduce custody risk.*

<div class="wiki-hatnote">

This entry covers centralised exchanges. For peer-to-peer trading, see [decentralised exchange](/decentralized-exchange/); for general exchange concepts, see [cryptocurrency exchange](/cryptocurrency-exchange/).

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Centralised Exchange — key facts</div>

<img src="/svg/crypto.svg" alt="CEX trading interface and order book" />

<div class="wiki-infobox-caption">A centralised exchange: fast, liquid, but custodial.</div>

|   |   |
|---|---|
| **Operator** | A company (centralised) |
| **Custody** | Exchange holds user funds |
| **Speed** | Instant (off-chain) |
| **Liquidity** | Deep (depends on volume) |
| **Fee** | 0.1–0.5% per trade |
| **Regulation** | Varies by jurisdiction; KYC/AML required |
| **Risks** | Hacking, fraud, bankruptcy |
| **Major examples** | Binance, Coinbase, Kraken, OKX |

</aside>

## How a CEX operates

1. **User deposits.** A user sends fiat (via bank transfer) or cryptocurrency to the exchange's addresses.
2. **Account credited.** The exchange credits the user's account with a balance.
3. **Trading.** The user places buy/sell orders on the exchange's order book.
4. **Order matching.** When a buyer and seller agree on price, the exchange executes the trade.
5. **Settlement.** The exchange updates both users' balances instantly (no blockchain delay).
6. **Withdrawal.** Users can withdraw funds to their own wallets or bank accounts.

The exchange manages all balances in its own database; blockchains are used only for deposits/withdrawals.

## Order book mechanism

A CEX typically uses a **limit order book**:

- **Bid side:** Buyers listing prices they are willing to pay.
- **Ask side:** Sellers listing prices they are willing to accept.
- **Spread:** The gap between the best bid and best ask (the exchange's profit).

When a market order is placed (buy/sell at any price), it matches against limit orders on the opposite side.

## Advantages of CEX

**Speed.** Trades execute in milliseconds, using the exchange's internal matching engine (no blockchain delays).

**Liquidity.** Large, established exchanges have deep order books and high volume, allowing users to buy/sell large amounts without major price impact.

**Ease of use.** Simple interface, one-click trading, familiar to traditional finance users.

**Fiat on/off-ramps.** Easy conversion to/from traditional currencies (USD, EUR, etc.).

**Leverage and margins.** Some CEXs offer margin trading (borrow to amplify trades).

## Disadvantages of CEX

**Custody risk.** The exchange holds user funds. If hacked, funds are lost. If the exchange collapses, users are unsecured creditors (likely lose everything).

**Censorship.** Exchanges can freeze accounts, prevent withdrawals, or refuse service.

**Regulatory burden.** Exchanges must comply with KYC (know-your-customer) and AML (anti-money laundering) regulations, limiting privacy.

**Counterparty risk.** You must trust the exchange to:
- Not lose your funds through negligence.
- Not steal your funds.
- Remain solvent.

## Notable CEX failures

**Mt. Gox (2014):** Lost 850,000 Bitcoin (worth ~$500 million at the time, ~$34 billion today). Customers lost everything.

**FTX (2022):** Collapsed after mismanagement and fraud. Founder Sam Bankman-Fried was arrested. Customers have recovered only a fraction of losses.

**QuadrigaCX (2019):** Owner died; private keys were lost. Customers lost access to ~$190 million.

These failures demonstrate the custodial risk of CEXs.

## Major CEX platforms

**Binance:** The largest CEX by trading volume (~$10+ billion daily). Offers extensive trading pairs and features.

**Coinbase:** One of the oldest and most regulated (has licenses in many jurisdictions). Beginner-friendly.

**Kraken:** Known for security practices and transparency.

**OKX:** Asian-focused exchange, large volume.

**Gemini:** US-based, heavily regulated, known for security.

## Regulatory compliance

CEXs in regulated jurisdictions must:

- Obtain money transmitter licenses.
- Implement KYC (verify user identity).
- Implement AML (prevent money laundering).
- Report suspicious activity.
- Segregate customer funds.

These regulations improve consumer protection but also require personal data disclosure, limiting privacy.

## Insurance and customer funds

Most CEXs do not have FDIC insurance (banks do). Some CEXs carry cyber insurance to protect against hacks, but coverage is typically limited and may not fully compensate users.

## Comparison with DEX

| Aspect | CEX | [DEX](/decentralized-exchange/) |
|--------|---|---|
| **Speed** | Fast (instant) | Slow (blockchain speed) |
| **Custody** | Custodial | Non-custodial |
| **Liquidity** | Deep | Variable |
| **Ease of use** | Easy | Complex |
| **Risk** | Counterparty risk | Smart contract risk |
| **Censorship** | Can censor | Cannot censor |

CEXs excel at speed and ease; DEXs excel at custody control and censorship resistance.

## Future of CEX

CEX regulation is tightening. Some jurisdictions (like Singapore, Switzerland) have created licensing frameworks. Others (like the US) are still developing regulations.

The trend is toward more regulated, professional CEXs and fewer unregulated platforms.

## See also

<div class="wiki-seealso">

### Closely related

- [Cryptocurrency exchange](/cryptocurrency-exchange/) — general exchanges
- [Decentralised exchange](/decentralized-exchange/) — peer-to-peer alternative
- [Automated market maker](/automated-market-maker/) — DEX mechanism
- [Liquidity pool](/liquidity-pool/) — provides DEX liquidity

### Wider context

- [Bitcoin](/bitcoin/), [Ethereum](/ethereum/) — major traded assets
- Smart contract — used in DEX
- [Cryptocurrency](/blockchain-fundamentals/) — general category

</div>
