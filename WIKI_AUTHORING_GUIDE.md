# Pomegra Wiki — authoring guide

The contract that every wiki entry is held to. Read this in full before writing or commissioning a new article. The exemplar to imitate is [`content/stock.md`](./content/stock.md) — open it in another tab and keep it there as you write.

---

## 1. What an entry is

A Pomegra Wiki entry is a single Markdown file at `content/<category>/<sub-category>/<slug>.md` that explains one finance-world concept — an instrument, a ratio, an institution, a phenomenon — to an intelligent general reader who arrived cold.

The directory structure is **organisational only**. Hugo's permalink rule maps every entry to `/wiki/<slug>/` regardless of how deeply it is nested — `content/derivatives/option-strategies/iron-condor.md` and `content/iron-condor.md` would both serve at `/wiki/iron-condor/`. So always pick the most natural sub-folder; URLs are stable. The canonical sub-category list lives in [`scripts/taxonomy.py`](./scripts/taxonomy.py). When in doubt, drop into the `general/` bucket for the category.

Each entry must:

- Stand on its own. Assume the reader has not read any other entry.
- Be plain-language. Define every jargon term the first time it appears.
- Cross-link generously to neighbouring entries (5–12 links per article).
- Read like a quality magazine. **Not** like a textbook, not like a chatbot, not like marketing copy.

Target length: **900–1300 words**. Substantial enough to be useful, short enough that the reader finishes.

---

## 2. The voice

Imitate a confident, slightly opinionated magazine editor. Concretely:

- **Commit to definitions.** "A stock is …" not "A stock can be thought of as …".
- **Use editorial flourishes.** "Spectacular or zero". "At the back of the queue". "The most-watched ratio in finance — and still routinely misunderstood." One per article, used sparingly, never forced.
- **Mark what is contested.** When a definition or convention is disputed, say so plainly — "Most economists use X; the NBER reserves Y."
- **Avoid hedging filler.** Cut "it's worth noting that", "essentially", "basically", "in many ways".
- **Use British or American English consistently** — the existing entries lean British (-ise, -our). Match what's already there.

### Things that must never appear

These are non-negotiable. They make the wiki look AI-generated and untrustworthy:

| Forbidden | Why |
|---|---|
| "Let's explore", "In this article we will", "We've covered", "In summary", "Hope this helps" | AI tells — a confident editor would never write these. |
| "It's worth noting that", "It is important to remember" | Filler that signals the author isn't sure the point matters. |
| "I think", "I believe", first-person opinion | The entry speaks for the wiki, not for a person. |
| "Scaffolded", "placeholder", "TODO", "Coming soon", "[Next article placeholder]" | Status language. Production-served content must read as finished. |
| Any model or engine name | We don't disclose tooling in the prose. |
| The literal visible word **"Mermaid"** | Diagram code fences ```mermaid are fine. Captions should say "Decision tree", "Flowchart", or have no caption. |

---

## 3. Article structure (mandatory)

Every entry must contain these elements, in this order:

### 3.1 Front matter

YAML between `---` delimiters. The minimum:

```yaml
---
title: "Earnings per share"
description: "A one-paragraph SEO description that doubles as the meta description and the social-card text."
keywords:
  - earnings per share
  - EPS
  - basic EPS
  - diluted EPS
  - EPS calculation
image: "https://images.unsplash.com/photo-XXXX?w=900&q=80"
---
```

Notes:
- **Do not set `slug:` or `url:`.** The URL is derived from the filename via the `[permalinks]` rule in `hugo.toml`. `earnings-per-share.md` always serves at `/earnings-per-share/`.
- `image:` is the hero image — used by Open Graph cards and the home page's featured-entry card. Lift the URL from your in-body `<img>` using `python scripts/extract_hero_image.py` after you've drafted the article.
- Avoid `weight:`. The wiki has no global ordering — entries surface via cross-links, A–Z, and search.

### 3.2 Lede

The first body paragraph, wrapped in markdown italics `*…*`. CSS auto-styles it as the article's lede.

```markdown
*A **stock** — also called a **share** or an **equity** — is a unit of ownership in a [public company](/public-company/). Each share represents a small, transferable slice of the company's profits, its voting power, and its residual value if it is ever sold or wound up.*
```

One paragraph. Two to four sentences. Names the thing, locates it among other things, gestures at why it matters. Bold-mark the entry's name and any synonyms on first mention.

### 3.3 Hatnote (optional but common)

A single italic disambiguation/redirect line under the lede:

```html
<div class="wiki-hatnote">

