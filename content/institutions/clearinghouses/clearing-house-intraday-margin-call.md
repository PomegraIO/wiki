---
title: "Intraday Margin Calls at Clearinghouses"
description: "How central clearinghouses issue same-day variation margin calls when markets spike, and what triggers and payment expectations follow."
keywords:
  - intraday margin call clearinghouse
  - variation margin clearinghouse
  - central counterparty margin
  - same-day margin requirement
  - clearing house margin mechanics
image: /svg/institutions.svg
---

*During sharp market moves, central clearinghouses issue **intraday margin calls** to their member firms throughout the trading day—not just at the close. These variation margin demands must be met within hours, not days, forcing firms to maintain liquidity buffers and credit lines specifically to handle mid-session shocks.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Intraday Margin Calls — key facts</div>

<img src="/svg/institutions.svg" alt="An abstract editorial mark for institutions and infrastructure." />

<div class="wiki-infobox-caption">Real-time capital demands that protect a clearinghouse from member default during volatile sessions.</div>

|   |   |
|---|---|
| **Trigger** | Cumulative daily loss on member's position exceeds threshold; typically checked hourly or continuously |
| **Timing** | Multiple calls throughout the day; not overnight |
| **Payment window** | Usually 1–4 hours, depending on clearinghouse; intraday, same business day |
| **What covers it** | Cash, bank guarantee, or pre-positioned credit line |
| **If unpaid** | Member defaulted; clearinghouse liquidates positions and seizes collateral |
| **Typical amounts** | Can be millions per call, depending on position size and price moves |
| **Related mechanism** | [Repurchase agreement](/repurchase-agreement/); [counterparty risk](/counterparty-risk/) |

</aside>

## Why clearinghouses collect intraday, not just at the close

A central counterparty (CCP) stands between buyers and sellers, becoming the counterparty to every trade. When market prices move sharply, some members' positions slip into heavy losses. If a member defaults mid-session without posting additional collateral, the CCP is exposed to massive loss and may become insolvent.

Before the 2008 financial crisis and the rise of post-crisis regulations, clearinghouses collected margin once per day, after the close. In a crisis with overnight gaps, that daily interval was too long. The CCP could suffer a default between the close and the next morning, eating losses from the overnight move.

Today, the major clearinghouses (CME Clearing, LCH.Clearnet, Eurex Clearing, DTCC, etc.) monitor member positions continuously or at frequent intervals—often hourly, sometimes every 15 minutes—during the trading day. If a member's cumulative loss crosses a **variation margin** threshold, the clearinghouse issues a call immediately and expects payment the same day.

This real-time monitoring is a key pillar of financial stability. It prevents large losses from accumulating invisibly and then shocking the system at the next settlement window.

## Mechanics of an intraday margin call

Here is how a call typically unfolds:

1. **Position monitoring** — The clearinghouse's risk engine tracks mark-to-market losses on all members' positions in real time.

2. **Threshold breach** — When cumulative losses exceed the daily variation margin requirement, the clearinghouse's system generates a call. For a large derivatives trader, this might happen several times during a volatile morning.

3. **Notification** — The clearinghouse sends the call to the member's treasury and operations teams, specifying the amount due and the payment deadline. A typical deadline is within 1–4 hours.

4. **Settlement** — The member must wire the funds, credit the clearinghouse with pre-positioned collateral, or draw on a pre-arranged bank credit line. Payment is processed through designated settlement banks.

5. **Position management** — If the member does not pay by the deadline, the clearinghouse's default procedures kick in. It forcibly closes the member's positions (at market prices, which may be worse than recent levels) and seizes collateral.

The speed is intentional. A member cannot claim "the wire is slow" or "my bank is closed." The expectation is that a professional derivatives trader maintains enough liquidity to cover several intraday margin calls simultaneously.

## Why size and volatility drive multiple calls

During volatile markets, a single member can receive multiple margin calls in one trading session. Consider a large oil trader holding a long position in crude futures:

- 9:00 a.m.: Oil prices slide $2/barrel on supply news. The trader's 10,000-contract position is down ~$20 million. Margin call issued: $10 million due by 11 a.m.
- 10:15 a.m.: Oil continues falling another $1. The cumulative loss grows. Second margin call: $8 million due by 12:30 p.m.
- 11:45 a.m.: Prices stabilize and bounce slightly, but not enough. Third margin call: $5 million due by 1:30 p.m.

By noon, the trader has been asked to deposit $23 million across three calls—all on the same morning. This is not hypothetical; it happened regularly during the March 2020 volatility spike, when oil crashed and wheat prices spiked, generating record margin calls.

