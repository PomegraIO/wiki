---
title: "ZeroStack Corp. (ZSTK)"
description: "ZeroStack supplies cloud infrastructure software enabling enterprises to deploy and manage private cloud and edge computing environments without relying on public cloud providers."
keywords:
  - cloud infrastructure
  - edge computing
  - private cloud
  - virtualization
  - infrastructure software
  - data sovereignty
handwritten: true
---

ZeroStack is a software company that helps enterprises build and operate their own cloud infrastructure. Rather than relying wholly on public cloud providers, organizations use ZeroStack's platform to manage computing, storage, and networking resources across their own data centres or edge locations. The company occupies a strategic but contested market: customers that want cloud-like capabilities but with more control, lower long-term cost, or specific compliance and data-sovereignty requirements. It is a category that has attracted dozens of vendors, many with far more capital and brand awareness, which means ZeroStack's durability depends entirely on execution and the stickiness of its product.

<aside class="wiki-infobox">
<table>
<tr><th>Ticker</th><td>ZSTK (OTC Markets)</td></tr>
<tr><th>Founded</th><td>2013</td></tr>
<tr><th>Sector</th><td>Cloud infrastructure software</td></tr>
<tr><th>Primary product</th><td>Private cloud and edge computing platform</td></tr>
<tr><th>Customer base</th><td>Enterprise data centres, telecommunications, edge deployments</td></tr>
<tr><th>Business model</th><td>Software licensing and support services</td></tr>
<tr><th>SEC CIK</th><td>0001790169</td></tr>
</table>
</aside>

## Origins in the hypervisor era

ZeroStack was founded in 2013 at a moment when the cloud infrastructure category was rapidly consolidating. Amazon Web Services had established public cloud as a legitimate alternative to owning data centres, but many large enterprises remained hesitant: they had legacy workloads running on-premises, data residency and sovereignty requirements that public clouds did not satisfy, or concerns about long-term vendor lock-in and egress costs. At the same time, open-source virtualization technology — principally KVM and OpenStack — had matured enough that building private cloud infrastructure was technically feasible.

The company's founding thesis was straightforward: there was a market for software that let enterprises operate OpenStack-based private clouds without the operational burden of managing OpenStack themselves. Rather than asking customers to become OpenStack experts, ZeroStack would package OpenStack, add its own management and deployment tools, provide support, and handle upgrades and operational expertise. This positioning placed ZeroStack in the emerging category of "private cloud" or "on-premises cloud" — a middle ground between owning all infrastructure and surrendering entirely to a public cloud provider.

## The early product and platform strategy

ZeroStack's initial product was a software platform that could be deployed on standard x86 server hardware in a customer's own data centre. Once installed, it provided a cloud-like user experience: customers could provision virtual machines, manage networking, handle storage, and orchestrate workloads through APIs and a web interface. The underlying implementation built on OpenStack, but ZeroStack's value proposition was integration, support, and operational simplification — handling the complexity that made raw OpenStack difficult for many enterprises to adopt.

The company targeted mid-market and large enterprises with significant workloads, particularly those in heavily regulated industries where data residency was non-negotiable. Healthcare organizations, financial services firms, and government agencies represented strong early customer opportunities. These customers had the capital budget for on-premises infrastructure, the technical depth to evaluate and adopt new platforms, and the regulatory incentives to maintain data within their own four walls.

Revenue came from software licensing (either subscription-based or perpetual licenses plus support) and from professional services — implementation, customization, and operational support. The services component was high-margin but labour-intensive, creating a constraint on how fast the company could scale. The licensing component, by contrast, could scale without proportional cost increases, but required a large installed base to become meaningful.

## Expansion into edge computing

As the company matured through the mid-2010s, a new category — edge computing — began to emerge as adjacent opportunity. Edge computing distributes computing workloads closer to where data is generated: in retail locations, manufacturing facilities, telecom networks, or other distributed sites rather than in centralized data centres. The motivation is latency reduction, bandwidth savings, and operational resilience. But deploying workloads at the edge also requires software that can manage multiple small deployments, update them remotely, and maintain operational visibility across dozens or hundreds of locations simultaneously.

ZeroStack repositioned its platform to address this opportunity. The same underlying software that managed private clouds in data centres could, with appropriate refinement, manage compute resources spread across dozens of edge locations. This gave the company a growth vector beyond the existing on-premises cloud market, particularly in telecommunications and industrial sectors.

## The competitive gauntlet

By the late 2010s, ZeroStack faced a crowded and well-funded competitive landscape. Cloud infrastructure software attracted investment because the market itself was enormous. Canonical (the company behind Ubuntu Linux) invested heavily in OpenStack and related tooling. Red Hat released OpenStack and later acquired it through the Kubernetes ecosystem, betting on hybrid cloud as a category. VMware, a long-established virtualization vendor, built vCloud to address hybrid workloads. And all the while, AWS, Microsoft Azure, and Google Cloud invested billions in making their public cloud offerings more cost-effective and feature-complete, narrowing the gap that had once made private cloud attractive.

ZeroStack's challenge was becoming acute: it had viable technology and real customers, but it was the smallest player in a market that seemed to be consolidating around larger, better-capitalized competitors. Red Hat's OpenStack ambitions, backed by IBM's subsequent acquisition of Red Hat, gave that ecosystem massive resources. VMware's installed base of on-premises virtualization made vCloud an easier sell to existing customers. Meanwhile, the public cloud providers were steadily improving their offerings, making the economic case for private cloud weaker over time.

## Present-day position and strategy

Today, ZeroStack persists as a smaller vendor in a market that has partially bifurcated. The "pure private cloud" segment has contracted as public cloud became both more capable and, often, more cost-effective than enterprises expected. But a genuine demand persists for on-premises and edge-deployable cloud platforms in specific verticals: telecommunications companies running containerized workloads in distributed networks, manufacturing firms deploying industrial edge computing, government agencies with strong data sovereignty requirements, and enterprises that have made strategic bets on retaining infrastructure in-house.

ZeroStack's survival strategy hinges on serving these niches exceptionally well, building deep relationships in verticals like telecommunications where edge computing genuinely aligns with network architecture, and maintaining a lean cost structure that does not require the scale that larger competitors demand. The company must also continually evolve its platform to integrate with modern containerization and orchestration tools — Kubernetes has become the industry standard for workload orchestration, so any edge or private cloud platform must integrate seamlessly with Kubernetes and related cloud-native tooling.

## Evaluating ZeroStack

Start with the company's most recent 10-K filing (SEC CIK 0001790169) to understand revenue sources, the health and concentration of its customer base, and management's own articulation of competitive threats. Pay particular attention to customer acquisition cost and customer retention rates — these metrics reveal whether the business model is sustainable and whether the product has become truly sticky to its user base.

Monitor the company's evolution of its platform: does it keep pace with industry standards like Kubernetes, containerization, and cloud-native development patterns? A private cloud platform that lags in these areas will find that new customer deployments gravitate toward more modern stacks.

Watch the telecommunications sector specifically. This is where ZeroStack's edge computing positioning has the strongest rational basis, and any wins or losses in major telecom deployments represent concrete evidence of whether the company's strategy is resonating. Track any partnership announcements, particularly with major infrastructure vendors or cloud-native ecosystem players. These indicate whether ZeroStack is gaining or losing relevance in how enterprises architecture their distributed computing infrastructure.
