---
title: "Yield Curve Carry Trade: Borrowing Short to Lend Long"
description: "How the yield curve carry trade works: funding at short-term rates and earning long-term rates. Mechanics, profit calculation, and curve-flattening risks."
keywords:
  - yield curve carry trade explained
  - carry trade funding long-term rates
  - borrowing short lending long
  - curve carry strategy
  - interest-rate risk carry trade
  - funding risk curve flatten
image: /svg/fixed-income.svg
---

*The **yield curve carry trade** borrows at short-term interest rates and lends or invests the proceeds at longer-term rates, pocketing the difference as carry. It is among the most intuitive fixed-income trades—and one of the most dangerous when the curve flattens or inverts.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Yield Curve Carry Trade — key facts</div>

<img src="/svg/fixed-income.svg" alt="An abstract editorial mark for fixed-income markets." />

<div class="wiki-infobox-caption">Earning a spread between short and long rates, until refinancing risk strikes.</div>

|   |   |
|---|---|
| **Core idea** | Borrow short, lend long; keep the spread |
| **Carry component** | Difference between long-term and short-term yields |
| **Refinancing risk** | Must roll short-term funding; rates may spike on renewal |
| **Curve flattening risk** | Spread narrows; profit margin evaporates |
| **Typical execution** | [Repo](/repurchase-agreement/), [commercial paper](/alternative-trading-system/), [T-bills](/treasury-bill/) as funding; bonds or mortgages as investments |
| **Profit driver** | Slope of the [yield curve](/yield-curve/) and [duration](/duration/) difference |

</aside>

## The Mechanics of Yield Curve Carry

A trader executes a yield curve carry trade by exploiting the normal downward slope of the yield curve. Under typical conditions, longer-dated securities offer higher [yields](/yield-to-maturity/) than shorter-dated ones, rewarding investors for time and uncertainty. A carry trader uses this pattern as a mechanical advantage: borrow short at a low rate, invest the money in longer-dated securities at a higher rate, and collect the difference.

The simplest example: fund borrowing costs 2% on a rolling three-month basis, while the 10-year bond yields 4%. The trader buys the 10-year bond, financing it overnight or rolling 90-day instruments. If rates remain constant and the bond is held to maturity, the trader earns 2% per year in carry—pure interest-rate arbitrage. The catch is that rates are never constant, and the borrowing must be repeatedly renewed.

More formally, the carry component in basis points is the difference between the yield on the long-term investment and the funding rate, scaled for the period held. A trader borrowing at 2% and investing at 4% earns 200 basis points of carry annually. On a notional position of $100 million, that is $2 million gross. After transaction costs, funding charges, and broker fees, net carry remains significant but lower.

## Rolling Risk and the Refinancing Problem

The carry trade's vulnerability lies in the renewal of short-term funding. At any point, the trader must roll the financing—that is, pay back the maturing borrowing and take out new borrowing at the prevailing short-term rate. If short rates have risen in the interim, the carry shrinks immediately. If they spike sharply, carry can flip to loss.

Consider: a trader borrows at 2.00% for three months, locks in a 4.00% long-term investment. After three months, the short-term rate has risen to 3.50%. Refinancing is now more expensive; carry compresses from 200 basis points to 50 basis points. If short-term rates spike to 4.50% or above, carry becomes negative—the trader loses money every quarter.

This scenario is not theoretical. During the 2008 financial crisis, short-term funding markets froze; rates on overnight loans surged, and carry-trade positions across the market hemorrhaged in days. Traders and institutions that had leveraged the curve were forced to liquidate at the worst time or face margin calls. The carry trade can amplify small rate moves into large losses when [leverage](/leverage-ratio-forex/) is present.

## Curve Flattening: The Squeeze

A more insidious risk is curve flattening. The spread between short-term and long-term rates narrows over time—sometimes naturally as the cycle matures, sometimes due to central-bank action or market stress. A trader who has locked in a 200-basis-point carry spread can watch it narrow to 100 basis points, then 50 basis points, as the market re-prices the long end.

If the trader holds the long-term bond to maturity, this compression is immaterial—the stated yield is fixed. But if the trader must exit early to raise cash or meet margin requirements, the bond has declined in price (because existing bonds are now worth less when new issues offer lower yields), crystallizing losses.

Curve inversion—when short-term yields exceed long-term yields—is the carry trade's nightmare. A trader who borrowed at 2% and invested at 4% is suddenly holding a position that costs 3% to fund, while the long-term investment yields only 3.5% or less. Carry has become a small, negative business, and the volatility of rolling rates makes outcomes uncertain. Large carry positions unwind quickly in these episodes, amplifying price moves.

