---
title: "Eligible Collateral at a Clearinghouse: What Assets Qualify as Margin"
description: "Eligible collateral types at CCPs range from cash and treasuries to equities and gold; haircuts reduce their value as initial margin."
keywords:
  - eligible collateral clearinghouse types
  - clearinghouse margin requirements
  - collateral haircuts
  - initial margin assets
  - ccp collateral
  - margin acceptance
---

*Central counterparty clearinghouses accept a diverse set of assets as **eligible collateral** to back initial margin and protect against default, but each asset class carries a different **haircut**—a percentage discount that reduces its posted value to account for liquidity and price risk.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Eligible Collateral at CCPs — Key Facts</div>

<img src="/svg/institutions.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Major clearinghouses publish eligibility lists and haircuts daily; acceptance and haircuts vary by economic cycle and volatility.</div>

|   |   |
|---|---|
| **Primary collateral** | Cash, government bonds, equities |
| **Secondary collateral** | Corporate bonds, gold, international securities |
| **Typical cash haircut** | 0% (baseline) |
| **Typical equity haircut** | 5–15% |
| **Typical bond haircut** | 1–5% for sovereigns; 2–10% for corporates |
| **Gold haircut** | 5–7% |
| **Review frequency** | Daily to intraday, adjusted for volatility |

</aside>

## Cash and Cash Equivalents

Cash in the currencies the clearinghouse operates—US dollars at a US CCP, euros at EUREX—is the safest collateral and carries a 0% haircut. U.S. Treasury bills are also accepted with minimal haircut (typically 0–0.5%) because they are liquid and backed by the full faith of the U.S. government.

Eligible currencies vary by clearing house and the contracts cleared. The [Federal Reserve](/federal-reserve/), EUREX, and other operators accept only specific currencies. Posting cash in a non-eligible or non-base currency triggers a haircut of 1–3% to account for foreign exchange conversion risk.

## Government Bonds and Treasury Securities

Government securities of major OECD nations—U.S. Treasuries, German Bunds, U.K. Gilts, Japanese Government Bonds—are accepted as initial margin collateral at most CCPs. Haircuts depend on maturity and issuer credit rating.

A 2-year U.S. Treasury might carry a 0.5–1% haircut; a 10-year Treasury 1–2%; a 30-year 2–4%. Longer maturity means greater interest-rate sensitivity and volatility, hence higher haircut. Government bonds outside the G7 (e.g., Canadian, Australian sovereigns) are accepted but with slightly higher haircuts (1–3%).

If the issuer's credit rating falls or sovereign default risk rises during a crisis, the CCP may widen haircuts or delist the bond from eligible collateral. During the 2020 COVID crisis, many CCPs widened government bond haircuts temporarily to account for temporary rate volatility.

## Equities and Stock Positions

Equities from major indices—S&P 500 components, EURO STOXX 50 stocks, FTSE 100 names—are accepted as collateral at equity and multi-asset CCPs. Haircuts typically range from 5–15% depending on liquidity and volatility.

Large-cap, highly liquid stocks (Apple, Microsoft, ExxonMobil) might carry a 5–8% haircut. Mid-cap or more volatile stocks face 10–15% haircuts. Stocks outside major indices are often not eligible or face 20%+ haircuts. The CCP reviews haircuts daily and tightens them if the stock's volatility spikes or if market-wide equity risk rises sharply.

Dividend payments on posted equity collateral sometimes accrue to the posting party (beneficial owner), but this varies by CCP and the specific transaction. During periods of high equity volatility (e.g., March 2020), haircuts widened from 8% to 12–15%, reflecting higher margin calls for equity holders.

## Corporate Bonds and Credit Securities

Investment-grade corporate bonds—those rated BBB− or higher by major rating agencies—are accepted at most CCPs, but at higher haircuts than government securities. A AAA-rated corporate bond might carry a 2–3% haircut; a BBB-rated bond 5–10%.

High-yield or "junk" bonds (rated below BBB−) are typically ineligible at major CCPs, though some specialized CCPs or bilateral margin agreements do accept them with steep haircuts (15–30%) if at all. During credit stress, CCPs may downgrade or delist corporate bonds from eligibility if their rating falls.

## Gold and Precious Metals

Gold bullion is widely accepted as collateral at global CCPs, with haircuts of 5–7%. The metal's acceptance reflects its universal value storage and low credit risk—gold prices fluctuate with real interest rates and geopolitical tension, not the creditworthiness of an issuer.

Silver, platinum, and other precious metals are less universally accepted. Some CCPs list them as eligible; others do not. When accepted, haircuts are typically 8–12%, slightly higher than gold because they are less liquid and less globally traded.

## International and Non-Base Currency Securities

Securities denominated in non-base currencies (e.g., euro-denominated securities posted at a U.S. CCP, or yen bonds posted in dollars) face an additional haircut to cover foreign exchange volatility, typically 2–5% on top of the asset-class haircut.

Emerging-market government bonds are accepted at some CCPs but rarely as freely as OECD sovereign debt. Haircuts range from 5–20% depending on the country's credit rating and the bond's maturity. CCPs often require such bonds to be from a whitelist of eligible issuers, and haircuts may widen sharply if the issuer's risk rises.

## How Haircuts Are Set and Adjusted

CCPs publish detailed haircut schedules daily. The schedule lists each eligible asset (usually by ISIN or ticker), its haircut percentage, and any eligibility restrictions (e.g., minimum credit rating, maturity range).

Haircuts are calibrated to cover the expected loss if the clearinghouse must liquidate the collateral in a stressed scenario. A 10% haircut on an equity reflects an assumption that, in a liquidity crisis, the CCP might recover 90% of the security's market value after bid-ask spreads, fire-sale discounts, and settlement delays.

During volatile periods, CCPs raise haircuts. In March 2020, some CCPs raised equity haircuts from 8% to 15% as the market plunged and liquidity tightened. As volatility subsides and liquidity recovers, haircuts are lowered. This dynamic adjustment can amplify margin calls during stress—holders of equity collateral suddenly face larger margin requirements when haircuts widen, forcing additional cash deposits.

## Concentration Limits

Many CCPs also impose limits on how much of a single asset a clearing member can post. For example, a member might be allowed to post no more than 20% of required margin in a single stock, or 30% in equities overall. These [concentration-risk](/concentration-risk/) limits prevent members from posting illiquid or correlated collateral, which would leave the CCP exposed if multiple defaults occurred simultaneously.

## See also

<div class="wiki-seealso">

### Closely related

- [Counterparty Risk](/counterparty-risk/) — The default risk CCPs manage through collateral
- [Initial Margin](/initial-margin/) — The deposit amount that eligible collateral covers
- [Repurchase Agreement](/repurchase-agreement/) — Bilateral repo collateral terms, which informed CCP standards
- [Risk-Weighted Assets](/risk-weighted-assets/) — Similar haircut logic applied by banks to their own portfolios
- [Basis Risk](/basis-risk/) — When hedging instruments don't perfectly offset underlying exposure

### Wider context

- Central Counterparty — How CCPs use collateral to manage systemic risk
- [Derivatives Hedging](/derivatives-hedging/) — Why collateral is posted on derivative positions
- [Securities and Exchange Commission](/securities-and-exchange-commission/) — U.S. regulator of CCP rules and standards
- [Credit Risk](/credit-risk/) — Core risk that clearinghouse collateral covers

</div>
