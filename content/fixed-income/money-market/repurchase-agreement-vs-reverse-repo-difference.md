---
title: "Repo vs Reverse Repo: Same Trade, Two Perspectives"
description: "Why repo and reverse repo describe the same transaction from opposite sides; explained with a single example."
keywords:
  - difference between repo and reverse repo
  - repurchase agreement reverse repo
  - repo vs reverse repo
  - reverse repurchase agreement
image: "/svg/fixed-income.svg"
---

*A **repo** and a **reverse repo** are not two different transactions — they are the same transaction seen from opposite ends. When a [bond](/bond/) trader says "I'm doing a repo," they mean they are selling a security with an agreement to buy it back. When the counterparty says "I'm doing a reverse repo," they mean they are buying that same security with an agreement to sell it back. The confusion arises because the trade has two names, one for each participant. Understanding this perspective flip is essential for reading financial news, as [central banks](/central-bank/), dealers, and [hedge funds](/hedge-fund/) all use the terms to describe their own side of the transaction.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Repo vs Reverse Repo — key facts</div>

<img src="/svg/fixed-income.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">One trade, two voices: the naming is relative to the speaker, not the securities.</div>

|   |   |
|---|---|
| **Same transaction?** | Yes. Repo to the seller = reverse repo to the buyer. |
| **Cash driver** | Seller needs cash short-term; buyer has excess cash. |
| **Security involved** | [Treasury](/treasury-bond/), corporate [bond](/bond/), mortgage-backed. Any marketable instrument. |
| **Term** | Overnight (ON), 1-week, 1-month, or longer. |
| **Rate** | The [repo rate](/repurchase-agreement/) is the interest charged; determined by supply and demand. |
| **Typical users** | Dealers (funding), hedge funds (leverage), central banks ([monetary policy](/monetary-policy/)), [custodians](/custodian/). |
| **Risk** | [Counterparty risk](/counterparty-risk/), [liquidity risk](/liquidity-risk/), [haircut](/repurchase-agreement/) adjustment. |

</aside>

## The Perspective Flip

Imagine a bond dealer at Goldman Sachs holding $100 million of 10-year Treasury bonds. It's Friday afternoon, and the dealer needs cash over the weekend to cover other trades. The dealer calls a [money market](/money-market-fund/) fund manager who has excess cash sitting idle.

**From the dealer's perspective:**
"I am **doing a repo.** I will sell you these $100 million Treasuries, and I promise to buy them back from you Monday morning at a slightly higher price. For example, I sell at 100 and repurchase at 100.01. The 0.01 difference is interest — the repo rate."

**From the fund manager's perspective:**
"I am **doing a reverse repo.** I will buy these $100 million Treasuries from you, and you promise to buy them back Monday morning at 100.01. I'm earning the repo rate as interest for lending my cash."

Both are describing the exact same transaction. The only difference is the vantage point. The dealer is borrowing cash and pledging securities as collateral; the fund is lending cash and receiving securities as collateral. But the securities sold and the securities repurchased are identical. The cash flow timing is identical.

## Why the Name Exists

The terms "repo" and "reverse repo" emerged from market practice and are baked into trading conventions, clearing systems, and regulatory terminology. The naming is relative, not absolute. There is no intrinsic "forward" direction.

When the [Federal Reserve](/federal-reserve/) conducts [open market operations](/monetary-policy/), it uses these terms from its own perspective. When the Fed wants to reduce money supply, it offers **reverse repos**: the Fed takes in cash from banks and brokers, and lends out securities in return. The Fed calls it a reverse repo because, from the Fed's seat, it is the reverse of the normal pattern it uses in other operations.

When a dealer needs funding, it uses the term **repo** because it is selling securities and buying them back — the "repurchase."

## A Worked Example

Let's detail the trade between the Goldman dealer and the fund manager:

| Actor | Action | Value | Rate |
|-------|--------|-------|------|
| **Dealer (seller)** | Sells Treasuries to fund on Friday | $100,000,000 | — |
| **Fund (buyer)** | Buys Treasuries from dealer on Friday | $100,000,000 | — |
| **Dealer** | Repurchases Treasuries from fund on Monday | $100,000,020 | 0.02% annualized |
| **Fund** | Resells Treasuries to dealer on Monday | $100,000,020 | 0.02% annualized |

**Dealer's journal entry (Friday):**
- Cash in: +$100,000,000
- Securities out: –$100,000,000 Treasuries
- Label: "Repo transaction"

