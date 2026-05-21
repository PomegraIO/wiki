---
title: "Yield Farming"
description: "Earning rewards by providing liquidity, staking tokens, or supplying assets to decentralized-finance protocols."
---

*Yield farming is the practice of earning cryptocurrency rewards by locking assets into decentralized-finance (DeFi) protocols. A user might provide Bitcoin and Ethereum to a [liquidity-pool](/wiki/liquidity-pool/) and earn a percentage of trading fees. Or they might stake tokens in a lending protocol and earn interest. Or they might provide collateral to a borrowing protocol and earn governance tokens as incentive rewards. The goal is to earn a higher yield than traditional finance while exposing yourself to smart-contract risk.*

## The basic mechanism

Most DeFi protocols need liquidity to function. An automated market maker (AMM) like Uniswap needs millions in locked tokens to minimize [slippage](/wiki/impermanent-loss/) on swaps. A lending protocol like Aave needs lenders to deposit assets before borrowers can borrow. Yield farming solves the bootstrap problem: the protocol offers rewards to liquidity providers or lenders, creating an incentive to supply capital.

These rewards often come in the form of the protocol's native governance token. Uniswap may offer 100 UNI per day to liquidity providers in the Ethereum-USDC pool. Lenders on Aave earn a percentage of interest paid by borrowers plus supplementary AAVE token rewards. The protocol thereby transfers newly minted tokens to capital suppliers in exchange for liquidity.

## Liquidity mining vs. staking

Liquidity mining typically refers to providing two tokens to an AMM in a 1:1 value ratio. Uniswap liquidity providers deposit, say, $5,000 in Ethereum and $5,000 in USDC, receiving liquidity tokens that represent their share of the pool. They earn a percentage of trading fees (0.3% on Uniswap v3, split among liquidity providers) plus any supplementary token rewards the protocol offers.

Staking typically means locking a single token in a protocol and earning yields without providing liquidity. A proof-of-stake validator stakes Ethereum, earns staking rewards from the protocol (currently ~3–4% annually), and participates in consensus. A [proof-of-stake](/wiki/proof-of-stake/) system like Cardano works similarly. Staking is simpler than liquidity mining because you do not have to manage two tokens, but it typically offers lower yields.

## The yield-farming boom and aftermath

In 2020–2021, DeFi yield farming became a mania. Protocols offered absurdly high yields—50%, 100%, or even 1,000% annualized—to attract capital. Yield farmers would chase these rewards, locking huge sums into risky protocols. When the yields were unsustainable, the protocols collapsed (Luna, Celsius) and farmers lost their capital.

The yields were unsustainable because they were funded by token inflation, not by economic activity. A protocol might offer 1,000% yields by issuing new tokens at a rate that grows the supply by 1,000% per year. Farmers would earn huge token rewards, immediately sell them (because they were worthless), and crash the token price. The protocol would run out of resources to pay new farmers, causing a collapse.

Modern yield farming has moderated. Sustainable yields are typically in the 5–20% range and are funded by real economic activity (trading fees or borrow interest) rather than unsustainable token inflation. Farmers who seek higher yields are essentially betting on the protocol's token appreciating.

## Impermanent loss

The major risk of liquidity mining is [impermanent-loss](/wiki/impermanent-loss/). When you provide liquidity to an AMM, the protocol uses your tokens to satisfy swaps. If one token's price rises relative to the other, you end up with more of the asset that has fallen and less of the asset that has risen. This is a cost of providing liquidity—you missed out on the upside by holding the token that appreciated.

This loss is "impermanent" because if the price reverts, the loss recovers. But if the price divergence persists, the loss is realized. Many liquidity providers underestimate this risk. They see that they earn trading fees (say 5% annually) and do not realize that impermanent loss is costing them 20% of their capital due to price divergence. Net yield is negative.

## Smart-contract risk

Yield farming exposes you to smart-contract risk. If a protocol has a bug or is exploited, your capital can be lost instantly. Several major DeFi hacks have resulted in farmers losing tens or hundreds of millions of dollars. Even audited protocols can fail. The more novel and less-tested the protocol, the higher the smart-contract risk.

Some farmers mitigate this by using only well-tested protocols (Uniswap, Aave, Curve) with long track records and multiple audits. Others diversify across many protocols and accept the possibility of occasional losses as the cost of chasing higher yields.

## Incentivized farming and protocol governance

Many protocols offer supplementary token rewards to farmers specifically to bootstrap adoption. Uniswap distributes UNI to liquidity providers; Aave distributes AAVE to lenders and borrowers. These incentives are temporary—the protocol gradually reduces them over time as the protocol becomes self-sustaining.

This creates a perverse incentive: farmers are incentivized to lock capital into whatever protocol is offering the highest rewards, not necessarily the most useful protocol. Sophisticated farmers track dozens of protocols, monitor reward rates, and quickly move capital to wherever yields are highest. This leads to capital flowing to shiny new protocols with unsustainable reward rates, leaving more mature protocols starved of liquidity.

## The taxonomy of yield sources

The most sustainable yields come from:

1. **Borrow interest.** If you lend money, borrowers pay interest. Aave lenders earn a percentage of the interest paid by borrowers—typically 3–8% depending on the asset. This is backed by real economic demand for borrowing.

2. **Trading fees.** Decentralized exchange liquidity providers earn a percentage of trading fees (typically 0.01–0.3%). This is backed by actual trading volume.

3. **Validator rewards.** Proof-of-stake networks reward validators who secure the network. Ethereum validators earn ~3% annualized. This is economically sustainable because it is a cost of securing the network, similar to mining costs in proof-of-work systems.

4. **Governance token appreciation.** When a protocol distributes governance tokens as rewards, farmers are banking on the token appreciating. This is speculative and not backed by economic activity—it depends on future demand for the token.

The highest-yielding opportunities are often a mix, where governance tokens provide additional yield on top of economic yields. But if the governance token appreciates only because of yield-farming hype and then collapses, farmers suffer catastrophic losses.

<div class="wiki-seealso">
<h2>See also</h2>
<h3>Closely related</h3>
<ul>
<li><a href="/wiki/impermanent-loss/">Impermanent Loss</a> — the cost of providing liquidity when prices diverge.</li>
<li><a href="/wiki/liquidity-pool/">Liquidity Pool</a> — the mechanism enabling yield farming.</li>
<li><a href="/wiki/staking/">Staking</a> — earning rewards by securing the network.</li>
</ul>
<h3>Wider context</h3>
<ul>
<li><a href="/wiki/decentralized-exchange/">Decentralized Exchange</a> — the primary platform for liquidity farming.</li>
<li><a href="/wiki/governance-token/">Governance Token</a> — often distributed as farming rewards.</li>
<li><a href="/wiki/automated-market-maker/">Automated Market Maker</a> — the mechanism underlying liquidity mining.</li>
</ul>
</div>
