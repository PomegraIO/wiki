---
title: "Marking the Close Prohibition"
description: "SEC rule banning trades executed near or at the market close specifically to influence the official closing price."
keywords:
  - marking the close
  - close manipulation
  - market manipulation
  - closing price
  - sec trading rules
---

*The **marking the close prohibition** forbids traders from executing large trades in the final minutes of the trading day with the intent to move the official closing price. The rule targets a specific form of [market manipulation](/), one that distorts the price used as a benchmark for portfolio valuations, index rebalancing, and the next day's opening.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Marking the Close Prohibition — key facts</div>

<img src="/svg/regulation.svg" alt="An abstract editorial mark for market regulation." />

<div class="wiki-infobox-caption">Closing prices matter far beyond the final tick.</div>

|   |   |
|---|---|
| **What it is** | SEC rule prohibiting execution of trades to artificially move the official closing price |
| **Legal basis** | Securities Exchange Act Section 10(b) and Rule 10b-5; codified in Regulation SHO and antifraud rules |
| **Key marker** | Intent to affect the close; effect on price is not always required |
| **Typical window** | Last 10–15 minutes of regular trading; also applies to [after-hours](/), pre-market |
| **Enforcement** | SEC and [FINRA](/); civil and criminal penalties available |
| **Major cases** | Barclays (2012), Deutsche Bank (2015), various high-frequency traders |
| **Why it matters** | Closing prices are benchmarks for valuations, option settlement, and fund performance |

</aside>

## Why the closing price is a prize worth fighting for

Every trading day ends at 4:00 p.m. ET on US equity exchanges. The last price at which a stock changes hands becomes the official close—the figure printed in financial databases, used to calculate [net asset value](/net-asset-value/) for [mutual funds](/mutual-fund/) and [ETFs](/etf/), and the benchmark against which institutional investors judge fund manager performance.

Because the closing price carries such weight, it becomes a target for manipulation. A trader holding a large position in a stock—say, 1 million shares bought at $50—can push the close higher by flooding the final minutes with buy orders, even at inflated prices. This artificial bump raises the [closing price](/), making the trader's position more valuable on paper. If the trader plans to sell in the next day's [opening](/), the inflated close flows into tomorrow's benchmark prices, potentially drawing in unsuspecting buyers.

