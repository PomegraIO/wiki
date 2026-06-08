---
title: "Trusted Setup Ceremony in ZK Proofs"
description: "A trusted setup ceremony generates cryptographic parameters for zero-knowledge proofs. Learn why a compromised setup would break privacy, and how multi-party ceremonies reduce that risk."
keywords:
  - trusted setup ceremony zero knowledge proof
  - zk proof setup ceremony
  - powers of tau ceremony
  - circuit-specific trusted setup
  - zk proof security assumption
  - multi-party computation ceremony
---

*A **trusted setup ceremony in zero-knowledge proofs** is a one-time initialization ritual in which cryptographic parameters are generated and then permanently destroyed. These parameters enable the prover to create proofs that reveal nothing about a secret, but if the parameters were compromised during generation, an attacker could forge fake proofs. Most ceremonies use multi-party computation (MPC) so that no single entity ever holds the full key to the kingdom—the secret is split among dozens of participants, and only if all of them conspire can the scheme be broken.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Trusted Setup Ceremony — key facts</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">A ceremony turns toxic waste into usable proof parameters—but only if nobody cheats.</div>

|   |   |
|---|---|
| **Purpose** | Generate public parameters needed for zero-knowledge proof systems |
| **Output** | Proving key and verification key (published); secret "toxic waste" destroyed |
| **Risk if compromised** | An attacker holding the secret could forge false proofs |
| **Mitigation** | Multi-party computation distributes secret across many participants |
| **Ceremony size** | Powers-of-tau ceremonies: dozens to thousands of participants |
| **Irreversibility** | Once parameters are published, they cannot be regenerated or changed |
| **Types** | Powers-of-tau (general, one-time) or circuit-specific (protocol-dependent) |

</aside>

## Why ZK Proofs Need a Setup Phase

Most practical zero-knowledge proof systems that achieve high privacy and speed—particularly zk-SNARKs (succinct non-interactive arguments)—require a **structured reference string** (SRS), a set of public cryptographic parameters committed to before any proofs are made. These parameters create the bridge between the prover's secret and the verifier's confidence: the prover uses them to construct a proof that is consistent with the secret but leaks nothing about it.

The security of such systems rests on the assumption that these parameters were generated honestly. If an attacker obtained the randomness used to generate them—the "toxic waste"—that attacker could create false proofs that appear valid. A verifier who checks a forged proof against the public parameters would be fooled.

This is not a theoretical edge case: if the founder of a Zcash block (the first production zk-SNARK cryptocurrency) had secretly kept a copy of the setup randomness, they could have created counterfeit coins undetectably. The only reason we trust that didn't happen is the ceremony design itself.

## The Powers-of-Tau Pattern

The most common setup approach is **powers-of-tau**, a multi-party ceremony that works like this:

1. **Initialization**: One person (call them Alice) generates a random secret, say τ (tau). She computes the list: g, g^τ, g^(τ²), g^(τ³), ... , g^(τ^n) for some large n, where g is a generator of an elliptic-curve group. She publishes this list but **destroys τ**. This is the beginning of the SRS.

2. **Round 1 (new person)**: Bob receives the list. He generates his own random secret, β. He multiplies each element by some function of β, re-randomizes the whole thing, destroys β, and passes it on to Carol.

3. **Round 2 and beyond**: Carol does the same—generate a secret, apply it, destroy it, pass on. This repeats through dozens or hundreds of participants.

4. **Finality**: After the last person, the accumulated parameters are published. The published SRS is now a function of the secrets of all participants. As long as **at least one participant honestly destroyed their secret** and did not collude with all the others, the original toxic waste is gone forever.

The cryptographic property is that if you have the output list g, g^τ, g^(τ²), ... but not τ itself, you cannot efficiently compute further powers. So even if Alice, Bob, and Carol all collude, unless they can reconstruct each other's secrets from the data passed between them (computationally infeasible if the ceremony is well-designed), they cannot recreate τ.

## Circuit-Specific Setup: More Power, More Risk

