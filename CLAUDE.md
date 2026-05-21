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
# Dev (with live reload). Use port 1314 to avoid clashing with `learn`'s 3000s.
hugo server --port 1314 --bind 127.0.0.1 --baseURL "http://localhost:1314/" --appendPort=false --disableFastRender

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

- One Markdown file per entry, at `content/<slug>.md`. The slug is the URL — `content/yield-curve.md` becomes `/yield-curve/`.
- Front matter is minimal: `title`, `description`, `keywords`, and `image` (lifted from the body's first `<img>` by `scripts/extract_hero_image.py`).
- Each entry opens with an italic lede paragraph (markdown `*…*` on a single paragraph), optionally a hatnote, then an `<aside class="wiki-infobox">`, then 4–6 `##` sections, then a closing `<div class="wiki-seealso">` block.
- Cross-link **generously**. The "Cross-link allowlist" rule in the authoring guide must hold: only link to slugs that actually exist in `content/`. A wiki where 1% of links are broken feels broken everywhere.

## How permalinks work

`hugo.toml` sets:

```toml
[permalinks]
  page = '/:contentbasename/'
```

This pins the URL to the filename, *not* the title. `etf.md` is always `/etf/`, never `/etf-exchange-traded-fund/`. This is what makes the cross-link allowlist trustworthy — slugs in markdown match filenames on disk one-to-one.

Do not change this rule lightly. If you do, every existing cross-link in every article breaks at once.

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

- **No deployment / CI yet.** The user explicitly deferred Pomegra-infra wiring; do not assume a `Dockerfile`, `.github/workflows/`, or `helm/` exists.
- **No analytics include yet.** When wired, mirror `learn/books/_shared/umami-events.js` (load via `<script src="…" defer>` in `layouts/_default/baseof.html`, not via NPM).
- **No tests.** "Tests" effectively mean: `hugo --gc --minify` exits 0 and the rendered site looks right when you open `hugo server`.

## A note on cross-links and 10k-scale future

The wiki is intended to grow to 10,000+ entries. Two things keep that survivable:

1. **Hugo is fast.** Even at 10k pages, builds will be in single-digit seconds.
2. **Cross-links use absolute root paths** (`[Stock](/stock/)`), so adding/renaming/moving articles never breaks an existing one as long as the filename slug is stable.

When you write or commission a new entry, the single most-important hygiene rule is: **never link to a slug that does not exist on disk.** Run `grep -r 'href="/[a-z-]*/"' content/ | awk -F'"' '{print $2}' | sort -u` against `ls content/` and reconcile before opening a PR.
