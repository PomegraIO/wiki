---
title: "Margin Period of Risk"
description: "The regulatory window that defines how long a CCP has to close out a defaulted member's positions, determining initial margin buffer size."
keywords:
  - margin period of risk
  - mpor
  - central clearing
  - counterparty risk
  - initial margin
image: "/svg/institutions.svg"
---

*The **margin period of risk** (MPOR) is the regulatory close-out window that a central clearinghouse uses to calculate how much [initial margin](/initial-margin/) a clearing member must post. It represents the calendar days and trading time assumed necessary for the clearinghouse to liquidate or hedge a defaulted member's positions without undue loss. The longer the assumed close-out window, the larger the margin buffer must be.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">MPOR — key facts</div>

<img src="/svg/institutions.svg" alt="An abstract editorial mark for institutions." />

<div class="wiki-infobox-caption">The regulatory close-out window that calibrates a CCP's margin demand.</div>

|   |   |
|---|---|
| **What it is** | The assumed number of days to liquidate a defaulted member's portfolio |
| **Also called** | Liquidation period, close-out window |
| **Set by** | Regulators and the central clearinghouse itself |
| **Typical range** | 1 to 5+ days, depending on asset class and liquidity |
| **Purpose** | Ensures initial margin covers potential price moves during forced liquidation |
| **Impact on margin** | Longer MPOR → larger margin requirement |

</aside>

## Why clearinghouses need a close-out assumption

When a clearing member defaults, the [central counterparty](/central-counterparty-clearing/) must immediately offload or hedge the member's open positions. This liquidation does not happen in an instant. On an illiquid morning after a large default, the exchange may face slippage, incomplete fills, or the need to hold positions open across multiple trading sessions. The MPOR formalises this reality by assuming a worst-case close-out timeline.

The [initial margin](/initial-margin/) collected from all members is calibrated to cover price movements that could occur over that close-out window. If a member posts enough margin to cover two days of volatility, but the clearinghouse needs five days to liquidate the portfolio, a shortfall is possible. Setting MPOR too short invites underfunding; setting it too long imposes an uneconomical capital cost on clearing members.

## MPOR varies by asset class and liquidity

Not all assets can be unwound at the same speed. A large block of [Treasury bonds](/treasury-bond/) can usually be sold within one trading day. A concentrated position in a small-cap stock or an exotic derivative might require days to move without triggering market dislocations. Clearinghouses typically differentiate MPOR by asset class, product, and even by market condition.

For highly liquid assets traded on major [stock exchanges](/stock-exchange/), an MPOR of one day is standard. For less liquid instruments—corporate bonds, FX forwards, or illiquid equities—the CCP may assume two to five days. Some clearinghouses apply a longer MPOR during market stress, when liquidity evaporates. Others adjust MPOR dynamically based on recent bid-ask spreads and trading volumes.

## Regulatory requirements and validation

Banking regulators and securities authorities require that clearinghouses justify their MPOR with empirical evidence. Under frameworks such as the [Dodd-Frank Act](/dodd-frank-act/), CCPs must regularly backtest their close-out assumptions using historical data on price volatility, market depth, and transaction sizes. If liquidations routinely occur faster than assumed, the MPOR can be shortened. If actual close-out times exceed the assumed window, the margin buffer is found to be inadequate, and the MPOR must extend.

A clearinghouse defending its MPOR must produce stress test scenarios: What if a very large member defaults during a market shock? Can positions be closed out in the assumed window, or does volatility spike so severely that close-outs bleed into an extra day? These exercises inform both the MPOR itself and the calibration of [initial margin](/initial-margin/) to cover the range of possible price moves.

## MPOR and member costs

For clearing members, MPOR is a hidden but substantial cost driver. A longer MPOR inflates the required margin deposit, which ties up capital and reduces the member's ability to leverage positions. In competitive clearing markets, a CCP perceived as using an overly conservative MPOR may lose member business to rivals with lower margin requirements. Conversely, a CCP that cuts MPOR too aggressively faces regulatory scrutiny and potential loss of confidence.

Members and their regulators closely monitor MPOR changes. A sudden jump in MPOR—perhaps triggered by a liquidity crisis or a large default elsewhere in the financial system—can force members to post additional margin immediately, tightening their balance sheets. Some clearing agreements allow MPOR to rise or fall within a band, cushioning minor changes but still signalling stress when the band widens.

## The practical reality: stress and uncertainty

In theory, MPOR is a static number set conservatively and then validated quarterly. In practice, the margin period of risk embodies an uncomfortable truth: no one knows exactly how long a large, complex portfolio would take to liquidate under severe market stress. A default that unfolds during a [liquidity crisis](/liquidity-risk/) or a sharp market move could easily exceed the assumed close-out window. For this reason, responsible clearinghouses maintain [initial margin](/initial-margin/) buffers well above the minimum required by MPOR alone, and they monitor their largest members' positions continuously to catch concentration risk before a default scenario arrives.

## See also

<div class="wiki-seealso">

### Closely related

- [Initial Margin](/initial-margin/) — the cash or collateral members post to cover price moves during MPOR
- [Central Counterparty Clearing](/central-counterparty-clearing/) — the CCP that manages member defaults
- [Client Clearing](/client-clearing/) — how end-users access CCP services indirectly
- [Portability of Client Positions](/portability-client-positions/) — transferring a defaulted member's trades to a surviving firm
- [CCP Recovery and Resolution](/ccp-recovery-resolution/) — tools for a failing CCP beyond orderly liquidation

### Wider context

- [Counterparty Risk](/counterparty-risk/) — why clearinghouses exist
- [Dodd-Frank Act](/dodd-frank-act/) — US regulatory framework for clearing
- [Concentration Risk](/concentration-risk/) — large bets by single members
- [Stress Testing](/stress-testing/) — validating margin models under extreme scenarios

</div>
