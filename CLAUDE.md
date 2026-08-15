# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

`PomegraIO/wiki` — Pomegra's reader-friendly encyclopedia of the financial world. A static **Hugo** site that ships as a single Nginx-served directory. Each `content/*.md` file is one wiki entry. The site uses the Pomegra editorial design language (cream paper, Fraunces serif headings, Geist body, accent red) shared with `PomegraIO/learn`, but the *content shape* is wiki-style: every entry stands on its own and links generously to every neighbour.

It is the sibling project of `PomegraIO/learn`:
- **Learn** is a curriculum (chapter form, sequenced).
- **Wiki** is an encyclopedia (entry form, network-shaped).

## Why Hugo, and why it matters

Hugo was chosen explicitly so the wiki **scales to 10,000+ entries without ever becoming slow to build**. As of this writing, ~40 pages build in **~40 ms**. That headroom is the entire point — do not migrate to a Node-based static-site generator (Docusaurus, Next, Astro, etc.) without a very deliberate conversation, because they would re-introduce the multi-minute-build problem that motivated this stack.

Practical consequences:
- No `node_modules`, no `package.json`, no JS build pipeline. The toolchain is **one binary** (`hugo.exe`) plus optional Python for migration scripts.
- The whole asset pipeline (CSS minification + fingerprinting) is Hugo Pipes, not webpack. See `layouts/_default/baseof.html`.
- We rely on Hugo's templating, not JSX/MDX. Adding a "component" means a new partial in `layouts/partials/` or a shortcode in `layouts/shortcodes/` — not React.

## Commands

```bash
# Dev (with live reload). Port 1314 avoids clashing with /learn/'s 3000s.
# The wiki is served under /wiki/ in production, so dev must match:
hugo server --port 1314 --bind 127.0.0.1 \
            --baseURL "http://localhost:1314/wiki/" \
            --appendPort=false --disableFastRender
# Then open http://localhost:1314/wiki/

# Production build (output to public/)
hugo --gc --minify

# Inspect what got rendered
hugo list all
hugo list drafts
```

Hugo isn't on PATH on the build host. The installer at the moment lives at `C:\Users\mk\bin\hugo.exe` (Hugo Extended 0.161+). If you need to reinstall:
- Download `hugo_extended_<version>_windows-amd64.zip` from <https://github.com/gohugoio/hugo/releases>
- Unzip, place `hugo.exe` somewhere on PATH.

## Authoring conventions

The full editorial style is in [WIKI_AUTHORING_GUIDE.md](./WIKI_AUTHORING_GUIDE.md). Read that before writing or editing an entry. The very short version:

