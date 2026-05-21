#!/usr/bin/env python3
"""The canonical taxonomy for content/.

The wiki is content/<category>/<sub-category>/<slug>.md. Hugo's permalink
rule (`:contentbasename`) ignores nesting — URLs stay /wiki/<slug>/ — so
the only purpose of sub-directories is filesystem ergonomics: at 10k+
entries, a single directory of 1k files is unworkable for git, IDEs,
agent prompts, and human review.

Sub-categories are matched against article filenames (slugs) via keyword
substring matching. The first sub-category whose `kw` list contains a
matching keyword wins. Entries that match nothing land in the
`general/` bucket of their category, which we keep small.

Targets reflect the steady-state size we're aiming for after the next
authoring sweep — used by `plan_new_entries.py` to compute the gap.
"""
from __future__ import annotations
from pathlib import Path

# ── taxonomy ────────────────────────────────────────────────────────────
# Format per category:
#   "category-slug": [
#     ("subcat-slug", target_count, ["keyword1", "keyword2", ...]),
#     ...
#     ("general", 10, []),    # MUST be the last bucket — catch-all
#   ]
#
# Keyword matching: a slug matches a sub-category if any keyword is a
# substring of the slug (after normalising hyphens). Match order = declared
# order, so put narrower buckets first.
TAXONOMY: dict[str, list[tuple[str, int, list[str]]]] = {
    "equity": [
        ("share-classes",      30, ["preferred", "common-stock", "share-class", "dual-class", "non-voting", "callable-preferred", "cumulative", "participating", "convertible-preferred"]),
        ("corporate-actions",  35, ["buyback", "repurchase", "split", "spin-off", "spinoff", "rights-offering", "tender", "dividend", "reverse-stock", "stock-dividend", "stock-split", "treasury-stock"]),
        ("employee-equity",    25, ["esop", "espp", "iso", "nqso", "rsu", "restricted-stock", "vesting", "cliff", "employee-stock", "option-grant"]),
        ("offerings",          30, ["ipo", "follow-on", "atm", "at-the-market", "pipe", "secondary-offering", "direct-listing", "spac", "lock-up", "lockup", "private-placement", "underwriter"]),
        ("depositary-receipts", 15, ["adr", "gdr", "sponsored", "depositary", "level-i", "level-ii", "level-iii"]),
        ("shareholder-rights", 20, ["shareholder", "proxy", "activism", "activist", "voting-rights", "golden-share", "founder-shares", "transfer-agent", "warrant"]),
        ("general",            15, []),
    ],
    "derivatives": [
        ("option-types",       30, ["american-option", "european-option", "asian-option", "bermudan-option", "barrier-option", "binary-option", "basket-option", "compound-option", "knock-in", "knock-out", "exotic-option"]),
        ("option-basics",      25, ["call-option", "put-option", "strike", "expiration", "at-the-money", "in-the-money", "out-of-the-money", "intrinsic-value", "time-value", "option-premium", "moneyness"]),
        ("option-strategies",  30, ["covered-call", "protective-put", "iron-condor", "iron-butterfly", "straddle", "strangle", "spread", "collar", "ratio", "calendar-spread", "vertical-spread"]),
        ("greeks",             15, ["delta", "gamma", "theta", "vega", "rho", "vanna", "charm", "vomma", "speed", "greeks"]),
        ("pricing-models",     20, ["black-scholes", "binomial", "monte-carlo", "finite-difference", "trinomial", "heston", "local-volatility", "implied-volatility", "historical-volatility", "volatility-smile", "volatility-surface", "volatility-swap"]),
        ("futures-forwards",   25, ["futures", "forward", "contango", "backwardation", "cost-of-carry", "basis", "open-interest", "margin", "mark-to-market", "settlement"]),
        ("swaps",              20, ["swap", "cds", "credit-default", "interest-rate-swap", "currency-swap", "total-return", "sofr", "libor", "swaption"]),
        ("general",            15, []),
    ],
    "fixed-income": [
        ("government-bonds",   30, ["treasury", "gilt", "bund", "jgb", "tips", "i-bond", "savings-bond", "sovereign"]),
        ("corporate-bonds",    25, ["corporate-bond", "investment-grade", "high-yield", "junk-bond", "convertible-bond", "callable-bond", "putable", "perpetual-bond", "covenant"]),
        ("municipal-bonds",    15, ["municipal", "general-obligation", "revenue-bond", "build-america", "amt-bond"]),
        ("structured-credit",  20, ["asset-backed", "mortgage-backed", "mbs", "cmbs", "clo", "cdo", "collateralized", "securitization", "tranche"]),
        ("money-market",       15, ["money-market", "commercial-paper", "certificate-of-deposit", "repo", "repurchase", "reverse-repo", "treasury-bill"]),
        ("credit-ratings",     10, ["credit-rating", "rating-agency", "investment-grade", "default-rate"]),
        ("bond-math",          25, ["duration", "convexity", "yield-to-maturity", "yield-to-call", "current-yield", "coupon", "par-value", "zero-coupon", "accrued-interest", "credit-spread", "option-adjusted"]),
        ("yield-curve",        15, ["yield-curve", "term-structure", "inversion", "twist", "butterfly", "bootstrap", "spot-rate", "forward-rate"]),
        ("general",            10, []),
    ],
    "derivatives-skip": [],  # placeholder so duplicate keys don't collide
    "funds": [
        ("etfs",               40, ["etf", "exchange-traded", "authorized-participant", "creation-redemption", "tracking-error", "expense-ratio", "premium-discount", "bid-ask"]),
        ("mutual-funds",       20, ["mutual-fund", "open-end-fund", "closed-end-fund", "interval-fund", "no-load", "load-fund"]),
        ("hedge-funds",        20, ["hedge-fund", "long-short", "market-neutral", "global-macro", "merger-arbitrage", "managed-futures", "event-driven"]),
        ("private-equity",     15, ["private-equity", "leveraged-buyout", "venture-capital", "growth-equity", "distressed", "secondaries-fund"]),
        ("specialty-funds",    20, ["target-date", "lifecycle", "balanced-fund", "asset-allocation-fund", "fund-of-funds", "money-market-fund", "bond-etf", "sector-etf", "factor-etf", "smart-beta-etf", "leveraged-etf", "inverse-etf", "thematic-etf", "frontier", "emerging-markets", "international-mutual"]),
        ("fund-economics",     15, ["expense-ratio", "management-fee", "performance-fee", "high-water-mark", "carried-interest", "two-and-twenty", "load"]),
        ("general",            10, []),
    ],
    "forex": [
        ("currency-pairs",     20, ["eur-usd", "usd-jpy", "gbp-usd", "usd-chf", "aud-usd", "majors", "minors", "cross-rate", "exotic-pair"]),
        ("fx-regimes",         15, ["pegged", "floating", "managed-float", "currency-board", "dollarization", "free-float", "crawling-peg"]),
        ("fx-derivatives",     15, ["fx-forward", "fx-future", "fx-option", "ndf", "non-deliverable", "currency-swap", "fx-swap"]),
        ("fx-mechanics",       20, ["bid-ask", "spread", "pip", "lot", "leverage", "carry-trade", "interest-rate-parity", "purchasing-power-parity", "balance-of-payments"]),
        ("reserve-currencies", 15, ["reserve-currency", "petrodollar", "eurodollar", "yen", "renminbi", "sdr", "special-drawing"]),
        ("intervention",       10, ["intervention", "plaza-accord", "louvre-accord", "swap-line", "central-bank-fx"]),
        ("general",            15, []),
    ],
    "commodities": [
        ("metals",             20, ["gold", "silver", "platinum", "palladium", "copper", "aluminum", "zinc", "nickel", "iron-ore", "rare-earth"]),
        ("energy",             20, ["crude-oil", "wti", "brent", "natural-gas", "lng", "gasoline", "heating-oil", "ethanol", "uranium", "coal"]),
        ("agriculture",        20, ["wheat", "corn", "soybean", "rice", "sugar", "coffee", "cocoa", "cotton", "lumber", "rubber", "orange-juice"]),
        ("livestock",          10, ["live-cattle", "feeder-cattle", "lean-hogs", "pork", "dairy"]),
        ("commodity-curves",   15, ["futures-curve", "contango", "backwardation", "carry", "spread", "spot", "convenience-yield"]),
        ("commodity-vehicles", 15, ["commodity-etf", "etn", "commodity-pool", "managed-futures-commodity", "commodity-index"]),
        ("general",            10, []),
    ],
    "macro": [
        ("output",             18, ["gdp", "real-gdp", "nominal-gdp", "output-gap", "potential-output", "industrial-production", "capacity-utilization"]),
        ("prices",             20, ["cpi", "ppi", "core-inflation", "headline-inflation", "deflation", "stagflation", "hyperinflation", "inflation-expectations", "breakeven", "pce"]),
        ("labor",              15, ["unemployment", "nonfarm-payroll", "labor-force", "participation-rate", "u-3", "u-6", "wage-growth", "jolts"]),
        ("business-cycle",     15, ["expansion", "recession", "depression", "trough", "peak", "leading-indicator", "coincident-indicator", "lagging-indicator", "nber"]),
        ("trade-bop",          12, ["trade-balance", "current-account", "capital-account", "balance-of-payments", "tariff", "remittance", "foreign-direct-investment"]),
        ("growth-theory",      15, ["solow", "endogenous-growth", "convergence", "total-factor-productivity", "real-business-cycle", "secular-stagnation", "demographic"]),
        ("general",            15, []),
    ],
    "monetary": [
        ("central-banks",      20, ["federal-reserve", "ecb", "bank-of-england", "bank-of-japan", "boj", "pboc", "swiss-national-bank", "fomc", "governing-council"]),
        ("policy-tools",       20, ["open-market", "discount-rate", "reserve-requirement", "iorb", "iorr", "repo-facility", "reverse-repo-facility", "quantitative-easing", "qe", "qt", "yield-curve-control", "forward-guidance", "operation-twist"]),
        ("money-supply",       12, ["m0", "m1", "m2", "m3", "monetary-base", "money-multiplier", "velocity-of-money"]),
        ("interest-rates",     18, ["policy-rate", "fed-funds-rate", "discount-rate", "prime-rate", "sofr-rate", "libor-rate", "natural-rate", "neutral-rate", "real-rate", "nominal-rate", "taylor-rule"]),
        ("currency",           10, ["currency-issuance", "seignorage", "dollarization", "currency-board", "gold-standard", "bretton-woods", "fiat-currency"]),
        ("frameworks",         10, ["inflation-targeting", "price-level-targeting", "ngdp-targeting", "dual-mandate", "monetarism", "mmt"]),
        ("general",            10, []),
    ],
    "fiscal": [
        ("budgets",            15, ["budget-deficit", "budget-surplus", "primary-balance", "structural-deficit", "automatic-stabilizer", "discretionary-spending", "mandatory-spending", "appropriations"]),
        ("government-debt",    18, ["sovereign-debt", "debt-to-gdp", "debt-ceiling", "treasury-issuance", "sovereign-default", "restructuring", "debt-sustainability"]),
        ("taxation-policy",    15, ["progressive-tax", "regressive-tax", "flat-tax", "vat", "sales-tax", "consumption-tax", "wealth-tax", "carbon-tax", "estate-tax"]),
        ("transfer-programs",  10, ["social-security", "medicare", "medicaid", "unemployment-insurance", "snap", "tanf"]),
        ("fiscal-multipliers", 12, ["multiplier", "crowding-out", "ricardian-equivalence", "balanced-budget-multiplier", "marginal-propensity"]),
        ("sovereign-default",  10, ["default", "haircut", "paris-club", "london-club", "imf-program", "world-bank-program", "credit-event"]),
        ("general",            10, []),
    ],
    "ratios": [
        ("valuation-ratios",   25, ["pe-ratio", "peg", "price-to-book", "price-to-sales", "price-to-cash-flow", "ev-ebitda", "ev-sales", "shiller-pe", "earnings-yield", "dividend-yield"]),
        ("profitability",      20, ["roi", "roe", "roa", "roic", "rota", "gross-margin", "operating-margin", "net-margin", "ebitda-margin", "pretax-margin"]),
        ("liquidity",          12, ["current-ratio", "quick-ratio", "cash-ratio", "operating-cash-flow-ratio", "defensive-interval"]),
        ("solvency-leverage",  18, ["debt-to-equity", "debt-to-assets", "debt-to-ebitda", "interest-coverage", "fixed-charge-coverage", "times-interest-earned", "altman-z"]),
        ("efficiency",         15, ["inventory-turnover", "receivables-turnover", "payables-turnover", "asset-turnover", "cash-conversion-cycle", "days-sales-outstanding", "days-payable-outstanding"]),
        ("market-risk",        12, ["beta", "alpha", "sharpe-ratio", "sortino-ratio", "treynor-ratio", "information-ratio", "calmar-ratio", "max-drawdown"]),
        ("general",            10, []),
    ],
    "accounting": [
        ("financial-statements", 12, ["balance-sheet", "income-statement", "cash-flow-statement", "stockholders-equity-statement", "comprehensive-income", "10-k", "10-q", "8-k"]),
        ("balance-sheet-items",  20, ["accounts-payable", "accounts-receivable", "inventory", "ppe", "goodwill", "intangible-asset", "deferred-tax-asset", "deferred-tax-liability", "accrued-liability", "prepaid", "contingent-liability"]),
        ("income-recognition",   12, ["revenue-recognition", "asc-606", "accrual-accounting", "cash-basis", "deferred-revenue", "matching-principle"]),
        ("cost-allocation",      15, ["depreciation", "accumulated-depreciation", "amortization", "depletion", "straight-line", "double-declining", "units-of-production", "macrs"]),
        ("standards-and-audit",  15, ["gaap", "ifrs", "fasb", "iasb", "pcaob", "audit-opinion", "going-concern", "sarbanes-oxley"]),
        ("special-topics",       15, ["lease-accounting", "asc-842", "operating-lease", "finance-lease", "stock-based-compensation", "asc-718", "purchase-accounting", "consolidation"]),
        ("general",              10, []),
    ],
    "strategies": [
        ("value-strategies",   18, ["value-investing", "deep-value", "garp", "dividend-investing", "dividend-aristocrats", "dividend-growth", "contrarian", "magic-formula", "net-net"]),
        ("growth-momentum",    15, ["growth-investing", "momentum-investing", "trend-following", "breakout", "swing-trading", "relative-strength"]),
        ("factor-investing",   18, ["factor-investing", "value-factor", "size-factor", "momentum-factor", "quality-factor", "low-volatility-factor", "profitability-factor", "investment-factor", "smart-beta"]),
        ("portfolio-construction", 18, ["asset-allocation", "diversification", "all-weather", "permanent-portfolio", "core-satellite", "lazy-portfolio", "three-fund", "60-40", "barbell", "bullet", "ladder"]),
        ("rebalancing-tactics", 12, ["asset-rebalancing", "calendar-rebalancing", "threshold-rebalancing", "tax-loss-harvesting", "tax-gain-harvesting", "lump-sum", "dollar-cost-averaging"]),
        ("quant-systematic",   15, ["quantitative-investing", "systematic-investing", "statistical-arbitrage", "pairs-trading", "mean-reversion", "merger-arbitrage", "capital-structure-arbitrage", "convertible-arbitrage"]),
        ("trading-styles",     12, ["day-trading", "scalping", "position-trading", "swing-trading", "high-frequency", "algorithmic"]),
        ("rotation",           10, ["sector-rotation", "geographic-rotation", "style-rotation", "capital-rotation", "macro-rotation"]),
        ("general",            10, []),
    ],
    "risk": [
        ("risk-types",         20, ["market-risk", "credit-risk", "liquidity-risk", "operational-risk", "counterparty-risk", "systemic-risk", "concentration-risk", "currency-risk", "country-risk", "interest-rate-risk", "model-risk", "legal-risk"]),
        ("risk-measurement",   18, ["var", "value-at-risk", "cvar", "expected-shortfall", "stress-testing", "scenario-analysis", "monte-carlo-var", "historical-var", "parametric-var", "beta-coefficient", "tracking-error"]),
        ("hedging",            15, ["delta-hedge", "gamma-hedge", "cross-hedge", "natural-hedge", "currency-hedge", "interest-rate-hedge", "portfolio-hedge", "tail-hedge"]),
        ("risk-management",    15, ["position-sizing", "stop-loss", "kelly-criterion", "fixed-fractional", "max-drawdown", "risk-budget", "risk-parity"]),
        ("regulatory-risk",    10, ["basel", "tier-1", "tier-2", "lcr", "nsfr", "ccar", "stress-test-regulatory"]),
        ("general",            10, []),
    ],
    "behavioral": [
        ("cognitive-biases",   20, ["anchoring", "confirmation", "hindsight", "availability", "representativeness", "ambiguity-aversion", "overconfidence", "framing", "endowment", "status-quo"]),
        ("loss-aversion",      12, ["loss-aversion", "prospect-theory", "disposition-effect", "house-money", "break-even-bias", "regret-aversion"]),
        ("herding-social",     10, ["herding", "informational-cascade", "groupthink", "fomo", "fear-of-missing-out", "social-proof"]),
        ("mental-accounting",  10, ["mental-accounting", "narrow-framing", "broad-framing", "earmarking", "bucketing"]),
        ("sentiment",          15, ["investor-sentiment", "vix", "fear-and-greed", "put-call-ratio", "aaii-sentiment", "consumer-confidence", "buffett-indicator"]),
        ("market-anomalies",   12, ["january-effect", "halloween-effect", "weekend-effect", "monday-effect", "size-effect", "low-volatility-anomaly", "post-earnings-drift"]),
        ("general",            10, []),
    ],
    "history": [
        ("crises",             18, ["great-depression", "1987-crash", "asian-financial-crisis", "russian-default", "ltcm", "dot-com-crash", "global-financial-crisis", "european-sovereign-debt", "covid-crash", "svb-collapse"]),
        ("bubbles",            12, ["tulip-mania", "south-sea-bubble", "japanese-asset-bubble", "dot-com-bubble", "housing-bubble", "crypto-bubble", "meme-stock"]),
        ("structural-shifts",  15, ["bretton-woods", "gold-standard", "nixon-shock", "big-bang", "deregulation", "glass-steagall-repeal", "high-frequency-emergence", "etf-emergence"]),
        ("famous-trades",      15, ["soros-pound", "big-short", "volkswagen-short-squeeze", "gamestop-squeeze", "long-term-capital", "metallgesellschaft", "kerviel", "barings"]),
        ("regulatory-events",  10, ["1929-crash-securities-act", "sec-creation", "investment-company-act", "ibond-creation", "sox", "dodd-frank-passage"]),
        ("general",            10, []),
    ],
    "people": [
        ("legendary-investors", 20, ["warren-buffett", "charlie-munger", "benjamin-graham", "peter-lynch", "john-templeton", "philip-fisher", "walter-schloss", "irving-kahn", "seth-klarman", "howard-marks"]),
        ("traders",            15, ["george-soros", "stanley-druckenmiller", "paul-tudor-jones", "jim-rogers", "michael-burry", "ray-dalio", "jesse-livermore", "jim-simons"]),
        ("economists",         15, ["milton-friedman", "john-maynard-keynes", "paul-samuelson", "robert-shiller", "eugene-fama", "kenneth-french", "robert-merton", "myron-scholes", "harry-markowitz", "william-sharpe"]),
        ("modern-thinkers",    15, ["nassim-taleb", "michael-mauboussin", "morgan-housel", "burton-malkiel", "jack-bogle", "david-swensen", "charley-ellis"]),
        ("activists-quants",   12, ["carl-icahn", "bill-ackman", "dan-loeb", "nelson-peltz", "paul-singer", "renaissance-technologies", "two-sigma", "citadel"]),
        ("general",            10, []),
    ],
    "regulation": [
        ("securities-laws",    18, ["securities-act-1933", "securities-exchange-act-1934", "investment-company-act", "investment-advisers-act", "regulation-d", "regulation-a", "regulation-cf", "regulation-s", "jobs-act", "sarbanes-oxley", "dodd-frank"]),
        ("regulators",         15, ["sec", "finra", "cftc", "occ", "fdic", "ncua", "fhfa", "msrb", "esma", "fca", "asic"]),
        ("market-rules",       15, ["regulation-nms", "regulation-sho", "regulation-ats", "best-execution", "rule-144", "rule-144a", "rule-10b5-1", "rule-415", "rule-701"]),
        ("aml-kyc",            10, ["kyc", "aml", "bsa", "fincen", "ofac", "patriot-act", "fatca", "crs"]),
        ("international",      12, ["mifid", "mifid-ii", "emir", "ucits", "aifmd", "psd2", "gdpr", "fatca-international"]),
        ("compliance",         10, ["compliance-officer", "sox-controls", "soc-2", "iso-27001", "form-adv", "form-pf", "form-13f"]),
        ("general",            10, []),
    ],
    "corporate": [
        ("mergers-acquisitions", 20, ["merger", "acquisition", "horizontal-merger", "vertical-merger", "conglomerate-merger", "tender-offer", "hostile-bid", "friendly-bid", "stock-merger", "cash-merger", "earnout"]),
        ("takeover-defenses",   12, ["poison-pill", "white-knight", "white-squire", "pacman-defense", "crown-jewel", "staggered-board", "supermajority", "shark-repellent"]),
        ("leveraged-buyouts",   12, ["leveraged-buyout", "lbo", "management-buyout", "club-deal", "going-private", "stub-equity", "dividend-recapitalization"]),
        ("governance",          18, ["board-of-directors", "lead-director", "audit-committee", "compensation-committee", "nominating-committee", "say-on-pay", "clawback", "fiduciary-duty", "duty-of-care", "duty-of-loyalty", "business-judgment"]),
        ("capital-policy",      15, ["dividend-policy", "buyback-policy", "capital-allocation", "spin-off", "split-off", "carve-out", "tracking-stock", "exchange-offer"]),
        ("activism",            10, ["activist-investor", "13d", "13g", "proxy-fight", "vote-no-campaign", "letter-campaign"]),
        ("general",             10, []),
    ],
    "personal-finance": [
        ("retirement-accounts", 20, ["401k", "403b", "457", "ira", "roth-ira", "sep-ira", "simple-ira", "thrift-savings", "tsp", "solo-401k", "rmd", "required-minimum"]),
        ("savings",             15, ["emergency-fund", "high-yield-savings", "certificate-of-deposit", "money-market-account", "savings-account", "529", "college-savings"]),
        ("budgeting",           15, ["50-30-20", "envelope-method", "zero-based-budget", "ynab", "expense-tracking", "fixed-expenses", "variable-expenses", "discretionary"]),
        ("credit-debt",         15, ["credit-score", "fico", "vantagescore", "credit-utilization", "credit-history", "secured-credit-card", "balance-transfer", "debt-snowball", "debt-avalanche"]),
        ("insurance",           18, ["term-life", "whole-life", "universal-life", "variable-life", "long-term-care", "disability-insurance", "umbrella-insurance", "health-insurance", "auto-insurance", "homeowners-insurance", "renters-insurance"]),
        ("homeownership",       15, ["mortgage", "fixed-rate-mortgage", "adjustable-rate-mortgage", "fha-loan", "va-loan", "jumbo-loan", "pmi", "escrow-account", "home-equity", "heloc"]),
        ("estate-planning",     10, ["will", "trust", "revocable-trust", "irrevocable-trust", "estate-tax", "gift-tax", "beneficiary-designation", "power-of-attorney"]),
        ("general",             10, []),
    ],
    "taxes": [
        ("capital-gains",       15, ["short-term-capital-gain", "long-term-capital-gain", "qualified-dividend", "ordinary-dividend", "cost-basis", "wash-sale", "tax-lot", "fifo", "lifo", "specific-id"]),
        ("retirement-tax",      10, ["traditional-401k", "roth-401k", "backdoor-roth", "mega-backdoor", "rmd-tax", "early-withdrawal-penalty", "in-service-distribution"]),
        ("investment-vehicles", 15, ["municipal-bond-tax", "treasury-tax", "tips-tax", "mlp-k1", "reit-tax", "etf-tax-efficiency", "mutual-fund-distribution", "qualified-opportunity-zone"]),
        ("real-estate-tax",     10, ["1031-exchange", "1031-like-kind", "primary-residence-exclusion", "depreciation-recapture", "qbi", "rental-property-tax"]),
        ("estate-gift-tax",     10, ["estate-tax-exemption", "gift-tax-exemption", "annual-exclusion", "step-up-basis", "carryover-basis"]),
        ("alternative-tax",     10, ["amt", "alternative-minimum-tax", "niit", "additional-medicare-tax", "kiddie-tax"]),
        ("forms",               12, ["1099-b", "1099-div", "1099-int", "1099-r", "5498", "schedule-d", "form-8949", "schedule-k1", "form-1040"]),
        ("general",             10, []),
    ],
    "real-estate": [
        ("residential",         15, ["primary-residence", "second-home", "vacation-home", "single-family", "multi-family", "condominium", "townhouse", "duplex"]),
        ("commercial",          15, ["office-building", "retail-real-estate", "industrial-real-estate", "warehouse", "data-center", "self-storage", "medical-office", "shopping-center", "strip-mall"]),
        ("mortgages",           18, ["fixed-rate", "adjustable-rate-mortgage", "interest-only", "balloon-payment", "fha-loan", "va-loan", "conventional-loan", "jumbo-loan", "non-conforming", "reverse-mortgage"]),
        ("reits",               12, ["equity-reit", "mortgage-reit", "hybrid-reit", "public-reit", "private-reit", "non-traded-reit", "office-reit", "residential-reit", "industrial-reit", "healthcare-reit"]),
        ("financing-investing", 15, ["cap-rate", "noi", "cash-on-cash", "irr-real-estate", "ltv", "dscr", "appraisal", "comparable-sales", "income-approach", "cost-approach"]),
        ("operations",          10, ["property-management", "lease", "tenant-improvement", "common-area", "triple-net", "modified-gross", "gross-lease"]),
        ("general",             10, []),
    ],
    "trading": [
        ("order-types",         18, ["market-order", "limit-order", "stop-order", "stop-limit", "trailing-stop", "fill-or-kill", "all-or-none", "iceberg", "midpoint-peg", "discretion"]),
        ("execution",           15, ["best-execution", "smart-order-router", "vwap", "twap", "implementation-shortfall", "arrival-price", "participation-rate", "dark-pool", "lit-venue"]),
        ("market-structure",    18, ["maker-taker", "payment-for-order-flow", "pfof", "internalization", "wholesaler", "designated-market-maker", "specialist", "high-frequency-trading", "co-location"]),
        ("settlement-clearing", 12, ["t-plus-1", "t-plus-2", "novation", "central-counterparty", "ccp", "dtcc", "occ", "settlement-fail", "buy-in"]),
        ("intraday-phenomena",  10, ["opening-auction", "closing-auction", "circuit-breaker", "limit-up-limit-down", "lulld", "trading-halt", "imbalance"]),
        ("trading-costs",       10, ["bid-ask-spread", "commission", "slippage", "market-impact", "implementation-shortfall", "exchange-fee", "sec-fee", "finra-taf"]),
        ("general",             10, []),
    ],
    "crypto": [
        ("major-chains",        15, ["bitcoin", "ethereum", "solana", "cardano", "polkadot", "avalanche", "cosmos", "tron", "polygon", "arbitrum", "optimism", "base"]),
        ("consensus",           10, ["proof-of-work", "proof-of-stake", "delegated-pos", "proof-of-authority", "byzantine-fault-tolerance", "finality", "nakamoto"]),
        ("tokens-instruments",  18, ["stablecoin", "usdc", "usdt", "dai", "wrapped-token", "wbtc", "weth", "governance-token", "utility-token", "security-token", "nft"]),
        ("defi",                18, ["uniswap", "automated-market-maker", "amm", "liquidity-pool", "impermanent-loss", "yield-farming", "lending-protocol", "aave", "compound-finance", "maker-dao", "synthetix"]),
        ("custody-trading",     12, ["self-custody", "hot-wallet", "cold-wallet", "hardware-wallet", "multisig", "centralized-exchange", "decentralized-exchange", "dex", "cex"]),
        ("scaling-tech",        12, ["layer-2", "rollup", "optimistic-rollup", "zk-rollup", "sidechain", "state-channel", "sharding", "bridge"]),
        ("crypto-tax-reg",      10, ["crypto-tax", "1099-da", "fbar-crypto", "form-8949-crypto", "wash-sale-crypto", "specific-id-crypto"]),
        ("general",             10, []),
    ],
    "technical-analysis": [
        ("candlesticks",        15, ["doji", "hammer", "shooting-star", "engulfing", "hanging-man", "morning-star", "evening-star", "harami", "marubozu", "three-white-soldiers", "three-black-crows"]),
        ("chart-patterns",      18, ["head-and-shoulders", "double-top", "double-bottom", "triple-top", "triple-bottom", "ascending-triangle", "descending-triangle", "symmetrical-triangle", "rectangle", "flag", "pennant", "cup-and-handle", "rounding-bottom"]),
        ("support-resistance",  10, ["support-level", "resistance-level", "trendline", "fibonacci-retracement", "fibonacci-extension", "pivot-point", "psychological-level"]),
        ("indicators-trend",    15, ["sma", "ema", "macd", "adx", "parabolic-sar", "ichimoku", "donchian-channel", "keltner-channel", "bollinger-band", "moving-average-ribbon"]),
        ("indicators-momentum", 12, ["rsi", "stochastic-oscillator", "williams-r", "cci", "commodity-channel-index", "momentum-oscillator", "roc-rate-of-change"]),
        ("volume-indicators",   10, ["obv", "on-balance-volume", "chaikin-money-flow", "accumulation-distribution", "vwap", "money-flow-index"]),
        ("market-breadth",      10, ["advance-decline", "ad-line", "mcclellan-oscillator", "new-highs-new-lows", "tick-trin", "percent-above-200dma"]),
        ("general",             10, []),
    ],
    "institutions": [
        ("exchanges",           15, ["nyse", "nasdaq", "lse", "tokyo-stock-exchange", "hong-kong-exchange", "shanghai-stock-exchange", "shenzhen-stock-exchange", "euronext", "deutsche-borse", "cboe", "cme"]),
        ("index-providers",     10, ["sp-global", "msci", "ftse-russell", "stoxx", "bloomberg-barclays", "ice-data", "wilshire-associates"]),
        ("rating-agencies",     10, ["sp-ratings", "moodys", "fitch", "dbrs", "morningstar-ratings", "kbra"]),
        ("clearinghouses",      12, ["dtcc", "nscc", "occ", "icc", "lch", "eurex-clearing", "japanese-securities-clearing", "cme-clearing"]),
        ("major-firms",         18, ["goldman-sachs", "morgan-stanley", "jpmorgan", "blackrock", "vanguard", "fidelity", "state-street", "schwab", "interactive-brokers", "citadel-securities", "virtu-financial", "two-sigma-securities"]),
        ("regulators",          10, ["nyse-regulation", "finra-firms", "iiroc", "fca-uk", "esma", "bis", "fsb"]),
        ("general",             10, []),
    ],
    "valuation": [
        ("dcf",                 18, ["dcf", "discounted-cash-flow", "free-cash-flow", "fcff", "fcfe", "wacc", "terminal-value", "gordon-growth", "perpetuity", "exit-multiple", "two-stage-dcf", "three-stage-dcf"]),
        ("multiples",           18, ["pe-multiple", "ev-ebitda", "ev-sales", "ev-ebit", "price-to-book", "price-to-cash-flow", "shiller-pe", "regression-multiples", "comparable-companies", "precedent-transactions"]),
        ("residual-income",     10, ["residual-income-model", "abnormal-earnings", "rim", "clean-surplus", "equity-charge"]),
        ("dividend-models",     10, ["dividend-discount", "gordon-growth-ddm", "two-stage-ddm", "h-model", "spot-yield-ddm"]),
        ("real-options",        10, ["real-option", "deferral-option", "expansion-option", "abandonment-option", "switching-option", "option-pricing-applied"]),
        ("private-company",     10, ["liquidity-discount", "minority-interest-discount", "control-premium", "build-up-method", "venture-capital-method"]),
        ("general",             10, []),
    ],
    "markets": [
        ("primary-vs-secondary", 10, ["primary-market", "secondary-market", "ipo-market", "follow-on-market", "private-placement-market", "rule-144-market"]),
        ("venues",              18, ["nyse-market", "nasdaq-market", "ats", "alternative-trading-system", "ecn", "electronic-communication-network", "dark-pool", "lit-market", "internalizer", "wholesale-market"]),
        ("market-types",        15, ["bull-market", "bear-market", "correction", "recovery", "sideways-market", "volatile-market", "trending-market", "breakout-market"]),
        ("indices",             15, ["sp-500", "dow-jones", "nasdaq-composite", "russell-2000", "ftse-100", "dax", "nikkei", "hang-seng", "msci-world", "msci-emerging"]),
        ("market-mechanics",    12, ["opening-bell", "closing-bell", "after-hours", "pre-market", "trading-day", "settlement-day", "ex-dividend-date", "record-date"]),
        ("global-markets",      12, ["us-equity-market", "european-equity-market", "asian-equity-market", "emerging-equity-market", "frontier-equity-market", "japan-equity-market"]),
        ("general",             10, []),
    ],
}