**Fund's journal entry (Friday):**
- Cash out: –$100,000,000
- Securities in: +$100,000,000 Treasuries
- Label: "Reverse repo transaction"

**Settlement (Monday):**
- Dealer pays $100,000,020 and receives $100,000,000 Treasuries back.
- Fund receives $100,000,020 and delivers $100,000,000 Treasuries.

From the dealer's side, it is a classic repo: pledge collateral, borrow cash, repay with interest. From the fund's side, it is a reverse repo: lend cash against collateral, receive collateral, get cash back with interest.

## Why It Matters: Systemic and Individual

Understanding the perspective flip is critical for reading policy announcements and market analysis.

When news outlets report "The Federal Reserve injected liquidity via reverse repos," they mean the Fed is lending securities to banks to absorb cash (reducing money supply). From a dealer's perspective, the Fed is doing a repo (the Fed is the security seller and the dealer is the security buyer). But the Fed calls it a reverse repo because it is reversing its typical operation.

When a [hedge fund](/hedge-fund/) announces "We are using repo to leverage our positions," it means the fund is pledging securities to borrow cash and then deploy that cash to buy more securities. The fund is the borrower and sees the trade as a repo.

The two perspectives are not contradictory — they are complementary. Every repo has a counterparty doing a reverse repo. If you focus only on one side, you miss the full picture.

## Haircuts and Collateral Management

In practice, repos involve a **[haircut](/repurchase-agreement/)** — a discount applied to the collateral to protect the lender. If the dealer tries to repo $100 million of Treasuries, the lender (fund) may only lend $99 million, taking a 1% haircut. This protects the fund in case the security value falls; it can sell the collateral and still recover its cash.

Haircuts vary by security type, credit quality, and [volatility](/currency-volatility/). Treasury haircuts are typically 0.5–2%. Corporate bond haircuts are 5–15%. [Mortgage-backed securities](/mortgage-backed-security/) can be 10–25%.

These haircuts are negotiated between counterparties and may be adjusted intraday if collateral values move significantly. During stress periods (like March 2020), haircuts widen, making repo financing more expensive and harder to access.

## The Role in Money Markets and Central Bank Operations

Repos are the lifeblood of short-term funding for dealers, banks, and [hedge funds](/hedge-fund/). At any moment, hundreds of billions of dollars are circulating through the repo market.

The [Federal Reserve](/federal-reserve/), [European Central Bank](/european-central-bank/), and other central banks use repos as a primary tool of [monetary policy](/monetary-policy/). By adjusting the **repo rate** — the interest rate on overnight repos — they can influence [money supply](/monetary-policy/) and [short-term interest rates](/federal-funds-rate/). In late 2019, the Fed intervened heavily in the repo market after a sudden spike in overnight repo rates (the "repo crisis"), injecting liquidity through reverse repos to stabilize funding conditions.

## Common Pitfalls

A frequent source of confusion is that the same institution may be on both sides simultaneously. A dealer may be doing repos with one counterparty (borrowing cash) while simultaneously doing reverse repos with another counterparty (lending cash). From a net perspective, the dealer may be a cash borrower, but the individual trades are labeled differently depending on the direction.

Another pitfall is thinking that repo and reverse repo have different economic outcomes. They don't. The outcome is determined by the terms (the rate, the haircut, the collateral) and the counterparty creditworthiness, not by which label is used.

## See also

<div class="wiki-seealso">

### Closely related

- [Repurchase agreement](/repurchase-agreement/) — The mechanics, rates, and regulation of repo markets.
- [Money market](/money-market-fund/) — The ecosystem where repos are the primary tool.
- [Counterparty risk](/counterparty-risk/) — Why haircuts and collateral matter in repo.
- [Liquidity risk](/liquidity-risk/) — What happens when repo funding dries up.
- [Treasury bond](/treasury-bond/) — The most common collateral in repo transactions.
- [Monetary policy](/monetary-policy/) — How central banks use repos to manage money supply.

### Wider context

- [Federal Reserve](/federal-reserve/) — Operations that inject or drain liquidity via reverse repos.
- [Bond](/bond/) — General securities used as repo collateral.
- [Hedge fund](/hedge-fund/) — Major repo users for leverage and short-term funding.
- [Broker](/broker/) — Intermediaries that facilitate and clear repo trades.

</div>
