---
title: "DeFi Lending Interest Rate Models"
description: "DeFi lending interest rate models automatically adjust borrow and supply APY as pool utilization rises and falls, balancing supply and demand."
keywords:
  - defi lending interest rate model
  - utilization-based rates
  - apy curve defi
  - aave interest model
  - defi borrowing rates
image: /svg/crypto.svg
---

*A **DeFi lending interest rate model** is an automated formula that sets the borrow and supply interest rates on a lending protocol based on the utilization rate of the pool—the ratio of borrowed assets to total assets available for lending. As utilization rises, rates increase algorithmically to incentivize deposits and discourage further borrowing, keeping the pool solvent. Unlike traditional banks, which set rates through manual discretion, DeFi protocols use mathematical curves that respond instantly to market conditions, creating a system where interest rates clear supply and demand without human intervention.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Utilization-Based Rate Models — automatic feedback</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Interest rates adjust in real-time to balance lenders and borrowers with no manual intervention.</div>

|   |   |
|---|---|
| **Core mechanic** | Borrow/supply rates are functions of utilization percentage |
| **Utilization** | Borrowed amount ÷ (borrowed + idle available) |
| **Rate direction** | Rates rise sharply as utilization nears 100% |
| **Supply rate** | Percentage of borrow rate, paid to lenders minus protocol fees |
| **Adjustment speed** | Instant, per transaction; no settlement delays |

</aside>

## The utilization rate and why it matters

The foundation of DeFi lending is the **utilization rate** (U), expressed as a percentage:

```
U = Total Borrowed / (Total Borrowed + Total Available)
```

When a protocol has $100 million in deposits and $50 million is borrowed, utilization is 50%. If $80 million is borrowed, utilization is 80%.

This ratio matters because a protocol's solvency depends on its ability to meet withdrawal requests. If utilization is 95%, only 5% of deposits are idle and available for immediate withdrawal. If depositors want to withdraw more than 5%, they must wait for borrowers to repay, or the protocol enters default.

The interest rate model uses utilization as a signal: high utilization means deposits are scarce and borrowing is attractive, so rates should rise to attract new deposits and discourage new borrowing. Low utilization means deposits are abundant and capital is idle, so rates should fall to stimulate borrowing and put capital to use.

This is not mysterious. It is a supply-and-demand mechanism expressed through automated code instead of human negotiation.

## Standard utilization curves

The earliest DeFi lending protocols, like Compound, used a **piecewise-linear interest rate model**:

- **Below a kink utilization** (e.g., 80%): rates increase slowly, with a small slope. This range is "normal operation."
- **Above the kink**: rates increase steeply, with a steep slope. This range is "stress mode."

For example:

- At 50% utilization: borrow rate = 2% APY.
- At 80% utilization (the kink): borrow rate = 4% APY.
- At 95% utilization: borrow rate = 20% APY (steep slope above kink).

The supply rate paid to depositors is typically a fraction of the borrow rate (e.g., 80%), since the protocol retains a fee:

```
Supply Rate = Borrow Rate × (1 - Protocol Fee) × (Utilization)
```

At 80% utilization with 4% borrow rate:
```
Supply Rate = 4% × (1 - 0.1) × 0.80 = 2.88% APY
```

This ensures lenders always earn less than borrowers pay, and the difference funds protocol operations and reserves.

## Why the kink exists

The kink—the point where the slope changes—is a design choice balancing stability and efficiency. Below the kink, the protocol operates in a "comfortable" mode where capital is well-deployed but not scarce. Rates are relatively stable and predictable, attracting long-term lenders.

Above the kink, the protocol signals distress. If utilization hits 85% and then 90%, the rate jumps dramatically. The steepness incentivizes depositors to rush new capital in and borrowers to pay back debt, bringing utilization back down.

Without the kink—with a single gentle slope everywhere—the protocol would struggle to respond when capital becomes very scarce. Rates would be too low at high utilization, and the pool would be drained by withdrawals it could not accommodate.

Different protocols tune the kink level and slopes to their risk tolerance. A conservative protocol might use a kink at 60% with a steep upper slope, penalizing high utilization early. An aggressive protocol might use a kink at 90%, allowing higher capital efficiency until the absolute brink of distress.

## Aave's interest model and variants

Aave, the largest DeFi lending protocol, uses a similar but more complex model. Aave introduced **stable rates** and **variable rates**:

