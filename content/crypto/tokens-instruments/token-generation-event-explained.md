---
title: "Token Generation Event (TGE) Explained"
description: "What a token generation event is, how it differs from ICOs and IDOs, what happens on-chain during minting, and why vesting schedules center on the TGE date."
keywords:
  - token generation event
  - TGE cryptocurrency
  - token minting
  - vesting schedules
  - initial token distribution
  - blockchain launch
---

*A token generation event (TGE) is the moment a cryptocurrency project mints and distributes its initial supply of tokens on-chain, marking the official start of circulation and the trigger date for vesting schedules.* The TGE is often confused with an ICO (initial coin offering, a fundraising event) or an IDO (initial DEX offering), but it is a distinct technical and legal milestone. Understanding TGEs requires clarity on what happens on-chain, how allocations work, and why the TGE date matters for lock-ups and unlocks across years.

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Token Generation Event — key facts</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">The TGE is the on-chain moment when all token supply comes into existence and begins distributing to stakeholders.</div>

|   |   |
|---|---|
| **What it is** | The on-chain creation and initial distribution of a blockchain project's native token |
| **Typical timing** | Days or weeks after a fundraising round or community event |
| **Common participants** | Founders, investors, community members, early employees |
| **Role in vesting** | TGE date is the Day 1 reference point for all lock-ups and releases |
| **Token supply created** | Usually 100% of the planned maximum supply at TGE, though issuance may be gradual |
| **Governance** | Determined by smart contract or protocol rules, executed by core team |

</aside>

## The TGE is a technical event, not a fundraising one

Many people conflate TGE with fundraising, but they are separate. A project might hold an IDO or receive venture capital investment months or even years before the TGE. During that time, the blockchain network may exist but no tokens have been minted. The project is still in development. Only at the TGE does the on-chain token supply actually come into being.

Some projects run a TGE immediately after a token sale (ICO or IDO). Others launch a public network first, then mint tokens once the network is stable. The timeline varies wildly. The defining characteristic is this: before TGE, zero tokens exist on the blockchain. After TGE, the full or near-full supply exists and begins circulating to the designated recipients.

## What happens on-chain during a TGE

On a [blockchain](/blockchain-fundamentals/) like Ethereum, the TGE involves deploying a token [smart contract](/smart-contract/) (a self-executing program). That contract specifies the total supply, the initial distribution addresses, and any lock or vesting logic. Once deployed and initialized, the token supply is minted—created from nothing—and attributed to the addresses that earned it.

The mint transaction is recorded permanently on the ledger. Everyone can see it: "On block X, at time Y, tokens were created and sent to address Z." There is no ambiguity. All future transactions and transfers derive from that TGE mint.

Large projects may distribute tokens across many addresses in a single TGE transaction (batch distribution), or in waves if the infrastructure cannot handle millions of recipients at once. Smaller projects might transfer tokens to a holding contract that then releases them gradually. The method does not change the essential fact: the tokens came into existence at the TGE block.

## TGE allocation breakdown

The TGE supply is typically split among several constituencies:

**Founders and core team**: Often 15–30% of total supply, subject to multi-year [vesting](/token-generation-event-explained/) schedules (e.g., 4-year vest, 1-year cliff, meaning no tokens unlock for 12 months, then 1/48 per month thereafter).

**Early investors and venture capitalists**: Often 20–40%, also vested. Earlier investors may have better terms (faster unlock).

**Community and public sale**: Usually 10–30%, distributed to ICO/IDO participants or airdropped to wallet holders.

**Foundation or ecosystem reserve**: 10–30%, held for development, partnerships, and long-term incentives.

**Liquidity pools and market makers**: 1–10%, deposited into [decentralized exchanges](/cryptocurrency-exchange/) to enable trading.

The exact split varies by project philosophy and business needs. Decentralized projects may allocate more to community; venture-backed ones may allocate more to founders and investors.

## Vesting schedules centered on the TGE date

The TGE date is the universal Day 0 reference. Every lock, cliff, and vesting schedule is calculated from that moment. Example:

A founder receives 1 million tokens at TGE with a "4-year vest, 1-year cliff" schedule. That means:
- Days 0–365 (Year 1): tokens are locked, not transferable.
- Day 365 (Year 1 anniversary): 25% unlock (250,000 tokens).
- Months 13–48: 1/48 of the remaining 750,000 unlock each month.
- Month 48+: all remaining tokens are unlocked.

An investor who participated in a seed round might have different terms: "2-year vest, no cliff," meaning a constant monthly or daily drip from Day 0 onward.

These schedules are either written into the smart contract itself (so no human can override them) or tracked off-chain and enforced by the core team. On-chain enforcement via contract is more transparent and trustworthy.

## TGE vs. ICO vs. IDO

These terms are often jumbled:

**ICO (Initial Coin Offering)**: A fundraising event, typically before TGE, where the project sells tokens (or promises to deliver them at TGE) to investors. Investors send funds; the project receives capital.

**IDO (Initial DEX Offering)**: A fundraising event on a decentralized exchange, where users provide liquidity or buy tokens at a set price. Also typically before or simultaneous with TGE.

**TGE (Token Generation Event)**: The on-chain moment when tokens are actually minted and distributed. It is the technical execution, not the fundraising event.

A project might run an ICO in Month 1, then a TGE in Month 4 once development milestones are met. Or it might combine them: fundraise and generate tokens in a single week. The three are functionally distinct roles.

## Token supply dynamics post-TGE

At TGE, a fixed amount of tokens come into existence. Over time, the circulating supply changes as vesting schedules unlock and tokens move from locked to liquid. A project might start TGE with 1 billion total supply, but only 200 million in circulating supply (the rest locked or in reserves). After 2 years, circulating supply might be 500 million. This gradual unlock is reflected in price charts and liquidity metrics.

Some projects mint new tokens post-TGE through inflation or liquidity farming rewards. Others have a hard cap, so no new tokens ever exist beyond the TGE supply. The TGE itself does not determine post-TGE issuance policy; that is a separate protocol rule.

## See also

<div class="wiki-seealso">

### Closely related

- [Smart contract](/smart-contract/) — the code that defines and enforces token distribution
- [Blockchain fundamentals](/blockchain-fundamentals/) — the underlying system recording token creation
- [Distributed ledger](/distributed-ledger/) — the technology storing TGE and all subsequent transactions
- [Cryptocurrency exchange](/cryptocurrency-exchange/) — where tokens trade post-TGE
- [Proof of stake](/proof-of-stake/) — common post-TGE token use case for staking rewards
- [Vesting](/token-generation-event-explained/) — how TGE allocations are gradually unlocked

### Wider context

- [Initial public offering](/initial-public-offering/) — traditional-finance analog (though not identical)
- [Qualified dividend](/qualified-dividend/) — tax treatment of token distributions (varies by jurisdiction)
- [Capital gains tax (investor)](/capital-gains-tax-investor/) — tax implications of TGE token acquisitions
- [Equity financing](/equity-financing/) — comparison to traditional startup funding

</div>
