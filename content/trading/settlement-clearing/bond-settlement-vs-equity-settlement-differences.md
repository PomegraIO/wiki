---
title: "Bond Settlement vs Equity Settlement: Key Differences"
description: "Compare settlement cycles, conventions, and infrastructure for bonds and equities, from T+0 to T+2 timelines and accrued interest."
keywords:
  - bond settlement
  - equity settlement
  - settlement cycle differences
  - fixed income settlement
  - accrued interest
  - bond trading settlement
  - settlement convention
---

*While equities and bonds both move through a settlement system to transfer ownership and funds, they follow fundamentally different timelines, pricing conventions, and institutional pathways. Bond settlement can happen as early as the same day (T+0), while equities typically settle T+1; bonds accrue interest daily and are priced "plus accrued," while equities are not. Understanding these distinctions matters for traders, portfolio managers, and anyone dealing with [fixed-income](/bond/) instruments.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Bond vs Equity Settlement — key facts</div>

<img src="/svg/trading.svg" alt="An abstract editorial mark for trading infrastructure." />

<div class="wiki-infobox-caption">Bond and equity settlement differ in speed, pricing convention, and the infrastructure used.</div>

|   | Equities | Bonds |
|---|---|---|
| **Typical settlement cycle** | T+1 | T+0 or T+1 (varies) |
| **Pricing convention** | Clean price (no interest) | Dirty price (includes accrued interest) |
| **Interest accrual** | None (only dividends) | Daily accrual; buyer pays seller accrued interest |
| **Clearing house role** | Central (mandatory) | Lighter; many trades clear bilaterally |
| **CSD use** | Always; immobilized or dematerialized | Usually, but less standardized |
| **Netting** | Aggressive; multilateral netting common | Conservative; often bilateral netting |
| **Trading venues** | Centralized exchanges | Decentralized; mostly over-the-counter |
| **Settlement instruction matching** | Highly automated | Often manual or semi-automated |
| **Failure frequency** | Rare | More common (especially in emerging markets) |
| **Repo vs outright** | Repo less common in equities | Repo is primary market for short-term funding |

</aside>

## Why Bonds and Equities Differ

The gap between bond and equity settlement stems from their economic natures. A [stock](/stock/) is a claim on a company's residual cash flows after all obligations are met. An equity trade is a simple swap: buyer gets shares, seller gets cash. The transfer date is mechanical; accrued value is zero.

A [bond](/bond/) is a fixed-income obligation. It carries a coupon—periodic interest—and that interest accrues daily. When a buyer purchases a bond halfway through a coupon period, the seller has "earned" part of the next coupon payment (accrued interest), and the buyer will owe it. This means bond pricing must account for accrued interest, and bond settlement must transfer that accrued amount from buyer to seller, in addition to the security itself.

This one feature—accrued interest—cascades into different clearing practices, settlement timelines, and infrastructure choices.

## Settlement Cycle: Speed Differences

**Equities** settle T+1 in most developed markets (as of 2024). A trade on Monday settles Tuesday. The buyer receives shares; the seller receives cash. No interest is involved, so there is no pressure to settle faster.

**Bonds** settle much faster—often T+0 (same day) in developed markets. A U.S. government bond traded at 10 a.m. might settle before market close the same afternoon. Corporate and municipal bonds often settle T+1 but with greater flexibility; some trades can settle T+0 or T+2 depending on agreement.

The faster bond settlement reflects two pressures: (1) bonds are short-term funding vehicles and traders need quick access to cash, and (2) the daily accrual of interest makes delay costly—waiting an extra day changes the accrued amount and forces repricing.

## Pricing: Clean vs Dirty

**Equities** are quoted and traded on a *clean price*—the price you see on a screen is the price you pay (plus a [bid-ask spread](/bid-ask-spread/), of course). There is no hidden cost.

**Bonds** are quoted on a *clean price* but settled on a *dirty price*. The dirty price = clean price + accrued interest.

### Example: Corporate Bond Settlement

Suppose an ABC Corp bond with a $1,000 par value and a 4% annual coupon is trading. The coupon is paid twice yearly, $20 per payment. The last coupon was paid 45 days ago; the next coupon is due in 135 days.

Accrued interest = ($20 × 45 days) / 180 days = $5.

If the bond's clean price is quoted as $98 (meaning $980 per bond), the dirty price (settlement price) is $980 + $5 = $985 per bond.

The buyer pays $985 per bond at settlement. The seller receives $985 per bond. Of that $985, $5 is accrued interest (which belongs to the seller because it earned interest during the 45-day holding period) and $980 is the principal.

This calculation happens automatically in bond settlement systems, but it means every bond trade effectively bundles a principal transfer with an interest transfer. Equities have no equivalent: a stock sale is purely principal.

## Clearing Infrastructure: Centralized vs Bilateral

**Equities** are routed through a central [clearing house](/clearing-house-margin-call-process/), which interposes itself as buyer to every seller and seller to every buyer. The clearing house nets trades, collects [margin](/clearing-house-margin-call-process/), and manages counterparty risk.

