---
title: "Call Spread Corporate"
description: "Corporate bond or preferred stock with embedded call option, allowing issuer to redeem early."
keywords:
  - callable bonds
  - embedded options
  - issuer redemption
  - call spread
  - bond risk
---

*A **call spread corporate** is a corporate [bond](/wiki/corporate-bond/) or [preferred stock](/wiki/preferred-stock/) that is [callable](/wiki/callable-bond/) — the issuer holds the right (but not the obligation) to repurchase or redeem the security at a specified call price on or after a given date. The term "spread" refers to the yield difference between the callable bond and a comparable non-callable bond, compensating the investor for the risk that the bond will be called away if rates fall.*

<div class="wiki-hatnote">
For callable bonds specifically, see <a href="/wiki/callable-bond/">/wiki/callable-bond/</a>. For the embedded option itself, see <a href="/wiki/call-option/">/wiki/call-option/</a>.
</div>

<aside class="wiki-infobox">

| Aspect | Detail |
|--------|--------|
| **Issuer Right** | Redeem bond before maturity at call price |
| **Call Price** | Usually 100–105% of par, gradually declining to par near maturity |
| **Call Date** | Often 5–10 years after issuance ("call protection" period) |
| **Benefit to Issuer** | Refinance at lower rates if bond price rises above call price |
| **Cost to Investor** | Capped upside if rates fall; negative convexity |
| **Yield Spread** | Callable bonds yield more than comparable non-callable bonds |
| **Duration Risk** | Asymmetric: positive in rising-rate scenarios, compressed in falling-rate scenarios |
| **Most Common Issuers** | Investment-grade corporates, utilities, real estate trusts (REITs) |

</aside>

## How embedded callability works

A callable bond is a standard [corporate bond](/wiki/corporate-bond/) with an embedded [call option](/wiki/call-option/) that belongs to the issuer, not the bondholder. The issuer receives the coupon payments and principal repayment from the investor, but also retains the right to "call" the bond — that is, to repurchase it from the investor at a pre-specified price (the call price) on or after a specified date (the call date).

The call price is typically set slightly above par (e.g., 102% of face value for a newly issued bond), and it often declines over time, eventually approaching par as the bond approaches maturity. This declining call price reflects the issuer's incentive: early in the bond's life, the call price is higher, making it expensive for the issuer to call. As the bond ages, the call price declines, making early redemption more attractive to the issuer.

The issuer exercises the call when rates fall, allowing it to refinance the bond at a lower cost. Suppose an issuer sold a 5-year callable bond with a 5% coupon when rates were elevated. Two years later, rates fall to 3%, and new bonds can be issued at 3%. The issuer calls the old 5% bond at the call price (say, 101% of par), refinances by issuing a new 3% bond, and saves the difference in coupon costs over the remaining life of the original bond.

## The investor's perspective: negative convexity

From the bondholder's perspective, the callable bond is an ordinary bond, minus a call option. The investor receives the coupon and principal repayment, but has surrendered the right to receive the full benefit of a rate drop.

In a traditional [non-callable bond](/wiki/bond/), if rates fall, the bond's price rises. A 5% coupon bond becomes more valuable if new bonds yield only 3%; its price might rise to $120 per $100 par. The bondholder benefits from this price appreciation if they sell the bond before maturity.

In a callable bond, the issuer prevents the bondholder from capturing the full upside. If rates fall and the bond price rises toward $110, the issuer calls the bond at $101 (the call price). The bondholder's gain is capped at the call price. This is **negative convexity** — the bond's price appreciation is limited in falling-rate scenarios, while its price depreciation is not limited in rising-rate scenarios. The payoff is asymmetric and unfavorable to the bondholder.

## Call spreads and the yield compensation

To attract buyers despite the embedded call, issuers must offer a higher yield. A callable bond typically yields 50–200 basis points more than a comparable non-callable bond (the "call spread"), depending on the likelihood of the bond being called and the riskiness of the issuer.

The call spread compensates the investor for:
1. The lost upside if rates fall and the bond is called.
2. The uncertainty about the bond's maturity (it could be called early).
3. The reinvestment risk (if the bond is called, the investor must reinvest the proceeds at prevailing rates, possibly lower than the original yield).

