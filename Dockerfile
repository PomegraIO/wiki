# syntax=docker/dockerfile:1
#
# Pomegra Wiki — Hugo static site → nginx
# Mirrors the deploy shape of PomegraIO/learn (multi-stage: builder → nginx)
# so that GitOps and image layout stay consistent across sibling sites.

# ── Stage 1: Build the Hugo site ────────────────────────────────────────
FROM hugomods/hugo:exts-0.161.1 AS builder

WORKDIR /src

# Hugo benefits very little from layered caching (it's a single binary
# and one full read of content/). Copy the whole tree and let `hugo --gc`
# decide what to do.
COPY . .

# Build for /wiki/ on pomegra.io. Override the dev-friendly defaults so
# absolute URLs are correct and minification is on. canonifyURLs (set in
# hugo.toml) takes care of rewriting markdown body links like /stock/
# into /wiki/stock/.
RUN hugo --gc --minify --baseURL "https://pomegra.io/wiki/"

# ── Stage 2: Serve with Nginx ───────────────────────────────────────────
FROM nginx:alpine

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
