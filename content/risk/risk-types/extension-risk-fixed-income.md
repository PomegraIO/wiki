---
title: "Extension Risk in Fixed Income"
description: "How rising interest rates slow prepayments and extend the effective duration of callable bonds and mortgage-backed securities beyond expectations."
keywords:
  - extension risk fixed income
  - callable bond extension risk
  - mortgage-backed security prepayment
  - interest rate duration risk
  - negative convexity bonds
  - prepayment risk extended duration
image: "/svg/risk.svg"
---

*The **extension risk** in fixed-income markets is the danger that rising interest rates will slow borrower prepayments on callable bonds and mortgage-backed securities, forcing investors to hold longer-duration assets than they bargained for—locking in returns that are inadequate in a higher-rate environment.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Extension Risk in Fixed Income — key facts</div>

<img src="/svg/risk.svg" alt="An abstract editorial mark for risk." />

<div class="wiki-infobox-caption">The flip side of prepayment risk: borrowers refinancing less means bonds last longer.</div>

|   |   |
|---|---|
| **What it is** | Effective maturity extends beyond expectations when rates rise and prepayments fall |
| **Affects** | Callable bonds, [mortgage-backed securities](/mortgage-backed-security/), some corporate bonds, [municipal bonds](/municipal-bond/) |
| **Root cause** | Borrowers stop refinancing when new debt costs more than the old coupon |
| **Investor impact** | Locked into lower yields for longer; price declines are magnified due to increased [duration](/duration/) |
| **Duration trap** | "Negative convexity": bond appreciates less when rates fall, depreciates more when rates rise |
| **Key metric** | Effective [duration](/duration/) (actual time to expected cash flows) vs. stated maturity |
| **Mitigation** | Use [duration](/duration/) hedges, buy shorter-maturity bonds, or accept the risk as part of the yield premium |
| **Market cycle** | Most acute when transitioning from falling to rising rate environments |

</aside>

## Why prepayments exist and why they matter

A homeowner with a 3% mortgage, when rates rise to 6%, has no incentive to refinance—the new loan would be more expensive. Conversely, when rates fall from 6% to 3%, the homeowner rushes to refinance at the lower rate. The original mortgage is paid off early (prepaid), and the lender's principal is returned ahead of schedule.

The same logic applies to callable bonds. A company that issued a 4% coupon bond when rates were high is unlikely to refinance when rates fall—why pay off the cheap debt? But if rates rise and new debt becomes expensive, the company keeps the old 4% bond outstanding. In both cases, prepayment is the borrower's rational choice to minimize its financing cost.

For the bond or mortgage investor, prepayment is a double-edged sword:

- **When rates fall:** Prepayments accelerate. The investor gets principal back early and must reinvest at lower rates (bad for the investor; this is called [prepayment risk](/mortgage-backed-security/) or "shortening risk").
- **When rates rise:** Prepayments slow or stop. The investor is stuck holding a low-coupon bond while rates have risen (bad for the investor; this is extension risk or "lengthening risk").

## The mechanism: how rates drive prepayment behavior

A mortgage-backed security (MBS) or callable bond comes with a prepayment function. The borrower can refinance whenever the economic incentive is large enough—typically when rates have fallen 50–75 basis points below the coupon (the "refi threshold").

As long as rates are above that threshold, prepayments are slow. The loan or bond has its stated maturity (e.g., 30 years for a mortgage, 10 years for a bond). But the moment rates fall below the threshold, refinancing accelerates. The effective maturity—the weighted average time to receive principal—can shrink to half the stated maturity or less.

When rates rise beyond the original coupon, the refinancing threshold is no longer in play. Borrowers have zero incentive to refinance at a higher cost. Prepayments drop to near zero (only involuntary prepayments from property sales or defaults occur). The investor's principal return, once expected in a few years, is now expected 30 years hence. The effective [duration](/duration/) (sensitivity to rate changes) extends dramatically.

