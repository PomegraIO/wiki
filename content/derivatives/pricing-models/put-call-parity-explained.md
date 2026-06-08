---
title: "Put-Call Parity Explained"
description: "Put-call parity is the no-arbitrage relationship between call and put prices. Learn how deviations create riskless arbitrage opportunities with a worked example."
keywords:
  - put call parity
  - put call parity explained
  - options parity
  - call put relationship
  - riskless arbitrage options
image: "/svg/derivatives.svg"
---

*The **put-call parity** relationship is a no-arbitrage principle linking [call](/call-option/) and [put](/put-option/) prices to the underlying asset and the risk-free rate: a call, minus a put, at the same strike and expiration, should equal the underlying price minus the present value of the strike. Any deviation creates a riskless arbitrage opportunity—traders lock in a profit by buying the underpriced side and selling the overpriced side.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Put-Call Parity — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives." />

<div class="wiki-infobox-caption">The relationship ensures options and spot markets cannot drift apart without triggering arbitrage.</div>

|   |   |
|---|---|
| **The equation** | C - P = S - PV(K), or C = P + S - PV(K) |
| **Where** | C = call price, P = put price, S = spot price, K = strike, PV(K) = present value of strike |
| **Holds when** | European-style options, no dividends, same strike and expiration |
| **Violation** | Creates riskless arbitrage—buy the cheap side, sell the dear |
| **Dividend adjustment** | Subtract dividend PV from S; American options violate parity due to early exercise |
| **Practical use** | Traders detect mispricings; market makers use it to hedge; it anchors option prices |

</aside>

## The core principle

Put-call parity states that a certain combination of options and the underlying must have the same value. Specifically, if you own a call and short a put (both at strike K, expiration T), you own a position that is economically identical to owning the underlying stock today and financing it at the risk-free rate.

Think of it this way:

- **Owning a call** gives you the right to buy the stock at K.
- **Shorting a put** means you are obligated to buy the stock at K if the buyer exercises.
- **Together**, you will own the stock at K no matter what the price does.

This is the same as buying the stock now and borrowing the strike price at the risk-free rate to pay for it later. Therefore, the value of the call minus the put must equal the value of owning the stock financed by borrowing:

**C - P = S - PV(K)**

Where PV(K) is the present value of the strike—how much you need to borrow today to have K dollars at expiration.

## A numerical example

Suppose a stock trades at \$100, and we have European call and put options both struck at \$100, expiring in one year. The risk-free rate is 5%.

The present value of the strike is:

**PV(K) = \$100 / 1.05 = \$95.24**

According to put-call parity:

**C - P = \$100 - \$95.24 = \$4.76**

This means the call should be worth \$4.76 more than the put.

Now suppose the market prices the call at \$7 and the put at \$1.50. The difference is \$5.50, which violates parity—the call is too expensive relative to the put.

An arbitrageur would:

1. **Short the call** (receive \$7)
2. **Buy the put** (pay \$1.50)
3. **Buy the stock** (pay \$100)
4. **Borrow \$95.24** at 5% (to be repaid in one year)

Net immediate cash flow: \$7 - \$1.50 - \$100 + \$95.24 = \$0.74 (profit locked in today)

Now consider what happens at expiration in one year:

- **If the stock is at \$120**: The call is exercised against us; we deliver the stock. The put expires worthless. We repay the loan (\$95.24 × 1.05 = \$100). Net: we received \$7 upfront and paid \$1.50 for the put = \$5.50 profit.
- **If the stock is at \$80**: The put is exercised by us; we are forced to buy at \$100 (we already own it, so no new purchase needed—this just matches our obligation). The call expires worthless. We repay the loan (\$100). Net: same \$5.50 profit.
- **If the stock is at \$100**: The call and put both expire worthless. We own the stock at \$100 and repay the loan (\$100). Net: \$5.50 profit.

The arbitrage locks in \$5.50 regardless of where the stock ends up—a riskless profit created by the parity violation.

## The equation with dividends

