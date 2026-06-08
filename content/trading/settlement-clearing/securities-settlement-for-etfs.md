---
title: "Securities Settlement for ETF Creation and Redemption"
description: "Securities settlement for ETF creation and redemption involves in-kind delivery of the underlying basket from authorized participants to the fund on T+1 or T+2, settled through the CSD."
keywords:
  - securities settlement
  - etf creation redemption
  - authorized participant
  - in-kind delivery
  - central securities depository
  - settlement cycle
---

*When an authorized participant creates or redeems shares of an **ETF**, the fund and the participant must settle the physical (or electronic) transfer of the underlying securities. Rather than cash, ETFs typically use **securities settlement** to exchange in-kind baskets of stocks or bonds on a standard T+1 or T+2 cycle through the central securities depository—the same infrastructure that clears regular equity trades.*

<div class="wiki-hatnote">

This article covers the post-trade mechanics of ETF share creation and redemption. For the economic incentives driving in-kind delivery and arbitrage, see authorized participant and ETF premium/discount.

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Securities Settlement for ETF Creation and Redemption — key facts</div>

<img src="/svg/trading.svg" alt="An abstract editorial mark for trading and markets." />

<div class="wiki-infobox-caption">ETF creation and redemption settle as in-kind basket transfers, not cash, via the central depository.</div>

|   |   |
|---|---|
| **Settlement standard** | T+1 (same-day) or T+2 (next business day), depending on the asset class and jurisdiction |
| **Delivery mechanism** | In-kind: the AP delivers the full basket of securities; the fund issues shares |
| **Custodian role** | Holds the ETF's securities and verifies the basket matches the fund's required composition |
| **Clearing venue** | Central Securities Depository (CSD) in the relevant country; e.g., Depository Trust & Clearing Corp. (DTCC) in the U.S. |
| **Failure penalty** | Late settlement incurs fees; repeated failures can lead to suspension of creation privileges |
| **Cash component** | Usually <2% "cash in lieu" allowed to handle rounding or intra-day fractional shares |

</aside>

## How Authorized Participants Initiate Settlement

An **authorized participant** (AP) is a licensed firm—typically a broker-dealer or bank—that holds creation/redemption privileges with the ETF issuer. When the AP decides to create new ETF shares, it submits a creation order specifying the number of shares it wants and deposits the corresponding basket of securities with the fund's custodian.

The AP does not deliver the securities directly to the fund. Instead, it instructs its broker or custodian to settle the trade in the name of the ETF issuer through the central depository. For U.S. equities, this means a transfer on the books of the Depository Trust Company (DTC), which acts as the CSD. For European stocks, settlement flows through Euroclear or Clearstream. For futures, swaps, and other derivatives, settlement occurs through the relevant clearing house.

## The Settlement Timeline: T+1 and T+2

