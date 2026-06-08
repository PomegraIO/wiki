---
title: "Hardware Wallet Passphrase (25th Word) Explained"
description: "The BIP-39 passphrase creates a hidden wallet from your seed phrase—adding a 25th word for extra security, but with irreversible loss risk if forgotten."
keywords:
  - hardware wallet passphrase
  - 25th word bip-39
  - seed phrase extension
  - cryptocurrency custody security
image: /svg/crypto.svg
---

*A **hardware wallet passphrase**, known as the 25th word or BIP-39 passphrase, is an optional encryption layer that transforms your standard seed phrase into a hidden wallet. Unlike your regular 12 or 24-word seed, this passphrase is not stored anywhere—only you know it—and forgetting it means permanent loss of access to that hidden wallet's funds.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Hardware Wallet Passphrase — Key Facts</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for cryptocurrency custody." />

<div class="wiki-infobox-caption">A 25th word transforms your seed into a completely separate wallet with no recovery path if lost.</div>

|   |   |
|---|---|
| **Also called** | BIP-39 passphrase, 25th word, plausible deniability extension |
| **Length** | 0–100+ characters, not limited to 11 words |
| **Storage** | Your memory only—never written down with your seed |
| **Recovery** | None—if forgotten, that wallet is inaccessible forever |
| **Security gain** | Creates mathematically independent wallet from seed alone |
| **Main risk** | Death, illness, or memory loss locks out funds permanently |

</aside>

## What the 25th Word Actually Does

The 12 or 24-word seed phrase your hardware wallet generates is not secret by itself—it derives your private keys using a deterministic function. A **passphrase** is an additional input to that function. Even identical seed phrases produce entirely different wallets if different passphrases are used.

Think of it this way: your seed phrase + an empty passphrase creates Wallet A. The same seed phrase + "MySecretWord" creates Wallet B. These wallets are completely independent. No one can derive Wallet B from Wallet A or the seed alone; they would need both the seed and the exact passphrase.

Because the passphrase is not part of the seed backup, it exists only in your knowledge. This is by design—the idea is to separate the backup (which might be stolen or compromised) from the master key that unlocks a separate, hidden wallet.

## The Trade-Off: Security vs. Irretrievable Loss

Adding a passphrase genuinely improves security if someone physically steals your written seed phrase. They can access your standard wallet (derived from the seed + empty passphrase), but not your hidden wallet behind the 25th word.

This is sometimes called a "duress wallet" pattern: you keep modest funds in the standard wallet and store the bulk of your holdings behind a passphrase that you never write down.

But this security comes with a stark downside: **if you forget the passphrase, there is no recovery mechanism**. Your hardware wallet cannot retrieve it, the manufacturer cannot override it, and no backup exists. The only way in is with the correct passphrase—byte-perfect—every single time. A typo, a misremembered phrase, or a password manager entry that was corrupted all mean permanent loss.

Historical precedent matters here. Thousands of [cryptocurrency](/cryptocurrency-exchange/) holders have lost access to passphrases through death, illness, or simple human memory failure. Unlike a forgotten PIN on a hardware wallet (which often has a limited retry count before a reset), there is no fallback.

## How to Use It Safely

If you decide a passphrase is worth the risk, a few practices reduce the stakes:

**Test it immediately.** After setting the passphrase on your hardware wallet, verify you can derive and access the wallet with it. Do this while you still remember what you typed.

**Document it securely, but not next to the seed.** The passphrase must be stored separately from your seed phrase. A password manager (offline or encrypted cloud), a separate safe deposit box, or a trusted family member's hands are common choices. The location must be something you trust will survive you, since recovery is genuinely irreversible.

**Use a memorable passphrase.** Avoid random character strings unless you have a reliable system to store them. The whole point is a phrase you can remember under pressure.

**Inform your heirs.** If you die, whoever inherits your hardware wallet needs access to the passphrase or they own an inaccessible brick. Estate planning around passphrases is uncommon but necessary if significant funds are involved.

**Start small.** Some users keep a tiny amount in the passphrase wallet as a proof-of-concept before moving larger sums.

## Passphrase vs. PIN: The Difference

A hardware wallet's PIN code is a 4–8 digit code you set locally on the device. Enter it wrong a few times and the device wipes. A **passphrase** is different: it's text you supply during key derivation, and there is no wrong-guess limit—you simply generate the wrong wallet if you get it wrong.

The passphrase is typically entered once when you set up the wallet, then remembered or retrieved from secure storage every time you want to access that wallet on the device. A PIN is a security gate on the hardware itself.

## Why This Exists: Plausible Deniability

The BIP-39 standard (the industry standard for seed phrases) includes the passphrase mechanism specifically to support deniability. In a scenario where someone coerces you to reveal your seed phrase, you can hand it over and truthfully claim that's your entire wallet—while your real holdings sit behind a passphrase you refuse to disclose. This is why it is sometimes called a "25th word" even though it need not be a single word.

For most users in low-threat environments, this is theoretical. But for politically active individuals, journalists, or people in high-surveillance jurisdictions, the feature is meaningful.

## Common Mistakes

**Writing the passphrase next to the seed.** This defeats the entire purpose; treat them as separate secrets.

**Using the same passphrase across multiple devices or wallets.** This can compromise the isolation you're trying to create.

**Assuming a passphrase protects against a compromised hardware wallet.** It does not—if the device is infected with malware, that malware can observe what you type or transmit your private keys when derived. The passphrase only protects against someone with the seed phrase alone.

**Forgetting to test it.** Discovering after a year that you misremembered one character is a tragedy that could be prevented with a single test.

## See also

<div class="wiki-seealso">

### Closely related

- Seed Phrase — the 12 or 24-word recovery code for your wallet
- Hardware Wallet — the physical device that stores your private keys
- Cryptocurrency Custody — how to safely store digital assets
- Private Key — the cryptographic secret that signs transactions

### Wider context

- Key Derivation — how seed phrases mathematically generate wallets
- [Bitcoin](/bitcoin/) — the most common asset secured by hardware wallets
- [Proof of Work](/proof-of-work/) — the security model behind blockchain
- [Distributed Ledger](/distributed-ledger/) — how cryptocurrency transactions are recorded

</div>
