---
title: "Bid-Ask Spread in Illiquid Stocks"
description: "Why bid-ask spreads widen dramatically for thinly traded stocks and how to estimate the true round-trip cost before placing a trade."
keywords:
  - bid ask spread illiquid stocks
  - illiquidity trading cost
  - thin stock spread
  - market microstructure
  - trading liquidity
---

*In illiquid stocks, the **bid-ask spread**—the difference between the highest price a buyer will pay and the lowest price a seller will accept—widens dramatically compared to liquid large-cap stocks. A [liquid](/liquidity-risk/) stock might trade with a 1-cent spread, while a thinly traded stock might face a 50-cent or wider spread. These spreads represent a hidden cost that can turn a modest expected return into a net loss.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Bid-Ask Spread in Illiquid Stocks — key facts</div>

<img src="/svg/trading.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">The market microstructure cost of trading small-cap and thinly traded securities, often exceeding commissions and slippage combined.</div>

|   |   |
|---|---|
| **Typical spread: large-cap** | 1–2 cents (0.01%–0.02% of price) |
| **Typical spread: small-cap** | 5–50 cents (0.1%–1.0% of price) |
| **Extreme spreads** | $1–$5+ on very thinly traded stocks or micro-caps |
| **Round-trip cost** | Buy at ask, sell at bid = 2× the spread as a percentage of investment |
| **Primary driver** | Dealer risk and inventory holding; low trading volume |
| **Secondary drivers** | Volatility, news events, after-hours trading |
| **Mitigation** | Limit orders, patient trading, market-on-open/close orders |

</aside>

## Why spreads widen for illiquid stocks

The [bid-ask spread](/bid-ask-spread/) exists because market makers and dealers face risk when they hold inventory. When you place a [market order](/market-order/) to buy 1,000 shares of a thinly traded stock, a dealer steps in and sells those shares to you at the asking price. The dealer now owns the other side: they are short the stock. If the stock falls before the dealer can sell those shares to another buyer, the dealer loses money. To compensate for this risk, dealers build a cushion into their prices.

For liquid stocks like Apple or Microsoft, where thousands of shares trade per second, a dealer can unwind inventory almost instantly at minimal risk. The bid-ask spread might be just 1 cent. For a thinly traded small-cap stock, where the entire daily volume might be only 5,000 shares and price discovery is difficult, the dealer faces much higher risk. They might widen the spread to 50 cents or more to protect themselves.

This dynamic is called **adverse selection risk**. The dealer worries that if someone is trying to sell a large block of an illiquid stock, it might be because the seller has unfavorable information—the stock is about to drop in price. To protect against this risk, dealers offer lower prices to sellers and demand higher prices from buyers, widening the spread.

## How spreads vary by trading volume and volatility

