---
title: "How a Clearing House Issues a Margin Call"
description: "Trace the intraday process by which a central counterparty (CCP) detects exposure breaches and demands margin from clearing members."
keywords:
  - clearing house margin call
  - margin call process
  - initial margin
  - variation margin
  - central counterparty
  - clearing member margin
  - intraday risk monitoring
---

*A clearing house (also called a central counterparty, or CCP) monitors the financial health of its members throughout the trading day. When a member's unrealized losses exceed its posted margin, the clearing house issues a **margin call**—a demand for additional cash or collateral. Understanding this process is essential to knowing how clearing houses contain counterparty risk between trade and settlement.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Margin Call Mechanics — key facts</div>

<img src="/svg/trading.svg" alt="An abstract editorial mark for trading infrastructure." />

<div class="wiki-infobox-caption">Clearing houses police member solvency in real-time, calling margin before losses spiral.</div>

|   |   |
|---|---|
| **Who triggers it** | The clearing house risk team, via automated systems |
| **When it happens** | Intraday, often multiple times; before T+1 settlement |
| **Initial margin** | Upfront collateral posted before trading; covers potential 1–5 day loss |
| **Variation margin** | Daily settlement of gains/losses; called when unrealized loss exceeds thresholds |
| **Haircut** | Discount applied to collateral value; 5–20% depending on asset type |
| **Grace period** | Usually 1–4 hours to post funds; varies by exchange |
| **Consequences of non-payment** | Member account frozen, positions force-liquidated, potential default auction |
| **Technology** | Real-time position and risk calculation; automated call generation |

</aside>

## The Two Types of Margin: Initial and Variation

Before a clearing member can trade, it must post **initial margin**—cash or liquid securities held by the clearing house as a buffer. The amount depends on the member's portfolio: its size, concentration, and estimated volatility. A member trading 10 small positions posts less initial margin than one trading 1,000 contracts of a volatile futures index.

Initial margin is meant to cover potential losses over the clearing house's "close-out window"—typically 1 to 5 business days, depending on the product and market. If a member defaults, the clearing house has that window to liquidate the member's positions without massive losses. Initial margin must be enough to absorb those potential close-out losses.

**Variation margin** is different. It is the daily (or intraday) profit-and-loss settlement. At the end of each day, every trade is marked-to-market at the closing price. If a member is long a futures contract and the price rose, the member has made a gain; the clearing house credits its account. If the price fell, the member has an unrealized loss; the clearing house debits its account.

When variation margin is debited faster than gains are credited, the member's margin balance shrinks. If the balance approaches or falls below a threshold—often zero or a small positive buffer—the clearing house issues a variation margin call.

## How a Clearing House Detects Exposure

Clearing houses use real-time position and risk systems. All-day long, as trades are executed and reported, the clearing house's computers update each member's:

- **Net position** in each security or contract (long 1,000 shares minus short 500 shares = net long 500).
- **Mark-to-market value** of that position at current market prices.
- **Unrealized P&L** (position value today minus position value at the time of deposit or last margin call).
- **Margin balance** (initial margin posted minus unrealized losses).

Consider an example: Member A is a clearing member at an equities exchange. It has posted $1 million in initial margin. It enters the day with no open positions. During the morning, it executes trades and accumulates a long position in XYZ stock worth $50 million at current market price. The clearing house's risk system sees this and calculates that a 5% one-day market move would cause a loss of $2.5 million—more than the initial margin posted. The system flags the position for increased monitoring.

By mid-afternoon, XYZ's price drops 3%. The member's unrealized loss is $1.5 million. The member's margin balance is now $1 million minus $1.5 million = negative $500,000. The margin balance has gone negative—a red flag. The clearing house's automated system triggers a variation margin call.

## The Margin Call Process

Once the clearing house's risk system detects a margin deficit, it follows a protocol:

### Step 1: Calculation and Notification

The risk team (or an automated algorithm) calculates the exact amount of the call. It may include:

- The current variation margin deficit (the loss since the last margin call).
- An estimate of additional margin to cover potential further losses until the next call window.
- Interest on any previous unpaid margin.
- Administrative fees.

The member is notified electronically (via email, API, or telephone hotline). The notification includes the call amount and the grace period—typically 1 to 4 hours depending on the exchange and the member's status.

### Step 2: Member Response

The member now has a choice:

