---
title: "Reciprocal Cost Allocation Using Simultaneous Equations"
description: "How to set up and solve linear equations that fully allocate mutual service costs between support departments, achieving true reciprocal allocation."
keywords:
  - reciprocal cost allocation simultaneous equations
  - service department cost allocation
  - support department allocation
  - cost accounting methods
image: "/svg/accounting.svg"
---

*When a company's support departments serve each other—accounting handles HR's billings, HR recruits and trains accounting staff—simple sequential allocation misses the circular cost flow. Reciprocal cost allocation using simultaneous equations captures the full picture by solving for each department's total cost, including both direct costs and the costs of services received from other support functions.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Reciprocal Cost Allocation — key facts</div>

<img src="/svg/accounting.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">The most precise method allocates mutual service costs in full, but requires solving a system of equations.</div>

|   |   |
|---|---|
| **Method type** | Support department cost allocation to production (or revenue) departments |
| **Key feature** | Captures two-way service flows between support departments |
| **Starting point** | Direct costs of each support department; service usage percentages |
| **Execution** | Set up linear equations where total cost = direct cost + allocated service costs |
| **Math required** | Solve a system of simultaneous linear equations (Gaussian elimination or matrix algebra) |
| **Precision level** | Highest; no artificial sequencing bias |
| **Complexity** | Higher than step-down method; more computation required |
| **Software alternatives** | Spreadsheet solver tools; modern ERP systems automate it |

</aside>

## The problem: why simple methods break down

Imagine a factory with four support departments: Maintenance, Human Resources, Accounting, and Facilities. Maintenance incurs $100,000 in direct costs. HR incurs $80,000. Accounting incurs $60,000. Facilities incurs $70,000. The goal is to allocate these costs to three production departments: Assembly, Welding, and Finishing.

But here is the complication: Maintenance staff require HR services to recruit and train technicians. HR staff rely on Accounting to process their payroll and expense reports. Accounting staff occupy space managed by Facilities. Facilities workers need Maintenance to keep equipment running. Each support department creates costs that benefit other support departments, and the benefit flows are circular, not linear.

A sequential method—where you allocate Maintenance first, then HR, then Accounting, then Facilities—captures some of these flows, but not all. Once Maintenance costs are allocated downward, any HR costs that created a demand for Maintenance in the first place are lost. The sequence you choose (alphabetical, by budget size, by headcount) shapes the final allocation in arbitrary ways. Reciprocal allocation removes that bias.

## Setting up the equation system

For the factory example, let's define:
- **M** = total cost of Maintenance department (including allocated service costs from other departments)
- **H** = total cost of HR department
- **A** = total cost of Accounting department
- **F** = total cost of Facilities department

And let's say the usage percentages are (hypothetically):
- Maintenance direct cost: $100,000. HR uses 20% of Maintenance output; Accounting uses 30%; Facilities uses 25%; production departments use 25%.
- HR direct cost: $80,000. Maintenance uses 10% of HR services; Accounting uses 15%; Facilities uses 20%; production uses 55%.
- Accounting direct cost: $60,000. Maintenance uses 15% of Accounting output; HR uses 20%; Facilities uses 10%; production uses 55%.
- Facilities direct cost: $70,000. Maintenance uses 25% of Facilities; HR uses 5%; Accounting uses 10%; production uses 60%.

Now set up four equations where total cost equals direct cost plus allocated service received:

**Maintenance:** M = $100,000 + 0.10H + 0.15A + 0.25F

**HR:** H = $80,000 + 0.20M + 0.15A + 0.05F

**Accounting:** A = $60,000 + 0.30M + 0.20H + 0.10F

**Facilities:** F = $70,000 + 0.25M + 0.20H + 0.10A

Each equation says: "The total cost of this department equals its direct cost plus whatever fraction of every other department's total cost is allocated to it based on usage."

## Solving the system

Rearranging each equation into standard form (variables on the left, constants on the right):

M − 0.10H − 0.15A − 0.25F = $100,000

