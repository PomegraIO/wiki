---
title: "Valuing Preferred Stock with the Dividend Discount Model"
description: "The dividend discount model values preferred stock as a perpetuity; adjustments account for callability, cumulative arrears, and conversion features."
keywords:
  - dividend discount model preferred stock
  - preferred stock valuation
  - perpetuity dividend model
  - callable preferred stock
  - cumulative preferred dividend
  - perpetuity formula valuation
  - preferred stock pricing
image: /svg/valuation.svg
---

*Preferred stock occupies the middle ground between bonds and equity: it pays a fixed [dividend](/dividend/) (like a bond coupon), but has no maturity date and lower priority in bankruptcy. The **dividend discount model for preferred stock** simplifies to a perpetuity formula, but real-world adjustments for callability, arrears, and conversion terms are essential to avoid overpaying.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Valuing Preferred Stock with DDM — key facts</div>

<img src="/svg/valuation.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Preferred stock DDM is a perpetuity; the issuer's call option reduces fair value.</div>

|   |   |
|---|---|
| **Core formula** | V = D / r, where D is the annual dividend and r is the required return |
| **Perpetuity assumption** | Preferred stock has no maturity; dividends continue indefinitely (unless called) |
| **Required return** | Blends credit spread, equity risk premium, and interest-rate risk; typically 4–8% for investment-grade issuers |
| **Call feature** | Almost all preferred stock is callable; issuer will exercise if rates fall, capping upside for buyer |
| **Cumulative arrears** | Missed dividends accrue as a liability; buyer inherits risk of payment delays |
| **Conversion** | Convertible preferreds trade as equity-bond hybrids; use option-adjusted valuation |

</aside>

## The Perpetuity Formula for Non-Callable Preferred Stock

Unlike common stock, whose value depends on uncertain future earnings, or bonds, which mature at a stated date, preferred stock pays a known dividend in perpetuity. This simplicity makes the [dividend discount model](/dividend-discount-model/) the natural tool.

The formula is:

$$V = \frac{D}{r}$$

where *V* is the fair value, *D* is the annual dividend per share, and *r* is the required annual return (discount rate).

**Example:** A preferred stock paying $5 per share annually. If your required return is 5%, fair value is $5 / 0.05 = $100. If required return rises to 6%, fair value falls to $5 / 0.06 = $83.33.

This inverse relationship between required return and value is critical: when interest rates rise or credit spreads widen, required returns increase, and preferred stock prices fall sharply. Conversely, in a falling-rate environment, preferred stock rallies.

## Estimating the Required Return

The required return *r* reflects three components:

**Risk-free rate:** Start with U.S. Treasury yields. A 10-year Treasury at 4% provides a baseline.

**Credit spread:** The issuer's financial condition determines how much extra yield you demand above the risk-free rate. A stable bank might have a 200–300 basis point spread; a struggling utility might be 400–600 basis points; a speculative issuer might be 800+ basis points.

