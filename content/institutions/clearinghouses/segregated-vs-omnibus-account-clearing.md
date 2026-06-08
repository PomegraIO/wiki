---
title: "Segregated vs Omnibus Client Accounts at a Clearinghouse"
description: "Segregated vs omnibus account clearing: individual isolation protects clients if a broker defaults, while omnibus pooling lowers costs but concentrates risk."
keywords:
  - segregated vs omnibus account clearing
  - segregated account clearinghouse
  - omnibus account clearing
  - client protection clearinghouse
---

*When you clear a trade through a **clearinghouse**, your account sits in one of two structures: **segregated** (your positions are individually isolated from other clients) or **omnibus** (your positions are pooled with those of other clients of the same broker). Each structure offers different protections and costs.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Segregated vs Omnibus — key facts</div>

<img src="/svg/institutions.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Segregated accounts protect you if your broker fails; omnibus accounts cost less but concentrate risk on the broker's solvency.</div>

|   |   |
|---|---|
| **Segregated** | Your positions isolated; visible in individual account at CCP |
| **Omnibus** | Pooled with other clients under one broker account at CCP |
| **Broker default (segregated)** | Your positions transfer cleanly; you keep all margin |
| **Broker default (omnibus)** | Your margin commingled; recovery may be delayed or incomplete |
| **Cost** | Segregated higher (CCP processing, risk fees); omnibus lower |
| **Who chooses** | Broker decides, sometimes with client negotiation |

</aside>

## The two account structures

When a broker clears trades on your behalf, the broker must hold an account at the clearinghouse. That account is where your margin sits, and where the CCP tracks open positions and applies margin charges.

The CCP offers the broker a choice of how to organize client accounts:

**Segregated clearing** means the CCP maintains a separate account in your name at the clearinghouse. Your margin and positions are recorded individually. The CCP's records show: "Client A's account has 500 ES contracts and $2.5 million margin." Every client has a distinct ledger.

**Omnibus clearing** means the CCP maintains a single account in the broker's name for all of that broker's clients. The CCP's records show: "Broker X's account has 50,000 ES contracts and $125 million margin," but does not distinguish which client owns which position. The broker keeps a separate internal ledger showing the allocation to individual clients.

## Segregation and insolvency protection

The practical difference becomes clear if the broker fails.

**Segregated scenario**: A broker holding segregated accounts goes bankrupt. The CCP still has you listed as the individual account holder. Your positions and margin remain in your CCP account, untouched. A trustee or the CCP itself can transfer your account to another broker, or liquidate your positions, without your margin being mingled with other clients' funds or the broker's own assets.

**Omnibus scenario**: The broker goes bankrupt. The CCP sees only the aggregate "Broker X" account. Your margin and positions are legally commingled with those of every other client of that broker. A bankruptcy trustee must then parse the broker's internal records to figure out which margin belongs to whom. That process can take weeks or months, and if the broker's records are incomplete or disputed, you may recover only a fraction of your margin.

This is not theoretical. During the 2008 financial crisis, when Lehman Brothers collapsed, clients with omnibus accounts faced months of uncertainty and partial recovery. Clients with segregated accounts were transferred cleanly to other brokers within days.

For this reason, large institutional clients almost always insist on segregated clearing. Retail clients, especially at low-cost brokers, often end up in omnibus accounts because the broker passes savings to them.

## The cost difference

Segregated clearing is more expensive for a broker. The CCP must:
- Maintain and reconcile individual accounts for every client.
- Apply margin calculations and risk charges individually.
- Process more granular settlement and collateral flows.

The CCP passes these costs back to the broker via higher clearing fees, and the broker may pass them to clients via higher commissions or margin rates.

Omnibus clearing is cheaper. The CCP performs margin calculations once per broker account, not per client. The broker absorbs the administrative burden of tracking individual client positions internally.

Brokers that cater to cost-sensitive clients—including most retail brokers—use omnibus clearing and advertise lower commissions as a result.

## Regulatory landscape

Regulators have pushed for more segregation in recent years. The [Dodd-Frank Act](/dodd-frank-act/) mandated that U.S. [futures](/futures-contract/) clients receive segregated clearing by default. However, a client can elect omnibus clearing if they choose (usually by signing a form). Similarly, the EU's EMIR rules give clients the right to segregated clearing, though again, a client can opt into omnibus if they accept the risk.

The rules recognize that segregation imposes real costs, so they allow clients and brokers to choose trade-offs. A hedge fund managing billions of dollars will choose segregation; a retail trader might not be offered it or might reject it to save on fees.

## Bankruptcy and recovery risk

The commingling risk in omnibus accounts is substantial but also nuanced.

If a broker fails and its omnibus account is in surplus (aggregate margin posted exceeds aggregate liabilities), all clients typically recover in full. The trustee liquidates positions, collects the margin, and distributes it pro rata.

But if the omnibus account is in deficit—the broker has suffered losses and cannot cover them—or if the broker has siphoned client margin to cover its own trading losses, recovery becomes contested. Clients stand in line with other creditors, and funds may be exhausted before reaching all claimants.

In segregated accounts, the default by the broker does not directly threaten your positions or margin. The risk is limited to operational delays (a few days to a week) while your account transfers to a new broker.

## Cross-margin and re-hypothecation

Omnibus clearing can also facilitate dangerous practices. A broker holding omnibus accounts may use client margin to secure its own financing or may allow clients' collateral to be re-hypothecated (re-pledged) by the CCP or lenders. These practices reduce what is returned to clients if the broker fails.

Segregated clearing constrains this. If margin is in a segregated account in your name at the CCP, the broker has less latitude to use it for its own purposes.

## Which structure for whom

**Institutions** (hedge funds, asset managers, large prop traders) almost always insist on segregated clearing. The cost is small relative to their volume, and insolvency protection is critical.

**Active retail traders** may request segregated clearing, especially if trading with a small or less-established broker. The extra fee (perhaps 10–20% higher commission) is worthwhile for the protection.

**Cost-conscious retail traders** use omnibus clearing and accept the broker-insolvency risk. Most brokers that advertise rock-bottom commissions achieve those prices partly by using omnibus clearing.

**Small institutional clients** and RIAs often end up in omnibus accounts because their brokers default to it and it is cheaper. A client who asks for segregation can usually get it, but not always.

## Practical implications

If you trade through a broker, you can ask your operations team which clearing structure you are in. The answer will be on your account opening paperwork or in a FAQ.

If you value insolvency protection over cost, request segregated clearing. If you prioritize lower commissions and are comfortable with the broker-solvency risk, omnibus is simpler and cheaper.

In either case, the CCP itself is not insolvent; it is the broker's solvency that is the variable. Segregation protects you from that specific failure mode.

## See also

<div class="wiki-seealso">

### Closely related

- Central Counterparty — the CCP that maintains account structures
- [CCP Stress Testing Explained](/ccp-stress-testing-explained/) — how CCPs ensure they can absorb broker defaults
- [Securities Lending and Clearinghouses](/securities-lending-and-clearinghouses/) — how account types affect repo and securities-lending settlement
- Margin — the collateral in these accounts

### Wider context

- [Counterparty Risk](/counterparty-risk/) — the risk segregation and omnibus structure manage
- [Broker](/broker/) — the intermediary offering either structure
- [Dodd-Frank Act](/dodd-frank-act/) — U.S. regulation mandating segregation rights

</div>
