---
title: "Variation Margin vs Initial Margin"
description: "How variation margin covers daily mark-to-market losses while initial margin covers potential future exposure; why a clearinghouse collects both."
keywords:
  - variation margin vs initial margin difference
  - initial margin requirement
  - variation margin daily
  - mark-to-market futures clearing
  - margin call clearinghouse
image: "/svg/institutions.svg"
---

*A **variation margin vs initial margin** distinction is the backbone of futures and cleared derivatives risk management.* **Initial margin** is the upfront collateral a trader must post to enter a position—a buffer against potential future price swings. **Variation margin** is the daily cash settlement of actual losses and gains, collected at the end of each trading session. A clearinghouse requires both, and the two work in tandem: initial margin guards against default from hypothetical moves, while variation margin ensures daily losses don't accumulate into a catastrophic hole.

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Variation Margin vs Initial Margin — key facts</div>

<img src="/svg/institutions.svg" alt="An abstract editorial mark for institutions." />

<div class="wiki-infobox-caption">Initial margin is upfront collateral; variation margin is daily settled gain or loss. A clearinghouse collects both to protect itself and other clearing members.</div>

|   |   |
|---|---|
| **Initial margin** | Upfront collateral; remains in account; covers potential future loss |
| **Variation margin** | Daily cash settlement of mark-to-market gain/loss |
| **Collection frequency** | Initial: once per position; Variation: daily (usually end of session) |
| **Purpose of initial** | Absorb hypothetical adverse moves before default |
| **Purpose of variation** | Lock in daily realized losses; prevent accumulation |
| **Who collects** | Clearinghouse on behalf of clearing members and market |
| **When margin call occurs** | When account falls below minimum threshold (usually 75% of initial) |

</aside>

## Initial Margin: Upfront Collateral

**Initial margin** is the cash or securities a trader must deposit when opening a futures or cleared derivatives position. It exists to cover the clearinghouse's expected loss if the trader defaults and the position must be liquidated at a loss. The size of initial margin is set by the clearinghouse based on the instrument's historical volatility and the maximum single-day price move that the margin should cover.

**Example:** A trader buys one crude oil futures contract. The contract size is 1,000 barrels; the front-month crude contract trades around $70/barrel. Initial margin for crude is typically $5,000–$6,000 per contract (a one-day volatility buffer of perhaps $2–$3). The trader must deposit $5,500 in cash or acceptable securities. That $5,500 sits in the account and remains there as long as the position is open. It is *not* spent or withdrawn at the end of the day; it is collateral.

Initial margin typically covers a one-day adverse move at a confidence level the clearinghouse chooses (often 99%). This means the clearinghouse expects that on roughly 250 trading days per year, the daily loss could exceed the initial margin. In those cases, variation margin is meant to have already reduced the account balance, or a [margin call](/margin-call-forex/) forces the trader to post more collateral. But the day-to-day protection comes from variation margin.

## Variation Margin: Daily Settlement

**Variation margin** is the cash that flows in or out of an account at the end of each trading day, reflecting the change in the value of the trader's position. It is also called **mark-to-market** settlement.

**Example (continued):** The crude contract opens at $70/barrel. The trader bought at $70 and nothing has moved, so variation margin is zero. By the close, crude has risen to $71. The contract is now worth an additional $1 × 1,000 barrels = $1,000. The clearinghouse credits the trader's account with $1,000 in variation margin. That cash is immediately available—the trader could withdraw it. The next day, if crude falls to $69, the trader loses $2,000 (from the original $70 entry). The clearinghouse debits the account by $2,000. The trader must cover this variation margin debit or face a margin call.

Variation margin is settled daily, at a fixed time (usually after market close). For some instruments (certain exchange-traded derivatives), it may be settled intraday if volatility spikes and positions move sharply. The clearinghouse transfers the cash between the buyer and seller, netting out the gain and loss.

## Why the Clearinghouse Requires Both

The clearinghouse is the counterparty to every open position after [novation](/clearing-fee-how-it-works/)—it stands between the buyer and the seller. If a trader defaults, the clearinghouse must be able to liquidate the position without taking a loss itself. Here's the logic:

