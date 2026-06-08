---
title: "Limit Up Limit Down Rule Explained"
description: "How the LULD price-band mechanism halts trading in individual stocks when prices move too fast, distinct from market-wide circuit breakers."
keywords:
  - limit up limit down rule
  - luld trading halt
  - stock price limits
  - circuit breaker rules
  - trading halts individual stocks
image: "/svg/markets.svg"
---

*The **Limit Up Limit Down (LULD)** rule is a circuit-breaker mechanism that pauses trading in a single stock or [ETF](/etf/) when its price moves more than a certain percentage in a short period—usually five minutes. Unlike market-wide circuit breakers that shut down the entire stock market when the [S&P 500 index](/sp-500-index/) falls by 7%, 13%, or 20%, LULD operates at the security level to prevent wild price swings driven by algorithmic trades, data errors, or liquidity shocks in individual names. When a stock hits its limit-up or limit-down band, trading is halted for a brief period—typically 15 seconds—to allow prices to stabilize and investors to respond.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Limit Up Limit Down — key facts</div>

<img src="/svg/markets.svg" alt="An abstract editorial mark for market structures." />

<div class="wiki-infobox-caption">A price circuit-breaker for individual securities, not the whole market.</div>

|   |   |
|---|---|
| **Triggered by** | Price move of 5% or 10% in 5 minutes (varies by price tier) |
| **Securities covered** | Stocks and [ETFs](/etf/) listed on U.S. exchanges |
| **Halt duration** | 15 seconds (or until 4:00 pm if triggered in final minute of trading) |
| **Who enforces** | [FINRA](/finra/), [SEC](/securities-and-exchange-commission/), and exchange operators |
| **How it differs** | LULD halts one stock; market-wide circuit breakers halt all trading |
| **Implemented** | April 2013, after the "flash crash" of 2010 |

</aside>

## The 2010 Flash Crash and Birth of LULD

On May 6, 2010, the U.S. stock market fell roughly 9% in minutes, then recovered almost entirely within an hour. The [S&P 500 index](/sp-500-index/) dropped 600 points. Some stocks traded at a penny, others at 100 times their true value. A mutual fund that owned equities lost billions in mark-to-market losses in a few seconds. Then everything snapped back. No one was entirely certain what had caused the chaos, but the prevailing theory involved a large [mutual fund](/mutual-fund/) seller hitting the market, followed by a cascade of algorithmic sell orders that overwhelmed the market's ability to absorb the selling pressure.

The flash crash revealed a gap in market protection. Existing circuit breakers were designed to halt the entire market if prices fell too far too fast. But individual stocks could plummet or spike with no protection. Traders executed orders at absurd prices—paying a dollar for a stock that normally traded for $20, or selling for a penny a stock worth much more. The [Securities and Exchange Commission](/securities-and-exchange-commission/) and [FINRA](/finra/) concluded that individual securities needed their own circuit breakers to prevent such anomalies.

The result was LULD, implemented in April 2013. For the first time, if a single stock moved too far too fast, trading in that stock would halt automatically, giving [market participants](/stock-exchange/) a chance to catch their breath and reassess.

## How LULD Bands Work

LULD prices are set using an algorithm based on the stock's recent trading volatility and price level. The bands are widest during periods of known high volatility (such as the first 15 minutes of the trading day, when large orders hit the market) and narrower during calmer times. In general, bands widen as stock prices fall—a $1 stock has a wider percentage band than a $100 stock, because lower-priced stocks are naturally more volatile.

For most stocks trading between $3 and $1,000, the typical LULD band is 5% during most of the day and 10% at the open and close. This means if a stock is trading at $50, a move to $52.50 or $47.50 would trigger a halt. Some stocks, particularly those deemed highly volatile or prone to gaps (such as recent IPOs or biotech names with binary events), may have wider bands. Conversely, liquid, stable stocks may have tighter bands.

The five-minute window is key. LULD is not triggered by any single trade at an off-market price. Rather, the last sale price (the price of the most recent trade) must move 5% from a rolling reference price over a five-minute window. This rolling reference is called the "maximum price level" or "average reference price." It is recalculated continuously, so the band moves with the market.

## When LULD Halts Trading

When a stock's last sale price breaches the upper or lower LULD band, an automatic halt is triggered. The stock stops trading on all U.S. exchanges and all alternative trading systems simultaneously. For 15 seconds, no transactions can occur. This gives buyers and sellers a moment to reassess. News sites update, traders check their screens, and market makers recognize the halt.

After 15 seconds, the trading halt lifts and the stock reopens. Often, an imbalance of buy or sell orders has accumulated during the halt. When the stock reopens, the opening price may jump or drop to clear that imbalance. If the imbalance is one-sided (say, millions more shares to buy than to sell at current prices), the opening price may move up sharply. If the rush continues in the same direction and immediately hits the LULD band again, another halt triggers.