**Bonds** use a lighter-touch model. Many institutional bond trades are cleared bilaterally, meaning the buyer and seller confirm the trade directly with each other without a central clearing house in between. Some bond venues (especially those for government bonds) use central clearing, but the infrastructure is less standardized than for equities.

This difference reflects the bond market's structure: it is fragmented and over-the-counter, with direct relationships between dealers and clients. Equities trade on centralized exchanges with standardized contracts, so central clearing is practical.

## Settlement Instruction Matching

For equities, both sides' settlement instructions are submitted electronically and automatically matched by the [CSD](/csd-role-in-securities-settlement/). If the trade details (shares, price, counterparty IDs) match, the instruction is queued for settlement. Mismatches are flagged and rejected.

For bonds, especially corporate bonds, settlement instructions are often submitted manually or via older messaging protocols. Matching can be slower. Fails are more common because instructions arrive late or contain errors.

## Role of the CSD

Equities almost always settle through a [central securities depository](/csd-role-in-securities-settlement/). The CSD holds the shares, records ownership in its ledger, and orchestrates the T+1 transfer.

Bonds vary. Government bonds often use a CSD but may also use a central bank's settlement system (for example, many Treasuries settle through the Federal Reserve's book-entry system, which predates and is separate from typical CSDs). Corporate and municipal bonds use CSDs in developed markets but may use physical certificates or alternative systems in emerging markets.

## Netting Practices

Equities benefit from aggressive multilateral netting. A clearing house nets all of a participant's trades across hundreds of securities in real-time or batch, reducing the number of settlements needed.

Bonds typically use bilateral netting—each pair of counterparties nets their mutual obligations. This is less efficient but reflects the bilateral nature of bond trading.

## Fails: Frequency and Tolerance

Equity fails are rare in developed markets, typically under 0.1% of trades. The infrastructure is mature, settlement is T+1 which is tight but achievable, and regulatory penalties for fails are strict.

Bond fails are more common, especially in corporate bonds and in emerging markets. A fail rate of 1-5% is not unusual. Several factors contribute: (1) bonds trade over-the-counter with less standardization, (2) matching is manual, (3) the bond market is fragmented across multiple CSDs and custodians, (4) market disruptions (like those in March 2020) can spike fails.

## Repo Market: Financing via Bond Settlement

The [repo](/repurchase-agreement/) (repurchase agreement) market is massive in fixed-income but barely exists in equities. A repo is a simultaneous sale and forward repurchase of a bond. Dealer A sells a bond to Dealer B for cash (the repo rate determines the cost of the financing). Dealer B agrees to sell it back in 1 day, 1 week, or 1 month. From a settlement standpoint, two separate settlements occur: the initial outright sale settles immediately (T+0), and the forward repurchase settles on the agreed date.

Repo is used for short-term financing because it is quick and low-friction. An equity repo market exists but is tiny, because equity traders prefer outright sales and [short selling](/short-selling/) for financing needs.

## Cross-Border Bond Settlement

Bonds issued by non-U.S. entities or denominated in foreign currencies settle through the relevant foreign CSD or central bank. A Japanese government bond (JGB) settles in Japan; a Eurobond settles through Euroclear. Cross-border bond trades introduce additional settlement lag because two CSDs and two payment systems must coordinate. Many bonds settle T+2 or even T+3 due to cross-border friction.

## Convertible and Hybrid Bonds

[Convertible bonds](/convertible-bond/) are a hybrid: they settle like bonds (T+0 or T+1, with accrued interest) but can be converted into equity. Once converted, they trade and settle like equities.

## Key Practical Implications

For a trader:

- Bond trades often settle faster, reducing financing costs and allowing quicker redeployment of capital.
- Bond prices always include accrued interest; the dirty price is what you pay, not the quoted clean price.
- Bilateral clearing means more manual work; fails are more likely.
- The settlement timeline is flexible—you can negotiate T+0, T+1, or T+2 depending on market conditions and counterparty agreement.

For an investor:

- When buying a bond, expect to pay accrued interest (bundled into the settlement price).
- Bond settlements are less standardized than equity settlements; keep cash on hand for T+0 settlement.
- In a market disruption (like March 2020), bond settlement can break down; equity settlement is more resilient.

---

## See also

<div class="wiki-seealso">

### Closely related

- [Cash Equities Settlement Cycle Explained](/cash-equities-settlement-cycle-explained/) — Detailed walk-through of T+1 equity settlement
- [Central Securities Depositories: Role in Settlement](/csd-role-in-securities-settlement/) — The infrastructure used for both bonds and equities
- [How a Clearing House Issues a Margin Call](/clearing-house-margin-call-process/) — Risk management (more developed for equities)
- [Bond](/bond/) — Fixed-income instruments and their cash flows
- [Stock](/stock/) — Equity instruments

### Wider context

- [Coupon Payment](/coupon-payment/) — The interest component that drives bond settlement complexity
- [Accrual Accounting](/accrual-accounting/) — The accrued-interest concept applied to bonds
- [Repurchase Agreement](/repurchase-agreement/) — Bond financing via repo; essentially nonexistent for equities
- [Price Discovery](/price-discovery/) — How both assets are priced pre-settlement
- [Securities and Exchange Commission](/securities-and-exchange-commission/) — Regulates U.S. equity and bond settlement

</div>
