---
title: "Limit-Up Limit-Down Market"
description: "A circuit-breaker regime that halts trading when a security's price moves beyond a rolling reference band, protecting against runaway volatility."
keywords:
  - circuit breaker
  - volatility control
  - trading halt
  - market protection
  - price limits
image: "/svg/markets.svg"
---

*The **limit-up limit-down** (LULD) market system is a regulatory circuit breaker that pauses trading in a security when its price moves beyond a dynamically calculated band around a rolling reference price. Activated in 2012 following the 2010 flash crash, LULD restricts per-stock price swings to prevent algorithmic feedback loops and extreme volatility from cascading through the market.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Limit-Up Limit-Down — key facts</div>

<img src="/svg/markets.svg" alt="An abstract editorial mark for market structure and trading venues." />

<div class="wiki-infobox-caption">The SEC's response to flash crashes; a circuit breaker that treats individual stocks like fuses.</div>

|   |   |
|---|---|
| **What it is** | Dynamic price-movement bands that trigger trading halts |
| **Also called** | LULD, stock-level circuit breaker, price-movement limits |
| **Band width** | 5%, 10%, or 20% depending on volatility and price tier |
| **Reference period** | Rolling five-minute window |
| **Trigger effect** | 15-second trading pause; orders queued, not cancelled |
| **Applies to** | All stocks on NMS plans; excludes after-hours trading |
| **Regulator** | SEC; administered via Securities Information Processor |

</aside>

## Origins: the 2010 flash crash

The limit-up limit-down regime emerged from the chaos of May 6, 2010, when the U.S. stock market experienced a sudden, severe drop in less than an hour. The S&P 500 fell roughly 9% in minutes, triggered by a large sale and amplified by automated trading algorithms. Sell orders hit [market makers](/market-maker-trading/) faster than they could process them; [market makers](/market-maker-trading/) withdrew liquidity; algorithms, sensing falling prices, sold more aggressively. The feedback loop fed on itself. Thousands of trades executed at absurd prices—one stock trading for a cent, another for several hundred dollars—before the market stabilized.

The flash crash revealed that modern electronic markets, despite their speed and efficiency, lacked individual-security safeguards. Regulatory halts existed at the broad market level (circuit breakers on the S&P 500 or [NASDAQ](/nasdaq/)), but not on individual stocks. A single illiquid security could swing wildly before any halt triggered, harming traders caught on the wrong side and shaking confidence in market integrity.

The SEC's response was to implement LULD: a granular, security-by-security mechanism to prevent extreme price swings. Rather than wait for a stock to collapse or spike, LULD halts trading before the move becomes extreme—a circuit breaker at the stock level, like a fuse in an electrical system.

## How the bands are set and updated

The LULD system defines separate bands for limit-up and limit-down prices, both symmetrical around a rolling reference price. The reference price is calculated as the average price during the preceding five-minute window of active trading. The bands are typically set at 5%, 10%, or 20% above and below that reference, depending on the security and market volatility tier.

Securities are classified into three tiers based on average price and recent volatility. Tier 1 includes S&P 500 stocks and high-volume securities; Tier 2 covers other widely traded stocks; Tier 3 encompasses lower-priced and less liquid stocks. Tier 1 stocks usually operate under a 5% band; Tier 2 at 10%; Tier 3 at 20%. The bands are tighter for the most liquid, stable stocks and wider for those with higher expected volatility.

The rolling five-minute window is crucial. As each minute passes, the oldest minute drops out of the calculation and the newest minute is added, keeping the reference price dynamic. This means the limit-up and limit-down prices shift every minute in response to recent trading activity. If Apple trades $150–$152 during the last five minutes, the reference is around $151, and the LULD bands are roughly $143.55 to $158.55. If the next minute is explosive and Apple trades $155–$160, the new five-minute window shifts the reference and bands upward, allowing the next price move to occur at higher levels.

This design prevents the bands from being too rigid. During normal trading, the rolling reference tracks the stock price smoothly. During volatility, the bands expand to reflect recent activity, avoiding the freeze-up that would occur if bands were fixed at the opening price.

## The trading halt and order management

When a security trades at or beyond its limit-up or limit-down price, trading halts for 15 seconds. Orders submitted during the halt are not cancelled; instead, they queue in the system. After 15 seconds, the trading pause lifts, the reference price recalculates based on the newest five-minute window, the bands reset, and trading resumes.

