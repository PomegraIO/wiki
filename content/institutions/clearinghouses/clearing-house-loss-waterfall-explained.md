---
title: "Clearinghouse Loss Waterfall: Who Absorbs Losses and in What Order"
description: "How clearing houses manage default: the loss waterfall defines the sequence in which defaulter's margin, fund contributions, and surviving member capital absorb losses."
keywords:
  - clearinghouse loss waterfall
  - CCP default management
  - counterparty risk
  - clearing member default
  - default waterfall order
image: /svg/institutions.svg
---

*When a **clearing member** defaults on a futures or derivatives exchange, losses do not fall on the broader market at random. A **clearinghouse loss waterfall** is a legal and financial stack that absorbs losses in a fixed sequence: first the defaulter's own margin and fund contributions; then the clearinghouse's capital; then surviving members' contributions to a mutually-owned loss fund. This hierarchy is designed to contain contagion and allocate pain in a predictable way.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Clearing house loss waterfall — key facts</div>

<img src="/svg/institutions.svg" alt="An abstract editorial mark for financial institutions." />

<div class="wiki-infobox-caption">Losses flow downhill in order: defaulter's assets, then CCP's assets, then surviving members.</div>

|   |   |
|---|---|
| **Layer 1** | Defaulter's initial [margin](/margin-call-forex/) and variation margin |
| **Layer 2** | Defaulter's contribution to clearing fund |
| **Layer 3** | Clearinghouse's own [capital](/capital-adequacy/) and reserves |
| **Layer 4** | Surviving members' fund contributions (up to limit) |
| **Layer 5** | Rare: government or industry bailout |
| **Purpose** | Isolate losses and prevent systemic contagion |

</aside>

## The waterfall hierarchy: why it matters

A central counterparty (CCP) or clearing house exists to guarantee trades. When you trade a [futures contract](/futures-contract/) on an exchange like the Chicago Mercantile Exchange (CME), the clearinghouse steps between buyer and seller. If the buyer defaults, the clearinghouse covers the loss from its own pocket—at least initially. The loss waterfall defines how that pocket is refilled, and in what order other market participants bear the cost.

This hierarchy exists because:

1. **Clarity**: All members know beforehand which layer will absorb losses first, reducing uncertainty and panic.
2. **Discipline**: Knowing the waterfall exists, members have incentive to monitor each other's risk and demand margin increases before things get dire.
3. **Moral hazard control**: Members cannot assume they will be bailed out early in the waterfall; they must manage counterparty risk themselves.
4. **Orderly wind-down**: During a crisis, regulators and clearing members know which entity bears losses when, enabling an orderly liquidation rather than a free-for-all.

## Layer 1: The defaulter's own margin and guarantees

The first loss falls on the failing member. When a futures trader opens a position, they post [initial margin](/margin-call-forex/)—a cash deposit or treasury bond held by the clearinghouse. As the position moves against them, they post [variation margin](/margin-call-forex/)—additional funds daily to cover losses. These are the member's own funds, and they are the first to go.

If a member's open positions have a cumulative loss of $10 million and the member posted $8 million in initial and variation margin, the clearinghouse covers the $2 million shortfall from the next layer. The member's own collateral is exhausted.

Some clearing members are also primary dealers or banks with other assets pledged to the clearinghouse. These assets form a "guarantee fund" or "guarantee deposit" that is liquidated second—ahead of the clearinghouse's own capital, but after the initial margin.

## Layer 2: The defaulter's clearing fund contribution

Clearing members pay dues into a **clearing fund** (also called a **guarantee fund** or **mutualized loss fund**). This is collective protection. Each member contributes a percentage of its clearing activity or a flat annual fee. The CME Clearing Fund, for example, required members to contribute hundreds of millions of dollars.

If the defaulter's own margin and deposits are exhausted, the defaulter's share of the clearing fund is drawn. This can be a significant sum—sometimes 100% of that member's annual dues multiplied by a retention factor. On the CME, the waterfall specifies exactly how many years of each member's contributions are available.

The logic: the defaulting member paid into a mutual loss pool while operating, so its money should cover part of the damage it caused.

## Layer 3: Clearinghouse capital and reserves

Once the defaulter's own money is gone, the clearinghouse itself steps in. Large clearing houses hold substantial capital—equity and retained earnings—specifically to absorb unexpected losses from member defaults. The CME holds tens of billions of dollars in capital; Eurex and LCH hold billions more.

This is a critical shock absorber. The clearinghouse's capital is not mutualized; it is at risk only for the CCP's own benefit. Drawing on CCP capital means losses are borne by the shareholders (typically the largest clearing members, which own the exchange) and by the CCP's ability to operate.

