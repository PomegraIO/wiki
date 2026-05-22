---
title: "Floating Rate Bond Mechanics"
description: "Bond structure where coupon adjusts periodically based on a reference rate (SOFR, LIBOR, Treasury) plus a fixed spread, isolating interest-rate risk."
keywords:
  - floating rate bonds
  - SOFR reference
  - coupon adjustment
  - interest rate risk
---

*A **floating rate bond** has a coupon that resets every 3 or 6 months based on a [reference rate](/wiki/libor/) (most commonly [SOFR](/wiki/sofr/)) plus a fixed spread, allowing the bond's yield to rise or fall with prevailing [interest rates](/wiki/interest-rate/) and isolating the bondholder from [duration](/wiki/duration/) risk.*

<div class="wiki-hatnote">
Distinct from fixed-rate bonds, which have coupons locked at issuance, and from perpetual bonds, which have no maturity date.
</div>

<aside class="wiki-infobox">

| Aspect | Detail |
|--------|--------|
| **Coupon formula** | Reference rate + fixed spread (often 1–2%) |
| **Reset frequency** | Every 3 or 6 months (quarterly or semi-annual) |
| **Reference rate** | SOFR (US), EURIBOR (EU), SONIA (UK), or Treasury |
| **Spread component** | Fixed at issuance, reflects credit risk |
| **Duration** | Very short (0.1–0.5 years), compared to fixed bonds (3+ years) |
| **Price volatility** | Low; bond prices change mainly when spread widens/tightens |
| **Yield advantage** | Lower initial yield than fixed bonds (lower duration premium) |
| **Common issuers** | US Treasuries (floating-rate notes), investment-grade corporates, mortgages |

</aside>

## How coupon resets work: SOFR plus spread

A floating-rate bond pays coupon = [SOFR](/wiki/sofr/) + 200 basis points. If [SOFR](/wiki/sofr/) is currently 5%, the bondholder receives 7% annually (100 basis points = 1%). Every six months, the coupon is recalculated: if [SOFR](/wiki/sofr/) falls to 4%, the coupon drops to 6%. This mechanism insulates the bondholder from [interest rate](/wiki/interest-rate/) risk—when rates rise, coupons rise, preventing bond prices from falling sharply. In a fixed-rate bond, rising rates mean the bond's price falls (because new bonds with higher coupons now compete). Floating-rate bonds avoid this—their coupons simply adjust upward, keeping prices near par (face value).

## Reference rate evolution: LIBOR to SOFR transition

For decades, **LIBOR** (London Interbank Offered Rate) was the benchmark. Banks self-reported the cost of borrowing; the reported rates were averaged to compute LIBOR. However, LIBOR was easily manipulated (wide discretion in reporting), and a 2012 scandal revealed widespread rate-fixing. Regulators demanded a shift to transaction-based rates. The **[SOFR](/wiki/sofr/)** (Secured Overnight Financing Rate), launched in 2018, is calculated from actual repurchase agreements (repo transactions), making it manipulation-proof. The US Treasury and Fed mandated SOFR for new floating-rate debt; old LIBOR contracts were "tough legacy" (still in use but slated for phase-out by 2024 in most markets). Many floating-rate notes issued before 2020 used LIBOR; these are gradually maturing or being refinanced at SOFR.

## Spread mechanics and credit risk

The **spread** (the fixed percentage above the reference rate) reflects issuer credit quality. A AAA-rated bond might trade at SOFR + 50 basis points; a BBB-rated bond at SOFR + 200 basis points. This spread doesn't reset—it's locked at issuance and doesn't change even if the issuer's credit rating changes. This means a bond issued at SOFR + 50 bp could widen to SOFR + 150 bp in the secondary market if the issuer's credit deteriorates. However, on the reset date, the coupon still uses the original 50 bp spread. This structure isolates the reference-rate reset from credit-spread risk—the coupon floats with rates, but the spread is fixed.

## Price volatility and duration

A fixed-rate 10-year bond has a duration of ~8 years—a 1% rise in yields triggers an ~8% price decline. A floating-rate bond reset every 6 months has a duration of ~0.25 years (6 months ÷ 2)—the same 1% yield rise causes a ~0.25% price decline. This ultra-low duration makes floating-rate bonds nearly risk-free in terms of interest-rate moves. However, the trade-off is yield: because investors pay less for duration risk, floating-rate bonds offer lower coupons than fixed-rate bonds. A 10-year fixed-rate bond might yield 5%; a floating-rate bond might yield SOFR + 100 bp (currently ~6%, but only because SOFR is elevated).

