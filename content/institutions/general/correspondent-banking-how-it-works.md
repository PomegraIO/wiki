---
title: "Correspondent Banking: How It Works"
description: "Correspondent banking allows banks without local presence to route payments through a correspondent bank holding a nostro account on their behalf."
keywords:
  - correspondent banking
  - how correspondent banking works
  - nostro account
  - vostro account
  - cross-border payments
  - correspondent bank relationship
---

*When a bank in one country needs to execute a payment in another country where it has no branch, it uses **correspondent banking**—a relationship with a local bank that holds funds on its behalf and settles transactions. The account the correspondent holds is called a nostro; the correspondent's view of the same account is a vostro.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Correspondent Banking — Key Facts</div>

<img src="/svg/institutions.svg" alt="An abstract editorial mark for financial institutions." />

<div class="wiki-infobox-caption">The backbone of cross-border payments; enables global commerce without universal branch networks.</div>

|   |   |
|---|---|
| **Core relationship** | Sending bank ← → Correspondent bank |
| **Account held by correspondent** | Called a nostro (our money) from the sender's view |
| **Same account from correspondent** | Called a vostro (their money) from the correspondent's view |
| **Settlement currency** | Local currency of the correspondent's country |
| **Typical flow** | Payment instruction, debit nostro, credit beneficiary, settlement |

</aside>

## The Basic Structure

A **correspondent banking** relationship is a contractual arrangement between two banks: the sending bank (often called the originating bank) and the correspondent bank. The sending bank does not have a physical presence or [custodian](/custodian/) account in a particular country, so it cannot hold funds or directly execute payments there. The correspondent bank, situated in that country, maintains an account on behalf of the sending bank—the **nostro account**.

The term "nostro" is Italian for "ours." From the sending bank's perspective, the nostro account is *its* money, held by the correspondent for settlement purposes. From the correspondent bank's perspective, the same account is a "vostro" account—from "vostro," meaning "yours." The nomenclature highlights the two-sided nature of the relationship: one bank deposits, one bank safeguards.

The correspondent bank maintains the nostro account just as it would maintain a customer's deposit account. It tracks the balance, executes transactions, and pays interest (if applicable). The sending bank, in turn, maintains the relationship through deposit balances, fees, and a contractual service agreement specifying settlement terms, fees, and liability.

## How a Payment Flows

Imagine a U.S. bank needs to wire funds to a recipient in Singapore. The U.S. bank does not have a branch in Singapore and cannot directly credit a Singapore bank account. Here is how correspondent banking solves the problem:

1. **Payment instruction**: The U.S. bank receives a customer's payment order to send, say, $100,000 to a Singapore bank account.

2. **Nostro transfer**: The U.S. bank debits its customer's account and sends an electronic payment instruction to its correspondent bank in Singapore, asking it to credit the Singapore recipient's local bank account.