Regulators require clearinghouses to hold enough capital to cover the default of the *two largest members*—the "cover-two standard." This is meant to ensure that even if two major dealers blow up simultaneously, the CCP can absorb the losses without calling on surviving members.

However, the 2008 financial crisis and more recent stress tests have shown that extreme scenarios can exceed cover-two. If the CCP's capital is exhausted, the waterfall moves to the fourth layer.

## Layer 4: Surviving members' additional contributions

This is the nuclear option. Once the CCP's capital is depleted, the clearing house has the right to call on surviving members for additional payments into the loss fund. This is called a **loss assessment** or **emergency assessment**.

The CME Clearing Fund waterfall specifies that surviving members contribute additional amounts equal to their historical percentage of the clearing activity, capped at a maximum. Typical caps are equivalent to 10–50 years of a member's annual dues. This can amount to hundreds of millions of dollars for a large dealer.

When a loss assessment is triggered, surviving members must pay within days or hours. Failure to pay can result in suspension or expulsion from the exchange. This structure creates a second round of moral hazard: members know that a huge loss at one shop could require them to bail out the system, so they police each other's risk closely.

The fear of assessment is so strong that clearing members actively lobby for higher capital requirements at the CCP—they would rather the CCP be well-capitalized than face the uncertainty and cost of a loss assessment. This is one reason CCPs have been well-capitalized since 2008.

## Layer 5: Government intervention and industry bailouts

In the absolute worst case—losses exceed the clearing fund, CCP capital, and surviving members' assessed contributions—the clearing house may turn to government or industry backstops. This has never happened at a major US futures clearing house, but it is not ruled out.

During the 2008 crisis, the government provided emergency liquidity to clearinghouses, but this was more about funding than about covering fundamental losses. The AIG bailout included payments related to credit derivatives cleared at LCH, but the CCP itself did not require a bailout.

The mere existence of this theoretical layer reinforces the incentive for earlier layers to hold enough capital. No one wants to be the clearing house that requires a government rescue.

## The 2020 Archegos test: why the waterfall matters

The Archegos Capital default in March 2020 was a live test of the waterfall. Archegos was not a clearing member itself—it was a prime brokerage client of banks like Credit Suisse and Nomura. But the losses it created ($10+ billion) exposed the underlying risk: if a large clearing member had defaulted, the waterfall would have been triggered.

In the event, prime brokers absorbed the losses directly and called margins on Archegos' positions. The clearing house did not face a default. But the incident showed regulators that leverage in the ecosystem remained high and that a clearing member default was still a non-trivial tail risk.

## Key features of the waterfall framework

Modern clearing house rules (enforced by regulators like the SEC, CFTC, and ESMA) specify:

- **Absolute priority**: Losses are absorbed in a strict sequence; no mixing of layers.
- **Transparency**: The waterfall is published in clearing rules and regularly stress-tested.
- **No re-ordering**: The clearinghouse cannot change the waterfall to protect favored members.
- **Speed**: Losses are allocated within 24–48 hours to prevent cascading defaults elsewhere.
- **Pre-funding**: Most layers (defaulter's margin, clearing fund) are pre-funded; the clearinghouse can call on them without negotiation.

Some jurisdictions also require "skin in the game"—clearinghouses must hold at least 1–2% of their capital at the front of their own default waterfall, in addition to capital for cover-two. This makes the CCP itself a meaningful loser in its own default scenario, aligning incentives.

## Cross-border complexity

The waterfall becomes murky in cross-border situations. If a US clearing member of CME clears Canadian futures, does the CME waterfall or the Canadian clearing house waterfall apply? Regulators have negotiated "interoperability" agreements, but gaps remain. A default touching multiple jurisdictions could expose inconsistencies in the waterfall hierarchy.

This is one reason the Financial Stability Board (FSB) and regulators have pushed all standardized derivatives into centralized clearing houses—to simplify the waterfall and reduce bilateral [counterparty risk](/counterparty-risk/).

## See also

<div class="wiki-seealso">

### Closely related

- [Counterparty risk](/counterparty-risk/) — the risk the waterfall is designed to mitigate
- [Futures contract](/futures-contract/) — contracts whose losses trigger the waterfall
- [Clearinghouse](/clearing-house-loss-waterfall-explained/) — the institution that manages the waterfall
- [Margin call](/margin-call-forex/) — deposits that form Layer 1
- [Credit default swap](/credit-default-swap/) — derivatives that also sit behind central clearing

### Wider context

- [Financial crisis 2008](/great-depression/) — when the waterfall was tested and reformed
- [Systemic risk](/systemic-risk/) — why clearing house stability matters
- [Central bank](/central-bank/) — backstop in extreme scenarios
- [Regulatory framework](/dodd-frank-act/) — Dodd-Frank and post-2008 reforms that shaped the waterfall

</div>
