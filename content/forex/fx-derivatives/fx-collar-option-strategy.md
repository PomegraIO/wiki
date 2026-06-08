---
title: "FX Collar Option Strategy for Corporate Hedgers"
description: "An FX collar combines a long put and short call (or vice versa) to cap both upside and downside on currency exposure, often at zero net cost."
keywords:
  - fx collar option
  - fx collar strategy
  - zero-cost collar
  - corporate currency hedging
  - option collar structure
image: /svg/forex.svg
---

*An **FX collar** is a two-legged option strategy where you buy protective downside (a [put option](/put-option/)) and sell profitable upside (a [call option](/call-option/)) on the same currency pair and date. The premium from selling the call offsets (often exactly) the cost of buying the put, making it a low-cost or zero-cost hedge—at the cost of capping your gain if the currency moves in your favor.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">FX Collar Option Strategy — Key Facts</div>

<img src="/svg/forex.svg" alt="An abstract editorial mark for forex derivatives." />

<div class="wiki-infobox-caption">Buy a floor (put) and sell a ceiling (call) to hedge exposure without paying an upfront premium.</div>

|   |   |
|---|---|
| **Structure** | Long put + short call at different [strike prices](/strike-price/) |
| **Put strike** | Usually [in-the-money](/in-the-money/) or near-the-money (protection floor) |
| **Call strike** | Usually out-of-the-money (profit ceiling) |
| **Net cost** | Zero to small positive/negative (premiums offset or nearly offset) |
| **Upside** | Capped at the call strike—any further gain is forfeited |
| **Downside** | Protected below the put strike—losses beyond that point don't hurt |
| **Who uses it** | Exporters and importers wanting budget certainty without paying net premium |
| **Duration** | Usually 3–12 months, matching operating cycle |

</aside>

## The Core Mechanics

A **collar** is a [protective put](/protective-put/) married to a [covered call](/covered-call/). You're long a real or anticipated currency exposure (e.g., you expect 1 million euros). You buy a put at, say, 1.08 USD/EUR to protect if the euro falls. You sell a call at 1.12 to collect a premium. If the call premium exactly equals the put premium, your net cost is zero.

**Example of a zero-cost collar:**

You are a US exporter expecting €1 million in 6 months. Current spot is 1.10 USD/EUR.

- **Buy EUR put, strike 1.08**: Costs you $0.025 per euro = $25,000 for €1M.
- **Sell EUR call, strike 1.12**: Receives $0.025 per euro = $25,000 for €1M.
- **Net cost**: $0 (the premiums cancel).

**Outcome at maturity:**

| **Spot at maturity** | **Your gain/loss** |
|---|---|
| 1.00 (euro crashes) | Locked in at 1.08 (put floor) → earn $1.08M |
| 1.08 | Put is [at-the-money](/in-the-money/), call [out-of-the-money](/out-of-the-money/) → earn $1.08M |
| 1.10 | Spot = initial; both options expire worthless → earn $1.10M |
| 1.12 | Call is [at-the-money](/in-the-money/), put is deep [out-of-the-money](/out-of-the-money/) → earn $1.12M (call capped you) |
| 1.15 (euro surges) | Call is exercised; you're capped at 1.12 → earn $1.12M (you miss the upside) |

The collar guarantees you between $1.08M and $1.12M. You lose the upside above 1.12, but you sleep knowing your revenue won't drop below $1.08M.

## Why Corporates Prefer Collars to Straight Puts

A simple long put—"I'll just buy insurance"—is the purest protection. But it's not free. For a 6-month EUR/USD put, 2–3% [out-of-the-money](/out-of-the-money/), the [option premium](/option-premium/) might cost 1.5–2% of notional annually.

**Cost of a plain put on €1M at 1.08 strike (spot 1.10):**
- Premium: ~2% = $20,000 annual / $10,000 for 6 months.
- This is a real expense that reduces the value of your hedge.

**Cost of a collar (same put, paired with a call at 1.12):**
- Put cost: −$10,000
- Call income: +$10,000
- Net cost: $0

For treasurers budgeting currency costs, the zero-cost collar is psychologically and financially easier to justify. You're not paying out of pocket; you're giving up upside you wouldn't otherwise have had (since you didn't budget for a euro rally anyway).

The trade-off is conscious and explicit: you surrender gains above 1.12 in exchange for eliminating the put premium.

## Choosing Strike Levels

Strike selection depends on your risk tolerance and expected range.

**Wide collar (loose floor and ceiling):**
- Put strike: 1.06 (3.6% below spot)
- Call strike: 1.14 (3.6% above spot)
- Net cost: Often slightly positive (you pay a small amount) because the put is deeper [out-of-the-money](/out-of-the-money/) and costs less than a deeper out-of-the-money call earns.
- Upside/downside: You have a wide band of unhedged risk, but the collar is cheap or free.

**Tight collar (close floor and ceiling):**
- Put strike: 1.08 (1.8% below spot)
- Call strike: 1.12 (1.8% above spot)
- Net cost: Often zero or a small debit, because both legs are similar distances from the money.
- Upside/downside: You're protected on a narrow range. Any move beyond the band is locked in.

