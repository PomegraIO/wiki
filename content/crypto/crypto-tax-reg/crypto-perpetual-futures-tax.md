---
title: "Tax Treatment of Crypto Perpetual Futures"
description: "Whether perpetual swap funding payments and PnL settlements qualify as Section 1256 contracts or ordinary income under U.S. tax law."
keywords:
  - crypto perpetual futures tax
  - perpetual swap tax treatment
  - section 1256 contracts crypto
  - funding payment tax
  - unrealized pnl settlement tax
image: "/svg/crypto.svg"
---

*The tax treatment of **crypto perpetual futures** remains contested between traders and the IRS, hinging on whether perpetual swaps are *derivatives* (eligible for Section 1256 treatment and 60/40 long-term gains) or cash-settled *forward contracts* taxed as ordinary income. Funding payments and the daily cash settlement of unrealized PnL create a gray zone that the IRS has not formally clarified.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Crypto Perpetual Futures Tax — Key Facts</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for cryptocurrency." />

<div class="wiki-infobox-caption">Unclear IRS treatment of perpetual swaps creates compliance risk for traders.</div>

|   |   |
|---|---|
| **Current IRS stance** | No formal guidance; Section 1256 applicability disputed |
| **Funding payments** | Likely ordinary income, but deductible as investment expenses |
| **Unrealized PnL settle** | Unclear; some argue daily settlement is a realization event |
| **Favorable treatment route** | Section 1256 eligibility (if IRS agrees) = 60% long-term, 40% short-term |
| **Main risk** | IRS audit; conservative position treats perpetuals as ordinary income |
| **Documentation requirement** | Detailed cost basis, entry/exit prices, and funding payment records |

</aside>

## The Core Issue: Section 1256 vs. Ordinary Income

Under U.S. federal tax law, [capital gains](/capital-gains-tax-investor/) are taxed differently depending on asset class and holding period. For a decade, crypto traders have assumed that spot holdings of [Bitcoin](/bitcoin/) and [Ethereum](/ethereum/) are capital assets taxed on realization (when sold). [Options](/option/) and [futures contracts](/futures-contract/) on regulated exchanges, by contrast, are *Section 1256 contracts*—they receive favorable treatment: any position held longer than one day is treated as 60% long-term and 40% short-term, regardless of how long you actually held it.

Perpetual futures (also called perpetual swaps) blur this line. They are:
- Not spot [cryptocurrency](/cryptocurrency-exchange/); you do not own the underlying token
- Not listed on traditional CME or CBOT exchanges; they trade on crypto platforms (Binance, FTX before collapse, Bybit, etc.)
- Traded with leverage; they reset daily via funding payments and cash PnL settlement
- Indefinite in duration (no expiration date)

The IRS has not issued guidance specifically on perpetuals. The best-case scenario for a trader is that the IRS treats them as Section 1256 futures contracts (eligible for 60/40 rates). The worst case is that they are ordinary income, taxed at your full marginal rate.

## Funding Payments and Daily Settlement

Perpetual swaps require **funding payments**—periodic cash flows between long and short traders to keep the perpetual contract price near the spot price. When you are long and funding rates are positive, you pay funding; when funding is negative, you receive it. These payments are typically daily or every eight hours.

Most tax professionals treat funding payments as **ordinary income** (if you receive them) or deductions (if you pay them), because they are not a realization of gain. They flow in and out continuously and depend on market structure, not your position's profitability.

Daily **unrealized PnL settlement** is more complicated. When you hold a long perpetual, your unrealized gain or loss is settled in cash every day (or every funding period). Some traders argue this *daily settlement is a realization event*—you are closing and reopening a position every day, which would trigger daily tax reporting. Others argue the perpetual is a single position held continuously, so settlement is merely accounting, not a taxable event. The IRS has not clarified.

## Conservative vs. Aggressive Positions

**Conservative traders assume ordinary income treatment:**
- Treat the entire perpetual trade (funding payments + realized PnL) as ordinary income
- Report gains/losses on [Schedule D](/schedule-d/) or Form 8949 as a short-term [capital gain](/capital-gains-tax-investor/)
- Claim funding payments and transaction fees as investment expenses (though ordinary income losses offset only ordinary income, not [capital gains](/capital-gains-tax-investor/))
- Maintain meticulous records of daily PnL settlements and funding payments

This approach is defensive and IRS-audit-resistant, but costly if the perpetual would qualify for Section 1256 treatment.