The 15-second pause serves a specific purpose: it interrupts the feedback loop. When algorithms and [market makers](/market-maker-trading/) see prices moving faster than they can track, they often respond mechanically—selling into falling prices, buying into rising prices. Pausing breaks that mechanical reaction. During the pause, new information can emerge, traders can reconsider their positions, and [market makers](/market-maker-trading/) can rebalance their quotes.

If the stock tries to trade beyond the new bands immediately after resuming, another 15-second halt triggers. In extreme volatility, a stock can experience multiple halts in succession. This is intentional; the system is designed to be more aggressive as volatility increases, enforcing more frequent halts to prevent runaway moves.

## The impact on trading behavior and [market makers](/market-maker-trading/)

LULD fundamentally changed how traders and market makers approach volatile situations. Before LULD, a sudden plunge invited aggressive selling; LULD now stops that selling temporarily. The halt-and-resume cycle gives [market makers](/market-maker-trading/) and algorithms time to recalibrate. Many have since coded LULD-aware strategies that anticipate halts and adjust positions before they trigger.

The halts have also improved market quality in some dimensions. Extreme single-stock flash crashes are rarer since LULD was implemented. Most traders and institutions have adapted by accepting that they cannot execute massive volumes instantly without triggering pauses. Large institutions now break orders into smaller pieces and execute over longer timeframes, a safer approach.

However, LULD creates new frictions. During a halt, traders cannot exit positions immediately even if they want to. A holder of a stock experiencing a limit-down halt cannot sell until trading resumes. This has raised concerns that LULD might trap traders on one side of an extreme move. If a stock is limit-down and the trader wants to sell, the halt prevents the sale, potentially turning a bad situation worse.

The SEC has addressed this by allowing trading to resume during the 15-second halt under specific conditions. Limited "quotation-only" trading can occur in the final 30 seconds before the halt ends, allowing some orders to begin matching before full trading resumes. This partial reopening reduces the jam of pent-up orders when the 15 seconds elapse.

## LULD and after-hours trading

An important limitation of LULD is that it applies only to normal market hours (9:30 a.m. to 4:00 p.m. ET) on the centralized exchanges. After-hours trading on [alternative trading systems](/alternative-trading-system/) and electronic communications networks operates under different rules. Stocks can move dramatically after hours without LULD halts. This creates a risk: a stock can gap sharply on news released after 4 p.m., and the opening the next morning may see limit-up or limit-down halts as the market tries to reprice.

This asymmetry has frustrated traders holding positions overnight, especially during earnings announcements or major news events. The solution—extending LULD to after-hours trading—remains debated because after-hours markets are less liquid and more prone to wide spreads; LULD restrictions might make them less tradable, not more.

## Evaluating effectiveness

Since its implementation in 2012, LULD has successfully prevented most flash-crash-like events in individual stocks. Extreme intraday moves of 20%+ in major liquid stocks are far rarer than they were in the 2000s. The halts work mechanically; they impose order and predictability in volatile moments.

Critics argue LULD is reactive rather than curative. It does not address the underlying cause of extreme volatility—whether it is legitimate price discovery reacting to new information, or algorithmic feedback. It simply pauses trading until the market can absorb the move. Some academics contend that LULD delays price discovery and creates artificial trading friction, though empirical evidence on this point is mixed.

The system also has unintended consequences for illiquid stocks. A small, thinly traded stock experiencing genuine fundamental news can hit its bands easily, triggering halts that frustrate legitimate traders wanting to re-price quickly. For these stocks, the 5–20% bands are sometimes too restrictive.

## See also

<div class="wiki-seealso">

### Closely related

- [Circuit breaker](/volatility-smile/) — broad market trading halts triggered by index movements
- [Volatility](/historical-volatility/) — the pricing dynamics that drive LULD bands
- [Market order](/market-order/) — immediate execution vulnerable to halts during volatile moves
- [Alternative trading system](/alternative-trading-system/) — venues where LULD operates differently
- [Market maker](/market-maker-trading/) — the intermediaries managing inventory during halts

### Wider context

- [Stock exchange](/stock-exchange/) — where LULD rules are enforced
- [Securities and exchange commission](/securities-and-exchange-commission/) — regulator that administers LULD
- [Stress testing](/stress-testing/) — how regulators evaluate market resilience
- [Systemic risk](/systemic-risk/) — the broad market instability LULD aims to prevent
- [Locked market](/locked-market/) — another anomaly in modern market structure

</div>
