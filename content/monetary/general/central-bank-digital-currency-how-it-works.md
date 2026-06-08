---
title: "Central Bank Digital Currency: How a CBDC Works"
description: "How central bank digital currencies work, their design choices—retail vs wholesale, account-based vs token-based—and how they differ from bank deposits and private stablecoins."
keywords:
  - central bank digital currency
  - cbdc design
  - token-based currency
  - account-based currency
  - digital money
  - cryptocurrency regulation
  - digital payment systems
image: /svg/monetary.svg
---

*A **central bank digital currency**, or CBDC, is money issued directly by a country's central bank in digital form. Unlike physical cash, a CBDC exists only as data; unlike private stablecoins, it carries the credit and safety of the issuing nation. How it works depends on a series of architectural choices—whether it targets consumers and businesses directly or settles transactions between banks, whether holdings live in identified accounts or anonymous tokens—that shape its efficiency, privacy, and systemic impact.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">CBDC — Key Design Axes</div>

<img src="/svg/monetary.svg" alt="An abstract editorial mark for monetary policy." />

<div class="wiki-infobox-caption">The architecture of a CBDC hinges on four core decisions that determine who uses it and how.</div>

|   |   |
|---|---|
| **Two main types** | Retail CBDC (public), Wholesale CBDC (banks only) |
| **Account model** | Account-based (tied to identity) vs. token-based (like cash) |
| **Technology** | Distributed ledger or centralized database |
| **Interest policy** | Can earn/pay interest, unlike physical cash |
| **Access layer** | Direct from central bank or through commercial banks |

</aside>

## What separates a CBDC from existing money

A CBDC is best understood by comparing it to the three other forms of money in your economy. Physical cash—coins and notes—is anonymous, can be held indefinitely, and bears no interest. [Commercial bank deposits](/accounts-receivable/) sit in a [commercial bank](/broker/), earn interest, and are insured up to a statutory limit. A [private stablecoin](/cryptocurrency-exchange/), issued by a company rather than a central bank, claims a backing asset (often dollars held in reserve) but relies on issuer solvency and regulatory forbearance.

A CBDC occupies a unique middle ground. It is the central bank's own liability, so it carries sovereign credit risk only—safer than any private stablecoin. It can be designed to earn interest (unlike cash or crypto), making it a genuine competitor to bank deposits. And, crucially, a CBDC lets the central bank bypass commercial banks entirely: individuals and firms can hold money directly at the central bank.

That last point is the most unsettling to existing financial architecture. Today, deposits at commercial banks are the lifeblood of the system; banks lend that money out to earn the spread between deposit rates and loan rates. A CBDC that attracts deposits away from banks could drain their funding sources—a risk central banks take seriously.

## Retail vs. wholesale architecture

Most discussions of CBDC divide them into two categories based on *who* can hold them.

**Retail CBDCs** are designed for public use—consumers, small businesses, anyone with a payment device and internet access. This is what most people imagine when they hear "digital dollar" or "digital euro." A retail CBDC would allow you to transfer money to another person as easily as sending an email, with the transaction settling directly at the central bank. It could eliminate the need for intermediary banks for simple payments.

**Wholesale CBDCs** are restricted to banks and other financial institutions. They settle interbank payments and securities trades with finality and speed. Many central banks have already piloted wholesale CBDCs—the U.S. Federal Reserve's FedNow service and similar schemes elsewhere operate in this space. A wholesale CBDC is less disruptive; it doesn't compete with retail banking but accelerates the plumbing beneath it.

Most developed nations considering CBDC for retail use have also acknowledged the deposit-draining risk. Their solutions: offer CBDC only through commercial banks (so the banks remain intermediaries), cap holdings per individual, or simply pay a lower interest rate on CBDC than on insured deposits.

## Account-based vs. token-based design

The second axis divides CBDCs by *how* a user proves ownership.

**Account-based CBDCs** tie each balance to an identity verified with the central bank. Money lives in a named account. Transactions are recorded, and the central bank knows who holds what. This design mirrors today's banking: it enables KYC/AML compliance, makes tax collection straightforward, and prevents anonymous hoarding. It is also less cash-like—you cannot hand over digital coins to someone else without the system knowing.

