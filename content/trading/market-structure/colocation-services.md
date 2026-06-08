---
title: "Colocation Services"
description: "Exchange-hosted server space that allows high-frequency trading firms to place their servers microseconds closer to matching engines."
keywords:
  - high-frequency trading
  - colocation
  - latency
  - market structure
  - algorithmic trading
  - microseconds
  - competitive advantage
image: "/svg/trading.svg"
---

*Colocation services are physical server arrangements offered by stock exchanges and trading venues, in which a firm rents space in the exchange's data center to house its own trading servers. By placing hardware mere feet or metres from the exchange's matching engine, a trader gains a fractional-second advantage over remote competitors—an advantage that, at high-frequency scales, can translate to enormous profits and market distortions.*

## The speed advantage

In traditional [market-maker trading](/market-maker-trading/), physical distance mattered little. Today, it matters absolutely. A buy order placed from a server 100 miles away travels across fibre-optic cables and through dozens of routers before reaching the exchange's matching engine; the round-trip latency is measured in milliseconds. A server in the exchange's colocation facility, by contrast, reaches the engine in microseconds—often fewer than 100 microseconds.

This microsecond advantage is not academic. In [algorithmic trading](/algorithmic-trading/) strategies, especially [high-frequency trading](/algorithmic-trading/), the trader who sees a price move first and can submit an order nanoseconds before the rest of the market gains a decisive edge. They can front-run, arbitrage, or simply hit [bid-ask spreads](/bid-ask-spread/) before slower traders can react.

## How colocation works

Exchanges offer colocation as a commercial service, much like renting office space. A trading firm signs a contract, pays a monthly fee (often thousands of dollars), and installs its servers in the exchange's facility. The firm's technicians maintain the hardware; the exchange maintains power, cooling, and network connectivity to the matching engine.

The service is deliberately standardized—exchanges offer colocation to any qualified participant, not only favoured customers. Legally, this neutrality helps exchanges defend themselves against charges of unfair advantage. Practically, it means only the richest and most sophisticated traders can afford to use it effectively. A retail investor has no realistic path to colocation; the setup cost and monthly fees are prohibitive.

## The arms race in latency

Colocation has triggered a competitive arms race. Firms invest heavily in optimizing not just latency but latency variance. Submitting an order in 50 microseconds is good; submitting it in 50 microseconds ±2 microseconds is better, because predictability allows better timing of dependent trades.

Exchanges respond by upgrading their matching engines and network hardware. Some offer tiered colocation options: standard colocation, and premium colocation with direct connections to the matching engine or reserved bandwidth. Firms then optimize their software to extract every nanosecond of advantage—this is where the real engineering cost lies.

## Regulatory questions

Colocation itself is not illegal. The [Securities and Exchange Commission](/securities-and-exchange-commission/) permits it, and exchanges advertise their colocation facilities openly. However, regulators worry that it exacerbates [information asymmetry](/bid-ask-spread/) and speeds up [market timing](/market-timing/) strategies that may harm ordinary investors.

In particular, colocation enables certain [spoofing](/spoofing-and-layering/) and [layering](/spoofing-and-layering/) tactics. A trader with microsecond latency can place fake orders, observe how the market reacts at the nanosecond scale, and cancel them before anyone else's response order even arrives at the exchange. This makes detection harder and the manipulation more profitable.

Some policymakers have argued for latency floors—rules that would artificially slow down all trading to some minimum level, eliminating the advantage of colocation. No such rule has been implemented in the U.S., in part because such a change would require exchanges and brokers to agree (and they have no incentive to do so) or would require a major statutory change.

## Fairness and market integrity

The fairness critique goes deeper than latency. Colocation is, fundamentally, a way of converting money into speed. Only firms with sufficient capital can afford it; only those firms can compete effectively in speed-dependent trading. This creates a two-tier market: fast traders (colocated) who can respond instantaneously to events, and slow traders (everyone else) who are at a structural disadvantage.

Some argue this is simply the nature of capitalism—those who invest more get better tools. Others argue that exchanges, being public institutions or utility-like entities, have an obligation not to sell speed advantages that corrupt price discovery. The debate remains unresolved.

## The broader ecosystem

Colocation has also driven development of adjacent services. Data-center operators now specialize in ultra-low-latency hosting. Financial-technology companies sell software optimized for microsecond response. Networking firms build and maintain the fibre-optic cables that connect trading centers. An entire industry exists to serve the colocation market, even as most participants remain ignorant of it.

## Reality check: who actually uses it

Despite the publicity, the majority of equity trading volume in major markets is still conducted by traditional brokers and [market makers](/market-maker-trading/) with conventional infrastructure. Colocation use is concentrated in certain strategies: index arbitrage, statistical arbitrage, latency-sensitive liquidity-provision, and [spoofing](/spoofing-and-layering/) or front-running tactics.

For most retail and long-term institutional investors, colocation is irrelevant; their brokers execute on their behalf using ordinary infrastructure. But for the strategies that do depend on speed, colocation has become an essential competitive tool, and the fees it commands are a legitimate cost of doing business.

## See also

<div class="wiki-seealso">

### Closely related

- [Algorithmic trading](/algorithmic-trading/) — the trading strategies that benefit most from colocation
- [High-frequency trading](/algorithmic-trading/) — the extreme end of speed-dependent trading
- [Market maker trading](/market-maker-trading/) — traditional liquidity provision, now often combined with colocation
- [Bid-ask spread](/bid-ask-spread/) — narrowed by faster traders with better information
- [Spoofing and layering](/spoofing-and-layering/) — manipulative tactics enabled by colocation's latency advantage
- [Price discovery](/price-discovery/) — corrupted when speed becomes the dominant advantage

### Wider context

- [Market timing](/market-timing/) — the broader category of strategies that exploit small price movements
- [Securities and exchange commission](/securities-and-exchange-commission/) — regulator of exchange colocation services
- [Information asymmetry](/bid-ask-spread/) — worsened by speed advantages
- [Block trading facility](/block-trading-facility/) — an alternative venue designed to reduce the speed advantage

</div>