Some newer proof systems (like the Plonk family) allow for **universal** setups that work across many circuits. But earlier systems, and some optimized constructions, require a setup specific to each arithmetic circuit being verified—the specific computation you want to prove.

A circuit-specific setup involves generating parameters tailored to constraints in that exact circuit. The advantage is smaller proofs or faster verification. The disadvantage is that every new application needs its own ceremony, and the ceremony must involve participants who understand the circuit structure. This increases both cost and friction, and concentrates trust more narrowly.

Zcash's original 2016 ceremony was circuit-specific to Zcash's shielded transactions. Later systems moved toward universal setups (like Plonk's) to avoid repeating the ceremony for each application.

## Multi-Party Computation: How Collusion Risk Is Managed

The security argument for a multi-party setup is probabilistic and social, not purely cryptographic. The claim is: if you gather enough independent, trustworthy people (or diverse organizations) and run the ceremony in a way that no two consecutive participants can easily compare notes, then the probability that all of them conspire to preserve a shared secret approaches zero.

**Practical safeguards include:**

- **Diverse participants**: Researchers, companies, activists, individuals from different countries and jurisdictions, reducing the likelihood of a single actor influencing everyone.
- **Open monitoring**: Participants can publish cryptographic commitments to their work, allowing observers to verify that the ceremony rules were followed.
- **Sequential anonymity**: Participants are ordered randomly, and each sees only the output of the previous round—not who contributed before or after, reducing collusion signals.
- **Transparency logs**: The entire transcript can be published for retrospective audit, though it cannot prove that a particular person did or didn't collude.

A ceremony with, say, 100 independent participants from 50 countries and 30 organizations is much harder to compromise than one with 5 participants. Zcash's original ceremony had fewer than a dozen participants; later circuits expanded to dozens.

## The Catch: You Must Still Trust the Organizers

Even with a large multi-party ceremony, security ultimately rests on the ceremony's design and execution. If the organizers secretly run the ceremony twice—once honestly (to publish) and once with collusion (to capture the secret)—the participants would have no way to know. This is why transparency, open-source ceremony code, and post-hoc audits matter.

Additionally, **the ceremony participants must trust their hardware**: if your computer is compromised by malware, you cannot reliably destroy your secret, and the attacker gains a piece of the toxic waste.

## Where Trusted Setup Is Used (and Avoided)

**zk-SNARK systems** (Zcash, some Ethereum scaling solutions) rely on trusted setup and require ceremonies.

**zk-STARK systems** (StarkWare, some newer protocols) avoid setup entirely by using different cryptographic assumptions (hash functions instead of discrete-log hardness). STARKs are "setup-free" but have larger proof sizes and slower proving times.

**Newer universal systems** (Plonk, Marlin) run the ceremony once and reuse the parameters for many circuits, amortizing trust cost.

This choice—setup-free vs. setup-based—is a major architectural decision in protocol design. It trades off proof size, proving speed, and verifier time against the need for a ceremony and ongoing setup assumption.

## The Atomic Incineration Problem

Once the ceremony completes and the proof parameters are published, there is no way to re-run it or adjust the parameters. If a new vulnerability is discovered in the proof system, the only fix is to restart the ceremony from scratch with a corrected circuit. This is expensive in social and computational terms, which is why ecosystem participants have a strong incentive to audit the circuit design before the ceremony runs.

## See also

<div class="wiki-seealso">

### Closely related

- Zero-knowledge proof — the proof system that relies on the setup
- Elliptic curve cryptography — the math foundation for most setup ceremonies
- Discrete logarithm problem — the hardness assumption that makes toxic waste destruction work
- Proof system — the broader category containing SNARKs, STARKs, and other schemes
- Multi-party computation — the technique used to distribute setup across participants
- Cryptographic commitment — used to verify ceremony steps without revealing secrets

### Wider context

- Blockchain security assumptions — the trust model for the entire protocol
- [Distributed ledger](/distributed-ledger/) — the context in which setup ceremonies are most commonly used
- Cryptocurrency privacy — the application driving much ZK proof adoption

</div>