This can create a staircase of halts. A stock that is crashing due to a major news event might halt multiple times on the way down, with each halt lasting 15 seconds and each reopening jumping to a new lower price as buyers withdraw. The effect is to slow the crash, not to stop it—but the slowness allows human traders and portfolio managers to respond, rather than executing large positions at absurd prices automatically.

## LULD vs. Market-Wide Circuit Breakers

It is critical to distinguish LULD from the market-wide circuit breakers that govern the [S&P 500 index](/sp-500-index/). Circuit breakers halt the entire market if it falls 7%, 13%, or 20% in a single trading day. LULD halts individual securities when they move 5–10% in five minutes.

The two systems operate independently. A stock could be halted by LULD every few minutes if it is highly volatile, yet the overall market could be trading normally. Conversely, the market could be in free fall, triggering a circuit breaker that halts all trading, without LULD being relevant. In practice, circuit breaker halts are rare—the last one occurred in 2020 during the COVID-19 market panic. LULD halts, by contrast, happen multiple times per day across the market. On any given day, a few stocks somewhere will hit LULD due to earnings surprises, acquisitions, or data-driven selling.

## The Role of Algorithmic Trading

LULD was designed partly to protect against algorithmic malfunction. When a computer program is coded to sell if a price crosses a threshold, and that threshold is reached for a moment due to a data error or a liquidity squeeze, the algorithm can execute a huge block of shares before human traders even know what is happening. If that sale hits the market, it can trigger other algorithms to sell, creating a cascade.

A 15-second halt breaks that cascade. By stopping trading, LULD gives human traders a chance to recognize the anomaly and step in, or it gives the exchange a chance to cancel erroneous trades (known as trade-throughs). A stock that would have crashed 30% in one minute might instead take five minutes to fall 15% over a series of halts, giving market participants time to adjust.

This is particularly important for [passive funds](/index-fund/) and algorithms that do not monitor price in real time but rely on end-of-day prices or scheduled rebalances. An unhalted flash crash in a single stock could cause a fund to be liquidated or a portfolio to be marked at a loss based on a price that lasted a second. LULD prevents that outcome.

## The Experience of a LULD Halt

For a trader managing a position, a LULD halt is frustrating but generally protective. If you are trying to sell a stock and it halts, your sell order is stuck in the queue. You cannot panic-sell at a lower price during the halt, but also, you cannot execute any sales at that moment. When the stock reopens 15 seconds later, the price might be lower (if the seller-initiated halt was driven by forced selling), or it might be higher (if the halt allowed buy-side demand to accumulate).

For a large [mutual fund](/mutual-fund/) rebalancing, a LULD halt can be annoying because it slows execution. But it is generally viewed as a small cost for protection against flash crashes. The alternative—allowing a stock to fall 50% in five seconds due to an algorithm malfunction—is much worse.

For a high-frequency trading firm or a market maker, LULD introduces unpredictability. They cannot assume that a price move will be smooth or continuous. But they can build LULD into their models and adjust their strategies accordingly.

## The Broader Market Structure

LULD is part of a larger regulatory framework built after 2008 and refined after 2010. The [Securities and Exchange Commission](/securities-and-exchange-commission/) and [FINRA](/finra/) also require market makers to post firm bids and offers (not just indicative prices), and they regulate [margin](/leverage-ratio-forex/) requirements to limit the risk that forced liquidations will cause cascades. Market-wide circuit breakers, exchange-level circuit breakers (which are tighter than market-wide ones), and now LULD form layers of protection.

Debate continues about whether these layers are sufficient. Critics argue that LULD halts can themselves create volatility, as traders rush to exit positions before a halt, knowing the halt will prevent them from selling during the pause. Supporters note that flash crashes have not recurred since LULD was implemented, and that the brief pauses have likely prevented billions in misdirected algorithmic trades.

## See also

<div class="wiki-seealso">

### Closely related

- [Market Maker Trading](/market-maker-trading/) — the dealers managing quotes during halts
- [Algorithmic Trading](/algorithmic-trading/) — the trading methods LULD was designed to contain
- [Price Discovery](/price-discovery/) — how prices find equilibrium during volatile moments
- [ETF](/etf/) — exchange-traded funds subject to LULD
- [Execution Risk](/execution-risk/) — why traders cannot always execute at intended prices
- [FINRA](/finra/) — the regulator enforcing LULD alongside the SEC

### Wider context

- [Stock Market](/stock-market/) — the broader exchange where LULD operates
- [Securities and Exchange Commission](/securities-and-exchange-commission/) — the federal regulator setting LULD policy
- Flash Crash of 2010 — the event that prompted LULD's creation
- [Systemic Risk](/systemic-risk/) — why circuit breakers exist at all levels

</div>
