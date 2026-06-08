---
title: "Seed Phrase: What It Is and How It Works"
description: "A seed phrase is a string of 12–24 words that derives private keys for a crypto wallet. Learn how BIP-39 mnemonics work and how to secure them offline."
keywords:
  - what is a seed phrase
  - seed phrase crypto
  - bip-39 mnemonic
  - private key derivation
  - hardware wallet backup
image: /svg/crypto.svg
---

*A **seed phrase** (also called a mnemonic or recovery phrase) is a sequence of 12, 18, or 24 common English words that encodes the master secret needed to generate all the private keys in a cryptocurrency wallet. The phrase itself is not the private key; instead, it is run through a cryptographic derivation function (BIP-39) to produce a master key, from which all individual keys are derived. Anyone who possesses the seed phrase can recover the entire wallet, so securing it offline is the highest priority.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Seed Phrase — key facts</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for cryptocurrency." />

<div class="wiki-infobox-caption">12–24 words unlock an entire wallet; loss or theft means loss of all funds.</div>

|   |   |
|---|---|
| **Length** | 12, 18, or 24 words; 24-word phrases are considered most secure. |
| **Standard** | BIP-39 (Bitcoin Improvement Proposal 39) defines the word list and derivation. |
| **Derivation** | Words → entropy → PBKDF2 function → master key → individual private keys. |
| **Who generates it** | The wallet software (e.g., MetaMask, Ledger, Trezor) creates it at setup. |
| **Storage** | Write it down on paper or metal, stored in a secure location (safe, vault). |
| **Recovery** | If the device is lost, enter the seed phrase into any compatible wallet to restore all keys. |
| **Never** | Share, photograph, email, or store online. One copy in one secure place is ideal. |

</aside>

## Why Seed Phrases Exist

Traditional banking uses a single password or PIN to protect your account. But cryptocurrency is different. There is no bank; you are your own bank. Your private keys are the only proof of ownership, and there is no password reset, no customer service, no "forgot password" link. If you lose your private key, your funds are gone forever.

Early wallet software (like Bitcoin Core) stored private keys in a random format that was hard to remember and harder to back up. If your computer crashed, you had to restore from a backup file, which was fragile and risky.

In 2013, the Bitcoin Improvement Proposal 39 (BIP-39) introduced a better way: a **seed phrase**, a short sequence of memorable words that encodes all the entropy (randomness) needed to recreate your keys. This made it far easier to write down, memorize (with care), and store in a safe. It also meant that any wallet software that followed the same standard could import your seed phrase and recover your funds.

## How a Seed Phrase Is Generated

When you create a new wallet (in MetaMask, Ledger, Trezor, or other software), the wallet generates a long string of random bytes—typically 128, 160, or 256 bits of entropy. That entropy is then passed through a hash function and converted to a checksum.

The entropy plus checksum is broken into 11-bit chunks, each of which maps to a number between 0 and 2047. That number selects a word from the official BIP-39 word list (a standardized list of 2048 common, unambiguous English words).

- 128 bits of entropy → 12-word phrase
- 160 bits of entropy → 15-word phrase
- 192 bits of entropy → 18-word phrase
- 256 bits of entropy → 24-word phrase

The more bits of entropy, the harder the phrase is to brute-force (guess). A 12-word phrase has roughly 128 bits of security; a 24-word phrase has 256 bits. In practice, 12-word phrases are considered adequately secure for most users, though 24-word phrases are preferred for large holdings or institutional use.

## From Phrase to Private Keys

Once you have the seed phrase, it is not directly usable as a private key. Instead, it is converted into a master private key using a function called PBKDF2, combined with a salt (typically the word "mnemonic" plus an optional passphrase chosen by the user).