1. **Initial margin** protects the clearinghouse against a sudden, large overnight move. If crude gaps up $5/barrel at the open, the trader's short position is underwater by $5,000 immediately. The initial margin buffer absorbs this. The trader might have enough equity in the account to stay above the maintenance margin threshold (often 75% of initial margin, or $4,125 in this example).

2. **Variation margin** prevents the problem from *compounding*. If daily losses are not settled immediately, they accumulate. A trader could rack up $50,000 in paper losses before the clearinghouse realizes the account is depleted. By settling variation margin daily, the clearinghouse extracts cash from the losing trader and credits the winning trader, ensuring the account doesn't disappear without action.

3. **[Margin calls](/margin-call-forex/)** bridge the gap. If the account falls below the maintenance margin threshold (often 75% of initial margin), the clearinghouse issues a margin call: "Post another $X by tomorrow's open or we liquidate your position." This forces a trader to choose between adding capital or exiting the trade, rather than hoping for a reversal and running a growing deficit.

## The Mechanics of a Daily Cycle

At the end of each trading day, the clearinghouse:

1. Marks all open positions to the closing price.
2. Calculates the gain or loss for each position since the *previous day's close* (or since inception, if the position was opened that day).
3. Debits or credits each clearing member's account with variation margin.
4. Checks whether each clearing member's account balance (initial margin + accumulated variation margin gains – accumulated variation margin losses) exceeds the maintenance margin threshold.
5. If not, issues a margin call for additional funds by the next morning.

**Example:** A trader buys a futures contract with initial margin of $5,000. After day 1, the contract gains $1,000 (variation margin in). The account has $6,000. After day 2, it loses $3,000 (variation margin out). The account has $3,000. If maintenance margin is $3,750 (75% of $5,000), the account is now below the threshold, and the trader receives a margin call for at least $750 to restore the threshold.

## Initial Margin and Volatility

Clearinghouses adjust initial margin based on market conditions. When volatility spikes—a surprise interest-rate decision, a geopolitical shock—the clearinghouse may increase initial margin requirements. A crude contract with a $5,500 initial margin might jump to $7,000 or higher if volatility doubles. Existing positions see the new requirement; new positions must meet the higher amount. This proactive adjustment protects the clearinghouse by ensuring the buffer is still sufficient.

## Variation Margin Under Stress

During extreme market moves, variation margin can demand large cash outflows in a single day. A trader holding a large short position when the market gaps sharply up might face a sudden debit of hundreds of thousands of dollars. This is where [liquidity risk](/liquidity-risk/) becomes critical: the trader must have access to cash at the start of the next trading day, or the clearinghouse liquidates the position.

## The Role of the Clearing Member

Individual traders do not interact directly with the clearinghouse. Instead, they trade through a **broker** (a [clearinghouse](/clearing-fee-how-it-works/) member or a firm that clears through a member). The member firm collects initial margin from the trader, maintains it at the clearinghouse, and rebalances it as variation margin flows in and out. The member firm may also charge the trader for [variation margin financing](/clearing-fee-how-it-works/) (if the clearinghouse uses intraday margining) and may add its own buffer on top of the clearinghouse requirement for risk management.

## See also

<div class="wiki-seealso">

### Closely related

- [Margin Call (Forex)](/margin-call-forex/) — the trigger when account falls below maintenance threshold
- [Clearing Fee](/clearing-fee-how-it-works/) — fees assessed alongside margin collection
- [Open Interest and Clearing](/open-interest-and-clearing/) — how positions are tracked and novated
- [Futures Contract](/futures-contract/) — the instrument settled with initial and variation margin
- [Counterparty Risk](/counterparty-risk/) — why the clearinghouse requires both margin types

### Wider context

- [Clearinghouses](/clearing-fee-how-it-works/) — institutions managing default risk and settlement
- [Central Bank](/central-bank/) — oversees clearing rules and systemic risk
- [Systemic Risk](/systemic-risk/) — why margin standards matter for stability
- [Derivatives Hedging](/derivatives-hedging/) — how firms use futures and require margin
- [Volatility Smile](/volatility-smile/) — drives changes in initial margin settings

</div>