3. **Correspondent settlement**: The Singapore correspondent bank credits its own customer (the recipient's local bank) with the funds—drawn from the nostro account it maintains in Singapore dollars (or another settlement currency).

4. **Back-office reconciliation**: The correspondent bank confirms execution of the payment, and both banks reconcile their records. The U.S. bank's nostro balance declines; the Singapore correspondent's vostro liability (from its perspective) increases by an offsetting amount.

The entire process takes seconds to minutes for electronic transfers, though message delays and time-zone differences can extend settlement.

## Nostro and Vostro: The Mirror Relationship

The nostro and vostro are the same account, viewed from opposite sides. A more complex example clarifies:

- **Bank A** (in the U.S.) maintains a nostro account at **Bank B** (in the U.K.). From Bank A's perspective, this is "our money" held in London.
- From Bank B's perspective, the same account is a vostro account: "their money" held on Bank B's books.
- If Bank A deposits $1 million via electronic transfer, Bank B credits Bank A's nostro account with $1 million equivalent in pounds sterling. Bank B's balance sheet shows a liability (vostro payable to Bank A); Bank A's balance sheet shows an asset (nostro deposit at Bank B).
- When Bank A instructs Bank B to pay a third party in the U.K., Bank B debits the nostro/vostro account and credits the beneficiary's account, settling the payment.

The nostro/vostro terminology is essential for understanding correspondent banking flows because it prevents confusion over whose liability is whose. Without the distinction, bankers would easily lose track of whether a balance represents a deposit due *to* the foreign bank or *from* the foreign bank.

## Why Correspondent Banking Persists Despite Fragmentation

In an ideal world, every bank would maintain correspondent relationships with every other major bank in every major currency and jurisdiction. In practice, correspondent networks are selective and hierarchical. Large global banks (JPMorgan, Bank of America, HSBC) maintain thousands of correspondent relationships and serve as regional hubs. Smaller or regional banks maintain fewer relationships, often funneling payments through larger correspondent banks—a practice called "nested" correspondent banking.

This creates both efficiency and risk. Efficiency: payment volumes and infrastructure investment are concentrated among institutions best positioned to manage them. Risk: if a major correspondent bank fails or exits a jurisdiction, smaller banks dependent on it face disruption. During the 2008 financial crisis, several correspondent banks withdrew from emerging markets, cutting off smaller banks' access to international payments.

Also, **de-risking**—the practice of correspondent banks exiting relationships with certain client banks deemed higher-risk—has reduced access for financial institutions in some regions. Banks in jurisdictions with higher perceived [counterparty risk](/counterparty-risk/), sanctions concerns, or weak [capital adequacy](/capital-adequacy/) regulations have had correspondent relationships terminated, making cross-border payments expensive or impossible.

## Settlement and Funding

The correspondent bank does not extend unlimited credit to the sending bank; funds must be pre-deposited or committed. The sending bank maintains a balance in its nostro account proportional to its expected payment volume. This is costly: a nostro balance is an unproductive asset, not generating the [return on assets](/return-on-assets/) the sending bank might earn elsewhere. But it is necessary for operational efficiency.

Settlement occurs through multiple channels: wire transfers (SWIFT, FedWire in the U.S., CHIPS), automated clearing houses (ACH), or physical currency movements for large or specialized transactions. The correspondent bank's role is to translate instructions from the sending bank into local clearing house formats and ensure the beneficiary receives the credit.

## Fees and Economics

Correspondent banking is not free. The sending bank pays the correspondent bank:

- **Flat monthly fees** for maintaining the relationship and the nostro account
- **Per-transaction fees** for each payment processed
- **Spread fees** on currency conversion if the payment involves [foreign exchange](/currency-volatility/)
- **Charges for reconciliation, compliance, and reporting**

For a large bank executing thousands of payments monthly, these fees aggregate substantially. But they are typically lower than the cost of establishing and maintaining a branch in every jurisdiction.

## Regulatory and Compliance Burden

Correspondent banks have become frontline enforcers of [anti-money laundering](/securities-and-exchange-commission/) (AML) and sanctions compliance. They are required to perform due diligence on the sending bank, verify the legitimacy of beneficiaries, and screen payments against sanctions lists. This compliance burden has increased sharply since the 2001 PATRIOT Act, and international standards (FATF recommendations) have strengthened it further.

A correspondent bank that fails to detect illicit activity through its nostro accounts faces severe penalties and reputational risk. This has caused major banks to exit certain correspondent relationships, particularly with financial institutions in higher-risk jurisdictions or with weaker compliance infrastructure. The result is that some developing-country banks struggle to maintain U.S. dollar correspondent relationships, reducing their ability to execute cross-border payments for customers.

## The Future: CBDC and Alternative Networks

Central banks are exploring Central Bank Digital Currencies (CBDCs) and blockchain-based settlement networks that could eventually reduce reliance on correspondent banking. A CBDC would allow direct settlement between central banks and their respective banks without intermediary correspondent banks. However, CBDCs remain in pilot stages, and correspondent banking is entrenched in global payment flows.

Some private blockchain networks and stablecoins have proposed alternatives to correspondent banking, but regulatory uncertainty and operational immaturity have slowed adoption. Correspondent banking, despite its inefficiencies and costs, remains the backbone of cross-border payments for the foreseeable future.

## See also

<div class="wiki-seealso">

### Closely related

- [Custodian](/custodian/) — the fiduciary role of holding assets; correspondent banks perform a custodial function for nostro accounts
- [Counterparty Risk](/counterparty-risk/) — the risk that the correspondent bank fails to settle or defaults
- [Foreign Exchange](/currency-volatility/) — how correspondent banks manage currency conversion in payment flows
- [Wire Transfer](/securities-and-exchange-commission/) — the settlement mechanism correspondent banks use
- [Capital Adequacy](/capital-adequacy/) — regulatory capital that correspondent banks must maintain
- [Anti-Money Laundering](/securities-and-exchange-commission/) — compliance obligations correspondent banks enforce
- [Bank of America](/bank-of-america/), [JPMorgan Chase](/jpmorgan-chase/) — major correspondent banking hubs

### Wider context

- [Broker](/broker/) — institutions that rely on correspondent banking for settlement
- [Central Bank](/central-bank/) — actors designing future payment networks
- [Credit Risk](/credit-risk/) — the risk of counterparty failure in correspondent relationships
- [Liquidity Risk](/liquidity-risk/) — correspondent banking provides the liquidity to settle cross-border transactions

</div>