Alternatively, a short seller betting that a stock will fall can execute a flurry of sell orders in the final seconds to depress the close, triggering [stop-loss](//) orders on long positions and sowing pessimism before the next day. The closing price, once moved, becomes an anchor that influences how other investors view the stock for hours.

## The rule and its scope

The SEC prohibition on marking the close does not ban trading near the close outright. Legitimate traders execute billions of dollars in equity transactions in the final hour every day. The rule targets trades executed *with the intent* to move the closing price. The regulator need not prove that the trade actually moved the price—only that the trader intended to move it.

The rule applies across all venues: stock exchanges, [alternative trading systems](/alternative-trading-system/), and [over-the-counter](/over-the-counter-market/) markets. It covers the regular [market close](/), [after-hours](/), and [pre-market](//) trading windows. It catches traders buying or selling for their own account, traders executing on behalf of clients (if the client conspires with the trader), and [broker-dealers](/broker/) that facilitate such trades while aware of the intent.

Enforcement cases have named proprietary traders, hedge funds, and even major financial institutions. In 2012, the SEC charged [Barclays](//) with manipulative trading in the final seconds of days when major stock indices were rebalancing. In 2015, [Deutsche Bank](//) admitted to a smaller variant of the scheme. The cumulative effect is to deter most obvious marking-the-close schemes, though regulators continue to investigate traders and algorithms suspected of doing it subtly.

## How traders attempt to mark the close

The mechanics vary. A trader might accumulate a large position during the day at relatively low prices, then execute a wave of large orders in the final 30 seconds of the close. If the trader owns 500,000 shares, the orders create a buying frenzy that pushes the last print higher. The trader's cumulative position is now marked higher on the books, and—if the trader is a fund manager—the fund's net asset value climbs, which may trigger redemptions from new investors or bonuses for the manager.

Alternatively, a trader might layer orders on one side of the book (buying), then cancel them if they don't execute, replicating the tactic a few times until a few orders finally transact in the closing moments. The sequence of cancellations and fills mimics natural market activity but with the intent to move price.

Some traders use affiliated entities: a trader parks a position in one account, then has another account execute the marking-the-close trade, making it harder for regulators to connect the intent. Others exploit the fact that index [rebalancing](//) occurs at the close; if a trader knows that a major index will add a stock at the close, the trader can buy ahead of the algorithmic demand and exit on the rebalancing wave, pocketing the mark-up.

## Detecting marking the close: data and burden

The SEC and [FINRA](//) rely on post-trade data and surveillance algorithms to catch marking the close. They examine order timestamps, execution prices, order sizes, and cancellation patterns in the final minutes. An algorithm might flag a trader who executes 50,000 shares on every trading day at 3:59:55 p.m., always in the same direction, always pushing price. Investigators then examine blotters and emails to establish intent.

The challenge is distinguishing genuine market activity from manipulation. A hedge fund with a large equity position that wants to rebalance before month-end may legitimately execute in the final hour. A mutual fund tracking an index must execute close to the close to minimize tracking error. The rule requires that intent be shown, and intent often lives in email or verbal communication. Successful enforcement cases typically involve written records ("front the close," "paint the tape," "mark up the book") or testimony from co-conspirators.

## Impact on closing auctions and market structure

The rule has shaped how exchanges handle the closing auction. Rather than a single "trade-at-the-close" transaction, many brokers now place orders in a randomized closing auction so that no single large order dominates the final price. The NYSE and NASDAQ both randomize the closing auction within a few seconds to make it harder for a single trader to move the close with precision.

Market fragmentation has also complicated enforcement. With [alternative trading systems](/alternative-trading-system/) capturing roughly 25–30% of US equity volume, a trader marking the close on a dark pool might sidestep the most visible exchanges' closing auction protections. The SEC has tightened rules on dark pool operators to report suspicious activity, but the burden of surveillance is immense.

## Penalties and deterrence

SEC enforcement actions against marking the close typically result in disgorgement (return of ill-gotten gains), civil penalties, and, in egregious cases, criminal referrals to the Department of Justice. Individuals have faced prison sentences. The SEC also pursues [cease-and-desist](//) orders, suspensions of trading privileges, and bars from the industry.

Despite penalties, marking the close persists because the reward can be large and the risk of detection remains modest if the trader is careful. Regulators audit a small fraction of all trades. The most sophisticated marking-the-close schemes are subtle, embedding the manipulation in ordinary-looking order flow. As algorithms grow faster and more complex, the cat-and-mouse game between traders and regulators intensifies.

## See also

<div class="wiki-seealso">

### Closely related

- [Market Maker](/market-maker-trading/) — professional traders who shape closing prices and may be targets of manipulation schemes
- [Alternative Trading System](/alternative-trading-system/) — off-exchange venues where marking the close may be harder to detect
- [Over-the-Counter Market](/over-the-counter-market/) — bilateral trading where close manipulation can occur without exchange oversight
- [Algorithmic Trading](/algorithmic-trading/) — automated strategies that may execute close-marking logic at high speed
- [Large Trader Reporting](/large-trader-reporting/) — SEC rule providing surveillance data used to catch marking the close

### Wider context

- [Securities Exchange Act](//) — foundational law granting the SEC antifraud authority
- [Price Discovery](/price-discovery/) — mechanism that marking the close distorts
- [Stock Exchange](/stock-exchange/) — institution whose closing auction the rule protects
- [Market Manipulation](//) — broader category of illegal trading practices of which marking the close is one type

</div>
