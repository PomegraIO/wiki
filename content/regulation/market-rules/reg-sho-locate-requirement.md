---
title: "Reg SHO Locate Requirement"
description: "The broker-dealer obligation to locate shares before executing a short sale under Reg SHO, including valid locate sources and exemptions."
keywords:
  - reg sho locate requirement
  - short sale locate
  - broker-dealer compliance
  - short selling rules
  - locate share requirement
image: /svg/regulation.svg
---

*Before a broker-dealer can execute a **short sale**, it must have a reasonable belief that it can borrow the shares to deliver them. The **Reg SHO locate requirement** imposes this obligation formally: the broker must obtain a "locate"—a written confirmation from the securities department, a borrow source, or an internal inventory—that the shares are available before sending the order to the market. Without a valid locate, the trade is prohibited, even if the underlying company is not on a short-sale restriction list.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Reg SHO Locate — Key Facts</div>

<img src="/svg/regulation.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">A locate is the gatekeeper for every short sale order.</div>

|   |   |
|---|---|
| **Timing requirement** | Before order is sent to market (not after fill) |
| **Who obtains it** | The broker's operations/back-office team |
| **Valid sources** | Internal inventory, borrowing agent, prime broker, clearing firm |
| **Documentation** | Written; must identify the specific source |
| **Duration** | Valid for the day of the short sale; carries forward if not used |
| **Penalties** | SEC sanctions, customer restitution, trade cancellation |
| **Exceptions** | Some exempted securities or market-maker quotes in their own names |

</aside>

## The Purpose and Origin

The locate requirement exists to prevent **naked short selling**—selling shares the seller does not own and cannot borrow, leaving a failure to deliver (FTD). In the early 2000s, naked short selling became a problem in small-cap and over-the-counter markets, allowing bad actors to manipulate prices downward and leave unsettled trades. The SEC adopted Reg SHO in 2005 partly to enforce the locate rule, requiring brokers to be certain of their ability to borrow *before* a short sale executes, not merely *hoping* they could find shares later.

A locate is not the same as actually borrowing the shares (which happens at settlement). Instead, it is a commitment from an internal or external source that the shares will be available for borrowing when needed. This distinction matters: the borrowing agent says "yes, we can source these," not "we have already borrowed them." But the broker is not supposed to route a short sale unless that commitment is firm.

## Valid Locate Sources

A broker-dealer can obtain a locate from:

