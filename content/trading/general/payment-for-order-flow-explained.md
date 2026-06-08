---
title: "Payment for Order Flow Explained"
description: "How brokers earn revenue by selling retail orders to market makers, why it's controversial, and what it means for the prices retail traders receive."
keywords:
  - payment for order flow explained
  - order flow monetization
  - market maker revenue
  - retail order routing
  - execution quality
  - broker-dealer revenue
image: "/svg/trading.svg"
---

*When you place a buy or sell order through a retail broker, that order is extremely valuable—not to you, but to the broker. Many brokers now earn a substantial portion of their revenue by selling your order flow to **market makers**, who will execute the trade. This practice, called **payment for order flow (PFOF)**, is legal and ubiquitous, but it raises a fundamental question: if your broker is paid to send your order to a specific market maker, is your trade being executed at the best available price?*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Payment for Order Flow — key facts</div>

<img src="/svg/trading.svg" alt="An abstract editorial mark for trading mechanics." />

<div class="wiki-infobox-caption">A revenue model that upends the traditional broker-customer relationship.</div>

|   |   |
|---|---|
| **What it is** | Broker receives cash for routing orders to [market makers](/market-maker-trading/) |
| **Who benefits** | Brokers (direct revenue); market makers (flow to trade) |
| **Who may suffer** | Retail traders (wider [spreads](/bid-ask-spread/), worse execution) |
| **Typical payment** | Fractions of a cent per share; varies by order type |
| **Regulation** | SEC [Regulation SHO](/broker/); [FINRA](/finra/) oversight |
| **Disclosure** | Brokers must disclose routing practices quarterly to SEC |

</aside>

## Why brokers sell order flow

Retail brokers face a business-model puzzle. For decades, they earned revenue primarily from commissions—you paid $10 per trade, the broker kept it. Then, starting in the late 1990s, competition drove commissions to zero. Interactive Brokers, E-Trade, and others eliminated trading fees to attract customers. Today, nearly all retail brokers offer free stock and ETF trades.

If there are no commissions, how do brokers make money? The answer is order flow. A market maker will pay a broker a small amount—typically 0.001 to 0.005 dollars per share—for the right to execute that order. If you buy 100 shares of Apple at zero commission, Broker A receives perhaps $0.10 to $0.50 from the market maker who fills your order. Multiply that across millions of retail orders daily, and the revenue is substantial. A broker routing 100 million shares daily might earn hundreds of thousands of dollars.

From the broker's perspective, PFOF is a clean solution: the customer gets commission-free trading, and the broker monetizes the valuable order flow. From the market maker's perspective, retail order flow is desirable because it is typically small, non-toxic (retail orders don't have the signaling problems of large institutional orders), and predictable in direction (retail investors often buy into strength, sell into weakness). The market maker profits by offering slightly worse prices than they would for institutional orders, capturing the difference.

## The execution quality question

Here lies the controversy. If your broker has an incentive to route your order to Market Maker X (because X pays more), but Market Maker Y would give you a better price, your broker faces a conflict of interest. Regulators require brokers to route orders at "best execution"—defined broadly as achieving the most favorable overall terms, considering price, speed, size, and nature of execution. But "best execution" has proven ambiguous in practice.

The [SEC](/securities-and-exchange-commission/) and academic research have measured the impact of PFOF on retail traders. For a typical small order in a liquid stock, the effect may be negligible—a penny or two per share isn't perceptible. But for:

- Large retail orders
- Thinly traded stocks
- Illiquid options
- Times of high volatility

The gap between the market maker's [bid-ask spread](/bid-ask-spread/) and the broader market's spread can be meaningful. A retail trader buying 1,000 shares at a half-cent worse price than the mid-quote loses $5 on the trade—small in isolation, but significant if repeated.

The key tension: a broker can argue that [market makers](/market-maker-trading/) provide immediate execution and narrow spreads precisely because they earn PFOF revenue. Without PFOF, market makers wouldn't service retail orders, and retail traders would face wider spreads and slower execution in the open market. The SEC has grappled with this counterfactual. Some economists argue PFOF is net-positive for retail traders (better than the alternative). Others argue it is rent extraction, tilting execution quality in favor of broker profit.

## How much are you losing?

The answer depends on your trading pattern:

- **Long-term buy-and-hold investors**: PFOF likely has minimal impact. The spread you pay on entry is tiny relative to your holding period and return.
- **Day traders or high-frequency retail traders**: You may be paying 1–5 cents per share in execution leakage cumulatively, if your broker routes to a paying market maker with poor price improvement.
- **Options traders**: Leakage can be larger because bid-ask spreads in options are wider and PFOF incentives are stronger.

A trade with a 0.5-cent spread vs. a 1-cent spread in a 1,000-share order is a $5 difference. Over 100 trades, that's $500. Most retail traders don't quantify this, so PFOF's real cost is invisible.

## Regulatory scrutiny and alternatives

PFOF has drawn sustained scrutiny from regulators and lawmakers. In 2021–2023, proposals emerged to ban it outright or restrict it to "non-toxic" venues where transparency is high. The argument from critics is simple: if a broker's profit incentive is divorced from your profit, the structure is suspect. Some brokers, like Fidelity and others, have chosen to absorb order flow costs and route to venues that offer the best public prices, advertising this as a differentiator.

The counter-argument from PFOF defenders—and some brokers rely on this revenue—is that it subsidizes commission-free trading. If PFOF were banned, brokers might reintroduce fees or offer fewer services.

In practice, the SEC has required brokers to **disclose** where they route orders and the payments they receive quarterly. This transparency is imperfect but at least allows sophisticated investors to audit routing practices. Most retail traders, however, don't examine these filings.

## How to mitigate PFOF impact

If you want to minimize PFOF friction:

- **Route to lit markets directly**: Use a broker that routes to public exchanges ([NYSE](/new-york-stock-exchange/), [NASDAQ](/nasdaq/)) and publishes execution benchmarks.
- **Avoid options**: Bid-ask spreads are wider, and PFOF incentives are stronger, so leakage is more visible.
- **Trade liquid, large-cap stocks**: The spread between market makers is thin, so PFOF can't hide much.
- **Avoid trading on news or high-volatility days**: This is when spreads widen and PFOF can cause larger execution slippage.
- **Use limit orders**: This gives you transparency on the price you'll accept, reducing execution ambiguity.

## See also

<div class="wiki-seealso">

### Closely related

- [Market Maker](/market-maker-trading/) — The entity earning PFOF
- [Bid-Ask Spread](/bid-ask-spread/) — How PFOF impacts pricing
- [Broker](/broker/) — The intermediary profiting from order flow
- [Execution Risk](/execution-risk/) — The broader class of risks PFOF exemplifies
- [Regulation SHO](/broker/) — SEC rules governing order routing

### Wider context

- [Securities and Exchange Commission](/securities-and-exchange-commission/) — Regulator of PFOF
- [FINRA](/finra/) — Self-regulatory body overseeing broker practices
- [Liquidity Risk](/liquidity-risk/) — The supply-side effect of PFOF concentration
- [Market Order](/market-order/) — The trade type most affected by PFOF

</div>
