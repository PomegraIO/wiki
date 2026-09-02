---
title: "Pass-Through Security"
description: "A securitized bond structured to pass cash flows (principal and interest) directly from underlying borrowers through to investors, proportionally and without recourse."
---

*A pass-through security is the simplest form of securitization. Mortgages generate monthly payments; instead of the bank keeping the money, it passes it through to investors. A mortgage-backed security is typically a pass-through—investors receive monthly distributions of principal and interest proportional to their share. Unlike a bond that returns principal at maturity, a pass-through investor receives a stream of principal repayments as borrowers repay, refinance, or default.*

## The mechanism: principal and interest pass directly

In a pass-through, the issuer (often a bank or agency) pools mortgages, issues certificates to investors, and each month distributes:

- Interest collected: $1.2 million (pooled mortgage payments at the stated coupons)
- Principal repaid: $800,000 (scheduled principal from mortgages plus prepayments minus defaults)
- Minus servicing fees: -$50,000

Each investor receives their pro-rata share. An investor holding $10 million of $100 million in certificates gets 10% of distributions: $122,000 in interest and $80,000 in principal that month.

This is fundamentally different from a traditional bond, which pays fixed interest every period and principal at maturity. A pass-through's principal stream is uncertain (it depends on borrower prepayments and defaults) and distributed throughout the certificate's life.

## Who issues pass-throughs?

In the U.S., mortgage pass-throughs are typically issued by:

- **Fannie Mae, Freddie Mac, and Ginnie Mae**: Issue agency pass-throughs backed by conforming mortgages, with implicit or explicit U.S. government backing.
- **Banks and mortgage companies**: Issue non-agency (private-label) pass-throughs without government backing; these are higher-yielding but carry full credit risk.
- **Foreign banks**: Issue pass-throughs in their home countries backed by mortgages, auto loans, or other collateral.

The collateral backing a pass-through can be mortgages, auto loans, credit card receivables, or any amortizing debt. The structure is the same: cash flows pass through proportionally.

## Key characteristics: uncertainty and reinvestment risk

Because pass-through principal is lumpy (concentrated prepayments in some months, sparse in others), investors face uncertainty about:

- **Weighted average life (WAL)**: How long the investor will hold the security. In a low-rate environment with high prepayment, WAL is short (2–3 years). In a high-rate environment with slow prepayment, WAL stretches (8–12 years).
- **Reinvestment risk**: When principal returns faster (due to prepayments), the investor must reinvest at prevailing rates. If rates have fallen, reinvestment returns are lower. If rates have risen, they are higher.
- **Convexity**: The negative convexity of pass-throughs is well-known. Investors pay up for pass-throughs when rates are high (low prepayment expected, long WAL) and sell when rates are low (high prepayment expected, short WAL). This timing mismatch creates losses.

An investor who buys a 3.5% mortgage pass-through at par when prevailing rates are 4% expects a 5-year WAL. If rates fall to 2.5%, prepayment accelerates, WAL compresses to 2 years, and she has invested capital in a 2-year security yielding 1.5% below market.

## Agency vs. non-agency pass-throughs

Agency pass-throughs (Fannie Mae, Freddie Mac, Ginnie Mae) carry implicit or explicit U.S. government backing. Investors receive principal and interest on time, even if borrowers default. The agencies are obligated to make whole.

This guarantee carries a price: agency pass-throughs trade at tighter spreads (lower yields). A 4% agency pass-through might yield 80 bp over Treasuries. A 4% non-agency pass-through, carrying full credit risk, might yield 200+ bp over Treasuries.

Non-agency pass-throughs are credit instruments. Investors must assess collateral quality and structure. Many non-agency issuers layer tranches on top of pass-throughs (or use more complex structures), but the base product—the pass-through—remains a simple cash-flow conduit.

## Weighted average coupon (WAC) and the spread game

Mortgage pass-throughs are characterized by their "weighted average coupon" (WAC), the average interest rate of the underlying mortgages. If a pool contains 50% mortgages at 4% and 50% at 4.5%, the WAC is 4.25%.

