---
title: "Short-Sale Circuit Breaker"
description: "An alternative uptick rule that restricts short selling for two days when a stock price drops 10 percent or more intraday."
keywords:
  - short sale restriction
  - circuit breaker
  - uptick rule
  - short selling regulation
  - trading halts
  - price decline threshold
image: "/svg/regulation.svg"
---

*The **short-sale circuit breaker** is a regulatory mechanism that automatically restricts [short selling](/short-selling/) on a security when its price falls 10 percent or more from the previous day's closing price. Once triggered, a modified uptick rule applies for the remainder of that day and the next trading day, requiring short sales to occur only on an uptick (at a price higher than the last transaction price) or on a zero-plus uptick.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Short-Sale Circuit Breaker — key facts</div>

<img src="/svg/regulation.svg" alt="An abstract editorial mark for regulation." />

<div class="wiki-infobox-caption">Automatic restriction triggered by a 10 percent single-day decline.</div>

|   |   |
|---|---|
| **What it is** | Temporary ban on short sales except on upticks during sharp declines |
| **Trigger** | Stock price falls 10% or more from prior close |
| **Duration** | Rest of trigger day plus next trading day |
| **Rule basis** | Regulation SHO, Rule 10a-1 (alternative uptick rule) |
| **Enforced by** | SEC, SROs (exchanges and FINRA) |
| **Exemptions** | Certain hedging activities and market-maker functions |

</aside>

## The mechanics of the rule

The circuit breaker activates automatically when a security's price declines 10 percent or more from the previous day's closing price. This threshold is checked once per day, typically at the open or during the first hours of trading. When the trigger is hit, a modified version of the uptick rule springs into effect immediately.

Under this modified rule, short sellers may only execute sales at a price higher than the last sale price (an "uptick") or at the same price if the last change in price was itself an uptick ("zero-plus uptick"). This contrasts with normal trading, where short sales can occur at any price. The restriction remains in effect for the remainder of the day on which it is triggered, and for the entire next trading day. It then expires automatically at the market close on the second day.

The rule applies only to short sales; long sales and all purchases are unaffected. Certain exemptions exist for transactions by market makers and for bona fide hedging (such as a shareholder shorting to hedge a long position in derivatives on the same stock). However, these exemptions are narrowly construed and require pre-notification to the exchange in some cases.

## Historical roots and the 2008 reform

The original uptick rule, adopted in 1938, required all short sales to occur on an uptick. However, in 2007, the SEC repealed it, finding no clear evidence that it prevented manipulation. When the financial crisis erupted in 2008, critics argued that removing the uptick rule enabled short sellers to accelerate the collapse of major financial institutions.

In response, the SEC adopted the alternative uptick rule and the circuit-breaker version in July 2010 as part of Regulation SHO. The new rule was designed to provide circuit-breaker protection during extreme volatility without the broad restrictions of the original rule.

## Policy rationale

The circuit breaker aims to prevent cascading declines driven by short-sale pressure during panic or stress. If prices fall sharply, an unrestricted ability to short at any price can create a feedback loop: shorts push prices down, triggering more shorts, which push prices down further. The uptick requirement disrupts this loop by forcing shorts to wait for a price recovery before they can sell.

Not all economists agree that the rule achieves its goals. Some studies find minimal impact on price dynamics, because short sellers can simply wait for an uptick. Others argue that dampening short selling may reduce price discovery by preventing the market from testing lower support levels.

## Interaction with other circuit breakers

The short-sale circuit breaker is part of a broader suite of trading halts and circuit breakers. Exchanges also implement individual stock halts when volatility or order imbalances become extreme. Market-wide circuit breakers (sometimes called "curbs") halt all trading on major exchanges if the S&P 500 falls 7 percent, 13 percent, or 20 percent from the previous day's close. These operate independently of the short-sale rule and serve a similar purpose: to reduce panic and create breathing room for the market.

The interaction between these mechanisms can be complex. A stock might be subject to the short-sale circuit breaker (10 percent down) while the broader market is not in a halt (less than 7 percent down). Conversely, a market-wide circuit breaker would apply to all stocks, including those where the short-sale rule is active. Traders and brokers must track multiple regulatory constraints simultaneously.

## Effectiveness and debate

Empirical research on the short-sale circuit breaker's effectiveness is mixed. Some studies find that short-sale restrictions reduce volatility during market stress, while others find no statistically significant effect. The challenge is that few large, sharp declines occur, so there are limited data points from which to draw conclusions.

Proponents of the rule note that the financial system has been more stable since its adoption (the rule was adopted in 2010, after the worst of the crisis). Sceptics respond that this post hoc argument conflates correlation with causation; the stability may be due to stronger bank capital requirements, quantitative easing, or lower interest rates, not the circuit breaker rule.

One empirical finding is fairly robust: the rule does slow trading velocity during the trigger period. Fewer short sales occur, and order flow is less aggressive. Whether this slowdown is beneficial (because it reduces panic) or harmful (because it reduces liquidity) depends on one's view of market microstructure and the role of short selling in price discovery.

## Regulatory oversight and evolution

The SEC periodically reviews the circuit-breaker rule and has considered raising or lowering the 10 percent threshold, shortening or lengthening the duration, or applying it selectively to certain asset classes or market conditions. International regulators have adopted similar rules; the European Union and many other jurisdictions have their own short-sale restrictions triggered by price declines.

Brokers are required to monitor their order flow and prevent non-exempt short sales during the restriction period. Violations can result in fines and regulatory discipline. Compliance systems at most brokers automatically reject or mark short orders as ineligible if the stock is in a circuit-breaker halt.

The rule remains one of the more contentious post-crisis regulations, with no clear consensus on whether its benefits outweigh its costs. However, it is unlikely to be repealed in the near term, given political support for short-sale restrictions and the absence of compelling evidence that it causes material harm to market function.

## See also

<div class="wiki-seealso">

### Closely related

- [Short Selling](/short-selling/) — practice that the circuit breaker regulates during price declines
- [Market Manipulation Prohibition](/market-manipulation-prohibition/) — broader regulatory framework of which the circuit breaker is a part
- [Regulation SHO](/regulation-sho/) — comprehensive short-sale regulation including the circuit breaker
- [Settlement Finality Rules](/settlement-finality-rules/) — ensures short positions, once settled, become irrevocable
- [Securities and Exchange Commission](/securities-and-exchange-commission/) — regulator that adopted and oversees the rule
- [T+1 Settlement](/t-plus-one-settlement/) — faster settlement cycle that interacts with short-sale timing

### Wider context

- [Stock Exchange](/stock-exchange/) — venue where circuit breakers are enforced
- [Market Risk](/market-risk/) — broader category of risks the rule aims to mitigate
- [Volatility Smile](/volatility-smile/) — changes in volatility during stress periods
- [Stock Market](/stock-market/) — system of which the circuit breaker is a regulatory component
- [Business Cycle](/business-cycle/) — economic context in which regulatory restrictions become politically necessary

</div>