# Drop the placeholder duplicate-key entry.
del TAXONOMY["derivatives-skip"]


def category_for_slug(category: str, slug: str) -> str:
    """Return the sub-category slug for an article in `category` named `slug`.

    Match order is significant: the first matching keyword wins. The
    'general' bucket (declared last in each category) catches everything.
    """
    buckets = TAXONOMY.get(category, [("general", 999, [])])
    normalized = slug.lower()
    for subcat, _target, kws in buckets:
        for kw in kws:
            if kw in normalized:
                return subcat
    return "general"


def all_subcats(category: str) -> list[str]:
    """All sub-cats declared for a category, in order."""
    return [b[0] for b in TAXONOMY.get(category, [])]


def target_for(category: str, subcat: str) -> int:
    """Target count for a (category, subcat) — used by plan_new_entries.py."""
    for b in TAXONOMY.get(category, []):
        if b[0] == subcat:
            return b[1]
    return 0


if __name__ == "__main__":
    import sys
    # Smoke-test: report total target counts.
    total = sum(b[1] for cat in TAXONOMY for b in TAXONOMY[cat])
    cats = len(TAXONOMY)
    subcats = sum(len(TAXONOMY[c]) for c in TAXONOMY)
    print(f"taxonomy: {cats} categories, {subcats} sub-categories, target {total} entries total")