If the stock pays dividends, put-call parity adjusts. The dividend goes to the call holder (not the put holder) if paid before expiration, so the put becomes relatively more expensive. The adjusted formula is:

**C - P = S - Dividends - PV(K)**

Or, equivalently, subtract the present value of expected dividends from the spot price. If a \$100 stock pays a \$2 dividend before expiration, the put is worth \$2 more (approximately) than pure parity would suggest, because the put holder avoids the dividend.

This is why dividend dates matter for option traders: they shift the call-put balance.

## American vs European options

Parity in its simplest form applies to **European options**, which can only be exercised at expiration. American options, which can be exercised early, do not strictly obey parity, because early exercise creates an additional decision point.

For example, if a deep-in-the-money American call trades far below parity, an arbitrageur might exercise it early rather than wait, disrupting the arbitrage. Similarly, an early-exercised American put can violate the parity relationship. In practice, American option prices stay close to the parity band, but the band is wider because early exercise is possible.

## Why parity matters in practice

**For market makers**: Option traders use parity to hedge their positions. If a trader sells a call, they know they can construct a risk-free hedge by buying a put and the stock, financing it at the repo rate. This allows them to price the call as a derivative of the put and spot market, not as an independent guess.

**For traders spotting mispricings**: When options and stocks become dislocated—such as in a market crash or illiquidity event—parity violations appear. A skilled trader can execute the arbitrage and lock in a profit, which simultaneously brings prices back into line.

**For option pricing models**: Parity is a sanity check for any option model ([Black-Scholes](/black-scholes-model/), binomial, etc.). If a model generates call and put prices that violate parity, the model is wrong.

**For leverage and portfolio management**: An investor who wants to create a synthetic long stock position can buy a call and short a put, which is equivalent to buying stock with leverage. Parity ensures this synthetic position is fairly priced relative to the real stock.

## When parity breaks in real markets

Parity violations are rare but can occur in stressed conditions:

- **Extreme illiquidity**: If a small-cap stock's options market is thin, the bid-ask spread on calls and puts can be so wide that parity violations exist on the quoted market. But the arbitrageur's costs to trade multiple legs would consume the profit.

- **Credit risk**: If the counterparty risk of a borrow or a clearing house is not trusted equally by all traders, one side of the arbitrage might be worth more or less than parity suggests.

- **Circuit breakers and trading halts**: During a market halt, call and put prices might become stale, creating apparent parity violations that evaporate once markets reopen.

- **Dividend surprises**: If a company announces an unexpected dividend close to an option expiration date, the adjustment to parity lags for a moment until prices reset.

- **Interest rate spikes**: A sudden jump in the risk-free rate (such as a central bank shock) changes PV(K) instantly. Spot and option prices may lag, creating a brief window.

In most cases, parity is maintained tightly by institutional arbitrage. Retail traders rarely see true violations, but understanding parity helps them evaluate whether an option quote is reasonable.

## Inverse parity: reverse arbitrage

If the call is too cheap relative to the put, the opposite trade applies: short the put, short the stock, and buy the call. This locks in a riskless profit if the call underprices relative to parity. The mathematics is identical—any deviation can be exploited in both directions.

## See also

<div class="wiki-seealso">

### Closely related

- [Call option](/call-option/) — one side of the parity relationship
- [Put option](/put-option/) — the other side
- [Cash-settled vs physically settled options](/cash-settled-vs-physically-settled-options/) — settlement affects arbitrage mechanics
- [Black-Scholes model](/black-scholes-model/) — option pricing framework that assumes parity
- [Derivatives hedging](/derivatives-hedging/) — practical use of options and put-call combinations
- [Strike price](/strike-price/) — the exercise point linking calls and puts
- [Option premium](/option-premium/) — the price determined in part by parity relationships

### Wider context

- [Option](/option/) — the broader concept
- Arbitrage — riskless profit opportunities
- [Futures contract](/futures-contract/) — related derivative with its own parity concepts
- [Risk-free rate](/risk-free-rate/) — the discount rate in the parity equation

</div>
