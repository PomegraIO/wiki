---
title: "DeFi Yield Harvesting as a Tax Event"
description: "When claiming or auto-compounding DeFi yield triggers taxable income, how the reward is classified, and how to establish cost basis on harvested tokens."
keywords:
  - is defi yield harvesting a taxable event
  - defi yield tax event
  - defi yield harvesting income
  - cryptocurrency yield tax
image: /svg/crypto.svg
---

*Claiming **DeFi yield** is a taxable event in most jurisdictions. The moment you harvest rewards—whether you manually claim them or they auto-compound—you recognize income equal to the fair-market value of the tokens received. That income is ordinary income (not [capital gains](/long-term-capital-gain-tax/)), and it triggers cost basis for future sales.*

## When Harvesting Is Taxable

Harvesting occurs when you claim earned rewards from a lending protocol, liquidity pool, or staking contract. Examples:

- Staking Ethereum and claiming ETH rewards
- Providing liquidity to a decentralized exchange and collecting protocol tokens (e.g., UNI, AAVE)
- Depositing stablecoins in a lending protocol (e.g., Aave, Compound) and claiming accrued interest plus governance tokens
- Yield farming on a protocol that distributes new tokens to liquidity providers

The moment the token enters your wallet—even if you immediately re-stake or re-deposit it—a taxable event occurs. The IRS (and tax authorities in most countries) treat this as income receipt, not a return of your principal.

## How Income Is Classified

DeFi yield is ordinary income, taxed at your marginal tax rate (same as salary or business income), not as long-term capital gains. If you're in the 37% federal bracket, every dollar of harvested yield is taxed at 37% plus state and FICA taxes if self-employed.

This is crucial: a $10,000 harvest when Ethereum is at $3,000 per ETH means you have $10,000 in taxable ordinary income, regardless of whether ETH rallies to $4,000 later. You've locked in an ordinary-income tax bill right away, and you haven't yet made any capital gain or loss on the tokens themselves.

Different yield types:

| Yield type | Tax classification | Timing of recognition |
|---|---|---|
| Staking rewards (PoS consensus) | Ordinary income | When received/claimed |
| Liquidity mining (governance tokens) | Ordinary income | When claimed/auto-compounded |
| Interest from lending (stablecoins) | Ordinary income | When accrued or paid (per IRS Notice 2018-86) |
| LP fee distributions (native token) | Ordinary income | When claimed |

## Accrual vs. Cash Basis Timing

The IRS has indicated (in Notice 2018-86, addressing cryptocurrency in general) that most taxpayers must use cash-basis accounting. Under cash basis, you recognize income when you actually receive or claim it, not when it accrues in the smart contract. This is favorable: if you claim a harvest on December 31, you have income in that year; if you wait until January 2, income recognition pushes to the next year.

However, some tax professionals argue that certain lending-platform interest (especially on stablecoins) could be treated as accrued income even before claiming, especially if you're required to report on accrual basis. This is unsettled law, and the safer approach is to claim harvests deliberately and recognize income upon claim.

## Establishing Cost Basis on Harvested Tokens

Once you claim yield, the received tokens have a cost basis: the fair-market value in USD (or your local currency) at the moment of receipt. This is your "purchase price" for future [capital gains tax](/long-term-capital-gain-tax/) purposes.

Example:
- You harvest 1 ETH in staking rewards when ETH is $3,500.
- Your cost basis on that 1 ETH: $3,500.
- You pay ordinary income tax on $3,500 in that year.
- If you later sell that 1 ETH at $4,200, your capital gain is $700 (short-term if held < 1 year, long-term if > 1 year).

This is where meticulous record-keeping becomes essential. You must document the date and USD value of every harvest. Most protocols show your harvest history on-chain, but you need to record the USD price at harvest time (use a price API, exchange data, or a crypto-tax service).

## Auto-Compounding and Nested Taxable Events

Many DeFi protocols auto-compound rewards: they harvest and re-stake without your manual action. This does not exempt the harvest from tax. Each auto-compound is a separate taxable event.

Example:
- Day 1: You deposit 10 ETH. Cost basis: $35,000 (at $3,500/ETH).
- Day 30: Protocol auto-compounds 0.1 ETH earned. At that moment, ETH is $3,600.
  - Taxable event: Ordinary income of $360 (0.1 × $3,600).
  - Your cost basis on the 0.1 ETH: $360.
  - Your total ETH holding: 10.1, with mixed cost basis.