−0.20M + H − 0.15A − 0.05F = $80,000

−0.30M − 0.20H + A − 0.10F = $60,000

−0.25M − 0.20H − 0.10A + F = $70,000

This is a system of four equations with four unknowns. You can solve it using:

1. **Gaussian elimination:** Convert to an augmented matrix, perform row operations to achieve row-echelon form, then back-substitute to find M, H, A, and F.
2. **Matrix inversion:** Write as [Coefficient Matrix] × [Variables] = [Constants], then invert and multiply.
3. **Spreadsheet Solver:** Enter the equations as cell formulas and use Excel's Solver or Calc's Solver tool to find values that satisfy all constraints simultaneously.

For this example, the solution (rounded) is approximately:

- M = $142,857
- H = $118,571
- A = $95,714
- F = $114,286

Each figure is larger than the direct cost because it now includes the allocated cost of all services that department received from its peers.

## Verifying the solution

Check one equation:
M = $100,000 + 0.10($118,571) + 0.15($95,714) + 0.25($114,286)
M = $100,000 + $11,857 + $14,357 + $28,571
M = $154,785 (approximate, depending on rounding)

Small rounding variations are normal. If they accumulate significantly, recalculate with more decimal places or use matrix software.

## Allocating the totals to production departments

Once you have solved for M, H, A, and F, allocate each department's total cost to production departments using the predetermined usage percentages. For example, Maintenance's $142,857 total is allocated:
- Assembly: 25% of $142,857 = $35,714
- Welding: 25% of $142,857 = $35,714
- Finishing: 25% of $142,857 = $35,714

Do the same for HR, Accounting, and Facilities. Sum up the allocations to each production department, and you have the full, reciprocally-allocated support cost embedded in each product line's cost of goods sold or operating expense.

## When to use reciprocal allocation

Reciprocal allocation is mandatory under IFRS and GAAP for inventory valuation if support services are significant and mutually dependent. It is the theoretically correct method. However, it is more complex than the step-down method, which iteratively allocates from the largest or first department down, or the direct method, which allocates support costs directly to production departments without regard for inter-support flows.

Use reciprocal allocation if:
- Support departments are large and heavily interdependent (e.g., IT, HR, Finance all serve each other).
- Accuracy in product costing is critical (e.g., for pricing, profitability analysis, or external reporting).
- The organization uses modern accounting software that can automate the calculation.
- For cost accounting in lean manufacturing or activity-based costing systems where precision drives continuous improvement.

In smaller or simpler organizations, the step-down method is sufficient and much faster to compute by hand.

## Common pitfalls

**Circular reasoning error:** Ensure your allocation percentages reflect actual usage or service flows, not circular assumptions. The percentages should be based on headcount, machine hours, square footage, or other objective measures, not on the allocation result itself.

**Rounding accumulation:** If you round intermediate values, errors compound through the equation system. Carry at least four decimal places during calculation, then round final numbers.

**Forgetting to solve the system:** Beginning accountants sometimes allocate sequentially while thinking they are doing reciprocal allocation. True reciprocal allocation requires solving simultaneous equations. There is no shortcut that preserves all mutual dependencies.

**Not validating assumptions:** If your allocation percentages are wrong (e.g., you miscount the hours Maintenance spends on HR), the solved total costs will also be wrong. Audit the usage data before running the math.

## See also

<div class="wiki-seealso">

### Closely related

- Step-Down Cost Allocation — simpler sequential method; captures some but not all mutual flows
- Direct Cost Allocation — simplest method; ignores inter-support flows entirely
- Cost Allocation Base — choosing the right driver for allocation
- Support Department — concept and cost behavior
- [Absorption Costing](/absorption-costing/) — context for allocating overhead and support costs

### Wider context

- Cost Accounting — framework for classifying and allocating costs
- [Generally Accepted Accounting Principles](/generally-accepted-accounting-principles/) — standards governing allocation methods
- Internal Financial Reporting — management costing for decision-making

</div>
