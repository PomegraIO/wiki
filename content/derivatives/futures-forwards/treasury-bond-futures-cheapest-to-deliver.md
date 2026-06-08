---
title: "Treasury Bond Futures: Cheapest-to-Deliver Bond"
description: "T-bond futures contracts allow delivery of multiple qualifying bonds. The conversion factor system creates arbitrage; the short selects the cheapest to deliver."
keywords:
  - treasury bond futures cheapest to deliver bond
  - conversion factor treasury futures
  - cft bond delivery
  - bond futures arbitrage
image: "/svg/derivatives.svg"
---

*The short seller in a Treasury [bond](/bond/) [futures](/futures-contract/) contract can deliver any bond meeting maturity and coupon specifications. The **conversion factor** system attempts to equalize returns across bonds, but price differences remain. The short side exploits this by computing the net-cash delivery cost and choosing the **cheapest-to-deliver** (CTD) bond—the choice with the lowest actual cost.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">T-Bond Futures Delivery — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives." />

<div class="wiki-infobox-caption">A mismatch between standardized pricing and real cash bonds creates a consistent arbitrage: the short picks the bond it costs least to deliver.</div>

|   |   |
|---|---|
| **Futures contract** | CME 30-year U.S. Treasury futures; contract size $100,000 face value |
| **Deliverable universe** | Any non-callable T-bond with 15–25 years to maturity (or call date), coupon ≥ 6% |
| **Conversion factor (CF)** | Standardized factor applied to each eligible bond to adjust for coupon and time-to-maturity differences |
| **Delivery price to long** | (Futures settlement price) × (Conversion factor) + accrued interest |
| **Cheapest-to-deliver** | Bond with minimum: (spot price) - (futures price × CF + accrued interest) |
| **CTD identification** | Requires daily calculation of net cash cost for each eligible bond; CTD shifts as yields and prices change |
| **Profit to short** | Repo rate and financing costs minus the CTD advantage; arbitrage drives futures prices toward fair value |
| **Practical impact** | CTD often has lower coupon and longer duration; long futures investors are implicitly long a proxy bond, not the whole basket |

</aside>

## The standardization problem

A 30-year Treasury [futures](/futures-contract/) contract is a commitment to deliver $100,000 face value of a U.S. Treasury bond. But which bond? There are dozens outstanding—different issuance dates, coupons (4%, 5%, 6%, 7%+, etc.), and maturities.

If the contract specified a single bond (e.g., "the 5% bond due 2054"), futures traders could avoid the standard by simply holding that one bond in stock, and delivery arbitrage would be impossible. The market would be illiquid.

Instead, the CME allows **multiple eligible bonds** to be delivered against the contract. The rules specify: any non-callable U.S. Treasury bond with 15–25 years to maturity (or years until first call date for callable bonds), coupon of at least 6%.

This broadens the deliverable universe and ensures liquidity, but it creates a problem: bonds with different coupons and maturities have different [duration](/duration/) and convexity. A bond with a 3% coupon and 20 years to maturity behaves very differently from a 7% coupon, 18-year bond when yields shift.

The **conversion factor** (CF) is meant to solve this.

## How the conversion factor works

Each eligible bond receives a **conversion factor**—a multiplier that standardizes the bond's price for delivery purposes.

The conversion factor is computed as if the bond were priced to yield 6% (the historical "par coupon" for futures contracts). If a bond has a 4% coupon and 20 years to maturity, its CF will be less than 1.0 (because it trades at a discount); a bond with an 8% coupon will have a CF greater than 1.0 (because it trades at a premium).

Example: suppose the 4% coupon bond has CF = 0.82, and the 8% coupon bond has CF = 1.15.

If the futures contract settles at 130 (i.e., $130,000 for a $100,000 face value bond), the delivery price to the long is:

- **4% bond**: $130,000 × 0.82 + accrued interest = $106,600 + accrued ≈ $106,850
- **8% bond**: $130,000 × 1.15 + accrued interest = $149,500 + accrued ≈ $149,750

The short side (whoever is short the futures and must deliver) will deliver the 4% bond because it costs less to acquire in the spot market (it actually trades at a discount to par, unlike the 8% bond).

The conversion factor is designed to neutralize coupon and duration differences, making all deliverable bonds economically equivalent to the short. In a perfect world, the short would be indifferent about which bond to deliver.

But the conversion factor is computed at a fixed 6% yield assumption. When actual market yields differ from 6%, the CF's neutralization breaks down.

## When conversion factors fail: the CTD emerges

The CTD bond emerges because the conversion factor is calculated at a fixed yield, and actual market yields fluctuate.

When market yields are above 6%, bonds with lower coupons (e.g., 3% or 4%) trade at steeper discounts relative to the 6% assumption. Their CF adjusts down, but not enough to offset their spot price discount. To the short side, these low-coupon bonds are cheaper to acquire and deliver.

