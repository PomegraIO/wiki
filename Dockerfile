# syntax=docker/dockerfile:1
#
# Pomegra Wiki — Hugo static site → nginx
# Mirrors the deploy shape of PomegraIO/learn (multi-stage: builder → nginx)
# so that GitOps and image layout stay consistent across sibling sites.

# ── Stage 1: Build the Hugo site ────────────────────────────────────────
# Pull Hugo extended directly from the GitHub release tarball. This keeps
# us off the hugomods/hugo Docker Hub registry (which has unstable tags and
# rate limits) and pins to an exact version reproducibly.
FROM alpine:3.20 AS builder
ARG HUGO_VERSION=0.161.1
# python3 is only for scripts/check_links.py (stdlib only, no pip) - the
# pre-build link gate below.
RUN apk add --no-cache wget tar libstdc++ libc6-compat git python3 \
 && wget -q "https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/hugo_extended_${HUGO_VERSION}_linux-amd64.tar.gz" -O /tmp/hugo.tgz \
 && tar -xzf /tmp/hugo.tgz -C /usr/local/bin/ hugo \
 && rm /tmp/hugo.tgz \
 && hugo version

WORKDIR /src

# Hugo benefits very little from layered caching (it's a single binary
# and one full read of content/). Copy the whole tree and let `hugo --gc`
# decide what to do.
COPY . .

# Link gate: every cross-link must be a root-absolute `/<slug>/` that exists
# on disk. Relative, category-path, `/link/` and `.md` targets all became
# crawlable 404s in Search Console (thousands of them), so a build with a
# single malformed or dangling link fails here instead of shipping.
RUN python3 scripts/check_links.py --strict

# Build for /wiki/ on pomegra.io. Override the dev-friendly defaults so
# absolute URLs are correct and minification is on. canonifyURLs (set in
# hugo.toml) takes care of rewriting markdown body links like /stock/
# into /wiki/stock/.
RUN hugo --gc --minify --baseURL "https://pomegra.io/wiki/"

# ── Stage 2: Serve with Nginx ───────────────────────────────────────────
FROM nginx:alpine

# OCI source label so GHCR auto-links this package to the wiki repo —
# without it, pushes from PomegraIO/wiki's GITHUB_TOKEN are rejected
# because the package was originally seeded out-of-band.
LABEL org.opencontainers.image.source="https://github.com/PomegraIO/wiki"
LABEL org.opencontainers.image.description="Pomegra Wiki — Hugo static site"
LABEL org.opencontainers.image.licenses="MIT"

ARG APP_ENV=production

COPY nginx/*.conf /etc/nginx/conf.d/
RUN ln -sf /etc/nginx/conf.d/${APP_ENV}.conf /etc/nginx/conf.d/env.conf

# Static landing-page assets (mirrors the /learn/ shape — a tiny root
# placeholder so requests that miss /wiki/ don't fall through to 404).
COPY nginx/www /usr/share/nginx/html

# Copy the built site under /wiki/ — that's the path APISIX routes traffic
# to, matching the baseURL the build used.
COPY --from=builder /src/public /usr/share/nginx/html/wiki

EXPOSE 8888
CMD ["nginx", "-g", "daemon off;"]