Firms caught unprepared had to liquidate positions to raise cash, sometimes at terrible prices, because they did not have sufficient liquid buffers. Those that did—with pre-arranged lines and large cash reserves—paid the calls and held their positions.

## The role of collateral and credit lines

To manage intraday margin risk, large derivatives traders maintain three layers of liquidity:

1. **Cash on deposit** at the clearinghouse. Amounts vary but often run into the hundreds of millions for major firms.

2. **Credit lines** from banks, specifically earmarked for margin calls. A Goldman Sachs or JPMorgan might have $5–10 billion in committed margin credit lines across all clearinghouses.

3. **Collateral pools** of government bonds, money market instruments, or other highly liquid assets that can be pledged rapidly if a call exceeds cash on hand.

The cost of maintaining these buffers is real—banks charge fees for committed credit lines, and holding cash is a drag on returns. But the alternative—being caught short on margin and forced to liquidate—is far more expensive.

Smaller firms and newer members sometimes underestimate the scale of intraday calls. During a stress event, a firm might have enough cumulative margin to cover the day-end settlement but not enough cash or credit to cover 4–5 intraday calls stacked within a few hours. This liquidity mismatch is a chronic source of stress in volatile periods.

## When intraday calls become crisis signals

Intraday margin calls are a normal part of clearinghouse risk management, but their magnitude and frequency are also a barometer of systemic stress.

During the March 2020 COVID crash, clearinghouses issued unprecedented intraday calls—CME Clearing's calls routinely reached $100+ million per member for major traders. The calls were so large and frequent that some firms breached their credit lines and had to negotiate emergency increases with their banks.

In September 2022, when the UK gilt market seized up, LCH.Clearnet's variation margin calls spiked to extremes, forcing the Bank of England to intervene with emergency funding to prevent member defaults and a broader financial contagion.

These episodes illustrate that intraday margin calls are not just mechanical. During crisis scenarios, they can become a liquidity cascade: calls spike, firms scramble to raise cash, that scramble itself pushes prices further, which triggers larger calls. A clearinghouse managing this must sometimes ease margin requirements temporarily (to prevent defaults that would spread) while the underlying market finds a bottom.

## How members anticipate and prepare for calls

Sophisticated traders use historical volatility and [value at risk](/value-at-risk/) (VaR) models to forecast potential intraday margin calls under stressed scenarios. A trader holding a large position might run a simulation: *If oil drops $5 in one session, what is my expected cumulative margin call?* They then maintain sufficient buffers to cover a multiple of that worst case.

Some firms also time their position entry and exit to avoid peak volatility windows. A trader who knows the FOMC announcement is at 2 p.m. might reduce size ahead of the meeting, knowing that a surprise outcome could trigger large intraday calls in the 2:01–3:00 p.m. window.

Trading desks also communicate with their treasury teams on market-open mornings when volatility is elevated. "We're holding 50,000 contracts into a G7 announcement. We might see a $50M call. Let's make sure the credit line is active."

## The settlement bank role

Clearinghouses do not process margin calls directly with cash; they use settlement banks. A member firm sends funds to its settlement bank, which then credits the clearinghouse's account at a different settlement bank. This adds a layer of indirection but also ensures that clearinghouse operations are not disrupted by bank processing delays.

During crisis episodes, settlement banks themselves can become a bottleneck. If volatility is so high that dozens of members are making intraday margin payments simultaneously, some settlement banks' systems can slow. This is rare but has happened—in March 2020, some clearing members complained of delays in margin payment processing, even though the underlying banking system was functioning.

## See also

<div class="wiki-seealso">

### Closely related

- Clearing house — the institution that issues intraday margin calls and manages counterparty risk
- [Counterparty risk](/counterparty-risk/) — the risk that a trading partner defaults, which intraday calls help mitigate
- [Variation margin](/margin-call-forex/) — daily losses that must be collateralized; contrast with initial margin
- [Repurchase agreement](/repurchase-agreement/) — short-term funding mechanism often collateralized with government bonds

### Wider context

- [Central bank](/central-bank/) — lender of last resort that may step in during clearing system stress
- [Systemic risk](/systemic-risk/) — how clearing house failures can cascade through the financial system
- [Futures contract](/futures-contract/) — the derivatives that require margin and are cleared through clearinghouses
- [Stress testing](/stress-testing/) — how banks and traders simulate intraday margin demands under extreme scenarios

</div>