The value of the call option embedded in the bond can be approximated using [option pricing](/wiki/black-scholes-model/) models. The call option is more valuable (i.e., the call spread should be wider) when:
- Interest rate volatility is high (more likely rates will fall and trigger a call).
- The bond's coupon is far above current market rates (more likely the issuer will want to call).
- The time to the call date is long (more time for rates to fall).

## Common in corporate bonds and preferred stock

Callable bonds are standard in investment-grade corporate debt. Virtually all [corporate bonds](/wiki/corporate-bond/) of 5+ year maturity include call protection and thereafter are callable. The issuer's option to refinance is valuable, and it is reflected in the bond's pricing.

[Preferred stock](/wiki/preferred-stock/) — a hybrid security between equity and debt — is almost universally callable. A utility's preferred stock issued at a 6% dividend yield is typically callable by the utility a few years after issuance. If the utility's creditworthiness improves and new preferred stock can be issued at 5%, it will call the old 6% preferred and refinance at the lower rate.

[REIT](/wiki/real-estate-investment-trust/) debt is frequently callable, as REIT managers actively manage their capital structures and refinance when opportunities arise.

## Call-adjusted duration and analysis

Because a callable bond has limited upside, its [duration](/wiki/duration/) — the sensitivity to interest rate changes — is asymmetric. In rising-rate environments, the bond behaves like a typical bond: its price falls by a predictable amount per basis point of rate increase. In falling-rate environments, the price rise is compressed because the call kicks in, and the duration becomes shorter.

Professional analysts compute **option-adjusted duration** (OAD), which accounts for the embedded call and provides a more accurate picture of the bond's interest rate sensitivity. A 10-year callable corporate bond might have an effective duration of 5–7 years, because the call option compresses its price appreciation.

## The timing of calls: refinancing thresholds

Issuers do not call bonds the instant it is profitable; they typically call when the bond price is 3–5% above the call price, reflecting transaction costs (legal fees, underwriting fees, etc.) of refinancing. This "refinancing threshold" varies by issuer and market conditions.

In periods of stable rates, callable bonds trade at relatively stable spreads. In volatile environments, the call option becomes more valuable, and call spreads widen, making callable bonds less attractive to new buyers.

## Alternatives and implications for investors

Investors uncomfortable with negative convexity can:
1. Buy non-callable bonds (usually paying a tighter spread, i.e., lower yield).
2. Buy shorter-maturity callable bonds, where the call option is less valuable.
3. Pair a long callable bond position with a short position in [call options](/wiki/call-option/) on the issuer, synthetically creating a non-callable bond payoff (this is sophisticated and expensive).

For a buy-and-hold investor in a callable bond, the main risk is that rates fall, the bond is called, and the investor must reinvest at lower rates. For a trader, callable bonds offer opportunities: if rates are expected to rise, a callable bond's limited downside (due to the call option) makes it attractive; if rates are expected to fall, a non-callable bond is preferable.

<div class="wiki-seealso">

### Closely related
- <a href="/wiki/callable-bond/">/wiki/callable-bond/</a> — General callability mechanics and definitions
- <a href="/wiki/corporate-bond/">/wiki/corporate-bond/</a> — Standard corporate debt structure
- <a href="/wiki/preferred-stock/">/wiki/preferred-stock/</a> — Hybrid equity-debt securities, often callable
- <a href="/wiki/call-option/">/wiki/call-option/</a> — The embedded option mechanics

### Wider context
- <a href="/wiki/bond-yield-curve-risk/">/wiki/bond-yield-curve-risk/</a> — Interest rate risk in bonds
- <a href="/wiki/convexity/">/wiki/convexity/</a> — Price-yield curve curvature
- <a href="/wiki/credit-spread/">/wiki/credit-spread/</a> — Yield premium for credit risk
- <a href="/wiki/real-estate-investment-trust/">/wiki/real-estate-investment-trust/</a> — Major issuers of callable debt
- <a href="/wiki/bond-refunding/">/wiki/bond-refunding/</a> — The issuer's motivation to call bonds

</div>