1. **Its own securities department** (inventory): the broker holds shares in-house, either as part of its trading inventory, customer margin accounts, or stock-lending pool.
2. **A borrow agent or securities lending firm**: a third-party specialist (e.g., Equiloan, DTC, a prime broker's securities lending desk) that maintains a pool of lendable shares and agrees to make them available.
3. **A prime broker or clearing firm**: for introducing brokers or hedge funds, the prime broker's back-office may provide the locate on behalf of a client.
4. **The customer's own broker** (for customer short sales): if the customer already holds shares, the broker may lend them from the customer account; the broker then locates them internally.

What does **not** count as a valid locate:

- A promise to "try to borrow" or "best-efforts" language. The source must affirmatively confirm availability.
- Relying on the short seller's assertion that they own shares elsewhere. The locate must come from a custodian or lending source, not the customer's honor system.
- A locate obtained *after* the order is sent to the market. Timing is critical: the locate must be in place *before* the order leaves the broker's system.

## The Locate Process in Practice

A typical workflow:

1. **Customer orders a short sale** of 1,000 shares of Company X.
2. **Broker's operations team** checks: Do we have 1,000 shares available? (They review inventory, margin accounts, stock-lending pool, and third-party borrow sources.)
3. **A borrow agent confirms**: "Yes, we can lend 1,000 shares of Company X."
4. **Broker obtains a written locate** (often a system flag, ticket, or confirmation email) showing the date, security, quantity, and source.
5. **Only then** does the broker send the short-sale order to the market for execution.
6. **At settlement** (usually T+2), the borrowed shares are delivered to the buyer's account.

If the broker *cannot* obtain a locate—say, shares are in short supply and no lender will commit—the broker **must refuse the short-sale order**. The customer cannot short-sell that stock, period. This is where the locate requirement bites: it is not a suggestion or a best-efforts rule. Failure to locate makes the trade illegal.

## Exceptions and Exemptions

The locate requirement has narrow carve-outs:

- **Designated market makers (DMMs) on NYSE** are sometimes exempt from the locate requirement when quoting in their designated securities, on the assumption that they facilitate price discovery and liquidity.
- **Nasdaq market makers** may have similar exemptions for their own quoted securities, subject to other Reg SHO compliance obligations.
- **Certain corporate securities**, particularly those with low trading volume or illiquidity, may be subject to alternative locate procedures.

However, these exemptions are narrow and do not excuse brokers from obtaining a locate for ordinary customer short sales.

## How Brokers Document and Communicate Locates

Large brokers maintain internal systems that log locates by:

- Date and time of the locate
- Security symbol and quantity
- Source (internal department code, external lender name)
- Expiration or carry-forward status

When a customer places a short-sale order, the broker's order-entry system checks the locate log automatically. If no locate is found, the system flags it as a "no-locate" order and rejects it or marks it for manual review.

Some brokers notify customers in real time: "Short sale accepted—1,000 shares located" appears on the trade confirmation. Others only document it internally. Either way, the SEC expects the broker to maintain audit trails showing when and from where the locate was obtained.

## Failures to Deliver and the Close-Out Rule

If a broker routes a short sale without a valid locate and the trade settles, the result is a **failure to deliver (FTD)**. Under Reg SHO's close-out rule, if an FTD persists for 13 consecutive settlement days (in a threshold security), the broker must close out the short position—buy in the shares to force a delivery and end the naked short.

Locates are the front-line defense: a proper locate means the broker is confident it can satisfy delivery. If delivery fails anyway (a lender changes its mind, or shares are tied up unexpectedly), the broker absorbs the cost of the buy-in. This creates a strong incentive for brokers to take locates seriously.

## Enforcement and Penalties

The SEC has fined and sanctioned brokers and clearing firms for locate violations, including:

- **Execution of short sales without a valid locate**: trading activity against Reg SHO.
- **Inadequate locate documentation**: failure to maintain audit trails.
- **Circumventing the rule**: using sham locates or false confirmations.

Penalties range from warning letters to fines of millions of dollars, plus customer restitution and third-party monitoring. In egregious cases, the SEC has also referred brokers to FINRA for additional disciplinary action, including suspension of short-selling privileges.

## Relationship to Price Stability and Restrictions

The locate requirement interacts with other short-sale restrictions. If a stock triggers a short-sale circuit breaker (such as the Uptick Rule alternative in Reg SHO Rule 10a-1), short sales are already restricted. A trader must still obtain a locate, *and* comply with the uptick rule or limit order requirement. The locate is a separate gate: even if the uptick rule allows your short sale, your broker still cannot execute it without a locate.

## See also

<div class="wiki-seealso">

### Closely related

- [Short Selling](/short-selling/) — the trading strategy regulated by Reg SHO
- [Clearly Erroneous Trade Cancellation](/clearly-erroneous-trade-cancellation/) — another market integrity mechanism
- [Consolidated Audit Trail (CAT) Reporting](/consolidated-audit-trail-cat-reporting/) — SEC system tracking order and trade details used to police short-sale compliance
- Failure to Deliver — outcome of unlocated short sales
- [Market Maker Quoting Obligations](/market-maker-quoting-obligations/) — related regulatory obligations for trading

### Wider context

- [Securities and Exchange Commission](/securities-and-exchange-commission/) — regulator enforcing Reg SHO
- [Broker](/broker/) — the party responsible for obtaining the locate
- Clearing and Settlement — where delivery obligations are resolved
- Trading Halt — another tool for controlling short selling
- [Circuit Breaker](/circuit-breaker/) — market-wide short-sale restrictions

</div>