- **Variable rates** follow the utilization model described above, adjusting per block as utilization changes.
- **Stable rates** are fixed at the time of borrowing, protecting borrowers from sudden rate spikes. But Aave re-balances the stable rate periodically (monthly or on governance decision), capping the duration of the fixed rate.

Aave also introduced **interest rate strategies**—different curves for different assets. Stablecoins might have a gentle curve (low risk, stable demand), while volatile assets like AAVE or other governance tokens might have aggressive curves to discourage excessive borrowing.

More recent protocols have experimented with **dynamic kinks**: the kink position itself adjusts based on historical utilization patterns, concentrating steep slopes where the market naturally settles.

## Interest rate model versus actual equilibrium

The model is a tool, not a guarantee. It shapes incentives, but market behavior often diverges from the model's intent.

If a borrowing opportunity emerges elsewhere (e.g., a new competing protocol launches), borrowers may demand lower rates than the model suggests, and the protocol may face an outflow. Conversely, if panic spreads, depositors may demand high supply rates to compensate for perceived risk, and the protocol must raise rates sharply to prevent a run.

High inflation or bear markets can also invert the curve's incentives. In a crash, utilization may spike not because demand is strong but because panic-stricken borrowers cannot repay, and new borrowing is unattractive at any rate. The protocol may watch utilization hit 90% while deposit outflows accelerate—a condition the model did not anticipate.

## Reserve factors and protocol sustainability

A portion of the interest paid by borrowers does not go to depositors; it is held as a **reserve factor** by the protocol. Aave reserves 10% to 20% of borrow interest, Compound around 10%.

These reserves fund protocol operations, pay governance participants, and build a cushion against losses from bad debt. They also partially compensate the protocol for credit risk—since DeFi lending is uncollateralized by nature, defaults do occur, and the reserve must cover losses.

However, high reserve factors reduce the supply rate paid to depositors, which can discourage deposits. A protocol faces a trade-off: build larger reserves and reduce yields, or operate lean and risk insolvency during stress.

## Practical implications for lenders and borrowers

For **lenders**: the interest rate model means you earn more when capital is scarce (high utilization) but face higher liquidation risk, because high utilization correlates with high leverage and market stress.

For **borrowers**: the model means you pay less when capital is abundant (low utilization) but face sharp rate spikes if the protocol fills up. Borrowing at 5% APY is attractive until utilization hits 95% and your rate spikes to 40% APY. Savvy borrowers monitor utilization and lock in rates when they are low, while avoiding peak-utilization periods.

## Limitations and edge cases

Interest rate models assume rational behavior and that price discovery works. In extreme conditions, these assumptions fail:

- **Positive feedback loops**: If a major borrower defaults, the supply rate falls (less income to lenders), which causes more depositors to withdraw (searching for better yields), which reduces available capital, which forces the remaining depositors to bear more risk. The rate model does not prevent this spiral; it can only slow it.
- **Oracle failures**: If the price oracle that feeds utilization data fails (not uncommon in DeFi), the interest rate model responds to stale or manipulated data, pushing rates in the wrong direction.
- **Curve mismatch**: A curve designed for calm markets may not adapt quickly enough during crashes. By the time utilization spikes to 95%, it may already be too late to attract new deposits.

A more sophisticated model might incorporate [volatility](/currency-volatility/) or credit history, but DeFi protocols avoid complexity to reduce smart contract risk and preserve decentralization.

## See also

<div class="wiki-seealso">

### Closely related

- [Liquidation mechanics in lending pools](/defi-lending-interest-rate-model/) — how collateral is seized when utilization is high
- [Aave protocol mechanics](/defi-sandwich-attack-explained/) — application of utilization-based rates at scale
- [Yield farming and APY strategies](/ethereum/) — how lending rates drive user behavior
- [Rehypothecation risk in DeFi](/rehypothecation-risk-in-defi/) — how high utilization and leverage interact
- [Smart contract risk and governance](/blockchain-fundamentals/) — how rate models can be changed

### Wider context

- [Interest rates and the yield curve](/yield-curve/) — traditional finance parallels
- Supply and demand in markets — the economic foundation of rate models
- [Automated market makers and algorithmic pricing](/cryptocurrency-exchange/) — similar automated mechanisms in DeFi
- Credit risk and collateral — why lending requires solvency and reserves

</div>
