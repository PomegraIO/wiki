---
title: "Rehypothecation Risk in DeFi"
description: "Rehypothecation risk in DeFi occurs when collateral is reused across multiple protocols simultaneously, amplifying systemic risk during market stress."
keywords:
  - rehypothecation risk
  - collateral reuse defi
  - cascading liquidation
  - systemic risk crypto
  - defi leverage cycles
image: /svg/crypto.svg
---

*In DeFi, **rehypothecation risk** arises when the same collateral asset is reused across multiple protocols simultaneously—pledged to one protocol as collateral for a loan, while that borrowed asset is itself pledged elsewhere as collateral for another loan. During normal market conditions, this leverage cycle is profitable. But when collateral prices fall sharply, liquidations cascade: a price drop forces a redemption at one protocol, which pulls collateral from a second protocol, triggering redemptions there, and spreading the damage across the ecosystem. The cycle amplifies losses and can topple otherwise solvent participants.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Rehypothecation in DeFi — systemic vulnerability</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Reusing collateral across protocols creates fragile chains of dependency and contagion risk.</div>

|   |   |
|---|---|
| **What it is** | Collateral pledged to one protocol while borrowed assets are pledged to another |
| **Who is exposed** | Borrowers, lenders, and all interconnected protocols during market downturns |
| **Primary mechanism** | Cascading liquidations across protocols when collateral declines |
| **Trigger condition** | Sharp decline in collateral asset price; loss of confidence in any linked protocol |
| **Historical example** | 2022 Three Arrows Capital collapse; contagion across Celsius, Voyager, Celsius |

</aside>

## How collateral gets rehypothecated

Rehypothecation in DeFi happens through a simple chain of events, each individually rational:

1. A user deposits ETH into a lending protocol (Protocol A) and borrows stablecoins against it at 75% loan-to-value (LTV).
2. The user takes those stablecoins and deposits them into a yield farm (Protocol B), earning 15% APY—attractive because stablecoins are supposed to be stable and low-risk.
3. Protocol B uses those stablecoins as collateral to borrow more ETH or other assets for leverage, hoping to amplify yields.
4. A third participant repeats the cycle, using their borrowed assets as collateral elsewhere.

At each step, the participant sees an attractive return and the protocols see deposits that increase their TVL (total value locked). The ecosystem celebrates growth. What few notice is that a single ETH deposit has now been used as collateral three times over—supporting three layers of borrowing.

This is not unique to DeFi. Traditional finance rehypothecates collateral too—a bond can be pledged to a bank, which lends against it, and the bank itself uses the bond as collateral at a clearinghouse. But traditional markets have circuit breakers, clearinghouse capital requirements, and regulatory oversight. DeFi has none of these. The chains can grow many layers deep before anyone looks at the aggregate risk.

## Why rehypothecation amplifies losses

The danger crystallizes during a downturn. Suppose ETH drops 20% in a day. Here is what happens:

- The user in step 1 is now underwater or near liquidation. Their 75% LTV position is at 80% of borrowed value—above the liquidation threshold on most protocols.
- To raise capital or deleverage, they sell the stablecoins they earned in step 2. But if many users do this at once, stablecoins lose their peg, trading at $0.95 instead of $1.00.
- Stablecoin holders at Protocol B now suffer a loss, and the protocol's collateral base weakens. The protocol may require liquidations of its own borrowers to meet solvency requirements.
- Those liquidations force more collateral sales, pushing prices lower, triggering more liquidations in a feedback loop.

The cascade spreads because the protocols are not independent. They share the same underlying assets—ETH, stablecoins, and tokens—and are connected through borrowers and lenders who operate across multiple platforms. When one protocol faces a shortfall, it attempts to recall collateral or force redemptions, yanking liquidity from others.

In the 2022 contagion that toppled Celsius, Three Arrows Capital, and Voyager Digital, this is precisely what happened. Each firm had collateral rehypothecated across multiple DeFi lending pools and counterparties. When the first large price drop hit, redemption requests cascaded, and no single entity had enough liquidity to meet all claims at once.

## LTV ratios and the illusion of safety

Each DeFi protocol sets a maximum LTV—the amount you can borrow against your collateral. A 75% LTV on ETH sounds safe: the collateral is 33% larger than the debt, leaving room for a decline. The problem is that this LTV is designed for a single protocol's risk, not for the systemic risk created when the same collateral is used multiple times.

If the same ETH supports $75, $60, and $50 in borrowing across three protocols (because each protocol thinks the LTV is safe for its own purposes), the true aggregate leverage is much higher. The collateral is supporting $185 in total claims—a 2.5x ratio—on an asset worth $100. A 40% price drop eliminates all claims entirely, and liquidations become disorderly.

