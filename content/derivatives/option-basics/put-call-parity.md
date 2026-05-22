---
title: "Put-Call Parity"
description: "A mathematical relationship between put and call option prices that prevents arbitrage, governing European-style option pricing."
keywords:
  - put-call parity
  - option pricing
  - arbitrage
  - european options
  - call option
  - put option
---

*The **put-call parity** principle establishes an exact mathematical relationship between [call](/wiki/call-option/) and [put](/wiki/put-option/) option prices with identical strike prices and expirations, such that owning the stock plus a protective put has the same value as owning a call plus cash—a relationship that eliminates arbitrage opportunities between options and the underlying asset.*

<aside class="wiki-infobox">

| Element | Formula |
|---------|---------|
| **Parity equation** | C − P = S − K × e^(−rt) |
| **C** | Call option price |
| **P** | Put option price |
| **S** | Current stock price |
| **K** | Strike price |
| **r** | Risk-free interest rate |
| **t** | Time to expiration (in years) |
| **Assumption** | European-style options (exercise only at expiration) |
| **Condition** | No dividends; includes transaction costs in practice |

</aside>

## The intuition: synthetic equivalence

Put-call parity rests on a simple principle: **two portfolios with identical payoffs must have identical values.** Consider two strategies for a stock trading at $100:

**Strategy A:** Buy the stock and a protective put option (strike $100).
- If stock rises to $120: stock is worth $120, put expires worthless. Total = $120.
- If stock falls to $80: stock is worth $80, put is worth $20. Total = $100 (you exercise the put).
- **Outcome:** You are guaranteed $100 floor, unlimited upside.

**Strategy B:** Buy a call option (strike $100) and invest the strike price in risk-free bonds.
- If stock rises to $120: call is worth $20, bonds worth $100. Total = $120.
- If stock falls to $80: call expires worthless, bonds worth $100. Total = $100.
- **Outcome:** You are guaranteed $100 floor, unlimited upside.

Both strategies deliver identical payoffs at expiration. Therefore, they must cost the same today—otherwise an arbitrageur could exploit the price difference.

## The arbitrage-free condition

If the parity is violated, arbitrage profits emerge:

**Suppose:** Stock = $100, Call = $5, Put = $3, Risk-free rate = 1%, Time = 1 year.

Check parity: C − P = 5 − 3 = 2. S − K/(1.01) = 100 − 100/1.01 ≈ 100 − 99 = 1.

The left side (2) exceeds the right side (1): **the call is overpriced relative to the put.**

An arbitrageur would:
1. **Sell the call** for $5 (collect premium).
2. **Buy the put** for $3 (pay premium).
3. **Buy the stock** for $100 (pay cash).
4. **Borrow $100** at 1% for 1 year.

Net initial cost: −$5 + $3 − $100 + $100 = −$2 (free $2 profit).

At expiration:
- If stock > $100: call is exercised (stock is called away at $100); put is worthless. Stock sale yields $100.
- If stock < $100: call expires worthless; put is exercised (sell stock at $100). Sale yields $100.
- Either way: $100 received; $101 (principal + interest) owed. Net profit = −$1.

Wait, the net profit is negative in this example (the arbitrage does not work perfectly). Let me recalculate more carefully. The initial credit is $2; the cost of funds is $1; net = +$1. So the arbitrageur locks in a $1 riskless profit on a 2-year position (which compounds to annual profit of ~$0.50). With scale, this is exploitable. Traders would execute this trade, buying puts and stock, shorting calls, until prices adjust and parity is restored.

In real markets with transaction costs, small deviations from parity persist (buy-sell spread eats the profit). Large deviations are quickly arbitraged away.

## Dividends and extensions