**Token-based CBDCs** mimic physical cash: you hold cryptographic tokens that you can transfer to another person without revealing your identity to the central bank. The token itself proves ownership, like a banknote. This preserves privacy and feels more like cash, but it complicates compliance—the central bank sees outflows but not destination—and invites regulatory tension (authorities worry about money laundering and tax evasion).

Most CBDC pilots lean toward account-based design, especially in democracies with strong AML regimes. But some jurisdictions—often those aiming to upgrade cash in developing markets—are experimenting with hybrid models: anonymous tokens for small transactions, identified accounts for large ones.

## Technology and settlement

A CBDC can run on a centralized ledger (a database owned entirely by the central bank) or a distributed ledger (a blockchain-like system where participants validate transactions). Neither is the "correct" choice; they trade off privacy, speed, and resilience differently.

A centralized ledger is simpler for the central bank to operate, audit, and control. It can process millions of transactions per second without the communication delays that plague blockchains. But it is a single point of failure; if the database is compromised or goes down, so does the payment system.

A distributed ledger can continue operating even if some participants are offline and can be easier to audit across parties. But it is slower, consumes more energy, and requires all participants to agree on the transaction log. Most tested CBDCs use centralized databases with distributed access layers—a hybrid that gives participants an interface to the central bank's ledger without requiring a global consensus mechanism.

## The interest-rate policy trap

Unlike cash, a CBDC can earn interest. The central bank simply sets a rate and applies it to all CBDC balances at regular intervals. This is powerful: during a deep recession, the central bank could make CBDC rates negative (you pay a fee to hold it), incentivizing you to spend or invest rather than hoard. This is nearly impossible with physical cash, which always earns zero.

But negative rates on widely held CBDC create a different problem. Instead of hoarding cash, people would move money into physical assets, foreign currencies, or cash withdrawal—and if cash is cheap, they would stuff mattresses. The central bank's ability to implement deeply negative rates in a crisis could be illusory.

## Why adoption has been slow

Most advanced economies have not rolled out a retail CBDC, despite years of research. The reasons are practical: existing payment systems are already fast and convenient, the deposit-flight risk is real, and the central bank's balance sheet would swell if CBDC replaced a significant fraction of commercial deposits. Political resistance from banks and privacy advocates also matters.

Some nations—China's digital yuan, the Caribbean's Sand Dollar—have deployed working retail CBDCs, usually in narrower use cases or with tight controls. The European Central Bank and Federal Reserve continue large-scale pilots but have set no launch dates.

## CBDC vs. stablecoins and cryptocurrency

A CBDC is not a [stablecoin](/cryptocurrency-exchange/). A stablecoin is a privately issued digital token that claims backing by a real asset (usually USD held in reserve). It depends on the private company's solvency and regulatory oversight; if the backing disappears, holders lose money. A CBDC is direct liability of the central bank, backed by the nation's entire financial system.

[Cryptocurrency](/cryptocurrency-exchange/), like Bitcoin or Ethereum, is decentralized, algorithmic, and not backed by any institution. A CBDC is centralized and backed by the sovereign.

The distinction matters for stability: a CBDC can be trusted the way you trust [Treasury bills](/treasury-bill/)—as a direct obligation of the state. A stablecoin is only as reliable as the company managing it and the regulators watching it. Cryptocurrency is trustless by design, but trust-less also means no recourse if something breaks.

## See also

<div class="wiki-seealso">

### Closely related

- [Monetary Policy](/monetary-policy/) — How central banks adjust money supply and interest rates
- [Federal Reserve](/federal-reserve/) — The U.S. central bank
- [European Central Bank](/european-central-bank/) — The eurozone's central bank
- [Cryptocurrency Exchange](/cryptocurrency-exchange/) — Where crypto and stablecoins trade
- [Blockchain Fundamentals](/blockchain-fundamentals/) — The distributed ledger technology underlying some CBDC proposals

### Wider context

- [Interest Rate](/interest-rate/) — The price of borrowing and the yield on savings
- Financial System — Banks, payments, and credit in context
- [Quantitative Easing](/quantitative-easing/) — When central banks inject money directly into the economy

</div>
