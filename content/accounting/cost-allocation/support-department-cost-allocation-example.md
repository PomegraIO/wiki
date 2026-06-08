---
title: "Support Department Cost Allocation: A Step-by-Step Example"
description: "Work through a numerical example of allocating IT, HR, and facilities costs to production departments using direct and step-down allocation methods."
keywords:
  - support department cost allocation example
  - cost allocation methods
  - step-down method
  - direct allocation
  - indirect costs
  - overhead allocation
image: /svg/accounting.svg
---

*A **support department cost allocation example** demonstrates how indirect costs—IT, HR, facilities—flow into product lines using two competing methods: the direct method (simple, ignores interdepartmental services) and the step-down method (sequential, captures partial service sharing). Walking through the numbers shows why choice of method matters for product profitability.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Support Department Cost Allocation — Key Facts</div>

<img src="/svg/accounting.svg" alt="An abstract editorial mark for accounting." />

<div class="wiki-infobox-caption">Two allocation frameworks yield different product costs; choice affects pricing and margin analysis.</div>

|   |   |
|---|---|
| **Direct method** | Allocates support costs to production only; ignores services between support departments. Simplest, often understates product costs. |
| **Step-down method** | Allocates one support dept at a time in order of precedence; later depts absorb earlier depts' costs. More realistic, moderately complex. |
| **Reciprocal method** | Solves simultaneous equations when support depts serve each other. Most accurate, rarely used in practice. |
| **Cost pools** | HR, IT, Facilities, and other overhead centers; each uses a driver (headcount, CPU hours, sq. footage, etc.). |
| **Allocation base** | The denominator: total headcount, machine hours, or transactions that ties support costs to production. |
| **Product cost impact** | Choice of method can shift unit product cost by 5–15%, swinging profitability ranking. |

</aside>

## The Scenario

Imagine a small manufacturer with three support departments and two production departments:

| Department | Annual Cost |
|---|---|
| IT | $200,000 |
| HR | $150,000 |
| Facilities | $100,000 |
| Production A | $500,000 (direct labor + materials) |
| Production B | $400,000 (direct labor + materials) |

The company produces two products: Product X (made in both departments) and Product Y (made in Production A only).

To calculate the true cost of each product, the support department costs must be allocated to Production A and Production B. But how?

First, identify the **allocation drivers**:

- **IT support** is consumed based on number of users and computing power. Let us use "headcount" as the driver.
- **HR support** is consumed based on number of employees to recruit, train, and administer.
- **Facilities** is consumed based on square footage occupied.

The company has the following data:

|  | IT Users | Employees | Sq. Footage |
|---|---|---|---|
| IT Dept | 5 | 8 | 2,000 |
| HR Dept | 3 | 5 | 1,500 |
| Facilities Dept | 2 | 3 | 1,000 |
| Production A | 30 | 60 | 15,000 |
| Production B | 15 | 30 | 10,000 |
| **Total** | **55** | **106** | **29,500** |

## The Direct Method

Under the **direct method**, support department costs are allocated *only* to the production departments. Any services that support departments provide to each other are ignored.

Calculate the allocation rates for each support department, using only the production departments as the denominator:

**IT allocation rate:**
- IT users in production depts only: Production A (30) + Production B (15) = 45
- Allocation rate: $200,000 ÷ 45 = $4,444.44 per IT user

**HR allocation rate:**
- Employees in production depts only: Production A (60) + Production B (30) = 90
- Allocation rate: $150,000 ÷ 90 = $1,666.67 per employee

**Facilities allocation rate:**
- Sq. footage in production depts only: Production A (15,000) + Production B (10,000) = 25,000
- Allocation rate: $100,000 ÷ 25,000 = $4.00 per sq. foot

Now allocate each support cost:

| Department | IT Cost Allocated | HR Cost Allocated | Facilities Cost Allocated | **Total Allocated** |
|---|---|---|---|---|
| Production A | 30 × $4,444.44 = $133,333 | 60 × $1,666.67 = $100,000 | 15,000 × $4.00 = $60,000 | $293,333 |
| Production B | 15 × $4,444.44 = $66,667 | 30 × $1,666.67 = $50,000 | 10,000 × $4.00 = $40,000 | $156,667 |
| **Total Allocated** | **$200,000** | **$150,000** | **$100,000** | **$450,000** |

**Total cost after allocation:**

- Production A: $500,000 + $293,333 = **$793,333**
- Production B: $400,000 + $156,667 = **$556,667**

