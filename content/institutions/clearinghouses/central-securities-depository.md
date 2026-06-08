---
title: "Central Securities Depository"
description: "Institution that immobilises securities and maintains the authoritative record of ownership, eliminating physical certificates."
keywords:
  - central securities depository
  - csd
  - securities immobilisation
  - dematerialisation
  - legal ownership record
  - settlement infrastructure
image: /svg/institutions.svg
---

*A **central securities depository** (CSD) is the infrastructure operator that takes custody of securities and maintains the definitive record of who owns them. Instead of paper certificates changing hands, CSDs immobilise securities in a vault and update ledgers to track beneficial owners — turning physical assets into account entries.*

The most obvious problem CSDs solve is physical logistics. Before electronic settlement, stock certificates were literally handed over during a sale, then forwarded to a registrar, cleared by hand, and re-registered. A high-volume market could choke on paper alone. CSDs eliminated that bottleneck by taking permanent custody of securities and issuing electronic claims on behalf of owners. You don't hold the actual share; you hold an account entry at the CSD that says you're entitled to the share.

## The shift from certificates to accounts

Historically, shareholding meant owning a piece of paper. You carried the certificate, endorsed it, passed it to a buyer. If the certificate was lost or stolen, you lost your claim. If it was damaged, reissuing it took weeks. By the 1960s, even with modest trading volumes, this system was breaking. The New York Stock Exchange famously closed on Wednesdays just to process the backlog of paper.

CSDs arose as the solution. Rather than moving certificates, they moved them once — into a vault — and then moved only electrons. A seller's account was debited; a buyer's was credited. The physical certificate never moved again. This is called **immobilisation**. In many jurisdictions, immobilised securities are legally fungible; the CSD doesn't segregate individual certificate serial numbers but instead treats all securities of the same type as a pool.

Some countries went further and abolished the physical certificates entirely — a process called **dematerialisation**. The security exists only as an electronic record. For intangible assets like equities or bonds, this is administratively simpler and eliminates the risk of loss or forgery.

## Legal ownership and the depository record

A critical feature of a CSD is that it maintains the authoritative ownership record. When you buy a share via a [broker](/broker/), your broker's account at the CSD is credited. If you ask for a statement of your holdings, you're receiving a certified copy of the CSD's ledger entry for your broker's account, which your broker then allocates to you in its own records.

This architecture introduces a layer of indirection. You are not the direct owner of the share in the CSD's books; you are the beneficial owner—the person with economic rights—but your name may not appear in the CSD's records at all. Instead, your broker holds the shares in its name (or a [custodian](/custodian/)'s name) as nominee. This arrangement speeds up settlement because the actual owner need not be updated on every trade; only the nominee account holder is.

Many CSDs distinguish between **immobilised** securities (physical certificate locked away) and **dematerialised** ones (no certificate exists at all). The legal effect is similar—both become account entries—but dematerialised securities have no physical claim outstanding. Corporations issue them directly in electronic form.

## Settlement and linkage with clearing

CSDs operate in tandem with clearing houses (CCPs). A CCP nets trades; a CSD executes the settlement. Once a CCP has calculated who owes what, it instructs the CSD to move securities and the [central bank](/central-bank/) (or a payment system) to move cash. The two legs—asset and cash—are coordinated via [delivery versus payment](/delivery-versus-payment/) to ensure neither party bears settlement risk.

A CSD typically connects to at least one [real-time gross settlement](/real-time-gross-settlement/) (RTGS) system to ensure cash moves instantly when securities are transferred. This removes the window of time in which a buyer has securities but the seller hasn't yet received cash, or vice versa.

## Tiered participant structure

CSDs do not deal with every investor directly. Instead, they maintain accounts for a relatively small number of participants: [stockbrokers](/broker/), [custodians](/custodian/), banks, and other large institutional players. Each participant then maintains sub-accounts for its own clients. This tiering reflects both operational reality (CSDs cannot manage millions of individual investors) and legal structure (many jurisdictions require beneficial owners to operate through a licensed intermediary).

A single investor's beneficial claim may rest on a chain of ledger entries: the investor's account at a broker, the broker's account at a custodian, the custodian's account at the CSD. Aggregating and reconciling these chains is a routine but critical function.

## International settlement and links

For cross-border trades, multiple CSDs are involved. An American investor buying German shares would be buying through a broker that operates accounts at both a US CSD and a German CSD, or through an international custodian that does. [Delivery versus payment](/delivery-versus-payment/) becomes more complex in multi-CSD settlement because the two legs—securities in Germany, cash in dollars—must coordinate across time zones and systems.

Some CSDs operate **links** with foreign counterparts, establishing automatic settlement pathways. Others rely on custodians to manage the complexity. The Hague Securities Convention (2002) attempted to harmonise conflict-of-law rules around securities held in CSDs, making international settlement more predictable.

## Risk management and regulation

Because CSDs hold assets worth trillions of dollars, they are heavily regulated. The [International Organization of Securities Commissions](/iosco/) (IOSCO) sets standards for CSD risk management, including safeguarding, segregation of client assets, and operational resilience.

A CSD must manage several risks. **Operational risk** is paramount: a system outage could halt settlement for the entire market. **Custody risk**—the risk the CSD loses or misappropriates securities—is mitigated by strict segregation, insurance, and bankruptcy-remote structures. **Cyber risk** is increasingly material as settlement becomes more digital.

CSDs are also systemically important in most markets. A failure would cascade through the entire financial system. This means they face intensive regulatory oversight, stress testing, and often implicit or explicit government backing.

## See also

<div class="wiki-seealso">

### Closely related

- [Delivery Versus Payment](/delivery-versus-payment/) — how CSDs coordinate securities and cash legs to eliminate settlement risk
- [Central Bank](/central-bank/) — often operates or backstops the CSD and its linked RTGS system
- [Custodian](/custodian/) — financial intermediary that holds securities on your behalf, typically using a CSD
- Clearinghouse — nets trades before the CSD executes settlement
- [Real-Time Gross Settlement](/real-time-gross-settlement/) — payment system that CSDs use to move cash in sync with securities
- [Multilateral Netting](/multilateral-netting/) — how a CCP compresses settlement obligations before handing them to the CSD
- [Broker](/broker/) — uses the CSD to hold clients' securities in its name

### Wider context

- [Stock Market](/stock-market/) — public venue that relies on CSDs for settlement and ownership recording
- Securitisation — process that often results in a new security registered with a CSD
- Settlement Infrastructure — system of which the CSD is a core component
- [Market Risk](/market-risk/) — CSDs exist partly to isolate settlement and custody risk from price risk

</div>
