---
title: "Omnibus Account"
description: "A brokerage or intermediary account that aggregates holdings from multiple beneficiaries under a single beneficial owner, masking individual investor identities from the fund."
keywords:
  - omnibus account
  - beneficial ownership
  - street name shares
  - broker account
  - shareholder record
image: "/svg/funds.svg"
---

*An **omnibus account** is a single brokerage or custodial account held in the name of one intermediary—typically a broker or clearing firm—that contains the combined holdings of multiple underlying beneficiaries whose identities are not disclosed to the fund. The fund's transfer agent sees only the intermediary as the shareholder; the identities of the actual investors behind that account remain opaque. Omnibus accounts are standard in the mutual fund industry and serve both operational and privacy purposes.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Omnibus Account — key facts</div>

<img src="/svg/funds.svg" alt="An abstract editorial mark for investment funds." />

<div class="wiki-infobox-caption">One visible owner, many hidden beneficiaries; standard in retail fund distribution.</div>

|   |   |
|---|---|
| **What it is** | An aggregated brokerage account masking individual investor identities from the fund |
| **Also called** | Omnibus holder, street name account, aggregated account |
| **Typical owner** | A broker, clearing firm, custodian, or financial adviser |
| **Beneficial owners** | Individual investors whose names don't appear to the fund |
| **Regulatory framework** | Required by Regulation SHO and SEC rules |
| **Privacy implication** | Fund cannot easily identify individual shareholders |

</aside>

## How it works

When an investor buys a [mutual fund](/mutual-fund/) through a broker like Charles Schwab or [Fidelity](/fidelity-investments/), or through a financial adviser, the shares are typically registered in the broker's or adviser's name, not the investor's own name. The fund's transfer agent records Schwab (or the clearing firm behind Schwab) as the shareholder of record. Behind that one account, Schwab holds shares on behalf of thousands of clients, each with a separate account balance.

The fund does not know who the beneficiary is. It cannot send a prospectus directly to the underlying investor. It cannot solicit votes from the beneficiary on proposed merger or fee changes. Dividends and distributions flow to the omnibus account holder (Schwab), which then routes them to each beneficial owner's brokerage account. From the fund's perspective, it is dealing with one customer: the broker.

## Why omnibus accounts exist

The practice solved a scaling problem. In the early days of mutual funds, every shareholder had to be registered by name. A large fund might have millions of individual shareholders, each requiring a separate record, each requiring mail, each potentially requiring individual vote solicitation. Transfer agents and funds struggled with administrative volume.

Omnibus structures let a single broker represent all its clients at once. Schwab holds one omnibus account per [mutual fund](/mutual-fund/)—potentially containing millions of shares for millions of Schwab clients. The fund's transfer agent maintains one record instead of millions. When a Schwab client redeems shares, Schwab adjusts its internal ledger and submits a bulk redemption instruction to the fund. The fund processes it as one transaction.

This efficiency was essential to the growth of retail [mutual fund](/mutual-fund/) distribution. Without omnibus accounts, the infrastructure cost of servicing millions of small investors would be prohibitive.

## Privacy and regulatory trade-offs

From a privacy standpoint, omnibus accounts mean the fund has no direct knowledge of who its shareholders are. It cannot market directly to you. It cannot tell you have accounts at multiple funds. It cannot solicit proxies in your name. The broker sits between you and the fund, controlling the communication channel.

Regulators accepted this structure because the broker (the omnibus account holder) is a regulated entity, and the SEC can compel disclosure when necessary. If the SEC needs to identify shareholders for an investigation, it can subpoena the broker's records. Mutual funds, for tax and compliance purposes, can request (though not always obtain) beneficiary data from omnibus holders.

But the default position is opacity. This has created recurring problems: class action settlements struggle to identify claimants; corporate events affecting a fund (like a merger) must be communicated through intermediaries; dividend record dates become complicated because the fund's official shareholder list does not match the true investor base.

## Clearing and settlement layers

Omnibus accounts often sit in a hierarchy. You own shares; your broker (Schwab) holds them in an omnibus account at its clearing firm; the clearing firm holds them in an omnibus account at a central securities depository. Each layer uses "street name" registration, a naming convention that identifies the intermediary rather than the beneficial owner.

This layering is necessary for settlement speed. When you buy a fund share, it must be paid for and transferred within a standard settlement period (typically one business day). If each purchase required updating the fund's registry with your name, it would be too slow. Instead, Schwab updates its internal system, notifies the clearing firm, and the clearing firm eventually updates the depository. The fund sees only its direct counterparty.

## Data gaps and shareholder reporting

Omnibus structures create information asymmetries. A fund cannot easily answer questions like "How many of my shareholders are women, or aged over 65, or based in California?" unless the omnibus holders voluntarily provide that data, which they often refuse to do citing competitive reasons.

This matters for marketing, product development, and compliance. A fund that wants to understand its shareholder base must ask brokers for details—and brokers, viewing shareholder data as proprietary, are reluctant. Some advisers pay for third-party research to infer shareholder demographics from public records, a costly and inexact workaround.

## Impact on investor relations and voting

For proxy votes, omnibus holders face a different problem. When a fund holds an election or proposes a fee change, it must conduct the vote through intermediaries. The fund sends proxy materials to Schwab; Schwab forwards them to its clients; clients vote; Schwab tabulates and sends totals back to the fund.

This process is slower and less certain than direct voting. Some investors don't see the proxy materials. Voting participation rates are lower in omnibus structures than in direct-registered accounts. This weakens shareholder engagement and makes fund governance more insular.

## Regulatory pressures and evolution

In recent years, regulators and shareholder advocates have called for more transparency. Rule changes requiring better beneficial ownership disclosure have been proposed but not fully implemented. Blockchain and distributed ledger technology have raised hopes for more granular ownership records, though adoption remains nascent.

For now, omnibus accounts remain the industry standard. They persist because they are cheap and convenient for brokers and funds, even if they diminish investor privacy and shareholder voice. A small number of investors choose to register shares directly in their own names (avoiding the broker intermediary), but most accept the trade-off of convenience for anonymity.

## See also

<div class="wiki-seealso">

### Closely related

- [Mutual Fund](/mutual-fund/) — the fund entity that sees only the omnibus holder
- [Broker](/broker/) — typically the omnibus account holder
- [Custodian](/custodian/) — another common omnibus account holder for institutional funds
- Street Name Registration — the naming convention used in omnibus accounts
- [Share Buyback](/share-buyback/) — an example of a shareholder action affected by omnibus structure

### Wider context

- [Fund Prospectus](/fund-prospectus/) — proxy voting and shareholder disclosure rules detailed here
- [Securities and Exchange Commission](/securities-and-exchange-commission/) — regulates omnibus account practices
- [Redemption Rights](/redemption-rights-equity/) — redemptions processed through the omnibus holder
- [Net Asset Value](/net-asset-value/) — calculated on the fund's total shares, including omnibus holdings

</div>
