---
title: "Borrowing Against Crypto vs Selling: DeFi Tax Implications"
description: "How collateralized DeFi loans avoid taxable disposal, contrasting tax treatment and risk profile of borrowing against crypto versus selling."
keywords:
  - defi borrowing crypto
  - borrowing against crypto
  - crypto loan tax
  - collateralized loan defi
  - avoiding capital gains
  - crypto disposal
image: "/svg/crypto.svg"
---

*In **borrowing against crypto vs selling**, the key difference is whether you dispose of your asset (triggering a taxable event) or use it as collateral for a loan (avoiding immediate taxation). A DeFi borrower deposits cryptocurrency as collateral into a [smart contract](/distributed-ledger/) and receives stablecoin or fiat in return, deferring [capital gains tax](/capital-gains-tax-investor/) until the loan is repaid or the collateral is liquidated.*

## The Collateral Mechanism in DeFi

Decentralized lending protocols like Aave, Compound, and MakerDAO use cryptocurrency collateral to secure loans. When you deposit 1 Bitcoin as collateral, you do not sell it. Instead, the smart contract locks it in an escrow smart contract and issues you a claim token (often a wrapped version of the original asset) that represents your deposit. You can then borrow against this collateral—typically 50–80% of its value, depending on the protocol and the volatility of the underlying asset.

The borrowed amount is usually issued in stablecoin form (USDC, DAI, USDT) or Ethereum, giving you liquidity without touching your Bitcoin holdings. You pay interest on the borrowed amount—rates vary from 2% to 10% annually depending on market conditions and which protocol you use. As long as you hold the collateral in the smart contract and the collateral value remains above the minimum threshold (called the collateralization ratio), your original crypto asset is not sold and remains exposed to price appreciation.

## Tax Treatment: Borrowing vs Selling

**Selling cryptocurrency is an immediately taxable event.** If you bought Bitcoin for $30,000 and sell it for $50,000, you owe [capital gains tax](/capital-gains-tax-investor/) on the $20,000 gain. If you held it for more than one year, you owe long-term capital gains tax; under one year, short-term (usually taxed as ordinary income at higher rates). The tax is due in the tax year of the sale, regardless of whether you reinvest the proceeds.

**Borrowing against cryptocurrency is not taxable upon loan origination.** The IRS does not treat a collateralized loan as a disposal of the underlying asset—the crypto remains yours for tax purposes. You do not recognize a gain or loss when you borrow against it. The only tax consequence is the interest paid: interest on a loan used for investment purposes may be deductible as an investment expense (subject to limits), though the rules are complex and opinions vary.

However, when you eventually repay the loan and reclaim your collateral, there is still no tax event—you are simply unwinding the loan. The tax event occurs only if:

1. **The collateral is liquidated** during the loan term (because the price fell and you fell below the collateralization ratio). At that moment, the smart contract automatically sells a portion of your collateral to repay the loan. This forced sale triggers capital gains or losses.

2. **You sell the collateral intentionally** after reclaiming it from the smart contract.

3. **The borrowed asset appreciates and you sell it.** If you borrow USDC and use it to buy another cryptocurrency, and that crypto gains value, you owe tax on that gain when you sell it.

## Why Borrowing Defers Gains

The tax deferral benefit is significant for long-term holders seeking liquidity. Suppose you have $500,000 of Bitcoin and need cash for a business investment or home down payment. You can either:

- **Sell $100,000 of Bitcoin.** If you have an unrealized gain of $300,000 (bought at $100,000, now worth $400,000), selling $100,000 triggers a $75,000 taxable gain. You owe federal long-term capital gains tax (20% if you're in the highest bracket) plus state tax—potentially $15,000–$20,000 in taxes, reducing your cash to $80,000–$85,000.

- **Borrow $100,000 against Bitcoin.** You deposit $150,000–$200,000 of Bitcoin as collateral (to maintain a 75% collateralization ratio, a typical threshold), borrow $100,000 USDC, and pay 3–5% annual interest. Your Bitcoin remains intact and exposed to future appreciation. You owe no tax upon borrowing. If Bitcoin appreciates another 50% in the following two years, that additional $250,000 gain is tax-deferred.

The cost is the interest: on $100,000 at 4% annually, you pay $4,000 per year in interest. But if your Bitcoin is expected to appreciate 20%+ annually, or if you can deploy the borrowed capital into an investment returning 8%+ annually, the interest cost is economically worthwhile.

## Risks of Liquidation

The primary downside of borrowing is **liquidation risk**. If the price of your collateral falls sharply, the smart contract may force-sell your collateral to protect the lender. In Aave, for example, if you borrow against Bitcoin at a 75% ratio (you can borrow $7,500 for every $10,000 deposited), a 25% drop in Bitcoin's price brings you to the liquidation threshold. A liquidator bot automatically sells your collateral to repay the loan, triggering a forced tax event and capturing your unrealized loss as a realized tax event.

Additionally, **interest and liquidation penalties compound.** If you borrow for 10 years and only pay interest, you may owe more in interest than your original borrowed amount. If you are liquidated, you also pay liquidation fees (typically 5–10% of the collateral sold), which are irretrievable losses.

## Staking and Income Taxation

An indirect risk in DeFi borrowing involves **yield farming.** Some protocols offer yield rewards for depositing collateral—Compound, for example, distributes COMP tokens to lenders. These rewards are ordinary income and are taxable when received, not when sold. If you borrow $100,000 and receive $5,000 of COMP in year one, you owe income tax on $5,000 immediately, even though you never sold the COMP.

## Timing and Planning

Borrowing is most attractive when:

- You have unrealized gains exceeding 50% of your cost basis.
- You expect the collateral to appreciate further.
- You need liquidity for at least 2–3 years (to amortize interest costs).
- Interest rates are below 5% annually.
- The protocol has a strong track record and your liquidation risk is manageable.

Selling is more appropriate when:

- You are uncertain about future price direction.
- You need cash without ongoing repayment obligations.
- You have tax losses to offset the gains ([tax loss harvesting](/tax-loss-harvesting/)).
- You expect lower future returns from the collateral.

## See also

<div class="wiki-seealso">

### Closely related

- [Capital Gains Tax Investor](/capital-gains-tax-investor/) — how gains are taxed upon disposal
- [Tax Loss Harvesting](/tax-loss-harvesting/) — using realized losses to offset gains
- [Cryptocurrency Exchange](/cryptocurrency-exchange/) — spot trading and asset disposal
- [Distributed Ledger](/distributed-ledger/) — blockchain infrastructure underlying DeFi protocols
- [Gift Tax on Cryptocurrency Transfers](/gift-tax-on-cryptocurrency-transfers/) — tax rules for transfers to others

### Wider context

- [Interest Rate](/interest-rate/) — how borrowing costs are determined
- Collateral — general concept of securing loans (article not in allowlist; cross-link only if appropriate)
- [Liquidation](/liquidation/) — forced asset sales when collateral thresholds are breached

</div>