## Example: the extension scenario

A 4% mortgage-backed security pays a coupon of 4% annually and has a stated maturity of 30 years. When issued, investors expect:
- If rates stay flat or rise, the security will have an effective duration of ~8–10 years and run most of its life.
- If rates fall sharply, prepayments accelerate and the effective duration contracts to ~2–3 years.

**Scenario A: Rates fall to 2%**  
Mortgage borrowers rush to refinance. Prepayments accelerate. The average loan is paid off in ~5 years instead of 30. The investor receives principal early and must reinvest at 2% yields. This is annoying (prepayment risk) but manageable: the investor understood the upside-down payoff.

**Scenario B: Rates rise to 6%**  
Mortgage borrowers hold their 4% loans and do not refinance. Prepayments slow almost completely. The investor now expects to hold the 4% security for ~30 years—locked in a 4% yield while new mortgages pay 6%. The bond's price has fallen (because its yield is now below market rates), and its effective duration has extended from 8 years to ~27 years. The investor has suffered a double loss: price depreciation plus extended duration.

## The negative convexity trap

A key feature of callable bonds and MBS is **negative convexity**: the price-yield relationship is asymmetric.

For a regular, non-callable bond:
- When rates fall 100 bps, the bond price rises by, say, 8% (high positive convexity).
- When rates rise 100 bps, the bond price falls by ~8% (symmetric).

For a callable bond or MBS:
- When rates fall 100 bps, the bond price rises by only 2–3% because prepayments accelerate and principal is returned early; the investor loses the upside (prepayment risk).
- When rates rise 100 bps, the bond price falls by 15–20% because prepayments stop, extending duration and amplifying the price decline (extension risk).

This asymmetry is a form of risk: the investor never fully participates in a rally but suffers fully in a decline.

## Historical example: the 2022 mortgage crisis

In early 2022, the Federal Reserve began raising rates aggressively. The Fed Funds Rate went from 0.25% in March to 4.25% by December. Mortgage rates jumped from 3% to 7%.

Investors who owned 3% mortgage-backed securities expected near-term refinancing as rates fell. Instead, rates soared. Refinancing came to a halt. Prepayment speeds (PSA model) dropped from 80% to near 20%, meaning the average mortgage would take 15+ years to be paid off instead of ~5 years.

The MBS price fell sharply due to the rate rise, but the damage was amplified by extension: investors were no longer holding a short-duration security but a long-duration security in a rising-rate environment. Many institutional portfolios that had hedged for prepayment risk (by shorting long-dated Treasuries, for example) were caught off-guard by extension and suffered losses on both the MBS and the short hedge.

## How duration changes with prepayment expectations

The effective duration of a callable bond or MBS is not fixed—it changes based on the expected prepayment rate.

| Rate environment | Prepayment expectation | Effective duration | Investor position |
|---|---|---|---|
| Rates well above coupon (e.g., 6% rates on 4% MBS) | Very slow; minimal refi | ~15–20 years | Locked in at 4%; extended risk acute |
| Rates near coupon (e.g., 4.2% rates on 4% MBS) | Moderate; some refi | ~6–8 years | Baseline risk |
| Rates below coupon (e.g., 2.5% rates on 4% MBS) | Rapid; heavy refi | ~2–3 years | Prepayment risk acute; cash return soon |

Notice that the bond's duration is longest precisely when rates are highest and the investor is most underwater on a price basis. This amplifies losses.

## How investors price extension risk

When buying a callable bond or MBS, sophisticated investors use **option-adjusted spread (OAS)** models that account for prepayment uncertainty and embedded options. The OAS is the yield spread over Treasuries after adjusting for the value of the embedded call option (which is owned by the borrower).

A 4% mortgage at face value might offer an OAS of 80 basis points, meaning the investor earns 80 bps more than a risk-free Treasury of comparable duration, as compensation for bearing prepayment and extension risk.

