---
title: "Eclipse Attack on Blockchain Nodes"
description: "An eclipse attack monopolises a blockchain node's peer connections to deliver false chain data, enabling double-spends or wasted mining effort."
keywords:
  - eclipse attack blockchain nodes
  - eclipse attack cryptocurrency
  - network isolation attack
  - sybil attack peer-to-peer
  - blockchain network security
  - node eclipse attack
image: "/svg/crypto.svg"
---

*An **eclipse attack** occurs when an attacker floods a blockchain node's peer list with malicious nodes it controls, forcing the target to communicate only with that attacker's network. This isolation lets the attacker feed false chain data to the victim, potentially enabling double-spends, orphaning valid blocks, or wasting mining resources.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Eclipse Attack — Key Facts</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">A network-layer attack that severs a node from honest peers.</div>

|   |   |
|---|---|
| **Attack type** | Network isolation; Sybil-attack variant |
| **Target** | Individual blockchain node |
| **Attacker requirement** | Control of many IP addresses or accounts |
| **Outcome** | Node receives false blockchain state |
| **Risk to** | Full nodes, mining pools, light clients |
| **Defense** | Outbound connection limits, persistent peers, IP diversity checks |

</aside>

## How the Eclipse Attack Works

A blockchain node maintains a list of peer addresses it can connect to. When the node needs new peers, it queries existing neighbors for recommendations or fetches lists from seed nodes. An attacker running many malicious nodes can exploit this process by flooding the peer discovery system with its own addresses.

Once the attacker's nodes dominate the victim's peer list, legitimate connections drop away. The node's new peers connect only to the attacker's infrastructure. From that point forward, the isolated node receives only the data the attacker chooses to send—whether a genuine blockchain state or a false one.

The eclipse attack succeeds because peer-discovery protocols historically lacked defenses against [Sybil attacks](/sybil-attack/). In a Sybil attack, one attacker creates many fake identities (nodes) to gain disproportionate influence. Blockchain networks did not always distinguish between one honest peer and one hundred nodes controlled by the same adversary.

## The Attack Vector: Peer Discovery and IP Spoofing

Most blockchain nodes use gossip protocols to learn about new peers. A node might ask, "Who else should I connect to?" Existing peers respond with a list of addresses. An attacker can:

1. Run hundreds or thousands of malicious nodes on different machines or cloud instances
2. Inject these addresses into the peer-discovery process
3. Ensure these addresses spread through the gossip network
4. Wait for the victim node to request new peer recommendations and receive mostly attacker nodes

The attack is cheaper and faster on large IP-address ranges and public cloud providers where an attacker can spin up instances quickly. If the victim node lacks strong filtering, it will eventually have more connections to hostile nodes than honest ones.

## Practical Consequences: Double-Spend and Wasted Work

An eclipse-attacked node operates on false information. Consider these scenarios:

**Double-spend scenario:** An attacker isolates a merchant's node and sends it a transaction paying for goods, then broadcasts a conflicting spend to the honest network. The merchant's isolated node believes the payment is valid (because the attacker's nodes confirm it), ships the goods, but later finds the transaction invalid on the real chain—the funds were already spent elsewhere.

**Mining pool attack:** If an attacker eclipses a mining pool's nodes, the pool mines on a false chain history, wasting hash power on blocks that won't be accepted by the main network. The attacker's own nodes or accomplices mine the real chain, capturing rewards the victim should have earned.

**Orphaning blocks:** A node receiving false chain data may reject valid blocks from the honest network as "stale" or conflicting, fragmenting consensus for a period.

## Defenses and Mitigations

Modern blockchains employ several protections:

**Connection limits:** A node limits how many peers it accepts from any single source or IP range. This raises the attacker's cost—they must control many distinct IP addresses.

**Persistent peer connections:** Nodes maintain long-term connections to trusted, manually-configured peers that an attacker cannot easily eclipse. These connections act as an anchor to the honest network.

**IP diversity checks:** Before accepting a peer, the node verifies that peer recommendations come from different IP subnets. If all recommendations cluster in a few address ranges, the node becomes suspicious.

**Proof-of-work or stake filters:** Some protocols weight peer recommendations by the recommender's stake or hash rate, making it harder for a low-resource attacker to poison the list.

**Outbound connection diversity:** The most effective defense: a node initiates outbound connections to random peers, not only peers that advertise themselves. This randomness makes it harder to predict and control which nodes a victim will connect to.

## Eclipse Attacks vs. Sybil Attacks

The terms overlap but are distinct. A [Sybil attack](/sybil-attack/) is creating many fake identities to gain influence in a system. An eclipse attack uses Sybil identities to isolate a target. An eclipse attack is a *directed* form of Sybil exploitation.

Not all Sybil attacks aim to eclipse a node—some simply inflate voting power in consensus or governance. But most practical eclipse attacks require a Sybil component to work at scale.

## Historical Examples and Remedies

Early Bitcoin clients were vulnerable to eclipse attacks because they relied heavily on DNS seed nodes and lacked strict peer diversity. Attackers could eclipse mining pools, causing them to lose work. Bitcoin addressed this by:

- Requiring nodes maintain at least 8 outbound connections (later hardened)
- Using cryptographic seeds to randomize peer selection
- Implementing asmap-based IP diversity to detect clustering

Ethereum and other protocols have adopted similar defenses, particularly cryptographic proof requirements for peer identity and rate-limiting of peer advertisements.

## Detecting an Eclipse Attack

A node under eclipse may show signs:

- Extremely long block propagation times or persistent sync delays
- Sudden absence of transactions visible on other nodes
- Receiving blocks with timestamps far in the past or future
- Peer list dominated by nodes in geographically implausible locations

Operators running critical nodes (exchanges, mining pools, validators) often monitor peer diversity and maintain manual trusted-peer lists as a safety net.

## See also

<div class="wiki-seealso">

### Closely related

- [Sybil attack](/sybil-attack/) — Creating many fake identities to influence a distributed system
- Peer-to-peer network security — Defending decentralized networks against network-layer attacks
- Double-spend — Spending the same digital asset twice
- Consensus mechanisms — How blockchain networks agree on state
- Block propagation — How new blocks spread through the network

### Wider context

- [Blockchain fundamentals](/blockchain-fundamentals/) — Distributed ledgers and their security model
- [Cryptocurrency exchange](/cryptocurrency-exchange/) — Where coins trade and funds are at risk
- [Smart contract](/smart-contract/) — Code running on-chain that can be affected by network attacks
- [Proof-of-work](/proof-of-work/) — Consensus via computational puzzle-solving

</div>