The direct method is fast and transparent. But it ignores that IT provides 5 users to the IT department itself, HR manages the HR department, and Facilities occupies 1,000 sq. ft. Those internal costs are *absorbed* by the production departments and effectively shifted proportionally to them. Many accountants consider this imprecise.

## The Step-Down Method

The **step-down method** recognizes that support departments serve each other. The usual order is:

1. Facilities (consumes the fewest services from other depts)
2. IT (consumes Facilities, provides to HR and Production)
3. HR (provides to Production)
4. Production depts (consume the others)

**Step 1: Allocate Facilities**

Facilities costs are allocated to *all* other departments (IT, HR, Production A, Production B), using the full headcount (including Facilities' own staff):

- Allocation rate: $100,000 ÷ 29,500 sq. ft. = $3.39 per sq. foot

| Department | Allocation |
|---|---|
| IT Dept | 2,000 × $3.39 = $6,780 |
| HR Dept | 1,500 × $3.39 = $5,085 |
| Production A | 15,000 × $3.39 = $50,850 |
| Production B | 10,000 × $3.39 = $33,900 |
| **Total** | **$100,000** |

**Step 2: Allocate IT (now includes Facilities allocation)**

IT's new total: $200,000 + $6,780 = $206,780

IT is allocated to HR, Production A, and Production B (not back to Facilities, which has already been allocated):

- IT users excluding IT dept itself: HR (3) + Production A (30) + Production B (15) = 48
- Allocation rate: $206,780 ÷ 48 = $4,307.50 per user

| Department | Allocation |
|---|---|
| HR Dept | 3 × $4,307.50 = $12,922.50 |
| Production A | 30 × $4,307.50 = $129,225 |
| Production B | 15 × $4,307.50 = $64,612.50 |
| **Total** | **$206,780** |

**Step 3: Allocate HR (now includes Facilities and IT allocations)**

HR's new total: $150,000 + $5,085 + $12,922.50 = $168,007.50

HR is allocated to Production A and Production B:

- Employees in HR (excluding HR itself): Production A (60) + Production B (30) = 90
- Allocation rate: $168,007.50 ÷ 90 = $1,866.75 per employee

| Department | Allocation |
|---|---|
| Production A | 60 × $1,866.75 = $112,005 |
| Production B | 30 × $1,866.75 = $56,002.50 |
| **Total** | **$168,007.50** |

**Step 4: Total Allocated Costs**

| Department | Original Cost | Facilities | IT | HR | **Total** |
|---|---|---|---|---|---|
| Production A | $500,000 | $50,850 | $129,225 | $112,005 | **$792,080** |
| Production B | $400,000 | $33,900 | $64,612.50 | $56,002.50 | **$554,515** |
| **Total** | **$900,000** | **$100,000** | **$206,780** | **$168,007.50** | **$1,346,595** |

## Comparison

| Metric | Direct Method | Step-Down Method |
|---|---|---|
| Production A Total Cost | $793,333 | $792,080 |
| Production B Total Cost | $556,667 | $554,515 |
| **Difference** | — | $1,253 shift to A, $2,152 shift to B |

In this example, the difference is small (< 1%). In larger firms with heavier interdepartmental service sharing, step-down allocations can shift product costs by 5–15%, materially changing which products appear profitable.

## Why the Method Matters

If the company uses the direct method and Product X has a unit cost of $100, but the step-down method yields $103, the difference might determine whether a pricing decision or a make-or-buy decision is sound. Accountants and cost managers must choose a method and apply it consistently, disclosing the choice in footnotes.

The step-down method is a practical middle ground: more realistic than direct allocation, but far simpler than the reciprocal method (which requires solving simultaneous equations and is rarely used outside textbooks).

## See also

<div class="wiki-seealso">

### Closely related

- [Accrual Accounting](/accrual-accounting/) — The framework within which cost allocation occurs.
- [Generally Accepted Accounting Principles](/generally-accepted-accounting-principles/) — Standards governing support cost treatment.
- [Cost of Debt](/cost-of-debt/) — How indirect financing costs are allocated in valuation.
- [Revenue Recognition](/revenue-recognition/) — How allocated costs affect profit reporting.

### Wider context

- [Income Statement](/income-statement/) — Where allocated overhead appears.
- [Budgeting Methods](/budgeting-methods/) — How forecasted support costs flow into departmental budgets.
- [Return on Invested Capital](/return-on-invested-capital/) — How accurate cost allocation improves ROIC analysis.

</div>
