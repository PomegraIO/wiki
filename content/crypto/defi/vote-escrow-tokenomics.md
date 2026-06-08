---
title: "Vote-Escrow Tokenomics"
description: "The ve-model that locks governance tokens for voting power and participation in protocol decisions, aligning long-term incentives."
keywords:
  - vote escrow
  - ve tokenomics
  - governance
  - token locking
  - voting power
  - curve dao
image: "/svg/crypto.svg"
---

*The vote-escrow (ve) model locks governance tokens for a set duration in exchange for voting power, a share of protocol revenue, or other benefits. Originated by Curve Finance, the ve-model forces a choice between liquid (but powerless) tokens and illiquid (but influential) ones, reducing short-term sell pressure while directing capital and decision-making power toward long-term stakeholders.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Vote-Escrow Tokenomics — key facts</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for decentralized finance." />

<div class="wiki-infobox-caption">Locking tokens for voting power aligns governance with long-term protocol success.</div>

|   |   |
|---|---|
| **What it is** | Locking governance tokens for a commitment period to gain voting influence and revenue share |
| **Originated by** | Curve Finance (2020, Curve DAO / veCRV) |
| **Lock duration** | Typically 1 week to 4 years; longer lock = more voting power per token |
| **Voting power formula** | Often linear with lock duration: 1 CRV locked for 4 years = ~4 veCRV |
| **Benefits of locking** | Governance votes, protocol fee revenue share, emission boost, governance multisig seat |
| **Tradeable votes** | Some protocols allow veCRV/veOHM to be traded; others make them non-transferable |

</aside>

## Why Curve created the model

[Curve Finance](/etf/) dominates stablecoin and correlated-asset trading. Its native token, CRV, distributed as [liquidity mining](/etf/) rewards. But pure liquidity mining creates misalignment: LPs earn CRV, immediately dump it, and then leave the protocol. Curve needed long-term governance committed to the protocol's success, not short-term mercenaries chasing yield.

Curve introduced veCRV (vote-escrow CRV) in 2020. Users who locked CRV for 4 years received maximum voting power. Those who locked for 1 week received minimal voting power. The longer you locked, the more votes you had. The voting power decayed linearly: as your lock approached expiration, your votes diminished.

The genius of the model was immediate. It created two distinct token classes: liquid CRV (worthless for governance) and locked veCRV (powerful). Long-term believers locked tokens and captured governance. Short-term traders sold liquid CRV and had no say. The protocol shifted power to patient capital.

## The economic incentives

Vote-escrow models layer incentives on top of locking. Early Curve veCRV holders received:

1. **Governance votes** — influence over fee parameters, emission distribution, and protocol upgrades
2. **Fee revenue share** — a portion of the 0.04% trading fees from the entire Curve protocol flowed to veCRV holders, usually distributed weekly
3. **Emission boost** — liquidity miners who locked their CRV received 2.5x higher token rewards on subsequent farming

These benefits compound. If you believe in Curve's long-term success, locking for 4 years gives you voting control, a steady revenue stream, and higher future yield. The longer you lock, the more compelling the case becomes.

The model also created scarcity. Only a fraction of circulating tokens are ever locked—most holders prefer liquidity. This makes locked tokens power-concentrated. In Curve's case, veCRV holders represent perhaps 10–30% of all CRV, but control 100% of governance. Ownership of the protocol is concentrated in committed hands.

## Fee revenue and sustainability

Fee capture for locked-token holders was transformative. In earlier DAO models, governance tokens had no cash flow. Owning UNI or COMP gave you votes, but no revenue—they were voting chips, not equity. Vote-escrow made tokens revenue-bearing. A veCRV holder locks $100,000 worth of CRV for 4 years and receives steady fee distributions, say $5,000–$15,000 per year (depending on Curve volume).

This creates a different incentive structure. A holder who receives revenues is motivated to grow the protocol's trading volume. They function like shareholders in a traditional equity. Early protocols offered extreme yields—Olympus DAO's governance tokens promised 80–100% APY to lockers (later unsustainable)—but modern ve protocols aim for 5–20% APY from genuine fee revenue.

The sustainability of this model depends entirely on protocol cash flow. If Curve maintains high trading volume and collects meaningful fees, veCRV is a dividend-bearing asset. If volume collapses, fee distributions decline and lock incentives evaporate.

## Governance concentration and veTokenomics arms races

The model created a new dynamics: protocols competing for locked capital. If you hold large amounts of CRV, you can lock it and control Curve's governance. But what if you hold other ve-tokens? The Balancer ecosystem, Aave, and dozens of newer protocols adopted ve-models.

This created a phenomenon: "ve-tokenomics wars." Large holders (often hedge funds, treasuries, or wealthy individuals) lock tokens across multiple protocols to maximize voting power and fee share. A holder with $10 million locked in Curve, Balancer, Aave, and Convex controls governance across all four. Protocols began paying voting incentives—bribing lockers—to vote their way.

Convex Finance amplified this dynamic. Convex lets users deposit CRV into a smart contract, which locks it for maximum veCRV power on behalf of users. Convex then uses that vast veCRV to direct Curve emissions to select pools, and gives Convex users a share of the rewards. Most CRV is now locked via Convex, concentrating power further. Convex essentially became the de facto governor of Curve, generating enormous fees for Convex token holders.

## Evolution and variations

The original Curve model was non-transferable: veCRV could not be traded. You either locked your CRV or didn't; there was no secondary market. This was intentional—it prevented whales from renting votes and ensured lock-in was genuine.

Later protocols introduced tradeable ve-tokens. Balancer's veBAL and Aave's veAIAVE can be bought and sold, creating liquid voting markets. This undermined the lock-in, because someone could buy voting power without the long-term commitment, but it increased liquidity and access.

Some newer protocols use decay curves instead of linear decay: your voting power decays faster as the lock period shortens, incentivizing longer locks. Others introduced "revenue bonds"—locking not just for votes, but for guaranteed fee distributions that are actually backed by protocol revenue, not promises.

## Governance quality and concentrated power

The model has a tension: locking aligns incentives, but it also concentrates power. Early ve protocols were governed by a handful of large lockers or organized blocs (whales cooperating to control outcomes). This led to some protocols making poor decisions—voting themselves massive incentives, acquiring bad assets, or allocating emissions inefficiently.

Some protocols mitigate this with multi-sig committees (trusted governance board that reviews major votes) or time-locks (decisions cannot execute immediately, giving the community time to challenge them). These layers reduce both agility and decentralization, but improve governance quality.

## See also

<div class="wiki-seealso">

### Closely related

- [Protocol-owned liquidity](/protocol-owned-liquidity/) — often paired with ve-models to reduce liquidity mining costs
- [Concentrated liquidity](/concentrated-liquidity/) — efficient AMM mechanic frequently governed by ve-token holders
- [Governance token](/dividend/) — the asset that ve-models operate on
- [Decentralized governance](/dividend/) — the decision-making process ve-tokens enable
- [Liquidity mining](/etf/) — often combined with ve-models to direct emissions

### Wider context

- [Shareholder equity](/common-stock/) — traditional ownership analogue that ve-models approximate
- [Dividend](/dividend/) — the fee distributions ve-lockers receive
- [Automated market maker](/etf/) — the protocol type most commonly using ve-models

</div>
