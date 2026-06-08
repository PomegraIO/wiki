---
title: "PSD2 Strong Customer Authentication Explained"
description: "How the EU's Payment Services Directive 2 requires two-factor authentication for online payments and which transactions are exempt."
keywords:
  - psd2 strong customer authentication explained
  - payment services directive 2 two factor authentication
  - sca exemptions psd2
  - psd2 compliance requirements
  - european payment regulation
image: "/svg/regulation.svg"
---

*The EU's Payment Services Directive 2 (PSD2) mandates that payment service providers use **strong customer authentication (SCA)** — a two-factor verification — for most online payment initiation and account access. The regulation, which went into effect in 2019, was designed to reduce payment fraud and protect consumers, but it created complexity for merchants and new exemptions for frictionless transactions. Understanding which payments require SCA and which do not is essential for compliance and user experience.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">PSD2 Strong Customer Authentication — key facts</div>

<img src="/svg/regulation.svg" alt="An abstract editorial mark for regulation." />

<div class="wiki-infobox-caption">SCA protects most payments but has been carved with exemptions to balance security and convenience.</div>

|   |   |
|---|---|
| **Requirement** | Two independent factors (knowledge, possession, biometric) for payment initiation and access |
| **Applies to** | Credit transfers, card payments, account access in the EU |
| **Effective date** | September 14, 2019 (with enforcement flexibility) |
| **Exemptions** | Low-value transactions, trusted beneficiaries, merchant-initiated, recurring, some exemptions per transaction |
| **Enforcement** | Payment Service Providers and banks; merchants must handle SCA requests via banks |

</aside>

## What PSD2 Strong Customer Authentication Is

PSD2 defines **strong customer authentication** as a two-step verification using at least two independent factors from three categories:

1. **Something you know:** A PIN, password, or security question.
2. **Something you have:** A physical device—a phone, card, or hardware token.
3. **Something you are:** Biometric data—fingerprint, face recognition, voice.

The two factors must be independent. Using a password and then a PIN, both typed on the same device, does not qualify because both are "something you know" and both are submitted via the same channel. But a password (knowledge) plus a one-time code sent to your phone (possession) does qualify.

The regulation applies to payment service providers (banks, fintech payment firms) across the EU. It covers:
- **Payment initiation:** When you authorize a credit transfer or card payment.
- **Account access:** When you log in to your online banking or payment app.
- **Recurring or card-present transactions:** With some exceptions (see below).

The stated goal was to reduce fraud. Before PSD2, a stolen card or login credential was enough to drain an account. With SCA, a thief needs both your password and your phone (or fingerprint), raising the bar.

## How SCA Works in Practice

When you initiate a payment in an EU bank's app or website, your bank triggers SCA. Here is the typical flow:

1. You enter payment details (payee, amount, account).
2. Your bank presents an SCA challenge. Usually, they send a one-time code (OTP) to your phone via SMS or a secure app push notification.
3. You receive the code, re-enter it into the payment interface, and confirm.
4. Your bank verifies the code and executes the payment.

For recurring transactions or card payments, the flow is similar but may be initiated by the merchant or payment processor rather than directly by you.

**Dynamic linking:** PSD2 also introduced "dynamic linking" for card-not-present transactions. When you use your card online, the merchant or payment processor can include the transaction amount and payee details in the authentication challenge. This prevents attackers from stealing your OTP for one transaction and using it for a different (larger) transaction. You verify the exact details before confirming.

## Key Exemptions and Carveouts

Strict SCA would grind ecommerce to a halt. A customer forced to authenticate every $5 coffee purchase would abandon their cart. Regulators and payment processors have carved out exemptions:

**Low-value transactions:** Transactions under €30 do not require SCA. This threshold was intended to keep frictionless purchasing alive. Merchants can exceed this threshold once per transaction or in aggregate (e.g., allow a customer to skip SCA up to €100 cumulative in a month), but the customer must re-authenticate periodically.

**Whitelisted or trusted beneficiaries:** Once you have authenticated a transfer to a given account or payee (e.g., your electricity company), subsequent transfers to that same account are often exempted from SCA. This incentivizes you to safelist trusted payees and reduces repetitive authentication.

**Merchant-initiated transactions:** Some recurring payments (subscriptions, installments) are initiated by the merchant, not the customer, and may be exempt if the merchant is PCI DSS compliant or the customer has pre-authorized the recurring mandate.

