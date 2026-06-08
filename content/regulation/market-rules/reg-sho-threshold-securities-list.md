---
title: "Reg SHO Threshold Securities List Explained"
description: "What stocks land on the SEC's reg SHO threshold securities list, and what close-out rules that creates for short sellers."
keywords:
  - reg sho threshold securities list
  - threshold list short selling
  - sec short sale close-out requirements
  - naked short selling regulation
image: /svg/regulation.svg
---

*The **Reg SHO threshold securities list** is the SEC's daily inventory of stocks where excessive naked short positions have failed to settle. Landing on the list does not ban short selling—it triggers mandatory close-out of the oldest failed trades, and requires brokers and clearing houses to make extra efforts to locate shares before executing fresh short sales.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Reg SHO Threshold List — Key Facts</div>

<img src="/svg/regulation.svg" alt="An abstract editorial mark for regulation." />

<div class="wiki-infobox-caption">Daily list of equities where failed settlements exceed thresholds; subjects short sellers to mandatory close-out schedules.</div>

|   |   |
|---|---|
| **Trigger threshold** | Fails-to-deliver exceeding 0.5% of shares outstanding for five consecutive days |
| **Who publishes it** | SEC (via FINRA data feeds) |
| **Main consequence** | Required close-out of oldest unsettled short sale by specific deadline |
| **Effect on new shorts** | Broker must locate shares before executing; no naked shortening allowed |
| **Removal timeline** | Stock removed the day fails fall below threshold for five consecutive settlement days |
| **Applies to** | All US equities, listed and OTC |

</aside>

## How a stock lands on the list

A stock appears on the Reg SHO threshold list when **fails-to-deliver in that security accumulate to 0.5% or more of the company's outstanding shares for five consecutive settlement days**. A "fail-to-deliver" is a short sale that has not yet settled—the short seller has not delivered shares to the buyer by the required settlement date (typically two business days after the trade).

This is not a judgment call or SEC discretion. The list is mechanical: FINRA collects settlement data, calculates the fail percentage each day, and if the threshold is crossed for five straight days, the security is added to the next published list. Conversely, once fails drop below 0.5% for five consecutive settlement days, the stock is removed.

The list is published daily by FINRA and the SEC, making it a matter of public record. Major financial vendors (Bloomberg, Reuters, Morningstar) republish it; many retail brokers alert clients to threshold status. This transparency means traders and investors know immediately which stocks are experiencing settlement problems.

## Why fails accumulate: naked short selling

A fail-to-deliver occurs when a short seller borrows (or promises to borrow) shares but does not actually deliver them by settlement. In "naked" short selling, the seller never bothers to locate the shares beforehand. A broker then has failed to deliver and, by regulation, must take steps to resolve it.

Fails happen for legitimate reasons too—a lending agent may miscommunicate, a broker's internal systems may break, or market conditions may prevent locating shares. But sustained fails across thousands of shares suggest either incompetence or deliberate abuses. The threshold list is the SEC's main tool to force resolution.

## Close-out obligations: the enforcement mechanism

Once a stock lands on the threshold list, the rules tighten immediately. **The short seller must close out (buy back) the oldest fails within a set deadline—usually by settlement day T+35 (35 days after the failed trade).**

If the fail is not covered, the broker and clearing house become liable for the delivery obligation. This creates pressure up the chain: the clearing house (DTCC) may force the broker's position, and the broker may force the trader's position. The goal is to make holding a failed position too expensive or risky to bear.

Brokers also face restrictions on executing new short sales in threshold securities. Before shorting a stock on the threshold list, a broker must "locate" the shares—demonstrating that borrowable inventory exists and can actually be delivered by T+2. This is not a light duty: it means the broker must have a specific, bona fide borrow lined up, not a vague promise. In practice, this makes shorting threshold securities much harder and more expensive.

## The critical distinction: listing ≠ ban

A common misunderstanding: **being on the threshold list is not the same as being naked-short banned**. The list does not forbid short selling. It simply mandates that new shorts must be settled and that old fails must be closed out on schedule.

Some stocks have been on and off the threshold list dozens of times over years. A stock can appear when big institutional shorts fail (e.g., a hedge fund short that settles slowly, technical glitches in clearing), then be removed days later when the backlog clears. Other stocks, particularly those with low free float or where there is significant short interest and tight borrowing markets, may remain on the list chronically.

The SEC can impose a temporary short sale circuit breaker on a security under Rule 10a-1, but that is a separate, more drastic step reserved for extreme cases. Threshold list status is preventative, not prohibitive.

## Who monitors and enforces

FINRA collects fail data from all brokers and dealers. The SEC and FINRA jointly publish the list. Brokers are responsible for ensuring they do not execute short sales that fail to settle, and for closing out positions that do fail. Clearing houses and prime brokers audit the data and enforce deadlines.

Retail short sellers rarely deal with threshold rules directly—their brokers do. But institutional shorts, hedge funds, and proprietary traders need to track the list closely, because the locate requirement and close-out schedule directly impact their strategy and cost of capital.

## Real-world patterns

Threshold lists are most common among:

- **Highly shorted stocks** with small free float (shares available to lend).
- **Penny stocks and microcaps**, where settlement infrastructure is weaker and borrowing is concentrated.
- **Highly volatile or distressed equities**, where trading volume spikes but settlement capacity lags.
- **Newly IPO'd stocks**, where lending inventory is scarce and short interest builds quickly.

Large-cap stocks seldom appear, because lending markets are deep, settlement infrastructure is robust, and short interest is spread across many lenders. When a blue-chip stock does land on the list (e.g., during a short squeeze or crisis), it usually signals temporary market stress, not a structural problem.

## Regulatory intent and limitations

The threshold list is part of the SEC's **2005 Reg SHO reforms**, which aimed to reduce naked short selling and delivery failures. Before these rules, failed deliveries were rampant and, in some cases, naked shorting was used to manipulate small-cap stock prices. The threshold list and close-out obligation have reduced naked shorting materially, but have not eliminated it—brokers, traders, and lenders still find ways to stretch settlement, especially in illiquid securities.

Critics argue that the rules are toothless for coordinated manipulation and that chronic threshold stocks remain too common. Supporters note that the list is transparent, enforcement is automatic, and costs to short have risen meaningfully. The debate persists.

## See also

<div class="wiki-seealso">

### Closely related

- [Short selling](/short-selling/) — the practice of selling borrowed securities to profit from a price decline.
- [Bid-ask spread](/bid-ask-spread/) — the cost gap that short sellers face when covering fails in thin markets.
- [Liquidity risk](/liquidity-risk/) — why hard-to-borrow stocks often land on the threshold list.
- [Market maker trading](/market-maker-trading/) — how dealers manage inventory and fails in equities.
- [Counterparty risk](/counterparty-risk/) — the broker and clearing house exposure when fails persist.

### Wider context

- [Securities and Exchange Commission](/securities-and-exchange-commission/) — the federal regulator that publishes and enforces the threshold list.
- [Finra](/finra/) — the self-regulatory organization that collects and reports fail data.
- [Proxy fight](/proxy-fight/) — shareholder contests where naked short selling and threshold lists have been flashpoints.
- [Stock exchange](/stock-exchange/) — the venues where threshold-listed securities are traded.

</div>
