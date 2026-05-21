---
title: "Token Burn"
description: "The permanent destruction of tokens by sending them to an inaccessible address, reducing total supply."
---

*Token burn is the practice of permanently removing tokens from circulation by sending them to an address whose private key is publicly provable to not exist. Tokens sent to a burn address can never be recovered or spent. A protocol might burn tokens to reduce inflation, reward holders through deflationary value creation, or destroy tokens that violate rules. It is a one-way destruction, the digital equivalent of a company buying back and shredding its own stock.*

<aside class="wiki-infobox">
<div class="wiki-infobox-title">Token Burn — key facts</div>
<table>
<tr><th>Purpose</th><td>Reduce supply, increase scarcity, reward holders</td></tr>
<tr><th>Mechanism</th><td>Sending tokens to an inaccessible address</td></tr>
<tr><th>Irreversible</th><td>Yes — burned tokens are permanently gone</td></tr>
<tr><th>Effect on price</th><td>Uncertain — depends on demand expectations</td></tr>
</table>
</aside>

## How token burn works

A burn address is a public-key address whose private key has never been generated or has been verifiably destroyed. The most famous burn address on Ethereum is `0x0000000000000000000000000000000000000000`, an address that was never issued a private key during the protocol's setup. Tokens sent to this address are stranded—no one can withdraw them.

Any smart contract or individual can initiate a burn by transferring tokens to the burn address. The transaction is recorded on the blockchain, providing transparent proof of destruction. Protocols often write burn events into their code: Ethereum burns a portion of transaction fees; some [decentralized-exchange](/wiki/decentralized-exchange/) protocols burn a percentage of trading volume; [proof-of-stake](/wiki/proof-of-stake/) systems sometimes burn staked tokens from validators who misbehave.

## Why protocols burn tokens

**Deflationary incentive.** If a protocol's token supply is fixed and transaction volume grows, each token becomes more scarce and potentially more valuable. Alternatively, if a protocol has steady inflation but also steady burns, the net supply can stabilize or decline. This deflation is attractive to token holders because it implies that their ownership percentage increases over time as the total supply shrinks.

**Reward mechanism.** Some protocols use burning as a way to benefit existing holders without distributing new tokens. Uniswap v3 protocols sometimes burn transaction fees rather than sending them to a treasury or liquidity providers. This rewards holders pro-rata because the reduction in supply increases the value per share, even if no new tokens are issued.

**Risk punishment.** In [delegated-proof-of-stake](/wiki/delegated-proof-of-stake/) systems, validators who act maliciously—double-sign blocks or propose conflicting transactions—have their staked tokens slashed (burned). This punishes bad behavior directly and deters it because the economic loss is large.

## Burn vs. buyback

In traditional finance, a company can repurchase its own stock and burn it (technically called "retiring" the stock). This increases earnings per share if the company buys back below intrinsic value, but it is not value-creating in isolation—it is merely reshuffling ownership among remaining shareholders.

Similarly, a crypto protocol burning its own tokens does not create value by itself. The burn only increases the value per remaining token if the underlying demand for the token is growing faster than the burn rate or if the burn is so large and public that it changes investor perception of the protocol's commitment to deflation.

## The psychology vs. the economics

Token burns are popular with retail investors because they feel like scarcity creation. A smaller total supply intuitively suggests a higher price—all else equal, owning a 1% stake in a 100-unit supply seems better than owning 1% of a 1,000-unit supply. But all else is rarely equal. If the protocol has declining transaction volume or declining user adoption, a burn does not address the fundamental problem. The token can decline in value even if the total supply shrinks.

Some critics argue that burns are pure psychology: a protocol claiming to be "deflationary" signals confidence to investors, which can temporarily boost price. But the boost is not fundamental value creation; it is sentiment-driven. Sophisticated investors look through the psychology to the underlying economics: What is the protocol's actual utility? Are fees sustainable? Is user adoption growing? A burn does not answer these questions.

## Burn rate and sustainability

The sustainability of a burn depends on whether it is funded by a meaningful economic activity. If Ethereum burns transaction fees, that burn is sustainable only if the protocol continues to have transaction volume. If a protocol dedicates a percentage of inflation to buying and burning its own token, it is essentially paying to reduce supply—a subsidy with a cost. That subsidy must be funded by inflation, which eventually stops or becomes infeasible.

Some protocols have committed to perpetual burns that exceed inflation, creating a deflationary spiral. These commitments are often unsustainable if the underlying economic activity (fees, transactions, revenue) declines. A protocol might burn for years in a bull market and then reverse the burn rate or cease burning entirely when market conditions deteriorate.

## Tokenomics design implications

Burning is one tool in the broader [tokenomics](/wiki/tokenomics/) toolkit. It can reduce dilution, incentivize long-term holding, and signal confidence in the protocol. However, it is not a substitute for building utility and adoption. A protocol with declining usage but massive token burns will eventually fail because the burns will be unsustainable. The most successful token burns are byproducts of genuine economic success: a protocol that is profitable enough to use cash flows for buyback-and-burn strategies.

<div class="wiki-seealso">
<h2>See also</h2>
<h3>Closely related</h3>
<ul>
<li><a href="/wiki/token-vesting/">Token Vesting</a> — mechanism releasing tokens over time.</li>
<li><a href="/wiki/dilution-cryptocurrency/">Dilution (Cryptocurrency)</a> — the effect of new token issuance on existing holders.</li>
<li><a href="/wiki/tokenomics/">Tokenomics</a> — overall design of a token's economic system.</li>
</ul>
<h3>Wider context</h3>
<ul>
<li><a href="/wiki/ethereum/">Ethereum</a> — a major protocol that burns transaction fees.</li>
<li><a href="/wiki/share-buyback/">Share Buyback</a> — the traditional-finance analog of token burns.</li>
<li><a href="/wiki/decentralized-exchange/">Decentralized Exchange</a> — often implements token burns as a fee-distribution mechanism.</li>
</ul>
</div>