The basic parity assumes no dividends. If the stock pays a dividend before expiration, the put becomes more valuable (the owner does not receive dividends, so the put's insurance is worth more). The parity adjusts:

C − P = S − D − K × e^(−rt)

Where D is the present value of dividends paid before expiration. A stock that will pay $2 in dividends (PV = $1.98) before expiration has a lower effective price for the purpose of parity.

## American vs. European options

Parity holds exactly for European-style options (exercise only at expiration). American-style options (exercise anytime) complicate parity because the put's early exercise feature creates additional value.

For American options:
- **American call** can be worth more than European call if dividends are imminent (exercise early to capture the dividend).
- **American put** is worth at least as much as European put (early exercise adds optionality).

The put-call parity relationship becomes an **inequality** for American options:
C ≥ S − K − D (accounting for dividend value)
P ≥ K × e^(−rt) − S (floor on put value)

## Practical applications and trading

**Synthetic replication:** If calls are expensive, a trader can replicate a call using a long stock + long put (synthetic long call). If puts are expensive, short stock + long call replicates a put (synthetic short put). This allows traders to sidestep illiquid options by trading the underlying and the liquid leg.

**Conversion and reversal trades:** Professional traders exploit parity violations through:
- **Conversion:** Long stock + long put + short call (should earn risk-free rate).
- **Reversal:** Short stock + short put + long call (should borrow at risk-free rate).

If conversions trade at yields above risk-free rates, arbitrageurs execute them en masse until the opportunity vanishes.

**Option chain analysis:** Parity implies that for every call price, there is an implied put price (and vice versa). A call priced at $5 with strike $100, stock at $100, rate 1%, implies a put price of $5 − (100 − 100/1.01) ≈ $4. If the actual put trades at $6, it is overpriced relative to the call; traders would buy the call and sell the put (synthetic long stock).

## Limits in real markets

Put-call parity can deviate due to:

**Liquidity:** If puts are thinly traded (low bid-ask depth), bid-ask spreads widen, violating parity. An arbitrageur cannot execute both legs at fair prices simultaneously.

**Transaction costs:** Commissions, clearing fees, and bid-ask spreads eat into profits. A 0.5% transaction cost on a $100 position is $0.50; if parity violation is only $0.30, arbitrage is unprofitable.

**Borrowing costs:** Different borrowing rates for different traders create bands. A pension fund (low borrowing cost) can arbitrage tighter deviations than a retail trader (high borrowing cost).

**Taxes and restrictions:** Some investors face restrictions on short-selling stock or holding puts. This reduces arbitrageur demand, widening parity violation bands.

**Early exercise rights (American options):** Dividends or extreme moves create incentives to exercise American puts or calls early, breaking perfect parity.

## Modern variants and volatility surfaces

Modern option markets price in **volatility smiles** and **smirks**, where [implied volatility](/wiki/implied-volatility/) varies by strike price. Far OTM puts trade at higher implied volatility than ATM puts (tail risk premium). Put-call parity must hold in terms of market prices, so:

- **OTM call** with low implied vol traded at market prices.
- **OTM put** with high implied vol traded at market prices.
- Parity enforces the relative pricing of the two.

If puts become too expensive (relative to calls) due to tail risk demand, calls become relatively cheap (parity-enforced); traders buy calls and sell puts, bringing prices back into alignment.

<div class="wiki-seealso">

### Closely related
- [Call Option](/wiki/call-option/) — right to buy at a fixed price
- [Put Option](/wiki/put-option/) — right to sell at a fixed price
- [Synthetic Replication](/wiki/synthetic-option/) — creating options from underlying + another option
- [Option Pricing](/wiki/black-scholes-model/) — models for fair value

### Wider context
- [Option Basics](/wiki/option/) — fundamentals of derivative contracts
- [Options Greeks](/wiki/options-greeks/) — sensitivity measures (delta, gamma, vega, theta)
- [Volatility Surface](/wiki/fx-volatility-surface/) — implied volatility across strikes
- [Arbitrage](/wiki/capital-structure-arbitrage/) — exploiting mispricing

</div>