Furthermore, LTV ratios are often set assuming that collateral can be liquidated quickly at fair prices. During market stress, this assumption breaks. Liquidations must be forced at market prices, which are often far worse than the models expected. Slippage widens, oracles lag, and the effective liquidation price is much lower than the assumed price.

## Interconnectedness and contagion

The DeFi ecosystem is a network of dependencies. A single protocol failure—whether due to poor governance, a smart contract bug, or a borrower default—can ripple outward. If Protocol B fails and cannot meet withdrawals, then users who trusted it lose capital. But more critically, the collateral that was held at Protocol B is frozen or lost, affecting the next layer of protocols that depended on it.

This is contagion. It is the same phenomenon that nearly destroyed the global financial system in 2008, when the failure of Lehman Brothers and other interconnected institutions caused a systemic crisis. DeFi is more transparent but even more fragile because there is no backstop—no central bank to inject liquidity, no lender of last resort to stabilize an illiquid asset.

Large multi-protocol failures like those in 2022 demonstrated that rehypothecation risk is not theoretical. Firms that felt diversified across multiple platforms discovered that those platforms were not independent; they all faced the same demand for collateral at the same time, and none had enough.

## Measuring and monitoring rehypothecation

Users who want to understand their exposure face a difficult problem: **data opacity**. DeFi does not have a consolidated view of capital flows across all protocols. To understand how much collateral is being rehypothecated, you would need to trace capital through each protocol and its participants—a Sisyphean task.

Some on-chain analysis firms attempt to map these flows, but the data is noisy and lagged. Cross-collateralization is often hidden inside smart contracts or multi-signature wallets. The true rehypothecation network is visible only in hindsight, when contagion strikes and participants suddenly realize how connected everything was.

This opacity is a core risk. Participants cannot accurately price systemic risk because they cannot see the full dependency chain. Markets misprice risk during periods of low volatility and punish the misprice during crises.

## Defenses and their limits

Several defenses have been proposed or implemented:

- **Conservative LTV ratios**: Protocols that keep LTV below 60% leave more margin for error. But this also reduces yield and capital efficiency, limiting growth.
- **Diversified collateral**: If each protocol accepts many types of collateral and borrowers do not re-use the same collateral across chains, contagion risk falls. But this conflicts with yield-seeking behavior; users are drawn to rehypothecation because it increases returns.
- **Isolation mode**: Some protocols, like Aave, allow certain collateral to be siloed—usable for borrowing only within that isolation—preventing contagion. But silo borrowers pay higher rates, and silo assets earn less yield.
- **Insurance and liquidation pools**: Some protocols pool insurance reserves to handle unexpected shortfalls. But these pools are too small relative to the ecosystem size. A major event exhausts them quickly.

The hard truth is that rehypothecation risk is not solvable without reducing leverage and interconnectedness. And leverage is profitable, so market forces continually drive it back up.

## Stress testing and resilience

Some protocols now run stress tests: simulations of what happens if collateral prices fall 30%, 50%, or more, and if certain counterparties default. These tests are useful for internal risk management but are not standardized across the ecosystem. A protocol might pass its own stress test while remaining vulnerable to failure at a linked protocol it did not stress-test.

DeFi as a whole lacks an equivalent to the Federal Reserve's [stress testing](/stress-testing/) of banks, where regulators require firms to prove they can survive a financial crisis. Instead, participants discover fragility in real time, through live blowups.

## See also

<div class="wiki-seealso">

### Closely related

- [Liquidation mechanics in DeFi](/defi-lending-interest-rate-model/) — how collateral is forced into sales
- [Smart contract risk and systemic risk](/blockchain-fundamentals/) — contagion and interconnectedness in protocols
- [Sandwich attacks in DeFi](/defi-sandwich-attack-explained/) — related DeFi vulnerabilities
- [Leverage and margin calls in crypto](/leverage-ratio-forex/) — how borrowed capital amplifies gains and losses
- [Stablecoin design and reserve risk](/cryptocurrency-exchange/) — why stablecoins fail during stress

### Wider context

- Financial contagion and systemic risk — 2008 crisis parallels
- [Concentration risk and portfolio diversification](/diversification/) — how dependency on single assets or platforms increases loss potential
- Collateral and secured lending — fundamentals of using assets as security for loans
- [Cryptocurrency volatility](/currency-volatility/) — price swings that trigger rehypothecation cascades

</div>
