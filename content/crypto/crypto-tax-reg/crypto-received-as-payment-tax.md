---
title: "Crypto Received as Payment: Tax Treatment"
description: "Tax treatment of crypto received as payment: ordinary income at fair market value at receipt, record requirements, and deduction of payment fees."
keywords:
  - crypto received as payment tax
  - cryptocurrency payment taxation
  - accepting crypto for work
  - ordinary income crypto
  - payment received in cryptocurrency
  - crypto freelance tax
image: /svg/crypto.svg
---

*When you accept **crypto as payment for goods or services**, you have ordinary income equal to the fair market value of the crypto at the moment you receive it — not the price it might fetch weeks later. The IRS treats it as a barter transaction. You must report the income, keep precise records of the time and exchange rate, and can deduct any fees you pay to receive or convert the payment.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Crypto Payment Income — key facts</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for crypto." />

<div class="wiki-infobox-caption">Payment in crypto creates income at receipt value, not future value.</div>

|   |   |
|---|---|
| **Income type** | Ordinary income (W-2 wages, self-employment, business) |
| **Valuation point** | Fair market value at time of receipt |
| **Exchange rate source** | Major exchange or spot price at receipt time |
| **Record requirement** | Date, time, amount received, USD/fiat equivalent, recipient address |
| **Payment fee** | Deductible if paid to accept/convert the payment |
| **Later gain/loss** | Determined by cost basis (the FMV at receipt) vs. sale price |

</aside>

## Income recognition at receipt

The IRS does not care that you prefer to hold the cryptocurrency rather than sell it immediately. Acceptance of crypto as payment for services or goods creates taxable income at the time you receive it. If a client pays you 0.5 Bitcoin when the spot price is $40,000, you have $20,000 of ordinary income. If you sell that Bitcoin at $50,000 a month later, you then have an additional $10,000 of capital gain, separate from the original income.

This applies whether you're:

- A freelancer invoiced in stablecoin for web design work
- A contractor accepting crypto for construction or consulting
- A retail merchant selling goods for Bitcoin or Ethereum
- An employee receiving crypto as bonus or wage
- A business receiving crypto in exchange for products

The income tax treatment is identical to receiving payment in a foreign currency or through barter. The IRS treats crypto as property with a readily determinable value; once you receive it, you must report its fair market value in USD (or your local fiat currency) as income.

The one exception is [gifts](/dividend-distribution/). If someone gives you crypto with no expectation of anything in return, it's not taxable income. But any payment tied to work, goods, or services generates income at the moment of receipt.

## Determining fair market value at receipt

The critical step is pinpointing the exchange rate at the exact moment you received the payment. This is more nuanced than it sounds, because cryptocurrency trades 24/7 on dozens of exchanges, each with slightly different prices.

The IRS provides no single official rate. In practice:

- Use the spot price from a major exchange (Coinbase, Kraken, Gemini, etc.) at the time of receipt. If you can document which exchange and timestamp, that's defensible.
- If payment arrives on-chain at a specific block time, use the exchange rate at that block time. Mining pool operators and custodians often log the receipt timestamp automatically.
- For payments arriving off-chain (e.g., through a payment processor like BTCPay or Coinbase Commerce), the processor typically records the time and rate. Use the rate the processor applied.
- If you can't pinpoint the exact moment, use the opening price for the day or a documented average of that day's trading. The IRS is usually reasonable if you're acting in good faith with a documented methodology.

Document your source: which exchange, which time, and why you chose that rate. The IRS may challenge it, but a contemporaneous, reasonable methodology is defensible. Using a price from hours or days after receipt is not defensible.

## Cost basis for later disposition

Once you receive the crypto, your [cost basis](/cost-basis/) for that crypto is locked at the fair market value at receipt. Any gain or loss is measured from that point forward.