The pass-through security itself issues at a coupon (usually 0.5% lower than WAC) to account for servicing fees. A pool with 4% WAC might issue a 3.5% pass-through certificate. The 0.5% difference compensates the servicer (the bank that collects payments, handles delinquencies, and distributes to investors).

This coupon "pass-through" is why the security is called a pass-through. The investor gets nearly all of what borrowers pay; the servicer keeps a small slice.

## Adjustable-rate mortgage (ARM) pass-throughs

Some pass-throughs are backed by adjustable-rate mortgages (ARMs). These introduce additional complexity: the coupon of the pass-through resets periodically to reflect changes in the underlying ARM rates.

An ARM pass-through might have a floating coupon tied to SOFR + 2.5%, resetting monthly. As SOFR changes, the investor's coupon changes. This transfers interest-rate risk from the issuer to the investor (the investor bears the risk that rates rise and the coupon drops, or fall and the coupon rises).

ARM pass-throughs appeal to floating-rate investors (such as banks managing interest-rate mismatches) but are less popular with traditional bond investors.

## Principal-only (PO) and interest-only (IO) strips

Some pass-throughs are decomposed into components. The principal stream (all principal payments) is separated from the interest stream (all interest payments), and each is sold as a separate security:

- **Principal-only (PO) strips**: The investor receives only principal, no interest. POs have extreme prepayment sensitivity. When rates fall and mortgages prepay, POs perform spectacularly (principal arrives ahead of schedule). When rates rise and prepayment slows, POs perform poorly (principal is delayed).
- **Interest-only (IO) strips**: The investor receives only interest. IOs have inverse prepayment sensitivity. High prepayment (low rates) is bad for IO holders (less interest is collected as mortgages pay off). Low prepayment (high rates) is good.

PO and IO strips are used by sophisticated investors to take directional bets on prepayment (and thus interest rates) or to hedge portfolios. A investor long mortgages (benefiting from low prepayment) might buy IOs to hedge. An investor short mortgages might buy POs.

## Servicing and the importance of the servicer

The servicer is the intermediary between borrowers and investors. The servicer:

- Collects monthly payments from borrowers.
- Enforces payment discipline (sends delinquency notices, initiates foreclosures).
- Manages the float (holds borrower payments temporarily before distributing to investors).
- Ensures timely payment to investors (using its own funds if necessary to make whole in case of default or delay).

Servicing quality varies. A competent servicer minimizes delinquencies and prepares borrowers for alternatives to foreclosure (loan modifications). A poor servicer lets delinquencies mount and forecloses hastily. Pass-through investors, particularly in non-agency structures, pay attention to servicer identity and track record.

The servicing fee (typically 0.25–0.5%) is built into the coupon spread. If a mortgage yields 4% and the pass-through issues at 3.5%, 0.5% goes to servicing (and possibly a reserve account or the issuer's guarantee).

<div class="wiki-seealso">
<h2>See also</h2>
<h3>Closely related</h3>
<ul>
<li><a href="/wiki/mortgage-backed-security/">Mortgage-Backed Security</a> — the most common form of pass-through.</li>
<li><a href="/wiki/prepayment-risk/">Prepayment Risk</a> — the defining risk of pass-throughs.</li>
<li><a href="/wiki/securitization/">Securitization</a> — the process that creates pass-throughs.</li>
<li><a href="/wiki/asset-backed-security/">Asset-Backed Security</a> — non-mortgage pass-throughs.</li>
<li>Weighted Average Coupon — a key characteristic of pass-through pools.</li>
</ul>
<h3>Wider context</h3>
<ul>
<li>Fixed Income — the asset class pass-throughs belong to.</li>
<li><a href="/wiki/interest-only-strip/">Interest-Only Strip</a> — a derivative of pass-throughs.</li>
<li><a href="/wiki/principal-only-strip/">Principal-Only Strip</a> — another pass-through derivative.</li>
</ul>
</div>
