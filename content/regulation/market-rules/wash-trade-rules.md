---
title: "Wash Trade Rules"
description: "Prohibition on simultaneous offsetting trades to create false volume, designed to prevent market manipulation."
keywords:
  - wash trade
  - market manipulation
  - false volume
  - offsetting positions
  - sec rule
  - market integrity
  - trading rules
---

*A **wash trade** is a transaction in which a trader simultaneously or nearly simultaneously buys and sells the same security, offsetting the position to create no net market exposure. The intent is typically to artificially inflate trading volume, create a false impression of market demand, or manipulate price. Wash trading is prohibited under securities law in the United States and most other jurisdictions.*

<aside class="wiki-infobox">

| Attribute | Value |
|-----------|-------|
| **Primary regulation** | Securities Exchange Act of 1934, Section 10(b) |
| **Rulemaking** | SEC Rule 10b-5, FINRA Rule 5210 |
| **Penalty** | Civil and criminal; bars, fines, disgorgement |
| **Detection** | Timing, counterparty, pricing, sequence |
| **Common schemes** | Pump-and-dump, volume stuffing, price painting |
| **Crypto gray area** | Evolving enforcement in unregulated markets |
| **Intent requirement** | Varies; some rules require scienter (intent) |

</aside>

## What constitutes wash trading

A wash trade involves:

1. **Same security**: The same stock, bond, option, or crypto token.
2. **No change in beneficial ownership**: The trader ends with the same position (or none) before and after.
3. **Offsetting transactions**: A buy is followed (or preceded) by a sale at roughly the same price.
4. **Motivation**: Intent to create false volume, mislead other traders, or manipulate price.

Example: A trader owns 10,000 shares of XYZ. To create the appearance of strong demand, the trader instructs a broker to buy 10,000 shares from an affiliated account at market price, then immediately sells the same 10,000 shares back to that account at the same price. Net effect: zero change in position, two large trades recorded, volume is inflated.

## Why it is prohibited

Wash trading harms market integrity by:

- **False volume**: Other traders see huge volume and infer demand or supply, making decisions on false information.
- **Price painting**: By executing many trades at progressively higher (or lower) prices, the trader creates a visual trend that has no fundamental basis.
- **Momentum bias**: Algorithmic traders and momentum investors may chase the false volume, buying when demand is fake, and suffering losses.
- **Volatility exaggeration**: False volume can exaggerate price moves and trigger stop-losses in other traders' positions.

The SEC's position is that markets depend on trust. If traders believe that volume reflects genuine demand, they can make informed decisions. False volume erodes that trust.

## Enforcement and detection

The SEC and FINRA monitor for wash trading through:

1. **Timing analysis**: Identical buy and sell within seconds or minutes to the same counterparty is a red flag.
2. **Price analysis**: Trades at identical or nearly identical prices (down to the penny) are unusual and suggest no real price negotiation.
3. **Account analysis**: Does the trader's account show consistent offsetting trades? Is there an affiliated account that is systematically the counterparty?
4. **Intent evidence**: Does the trader have communications (emails, messages) suggesting intent to manipulate?

Penalties include:
- **Disgorgement**: Return of profits (and sometimes treble damages).
- **Fines**: Civil penalties up to $5 million per violation or treble damages, whichever is greater.
- **Bars**: Prohibition from trading or working in securities.
- **Criminal prosecution**: In egregious cases, jail time (rare but possible).

A famous case: In 2020, the SEC charged a day trader with wash trading cryptocurrency on Kraken, artificially inflating trading volume. The trader was fined and barred.

## Related schemes: pump-and-dump and spoofing

**Pump-and-dump**: A trader (or group) buys a thinly traded stock, promotes it heavily (pumps), and when other traders buy on the hype, the instigators sell (dump) their shares at inflated prices. This often involves wash trading to create initial volume and momentum.

**Spoofing**: A trader places large orders with the intent to cancel them before execution, creating a false impression of demand or supply. The canceled orders never trade but move the market. The trader then profits when others react. This is distinct from wash trading (no actual offsetting trades) but similarly prohibited.

**Layering**: Similar to spoofing; multiple orders at different price levels, all intended to be canceled, create a false sense of market depth and may trigger algorithms to trade.

## Gray area: intent and mechanical matching

Not all buy-sell sequences are wash trades. A trader might:
- Buy 10,000 shares in the morning, then sell 10,000 shares in the afternoon when the outlook changes. This is a normal trade, not a wash.
- Have an automated system that buys and sells to maintain a hedge. If done in good faith (e.g., rebalancing a fund), it is generally allowed.

The key is **intent**. If the trader intends to create a false impression of volume or manipulate price, it is a wash trade. If the trader intends to genuinely adjust a position, it is not.

However, the SEC can infer intent from patterns. A trader who consistently buys and sells the same stock in a narrow time window, with offsetting prices, will face scrutiny—the pattern itself suggests intent.

## Crypto and unregulated markets

In cryptocurrency, wash trading is rampant on unregulated exchanges. A user with two accounts can trade with themselves to inflate volumes, deceive others about liquidity, and manipulate price. Many small crypto exchanges have engaged in this to attract users ("See our volume!").

Regulation is evolving. The CFTC and SEC are extending wash trade rules to crypto derivatives and spot trading. Compliance by major exchanges (Coinbase, Kraken) now includes monitoring for wash trading, though enforcement remains limited on fully unregulated platforms.

## Practical compliance

Brokers and market makers:
- Monitor their own clients' trading for patterns.
- Implement pre-trade surveillance (checking if a client's pending order looks like a wash trade).
- Report suspicious activity to regulators.
- Train traders on the rules.

Traders should:
- Avoid any intentional offsetting trades.
- Be aware that algorithmic systems might inadvertently create wash-trade-like patterns (e.g., market-making algorithms buying and selling rapidly). Some safe harbors exist for market makers and hedgers, but documentation is required.
- Understand that offshore accounts or trading through multiple brokers does not hide wash trades; surveillance systems track beneficial owners and find connections.

---

<div class="wiki-seealso">

### Closely related

- [Market Surveillance](/market-surveillance/) — Regulatory monitoring
- Spoofing — Related order-based manipulation
- [Pump and Dump](/boiler-room-fraud/) — Classic manipulation scheme
- Market Integrity — Foundational principle
- [Insider Trading](/insider-trading-law/) — Other market abuse form

### Wider context

- [SEC Enforcement](/sec-enforcement/) — Prosecution authority
- [FINRA](/finra/) — Self-regulatory body monitoring
- [Rule 10b-5](/rule-10b-5/) — Core anti-fraud rule
- [Securities Exchange Act of 1934](/securities-exchange-act-of-1934/) — Statutory framework
- [Market Maker Obligations](/market-maker-obligations/) — Related compliance rules

</div>