This entry is about the financial instrument. For the venue where stocks trade, see [stock exchange](/stock-exchange/); for the broader system, see [stock market](/stock-market/).

</div>
```

Use only when the entry's name is ambiguous or commonly confused with a sibling concept. Skip otherwise.

### 3.4 Infobox

Floats right on wide screens, full-width on narrow. Image at the top, caption, then a key-facts table. Template:

```html
<aside class="wiki-infobox">

<div class="wiki-infobox-title">Entry name — key facts</div>

<img src="https://images.unsplash.com/photo-XXXX?w=600&q=80" alt="Describe the image, not the topic." />

<div class="wiki-infobox-caption">A single editorial sentence about the image. Italics applied by CSS.</div>

|   |   |
|---|---|
| **What it is** | A unit of ownership in a company |
| **Also called** | Share, equity |
| **Issued by** | A [public company](/public-company/) |
| **Traded on** | A [stock exchange](/stock-exchange/) |
| **Holder is called** | Shareholder, stockholder |
| (4–9 rows total, customised per entry) | |

</aside>
```

The blank lines around the inner Markdown elements (`<div>...</div>`, the image, the table) are required — without them Goldmark won't parse them as Markdown.

### 3.5 Body

4–6 H2 sections of substantive prose. Each H2 is a real claim, not a label:

- ✅ `## What a share actually entitles you to`
- ✅ `## How a share gets its price`
- ✅ `## Risks worth knowing`
- ❌ `## Overview`
- ❌ `## Introduction`
- ❌ `## More information`

Inside each section, mix paragraphs, lists, occasional small tables, and occasional pull-quotes (`>` blockquotes — used for a single memorable line, not a wall of text). H3 subsections are allowed but optional.

### 3.6 See also

The closing block. Always present, always last.

```html
<div class="wiki-seealso">

### Closely related

- [Stock exchange](/stock-exchange/) — the venue where stocks change hands
- [Public company](/public-company/) — what issues a stock in the first place
- [Dividend](/dividend/) — the cash a stock pays out
- … 5–8 entries

### Wider context

- [Diversification](/diversification/) — why owning many stocks beats owning one
- [Asset allocation](/asset-allocation/) — how stocks fit into a portfolio
- … 3–5 entries

</div>
```

The CSS renders this as two columns. Each item is a link plus a one-line gloss — *not* a copy of the linked article's lede; rewrite it from the perspective of *this* article.

> Note: when authoring via Hugo's structured front-matter mode (`see_also:` / `wider_context:`), the layout produces the exact same DOM. Either form is valid; the inline-HTML form is what most entries use.

---

## 4. Cross-linking rules

Cross-linking is what makes the wiki feel like a wiki. The rules are strict because broken links are visible to every reader.

### 4.1 The allowlist

**A link target is valid if and only if a file with that filename exists in `content/`.** Before you ship an entry, run:

```bash
# All href targets used in the article:
grep -oE 'href="/[a-z-]+/"' content/your-article.md | sort -u

# Compare against what actually exists:
ls content/ | sed 's/.md$//' | sort -u
```

If a slug appears in the first list but not the second, the link is broken. Either:
- create the entry (if the topic deserves one), or
- delete the link (and reword the surrounding prose to read naturally without it).

**Never** invent a slug under the assumption that you'll add the article "soon". That has cost the Pomegra Learn library thousands of broken links in the past.

### 4.2 Link styling

Always use root-absolute paths with a trailing slash:

- ✅ `[stock exchange](/stock-exchange/)`
- ❌ `[stock exchange](/stock-exchange)` (Hugo serves with trailing slash; this form works but is inconsistent)
- ❌ `[stock exchange](stock-exchange)` / `[stock exchange](stock-exchange/)` (no leading slash: the browser resolves it *under the current article*, producing a crawlable 404 like `/wiki/ipo/stock-exchange/` — the single largest 404 source in Search Console)
- ❌ `[stock exchange](/equity/stock-exchange/)` / `[stock exchange](/markets/exchanges/stock-exchange/)` (the on-disk `content/` sub-directory is **not** part of the URL; `hugo.toml` flattens every entry to `/<slug>/`)
- ❌ `[stock exchange](/link/stock-exchange/)` (there is no `/link/` route; this was an authoring-tool artifact)
- ❌ `[stock exchange](stock-exchange.md)` / `[stock exchange](/stock-exchange.md)` (`.md` is a filename, not a URL — Hugo does not resolve it at this site's permalink settings)
- ❌ `[stock exchange](https://wiki.pomegra.io/stock-exchange/)` (breaks local dev)

`python3 scripts/check_links.py --strict` rejects every ❌ form above and runs in the Docker build, so a page with one of them cannot ship.

### 4.3 Density

- **Lede**: 1–3 cross-links.
- **Body sections**: 1–3 per paragraph, generally. Don't over-link the same term repeatedly — link the first salient occurrence, then plain-text thereafter.
- **Infobox key facts**: link concept terms.
- **See also**: 8–13 total links across both subgroups.

Total per article: **5–15 cross-links**, biased toward the lower end if the topic is narrow.

### 4.4 External links

- `https://pomegra.io` and `https://pomegra.io/learn` are allowed, max one each per article, used sparingly (typically only in About-style entries).
- Image hot-link domains: `https://images.unsplash.com/photo-…?w=900&q=80` is the standard. Add `rel="noopener"` if you ever add `target="_blank"` (currently we don't).
- Do **not** link to Wikipedia, Investopedia, etc. — the wiki is meant to be a self-contained reference.

---

## 5. Images

Every entry should have at least one image. The default placement is in the infobox; long articles may have one additional inline image mid-body.

### 5.1 Source

We use Unsplash hot-links because they are stable, free, and the [Unsplash licence](https://unsplash.com/license) explicitly permits this. URL shape:

```
https://images.unsplash.com/photo-{PHOTO_ID}?w={WIDTH}&q=80
```

- `w=900` for infobox
- `w=1200` for hero / featured-entry
- `q=80` is the JPEG quality. Don't go higher; it costs bandwidth and visible difference is negligible.

### 5.2 Picking a photo

The image should be *editorial*, not *decorative*. Concretely:

- ✅ A trading-floor photo for a stock-market entry.
- ✅ A photo of receipts for an inflation entry.
- ✅ A classical-architecture photo for a central-bank entry.
- ❌ Stock photos of "abstract success" — handshakes, suit-and-tie close-ups, hovering 3D coins.
- ❌ AI-generated illustrations of any kind.

If you can't find one good photo, leave the infobox without one; an honest empty space is better than a generic-looking filler.

### 5.3 Alt text and caption

- `alt=""` must describe the image (what it shows), **not** the article's topic. "A trading desk with three monitors showing red and green prices" — not "Stock market."
- The caption (rendered below the image) is the editorial line. One short sentence. Italics applied by CSS — don't double-italicise.

---

## 6. Writing checklist

Before opening the PR or marking an entry done, verify:

- [ ] Length is 900–1300 words.
- [ ] Front matter has `title`, `description`, `keywords` (4–10), `image`.
- [ ] Lede is one italicised paragraph that names the entry and locates it.
- [ ] Hatnote is present if and only if the topic is genuinely ambiguous.
- [ ] Infobox has image + caption + 4–9 key-facts rows.
- [ ] Body has 4–6 H2 sections, each a real claim.
- [ ] 5–15 cross-links, **every one** matching an existing `content/*.md` filename.
- [ ] See-also has 8–13 entries across two subgroups, with one-line glosses.
- [ ] No AI tells, no engine names, no placeholder language, no visible "Mermaid".
- [ ] `hugo --gc --minify` exits 0 with no warnings about the new file.
- [ ] You opened the rendered page in `hugo server` and skimmed it end-to-end.

---

## 7. Workflow for batch authoring (subagents)

When commissioning a batch of entries via subagents, the prompt **must** include:

1. The path to this guide.
2. The path to `content/stock.md` as the canonical exemplar to read first.
3. **The full cross-link allowlist** (filenames that exist in `content/`) — see the [memory](https://github.com/anthropics/...) on "Cross-link allowlist for batch agents". Without an explicit allowlist, agents fabricate plausible-but-broken slugs.
4. A per-article assignment: filename, title, one-line angle, exact Unsplash image URL, image caption. Do not ask the agent to pick the image.
5. Editorial rules from §2 above, repeated inline. Subagents do not retain context across runs.

The Haiku model is usually fine for this when constrained as above. Always spot-check at least one entry from each batch before merging.

---

## 8. When in doubt

Read `content/stock.md` one more time. It is the canonical exemplar; everything in this guide either describes or follows from it.

---

## 9. Company entries (`content/companies/`) — a deliberate exception

Company profiles (the `<ticker>-stock.md` files served at e.g. `/aapl-stock/`, indexed by **The Exchange** at `/companies/`) follow **different rules from concept entries.** The mandatory structure in §3 does **not** apply to them. Two principles govern instead:

1. **No template — ever.** Concept entries share one house structure on purpose; company entries must **not.** They were once all generated from a single skeleton (same lede → infobox → four fixed headings → see-also) and read as interchangeable. That is banned. Every company profile must be **hand-written from scratch** so it reads as though a different writer learned that specific business and wrote it fresh — distinct headings, distinct ordering, distinct shape. Do not reuse boilerplate sentences or carry phrasing between companies.

2. **Substantial, sized to the company.** These entries must be full, informative articles, not stubs — earned with real substance about the actual business, never padding:
   - Dormant shell / tiny micro-cap with little real operation: **~500–750 words.**
   - Ordinary operating company: **~900–1,300 words.**
   - Major, storied, or complex company (megacap, big bank, household brand): **~1,500–2,000 words.**

**Ingredients, not a checklist.** A strong company entry works through the substance that matters for *that* company — what it is and its sector (early), origin/history, how it makes money (segments, what's recurring), what makes it distinctive (moat, competition), pressures and risks, and how a reader would research it (10-K, what to watch). Draw from these as needed and arrange them however the company and the chosen shape call for. Never march through them in a fixed order, and never invent history, products, or figures to fill a section.

**The exemplar is `content/companies/a/aapl-stock.md` (Apple).** It sets the bar for depth, tone, and structure: crisp lede, a key-facts infobox, several substantial sections under distinct company-specific headings, a framed segment table, a natural "how to research it" close — all evergreen, plain-language. Match its quality; never copy its headings or sentences. (Concept entries still look to `content/stock.md`; company entries look to Apple.)

**Evergreen + accurate:** as everywhere, no live prices/market cap/P-E/revenue/headcount as hard numbers, no "as of <year>", scale only qualitatively — and write only what is true of the company.

### 9.1 Authoring workflow — one agent per company, hand-written, no exceptions

Company profiles are commissioned **one Haiku subagent per company, dispatched in parallel — never batched into one agent, and never written on the main thread.** This is a hard operational rule, not a preference, and there are no workarounds (the main thread orchestrates and verifies; it does not author company files).

- The operational brief every writer agent reads is **`_company_scaffold/_CONTRACT.md`**, generated by `_company_scaffold/make_contract.py`. Edit the Python (not the generated file) to change the brief, then re-run it to refresh the live cross-link allowlist. The contract carries the depth tiers, the ingredients list, the no-template rule, and the nine starting *shapes* (continuous essay, Q&A, field notes, infobox-led, pull-quote, segmented, origin-to-now, plain-talk, free choice) — the shape varies the structure; the depth rules fill it.
- Each dispatch gives one agent: the exact file path, company name, ticker, SEC CIK, and one assigned format number. The agent reads `_CONTRACT.md`, writes that one file, and sets `handwritten: true` in the front matter.
- `handwritten: true` is the resumability flag — it marks an entry as written to the current standard, so a sweep can find and re-do anything still missing it.
- Slugs are predefined and de-duplicated **before** the swarm (from SEC EDGAR's canonical ticker list); writers receive explicit, non-overlapping file lists. Never post-hoc dedup.

### 9.2 Company entry checklist

- [ ] Hand-written from scratch; shares **no** structure/boilerplate with other company entries.
- [ ] Length matches the company's tier (above); substance, not padding.
- [ ] Names what the company is and its sector early; covers the relevant ingredients in a company-specific order.
- [ ] Front matter has `title` (exact `Name (TICKER)`), `description` (150–200 chars, no HTML), `keywords` (4–8), and `handwritten: true`.
- [ ] Evergreen and accurate — no live figures, no invented facts.
- [ ] 4–10 cross-links, **every one** in the allowlist; no fabricated slugs.
- [ ] No AI tells, no placeholder language, no visible "Mermaid", no investment advice.
