# Company autolinking — method & rollout

How the company profiles under `content/companies/` go from ~1 in-body
cross-link (just the `10-K`) to a richly interlinked page, without editing any
file by hand.

## The problem

Each `content/companies/<letter>/<ticker>-stock.md` was hand-written, but the
writers rarely linked the financial concepts they mentioned. A typical page
carried a single cross-link — the `10-K` — so the prose read as an isolated
island, and the only "related" navigation was the right-rail *Sister entries*
widget, which shows the same alphabetically-first companies on every page. The
result looked templatish and cheap.

The wiki already has **~2,500 concept entries** (`balance sheet`, `free cash
flow`, `recession`, `operating margin`, `network effect`, …). Company prose is
full of those exact phrases. They simply weren't linked.

## The method

`scripts/autolink_companies.py` scans each company's prose and links the first
occurrence of any phrase that matches an existing concept entry's title.

1. **Dictionary** — built at runtime from every `content/**/*.md` that is *not*
   a company page. Each entry contributes its front-matter `title` (minus any
   trailing parenthetical) mapped to its filename slug. A plural variant is
   added for each phrase. A small hand-curated `SYNONYMS` map catches common
   surface forms (`annual report → 10-k`, `market cap → market-capitalization`).
   ~4,300 phrase variants over ~2,500 valid slugs.

2. **Precision gates**
   - **Multi-word titles** are admitted wholesale — they are specific enough to
     be unambiguous (`cash flow statement`, `bid-ask spread`).
   - **Single-word titles** are *excluded by default* (too ambiguous: "lead",
     "gold", "alpha", "spread") and only re-admitted from a curated
     `KEEP_SINGLES` set of unambiguous finance terms (`amortization`,
     `goodwill`, `ebitda`, `dividend`, `merger`, …).
   - `STOP_SLUGS` drops a few generic targets (`stock`, `share`, `company`).
   - Longest phrase wins at each position, so `cash flow statement` beats
     `cash flow`.

3. **Surgical insertion** — before matching, the body is masked so links are
   *never* injected into: the `<aside>` infobox, any HTML tag, existing
   markdown links/images, fenced or inline code, bare URLs, or any line that is
   a heading (`#`), blockquote (`>`), or table row (`|`). Front matter is split
   off and never touched.

4. **Safety invariants**
   - **Allowlist-safe by construction**: a link target is only ever a slug that
     exists on disk, so the script *cannot* create a broken link.
   - **One link per slug per file**, first occurrence only.
   - **Per-file cap** (`--cap`, default 12) keeps density tasteful.
   - **Idempotent**: a slug already linked in the file (in either `/slug/` or
     `/wiki/slug/` form) is skipped, so re-running adds nothing new.
   - Respects the "no templating company entries" rule — it enriches existing
     prose in place and adds **no** uniform block.

Emitted links use the bare root-absolute form `[text](/slug/)`, matching the
authoring guide. (`canonifyURLs` rewrites both `/slug/` and the legacy
`/wiki/slug/` form to the correct `https://pomegra.io/wiki/slug/`; the bare
form is canonical.)

## How it was tested on the `z` letter

```bash
cd repos/wiki

# 1. Preview — counts only, writes nothing
python scripts/autolink_companies.py --letter z --dry-run
#   -> would add 109 links across 29/30 files

# 2. Apply
python scripts/autolink_companies.py --letter z

# 3. Rebuild and validate every internal link on the z pages
"/c/Users/mk/bin/hugo.exe" --gc --minify
python scripts/validate_links.py --letter z
#   -> 778 internal links checked; the only broken ones are 7 PRE-EXISTING
#      hand-authored links (syK-stock, biopharmaceutical, clinical-stage,
#      two-sided-marketplace, panw-stock, pfe-stock, cik). The autolinker
#      introduced zero broken links.

# 4. Eyeball every added link for quality
git -c core.autocrlf=false diff content/companies/z/ \
  | grep -E '^\+' | grep -oE '\[[^]]+\]\(/[a-z0-9-]+/\)' | sort | uniq -c | sort -rn

# 5. Confirm idempotency — re-running must add nothing
python scripts/autolink_companies.py --letter z --dry-run   # -> 0
```

Manual spot-checks (`zm`, `zim`, `zts`, micro-caps) confirmed the links land in
natural prose positions and read correctly: `[recession](/recession/)`,
`[debt-to-equity ratios](/debt-to-equity-ratio/)` (plural → singular slug),
`[New York Stock Exchange](/new-york-stock-exchange/)`, etc. Thin micro-caps
correctly received only 1–2 links; substantive profiles received 5–8.

## Rolling out to every other letter

Do it letter-by-letter so each batch can be reviewed and reverted independently,
or all at once. Either way: **dry-run → apply → build → validate → review**.

```bash
cd repos/wiki

# --- one letter at a time (recommended for review) ---
python scripts/autolink_companies.py --letter a --dry-run
python scripts/autolink_companies.py --letter a
# ...repeat for b, c, … y

# --- or the whole corpus in one pass ---
python scripts/autolink_companies.py --all --dry-run     # preview totals
python scripts/autolink_companies.py --all               # apply

# Always finish with a build + validation sweep:
"/c/Users/mk/bin/hugo.exe" --gc --minify
python scripts/validate_links.py --all
```

`validate_links.py --all` reports every broken *page* link across the whole
company corpus. Because the autolinker can't create broken links, anything it
flags is a pre-existing hand-authored link worth fixing separately.

### Tuning

- `--cap N` raises/lowers the max links added per file (default 12).
- Edit `KEEP_SINGLES` to admit/deny single-word concepts.
- Edit `STOP_SLUGS` to blacklist a target.
- Edit `SYNONYMS` to map a surface form to a slug.

After editing the lists, re-run with `--dry-run` to preview before applying.
Because the script is idempotent, it is safe to re-run after tuning — it only
adds links that aren't already present.

## Files

- `scripts/autolink_companies.py` — the linker.
- `scripts/validate_links.py` — post-build link validator (page links only).
