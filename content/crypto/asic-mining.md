---
title: "ASIC Mining"
description: "An ASIC miner is specialised hardware designed specifically for cryptocurrency mining. ASIC stands for application-specific integrated circuit and refers to chips optimised to solve proof-of-work puzzles efficiently."
keywords:
  - asic
  - application-specific integrated circuit
  - mining hardware
  - bitcoin mining
  - specialised hardware
  - hash rate
image: "/svg/crypto.svg"
---

*An **ASIC** (application-specific integrated circuit) **miner** is specialised hardware designed solely for [cryptocurrency mining](/mining-bitcoin). ASICs are thousands of times more efficient than general-purpose computers or GPUs at solving [proof-of-work](/proof-of-work) puzzles, making them the only economically viable option for mining [Bitcoin](/bitcoin) and similar proof-of-work cryptocurrencies.*

<div class="wiki-hatnote">

This entry covers ASIC hardware. For mining generally, see [mining Bitcoin](/mining-bitcoin); for mining pools, see [mining pool](/mining-pool); for the underlying algorithm, see [proof-of-work](/proof-of-work).

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">ASIC Mining — key facts</div>

<img src="/svg/crypto.svg" alt="Modern ASIC miner hardware" />

<div class="wiki-infobox-caption">An ASIC miner: specialised hardware for mining.</div>

|   |   |
|---|---|
| **What it is** | Custom chip designed for mining |
| **Efficiency** | 1,000–10,000x better than GPU |
| **Cost** | $1,000–$10,000+ per unit |
| **Lifespan** | 3–7 years before becoming obsolete |
| **Power consumption** | 1–3 kilowatts per unit |
| **Hash rate** | 50–100 terahash/second (modern) |
| **ROI** | 6 months–2 years (at current prices) |
| **Manufacturer** | Bitmain, Whatsminer, Canaan, others |

</aside>

## What is an ASIC?

An ASIC is a custom-designed computer chip optimised for a single task: computing the hash function used in [proof-of-work](/proof-of-work) mining. Unlike a CPU or GPU, which are general-purpose and can run any software, an ASIC is hardwired to do one thing — and does it very efficiently.

For example, a Bitmain Antminer S21 is an ASIC designed for Bitcoin mining (using SHA-256 hashing). It cannot run general software, cannot mine other cryptocurrencies, and becomes worthless when the algorithm it targets is abandoned.

## Efficiency advantage

An ASIC is thousands of times more efficient than a GPU or CPU:

- **CPU:** ~1 megahash per second (MH/s), consuming 100W. Efficiency: 0.01 MH/s per watt.
- **GPU:** ~1 gigahash per second (GH/s), consuming 300W. Efficiency: 3 GH/s per watt.
- **ASIC:** ~100 terahash per second (TH/s), consuming 3,000W. Efficiency: 33 TH/s per watt.

An ASIC is roughly 3,300x more efficient than a GPU per unit power consumed.

This efficiency advantage is why ASIC mining dominates [Bitcoin](/bitcoin). A GPU miner would never find a block before an ASIC miner; the ASIC miner would find it first, every time.

## Cost and economics

ASIC miners are expensive: a modern Bitmain Antminer S21 costs ~$5,000–$10,000, depending on market conditions. Older models cost less but consume more electricity per hash.

An ASIC miner's profitability depends on:

1. **Electricity cost.** ASICs consume 1–3 kW; at $0.05–$0.15 per kWh, electricity is the dominant operating cost.
2. **Bitcoin price.** Higher prices improve profitability; lower prices can make mining unprofitable, causing miners to shut down.
3. **Competition.** Higher network [hash rate](/hash-rate) increases competition and reduces individual miner rewards.

Return on investment typically occurs within 6 months to 2 years, though this varies dramatically with Bitcoin price and electricity cost.

## ASIC manufacturers

- **Bitmain:** The largest manufacturer, producing the Antminer line.
- **MicroBT:** Produces the Whatsminer line, a major competitor.
- **Canaan:** Produces the Avalon line.
- **Others:** Ebang, Innosilicon, and smaller manufacturers.

These manufacturers compete on efficiency (hash rate per watt) and cost. A 10% improvement in efficiency can significantly improve miner profitability.

## Obsolescence and upgrades

ASIC miners become obsolete as the network [hash rate](/hash-rate) grows and newer, more efficient models are released. A miner that was profitable in 2020 might be unprofitable in 2024.

When an ASIC becomes unprofitable, miners face a choice:

1. **Mothball or resell.** Some miners keep old ASICs as backup or sell them on secondary markets.
2. **Mine a different coin.** An ASIC for SHA-256 (Bitcoin) might not work for other algorithms, but [Litecoin](/litecoin) uses a different algorithm (Scrypt), so SHA-256 ASICs cannot mine it.
3. **Scrap for parts.** Old ASICs are dismantled for components.

## The centralisation concern

ASIC mining has created a centralisation pressure: only wealthy entities or mining pools can afford ASICs and operate at scale. This threatens the decentralisation of cryptocurrencies.

[Bitcoin](/bitcoin) maximalists argue that decentralisation is still maintained because anyone can run an ASIC, and [mining pools](/mining-pool) are voluntary coalitions (miners can change pools). Critics argue that the wealth barrier is substantial enough to exclude ordinary users.

Some cryptocurrencies (like [Monero](/monero)) use ASIC-resistant algorithms to prevent ASIC dominance, though ASIC manufacturers eventually optimise for nearly every algorithm.

## Power consumption and cooling

A modern ASIC mining operation consumes megawatts of power and requires substantial cooling infrastructure. A large mining facility might have thousands of ASICs running 24/7.

This creates environmental concerns and explains why Bitcoin mining clusters are built in regions with cheap, abundant electricity (Iceland, El Salvador, etc.).

## Second-hand markets

Used ASICs sell on secondary markets (eBay, specialist forums) at reduced prices. A miner might buy a used ASIC for 50–70% of its original price when the miner upgrades to a newer model.

This allows smaller operators to mine profitably, though with lower efficiency than owning the latest hardware.

## Chip fabrication advances

ASIC efficiency improves roughly every 2–3 years as chip fabrication processes advance (from 7 nm to 5 nm to 3 nm, etc.). This "Moore's Law" dynamic drives constant hardware innovation and obsolescence cycles.

## See also

<div class="wiki-seealso">

### Closely related

- [Mining Bitcoin](/mining-bitcoin) — ASIC mining is the practical implementation
- [Hash rate](/hash-rate) — measure of total mining power
- [Mining pool](/mining-pool) — where ASICs typically contribute
- [Proof-of-work](/proof-of-work) — the mechanism ASICs solve
- [Difficulty adjustment](/difficulty-adjustment) — responds to ASIC deployment

### Wider context

- [Bitcoin](/bitcoin) — the most mined cryptocurrency
- [Litecoin](/litecoin) — uses Scrypt, different ASICs
- [Monero](/monero) — ASIC-resistant algorithm
- [Blockchain fundamentals](/blockchain-fundamentals) — the underlying technology

</div>
