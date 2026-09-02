---
title: "Share Warrants"
description: "Derivative instruments granting the holder the right to purchase shares of a company at a fixed exercise price on or before a maturity date."
---

*A share warrant is a security that gives the holder the right (but not the obligation) to purchase a specified number of [common stock](/wiki/common-stock/) shares from the company at a predetermined exercise price (strike) on or before an expiration date. Warrants are similar to [call options](/wiki/call-option/) but are issued directly by the company rather than traded on options exchanges, and they typically have longer durations (years rather than months). When a warrant is exercised, the company issues new shares, diluting existing shareholders.*

## Core features

**Exercise price (strike)**: The fixed price at which the warrant holder can buy the underlying shares. Often set 10–25% above the stock price at the time of warrant issuance.

**Maturity date (expiration)**: The date on which the warrant expires and becomes worthless if not exercised. Warrants can have durations of 5–10 years or more (much longer than standard options).

**Automatic or cash exercise**: The holder can exercise by paying cash (standard) or, in some structures, settle on a cashless basis—surrendering shares worth the intrinsic value instead of paying cash.

**Dilution**: Exercising a warrant creates new shares, diluting the ownership percentage and EPS of existing shareholders. The company receives the exercise price as cash proceeds.

**Transferability**: Warrants can be publicly traded (if listed on an exchange) or privately held, depending on the structure.

## Why companies issue warrants

**Sweetener in financing**: Companies issue warrants alongside debt or preferred stock to lower the coupon or make the investment more attractive. An investor might accept a 4% coupon on bonds if they also receive warrants to buy stock at a below-market price. The warrants provide upside exposure.

**Acquisition consideration**: In an acquisition, the buyer pays partly in cash and partly in warrants, deferring part of the consideration to the future (if the stock performs well).

**Employee incentive**: Some companies issue warrants to employees instead of (or alongside) [restricted shares](/wiki/restricted-shares/) or [options](/wiki/employee-stock-options/).

**Equity financing without immediate dilution**: Warrants defer dilution. If warrants are exercised, new capital flows in (the exercise price), allowing the company to grow without immediate equity issuance.

**Venture capital structures**: VCs sometimes receive warrants alongside preferred stock, providing both downside protection (preferred with liquidation preference) and upside leverage (warrants on common).

<aside class="wiki-infobox">
  <div class="wiki-infobox-title">Share Warrants — key facts</div>
  <table>
    <tr><th>Type</th><td>Derivative; right to purchase common shares at fixed price</td></tr>
    <tr><th>Issuer</th><td>The company itself, not an exchange</td></tr>
    <tr><th>Duration</th><td>Typically 5–10 years; much longer than traded options</td></tr>
    <tr><th>Exercise</th><td>Cash or cashless settlement; creates new shares</td></tr>
  </table>
</aside>

## Warrants vs. options

**[Options](/wiki/option/)** (call options specifically):

- Issued by exchanges, not the company.
- Trade on options markets (CBOE, etc.).
- Short duration (days to months, rarely years).
- Exercise typically settled in cash; if exercised, shares are provided by the exchange (not newly issued).
- Actively traded with transparent pricing.

**Warrants**:

- Issued directly by the company.
- Often held privately or listed on equity exchanges as standalone securities.
- Long duration (years).
- Exercise creates new shares, diluting existing equity.
- Less liquid; pricing may be opaque.

## Types of warrants

**American warrants**: Can be exercised at any time until expiration. Most common.

**European warrants**: Can only be exercised on the expiration date.

**Bermudian warrants**: Can be exercised on specific dates (e.g., quarterly).

**Cashless exercise warrants**: The holder can exercise without cash by surrendering shares worth the intrinsic value. Used when liquidity is uncertain.

**Equity-net settled warrants**: Upon exercise, the company issues the net shares (shares purchased minus the value of the warrant; no cash changes hands).

## Warrant pricing and valuation

Warrant value depends on:

1. **Intrinsic value**: Max(stock price - exercise price, 0). If the warrant is in-the-money (stock > strike), the intrinsic value is positive.
2. **Time value**: The value of the optionality (the right, but not obligation, to buy). Longer duration and higher volatility increase time value.
3. **Stock price volatility**: Higher volatility increases the warrant's value (wider range of potential outcomes, more upside leverage).
4. **Interest rates**: Higher rates slightly increase warrant value (the warrant allows the holder to defer capital commitment).
5. **Dividend yield**: Higher dividends reduce warrant value (the warrant holder does not receive dividends while holding the warrant, only when the underlying stock is acquired).

Warrants are typically priced using the Black-Scholes model (same as options), adjusting for the longer duration and accounting for dilution.

## Warrant exercise and dilution

When a warrant is exercised:

