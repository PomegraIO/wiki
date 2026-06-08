---
title: "T+1 vs T+2 Settlement Across Global Markets"
description: "How settlement cycles differ across major stock exchanges and the cash flow and operational risk implications for cross-border traders."
keywords:
  - t+1 settlement
  - t+2 settlement
  - t+1 vs t+2 settlement global markets
  - settlement cycles
  - trade settlement
  - cross-border trading
image: "/svg/markets.svg"
---

*Different stock exchanges settle trades on different timelines—some in **T+1** (one business day), others in **T+2** (two business days)—creating timing mismatches for investors who trade across borders and requiring bridge financing, careful cash forecasting, and coordination with [custodians](/custodian/).*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Settlement Cycles — key facts</div>

<img src="/svg/markets.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">You trade today; money and shares move days later. Different markets have different calendars.</div>

|   |   |
|---|---|
| **T+1 definition** | Trade settles and cash/shares exchange one business day after the trade date |
| **T+2 definition** | Trade settles and cash/shares exchange two business days after the trade date |
| **T+1 markets** | U.S., Canada, Australia, Hong Kong, some European markets (as of 2024) |
| **T+2 markets** | Japan, India, Singapore, many Asian and European bourses; gradually transitioning |
| **Risk window** | Counterparty risk during the gap; buyer holds share before owning it, seller holds cash before receiving it |
| **Coordination cost** | Cross-border traders face mismatched settlement dates; need bridge financing and careful cash planning |

</aside>

## The settlement timeline explained

When you buy or sell a stock on an exchange, the trade is **executed instantly**—you and your counterparty agree on a price and quantity in microseconds. But the actual transfer of cash and shares takes time: clearing houses, [custodians](/custodian/), and banking systems must verify identities, check for fraud, and move funds between accounts across different banking networks.

**T+1** means settlement occurs one business day after the trade. If you buy stock on a Monday, the seller receives the cash and you receive the shares on Tuesday. **T+2** means settlement is two business days later—a Monday trade settles on Wednesday.

The difference is not arbitrary. A T+1 settlement requires faster back-office processing, more automated fraud detection, and tighter coordination between brokers and clearing houses. A T+2 cycle is slower but historically left more time for manual verification and paper-based processes. As exchanges have invested in technology, many have moved to T+1 to reduce risk and speed up capital reuse.

## Why markets chose different timelines

**The United States moved to T+1 in 2024**, completing a years-long industry initiative that began in 2015. Before that, U.S. equity markets had settled on T+2 for decades. The push to T+1 was driven by the desire to shrink the **window of counterparty risk**: during the T+2 period, the buyer's broker is owed shares it doesn't yet own, and the seller's broker is holding cash before passing it along. If a broker fails during that window, the other party may face losses or delays.

**Canada, Australia, and Hong Kong moved to T+1 earlier**, partly to align with innovation leadership and partly because their financial infrastructure was newer and more readily adaptable to faster settlement. **Japan, India, and Singapore remain on T+2**, though there is industry discussion about accelerating. Regulatory inertia, legacy systems, and the cost of switching are the main obstacles.

European exchanges are mixed: some large bourses like Euronext moved toward T+1, while others remained on T+2. This fragmentation is one reason Europe has been slower to consolidate its equity markets than the U.S. and Asia-Pacific.

## The cross-border settlement mismatch

The real cost emerges when an investor or fund manager trades across borders. Suppose a U.S. pension fund buys Japanese shares on the Tokyo Stock Exchange on a Monday. The U.S. market settles T+1 (Tuesday), but Japan settles T+2 (Wednesday). The fund's cash obligation comes due Tuesday, but the Japanese shares don't arrive until Wednesday—a one-day mismatch.

The fund can manage this by holding a [cash conversion cycle](/cash-conversion-cycle/) buffer, borrowing short-term cash, or asking its [custodian](/custodian/) to extend credit. But each option has a cost: the interest rate on overnight borrowing, the opportunity cost of idle cash, or explicit lending fees charged by the custodian. For large institutional traders making dozens of cross-border trades daily, these mismatches accumulate into thousands of dollars per month in financing costs.

Some custodians offer **settlement matching services**, where they accelerate the arrival of foreign shares or delay the outflow of cash to align settlement dates. These services are not free—they represent a service charge that factors into the total cost of a trade.

## Risk during the settlement window

Between trade and settlement, several risks lurk. **Counterparty risk** is the primary one: if the broker on either side fails, the other party may be left holding an uncompleted trade. In a T+1 world, this risk window is shorter, so the exposure is lower. But it's not zero.

