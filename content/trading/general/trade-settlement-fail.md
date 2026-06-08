---
title: "Trade Settlement Fail"
description: "A trade settlement fail occurs when a buyer or seller cannot deliver cash or securities by the settlement date. The SEC requires forced close-out under Rule 204."
keywords:
  - trade settlement fail
  - settlement failure
  - naked short selling
  - sec rule 204
  - close-out requirement
  - failed trade
---

*A **trade settlement fail** happens when either the buyer or seller in a stock transaction fails to deliver the required cash or securities by the agreed settlement date. The SEC's Rule 204 mandates forced close-out of persistent fails and bans naked short selling to prevent endless failed deliveries.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Trade Settlement Fail — Key Facts</div>

<img src="/svg/trading.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Settlement fails are rare in normal markets but spike during stress and can trigger regulatory forced buys.</div>

|   |   |
|---|---|
| **Definition** | Failure to deliver cash (buyer) or securities (seller) by T+1 or T+2 |
| **Standard settlement** | T+1 (next business day) for most US equities as of 2024 |
| **Regulatory trigger** | SEC Rule 204 forces close-out after 13 consecutive days of fail to deliver |
| **Main cause** | Operational delays, bankruptcy, missing shares, or short-selling abuse |
| **Retail investor risk** | Low in normal conditions; grows in low-liquidity stocks or during market stress |
| **Institutional impact** | Can amplify systemic risk if widespread across counterparties |

</aside>

## How Settlement Works and When It Fails

When you buy or sell a stock through a broker, the transaction happens in two parts: the trade execution (T) and the settlement (T+n). For most US equity trades today, settlement occurs T+1 (one business day later). The seller must deliver the securities; the buyer must deliver the cash.

A settlement fail occurs when the seller cannot produce the securities on time or the buyer cannot produce the cash. The reasons vary. A seller might have borrowed shares that weren't available in the expected quantity. A buyer's bank transfer might delay. A corporate action—dividend payment, stock split, merger deadline—can create a temporary mismatch. In rare cases, operational errors in the [custodian](/custodian/) or [clearing house](/stock-exchange/) systems cause a cascade of fails. During market dislocations, when counterparties face financial stress, fails can spike dramatically.

Most settlement fails resolve within a few days as the missing party scrambles to locate securities or clear funds. But some persist, especially if the seller never intended to deliver because they were engaged in naked short selling—selling shares they didn't own and had no imminent plan to borrow.

## SEC Rule 204 and Forced Close-Outs

The Securities and Exchange Commission introduced Rule 204 (Regulation SHO) partly to address the problem of persistent fails. Under this rule, if a firm fails to deliver securities for 13 consecutive settlement days (roughly two weeks), the firm must **close out** the position—that is, buy back the shares in the open market and force delivery. There is no discretion: after the 13-day window, the firm must act.

Before Rule 204, a short seller could allow a fail to persist indefinitely, effectively selling shares into the market that they neither owned nor intended to borrow, distorting the price. The rule's intent was to keep fails short-lived and discourage naked short selling.

In practice, enforcement requires that the counterparty—the [broker](/broker/) handling the fail—actively track and comply. A broker found repeatedly violating Rule 204 faces fines and operational restrictions. During the COVID-19 volatility spike in March 2020 and the retail trading surge of early 2021, fail-to-deliver reports spiked, prompting SEC scrutiny of certain brokers and market-makers.

## Naked Short Selling and Systemic Implications

A settlement fail becomes most damaging when it stems from naked short selling. In a naked short, the seller sells shares without ever arranging a borrow, hoping to buy them back lower before settlement. If the share price rises sharply or the borrower cannot be found, the seller is forced to buy at a loss or default.

Retail investors often don't notice fails because brokers absorb the immediate cost. But at the institutional level, widespread fails can cascade. If a major market-maker or dealer fails to settle, it can freeze credit flows and trigger forced liquidations elsewhere. The 2008 financial crisis saw several episodes of settlement gridlock as counterparty risk spiked.

The SEC's subsequent tightening of Rule 204 and the introduction of "locate" requirements (a broker must locate borrowable shares *before* short selling) was meant to reduce naked shorts and the fails they create. But the rule has exceptions for market-makers executing customer orders, so some degree of naked short selling persists under regulatory tolerance.

## Retail Investor Exposure and Low-Liquidity Stocks

For a typical retail investor holding shares, a settlement fail is almost invisible. You sell, your broker collects cash or receives shares, and you never know if the counterparty later had a problem settling.

The real risk to retail investors comes indirectly. In illiquid or low-cap stocks—where shares are harder to borrow—fails can be more common. If you are a holder in such a stock and the short-side of the market fails to deliver, the settlement backlog can suppress price discovery: fake shares (failed deliveries) depress the price artificially, and when forced close-outs finally happen, the price can spike. Trading thinly traded stocks carries [liquidity risk](/liquidity-risk/) for this reason, not merely from [bid-ask spreads](/bid-ask-spread/).

Conversely, if you are trying to *short* a low-liquidity stock and fail to deliver, your broker has regulatory obligation to close you out after 13 days. During that wait, your losses may mount, or your order to buy back to close may itself move the market against you.

## Retail Versus Institutional Fails

Retail brokers (like those handling individual accounts) experience fails primarily through operational delays: a customer's bank takes longer than expected to clear a wire, or the customer mistakenly sells shares before the prior purchase settled (buying power lag). These fails are typically resolved within a few days.

Institutional fails are more strategic and risky. A [hedge fund](/hedge-fund/) or proprietary trader might intentionally allow a short-sale fail to persist, betting on a continued price decline. A [prime broker](/broker/) funding multiple short-sellers might fail to locate enough shares quickly and carry multiple positions at fail simultaneously. These fails are larger in absolute dollars and can create [counterparty risk](/counterparty-risk/) if the failing party's capital erodes.

During stress events—earnings surprises, regulatory announcements, or bankruptcies—failed deliveries spike across both retail and institutional segments, though the institutional side usually matters more for systemic stability.

## What Happens After a Fail Is Closed Out

Once a forced close-out is executed (after 13+ days), the failing firm buys shares on the open market to settle the obligation. If the stock has risen, the firm realizes a loss. If it has fallen, they gain. But the point of Rule 204 is not to profit the defaulter; it is to **force re-entry** into the market and allow price discovery to function.

A forced buy-to-close also tends to be visible to other market participants as unusual order flow, which can trigger a rally in the shorted stock. This is one reason short-sellers and their brokers work hard to avoid hitting the 13-day threshold: the forced close-out is expensive and public.

## See also

<div class="wiki-seealso">

### Closely related

- [Short selling](/short-selling/) — selling shares you don't own, the practice that spawns many settlement fails
- [Bid-ask spread](/bid-ask-spread/) — the cost of re-entry when forced to buy back failed shares
- [Counterparty risk](/counterparty-risk/) — the danger that a failing settlement counterparty causes contagion
- [Market maker trading](/market-maker-trading/) — how dealers provide liquidity despite settlement friction
- [Over-the-counter market](/over-the-counter-market/) — OTC equities and bonds have higher fail rates than exchange-listed stock
- [Custodian](/custodian/) — the entity holding securities and responsible for delivery

### Wider context

- [Stock exchange](/stock-exchange/) — the venue where shares trade and settle
- [Stock](/stock/) — the basic security whose delivery fails we are discussing
- [Liquidity risk](/liquidity-risk/) — the broader category of risks from illiquid positions
- [Concentration risk](/concentration-risk/) — how fails can concentrate losses in tight markets

</div>
