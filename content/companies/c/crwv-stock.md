---
title: "CoreWeave, Inc. (CRWV)"
description: "CoreWeave operates cloud GPU infrastructure — rented compute capacity that powers machine-learning model training and inference at scale. Its business focuses on specialised, GPU-heavy workloads where general-purpose cloud providers come second."
keywords:
  - cloud infrastructure
  - GPU compute
  - machine learning
  - data centre operations
  - cloud services
handwritten: true
---

CoreWeave is a cloud-infrastructure company built to serve a narrow but crucial slice of computing: the GPU-powered workloads that train and run large machine-learning models. The company operates data centres stocked with graphics processors — chips that excel at the matrix mathematics that neural networks require — and leases access to that compute capacity to researchers, startups, and enterprises building or running AI systems. Its thesis is that general-purpose cloud providers like Amazon Web Services and Google Cloud have underinvested in GPU supply relative to demand, and that a specialist operator with purpose-built infrastructure can capture premium margins by meeting that demand first.

## What does CoreWeave actually do?

CoreWeave provides cloud-based GPU compute through a software layer — customers connect via API, request instances configured with one or more GPUs (typically [NVIDIA](/nvda-stock/)'s flagship chips), run their workloads, and pay per hour of compute consumed. The company has built a network of data centres, initially in North America, each outfitted with bulk GPU hardware, networking capable of handling the high-bandwidth requirements of large-model training, and the software plumbing that parcels out resources to customers.

The business is capital-intensive in a specific way: it requires heavy upfront spending on data-centre construction and hardware [acquisition](/acquisition/), but once those assets are built, the marginal cost of leasing additional capacity is low. This structure — high fixed costs, low variable costs — means unit economics improve sharply as utilisation rises. A data centre running at 95 per cent capacity is far more profitable than one at 60 per cent, which creates strong incentives to fill capacity and strong penalties for idle hardware.

## Why does GPU capacity matter so much right now?

The explosive growth of large language models and other neural-network applications has created an enormous appetite for GPU compute, and that appetite has outpaced the supply of available machines. The dominant GPU manufacturer, NVIDIA, has struggled to produce enough chips to meet demand. General-purpose cloud providers can offer GPU instances, but they often have long waitlists, and they optimise their hardware portfolios toward the broadest possible customer base, not specifically toward the compute-intensive training runs that machine-learning researchers and companies require. CoreWeave's pitch is that it exists purely to serve that demand — it buys as many GPUs as it can acquire, provisions them in dense clusters optimised for machine learning, and leases them out.

This positions CoreWeave in a privileged place in the supply chain: it sits between customers desperate for access to GPU capacity and NVIDIA, which can barely satisfy the entire world's demand for its chips. As long as that imbalance persists, companies offering dedicated GPU infrastructure have significant pricing power.

## How does CoreWeave make money?

CoreWeave's revenue model is straightforward: customers pay per instance-hour for GPU access, similar to how general-purpose cloud providers charge for compute. The pricing scales with the specific GPU model (older, slower chips are cheaper; the latest flagship NVIDIA GPUs command premium rates) and the complementary resources bundled with it (CPU, memory, bandwidth, storage). Some customers run short jobs lasting hours; others have multi-month training runs that consume thousands of GPU-hours.

The company also offers reserved-capacity agreements, where customers commit to future usage and receive a discount, trading flexibility for lower unit costs. These contracts provide revenue visibility that pure spot-pricing lacks.

Profitability depends entirely on utilisation and the spread between what CoreWeave pays for hardware and what it charges customers. If the company can maintain high utilisation — keeping its data centre GPUs busy — and if the cost of acquiring hardware remains below the premium customers will pay, margins can be substantial. But the relationship is brittle: a slowdown in demand, a collapse in GPU prices, or a sudden influx of general-purpose cloud capacity could squeeze margins quickly.

## What are the structural risks?

The business model exposes CoreWeave to several pressures. First, **NVIDIA dependency:** the company is hostage to NVIDIA's ability to supply GPUs in the volumes it needs. If NVIDIA's yield improves and supply becomes abundant, prices will fall, and CoreWeave's margins erode. If NVIDIA falters or faces geopolitical restrictions (as has threatened), CoreWeave's own supply dries up.

Second, **customer concentration:** the market for GPU capacity is dominated by a small number of large model-training companies and research labs. A handful of customers likely account for a substantial fraction of CoreWeave's revenue. The loss of a major customer is a material risk.

Third, **capital intensity and cash burn:** CoreWeave must continually spend tens of millions of dollars on new hardware and infrastructure to stay ahead of demand. That requires either profitable operations generating cash, external funding, or both. Any extended period of underutilisation, margin compression, or unexpected technical costs could force the company to raise capital at unfavourable terms or slow expansion.

Fourth, **competition:** as GPU supply improves or as general-purpose cloud providers invest more heavily in GPU infrastructure, CoreWeave's moat weakens. If AWS or Google Cloud can match CoreWeave's availability and undercut on price by bundling GPU compute with their broader suite of services, CoreWeave becomes a secondary option.

## How does CoreWeave differentiate itself?

The company's edge rests on speed and specialisation. It can provision GPUs faster than generalist competitors, often with minimal queueing. Its data centres are architected specifically for the patterns of GPU-heavy workloads — high-bandwidth interconnects between machines, careful placement of storage to minimise latency, and a customer-service layer tuned to technical teams who need rapid iteration. It is not trying to be a full-service cloud provider like AWS; it is trying to be the fastest, most responsive supplier of a specific commodity.

The company has also invested in developer experience — tooling that makes it easy to launch workloads, port code from other clouds, and manage billing. For a startup or researcher, being able to spin up GPU capacity in minutes rather than weeks is a meaningful advantage.

## What should a reader watch?

The health of CoreWeave's business is visible in a few metrics and narratives. Quarterly customer additions and revenue per customer reveal demand and pricing power. Gross margin trends show whether the company is retaining pricing advantage or being forced to compete harder. Utilisation rates indicate whether capacity is being filled or sitting idle. Any commentary from management about capital deployment plans reveals how aggressively the company is building new data centres — aggressive expansion signals confidence in future demand, but it also locks in spending.

A reader researching CoreWeave should begin with the company's annual 10-K filing (SEC CIK 0001769628) and quarterly earnings statements, which break down revenue by customer segment, discuss capital spending plans, and lay out management's assessment of risks. The earnings calls are where colour appears — watch for discussion of GPU availability, customer demand trends, pricing, and any changes to the competitive landscape.

The trajectory of GPU pricing and NVIDIA's supply situation is external but crucial context. Any deterioration in GPU availability relative to demand benefits CoreWeave; any improvement threatens it. Similarly, developments in the large-language-model market — whether demand for training capacity remains insatiable or begins to cool — directly affect the company's prospects. Finally, the competitive moves of AWS, Google Cloud, and other infrastructure providers are worth tracking. If general-purpose clouds announce major GPU availability improvements, CoreWeave's pricing power and growth could be constrained.
