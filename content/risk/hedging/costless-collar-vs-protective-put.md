---
title: "Costless Collar vs Protective Put"
description: "Costless collar vs protective put: compare premium costs, upside caps, and downside protection to choose the right hedge for your risk budget."
keywords:
  - costless collar vs protective put
  - collar hedge vs put option
  - zero cost collar downside protection
  - protective put collar comparison
  - option hedging strategies
image: /svg/risk.svg
---

*A **protective put** and a **costless collar** are both [derivatives hedging](/derivatives-hedging/) strategies that protect against downside, but they trade premium costs differently: a put costs cash upfront, while a collar finances the put by selling call [call options](/call-option/), capping your upside in exchange for zero premium.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Costless Collar vs Protective Put</div>

<img src="/svg/risk.svg" alt="An abstract editorial mark for risk." />

<div class="wiki-infobox-caption">Both limit losses, but collars limit gains; puts cost cash but leave upside uncapped.</div>

|   |   |
|---|---|
| **Protective Put: Premium cost** | Paid upfront; ranges from 1% to 5%+ of stock value depending on strike and time |
| **Protective Put: Downside floor** | Set by the [strike price](/strike-price/); losses capped |
| **Protective Put: Upside** | Unlimited; all gains above strike are yours |
| **Costless Collar: Premium cost** | Zero (or near-zero) due to offsetting call sale |
| **Costless Collar: Downside floor** | Set by put strike; losses capped |
| **Costless Collar: Upside cap** | Set by call strike; gains capped above that level |
| **Collar width** | Gap between put and call strikes; wider = more upside available, higher put cost |

</aside>

## Protective Put: Full Protection, Full Cost

A **protective put** is straightforward: you own a stock and buy a [put option](/put-option/) on it. The put gives you the right to sell the stock at a fixed strike price, no matter how far the stock falls. If you own 100 shares of a stock at $100 and buy a put at a $90 strike, your loss is capped at $10 per share (plus the put [option premium](/option-premium/) you paid).

For example:
- You own 100 shares at $100 ($10,000 position).
- You buy a three-month put with a $90 strike, paying $2 per share ($200 total premium).
- If the stock drops to $70, you exercise the put, selling at $90. Your loss is $10/share (the $10 drop from $100 to $90) plus $2/share (the premium) = $12/share or $1,200 total.
- If the stock rises to $130, the put expires worthless, but you keep the gains. Your gain is $30/share minus $2/share (premium) = $28/share or $2,800 total.

The protective put is clean: you pay for protection, and the cost is transparent. You choose the strike to set your acceptable loss. A put closer to the current price costs more but protects against smaller declines. A put further out-of-the-money costs less but leaves you exposed to larger losses.

The premium is the cost of certainty. If the stock falls 50%, the put saves you tens of thousands. If the stock rises 50%, you forgoe the upside minus the premium cost (a small tax on your gains). Most investors view this as fair insurance.

## Costless Collar: No Premium, Capped Upside

A **costless collar** is a compound strategy: you buy a put (downside protection) and simultaneously sell a call (upside cap) at a higher strike. The call sale generates premium that offsets the put cost, ideally to zero.

For example:
- You own 100 shares at $100.
- You buy a three-month put at a $90 strike (costing $2 per share, $200 total).
- You sell a three-month call at a $110 strike (generating $2 per share, $200 total).
- Net cost: $0.

Now, if the stock falls to $70, you exercise the put and sell at $90 (loss of $10/share). If the stock rises to $130, the call is exercised and you are forced to sell at $110 (capping your gain at $10/share). If the stock stays between $90 and $110, both options expire worthless and you keep the shares.

The collar has locked in a range: you cannot lose more than $10 per share, and you cannot gain more than $10 per share. The protection is free because the upside is sold away.

## When Each Makes Sense

**Protective puts** are ideal if:

- You believe in the stock's long-term upside and want to protect against tail risk without limiting gains.
- You can afford the premium (typically 1% to 5% of position value per three-month period).
- You want clear, linear downside protection—a floor below which you do not go.
- You plan to hold the stock long-term and may roll (renew) the put repeatedly.

Example: A founder holding 50,000 shares in their company (worth $5 million) faces stock volatility. A 2% annual put premium ($100,000) is expensive but preserves upside. They are betting the business will compound, and insurance is a small price for peace of mind.

**Costless collars** are ideal if:

- Your main goal is downside protection, and you are indifferent to capping upside (or believe the upside cap is above realistic outcomes).
- You want to reduce [portfolio risk](/market-risk/) without paying premium.
- You are uncertain about near-term direction and want a defined-risk structure.
- You need protection now but do not have capital to spend on premium.

Example: An employee with 10,000 shares of restricted stock worth $500,000 faces vesting and lockup restrictions. A costless collar at $40 put / $50 call limits losses to 20% and gains to 25%, with zero cost. This allows the employee to sleep at night during the vesting window.

## The Cost Trade-Off

