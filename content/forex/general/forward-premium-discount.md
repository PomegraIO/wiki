---
title: "Forward Premium and Discount"
description: "Whether a currency's forward rate is priced above or below spot, reflecting interest-rate differentials."
keywords:
  - forward premium
  - forward discount
  - interest rate parity
  - forward exchange rate
  - currency derivatives
image: "/svg/forex.svg"
---

*A currency's **forward rate**—its price for delivery 30, 90, or 180 days hence—rarely matches its spot rate today. When the forward rate is higher than spot, the currency is trading at a **forward premium**; when lower, a **forward discount**. This difference reflects the interest-rate gap between the two countries: investors will not lend at different rates in different currencies unless the expected exchange-rate movement compensates them.*

## The mechanics: arbitrage locks in the relationship

Suppose the US dollar trades at 1.10 dollars per euro on the spot market today. An American investor could lend dollars at 4% for one year. A European investor could lend euros at 2% for the same period. Which is the better deal?

If the euro-dollar rate does not change, the dollar earns 4% and the euro earns 2%. The dollar is clearly superior. But now consider an American who wants to invest in euros for one year without bearing exchange-rate risk. She could buy euros at 1.10, invest them at 2%, and lock in a forward sale of euros at a rate agreed today (a *forward contract*). If she insists on earning the same 4% she could get in dollars, the forward rate must be set so that her eventual return—including the forward exchange gain—equals 4%.

This is **interest-rate parity** in action. Arbitrage forces the forward rate to be higher than spot (the euro at a **forward premium**) by just enough to offset the interest-rate gap. In this example, the euro might trade forward at 1.1220 dollars per euro, promising the American investor enough appreciation (in dollar terms) to bring her total return to 4%.

By contrast, if the dollar interest rate were lower than the euro rate, the dollar would trade at a forward discount (forward rate lower than spot), because arbitrage would drive euros into the forward market to capture the higher euro rate.

## The signal: forward premiums hint at future spot rates

Investors sometimes use forward premia and discounts as rough guides to future exchange-rate movements. The reasoning is clean: if the euro is at a forward premium, perhaps the market is pricing in future euro appreciation. Conversely, a forward discount might signal expected depreciation.

But this inference is treacherous. The forward rate embeds two separate expectations: the market's expectation of the spot rate in the future, *and* the current interest-rate differential. A large forward premium could reflect a large interest-rate gap with no expected currency movement, or a small interest-rate gap with a large expected depreciation of the base currency, or any combination. The forward premium alone does not tell you what the market thinks the spot rate will be; you have to disentangle the interest-rate component.

Empirically, forward exchange rates have historically been poor predictors of future spot rates. The currency carry trade—borrowing in low-interest-rate currencies and investing in high-interest-rate currencies—has been profitable over long periods, which would not be true if forward rates accurately predicted future spot rates. This anomaly, called the "forward-premium puzzle," remains debated among economists and is a standing invitation to researchers.

## Why traders care about forward discounts and premiums

For corporate treasurers and traders, forward premiums and discounts are not abstract: they determine the cost of hedging. If a US exporter expects to receive 1 million euros in 90 days, she can lock in today's forward rate to eliminate currency risk. But the forward rate is typically different from the current spot rate, and that difference is driven by the interest-rate gap. A large forward discount means the exporter will receive fewer dollars when she converts the euros. That is the price of certainty.

Equally, speculators monitor forward premiums for arbitrage. If a currency's forward premium is unusually large relative to the interest-rate differential, it may offer a riskless profit (or a signal of market inefficiency or credit risk). Central banks and major financial institutions run automated systems to detect and exploit these gaps, which keeps the relationship tight in deep markets like the dollar-euro pair.

## The relationship breaks down at the extremes

Interest-rate parity holds well for major currencies in normal times because arbitrage is frictionless and capital moves freely. But it can break down. During currency crises, when confidence in a currency evaporates, the interest-rate differential may explode (the weak currency's rate soars, reflecting default risk) while the forward rate plummets (capital is fleeing). In 1998, during the Russian ruble crisis, interest rates on ruble assets were astronomical, but no forward rate could compensate for the risk of a sudden devaluation—because devaluation happened anyway, and arbitrage failed.

Conversely, when interest-rate differentials are tiny (as between the US and Canada, or within the eurozone), the forward premium or discount is small, and physical arbitrage becomes uneconomical. Transaction costs and bid-ask spreads widen relative to the premium, and the relationship becomes looser.

## See also

<div class="wiki-seealso">

### Closely related

- [Interest Rate](/interest-rate/) — the fundamental driver of forward premiums
- Spot Exchange Rate — the current rate to which forward premiums are compared
- [Forward Contract](/forward-contract/) — the derivative instrument that creates forward rates
- [Currency Risk](/currency-risk/) — what forward contracts hedge
- Currency Carry Trade — the strategy that exploits forward discounts and interest differentials

### Wider context

- Covered Interest Rate Parity — the principle that makes forward premiums predictable
- Exchange Rate — the price that forward contracts lock in
- Arbitrage — the mechanism that enforces the relationship
- [Optimum Currency Area](/optimum-currency-area/) — why countries with different interest rates are problematic in a currency union

</div>
