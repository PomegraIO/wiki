---
title: "CCP Default Auction: How a Clearinghouse Manages a Defaulted Portfolio"
description: "When a clearing member defaults, the CCP auctions their portfolio to surviving members in a competitive process; if bids fall short, the CCP absorbs losses from its default fund."
keywords:
  - ccp default auction
  - clearing house defaulted portfolio
  - central counterparty resolution
  - defaulted member auction process
  - clearing fund waterfall
image: "/svg/institutions.svg"
---

*A **CCP default auction** is the competitive bidding process by which a clearing house invites surviving members to take on a failed member's open positions—trades, collateral, and liabilities—after that member has ceased to meet margin requirements or capital calls. It is the clearinghouse's primary tool to transfer risk away from itself and prevent the default from cascading across the entire system.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">CCP Default Auction — key facts</div>

<img src="/svg/institutions.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">An auction that decides who absorbs a failed counterparty's risk.</div>

|   |   |
|---|---|
| **When triggered** | Member fails margin call or capital requirement; CCP declares default. |
| **What's auctioned** | Open positions, collateral, and all contractual obligations of the failed member. |
| **Who bids** | Surviving members; often investment banks, hedge funds, or dedicated capital providers. |
| **Auction structure** | Typically sealed-bid or iterative rounds; CCP may offer initial haircuts or sweeteners. |
| **If bids succeed** | Winning bidder assumes all positions at the agreed price; defaulter's members are protected. |
| **If bids fail** | CCP draws on its own [default fund](/default-fund/); losses cascade through member contribution tiers. |
| **Timeline** | Usually within hours to 2–3 days; speed is critical to prevent [systemic risk](/systemic-risk/). |

</aside>

== Why the Auction Matters

Before modern central counterparties (CCPs) became standard, a member's bankruptcy could unravel the entire network. When a large [broker](/broker/) or dealer failed, their counterparties faced sudden exposure they'd thought was hedged, forcing a chain of defaults. The CCP auction was designed to break that chain by transferring the failed member's book to a willing counterparty quickly and without negotiation delays.

The auction accomplishes several goals at once:
- **Protects members**: Surviving members' positions are preserved and unchanged; they remain counterparties to the CCP, not to the failed firm.
- **Achieves price discovery**: The market decides the fair value of the failed member's portfolio through competitive bidding.
- **Preserves netting benefits**: The CCP can transfer the failed member's full position set (often thousands of contracts) as a legal unit, preserving the netting offsets that reduce credit exposure.
- **Buys time**: The CCP avoids forced liquidation in a panic market; instead, a buyer can decide whether to hold, unwind, or hedge the positions gradually.

== The Auction Process: Structure and Timeline

Most CCPs follow a roughly similar process:

**1. Default Declaration (Hours 0–2)** The CCP declares a member in default after the member fails to post margin or meet a capital call. The CCP immediately begins assembling the member's complete position inventory, including all derivatives, security holdings, collateral, and cash balances across all accounts.

**2. Auction Preparation (Hours 2–8)** The CCP publishes an outline of what will be auctioned: the list of positions, their sizes, mark-to-market values (or proxy valuations), collateral available, and the member's net debit or credit. The CCP may also announce initial terms: whether it will cover losses up to a certain threshold, offer a guarantee period on the positions, or provide other inducements.

**3. Invitation to Bid (Hours 8–12)** The CCP invites all surviving members (and, in some cases, non-members with special auction access) to submit bids. The bid includes an offer price—expressed as a cash adjustment or haircut to the mark-to-market value—and any conditions (e.g., "I will assume these positions only if you also cover the first $5 million in funding shortfall").

**4. Bid Evaluation and Selection (Hours 12–20)** The CCP evaluates all bids. If the default fund has cushion, the CCP may accept the highest bid even if it doesn't cover 100% of the losses; the difference comes from the CCP's resources. If the default fund is tight, the CCP may auction in multiple rounds, seeking progressively lower prices or offering additional incentives.

**5. Transfer and Settlement (Hours 20–48)** The winning bidder assumes all positions at the agreed price. The CCP transfers contracts, collateral, and any cash settlement. The defaulter's members are made whole; the winning bidder becomes the new counterparty to all affected clearing members.

