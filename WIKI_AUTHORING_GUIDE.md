# Pomegra Wiki — authoring guide

The contract that every wiki entry is held to. Read this in full before writing or commissioning a new article. The exemplar to imitate is [`content/stock.md`](./content/stock.md) — open it in another tab and keep it there as you write.

---

## 1. What an entry is

A Pomegra Wiki entry is a single Markdown file at `content/<slug>.md` that explains one finance-world concept — an instrument, a ratio, an institution, a phenomenon — to an intelligent general reader who arrived cold. Each entry must:

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
- ❌ `[stock exchange](stock-exchange.md)` (Hugo can resolve `.md` paths but it ties the prose to the file layout)
- ❌ `[stock exchange](https://wiki.pomegra.io/stock-exchange/)` (breaks local dev)

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
