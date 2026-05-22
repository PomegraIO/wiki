---
title: "ADR Issuance"
description: "Process of creating American Depositary Receipts from foreign shares, enabling US investors to trade foreign stocks."
keywords:
  - adr issuance
  - american depositary receipt
  - adr creation
  - depository program
---

*An **ADR issuance** is the process by which a foreign company, working with a US bank (the depository), converts its home-market shares into ADRs — receipts representing ownership of the underlying foreign shares. When the shares are deposited with a foreign custodian, the US depository bank issues ADRs in return. This allows US investors to buy and sell the foreign stock on US exchanges without dealing with foreign custody, currency conversion, or trading mechanics.*

<aside class="wiki-infobox">

| Factor | Detail |
|--------|--------|
| **Underlying Asset** | Ordinary shares of a foreign company |
| **US Depository** | Bank authorized by the company (typically BNY Mellon, JPMorgan, Citibank) |
| **Depository Ratio** | Number of foreign shares per ADR (e.g., 1 ADR = 5 ordinary shares) |
| **Listing Venue** | [NYSE](/wiki/new-york-stock-exchange/), NASDAQ, OTC Pink Markets |
| **Dividend Reinvestment** | Depositary converts foreign dividends to USD |
| **Voting Rights** | ADR holders have voting rights (if depository passes them through) |
| **Cost** | Depository fees (~$0.01–0.10 per ADR annually); pass-through currency conversion |
| **Levels** | Level I (OTC), Level II (NASDAQ/NYSE), Level III (with capital raise) |

</aside>

## The mechanics of ADR creation

A foreign company (e.g., Alibaba in China) decides to offer its shares to US investors. It enters into a depository agreement with a US bank (BNY Mellon, for instance). The agreement specifies the ratio: how many foreign shares equal one ADR.

**Step 1: Share deposit.** The foreign company or a major shareholder instructs its home-market custodian to deposit ordinary shares (e.g., 10 million shares) with BNY Mellon's representative in the home country.

**Step 2: ADR issuance.** BNY Mellon verifies receipt of the shares and issues ADRs to the depositor (or their designated US account). If the ratio is 1 ADR = 5 ordinary shares, 10 million shares become 2 million ADRs.

**Step 3: US listing.** The ADRs are listed on a US exchange or traded OTC. US investors buy and sell ADRs as if they were US stocks, in dollars, on US market hours.

**Step 4: Ongoing custody.** The underlying ordinary shares remain on deposit with the custodian in the home country. BNY Mellon acts as intermediary, collecting dividends, voting proxies, and handling corporate actions.

## ADR ratios and pricing

The depository ratio is chosen to create an economically meaningful share price. If Alibaba's share price in Hong Kong is 100 HKD (~$13 USD), the depository might set the ratio at 1 ADR = 8 ordinary shares, resulting in an ADR price of ~$100. This avoids a fractional or very low US price, which some investors find less attractive.

If the foreign share price changes dramatically (e.g., due to a [stock split](/wiki/stock-split/) or [reverse split](/wiki/reverse-stock-split/) in the home market), the depository may adjust the ratio to maintain a reasonable ADR price. These adjustments require shareholder approval in some jurisdictions.

## Types of ADRs: Levels I, II, and III

**Level I (Unsponsored, OTC):** Typically created by a broker or investor without the foreign company's involvement. The company does not participate in governance. Level I ADRs are traded on the [OTC pink markets](/wiki/otc-pink/) and have minimal disclosure requirements. They are illiquid and subject to lower regulatory standards.

**Level II (Sponsored, NASDAQ/NYSE):** Created with the foreign company's explicit sponsorship and cooperation. The company is subject to [SEC](/wiki/securities-and-exchange-commission/) reporting requirements similar to US domestic companies (annual [10-K](/wiki/10-k/), quarterly [10-Q](/wiki/10-q/)). Level II ADRs are more liquid and attract larger institutional investors. The company does not raise new capital (unlike Level III).

**Level III (Sponsored with capital raise):** Combines Level II listing with a US [public offering](/wiki/initial-public-offering/) where the company raises new capital by issuing ADRs. This requires full [SEC registration](/wiki/sec-registration-statement/), [IPO](/wiki/initial-public-offering/) roadshow, and [prospectus](/wiki/fund-prospectus/). Level III is the most onerous but also the most prestigious, attracting large institutional investors and Wall Street research coverage.

## Dividends and currency conversion