The relationship between trading volume and spread is nearly linear on a [log scale](https://en.wikipedia.org/wiki/Logarithmic_scale). The top 100 most-traded US stocks have spreads under 5 cents. Stocks trading 1,000 shares per day might have spreads of 25–50 cents. Stocks trading a few hundred shares per day might face spreads exceeding $1.

**Volatility** amplifies this effect. A thinly traded biotech stock with high [implied volatility](/implied-volatility/) (due to pending FDA approval, for example) might have a spread two or three times wider than a thinly traded utility stock with stable cash flows. The dealer is compensating for the risk that the stock will gap against their position before they can exit.

**Time of day** also matters. Spreads are tightest during the open (9:30 AM Eastern), when volume is highest. They widen during lunch hours and are often very wide in after-hours trading (4 PM–8 PM and pre-market 7 AM–9:30 AM), when volume evaporates and dealers are cautious about holding overnight risk.

## Calculating the true round-trip cost

To understand the hidden cost of trading illiquid stocks, imagine you buy 500 shares of a thinly traded stock with a bid-ask spread of $0.50:

- **Current bid**: $10.00 (what you can sell for now)
- **Current ask**: $10.50 (what you must pay to buy now)
- **Spread**: $0.50 (5% of the mid-price of $10.25)

You place a [market order](/market-order/) to buy 500 shares. You pay the ask price: 500 × $10.50 = $5,250.

A few hours later, you decide to exit. The stock has not moved; the bid and ask are still $10.00 and $10.50. You place a market sell order. You receive the bid price: 500 × $10.00 = $5,000.

**Your loss**: $5,250 − $5,000 = $250, or roughly 4.8% of your investment, entirely due to the bid-ask spread (ignoring commissions). This is your **round-trip cost**. 

The formula is simple:

**Round-trip cost (%) = (Ask − Bid) / Mid-price × 200%**

In this example: ($10.50 − $10.00) / $10.25 × 200% ≈ 9.8%, which reflects both the buy and sell legs.

For a large-cap stock with a $0.01 spread on a $150 stock:

**Round-trip cost (%) = $0.01 / $150 × 200% ≈ 0.013%**

The difference is staggering: 9.8% vs. 0.013%. Over a one-year holding period, the illiquid stock must outperform the liquid stock by roughly 9.8% just to break even on trading costs alone.

## Impact on portfolio returns

For buy-and-hold investors in illiquid stocks, a single bid-ask spread cost is manageable—it is a one-time friction. But for active traders, spreads compound quickly.

Consider a day trader in an illiquid micro-cap stock. If they execute 10 round-trip trades per day with an average spread cost of 2%, they accumulate 20% in annual spread costs just from market impact. Add in any price appreciation they expect, and the math becomes unforgiving.

For institutional investors who must build or unwind large positions in illiquid stocks, the situation is worse. Buying 50,000 shares of a thinly traded stock over several days may move prices significantly—not just the bid-ask spread, but also deeper-order-book slippage. The total cost can easily exceed 5–10% of the position.

## Strategies to minimize spread costs

**1. Use limit orders instead of market orders.** A [limit order](/limit-order/) specifies a maximum buy price or minimum sell price. You may not execute immediately, but you avoid paying the ask price on a buy or accepting the bid price on a sell. Patience is rewarded: if you are willing to wait a few minutes or hours, the stock may trade at your limit price.

**2. Trade during peak volume times.** Execute orders during the open (first 30 minutes) and early afternoon, when volume is highest and spreads are tightest.

**3. Split large orders into smaller tranches.** Instead of buying 10,000 shares in one market order, buy 1,000 shares at a time over several minutes or hours. Smaller orders draw less dealer caution.

**4. Use algorithmic execution.** Institutional traders use algorithms that track the order book, execute in small increments, and adjust for order imbalance. These can reduce effective spreads on large orders by 20–30% compared to naive market orders.

**5. Consider pre-market or after-hours trading with caution.** Spreads are wider, but volume is lower—you may find your exact order price if you are very patient.

**6. Check multiple venues.** If a stock trades on multiple exchanges, bid-ask spreads may differ. Some market data terminals allow traders to see all bids and asks across venues and route to the tightest spread.

## The relationship between spread and expected return

A fundamental principle: **illiquidity is a cost that must be offset by higher expected returns.** An illiquid stock is less desirable than a liquid stock with identical fundamentals, because investors face real costs to enter and exit positions.

For long-term value investors, this translates into a discount: illiquid stocks must trade at lower valuations (higher [price-to-earnings ratios](/price-to-earnings-ratio/) are riskier; lower [dividend yields](/dividend-yield/) are less attractive). For traders, the spread is a drag on [alpha](/alpha/). A strategy that generates 3% annual alpha in liquid large-caps may generate negative alpha in illiquid micro-caps, because the spread eats the excess return.

Sophisticated investors use this principle to their advantage: they may deliberately focus on illiquid securities where spreads are wide but fundamental value is clear. By being patient and executing smartly, they capture the liquidity discount as an investment return.

## Corporate actions and spread changes

Spreads can widen suddenly during corporate events. If a company announces earnings, an acquisition, or a major lawsuit, [volatility](/historical-volatility/) spikes and dealers widen spreads to protect inventory. Similarly, if a company undergoes a reverse split, consolidates, or is delisted from a major exchange, liquidity often evaporates and spreads can widen five-fold or more.

For traders in illiquid stocks, staying aware of event calendars is critical. Exiting a position before an earnings announcement or news event, even at a less favorable price, may be cheaper than waiting and facing a much wider spread post-announcement.

## The limits of market makers

Finally, it is worth noting that market makers have limits to their willingness to provide liquidity. In true crises—market panics, regulatory halts, or systematic sell-offs—even the bid-ask spread disappears because the market freezes entirely. No spread can get wider than infinity. The lesson: illiquidity is not just the spread; it is the risk that trading becomes impossible when you most need to exit.

## See also

<div class="wiki-seealso">

### Closely related

- [Bid-Ask Spread](/bid-ask-spread/) — the fundamental concept
- [Market Order](/market-order/) — immediate execution at ask or bid
- [Limit Order](/limit-order/) — patient execution at a specified price
- [Liquidity Risk](/liquidity-risk/) — broader concept of trading difficulty
- [Market Maker Trading](/market-maker-trading/) — how dealers set spreads
- [Price Discovery](/price-discovery/) — how spreads affect valuation

### Wider context

- [Over-the-Counter Market](/over-the-counter-market/) — venue for illiquid securities
- [Stock Exchange](/stock-exchange/) — venue for listed, typically more liquid stocks
- [Volatility](/historical-volatility/) — driver of spread widening
- [Cost of Equity](/cost-of-equity/) — how liquidity discount affects valuation
- [Alpha](/alpha/) — trading returns after accounting for spread costs
- [Slippage](/bid-ask-spread/) — related trading friction

</div>
