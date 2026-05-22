---
title: "Effective Duration"
description: "A measure of bond price sensitivity to yield changes that accounts for bonds with embedded options, like callable or putable bonds."
keywords:
  - effective duration
  - bond price sensitivity
  - callable bonds
  - embedded options
  - duration calculation
---

*An **effective duration** (or option-adjusted duration) measures how much a bond's price changes when yields move 1%, accounting for the possibility that the issuer or bondholder might exercise an embedded option (call, put, or conversion). Unlike [Macaulay duration](/wiki/macaulay-duration/), effective duration reflects the realistic price path that includes the option exercise decision.*

<aside class="wiki-infobox">

| Key fact | Detail |
|---|---|
| **Formula** | (Price if yields fall 1%) − (Price if yields rise 1%) / (2 × Initial price × Yield change) |
| **Applies to** | [Callable bonds](/wiki/callable-bond/), [putable bonds](/wiki/putable-bond/), [convertible bonds](/wiki/convertible-bond/), [mortgage-backed securities](/wiki/mortgage-backed-security/) |
| **Difference from duration** | Accounts for when options go in-the-money and holders exercise |
| **Typical range** | 2–8 years for corporate callable; 0.1–2 for MBS |
| **Computation method** | Binomial tree or Monte Carlo; most bond pricing tools calculate automatically |

</aside>

## Why Macaulay duration fails for bonds with options

A [callable bond](/wiki/callable-bond/) issued at par yields 4%, but the issuer can redeem it at par if yields fall below 3%. An investor buying the bond has sold an embedded [call option](/wiki/call-option/) to the issuer. The traditional [Macaulay duration](/wiki/macaulay-duration/) formula assumes the bondholder gets all promised coupons until [maturity](/wiki/bond-maturity-corporate/). But if yields fall and the issuer calls, the bondholder's cash flows stop early and at par—locking in the issuer's gain but not the bondholder's upside.

When interest rates fall, the callable bond's price rises less than a straight bond because of the call. The embedded option acts as a cap—as yields drop toward the call price, the bond's price momentum slows. Macaulay duration would predict a 7-year bond should gain 7% if yields fall 1%; but a callable version of the same bond might gain only 3% because the call becomes likely. Macaulay duration is dangerously high.

Effective duration corrects this by using the *actual* expected price change, not the theoretical one. If you value the callable bond and find its price rises only 3% when yields fall 1%, the effective duration is 3, even though the stated maturity is 7 years.

## Calculating effective duration

The calculation uses a binomial interest-rate tree or Monte Carlo model. The process:

1. Project future short rates under different scenarios (up and down moves with given volatility).
2. For each rate path, value the bond by working backward (discounting future coupons and principal to today).
3. At each node, check if the issuer or bondholder would exercise the option. For a callable bond, if the bond's value exceeds par, assume the issuer calls and truncate the value at par.
4. Average the results across all paths.
5. Calculate the "price if yields up 1%" and "price if yields down 1%" using the same tree.
6. Apply the duration formula.

The result is a duration that reflects the path-dependent behavior of the option. A heavily callable bond (high call probability at current rates) shows a lower effective duration than its maturity would suggest.

## Option-adjusted spread and effective duration

The same binomial tree that calculates effective duration also produces the [option-adjusted-spread](/wiki/option-adjusted-spread/) (OAS). OAS is the yield spread above Treasuries that compensates for [credit risk](/wiki/credit-risk/) and liquidity, *after* accounting for the embedded option. A callable bond might trade at 200 bp over Treasuries in OAS, but if you naively add 200 bp to the Treasury yield and calculate duration, you get a wrong answer. The correct effective duration is what the tree gave you after backing out the option value.

This is why [fund managers](/wiki/actively-managed-fund/) care about OAS for bonds with options. A 3% effective duration bond with a 200 bp OAS looks better risk-adjusted than a 5% effective duration bond with the same spread, because the shorter effective duration means less [interest-rate risk](/wiki/interest-rate-risk/).

## Effective duration of mortgage-backed securities

[Mortgage-backed securities](/wiki/mortgage-backed-security/) (MBS) embed a borrower's [prepayment option](/wiki/prepayment-risk/). When rates fall, homeowners refinance, and the MBS is repaid early at par. The effective duration of an MBS is typically 0.5–3 years despite a stated maturity of 15–30 years. When rates rise, prepayments slow and effective duration extends (called [extension risk](/wiki/extension-risk//)). When rates fall, prepayments accelerate and effective duration shortens (called [negative-convexity](/wiki/negative-convexity/)). This dynamic confuses investors who assume MBS behave like fixed-rate bonds.

A portfolio manager hedging an MBS position needs to use effective duration, not stated maturity. If the portfolio has $100M of MBS with an effective duration of 2.5, buying $2.5M of long-term Treasury futures (assuming a Treasury effective duration of 10) hedges the interest-rate risk. Using stated maturity (assume MBS at 30 years) would over-hedge and create basis risk.

## Interpreting effective duration in a rising-rate environment

When the [yield-curve](/wiki/yield-curve/) is steep and rates are low, callable bonds have low effective duration but face [extension risk](/wiki/extension-risk/) if yields rise sharply. A 2.5-year effective duration bond might suddenly behave like a 5-year bond if rates surge and the call goes deep out-of-the-money. Conversely, [putable bonds](/wiki/putable-bond/) have low effective duration when yields are high because the put is likely to be exercised; if rates fall, the put expires worthless and the effective duration extends.

This is the central risk in options-embedded bonds: effective duration is not stable across yield scenarios. A bond manager must stress-test the portfolio across multiple rate paths to understand how effective duration changes—what is called [convexity](/wiki/convexity/) risk. A callable bond has negative convexity (price appreciation is capped); a putable bond has positive convexity (price appreciation is enhanced).

## Why option-adjusted duration matters

Using the right duration measure prevents [hedging](/wiki/hedging-with-futures/) mistakes, mismatches in [asset-allocation](/wiki/asset-allocation/), and surprise losses when options go in-the-money. A portfolio manager believing the portfolio has a 4-year duration (using Macaulay on callable bonds) might hold a lot of convex risk without realizing it. When yields fall 100 bp, instead of gaining 4%, the portfolio gains only 2% because of embedded calls. An investor expecting capital appreciation is blindsided.

Effective duration is the standard in professional [fixed-income fund](/wiki/fixed-income-fund-strategy/) management. Bloomberg terminals and most [bond-pricing](/wiki/bond-price-formula/) platforms calculate it automatically. But it requires the user to input [interest-rate-volatility](/wiki/volatility-smile/) assumptions and the call/put parameters. If the bond market's volatility assumptions change, or the issuer alters call dates, effective duration must be recalculated.

<div class="wiki-seealso">

### Closely related
- [Macaulay duration](/wiki/macaulay-duration/) — The baseline duration measure for straight bonds
- [Modified duration](/wiki/modified-duration/) — Macaulay duration adjusted for yield
- [Callable bond](/wiki/callable-bond/) — Bonds with issuer call options
- [Putable bond](/wiki/putable-bond/) — Bonds with bondholder put options
- [Convexity](/wiki/convexity/) — How duration changes as yields change

### Wider context
- [Option-adjusted spread](/wiki/option-adjusted-spread/) — Spread measure that complements effective duration
- [Mortgage-backed security](/wiki/mortgage-backed-security/) — A major use case for effective duration
- [Interest-rate risk](/wiki/interest-rate-risk/) — The risk being measured
- [Bond yield curve risk](/wiki/bond-yield-curve-risk/) — How curve shape affects bonds with options

</div>
