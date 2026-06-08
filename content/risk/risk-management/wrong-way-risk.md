---
title: "Wrong-Way Risk"
description: "When counterparty credit quality deteriorates precisely as your exposure to that counterparty rises, amplifying loss."
keywords:
  - counterparty risk
  - credit correlation
  - derivatives exposure
  - credit contagion
  - correlation risk
  - systemic risk
image: /svg/risk.svg
---

*A trader holds a [derivative](/option/) [contract](/expiration-date/) with a counterparty—say, a five-year interest rate [swap](/option/). If rates fall, the contract becomes an asset worth millions. But if the counterparty is a bank that also benefits from falling rates, the bank may be in crisis precisely when it owes you the most. This is **wrong-way risk**: when the market move that makes your contract valuable is the same move that weakens your counterparty's ability to pay.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Wrong-Way Risk — key facts</div>

<img src="/svg/risk.svg" alt="An abstract editorial mark for risk management topics." />

<div class="wiki-infobox-caption">The perverse correlation between gain and counterparty failure.</div>

|   |   |
|---|---|
| **What it is** | Exposure to a counterparty rises when that counterparty's credit quality falls |
| **Most common in** | Interest rate swaps, FX forwards, commodity derivatives, and structured products |
| **Key risk** | You become most exposed to default when you most need to collect |
| **Correlation source** | Market moves that enrich you impoverish your counterparty, or expose both to the same shock |
| **Mitigation** | Collateral agreements, central clearing, netting, and avoiding levered counterparties |

</aside>

## The AIG lesson: synthetic exposure creates contagion

The clearest historical example is AIG. In the 2007–2008 financial crisis, many large banks had sold protection on mortgage bonds via credit default swaps (a type of [derivative](/option/)). AIG was the counterparty on the other side, effectively short mortgage credit. As housing collapsed, AIG's exposure ballooned—banks owed billions if the mortgage bonds defaulted. But the same housing collapse that made those contracts valuable to the banks was ruining AIG's balance sheet. AIG was running out of collateral to post and unable to refinance. The U.S. government was forced to bail out AIG with $180 billion to prevent a cascade of counterparty failures across the financial system.

This is wrong-way risk in its most dangerous form: the banks had hedged their mortgage risk by selling protection to AIG, but the hedge failed precisely when they needed it most. The exposure and the counterparty weakness were perfectly, perversely correlated.

## Why derivatives are vulnerable

Derivatives are often wrong-way by design. A [swap](/option/) is a bet: the winner gains when a market move happens; the loser is exposed when it doesn't. If both parties are levered or both operate in the same sector, the loser may face a credit squeeze just as the winner goes deep in the money.

A classic example: a large hedge fund is short equity volatility, selling [straddles](/put-option/) on major indices to a dealer. If the stock market crashes, [volatility](/historical-volatility/) soars, and the hedge fund owes tens of millions to the dealer. But the crash has also wiped out the hedge fund's capital, dried up its funding, and destroyed its credit rating. The dealer, now an unsecured creditor, will recover only cents on the dollar—if the fund collapses before unwinding the position.

## The leverage amplifier

Leverage makes wrong-way risk worse. A pension fund borrowing 2:1 to own corporate bonds is vulnerable to the fund's lender raising rates. But a [dealer](/option/) using 10:1 or 20:1 leverage on a leveraged portfolio is a prisoner of its own borrowing: if the assets it is levered into fall sharply, the dealer's counterparties (its own lenders and [swap](/option/) partners) suddenly fear default. Everyone tightens at once.

During the 2020 COVID crash, dealers faced calls from their own lenders to post more collateral (because mark-to-market values were falling) even as counterparties on the other side of their derivatives books were failing to pay. The mismatch between when dealers could borrow and when they could collect created acute funding stress.

## Identifying wrong-way exposure

A risk manager must ask: "If I become heavily exposed to this counterparty via this derivative, will the counterparty be stronger or weaker?" Some examples:

- **Interest rate swap**: You pay fixed to a bank and receive floating. If rates rise, the swap becomes valuable to you. But a rising-rate environment typically weakens a bank (existing bond holdings fall in value, mortgage prepayments drop). This is mildly wrong-way.
- **Credit [put](/put-option/)**: You own a five-year [put](/put-option/) on a company's bonds, paying a spreads seller for protection. If credit spreads widen (bonds fall), your put is in the money. But the spreads seller, levered on credit, is now facing margin calls or insolvency. Wrong-way.
- **FX [swap](/option/)**: A developing-country central bank borrows dollars via a [swap](/option/) from a major bank. If the local currency collapses (making the swap expensive to unwind), the developing-country bank's credit is likely impaired. Wrong-way.

## Mitigation: collateral and central clearing

The financial system has built tools to reduce wrong-way risk:

- **Collateral agreements**: A bank holding derivatives against a counterparty agrees that the counterparty posts cash or securities daily as mark-to-market values change. If the counterparty's credit begins to crack, the bank has already received collateral that it can liquidate. This converts unsecured wrong-way exposure into secured exposure.
- **Central clearing**: Instead of bilateral swaps, both parties clear through a central counterparty (CCP). The CCP is typically much safer than individual counterparties, and the CCP uses collateral extensively. This is why regulators now mandate clearing for many derivatives.
- **Netting**: Offsetting exposure with the same counterparty reduces gross risk, though it doesn't eliminate wrong-way correlation.

However, collateral and clearing are not costless. They require that counterparties have access to cash and liquid collateral—precisely what they lack in a crisis. The 2008 crisis proved that no mitigation is perfect.

## Systemic wrong-way risk

On the broadest scale, entire financial systems can face wrong-way risk. If all major banks are levered on the same assets and all have borrowed short-term from the same lenders, a shock (rising rates, credit event) that makes their [derivatives](/option/) liabilities balloon will also trigger lender withdrawals. [Funding liquidity risk](/funding-liquidity-risk/) becomes systemic [counterparty risk](/counterparty-risk/). This is how a localized crisis becomes a cascade.

A banker must thus distinguish between idiosyncratic wrong-way risk (this one counterparty is levered on commodities, and I'm short commodities) and systemic risk (everyone is levered on the same pool of assets, and that asset class is under stress). The former is manageable via diversification; the latter is not.

## See also

<div class="wiki-seealso">

### Closely related

- [Counterparty Risk](/counterparty-risk/) — the general risk that a counterparty cannot pay
- [Funding Liquidity Risk](/funding-liquidity-risk/) — when funding dries up, amplifying counterparty fear
- [Dynamic Hedging](/dynamic-hedging/) — a hedge that may fail if the counterparty itself fails
- [Gamma Risk](/gamma-risk/) — another form of correlation risk in derivatives
- [Systemic Risk](/systemic-risk/) — when one failure triggers a cascade
- [Credit Risk](/credit-risk/) — the broader category covering counterparty failure
- Derivatives Risk — the full landscape of risks in swaps and options

### Wider context

- [Swap](/option/) — the most common source of wrong-way exposure
- [Options](/option/) — another source, especially credit derivatives
- [Hedge Fund](/hedge-fund/) — institutions often on both sides of wrong-way bets
- [Leverage Ratio](/leverage-ratio-forex/) — how leverage amplifies wrong-way pain

</div>