## Negative convexity and cap features

Some floating-rate bonds have **caps** (maximum coupon) and **floors** (minimum coupon). A bond paying SOFR + 200 bp with a 7% cap means the coupon never exceeds 7%, even if SOFR + spread would suggest 10%. This benefits the issuer (capping liabilities in a high-rate environment) but hurts the bondholder (upside capped). Similarly, a floor ensures the coupon never falls below some level (e.g., 3%), protecting the bondholder in a low-rate scenario but limiting issuer upside. Bonds with caps have **negative convexity**—as rates rise beyond the cap, the bond behaves like a fixed-rate bond (price falls). This was a major issue during the 2022 rate hike: floating-rate corporate bonds with low caps underperformed because investors feared the capped coupons.

## When floating-rate bonds outperform: rising-rate environments

In 2022–2024, when [interest rates](/wiki/interest-rate/) rose sharply, floating-rate bonds outperformed fixed-rate bonds. A bondholder holding a SOFR + 200 bp bond saw coupons jump from 3% to 7% as SOFR rose—capturing the full benefit of higher rates. A fixed-rate bondholder with a 3% coupon saw bond prices collapse. Floating-rate bonds are thus [interest-rate hedges](/wiki/interest-rate-hedging/)—ideal for investors who view rising rates as likely or who want to lock in current spread premiums while avoiding duration losses. This is why central banks hold floating-rate debt and why pension funds with inflation concerns favor them.

## Basis risk: spread vs. rate moves

Floating-rate bonds are protected against [reference rate](/wiki/libor/) changes but exposed to **spread risk**—the margin above the reference rate can widen or tighten based on credit conditions and market demand. During the 2008 financial crisis, spreads widened 500+ basis points for corporate floating-rate bonds, even as SOFR (then LIBOR) fell—a double whammy for investors (coupons fell, but bond prices fell further due to spread widening). This **[basis risk](/wiki/basis-risk/)** is the main danger with floating-rate debt. Low-credit-quality issuers' floating-rate bonds are riskier than they appear; spreads can blow out rapidly.

## Application in mortgages and adjustable-rate debt

Adjustable-rate mortgages (ARMs) are consumer-level floating-rate debt—the rate resets annually or every few years. A borrower locking in an ARM rate of SOFR + 250 bp enjoys lower initial rates than a 30-year fixed mortgage but faces rate-hike risk after the initial period. During 2022–2023, ARMs reset upward sharply, straining borrowers. This illustrates the distribution of interest-rate risk: the lender (mortgage servicer) is hedged by floating rates; the borrower bears the risk. Understanding this risk distribution is key to personal finance decisions.

## Portfolio role and duration management

Floating-rate bonds serve as cash substitutes or duration hedges. A pension fund with a 5-year [liability duration](/wiki/duration/) might hold 3-year fixed bonds + 2-year floating bonds to match. If rates rise, the floating bonds' coupons rise, offsetting the [interest-rate risk](/wiki/interest-rate-risk/) on the fixed bonds. Alternatively, institutions use floating-rate bonds to park excess cash while earning a spread premium over cash. Since [SOFR](/wiki/sofr/) rates now closely track Fed [overnight](/wiki/federal-funds-rate/) rates, floating-rate bonds offer competitive short-term yields—typically 20–100 basis points above cash.

<div class="wiki-seealso">

### Closely related
- [Floating Rate Note](/wiki/floating-rate-note/) — US Treasury floating-rate instrument
- [SOFR](/wiki/sofr/) — primary reference rate (post-LIBOR)
- [LIBOR](/wiki/libor/) — legacy reference rate
- [Bond](/wiki/bond/) — foundational bond concepts
- [Interest Rate Risk](/wiki/interest-rate-risk/) — what floating-rate bonds hedge

### Wider context
- [Duration](/wiki/duration/) — measure of price sensitivity
- [Spread](/wiki/credit-spread/) — credit component of coupon
- [Basis Risk](/wiki/basis-risk/) — residual spread risk
- [Callable Bond](/wiki/callable-bond/) — related structure with early redemption
- [Adjustable Rate Mortgage](/wiki/adjustable-rate-mortgage/) — consumer equivalent
- [Interest Rate Hedging](/wiki/interest-rate-hedging/) — portfolio application

</div>