---
title: "Tokenized Treasury"
description: "On-chain tokens backed one-for-one by short-duration government bonds, creating a DeFi-native yield instrument."
keywords:
  - tokenized treasury
  - treasury tokens
  - decentralized finance
  - government bonds
  - on-chain yield
  - stablecoin alternative
image: "/svg/crypto.svg"
---

*A **Tokenized Treasury** is an on-chain token that represents a claim on short-duration government bonds held in reserve. Each token is backed one-for-one (or close to it) by securities like U.S. Treasury bills or other low-default-risk government debt. Token holders earn yield paid from the underlying bonds' coupon payments, making them a bridge between traditional fixed income and decentralized finance.*

## The core appeal: yield without counterparty risk

For the first decade of crypto, stablecoins offered liquidity but no yield. A holder of USDC or Tether received no interest. Decentralized finance protocols offered yield, but through smart contract risk — lenders faced liquidation, oracle manipulation, or protocol collapse. Tokenized Treasuries attempt a third path: legitimate yield (from U.S. government bonds) with minimal counterparty risk (Treasury bonds have near-zero default risk) and full on-chain access.

When a project like Ondo Finance or Franklin Templeton tokenizes Treasury bonds, they hold the actual bonds in a custodian and mint tokens representing claims on those bonds. The token trades on-chain, can be used as collateral in DeFi protocols, and generates yield passed to holders. The yield is typically 4–5% annually (depending on bond duration and current rates), paid in the underlying token or stablecoins.

## Why institutions care

Tokenized Treasuries attract institutional crypto investors — hedge funds, family offices, yield-focused asset managers — who need regulatory clarity and genuine returns. Traditional stablecoins offer no yield. Money market funds offer yield but aren't on-chain. Tokenized Treasuries split the difference.

They also allow financial institutions to enter DeFi without building custom integrations. A fund can buy Tokenized Treasury tokens on a decentralized exchange, hold them in a crypto custody solution, and use them as collateral for loans on DeFi protocols. They earn Treasury yield while maintaining exposure to blockchain infrastructure.

Large institutional crypto funds have accumulated billions in these instruments. They represent a structural bridge from traditional finance into crypto rails.

## How the infrastructure works

A typical tokenized Treasury setup involves:

1. **Custodian:** A regulated third party (often a major bank like BNY Mellon or a crypto-native custodian like Coinbase Custody) holds the actual Treasuries.

2. **Token issuer:** A blockchain project or a traditional financial firm (like Franklin Templeton's on-chain Treasury fund) mints tokens representing the bonds. The issuer verifies that tokens and underlying bonds are always backed one-for-one (or within a small tolerance).

3. **Smart contract:** Code on Ethereum or another blockchain manages minting, redemption, and yield distribution. Redemptions are asynchronous — a token holder may need to wait 1–3 days for their Treasuries to be unblocked and liquidity provided.

4. **Secondary markets:** Tokens trade on decentralized exchanges (Uniswap, Curve) and some centralized exchanges. This creates liquidity even though the underlying bonds aren't instantly tradeable.

The yield from bonds is distributed pro-rata to token holders, usually daily or weekly.

## Execution risk and the custody problem

Tokenized Treasuries are not risk-free. The Treasury bonds themselves are safe, but the operational chain isn't:

**Custodial risk:** If the custodian is compromised or goes insolvent, token holders have a claim on the institution's assets, but it's a legal claim, not an on-chain guarantee. Most custodians use insurance and segregated accounts, but this introduces traditional finance counterparty risk.

**Smart contract risk:** The token contract could have bugs. Yield distribution could stall. Redemption mechanisms could fail. Most issuers audit their contracts, but exploits are rare rather than impossible.

**Regulatory risk:** Tokenized Treasuries exist in a gray zone. The SEC has not formally blessed them as non-securities, though the Treasury Department and Federal Reserve have expressed openness. An adverse regulatory ruling could force issuers to halt minting or redemptions.

**Basis risk:** If bond yields fall sharply, a token holder locked in at 5% yield might find that new Treasuries offer only 2%. The token's secondary market price will reflect the new rate environment, creating mark-to-market losses.

## Why not just buy Treasuries directly?

For most retail investors and many institutions, direct Treasury ownership is simpler and cheaper. You can buy a Treasury bill at a bank or through your brokerage, hold it to maturity, and receive par plus interest. No smart contract risk. No custody intermediaries.

Tokenized Treasuries make sense for:

- **DeFi participants** who want yield while remaining on-chain without bridging to traditional brokerage systems.
- **International investors** who find on-chain Treasury access simpler than opening U.S. bank accounts.
- **Institutions using Treasuries as collateral** in DeFi lending protocols, where on-chain assets integrate directly into protocols.

For someone who just wants a safe fixed-income allocation, a traditional money market fund or Treasury bond is probably better.

## The yield-farming layer

Tokenized Treasury tokens themselves are sometimes deposited into yield farms or lending protocols that offer additional incentives. A user might buy a Tokenized Treasury token (earning 4% from the underlying bond), then stake it in a protocol to earn governance tokens or protocol rewards (earning another 2–3%). This layering of yield is lucrative but concentrates smart contract risk.

Some users treat Tokenized Treasury tokens as a base layer — the safest yield available on-chain — and use them as collateral for leverage trades elsewhere. This leverage reintroduces the counterparty risk that Tokenized Treasuries were meant to minimize.

## See also

<div class="wiki-seealso">

### Closely related

- [Treasury Bill](/treasury-bill/) — the underlying instrument being tokenized
- [Blockchain Fundamentals](/blockchain-fundamentals/) — the infrastructure enabling on-chain Treasuries
- [SAFT Agreement](/saft-agreement/) — an earlier crypto fundraising instrument
- [Initial Coin Offering](/initial-coin-offering/) — the precursor to modern token offerings
- [Cryptocurrency Exchange](/cryptocurrency-exchange/) — where Treasury tokens trade

### Wider context

- Decentralized Finance — the ecosystem consuming Treasury tokens as collateral
- [Federal Reserve](/federal-reserve/) — issuer of policy affecting Treasury yields
- [Interest Rate](/interest-rate/) — the driver of Treasury valuations
- [Credit Risk](/credit-risk/) — minimal for government bonds, but custodial risk remains

</div>