**Equity risk premium:** Preferred stock is subordinated to bonds but senior to common equity. If you think the company's equity risk premium (the return you'd demand to own common stock) is 6%, preferred stock might warrant 3–4% (lower, because it's senior and has a fixed payment).

**Sum:** For a stable bank issuer: 4% (risk-free) + 2.5% (credit) + 1% (equity subordination) = 7.5% required return. Using the perpetuity formula with a $5 dividend: V = $5 / 0.075 = $66.67.

## Callable Preferred Stock: The Real-World Discount

Nearly all preferred stock issued by corporations is callable—the issuer can force redemption at a set price (usually par) after a date or at the issuer's discretion.

From the buyer's perspective, the call is a problem. If you buy a preferred at $98 with a 5% dividend (paying $5 annually) and rates fall, the issuer calls it away at $100. You get par back but lose the high-yielding stream. The price of the preferred doesn't rally much even if rates fall sharply, because the issuer will call if it becomes profitable.

**The option-adjusted approach:** Treat the call as an embedded short call option on the preferred. The fair value is the perpetuity value minus the value of the call option.

$$V_{\text{preferred}} = \frac{D}{r} - \text{Call Option Value}$$

The call option value depends on:
- **How far above the call price the preferred trades.** If the preferred trades at $102 and the call price is $100, there's $2 of "in-the-money" value—immediate loss if called.
- **Interest-rate volatility.** Higher volatility means the call option is worth more (more upside scenarios where rates fall and the call is exercised). Higher volatility reduces the preferred's value.
- **Time to call date.** A call available immediately is more valuable than one 10 years hence.

**Practical rule:** For an "at the money" callable preferred (trading near par), assume the call reduces fair value by 5–15% from the perpetuity value, depending on rate volatility.

## Adjusting for Cumulative Arrears

A preferred stock can be cumulative or non-cumulative. Cumulative means if the company suspends the dividend, the amount owed accumulates and must be paid in full before common shareholders receive anything.

During a financial crisis or restructuring, some preferred holders face deferred dividends. If a preferred promises $5 annually and dividends are suspended for 2 years, $10 of arrears accrue. When the company resumes payments, it must pay the $10 arrears before continuing regular dividends.

**Valuation impact:** If you're buying a preferred with known arrears:
1. Adjust *D* upward by the deferred amount. If $5 annual dividend is standard and $10 is owed, use $15 in the numerator (this year's dividend plus the catch-up).
2. Discount for the probability and timing of payment. If payment is uncertain, apply a default probability and recovery rate similar to distressed [credit-default-swap](/credit-default-swap/) analysis.

A preferred with $10 in arrears on a $5 annual stream might be valued at ($5 + $10 weighted for risk) / 0.08 = $150–$180, well below par ($100), reflecting the risk that arrears are never fully paid.

## Convertible Preferred Stock

Some preferred stock is convertible into common shares at a fixed price. This adds equity optionality.

If a preferred paying $5 annually is convertible into common stock worth $50, and the conversion ratio is 1 share, the buyer has a choice: hold the preferred for steady $5 annual payments, or convert and hope for capital appreciation on the common stock.

Valuation requires a hybrid approach:
- Value the bond floor (perpetuity of $5 dividends).
- Add the option value of converting into common stock.
- Use a similar framework to option-adjusted spreads on convertible bonds.

In practice, convertible preferreds trade closer to common stock than traditional preferreds, especially if the common stock is volatile or has strong growth expectations.

## Building a Valuation Table

Consider comparing several preferred-stock issues with different call dates and credit spreads:

| Issuer | Dividend | Call Date | Required Return | Perpetuity Value | Estimated Call Value | Fair Value |
|--------|----------|-----------|-----------------|------------------|----------------------|------------|
| Bank A | $5.50 | 2027 | 5.5% | $100 | $3 | $97 |
| Bank B | $6.00 | 2028 | 6.2% | $96.77 | $5 | $91.77 |
| Utility C | $5.00 | Perpetual | 4.8% | $104.17 | $0 | $104.17 |

Bank A's callable preferred looks fairly valued if it trades near $97. Bank B's discount to perpetuity value reflects the near-term call risk. Utility C, being non-callable (or with a very distant call), captures the full perpetuity value.

## Interest-Rate Sensitivity

Preferred stock is sensitive to interest-rate changes, but less so than bonds (because there's no maturity) and more so than common stock (because the payment is fixed).

A 100 basis-point rise in required returns causes a preferred paying $5 to fall from $100 (at 5%) to $83.33 (at 6%)—a 16.7% loss.

For comparison, a 10-year bond with a 5% coupon loses roughly 8% in the same scenario. Preferred stock sits between equity (which might rise or fall based on earnings) and bonds (shorter duration).

This sensitivity is highest for non-callable preferreds trading well above par and lowest for trading near the call price.

## Practical Valuation Checklist

1. **Identify the annual dividend and its permanence.** Is it stated as a percentage of par, a fixed dollar amount, or floating? Is it cumulative or non-cumulative?
2. **Estimate the required return.** Use comparable preferred spreads, credit ratings, and the current risk-free rate.
3. **Calculate perpetuity value.** V = D / r.
4. **Estimate the call-option drag.** If callable before 5 years, reduce value by 5–15%.
5. **Adjust for arrears.** If dividends are deferred, add a weighted-for-risk catch-up to *D*.
6. **Compare to market price.** If your fair value is $85 and it trades at $75, it may be attractive; if it trades at $90, it may be rich.

## See also

<div class="wiki-seealso">

### Closely related

- [Dividend discount model](/dividend-discount-model/) — foundational perpetuity and finite-term models
- [Preferred stock](/preferred-stock/) — structure, rights, and seniority of preferred equity
- [Callable bond](/callable-bond/) — debt analog with embedded call option reducing fair value
- [Dividend](/dividend/) — fixed payments and policy; contrast with growth expectations
- [Credit spread](/credit-spread/) — how to estimate the risk premium in required return
- Option-adjusted spread — framework for valuing bonds and convertibles with embedded options

### Wider context

- Valuation — broader methods for equity, debt, and hybrid instruments
- Perpetuity formula — mathematical foundation for preferred valuation
- [Interest rate risk](/interest-rate-risk/) — why preferred stock prices move when rates change
- [Default rate](/default-rate/) — credit risk affecting required return and fair value

</div>
