---
title: "How a Clearinghouse Margin Call Works"
description: "Understand how clearinghouse margin calls work: initial margin requirements, variation margin daily settlement, and consequences of member default."
keywords:
  - clearinghouse margin call
  - variation margin
  - initial margin
  - central counterparty
  - futures settlement
  - counterparty risk
---

*A **clearinghouse margin call** enforces two safety buffers: initial margin (upfront collateral posted before trading) and variation margin (daily cash settlement of mark-to-market losses). When a futures or derivatives position moves against a member, the clearinghouse demands variation margin by the next day; if the member cannot pay, the clearinghouse liquidates the position and may seize other collateral to cover losses.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Clearinghouse Margin Call — key facts</div>

<img src="/svg/institutions.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Central counterparties use margin calls to manage default risk in real time.</div>

|   |   |
|---|---|
| **Initial margin** | Posted upfront; protects against gap risk during liquidation |
| **Variation margin** | Settled daily (or intraday); equalizes mark-to-market P&L |
| **Margin call timeline** | Typically issued next business day after loss; payment due same or next day |
| **Member failure** | Clearinghouse liquidates position, uses collateral, may auction contracts |
| **Intraday monitoring** | Some clearinghouses (CME, Eurex) monitor and call during the trading day |

</aside>

## Why Clearinghouses Collect Margin

A derivatives clearinghouse stands as the central counterparty between every buyer and seller. Instead of worrying about whether Party A will pay Party B when a contract settles, both parties know the clearinghouse will perform. The clearinghouse's survival depends on never suffering a loss—it must eliminate the possibility that a member defaults and cannot cover losses.

Margin serves this goal. It is collateral that absorbs losses before the clearinghouse's own capital is at risk. There are two types: initial margin and variation margin.

## Initial Margin

**Initial margin** is posted before the trade and remains in the clearinghouse's custody throughout the contract's life. It acts as a shock absorber for the most severe adverse moves the clearinghouse expects a position to face during liquidation.

The amount is calculated using risk models (typically VaR-based) that account for the contract's volatility and the time it would take to liquidate the position. For highly liquid contracts like E-mini S&P 500 futures, initial margin might be 5–10% of notional value. For less liquid contracts or during stress periods, it can be 20% or higher.

**Example:** A trader buys a single crude oil futures contract (1,000 barrels). The notional value is $60,000 (at $60/barrel). The clearinghouse requires $3,000 in initial margin. This amount sits in the clearinghouse's account; the trader has funded it but no longer controls it.

## Variation Margin and Daily Settlement

At the end of each trading day, the clearinghouse marks every open position to the closing price (mark-to-market). The profit or loss since the previous mark is calculated, and the member's margin account is credited or debited accordingly.

**Variation margin** is the daily cash settlement of that P&L. If the trader's position has lost $500, the clearinghouse sends a variation margin call for $500 the next morning. The member must pay by a deadline (typically the same day or early the following day, depending on the clearinghouse).

If the position has gained $500, the member receives the cash credit.

### Intraday Margin Calls

Most U.S. futures clearinghouses (CME Clearing, ICE Clear U.S.) now monitor positions intraday. If a member's losses accelerate and threaten to breach initial margin, the clearinghouse may issue a call during the trading day—not waiting until the close. This is a powerful tool during market dislocations when gap risk is highest.

## The Member Cannot Pay: What Happens

When a member cannot or will not post variation margin, the clearinghouse assumes full control of the position. The timeline is:

**Day 1 (T):** Clearinghouse discovers shortfall and sends demand; member has a few hours (often until the end of the day) to pay.

**Day 1–2 (T to T+1):** If member does not pay, the clearinghouse declares it in default and immediately liquidates its positions. For futures and exchange-traded derivatives, this means flattening all open contracts in the market—selling longs, buying shorts.

**Liquidation losses:** If the clearinghouse must sell a large long position into a falling market, it may realize a loss. That loss is absorbed first by the defaulting member's initial margin. If losses exceed initial margin, the clearinghouse dips into its own guarantee fund (funded by fees and contributions from all members).

**Auction or mutualization:** If the default is large, the clearinghouse may auction the member's remaining contracts to other members at a discount, or spread the loss across all surviving members (mutualization).

## Collateral Management and Rehypothecation

Members typically post initial margin in the form of cash, Treasury securities, or other high-quality collateral. The clearinghouse does not earn yield on this collateral; instead, it holds it as a buffer.

Some clearinghouses rehypothecate (reuse) margin collateral—borrowing against it to fund operations or lend to other members for short-term liquidity. This introduces its own risk: if collateral value falls (e.g., Treasuries drop in value during a rate shock), the clearinghouse may face a shortfall. Most modern clearinghouses have tightened rehypothecation to reduce this tail risk.

## Stress and Higher Margin

Margin levels are not static. During periods of heightened volatility or [credit-event-sovereign](/credit-event-sovereign/) stress, clearinghouses raise initial margin requirements. When the implied volatility of equity index futures spiked in March 2020, the CME increased S&P 500 margin by 25–50% in a matter of days. This forces members to post additional collateral, which can trigger a liquidity crunch if they have tied up capital elsewhere.

Similarly, after a member default or a significant market event, clearinghouses may raise margin across the board to rebuild the safety buffer.

## The 2008 Crisis and Lehman: A Case Study

When Lehman Brothers defaulted in September 2008, it had large derivative positions at multiple clearinghouses. The CME and LCH had to liquidate thousands of contracts within hours. The clearinghouse's initial margin buffer on Lehman's positions was sufficient to cover the losses in most cases, though liquidation at distressed prices was costly and market-moving.

Lehman's default illustrated both the system's resilience (no clearinghouse failed despite a major bank collapsing) and the tightness of margins in extreme stress. Today, clearinghouses hold significantly more capital and use more sophisticated risk models, partly in response to those lessons.

## See also

<div class="wiki-seealso">

### Closely related

- Central Counterparty — The clearinghouse institution and its role in derivative settlement
- [Futures Contract](/futures-contract/) — The standardized instruments cleared and margined by clearinghouses
- [Counterparty Risk](/counterparty-risk/) — The credit risk that margin is designed to mitigate
- [Initial Public Offering](/initial-public-offering/) — Unrelated to initial margin; see [Derivatives Hedging](/derivatives-hedging/) for context on derivative instruments
- [Margin Call Forex](/margin-call-forex/) — How margin calls work in currency trading, a related but distinct mechanism

### Wider context

- [Credit Risk](/credit-risk/) — The fundamental risk margin is designed to control
- [Systemic Risk](/systemic-risk/) — Why clearinghouse operations matter to financial stability
- [Stress Testing](/stress-testing/) — How clearinghouses validate margin adequacy
- [Securitization](/securitization/) — Another institution-level mechanism for managing credit exposure

</div>
