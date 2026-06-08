---
title: "Put-Call Parity for European Options"
description: "The put-call parity relationship for European options, how arbitrageurs enforce it, and the effect of dividends and interest rates."
keywords:
  - put call parity european options explained
  - put-call parity formula
  - european option arbitrage
  - put call parity dividend effect
  - riskless arbitrage options
---

*The **put-call parity** relationship is a no-arbitrage law: for European options on the same underlying, strike, and expiration, the difference between a call price and a put price is determined entirely by the current stock price, the strike, the risk-free rate, and expected dividends. Violate this relationship, and arbitrageurs will buy the cheap side and sell the dear side, pocketing a risk-free profit. This relationship anchors both option [pricing models](/black-scholes-model/) and market discipline.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Put-Call Parity — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives." />

<div class="wiki-infobox-caption">A mathematical identity that no-arbitrage enforcement makes true in liquid markets.</div>

|   |   |
|---|---|
| **Core formula** | C – P = S₀ – K·e^(–r·T) – PV(Dividends) |
| **What it means** | Call minus put equals stock price minus present value of strike (and dividends) |
| **Enforcement** | Arbitrageurs buy underpriced side, short overpriced side; trade disappears when parity holds |
| **Key assumptions** | European-exercise only; no [transaction costs](/), no taxes, no borrowing constraints |
| **Dividend treatment** | Parity adjusts downward for expected dividends (reduces call value, raises put value) |
| **Interest-rate effect** | Higher rates increase call value and decrease put value (more valuable to delay strike payment) |

</aside>

## The basic no-arbitrage argument

Imagine a stock trades at $100. A European [call option](/call-option/) with strike $105 and one year to expiration costs $5. A European [put option](/put-option/) with the same strike and expiration costs $8.

Now consider a simple portfolio: buy the call, sell the put, and short the stock. Today's cash flow is –$5 + $8 + $100 = $103.

In one year, two outcomes:
- **Stock above $105:** Call is in-the-money and worth $105 – $105 = $0; put is worthless (expires). You own the stock (from the short sale) and deliver it for $105. Net gain: $105 – $103 = $2.
- **Stock below $105 (say, $95):** Call expires worthless; put is in-the-money and worth $105 – $95 = $10. You pay $10 to buy the stock at $105 (the put strike), then return it to cover the short. Net cost: $10, so profit is $105 – $103 – $10 = –$8. Wait, that's a loss.

The two outcomes don't match—this portfolio is not risk-free. The problem is that the option prices are inconsistent. If we adjust them to satisfy parity, the arbitrage disappears.

## Deriving put-call parity

Consider two portfolios:

**Portfolio A:** Buy one call (call price = C) and lend money (borrow –K at rate r) such that you receive K in T years (one year, say).

**Portfolio B:** Buy one put (put price = P) and buy one share (stock price = S₀).

Both portfolios have identical payoffs in T years:

| Payoff when… | Portfolio A | Portfolio B |
|---|---|---|
| **S_T > K** (in-the-money call) | C + K (call value: S_T – K, plus lent amount grows to K) = S_T | S_T (put worthless; own stock worth S_T) |
| **S_T ≤ K** (out-of-the-money call) | K (lent amount + expired call) | K (put is in-the-money; exercise to buy at K; own stock) |

Both portfolios are worth S_T if S_T > K, and K if S_T ≤ K. They have identical payoffs, so by no-arbitrage, they must cost the same today:

<div style="background: #f5f5f5; padding: 12px; margin: 12px 0; border-left: 4px solid #ccc; font-family: monospace;">
C + K·e^(–r·T) = P + S₀
</div>

Rearranging:

<div style="background: #f5f5f5; padding: 12px; margin: 12px 0; border-left: 4px solid #ccc; font-family: monospace;">
C – P = S₀ – K·e^(–r·T)
</div>

This is the fundamental put-call parity relationship. The left side is the call-put spread; the right side is the present value of the stock minus the present value of the strike.

## Effect of dividends

The derivation above assumes no dividends. If the stock pays a dividend (or multiple dividends) before expiration, parity adjusts:

<div style="background: #f5f5f5; padding: 12px; margin: 12px 0; border-left: 4px solid #ccc; font-family: monospace;">
C – P = S₀ – K·e^(–r·T) – PV(Div)
</div>

Where PV(Div) is the present value of all dividends expected before expiration.

**Why?** The call holder receives the stock but forgoes any dividends until expiration—the dividend belongs to the previous owner if the call holder hasn't exercised. The put holder buys the stock and receives the dividend. This makes the put more valuable (you get paid to wait) and the call less valuable (you miss the dividend).