**Asymmetric collar:**
- Put strike: 1.07 (wider downside)
- Call strike: 1.12 (tighter upside)
- Net cost: Usually positive (you pay a little) because you're buying more protection than you're selling.
- Use case: You're very risk-averse and willing to cap upside tightly to buy a wider floor.

## Common Variations

**Reverse collar** (short put + long call):
Used by importers or those with short currency exposure. You buy a call (paying premium) and sell a put (receiving premium). The long call is your protection ceiling; the short put caps your downside benefit. Less common than standard collars, but the same zero-cost principle applies.

**Ratio collar:**
Buy 1 put and sell 2 calls, or vice versa. This introduces [gamma](/gamma/) imbalance and leverage. A 1:2 collar can be zero-cost but gives unlimited upside loss if the currency rallies hard (you're short more call optionality than you own put). Typically used only by sophisticated traders comfortable with leverage.

**Rolling collars:**
As one collar expires, you close it and open a new one at fresh strike levels. Many corporates roll quarterly or semi-annually, resetting the protection band as market conditions and the underlying exposure change. Rolling is cheaper than closing and reopening if you can negotiate favorable spreads on the back-to-back trade.

## How the Collar Affects Accounting and Reporting

In [accrual accounting](/accrual-accounting/), if your collar qualifies as a [cash-flow hedge](/cash-flow-hedge/) under [ASC 815](/asc-606/) (US GAAP), the premium (or zero-cost nature) of the collar gets recorded in other comprehensive income, not immediately in earnings. This can make a zero-cost collar attractive to CFOs who want to avoid balance-sheet noise.

A put alone, costing $10K, hits your P&L. A zero-cost collar doesn't. However, if the collar is *not* designated as a hedge (the company doesn't document it as hedging a specific exposure), the daily [mark-to-market](/mark-to-market/) profit/loss on the collar is recorded in earnings, creating potentially confusing volatility.

Many corporates pair a collar with a [forward contract](/forward-contract/) or money-market hedge for this reason—the collar is the "optional protection," the forward locks in the rate, and the collar is the insurance layer above it.

## When Collars Work Best

**Tight operating cycles**: If you receive invoices in 30–90 days and need certainty for budgeting or margin calculations, a 3–6 month collar is straightforward. You know your floor and ceiling; you plan accordingly.

**Stable underlying exposure**: If you have regular, predictable foreign-currency cash flows (monthly royalties, quarterly subsidiary dividends, annual bonus payouts in foreign currency), a collar aligns well. You're not guessing at notional; you know what you're hedging.

**Moderate volatility regimes**: In very calm markets, put premiums are cheap and call premiums are small; the zero-cost collar is easy to construct. In extreme [volatility](/volatility-smile/), puts become expensive and calls less valuable—collars widen or cost money. In a [risk-on](/risk-on-risk-off/) environment, the market expects the currency to rally, so call premiums are meager and your zero-cost collar requires you to give up less upside.

## Limitations and Risks

**Capped upside**: If the hedged currency rallies 5% but your call is struck only 2% higher, you pocket the 2% and miss the 3%. Over a year, this can be material.

**Accounting volatility if not hedged**: If the collar is not designated as a hedge, daily mark-to-market swings hit earnings. Many corporates accept this for small notionals.

**[Counterparty risk](/counterparty-risk/)**: You are long a put (owe on it if it goes deep [in-the-money](/in-the-money/)) and short a call (your dealer owes you if it goes far [in-the-money](/in-the-money/)). The dealer is your counterparty on both legs; if they default, you lose the put's value.

**No protection against volatility alone**: A collar protects level (spot moving against you) but not [volatility](/historical-volatility/). If the euro is volatile but ends near where it started, your collar does nothing—you've capped your upside for no downside event.

## See also

<div class="wiki-seealso">

### Closely related

- [Put Option](/put-option/) — The protective leg of the collar
- [Call Option](/call-option/) — The funded leg; selling it pays for the put
- [Strike Price](/strike-price/) — Choosing collars depends on where you place the floor and ceiling
- [Option Premium](/option-premium/) — Why zero-cost collars zero out two premiums
- [In-the-Money](/in-the-money/) — How payoff changes as spot crosses the strikes
- [FX Option Expiry Cut Conventions](/fx-option-expiry-cut-conventions/) — Collar settlement uses the same cut mechanics as single options
- [Currency Risk](/currency-risk/) — The underlying exposure being hedged

### Wider context

- [Derivatives Hedging](/derivatives-hedging/) — Broader hedging toolkit
- [Forward Contract](/forward-contract/) — Often paired with collars for multi-layer hedges
- Money Market Hedge — Alternative approach using borrowing/lending
- [Quanto FX Options Explained](/quanto-fx-option-explained/) — Exotic collar variants where FX itself is the reference
- [Mark-to-Market](/mark-to-market/) — How collars are valued daily

</div>