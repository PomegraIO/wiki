---
title: "Securities Lending: How It Works"
description: "How securities lending works: custodians lend shares and bonds to borrowers, who post collateral. Learn fees, recall rights, and risks for investors."
keywords:
  - how securities lending works
  - securities lending mechanics
  - securities lending collateral
  - lending agents
  - stock lending process
image: "/svg/institutions.svg"
---

*How securities lending works is a mechanism where a **custodian**—typically a bank holding securities on behalf of an investor or fund—lends those shares or bonds to a borrower (usually a hedge fund or trader) for a fixed term in exchange for collateral and a fee. The borrower must return identical securities, the lender earns a revenue stream without selling the position, and a lending agent (often the custodian itself) administers collateral, recall rights, and settlement.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Securities Lending — key facts</div>

<img src="/svg/institutions.svg" alt="An abstract editorial mark for financial institutions." />

<div class="wiki-infobox-caption">A low-visibility income source for passive portfolios; a tool for short-sellers and arbitrageurs.</div>

|   |   |
|---|---|
| **Lender** | Custodian or beneficial owner of shares/bonds |
| **Borrower** | Trader, hedge fund, or other entity needing to short or arbitrage |
| **Collateral** | Cash or securities, typically 100–110% of borrowed security value |
| **Fee structure** | Rebate (paid to borrower), utilization fee (paid to lender) |
| **Term** | Overnight, term lending, or open (indefinite, callable) |
| **Recall right** | Lender can demand return of securities on notice (often 1 trading day) |

</aside>

## The Basic Flow

Securities lending begins with ownership. An asset manager, pension fund, or wealthy individual holds a portfolio. A custodian (a bank like BNY Mellon or State Street) holds these securities in safekeeping. The beneficial owner earns no fee for the custodian's service; instead, the custodian often keeps a small spread on dividends or interest, or the account is fee-generating.

To make money on idle securities, the custodian (or the beneficial owner, if authorized) lends them out. A hedge fund wants to short sell a stock—it wants to sell shares it doesn't own, betting the price will fall, and then buy them back cheaper. To settle the short sale, the exchange demands it deliver shares. So the hedge fund borrows them. Alternatively, a trader might borrow a bond to execute a basis trade (longing the future, shorting the spot) or an arbitrage.

The custodian transfers the shares or bonds to the borrower's account. The borrower posts **collateral**—usually cash or liquid securities—equal to at least the market value of the borrowed securities, often 102–110% to cover price volatility. This collateral is held in a segregated account and marked to market daily.

The borrower pays a **lending fee** (often called the rebate or haircut rebate), which is a percentage of the collateral value per annum. The custodian and beneficial owner split this fee by agreement. If the borrower posts cash, they might also receive an interest rebate (a portion of the interest earned on the collateral), because the lender is profiting from that interest too.

## Collateral and Marking to Market

The collateral is the lender's safety net. If the borrower fails to return the securities and defaults, the lender can liquidate the collateral to buy them back in the open market.

The challenge is price risk. The borrowed securities may rise or fall. If they rise sharply, the collateral (fixed in nominal amount) falls short. Most lending agreements require **daily marking to market**: the collateral amount is adjusted daily to equal the new market value of the lent securities plus a haircut. If a borrowed stock rises 5%, the borrower must post 5% more collateral. If it falls, the borrower receives collateral back.

This daily settlement protects the lender from default risk but creates cash flow volatility for the borrower. A large move can force the borrower to post significant additional collateral overnight, draining cash reserves.

## Recall Rights and Duration

Securities lending is not permanent. Most loans are **open** (indefinite, callable) or **term** (fixed duration). On an open loan, the lender can recall the securities—demand their return—on short notice, often one trading day. This protects the beneficial owner, who may need to sell the position or exercise voting rights (though custodians and lenders typically handle this).

Borrowers dislike recall risk; it forces them to return borrowed shares even if their trade is not yet profitable, or to pay a fee to extend the loan. Some loans are **term**: fixed for 30, 90, or 180 days, after which the borrower returns the securities or the loan rolls.

Highly liquid, heavily shorted securities (Tesla, Gamestop, certain tech stocks) have tight lending markets and high fees, because many borrowers compete for a limited supply and lenders know there is strong demand. Illiquid securities have low or near-zero lending fees; few borrowers want them.

## The Role of Lending Agents

Large custodians often manage a dedicated **securities-lending program**. The agent (the custodian's lending desk) contacts potential borrowers, quotes lending fees, negotiates terms, and matches borrowers to lenders. The agent:

- Maintains a database of loanable securities and their available quantities
- Quotes fees to borrowers and negotiates rates
- Arranges settlement and transfer of securities to the borrower
- Monitors collateral daily and adjusts for price moves
- Processes recalls and loan returns
- Handles corporate actions (dividends, stock splits, tender offers) on lent securities

The agent typically takes a spread: it quotes a borrower a fee of 15 basis points (0.15%) per annum, but pays the beneficial owner 5 basis points (0.05%), keeping a 10 basis point spread.

## Income and Risk for the Beneficial Owner

From the perspective of a passive investor, securities lending is a way to earn additional income on a portfolio. An index fund holding a large position in a liquid stock can lend it, earn 5–20 basis points per annum, and keep the upside if the price rises. Over many positions, this adds up: a 0.3% annual boost to returns is significant for an index fund with a 0.05% expense ratio.

The risks are subtle. The lender retains voting rights in theory but often delegates them to the borrower during the loan. If the borrower votes against the beneficial owner's interests (e.g., votes for a hostile takeover), this becomes contentious. Most custodial agreements specify that the beneficial owner retains voting rights and will instruct the lending agent how to vote, but in practice, large-scale lending can dilute control.

More significantly, the lender is exposed to borrower creditworthiness and collateral risk. If the collateral is other securities and those assets collapse, the lender's collateral is worth less precisely when it is needed—when the borrower defaults.

## Regulatory and Clearing Considerations

Securities lending is regulated but loosely. In the US, the SEC requires lending agents to maintain records and segregate collateral. Custodians must have systems to manage collateral daily and recall loans. However, rules differ by asset class and jurisdiction.

In Europe, securities financing transactions (SFTs), including lending, fall under SFTR (Securities Financing Transactions Regulation), which requires reporting to a central repository. This increases transparency and reduces counterparty risk in the system.

For equity lending in the US, stock borrows can clear through the Depository Trust Company (DTC) or over-the-counter. OTC equity lending is opaque, making hard-to-borrow stocks (those with few shares outstanding or high short interest) very expensive.

## See also

<div class="wiki-seealso">

### Closely related

- [Custodian](/custodian/) — Financial institution holding securities; manages lending programs
- [Short selling](/short-selling/) — Selling a security one does not own; requires borrowing shares
- [Counterparty risk](/counterparty-risk/) — Risk that the borrower fails to return securities or defaults
- Collateral — Asset posted as security; critical to managing lending risk
- [Repurchase agreement](/repurchase-agreement/) — Similar mechanism using bonds and repos; a cousin to securities lending

### Wider context

- [Broker](/broker/) — Entity facilitating trades; often involved in securities lending
- [Derivative](/derivatives-hedging/) — Securities lending enables certain derivative strategies
- Arbitrage — Traders often borrow securities to execute arbitrage
- [Market maker](/market-maker-trading/) — May borrow securities to provide liquidity

</div>
