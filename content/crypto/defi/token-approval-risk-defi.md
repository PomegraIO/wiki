---
title: "Token Approval Risk in DeFi"
description: "Token approval risk is the exposure you create by authorizing DeFi contracts to spend your tokens. Unlimited approvals can be exploited for total asset loss."
keywords:
  - token approval risk defi
  - unlimited token approvals
  - revoke token approval
  - smart contract risk
  - defi security wallet
image: "/svg/crypto.svg"
---

*When you interact with a DeFi protocol—swapping tokens, providing liquidity, borrowing—you must "approve" the contract to spend your tokens. The danger is **token approval risk**: approving a contract to spend an *unlimited* amount of your tokens. If the contract is hacked, the code is malicious, or the protocol becomes abandoned, attackers can drain your entire balance without further consent. The approved amount remains active until explicitly revoked, sometimes indefinitely. Most DeFi users unknowingly grant unlimited approvals and never revoke them.*

## How Token Approvals Work

On blockchains like [Ethereum](/ethereum/), tokens themselves (like USDC, DAI, or custom ERC-20 tokens) are smart contracts that track balances and ownership. Unlike native assets (ETH on Ethereum, native assets on other chains), moving an ERC-20 token requires permission from the owner.

To use a token in a DeFi contract, you perform two steps:

1. **Approve**: You sign a transaction that tells the token's smart contract: "Let contract X spend up to N amount of my tokens."
2. **Use**: The DeFi contract then transfers your approved tokens into the protocol (for a swap, a liquidity pool, a loan, etc.).

The approval is a separate transaction. Once granted, it remains active. The DeFi contract can spend your tokens repeatedly, up to the approved amount, without asking again.

