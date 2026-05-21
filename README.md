# Pomegra Wiki

> A reader-friendly encyclopedia of the financial world. Plain-language entries on markets, instruments, institutions, and ideas, densely cross-linked.

Pomegra Wiki is a static Hugo site. Each `content/*.md` file is one wiki entry. The site shares its editorial design language with [PomegraIO/learn](https://github.com/PomegraIO/learn) — cream paper, Fraunces display serif, accent red — but the content shape is wiki-style: every entry stands on its own and links generously to every neighbour.

## Quickstart

Hugo Extended ≥0.144 is the only requirement.

```bash
# Dev server with live reload at http://localhost:1314
hugo server --port 1314 --bind 127.0.0.1 --baseURL "http://localhost:1314/" --appendPort=false --disableFastRender

# Production build → public/
hugo --gc --minify
```

If you don't have Hugo, grab the Extended binary from <https://github.com/gohugoio/hugo/releases>.

## Repo layout

```
content/         one Markdown file per wiki entry
layouts/         Hugo templates (baseof, single, list, index, partials)
assets/css/      single hand-written stylesheet (Hugo Pipes minifies it)
data/themes.toml home-page theme grid (data-driven)
static/img/      favicon, logo, robots.txt
scripts/         one-shot migration helpers (Python)
hugo.toml        site config
```

## Adding an entry

Read [`WIKI_AUTHORING_GUIDE.md`](./WIKI_AUTHORING_GUIDE.md) before writing. The very short version:

1. Create `content/<slug>.md`. The filename **is** the URL — `content/yield-curve.md` serves at `/yield-curve/`.
2. Use [`content/stock.md`](./content/stock.md) as the structural exemplar (front matter, lede, hatnote, infobox, sections, see-also).
3. Cross-link **only** to slugs that exist in `content/`. Broken links visibly degrade the wiki.
4. Run `hugo` and open the new page in dev before opening a PR.

## Working with agents

[`CLAUDE.md`](./CLAUDE.md) is the orientation for Claude Code (and Claude Agent SDK) sessions. The authoring guide is the editorial contract. Together they should bring a new agent up to speed in one read.

## Why Hugo

The wiki is designed to grow to 10,000+ entries. Hugo was chosen because it stays fast at that scale — current builds (~40 pages) finish in ~40 ms; expected 10k-page builds are still single-digit seconds. The previous Docusaurus prototype was rejected for this reason; do not migrate to a Node-based SSG without a deliberate conversation.

## Licence

Text © Pomegra. Photographs are credited inline and used under their source licence (typically [Unsplash](https://unsplash.com/license)).
