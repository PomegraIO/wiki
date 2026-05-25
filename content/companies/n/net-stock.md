---
title: "Cloudflare (NET)"
description: "Global connectivity-cloud company providing CDN, DDoS protection, WAF, Zero Trust security, and edge computing services to enterprises and developers."
keywords:
  - cloudflare
  - content delivery network
  - ddos protection
  - zero trust security
  - edge computing
  - waf
handwritten: true
---

<aside class="wiki-infobox">

**Cloudflare, Inc.**
- **Ticker:** NET (NYSE)
- **CIK:** 1477333
- **Founded:** 2009
- **Headquarters:** San Francisco, CA
- **Sector:** Cloud infrastructure, cybersecurity
- **Business:** Global connectivity cloud providing CDN, DDoS mitigation, Web Application Firewall (WAF), Zero Trust security, DNS, and edge compute services

</aside>

Cloudflare operates as a connectivity platform sitting between internet users and origin web infrastructure. The company has reframed itself beyond a traditional content delivery network (CDN) into something more ambitious: a distributed computing platform that routes and processes traffic globally while layering security, performance, and intelligence into the flow. For enterprises navigating an increasingly complex threat landscape and expecting near-instant response times, Cloudflare has become a foundational piece of internet architecture.

## The Business Model

Cloudflare makes money primarily through subscription services, with customers paying based on traffic volume, feature tier, and add-on security modules. The pricing ladder runs from free plans (mostly for developers and tiny sites) through professional tiers targeting SMBs, enterprise tiers for large organizations, and specialized packages for high-security use cases. A single large enterprise customer might pay six or seven figures annually for full Cloudflare stack deployment.

The company does not charge per-request like older CDNs; instead, it uses monthly subscriptions tied to domain count, traffic volume, or security feature bundles. This creates recurring, predictable revenue and aligns Cloudflare's economics with customer success—faster, more secure sites drive customer stickiness. The business segments roughly into two streams: security services (DDoS, WAF, bot management, DNS filtering) and performance services (CDN, image optimization, caching). In practice, customers rarely buy just one. The bundle strategy is deliberate: a customer defending against DDoS attack traffic might as well accelerate legitimate requests through the same edge network.

## Competitive Position and What Drives Adoption

Cloudflare faces competition from older CDN players (Akamai, Fastly) and cloud giants (AWS CloudFront, Google Cloud CDN, Microsoft Azure) who offer similar capabilities embedded in their broader ecosystems. Yet Cloudflare has carved out sustained demand by being genuinely easier to deploy than Akamai's legacy systems, cheaper at scale than hyperscaler equivalents, and more specialized than general-cloud offerings.

The technical moat is real but not unassailable. Cloudflare's distributed edge footprint—network presence in hundreds of data centers worldwide—is expensive to replicate and creates genuine performance advantage. The security product (especially DDoS mitigation, which requires absorbing multi-terabit attacks in real time) benefits from scale: the more traffic Cloudflare touches, the better its threat detection algorithms become, and the harder it is for competitors to match protection quality without similar volume. WAF and bot-detection are somewhat easier to replicate, and Cloudflare faces pressure from specialized security vendors and from cloud-native SIEM/WAF startups.

What really cements stickiness is the developer experience. Cloudflare's API, dashboard, and worker-script platform are genuinely well-designed compared to Akamai's arcane configuration models. Developers choose Cloudflare, advocate for it internally, and that bottom-up adoption is durable. The company also benefits from being young enough to have built for a cloud-native world, while older competitors are still carrying technical debt from the pre-containerization era.

## Growth Dynamics and Pressure Points

Cloudflare's growth has outpaced the broader CDN market, but the law of large numbers applies. The company crossed $1 billion in ARR (annual recurring revenue) in 2023 and is chasing further expansion, but at much-larger scale, sustaining 40%+ year-over-year growth becomes harder. The company is pushing deeper into security (zero-trust networking, identity management) and applications (serverless compute via Workers) to drive incremental expansion within the installed base and to defend against displacement by hyperscalers bundling network and security into integrated offerings.

Pricing is also under pressure. Hyperscalers can afford to discount aggressively on CDN because it drives consumption of higher-margin services (compute, storage, data). Cloudflare must prove its all-in cost is lower and stickiness is higher, which works for many use cases but not all. Very large cloud-native enterprises with AWS or Google Cloud commitments can achieve acceptable CDN economics without adding Cloudflare. 

Another structural tension: Cloudflare's security services (DDoS, WAF, bot management) sometimes cannibalize each other in terms of pricing power. If a customer adopts DDoS protection, they are less likely to justify separate spending on bot management if Cloudflare bundles it. This drives customer concentration on fewer, larger deals rather than land-and-expand across point products.

## Evergreen Dependencies

The business is exposed to internet traffic patterns and the cybersecurity budget environment. During downturns, enterprises delay security upgrades and performance optimization projects. DDoS attacks themselves are not growing or shrinking predictably, and Cloudflare cannot predict when a major customer will face a catastrophic attack that either drives deeper commitment (sunk-cost psychology) or, if Cloudflare's mitigation is insufficient, erodes trust.

The competitive position with hyperscalers is long-term uncertain. AWS, Google Cloud, and Azure have incentive and capacity to embed superior CDN and DDoS protection directly into their networks. Cloudflare remains vendor-agnostic, which is its advantage; enterprises want not to be locked into one cloud's networking. But if the hyperscalers decide to bundle aggressively and absorb CDN margin as a loss leader for overall cloud adoption, Cloudflare's pricing power erodes.

## Researching Cloudflare

The [10-K](/wiki/10-k/) is essential reading: it details customer concentration (usually a handful of large customers represent a meaningful slice of revenue), product adoption trends across security and performance modules, and churn rates. Pay attention to comments on pricing dynamics and competitive pressure in the management discussion and analysis. Watch the quarterly earnings calls for tone on enterprise security budget health, win rates against incumbents, and uptake of newer product lines like Workers and Cloudflare Zero Trust (a rebranding of their identity and network access offering).

Relevant metrics to track: net dollar retention (how much existing customers expand spending year-over-year), customer count and average contract value, gross margin trends (Cloudflare has high gross margins as a software business), and whether the company is investing more in R&D relative to revenue (a sign of either defending against competition or chasing new markets). The business is profitable on an operating basis, but watch cash burn relative to [free cash flow](/free-cash-flow/), as the company has made strategic M&A to fill product gaps and accelerate adjacent markets.

The company's network and security services are not commodity—they are becoming infrastructure that large organizations expect their vendors and providers to integrate. Cloudflare's long-term value depends on deepening that integration and expanding from network edge into application edge and beyond, a transition the company has been orchestrating for the past several years. Success or failure will reshape the competitive landscape in edge infrastructure.
