---
title: "DeFi Lending Utilization Rate Explained"
description: "How a DeFi lending pool's utilization rate—the share of deposits currently borrowed—determines both borrow APR and supply APR in money-market protocols."
keywords:
  - defi lending utilization rate
  - money market utilization rate
  - aave utilization rate
  - lending pool utilization
  - defi borrow rate supply rate
image: /svg/crypto.svg
---

*In decentralized finance lending pools, the **utilization rate** — the percentage of deposited assets that are currently borrowed — directly determines interest rates paid by borrowers and earned by lenders. A rising utilization rate increases borrow rates (to discourage further borrowing and protect the pool) and supply rates (rewarding lenders for capital tied up in a tight market).*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">DeFi Lending Utilization — key facts</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for cryptocurrency." />

<div class="wiki-infobox-caption">Utilization rate is a mechanical pricing lever; it rises when demand for loans is high relative to deposits.</div>

|   |   |
|---|---|
| **Definition** | (Total Borrowed) / (Total Supplied) × 100% |
| **Rate function** | Borrow APR and supply APR rise as utilization climbs |
| **Typical ranges** | 20–80% on major pools; >90% signals capital scarcity |
| **Supply APR** | Borrow APR × Utilization Rate (minus protocol fees) |
| **Governance** | Protocol can adjust rate curves; Aave, Compound, Morpho allow DAO adjustments |
| **Risk driver** | High utilization reduces lender withdrawal liquidity; pools can hit 100% and halt new borrows |

</aside>

## How Utilization Rate Works

A DeFi lending pool like Aave or Compound operates as a simple ledger: lenders deposit assets (earning interest), borrowers withdraw assets (paying interest), and the protocol balances supply and demand through interest rates.

The utilization rate is calculated as:

**Utilization = Total Borrowed / (Total Supplied)**

For example, if a pool has $100 million in deposits and $60 million is currently borrowed, the utilization rate is 60%. If borrowing grows to $80 million, utilization rises to 80%.

This single number becomes the master control for the pool's interest rates. As utilization climbs, both borrow rates and supply rates rise algorithmically. The protocol does this mechanically — no human decision-maker or vote is required for each interest rate change.

## The Rate Curve: How Interest Rates Respond to Utilization

Each lending protocol defines a **rate curve** — a formula that maps utilization to interest rates. The exact curve varies by protocol and asset type, but the logic is universal:

- **At low utilization (e.g., 20%):** Borrow rates are low (perhaps 2% APY), encouraging borrowing and balancing the supply that's sitting idle.
- **At medium utilization (e.g., 60%):** Rates rise (perhaps 5–8% APY), as the pool signal that capital is scarce.
- **At high utilization (e.g., 85%+):** Rates spike sharply (15%, 30%, or higher), discouraging further borrowing and protecting lenders who want liquidity.

The steep rise at high utilization serves two purposes:
1. It discourages marginal borrowers (making a 3% arbitrage trade won't make sense at 25% borrow rates).
2. It rewards patient lenders — if you lock capital in a 85%-utilized pool, you earn a high supply rate.

Most protocols also include a **kink** in the curve — a utilization threshold above which the rate slopes up much more steeply. For instance, rates might rise gradually from 0% to 80% utilization, then jump sharply above 80%, signaling "this pool is dangerously tight."

## Supply Rate Mechanics

The supply rate (what lenders earn) is not set independently. Instead, it's calculated as:

**Supply APR = (Borrow APR × Utilization Rate) – (Protocol Fee)**

This elegantly ties borrower and lender returns together. If borrow APR is 10%, utilization is 70%, and protocol fees are 10%, then:

Supply APR = (10% × 70%) – 10% = 7% – 10% = 5.9%

(Protocol fees vary; some protocols take a small cut, others take none.)

The logic is intuitive: lenders earn interest only on the borrowed portion (utilization × borrow APR). The idle portion of deposits earns nothing. As utilization rises, lenders capture a larger share of the borrow fees; as it falls, their returns shrink.

This creates a natural incentive: when utilization is low and supply rates are unattractive, lenders are tempted to withdraw. When utilization is high and supply rates are fat, lenders are incentivized to stay or deploy more capital.

## Why Utilization Rate Matters

**Risk and Liquidity**

A pool at 95% utilization has only 5% of deposits available for withdrawal. If lenders panic and rush to exit, the pool runs out of cash and halts withdrawals until borrowers repay loans. High utilization reduces what's called **withdrawal liquidity** — your ability to get your money out on demand.

By raising rates aggressively at high utilization, the protocol tries to prevent this scenario: high supply rates should attract capital, while high borrow rates should encourage repayment and discourage new loans.

**Capital Efficiency**

Borrowers and arbitrageurs use leverage. If a DEX [arbitrage](/algorithmic-trading/) opportunity exists but requires capital that's unavailable, utilization rises and borrow rates spike, making the trade uneconomical. This is the market working: capital flows to the highest-value use.

**Governance and Adjustment**

DAOs can adjust the rate curves over time. Aave, for instance, allows governance votes to change the slope and shape of the utilization-to-rate function. A more aggressive curve (steeper increase at high utilization) discourages overborrowing but may reduce pool utility. A gentler curve invites higher utilization but risks liquidity crunches.

## Comparing Utilization Across Pools

Different assets and pools have different typical utilization levels:

- **Stablecoins on major pools** (USDC, USDT, DAI): 30–70% utilization, relatively stable; high liquidity.
- **Ethereum and volatile collateral:** 50–85% utilization; higher variability and risk.
- **Emerging or niche tokens:** Can spike to 90%+ during hype cycles, then plummet; volatile.

Comparing utilization across pools is a shorthand for risk. A stable asset at 40% utilization is more liquid and safer than an alt-token at 85%. But utilization alone doesn't tell the whole story — you also need to know whether that 85% reflects genuine demand for loans or a liquidity crisis.

## Practical Implications for Lenders and Borrowers

**For lenders:** Chasing high supply APRs from high-utilization pools is a trade-off. You earn more interest but face withdrawal risk and potential [counterparty risk](/counterparty-risk/) if collateral prices fall and borrowers default. Diversifying deposits across pools with different utilization levels is prudent.

**For borrowers:** When utilization is high, borrow rates are steep. If you're borrowing for leverage or a time-sensitive trade, you want low utilization (low rates). If utilization spikes, your borrowing cost rises immediately, and [carry trade](/carry-trade/) opportunities evaporate.

**For protocol governance:** Adjusting rate curves affects the entire ecosystem. A steeper curve discourages leverage and risk; a gentler curve encourages capital recycling and arbitrage. Different philosophies lead to different governance votes.

## See also

<div class="wiki-seealso">

### Closely related

- [Cryptocurrency Exchange](/cryptocurrency-exchange/) — where borrowers source collateral and exit positions
- [Counterparty Risk](/counterparty-risk/) — the risk that a borrower defaults and lenders lose funds
- [Interest Rate](/interest-rate/) — how DeFi APRs compare to traditional finance
- [Carry Trade](/carry-trade/) — a common borrow-and-deploy strategy that uses DeFi leverage

### Wider context

- [Distributed Ledger](/distributed-ledger/) — the underlying technology enabling transparent, trustless lending pools
- [Smart Contract](/smart-contract/) — the code that executes rate curves and manages deposits and borrows
- [Liquidity Risk](/liquidity-risk/) — the broader concept that utilization-driven withdrawals embody
- [Credit Risk](/credit-risk/) — default risk inherent in DeFi lending when collateral is insufficient

</div>