- Day 60: Protocol auto-compounds another 0.1 ETH. ETH is now $3,700.
  - Taxable event: Ordinary income of $370.
  - Cost basis on new 0.1 ETH: $370.

If you sell all 10.1 ETH at $4,000 per ETH, you have:
- Proceeds: 10.1 × $4,000 = $40,400
- Cost basis: $35,000 + $360 + $370 = $35,730
- Capital gain: $4,670 (likely long-term if you held > 1 year)

But you also recognized $730 in ordinary income during the holding period from the harvest events.

## Impermanent Loss and Tax

If you provide liquidity and suffer impermanent loss, that loss is not directly deductible as a capital loss. Here's why: your initial deposit created a cost basis for the LP tokens you received. When you withdraw fewer tokens than you should have (due to impermanent loss), you have a capital loss only to the extent your final proceeds fall below your original cost basis—and only if you actually sell or exit the position.

Until you withdraw and realize the loss, it remains "unrealized." The IRS allows [capital loss deductions](/long-term-capital-gain-tax/) only on realized losses (actual sales or taxable dispositions). Some protocols let you exit a position at any time, which triggers a realized loss immediately. Others lock liquidity, delaying realization.

## Wash-Sale Rules

The IRS [wash-sale rule](/wash-sale/) prohibits claiming a loss and repurchasing the same security within 30 days. Crypto is property, not securities, so the IRS wash-sale rule does not formally apply. However, the IRS has indicated that similar "economic substance" rules could apply to crypto transactions. A conservative approach: if you sell at a loss, avoid buying back the same token within 30 days, or document a legitimate business reason for the repurchase.

## Staking and Custody

Some custodians and exchanges allow you to stake on their platform without ever taking custody of the tokens yourself. If you earn staking rewards but the exchange holds them, when are they taxable? The IRS has not issued definitive guidance, but most tax professionals advise recognizing income when the rewards are credited to your account, even if held in custody. This is the "discovery" point—you have constructive receipt and economic control.

If you stake directly from your own wallet, income is recognized when the reward hits your wallet.

## Record-Keeping Essentials

For DeFi yield harvesting, maintain:

1. **Harvest log**: Date, token claimed, quantity, USD value at harvest (screenshot the price or use a data source).
2. **Transaction hash**: Blockchain verification of the harvest on-chain.
3. **Cost basis tracking**: Link each harvested token to its cost basis and holding period.
4. **Gain/loss calculation**: When you sell or swap, compute short-term vs. long-term capital gain/loss.

Many crypto-tax services (CoinTracker, Koinly, etc.) auto-import harvest events from on-chain data and assign cost basis automatically. This is worth the fee to avoid errors and reduce audit risk.

## Jurisdiction Variations

Tax treatment of DeFi yield varies:

- **USA**: Ordinary income on harvest, capital gains on sale (as above).
- **UK**: Treated as miscellaneous income; gains/losses on sale are capital gains (subject to CGT allowance).
- **Canada**: 100% of gain/loss realized; includes harvested yield as income.
- **Germany**: Under €600 exemption if held > 1 year (much more favorable than US).

Non-US residents should consult local tax guidance; many countries have no explicit DeFi rules and default to general income-tax and capital-gains principles applied analogously.

## The Bottom Line

Harvesting DeFi yield is not optional tax reporting. It's ordinary income at the time of claim. If you earn $10,000 in yield over a year but the tokens later depreciate 50%, you still owe tax on the $10,000 in the year of harvest. This mismatch—recognizing income before realizing a gain—is why many yield farmers experience surprise tax bills. Track harvests methodically, establish cost basis immediately, and consult a tax professional if your yield is substantial.

## See also

<div class="wiki-seealso">

### Closely related

- [Long Term Capital Gain Tax](/long-term-capital-gain-tax/) — How gains on sold tokens are taxed
- [Cryptocurrency Exchange](/cryptocurrency-exchange/) — Platforms for buying, selling, and staking
- [Smart Contract](/smart-contract/) — How yield protocols automate rewards
- [Distributed Ledger](/distributed-ledger/) — The underlying blockchain technology

### Wider context

- [Proof of Stake](/proof-of-stake/) — How staking earns rewards
- [Blockchain Fundamentals](/blockchain-fundamentals/) — DeFi protocols and yield farming
- [Cost Basis](/cost-basis/) — General cost-basis rules in investing
- [Revenue Recognition](/revenue-recognition/) — When income is reported (applies to crypto analogously)

</div>
