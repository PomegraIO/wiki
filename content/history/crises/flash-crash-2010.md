---
title: "Flash Crash (2010)"
description: "Market plunge and rapid recovery on May 6, 2010, exposing algorithmic trading risks and market structure vulnerabilities."
keywords:
  - flash crash
  - May 6 2010
  - algorithmic trading
  - market circuit breakers
  - trading halts
---

*The Flash Crash of May 6, 2010, was a sudden, severe market decline and rapid recovery that occurred in less than an hour on U.S. stock markets. The S&P 500 fell roughly 9% intraday before recovering, and billions in trading volume evaporated in minutes. The event exposed the risks of algorithmic trading, gaps in market microstructure, and cascading interactions between futures, equities, and electronic trading systems.*

<aside class="wiki-infobox">

| Item | Details |
|------|---------|
| **Date** | May 6, 2010 |
| **Duration** | ~36 minutes (peak to trough) |
| **Peak decline** | S&P 500 dropped ~998 points intraday (9%) |
| **Recovery** | Recovered most losses within minutes |
| **Volatility** | VIX spiked; bid-ask spreads blew out |
| **Lessons** | Exposure of systematic risks in market design |

</aside>

## The May 6 timeline

Markets opened normally on May 6, 2010. Overnight, the [Greek debt crisis](/wiki/greek-debt-crisis/) intensified; fears of sovereign default rippled through European markets. U.S. equity futures opened lower. Early morning saw selling pressure in cyclical stocks and financial sector names. By mid-morning, selling accelerated. [Volatility](/wiki/fear-index/) began to rise, triggering [stop-loss orders](/wiki/stop-order/) in equities.

Around 2:30 p.m., the decline turned into a rout. Trading volume exploded. Electronic sellers overwhelmed buyers. Prices on large-cap stocks fell several dollars per second. Some stocks traded at implausible levels—one stock dropped to 1 penny before rebounding to $40+. Buyers simply disappeared. [Bid-ask spreads](/wiki/bid-ask-spread/) widened to several dollars. The limit-up and limit-down rules that were supposed to slow trading had not yet been invented.

By 3 p.m., the market had recovered 80% of losses. By close, the S&P 500 was down only 3.4% for the day—steep, but not catastrophic. But the violent intraday action left a clear mark: markets were far more fragile than assumed.

## Algorithmic trading and cascading failures

Investigations revealed that the crash was triggered by a combination of factors. A large trader sought to [sell](/wiki/short-selling/) roughly 75,000 [E-mini S&P 500 futures](/wiki/commodity-futures-trading-commission/) contracts. Instead of using a gradual execution algorithm, they employed an algorithm that sold a fixed volume per unit time. This sale pressure hit the [futures market](/wiki/futures-contract/), which immediately moved lower.

At that price level, [index arbitrage](/wiki/triangular-arbitrage/) algorithms detected a mismatch. S&P 500 [futures](/wiki/futures-contract/) had fallen relative to cash equities. Their programmed response was to short stocks and buy futures, locking in the spread. This triggered massive sell orders in individual equities. Other algorithms—momentum followers and volatility-driven systems—detected the falling prices and moved to sell as well.

The cascade was mechanical. Each selling algorithm's action prompted another algorithm to react, creating a feedback loop with no natural circuit breaker. [Market makers](/wiki/market-makers/) stopped providing liquidity. Exchanges received "cancel" and "kill all orders" commands from trading firms, leaving one-sided markets. The market briefly entered a state of near-zero liquidity.

## Market structure fragmentation

Part of the problem was market fragmentation. U.S. equities trade on multiple venues: the [NYSE](/wiki/new-york-stock-exchange/), [NASDAQ](/wiki/nasdaq/), and numerous [electronic communication networks](/wiki/electronic-communication-network-market/). Prices on different venues lagged each other by milliseconds. An [arbitrage algorithm](/wiki/arbitrage-pricing-theory/) that noticed the lag would route orders to different venues simultaneously, but due to transmission delays, orders could arrive in unpredictable sequence, creating unintended positions.

The 2010 crisis also exposed the fragility of the [depository trust company](/wiki/depository-trust-company/) and clearing systems. When volume spiked, settlement capacity was strained. Large trades executed at absurd prices had to be unwound post-hoc, creating legal and financial disputes.

## Regulatory responses: circuit breakers and rule changes

After May 6, the SEC and exchanges implemented tighter [circuit breakers](/wiki/circuit-breaker/). Trading now halts if the S&P 500 falls 7% (level 1), 13% (level 2), or 20% (level 3) in a day. Additionally, single-stock circuit breakers halt trading if a stock moves 10% or more in five minutes. The SEC also imposed rules on order entry—algorithms must have kill-switches, and risk limits must be applied before orders hit the market.

[Limit-up and limit-down](/wiki/lock-limit-rules/) rules were introduced to prevent stocks from trading at implausible prices. The SEC also tightened messaging rules on electronic [communication networks](/wiki/alternative-trading-system/) to prevent cascading cancellations.

These measures have worked. No equivalent event has occurred since 2010, despite several near-misses during volatile periods (e.g., August 2015, March 2020). However, critics argue the fixes are band-aids; the underlying fragility—the reliance on [algorithms](/wiki/algorithmic-trading/) and the speed mismatch between human judgment and machine execution—remains.

## Lessons for market microstructure

The Flash Crash demonstrated that market resilience depends not just on participants' willingness to trade, but on the technical and regulatory infrastructure supporting trading. [High-frequency traders](/wiki/high-frequency-trading/) can provide liquidity in normal times but withdraw it instantly in stress. There is no market-making obligation when prices move against the market maker's interest.

The event also highlighted the danger of correlated selling across asset classes. Equities, [futures](/wiki/futures-contract/), and [options](/wiki/option/) markets are mechanically linked. A shock in one propagates to others through [arbitrage](/wiki/arbitrage-pricing-theory/) trades. Without proper circuit breakers, a small local disturbance can explode into systemic dislocation.

## Legacy and ongoing research

Academics continue to study May 6. Questions remain: Could a more severe shock trigger another crash, or have the safeguards truly made markets safer? Some researchers argue that the increase in passive investing and the concentration of holdings in ETFs has re-created clustering risks similar to 2010. Others note that [volatility](/wiki/implied-volatility/) spikes and temporary dislocations in [bond](/wiki/bond-basics/) and currency markets since 2020 suggest fragility persists.

The Flash Crash remains a watershed moment: the day markets learned that their own infrastructure could be the primary threat to stability.

<div class="wiki-seealso">

### Closely related
- [Circuit Breaker](/wiki/circuit-breaker/) — Trading halt mechanisms introduced post-2010
- [Algorithmic Trading](/wiki/algorithmic-trading/) — Automated execution that triggered the crash
- [High-Frequency Trading](/wiki/high-frequency-trading/) — Technology at the root of the cascade
- [Volatility Index](/wiki/fear-index/) — Panic indicator during the event

### Wider context
- [Market Making](/wiki/market-maker-obligations/) — Liquidity provision under stress
- [Systemic Risk](/wiki/systemic-risk/) — Interconnectedness across markets
- [Regulatory Framework](/wiki/financial-regulation-and-supervision/) — SEC and CFTC response
- [Greek Debt Crisis](/wiki/greek-debt-crisis/) — Macro context triggering the crash

</div>