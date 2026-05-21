---
title: "Circuit breaker"
description: "A circuit breaker is an automated trading halt triggered when a security or the entire market falls (or rises) too fast. The halt allows volatility to cool and prevents panic-driven crashes. U.S. circuit breakers can halt trading from minutes to the rest of the day."
keywords:
  - circuit breaker
  - trading halt
  - volatility halt
  - market protection
image: "/svg/trading.svg"
---

*A **circuit breaker** is an automated market safeguard that pauses trading when prices fall (or occasionally rise) too fast in too short a time. When triggered, trading is halted for a set period (15 minutes to the rest of the day), allowing volatility to cool and preventing panic-driven cascades. U.S. markets have circuit breakers at both the market-wide level ([S&P 500](/stock-market) index) and the individual stock level.*

<div class="wiki-hatnote">

For temporary stock-specific halts, see trading halt. For intraday trading limits in other markets, see limit-up limit-down. For flash crashes, see flash crash.

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Circuit breaker — key facts</div>

<img src="/svg/trading.svg" alt="A trading floor during a circuit breaker halt" />

<div class="wiki-infobox-caption">Circuit breaker triggered: trading pauses to cool emotions and prevent cascades.</div>

|   |   |
|---|---|
| **Trigger** | S&P 500 falls 7%, 13%, or 20% from previous close |
| **Market-wide halts** | 15 min (7%), 15 min (13%), close for day (20%) |
| **Stock-specific halts** | 5 min if stock moves 10%+ in 5 minutes |
| **Purpose** | Prevent panic, allow orderly re-pricing, avoid flash crashes |
| **History** | Implemented after 1987 crash; refined after 2010 flash crash |

</aside>

## Market-wide circuit breakers (S&P 500 level)

The main circuit breakers trigger based on the **S&P 500 index level** (the main broad-market index):

**Level 1:** S&P 500 drops **7%** from prior close.
- Trading halts for **15 minutes** at the beginning and during the day.
- Allows portfolio managers to rebalance and traders to reassess.

**Level 2:** S&P 500 drops **13%** from prior close.
- Trading halts for **15 minutes**.
- More severe; suggests market uncertainty is high.

**Level 3:** S&P 500 drops **20%** from prior close.
- Trading halts for the **remainder of the day** (until 4:00 p.m.).
- Prevents a cascade crash; waits until the next trading day to resume.

## Stock-specific circuit breakers (limit-up-limit-down)

Individual stocks have their own halts triggered by the **Limit Up/Limit Down (LULD) rule:**

- If a stock's price moves **10% or more in 5 minutes** (in most cases), trading is halted for **5 minutes**.
- The 10% threshold is computed from a reference price calculated from the prior close and recent trading.
- This prevents rapid cascades in individual names due to algorithmic selling or fat-finger trades.

## Historical context and the 1987 crash

The **October 19, 1987 crash** (Black Monday) saw the S&P 500 fall ~22% in a single day. Margin calls triggered forced selling, which triggered more margin calls, creating a cascade.

Regulators realized they needed **circuit breakers** to interrupt the cycle and allow human judgment to take over. The first circuit breakers were implemented in 1988.

## The 2010 Flash Crash and LULD rules

On **May 6, 2010**, a single large block order (allegedly a $4.1 billion sale of S&P 500 futures) triggered a cascade:
- Algorithms unwind positions.
- Selling begets selling.
- The market falls ~1000 points in minutes (~9.7%).
- Prices are chaotic; $1 stocks trading at $0.01.

The market partially recovered within minutes, but the event exposed weaknesses in the circuit breaker system. The **Limit Up/Limit Down (LULD) rule** was introduced in 2012 to prevent such rapid swings in individual stocks.

## How circuit breakers prevent crashes

**Mechanical pause:** The halt forces a pause; humans and algorithms cannot execute trades during the halt.

**Price re-equilibration:** During the halt, traders adjust their view of fair value. Sellers who were in a panic might reconsider; buyers might re-engage.

**Margin call awareness:** Portfolio managers aware of margin calls can liquidate positions in an orderly manner, rather than cascading liquidations.

**Information absorption:** News or clarifications issued during the halt can restore confidence.

## Criticisms of circuit breakers

**They do not always work:** The 2010 flash crash happened despite circuit breakers. The breach in level 1 triggered the 15-minute halt, but the cascade was so fast that many traders could not respond in time.

**They can be gamed:** Some argue sophisticated traders can predict halt levels and position ahead, creating artificial demand or supply right before a halt.

**Regulatory uncertainty:** A halt creates uncertainty: will the market collapse further when it reopens? This can make sellers more panicked, not less.

**Unintended consequences:** The 2020 COVID crash saw several circuit breaker halts, and each halt caused volatility to spike further as traders scrambled to reposition.

## Circuit breakers and trading strategies

**Stop-loss avoidance:** During a halt, your stop-loss order does not execute. The stock can gap down past your stop, and when trading resumes, you are hit at a worse price.

**Halt trading:** Some traders monitor halt levels and buy (or short) expecting the halt to stabilize the market (or create panic on resume).

**Position sizing:** Traders managing risk must account for the possibility of halts and gaps. A simple stop-loss might not protect you if a halt causes a gap.

## International circuit breakers

Other exchanges have similar mechanisms:

- **London Stock Exchange:** Individual stock halts if move is too extreme.
- **Tokyo Stock Exchange:** Market-wide halts if Nikkei falls sharply.
- **China:** Circuit breakers triggered at 5% and 7% index falls (implemented 2016; later suspended).

Details vary, but the principle is universal: pause to prevent cascades.

## The debate: do circuit breakers help or hurt?

**Argument for:** They prevent flash crashes by forcing a pause. The 1987 crash would have been worse without circuit breakers.

**Argument against:** They create artificial price discovery gaps and can exacerbate panic when trading resumes.

**Consensus:** Circuit breakers are here to stay. Regulators continue to fine-tune thresholds and timing to balance protection against unintended consequences.

## See also

<div class="wiki-seealso">

### Closely related

- Limit-up-limit-down — individual stock circuit breaker rule
- Trading halt — temporary pause in trading
- Flash crash — rapid crash; circuit breakers aim to prevent
- [Market order](/market-order) — executes at whatever price during halts

### Market stress and volatility

- Volatility — what circuit breakers respond to
- Cascade — selling begets selling; breakers prevent
- Panic selling — emotional response circuit breakers interrupt
- **Margin call** — forced sales during crashes; breakers cool these

### Trading and risk

- Stop-loss — may not protect during halts
- Gap risk — price gap when trading resumes
- Position sizing — account for halt risk
- Risk management — incorporate halt risk

### Historical events

- Black Monday (1987) — motivate circuit breakers
- Flash crash (2010) — exposed weaknesses; LULD introduced
- COVID crash (2020) — tested circuit breakers again

</div>