Most equity ETFs settle **T+1**—one business day after the AP's creation order is executed. This means if the AP submits the basket on a Monday, it settles by Tuesday morning. The AP's custodian debits the securities from the AP's account, and the CSD credits them to the ETF's omnibus account (a pooled account held for the fund's shareholders). Simultaneously, the ETF issuer credits the AP's account with the newly created shares.

Some asset classes and jurisdictions use **T+2**: bond ETFs in some regions, emerging-market ETFs, and futures-based products. The longer settlement window allows time for clearance in less liquid or more fragmented markets.

For **redemption**, the sequence reverses. The AP delivers the shares to the ETF's custodian. Once the custodian confirms receipt and the CSD transfers the shares out of the ETF's account, the fund delivers the underlying basket to the AP. If there is a delay—the AP's broker is slow, or the CSD is congested—the redemption settles on T+2 or later.

## The Custodian's Role

The fund's custodian is responsible for verifying that the delivered basket matches the fund's required composition. If the AP delivers 30,000 shares of Apple, 20,000 of Microsoft, and 15,000 of Tesla (for a tech ETF), the custodian confirms that:

1. The share counts match the creation order exactly (or fall within a small tolerance for fees and rounding).
2. The shares are free of liens or encumbrances.
3. The settlement instruction is valid and properly formatted.

Only after this verification does the custodian instruct the CSD to move the securities. If there is a mismatch—the AP delivers 29,500 Apple shares instead of 30,000—the fund can reject the basket. The AP must correct it or eat the cost of buying the missing shares on the open market to complete the creation.

## Cash in Lieu and Fractional Shares

ETF baskets sometimes include fractional shares or cash to handle rounding or to fill a gap if a security is illiquid or halted. The fund's prospectus typically allows a small cash component—often 1–2% of the basket value—in place of the actual security.

If the basket is worth $100,000 and includes $98,000 in securities and $2,000 in cash, the AP sends the $98,000 in stocks and $2,000 in dollars to the custodian. The custodian credits the AP with the full creation-redemption shares. This mechanism prevents the AP from being forced to trade illiquid securities on the open market just to complete a settlement.

## Settlement Fails and Penalties

If the AP fails to deliver the basket by the settlement deadline, the fund's custodian initiates a "buy-in"—the custodian purchases the missing securities on the open market and charges the cost to the AP. The AP also pays interest on the fail. In severe or repeated cases, the ETF issuer can suspend the AP's creation privileges, which effectively prevents the AP from arbitraging the fund.

Similarly, if the ETF issuer fails to deliver shares (rare, but possible if the fund has operational issues), the AP incurs damages and can claim losses.

## Clearance Through the Central Depository

All settlement ultimately flows through the CSD. The DTC (in the U.S.) is a subsidiary of the Depository Trust & Clearing Corp. (DTCC) and settles trillions of dollars in securities transfers daily. The CSD's computer systems match both sides of the trade: the AP's delivery of securities and the ETF issuer's issuance of shares.

Once both legs are verified and matched, the CSD executes a "simultaneous bilateral transfer": securities move from the AP's account to the ETF's account, and shares move from the ETF account to the AP's account. This atomic swap eliminates settlement risk—neither side can fail without the other, because both movements happen at the same instant on the CSD's books.

## Timing Implications for Arbitrage

The settlement timeline is critical for ETF arbitrage. If an ETF is trading at a 2% discount to its net asset value (NAV), an AP can buy the ETF shares in the market and simultaneously short the underlying basket, then redeem. If the redemption settles T+1, the AP receives the underlying securities T+1 and must cover the short by T+1. If there is a one-day lag in CSD processing, the AP is briefly short without cover—a settlement risk.

Modern **settlement-for-value** models (also called "guaranteed settlement") require the CSD to guarantee that both legs of the redemption settle atomically, eliminating this timing mismatch. As of 2025, most major CSDs have adopted guaranteed settlement for ETF creation-redemption.

## See also

<div class="wiki-seealso">

### Closely related

- [Authorized participant](/authorized-participant/) — the intermediary who creates and redeems ETF shares
- [ETF](/etf/) — the fund structure and how in-kind settlement supports its mechanics
- [ETF premium/discount](/etf-premium-discount/) — how settlement timing affects arbitrage pricing
- [Custodian](/custodian/) — the operator who holds the securities and verifies basket delivery
- [Intraday liquidity patterns and execution timing](/intraday-liquidity-pattern-and-execution-timing/) — how APs time large basket trades
- [Secondary market](/secondary-market/) — where investors and APs trade ETF shares, distinct from creation-redemption

### Wider context

- Settlement cycle — the broader T+1/T+2 infrastructure
- [Central securities depository](/central-securities-depository/) — the institution that clears all trades
- [Depository Trust & Clearing Corp.](/federal-deposit-insurance-corporation/) — U.S. operator of DTC and DTCC
- [Price discovery](/price-discovery/) — how arbitrage through creation-redemption keeps ETF prices aligned with NAV
- [Securitization](/securitization/) — a related settlement mechanism for mortgage-backed and asset-backed securities

</div>