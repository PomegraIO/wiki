---
title: "Dilution (Cryptocurrency)"
description: "The reduction in ownership percentage and per-token value when new tokens are issued and added to total supply."
---

*Dilution in crypto occurs when new tokens are issued and added to the circulating supply, reducing the ownership percentage and potential per-token value of existing holders. If a protocol has 100 million tokens in circulation and issues 10 million new tokens, existing holders now own a smaller slice of the total supply. If the newly issued tokens are not consumed by demand that exceeds the issuance rate, the token price typically declines.*

## The dilution mechanic

Imagine you own 1% of a token (100,000 tokens out of 10 million). The protocol announces it will issue 10 million new tokens over the next year. Instantly, you own 0.5% instead of 1%, all else equal. Your ownership stake has been cut in half. If the new tokens are distributed to developers, stakeholders, or liquidity providers, your proportional voting power and profit share have also declined.

This is sometimes called "dilution" and sometimes called "inflation" (in the monetary sense). They are the same phenomenon: an increase in the money supply that makes each unit worth less in real terms. In crypto, the term dilution is preferred because inflation is already used to describe general price increases.

## Sources of dilution

**Inflationary issuance.** Protocols like Ethereum and Bitcoin issue new tokens through mining or staking rewards. Miners or validators who secure the network receive newly created tokens as compensation. This issuance is permanent (or long-term) and is announced upfront in the protocol rules. Bitcoin's inflation is well-known: 21 million Bitcoin total, but new blocks release ~6.25 BTC every 10 minutes. This issuance schedule is transparent and built into the protocol.

**Governance-approved inflation.** Some protocols allow their governance token holders to vote on issuance. They might vote to increase staking rewards, fund a treasury, or compensate early backers. Each vote to issue new tokens dilutes existing holders. This is economically similar to a shareholder vote to issue new equity in a traditional company.

**Continuous treasury issuance.** Many protocols issue tokens continuously to pay developers, researchers, and contributors. Yearn Finance, for example, has voted multiple times to issue additional YFI to compensate development teams. These issuances are often described as necessary to fund development, but from the perspective of existing token holders, they are dilutive.

## The price impact of dilution

Whether dilution actually causes the price to fall depends on demand dynamics. If newly issued tokens are immediately bought at market price by demand that exceeds the supply increase, the price can rise despite dilution. For example, if Ethereum issues 2% new tokens per year but the demand for Ethereum increases 10% per year, the token price rises even though existing holders are diluted.

However, most protocols experience the opposite: issuance exceeds demand, and price falls. Bitcoin and Ethereum are exceptions because the demand for security (proof-of-work mining) and transaction throughput has grown faster than issuance, creating a supply deficit that supports prices.

Newer protocols with speculative user bases often issue tokens faster than demand can absorb them. Yield-farming protocols, in particular, have been notorious for issuing tokens at such a high rate that the value of farming rewards declines weekly. Users are incentivized to sell tokens immediately after receiving them, creating a negative feedback loop: faster selling depresses prices, reducing the appeal of farming, which reduces demand for the token, which causes further issuance-driven dilution.

## Strategies to mitigate dilution

**Sustainable issuance.** Protocols can cap issuance at levels that roughly match organic demand growth. Bitcoin and Ethereum both have explicitly bounded issuance schedules. Bitcoin's inflation halves every four years and will reach zero around 2140. This commitment to bounded supply is a core feature and was designed to make the token predictable and resistant to monetary debasement.

**Token burning.** To counteract dilution, protocols can implement [token-burn](/wiki/token-burn/) mechanisms that remove tokens from circulation. If a protocol issues 1 million tokens per year but burns 500,000, the net supply grows at half the rate. Burning transaction fees (as Ethereum does) is a natural source of buyback-and-burn because it is funded by economic activity.

**Governance constraints.** Some protocols hard-cap the proportion of tokens that can be issued per year or require super-majority governance votes to increase issuance. This adds friction to dilution and forces proponents of new issuance to make public cases for why existing holders should accept dilution.

**Value creation.** The most important defense against dilution is not a mechanism but business fundamentals. If the protocol creates genuine value—transaction throughput, financial services, or network effects—demand can outpace supply growth, making dilution economically irrelevant to price. The Uniswap token (UNI) has not been heavily diluted because the governance token represents a claim on a valuable decentralized exchange that generates substantial fees.

## Long-term implications

Excessive dilution is ultimately unsustainable. If a protocol issues tokens faster than demand can consume them, the token price approaches zero, making future issuance meaningless as compensation. Most protocols that have survived multiple market cycles have either capped issuance (like Bitcoin) or shifted to sustainable models where issuance is funded by real economic activity (fees and transaction volume).

The risk of dilution is often invisible to casual observers. A protocol might market itself as "decentralized" and "governed by the community" while hiding the fact that governance votes have repeatedly increased token issuance in ways that disproportionately benefit a small group of insiders. Analyzing dilution requires reading governance proposals and tracking the issuance rate over time.

<div class="wiki-seealso">
<h2>See also</h2>
<h3>Closely related</h3>
<ul>
<li><a href="/wiki/token-burn/">Token Burn</a> — mechanism to offset dilution by removing tokens from supply.</li>
<li><a href="/wiki/tokenomics/">Tokenomics</a> — the overall design of token issuance and supply.</li>
<li><a href="/wiki/token-vesting/">Token Vesting</a> — determines the rate at which founder and team tokens enter supply.</li>
</ul>
<h3>Wider context</h3>
<ul>
<li><a href="/wiki/bitcoin/">Bitcoin</a> — designed with bounded issuance to avoid dilution.</li>
<li><a href="/wiki/ethereum/">Ethereum</a> — has explicit inflation rates and burning mechanisms.</li>
<li><a href="/wiki/yield-farming/">Yield Farming</a> — a major source of dilution through token-incentive programs.</li>
</ul>
</div>
