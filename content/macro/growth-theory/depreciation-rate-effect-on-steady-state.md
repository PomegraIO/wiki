---
title: "How the Depreciation Rate Affects the Steady State in Growth Models"
description: "See how a higher depreciation rate lowers steady-state capital stock and output per worker in the Solow model, with worked numerical examples."
keywords:
  - depreciation rate effect on steady state
  - solow model depreciation rate
  - steady state capital stock
  - capital accumulation and depreciation
---

*In the **Solow growth model**, the **depreciation rate** is a key determinant of the steady-state capital stock and output per worker. When the depreciation rate rises—machinery wears out faster or becomes obsolete more quickly—steady-state capital per worker declines, dragging down output per worker in turn. This relationship is direct and quantifiable: we can trace exactly how a 1% increase in depreciation reshapes the long-run equilibrium.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Depreciation & Steady State — key facts</div>

<img src="/svg/macro.svg" alt="An abstract editorial mark for macroeconomics." />

<div class="wiki-infobox-caption">Higher depreciation = lower steady-state capital = lower output per worker.</div>

|   |   |
|---|---|
| **Steady state** | Capital per worker no longer growing; capital depreciation = investment |
| **Depreciation rate** | % of capital stock lost per period due to wear, obsolescence, or scrapping |
| **Break-even investment** | Amount needed to replace depreciation and keep capital constant |
| **Relationship** | Higher δ → Lower k* → Lower y* (inversely proportional) |
| **Adjustment path** | Temporary growth slows, falls until new steady state reached |
| **Real-world analog** | Moore's Law (chip obsolescence), asset lives (vehicles, equipment) |

</aside>

## The steady-state condition: investment equals depreciation

In the Solow model, steady state is reached when capital per worker stops growing. At that point, gross investment (new capital added) exactly equals depreciation (capital lost to wear and obsolescence). Below this point, investment exceeds depreciation, so capital per worker rises. Above it, depreciation exceeds investment, and capital per worker falls. Steady state is the equilibrium.

Mathematically:

**k* = (s / (n + δ)) × (A × f(1))**

Where:
- **k*** = steady-state capital per worker
- **s** = savings rate
- **n** = population growth rate
- **δ** = depreciation rate
- **A** = labor productivity (technology)

The key insight: steady-state capital is inversely proportional to the depreciation rate. Raise δ, and k* falls. Lower δ, and k* rises.

## A worked example: U.S. manufacturing equipment

Suppose a stylized economy has:
- Savings rate (s) = 20% (0.20)
- Population growth (n) = 1% (0.01)
- Productivity (A) = 1 (normalized)
- Production function: y = k^0.3 (Cobb-Douglas)

**Scenario 1: Low depreciation (δ = 5%)**

Break-even investment per worker = (n + δ) × k* = (0.01 + 0.05) × k* = 0.06 × k*

At steady state: Investment = Savings × Output = 0.20 × y

If output per worker y = k^0.3, and we solve for k*:

Savings rate × k^0.3 = (n + δ) × k*
0.20 × k^0.3 = 0.06 × k*

Rearranging: k^0.3 / k* = 0.06 / 0.20 = 0.30
This implies k* ≈ 10 (capital per worker is 10 units)
Output y = 10^0.3 ≈ 2.0 units per worker

**Scenario 2: High depreciation (δ = 10%)**

Now: Break-even investment = (0.01 + 0.10) × k* = 0.11 × k*

At steady state:
0.20 × k^0.3 = 0.11 × k*
k^0.3 / k* = 0.11 / 0.20 = 0.55
This implies k* ≈ 3.8 (capital per worker is only 3.8 units)
Output y = 3.8^0.3 ≈ 1.5 units per worker

**The effect**: Doubling depreciation from 5% to 10% cut steady-state capital from 10 to 3.8 units per worker—a 62% decline—and output from 2.0 to 1.5 units, a 25% decline.

This is not a temporary shock. The economy adjusts downward and stays at the lower steady state permanently, unless depreciation rates or the savings rate change again.

## Why higher depreciation reduces capital accumulation

