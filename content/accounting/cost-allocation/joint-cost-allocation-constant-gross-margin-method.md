---
title: "Constant Gross Margin Method for Joint Cost Allocation"
description: "The constant gross margin method allocates joint production costs by working backward from a uniform gross margin percentage across all products."
keywords:
  - constant gross margin method
  - joint cost allocation
  - accounting allocation methods
  - joint products
  - relative sales value method
image: "/svg/accounting.svg"
---

*The **constant gross margin method** is a joint cost allocation technique that forces all co-products to share the same gross margin percentage. Rather than allocating costs in proportion to sales value (as the [relative-sales-value method](/backwardation/) does), this method assumes all products earn an identical margin and works backward from total revenue to determine how much of the joint costs each product should bear. It's less intuitive than other methods but has the advantage of yielding consistent profitability across the product line — a property favored by some manufacturers and required by certain regulatory regimes.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Constant Gross Margin Method — key facts</div>

<img src="/svg/accounting.svg" alt="An abstract editorial mark for accounting topics." />

<div class="wiki-infobox-caption">Allocate joint costs so all products hit the same profit margin.</div>

|   |   |
|---|---|
| **Core logic** | Uniform gross margin % across all products |
| **Calculation** | Work backward: allocate costs so margin is consistent |
| **Key input** | Total revenue, joint costs, separate costs |
| **Typical uses** | Regulated industries, internal reporting, cost control |
| **Contrast** | Relative-sales-value allocates by revenue weight |
| **Advantage** | Forces visibility into profitability per product |
| **Disadvantage** | Arbitrary and unrelated to production economics |

</aside>

## How the method works: backward allocation logic

Unlike the [relative-sales-value method](/backwardation/), which allocates joint costs proportionally to each product's market value, the constant gross margin method starts with a desired or implied profit margin and distributes costs to achieve it.

Here's the procedure:

1. **Calculate total revenue.** Sum the selling price of all products at the split-off point (or, for products sold further downstream, reduce by separable costs).

2. **Determine target gross margin percentage.** Decide what percentage of revenue should be gross profit. For example, if you want a 40% gross margin, then 60% of revenue should cover all costs.

3. **Calculate total costs available to allocate.** Add joint costs and all separable (direct) costs. This is the total amount to be recovered.

4. **Allocate joint costs.** Work backward: if total revenue is $1,000, the target margin is 40%, and total costs must be $600, then the remaining $400 is available to cover additional costs beyond the separable costs already assigned to individual products.

The joint cost allocated to each product is the amount required to bring its cost-to-revenue ratio in line with the uniform margin target.

## A worked example

Suppose a refinery processes crude oil into three products: gasoline, diesel, and fuel oil. The input costs are:

- **Joint processing cost:** $500,000
- **Split-off point sales (before separable costs):**
  - Gasoline: $400,000
  - Diesel: $300,000
  - Fuel oil: $200,000
  - **Total revenue:** $900,000

- **Separable (further-processing) costs:**
  - Gasoline: $50,000
  - Diesel: $40,000
  - Fuel oil: $30,000
  - **Total separable:** $120,000

**Step 1: Total costs to recover**
- Joint costs: $500,000
- Separable costs: $120,000
- **Total: $620,000**

**Step 2: Implied gross margin**
- Total revenue: $900,000
- Total costs: $620,000
- Gross profit: $280,000
- **Gross margin %: 280 / 900 = 31.1%**

Under the constant gross margin method, each product will show this same 31.1% margin. To achieve it, allocate the joint costs so that each product's total cost (joint + separable) leaves the 31.1% margin:

| Product | Revenue | Required Cost | Separable | Joint Cost Allocation |
|---------|---------|----------------|-----------|----------------------|
| Gasoline | $400,000 | $275,600 | $50,000 | $225,600 |
| Diesel | $300,000 | $206,700 | $40,000 | $166,700 |
| Fuel oil | $200,000 | $137,800 | $30,000 | $107,800 |
| **Total** | **$900,000** | **$620,100** | **$120,000** | **$500,100** |

