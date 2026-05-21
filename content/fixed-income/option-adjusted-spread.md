---
title: "Option-Adjusted Spread (OAS)"
description: "Option-adjusted spread is the credit spread of a bond adjusted to exclude the value of embedded options like call or conversion features."
keywords:
  - option-adjusted spread
  - OAS
  - credit spread
  - callable bonds
  - option value
image: "https://picsum.photos/seed/option-adjusted-spread/900/600"
---

*The **option-adjusted spread** — or **OAS** — is a [bond](/bond)'s [credit spread](/credit-spread) adjusted to exclude the value of embedded options. For a [callable bond](/callable-bond), OAS removes the value of the call option to isolate the pure credit risk premium. A [callable bond](/callable-bond) might have a 150-basis-point simple spread but an 100-basis-point OAS, with 50 basis points attributable to the call option.*

<div class="wiki-hatnote">

For the simple spread unadjusted for options, see [credit spread](/credit-spread). For callable bonds, see [callable bond](/callable-bond). For convertible bonds, see [convertible bond](/convertible-bond).

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Option-Adjusted Spread — key facts</div>

<img src="https://picsum.photos/seed/option-adjusted-spread/900/600" alt="A calculation showing how OAS is derived from simple spread and option value" />

<div class="wiki-infobox-caption">OAS isolates credit risk by removing the value of embedded options.</div>

|   |   |
|---|---|
| **What it is** | Credit spread minus option value |
| **Formula** | Simple spread = OAS + option value |
| **Applies to** | [Callable bonds](/callable-bond), [convertible bonds](/convertible-bond), MBS |
| **Calculation** | Model-based; requires assumptions about volatility |
| **Callable bonds** | OAS < simple spread (call reduces investor return) |
| **Putable bonds** | OAS > simple spread (put increases investor return) |
| **Use case** | Comparing bonds with different options fairly |

</aside>

## Why OAS matters

Consider two 10-year corporate bonds:
- Bond A: 5% coupon, not callable, 150-basis-point spread, 150-basis-point OAS
- Bond B: 6% coupon, callable in 3 years, 150-basis-point spread, 100-basis-point OAS

Both have the same simple 150-basis-point spread, but Bond A has higher OAS because it lacks the call option. Bond B's spread is partly compensation for credit risk (100 bps OAS) and partly compensation for the call option (50 bps option value).

If an investor buys either bond, Bond A offers more credit compensation (150 bps) while Bond B offers less (100 bps) plus a call option.

For credit analysis, OAS is the relevant metric — it isolates the pure credit compensation.

## Calculation and volatility

OAS calculation requires modeling the bond's value under many different interest-rate scenarios. The model must:

1. Generate future interest-rate paths (under volatility assumptions)
2. Calculate the bond's value under each path (accounting for the call/put option)
3. Find the constant spread that equates the bond's price to the average of those values

This is computationally complex, which is why OAS calculation is delegated to pricing systems and specialists.

The OAS calculated is sensitive to volatility assumptions. High volatility increases the value of [call options](/callable-bond) (call value rises), reducing OAS. Low volatility reduces option value, increasing OAS.

## Callable bond OAS

For a [callable bond](/callable-bond), the OAS is lower than the simple spread because the call option reduces the bondholder's return. The bondholder receives the OAS spread, but the issuer's call option extracts value.

When a bond is called, the bondholder's coupon income ceases and reinvestment occurs at lower rates — a loss. This loss is implicit in the option value, which reduces OAS.

## Putable bond OAS

For a [putable bond](/putable-bond), the OAS is higher than the simple spread because the put option increases the bondholder's return. The bondholder receives the OAS spread plus the value of the put option.

A put option allows redemption at par if credit deteriorates, protecting the bondholder. This protection has value, increasing OAS relative to simple spread.

## MBS and OAS

[Mortgage-backed securities](/mortgage-backed-security) have [prepayment risk](/mortgage-backed-security) similar to [call risk](/callable-bond). When rates fall, homeowners refinance, returning principal early. OAS accounts for this [prepayment risk](/mortgage-backed-security).

An MBS might have a 120-basis-point simple spread but 80-basis-point OAS, with 40 basis points reflecting the [prepayment option](/mortgage-backed-security) value.

## Z-spread vs. OAS

The **Z-spread** (zero-volatility spread) is a simpler spread measure that doesn't model options. It's the constant spread that equates the bond's price to the present value of its cash flows using non-parallel yield curve shifts.

OAS is more sophisticated — it models interest-rate volatility and option exercise — making it more appropriate for bonds with options.

## OAS indices and tracking

Bloomberg and other providers publish OAS indices for corporate and other bond markets:

- **Investment-grade OAS index** — tracks spread of [investment-grade bonds](/investment-grade-bond)
- **High-yield OAS index** — tracks [high-yield bonds](/high-yield-bond)
- **MBS OAS** — tracks [mortgage-backed securities](/mortgage-backed-security)

These indices help investors gauge market credit conditions independent of option value.

## Using OAS in portfolio management

Bond managers compare OAS across bonds to identify:

- **Attractive credit valuations** — Higher OAS means more credit compensation (all else equal)
- **Option risk** — Callable bonds with tight OAS might be overpriced (option value is high)
- **Market dislocations** — Bonds with abnormal OAS relative to credit rating might be misprice

A sophisticated manager might:
- Buy high-OAS bonds (good credit compensation)
- Sell low-OAS bonds (poor credit compensation)
- Avoid callable bonds with tight OAS (overpriced options)

## See also

<div class="wiki-seealso">

### Closely related

- [Credit spread](/credit-spread) — simple spread unadjusted for options
- [Callable bond](/callable-bond) — exhibits call option reducing OAS
- [Putable bond](/putable-bond) — exhibits put option increasing OAS
- [Mortgage-backed security](/mortgage-backed-security) — prepayment option reduces OAS
- [Convertible bond](/convertible-bond) — conversion option affects spread

### Wider context

- [Credit rating](/credit-rating) — determines credit compensation
- [Volatility](/stock) — affects option values and OAS
- [Interest rate](/interest-rate) — drives option exercise
- [Bond portfolio management](/hedge-fund) — OAS-based management
- [Risk management](/diversification) — OAS helps identify option risk

</div>