**Operational risk** also rises with a longer settlement window. If a back-office system crashes or a payment message is delayed, trades can back up. A T+2 system absorbs a one-day delay more easily; a T+1 system leaves no margin for error.

For the **buyer**, there's the risk of price movement before settlement. You buy a stock on Monday, intending to own it on Tuesday (T+1), but if a scandal breaks Tuesday morning before settlement, you're locked into ownership at Monday's price with no recourse. In a T+2 world, you have an extra day to walk away from failed trades (though you may face penalties).

For the **seller**, there's cash-in-hand risk: you don't hold the money until settlement is complete, leaving you exposed to the broker or custodian failing or losing the transaction in a system error.

## Global coordination and transition costs

The transition from T+2 to T+1 in the U.S. was not instantaneous—there was an industry-wide cutover on May 28, 2024. Every broker, custodian, fund manager, and clearing house had to test their systems, retrain staff, and update settlement instructions. The cost of that transition was measured in millions of dollars industry-wide, and smaller firms bore a disproportionate burden because they had fewer IT resources.

Japan and India are watching the U.S. experience before committing to a similar move. The cost-benefit calculation for them is different: in markets with lower per-capita volumes or less automation, the risk reduction from T+1 may not justify the upfront investment.

In the meantime, **cross-border traders must manage the mismatches themselves**. A global asset manager will maintain settlement calendars for each market, forecast cash flows by settlement date, and coordinate with custodians to optimize financing costs. Large trades are often negotiated with settlement timing explicitly included—a buyer might agree to pay a small premium if the seller consents to accelerated settlement, or vice versa.

## The borrowing cost calculation

For a trader or fund manager, the cost of a settlement mismatch is roughly the cost of borrowing money for one extra day. If overnight rates are 5% per year, the one-day cost of financing a $10 million trade is roughly $1,370. For a high-volume trader, this adds up fast.

Some market participants use **repurchase agreements** ([reverse repos](/repurchase-agreement/)) to manage settlement mismatches. They'll borrow cash against the shares they'll receive, covering the gap at a lower cost than unsecured borrowing. This is particularly common in institutional trading.

The savings from moving a market to T+1 are not just in lower counterparty risk—they're also in reduced financing costs. The global financial industry collectively saves billions of dollars per year by shortening settlement windows, because less working capital is tied up in the settlement window at any moment.

## Custody and local market rules

Different exchanges also impose different custody requirements. Some markets require foreign shares to be held by a **local custodian**, which means a global investor buying Tokyo-listed shares must hold them through a Japanese custodian, not their home-country broker. This creates an extra layer of settlement complexity: the investor's home broker settles with a foreign broker, which settles with the Japanese custodian.

For an investor managing money across 15 countries, this means 15 different settlement timelines, custody arrangements, and fee structures. The coordination cost is why large global asset managers employ entire teams of settlement specialists.

## The direction of change

The global trend is toward **faster settlement**. The U.S. completed its transition to T+1; other major markets will follow, though on their own timelines. The long-term goal in the industry is **T+0** (same-day settlement), which would eliminate the settlement window entirely—but this requires real-time payment systems and has proven technically and operationally challenging. Until then, T+1 is the ambitious frontier, and T+2 remains the practical global standard for many markets.

Investors who trade frequently across borders should track settlement calendars religiously and factor settlement costs into their expected returns. For buy-and-hold investors, settlement timing is a one-time cost on entry and exit, but for active traders managing dozens of simultaneous positions, it's a material operational expense.

## See also

<div class="wiki-seealso">

### Closely related

- [Dual-Listed Shares and Price Divergence](/dual-listed-shares-price-divergence/) — price gaps across exchanges, complicated by settlement timing
- [Custodian](/custodian/) — the entity holding your assets and managing settlement
- [Repurchase agreement](/repurchase-agreement/) — borrowing cash against securities to bridge gaps
- [Cash conversion cycle](/cash-conversion-cycle/) — managing timing of cash flows
- [Counterparty risk](/counterparty-risk/) — exposure when the other party fails
- [Settlement cycles](/secondary-market/) — how trades complete and ownership transfers

### Wider context

- [Secondary market](/secondary-market/) — where stocks trade after initial listing
- [Broker](/broker/) — intermediary between buyer and seller
- [Federal deposit insurance corporation](/federal-deposit-insurance-corporation/) — safety net if a broker fails
- [Stock exchange](/stock-exchange/) — the venue running the settlement infrastructure
- [New York Stock Exchange](/new-york-stock-exchange/) — U.S. exchange that moved to T+1
- [Tokyo Stock Exchange](/tokyo-stock-exchange/) — major T+2 market

</div>