## Leverage and Systemic Impact

The yield curve carry trade, when executed with leverage, becomes a capital-markets stress factor. [Hedge funds](/hedge-fund/), [banks](/broker/), and proprietary traders routinely scale the trade 5-to-1, 10-to-1, or more, financing long positions and hunting for fractional-percentage returns. When funding stalls or the curve inverts, these leverage positions are forced to sell simultaneously. The fire-sale of long-dated securities can crater bond prices even in liquid, government-backed markets.

Central banks are acutely aware of this risk. When they raise short-term [interest rates](/interest-rate/) aggressively—as the [Federal Reserve](/federal-reserve/) did in 2022–2023—they deliberately aim to punish carry traders and signal that easy funding has ended. The unwind that follows has often been violent: rising loan-loss provisions, hedging losses, and equity-market volatility as leveraged investors rebalance.

## Measuring and Comparing Carry

Traders quantify carry in multiple ways. The simplest is the spot spread: the difference in [yields](/yield-to-maturity/) today. If the three-month rate is 2.50% and the 10-year is 4.25%, the carry on that maturity pairing is 175 basis points.

A more refined measure accounts for [duration](/duration/)—how sensitive the long-term bond is to rate changes. A 10-year bond with a duration of 8 years will lose roughly 0.8% in price for every 1% rise in yields. A trader financing at 2.50% earns 1.75% carry annually, but is exposed to a duration loss that could exceed carry in bad scenarios. This is why carry traders often hedge part of the rate risk by buying [put options](/put-option/) or using [interest-rate swaps](/interest-rate-swap/) to cap funding costs.

Return-on-equity calculations also matter: the trader may earn 200 basis points of carry, but if the position is financed with 10% equity and 90% debt, the equity return is 2,000 basis points—a stunning 20% annual return on capital. Leverage amplifies the carry to a target return on equity, but it also amplifies losses.

## Carry in Other Markets

The yield curve carry trade exists wherever there are term structures and funding markets. In [forex](/currency-risk/), a trader borrows in a low-yielding currency and invests in a high-yielding currency—for example, borrowing Japanese yen at 0.5% and buying Brazilian real bonds at 10%. The 950-basis-point carry is intoxicating, and has repeatedly lured vast capital into [emerging-market carry trades](/carry-trade/) that unwind explosively when risk aversion strikes.

In [equities](/stock/), a similar structure appears: borrow at a low short-term rate and hold a [dividend](/dividend/)-paying stock or [fund](/mutual-fund/) that yields 3–4%. The carry is the dividend minus the funding cost. During the 2008 crisis, equity carry trades in high-dividend names collapsed as credit markets seized.

## When Carry Works, and When It Fails

The yield curve carry trade generates consistent, low-friction returns when the curve is steep and stable. It is a core business for bank [treasury](/treasury-bill/) desks, life insurers, and [pension funds](/401k-plan/), which naturally borrow short and lend long through their business model.

It fails—sometimes spectacularly—when:

- Short-term rates rise faster than long-term rates, narrowing or inverting the curve.
- Funding markets seize, forcing margin calls or forced liquidation.
- The long-dated investment depreciates sharply (e.g., when [credit risk](/credit-risk/) spikes or rates surge unexpectedly).
- Leverage amplifies small losses into equity wipeouts.

Understanding carry is essential to reading fixed-income markets. When carry is cheap, investors are compensated for very little additional risk—a sign of complacency. When carry is expensive, funding is tight and the curve is steep—often a precursor to tightening or crisis.

## See also

<div class="wiki-seealso">

### Closely related

- [Yield Curve](/yield-curve/) — definition and shapes in different economic cycles
- [Duration](/duration/) — how bond prices respond to rate changes
- [Interest-Rate Swap](/interest-rate-swap/) — hedging tool for carry traders
- [Repurchase Agreement](/repurchase-agreement/) — the funding mechanism for carry trades
- [Curve Flattening](/yield-curve/) — when carry profit margins compress

### Wider context

- [Federal Reserve](/federal-reserve/) — setting short-term rates that start carry unwinds
- [Hedge Fund](/hedge-fund/) — major users of leverage in carry strategies
- [Credit Risk](/credit-risk/) — factor in long-term investment returns
- [Leverage Ratio](/leverage-ratio-forex/) — how much carry can amplify losses

</div>