1. **Deposit funds** via wire transfer to the clearing house's designated bank account.
2. **Deposit eligible collateral** (Treasury securities, cash equivalents, etc.) to its collateral account.
3. **Liquidate positions** to reduce its net exposure, thereby lowering the margin requirement.
4. **Default** (stop posting margin and allow the clearing house to seize and liquidate the member's positions).

Most members deposit additional margin. The clearing house credits the deposit in real-time or within minutes. The member's margin balance is restored. The call is satisfied.

### Step 3: Non-Payment and Escalation

If the member does not post margin within the grace period, the clearing house escalates:

1. **Account freeze**: No new trades are accepted from the member. Only liquidations are allowed.
2. **Forced liquidation**: The clearing house (or a designated broker) begins selling the member's positions. The goal is to reduce the net exposure and the margin requirement as fast as possible.
3. **Default procedure**: If the member's margin account is completely exhausted (liquidation revenues do not cover the shortfall), the clearing house declares the member in default and enters a formal default management process—auctioning the failed member's book to other members, using the clearing house's guarantee fund to cover residual losses.

Defaults are rare in developed markets. The threat of forced liquidation and the guarantee-fund assessments on other members (which can be substantial) create strong incentives to post margin on time.

## Frequency and Timing

Margin calls can happen multiple times a day, especially in volatile markets. Some clearing houses issue intraday calls every 2 to 4 hours. Others use a single daily call after market close.

The Federal Reserve's Fedwire and many U.S. equities clearing systems use multiple intraday calls. The CME (for futures) uses a twice-daily standard (AM and PM) but can call additional margin if market volatility spikes.

The speed of margin settlement varies:

- **U.S. equities exchanges**: Margin calls are often settled same-day; members have 4 hours or so to post.
- **Futures exchanges (CME)**: Margin is typically called at 4 p.m. Chicago time and must be settled by 6 a.m. the next morning.
- **OTC derivatives (via LCH, CME ClearPort, etc.)**: Intraday calls can be issued continuously; members must often post within 2–4 hours.

## Haircuts and Collateral Valuation

When a member deposits collateral (rather than cash) to meet a margin call, the clearing house does not accept it at full face value. It applies a **haircut**—a percentage discount—to account for potential price moves and liquidity risk.

For example:

| Collateral Type | Haircut | Accepted Value |
|---|---|---|
| U.S. Treasuries | 2% | 98 per $100 par |
| High-grade corporate bonds | 5% | 95 per $100 par |
| Equities | 15% | 85 per $100 par |
| Emerging market bonds | 20%+ | 80 per $100 par or less |

A member posting a Treasury with $100 par value (and a 2% haircut) gets $98 of margin credit. If the Treasury price falls 2% overnight, the clearing house's loss is limited.

## Margin Models: VaR and Stress Testing

Modern clearing houses use sophisticated risk models—typically Value-at-Risk (VaR) or historical stress scenarios—to calculate initial margin. A typical model might say: "On a 99th-percentile bad day, in the worst 5 trading days, a member's portfolio could lose $X million." Initial margin is set to cover that $X, plus a buffer.

These models are recalibrated frequently (often daily) to account for changes in market volatility. During market spikes (like March 2020's volatility), initial margin requirements can double or triple in hours. Members suddenly face large top-up calls and must scramble to post additional funds or liquidate positions.

## Default Procedures and Guarantee Funds

Despite margin calls, a member can still default if its losses exceed the clearing house's initial margin estimate. When this happens, the clearing house activates its **guarantee fund**—a pool of capital contributed by all members, often sized to cover the failure of the two largest members.

The guarantee fund covers:

- Losses on the failed member's positions (after liquidation).
- Costs to auction the failed member's book.
- Temporary carry costs.

Surviving members are then assessed for contributions to restore the guarantee fund. These assessments can be substantial; after a major default (rare), surviving members might owe millions in guarantee-fund replenishments.

## Technology and Automation

Margin calls are now almost entirely automated. Clearing house risk systems run 24/7 and calculate margin on a rolling or pre-set schedule (e.g., every 4 hours). When a threshold is breached, an electronic notification is generated and sent to the member's risk management system.

Members receive calls via:

- Email alerts.
- Web portals (member dashboards showing current margin status).
- API feeds to the member's trading platform.
- Telephone hotlines for critical situations.

The automation has dramatically sped up the margin settlement process and reduced human error. But it has also reduced flexibility—members no longer negotiate margins; they accept the clearing house's calculation or default.

## Cross-Clearing and Portability

Some members clear through multiple clearing houses (equities through one exchange, futures through another). If a member defaults at one clearing house, can another clearing house seize positions at the first clearing house as security?

This question of "portability" and "cross-collateralization" is still evolving. Most clearing houses operate independently, so defaults at one do not automatically freeze accounts at another. But regulators are pushing for better coordination to reduce systemic risk. Some dealer consortia and interdealer brokers have begun to share margin collateral across multiple clearing houses, but this remains rare.

---

## See also

<div class="wiki-seealso">

### Closely related

- [Cash Equities Settlement Cycle Explained](/cash-equities-settlement-cycle-explained/) — Margin calls occur during the T to T+1 window
- [Central Securities Depositories: Role in Settlement](/csd-role-in-securities-settlement/) — The CSD and clearing house are separate but coordinate
- [Bond Settlement vs Equity Settlement: Key Differences](/bond-settlement-vs-equity-settlement-differences/) — Different products have different margin models
- [Counterparty Risk](/counterparty-risk/) — The risk margin calls are designed to contain
- [Leverage Ratio](/leverage-ratio-forex/) — How margin relates to leverage and solvency

### Wider context

- [Broker](/broker/) — Clearing members are typically large brokers
- [Stock Exchange](/stock-exchange/) — Where trades are executed, triggering margin requirements
- [Federal Reserve](/federal-reserve/) — Oversees margin standards and may set regulatory requirements
- [Value-at-Risk](/value-at-risk/) — The risk metric used to calculate margin
- [Futures Contract](/futures-contract/) — Heavily margined products; margin calls are routine

</div>