A Level II or III ADR includes dividend reinvestment: when the foreign company pays a [dividend](/wiki/dividend/) in home-country currency, the depository receives it, converts it to US dollars (at a current exchange rate set by the depository or a forex provider), and distributes the dollar amount to ADR holders. The [dividend](/wiki/dividend-per-share/) per ADR is adjusted proportionately to the depository ratio.

Dividend processing creates a lag (typically 1–2 months from payment date to US distribution) and currency conversion spreads are built into the process. A shareholder can see the conversion rate on the dividend statement.

## Voting rights and shareholder communication

ADR holders have the right to vote on shareholder matters (board elections, [merger](/wiki/merger/) approval, etc.), but they must exercise voting through the depository. The depository collects voting instructions from ADR holders and submits them to the foreign company's registrar or voting agent.

This creates a logistical burden: ADR holders must return voting forms to the depository within a tight window, and not all ADR holders actively vote. Major institutional holders often directly exercise voting power via their relationship with the foreign company or proxy advisors.

## Currency and exchange rate risk

Holding an ADR exposes the investor to the foreign [currency](/wiki/currency-pair/) risk. An ADR denominated in dollars does not eliminate the underlying currency risk; the ADR price reflects both the home-market stock price and the [exchange rate](/wiki/foreign-exchange-risk-bonds/). A US investor who buys a Chinese ADR is implicitly long the Chinese yuan.

Some investors hedge this currency exposure using [currency forwards](/wiki/fx-forward/) or [options](/wiki/currency-option/); others accept it as part of the international investment strategy.

## Administrative and regulatory compliance

The foreign company must maintain a depository agreement and comply with US reporting requirements if the ADR is Level II or III. This includes:

- Annual [10-K](/wiki/10-k/) and quarterly [10-Q](/wiki/10-q/) filings with the [SEC](/wiki/securities-and-exchange-commission/).
- [Sarbanes-Oxley](/wiki/sarbanes-oxley-act/) [internal control](/wiki/internal-control-assessment/) compliance ([Section 404](/wiki/sarbanes-oxley-act/)).
- [Listing](/wiki/exchange-listing-requirements/) standards of the exchange (NASDAQ, NYSE).
- Proxy statement ([Schedule 14A](/wiki/proxy-statement/)) filing for annual meetings.

These requirements impose significant compliance costs and legal burdens on the foreign company, which is why many only pursue Level I ADRs or remain unlisted.

## Advantages for foreign companies

- **US capital access:** Can raise capital from US public investors without establishing a US subsidiary.
- **Liquidity:** US market depth provides better liquidity than home-market shares alone.
- **Currency and investor diversification:** Access to USD-denominated capital and internationally diversified shareholder base.
- **Employee equity plans:** Can more easily grant [stock options](/wiki/employee-stock-options/) to US employees using ADR shares.

## Disadvantages and risks

- **Disclosure burden:** US regulatory compliance is expensive and time-consuming.
- **Dual listing complexity:** Managing both home-market and US shareholder bases; two dividend calendars; two governance processes.
- **Currency volatility:** [Exchange rate](/wiki/foreign-exchange-risk-bonds/) swings affect returns and stock price in USD terms.
- **Depository fees:** Annual per-ADR fees charged by the depository bank (typically $0.01–0.10).

## Market dynamics: sponsored vs. unsponsored

Most major ADRs are Level II or III (sponsored). Unsponsored Level I ADRs exist but are less common and trade with wider [bid-ask spreads](/wiki/bid-ask-spread/). The [SEC](/wiki/securities-and-exchange-commission/) has considered tightening rules on unsponsored ADRs due to investor protection concerns, but they remain legal and available.

<div class="wiki-seealso">

### Closely related
- [American Depositary Receipt](/wiki/adr/) — general ADR entry
- [ADR Trading](/wiki/adr-trading/) — secondary market mechanics
- [Initial Public Offering](/wiki/initial-public-offering/) — capital raise via Level III ADR
- [Depository Trust Company](/wiki/depository-trust-company/) — central depository
- [Currency Risk](/wiki/foreign-exchange-risk-bonds/) — FX exposure in ADRs

### Wider context
- [SEC Regulation](/wiki/securities-and-exchange-commission/) — oversight of Level II and III
- [Sarbanes-Oxley](/wiki/sarbanes-oxley-act/) — compliance requirement
- [Exchange Listing Requirements](/wiki/exchange-listing-requirements/) — listing standards
- [Dividend Reinvestment](/wiki/dividend-reinvestment-plan/) — currency conversion in ADRs
- [International Equity](/wiki/international-etf/) — ADRs as vehicles for foreign exposure

</div>