If PV(Div) is large (a high-yielding stock), the call becomes much cheaper and the put much more expensive, widening the call-put spread.

## Interest-rate effect

Higher risk-free rates increase C – P. Intuitively: if rates are high, the present value of the strike K·e^(–r·T) is lower (you discount more steeply). This makes the call more attractive (you get to delay paying K) and the put less attractive (waiting is costlier). The call-put spread widens.

Conversely, if rates are negative (rare, but true in some countries), the call-put spread narrows.

## How arbitrageurs enforce parity

Suppose the market violates parity:
- Call price = $6
- Put price = $7
- Stock price = $100
- Strike = $105
- Risk-free rate = 5% per year; T = 1 year
- PV(Strike) = $105 × e^(–0.05) ≈ $100

Parity says: C – P should equal $100 – $100 = $0. But the market shows C – P = $6 – $7 = –$1. The put is overpriced relative to the call.

An arbitrageur does this:
1. **Buy the call** (underpriced at $6).
2. **Sell the put** (overpriced at $7).
3. **Short the stock** ($100).
4. **Lend $100 at 5%** (to be repaid as $105 in one year).

Today's cash flow: –$6 + $7 + $100 – $100 = $1 (risk-free profit).

In one year:
- If stock > $105: Call is exercised; you buy at $105 using the loan repayment, return the stock. Put expires. Net: $0.
- If stock ≤ $105: Call expires; put is exercised; you are forced to buy at $105 using the loan repayment, return the stock. Net: $0.

The arbitrage trade locks in a $1 profit with zero risk. Many traders spot this; they all do it simultaneously. Demand for the call rises (pushing price up), demand for the put falls (pushing price down), until the spread adjusts back to $0 and parity is restored.

## Practical violations and transaction costs

Real markets rarely violate parity severely because of arbitrage. However, small violations persist due to:

- **Transaction costs:** Bid-ask spreads, commissions, and borrowing costs mean a violation must be large enough to exceed these costs to be profitable.
- **Borrowing rates:** The "risk-free" rate is not uniform; lending and borrowing rates differ. If you need to borrow shares to short the stock, the cost is higher than the Treasury rate.
- **Liquidity constraints:** If you can't short a stock (it's hard to borrow), or the options have wide spreads, arbitrage is expensive or impossible.
- **Early exercise (American options):** European parity doesn't apply to American options, which can be exercised early. A deep-in-the-money American call might be exercised to capture dividends, violating the European formula.

## Parity in option pricing models

The [Black-Scholes model](/black-scholes-model/) and other [option pricing](/option/) frameworks are constrained by put-call parity. You cannot solve for an independent call price and put price; once you know one, parity determines the other.

In practice, traders often:
1. Observe call [implied volatility](/implied-volatility/) from the market.
2. Use the model to price the call.
3. Apply parity to deduce the put price.

If the observed put price deviates significantly from the parity-implied price, the put is either a trading opportunity or a signal of market microstructure effects (liquidity, borrowing costs).

## Applications beyond basic arbitrage

**Hedge construction:** A protective put (owning a put to insure a stock) is equivalent to owning a call and lending at the risk-free rate, by parity. If puts are expensive, a trader might synthesize a put using the cheaper call.

**Strike selection:** Parity helps traders understand call-put prices across strikes. The call-put spread widens as you move out-of-the-money.

**Dividend strategy:** Before dividend ex-dates, parity dictates how call and put prices must shift. Arbitrageurs trade to exploit temporary dislocations around dividend announcements.

**Cross-market arbitrage:** If the same stock trades in multiple markets (US and European exchanges, for example), parity ensures prices don't diverge too much. A parity violation across exchanges would trigger capital flows until prices realign.

## See also

<div class="wiki-seealso">

### Closely related

- [Call option](/call-option/) — buying the right to purchase
- [Put option](/put-option/) — buying the right to sell
- [Black-Scholes model](/black-scholes-model/) — foundational option pricing framework
- [Implied volatility](/implied-volatility/) — market's expectation of future volatility, baked into option prices
- [Option premium](/option-premium/) — what you pay for the option
- [In-the-money](/in-the-money/) and out-of-the-money — moneyness and [strike price](/strike-price/)

### Wider context

- [Derivatives hedging](/derivatives-hedging/) — using options and parity relationships to manage risk
- Arbitrage — risk-free profit from price discrepancies
- [Counterparty risk](/counterparty-risk/) — who pays if the option is exercised?
- [Riskless arbitrage](/): theory and practice of enforcing market relationships

</div>