Most DeFi interfaces default to asking for an **unlimited approval**—meaning you authorize the contract to spend *all of your tokens indefinitely*. This is a convenience choice for users (you don't have to re-approve each time you trade) and developers (no limit-checking code to maintain). But it's dangerous.

## The Exploitation Scenario

Here's how unlimited approval becomes a catastrophic risk:

**Step 1: You approve a DeFi protocol**  
You want to trade USDC on what appears to be a legitimate decentralized exchange. You click "Approve," and your wallet shows a request asking permission for the contract to spend an unlimited amount of your USDC. You sign it.

**Step 2: The contract is exploited**  
Days or months later, a hacker discovers a vulnerability in the DeFi protocol. The hacker doesn't need to compromise *your* wallet or private keys. They exploit the contract's code and inject instructions to transfer all USDC from all approved accounts into an attacker-controlled address.

**Step 3: Your entire balance is stolen**  
The moment the exploit executes, your full USDC balance (or full balance of the approved token) is transferred out. No second approval was needed. The original approval you signed gave blanket permission.

This has happened repeatedly. In 2020–2023, stolen DeFi approvals have resulted in millions of dollars in losses across protocols like Uniswap, Balancer, Yearn Finance, and countless others. In many cases, the victims' wallets and private keys were perfectly secure—the theft came *through* the approved contracts, not *around* them.

## The Difference Between Approvals and Wallet Compromise

It's crucial to understand that token approval risk is **independent of wallet security**.

- **If your private key is stolen**: An attacker can drain all your assets and revoke or grant approvals on your behalf.
- **If an approval is exploited**: An attacker can drain only the tokens you approved *to that contract*. Other tokens in your wallet remain safe (unless they're also approved to the same contract).

This is why unlimited approvals are so dangerous: they create a single point of failure. One bad contract = potential loss of many tokens across your entire balance.

## Common Approval Patterns and Risk Tiers

**Unlimited approvals (highest risk):**
- You authorize a contract to spend an infinite amount, capped only by your balance.
- Pros: Convenient—you can trade, deposit, and swap unlimited times without re-approving.
- Cons: One exploit drains everything.
- Best for: Contracts you audit carefully or use repeatedly (e.g., your primary exchange).

**Limited approvals (medium risk):**
- You authorize a contract to spend exactly what you need for that transaction (e.g., approve 100 USDC to buy exactly 100 USDC worth of another token).
- Pros: Even if the contract is hacked, attackers can only drain that specific amount.
- Cons: You must re-approve for each new transaction or increase the limit.
- Best for: Untrusted or one-off interactions, high-risk protocols.

**Revoked approvals (lowest immediate risk):**
- You withdraw the contract's permission to spend your tokens entirely.
- Pros: The contract cannot transfer any of your tokens.
- Cons: You cannot use the contract until you approve again.
- Best for: Protocols you no longer use.

## Auditing Your Approvals

Every major blockchain lets you inspect approvals tied to your wallet. Most users grant 10, 20, or even 50+ approvals without realizing it. Many are to contracts that no longer exist or that the user abandoned months ago.

To audit and revoke approvals:

1. **Visit an approval explorer** (such as Etherscan's token approval tracker, or the approval dashboard in MetaMask 10.16+).
2. **Connect your wallet** and view all active approvals.
3. **Identify approvals** you no longer use or trust.
4. **Revoke selectively** by signing a transaction that sets the approved amount to zero. Revocation is cheap (single transaction) and immediate.

For example, if you tried a DeFi swap platform once in 2022, decided you didn't like it, and never returned—revoking the approval is prudent. If you actively use Uniswap every week, revoking its approval would be inconvenient, so you might keep it (accepting the risk) or revoke it and re-approve quarterly.

## Risk Factors: When Approvals Become Liabilities

**Contract code quality:**
- Audited, battle-tested protocols (Uniswap, Aave, Curve) have lower exploit risk than newer, unaudited ones.
- An approval to a 3-day-old contract is riskier than one to a 3-year-old market-leading protocol.

**Age and abandonment:**
- Approvals to contracts that are no longer maintained are particularly dangerous. If a developer stops monitoring the contract and a vulnerability emerges, it may never be patched.
- Check whether the protocol is still active, whether it has a team, and whether it has made recent updates.

**Token concentration:**
- If you approve a contract with 90% of your portfolio balance, that approval poses systemic risk. An exploit there could be catastrophic.
- Spreading assets across multiple contracts and wallets reduces single-contract failure impact.

**Staking and auto-compounding:**
- Some DeFi protocols (like yield farms) require you to approve the contract to deposit your tokens *and* approve it to earn and reinvest rewards. These carry compounded approval risk.

## Best Practices

**Revoke old approvals:**  
Set aside 30 minutes quarterly to audit and revoke approvals you no longer use. It costs only gas fees and takes seconds per revocation.

**Limit approval amounts:**  
When feasible, approve only what you need for a specific transaction. This requires slightly more transaction overhead but significantly reduces loss potential.

**Separate wallets for different risk profiles:**  
- Use a "hot" wallet for active trading with higher-risk approvals.
- Use a "cold" wallet for storing core long-term positions, approving only when moving assets between chains or into established protocols.

**Monitor newly deployed contracts:**  
If a protocol launches with a new contract version (to fix a bug or add features), be cautious. Request the team publish an audit before you migrate approvals to the new contract.

**Use approval limits where available:**  
Some modern DeFi front-ends (like newer versions of Uniswap) let you choose approval amounts (e.g., approve 1000 USDC instead of unlimited). Use these options.

## Revocation Mechanics and Edge Cases

Revoking an approval is straightforward: you send a transaction to the token contract saying "set the approved amount for [contract X] to zero."

However, there are edge cases:

- **Approval still appears in old dashboards**: After you revoke, some explorers may take hours or days to update. The approval is revoked on-chain; the interface is just behind.
- **Multiple contract versions**: Some protocols have multiple versions (V2 vs. V3). You may need to revoke approvals to *each* version separately.
- **Proxy contracts**: Some DeFi protocols use proxy patterns where a "proxy" contract calls a "logic" contract. You may need to revoke approval to the proxy, not the logic contract.

If you're unsure whether you've revoked an approval successfully, re-check the explorer 10–15 minutes after the revocation transaction confirms. The approval amount should show as zero.

## See also

<div class="wiki-seealso">

### Closely related

- [Smart contract](/smart-contract/) — the code that processes approvals and must be audited for security
- [Distributed ledger](/distributed-ledger/) — the blockchain that records approvals and transactions immutably
- [Proof of work](/proof-of-work/) — security model that makes blockchain exploits costly
- [Cryptocurrency exchange](/cryptocurrency-exchange/) — where centralized platforms reduce approval risk by holding custody

### Wider context

- [Blockchain fundamentals](/blockchain-fundamentals/) — how tokens and contracts interact on public ledgers
- DeFi — decentralized finance protocols and their risks
- [Ethereum](/ethereum/) — the primary blockchain where ERC-20 tokens and approval mechanisms operate
- [Counterparty risk](/counterparty-risk/) — the broader category of risk when trusting another party or contract with your assets

</div>