From the master key, an infinite number of child keys are derived using the [BIP-32](https://github.com/bitcoin/bips/blob/master/bip-0032.mediawiki) hierarchical deterministic (HD) derivation standard. Each key has a unique path—for example, "m/44'/0'/0'/0/0" refers to the first Bitcoin address in the first account in the first wallet—allowing a single seed phrase to generate keys for multiple blockchains and multiple addresses within each blockchain.

This design means:

- One seed phrase can back up all your wallets and all your addresses.
- You can restore the entire structure from just the seed phrase.
- The derivation is deterministic: the same seed always produces the same keys, so if you lose your device and import the seed into a new wallet, you recover the exact same addresses and funds.

## What the Seed Phrase Is Not

**It is not the private key itself.** The seed phrase is an intermediate, human-readable encoding that is run through a cryptographic function to produce the private key. It is more like a password to a password.

**It is not your password to the wallet.** Many modern wallets ask for a PIN or password when you open them, and a separate seed phrase for backup. The PIN protects the device; the seed phrase recovers everything if the device is lost.

**It is not the blockchain.** The seed phrase only exists on devices you control. The blockchain has no record of it. If you lose the seed phrase and the device storing it, there is no recovery, even from the blockchain itself.

## Storage and Security Best Practices

The seed phrase is as valuable as the funds it secures. Industry best practices include:

**Write it down.** Paper is actually a better backup medium than digital storage for a seed phrase. Digital files can be hacked, encrypted with ransomware, or lost to hard-drive failure. A handwritten note in a safe cannot be hacked remotely.

**Store offline.** Never type the seed phrase into an online device (computer, phone connected to the internet) unless you are actively importing it into a wallet in a controlled environment. Never email it, photograph it, or upload it to cloud storage.

**Use one primary copy.** Many security experts recommend a single, physically secure location (a safe-deposit box, a home safe) rather than multiple copies, which multiplies the risk of loss or theft.

**Optional: use a passphrase.** Some wallets (including many hardware wallets) allow you to add a 25th word (a passphrase) to your seed phrase, further protecting it. If an attacker steals your 24-word phrase but does not know the passphrase, they cannot access the funds. The trade-off is that if you forget the passphrase, you cannot recover the wallet.

**Never share.** Not with family, not with a trusted friend, not written in a will in plain language. If inheritance is a concern, consider a separate hardware wallet with clear instructions to heirs on how to access the seed in a secure location.

**Verify during import.** When importing a seed phrase into a new wallet, most reputable software will ask you to confirm it word-by-word. Do not skip this; typos or mistakes during import can result in a valid seed phrase that generates different keys than the original.

## Seed Phrases Across Blockchains

Because BIP-39 and BIP-32 are open standards, a seed phrase generated on one blockchain (e.g., Bitcoin) can often be imported into a wallet for another blockchain (e.g., Ethereum). However, the private key derived for Bitcoin differs from the Ethereum key, because they use different derivation paths. So the same seed phrase will produce different addresses on different blockchains—all controlled by the same seed.

This is both powerful (one phrase backs up everything) and dangerous (if a single phrase is compromised, all your addresses across all blockchains are at risk).

## Loss and Recovery Scenarios

**Scenario 1: Device lost, seed backed up.**
You lose your phone but have the seed phrase written in your safe. You buy a new phone, download the wallet app, and import the seed phrase. All your addresses and funds are restored instantly.

**Scenario 2: Device lost, seed not backed up.**
You lose your phone and never backed up the seed phrase. The funds are gone. There is no recovery, no customer service, no second chance.

**Scenario 3: Seed stolen.**
An attacker steals your written seed phrase from your safe (or finds a digital copy). They import it into their own wallet and drain all funds. There is no way to reverse this or prevent it.

**Scenario 4: Seed phrase typo during import.**
You mistype one word during import. The wallet is created successfully (BIP-39 checksum validation passes for the typo'd phrase), but it generates a different set of addresses than your original. Your funds remain in the original addresses, unreachable from the typo'd seed.

## Modern Alternatives and Enhancements

Some newer wallets and blockchain projects offer alternatives to seed phrases:

- **Social recovery wallets:** Multiple trusted contacts each hold a "share" of the recovery key. You need a majority of them to restore the wallet. This reduces single-point-of-failure risk but requires coordination.
- **Ledger Recover:** Some hardware wallet providers now offer optional cloud backup of encrypted seed phrases, with decryption controlled by the user. This adds convenience but shifts trust to a third party.
- **Account abstraction:** Emerging blockchain standards may allow wallets to recover from compromised keys via on-chain social recovery or other mechanisms, reducing reliance on a single seed phrase.

For now, the BIP-39 seed phrase remains the gold standard for self-custodial crypto wallets, and understanding its security implications is essential for anyone holding digital assets.

## See also

<div class="wiki-seealso">

### Closely related

- Private Key — The cryptographic secret that controls funds; derived from the seed phrase.
- Hardware Wallet — Physical devices that generate and store seed phrases securely.
- Wallet — The broader ecosystem of managing cryptocurrency addresses and keys.
- BIP-32 — The hierarchical deterministic standard for deriving keys from a seed.
- BIP-39 — The standard defining seed phrase word lists and derivation.

### Wider context

- Cryptocurrency Security — Best practices for protecting digital assets.
- Key Management — Enterprise and personal approaches to cryptographic key storage.
- Custody — Self-custody vs. third-party custody models and their trade-offs.
- [Blockchain Fundamentals](/blockchain-fundamentals/) — How cryptographic keys underpin blockchain ownership.

</div>