The intuition is straightforward: more capital is lost every year, so saving and investment must work harder just to keep the capital stock from shrinking. A worker in an economy with 5% annual depreciation can invest in machines that last 20 years on average; a worker in an economy with 10% depreciation faces machines lasting only 10 years on average. To maintain the same stock of productive equipment, the second economy must spend twice as much on replacement.

Those replacement investments are not available for expansion—for adding *new* capital per worker. The entire investment budget is consumed by replacements, leaving no room for growth. Over time, the capital stock stabilizes at a lower level because less net capital is being created.

In the real world, depreciation rates vary widely:

- **Information technology**: 20–30% annually (rapid obsolescence; Moore's Law)
- **Factory equipment**: 5–10% annually (10–20 year lifespans)
- **Structures and buildings**: 1–3% annually (40+ year lifespans)
- **Vehicles**: 10–15% annually (8–10 year economic lives)

An economy dominated by tech has a higher effective depreciation rate than one anchored in long-lived infrastructure. This partly explains why productivity growth in tech-heavy sectors is so volatile: new capital is expensive to maintain, and the capital stock can shift rapidly as innovations obsolete existing equipment.

## The adjustment path: transition to new steady state

When depreciation rises (say, due to faster technological change), the economy does not jump instantly to a new, lower steady state. The transition follows a predictable path:

1. **Capital stock initially unchanged**: Existing factories and equipment do not disappear the day a depreciation rate rises.
2. **Depreciation accelerates**: More capital wears out or becomes obsolete.
3. **Investment cannot keep pace**: Even with constant savings, investment now covers more depreciation and less expansion.
4. **Capital per worker falls**: The capital-to-labor ratio declines.
5. **Output per worker falls**: With less capital per worker, productivity declines.
6. **Growth becomes negative**: For some years, output per worker may actually decline as capital stock shrinks faster than new capital is added.
7. **Approach to new steady state**: Eventually, capital stock shrinks to the level where break-even investment again equals actual investment, and growth stops—but at a lower level.

This transition can take a decade or more, depending on how much capital needs to be shed.

## Empirical examples: technological change and depreciation

Japan's high growth in the 1960s–80s occurred alongside relatively low depreciation rates on long-lived manufacturing assets (steel mills, automobiles, chemicals) and a high savings rate. As Japan's capital stock aged and technological change accelerated (electronics, information technology), effective depreciation rates rose, contributing to slower growth in the 1990s–2000s.

The U.S. IT sector of the 1990s experienced a surge in depreciation as computer equipment and software became obsolete every 3–5 years instead of 10+. Firms had to invest heavily in replacement capital just to maintain the same capability, reducing net investment and eventually growth as Y2K fears faded and the tech bubble burst.

## Depreciation, policy, and growth

Policy implications follow. If government wants to raise steady-state capital and output per worker, it can:

1. **Raise the savings rate** (through tax incentives, reduced consumption, forced saving)—increases k*
2. **Lower population growth** (through immigration policy or demographics)—increases k*
3. **Lower effective depreciation** (through investment in durable infrastructure, durability standards, or capital preservation)—increases k*
4. **Raise productivity** (through education, R&D, institutional quality)—increases the return on capital and encourages more saving

Conversely, policies that accelerate depreciation—rapid technological mandatory obsolescence, poor maintenance, or regulatory depreciation schedules—lower steady-state capital and output.

Tax policy also influences effective depreciation. Accelerated depreciation schedules (which allow firms to deduct capital costs faster) reduce the effective life of assets and increase the depreciation *deduction*, even if physical depreciation rates do not change. This affects saving and capital investment decisions.

## See also

<div class="wiki-seealso">

### Closely related

- Capital accumulation — building capital stock over time
- Solow model — foundation of endogenous growth theory
- Steady state — long-run equilibrium without growth
- Capital stock — aggregate capital available to workers
- [Labor productivity](/labor-productivity/) — output per worker
- Technological change — exogenous driver of productivity

### Wider context

- Economic growth — rates and determinants across nations
- Capital investment — forms and returns
- [Business cycle](/business-cycle/) — short-run fluctuations around trend
- Fiscal policy — government influence on savings and investment
- [Inflation](/inflation/) — real depreciation rates and purchasing power

</div>