- One Markdown file per entry, at `content/<category>/<sub-category>/<slug>.md`. The slug is the URL — `content/derivatives/greeks/delta.md` serves at `/wiki/delta/`. Sub-directories are filesystem-only; Hugo's `:contentbasename` permalink rule ignores them.
- The canonical taxonomy of (category, sub-category) buckets is in [`scripts/taxonomy.py`](./scripts/taxonomy.py). `scripts/migrate_into_subdirs.py` is an idempotent classifier — re-run it any time after bulk imports.
- Front matter is minimal: `title`, `description`, `keywords`, and `image` (lifted from the body's first `<img>` by `scripts/extract_hero_image.py`).
- Each entry opens with an italic lede paragraph (markdown `*…*` on a single paragraph), optionally a hatnote, then an `<aside class="wiki-infobox">`, then 4–6 `##` sections, then a closing `<div class="wiki-seealso">` block.
- Cross-link **generously**. The "Cross-link allowlist" rule in the authoring guide must hold: only link to slugs that actually exist in `content/`. A wiki where 1% of links are broken feels broken everywhere.

## How permalinks work

`hugo.toml` sets:

```toml
[permalinks.page]
  '/**' = '/:contentbasename/'
```

This pins the URL to the filename, *not* the title. `etf.md` is always `/etf/`, never `/etf-exchange-traded-fund/`. This is what makes the cross-link allowlist trustworthy — slugs in markdown match filenames on disk one-to-one.

Do not change this rule lightly. If you do, every existing cross-link in every article breaks at once.

## Deployment: served under `/wiki/`

The wiki ships under `/wiki/` on the main pomegra.io site (sibling of `/learn/`).
Two settings in `hugo.toml` do the heavy lifting:

```toml
baseURL = 'https://pomegra.io/wiki/'
canonifyURLs = true
```

`canonifyURLs = true` is what makes the ~18k hardcoded markdown links like
`[Stock](/stock/)` resolve correctly. Without it, the rendered HTML would
emit `href="/stock/"` and the browser would 404 because the wiki isn't
mounted at the root. With it, Hugo rewrites every root-absolute URL in
content to include the baseURL — `href="https://pomegra.io/wiki/stock/"`.

Two consequences worth knowing:

1. **Use `relURL` over `absURL` for site-internal URLs in templates.**
   Hugo's `absURL` helper *strips* the baseURL path when the argument starts
   with `/` — `"/sitemap.xml" | absURL` returns `https://pomegra.io/sitemap.xml`,
   not `https://pomegra.io/wiki/sitemap.xml`. For places that genuinely need
   an absolute URL with the `/wiki/` prefix preserved (sitemap, OG image,
   JSON-LD), call the helper partial: `{{ partial "absolute-url.html" "/img/x.png" }}`.

2. **Always include the trailing `/` on cross-links.** Markdown like
   `[Stock](/stock)` (no trailing `/`) renders to `https://pomegra.io/wiki/stock`,
   which Nginx 301-redirects to `…/stock/`. The 301 works but wastes a round
   trip on every cross-link. `scripts/fix_link_slashes.py` is a one-shot sweep
   that adds the trailing slash to any `](/slug)` it finds — idempotent, run
   it after bulk content imports.

## SEO and analytics

Heavy SEO lives in `layouts/_default/baseof.html` and `layouts/partials/seo-jsonld.html`:
- Open Graph + Twitter Card on every page, OG image defaults to `static/img/og-default.png`
  (regenerated by `scripts/generate_og_image.py`).
- JSON-LD: Organization + WebSite + BreadcrumbList on every page; Article +
  DefinedTerm on entries; CollectionPage on the home. Each is emitted as a
  separate `<script type="application/ld+json">` block. **Always pipe through
  `safeJS` after `jsonify`** — without it Hugo treats `<script>` content as
  JS context and double-escapes the JSON into a quoted string, which Google's
  rich-results validator silently rejects.
- Sitemap is templated in `layouts/sitemap.xml` (priority/changefreq tweaks per
  page kind + image:image extension for hero SVGs).
- `layouts/robots.txt` sets the canonical sitemap URL and explicitly allows
  AI crawlers (GPTBot, Claude-Web, PerplexityBot, Google-Extended). The wiki
  is meant to be cited in AI answers.

Analytics is the same shared `analytics.pomegra.io` Umami instance that `/learn`
uses. Two pieces:
- The official tracker, loaded as a `<script defer>` from baseof.html with
  `data-website-id` set in `hugo.toml` `[params].umamiWebsiteId`. The wiki has
  its own website-id distinct from each learn book.
- `assets/js/wiki-events.js` is the Hugo-flavoured port of
  `learn/books/_shared/umami-events.js`. Same custom event taxonomy
  (scroll-depth, heartbeat, engagement-summary, reading-complete, theme-toggle,
  external-link-click, code-copy, etc.) plus wiki-specific events
  (`internal-link-click`, `cross-property-click`, `search-query`,
  `random-article`). The Docusaurus version is a `clientModule` driven by
  router lifecycle; this version is a single IIFE that starts on
  `DOMContentLoaded` and finalizes on `pagehide`.

## Ads

Google AdSense, driven entirely from `hugo.toml` `[params]` — three values, all
blankable to switch a piece off site-wide without touching a layout:

| Param | Effect |
|---|---|
| `googleAdsenseClient` | Publisher ID. Emits the `adsbygoogle.js` loader once in `<head>` (baseof.html) and gates every ad unit. Blank it and all ads vanish. |
| `googleAdsenseSlotInArticleTop` | Slot for the ad after an entry's first `##` section. |
| `googleAdsenseSlotInArticleMid` | Slot for the mid-article ad. |

The two in-article units are rendered by `layouts/partials/ad-inarticle.html`
(called with the slot ID as its context) and placed by `single.html`.

The placement is the only subtle part. Nearly every entry writes its lede,
hatnote and infobox *inline in the markdown body*, so there is no template seam
between "description" and "first section". `single.html` manufactures one by
splitting the **rendered** `.Content` on `<h2` — chunk 0 is the entire opening
block, each later chunk is one `##` section — then re-emits the chunks with the
top unit after the *first section* (not after chunk 0: the float-right infobox
is still in play there, and the ad's `clear: both` would open a tall empty
gutter between the lede and the first heading) and the mid unit before the
midpoint section, only when at least one full section separates the two units.
Two consequences:

- **Ads land on every entry automatically**, including new ones. Do not paste
  `<ins class="adsbygoogle">` into markdown files; you'd end up with duplicates.
- Entries with fewer than four `##` sections get the top unit only.

Ads are gated on `.Section` being non-empty, so root-level pages
(`content/about.md`) stay ad-free. The partial deliberately does *not* re-emit
the `adsbygoogle.js` tag — it is already loaded once in `<head>`, and Google
expects exactly one loader per page.

`.wiki-ad` in `assets/css/wiki.css` carries `clear: both`. That rule is
load-bearing: without it a unit that meets the `float: right` infobox renders
as a sliver in the leftover gutter. The CSS also collapses slots Google
reports as unfilled (`data-ad-status="unfilled"`) and, once a creative fills
(`data-ad-status="filled"`), frames the unit as a card with a visible
"Advertisement" kicker — gated on fill so blocked slots never show an empty
labelled box.

AdSense also expects an `ads.txt` at the **domain** root (`pomegra.io/ads.txt`).
That file belongs to the parent site, not this repo, since the wiki is mounted
at `/wiki/`.

## How the home page works

`layouts/index.html` reads:
- A "Featured entry" card pinned to the article with title `"Stock market"` (`where .Site.RegularPages "Title" "Stock market"`).
- A "Did you know?" panel with hand-curated facts (currently hardcoded in the template — move to `data/` if it grows).
- A theme grid driven by `data/themes.toml`. Add a new theme → edit that file, no template changes.

The home page does **not** auto-list all articles. The wiki has too many entries for that to be useful; readers find articles via search, the [A–Z index](./content/index-a-z.md), or by following cross-links.

## How styling is organised

A single hand-written stylesheet lives at `assets/css/wiki.css`. Hugo Pipes minifies + fingerprints it on each build.

The Pomegra editorial design tokens are all CSS custom properties at `:root`. Dark mode swaps them under `[data-theme='dark']`. The theme toggle is the only JavaScript on the site — see the inline script at the bottom of `layouts/_default/baseof.html`.

There is **no Tailwind, no CSS-in-JS, no PostCSS pipeline.** If you're tempted to add one, talk to a human first.

## Wiki-specific UI elements

Articles use four custom DOM patterns. Their HTML is written inline in markdown (Goldmark renders raw HTML because `markup.goldmark.renderer.unsafe = true` in `hugo.toml`):

| Pattern | Wrapper | Purpose |
|---|---|---|
| Hatnote | `<div class="wiki-hatnote">…</div>` | Italic disambiguation line under the title (e.g. "For X, see /x/"). |
| Infobox | `<aside class="wiki-infobox">…</aside>` | Floating-right key-facts card with image + caption + key-facts table. |
| See also | `<div class="wiki-seealso">…</div>` | Closing two-column list of related entries. |
| Lede | (No wrapper.) | The first body paragraph wrapped in `*…*` markdown italics. CSS auto-styles it via `:has(> em:only-child)`. |

All four are styled by `assets/css/wiki.css`. The single-page Hugo layout (`layouts/_default/single.html`) also supports the same elements via front matter (`hatnote:`, `infobox:`, `see_also:`, `wider_context:`), but most existing entries use the inline-HTML form. Either is supported.

## Migration scripts (`scripts/`)

These scripts are utilities, run on demand. They are idempotent.

- `migrate.py` — used once to strip Docusaurus-specific front matter (`sidebar_label`, `slug`, `hide_table_of_contents`, etc.) and the in-body `# Title` line after we moved from Docusaurus to Hugo.
- `extract_hero_image.py` — lifts the first `<img src="…">` URL in each article body up to `image:` in the front matter. Re-run this whenever you add new entries; it skips any article that already has `image:` set.

## What is *not* in this repo

- **No Dockerfile / CI yet.** The pomegra-infra wiring (image build, nginx
  routing for `pomegra.io/wiki/`, GitOps bump) is the next step. Until that
  lands, the production output is whatever `hugo --gc` produces in `public/`.
- **No tests.** "Tests" effectively mean: `hugo --gc --minify` exits 0 and the
  rendered site looks right when you open `hugo server`.

## A note on cross-links and 10k-scale future

The wiki is intended to grow to 10,000+ entries. Two things keep that survivable:

1. **Hugo is fast.** Even at 10k pages, builds will be in single-digit seconds.
2. **Cross-links use absolute root paths** (`[Stock](/stock/)`), so adding/renaming/moving articles never breaks an existing one as long as the filename slug is stable.

When you write or commission a new entry, the single most-important hygiene rule is: **never link to a slug that does not exist on disk.** Run `grep -r 'href="/[a-z-]*/"' content/ | awk -F'"' '{print $2}' | sort -u` against `ls content/` and reconcile before opening a PR.