**Low-risk transactions:** Payment processors can use fraud scores to exempt low-risk transactions from SCA. If a transaction matches your historical pattern and your IP, location, and device are consistent, the provider may waive SCA. But if you deviate (e.g., login from a different country), SCA is triggered.

**Exemptions per provider:** Not all exemptions apply globally. Some banks and processors, especially in high-fraud environments, apply stricter rules. Conversely, others lean into exemptions to reduce friction.

## Regulatory Context and Enforcement

PSD2 took effect on September 14, 2019, but enforcement has been uneven. Initially, regulators granted flexibility as payment providers upgraded their systems. The 2020 pandemic and increased online shopping accelerated the rollout. By 2021, most EU banks had implemented SCA, though compliance gaps persisted.

Banks and fintech firms are responsible for enforcing SCA. **Merchants and payment processors** do not implement SCA themselves; instead, they integrate with their acquiring bank or payment gateway, which handles the SCA exchange on behalf of the customer's bank.

**3D Secure 2 (3DS2):** In practice, most online card payments flow through the 3D Secure protocol, which has been updated to align with PSD2. When you buy something online with a card, the merchant's payment processor sends your transaction to your card issuer, which challenges you with 3DS2/SCA. This happens behind the scenes; the merchant sees only a "success" or "failed authentication" response.

## Liability Shift and Fraud Protection

A key lever in PSD2: **liability shifting**. If a customer was not properly authenticated via SCA and fraud occurred, the merchant or payment processor, not the customer's bank, bears the loss. This incentivizes merchants and processors to implement SCA correctly.

Before PSD2, if someone stole your card number and made a fraudulent purchase, the bank might absorb the loss, and the customer was protected. Under PSD2, if the merchant did not execute proper SCA, the merchant bears the chargeback. This has motivated the adoption of 3DS2 and biometric authentication in consumer apps.

However, there are exceptions: if the customer was negligent (e.g., wrote their PIN on the card) or if the transaction fell under an exemption, the liability split may differ.

## Challenges and Industry Response

**Abandonment rates:** Early implementations of SCA caused checkout abandonment as customers struggled with SMS-based authentication. Mobile apps and push notifications have improved experience, but friction remains for customers who do not have data or reliable signal.

**Regional variation:** Different EU countries and banks have interpreted PSD2 exemptions differently, creating a patchwork. What triggers SCA in Germany might not in Italy, confusing merchants operating pan-European.

**Biometric and app-based auth:** To reduce friction, banks and fintech firms have shifted from SMS-based OTPs to app-based push notifications and biometric (fingerprint, face) authentication. These are faster and more secure but require users to update apps and adopt new habits.

**Open Banking:** PSD2 also opened the door to "open banking" and third-party payment initiation. Non-bank fintech firms can now initiate payments on behalf of customers (with SCA) and access aggregated account data. This has bred new ecosystems of payment apps and financial aggregators, though onboarding friction is still high.

## Practical Compliance for Merchants

If you operate an ecommerce site in the EU:

1. **Work with a PCI DSS-compliant payment processor.** They handle SCA integration with card schemes and acquiring banks. You do not build SCA yourself.
2. **Understand exemptions.** If you offer low-value transactions, subscriptions, or recurring payments, discuss exemption rules with your processor to reduce friction without breaking compliance.
3. **Test 3DS2 flows.** Ensure your checkout handles SCA challenges transparently and that failed authentications are handled gracefully (e.g., "authentication failed, please try again").
4. **Monitor cross-border rules.** If you serve customers outside the EU, they may not require SCA. Ensure your processor distinguishes between EU and non-EU transactions.

## See also

<div class="wiki-seealso">

### Closely related

- [Securities and Exchange Commission](/securities-and-exchange-commission/) — the US equivalent of financial regulation, though PSD2 is EU-focused
- Regulatory Landscape and Compliance — broader context for how regulations shape financial markets
- Payment Processing — the operational and technical infrastructure that implements SCA

### Wider context

- [Cryptocurrency Exchange](/cryptocurrency-exchange/) — operates in a different regulatory framework than traditional payment processors
- Fintech — the industry most affected by PSD2's open banking provisions and SCA requirements
- Cybersecurity in Finance — the threat model that PSD2 aims to address

</div>