1. **Holder pays**: The strike price (say, $50 per share) per share purchased.
2. **Company issues**: New shares equal to the warrant's share count (say, 100 shares per warrant).
3. **New capital**: The company receives $5,000 (100 × $50).
4. **Dilution**: Existing shareholders' ownership percentage decreases (new shares are issued).

Example: Company has 1M shares outstanding. A warrant holder exercises warrants for 100K shares at $50/share. The company now has 1.1M shares (10% dilution) and receives $5M in cash.

## Warrant terms and covenants

Warrant agreements often include:

- **Adjustment provisions**: If the company pays a special dividend, splits stock, or undergoes a recapitalization, the exercise price or share count may adjust to protect warrant holders.
- **Call provisions**: Some warrants are callable by the company (similar to callable bonds), forcing early exercise.
- **Weighted-average anti-dilution**: If the company issues shares at a lower price (a down round), the warrant's exercise price adjusts downward to protect the warrant holder.
- **Make-whole provisions**: If the company is acquired, warrant holders may receive cash equal to the "make-whole" value instead of being forced to exercise.

## Real-world example: SPAC warrant

A special purpose acquisition company (SPAC) issues 10M common shares and 5M warrants to public investors. Each warrant entitles the holder to buy one share at $11.50 (the SPAC's initial public offering price is $10).

When the SPAC merges with an operating company ("the merger"), the warrants remain outstanding. If the merged company's stock rises to $20, the warrants are in-the-money by $8.50 per share ($20 - $11.50). Warrant holders exercise, buying shares at $11.50 and immediately owning $20 stock (a profit of $8.50 per warrant exercised).

If the stock falls to $8, the warrants expire worthless (out-of-the-money); holders lose their investment in the warrants.

## Warrant redemption and forced exercise

Some warrants include a "redemption call"—the company can force warrant holders to exercise or lose their warrants. For example:

- Warrant terms: "If the stock trades above $25 for 20 consecutive trading days, the company may redeem the warrants at $0.01 per warrant."
- Effect: Warrant holders must exercise (buy at the strike) or forfeit the warrant entirely. This limits the warrant holder's upside optionality and the duration of the leverage.

## Tax treatment

**For warrant holders**:

- Grant: Warrant grants to employees are taxed when they vest or are exercised.
- Exercise: No gain/loss upon exercise (it's simply the purchase of shares at the strike price).
- Sale of shares: When the underlying shares are later sold, capital gain/loss is recognized based on the basis (typically the strike price if exercised on the grant date) and the sale price.

**For the company**:

- Issuance: No expense; warrants are issued as part of equity financing.
- Exercise: The company receives the strike price as cash, a non-taxable capital transaction.
- Dilution: Warrant exercise may affect stock-based compensation accounting and EPS calculations but does not create a tax expense.

## Warrant vs. restricted shares vs. options

**Restricted shares**: Issued directly to the employee; the employee owns them (subject to vesting), receives dividends, and has voting rights. Upon exercise (vesting), there is an income tax on the fair market value.

**Options**: The employee has the right to buy shares at a strike. Upon exercise, the employee pays cash and receives shares. The economic outcome is similar to a warrant, but options typically have shorter duration.

**Warrants**: Like options, but issued by the company (not an exchange), with longer duration, and exercise creates new shares (vs. options, which are typically settled from existing or treasury shares).

## Historical note: Warrant explosion of 2020–2021

During the SPAC boom and COVID-era financing frenzy, millions of warrants were issued to retail investors in SPACs. Many were out-of-the-money upon expiration, and some warrant holders sued over disputed redemption mechanics. This highlighted the tail risks of holding warrants: long duration, leverage, and legal/structural complexity.

<div class="wiki-seealso">
<h2>See also</h2>
<h3>Closely related</h3>
<ul>
  <li><a href="/wiki/call-option/">Call Option</a> — the right to purchase shares, similar to a warrant but traded on options exchanges.</li>
  <li><a href="/wiki/employee-stock-options/">Employee Stock Options</a> — options granted to employees for equity compensation.</li>
  <li><a href="/wiki/restricted-shares/">Restricted Shares</a> — common shares issued with vesting restrictions.</li>
  <li><a href="/wiki/common-stock/">Common Stock</a> — the underlying shares that warrants grant the right to purchase.</li>
</ul>
<h3>Wider context</h3>
<ul>
  <li><a href="/wiki/special-purpose-acquisition-company/">Special Purpose Acquisition Company</a> — SPAC structure, common issuer of public warrants.</li>
  <li><a href="/wiki/leveraged-buyout/">Leveraged Buyout</a> — often uses warrants as part of the deal structure.</li>
  <li>Dilution — the impact of warrant exercise on existing shareholders' ownership and EPS.</li>
</ul>
</div>