The central trade-off is **premium vs. upside cap**. Put premiums have risen post-2020 due to higher implied volatility. A $100 stock might now require a $3–$5 per share put (3–5%) versus $1–$2 in a low-volatility era. This makes collars more attractive by relative value.

Yet the collar's upside cap is real. If the stock unexpectedly rallies 40% and your call is at a 10% cap, you miss 30% of the gains. In hindsight, you overpaid for protection you did not need. With a protective put, you keep the full 40% and only pay 2–3% of value as insurance.

Over many years and many attempts to hedge, neither strategy dominates. Markets are efficient enough that buying puts is neither expensive nor cheap on average; collars neither generously cap upside nor stingy. The choice depends on your risk tolerance and conviction.

## Practical Implementation

**Protective puts** are straightforward to execute. You buy a standard put option on an exchange (via your broker). Brokers list puts for virtually all liquid stocks, so finding the strike and [expiration date](/expiration-date/) you want is easy.

**Collars** are more bespoke. You need to find a put and call at strikes such that their premiums roughly offset. If you want a $90 put (costing $2) and call selling is generating only $1.50 (at the $110 strike), you have a net cost of $0.50. You might widen the gap—move the call to $115 to sell more premium—until the premiums match.

This matching is often done with the help of a broker, an advisor, or a derivatives dealer (for larger positions). Retail investors can attempt it themselves, but it requires comfort with [option Greeks](/delta/) and market prices.

## Dividends and Early Exercise

If your stock pays dividends, the put and call behave differently.

With a **protective put**, you hold the stock and collect dividends as usual. The put is separate and does not interfere. You can also exercise the put early if it moves deep in the money and the dividend is large enough to make early exercise worthwhile (though this is rare with American puts).

With a **costless collar**, you still own the stock and collect dividends. However, the call you sold can be exercised by the buyer at any time, especially just before a large dividend payment (the call buyer wants to capture the dividend). This can force early exit—you are called away before collecting all dividends. This is a hidden cost of collars when dividends are substantial.

## Time Decay and Rolling

Both puts and calls lose value as [expiration](/expiration-date/) approaches if they are out-of-the-money (a phenomenon called [time decay](/time-decay-theta/) or theta decay). This works in your favor if you are short the call (the call you sold depreciates), but against you if you are long the put (your protection depreciates).

For a protective put held over many months, you will eventually need to roll (buy back the old put and sell a new one at a later date and possibly different strike). Rolling costs money, so the true cost of a protective put over years is the sum of all rolled premiums.

For a collar, rolling is more nuanced. If the stock has risen and you are now in the call's in-the-money zone, rolling the call and put together to maintain a costless structure is difficult—the put will cost more (stock moved up, out-of-the-money put is cheaper to buy). You may end up with a net credit or debit, depending on implied volatility and the gap you want.

## Comparing Outcomes Over a Year

Assume a $100 stock, expecting 7% annualized return, with 20% annualized volatility.

**With protective put at $95 strike, 1-year expiry, costing $3:**
- Expected profit: $100 → $107 = $7, minus $3 premium = $4 net.
- 1% loss case: stock falls to $99. You exercise the put, selling at $95, losing $5, minus $3 premium = $8 loss total.

**With costless collar at $95 put / $105 call:**
- Expected profit: capped at $5 (the $105 – $100 difference), minus zero premium = $5 net.
- 1% loss case: stock falls to $99. You exercise the put at $95, losing $5, minus $0 premium = $5 loss total.

The protective put nets $4 in the normal case but loses $8 in a crash. The collar nets $5 normally and loses $5 in a crash. For volatile, uncertain periods, the collar's symmetric risk is appealing. For high-conviction upside, the put's upside preservation is attractive.

## Volatility's Hidden Role

The cost of both puts and calls depends on implied volatility. In low-volatility markets, puts are cheap, making protective puts attractive. In high-volatility markets, puts are expensive, making costless collars more valuable (because the sold call premium is also high, easier to match the put cost).

If you expect volatility to rise, buying puts now (before volatility spikes) locks in lower premium. If you expect volatility to fall, collars become less advantageous (call premium shrinks, making it harder to offset put cost).

## See also

<div class="wiki-seealso">

### Closely related

- [Put option](/put-option/) — the protective mechanics
- [Call option](/call-option/) — the upside cap mechanics
- [Protective put](/protective-put/) — standalone downside protection
- [Covered call](/covered-call/) — the inverse: selling upside to generate income
- [Option premium](/option-premium/) — what you pay or receive
- [Strike price](/strike-price/) — setting the floor and cap

### Wider context

- [Derivatives hedging](/derivatives-hedging/) — why and how to hedge with options
- [Portfolio risk](/market-risk/) — the broader context for hedging
- [Concentration risk](/concentration-risk/) — why single-position hedges matter
- [Implied volatility](/implied-volatility/) — what drives option prices
- [Black-Scholes model](/black-scholes-model/) — how option prices are calculated

</div>