(There's a $100 rounding difference; allocate it to the largest product or distribute proportionally.)

Each product now carries a 31.1% gross margin, even though the amount of joint cost assigned to each varies.

## Constant gross margin vs. relative-sales-value

The relative-sales-value method allocates joint costs based on each product's revenue as a percentage of total revenue. In the refinery example:

- Gasoline: 44.4% × $500,000 = $222,000
- Diesel: 33.3% × $500,000 = $166,500
- Fuel oil: 22.2% × $500,000 = $111,000

This is simpler and reflects the market value of each product. The constant gross margin method, by contrast, deliberately overrides market value in service of equal profitability.

The constant margin approach can produce strange results. If one product has high separable costs, it will bear much of the joint cost burden; if another has low separable costs, it will receive a smaller joint cost allocation — not because of its market value, but to achieve uniform margin percentages.

In the example, gasoline gets more joint cost ($225,600) than fuel oil ($107,800), not primarily because gasoline is more valuable, but because the constant margin requirement forces a specific distribution. This can feel arbitrary and may not reflect production economics.

## When and why this method is used

**Regulated industries:** Some utilities and natural resource processors use this method because regulators like the visible assumption that all customers or products bear "fair" costs. It prevents one product or customer class from subsidizing another.

**Internal management reporting:** A business may use it to identify which products are truly profitable independent of cost allocation assumptions. If all products must yield the same margin under this assumption, management can focus on volume and mix decisions rather than arguing over allocation methodology.

**Contractual compliance:** Joint venture agreements or cost-sharing arrangements sometimes specify a uniform margin as the basis for dividing results. Oil and gas partnerships, for example, may use constant margin formulas in their accounting agreements.

**Psychological simplicity:** Unlike relative-sales-value (which varies with market price), the constant gross margin method is stable period-to-period as long as product volumes and separable costs are stable. Some controllers prefer this predictability.

## Criticisms and limitations

The constant gross margin method is criticized as economically arbitrary. It ignores [market price](/price-discovery/), consumer demand, and production costs that actually drive profitability. A fuel oil product that costs far less to process should not bear the same margin burden as a refined specialty product.

It also inflates costs for low-revenue products. In the example, fuel oil's true economic profitability might be higher than the constant margin suggests, but the allocation hides that. This can mislead management into cutting unprofitable-looking products that should actually be retained.

The method also assumes all products share the same production risk and quality control costs, which is rarely true. It imposes a normative margin rather than discovering actual margins from market data.

## Regulatory and financial reporting context

[Under IFRS and GAAP](/backwardation/), joint cost allocation methods are discretionary as long as the chosen method is consistent and reasonable. The constant gross margin method is acceptable, but most publicly traded companies use relative-sales-value or physical-units allocation because they're simpler and more auditable.

For [cost accounting](/backwardation/) and [revenue recognition](/revenue-recognition/) purposes, the method must be applied consistently and disclosed clearly. Auditors are most comfortable when allocation choices are defensible — which the constant margin method is, provided the margin assumption itself is justified.

## The takeaway

The constant gross margin method is a deliberate choice to force uniform profitability across joint products, overriding market value. It's useful in regulated settings and for internal control but should not be mistaken for an economic representation of true product profitability. Understand your allocation method and its assumptions; the numbers it produces are no more true than the method itself.

## See also

<div class="wiki-seealso">

### Closely related

- [Revenue recognition](/revenue-recognition/) — how to record sales for joint products
- [Accumulated depreciation](/accumulated-depreciation/) — another allocation challenge in accounting
- [Cost of debt](/cost-of-debt/) — related to allocating financing costs across projects
- [Accrual accounting](/accrual-accounting/) — the framework in which cost allocation occurs
- [Balance sheet](/balance-sheet/) — where allocated joint costs appear as inventory value

### Wider context

- [Income statement](/income-statement/) — where allocated costs affect reported profit
- [Generally accepted accounting principles](/generally-accepted-accounting-principles/) — the rules governing allocation methods
- [Segment reporting](/backwardation/) — how businesses disclose profitability by product line
- [Accounts payable](/accounts-payable/) — cost management for suppliers

</div>