**Aggressive traders claim Section 1256 treatment:**
- Argue that perpetual futures on major platforms are economically identical to CME Bitcoin and Ethereum futures
- Apply 60/40 blended rate (lower tax bill)
- File Form 6781 reporting the position as a Section 1256 contract
- Document why they believe perpetuals meet the statutory definition

The second approach has not been tested in court, and the IRS has shown skepticism of aggressive crypto positions. An audit could result in reclassification, interest, and penalties.

## Practical Tax Planning Implications

**Cost basis tracking is critical.** You must record:
- Entry price and date for each perpetual position
- Daily funding payments received or paid
- Daily unrealized PnL settlement amounts
- Exit price and date (if you close the position)
- Cumulative realized gain or loss

Exchanges like Binance provide transaction history, but they often report funding payments separately from PnL, and they do not align with U.S. tax year calendars (crypto trades 24/7 globally). You must reconcile exchange reports to match your personal tax filing dates.

**Wash-sale rules may not apply.** Under [wash-sale](/wash-sale/) rules, you cannot deduct a loss on a security if you buy a substantially identical security within 30 days before or after the loss. The IRS's stance on whether perpetual Bitcoin is "substantially identical" to spot Bitcoin, Grayscale Bitcoin Trust shares, or CME Bitcoin futures is unclear. Conservative practitioners assume the rules apply; aggressives argue they do not.

**Section 1256 elections and marking-to-market.** If you claim Section 1256 treatment, you are also claiming that any open positions as of December 31 are marked-to-market at year-end, and the gains/losses are deemed realized. You must report this on Form 6781. If the IRS later disagrees that perpetuals are Section 1256 contracts, your entire filing unravels.

## Why the IRS Has Not Clarified

The IRS issued guidance on [Bitcoin](/bitcoin/) and spot crypto (Rev. Ruling 2019-24), treating them as property, not currency. But perpetuals are derivatives, and the IRS's Framework for Crypto Taxation (2023) does not explicitly address perpetual swaps traded on unregulated platforms. The agency is likely waiting to see whether perpetual trading activity scales further or concentrates among a smaller set of institutional players before issuing ruling language.

In the interim, private letter rulings (PLRs) and IRS examination guidance internal documents hint at skepticism. The IRS has audited large crypto traders and seems to reject aggressive Section 1256 claims unless the perpetual is traded on a CFTC-regulated exchange (which most crypto perpetuals are not).

## International Considerations

Non-U.S. traders face different regimes:
- **UK:** Crypto is treated as property or derivative depending on context; perpetuals may fall under [Financial Conduct Authority](/financial-conduct-authority/) rules and be taxed as ordinary income
- **Canada:** Revenue Agency likely treats perpetuals as ordinary income, with daily realization of PnL
- **Australia:** Perpetuals are property; gains are capital, losses depend on profit-making purpose

Traders subject to multiple jurisdictions must reconcile conflicting rules and currencies, making perpetual swap tax reporting extraordinarily complex.

## Recordkeeping Best Practices

- Export all exchange API data (trades, funding, settlements) to a CSV monthly
- Use a crypto tax software (CoinTracker, Koinly, etc.) to generate a preliminary report
- Cross-check the software output against your own spreadsheet
- For Section 1256 reporting, maintain Form 6781 drafts and explain your reasoning
- Keep email correspondence with your tax advisor confirming the treatment chosen
- Retain exchange account statements, bank deposits/withdrawals, and any trading notes for seven years

## See also

<div class="wiki-seealso">

### Closely related

- Section 1256 contracts — Favorable tax treatment for regulated futures and options
- [Capital gains tax (investor)](/capital-gains-tax-investor/) — How gains and losses are taxed
- [Wash-sale rule](/wash-sale/) — Limits on deducting losses on substantially identical securities
- [Crypto perpetual futures tax](/crypto-perpetual-futures-tax/) — Specific treatment of perpetual swaps

### Wider context

- [Bitcoin](/bitcoin/) — Digital currency and property classification
- [Ethereum](/ethereum/) — Smart contract platform and tax treatment
- [Cryptocurrency exchange](/cryptocurrency-exchange/) — Trading infrastructure for crypto
- [Derivatives hedging](/derivatives-hedging/) — Using derivatives to manage risk
- [Form 8949](/form-8949/) — Capital gains and losses reporting form

</div>