In some recent CCPs, this timeline has compressed to 4–6 hours through pre-positioned authority and technology. In other cases, especially if the defaulter's book is vast and complex, the auction may take 2–3 days.

== Variations: Partial Auctions and Portfolio Splitting

The CCP is not required to auction the entire portfolio to one buyer. If a single bidder cannot absorb $100 billion in exotic derivatives and Treasury bonds, the CCP can split the book: one buyer takes the FX positions, another takes rates, a third takes equities. This is common and often improves price discovery; each bidder is more expert in their segment.

Some CCPs also conduct iterative auctions: round one seeks a buyer for the entire book at a steep discount (e.g., 10% haircut). If no takers, round two re-auctions with a 15% haircut. This continues until a buyer is found or the discount reaches a maximum (e.g., CCP absorbs 30% loss).

== What Happens If No Bid Emerges

This is the nightmare scenario. If no surviving member is willing to assume the defaulted book at any price, the CCP must liquidate it in the open market. This is slow, risky, and often nets worse prices than an auction would. The CCP typically:

1. **Enters the market as a liquidator**, selling portions of the book through existing brokers or exchanges.
2. **Bears all losses** that exceed the defaulted member's collateral. These losses are absorbed by the CCP's capital first, then by the default fund.
3. **May trigger a waterfall**, where surviving members are asked to contribute additional capital to cover losses that exceeded the pre-funded default fund.

In extreme cases (e.g., if the defaulted member had massive leveraged positions and the market gapped overnight), the CCP may exhaust its entire default fund and be forced to invoke emergency mechanisms: haircut all members' collateral, cap member access to withdrawals, or request a government backstop.

## Why Auctions Can Still Fail

Even with a well-designed CCP and ample default fund, an auction can founder if:

- **The book is too large**: No single firm has the balance sheet capacity or risk appetite to assume $200 billion in positions.
- **Market stress is severe**: During a liquidity crisis, even well-capitalized firms are reluctant to take on additional risk and are hoarding liquidity.
- **Collateral is illiquid**: If the defaulted member posted obscure or hard-to-value collateral, the pool of resources is smaller than it appears.
- **The positions are exotic or concentrated**: A book of simple FX swaps is easy to assume; a book of bespoke credit derivatives with counterparty concentration is not.

The 2008 financial crisis tested CCPs (especially DTCC, which managed Lehman Brothers' positions). Lehman's clearance with DTCC was resolved through an auction that attracted multiple bidders because (1) DTCC had already de-risked Lehman through daily marking and margining, and (2) DTCC offered to assume a portion of the loss. The speed and success of that auction was a major reason the collapse did not trigger a cascading CCP failure.

== The Default Fund and Its Hierarchy

The CCP's default fund is financed by surviving members' contributions, sized to cover a "one-in-a-thousand year" loss (or whatever the regulator mandates). When an auction fails and losses exceed the defaulted member's collateral, the default fund is depleted in a waterfall:

1. **Defaulted member's contribution** (used first, already exhausted if they're bankrupt).
2. **Surviving members' prefunded contributions** (usually called the "default fund").
3. **CCP's own capital** (an emergency buffer).
4. **Survivor loss allocation** (CCP may force all members to post additional capital).

The existence of this waterfall is why CCPs must auction quickly and widely: every dollar the auction recovers above zero is a dollar that is not drawn from members' contributions.

== See also

<div class="wiki-seealso">

### Closely related

- Clearinghouse — The institution that runs default auctions
- Central Counterparty — The legal structure that enables auctions
- [Default Fund](/default-fund/) — The pool of capital that backs auction shortfalls
- Margin — The collateral that must be posted to prevent default
- [Counterparty Risk](/counterparty-risk/) — The credit risk the auction mechanism mitigates

### Wider context

- [Systemic Risk](/systemic-risk/) — Why failed auctions are a contagion threat
- [Liquidity Risk](/liquidity-risk/) — The real-time funding challenge during auctions
- [Credit Event (Sovereign)](/credit-event-sovereign/) — How defaults are triggered and managed

</div>