If rates rise sharply, the OAS widens (investors demand higher yield) because extension risk is now acute. The MBS price falls both because yields rise and because the OAS widens (a "double hit"). Conversely, when rates fall, the OAS compresses (yields tighten) because prepayment risk diminishes and the MBS is shorter-duration.

## Strategies to manage extension risk

**Hedging with interest-rate derivatives**  
An investor who owns MBS can hedge extension risk by buying swaptions or caps that pay off if rates rise, partially offsetting the MBS price loss. However, hedging costs money (the premium for the option), reducing yield.

**Buying shorter-maturity callable bonds**  
A 3-year callable corporate bond has much less extension risk than a 30-year MBS because its maturity is already short. If prepayments stop, the investor still gets principal back in a few years, not decades.

**Accepting the yield premium**  
Some investors accept extension risk as part of the return profile. They recognize that in a rising-rate environment, they will be hurt, but they expect to be compensated over time via higher yields. This is reasonable for investors with long time horizons who can afford to wait out poor periods.

**Monitoring prepayment speeds and rebalancing**  
Investors can track actual prepayment speeds and rebalance their portfolio as expectations change. If prepayment speeds fall sharply, signaling extension risk, they can reduce MBS holdings and buy shorter-duration bonds.

**Using inverse floaters or other structured products**  
Some investors buy inverse floaters or other structures that benefit from rising rates and extended duration, partially offsetting the extension risk of MBS or callable bonds. However, these products are complex and can backfire in certain scenarios.

## Extension risk in different fixed-income sectors

**Mortgage-backed securities (agency and non-agency)**  
Extension risk is most acute here because homeowners have the strongest refinancing incentive and are most sophisticated about rate changes. A 30-year maturity combined with unpredictable prepayment makes duration highly variable.

**Callable corporate bonds**  
Companies also refinance when rates fall, but corporate bonds are often sold with non-call periods (typically 3–5 years before the call can be exercised). This limits extension risk on newer bonds. Older callable corporates with deep in-the-money calls can have significant extension risk.

**Municipal bonds**  
Many municipal bonds are callable, especially advance-refunded bonds and GO bonds. Extension risk applies similarly to corporates and MBS.

**Floating-rate bonds**  
Floating-rate notes have minimal extension risk because the coupon adjusts with rates. If rates rise, the coupon rises, so price stays near par. There is little incentive for the borrower to refinance a floater at a higher rate (it will just reset higher anyway).

## The relationship to duration and convexity

Extension risk is inseparable from the concept of [duration](/duration/). A bond's duration measures sensitivity to rate changes, but duration itself changes as prepayment expectations change. This is why measuring duration is difficult for callable bonds.

The negative convexity of callable bonds means that the usual duration calculation (which assumes constant duration) understates the price decline in a rising-rate environment. Investors must use effective duration (which accounts for prepayment scenarios) or monte-carlo-based OAS models to capture the full risk.

## See also

<div class="wiki-seealso">

### Closely related

- [Duration](/duration/) — the measure of interest-rate sensitivity that extension risk modifies
- [Mortgage-Backed Security](/mortgage-backed-security/) — the primary instrument exposed to extension risk
- [Callable Bond](/callable-bond/) — bonds with embedded refinancing options
- [Prepayment Risk](/mortgage-backed-security/) — the flip side of extension risk
- [Option-Adjusted Spread](/option-adjusted-spread/) — the pricing framework that accounts for extension
- [Interest-Rate Risk](/interest-rate-risk/) — the broader category of risk that includes extension

### Wider context

- [Interest Rate](/interest-rate/) — the driver of prepayment behavior
- [Bond](/bond/) — foundational fixed-income instrument
- [Hedging](/derivatives-hedging/) — strategies to mitigate extension exposure
- [Credit Risk](/credit-risk/) — separate from extension risk; both affect MBS and callable bonds
- [Convexity](/duration/) — the mathematical concept underlying negative convexity

</div>