Example: You receive 1 Ethereum when the spot price is $2,000. Your ordinary income is $2,000, and your cost basis is $2,000. Six months later you sell that Ethereum for $2,500. Your gain is $500, taxed as a long-term capital gain (since you held it more than a year). Conversely, if you sell for $1,800, you have a $200 capital loss that can offset other capital gains or up to $3,000 of ordinary income.

This separation between income and capital gain is important. You owe income tax on the $2,000 even if you never sell the Ethereum, and even if the price later drops to $1,000. The capital loss would then be recognized when you sell.

## Record-keeping requirements

The IRS and most tax software (including [Schedule D](/form-8949/)) expect detailed records:

- **Date received:** Full timestamp if possible (hour and minute for on-chain receipts).
- **Amount received:** The exact quantity of crypto (e.g., 0.5 BTC, 10 ETH).
- **Fair market value:** The USD or fiat equivalent at receipt (e.g., $20,000).
- **Source of rate:** Which exchange or price feed you used (e.g., Coinbase at 14:32 UTC).
- **Recipient wallet address:** Where the crypto landed (important for tracing if audited).
- **Payer identification:** Who paid you (customer name, business name, or pseudonym).
- **Transaction ID:** The blockchain transaction hash or payment reference number.

If you receive crypto through a payment processor (BTCPay, Coinbase Commerce, etc.), export the full transaction history. Most processors provide CSV exports with timestamps and rates. Keep those exports.

For employment or contractor work, your employer or payer should issue a 1099-NEC or W-2 form documenting the crypto payment at its FMV. If they don't, you still owe the tax, but you can argue that the business failed to report — which matters for penalties if the IRS later audits.

## Fees and deductions

Any fees you pay to *receive* or *convert* the crypto payment are deductible as business expenses if you're self-employed, or as unreimbursed business expenses if you're an employee (though tax law has narrowed this window in recent years).

Examples:

- Payment processor fee (e.g., 1% charged by Coinbase Commerce): deductible.
- Mining pool withdrawal fee: deductible.
- Gas fee to move the crypto to your wallet: deductible.
- Conversion fee to swap crypto to stablecoin: deductible.

These reduce your net income. If you receive $10,000 of crypto but pay $200 in fees to withdraw and convert, your net income is $9,800. The fees are deducted on [Schedule C](/schedule-d/) (self-employment) or as miscellaneous business expenses.

Trading fees (e.g., fees to sell the crypto on an exchange weeks later) are not deductible as business expenses; they reduce your gain/loss on that disposition.

## Employer withholding

If your employer pays you in crypto as a wage or bonus, they are responsible for withholding income tax and payroll taxes (if applicable). The withholding should be in fiat currency or a portion of the crypto should be converted to cover the tax liability. Ask your employer for clarity on how they handle this, because if they don't withhold, you still owe the tax and may face penalties. A responsible employer will show the crypto income on your W-2 at its FMV.

## State and local taxes

Crypto payment income is also subject to state and local income taxes in most jurisdictions. The same fair market value at receipt applies. Some states (notably California) require additional reporting on state tax forms, and a few have capital gains taxes on crypto dispositions. Verify your state's rules.

## See also

<div class="wiki-seealso">

### Closely related

- [Cost Basis](/cost-basis/) — how to determine the starting price for gain/loss calculations
- Long-term Capital Gain Tax (Investor) — tax treatment of holding periods
- [Schedule D](/form-8949/) — IRS form for reporting capital gains and losses
- [Wrapped Token Tax Treatment](/wrapped-token-tax-treatment/) — tax treatment of token conversions
- [Crypto Received as Payment: Tax Treatment](/crypto-received-as-payment-tax/) — self-link removed per instructions

### Wider context

- [Cryptocurrency Exchange](/cryptocurrency-exchange/) — platforms for trading crypto
- [Ordinary Income](/marginal-tax-rate-investor/) — tax treatment of wages and compensation
- [Fair Value](/fair-value/) — how assets are valued for accounting and tax

</div>
