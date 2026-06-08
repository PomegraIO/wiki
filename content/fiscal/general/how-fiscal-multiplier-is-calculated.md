---
title: "How the Fiscal Multiplier Is Calculated"
description: "Learn how to calculate fiscal multiplier from marginal propensity to consume. Includes derivation, spending multiplier, tax multiplier, and worked examples."
keywords:
  - fiscal multiplier calculation
  - spending multiplier
  - tax multiplier
  - marginal propensity to consume
  - keynesian economics
  - multiplier effect
---

*The **fiscal multiplier** is calculated from the marginal propensity to consume (MPC) using a simple algebraic formula: the spending multiplier equals 1 divided by the marginal propensity to save (MPS). A worked example shows how a $100 billion government spending injection expands output by $250 billion or more, depending on behavioral assumptions about saving and leakage.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Fiscal Multiplier — key facts</div>

<img src="/svg/fiscal.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">The fiscal multiplier quantifies the amplification of spending shocks through the economy.</div>

|   |   |
|---|---|
| **Spending multiplier** | 1 ÷ MPS, or 1 ÷ (1 − MPC) |
| **Tax multiplier** | −MPC ÷ MPS |
| **Balanced-budget multiplier** | 1 (spending increase equals tax increase) |
| **MPC range** | Typically 0.7–0.9 for developed economies |
| **Key leakage** | Imports, taxes, and saving drain the circular flow |

</aside>

## The Building Block: Marginal Propensity to Consume

The fiscal multiplier is derived from a single behavioral fact: when households receive an extra dollar of income, they spend a fraction of it and save the rest. That fraction is the **marginal propensity to consume** (MPC).

If the MPC is 0.8, a household receiving $100 in new income will spend $80 and save $20. The reciprocal relationship—the fraction saved, or marginal propensity to save (MPS)—is therefore 0.2.

This simple observation chains through the economy. When the government injects $100 billion in spending, initial recipients earn $100 billion in income. If their MPC is 0.8, they spend $80 billion of that, creating income for suppliers and workers. Those second-round recipients spend 80% of their $80 billion, generating $64 billion in third-round spending. The cycle continues, with each round weaker than the last.

## Deriving the Spending Multiplier

The spending multiplier asks: by how much does total output increase from a one-dollar boost in autonomous spending?

Start with the aggregate demand identity:
Y = C + I + G + (X − M)

Where Y is output, C is consumption, I is investment, G is government spending, X is exports, and M is imports.

Consumption depends on disposable income: C = a + c·Yd, where a is baseline consumption, c is the MPC, and Yd is disposable income.

Assume disposable income equals output minus taxes: Yd = Y − T.

Substituting into the demand identity and solving for Y:

Y = a + c(Y − T) + I + G + (X − M)
Y = a + cY − cT + I + G + X − M
Y − cY = a − cT + I + G + X − M
Y(1 − c) = a − cT + I + G + X − M
Y = [a − cT + I + G + X − M] ÷ (1 − c)

The multiplier on government spending is the derivative of Y with respect to G:

**Multiplier on G = 1 ÷ (1 − c) = 1 ÷ MPS**

If MPC = 0.8 (and therefore MPS = 0.2), the spending multiplier is 1 ÷ 0.2 = **5**. A $1 increase in government spending raises output by $5.

## The Tax Multiplier

The tax multiplier measures the output effect of a tax cut. Since a dollar of tax cut increases disposable income by one dollar, and households spend c dollars of that, the initial spending boost is only c dollars—not the full dollar.

Taking the derivative of Y with respect to taxes:

**Multiplier on T = −c ÷ (1 − c) = −MPC ÷ MPS**

With MPC = 0.8, the tax multiplier is −0.8 ÷ 0.2 = **−4**. A $1 reduction in taxes raises output by $4, which is one unit smaller than the spending multiplier because the initial injection is smaller (only the consumed portion).

This is why a $1 tax cut is weaker stimulus than a $1 spending increase—it leaks through saving from the start.

## Worked Example: The $100 Billion Spending Boost

Suppose the government increases defense spending by $100 billion, and the MPC is 0.8.

**Round 1:** Defense contractors and workers earn $100 billion. They spend $80 billion (0.8 × $100 billion) and save $20 billion.

**Round 2:** Suppliers and retailers earn $80 billion. They spend $64 billion (0.8 × $80 billion) and save $16 billion.

**Round 3:** The next layer earns $64 billion and spends $51.2 billion.

The pattern continues: 100 + 80 + 64 + 51.2 + 40.96 + …

This is a geometric series with first term 100 and common ratio 0.8. The sum converges to:

**Total output increase = 100 ÷ (1 − 0.8) = 100 ÷ 0.2 = 500 billion**

So $100 billion in government spending translates to $500 billion in additional GDP—a multiplier of 5.

## Why Multipliers Differ from Theory

Real-world multipliers typically fall below the simple formula. Several leakages reduce the effect:

**Imports.** When households spend, they buy foreign goods too. Each spending round loses a slice to imports, cutting the effective MPC below the headline figure.

**Taxes.** Progressive tax systems claw back some income in higher brackets, shrinking disposable income and the consumption chain.

**Behavioral offsets.** Forward-looking households may save more if they expect future tax hikes to repay government borrowing (Ricardian equivalence), cutting the MPC.

**Interest-rate crowding out.** Government borrowing can push up real interest rates, discouraging private investment and partially offsetting the spending boost.

Empirical estimates for the U.S. spending multiplier typically range from 0.5 to 1.5 in normal times, well below the 5 implied by a 0.8 MPC. Tax multipliers are similarly dampened.

## Balanced-Budget Multiplier

A special case: when the government raises spending by $100 billion and finances it with $100 billion in taxes, what is the net output effect?

Using the formulas above, the combined effect is:
(1 ÷ MPS) × ΔG + (−MPC ÷ MPS) × ΔT
= (1 ÷ 0.2) × 100 + (−0.8 ÷ 0.2) × 100
= 500 − 400
= 100

The balanced-budget multiplier equals **1**. A dollar for dollar increase in spending paid for by equal taxation raises output by exactly one dollar. This result is independent of the MPC.

## See also

<div class="wiki-seealso">

### Closely related

- [Fiscal Multiplier](/fiscal-multiplier/) — The economic mechanism by which spending shocks propagate through aggregate demand
- [Marginal Propensity to Consume](/marginal-propensity-to-consume/) — The behavioral foundation of multiplier calculations
- [Discretionary Spending](/discretionary-spending/) — Government outlays subject to multiplier effects
- [Fiscal Consolidation](/fiscal-consolidation/) — When negative multipliers matter: austerity and contraction risk
- [Forward Guidance](/forward-guidance/) — Central bank communication that can anchor multiplier expectations

### Wider context

- [Business Cycle](/business-cycle/) — The demand-driven fluctuations multipliers help explain
- Keynesian Economics — The theoretical tradition underlying multiplier analysis
- [Monetary Policy](/monetary-policy/) — The policy lever that interacts with fiscal stimulus
- [Gross Domestic Product](/gross-domestic-product/) — The output measure multipliers amplify

</div>