When market yields are below 6%, high-coupon bonds (7%+) command premiums; the CF does not fully capture this. They become more expensive to deliver.

The short side computes a **"delivery cost"** or **"implied repo rate"** for each eligible bond:

Delivery cost = Spot price - [(Futures settlement price) × CF + Accrued interest]

The bond with the **lowest (most negative)** delivery cost is the cheapest to deliver. By delivering that bond, the short maximizes profit (or minimizes loss).

For example, if the spot price of the 4% bond is $104,000 and the futures settlement (after multiplying by CF) implies a delivery price of $106,850, the delivery cost is negative: $104,000 - $106,850 = -$2,850 (profit to the short). If the 8% bond has a spot price of $150,000 and delivery price of $149,750, the delivery cost is positive: $150,000 - $149,750 = $250 (loss to the short). The 4% bond is the CTD.

## Which bond is likely to be CTD?

The identity of the CTD bond depends on the **yield curve shape** and **level**.

When yields are high and the curve is steep, long-dated, low-coupon bonds are cheap relative to the conversion factor adjustment. These bonds are likely CTD. They have long duration, so their price sensitivity to yield changes is high.

When yields are low and the curve is flat or inverted, high-coupon bonds may be CTD (or bonds with shorter remaining time to maturity, which are less price-sensitive).

In practice, the CTD bond often has a below-average coupon (4–5% in recent years) and longer duration, because the conversion factor system biases the short side toward such bonds when rates are above the 6% assumption.

The CTD identity **shifts constantly** as yields and spot prices change. A bond that is CTD on Monday may not be CTD on Friday. Risk managers and traders must recalculate daily (or intraday) to know which bond the short side would actually deliver.

## Implications for long and short

**For the long** (buyer of the futures), this is important: you are not buying a specific bond. You are buying the right to receive whichever bond the short chooses to deliver. That turns out to be the CTD bond. So your effective long position is a long position in the CTD bond and (implicitly) short the curve shape that keeps it as CTD.

If the curve flattens or the CTD identity changes, your effective exposure shifts. This is **delivery-related basis risk**: you thought you were buying a general long-bond exposure, but you got a specific bond with specific duration and convexity.

**For the short**, the CTD is a huge advantage. By choosing the least expensive bond to deliver, the short can extract value from the futures contract. This is where the arbitrage profit lives.

## The implied repo rate and financing cost

A sophisticated short side (a dealer or hedge fund) will not simply compute the spot-futures price difference; they will also factor in **financing costs**.

To execute a "cash-and-carry" arbitrage:
1. Borrow money at the repo rate to buy the CTD bond in the spot market
2. Short the futures contract
3. Hold the bond, collect coupon
4. Deliver against futures at the agreed price
5. Return borrowed funds plus repo interest

Profit = (Futures price × CF + accrued interest) - (Spot price) - (Repo financing cost) + (Coupon collected while holding)

This profit is called the **implied repo rate**. If it exceeds the actual repo rate the trader can borrow at, the arbitrage is profitable.

The implied repo rate for the CTD bond sets a floor on futures prices. If futures are priced too high (implying a high repo rate), traders will buy CTD bonds and short futures, pulling down the futures price. If futures are too cheap, the reverse arbitrage unwinds.

## Practical trading and risk

Professional traders use CTD analysis to:

- **Price the futures contract fairly** by computing the cost of financing and delivering the CTD bond
- **Hedge bond portfolios** by shorting futures against long cash bond positions, adjusting notional size for the CTD's duration
- **Spot mispricing** when the implied repo rate for a specific bond is unusually high or low, suggesting arbitrage opportunity
- **Manage curve risk** by noting which bonds are CTD and therefore more sensitive to curve shape changes

For portfolio managers, the CTD shift is a risk. If you are long bonds and short an equivalent amount of futures (a classic hedge), your hedge breaks if a different bond becomes CTD. The new CTD might have different duration, and your hedge ratio is suddenly wrong.

## See also

<div class="wiki-seealso">

### Closely related

- [Futures Contract](/futures-contract/) — standardized contracts and delivery mechanics
- [Forward Contract](/forward-contract/) — over-the-counter alternative to exchange-traded futures
- [Duration](/duration/) — sensitivity of bond prices to yield changes; critical to CTD selection
- [Basis](/basis/) — spot-futures price difference that drives CTD arbitrage
- [Repurchase Agreement](/repurchase-agreement/) — short-term borrowing used in carry arbitrage
- [Bond](/bond/) — fundamentals of U.S. Treasury structure and pricing

### Wider context

- [Treasury Bill](/treasury-bill/) — shorter-dated Treasury debt instruments
- [Treasury Bond](/treasury-bond/) — the underlying cash instrument for the futures
- [Yield Curve](/yield-curve/) — shapes CTD identity by affecting relative bond values
- [Hedge Fund](/hedge-fund/) — sophisticated practitioners of CTD arbitrage strategies

</div>
